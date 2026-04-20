# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Audit and repair MITRE ATT&CK TTP tagging across every incident analysis.

The analyses produced by `analyze.py` occasionally place a technique under a
tactic that is NOT in that technique's canonical MITRE tactic list (see the
Cloud / IaaS matrix at https://attack.mitre.org/matrices/enterprise/cloud/iaas/).
Common failure modes:

  * A technique ID (e.g. "T1001") was written into a `tactic_id` field.
  * A technique is nested under the wrong tactic (e.g. T1530 "Data from Cloud
    Storage" tagged as Exfiltration instead of Collection; T1548 tagged as
    Lateral Movement instead of Privilege Escalation).
  * A parent technique and its subtechnique are duplicated across tactics.
  * `tactic_name` is stale / inconsistent with `tactic_id`.

This script does a pure, mechanical re-alignment pass. For each technique it
picks a canonical tactic from MITRE's `tactic_ids` list, preferring — in order
— the currently tagged tactic (if valid), the canonical tactic that also
appears elsewhere in the analysis, and finally the first canonical tactic in
kill-chain order. It then regroups `tactics_used`, rewrites every `tactic_id`
on `attack_chain_graph.nodes`, and fills canonical names.

Usage:
    python scripts/fix_ttps.py            # report + rewrite every analysis
    python scripts/fix_ttps.py --dry-run  # report only, do not write
    python scripts/fix_ttps.py --slug X   # only touch one incident
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from collections import OrderedDict
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent / "data"
ANALYSIS_DIR = DATA_DIR / "analysis"
ATTACK_DATA_PATH = DATA_DIR / "mitre_attack_cloud.json"

# Kill-chain order used to deterministically pick a canonical tactic when a
# technique has multiple (e.g. T1078 spans Initial Access → Defense Evasion).
TACTIC_EXECUTION_ORDER = [
    "TA0043",  # Reconnaissance
    "TA0042",  # Resource Development
    "TA0001",  # Initial Access
    "TA0002",  # Execution
    "TA0003",  # Persistence
    "TA0004",  # Privilege Escalation
    "TA0005",  # Defense Evasion
    "TA0006",  # Credential Access
    "TA0007",  # Discovery
    "TA0008",  # Lateral Movement
    "TA0009",  # Collection
    "TA0011",  # Command and Control
    "TA0010",  # Exfiltration
    "TA0040",  # Impact
]


def _normalize_technique_id(value: str) -> str:
    return (value or "").strip().upper().replace(" ", "")


def _pick_canonical_tactic(
    technique_id: str,
    current_tactic_id: str,
    attack_data: dict,
    in_use_tactic_ids: set[str],
) -> str | None:
    """Return the best canonical tactic_id for a technique, or None if unknown."""
    tech = attack_data.get("techniques", {}).get(technique_id)
    if not tech:
        # Fall back to the parent technique if this is a subtechnique — MITRE's
        # parent + subtechnique share the same tactic list.
        if "." in technique_id:
            tech = attack_data.get("techniques", {}).get(technique_id.split(".")[0])
    if not tech:
        return None

    canonical = [t for t in tech.get("tactic_ids", []) if t]
    if not canonical:
        return None

    # 1. Keep the current tactic if it's already canonical.
    if current_tactic_id in canonical:
        return current_tactic_id

    # 2. Prefer a canonical tactic that the incident already uses elsewhere, so
    #    we don't introduce a brand-new tactic column just to rehome one tech.
    reused = [t for t in canonical if t in in_use_tactic_ids]
    if reused:
        return sorted(reused, key=lambda t: TACTIC_EXECUTION_ORDER.index(t)
                      if t in TACTIC_EXECUTION_ORDER else 99)[0]

    # 3. Otherwise pick the earliest canonical tactic in kill-chain order.
    return sorted(canonical, key=lambda t: TACTIC_EXECUTION_ORDER.index(t)
                  if t in TACTIC_EXECUTION_ORDER else 99)[0]


def _tactic_sort_key(tactic_id: str) -> int:
    try:
        return TACTIC_EXECUTION_ORDER.index(tactic_id)
    except ValueError:
        return len(TACTIC_EXECUTION_ORDER) + 1


def _tech_list_to_flat(tactics_used: list) -> list[tuple[str, dict]]:
    """Flatten `tactics_used` into (current_tactic_id, technique_dict) pairs."""
    flat: list[tuple[str, dict]] = []
    for tactic in tactics_used or []:
        if not isinstance(tactic, dict):
            continue
        current_tactic = str(tactic.get("tactic_id", "")).strip().upper()
        for tech in tactic.get("techniques", []) or []:
            if not isinstance(tech, dict):
                continue
            tech = dict(tech)
            tech["technique_id"] = _normalize_technique_id(
                str(tech.get("technique_id", ""))
            )
            if not tech["technique_id"]:
                continue
            flat.append((current_tactic, tech))
    return flat


def realign_analysis(
    analysis: dict, attack_data: dict
) -> tuple[dict, list[dict]]:
    """Return (repaired_analysis, list_of_change_records)."""
    changes: list[dict] = []
    tactic_lookup = attack_data.get("tactics", {})
    technique_lookup = attack_data.get("techniques", {})

    flat = _tech_list_to_flat(analysis.get("tactics_used", []))
    in_use_tactic_ids = {t for t, _ in flat}

    # Group techniques by their newly-resolved canonical tactic, deduped by
    # technique_id so parent/subtechnique duplicates inside the same tactic are
    # collapsed (keeping the first occurrence).
    regrouped: "OrderedDict[str, OrderedDict[str, dict]]" = OrderedDict()
    unresolved: list[dict] = []

    for current_tactic, tech in flat:
        tid = tech["technique_id"]
        canonical_tactic = _pick_canonical_tactic(
            tid, current_tactic, attack_data, in_use_tactic_ids
        )

        if canonical_tactic is None:
            # Unknown technique — keep it under its current tactic so we don't
            # silently drop research, but flag it.
            canonical_tactic = current_tactic or "UNKNOWN"
            unresolved.append(
                {"technique_id": tid, "kept_under": canonical_tactic}
            )

        if canonical_tactic != current_tactic:
            changes.append(
                {
                    "technique_id": tid,
                    "from_tactic": current_tactic or None,
                    "to_tactic": canonical_tactic,
                }
            )

        bucket = regrouped.setdefault(canonical_tactic, OrderedDict())
        if tid in bucket:
            # Merge: keep the earlier entry, but inherit a better evidence quote
            # if the existing one is missing it.
            existing = bucket[tid]
            if not existing.get("evidence_quote") and tech.get("evidence_quote"):
                existing["evidence_quote"] = tech["evidence_quote"]
            continue

        # Canonical-ize the technique's displayed name when MITRE has one.
        canonical_name = technique_lookup.get(tid, {}).get("name")
        if canonical_name:
            tech["technique_name"] = canonical_name
        bucket[tid] = tech

    # Emit regrouped tactics_used in kill-chain order.
    new_tactics_used: list[dict] = []
    for tactic_id in sorted(regrouped.keys(), key=_tactic_sort_key):
        bucket = regrouped[tactic_id]
        tactic_name = tactic_lookup.get(tactic_id, {}).get("name") or tactic_id
        new_tactics_used.append(
            {
                "tactic_id": tactic_id,
                "tactic_name": tactic_name,
                "techniques": list(bucket.values()),
            }
        )

    analysis["tactics_used"] = new_tactics_used

    # Build tid → canonical tactic lookup for attack_chain / graph propagation.
    tid_to_tactic: dict[str, str] = {}
    for tactic in new_tactics_used:
        for tech in tactic["techniques"]:
            tid_to_tactic[tech["technique_id"]] = tactic["tactic_id"]

    # Propagate corrected tactic_id into attack_chain_graph.nodes. (The chain
    # list itself doesn't carry tactic_id, so no change needed there.)
    graph = analysis.get("attack_chain_graph")
    if isinstance(graph, dict) and isinstance(graph.get("nodes"), list):
        for node in graph["nodes"]:
            if not isinstance(node, dict):
                continue
            tid = _normalize_technique_id(str(node.get("technique_id", "")))
            if not tid:
                continue
            canonical = tid_to_tactic.get(tid) or _pick_canonical_tactic(
                tid,
                str(node.get("tactic_id", "")).strip().upper(),
                attack_data,
                set(tid_to_tactic.values()),
            )
            if canonical and canonical != node.get("tactic_id"):
                changes.append(
                    {
                        "technique_id": tid,
                        "from_tactic": node.get("tactic_id") or None,
                        "to_tactic": canonical,
                        "where": "attack_chain_graph.node",
                    }
                )
                node["tactic_id"] = canonical
            # Canonicalize technique name when MITRE provides one.
            canonical_name = technique_lookup.get(tid, {}).get("name")
            if canonical_name:
                node["technique_name"] = canonical_name

    return analysis, changes


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit and repair MITRE ATT&CK TTP tagging."
    )
    parser.add_argument(
        "--analysis-dir",
        default=str(ANALYSIS_DIR),
        help=f"Input analysis directory (default: {ANALYSIS_DIR})",
    )
    parser.add_argument(
        "--slug",
        help="Only audit this incident slug",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report changes without writing files",
    )
    parser.add_argument(
        "--report",
        default=None,
        help="Optional path to write a JSON change-report",
    )
    args = parser.parse_args()

    if not ATTACK_DATA_PATH.exists():
        log.error("Missing MITRE ATT&CK lookup: %s", ATTACK_DATA_PATH)
        return 1
    attack_data = json.loads(ATTACK_DATA_PATH.read_text(encoding="utf-8"))

    analysis_dir = Path(args.analysis_dir)
    if not analysis_dir.exists():
        log.error("Analysis directory not found: %s", analysis_dir)
        return 1

    all_changes: list[dict] = []
    touched = 0

    for slug_dir in sorted(analysis_dir.iterdir()):
        if args.slug and slug_dir.name != args.slug:
            continue
        path = slug_dir / "attack_analysis.json"
        if not path.exists():
            continue

        try:
            analysis = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            log.warning("Skipping %s (invalid JSON): %s", path, exc)
            continue

        if "tactics_used" not in analysis:
            # Error/stub file — skip.
            continue

        repaired, changes = realign_analysis(analysis, attack_data)
        if changes:
            touched += 1
            for change in changes:
                change["slug"] = slug_dir.name
            all_changes.extend(changes)
            log.info(
                "%-60s %d tactic reassignment(s)",
                slug_dir.name,
                len(changes),
            )

            if not args.dry_run:
                path.write_text(
                    json.dumps(repaired, indent=2) + "\n", encoding="utf-8"
                )

    log.info(
        "Audit complete. Touched %d incident(s), %d reassignment(s) total.",
        touched,
        len(all_changes),
    )

    if args.report:
        Path(args.report).write_text(
            json.dumps(all_changes, indent=2), encoding="utf-8"
        )
        log.info("Wrote report → %s", args.report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
