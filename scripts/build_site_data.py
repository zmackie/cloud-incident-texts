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
    site/public/data/technique_frequency.json
    site/public/data/attack_graph.json
    site/public/data/incidents_index.json
    site/public/data/incidents/<slug>.json

Usage:
    python scripts/build_site_data.py [--analysis-dir PATH] [--output-dir PATH]
"""
import argparse
import json
import logging
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize import canonical_impact, canonical_services  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent / "data"
ANALYSIS_DIR = DATA_DIR / "analysis"
SITE_DATA_DIR = Path(__file__).parent.parent / "site" / "public" / "data"
ATTACK_DATA_PATH = DATA_DIR / "mitre_attack_cloud.json"
ARTICLES_DIR = DATA_DIR / "articles"


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
    The display tactic is the most common per-step tactic observed for this
    technique across the corpus, so multi-tactic techniques (e.g. T1078.004)
    are shown under the tactic they're actually used for — not whatever tactic
    happens to sort first in MITRE's STIX output.
    """
    technique_lookup = attack_data.get("techniques", {})
    tactic_lookup = attack_data.get("tactics", {})

    freq: dict[str, dict] = {}
    # technique_id → Counter of per-step tactic_ids observed in the corpus.
    per_step_tactic_counts: dict[str, Counter] = defaultdict(Counter)

    for analysis in analyses:
        slug = analysis.get("incident_slug", "unknown")
        seen_in_incident: set[str] = set()

        for step in analysis.get("attack_chain", []):
            tid = step.get("technique_id", "")
            if not tid:
                continue
            step_tactic = str(step.get("tactic_id", "") or "").strip().upper()
            if step_tactic:
                per_step_tactic_counts[tid][step_tactic] += 1

            if tid in seen_in_incident:
                continue
            seen_in_incident.add(tid)

            if tid not in freq:
                tech_info = technique_lookup.get(tid, {})
                freq[tid] = {
                    "technique_id": tid,
                    "technique_name": tech_info.get("name", step.get("technique_name", tid)),
                    "tactic_id": "",
                    "tactic_name": "",
                    "tactic_shortname": "",
                    "is_subtechnique": tech_info.get("is_subtechnique", "." in tid),
                    "parent_id": tech_info.get("parent_id"),
                    "url": tech_info.get("url", f"https://attack.mitre.org/techniques/{tid.replace('.', '/')}/"),
                    "count": 0,
                    "incidents": [],
                }

            freq[tid]["count"] += 1
            freq[tid]["incidents"].append(slug)

    # Resolve display tactic for each technique: most common per-step tactic
    # observed. Fall back to MITRE's canonical list when nothing was observed.
    for tid, entry in freq.items():
        tech_info = technique_lookup.get(tid, {})
        display_tactic = ""
        counter = per_step_tactic_counts.get(tid)
        if counter:
            display_tactic = counter.most_common(1)[0][0]
        if not display_tactic:
            tactic_ids = tech_info.get("tactic_ids", [])
            display_tactic = tactic_ids[0] if tactic_ids else ""
        entry["tactic_id"] = display_tactic
        entry["tactic_name"] = tactic_lookup.get(display_tactic, {}).get("name", "") if display_tactic else ""
        entry["tactic_shortname"] = tactic_lookup.get(display_tactic, {}).get("shortname", "") if display_tactic else ""

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
    edge_evidence: dict[tuple, list] = defaultdict(list)

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
                for quote in (
                    sorted_chain[i].get("evidence_quote"),
                    sorted_chain[i + 1].get("evidence_quote"),
                ):
                    if isinstance(quote, str) and quote.strip():
                        edge_evidence[edge].append(quote.strip())

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
            "evidence_quotes": sorted(set(edge_evidence[(src, tgt)]))[:2],
        })

    return {"nodes": nodes, "edges": edges}


def _load_article_metadata(slug: str) -> dict:
    path = ARTICLES_DIR / slug / "metadata.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def build_incidents_index(analyses: list[dict]) -> list[dict]:
    """Lightweight per-incident index for list/browse views."""
    index = []
    for analysis in sorted(analyses, key=lambda a: a.get("incident_slug", "")):
        slug = analysis.get("incident_slug", "unknown")
        meta = _load_article_metadata(slug)

        technique_ids = list(dict.fromkeys(  # unique, preserving order
            s["technique_id"]
            for s in analysis.get("attack_chain", [])
            if s.get("technique_id")
        ))

        raw_impact = analysis.get("impact_type", "")
        raw_services = analysis.get("aws_services", [])
        index.append({
            "slug": slug,
            "name": meta.get("name") or slug.replace("-", " ").title(),  # fallback display name
            "technique_ids": technique_ids,
            "aws_services": canonical_services(raw_services),
            "aws_services_raw": list(raw_services or []),
            "impact_type": canonical_impact(raw_impact),
            "impact_type_raw": raw_impact,
            "initial_access_vector": analysis.get("initial_access_vector", ""),
            "event_date": meta.get("date", ""),
            "data_exfiltrated": analysis.get("data_exfiltrated", False),
            "confidence_score": analysis.get("confidence_score", 0),
            "analyzed_at": analysis.get("analyzed_at", ""),
        })
    return index


def build_catalog(incidents_index: list[dict]) -> dict:
    """Grouped catalog views for navigation."""
    by_impact: dict[str, list[dict]] = defaultdict(list)
    by_initial_access: dict[str, list[dict]] = defaultdict(list)
    by_year: dict[str, list[dict]] = defaultdict(list)

    for inc in incidents_index:
        by_impact[inc.get("impact_type") or "Unknown"].append(inc)
        by_initial_access[inc.get("initial_access_vector") or "Unknown"].append(inc)
        date_value = str(inc.get("event_date", "")).strip()
        year = date_value[:4] if len(date_value) >= 4 and date_value[:4].isdigit() else "Unknown"
        by_year[year].append(inc)

    def _sort_groups(groups: dict[str, list[dict]]) -> list[dict]:
        ordered = sorted(groups.items(), key=lambda item: (-len(item[1]), item[0]))
        return [
            {
                "group": key,
                "count": len(items),
                "incidents": sorted(items, key=lambda x: x.get("name", "")),
            }
            for key, items in ordered
        ]

    return {
        "by_impact": _sort_groups(by_impact),
        "by_initial_access": _sort_groups(by_initial_access),
        "by_year": _sort_groups(by_year),
    }


def write_per_incident_files(analyses: list[dict], out_dir: Path):
    """Write one JSON file per incident for detail pages."""
    incidents_dir = out_dir / "incidents"
    incidents_dir.mkdir(parents=True, exist_ok=True)

    for analysis in analyses:
        slug = analysis.get("incident_slug", "unknown")
        meta = _load_article_metadata(slug)
        enriched = dict(analysis)
        enriched["incident_name"] = meta.get("name") or slug.replace("-", " ").title()
        enriched["incident_date"] = meta.get("date")
        enriched["incident_root_cause"] = meta.get("root_cause")

        raw_impact = analysis.get("impact_type", "")
        enriched["impact_type"] = canonical_impact(raw_impact)
        enriched["impact_type_raw"] = raw_impact

        raw_services = analysis.get("aws_services", [])
        enriched["aws_services"] = canonical_services(raw_services)
        enriched["aws_services_raw"] = list(raw_services)

        # Canonicalize services referenced inside the step-by-step chain too,
        # so detail pages render the same canonical names as the index.
        chain = enriched.get("attack_chain")
        if isinstance(chain, list):
            enriched["attack_chain"] = [
                {**step, "aws_services_involved": canonical_services(step.get("aws_services_involved", []))}
                if isinstance(step, dict) else step
                for step in chain
            ]
        graph = enriched.get("attack_chain_graph")
        if isinstance(graph, dict) and isinstance(graph.get("nodes"), list):
            graph["nodes"] = [
                {**n, "aws_services_involved": canonical_services(n.get("aws_services_involved", []))}
                if isinstance(n, dict) else n
                for n in graph["nodes"]
            ]

        out_path = incidents_dir / f"{slug}.json"
        out_path.write_text(json.dumps(enriched, indent=2), encoding="utf-8")

    log.info("Wrote %d per-incident JSON files", len(analyses))


def build_stats(analyses: list[dict], technique_freq: dict) -> dict:
    """Overall statistics for the site hero section."""
    all_services: set[str] = set()
    for analysis in analyses:
        all_services.update(canonical_services(analysis.get("aws_services", [])))

    total_chain_steps = sum(
        len(a.get("attack_chain", [])) for a in analyses
    )

    impact_counts: Counter = Counter(
        canonical_impact(a.get("impact_type", "")) for a in analyses
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
        help=f"Output public data directory (default: {SITE_DATA_DIR})",
    )
    parser.add_argument(
        "--slug",
        help="Only include this specific incident slug (useful for iterative review)",
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

    # Load all analyses — treat a missing directory the same as an empty one
    # so initial/site-only deployments don't fail before Astro runs.
    if not analysis_dir.exists():
        log.warning("Analysis directory not found: %s – building empty site", analysis_dir)
        analyses = []
    else:
        analyses = load_analyses(analysis_dir)
    if args.slug:
        analyses = [a for a in analyses if a.get("incident_slug") == args.slug]
        log.info("Filtered analyses to slug=%s => %d", args.slug, len(analyses))

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
    catalog = build_catalog(incidents_index)

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
        "catalog.json": catalog,
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
