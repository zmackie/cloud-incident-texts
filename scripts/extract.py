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
# ]
# ///
"""
Content extraction utilities – URL → clean markdown.

Strategy (applied in order, first success wins):
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
import base64
import logging
from typing import Optional

import requests
import trafilatura
from bs4 import BeautifulSoup

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
# Main entry point
# ---------------------------------------------------------------------------

def extract_url(url: str, use_vision: bool = True) -> dict:
    """
    Fetch a URL and extract its text content as markdown.

    Returns a dict with keys: url, text, method, error
    """
    result = {"url": url, "text": "", "method": "", "error": ""}

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
