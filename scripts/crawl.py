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
Crawl all incident links from the aws-customer-security-incidents README
and save their content to data/articles/.

Usage:
    python scripts/crawl.py [--refresh] [--vision] [--workers N]

    --refresh   Re-fetch the incident list even if incidents.json exists
    --vision    Enable Claude vision OCR fallback (needs ANTHROPIC_API_KEY)
    --workers   Parallel worker threads (default: 5)
"""
import argparse
import json
import logging
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from parse_readme import load_or_fetch
from extract import extract_url

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent / "data"
ARTICLES_DIR = DATA_DIR / "articles"


def _slug(text: str) -> str:
    """Make a filesystem-safe slug from incident name + date."""
    s = re.sub(r"[^\w\s-]", "", text.lower())
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return s[:80]


def article_dir(incident: dict) -> Path:
    name = incident.get("name") or incident.get("report", "unknown")
    date = incident.get("date", "unknown")
    slug = _slug(f"{name}-{date}")
    return ARTICLES_DIR / slug


def already_crawled(incident: dict) -> bool:
    d = article_dir(incident)
    return (d / "index.md").exists()


def _unique_stem(d: Path, stem: str) -> str:
    """Return stem (or stem-2, stem-3, …) that isn't already taken in d."""
    candidate = stem
    n = 2
    while (d / f"{candidate}.md").exists():
        candidate = f"{stem}-{n}"
        n += 1
    return candidate


def _write_index(d: Path, incident: dict, results: list) -> None:
    name = incident.get("name", "Unknown")
    date = incident.get("date", "")
    root_cause = incident.get("root_cause", "")
    escalation = incident.get("escalation_vectors", "")
    impact = incident.get("impact", "")
    inc_type = incident.get("type", "")

    lines = [
        "---",
        f'name: "{name}"',
        f'date: "{date}"',
        f"type: {inc_type}",
        f'root_cause: "{root_cause}"',
        f'escalation_vectors: "{escalation}"',
        f'impact: "{impact}"',
        "---",
        "",
        f"# {name}",
        "",
    ]
    for label, value in [
        ("Date", date), ("Root Cause", root_cause),
        ("Escalation Vectors", escalation), ("Impact", impact),
    ]:
        if value:
            lines.append(f"**{label}:** {value}  ")

    if results:
        lines += ["", "## Sources", ""]
        for r in results:
            if r.get("file"):
                lines.append(
                    f"- [{r['link_text']}]({r['file']}) "
                    f"— {r['chars']:,} chars via `{r['method']}`"
                )
            else:
                lines.append(
                    f"- [{r['link_text']}]({r['url']}) "
                    f"— ⚠️ failed ({r.get('error', 'unknown')})"
                )

    (d / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def crawl_incident(incident: dict, use_vision: bool = False) -> dict:
    """Fetch every link for one incident, save results, return summary."""
    name = incident.get("name") or incident.get("report", "?")
    d = article_dir(incident)
    d.mkdir(parents=True, exist_ok=True)

    results = []
    for i, link in enumerate(incident.get("links", [])):
        url = link.get("url", "")
        link_text = link.get("text", "") or f"link-{i:02d}"
        if not url or url.startswith("#"):
            continue
        log.info("  [%s] fetching link %d: %s", name[:40], i + 1, url)
        r = extract_url(url, use_vision=use_vision)
        stem = _unique_stem(d, _slug(link_text) or f"link-{i:02d}")
        out_file = d / f"{stem}.md"
        if r["text"]:
            out_file.write_text(r["text"], encoding="utf-8")
        results.append({
            "url": url,
            "link_text": link_text,
            "file": out_file.name if r["text"] else None,
            "method": r["method"],
            "error": r["error"],
            "chars": len(r["text"]),
        })
        time.sleep(0.5)  # polite rate-limit

    _write_index(d, incident, results)
    ok = sum(1 for r in results if r.get("chars", 0) > 0)
    log.info("[%s] done – %d/%d links captured", name[:40], ok, len(results))
    return {"name": name, "ok": ok, "total": len(results)}


def crawl_all(refresh: bool = False, use_vision: bool = False, workers: int = 5):
    data = load_or_fetch(cache=not refresh)
    incidents = data["all"]
    log.info("Loaded %d incidents total", len(incidents))

    todo = [i for i in incidents if not already_crawled(i)]
    log.info("%d incidents need crawling (%d already done)", len(todo), len(incidents) - len(todo))

    if not todo:
        log.info("Nothing to do.")
        return

    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)

    summary = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(crawl_incident, inc, use_vision): inc for inc in todo}
        for future in as_completed(futures):
            try:
                result = future.result()
                summary.append(result)
            except Exception as e:
                inc = futures[future]
                log.error("Failed %s: %s", inc.get("name", "?"), e)

    ok_total = sum(s["ok"] for s in summary)
    link_total = sum(s["total"] for s in summary)
    log.info("Crawl complete: %d/%d links captured across %d incidents",
             ok_total, link_total, len(summary))

    # Write a crawl summary
    summary_path = DATA_DIR / "crawl_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
    log.info("Summary written to %s", summary_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl aws-customer-security-incidents links")
    parser.add_argument("--refresh", action="store_true", help="Re-fetch incident list")
    parser.add_argument("--vision", action="store_true", help="Enable Claude vision OCR fallback")
    parser.add_argument("--workers", type=int, default=5, help="Parallel workers (default: 5)")
    args = parser.parse_args()

    crawl_all(refresh=args.refresh, use_vision=args.vision, workers=args.workers)
