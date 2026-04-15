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
from extract import classify_source

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent / "data"
ARTICLES_DIR = DATA_DIR / "articles"

_RAW_FILE_RE = re.compile(r"^link_(\d+)\.md$")


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


def migrate_legacy_naming(slug_dir: Path, dry_run: bool) -> list[str]:
    """
    If we find the legacy pair (link_NN.md with frontmatter + link_NN.raw.md
    without frontmatter), swap them to the new scheme:
        link_NN.md (cleaned)     -> link_NN.clean.md
        link_NN.raw.md (raw)     -> link_NN.md
    """
    actions: list[str] = []
    for raw_legacy in sorted(slug_dir.glob("link_*.raw.md")):
        stem = raw_legacy.name[: -len(".raw.md")]  # link_NN
        current = slug_dir / f"{stem}.md"
        new_clean = slug_dir / f"{stem}.clean.md"

        if not current.exists():
            # Odd state: raw sidecar without a primary. Promote raw to primary.
            actions.append(f"{stem}: promote raw→primary")
            if not dry_run:
                raw_legacy.rename(current)
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
        else:
            # Not legacy — could be new-scheme that happens to have a .raw.md
            # for some reason. Leave alone.
            actions.append(f"{stem}: .raw.md present but not legacy shape — skip")
    return actions


def clean_one_link(raw_md: Path, url: str, source_type: str,
                   use_llm: bool, dry_run: bool) -> dict:
    """Clean a single link_NN.md -> link_NN.clean.md."""
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
    }

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

    if clean_path.exists():
        result["action"] = "skip_already_clean"
        return result

    try:
        cleaned = clean_markdown(
            raw_text, url=url, source_type=source_type, use_llm=use_llm,
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


def backfill_incident(slug_dir: Path, use_llm: bool, dry_run: bool) -> list[dict]:
    """Migrate + clean every link in one incident directory."""
    meta = _load_metadata(slug_dir)
    if meta is None:
        return [{
            "slug": slug_dir.name, "file": "", "action": "error",
            "error": "missing_metadata",
        }]

    migration_actions = migrate_legacy_naming(slug_dir, dry_run=dry_run)
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
    for raw_md in sorted(slug_dir.glob("link_*.md")):
        if raw_md.name.endswith(".clean.md") or raw_md.name.endswith(".raw.md"):
            continue
        if not _RAW_FILE_RE.match(raw_md.name):
            continue

        url = url_by_file.get(raw_md.name, "")
        existing_status = status_by_file.get(raw_md.name) or {}
        source_type = existing_status.get("source_type") or classify_source(url)

        r = clean_one_link(raw_md, url, source_type, use_llm, dry_run)
        results.append(r)

        if r["action"] == "cleaned" and not dry_run and existing_status:
            existing_status["file"] = raw_md.name
            existing_status["clean_file"] = r["clean_file"]
            existing_status.pop("raw_file", None)
            existing_status["source_type"] = source_type
            existing_status["cleanup_method"] = r["cleanup_method"]
            existing_status["title"] = r["title"]
            existing_status["author"] = r["author"]
            existing_status["published"] = r["published"]

        if r["action"] == "cleaned":
            time.sleep(1.0)  # polite delay — each clean call may hit Anthropic

    if not dry_run and any(r["action"] == "cleaned" for r in results):
        _save_metadata(slug_dir, meta)

    return results


def backfill_all(workers: int, use_llm: bool, dry_run: bool,
                 only: Optional[str] = None) -> None:
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
            pool.submit(backfill_incident, d, use_llm, dry_run): d
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
    args = p.parse_args(argv)

    backfill_all(
        workers=args.workers,
        use_llm=not args.no_llm,
        dry_run=args.dry_run,
        only=args.only,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
