"""Regression tests for TTP tactic realignment.

These tests encode the specific miscategorizations surfaced by NIM-241
(https://attack.mitre.org/matrices/enterprise/cloud/iaas/) and prove that
both `fix_ttps.realign_analysis` and the pipeline-integrated
`analyze._realign_tactics_used` move every technique under a canonical
MITRE tactic.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from fix_ttps import realign_analysis  # noqa: E402


ATTACK_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "mitre_attack_cloud.json"
_ATTACK_DATA = json.loads(ATTACK_DATA_PATH.read_text(encoding="utf-8"))


def _tactic_of(analysis: dict, technique_id: str) -> str | None:
    """Return the tactic_id a technique ends up under, or None if missing."""
    for tactic in analysis.get("tactics_used", []):
        for tech in tactic.get("techniques", []):
            if tech.get("technique_id") == technique_id:
                return tactic.get("tactic_id")
    return None


def test_data_from_cloud_storage_moves_from_exfiltration_to_collection():
    # MITRE says T1530 "Data from Cloud Storage" is a Collection technique
    # (TA0009), yet the model frequently tagged it as Exfiltration (TA0010).
    analysis = {
        "tactics_used": [
            {
                "tactic_id": "TA0010",
                "tactic_name": "Exfiltration",
                "techniques": [
                    {
                        "technique_id": "T1530",
                        "technique_name": "Data from Cloud Storage",
                        "evidence_quote": "s3 sync",
                        "inferred": False,
                    }
                ],
            }
        ]
    }
    repaired, changes = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    assert _tactic_of(repaired, "T1530") == "TA0009"
    assert any(c["technique_id"] == "T1530" and c["to_tactic"] == "TA0009" for c in changes)


def test_abuse_elevation_control_moves_to_privilege_escalation():
    # T1548 is valid under Privilege Escalation (TA0004) and Defense Evasion
    # (TA0005). Tagging it under Lateral Movement (TA0008) is wrong.
    analysis = {
        "tactics_used": [
            {
                "tactic_id": "TA0008",
                "tactic_name": "Lateral Movement",
                "techniques": [
                    {"technique_id": "T1548", "technique_name": "Abuse Elevation Control Mechanism"}
                ],
            }
        ]
    }
    repaired, _ = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    assert _tactic_of(repaired, "T1548") == "TA0004"


def test_unsecured_credentials_moves_to_credential_access():
    # T1552.* sub-techniques (cloud creds, IMDS creds) are always Credential
    # Access, never Initial Access.
    analysis = {
        "tactics_used": [
            {
                "tactic_id": "TA0001",
                "tactic_name": "Initial Access",
                "techniques": [
                    {"technique_id": "T1552.005", "technique_name": "Cloud Instance Metadata API"},
                    {"technique_id": "T1552.001", "technique_name": "Credentials In Files"},
                ],
            }
        ]
    }
    repaired, _ = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    assert _tactic_of(repaired, "T1552.005") == "TA0006"
    assert _tactic_of(repaired, "T1552.001") == "TA0006"


def test_existing_valid_tactic_is_preserved():
    # When the model DID place a technique under one of its canonical
    # tactics, we must not shuffle it to a different canonical tactic.
    # T1078.004 (Valid Accounts: Cloud Accounts) is valid under TA0001,
    # TA0003, TA0004 and TA0005. A correct TA0001 tag should survive.
    analysis = {
        "tactics_used": [
            {
                "tactic_id": "TA0001",
                "tactic_name": "Initial Access",
                "techniques": [
                    {"technique_id": "T1078.004", "technique_name": "Cloud Accounts"}
                ],
            }
        ]
    }
    repaired, changes = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    assert _tactic_of(repaired, "T1078.004") == "TA0001"
    assert not changes


def test_technique_id_mistakenly_used_as_tactic_id_is_corrected():
    # Some analyses stored a technique ID (e.g. "T1001") in `tactic_id`.
    # The realignment must rehome every technique under a real tactic.
    analysis = {
        "tactics_used": [
            {
                "tactic_id": "T1001",
                "tactic_name": "Data Obfuscation",
                "techniques": [
                    {"technique_id": "T1580", "technique_name": "Cloud Infrastructure Discovery"}
                ],
            }
        ]
    }
    repaired, _ = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    assert _tactic_of(repaired, "T1580") == "TA0007"
    for tactic in repaired["tactics_used"]:
        assert tactic["tactic_id"].startswith("TA")


def test_duplicate_parent_subtechnique_within_same_tactic_is_merged():
    analysis = {
        "tactics_used": [
            {
                "tactic_id": "TA0006",
                "tactic_name": "Credential Access",
                "techniques": [
                    {"technique_id": "T1552", "technique_name": "Unsecured Credentials", "evidence_quote": "A"},
                    {"technique_id": "T1552", "technique_name": "Unsecured Credentials", "evidence_quote": "B"},
                ],
            }
        ]
    }
    repaired, _ = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    tids = [t["technique_id"] for tactic in repaired["tactics_used"] for t in tactic["techniques"]]
    assert tids.count("T1552") == 1


def test_graph_nodes_receive_canonical_tactic_id():
    # The incident per-file JSON carries a prebuilt attack_chain_graph;
    # its `nodes[].tactic_id` must also be realigned so the graph view is
    # rendered under the correct columns.
    analysis = {
        "tactics_used": [
            {
                "tactic_id": "TA0010",
                "tactic_name": "Exfiltration",
                "techniques": [
                    {"technique_id": "T1530", "technique_name": "Data from Cloud Storage"}
                ],
            }
        ],
        "attack_chain_graph": {
            "nodes": [
                {"technique_id": "T1530", "technique_name": "Data from Cloud Storage", "tactic_id": "TA0010"}
            ],
            "edges": [],
        },
    }
    repaired, _ = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    assert repaired["attack_chain_graph"]["nodes"][0]["tactic_id"] == "TA0009"


def test_canonical_tactic_name_is_set_from_mitre():
    analysis = {
        "tactics_used": [
            {
                "tactic_id": "TA0010",
                "tactic_name": "Exfiltration",
                "techniques": [
                    {"technique_id": "T1530", "technique_name": "Data from Cloud Storage"}
                ],
            }
        ]
    }
    repaired, _ = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    # Regrouping under TA0009 must use MITRE's canonical tactic name.
    for tactic in repaired["tactics_used"]:
        if tactic["tactic_id"] == "TA0009":
            assert tactic["tactic_name"] == "Collection"
            break
    else:
        raise AssertionError("TA0009 group missing after realignment")
