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
Content extraction utilities.

Strategy (applied in order, first success wins):
1. trafilatura  – best for news/blog articles
2. BeautifulSoup readability fallback
3. PDF text extraction via pdfplumber
4. Claude vision OCR  – for scanned PDFs, screenshots, or JS-heavy pages
                        that resist plain-text extraction
"""
import io
import os
import base64
import logging
from typing import Optional
from urllib.parse import urlparse

import requests
import trafilatura
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)

# Shared session with browser-like headers to reduce bot blocking
_SESSION = requests.Session()
_SESSION.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
})


# ---------------------------------------------------------------------------
# HTML helpers
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
    """Extract main article text from HTML, falling back to BS4."""
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

    # BS4 fallback: strip boilerplate tags, return visible text
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()
    body = soup.find("body") or soup
    return body.get_text(separator="\n", strip=True)


# ---------------------------------------------------------------------------
# PDF helpers
# ---------------------------------------------------------------------------

def extract_pdf_bytes(data: bytes) -> str:
    """Extract text from a PDF given its raw bytes."""
    try:
        import pdfplumber
        with pdfplumber.open(io.BytesIO(data)) as pdf:
            pages = []
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    pages.append(t)
            text = "\n\n".join(pages)
            if text.strip():
                return text
    except Exception as e:
        log.warning("pdfplumber failed: %s", e)

    # pypdf fallback
    try:
        import pypdf
        reader = pypdf.PdfReader(io.BytesIO(data))
        pages = [p.extract_text() or "" for p in reader.pages]
        return "\n\n".join(pages)
    except Exception as e:
        log.warning("pypdf failed: %s", e)

    return ""


# ---------------------------------------------------------------------------
# Claude vision OCR  (the "OCR papers" approach)
# ---------------------------------------------------------------------------

def _pdf_to_images(data: bytes, max_pages: int = 10) -> list[bytes]:
    """Render PDF pages to PNG bytes using pypdf + pillow."""
    images = []
    try:
        import pypdf
        from PIL import Image as PILImage
        reader = pypdf.PdfReader(io.BytesIO(data))
        for i, page in enumerate(reader.pages[:max_pages]):
            # Extract any embedded images from the page as a proxy
            for img_obj in page.images:
                images.append(img_obj.data)
                break  # one image per page is enough for context
    except Exception as e:
        log.debug("pdf→image extraction: %s", e)
    return images


def ocr_with_claude(content: bytes, mime: str, prompt: str = "") -> str:
    """
    Use Claude's vision capability to OCR / summarise a document.

    content  – raw bytes (PDF or image)
    mime     – MIME type string
    prompt   – optional custom instruction

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

    # PDFs can be sent directly to Claude's API
    if "pdf" in mime:
        b64 = base64.standard_b64encode(content).decode()
        source: dict = {"type": "base64", "media_type": "application/pdf", "data": b64}
        doc_block: dict = {"type": "document", "source": source}
    else:
        # image
        b64 = base64.standard_b64encode(content).decode()
        doc_block = {
            "type": "image",
            "source": {"type": "base64", "media_type": mime, "data": b64},
        }

    instruction = prompt or (
        "Extract and return all meaningful text from this document. "
        "Preserve structure (headings, lists, tables). "
        "Focus on factual content; skip ads and navigation."
    )

    try:
        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": [doc_block, {"type": "text", "text": instruction}],
                }
            ],
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
    Fetch a URL and extract its text content.

    Returns a dict with keys:
        url, text, method, error
    """
    result = {"url": url, "text": "", "method": "", "error": ""}

    resp = _fetch_raw(url)
    if resp is None:
        result["error"] = "fetch_failed"
        return result

    if _is_pdf(resp):
        raw_text = extract_pdf_bytes(resp.content)
        if raw_text.strip():
            result["text"] = raw_text
            result["method"] = "pdfplumber"
            return result

        if use_vision:
            log.info("Falling back to Claude vision OCR for PDF: %s", url)
            text = ocr_with_claude(resp.content, "application/pdf")
            if text:
                result["text"] = text
                result["method"] = "claude_vision_pdf"
                return result

        result["error"] = "pdf_extract_failed"
        return result

    # HTML path
    ct = resp.headers.get("content-type", "")
    if "html" in ct or not ct:
        text = extract_html(resp.text, url=url)
        if text and len(text) > 100:
            result["text"] = text
            result["method"] = "trafilatura"
            return result

    result["error"] = "no_content"
    return result
