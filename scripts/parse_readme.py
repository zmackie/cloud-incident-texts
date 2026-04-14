# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.31.0"]
# ///
"""
Parse the aws-customer-security-incidents README into structured incident data.

Fetches the raw README from GitHub and extracts both the primary incident table
and the vendor case-study table into a list of dicts.
"""
import os
import re
import json
from pathlib import Path
from typing import Optional

import requests

README_URL = "https://raw.githubusercontent.com/ramimac/aws-customer-security-incidents/main/README.md"
DATA_DIR = Path(__file__).parent.parent / "data"


def fetch_readme(url: str = README_URL) -> str:
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.text


def _parse_link(cell: str) -> list[dict]:
    """Extract all markdown links from a table cell as {text, url} dicts."""
    return [
        {"text": m[0].strip(), "url": m[1].strip()}
        for m in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", cell)
    ]


def _clean(cell: str) -> str:
    """Strip markdown and whitespace from a cell."""
    cell = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cell)  # collapse links
    cell = re.sub(r"<[^>]+>", "", cell)                    # strip HTML tags
    return cell.strip()


def _parse_table(markdown: str, start_marker: str, columns: list[str]) -> list[dict]:
    """
    Pull rows out of the first markdown table that appears after start_marker.
    columns is the canonical list of field names mapped left-to-right.
    """
    # Find the section
    idx = markdown.find(start_marker)
    if idx == -1:
        return []
    section = markdown[idx:]

    # Find table rows (lines starting with |, skipping header and separator)
    rows = []
    in_table = False
    header_seen = False
    separator_seen = False

    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            if in_table:
                break  # table ended
            continue
        in_table = True
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if not header_seen:
            header_seen = True
            continue
        if not separator_seen:
            separator_seen = True
            continue
        if all(not c for c in cells):
            continue
        # Pad or trim to expected column count
        while len(cells) < len(columns):
            cells.append("")
        record = {}
        for i, col in enumerate(columns):
            raw = cells[i] if i < len(cells) else ""
            if col == "links":
                record[col] = _parse_link(raw)
            else:
                record[col] = _clean(raw)
        rows.append(record)

    return rows


PRIMARY_COLUMNS = ["name", "date", "root_cause", "escalation_vectors", "impact", "links"]
CASE_STUDY_COLUMNS = ["report", "date", "root_cause", "escalation_vectors", "impact", "links"]


def parse_incidents(markdown: str) -> dict:
    primary = _parse_table(
        markdown,
        "# Catalog of AWS Customer Security Incidents",
        PRIMARY_COLUMNS,
    )
    for inc in primary:
        inc["type"] = "primary"

    case_studies = _parse_table(
        markdown,
        "## Vendor-reported AWS Customer Security Incident Case Studies",
        CASE_STUDY_COLUMNS,
    )
    for inc in case_studies:
        inc["type"] = "case_study"
        # normalise field name
        inc["name"] = inc.pop("report", "")

    return {
        "primary": primary,
        "case_studies": case_studies,
        "all": primary + case_studies,
    }


def load_or_fetch(cache: bool = True) -> dict:
    cache_path = DATA_DIR / "incidents.json"
    if cache and cache_path.exists():
        return json.loads(cache_path.read_text())
    markdown = fetch_readme()
    data = parse_incidents(markdown)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(data, indent=2))
    return data


def get_readme_sha() -> Optional[str]:
    """Return the latest commit SHA that touched README.md (for change detection).

    Uses GITHUB_TOKEN env var if present to avoid unauthenticated rate limits
    (60 req/hr unauthenticated vs 5000/hr authenticated).
    """
    import logging
    log = logging.getLogger(__name__)

    api = "https://api.github.com/repos/ramimac/aws-customer-security-incidents/commits"
    headers = {}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        resp = requests.get(
            api, params={"path": "README.md", "per_page": 1},
            headers=headers, timeout=15,
        )
        remaining = resp.headers.get("X-RateLimit-Remaining", "?")
        if resp.status_code == 403:
            log.warning("GitHub rate limit hit (remaining=%s). Set GITHUB_TOKEN to raise limit.", remaining)
            return None
        resp.raise_for_status()
        commits = resp.json()
        return commits[0]["sha"] if commits else None
    except Exception as e:
        log.warning("get_readme_sha failed: %s", e)
        return None


if __name__ == "__main__":
    data = load_or_fetch(cache=False)
    print(f"Primary incidents : {len(data['primary'])}")
    print(f"Case studies      : {len(data['case_studies'])}")
    print(f"Total links       : {sum(len(i['links']) for i in data['all'])}")
