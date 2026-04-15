# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.25.0",
# ]
# ///
"""
Run the incident pipeline for a single slug with a built-in sanity check
and optional Playwright browser verification.

Typical usage:
    python scripts/run_iterative_pipeline.py --slug aws-2023-february \
        --playwright --site-url http://127.0.0.1:4321
"""

import argparse
import json
import logging
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_MODEL = "claude-sonnet-4-6"

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
ANALYSIS_DIR = DATA_DIR / "analysis"
SITE_DATA_DIR = DATA_DIR / "site_data"
SCRIPT_DIR = Path(__file__).parent
RUNS_DIR = DATA_DIR / "pipeline_runs"

LOG = logging.getLogger(__name__)


def _configure_logging(debug: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(message)s",
    )


def _run_cmd(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    LOG.info("running: %s", " ".join(cmd))
    return subprocess.run(cmd, check=True, text=True, capture_output=True)


def _load_analysis(slug: str) -> dict[str, Any]:
    path = ANALYSIS_DIR / slug / "attack_analysis.json"
    if not path.exists():
        raise FileNotFoundError(f"attack_analysis.json not found at {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _sanity_check(analysis: dict[str, Any]) -> dict[str, Any]:
    chain = analysis.get("attack_chain", [])
    report: dict[str, Any] = {
        "slug": analysis.get("incident_slug"),
        "has_attack_chain": bool(chain),
        "chain_steps": len(chain),
        "warnings": [],
        "errors": [],
    }

    if not chain:
        report["errors"].append("No attack_chain produced.")
        return report

    techniques = []
    steps = []
    unvalidated = 0
    missing_evidence = 0

    for idx, step in enumerate(chain, 1):
        if not isinstance(step, dict):
            report["errors"].append(f"Step {idx} is not a dict")
            continue

        tid = (step.get("technique_id") or "").strip()
        techniques.append(tid)
        step_no = step.get("step")
        if isinstance(step_no, int):
            steps.append(step_no)
        else:
            report["warnings"].append(f"Step {idx} missing valid step number")

        if not step.get("validated", False):
            unvalidated += 1
        if not step.get("evidence_quote"):
            missing_evidence += 1

        if not tid:
            report["errors"].append(f"Step {idx} missing technique_id")

    if steps and steps != sorted(steps):
        report["warnings"].append("Attack chain step order is non-monotonic")

    if len(set(steps)) != len(steps):
        report["warnings"].append("Duplicate step numbers detected")

    if missing_evidence == len(chain):
        report["warnings"].append("All steps missing evidence_quote")

    if unvalidated == len(chain):
        report["warnings"].append("All techniques were unvalidated against ATT&CK cloud dataset")

    if techniques:
        report["unique_techniques"] = len(set(techniques))
        report["unknown_techniques"] = sorted({
            s.get("technique_id")
            for s in chain
            if isinstance(s, dict) and s.get("technique_id") and not s.get("validated", False)
        })

    return report


def _playwright_check(base_url: str, slug: str, out_dir: Path, render_graph: bool = False) -> dict[str, Any]:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except Exception as exc:
        LOG.warning("Playwright not available; skipping browser verification: %s", exc)
        return {"playwright_available": False, "status": "skipped", "reason": str(exc)}

    checks: dict[str, Any] = {"playwright_available": True}
    base = base_url.rstrip("/")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1600, "height": 1200})

        incident_url = f"{base}/incident?slug={slug}"
        page.goto(incident_url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_selector("#incident-body", timeout=15000)

        checks["incident_screenshot"] = str(out_dir / "incident.png")
        checks["incident_chain_steps_visible"] = page.locator(".chain-step").count()
        checks["incident_loaded"] = page.locator("#incident-body").is_visible()
        page.screenshot(path=checks["incident_screenshot"], full_page=True)

        checks["incident_load_error"] = page.locator(".loading").count()

        if render_graph:
            graph_url = f"{base}/graph"
            page.goto(graph_url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_selector("#graph-container", timeout=15000)
            checks["graph_loaded"] = page.locator("#graph-container").is_visible()
            checks["graph_screenshot"] = str(out_dir / "graph.png")
            page.screenshot(path=checks["graph_screenshot"], full_page=True)

        browser.close()

    checks["status"] = "ok"
    return checks


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run one-incident iterative pipeline with optional browser validation"
    )
    parser.add_argument("--slug", required=True, help="Incident slug to process")
    parser.add_argument(
        "--reanalyze",
        action="store_true",
        help="Re-run analyze even if attack_analysis.json exists",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Claude model to pass to analyze.py (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--ensure-attack-data",
        action="store_true",
        help="Ask analyze.py to fetch ATT&CK data if missing",
    )
    parser.add_argument(
        "--skip-site-build",
        action="store_true",
        help="Skip building data/site_data for preview",
    )
    parser.add_argument(
        "--playwright",
        action="store_true",
        help="Run browser sanity checks (requires playwright)",
    )
    parser.add_argument(
        "--graph-view",
        action="store_true",
        help="Capture graph page screenshot too (implies --playwright)",
    )
    parser.add_argument(
        "--site-url",
        default="http://127.0.0.1:4321",
        help="Base URL for Playwright check (default: http://127.0.0.1:4321)",
    )
    parser.add_argument(
        "--artifact-dir",
        default=str(RUNS_DIR),
        help=f"Directory for sanity/review artifacts (default: {RUNS_DIR})",
    )
    parser.add_argument("--debug", action="store_true", help="Enable verbose logs")
    args = parser.parse_args()

    _configure_logging(args.debug)

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    artifact_dir = Path(args.artifact_dir) / f"{args.slug}-{run_id}"
    artifact_dir.mkdir(parents=True, exist_ok=True)

    # 1) Run analysis
    analyze_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "analyze.py"),
        "--slug",
        args.slug,
        "--workers",
        "1",
        "--model",
        args.model,
    ]
    if args.reanalyze:
        analyze_cmd.append("--reanalyze")
    if args.ensure_attack_data:
        analyze_cmd.append("--ensure-attack-data")
    if args.debug:
        analyze_cmd.append("--debug")

    run_report: dict[str, Any] = {
        "run_id": run_id,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "slug": args.slug,
        "commands": {
            "analyze": " ".join(analyze_cmd),
        },
    }

    try:
        analyze_proc = _run_cmd(analyze_cmd)
        run_report["commands"]["analyze_exit_code"] = analyze_proc.returncode
        analyze_output = analyze_proc.stdout or ""
        run_report["commands"]["analyze_stdout"] = analyze_output[-4000:]
    except subprocess.CalledProcessError as exc:
        run_report["status"] = "analyze_failed"
        run_report["error"] = str(exc)
        if exc.stdout:
            run_report["analyze_stdout"] = exc.stdout[-4000:]
        if exc.stderr:
            run_report["analyze_stderr"] = exc.stderr[-4000:]
        artifact = artifact_dir / "iteration_report.json"
        artifact.write_text(json.dumps(run_report, indent=2), encoding="utf-8")
        LOG.error("Analysis failed for %s", args.slug)
        return

    # 2) Load and sanity-check structured output
    analysis = _load_analysis(args.slug)
    run_report["analysis"] = {
        "status": "ok",
        "path": str(ANALYSIS_DIR / args.slug / "attack_analysis.json"),
        "confidence_score": analysis.get("confidence_score", 0),
        "framework": analysis.get("framework", {}),
        "attack_chain_length": len(analysis.get("attack_chain", [])),
    }
    run_report["sanity"] = _sanity_check(analysis)

    # 3) Rebuild lightweight site data for this incident only
    if not args.skip_site_build:
        build_cmd = [
            sys.executable,
            str(SCRIPT_DIR / "build_site_data.py"),
            "--analysis-dir",
            str(ANALYSIS_DIR),
            "--output-dir",
            str(SITE_DATA_DIR),
            "--slug",
            args.slug,
        ]
        run_report["commands"]["build_site_data"] = " ".join(build_cmd)
        build_proc = _run_cmd(build_cmd)
        run_report["commands"]["build_exit_code"] = build_proc.returncode
        if build_proc.stdout:
            run_report["commands"]["build_stdout"] = build_proc.stdout[-4000:]

    # 4) Optional browser + screenshot sanity
    if args.playwright or args.graph_view:
        checks = _playwright_check(args.site_url, args.slug, artifact_dir, render_graph=args.graph_view)
        run_report["playwright"] = checks

    run_report["status"] = "ok"
    run_report["completed_at"] = datetime.now(timezone.utc).isoformat()
    artifact = artifact_dir / "iteration_report.json"
    artifact.write_text(json.dumps(run_report, indent=2), encoding="utf-8")
    LOG.info("Wrote iterative report to %s", artifact)

if __name__ == "__main__":
    main()
