"""
Tests for scripts/extract.py — specifically source_type classification
when HEAD is unavailable (common: PDFs served from signed endpoints
that 403/405 on HEAD but return content on GET).
"""
from __future__ import annotations

import sys
from pathlib import Path
from unittest import mock

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

# extract.py imports requests/trafilatura/bs4 at module load; skip the
# whole module cleanly if those aren't installed locally.
pytest.importorskip("requests")
pytest.importorskip("trafilatura")
pytest.importorskip("bs4")

import extract  # noqa: E402
from extract import _PDF_MAGIC, _refine_source_type  # noqa: E402


# ---------------------------------------------------------------------------
# _refine_source_type: pure logic — upgrades article/other → pdf on signals
# ---------------------------------------------------------------------------

def test_refine_keeps_article_when_no_pdf_signals():
    assert _refine_source_type(
        "article", "https://example.com/post",
        content_type="text/html", snippet=b"<html>...",
    ) == "article"


def test_refine_upgrades_to_pdf_via_content_type():
    assert _refine_source_type(
        "article", "https://example.com/signed-url?id=1",
        content_type="application/pdf", snippet=b"",
    ) == "pdf"


def test_refine_upgrades_to_pdf_via_magic_bytes_when_header_missing():
    # Server lied / omitted header but the body starts with %PDF-
    assert _refine_source_type(
        "article", "https://example.com/signed-url?id=1",
        content_type="", snippet=_PDF_MAGIC + b"1.4 rest of pdf...",
    ) == "pdf"


def test_refine_does_not_downgrade_specific_types():
    # If caller already classified as youtube/archive, no header or
    # snippet should pull it back to article.
    assert _refine_source_type(
        "youtube", "https://www.youtube.com/watch?v=xyz",
        content_type="text/html", snippet=b"",
    ) == "youtube"


def test_refine_returns_other_when_unknown():
    assert _refine_source_type(
        "other", "https://example.com/foo.bin",
        content_type="application/octet-stream", snippet=b"",
    ) == "other"


# ---------------------------------------------------------------------------
# _probe_source_type: HEAD failure should fall back to Range GET
# ---------------------------------------------------------------------------

def _fake_response(status=200, content_type="", body=b""):
    r = mock.MagicMock()
    r.status_code = status
    r.headers = {"content-type": content_type} if content_type else {}
    r.iter_content = mock.MagicMock(return_value=iter([body]))
    r.close = mock.MagicMock()
    return r


def test_probe_prefers_head_when_content_type_is_present():
    with mock.patch.object(extract._SESSION, "head",
                           return_value=_fake_response(200, "application/pdf")), \
         mock.patch.object(extract._SESSION, "get") as mget:
        ct, snippet = extract._probe_source_type("https://example.com/x")
        assert ct == "application/pdf"
        assert snippet == b""
        mget.assert_not_called()


def test_probe_falls_back_to_range_get_when_head_rejected():
    with mock.patch.object(extract._SESSION, "head",
                           return_value=_fake_response(405, "")), \
         mock.patch.object(extract._SESSION, "get",
                           return_value=_fake_response(
                               206, "", _PDF_MAGIC + b"1.4 ...",
                           )) as mget:
        ct, snippet = extract._probe_source_type("https://example.com/signed")
        assert ct == ""  # server also omits content-type
        assert snippet.startswith(_PDF_MAGIC)
        mget.assert_called_once()
        # Must be a Range request so we don't download the whole body.
        _, kwargs = mget.call_args
        assert "Range" in kwargs.get("headers", {})


def test_probe_falls_back_when_head_throws():
    with mock.patch.object(extract._SESSION, "head",
                           side_effect=Exception("connection refused")), \
         mock.patch.object(extract._SESSION, "get",
                           return_value=_fake_response(
                               200, "application/pdf", b"%PDF-...",
                           )):
        ct, snippet = extract._probe_source_type("https://example.com/signed")
        assert ct == "application/pdf"


def test_probe_returns_empty_when_both_fail():
    with mock.patch.object(extract._SESSION, "head",
                           side_effect=Exception("nope")), \
         mock.patch.object(extract._SESSION, "get",
                           side_effect=Exception("nope")):
        assert extract._probe_source_type("https://example.com/x") == ("", b"")
