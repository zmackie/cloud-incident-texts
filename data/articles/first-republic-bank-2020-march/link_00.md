Title: First Republic Bank

URL Source: https://www.breaches.cloud/incidents/first-republic/

Published Time: 2023-12-13

Markdown Content:
# First Republic Bank - Public Cloud Security Breaches

[Public Cloud Security Breaches](https://www.breaches.cloud/)Documenting their mistakes so you don't make them.

*   [Home](https://www.breaches.cloud/)
*   [Incidents](https://www.breaches.cloud/incidents/)
*   [News](https://www.breaches.cloud/news/)
*   [About](https://www.breaches.cloud/about/)
*   [Search](https://www.breaches.cloud/search/)

## [First Republic Bank](https://www.breaches.cloud/incidents/first-republic/)

Date Created: 2023-12-13 Post Author: [Chris Farris](https://www.chrisfarris.com/)

[AWS](https://www.breaches.cloud/tags/aws/)|[Insider Threat](https://www.breaches.cloud/tags/insider-threat/)|

## Incident Details

**Victimized Company:**First Republic Bank
**Incident Dates:**2020-03-11 to 2020-03-12
**Disclosure Date:**N/A
**Current Status:**Perpetrator Plead Guilty

In March 2020, a cloud engineer was terminated from First Republic Bank and subsequently accessed their AWS & GitHub environment to cause damage.

## Incident

### Details of the Incident

Miklos Daniel Brody was employed as a cloud engineer for First Republic Bank. In March of 2020, he was terminated for violation of company policies. He had in his possession a company-issued PC and Macbook. He surrendered the PC at his termination on March 11, 2020, but did not have his Macbook present at the time. Later that evening, he used the Macbook to log in to the corporate VPN.

Once logged into the corporate VPN, Brody, as alleged in the criminal complaint:

1.   Logged into a Linux jump box
2.   Overwrote system logs
3.   “used a Linux administrator account to impersonate” another employee
4.   From an enterprise GitHub server, used a script to “terminate almost all instances in Amazon Web Services”.
5.   Deleted code repositories
6.   “broke the Ansible Tower.”
7.   “locked users out of an Amazon service called EMR. The primary purpose of this is to do mathematics.”

### Timeline

| Date | Event |
| --- | --- |
| **March 2, 2020** | Brody plugs in two USB Sticks to his company-issued PC |
| **March 11, 2020 3 pm** | Brody is terminated from First Republic Bank |
| **March 11, 2020 7:16 pm** | Brody signs into First Republic VPN using MFA. |
| **March 11, 2020 7:55 to March 12, 2020 10:30 am** | Malicious Activity at the bank |
| **March 12, 2020 10:30 am** | Brody’s credentials were finally deactivated |
| **March 13 - 30, 2020** | FRB attempts to recovery Brody’s Macbook |
| **March 16, 2020** | Brody files police report claiming the Macbook was stolen |
| **April 5, 2023** | Brody pled guilty to two counts |
| **December 11, 2023** | Brody sentenced to 24 months, and fined $529k |

### Attribution / Perpetrator

Miklos Daniel Brody was indicted in 2020 and pled guilty in April 2023. He was sentenced on December 11, 2023, to 24 months in prison and ordered to pay restitution of $529k.

### Long-term Impact

The [Criminal Complaint](https://www.breaches.cloud/incidents/first-republic/gov.uscourts.cand.375169.1.0_1.pdf) lists monetary damages to First Republic Bank in excess of $220,000.

## Summary of Coverage

*   US District Court: [Criminal Complaint](https://www.breaches.cloud/incidents/first-republic/gov.uscourts.cand.375169.1.0_1.pdf) March 11, 2021
*   DOJ: [“Disgruntled Cloud Engineer Sentenced To Two Years In Prison For Intentionally Damaging His Former Employer’s Computer Network After He Was Fired”](https://www.justice.gov/usao-ndca/pr/disgruntled-cloud-engineer-sentenced-two-years-prison-intentionally-damaging-his) December 11, 2023
*   Bleeping Computer: [Cloud engineer gets 2 years for wiping ex-employer’s code repos](https://www.bleepingcomputer.com/news/security/cloud-engineer-gets-2-years-for-wiping-ex-employers-code-repos/) December 12, 2023

## Cloud Security Lessons Learned

From 3 pm, when his termination meeting began, to 10:30 am, the next morning, First Republic neglected to disable Brody’s VPN access.

### Links

*   [GitHub](https://github.com/primeharbor/breaches.cloud)
*   [Twitter](https://twitter.com/jcfarris)
*   [PrimeHarbor](https://primeharbor.com/)
*   [RSS](https://www.breaches.cloud/index.xml)

### Resources

*   [AWS Customer Incidents](https://github.com/ramimac/aws-customer-security-incidents)
*   [TrailDiscover](https://traildiscover.cloud/)

### Tags

[Access Keys](https://www.breaches.cloud/tags/access-keys/)| [AWS](https://www.breaches.cloud/tags/aws/)| [AzureAD](https://www.breaches.cloud/tags/azuread/)| [Cloud Hygiene](https://www.breaches.cloud/tags/cloud-hygiene/)| [CloudTrail](https://www.breaches.cloud/tags/cloudtrail/)| [Credential Rotation](https://www.breaches.cloud/tags/credential-rotation/)| [Data Exfiltration](https://www.breaches.cloud/tags/data-exfiltration/)| [Forgotten Cloud Resources](https://www.breaches.cloud/tags/forgotten-cloud-resources/)| [GitHub](https://www.breaches.cloud/tags/github/)| [Google](https://www.breaches.cloud/tags/google/)| [IAM Users](https://www.breaches.cloud/tags/iam-users/)| [IMDSv1](https://www.breaches.cloud/tags/imdsv1/)| [Insider Threat](https://www.breaches.cloud/tags/insider-threat/)| [Jenkins](https://www.breaches.cloud/tags/jenkins/)| [Logging](https://www.breaches.cloud/tags/logging/)| [M365](https://www.breaches.cloud/tags/m365/)| [Metadata Abuse](https://www.breaches.cloud/tags/metadata-abuse/)| [MFA](https://www.breaches.cloud/tags/mfa/)| [Mishandled Secrets](https://www.breaches.cloud/tags/mishandled-secrets/)| [MultiAccount](https://www.breaches.cloud/tags/multiaccount/)| [news](https://www.breaches.cloud/tags/news/)| [Public Bucket](https://www.breaches.cloud/tags/public-bucket/)| [Public Instance](https://www.breaches.cloud/tags/public-instance/)| [Public Snapshots](https://www.breaches.cloud/tags/public-snapshots/)| [Ransomware](https://www.breaches.cloud/tags/ransomware/)| [RDS](https://www.breaches.cloud/tags/rds/)| [Root](https://www.breaches.cloud/tags/root/)| [S3](https://www.breaches.cloud/tags/s3/)| [S3 Buckets](https://www.breaches.cloud/tags/s3-buckets/)| [Secrets](https://www.breaches.cloud/tags/secrets/)| [SES](https://www.breaches.cloud/tags/ses/)| [Shared Credentials](https://www.breaches.cloud/tags/shared-credentials/)| [Shared Responsibility](https://www.breaches.cloud/tags/shared-responsibility/)| [Snowflake](https://www.breaches.cloud/tags/snowflake/)| [Spear Phishing](https://www.breaches.cloud/tags/spear-phishing/)| 

### Table of Contents

*   [Incident](https://www.breaches.cloud/incidents/first-republic/#incident)
    *   [Details of the Incident](https://www.breaches.cloud/incidents/first-republic/#details-of-the-incident)
    *   [Timeline](https://www.breaches.cloud/incidents/first-republic/#timeline)
    *   [Attribution / Perpetrator](https://www.breaches.cloud/incidents/first-republic/#attribution--perpetrator)
    *   [Long-term Impact](https://www.breaches.cloud/incidents/first-republic/#long-term-impact)

*   [Summary of Coverage](https://www.breaches.cloud/incidents/first-republic/#summary-of-coverage)
*   [Cloud Security Lessons Learned](https://www.breaches.cloud/incidents/first-republic/#cloud-security-lessons-learned)

### Pages

*   [Home](https://www.breaches.cloud/)
*   [Incidents](https://www.breaches.cloud/incidents/)
*   [News](https://www.breaches.cloud/news/)
*   [About](https://www.breaches.cloud/about/)
*   [Search](https://www.breaches.cloud/search/)

### Links

*   [GitHub](https://github.com/primeharbor/breaches.cloud)
*   [Twitter](https://twitter.com/jcfarris)
*   [PrimeHarbor](https://primeharbor.com/)
*   [RSS](https://www.breaches.cloud/index.xml)

### Tags

[Access Keys](https://www.breaches.cloud/tags/access-keys/)[AWS](https://www.breaches.cloud/tags/aws/)[AzureAD](https://www.breaches.cloud/tags/azuread/)[Cloud Hygiene](https://www.breaches.cloud/tags/cloud-hygiene/)[CloudTrail](https://www.breaches.cloud/tags/cloudtrail/)[Credential Rotation](https://www.breaches.cloud/tags/credential-rotation/)[Data Exfiltration](https://www.breaches.cloud/tags/data-exfiltration/)[Forgotten Cloud Resources](https://www.breaches.cloud/tags/forgotten-cloud-resources/)[GitHub](https://www.breaches.cloud/tags/github/)[Google](https://www.breaches.cloud/tags/google/)[IAM Users](https://www.breaches.cloud/tags/iam-users/)[IMDSv1](https://www.breaches.cloud/tags/imdsv1/)[Insider Threat](https://www.breaches.cloud/tags/insider-threat/)[Jenkins](https://www.breaches.cloud/tags/jenkins/)[Logging](https://www.breaches.cloud/tags/logging/)[M365](https://www.breaches.cloud/tags/m365/)[Metadata Abuse](https://www.breaches.cloud/tags/metadata-abuse/)[MFA](https://www.breaches.cloud/tags/mfa/)[Mishandled Secrets](https://www.breaches.cloud/tags/mishandled-secrets/)[MultiAccount](https://www.breaches.cloud/tags/multiaccount/)[news](https://www.breaches.cloud/tags/news/)[Public Bucket](https://www.breaches.cloud/tags/public-bucket/)[Public Instance](https://www.breaches.cloud/tags/public-instance/)[Public Snapshots](https://www.breaches.cloud/tags/public-snapshots/)[Ransomware](https://www.breaches.cloud/tags/ransomware/)[RDS](https://www.breaches.cloud/tags/rds/)[Root](https://www.breaches.cloud/tags/root/)[S3](https://www.breaches.cloud/tags/s3/)[S3 Buckets](https://www.breaches.cloud/tags/s3-buckets/)[Secrets](https://www.breaches.cloud/tags/secrets/)[SES](https://www.breaches.cloud/tags/ses/)[Shared Credentials](https://www.breaches.cloud/tags/shared-credentials/)[Shared Responsibility](https://www.breaches.cloud/tags/shared-responsibility/)[Snowflake](https://www.breaches.cloud/tags/snowflake/)[Spear Phishing](https://www.breaches.cloud/tags/spear-phishing/)

### Table of Contents

*   [Incident](https://www.breaches.cloud/incidents/first-republic/#incident)
    *   [Details of the Incident](https://www.breaches.cloud/incidents/first-republic/#details-of-the-incident)
    *   [Timeline](https://www.breaches.cloud/incidents/first-republic/#timeline)
    *   [Attribution / Perpetrator](https://www.breaches.cloud/incidents/first-republic/#attribution--perpetrator)
    *   [Long-term Impact](https://www.breaches.cloud/incidents/first-republic/#long-term-impact)

*   [Summary of Coverage](https://www.breaches.cloud/incidents/first-republic/#summary-of-coverage)
*   [Cloud Security Lessons Learned](https://www.breaches.cloud/incidents/first-republic/#cloud-security-lessons-learned)

Unless otherwise noted, the content of this site is licensed under 

[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).

© 2022-2024 [PrimeHarbor Technologies, LLC](https://www.primeharbor.com/) | [Contribute!](https://github.com/primeharbor/breaches.cloud) | Powered by [Hugo](https://gohugo.io/) and AWS | Theme based on [Fuji-v2](https://github.com/dsrkafuu/hugo-theme-fuji/)