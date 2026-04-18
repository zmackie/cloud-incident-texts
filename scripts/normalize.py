# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Normalization helpers shared across the pipeline.

The LLM freely produces long-tail variants for categorical fields (e.g. every
shade of ransomware/extortion/data-exfiltration wording). This module collapses
those variants into a small, stable taxonomy used by the site for badges,
filters, and catalog groupings.

Original LLM values are preserved alongside the canonical ones (see
build_site_data.py, which writes both impact_type and impact_type_raw).
"""
from __future__ import annotations

import re

CANONICAL_IMPACTS = (
    "Ransomware / Extortion",
    "Data Exfiltration",
    "Data Destruction / Disruption",
    "Cryptomining",
    "LLM / Resource Hijacking",
    "Account Takeover",
    "Credential Theft",
    "Phishing / SES Abuse",
    "Financial Theft",
    "Supply Chain",
    "Unauthorized Access",
    "Other",
)

UNKNOWN_IMPACT = "Unknown"


def canonical_impact(raw: str | None) -> str:
    """Collapse an LLM-generated impact_type string to a canonical bucket.

    Order matters: the first matching rule wins, so list the more specific
    or higher-severity buckets first (ransomware shadows plain extortion,
    destruction shadows disruption, etc.).
    """
    if not raw or not str(raw).strip():
        return UNKNOWN_IMPACT

    s = str(raw).lower()

    if "ransomware" in s:
        return "Ransomware / Extortion"
    # "extortion" alone (without data exfil) → ransomware-adjacent
    if "extortion" in s and "exfiltration" not in s and "exfil" not in s:
        return "Ransomware / Extortion"

    # Cryptomining and LLM-hijacking win over the destruction fallback, since
    # "Cryptojacking / DDoS Botnet" is primarily a mining incident.
    if "cryptojack" in s or "cryptomining" in s or "crypto mining" in s or "monero" in s:
        return "Cryptomining"

    if "llmjacking" in s or "llm jack" in s or "ai service" in s or "ai resource" in s:
        return "LLM / Resource Hijacking"
    # MITRE "Resource Hijacking" in modern incidents is dominated by LLM abuse
    if "resource hijacking" in s and "crypto" not in s and "mining" not in s:
        return "LLM / Resource Hijacking"

    if "phishing" in s or "smishing" in s or "ses abuse" in s or "sns" in s or "spam" in s:
        return "Phishing / SES Abuse"

    if "supply chain" in s or "magecart" in s or "skimming" in s or "nft theft" in s:
        return "Supply Chain"

    if "financial theft" in s or "cryptocurrency theft" in s:
        return "Financial Theft"

    # Destruction before exfiltration: when both are stated, destruction is
    # the more consequential outcome for the victim.
    if (
        "destruction" in s
        or "destructive" in s
        or "data deletion" in s
        or "disruption" in s
        or "denial of service" in s
        or re.search(r"\bd?dos\b", s)
        or "service interruption" in s
        or "system interruption" in s
        or "dns" in s
    ):
        return "Data Destruction / Disruption"

    if "exfiltration" in s or "data breach" in s or "data collection" in s:
        return "Data Exfiltration"

    if "credential" in s:
        return "Credential Theft"

    if "account takeover" in s:
        return "Account Takeover"

    if "unauthorized access" in s or "remote code execution" in s or "reconnaissance" in s:
        return "Unauthorized Access"

    return "Other"


__all__ = ["CANONICAL_IMPACTS", "UNKNOWN_IMPACT", "canonical_impact"]
