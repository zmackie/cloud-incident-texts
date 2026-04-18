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
        or "dns hijack" in s
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


# ── AWS / cloud service canonicalization ────────────────────────────────────
#
# The LLM emits ~125 distinct service strings — every shade of "IAM" vs
# "AWS IAM", "S3" vs "Amazon S3", plus parenthetical descriptors like
# "AWS Systems Manager (SSM)". This table maps every alias we've seen to
# a short canonical label. Keys are canonical names; values are alias sets
# (lowercased, with outer parentheticals stripped).
#
# For services we haven't enumerated, the fallback strips a leading
# "AWS "/"Amazon " prefix and passes the rest through, so new services
# work without table churn.

_SERVICE_ALIASES: dict[str, set[str]] = {
    "IAM":                  {"iam", "aws iam", "amazon iam"},
    "S3":                   {"s3", "aws s3", "amazon s3", "amazon simple storage service"},
    "EC2":                  {"ec2", "aws ec2", "amazon ec2"},
    "CloudTrail":           {"cloudtrail", "aws cloudtrail", "amazon cloudtrail"},
    "STS":                  {"sts", "aws sts", "amazon sts"},
    "RDS":                  {"rds", "aws rds", "amazon rds"},
    "VPC":                  {"vpc", "aws vpc", "amazon vpc"},
    "VPC Security Groups":  {"vpc security groups", "aws security groups", "ec2 security groups", "security groups"},
    "VPC Flow Logs":        {"vpc flow logs", "aws vpc flow logs"},
    "SES":                  {"ses", "aws ses", "amazon ses"},
    "SNS":                  {"sns", "aws sns", "amazon sns"},
    "SQS":                  {"sqs", "aws sqs", "amazon sqs"},
    "Lambda":               {"lambda", "aws lambda", "amazon lambda"},
    "GuardDuty":            {"guardduty", "aws guardduty", "amazon guardduty"},
    "CloudWatch":           {"cloudwatch", "aws cloudwatch", "amazon cloudwatch"},
    "EBS":                  {"ebs", "aws ebs", "amazon ebs"},
    "CloudFront":           {"cloudfront", "aws cloudfront", "amazon cloudfront"},
    "Bedrock":              {"bedrock", "aws bedrock", "amazon bedrock"},
    "ECS":                  {"ecs", "aws ecs", "amazon ecs"},
    "EKS":                  {"eks", "aws eks", "amazon eks"},
    "KMS":                  {"kms", "aws kms", "amazon kms"},
    "Route 53":             {"route 53", "aws route 53", "amazon route 53"},
    "DynamoDB":             {"dynamodb", "aws dynamodb", "amazon dynamodb"},
    "Redshift":             {"redshift", "aws redshift", "amazon redshift"},
    "Athena":               {"athena", "aws athena", "amazon athena"},
    "Cognito":              {"cognito", "aws cognito", "amazon cognito"},
    "API Gateway":          {"api gateway", "aws api gateway", "amazon api gateway"},
    "Systems Manager":      {"systems manager", "aws systems manager", "ssm", "aws ssm"},
    "Parameter Store":      {"parameter store", "aws systems manager parameter store", "ssm parameter store"},
    "Secrets Manager":      {"secrets manager", "aws secrets manager"},
    "Config":               {"aws config"},
    "Organizations":        {"organizations", "aws organizations"},
    "Backup":               {"backup", "aws backup"},
    "CloudFormation":       {"cloudformation", "aws cloudformation", "amazon cloudformation"},
    "CodePipeline":         {"codepipeline", "aws codepipeline"},
    "CodeBuild":            {"codebuild", "aws codebuild"},
    "IAM Identity Center":  {"iam identity center", "aws iam identity center", "aws identity center", "identity center", "aws sso", "sso"},
    "Management Console":   {"management console", "aws management console", "console", "aws console"},
    "CLI":                  {"aws cli"},
    "API":                  {"aws api"},
    "WAF":                  {"waf", "aws waf"},
    "Glue":                 {"glue", "aws glue"},
    "EMR":                  {"emr", "aws emr"},
    "Security Hub":         {"securityhub", "aws securityhub", "security hub", "aws security hub"},
    "SageMaker":            {"sagemaker", "aws sagemaker"},
    "ELB":                  {"elb", "aws elb", "elastic load balancing", "elastic load balancer"},
    "Service Quotas":       {"service quotas", "aws service quotas"},
    "Trusted Advisor":      {"trusted advisor", "aws trusted advisor"},
    "Compute Optimizer":    {"compute optimizer", "aws compute optimizer"},
    "AWS Health":           {"aws health"},
    "AWS Support":          {"aws support"},
    "Q Developer":          {"q developer", "aws q developer", "amazon q developer"},
    "S3 Glacier":           {"s3 glacier", "aws s3 glacier", "amazon s3 glacier", "glacier"},
    "IAM Access Analyzer":  {"iam access analyzer", "aws iam access analyzer", "access analyzer"},
    "IMDS":                 {"imds", "imdsv1", "imdsv2", "ec2 instance metadata service", "ec2 imds", "instance metadata service"},
    "AMI":                  {"ami", "community ami"},
    # Non-AWS tools that the LLM frequently lists alongside AWS services.
    "GitHub":               {"github", "github enterprise"},
    "GitHub Actions":       {"github actions"},
    "GitLab":               {"gitlab"},
    "Kubernetes":           {"kubernetes", "k8s"},
    "npm":                  {"npm", "node package manager"},
    "Okta":                 {"okta"},
    "Snowflake":            {"snowflake"},
    "Salesforce":           {"salesforce", "salesforce crm"},
    "Google Cloud":         {"google cloud", "google cloud platform", "gcp"},
    "Google Drive":         {"google drive"},
    "Cloudflare":           {"cloudflare", "cloudflare cdn"},
    # Generic/vague bucket — some incidents only say "AWS" with no specifics.
    "AWS":                  {"aws", "amazon web services", "aws cloud environment", "general cloud", "general cloud environment"},
}

# Precompute reverse lookup: lowercase alias -> canonical name.
_SERVICE_LOOKUP: dict[str, str] = {}
for _canonical, _aliases in _SERVICE_ALIASES.items():
    _SERVICE_LOOKUP[_canonical.lower()] = _canonical
    for _alias in _aliases:
        _SERVICE_LOOKUP[_alias] = _canonical

_PAREN_SUFFIX_RE = re.compile(r"\s*\([^)]*\)\s*$")
_PAREN_ANY_RE = re.compile(r"\s*\([^)]*\)")
_PREFIX_RE = re.compile(r"^(aws|amazon)\s+", re.IGNORECASE)


def canonical_service(raw: str | None) -> str:
    """Map a raw AWS/cloud service string to a canonical short label.

    - Empty input returns an empty string (caller filters it out).
    - Repeatedly strip trailing parentheticals ("AWS SES (Email)" -> "AWS SES").
    - Look up the stripped string against the alias table.
    - If no match, strip a leading "AWS "/"Amazon " and look up again.
    - If still no match, return the prefix-stripped value as-is so new
      services pass through without special-casing.
    """
    if raw is None:
        return ""
    s = str(raw).strip()
    if not s:
        return ""

    # Strip any parenthetical (trailing first; then any remaining) to avoid
    # variants like "AWS (general cloud environment)" or
    # "EC2 Instance Metadata Service (IMDSv1)" staying unique.
    while True:
        new = _PAREN_SUFFIX_RE.sub("", s).strip()
        if new == s:
            break
        s = new
    s = _PAREN_ANY_RE.sub("", s).strip()
    if not s:
        return ""

    key = s.lower()
    if key in _SERVICE_LOOKUP:
        return _SERVICE_LOOKUP[key]

    stripped = _PREFIX_RE.sub("", s).strip()
    key2 = stripped.lower()
    if key2 in _SERVICE_LOOKUP:
        return _SERVICE_LOOKUP[key2]

    # Fall back to the prefix-stripped form so new services show up cleanly
    # without requiring an alias table update. Preserve original capitalization.
    return stripped or s


def canonical_services(raw_list) -> list[str]:
    """Canonicalize a list of service strings and deduplicate, preserving order."""
    if not raw_list:
        return []
    seen: set[str] = set()
    out: list[str] = []
    for item in raw_list:
        canon = canonical_service(item)
        if not canon or canon in seen:
            continue
        seen.add(canon)
        out.append(canon)
    return out


__all__ = [
    "CANONICAL_IMPACTS",
    "UNKNOWN_IMPACT",
    "canonical_impact",
    "canonical_service",
    "canonical_services",
]
