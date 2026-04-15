# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.25.0",
# ]
# ///
"""
Clean a raw extracted markdown file (as produced by extract.py / Jina AI)
down to "just the meat" — the article body plus a small YAML frontmatter
with title, url, author, published, source_type.

Diffability guarantee
---------------------
Cleaning is *subtractive only*: we never let the LLM rewrite the body.
Both the LLM and the heuristic strategies produce a list of line ranges
to drop from the raw body; the cleaned body is assembled by deleting
those ranges. We then verify that every non-blank line in the cleaned
body appears verbatim as a line in the raw body. If verification fails
we fall back to the heuristic (or, finally, to the raw body unchanged).

Strategies, in order:
1. Claude LLM — one call returning strict JSON with title/author/published
   metadata plus `drop_ranges` (inclusive 1-indexed line ranges of the
   numbered raw body). Handles arbitrary site layouts.
2. Heuristic fallback — compute drop_ranges from regex boilerplate
   detection (cookie banners before the article H1, "Related posts" /
   newsletter / share widgets after).

CLI:
    python scripts/clean.py <file.md> [--url URL] [--source-type TYPE]
        [--no-llm] [-o OUTPUT]
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

log = logging.getLogger(__name__)


# Largest input we'll send to Claude in one shot. Above this we fall back
# to the heuristic cleaner (a handful of huge PDFs hit this).
_MAX_LLM_INPUT_CHARS = 180_000

# Heuristic: sections whose heading marks the start of "related/trailer" junk
# — we drop everything from that heading onward.
_TRAILING_JUNK_HEADING_RE = re.compile(
    r"^\s{0,3}#{1,6}\s*("
    r"related\s+(articles|posts|reading|stories)"
    r"|more\s+from"
    r"|you\s+may\s+also\s+like"
    r"|recent\s+posts"
    r"|subscribe"
    r"|newsletter"
    r"|sign\s+up"
    r"|share\s+this"
    r"|comments?\b"
    r"|about\s+the\s+author"
    r")\b",
    re.IGNORECASE | re.MULTILINE,
)


DropRange = tuple[int, int]  # inclusive, 1-indexed


@dataclass
class Cleaned:
    title: str = ""
    url: str = ""
    author: str = ""
    published: str = ""
    source_type: str = ""
    source_domain: str = ""
    body_md: str = ""
    # Line ranges (1-indexed, inclusive) dropped from the post-Jina-header
    # body when producing body_md. Recorded for debugging/auditing.
    drop_ranges: list[DropRange] = field(default_factory=list)
    cleanup_method: str = ""  # "llm", "fallback_heuristic", "already_clean", "raw"

    def to_markdown(self) -> str:
        """Render as a markdown file with YAML-ish frontmatter."""
        if self.cleanup_method == "already_clean":
            # Input already had frontmatter; body_md holds the full original
            # file verbatim. Return it unchanged so re-running clean.py on a
            # .clean.md file is an idempotent no-op (no nested frontmatter).
            out = self.body_md
            return out if out.endswith("\n") else out + "\n"
        fm_fields = [
            ("title", self.title),
            ("url", self.url),
            ("author", self.author),
            ("published", self.published),
            ("source_type", self.source_type),
            ("source_domain", self.source_domain),
            ("cleanup_method", self.cleanup_method),
        ]
        lines = ["---"]
        for k, v in fm_fields:
            if v:
                s = str(v).replace("\\", "\\\\").replace('"', '\\"')
                needs_quote = any(c in s for c in ':#"\n') or s.strip() != s
                lines.append(f'{k}: "{s}"' if needs_quote else f"{k}: {s}")
        lines.append("---")
        lines.append("")
        lines.append(self.body_md.strip())
        lines.append("")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Core primitives: line-range drops and subset verification
# ---------------------------------------------------------------------------

def apply_drops(body: str, drops: list[DropRange]) -> str:
    """
    Delete the given 1-indexed inclusive line ranges from `body`. Ranges
    may overlap and may be out of order; we normalize them. Preserves
    trailing-newline shape of the remaining lines.
    """
    if not drops:
        return body
    lines = body.split("\n")
    n = len(lines)
    kill = [False] * (n + 1)  # 1-indexed
    for start, end in drops:
        s = max(1, start)
        e = min(n, end)
        for i in range(s, e + 1):
            kill[i] = True
    kept = [lines[i - 1] for i in range(1, n + 1) if not kill[i]]
    return "\n".join(kept)


def verify_body_is_subset(clean_body: str, raw_body: str) -> bool:
    """
    True iff every non-blank line in `clean_body` appears as a full line
    in `raw_body`. This is the diffability invariant: cleaning deletes
    lines but never rewrites them.
    """
    raw_lines = set(raw_body.split("\n"))
    for line in clean_body.split("\n"):
        if not line.strip():
            continue
        if line not in raw_lines:
            return False
    return True


# ---------------------------------------------------------------------------
# Frontmatter parsing (for Jina-style header + pre-cleaned files)
# ---------------------------------------------------------------------------

_JINA_TITLE_RE = re.compile(r"^Title:\s*(.+?)\s*$", re.MULTILINE)
_JINA_URL_RE = re.compile(r"^URL Source:\s*(.+?)\s*$", re.MULTILINE)
_JINA_PUBLISHED_RE = re.compile(r"^Published Time:\s*(.+?)\s*$", re.MULTILINE)
_JINA_MARKDOWN_START_RE = re.compile(r"^Markdown Content:\s*$", re.MULTILINE)


def parse_jina_header(raw: str) -> dict:
    """Pull Title / URL / Published from a Jina-produced markdown file."""
    out = {"title": "", "url": "", "published": "", "body": raw}
    m = _JINA_TITLE_RE.search(raw[:2000])
    if m:
        out["title"] = m.group(1).strip()
    m = _JINA_URL_RE.search(raw[:2000])
    if m:
        out["url"] = m.group(1).strip()
    m = _JINA_PUBLISHED_RE.search(raw[:2000])
    if m:
        out["published"] = m.group(1).strip()
    m = _JINA_MARKDOWN_START_RE.search(raw[:4000])
    if m:
        out["body"] = raw[m.end():].lstrip("\n")
    return out


def has_frontmatter(text: str) -> bool:
    """True if the file already starts with a --- YAML frontmatter block."""
    return text.lstrip().startswith("---\n") or text.lstrip().startswith("---\r\n")


# ---------------------------------------------------------------------------
# Heuristic fallback cleaner
# ---------------------------------------------------------------------------

def _heuristic_drop_ranges(body: str, title: str = "") -> list[DropRange]:
    """
    Compute 1-indexed inclusive line ranges of boilerplate to drop.
    Drops a prefix range (everything before the real article heading)
    and a suffix range (from the first trailing-junk heading onward).
    """
    if not body:
        return []

    lines = body.splitlines()

    title_needle = re.sub(r"\W+", "", title).lower() if title else ""
    title_matches: list[int] = []
    first_substantive: Optional[int] = None
    for i, line in enumerate(lines):
        m = re.match(r"^\s{0,3}#{1,3}\s+(.+?)\s*$", line)
        if not m:
            continue
        heading = m.group(1).strip()
        # Jina commonly emits headings as markdown links, e.g.
        # `## [Section Name](https://site.tld/article-slug#anchor)`. The
        # raw heading string therefore contains the URL (and often the
        # article slug, which is a close cousin of the page title). If we
        # normalized that verbatim every section heading would appear to
        # contain title_needle and `title_matches[-1]` would land on a
        # late section — truncating the body to its tail. Strip the URL
        # portion of markdown links and any autolinks before normalizing.
        heading_text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        heading_text = re.sub(r"<[^>]+>", "", heading_text)
        norm = re.sub(r"\W+", "", heading_text).lower()
        if any(skip in heading_text.lower() for skip in (
            "cookie", "privacy", "consent", "menu", "navigation",
            "customize", "preferences", "skip to", "select your",
        )):
            continue
        if first_substantive is None:
            first_substantive = i
        if title_needle and title_needle[:40] in norm:
            title_matches.append(i)

    if title_matches:
        start_idx = title_matches[-1]
    elif first_substantive is not None:
        start_idx = first_substantive
    else:
        start_idx = 0

    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if _TRAILING_JUNK_HEADING_RE.match(lines[i] or ""):
            end_idx = i
            break

    ranges: list[DropRange] = []
    if start_idx > 0:
        ranges.append((1, start_idx))  # drop lines 1..start_idx (before article)
    if end_idx < len(lines):
        ranges.append((end_idx + 1, len(lines)))  # drop from junk heading on
    return ranges


def heuristic_clean(body: str, title: str = "") -> str:
    """Public heuristic cleaner — computes drops and applies them."""
    drops = _heuristic_drop_ranges(body, title=title)
    return apply_drops(body, drops).strip()


# ---------------------------------------------------------------------------
# Claude LLM cleaner — returns drop_ranges, not a rewritten body
# ---------------------------------------------------------------------------

_LLM_SYSTEM = (
    "You clean scraped web articles and PDFs into usable markdown for a "
    "security-incident research dataset. You return STRICT JSON only — no "
    "prose, no code fences. You NEVER rewrite or paraphrase content; you "
    "only identify line ranges of boilerplate to delete."
)

_LLM_USER_TEMPLATE = """\
Below is a raw scrape of a web page, PDF, or video transcript with each
line prefixed by its 1-indexed line number (format: "NNNN: <line>").
It may contain cookie banners, nav menus, social share widgets, newsletter
prompts, 'related articles' footers, repeated page headers/footers (from
PDFs), and other boilerplate surrounding the real article body.

Return a single JSON object with EXACTLY these keys:
  "title":       string — article / document title (no site-name suffix
                 like " | AWS Security Blog"). Empty if unknown.
  "author":      string — author name(s), comma-separated if multiple.
                 Empty if none stated.
  "published":   string — publication date in ISO 8601 (YYYY-MM-DD) if
                 derivable, else the original string, else empty.
  "drop_ranges": array of [start, end] pairs — inclusive 1-indexed line
                 ranges to DELETE. Ranges should cover: cookie/consent
                 banners, nav menus, breadcrumbs, social share buttons,
                 'filed under' / tag widgets, 'related posts' / 'more
                 from' / newsletter / comments sections, site footers,
                 repeated PDF page headers and bare page numbers.
                 DO NOT list ranges covering substantive article content.
                 You MUST NOT rewrite any line — you can only drop lines.

Context (use but do not echo):
  URL:          {url}
  Source type:  {source_type}
  Known title:  {hint_title}

Numbered raw input:
<<<
{numbered}
>>>

Return JSON only."""


def _strip_code_fences(s: str) -> str:
    s = s.strip()
    if s.startswith("```"):
        s = re.sub(r"^```(?:json)?\s*", "", s)
        s = re.sub(r"\s*```\s*$", "", s)
    return s.strip()


def _number_lines(body: str) -> str:
    lines = body.split("\n")
    width = max(4, len(str(len(lines))))
    return "\n".join(f"{i+1:0{width}d}: {line}" for i, line in enumerate(lines))


def llm_clean(
    raw_body: str,
    url: str = "",
    source_type: str = "",
    hint_title: str = "",
    model: str = "claude-opus-4-6",
) -> Optional[dict]:
    """
    Ask Claude for {title, author, published, drop_ranges}. Returns None
    if the API is unavailable or the response can't be parsed.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        log.warning("ANTHROPIC_API_KEY not set – skipping LLM cleanup")
        return None

    if len(raw_body) > _MAX_LLM_INPUT_CHARS:
        log.info("Input %d chars exceeds LLM budget %d; using heuristic",
                 len(raw_body), _MAX_LLM_INPUT_CHARS)
        return None

    try:
        import anthropic
    except ImportError:
        log.warning("anthropic package not installed")
        return None

    client = anthropic.Anthropic(api_key=api_key)
    prompt = _LLM_USER_TEMPLATE.format(
        url=url or "(unknown)",
        source_type=source_type or "(unknown)",
        hint_title=hint_title or "(unknown)",
        numbered=_number_lines(raw_body),
    )

    try:
        resp = client.messages.create(
            model=model,
            max_tokens=8000,
            temperature=0,
            system=_LLM_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
        )
    except Exception as e:
        log.warning("Claude cleanup API call failed: %s", e)
        return None

    try:
        text = resp.content[0].text
    except (AttributeError, IndexError):
        log.warning("Unexpected Claude response shape")
        return None

    try:
        data = json.loads(_strip_code_fences(text))
    except json.JSONDecodeError as e:
        log.warning("Claude returned non-JSON: %s (first 200 chars: %r)",
                    e, text[:200])
        return None

    if not isinstance(data, dict) or "drop_ranges" not in data:
        log.warning("Claude JSON missing drop_ranges")
        return None

    raw_ranges = data.get("drop_ranges") or []
    drops: list[DropRange] = []
    for r in raw_ranges:
        try:
            s, e = int(r[0]), int(r[1])
            if s <= e:
                drops.append((s, e))
        except (ValueError, TypeError, IndexError):
            continue

    return {
        "title": str(data.get("title") or "").strip(),
        "author": str(data.get("author") or "").strip(),
        "published": str(data.get("published") or "").strip(),
        "drop_ranges": drops,
    }


# ---------------------------------------------------------------------------
# Top-level entry point
# ---------------------------------------------------------------------------

def clean_markdown(
    raw: str,
    url: str = "",
    source_type: str = "",
    use_llm: bool = True,
) -> Cleaned:
    """
    Clean a raw extracted markdown string. Returns a Cleaned dataclass;
    call .to_markdown() to render the final file.
    """
    if has_frontmatter(raw):
        return Cleaned(cleanup_method="already_clean", body_md=raw.strip())

    jina = parse_jina_header(raw)
    url = url or jina["url"]
    parsed_host = urlparse(url).hostname or "" if url else ""

    cleaned = Cleaned(
        url=url,
        source_type=source_type,
        source_domain=parsed_host,
        title=jina["title"],
        published=jina["published"],
    )

    body_for_cleaning = jina["body"]

    llm_result = None
    if use_llm:
        llm_result = llm_clean(
            body_for_cleaning,
            url=url,
            source_type=source_type,
            hint_title=jina["title"],
        )

    applied_llm = False
    if llm_result is not None:
        candidate = apply_drops(body_for_cleaning, llm_result["drop_ranges"]).strip()
        # Safety: subset check should be trivially true (we only deleted
        # lines) but verify — and bail out if drops collapsed the article.
        if (
            verify_body_is_subset(candidate, body_for_cleaning)
            and len(candidate) >= max(200, len(body_for_cleaning) // 50)
        ):
            if llm_result["title"]:
                cleaned.title = llm_result["title"]
            cleaned.author = llm_result["author"]
            if llm_result["published"]:
                cleaned.published = llm_result["published"]
            cleaned.body_md = candidate
            cleaned.drop_ranges = llm_result["drop_ranges"]
            cleaned.cleanup_method = "llm"
            applied_llm = True
        else:
            log.warning("LLM drop_ranges failed verification — falling back")

    if not applied_llm:
        drops = _heuristic_drop_ranges(body_for_cleaning, title=cleaned.title)
        body = apply_drops(body_for_cleaning, drops).strip()
        if not verify_body_is_subset(body, body_for_cleaning):
            # Should never happen — heuristic only deletes lines.
            body = body_for_cleaning.strip()
            drops = []
            cleaned.cleanup_method = "raw"
        else:
            cleaned.cleanup_method = "fallback_heuristic"
        cleaned.body_md = body
        cleaned.drop_ranges = drops

    return cleaned


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(message)s",
        stream=sys.stderr,
    )
    p = argparse.ArgumentParser(description="Clean a scraped markdown file.")
    p.add_argument("input", help="Path to raw markdown file")
    p.add_argument("--url", default="", help="Source URL (overrides header)")
    p.add_argument("--source-type", default="", help="article|pdf|youtube|archive|other")
    p.add_argument("--no-llm", action="store_true",
                   help="Skip Claude cleanup; use heuristic only")
    p.add_argument("-o", "--output", default="-",
                   help="Output path ('-' for stdout, default)")
    args = p.parse_args(argv)

    raw = Path(args.input).read_text(encoding="utf-8")
    cleaned = clean_markdown(
        raw,
        url=args.url,
        source_type=args.source_type,
        use_llm=not args.no_llm,
    )
    out = cleaned.to_markdown()
    if args.output == "-":
        sys.stdout.write(out)
    else:
        Path(args.output).write_text(out, encoding="utf-8")
    log.info("Cleaned via %s (%d chars body, dropped %d range(s))",
             cleaned.cleanup_method, len(cleaned.body_md),
             len(cleaned.drop_ranges))
    return 0


if __name__ == "__main__":
    sys.exit(main())
