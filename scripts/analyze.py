# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.25.0",
# ]
# ///
"""
Analyze crawled incidents against MITRE ATT&CK for Cloud using Claude.

For each incident in data/articles/, reads the crawled Markdown files and
structured metadata, then calls Claude with forced tool use to extract a
structured ATT&CK mapping.  Also generates a parameterized attack scenario
template (for use in a separate private test-harness project).

Usage:
    python scripts/analyze.py [--slug SLUG] [--reanalyze] [--workers N]
                              [--model MODEL]

    --slug       Only analyze this single incident slug
    --reanalyze  Re-analyze even if attack_analysis.json already exists
    --workers    Parallel worker threads (default: 3)
    --model      Claude model to use (default: claude-sonnet-4-6)
"""
import argparse
import json
import logging
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import anthropic

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent / "data"
ARTICLES_DIR = DATA_DIR / "articles"
ANALYSIS_DIR = DATA_DIR / "analysis"
ATTACK_DATA_PATH = DATA_DIR / "mitre_attack_cloud.json"

DEFAULT_MODEL = "claude-sonnet-4-6"
MAX_CONTEXT_CHARS = 150_000
MIN_CHARS_FOR_FULL_CONFIDENCE = 500

# ── ATT&CK extraction tool definition ────────────────────────────────────────

ATTACK_ANALYSIS_TOOL = {
    "name": "extract_attack_analysis",
    "description": (
        "Extract a structured MITRE ATT&CK mapping from a cloud security incident. "
        "Map every observable attacker action to the most specific applicable technique. "
        "Order attack_chain chronologically as the attack actually unfolded."
    ),
    "input_schema": {
        "type": "object",
        "required": [
            "tactics_used",
            "attack_chain",
            "aws_services",
            "impact_type",
            "confidence_score",
        ],
        "properties": {
            "tactics_used": {
                "type": "array",
                "description": "ATT&CK tactics observed, each with its techniques",
                "items": {
                    "type": "object",
                    "required": ["tactic_id", "tactic_name", "techniques"],
                    "properties": {
                        "tactic_id": {"type": "string", "description": "e.g. TA0001"},
                        "tactic_name": {"type": "string", "description": "e.g. Initial Access"},
                        "techniques": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["technique_id", "technique_name", "inferred"],
                                "properties": {
                                    "technique_id": {
                                        "type": "string",
                                        "description": "e.g. T1190 or T1190.001",
                                    },
                                    "technique_name": {"type": "string"},
                                    "subtechnique_id": {
                                        "type": ["string", "null"],
                                        "description": "Subtechnique ID if applicable",
                                    },
                                    "evidence_quote": {
                                        "type": ["string", "null"],
                                        "description": (
                                            "Short verbatim or near-verbatim quote from "
                                            "the source text that supports this technique"
                                        ),
                                    },
                                    "inferred": {
                                        "type": "boolean",
                                        "description": (
                                            "True if strongly implied but not explicitly "
                                            "described in the text"
                                        ),
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "attack_chain": {
                "type": "array",
                "description": (
                    "Ordered chronological sequence of attack steps. "
                    "Each step is one technique execution."
                ),
                "items": {
                    "type": "object",
                    "required": ["step", "technique_id", "technique_name", "description"],
                    "properties": {
                        "step": {"type": "integer", "minimum": 1},
                        "technique_id": {"type": "string"},
                        "technique_name": {"type": "string"},
                        "description": {
                            "type": "string",
                            "description": "Concise description of what the attacker did at this step",
                        },
                        "aws_services_involved": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "AWS/cloud service names relevant to this step",
                        },
                    },
                },
            },
            "aws_services": {
                "type": "array",
                "items": {"type": "string"},
                "description": "All AWS/cloud services involved in the incident",
            },
            "initial_access_vector": {
                "type": ["string", "null"],
                "description": "Brief description of how the attacker gained initial access",
            },
            "persistence_mechanism": {
                "type": ["string", "null"],
                "description": "How the attacker maintained access, if applicable",
            },
            "privilege_escalation": {
                "type": ["string", "null"],
                "description": "How the attacker escalated privileges, if applicable",
            },
            "impact_type": {
                "type": "string",
                "description": (
                    "Primary impact category, e.g. Data Exfiltration, Cryptomining, "
                    "Ransomware, Denial of Service, Account Takeover"
                ),
            },
            "data_exfiltrated": {
                "type": "boolean",
                "description": "Whether data was exfiltrated",
            },
            "confidence_score": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
                "description": (
                    "Your confidence in this analysis: 1.0 = rich detailed source text, "
                    "0.5 = limited text but metadata is clear, "
                    "0.2 = very sparse, mostly inferred"
                ),
            },
        },
    },
}

# ── Scenario template tool definition ────────────────────────────────────────

SCENARIO_TEMPLATE_TOOL = {
    "name": "extract_scenario_template",
    "description": (
        "Extract a parameterized attack scenario template from the incident. "
        "This will be used to procedurally generate vulnerable cloud lab environments "
        "for testing LLM-based security agents."
    ),
    "input_schema": {
        "type": "object",
        "required": [
            "display_name",
            "difficulty",
            "attack_pattern_tags",
            "aws_services_required",
            "scenario_parameters",
            "terraform_hints",
            "agent_test_objectives",
            "narrative_summary",
        ],
        "properties": {
            "display_name": {
                "type": "string",
                "description": "Short descriptive name for this attack scenario",
            },
            "difficulty": {
                "type": "string",
                "enum": ["easy", "medium", "hard", "expert"],
            },
            "attack_pattern_tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "kebab-case tags describing the attack pattern",
            },
            "aws_services_required": {
                "type": "array",
                "items": {"type": "string"},
                "description": "AWS/cloud services needed to replicate this scenario",
            },
            "scenario_parameters": {
                "type": "object",
                "description": (
                    "Key parameters that can be varied to generate different lab instances. "
                    "Keys are parameter names, values describe the parameter."
                ),
                "additionalProperties": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string"},
                        "description": {"type": "string"},
                        "default": {},
                        "parameterizable": {"type": "boolean"},
                    },
                },
            },
            "terraform_hints": {
                "type": "object",
                "properties": {
                    "modules_needed": {"type": "array", "items": {"type": "string"}},
                    "key_misconfigurations": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Specific misconfigurations to introduce",
                    },
                },
            },
            "agent_test_objectives": {
                "type": "array",
                "description": "Ordered objectives for an LLM agent attempting this scenario",
                "items": {
                    "type": "object",
                    "required": ["id", "description", "success_criteria"],
                    "properties": {
                        "id": {"type": "string"},
                        "description": {"type": "string"},
                        "success_criteria": {"type": "string"},
                    },
                },
            },
            "narrative_summary": {
                "type": "string",
                "description": "2-3 sentence plain-English summary of the attack scenario",
            },
        },
    },
}


# ── Context assembly ──────────────────────────────────────────────────────────

def _build_context(incident_dir: Path) -> tuple[str, int]:
    """
    Assemble the analysis context from metadata + crawled markdown files.

    Returns (context_text, total_chars).
    """
    parts: list[str] = []

    # High-signal structured metadata block
    meta_path = incident_dir / "metadata.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        parts.append("## Incident Metadata (structured)\n")
        for field in ("name", "date", "root_cause", "escalation_vectors", "impact"):
            val = meta.get(field)
            if val:
                parts.append(f"{field.replace('_', ' ').title()}: {val}")
        # Include links list for context
        links = meta.get("links", [])
        if links:
            parts.append(f"\nSource URLs: {', '.join(l.get('url','') for l in links[:5])}")
        parts.append("\n")

    # All crawled markdown files
    md_files = sorted(incident_dir.glob("link_*.md"))
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8").strip()
        if not text:
            continue
        parts.append(f"\n---\n## Source: {md_file.name}\n\n{text}\n")

    context = "\n".join(parts)
    total_chars = len(context)

    # Truncate if needed, always keeping the metadata block
    if total_chars > MAX_CONTEXT_CHARS:
        meta_end = context.find("## Source:")
        if meta_end == -1:
            context = context[:MAX_CONTEXT_CHARS]
        else:
            header = context[:meta_end]
            body = context[meta_end:MAX_CONTEXT_CHARS]
            context = header + body
            log.debug(
                "Truncated context from %d to %d chars for %s",
                total_chars, len(context), incident_dir.name,
            )

    return context, total_chars


# ── Validation ────────────────────────────────────────────────────────────────

def _validate_techniques(analysis: dict, known_ids: set[str]) -> dict:
    """Mark unknown technique IDs as validated=False."""
    for tactic in analysis.get("tactics_used", []):
        for tech in tactic.get("techniques", []):
            tech["validated"] = tech["technique_id"] in known_ids

    for step in analysis.get("attack_chain", []):
        step["validated"] = step["technique_id"] in known_ids

    return analysis


# ── Per-incident analysis ─────────────────────────────────────────────────────

def analyze_incident(
    incident_dir: Path,
    client: anthropic.Anthropic,
    model: str,
    attack_data: dict,
    reanalyze: bool = False,
) -> dict:
    slug = incident_dir.name
    out_dir = ANALYSIS_DIR / slug
    analysis_path = out_dir / "attack_analysis.json"
    error_path = out_dir / "attack_analysis_error.json"

    # Idempotency check
    if analysis_path.exists() and not reanalyze:
        log.info("[%s] already analyzed, skipping", slug)
        return {"slug": slug, "status": "skipped"}

    context, total_chars = _build_context(incident_dir)

    if total_chars < 50:
        log.warning("[%s] insufficient text (%d chars), skipping", slug, total_chars)
        return {"slug": slug, "status": "skipped_no_text"}

    log.info("[%s] analyzing %d chars of context", slug, total_chars)
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        # ── Step 1: ATT&CK extraction ─────────────────────────────────────
        response = client.messages.create(
            model=model,
            max_tokens=4096,
            system=(
                "You are a cloud security analyst specializing in MITRE ATT&CK for Cloud. "
                "Analyze the provided incident text and extract a precise ATT&CK mapping. "
                "Be conservative: only assert techniques with evidence in the text. "
                "Mark techniques as inferred=true if strongly implied but not explicitly described. "
                "Always order attack_chain chronologically as the attack actually unfolded. "
                "Use real ATT&CK technique IDs (e.g. T1190, T1552.005)."
            ),
            tools=[ATTACK_ANALYSIS_TOOL],
            tool_choice={"type": "tool", "name": "extract_attack_analysis"},
            messages=[{"role": "user", "content": context}],
        )

        tool_block = next(
            b for b in response.content if b.type == "tool_use"
        )
        analysis: dict = tool_block.input

        # Validate technique IDs against known cloud techniques
        known_ids = set(attack_data.get("techniques", {}).keys())
        analysis = _validate_techniques(analysis, known_ids)

        # Cap confidence for very sparse incidents
        raw_confidence = analysis.get("confidence_score", 0.5)
        if total_chars < MIN_CHARS_FOR_FULL_CONFIDENCE:
            analysis["confidence_score"] = min(raw_confidence, 0.4)

        # Add provenance fields
        analysis["schema_version"] = "1.0"
        analysis["incident_slug"] = slug
        analysis["analyzed_at"] = datetime.now(timezone.utc).isoformat()
        analysis["model"] = model
        analysis["source_chars"] = total_chars

        analysis_path.write_text(json.dumps(analysis, indent=2), encoding="utf-8")
        log.info(
            "[%s] wrote attack_analysis.json (confidence=%.2f, %d chain steps)",
            slug,
            analysis.get("confidence_score", 0),
            len(analysis.get("attack_chain", [])),
        )

        # ── Step 2: Scenario template extraction ─────────────────────────
        # Only generate for incidents with reasonable text and chain
        if total_chars >= MIN_CHARS_FOR_FULL_CONFIDENCE and analysis.get("attack_chain"):
            mitre_ids = [s["technique_id"] for s in analysis["attack_chain"]]
            scenario_prompt = (
                f"{context}\n\n"
                f"---\n\n"
                f"## Extracted ATT&CK Chain\n\n"
                + "\n".join(
                    f"Step {s['step']}: {s['technique_id']} – {s['description']}"
                    for s in analysis["attack_chain"]
                )
            )

            scenario_response = client.messages.create(
                model=model,
                max_tokens=2048,
                system=(
                    "You are designing a vulnerable-by-design cloud lab environment based on "
                    "a real security incident. Extract the key misconfigurations and attack "
                    "parameters so that a Terraform generator can reproduce a similar environment. "
                    "Focus on what was misconfigured, what services were involved, and what an "
                    "LLM agent would need to discover and exploit to succeed."
                ),
                tools=[SCENARIO_TEMPLATE_TOOL],
                tool_choice={"type": "tool", "name": "extract_scenario_template"},
                messages=[{"role": "user", "content": scenario_prompt}],
            )

            scenario_block = next(
                b for b in scenario_response.content if b.type == "tool_use"
            )
            template: dict = scenario_block.input
            template["schema_version"] = "1.0"
            template["template_id"] = slug
            template["source_incident"] = slug
            template["mitre_techniques"] = mitre_ids
            template["generated_at"] = datetime.now(timezone.utc).isoformat()

            scenario_path = out_dir / "scenario_template.json"
            scenario_path.write_text(json.dumps(template, indent=2), encoding="utf-8")
            log.info("[%s] wrote scenario_template.json", slug)

        # Clean up any prior error file
        if error_path.exists():
            error_path.unlink()

        return {"slug": slug, "status": "ok", "confidence": analysis.get("confidence_score")}

    except Exception as exc:
        log.error("[%s] analysis failed: %s", slug, exc)
        error_path.write_text(
            json.dumps({"slug": slug, "error": str(exc),
                        "failed_at": datetime.now(timezone.utc).isoformat()}, indent=2),
            encoding="utf-8",
        )
        return {"slug": slug, "status": "error", "error": str(exc)}


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Analyze crawled incidents with MITRE ATT&CK extraction"
    )
    parser.add_argument("--slug", help="Only analyze this specific incident slug")
    parser.add_argument(
        "--reanalyze",
        action="store_true",
        help="Re-analyze even if attack_analysis.json already exists",
    )
    parser.add_argument("--workers", type=int, default=3, help="Parallel workers (default: 3)")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Claude model to use (default: {DEFAULT_MODEL})",
    )
    args = parser.parse_args()

    # Load MITRE ATT&CK data for validation
    if not ATTACK_DATA_PATH.exists():
        log.error(
            "MITRE ATT&CK data not found at %s. "
            "Run scripts/fetch_attack_data.py first.",
            ATTACK_DATA_PATH,
        )
        sys.exit(1)

    attack_data = json.loads(ATTACK_DATA_PATH.read_text(encoding="utf-8"))
    log.info(
        "Loaded %d ATT&CK techniques for validation",
        len(attack_data.get("techniques", {})),
    )

    # Discover incident directories
    if not ARTICLES_DIR.exists():
        log.error("Articles directory not found at %s. Run crawl.py first.", ARTICLES_DIR)
        sys.exit(1)

    if args.slug:
        incident_dirs = [ARTICLES_DIR / args.slug]
        if not incident_dirs[0].exists():
            log.error("Incident directory not found: %s", incident_dirs[0])
            sys.exit(1)
    else:
        incident_dirs = [
            d for d in sorted(ARTICLES_DIR.iterdir())
            if d.is_dir() and (d / "metadata.json").exists()
        ]

    log.info("Found %d incidents to process", len(incident_dirs))
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

    client = anthropic.Anthropic()

    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(
                analyze_incident, d, client, args.model, attack_data, args.reanalyze
            ): d
            for d in incident_dirs
        }
        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                d = futures[future]
                log.error("Unexpected error for %s: %s", d.name, exc)

    ok = sum(1 for r in results if r["status"] == "ok")
    skipped = sum(1 for r in results if r["status"].startswith("skipped"))
    errors = sum(1 for r in results if r["status"] == "error")

    log.info(
        "Analysis complete: %d analyzed, %d skipped, %d errors (total %d)",
        ok, skipped, errors, len(results),
    )

    # Exit non-zero when every attempted analysis failed so CI surfaces the
    # problem rather than committing stale outputs and triggering a deploy.
    if errors > 0 and ok == 0:
        log.error("All analyses failed — check ANTHROPIC_API_KEY and model availability.")
        sys.exit(1)


if __name__ == "__main__":
    main()
