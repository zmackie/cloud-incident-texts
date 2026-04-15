# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.25.0",
# ]
# ///
"""
Retroactively produce link_NN.clean.md for every crawled article.

File scheme (new):
  link_NN.md         — raw Jina / extractor output (unchanged, diffable)
  link_NN.clean.md   — cleaned article with YAML frontmatter

Legacy migration: an earlier version of this script wrote the cleaned
output back into link_NN.md and preserved the raw as link_NN.raw.md.
We detect that shape and swap it back to the new scheme before re-running.

For each incident directory:
  1. Migrate legacy files if present (raw↔clean rename).
  2. For each link_NN.md that has no link_NN.clean.md sibling, run
     clean_markdown and write link_NN.clean.md.
  3. Update metadata.json crawl_status entries with `file`, `clean_file`,
     title / author / published / cleanup_method.

Idempotent: safe to re-run. Parallel at the incident level.

Usage:
    python scripts/backfill_clean.py [--workers N] [--no-llm] [--dry-run]
        [--only SLUG]
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

from clean import clean_markdown, has_frontmatter
# Import from the lightweight `sources` module — NOT from `extract` —
# so this CLI does not transitively require requests/trafilatura/bs4,
# which aren't listed in this script's inline dependency header.
from sources import classify_source

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent / "data"
ARTICLES_DIR = DATA_DIR / "articles"

_RAW_FILE_RE = re.compile(r"^link_(\d+)\.md$")
_CLEANUP_METHOD_RE = re.compile(r"^cleanup_method:\s*\"?([A-Za-z_]+)\"?\s*$", re.MULTILINE)


def _existing_cleanup_method(clean_path: Path) -> Optional[str]:
    """Read the cleanup_method field from a clean file's frontmatter."""
    try:
        head = clean_path.read_text(encoding="utf-8", errors="replace")[:2000]
    except Exception:
        return None
    m = _CLEANUP_METHOD_RE.search(head)
    return m.group(1) if m else None

# Simple YAML-ish frontmatter reader that matches what Cleaned.to_markdown
# emits: `key: value` or `key: "quoted value"`, one per line, terminated
# by a `---` line. Good enough for the small, known schema we produce;
# deliberately doesn't pull in PyYAML.
_FRONTMATTER_LINE_RE = re.compile(
    r'^([A-Za-z_][A-Za-z0-9_]*):\s*(?:"((?:[^"\\]|\\.)*)"|(.*?))\s*$'
)


def _read_clean_frontmatter(path: Path) -> dict:
    """Parse title/author/published/etc. out of a .clean.md file's frontmatter.

    Returns an empty dict if the file is missing or lacks frontmatter.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = _FRONTMATTER_LINE_RE.match(line)
        if not m:
            continue
        key = m.group(1)
        val = m.group(2) if m.group(2) is not None else (m.group(3) or "")
        # Undo the escaping Cleaned.to_markdown applies to quoted values.
        val = val.replace('\\"', '"').replace("\\\\", "\\")
        out[key] = val
    return out


def _load_metadata(slug_dir: Path) -> Optional[dict]:
    meta_path = slug_dir / "metadata.json"
    if not meta_path.exists():
        return None
    try:
        return json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        log.warning("Bad metadata.json in %s: %s", slug_dir.name, e)
        return None


def _save_metadata(slug_dir: Path, meta: dict) -> None:
    (slug_dir / "metadata.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8"
    )


def migrate_legacy_naming(slug_dir: Path, dry_run: bool) -> tuple[list[str], set[str]]:
    """
    If we find the legacy pair (link_NN.md with frontmatter + link_NN.raw.md
    without frontmatter), swap them to the new scheme:
        link_NN.md (cleaned)     -> link_NN.clean.md
        link_NN.raw.md (raw)     -> link_NN.md

    Returns (action log, set of link stems that were actually migrated).
    Callers need the stem set to fix up metadata entries whose legacy
    ``raw_file`` / ``file`` fields still point at the old scheme.
    """
    actions: list[str] = []
    migrated: set[str] = set()
    for raw_legacy in sorted(slug_dir.glob("link_*.raw.md")):
        stem = raw_legacy.name[: -len(".raw.md")]  # link_NN
        current = slug_dir / f"{stem}.md"
        new_clean = slug_dir / f"{stem}.clean.md"

        if not current.exists():
            # Odd state: raw sidecar without a primary. Promote raw to primary.
            actions.append(f"{stem}: promote raw→primary")
            if not dry_run:
                raw_legacy.rename(current)
            migrated.add(stem)
            continue

        current_text = current.read_text(encoding="utf-8", errors="replace")
        raw_text = raw_legacy.read_text(encoding="utf-8", errors="replace")

        current_is_cleaned = has_frontmatter(current_text)
        raw_is_cleaned = has_frontmatter(raw_text)

        if current_is_cleaned and not raw_is_cleaned:
            # Legacy scheme confirmed. Swap.
            actions.append(f"{stem}: swap legacy (primary↔raw → clean/raw)")
            if not dry_run:
                if new_clean.exists():
                    log.warning("%s: %s already exists; leaving legacy alone",
                                slug_dir.name, new_clean.name)
                    continue
                # Move current (cleaned) out of the way first.
                current.rename(new_clean)
                raw_legacy.rename(current)
            migrated.add(stem)
        else:
            # Not legacy — could be new-scheme that happens to have a .raw.md
            # for some reason. Leave alone.
            actions.append(f"{stem}: .raw.md present but not legacy shape — skip")
    return actions, migrated


def _reextract_source(raw_md: Path, url: str, source_type: str,
                      dry_run: bool) -> tuple[bool, str, str]:
    """Re-run extract_url() and overwrite raw_md with fresh content.

    Returns (ok, method, error). Lazy-imports extract so backfill's default
    path does not require requests/trafilatura/bs4.
    """
    try:
        from extract import extract_url  # type: ignore
    except ImportError as e:
        return False, "", f"extract_import_failed: {e}"

    try:
        r = extract_url(url)
    except Exception as e:
        return False, "", f"extract_failed: {e}"

    if not r.get("text"):
        return False, r.get("method", ""), r.get("error", "") or "empty_text"

    if dry_run:
        return True, r.get("method", ""), ""

    raw_md.write_text(r["text"], encoding="utf-8")
    return True, r.get("method", ""), ""


def clean_one_link(raw_md: Path, url: str, source_type: str,
                   use_llm: bool, dry_run: bool,
                   redo_fallback: bool = False,
                   model: str = "claude-opus-4-6",
                   re_extract: bool = False) -> dict:
    """Clean a single link_NN.md -> link_NN.clean.md.

    With re_extract=True, first re-runs the source extractor (extract_url)
    and overwrites link_NN.md with fresh content before cleaning. This is
    how you upgrade an incident whose raw was captured via the wrong
    extractor (e.g. Jina footer-scrape of a YouTube page that should have
    gone through the transcript extractor).
    """
    clean_path = raw_md.with_name(raw_md.stem + ".clean.md")
    result = {
        "file": raw_md.name,
        "clean_file": clean_path.name,
        "slug": raw_md.parent.name,
        "action": "",
        "cleanup_method": "",
        "title": "",
        "author": "",
        "published": "",
        "error": "",
        "extract_method": "",
    }

    reextracted = False
    if re_extract and url:
        ok, method, err = _reextract_source(raw_md, url, source_type, dry_run)
        result["extract_method"] = method
        if not ok:
            result["action"] = "error"
            result["error"] = f"re_extract_failed: {err}"
            return result
        reextracted = True
        # Force a re-clean even if clean_path exists — the raw changed.
        if clean_path.exists() and not dry_run:
            clean_path.unlink()

    try:
        raw_text = raw_md.read_text(encoding="utf-8")
    except Exception as e:
        result["action"] = "error"
        result["error"] = f"read_failed: {e}"
        return result

    if not raw_text.strip():
        result["action"] = "skip_empty"
        return result

    if has_frontmatter(raw_text):
        # Primary is already a cleaned file (shouldn't happen post-migration,
        # but guard anyway).
        result["action"] = "skip_primary_is_cleaned"
        return result

    if clean_path.exists() and not reextracted:
        existing_method = _existing_cleanup_method(clean_path)
        if redo_fallback and existing_method and existing_method != "llm":
            # Previous run produced a non-LLM clean; caller wants a retry.
            result["previous_cleanup_method"] = existing_method
        else:
            result["action"] = "skip_already_clean"
            result["cleanup_method"] = existing_method or ""
            return result

    try:
        cleaned = clean_markdown(
            raw_text, url=url, source_type=source_type, use_llm=use_llm,
            model=model,
        )
    except Exception as e:
        result["action"] = "error"
        result["error"] = f"clean_failed: {e}"
        return result

    result["cleanup_method"] = cleaned.cleanup_method
    result["title"] = cleaned.title
    result["author"] = cleaned.author
    result["published"] = cleaned.published

    if dry_run:
        result["action"] = "dry_run"
        return result

    clean_path.write_text(cleaned.to_markdown(), encoding="utf-8")
    result["action"] = "cleaned"
    return result


def backfill_incident(slug_dir: Path, use_llm: bool, dry_run: bool,
                      redo_fallback: bool = False,
                      model: str = "claude-opus-4-6",
                      re_extract: bool = False) -> list[dict]:
    """Migrate + clean every link in one incident directory."""
    meta = _load_metadata(slug_dir)
    if meta is None:
        return [{
            "slug": slug_dir.name, "file": "", "action": "error",
            "error": "missing_metadata",
        }]

    migration_actions, migrated_stems = migrate_legacy_naming(slug_dir, dry_run=dry_run)
    for a in migration_actions:
        log.info("  %s migrate: %s", slug_dir.name, a)

    url_by_file = {}
    status_by_file = {}
    for entry in meta.get("crawl_status", []) or []:
        # Accept both new (`file` = raw) and legacy (`file` = cleaned,
        # `raw_file` = raw) entries — the raw file is always link_NN.md
        # after migration.
        fname = entry.get("file")
        if fname and _RAW_FILE_RE.match(fname):
            url_by_file[fname] = entry.get("url", "")
            status_by_file[fname] = entry
        raw_legacy = entry.get("raw_file")
        if raw_legacy and _RAW_FILE_RE.match(raw_legacy):
            # Legacy: raw is the sidecar. After migration it's link_NN.md.
            url_by_file[raw_legacy] = entry.get("url", "")
            status_by_file.setdefault(raw_legacy, entry)

    results = []
    metadata_dirty = not dry_run and bool(migrated_stems)
    for raw_md in sorted(slug_dir.glob("link_*.md")):
        if raw_md.name.endswith(".clean.md") or raw_md.name.endswith(".raw.md"):
            continue
        if not _RAW_FILE_RE.match(raw_md.name):
            continue

        url = url_by_file.get(raw_md.name, "")
        existing_status = status_by_file.get(raw_md.name) or {}
        source_type = existing_status.get("source_type") or classify_source(url)

        r = clean_one_link(raw_md, url, source_type, use_llm, dry_run,
                           redo_fallback=redo_fallback, model=model,
                           re_extract=re_extract)
        results.append(r)

        if r["action"] == "cleaned" and not dry_run and existing_status:
            existing_status["file"] = raw_md.name
            existing_status["clean_file"] = r["clean_file"]
            existing_status.pop("raw_file", None)
            existing_status["cleanup_method"] = r["cleanup_method"]
            existing_status["title"] = r["title"]
            existing_status["author"] = r["author"]
            existing_status["published"] = r["published"]
            if r.get("extract_method"):
                # Re-extract replaced raw_md; refresh the crawl-side fields.
                existing_status["method"] = r["extract_method"]
                existing_status["chars"] = raw_md.stat().st_size
                # Re-classify from the (possibly unwrapped) URL so an
                # archive-wrapped YouTube becomes source_type=youtube.
                existing_status["source_type"] = classify_source(url)
            else:
                existing_status["source_type"] = source_type
            metadata_dirty = True
        elif (
            r["action"] == "skip_already_clean"
            and not dry_run
            and existing_status
        ):
            # Clean file already exists on disk but metadata may be stale:
            #   - legacy migration (raw_file pointer, no clean_file)
            #   - crash recovery: clean file written but process died
            #     before _save_metadata in a prior run
            # Repair structural fields unconditionally and backfill
            # title/author/published/cleanup_method from the clean file's
            # frontmatter when the entry is missing them.
            clean_path = raw_md.with_name(raw_md.stem + ".clean.md")
            fm = _read_clean_frontmatter(clean_path)
            if (
                existing_status.get("file") != raw_md.name
                or existing_status.get("clean_file") != clean_path.name
                or "raw_file" in existing_status
            ):
                existing_status["file"] = raw_md.name
                existing_status["clean_file"] = clean_path.name
                existing_status.pop("raw_file", None)
                metadata_dirty = True
            if source_type and not existing_status.get("source_type"):
                existing_status["source_type"] = source_type
                metadata_dirty = True
            for key in ("title", "author", "published", "cleanup_method",
                        "source_type"):
                val = fm.get(key)
                if val and not existing_status.get(key):
                    existing_status[key] = val
                    metadata_dirty = True

        if r["action"] == "cleaned":
            time.sleep(1.0)  # polite delay — each clean call may hit Anthropic

    if not dry_run and metadata_dirty:
        _save_metadata(slug_dir, meta)

    return results


def backfill_all(workers: int, use_llm: bool, dry_run: bool,
                 only: Optional[str] = None,
                 redo_fallback: bool = False,
                 model: str = "claude-opus-4-6",
                 re_extract: bool = False) -> None:
    if not ARTICLES_DIR.exists():
        log.error("No articles directory at %s", ARTICLES_DIR)
        return

    slugs = [d for d in sorted(ARTICLES_DIR.iterdir()) if d.is_dir()]
    if only:
        slugs = [d for d in slugs if d.name == only]
        if not slugs:
            log.error("No incident directory named %s", only)
            return

    log.info("Backfilling %d incident(s); workers=%d llm=%s dry_run=%s",
             len(slugs), workers, use_llm, dry_run)

    totals: dict[str, int] = {}

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(backfill_incident, d, use_llm, dry_run,
                        redo_fallback, model, re_extract): d
            for d in slugs
        }
        for fut in as_completed(futures):
            d = futures[fut]
            try:
                results = fut.result()
            except Exception as e:
                log.error("incident %s failed: %s", d.name, e)
                totals["error"] = totals.get("error", 0) + 1
                continue
            for r in results:
                totals[r["action"]] = totals.get(r["action"], 0) + 1
                if r["action"] == "error":
                    log.warning("  %s/%s: %s", r["slug"], r["file"], r["error"])
                else:
                    log.info("  %s/%s: %s (%s)",
                             r["slug"], r["file"], r["action"],
                             r["cleanup_method"] or "-")

    log.info("Backfill totals: %s", totals)


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Retroactively clean crawled articles.")
    p.add_argument("--workers", type=int, default=5,
                   help="Parallel incident workers (default: 5)")
    p.add_argument("--no-llm", action="store_true",
                   help="Heuristic cleanup only; skip Claude")
    p.add_argument("--dry-run", action="store_true",
                   help="Report actions without writing any files")
    p.add_argument("--only", default=None,
                   help="Backfill a single incident slug (for testing)")
    p.add_argument("--redo-fallback", action="store_true",
                   help="Re-run clean files whose frontmatter cleanup_method "
                        "is not 'llm' (e.g. fallback_heuristic, raw). "
                        "LLM-cleaned files are still skipped.")
    p.add_argument("--model", default="claude-opus-4-6",
                   help="Anthropic model id (default: claude-opus-4-6). "
                        "Useful with --redo-fallback to retry with a "
                        "different model, e.g. claude-sonnet-4-6.")
    p.add_argument("--re-extract", action="store_true",
                   help="Re-run the source extractor (extract_url) and "
                        "overwrite link_NN.md with fresh content before "
                        "cleaning. Use this to upgrade raws captured with "
                        "the wrong extractor — e.g. a YouTube URL that "
                        "was initially Jina-scraped and should have gone "
                        "through the transcript path. Requires the full "
                        "extract.py dependency set (requests, trafilatura, "
                        "bs4, youtube-transcript-api).")
    args = p.parse_args(argv)

    backfill_all(
        workers=args.workers,
        use_llm=not args.no_llm,
        dry_run=args.dry_run,
        only=args.only,
        redo_fallback=args.redo_fallback,
        model=args.model,
        re_extract=args.re_extract,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
