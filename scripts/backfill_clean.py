# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.25.0",
# ]
# ///
"""
Retroactively clean every data/articles/<slug>/link_NN.md through the same
Claude-based cleanup pass that crawl.py now runs on new crawls.

For each existing link_NN.md:
  - If a sibling link_NN.raw.md already exists and link_NN.md has a YAML
    frontmatter block, the file is already cleaned → skip.
  - Otherwise: rename link_NN.md → link_NN.raw.md, write the cleaned
    output to link_NN.md, and update the matching crawl_status entry in
    metadata.json with source_type / title / author / published /
    cleanup_method.

Idempotent: safe to re-run. Parallelism mirrors crawl.py.

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

_LINK_FILE_RE = re.compile(r"^link_(\d+)\.md$")


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


def _status_for_file(meta: dict, fname: str) -> Optional[dict]:
    """Find the crawl_status entry whose 'file' matches fname."""
    for entry in meta.get("crawl_status", []) or []:
        if entry.get("file") == fname:
            return entry
    return None


def clean_one_file(link_md: Path, url: str, source_type: str,
                   use_llm: bool, dry_run: bool) -> dict:
    """
    Clean a single link_NN.md in place. Returns a summary dict.
    """
    raw_path = link_md.with_name(link_md.stem + ".raw.md")
    result = {
        "file": link_md.name,
        "slug": link_md.parent.name,
        "action": "",
        "cleanup_method": "",
        "title": "",
        "author": "",
        "published": "",
        "error": "",
    }

    try:
        content = link_md.read_text(encoding="utf-8")
    except Exception as e:
        result["action"] = "error"
        result["error"] = f"read_failed: {e}"
        return result

    if raw_path.exists() and has_frontmatter(content):
        result["action"] = "skip_already_clean"
        return result

    if not content.strip():
        result["action"] = "skip_empty"
        return result

    try:
        cleaned = clean_markdown(
            content, url=url, source_type=source_type, use_llm=use_llm,
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

    # Preserve raw first, then overwrite link_NN.md with cleaned output.
    if not raw_path.exists():
        link_md.rename(raw_path)
    link_md.write_text(cleaned.to_markdown(), encoding="utf-8")
    result["action"] = "cleaned"
    return result


def backfill_incident(slug_dir: Path, use_llm: bool, dry_run: bool) -> list[dict]:
    """Clean every link_NN.md in one incident directory."""
    meta = _load_metadata(slug_dir)
    if meta is None:
        return [{
            "slug": slug_dir.name, "file": "", "action": "error",
            "error": "missing_metadata",
        }]

    # Build URL lookup: crawl_status.file -> url
    url_by_file = {}
    status_by_file = {}
    for entry in meta.get("crawl_status", []) or []:
        f = entry.get("file")
        if f:
            url_by_file[f] = entry.get("url", "")
            status_by_file[f] = entry

    results = []
    for link_md in sorted(slug_dir.glob("link_*.md")):
        if link_md.name.endswith(".raw.md"):
            continue
        if not _LINK_FILE_RE.match(link_md.name):
            continue

        url = url_by_file.get(link_md.name, "")
        existing_status = status_by_file.get(link_md.name) or {}
        source_type = existing_status.get("source_type") or classify_source(url)

        r = clean_one_file(link_md, url, source_type, use_llm, dry_run)
        results.append(r)

        if r["action"] == "cleaned" and not dry_run:
            # Update metadata for this link.
            if existing_status:
                existing_status["raw_file"] = link_md.stem + ".raw.md"
                existing_status["source_type"] = source_type
                existing_status["cleanup_method"] = r["cleanup_method"]
                existing_status["title"] = r["title"]
                existing_status["author"] = r["author"]
                existing_status["published"] = r["published"]

        # polite delay — each clean call may hit the Anthropic API
        if r["action"] == "cleaned":
            time.sleep(1.0)

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

    totals = {"cleaned": 0, "skip_already_clean": 0, "skip_empty": 0,
              "dry_run": 0, "error": 0}

    # Parallelize at the incident level (each incident is processed
    # serially internally so we don't stampede Anthropic / Jina).
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
                totals["error"] += 1
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
