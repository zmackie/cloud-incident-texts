"""Tests for scripts/normalize.py impact-type canonicalization."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from normalize import CANONICAL_IMPACTS, UNKNOWN_IMPACT, canonical_impact


def test_empty_input_is_unknown():
    assert canonical_impact(None) == UNKNOWN_IMPACT
    assert canonical_impact("") == UNKNOWN_IMPACT
    assert canonical_impact("   ") == UNKNOWN_IMPACT


def test_ransomware_wins_over_everything():
    # Double-extortion cases: keyword "ransomware" wins over "data exfiltration".
    assert canonical_impact("Ransomware / Data Exfiltration / Extortion") == "Ransomware / Extortion"
    assert canonical_impact("Ransomware (S3 Bucket Deletion + Extortion)") == "Ransomware / Extortion"
    assert canonical_impact("Data Exfiltration, Ransomware") == "Ransomware / Extortion"


def test_extortion_without_exfiltration_is_ransomware_bucket():
    assert canonical_impact("Extortion") == "Ransomware / Extortion"


def test_extortion_with_exfiltration_prefers_exfil():
    # Modern "data extortion" is primarily an exfiltration incident.
    assert canonical_impact("Data Exfiltration and Extortion") == "Data Exfiltration"
    assert canonical_impact("Extortion / Data Exfiltration") == "Data Exfiltration"


def test_cryptomining_variants_collapse():
    for variant in ("Cryptojacking", "Cryptomining", "Cryptomining (prevented)",
                    "Cryptojacking / DDoS Botnet", "Monero mining"):
        assert canonical_impact(variant) == "Cryptomining"


def test_llm_resource_hijacking_variants():
    for variant in ("LLMJacking", "LLMJacking (AI Resource Hijacking)",
                    "LLMJacking (Resource Hijacking / AI Service Abuse)",
                    "Resource Hijacking / Mass Phishing via SES"):
        # The last one hits resource-hijacking first (non-crypto), which is correct.
        assert canonical_impact(variant) == "LLM / Resource Hijacking"


def test_destruction_beats_exfiltration_when_both_present():
    # When destruction and exfiltration are co-listed, destruction is the
    # more consequential outcome and should dominate the category.
    assert canonical_impact("Data Destruction / Data Exfiltration") == "Data Destruction / Disruption"
    assert canonical_impact("Data Exfiltration and Data Destruction") == "Data Destruction / Disruption"
    assert canonical_impact("Data Deletion / Service Disruption") == "Data Destruction / Disruption"


def test_ddos_does_not_match_dos_substring():
    # Regression guard: "ddos" inside "cryptojacking / ddos botnet" must not
    # route to Destruction — mining is the primary outcome.
    assert canonical_impact("Cryptojacking / DDoS Botnet") == "Cryptomining"


def test_phishing_and_ses():
    for variant in ("Phishing / SES Abuse", "SES Abuse / Mass Phishing Campaign",
                    "AWS SNS SMS Phishing (Smishing)",
                    "Account Takeover / SES Abuse (Spam/Phishing Enablement)"):
        assert canonical_impact(variant) == "Phishing / SES Abuse"


def test_financial_theft_variants():
    assert canonical_impact("Financial Theft") == "Financial Theft"
    assert canonical_impact("Cryptocurrency Theft") == "Financial Theft"
    assert canonical_impact("Financial Theft / Cryptocurrency Theft") == "Financial Theft"


def test_supply_chain_variants():
    assert canonical_impact("Supply Chain Compromise / Magecart Malvertising") == "Supply Chain"
    assert canonical_impact("NFT Theft (Supply Chain / Web Skimming)") == "Supply Chain"


def test_plain_passthrough_values():
    assert canonical_impact("Data Exfiltration") == "Data Exfiltration"
    assert canonical_impact("Account Takeover") == "Account Takeover"
    assert canonical_impact("Credential Theft") == "Credential Theft"


def test_all_outputs_are_canonical():
    samples = [
        "", None, "Ransomware", "Data Exfiltration", "Cryptojacking",
        "LLMJacking (AI Resource Hijacking)", "Phishing / SES Abuse",
        "Account Takeover", "Financial Theft", "Supply Chain Compromise",
        "Unauthorized Access to Critical Assets", "Something completely novel",
    ]
    allowed = set(CANONICAL_IMPACTS) | {UNKNOWN_IMPACT}
    for s in samples:
        assert canonical_impact(s) in allowed
