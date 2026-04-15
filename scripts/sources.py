"""
Lightweight URL → source-type classification.

Kept in its own module (no network / parsing deps) so tools that only
need the taxonomy — e.g. scripts/backfill_clean.py — can import it
without pulling in requests/trafilatura/bs4 transitively.
"""
from __future__ import annotations

from urllib.parse import urlparse


YT_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}

ARCHIVE_HOSTS = {
    "web.archive.org", "archive.org", "archive.ph", "archive.today",
    "archive.is", "webcache.googleusercontent.com",
}


def classify_source(url: str, content_type: str = "") -> str:
    """
    Classify a source URL into one of:
        article, pdf, youtube, archive, other
    """
    try:
        u = urlparse(url)
    except Exception:
        return "other"
    host = (u.hostname or "").lower()
    path = (u.path or "").lower()
    ct = (content_type or "").lower()

    if host in YT_HOSTS:
        return "youtube"
    if host in ARCHIVE_HOSTS:
        return "archive"
    if path.endswith(".pdf") or "pdf" in ct:
        return "pdf"
    if "html" in ct or ct == "" or ct.startswith("text/"):
        return "article"
    return "other"
