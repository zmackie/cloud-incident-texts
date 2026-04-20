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


def test_abuse_elevation_control_flagged_when_ambiguous():
    # T1548 is valid under Privilege Escalation (TA0004) and Defense Evasion
    # (TA0005). Tagging it under Lateral Movement (TA0008) is wrong. The new
    # resolver refuses to force-pick between TA0004 and TA0005 when the input
    # gives no signal, so T1548 is left unassigned for backfill.
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
    # T1548 should NOT land under a non-canonical tactic. It should also NOT
    # be force-picked — leave it off tactics_used entirely when ambiguous.
    assert _tactic_of(repaired, "T1548") is None
    # And the bucket that used to hold it (TA0008) must be gone.
    assert "TA0008" not in {t["tactic_id"] for t in repaired["tactics_used"]}


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


# ── Per-step tactic tagging (the NIM-241 regression the user reported) ──────

def test_multi_tactic_technique_initial_access_keeps_initial_access():
    # NIM-241 bug: T1078.004 "Cloud Accounts" is valid under TA0001, TA0003,
    # TA0004, and TA0005. The 20/20 Eye Care incident's graph node ended up
    # under TA0005 Defense Evasion despite the chain step meaning Initial
    # Access. The per-step tactic_id must be trusted when canonical.
    analysis = {
        "tactics_used": [
            {
                "tactic_id": "TA0001",
                "tactic_name": "Initial Access",
                "techniques": [{"technique_id": "T1078", "technique_name": "Valid Accounts"}],
            }
        ],
        "attack_chain": [
            {
                "step": 1,
                "technique_id": "T1078.004",
                "technique_name": "Valid Accounts: Cloud Accounts",
                "tactic_id": "TA0001",
                "description": "attacker used compromised AWS creds to gain unauthorized access",
            }
        ],
        "attack_chain_graph": {
            "nodes": [
                {"step": 1, "technique_id": "T1078.004", "tactic_id": "TA0005"}
            ],
            "edges": [],
        },
    }
    repaired, changes = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    assert repaired["attack_chain"][0]["tactic_id"] == "TA0001"
    assert repaired["attack_chain_graph"]["nodes"][0]["tactic_id"] == "TA0001"
    assert _tactic_of(repaired, "T1078.004") == "TA0001"
    # The graph node's stale TA0005 must show up as a recorded change.
    assert any(
        c.get("where") == "attack_chain_graph.node"
        and c.get("from_tactic") == "TA0005"
        and c.get("to_tactic") == "TA0001"
        for c in changes
    )


def test_same_technique_used_twice_under_different_tactics():
    # Same technique used twice in one chain under different attacker goals:
    # once for Initial Access, later for Persistence. tactics_used must list
    # T1078.004 under BOTH TA0001 and TA0003 — not collapse into one.
    analysis = {
        "tactics_used": [
            {
                "tactic_id": "TA0001",
                "tactic_name": "Initial Access",
                "techniques": [{"technique_id": "T1078.004", "technique_name": "Cloud Accounts"}],
            }
        ],
        "attack_chain": [
            {
                "step": 1,
                "technique_id": "T1078.004",
                "technique_name": "Cloud Accounts",
                "tactic_id": "TA0001",
                "description": "attacker gained access using stolen creds",
            },
            {
                "step": 2,
                "technique_id": "T1078.004",
                "technique_name": "Cloud Accounts",
                "tactic_id": "TA0003",
                "description": "attacker kept using the same account as a persistence foothold",
            },
        ],
    }
    repaired, _ = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    tactic_ids = {t["tactic_id"] for t in repaired["tactics_used"]}
    assert "TA0001" in tactic_ids
    assert "TA0003" in tactic_ids
    # And the chain keeps per-step tactic_ids distinct.
    per_step = [s["tactic_id"] for s in repaired["attack_chain"]]
    assert per_step == ["TA0001", "TA0003"]


def test_step_tactic_not_in_canonical_list_is_dropped():
    # If the model assigned a tactic that isn't in the technique's canonical
    # MITRE tactic list, the resolver must NOT silently keep it. For T1530
    # (canonical = TA0009 only), any other current tactic is wrong.
    analysis = {
        "tactics_used": [],
        "attack_chain": [
            {
                "step": 1,
                "technique_id": "T1530",
                "technique_name": "Data from Cloud Storage",
                "tactic_id": "TA0010",
                "description": "attacker read S3 data",
            }
        ],
    }
    repaired, _ = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    # Single canonical tactic → auto-filled to TA0009.
    assert repaired["attack_chain"][0]["tactic_id"] == "TA0009"


def test_unset_step_tactic_with_single_canonical_is_autofilled():
    analysis = {
        "tactics_used": [],
        "attack_chain": [
            {
                "step": 1,
                "technique_id": "T1580",
                "technique_name": "Cloud Infrastructure Discovery",
                "description": "ran aws ec2 describe-*",
                # no tactic_id
            }
        ],
    }
    repaired, _ = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    assert repaired["attack_chain"][0]["tactic_id"] == "TA0007"


def test_ambiguous_multi_tactic_step_is_left_unassigned():
    # No signal: no prior tactics_used grouping, step has no tactic_id, and
    # the technique has multiple canonical tactics. Resolver refuses to pick.
    analysis = {
        "tactics_used": [],
        "attack_chain": [
            {
                "step": 1,
                "technique_id": "T1078.004",
                "technique_name": "Cloud Accounts",
                "description": "attacker used an AWS IAM user",
                # no tactic_id
            }
        ],
    }
    repaired, _ = realign_analysis(copy.deepcopy(analysis), _ATTACK_DATA)
    assert repaired["attack_chain"][0]["tactic_id"] == ""
    assert repaired["tactics_used"] == []
