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

Two strategies, in order:
1. Claude LLM cleanup – one call to claude-opus-4-6 returning strict JSON
   (title, author, published, body_md). Handles arbitrary site layouts.
2. Heuristic fallback – if Claude is unavailable or returns junk, strip
   obvious boilerplate with regex: leading cookie / nav blocks before the
   article H1, trailing "Related posts" / "Newsletter" / share widgets.

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
from dataclasses import dataclass, asdict
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


@dataclass
class Cleaned:
    title: str = ""
    url: str = ""
    author: str = ""
    published: str = ""
    source_type: str = ""
    source_domain: str = ""
    body_md: str = ""
    cleanup_method: str = ""  # "llm", "fallback_heuristic", or "raw"

    def to_markdown(self) -> str:
        """Render as a markdown file with YAML-ish frontmatter."""
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
                # Basic YAML escaping: quote anything containing ':' or starting
                # with reserved chars; escape embedded double quotes.
                s = str(v).replace("\\", "\\\\").replace('"', '\\"')
                needs_quote = any(c in s for c in ':#"\n') or s.strip() != s
                lines.append(f'{k}: "{s}"' if needs_quote else f"{k}: {s}")
        lines.append("---")
        lines.append("")
        lines.append(self.body_md.strip())
        lines.append("")
        return "\n".join(lines)


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

def heuristic_clean(body: str, title: str = "") -> str:
    """
    Best-effort boilerplate stripper. Runs only when the LLM pass is
    unavailable or failed. Drops:
      - everything before the first H1 whose text contains the article
        title (or, lacking that, the first H1/H2 that isn't just "menu"
        / "cookie" / "navigation").
      - everything from the first trailing-junk heading onward.
    """
    if not body:
        return body

    lines = body.splitlines()

    # Find the best substantive heading to start from. If the article title
    # appears as an H1 more than once (common: site nav crumb + real
    # article heading), prefer the LAST occurrence — everything before it
    # is very likely boilerplate.
    title_needle = re.sub(r"\W+", "", title).lower() if title else ""
    title_matches: list[int] = []
    first_substantive: Optional[int] = None
    for i, line in enumerate(lines):
        m = re.match(r"^\s{0,3}#{1,3}\s+(.+?)\s*$", line)
        if not m:
            continue
        heading = m.group(1).strip()
        norm = re.sub(r"\W+", "", heading).lower()
        if any(skip in heading.lower() for skip in (
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

    # Find first trailing-junk heading
    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if _TRAILING_JUNK_HEADING_RE.match(lines[i] or ""):
            end_idx = i
            break

    return "\n".join(lines[start_idx:end_idx]).strip()


# ---------------------------------------------------------------------------
# Claude LLM cleaner
# ---------------------------------------------------------------------------

_LLM_SYSTEM = (
    "You clean scraped web articles and PDFs into usable markdown for a "
    "security-incident research dataset. You return STRICT JSON only — no "
    "prose, no code fences."
)

_LLM_USER_TEMPLATE = """\
Below is a raw scrape of a web page, PDF, or video transcript. It may
contain cookie banners, nav menus, social share widgets, newsletter
prompts, 'related articles' footers, repeated page headers/footers (from
PDFs), and other boilerplate.

Return a single JSON object with EXACTLY these keys:
  "title":     string — the article / document title (no site name suffix
               like " | AWS Security Blog"). Empty string if unknown.
  "author":    string — author name(s), comma-separated if multiple. Empty
               string if none stated.
  "published": string — publication date in ISO 8601 (YYYY-MM-DD) if
               derivable, else the original string, else empty.
  "body_md":   string — ONLY the article / document body as markdown.
               Preserve headings, lists, code blocks, tables, blockquotes.
               Remove: cookie/consent banners, nav menus, breadcrumbs,
               social share buttons, 'filed under' / tag widgets,
               'related posts' / 'more from' / newsletter / comments
               sections, site footers, repeated PDF page headers and page
               numbers. Keep the substantive content intact — do not
               summarize, paraphrase, or truncate.

Context (use but do not echo into body_md):
  URL:          {url}
  Source type:  {source_type}
  Known title:  {hint_title}

Raw input:
<<<
{raw}
>>>

Return JSON only."""


def _strip_code_fences(s: str) -> str:
    s = s.strip()
    if s.startswith("```"):
        s = re.sub(r"^```(?:json)?\s*", "", s)
        s = re.sub(r"\s*```\s*$", "", s)
    return s.strip()


def llm_clean(
    raw: str,
    url: str = "",
    source_type: str = "",
    hint_title: str = "",
    model: str = "claude-opus-4-6",
) -> Optional[dict]:
    """
    Ask Claude to return {title, author, published, body_md}. Returns None
    if the API is unavailable or the response can't be parsed.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        log.warning("ANTHROPIC_API_KEY not set – skipping LLM cleanup")
        return None

    if len(raw) > _MAX_LLM_INPUT_CHARS:
        log.info("Input %d chars exceeds LLM budget %d; using heuristic",
                 len(raw), _MAX_LLM_INPUT_CHARS)
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
        raw=raw,
    )

    try:
        resp = client.messages.create(
            model=model,
            max_tokens=16000,
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

    if not isinstance(data, dict) or "body_md" not in data:
        log.warning("Claude JSON missing body_md")
        return None

    # Guard against the LLM silently collapsing the article.
    if len(data.get("body_md", "")) < max(200, len(raw) // 50):
        log.warning("Claude body_md suspiciously short (%d chars for %d raw); "
                    "falling back to heuristic",
                    len(data.get("body_md", "")), len(raw))
        return None

    return {
        "title": str(data.get("title") or "").strip(),
        "author": str(data.get("author") or "").strip(),
        "published": str(data.get("published") or "").strip(),
        "body_md": str(data.get("body_md") or "").strip(),
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
        # Already cleaned — don't re-run.
        out = Cleaned(cleanup_method="already_clean", body_md=raw.strip())
        return out

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

    if llm_result is not None:
        if llm_result["title"]:
            cleaned.title = llm_result["title"]
        cleaned.author = llm_result["author"]
        if llm_result["published"]:
            cleaned.published = llm_result["published"]
        cleaned.body_md = llm_result["body_md"]
        cleaned.cleanup_method = "llm"
    else:
        cleaned.body_md = heuristic_clean(body_for_cleaning, title=cleaned.title)
        cleaned.cleanup_method = "fallback_heuristic"

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
    log.info("Cleaned via %s (%d chars body)",
             cleaned.cleanup_method, len(cleaned.body_md))
    return 0


if __name__ == "__main__":
    sys.exit(main())
