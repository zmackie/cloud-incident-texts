# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests>=2.31.0",
# ]
# ///
"""
Fetch the MITRE ATT&CK Enterprise STIX bundle and extract cloud-relevant
techniques and tactics into a lean lookup file.

Usage:
    python scripts/fetch_attack_data.py [--output PATH] [--force]

    --output  Path to write the output JSON (default: data/mitre_attack_cloud.json)
    --force   Re-fetch even if the output file already exists
"""
import argparse
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

STIX_URL = (
    "https://raw.githubusercontent.com/mitre/cti/master/"
    "enterprise-attack/enterprise-attack.json"
)

# Platforms we consider "cloud-relevant"
CLOUD_PLATFORMS = {"AWS", "Azure", "GCP", "IaaS", "SaaS", "Office 365",
                   "Google Workspace", "Azure AD", "Containers"}

DATA_DIR = Path(__file__).parent.parent / "data"


def fetch_stix(url: str) -> dict:
    log.info("Fetching STIX bundle from %s", url)
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    log.info("Downloaded %.1f MB", len(resp.content) / 1_048_576)
    return resp.json()


def _tactic_shortname(name: str) -> str:
    return name.lower().replace(" ", "-")


def parse_stix(bundle: dict) -> dict:
    """Parse the STIX bundle into a lean cloud-focused lookup."""
    objects = bundle.get("objects", [])
    log.info("Parsing %d STIX objects", len(objects))

    # ── tactics ──────────────────────────────────────────────────────────────
    tactics: dict[str, dict] = {}
    for obj in objects:
        if obj.get("type") != "x-mitre-tactic":
            continue
        ext = obj.get("x_mitre_shortname", "")
        tactic_id = ""
        for ref in obj.get("external_references", []):
            if ref.get("source_name") == "mitre-attack":
                tactic_id = ref.get("external_id", "")
                break
        if tactic_id:
            tactics[tactic_id] = {
                "id": tactic_id,
                "name": obj["name"],
                "shortname": ext or _tactic_shortname(obj["name"]),
                "description": obj.get("description", "")[:300],
            }

    log.info("Found %d tactics", len(tactics))

    # Map shortname → tactic_id for kill chain lookup
    shortname_to_id = {v["shortname"]: k for k, v in tactics.items()}

    # ── techniques ───────────────────────────────────────────────────────────
    techniques: dict[str, dict] = {}
    skipped = 0
    for obj in objects:
        if obj.get("type") != "attack-pattern":
            continue
        if obj.get("x_mitre_deprecated") or obj.get("revoked"):
            continue

        platforms: set[str] = set(obj.get("x_mitre_platforms", []))
        if not platforms & CLOUD_PLATFORMS:
            skipped += 1
            continue

        technique_id = ""
        url_ref = ""
        for ref in obj.get("external_references", []):
            if ref.get("source_name") == "mitre-attack":
                technique_id = ref.get("external_id", "")
                url_ref = ref.get("url", "")
                break
        if not technique_id:
            continue

        # Resolve tactic IDs from kill chain phases
        tactic_ids: list[str] = []
        tactic_names: list[str] = []
        for phase in obj.get("kill_chain_phases", []):
            if phase.get("kill_chain_name") == "mitre-attack":
                sn = phase.get("phase_name", "")
                tid = shortname_to_id.get(sn)
                if tid:
                    tactic_ids.append(tid)
                    tactic_names.append(tactics[tid]["name"])

        is_subtechnique = "." in technique_id
        parent_id = technique_id.split(".")[0] if is_subtechnique else None

        techniques[technique_id] = {
            "id": technique_id,
            "name": obj["name"],
            "description": obj.get("description", "")[:500],
            "tactic_ids": tactic_ids,
            "tactic_names": tactic_names,
            "platforms": sorted(platforms),
            "is_subtechnique": is_subtechnique,
            "parent_id": parent_id,
            "url": url_ref,
        }

    log.info(
        "Kept %d cloud-relevant techniques (skipped %d non-cloud)",
        len(techniques), skipped,
    )

    # Determine ATT&CK version from bundle metadata
    version = "unknown"
    for obj in objects:
        if obj.get("type") == "x-mitre-collection":
            version = obj.get("x_mitre_version", "unknown")
            break

    return {
        "techniques": techniques,
        "tactics": tactics,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "attack_version": version,
        "source_url": STIX_URL,
        "cloud_platforms": sorted(CLOUD_PLATFORMS),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Fetch MITRE ATT&CK cloud technique data"
    )
    parser.add_argument(
        "--output",
        default=str(DATA_DIR / "mitre_attack_cloud.json"),
        help="Output path (default: data/mitre_attack_cloud.json)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-fetch even if output already exists",
    )
    args = parser.parse_args()

    out_path = Path(args.output)
    if out_path.exists() and not args.force:
        log.info("Output already exists at %s (use --force to re-fetch)", out_path)
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)
    bundle = fetch_stix(STIX_URL)
    data = parse_stix(bundle)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    log.info(
        "Wrote %d techniques + %d tactics to %s",
        len(data["techniques"]),
        len(data["tactics"]),
        out_path,
    )


if __name__ == "__main__":
    main()
