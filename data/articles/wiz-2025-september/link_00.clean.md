---
title: "From Compromised Keys to Phishing Campaigns: Inside a Cloud Email Service Takeover"
url: "https://www.wiz.io/blog/wiz-discovers-cloud-email-abuse-campaign"
author: Itay Harel, Hila Ramati
published: 2025-09-04
source_type: article
source_domain: www.wiz.io
cleanup_method: llm
---

# From Compromised Keys to Phishing Campaigns: Inside a Cloud Email Service Takeover

Exposed cloud credentials become the launchpad for mass phishing, highlighting email services as a prime target in cloud exploitation campaigns.

[Itay Harel](https://www.wiz.io/authors/itay-harel), [Hila Ramati](https://www.wiz.io/authors/hila-ramati)

September 4, 2025


## [](https://www.wiz.io/blog/wiz-discovers-cloud-email-abuse-campaign)**Intro**

The Wiz Research team continuously monitors trends across the threat landscape using Wiz Defend’s threat detection rules. Our goal is to track attacker tradecraft (TTPs) as it evolves, so we can rapidly adapt defenses and keep our customers protected.

Wiz Research identified a May 2025 SES (Amazon Simple Email Service) abuse campaign that stood out for its impact and the use of previously unseen attack patterns.

The attacker first compromised an AWS access key - a very common vector. We routinely observe tens of newly compromised cloud access keys each month, fueling hundreds of exploitation attempts.

Here, the attacker used the compromised key to access the victim’s AWS environment, bypass SES’s built-in restrictions, verify new “sender” identities, and methodically prepare and conduct a phishing operation. Our analysis of their activity enabled us to identify the attacker’s patterns and codify them into new detection rules. This expands our coverage across additional stages of the kill chain, ensuring that future abuse by this actor and others is detected more comprehensively.

## [](https://www.wiz.io/blog/wiz-discovers-cloud-email-abuse-campaign)**Background: Amazon SES and the Sandbox Constraint**

Amazon Simple Email Service (SES) is AWS’s cloud-based bulk email platform. By default, accounts operate in a restricted [“sandbox” mode](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html), where emails can only be sent to verified addresses and volumes are capped to 200 messages per day, at a maximum rate of one message per second. An account can be moved into the unrestricted “production” mode, in which emails can be sent to arbitrary recipients and the quota is raised, typically to 50,000 emails per day. The transition requires submitting account details for AWS review through the `PutAccountDetails` API, and customers who need even higher volumes can request additional capacity through a support ticket.

Production mode is designed with legitimate business use-cases in mind, but in the hands of an attacker, it can serve as the foundation for large-scale phishing and spam campaigns. [Wiz has identified SES abuse](https://threats.wiz.io/all-incidents/attack-abusing-amazon-ses) as a primary method for monetizing leaked AWS Access Keys. The appeal is clear: SES lets adversaries launch phishing at scale from trusted domains, shifting both financial costs and reputational damage onto the victim, while allowing malicious traffic to blend seamlessly with legitimate email flows and bypass many traditional defenses.

## [](https://www.wiz.io/blog/wiz-discovers-cloud-email-abuse-campaign)**From Stolen Keys to SES Sandbox Escape**

The attack began with a set of compromised access keys. While the exact vector remains unknown, such keys are often obtained through accidental public exposure (code repositories, misconfigured assets) or theft from a developer workstation. Once they obtained the AWS access key, the attacker’s first move was a simple `GetCallerIdentity` request _(ATT&CK:_[_T1078.004_](https://attack.mitre.org/techniques/T1078/004/)_)._ The API call response revealed that the access key had “ses-” embedded in its name, indicating it was originally provisioned with SES permissions. The attacker would have noticed this as well.

![Image 16](blob:http://localhost/e55326839549912516283a68ace303c9)

Next, the attacker began probing SES directly. They issued `GetSendQuota` and `GetAccount`calls, both intended to reveal the current state of the SES configuration and whether the account was still restricted to sandbox limits _(ATT&CK:_[_T1526_](https://attack.mitre.org/techniques/T1526/)_)._

This reconnaissance quickly escalated. Within a span of just ten seconds, we observed a burst of `PutAccountDetails`**requests that fanned out across all AWS regions** - a strong indicator of automation and a clear attempt to push the SES account into production mode _(ATT&CK:_[_T1098_](https://attack.mitre.org/techniques/T1098/)_)._ To our knowledge, this multi-regional use of `PutAccountDetails` has not been documented in prior reporting, making it a noteworthy and novel technique in the context of SES abuse. While the exact motive for the multi-regional activity is unclear, possible explanations include an attempt to maximize region-specific send quotas, evade region-level SCP restrictions, or simply build redundancy across regions.

Additionally, what the attacker included in those requests provides a useful look at how adversaries attempt to move SES accounts out of the sandbox. Their justification read:

![Image 18](blob:http://localhost/d1a2e3878eb8332e8c5315efa19bae5f)

Along with this, they included a website URL of a construction company that had no connection to the victim, or to the identities later used for phishing. It was a generic, almost boilerplate explanation, but just polished enough to pass as legitimate. The request was eventually approved by AWS support.

But the attacker wasn’t content with the default 50,000-emails-per-day quota. They tried to open a support ticket programmatically through the `CreateCase` API, asking AWS to further raise their limits _(ATT&CK:_[_T1098_](https://attack.mitre.org/techniques/T1098/)_)_, an attempt that failed due to insufficient permissions. Not giving up, they then attempted to escalate their privileges by creating an [IAM policy](https://www.wiz.io/academy/aws-iam-best-practices) named `ses-support-policy` and attaching it to the compromised IAM user _(ATT&CK:_[_T1098.003_](https://attack.mitre.org/techniques/T1098/003/)_)._ That effort also failed due to insufficient permissions, leaving them capped at the standard production quota. Interestingly, the use of `CreateCase` via API rather than the AWS Console - as we saw here - is uncommon, and serves as another strong indicator of suspicious activity.

Although the support case attempt failed, the attacker retained the default 50,000-emails-per-day quota. That capacity was sufficient on its own, and with production mode enabled, the final stage of the SES abuse campaign could begin.

## [](https://www.wiz.io/blog/wiz-discovers-cloud-email-abuse-campaign)**From Sandbox Escape to Phishing Infrastructure**

The attacker started by adding multiple domains as verified identities using the `CreateEmailIdentity` API. The domains were a mix of attacker-owned domains and legitimate domains with weak DMARC protections (which make it easier for attackers to spoof or send on behalf of the domain without being blocked by common email security controls) _(ATT&CK:_[_T1583.001_](https://attack.mitre.org/techniques/T1583/001/)_,_[_T1584.001_](https://attack.mitre.org/techniques/T1584/001/)_)_. The ones owned by the attackers were:

*   `managed7.com`

*   `street7news.org`

*   `street7market.net`

*   `docfilessa.com`

Once verified, they created email addresses tied to these domains, using common prefixes such as:

*   `admin@`

*   `billing@`

*   `sales@`

*   `noreply@`

## [](https://www.wiz.io/blog/wiz-discovers-cloud-email-abuse-campaign)Setup Enables Broader Phishing Campaign

We worked with our colleagues at Proofpoint, who had identified a phishing campaign that was using these domains for the sending email, to gather further insight.

The campaign targeted multiple organizations without a clear geographical or industry focus. The phishing messages referenced 2024 tax forms, with subjects such as “_Your 2024 Tax Form(s) Are Now Ready to View and Print - Reference Number: XXXX_” and “_Information Alert: Tax Records Contain Anomalies# XXXX_”.

The emails linked to what we assess was a credential theft site hosted at `irss[.]securesusa[.]com`. To evade detection, the attackers concealed the site behind a redirect provided by a commercial traffic analysis service - a technique commonly used in marketing campaigns, but here repurposed to both bypass security scanners and give the actors visibility into victim click-through rates.

These types of credential theft campaigns can facilitate a broad array of malicious activity, including credential theft, business email compromise and other schemes. Given the lightweight and opportunistic nature of this campaign, we assess that it was likely conducted for financial gain. However, we do not link it to any publicly tracked groups.

![Image 20](blob:http://localhost/d04d52e16d3108c8fa7d968fdce8cc82)

## [](https://www.wiz.io/blog/wiz-discovers-cloud-email-abuse-campaign)**Why SES Abuse Matters**

At first glance, SES abuse might look like a nuisance with negligible cost - pennies per thousand emails - but there are strong reasons to monitor it closely:

*   **Reputational and business risk:** If SES is configured in your account, attackers can send email from your verified domains. Beyond brand damage, this enables phishing that looks like it came from you and can be used for spearphishing, fraud, data theft, or masquerading in business processes.

*   **Compromise risk:**SES abuse rarely happens in isolation. It’s a clear indicator that adversaries already control valid AWS credentials that can be expanded into more impactful actions.

*   **Operational risk:**Spam or phishing activity can trigger abuse complaints to AWS, which may result in an abuse case being filed against your account - something any organization would want to avoid.

## [](https://www.wiz.io/blog/wiz-discovers-cloud-email-abuse-campaign)**Conclusion and Key Takeaways**

This campaign highlights several broader lessons for defending cloud environments.

*   **Leaked access keys** remain one of the most common and effective entry points for attackers. Signs to monitor include inactive keys suddenly becoming active, logins from unusual ASNs and activity from multiple countries. When these signals appear, start by addressing the highest-risk keys - those that have overly broad permissions or that are long-dormant.

*   Monitor for**sudden spikes** in cloud service usage. In AWS, you can surface these anomalies through CloudWatch metrics, billing console, or CloudTrail logs. Extra attention should be given to services that attackers frequently target for monetization, such as email, messaging, compute, or storage (for example, SES, SNS, EC2, and S3).

In addition, attacker techniques from this specific campaign worth monitoring include: multi-regional bursts of `PutAccountDetails` requests, non-console invocation of `CreateCase` API, and rapid creation of domains and email identities.

## [](https://www.wiz.io/blog/wiz-discovers-cloud-email-abuse-campaign)**Prevention Guidance**

Even without specialized tooling, organizations can take several steps to reduce the risk of SES abuse:

*   **Restrict SES if unused**: Apply an AWS Service Control Policy (SCP) to block SES entirely in accounts where it isn’t needed.

*   **Audit and rotate keys**: Regularly rotate IAM keys, and monitor for dormant keys that suddenly become active again.

*   **Enforce least privilege**: Ensure only designated roles and identities can verify new senders or request production access.

*   **Log and alert on SES activity**: Use CloudTrail to track SES API calls such as `PutAccountDetails`, and watch for spikes in `SendEmail` usage or unusual sender additions. SES _data events_ are a new CloudTrail feature that provide much more granular visibility into email sending activity, and organizations should enable them wherever possible.

## [](https://www.wiz.io/blog/wiz-discovers-cloud-email-abuse-campaign)**How Wiz Can Help**

Wiz Defend customers benefit from continuous monitoring and detections that are specifically designed to catch the early signals of SES abuse and other common monetization vectors of compromised access keys. In campaigns like this, several of our detection rules are effective in flagging the attacker’s behavior well before large-scale phishing operations could begin:

*   [**Multi-Regional Attempt to Leave SES Sandbox Mode**](https://app.wiz.io/policies/cloud-event-rules#%7E%28eventRule%7E%276e7afd9d-9574-5b14-9594-fee22ff49cd2%29)

*   [**IAM Access Key Used After Long Period of Inactivity**](https://app.wiz.io/policies/cloud-event-rules#%7E%28eventRule%7E%274137e60c-c800-5a64-af0f-d93716c72f26%29)

*   [**API Calls From Multiple Countries Within a Short Timeframe (Permanent Key)**](https://app.wiz.io/policies/cloud-event-rules#%7E%28eventRule%7E%2730286277-06f3-585d-9687-81c8c39c5069%29)

*   [**Domain Added to SES Configuration**](https://app.wiz.io/policies/cloud-event-rules#%7E%28eventRule%7E%275320b230-c600-5555-8aab-262729ba3adf%29)

*   [**Usage of Known Atomic IOCs**](https://app.wiz.io/policies/cloud-event-rules#%7E%28eventRule%7E%277c89eefb-8db8-5a2a-b735-ab669460229f%29)

![Image 22](blob:http://localhost/1c855c26ccf410acfd91a385b3484b38)

By correlating these behaviors across AWS services, Wiz Defend provides defenders with early warning and actionable context. Instead of spotting SES abuse only once phishing emails are already flowing, Wiz Defend highlights the attacker’s preparatory steps, giving security teams the opportunity to respond before the campaign scales.

Wiz also surfaces compromised access keys and continuously scans for exposed credentials, enabling organizations to rotate these compromised credentials before attackers have an opportunity to abuse them.
