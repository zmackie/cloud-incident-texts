"""
Tests for scripts/sources.py — URL → source-type classification.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from sources import classify_source  # noqa: E402


def test_classify_plain_youtube():
    assert classify_source("https://www.youtube.com/watch?v=abc") == "youtube"


def test_classify_youtu_be_short():
    assert classify_source("https://youtu.be/abc") == "youtube"


def test_classify_plain_archive():
    assert classify_source("https://web.archive.org/web/2020/https://example.com/post") == "archive"


def test_classify_pdf_by_path():
    assert classify_source("https://example.com/report.pdf") == "pdf"


def test_classify_pdf_by_content_type():
    assert classify_source(
        "https://example.com/signed-url?id=1",
        content_type="application/pdf",
    ) == "pdf"


def test_classify_article_by_html():
    assert classify_source(
        "https://example.com/post",
        content_type="text/html",
    ) == "article"


# ---------------------------------------------------------------------------
# Regression: archive-wrapped YouTube URLs must classify as youtube so the
# transcript path runs. Concrete case from the corpus:
#   https://web.archive.org/web/20201103091354/https://www.youtube.com/watch?v=rtEjI_5TPdw
# Previously returned "archive", causing extract_youtube() to be skipped
# and the page to fall through to Jina — which returned only footer
# boilerplate (see mandiant-insider-threat-scenario-2020-september).
# ---------------------------------------------------------------------------

def test_classify_archive_wrapped_youtube_as_youtube():
    url = (
        "https://web.archive.org/web/20201103091354/"
        "https://www.youtube.com/watch?v=rtEjI_5TPdw&feature=youtu.be/"
    )
    assert classify_source(url) == "youtube"


def test_classify_archive_wrapped_youtu_be():
    url = "https://web.archive.org/web/20200101000000/https://youtu.be/abcdefg"
    assert classify_source(url) == "youtube"


def test_classify_archive_wrapped_pdf():
    """An archive-wrapped PDF should classify as pdf, not archive."""
    url = "https://web.archive.org/web/20200101000000/https://example.com/report.pdf"
    assert classify_source(url) == "pdf"


def test_classify_archive_without_inner_url_stays_archive():
    """Plain archive index pages (no wrapped URL) remain 'archive'."""
    assert classify_source("https://web.archive.org/web/20200101000000/") == "archive"
