---
title: BeyondTrust Remote Support SaaS Service Security Investigation
url: "https://www.beyondtrust.com/remote-support-saas-service-security-investigation"
published: 2024-12-08
source_type: article
source_domain: www.beyondtrust.com
cleanup_method: llm
---

# BeyondTrust Remote Support SaaS Service Security Investigation

Updated 1/28/25 at 5:45 p.m. EST. First published 12/8/24 at 11:00 p.m. EST.

## Summary

In December 2024, BeyondTrust identified a security incident that involved 17 Remote Support SaaS customers. On December 5th, 2024, a root cause analysis into a Remote Support SaaS issue identified a BeyondTrust infrastructure API key for Remote Support SaaS had been compromised and used to enable access to certain Remote Support SaaS instances by resetting local application passwords. No BeyondTrust products outside of Remote Support SaaS were affected. BeyondTrust’s forensics investigation, in coordination with a leading third-party forensics firm, was completed on January 17, 2025.

## Timeline Overview

*   December 5, 2024 – Anomalous behavior was confirmed and a limited number of affected instances of Remote Support SaaS were identified.

*   December 5, 2024 – Initiated incident response protocols, engaged third-party forensics firm on retainer, revoked affected API key, and quarantined infrastructure for analysis.

*   December 8, 2024 – Published initial public security advisory.

*   December 10, 2024 – Notification to Federal law enforcement partners.

*   December 13, 2024 – CVE-2024-12356 and CVE-2024-12686 zero-day vulnerabilities discovered.

*   December 14-15, 2024 – Remote Support SaaS environments patched.

*   December 16, 2024 – Critical zero-day vulnerability (CVE-2024-12356) and patches announced.

*   December 19, 2024 – Medium-severity vulnerability (CVE-2024-12686) and patches announced.

*   December 19, 2024 – Law enforcement assigns attribution to China-nexus threat actors.

*   December 20, 2024 - Present – Continue to support affected customers and law enforcement in their respective investigations.

*   January 17, 2025 – BeyondTrust Investigation completed.

## Security Incident Details

BeyondTrust confirmed and began taking measures to address the security incident on December 5, 2024 that involved our Remote Support SaaS product. No BeyondTrust products outside of Remote Support SaaS were affected. No FedRAMP instances were affected. No other BeyondTrust systems were compromised, and ransomware was not involved.

Our investigation into the cause and impact of the compromise was conducted with a recognized third-party cybersecurity and forensics firm. The investigation determined that a zero-day vulnerability of a third-party application was used to gain access to an online asset in a BeyondTrust AWS account. Access to that asset then allowed the threat actor to obtain an infrastructure API key that could then be leveraged against a separate AWS account which operated Remote Support infrastructure. This vulnerability, as well as the two vulnerabilities discovered and disclosed as noted in the timeline above have been patched.

In response to the initial incident, BeyondTrust initiated our security incident response process and took actions including:

*   Immediately revoked the compromised API key.

*   Suspended and quarantined all known affected customer instances.

*   Notified affected customers and worked with them to provide alternative Remote Support SaaS instances.

*   Engaged a recognized third-party cybersecurity and forensics firm to assist in the investigation.

*   Communicated with federal law enforcement, with whom we continue to coordinate and share information.

Our forensics investigation is now complete and has identified no unauthorized access to these Remote Support SaaS instances since early December 2024. This has been confirmed by the leading third-party forensics provider who continues to scan our environment for any indicators of compromise or other signs of threat actor activity. All customers affected have been informed and continue to be actively engaged with our security teams. Additionally, our teams continue to support the ongoing law enforcement investigation.

## Recommended Best Practices for Customers

BeyondTrust patched all SaaS instances of Remote Support and has worked to raise awareness with customers who need to do their own patching for self-hosted Remote Support instances. Further, and in addition to the Remote Support [**configuration guidance**](https://docs.beyondtrust.com/rs/docs/on-prem-admin-guide) on our website, below are also good practices to consider when using Remote Support:

*   If self-hosted, stay up-to-date with current releases, and activate the "Apply Critical Updates Automatically" option found in the /appliance interface
*   Consider using external authentication provider (ex. SAML) over local accounts; and be sure to delete accounts not in use
*   Consider using outbound events to trigger notifications for session events
*   [Integrate with a SIEM](https://beyondtrustcorp.service-now.com/csm?id=kb_article_view&sysparm_article=KB0020338) using one of our various middleware for Session Data and periodically review for suspicious activity
*   Configure syslog to send all configuration changes and authentication events to your SIEM 
*   Practice least privilege for setting up user roles and capabilities, and for endpoint access
*   Periodically, review all Security Settings and leverage the Session Policy simulator to validate policies are being applied as intended
*   Periodically, review all active accounts on your appliance(s), especially those with admin privileges. Deactivate those not in use, and rotate passwords at recurring intervals where possible.
*   [Enable network restrictions where possible](https://docs.beyondtrust.com/rs/docs/on-prem-security-settings#network-restrictions)

## Indicators of Compromise (IoC)

The following Indicators of Compromise (IOCs) were identified during our investigation.

| Content table | Content table |
| --- | --- |
| 24.144.114.85 | 2604:a880:400:d1::7293:c001 |
| 142.93.119.175 | 2604:a880:400:d1::72ad:3001 |
| 157.230.183.1 | 2604:a880:400:d1::7716:1 |
| 192.81.209.168 | 2604:a880:400:d1::7df0:7001 |
|  | 2604:a880:400:d1::8622:f001 |

## Attribution

Federal law enforcement identified the unauthorized activity was attributed to a group of individuals associated with China.

## Closing Thoughts

Our forensics investigation is complete. We will now look to implement any necessary changes as part of our ongoing efforts to continuously strengthen our security posture. Our primary focus remains working with our affected customers’ security teams to ensure their own investigations are properly supported and concluded.

Organizations across every major industry are vulnerable to cyber threats, many of which, like these zero-day vulnerabilities, remain unknown. While our forensics investigation is complete, we know that controls and defenses should not remain static, and findings from our investigation will serve only to strengthen our security posture as we continue to implement measures to further enhance our security practices.

## Further Resources

As always, if you have a technical issue, please open a ticket via our secure customer portal link: [https://beyondtrust.com/myportal](https://beyondtrust.com/myportal)

You can also access the latest customer news and updates via our BeeKeepers community: [https://beekeepers.beyondtrust.com/](https://beekeepers.beyondtrust.com/)

## Previous Updates

| DATE: | UPDATE: |
| --- | --- |
| 1/17/25 | The investigation is complete. The 17 customers involved were all notified in early December, and BeyondTrust has since worked with them to fully support their investigations by providing artifacts, logs, indicators of compromise, and answering questions. Information has been shared to support (1) federal law enforcement efforts to pursue the threat actor and (2) threat intelligence information sharing organizations. BeyondTrust patched all SaaS instances of Remote Support and has worked to raise awareness with customers who need to do their own patching for self-hosted Remote Support instances. BeyondTrust is committed to using the findings from the investigation to further strengthen security controls and configurations holistically across its environment, and to help our customers do the same. |
| 1/6/25 | The forensic investigation into the Remote Support SaaS incident is approaching completion. All SaaS instances of BeyondTrust Remote Support have been fully patched against the vulnerabilities mentioned in our previous security advisories. A patch has also been pushed for self-hosted instances. No new customers have been identified beyond those we have communicated with previously. |
| 12/18/24 | As a result of our on-going investigation, we identified a medium-severity vulnerability ([CVE-2024-12686](https://www.beyondtrust.com/trust-center/security-advisories/bt24-11)) within our Remote Support and Privileged Remote Access products (both self-hosted and cloud). As communicated in the 12/16/24 (AM) update, all cloud instances have been patched for this vulnerability. We have also released a patch for self-hosted versions. We continue to pursue all possible paths as part of the forensic analysis, including our work with external forensic parties, to ensure we conduct as thorough an investigation as possible. We also continue to communicate and work closely with all known affected customers and will provide updates here until our investigation is concluded. |
| 12/16/24 (PM) | As part of our on-going forensics investigation into the Remote Support SaaS incident, we identified a critical vulnerability ([CVE-2024-12356](https://www.beyondtrust.com/trust-center/security-advisories/bt24-10)) within our Remote Support and Privileged Remote Access products (both self-hosted and cloud). As communicated in the 12/16/24 update, all cloud instances have been patched for this vulnerability. We have also released a patch for self-hosted versions. This update for all self-hosted versions is a non-disruptive patch pushed through the standard update feature of the product. There is no downtime associated with this patch, and it is being pushed to self-hosted Remote Support & Privileged Remote Access customers. We are pursuing all possible paths as part of the forensic analysis, including our work with external forensic parties, to ensure we conduct as thorough an investigation as possible. We continue to communicate and work closely with all known affected customers, and will provide updates here until our investigation is concluded. |
| 12/16/24 (AM) | We have proactively completed an update for our Secure Remote Access (Remote Support and Privilege Remote Access) Cloud customers, fortifying the security of their solution overall. We are pursuing all possible paths as part of the forensic analysis, including our work with external forensic parties, to ensure we conduct as thorough an investigation as possible. We continue to communicate and work closely with all known affected customers, and will provide updates here until our investigation is concluded. In addition, we are providing recommended resources that are available through our customer portal for your solutions including: - [Remote Support Offers IP Whitelisting and Other Network Restrictions](https://beyondtrustcorp.service-now.com/csm?id=kb_article_view&sysparm_article=KB0020032) - [Monitoring Appliance Activity with Syslog](https://beyondtrustcorp.service-now.com/csm?id=kb_article_view&sysparm_article=KB0020338) - [Securing Use of the Remote Support API](https://beyondtrustcorp.service-now.com/csm?id=kb_article_view&sysparm_article=KB0017829) |
| 12/12/24 | While the security incident forensics investigation remains ongoing, there are no material updates to provide at this time. We continue to pursue all possible paths as part of the forensic analysis, with the assistance of external forensic parties, to ensure we conduct as thorough an investigation as possible. We continue to communicate, and work closely with, all known affected customers. We will continue to provide updates here until our investigation is concluded. |
