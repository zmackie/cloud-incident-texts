"""
Tests for scripts/backfill_clean.py — specifically the metadata-repair
path when a .clean.md file already exists on disk but metadata.json is
stale (legacy migration or crash between file write and metadata save).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from backfill_clean import (  # noqa: E402
    _read_clean_frontmatter,
    backfill_incident,
)


CLEAN_FILE = """\
---
title: "Example Title"
url: "https://example.com/post"
author: "Jane Doe"
published: "2024-01-15"
source_type: article
source_domain: example.com
cleanup_method: llm
---

Real article body that would survive cleaning.
"""


RAW_FILE = """\
Title: Example Title

URL Source: https://example.com/post

Markdown Content:
# Example Title

Real article body that would survive cleaning.
"""


@pytest.fixture
def slug_dir(tmp_path: Path) -> Path:
    d = tmp_path / "example-incident"
    d.mkdir()
    (d / "link_00.md").write_text(RAW_FILE, encoding="utf-8")
    (d / "link_00.clean.md").write_text(CLEAN_FILE, encoding="utf-8")
    return d


def test_read_clean_frontmatter_parses_quoted_and_bare_values(tmp_path: Path):
    f = tmp_path / "x.clean.md"
    f.write_text(CLEAN_FILE, encoding="utf-8")
    fm = _read_clean_frontmatter(f)
    assert fm["title"] == "Example Title"
    assert fm["author"] == "Jane Doe"
    assert fm["published"] == "2024-01-15"
    assert fm["source_type"] == "article"
    assert fm["cleanup_method"] == "llm"


def test_read_clean_frontmatter_missing_file_returns_empty(tmp_path: Path):
    assert _read_clean_frontmatter(tmp_path / "nope.md") == {}


def test_read_clean_frontmatter_no_frontmatter_returns_empty(tmp_path: Path):
    f = tmp_path / "plain.md"
    f.write_text("just a line\n", encoding="utf-8")
    assert _read_clean_frontmatter(f) == {}


def test_backfill_repairs_stale_metadata_when_clean_file_exists(slug_dir: Path):
    """Simulates a crash between clean file write and metadata save:
    metadata entry has no clean_file / title / author — re-running must
    repair it from the existing clean file's frontmatter."""
    meta = {
        "crawl_status": [
            {
                "url": "https://example.com/post",
                "file": "link_00.md",
                # NOTE: no clean_file, no title/author/published/cleanup_method
            }
        ]
    }
    (slug_dir / "metadata.json").write_text(json.dumps(meta), encoding="utf-8")

    results = backfill_incident(slug_dir, use_llm=False, dry_run=False)

    assert len(results) == 1
    assert results[0]["action"] == "skip_already_clean"

    saved = json.loads((slug_dir / "metadata.json").read_text(encoding="utf-8"))
    entry = saved["crawl_status"][0]
    assert entry["file"] == "link_00.md"
    assert entry["clean_file"] == "link_00.clean.md"
    assert entry["title"] == "Example Title"
    assert entry["author"] == "Jane Doe"
    assert entry["published"] == "2024-01-15"
    assert entry["cleanup_method"] == "llm"
    assert entry["source_type"] == "article"


def test_backfill_repairs_legacy_raw_file_pointer(slug_dir: Path):
    """Legacy metadata shape has `raw_file` pointing at a .raw.md sidecar.
    After migration (no sidecar present) we must drop raw_file and fill
    clean_file."""
    meta = {
        "crawl_status": [
            {
                "url": "https://example.com/post",
                "file": "link_00.md",
                "raw_file": "link_00.raw.md",  # stale — file not on disk
            }
        ]
    }
    (slug_dir / "metadata.json").write_text(json.dumps(meta), encoding="utf-8")

    backfill_incident(slug_dir, use_llm=False, dry_run=False)

    entry = json.loads((slug_dir / "metadata.json").read_text(encoding="utf-8"))
    entry = entry["crawl_status"][0]
    assert "raw_file" not in entry
    assert entry["clean_file"] == "link_00.clean.md"


def test_backfill_noop_when_metadata_already_correct(slug_dir: Path):
    """If metadata is already complete and on-disk matches, no write."""
    meta = {
        "crawl_status": [
            {
                "url": "https://example.com/post",
                "file": "link_00.md",
                "clean_file": "link_00.clean.md",
                "source_type": "article",
                "cleanup_method": "llm",
                "title": "Example Title",
                "author": "Jane Doe",
                "published": "2024-01-15",
            }
        ]
    }
    meta_path = slug_dir / "metadata.json"
    meta_path.write_text(json.dumps(meta), encoding="utf-8")
    mtime_before = meta_path.stat().st_mtime_ns

    backfill_incident(slug_dir, use_llm=False, dry_run=False)

    # File should not have been rewritten.
    assert meta_path.stat().st_mtime_ns == mtime_before
