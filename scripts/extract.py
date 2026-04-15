# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests>=2.31.0",
#   "beautifulsoup4>=4.12.0",
#   "trafilatura>=1.8.0",
#   "pdfplumber>=0.10.0",
#   "pypdf>=4.0.0",
#   "anthropic>=0.25.0",
#   "lxml>=5.0.0",
#   "pillow>=10.0.0",
#   "youtube-transcript-api>=0.6.2",
# ]
# ///
"""
Content extraction utilities – URL → clean markdown.

Strategy (applied in order, first success wins):
0. YouTube transcript – if URL is a YouTube video, fetch the transcript via
                     youtube-transcript-api (no Jina / page scrape).
1. Jina AI reader  – r.jina.ai/<url> returns markdown for HTML *and* PDFs,
                     handles JS-rendered pages, web archives, etc.
                     Free without an API key; set JINA_API_KEY for higher limits.
2. trafilatura     – lightweight HTML article extractor (no network round-trip)
3. pdfplumber      – native PDF text extraction for text-layer PDFs
4. Claude vision   – last-resort OCR for scanned PDFs / images
                     (requires ANTHROPIC_API_KEY, enabled with --vision flag)
"""
import io
import os
import re
import base64
import logging
from typing import Optional
from urllib.parse import urlparse, parse_qs

import requests
import trafilatura
from bs4 import BeautifulSoup

# Re-export from the lightweight sources module so callers can keep
# `from extract import classify_source` working while keeping the
# classifier itself free of heavy HTTP/parsing dependencies.
from sources import (  # noqa: F401
    YT_HOSTS as _YT_HOSTS,
    ARCHIVE_HOSTS as _ARCHIVE_HOSTS,
    classify_source,
)

log = logging.getLogger(__name__)

# Shared HTTP session with browser-like headers
_SESSION = requests.Session()
_SESSION.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
})

# ---------------------------------------------------------------------------
# 1. Jina AI reader  (primary – markdown out for any URL)
# ---------------------------------------------------------------------------

def extract_with_jina(url: str) -> str:
    """
    Fetch any URL via r.jina.ai and return clean markdown.

    Works for news articles, blog posts, PDFs, web archives, and most
    JS-rendered pages.  No API key required; set JINA_API_KEY env var for
    higher rate limits (free tier ~20 req/min without a key).
    """
    jina_url = f"https://r.jina.ai/{url}"
    headers = {
        "Accept": "text/plain",
        "X-Return-Format": "markdown",
        # Ask jina to wait for JS rendering
        "X-Wait-For-Selector": "body",
    }
    api_key = os.environ.get("JINA_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        resp = requests.get(jina_url, headers=headers, timeout=60, allow_redirects=True)
        if resp.status_code == 200:
            text = resp.text.strip()
            if len(text) > 200:
                return text
        else:
            log.debug("Jina returned HTTP %d for %s", resp.status_code, url)
    except Exception as e:
        log.debug("Jina reader failed for %s: %s", url, e)

    return ""


# ---------------------------------------------------------------------------
# 2. HTML helpers  (trafilatura fallback)
# ---------------------------------------------------------------------------

def _fetch_raw(url: str, timeout: int = 20) -> Optional[requests.Response]:
    try:
        resp = _SESSION.get(url, timeout=timeout, allow_redirects=True)
        resp.raise_for_status()
        return resp
    except Exception as e:
        log.warning("fetch failed %s: %s", url, e)
        return None


def _head_content_type(url: str, timeout: int = 10) -> str:
    """Cheap HEAD request just to read Content-Type. Returns "" on failure."""
    try:
        resp = _SESSION.head(url, timeout=timeout, allow_redirects=True)
        if resp.status_code < 400:
            return resp.headers.get("content-type", "") or ""
    except Exception as e:
        log.debug("HEAD failed for %s: %s", url, e)
    return ""


def _is_pdf(resp: requests.Response) -> bool:
    ct = resp.headers.get("content-type", "").lower()
    return "pdf" in ct or resp.url.lower().endswith(".pdf")


def extract_html(html: str, url: str = "") -> str:
    """Extract main article text from HTML via trafilatura, falling back to BS4."""
    text = trafilatura.extract(
        html,
        url=url,
        include_comments=False,
        include_tables=True,
        no_fallback=False,
        favor_recall=True,
    )
    if text and len(text) > 200:
        return text

    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()
    body = soup.find("body") or soup
    return body.get_text(separator="\n", strip=True)


# ---------------------------------------------------------------------------
# 3. PDF helpers  (pdfplumber / pypdf fallback)
# ---------------------------------------------------------------------------

def extract_pdf_bytes(data: bytes) -> str:
    """Extract text from a PDF given its raw bytes."""
    try:
        import pdfplumber
        with pdfplumber.open(io.BytesIO(data)) as pdf:
            pages = [p.extract_text() or "" for p in pdf.pages]
            text = "\n\n".join(p for p in pages if p)
            if text.strip():
                return text
    except Exception as e:
        log.debug("pdfplumber failed: %s", e)

    try:
        import pypdf
        reader = pypdf.PdfReader(io.BytesIO(data))
        pages = [p.extract_text() or "" for p in reader.pages]
        return "\n\n".join(p for p in pages if p)
    except Exception as e:
        log.debug("pypdf failed: %s", e)

    return ""


# ---------------------------------------------------------------------------
# 4. Claude vision OCR  (last resort – scanned PDFs / images)
# ---------------------------------------------------------------------------

def ocr_with_claude(content: bytes, mime: str, prompt: str = "") -> str:
    """
    Use Claude's vision capability to OCR a document.

    content  – raw bytes (PDF or image)
    mime     – MIME type string
    Requires ANTHROPIC_API_KEY in environment.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        log.warning("ANTHROPIC_API_KEY not set – skipping vision OCR")
        return ""

    try:
        import anthropic
    except ImportError:
        log.warning("anthropic package not installed")
        return ""

    client = anthropic.Anthropic(api_key=api_key)

    if "pdf" in mime:
        b64 = base64.standard_b64encode(content).decode()
        doc_block: dict = {
            "type": "document",
            "source": {"type": "base64", "media_type": "application/pdf", "data": b64},
        }
    else:
        b64 = base64.standard_b64encode(content).decode()
        doc_block = {
            "type": "image",
            "source": {"type": "base64", "media_type": mime, "data": b64},
        }

    instruction = prompt or (
        "Extract and return all meaningful text from this document as markdown. "
        "Preserve structure (headings, lists, tables). "
        "Skip ads, navigation, and boilerplate."
    )

    try:
        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": [doc_block, {"type": "text", "text": instruction}],
            }],
        )
        return response.content[0].text
    except Exception as e:
        log.error("Claude vision OCR failed: %s", e)
        return ""


# ---------------------------------------------------------------------------
# 5. YouTube transcript extraction
# ---------------------------------------------------------------------------


def _youtube_video_id(url: str) -> Optional[str]:
    """Return the 11-char video id for a YouTube URL, or None if not YouTube."""
    try:
        u = urlparse(url)
    except Exception:
        return None
    host = (u.hostname or "").lower()
    if host not in _YT_HOSTS:
        return None
    if host == "youtu.be":
        vid = u.path.lstrip("/").split("/", 1)[0]
    elif u.path.startswith("/watch"):
        vid = parse_qs(u.query).get("v", [""])[0]
    elif u.path.startswith("/shorts/") or u.path.startswith("/embed/"):
        parts = u.path.strip("/").split("/")
        vid = parts[1] if len(parts) > 1 else ""
    else:
        vid = ""
    return vid if re.fullmatch(r"[A-Za-z0-9_-]{11}", vid or "") else None


def extract_youtube(url: str) -> str:
    """
    Fetch the transcript for a YouTube video and return it as markdown.

    Returns "" if the URL isn't YouTube, the transcript is unavailable,
    or the library isn't installed.
    """
    vid = _youtube_video_id(url)
    if not vid:
        return ""

    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        from youtube_transcript_api._errors import (
            TranscriptsDisabled, NoTranscriptFound, VideoUnavailable,
        )
    except ImportError:
        log.warning("youtube-transcript-api not installed")
        return ""

    try:
        # youtube-transcript-api >=1.0 removed the static `list_transcripts`
        # classmethod in favor of the instance method `.list()` on
        # `YouTubeTranscriptApi()`.  Support both so the extractor keeps
        # working across the version ranges allowed by pyproject.toml.
        try:
            transcripts = YouTubeTranscriptApi().list(vid)
        except AttributeError:
            transcripts = YouTubeTranscriptApi.list_transcripts(vid)
        # Prefer manually-created English, then any manual, then auto English,
        # then any auto-generated.
        for finder in (
            lambda: transcripts.find_manually_created_transcript(["en", "en-US", "en-GB"]),
            lambda: next(iter(transcripts._manually_created_transcripts.values())),
            lambda: transcripts.find_generated_transcript(["en", "en-US", "en-GB"]),
            lambda: next(iter(transcripts._generated_transcripts.values())),
        ):
            try:
                t = finder()
                entries = t.fetch()
                break
            except (NoTranscriptFound, StopIteration, AttributeError):
                continue
        else:
            return ""
    except (TranscriptsDisabled, VideoUnavailable) as e:
        log.debug("YouTube transcript unavailable for %s: %s", url, e)
        return ""
    except Exception as e:
        log.debug("YouTube transcript fetch failed for %s: %s", url, e)
        return ""

    # Format as plain text with simple timestamp markers every minute or so.
    lines = []
    last_mark = -60
    for e in entries:
        # entries may be dicts (older API) or FetchedTranscriptSnippet objects (newer).
        start = e["start"] if isinstance(e, dict) else getattr(e, "start", 0.0)
        text = e["text"] if isinstance(e, dict) else getattr(e, "text", "")
        text = text.replace("\n", " ").strip()
        if not text:
            continue
        if start - last_mark >= 60:
            mm, ss = divmod(int(start), 60)
            lines.append(f"\n[{mm:02d}:{ss:02d}]")
            last_mark = start
        lines.append(text)

    body = " ".join(lines).strip()
    if not body:
        return ""

    header = (
        f"Title: YouTube transcript ({vid})\n\n"
        f"URL Source: {url}\n\n"
        f"Markdown Content:\n"
    )
    return header + body


# ---------------------------------------------------------------------------
# 6. Source classification — see scripts/sources.py (imported above).
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def extract_url(url: str, use_vision: bool = True) -> dict:
    """
    Fetch a URL and extract its text content as markdown.

    Returns a dict with keys: url, text, method, error, source_type
    """
    result = {"url": url, "text": "", "method": "", "error": "",
              "source_type": classify_source(url)}

    # 0 ── YouTube: pull transcript directly
    if result["source_type"] == "youtube":
        text = extract_youtube(url)
        if text:
            result["text"] = text
            result["method"] = "youtube_transcript"
            return result
        # fall through to Jina for at least the video description

    # URL-only heuristics miss PDFs served from signed / query endpoints
    # (no ".pdf" suffix).  Do a cheap HEAD probe to pick up the real
    # Content-Type before Jina swallows it.  Skip for YouTube/archive
    # since those are already correctly classified from the host.
    if result["source_type"] in ("article", "other"):
        ct = _head_content_type(url)
        if ct:
            result["source_type"] = classify_source(url, content_type=ct)

    # 1 ── Jina AI reader (handles HTML + PDFs + JS pages)
    text = extract_with_jina(url)
    if text:
        result["text"] = text
        result["method"] = "jina"
        return result

    # 2 ── Raw fetch for fallback paths
    resp = _fetch_raw(url)
    if resp is None:
        result["error"] = "fetch_failed"
        return result

    # 3 ── PDF path: pdfplumber → Claude vision
    if _is_pdf(resp):
        result["source_type"] = "pdf"
        text = extract_pdf_bytes(resp.content)
        if text.strip():
            result["text"] = text
            result["method"] = "pdfplumber"
            return result

        if use_vision:
            log.info("Falling back to Claude vision OCR for %s", url)
            text = ocr_with_claude(resp.content, "application/pdf")
            if text:
                result["text"] = text
                result["method"] = "claude_vision_pdf"
                return result

        result["error"] = "pdf_extract_failed"
        return result

    # 4 ── HTML path: trafilatura → BS4
    ct = resp.headers.get("content-type", "")
    if "html" in ct or not ct:
        text = extract_html(resp.text, url=url)
        if text and len(text) > 100:
            result["text"] = text
            result["method"] = "trafilatura"
            return result

    result["error"] = "no_content"
    return result
