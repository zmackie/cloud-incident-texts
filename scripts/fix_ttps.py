# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.25.0",
# ]
# ///
"""
Audit and repair per-step MITRE ATT&CK tactic tagging across every incident.

The core insight fixed here: a tactic describes what the attacker was DOING at a
particular step, not an intrinsic property of a technique. MITRE lists many
techniques under multiple tactics (e.g. T1078.004 "Cloud Accounts" is valid
under Initial Access, Persistence, Privilege Escalation, and Defense Evasion),
because the same technique can serve any of those goals depending on HOW it's
used in the chain.

For each incident this script:

  1. Walks every chain step and resolves its `tactic_id` (the tactic matching
     the attacker's goal at that step). If the step already carries a
     canonical tactic_id, it's kept. Otherwise we try to infer one from:
       a. A single canonical MITRE tactic (technique only has one), or
       b. The single tactic the original tactics_used nested this technique
          under (when it happens to also be canonical).
     If neither rule resolves the step, it's flagged as "ambiguous".
  2. For ambiguous steps, optionally calls Claude with the incident context +
     chain to assign tactic_ids from the technique's canonical list.
  3. Rebuilds `tactics_used` by grouping chain steps by their resolved
     tactic_id (so the same technique can appear under multiple tactics when
     used for different purposes).
  4. Rewrites `attack_chain_graph.nodes[].tactic_id` to match the chain.

Usage:
    python scripts/fix_ttps.py                # rewrite every analysis
    python scripts/fix_ttps.py --dry-run      # report only, do not write
    python scripts/fix_ttps.py --slug X       # only touch one incident
    python scripts/fix_ttps.py --no-backfill  # skip the Claude backfill step
"""
from __future__ import annotations

import argparse
import json
import logging
import os
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
ARTICLES_DIR = DATA_DIR / "articles"
ATTACK_DATA_PATH = DATA_DIR / "mitre_attack_cloud.json"

DEFAULT_BACKFILL_MODEL = "claude-sonnet-4-6"

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


def _tactic_sort_key(tactic_id: str) -> int:
    try:
        return TACTIC_EXECUTION_ORDER.index(tactic_id)
    except ValueError:
        return len(TACTIC_EXECUTION_ORDER) + 1


def _canonical_tactic_ids(technique_id: str, attack_data: dict) -> list[str]:
    """Return the MITRE-canonical tactic_ids for a technique (or its parent)."""
    technique_lookup = attack_data.get("techniques", {})
    meta = technique_lookup.get(technique_id) or (
        technique_lookup.get(technique_id.split(".")[0])
        if "." in technique_id
        else None
    )
    return list(meta.get("tactic_ids", [])) if meta else []


def _resolve_step_tactic(
    technique_id: str,
    current_tactic_id: str,
    attack_data: dict,
    original_containing_tactics: list[str],
) -> str:
    """Return the best canonical tactic_id for this step, or "" if ambiguous.

    original_containing_tactics: the list of tactic_ids the original
    tactics_used grouped this technique (or its parent) under. Used as a hint
    when the technique has multiple canonical tactics.
    """
    tid = _normalize_technique_id(technique_id)
    if not tid:
        return ""

    canonical = _canonical_tactic_ids(tid, attack_data)
    current = (current_tactic_id or "").strip().upper()

    # Rule 1: a canonical current tactic is trusted.
    if current and canonical and current in canonical:
        return current
    # Edge case: no canonical list (e.g. unknown technique) — keep current.
    if current and not canonical:
        return current

    # Rule 2: single canonical tactic → unambiguous.
    if len(canonical) == 1:
        return canonical[0]

    # Rule 3: exactly one original tactic contained this technique and it's
    # canonical.
    canonical_hits = [
        t for t in original_containing_tactics if t in canonical
    ] if canonical else list(original_containing_tactics)
    unique_hits = list(dict.fromkeys(canonical_hits))
    if len(unique_hits) == 1:
        return unique_hits[0]

    return ""


def _original_tactics_by_technique(original_tactics_used: list) -> dict[str, list[str]]:
    """Map (technique_id OR parent) → list of tactic_ids it was nested under."""
    mapping: dict[str, list[str]] = {}
    for tactic in original_tactics_used or []:
        if not isinstance(tactic, dict):
            continue
        tactic_id = str(tactic.get("tactic_id", "")).strip().upper()
        if not tactic_id:
            continue
        for tech in tactic.get("techniques", []) or []:
            if not isinstance(tech, dict):
                continue
            tid = _normalize_technique_id(str(tech.get("technique_id", "")))
            if not tid:
                continue
            mapping.setdefault(tid, []).append(tactic_id)
            if "." in tid:
                parent = tid.split(".")[0]
                mapping.setdefault(parent, []).append(tactic_id)
    # Dedupe while preserving order.
    return {k: list(dict.fromkeys(v)) for k, v in mapping.items()}


def _synthesize_chain_from_tactics(original_tactics_used: list) -> list[dict]:
    """Build a synthetic chain from tactics_used (for analyses missing one)."""
    synthetic: list[dict] = []
    step = 0
    for tactic in original_tactics_used or []:
        if not isinstance(tactic, dict):
            continue
        tactic_id = str(tactic.get("tactic_id", "")).strip().upper()
        for tech in tactic.get("techniques", []) or []:
            if not isinstance(tech, dict):
                continue
            tid = _normalize_technique_id(str(tech.get("technique_id", "")))
            if not tid:
                continue
            step += 1
            synthetic.append(
                {
                    "step": step,
                    "technique_id": tid,
                    "technique_name": tech.get("technique_name", tid),
                    "tactic_id": tactic_id,
                    "evidence_quote": tech.get("evidence_quote"),
                    "synthetic_from_tactics_used": True,
                }
            )
    return synthetic


def _rebuild_tactics_used_from_chain(
    chain: list[dict], attack_data: dict
) -> list[dict]:
    """Group chain steps by resolved tactic_id into a fresh tactics_used list."""
    technique_lookup = attack_data.get("techniques", {})
    tactic_lookup = attack_data.get("tactics", {})

    buckets: "OrderedDict[str, OrderedDict[str, dict]]" = OrderedDict()
    for step in chain:
        if not isinstance(step, dict):
            continue
        tid = _normalize_technique_id(str(step.get("technique_id", "")))
        tactic_id = (str(step.get("tactic_id", "")) or "").strip().upper()
        if not tid or not tactic_id:
            continue
        bucket = buckets.setdefault(tactic_id, OrderedDict())
        if tid not in bucket:
            canonical_name = (
                technique_lookup.get(tid, {}).get("name")
                or step.get("technique_name")
                or tid
            )
            entry: dict = {
                "technique_id": tid,
                "technique_name": canonical_name,
                "inferred": False,
                "evidence_quote": step.get("evidence_quote"),
                "validated": bool(technique_lookup.get(tid)),
            }
            if "." in tid:
                entry["subtechnique_id"] = tid
            bucket[tid] = entry
        else:
            if not bucket[tid].get("evidence_quote") and step.get("evidence_quote"):
                bucket[tid]["evidence_quote"] = step.get("evidence_quote")

    out: list[dict] = []
    for tactic_id in sorted(buckets.keys(), key=_tactic_sort_key):
        out.append(
            {
                "tactic_id": tactic_id,
                "tactic_name": tactic_lookup.get(tactic_id, {}).get("name")
                or tactic_id,
                "techniques": list(buckets[tactic_id].values()),
            }
        )
    return out


def _update_graph_node_tactics(
    analysis: dict, chain: list[dict], attack_data: dict
) -> list[dict]:
    """Copy per-step tactic_ids into attack_chain_graph.nodes. Return changes."""
    changes: list[dict] = []
    technique_lookup = attack_data.get("techniques", {})

    step_by_no: dict[int, dict] = {}
    tech_to_tactic: dict[str, str] = {}
    for s in chain:
        if isinstance(s, dict):
            n = s.get("step")
            if isinstance(n, int):
                step_by_no[n] = s
            tid_s = _normalize_technique_id(str(s.get("technique_id", "")))
            t_s = (str(s.get("tactic_id", "")) or "").strip().upper()
            if tid_s and t_s and tid_s not in tech_to_tactic:
                tech_to_tactic[tid_s] = t_s

    graph = analysis.get("attack_chain_graph")
    if not isinstance(graph, dict) or not isinstance(graph.get("nodes"), list):
        return changes

    for node in graph["nodes"]:
        if not isinstance(node, dict):
            continue
        tid = _normalize_technique_id(str(node.get("technique_id", "")))
        if not tid:
            continue
        step_no = node.get("step")
        new_tactic = ""
        if isinstance(step_no, int) and step_no in step_by_no:
            new_tactic = (
                str(step_by_no[step_no].get("tactic_id", "") or "").strip().upper()
            )
        if not new_tactic:
            new_tactic = tech_to_tactic.get(tid) or tech_to_tactic.get(
                tid.split(".")[0] if "." in tid else tid, ""
            )
        old_tactic = str(node.get("tactic_id", "") or "").strip().upper()
        if new_tactic and new_tactic != old_tactic:
            changes.append(
                {
                    "technique_id": tid,
                    "from_tactic": old_tactic or None,
                    "to_tactic": new_tactic,
                    "where": "attack_chain_graph.node",
                }
            )
            node["tactic_id"] = new_tactic
        elif not new_tactic and old_tactic:
            changes.append(
                {
                    "technique_id": tid,
                    "from_tactic": old_tactic or None,
                    "to_tactic": "",
                    "where": "attack_chain_graph.node",
                }
            )
            node["tactic_id"] = ""
        canonical_name = technique_lookup.get(tid, {}).get("name")
        if canonical_name:
            node["technique_name"] = canonical_name

    return changes


def realign_analysis(
    analysis: dict, attack_data: dict
) -> tuple[dict, list[dict]]:
    """Resolve per-step tactic_ids and rebuild tactics_used from the chain.

    Returns (repaired_analysis, list_of_change_records). When the analysis
    has no attack_chain, a synthetic chain is built from tactics_used so the
    same resolution logic applies uniformly.
    """
    changes: list[dict] = []

    original_tactics_used = list(analysis.get("tactics_used", []) or [])
    containing_map = _original_tactics_by_technique(original_tactics_used)

    # Prefer the real chain; synthesize one from tactics_used if absent.
    raw_chain = analysis.get("attack_chain")
    synthesized = False
    if isinstance(raw_chain, list) and raw_chain:
        chain = raw_chain
    else:
        chain = _synthesize_chain_from_tactics(original_tactics_used)
        synthesized = True

    # Resolve each step's tactic_id.
    for step in chain:
        if not isinstance(step, dict):
            continue
        tid = _normalize_technique_id(str(step.get("technique_id", "")))
        if not tid:
            continue
        current = (str(step.get("tactic_id", "")) or "").strip().upper()
        containing = containing_map.get(tid) or containing_map.get(
            tid.split(".")[0] if "." in tid else tid, []
        )
        resolved = _resolve_step_tactic(tid, current, attack_data, containing)
        step["tactic_id"] = resolved

        if resolved != current:
            changes.append(
                {
                    "technique_id": tid,
                    "from_tactic": current or None,
                    "to_tactic": resolved or None,
                    "where": "attack_chain.step" if not synthesized else "tactics_used",
                    "step": step.get("step"),
                }
            )

    if not synthesized:
        analysis["attack_chain"] = chain

    # Rebuild tactics_used from the (possibly synthetic) resolved chain.
    rebuilt = _rebuild_tactics_used_from_chain(chain, attack_data)
    analysis["tactics_used"] = rebuilt

    # Propagate per-step tactic_id into graph nodes. Works for both real and
    # synthesized chains; for synthesized chains the match falls back to
    # technique_id since node.step won't align with the synthetic numbering.
    changes.extend(_update_graph_node_tactics(analysis, chain, attack_data))

    return analysis, changes


# ── Ambiguous-step backfill via Claude ────────────────────────────────────────

def _flagged_steps_for_backfill(
    analysis: dict, attack_data: dict
) -> list[dict]:
    """Return chain steps whose tactic_id is still empty after realignment."""
    flagged: list[dict] = []
    for step in analysis.get("attack_chain", []) or []:
        if not isinstance(step, dict):
            continue
        tid = _normalize_technique_id(str(step.get("technique_id", "")))
        if not tid:
            continue
        if str(step.get("tactic_id", "") or "").strip():
            continue
        canonical = _canonical_tactic_ids(tid, attack_data)
        if len(canonical) <= 1:
            # Already resolvable — shouldn't reach here, but don't backfill.
            continue
        flagged.append(step)
    return flagged


def _backfill_tool_schema(canonical_by_step: dict[int, list[str]]) -> dict:
    return {
        "name": "assign_step_tactics",
        "description": (
            "Assign a MITRE ATT&CK tactic_id to each provided attack_chain step. "
            "Each tactic_id must be drawn from the allowed_tactics list for that "
            "step (the technique's canonical MITRE tactic_ids)."
        ),
        "input_schema": {
            "type": "object",
            "required": ["assignments"],
            "properties": {
                "assignments": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["step", "tactic_id"],
                        "properties": {
                            "step": {"type": "integer"},
                            "tactic_id": {"type": "string"},
                            "rationale": {"type": "string"},
                        },
                    },
                }
            },
        },
    }


def _load_incident_sources(slug: str, max_chars: int = 40_000) -> str:
    """Pull in article markdown + metadata for the incident, truncated."""
    inc_dir = ARTICLES_DIR / slug
    parts: list[str] = []
    meta_path = inc_dir / "metadata.json"
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            for field in ("name", "date", "root_cause", "escalation_vectors", "impact"):
                v = meta.get(field)
                if v:
                    parts.append(f"{field}: {v}")
        except Exception:
            pass
    if inc_dir.exists():
        for md in sorted(inc_dir.glob("link_*.md")):
            try:
                parts.append(f"\n--- {md.name} ---\n{md.read_text(encoding='utf-8')}")
            except Exception:
                continue
    ctx = "\n".join(parts)
    return ctx[:max_chars]


def _backfill_via_claude(
    analysis: dict,
    flagged: list[dict],
    attack_data: dict,
    client,
    model: str,
) -> list[dict]:
    """Ask Claude to assign a canonical tactic_id to each flagged step.

    Returns a list of change records describing what was resolved.
    """
    slug = analysis.get("incident_slug", "unknown")
    source_ctx = _load_incident_sources(slug)
    chain = analysis.get("attack_chain", [])

    chain_summary_lines = []
    for s in chain:
        if not isinstance(s, dict):
            continue
        n = s.get("step")
        tid = s.get("technique_id", "")
        name = s.get("technique_name", tid)
        tactic = s.get("tactic_id") or "(unassigned)"
        desc = s.get("description", "")
        chain_summary_lines.append(
            f"  Step {n}: {tid} {name} [tactic={tactic}] — {desc}"
        )
    chain_summary = "\n".join(chain_summary_lines)

    allowed_per_step: dict[int, list[str]] = {}
    prompt_sections: list[str] = []
    for step in flagged:
        n = step.get("step")
        tid = step.get("technique_id", "")
        name = step.get("technique_name", tid)
        desc = step.get("description", "")
        quote = step.get("evidence_quote") or ""
        canonical = _canonical_tactic_ids(tid, attack_data)
        allowed_per_step[n] = canonical
        tactic_names = [
            f"{t} ({attack_data.get('tactics', {}).get(t, {}).get('name', '')})"
            for t in canonical
        ]
        prompt_sections.append(
            f"Step {n}: {tid} {name}\n"
            f"  description: {desc}\n"
            f"  evidence_quote: {quote}\n"
            f"  allowed_tactics: {', '.join(tactic_names)}"
        )

    user_message = (
        f"Incident slug: {slug}\n\n"
        f"Source material (truncated):\n{source_ctx}\n\n"
        f"Full attack chain (for context):\n{chain_summary}\n\n"
        f"Assign a tactic_id to each of these ambiguous steps. The tactic_id "
        f"MUST come from allowed_tactics (the technique's canonical MITRE "
        f"tactic list). Pick the one that matches the attacker's goal AT THAT "
        f"STEP, based on the chain context and evidence. Remember: a tactic "
        f"describes WHAT THE ATTACKER WAS DOING, not an intrinsic property of "
        f"the technique.\n\n"
        f"Steps needing a tactic_id:\n\n" + "\n\n".join(prompt_sections)
    )

    system = (
        "You are a MITRE ATT&CK analyst. For each flagged attack-chain step, "
        "assign the canonical tactic_id that matches what the attacker was "
        "doing at that step. Only choose from allowed_tactics for each step."
    )

    response = client.messages.create(
        model=model,
        max_tokens=2048,
        system=system,
        tools=[_backfill_tool_schema(allowed_per_step)],
        tool_choice={"type": "tool", "name": "assign_step_tactics"},
        messages=[{"role": "user", "content": user_message}],
    )

    tool_block = next((b for b in response.content if b.type == "tool_use"), None)
    if tool_block is None:
        return []
    assignments = tool_block.input.get("assignments", [])
    changes: list[dict] = []
    step_by_no = {s.get("step"): s for s in chain if isinstance(s, dict)}

    for a in assignments:
        n = a.get("step")
        new_tactic = str(a.get("tactic_id", "") or "").strip().upper()
        step = step_by_no.get(n)
        if not isinstance(step, dict) or not new_tactic:
            continue
        tid = _normalize_technique_id(str(step.get("technique_id", "")))
        canonical = _canonical_tactic_ids(tid, attack_data)
        if canonical and new_tactic not in canonical:
            log.warning(
                "[%s] backfill returned non-canonical tactic %s for step %s (%s); dropping",
                slug, new_tactic, n, tid,
            )
            continue
        step["tactic_id"] = new_tactic
        changes.append(
            {
                "technique_id": tid,
                "from_tactic": None,
                "to_tactic": new_tactic,
                "where": "attack_chain.step",
                "step": n,
                "source": "claude_backfill",
            }
        )
    return changes


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit and repair per-step MITRE ATT&CK tactic tagging."
    )
    parser.add_argument(
        "--analysis-dir",
        default=str(ANALYSIS_DIR),
        help=f"Input analysis directory (default: {ANALYSIS_DIR})",
    )
    parser.add_argument("--slug", help="Only audit this incident slug")
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
    parser.add_argument(
        "--no-backfill",
        action="store_true",
        help="Skip Claude backfill for ambiguous steps",
    )
    parser.add_argument(
        "--backfill-model",
        default=DEFAULT_BACKFILL_MODEL,
        help=f"Model used for ambiguous-step backfill (default: {DEFAULT_BACKFILL_MODEL})",
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

    client = None
    if not args.no_backfill:
        if not os.environ.get("ANTHROPIC_API_KEY"):
            log.warning(
                "ANTHROPIC_API_KEY not set; ambiguous steps will be left "
                "unassigned. Pass --no-backfill to silence this warning."
            )
        else:
            try:
                import anthropic  # type: ignore

                client = anthropic.Anthropic()
            except Exception as exc:  # pragma: no cover - defensive
                log.warning("Failed to init Anthropic client: %s", exc)

    all_changes: list[dict] = []
    touched = 0
    backfilled = 0

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

        if "tactics_used" not in analysis and "attack_chain" not in analysis:
            continue

        if "incident_slug" not in analysis:
            analysis["incident_slug"] = slug_dir.name

        repaired, changes = realign_analysis(analysis, attack_data)

        # Optional backfill for still-ambiguous steps.
        if client is not None and not args.dry_run:
            flagged = _flagged_steps_for_backfill(repaired, attack_data)
            if flagged:
                log.info(
                    "[%s] backfilling %d ambiguous step(s) via Claude",
                    slug_dir.name, len(flagged),
                )
                try:
                    backfill_changes = _backfill_via_claude(
                        repaired, flagged, attack_data, client, args.backfill_model
                    )
                except Exception as exc:
                    log.warning(
                        "[%s] backfill failed: %s (leaving steps unassigned)",
                        slug_dir.name, exc,
                    )
                    backfill_changes = []
                if backfill_changes:
                    backfilled += len(backfill_changes)
                    changes.extend(backfill_changes)
                    # Rebuild tactics_used + graph after backfill filled gaps.
                    repaired["tactics_used"] = _rebuild_tactics_used_from_chain(
                        repaired.get("attack_chain", []), attack_data
                    )
                    _update_graph_node_tactics(
                        repaired, repaired.get("attack_chain", []), attack_data
                    )

        if changes:
            touched += 1
            for c in changes:
                c["slug"] = slug_dir.name
            all_changes.extend(changes)
            log.info(
                "%-60s %d tactic change(s)",
                slug_dir.name,
                len(changes),
            )
            if not args.dry_run:
                path.write_text(
                    json.dumps(repaired, indent=2) + "\n", encoding="utf-8"
                )

    log.info(
        "Audit complete. Touched %d incident(s), %d change(s) total, %d via backfill.",
        touched, len(all_changes), backfilled,
    )

    if args.report:
        Path(args.report).write_text(
            json.dumps(all_changes, indent=2), encoding="utf-8"
        )
        log.info("Wrote report → %s", args.report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
