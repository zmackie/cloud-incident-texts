"""
Lightweight URL → source-type classification.

Kept in its own module (no network / parsing deps) so tools that only
need the taxonomy — e.g. scripts/backfill_clean.py — can import it
without pulling in requests/trafilatura/bs4 transitively.
"""
from __future__ import annotations

import re
from urllib.parse import urlparse


YT_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}

ARCHIVE_HOSTS = {
    "web.archive.org", "archive.org", "archive.ph", "archive.today",
    "archive.is", "webcache.googleusercontent.com",
}

# Wayback Machine path shape: /web/<timestamp>[<flag>]/<original-url>.
# Timestamp is 14 digits; optional trailing flag like "if_" / "id_" / "im_".
_WAYBACK_PATH_RE = re.compile(
    r"^/web/\d{14}[a-z_]*/(?P<inner>https?://.+)$", re.IGNORECASE
)


def _unwrap_archive(url: str) -> str:
    """
    If `url` is an archive-wrapped URL (e.g. Wayback Machine), return the
    inner original URL; otherwise return `url` unchanged. Lets callers
    classify by the real host (youtube.com, a .pdf path, etc.) instead
    of the wrapper's host.
    """
    try:
        u = urlparse(url)
    except Exception:
        return url
    if (u.hostname or "").lower() not in ARCHIVE_HOSTS:
        return url
    m = _WAYBACK_PATH_RE.match(u.path or "")
    if not m:
        return url
    inner = m.group("inner")
    # urlparse peeled off the query from the full URL, which actually
    # belongs to the inner URL (everything after the wrapper path is the
    # original). Re-append so downstream sees the full original URL.
    if u.query:
        inner = f"{inner}?{u.query}"
    return inner


def classify_source(url: str, content_type: str = "") -> str:
    """
    Classify a source URL into one of:
        article, pdf, youtube, archive, other

    Archive-wrapped URLs are classified by their *inner* URL so an
    archived YouTube page runs the transcript path and an archived PDF
    gets PDF handling. A bare archive page (no wrapped URL) still
    classifies as "archive".
    """
    unwrapped = _unwrap_archive(url)
    try:
        u = urlparse(unwrapped)
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
