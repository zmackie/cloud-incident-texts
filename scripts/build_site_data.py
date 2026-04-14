# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Aggregate per-incident ATT&CK analysis files into static JSON files
consumed by the website.

Reads from:
    data/analysis/<slug>/attack_analysis.json
    data/mitre_attack_cloud.json

Writes to:
    data/site_data/technique_frequency.json
    data/site_data/attack_graph.json
    data/site_data/incidents_index.json
    data/site_data/incidents/<slug>.json

Usage:
    python scripts/build_site_data.py [--analysis-dir PATH] [--output-dir PATH]
"""
import argparse
import json
import logging
import sys
from collections import Counter, defaultdict
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent / "data"
ANALYSIS_DIR = DATA_DIR / "analysis"
SITE_DATA_DIR = DATA_DIR / "site_data"
ATTACK_DATA_PATH = DATA_DIR / "mitre_attack_cloud.json"


def load_analyses(analysis_dir: Path) -> list[dict]:
    """Load all valid attack_analysis.json files."""
    analyses = []
    for slug_dir in sorted(analysis_dir.iterdir()):
        path = slug_dir / "attack_analysis.json"
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            # Skip error files (they won't have tactics_used)
            if "tactics_used" not in data:
                continue
            analyses.append(data)
        except Exception as exc:
            log.warning("Could not load %s: %s", path, exc)
    log.info("Loaded %d valid analyses", len(analyses))
    return analyses


def build_technique_frequency(
    analyses: list[dict], attack_data: dict
) -> dict:
    """
    Build a map: technique_id → {count, tactic, name, incidents, tactic_id}.
    Uses the attack_chain for counting (not tactics_used) to avoid duplicates.
    """
    technique_lookup = attack_data.get("techniques", {})
    tactic_lookup = attack_data.get("tactics", {})

    freq: dict[str, dict] = {}

    for analysis in analyses:
        slug = analysis.get("incident_slug", "unknown")
        seen_in_incident: set[str] = set()

        for step in analysis.get("attack_chain", []):
            tid = step.get("technique_id", "")
            if not tid or tid in seen_in_incident:
                continue
            seen_in_incident.add(tid)

            if tid not in freq:
                # Resolve display info from ATT&CK data
                tech_info = technique_lookup.get(tid, {})
                tactic_ids = tech_info.get("tactic_ids", [])
                tactic_id = tactic_ids[0] if tactic_ids else ""
                tactic_name = ""
                if tactic_id:
                    tactic_name = tactic_lookup.get(tactic_id, {}).get("name", "")

                freq[tid] = {
                    "technique_id": tid,
                    "technique_name": tech_info.get("name", step.get("technique_name", tid)),
                    "tactic_id": tactic_id,
                    "tactic_name": tactic_name,
                    "tactic_shortname": tactic_lookup.get(tactic_id, {}).get("shortname", ""),
                    "is_subtechnique": tech_info.get("is_subtechnique", "." in tid),
                    "parent_id": tech_info.get("parent_id"),
                    "url": tech_info.get("url", f"https://attack.mitre.org/techniques/{tid.replace('.', '/')}/"),
                    "count": 0,
                    "incidents": [],
                }

            freq[tid]["count"] += 1
            freq[tid]["incidents"].append(slug)

    # Sort incidents list for determinism
    for v in freq.values():
        v["incidents"] = sorted(set(v["incidents"]))

    return freq


def build_attack_graph(analyses: list[dict], technique_freq: dict) -> dict:
    """
    Build nodes + directed edges for the attack chain graph.
    Edges represent consecutive technique transitions within incidents.
    Node size = frequency; edge weight = co-occurrence count.
    """
    edge_counts: Counter = Counter()
    edge_incidents: dict[tuple, list] = defaultdict(list)

    for analysis in analyses:
        slug = analysis.get("incident_slug", "unknown")
        chain = analysis.get("attack_chain", [])
        sorted_chain = sorted(chain, key=lambda s: s.get("step", 0))

        for i in range(len(sorted_chain) - 1):
            src = sorted_chain[i].get("technique_id", "")
            tgt = sorted_chain[i + 1].get("technique_id", "")
            if src and tgt and src != tgt:
                edge = (src, tgt)
                edge_counts[edge] += 1
                edge_incidents[edge].append(slug)

    # Nodes: all techniques that appear in at least one chain
    node_ids = set(technique_freq.keys())
    for (src, tgt) in edge_counts:
        node_ids.add(src)
        node_ids.add(tgt)

    nodes = []
    for tid in sorted(node_ids):
        info = technique_freq.get(tid, {})
        nodes.append({
            "id": tid,
            "name": info.get("technique_name", tid),
            "tactic_id": info.get("tactic_id", ""),
            "tactic_name": info.get("tactic_name", ""),
            "tactic_shortname": info.get("tactic_shortname", ""),
            "count": info.get("count", 0),
        })

    edges = []
    for (src, tgt), count in sorted(edge_counts.items(), key=lambda x: -x[1]):
        edges.append({
            "source": src,
            "target": tgt,
            "count": count,
            "incidents": sorted(set(edge_incidents[(src, tgt)])),
        })

    return {"nodes": nodes, "edges": edges}


def build_incidents_index(analyses: list[dict]) -> list[dict]:
    """Lightweight per-incident index for list/browse views."""
    index = []
    for analysis in sorted(analyses, key=lambda a: a.get("incident_slug", "")):
        slug = analysis.get("incident_slug", "unknown")

        technique_ids = list(dict.fromkeys(  # unique, preserving order
            s["technique_id"]
            for s in analysis.get("attack_chain", [])
            if s.get("technique_id")
        ))

        index.append({
            "slug": slug,
            "name": slug.replace("-", " ").title(),  # fallback display name
            "technique_ids": technique_ids,
            "aws_services": analysis.get("aws_services", []),
            "impact_type": analysis.get("impact_type", ""),
            "data_exfiltrated": analysis.get("data_exfiltrated", False),
            "confidence_score": analysis.get("confidence_score", 0),
            "analyzed_at": analysis.get("analyzed_at", ""),
        })
    return index


def write_per_incident_files(analyses: list[dict], out_dir: Path):
    """Write one JSON file per incident for detail pages."""
    incidents_dir = out_dir / "incidents"
    incidents_dir.mkdir(parents=True, exist_ok=True)

    for analysis in analyses:
        slug = analysis.get("incident_slug", "unknown")
        out_path = incidents_dir / f"{slug}.json"
        out_path.write_text(json.dumps(analysis, indent=2), encoding="utf-8")

    log.info("Wrote %d per-incident JSON files", len(analyses))


def build_stats(analyses: list[dict], technique_freq: dict) -> dict:
    """Overall statistics for the site hero section."""
    all_services: set[str] = set()
    for analysis in analyses:
        all_services.update(analysis.get("aws_services", []))

    total_chain_steps = sum(
        len(a.get("attack_chain", [])) for a in analyses
    )

    impact_counts: Counter = Counter(
        a.get("impact_type", "Unknown") for a in analyses
    )

    return {
        "total_incidents": len(analyses),
        "total_unique_techniques": len(technique_freq),
        "total_aws_services": len(all_services),
        "total_chain_steps": total_chain_steps,
        "top_techniques": [
            {"technique_id": tid, "count": v["count"], "name": v["technique_name"]}
            for tid, v in sorted(technique_freq.items(), key=lambda x: -x[1]["count"])[:10]
        ],
        "impact_breakdown": dict(impact_counts.most_common()),
        "aws_services": sorted(all_services),
    }


def main():
    parser = argparse.ArgumentParser(description="Build static site data from ATT&CK analyses")
    parser.add_argument(
        "--analysis-dir",
        default=str(ANALYSIS_DIR),
        help=f"Input analysis directory (default: {ANALYSIS_DIR})",
    )
    parser.add_argument(
        "--output-dir",
        default=str(SITE_DATA_DIR),
        help=f"Output site_data directory (default: {SITE_DATA_DIR})",
    )
    args = parser.parse_args()

    analysis_dir = Path(args.analysis_dir)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load MITRE ATT&CK lookup for enrichment
    attack_data: dict = {}
    if ATTACK_DATA_PATH.exists():
        attack_data = json.loads(ATTACK_DATA_PATH.read_text(encoding="utf-8"))
        log.info(
            "Loaded ATT&CK data: %d techniques, %d tactics",
            len(attack_data.get("techniques", {})),
            len(attack_data.get("tactics", {})),
        )
    else:
        log.warning(
            "ATT&CK data not found at %s – technique names/tactics will be minimal",
            ATTACK_DATA_PATH,
        )

    # Load all analyses
    if not analysis_dir.exists():
        log.error("Analysis directory not found: %s", analysis_dir)
        sys.exit(1)

    analyses = load_analyses(analysis_dir)
    if not analyses:
        log.warning("No analyses found. Run analyze.py first.")
        # Still write empty files so the site loads without errors
        analyses = []

    # Build all data structures
    log.info("Building technique frequency map...")
    technique_freq = build_technique_frequency(analyses, attack_data)

    log.info("Building attack graph...")
    attack_graph = build_attack_graph(analyses, technique_freq)

    log.info("Building incidents index...")
    incidents_index = build_incidents_index(analyses)

    log.info("Building stats...")
    stats = build_stats(analyses, technique_freq)

    # Also copy ATT&CK metadata (tactics + technique list for matrix structure)
    attack_meta: dict = {}
    if attack_data:
        attack_meta = {
            "tactics": attack_data.get("tactics", {}),
            "techniques": {
                tid: {
                    "id": t["id"],
                    "name": t["name"],
                    "tactic_ids": t["tactic_ids"],
                    "is_subtechnique": t["is_subtechnique"],
                    "parent_id": t["parent_id"],
                    "url": t["url"],
                }
                for tid, t in attack_data.get("techniques", {}).items()
            },
            "attack_version": attack_data.get("attack_version", ""),
        }

    # Write all output files
    files = {
        "technique_frequency.json": technique_freq,
        "attack_graph.json": attack_graph,
        "incidents_index.json": incidents_index,
        "stats.json": stats,
        "attack_meta.json": attack_meta,
    }

    for filename, data in files.items():
        path = out_dir / filename
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        log.info("Wrote %s", path)

    write_per_incident_files(analyses, out_dir)

    log.info(
        "Build complete: %d incidents, %d techniques, %d graph edges",
        len(analyses),
        len(technique_freq),
        len(attack_graph["edges"]),
    )


if __name__ == "__main__":
    main()
