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
#   "schedule>=1.2.1",
# ]
# ///
"""
Monitor the aws-customer-security-incidents README for new incidents.

Polls the GitHub API every POLL_INTERVAL seconds. When the README commit SHA
changes it re-parses, diffs against the stored incident list, and crawls any
newly discovered incidents.

Usage:
    python scripts/monitor.py [--interval SECONDS] [--vision] [--once]

    --interval  Poll interval in seconds (default: 3600 = 1 hour)
    --vision    Enable Claude vision OCR for new incident links
    --once      Run one check then exit (useful for cron/CI)

Environment:
    ANTHROPIC_API_KEY  – optional, enables vision OCR fallback
    GITHUB_TOKEN       – optional, raises GitHub API rate limit
"""
import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# Allow running from the scripts/ directory or the project root
sys.path.insert(0, str(Path(__file__).parent))

from parse_readme import fetch_readme, get_readme_sha, parse_incidents
from crawl import crawl_incident

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent / "data"
STATE_FILE = DATA_DIR / "monitor_state.json"

DEFAULT_INTERVAL = 3600  # 1 hour


# ---------------------------------------------------------------------------
# State helpers
# ---------------------------------------------------------------------------

def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"last_sha": None, "known_incidents": [], "last_checked": None}


def save_state(state: dict):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def _incident_key(inc: dict) -> str:
    """Stable identity key for deduplication."""
    name = inc.get("name") or inc.get("report", "")
    date = inc.get("date", "")
    return f"{name.strip().lower()}|{date.strip().lower()}"


# ---------------------------------------------------------------------------
# Diff logic
# ---------------------------------------------------------------------------

def find_new_incidents(old_keys: set, fresh_incidents: list) -> list:
    new = []
    for inc in fresh_incidents:
        if _incident_key(inc) not in old_keys:
            new.append(inc)
    return new


# ---------------------------------------------------------------------------
# Main monitor loop
# ---------------------------------------------------------------------------

def check_once(state: dict, use_vision: bool = False) -> dict:
    """
    Fetch the current README SHA. If it changed (or we have no prior state),
    re-parse and crawl any new incidents. Returns updated state.
    """
    now = datetime.now(timezone.utc).isoformat()
    current_sha = get_readme_sha()
    log.info("Current README SHA: %s", current_sha)

    if current_sha and current_sha == state.get("last_sha"):
        log.info("No change detected.")
        state["last_checked"] = now
        return state

    log.info("Change detected (old=%s). Re-fetching README …", state.get("last_sha"))
    try:
        markdown = fetch_readme()
    except Exception as e:
        log.error("Failed to fetch README: %s", e)
        return state

    fresh = parse_incidents(markdown)
    fresh_all = fresh["all"]
    known_keys = set(state.get("known_incidents", []))

    new_incidents = find_new_incidents(known_keys, fresh_all)

    if new_incidents:
        log.info("Found %d new incident(s)!", len(new_incidents))
        for inc in new_incidents:
            log.info("  + %s (%s)", inc.get("name", "?"), inc.get("date", "?"))
            try:
                crawl_incident(inc, use_vision=use_vision)
            except Exception as e:
                log.error("    Crawl failed for %s: %s", inc.get("name"), e)
    else:
        log.info("README changed but no new incidents detected (edit/fix to existing entry?).")

    # Persist new state
    # Re-save the full incidents.json with the latest data
    incidents_path = DATA_DIR / "incidents.json"
    incidents_path.write_text(json.dumps(fresh, indent=2))

    state["last_sha"] = current_sha
    state["last_checked"] = now
    state["known_incidents"] = [_incident_key(i) for i in fresh_all]

    # Append to a change log
    if new_incidents:
        changelog = DATA_DIR / "changelog.jsonl"
        entry = {
            "detected_at": now,
            "sha": current_sha,
            "new_incidents": [
                {"name": i.get("name", "?"), "date": i.get("date", "?"), "type": i.get("type")}
                for i in new_incidents
            ],
        }
        with changelog.open("a") as f:
            f.write(json.dumps(entry) + "\n")
        log.info("Change log updated: %s", changelog)

    return state


def run_monitor(interval: int = DEFAULT_INTERVAL, use_vision: bool = False, once: bool = False):
    log.info("Monitor starting (interval=%ds, vision=%s)", interval, use_vision)
    state = load_state()

    while True:
        try:
            state = check_once(state, use_vision=use_vision)
            save_state(state)
        except Exception as e:
            log.error("Unhandled error in check_once: %s", e, exc_info=True)

        if once:
            break

        log.info("Sleeping %d seconds until next check …", interval)
        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor aws-customer-security-incidents for new entries")
    parser.add_argument("--interval", type=int, default=DEFAULT_INTERVAL,
                        help="Poll interval in seconds (default: 3600)")
    parser.add_argument("--vision", action="store_true",
                        help="Enable Claude vision OCR for new incident links")
    parser.add_argument("--once", action="store_true",
                        help="Run one check then exit")
    args = parser.parse_args()

    run_monitor(interval=args.interval, use_vision=args.vision, once=args.once)
