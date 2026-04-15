---
title: "A Surge in Identity-based Attacks: Cybersecurity trends from Sygnia's new 2025 Threat Report"
url: "https://www.sygnia.co/blog/sygnia-2025-field-report-identity-based-attacks/"
author: Sygnia Team
published: 2025-02-02
source_type: article
source_domain: www.sygnia.co
cleanup_method: llm
---

# A Surge in Identity-based Attacks: Cybersecurity trends from Sygnia’s new 2025 Threat Report

Explore key cybersecurity trends for 2025, including ransomware evolution, supply chain vulnerabilities, and identity-based threats. Discover actionable strategies and expert insights to strengthen your organization’s resilience.

Sygnia Team

2 February 2025

5 min


Sygnia’s 2025 Threat Report shares three real-world attacker trends that have consistently presented themselves on the frontlines over the last year—proving the need for immediate attention and strategic response by security leaders and practitioners alike. Evolving ransomware tactics, supply chain weaponization, and attacks on non-human identities have picked up speed in today’s threat landscape. In this blog, we provide a snapshot of the surge in identity-based attacks.

**Identity as the weakest link**. Aligning with the overarching organizational shift toward cloud-only and hybrid-cloud environments, our incident responders have observed a significant surge in the frequency and sophistication of threat actors focusing their efforts on **identity-based attacks** targeting cloud infrastructure to achieve initial access—with no indication of this slowing down.

With the increased exploitation of authentication systems and permission models, Sygnia has observed attackers systemically chaining minor permission gaps together to achieve sufficient privilege escalation and in turn leveraging compromised service accounts and SSO trust relationships to move laterally. In our latest [Threat Report](https://www.sygnia.co/sygnia-annual-threat-report-2025/), we highlight this trend along with the significant missteps of most organizations when it comes to effectively monitoring and controlling their identity access.

Misconfigured Identity and Access Management (IAM) policies are one of the biggest culprits in creating openings for lateral movement and privilege escalation by attackers. Lackluster monitoring of service accounts helps adversaries pivot between environments through SSO connections, ultimately enabling an additional attack vector in the end. And with the powerful onset of AI-driven attacks, the security barriers for identity defenses are facing even higher stakes.

**This can feel close to home.** In one standout instance observed by Sygnia incident responders, the identity-based attack began with social engineering tactics deployed by a state-sponsored threat group, through the popular LinkedIn and WhatsApp platforms. This group posed as professionals seeking technical advice from a select few of the targeted organization’s key development staff. After convincing these employees to download [what seemed to be harmless] code to their corporate laptops, used regularly for software development, this code harvested the desired access keys and credentials from their devices the attackers were looking for.

The attackers gained access to the organization’s Microsoft 365 tenant and authenticated against Entra ID using captured session tokens. This technique not only bypassed multi-factor authentication (MFA), but also circumvented other security controls that were in place. AWS access keys were discovered on the compromised devices as well, giving the attackers two ways into the AWS environment—through direct API access and the web console via compromised Entra ID users.

Once inside, they discovered an interesting weakness in the victim environment by modifying a Lambda function that had the ability to execute code on several previously inaccessible EC2 instances. **Each step seemed legitimate within the instance’s permissions and was expected in the day-to-day operations of this organization.** The organization’s weakness strengthened the attacker’s abilities greatly by helping the threat actor gain control over these instances and in turn craft fraudulent API calls that finally gave them access to the critical assets they were seeking.

![Image 24: Figure 1: Process flow of social engineering attack exploiting compromised credentials](blob:http://localhost/962f860a95ef804ffbe9e3163233c3bb)

_Figure 1: Process flow of social engineering attack exploiting compromised credentials_

**Forming a pattern.** While this case involved a state-sponsored threat group, similar attack methodologies are becoming a go-to for even less sophisticated adversaries. A clear indication of attack is only possible when looking at the complete chain of events, because each step on its own typically appears to be legitimate or harmless. This growing trend begs for security teams to place focus in this direction via identity-based security improvement plans and investments for 2025 and beyond.

**Key recommendations for mitigation**involve bolstering your identity governance, adopting zero trust principles, and participating in identity-focused red team assessments.

_Identity Governance:_ Limit permissions and require regular review to prevent adversaries from using stolen or privileged credentials to move laterally across environments.

1.   Conduct regular, automated audits of permissions to verify least-privilege access, especially for service and high-privilege accounts.
2.   Protect your sensitive credentials and API keys in a key vault.
3.   Scan code regularly and automatically to detect hard-coded or mishandled secrets.
4.   Auto-rotate credentials.
5.   Use cloud workload identities (e.g., attach AWS IAM roles) where applicable.

_Zero Trust Principles:_ Enforce re-authentication and context-aware access to limit the effectiveness of session-cookie theft and impersonation tactics seen in advanced phishing and deepfakes.

1.   Implement just-in-time (JIT) access for high sensitivity operations, requiring re-authentication for privileged actions.
2.   Transition from legacy remote access VPNs to Zero Trust Network Access (ZTNA) for all remote connections to ensure granular, policy-based access control.
3.   Implement strong authentication methods internally like MFA requirements for access within the corporate network and secure, token-based service-to-service authentication for internal APIs.

_Identity-Focused Red Teaming:_ Uncover subtle permission gaps and trust relationship vulnerabilities. These assessments validate the effectiveness of identity controls and reveal potential attack paths threat actors could exploit through permission mining and lateral movement techniques.

1.   Include identity-focused attack scenarios in red team exercises, specifically testing for permission chain exploitation, service account vulnerabilities, and SSO trust relationship weaknesses.

**Don’t stop here, learn more.** Read the latest issue of Sygnia’s new [2025 Threat Report](https://www.sygnia.co/sygnia-field-report-2025/). In this report, we dive into other trending topics like evolving ransomware group tactics and growing supply chain vulnerabilities—along with deeper coverage on the surge of identity-based attacks. Each trending cybersecurity topic in this report is supported by a frontline case study, mitigation recommendations, and a take-action checklist that you can rely on to ensure your bases are covered in the continuous effort to build a resilient security program for your organization.
