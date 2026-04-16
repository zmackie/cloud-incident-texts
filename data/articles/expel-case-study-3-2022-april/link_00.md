Title: Incident report: From CLI to console, chasing an attacker in AWS

URL Source: https://expel.com/blog/incident-report-from-cli-to-console-chasing-an-attacker-in-aws/

Published Time: 2022-04-05T20:04:54+00:00

Markdown Content:
# Incident report: From CLI to console, chasing an attacker in AWS | Expel

[Skip to content](https://expel.com/blog/incident-report-from-cli-to-console-chasing-an-attacker-in-aws/#primary)

[✕](https://expel.com/blog/incident-report-from-cli-to-console-chasing-an-attacker-in-aws/#)

Your best engineers shouldn't be tuning SIEM rules. Now they don't have to. Expel Managed SIEM is here.

[Learn more about Managed SIEM](https://expel.com/services/managed-siem/)

Primary Menu

*   [Blog](https://expel.com/blog/)
*   [Partners](https://expel.com/partner-program/)
*   [Customers](https://expel.com/customers/)
*   [Contact](https://expel.com/contact/)
*   Search for: 

[![Image 1: Expel](https://expel.com/wp-content/uploads/2026/03/expel-logo-dark_nw.png)](https://expel.com/)[![Image 2: Expel](blob:http://localhost/e060dc22f9fa74726e21296180c89c83)](https://expel.com/)

- [x] - [x] Primary Menu

*   [What we do](https://expel.com/services/managed-detection-response/)
    *   Services  
        *   [Managed Detection and Response (MDR) Tailored solutions for any size org offering 24×7 protection](https://expel.com/services/managed-detection-response/)
        *   [Managed SIEM Detection engineering for your existing SIEM](https://expel.com/services/managed-siem/)
        *   [Phishing Investigation and response for your phishing inbox](https://expel.com/services/phishing/)
        *   [Threat hunting Hypothesis-based activity hunting](https://expel.com/services/threat-hunting/)
        *   [Plans & Packages Choose the MDR bundle that’s right for you](https://expel.com/mdr-packages/)

    *   Our tech  
        *   [Workbench™ Operations Platform The SOC’s digital command center](https://expel.com/workbench-operations-platform/)
        *   [AI & automation engine Enable our experts to stop real threats, faster](https://expel.com/ai-automation/)
        *   [Security data lake Lower your storage costs while staying ahead of threats](https://expel.com/solutions/security-data-lake/)
        *   [Tech Integrations Make your technology work harder](https://expel.com/integrations/)

*   [Why Expel?](https://expel.com/why-expel/)
    *   Proof points  
        *   [Why Expel? Learn why leading organizations choose Expel for MDR](https://expel.com/why-expel/)
        *   [Our customers Real results from real customers across every industry](https://expel.com/customers/)
        *   [![Image 4](https://expel.com/wp-content/uploads/2025/10/Leader_182001-Badge.jpg) Forrester Wave Leader in MDR services Q1 2025](https://expel.com/forrester-wave/)

    *   How it works  
        *   [24x7 Security Operations World-class service delivered by the experts](https://expel.com/security-operations-center-soc/)
        *   [SOC experts We protect your environment just as we protect our own](https://expel.com/meet-the-soc-experts/)
        *   [Auto remediation We stop threats before they stop you](https://expel.com/auto-remediation/)
        *   [Detection Coverage Detect threats that slip between gaps in your tools](https://expel.com/detection-coverage/)
        *   [Expel Intel Cybersecurity intelligence, threat data, and research](https://expel.com/intel/)

*   [Coverage](https://expel.com/solutions/)
    *   Attack surface  
        *   [Cloud](https://expel.com/solutions/cloud-security/)
        *   [Email](https://expel.com/solutions/email-threat-detection/)
        *   [Endpoint](https://expel.com/solutions/endpoint-security-monitoring/)
        *   [Identity](https://expel.com/solutions/identity-security/)
        *   [Network](https://expel.com/solutions/secure-company-network/)
        *   [SaaS](https://expel.com/solutions/secure-saas-applications/)

    *   Environment use cases  
        *   [Amazon Web Services (AWS)](https://expel.com/solutions/aws-cloud-security/)
        *   [Google Cloud](https://expel.com/solutions/google-cloud-security/)
        *   [Kubernetes](https://expel.com/solutions/kubernetes-mdr-security/)
        *   [Microsoft](https://expel.com/solutions/microsoft-mdr-security/)
        *   [Oracle Cloud Infrastructure (OCI)](https://expel.com/solutions/oracle-cloud-security/)
        *   [SIEM](https://expel.com/solutions/optimize-your-siem-security/)
        *   [Tech integrations](https://expel.com/integrations/)

*   [Resources](https://expel.com/resources/)
    *   Resource Center  
        *   [Briefs & Datasheets](https://expel.com/resources/?type=briefs-datasheets)
        *   [Case studies](https://expel.com/resources/?type=case-studies)
        *   [ebooks & Whitepapers](https://expel.com/resources/?type=ebooks-whitepapers)
        *   [Podcasts](https://expel.com/resources/?type=podcasts)
        *   [Reports](https://expel.com/resources/?type=reports)
        *   [Tools](https://expel.com/resources/?type=tool)
        *   [Videos](https://expel.com/resources/?type=video)
        *   [Webinars](https://expel.com/webinars/)
        *   [View all resources](https://expel.com/resources/)

    *   Knowledge Center  
        *   [Blogs](https://expel.com/blog/)
        *   [Cybersecurity glossary](https://expel.com/cyberspeak/)

    *   Featured  
        *   [Forrester Wave](https://expel.com/forrester-wave/)
        *   [Gartner® Market Guide for MDR](https://expel.com/gartner-mdr-market-guide/)
        *   [Expel's 2026 Annual Threat Report Transforms real-life cybersecurity lessons into actionable insights for security operators](https://expel.com/annual-threat-report/)

*   [Company](https://expel.com/about/)
    *   About Expel  
        *   [About Us](https://expel.com/about/)
        *   [Careers](https://expel.com/about/careers/)
        *   [Equity, Inclusion & Diversity](https://expel.com/about/eid/)

    *   In the news  
        *   [Newsroom](https://expel.com/about/newsroom/)
        *   [News](https://expel.com/resource-type/news/)
        *   [Press releases](https://expel.com/resource-type/press-release/)

    *   Partners  
        *   [Partner Program](https://expel.com/partner-program/)
        *   [Incident Response](https://expel.com/partner-program/incident-response/)
        *   [Find a partner](https://expel.com/partner-program/partners/)

*   [Plans & Packages](https://expel.com/mdr-packages/)
*   [Schedule a demo](https://expel.com/request-demo/)

*   Search for: 
*   [What we do](https://expel.com/services/managed-detection-response/) 
    *   Services  
        *   [Managed Detection and Response (MDR) Tailored solutions for any size org offering 24×7 protection](https://expel.com/services/managed-detection-response/)
        *   [Managed SIEM Detection engineering for your existing SIEM](https://expel.com/services/managed-siem/)
        *   [Phishing Investigation and response for your phishing inbox](https://expel.com/services/phishing/)
        *   [Threat hunting Hypothesis-based activity hunting](https://expel.com/services/threat-hunting/)
        *   [Plans & Packages Choose the MDR bundle that’s right for you](https://expel.com/mdr-packages/)

    *   Our tech  
        *   [Workbench™ Operations Platform The SOC’s digital command center](https://expel.com/workbench-operations-platform/)
        *   [AI & automation engine Enable our experts to stop real threats, faster](https://expel.com/ai-automation/)
        *   [Security data lake Lower your storage costs while staying ahead of threats](https://expel.com/solutions/security-data-lake/)
        *   [Tech Integrations Make your technology work harder](https://expel.com/integrations/)

*   [Why Expel?](https://expel.com/why-expel/) 
    *   Proof points  
        *   [Why Expel? Learn why leading organizations choose Expel for MDR](https://expel.com/why-expel/)
        *   [Our customers Real results from real customers across every industry](https://expel.com/customers/)
        *   [![Image 6: Active exploitation notice: React2Shell critical vulnerability (CVE-2025-55182)](blob:http://localhost/346dadc7249b4f18bcd4f1d0d397bce6) Forrester Wave Leader in MDR services Q1 2025](https://expel.com/forrester-wave/)

    *   How it works  
        *   [24x7 Security Operations World-class service delivered by the experts](https://expel.com/security-operations-center-soc/)
        *   [SOC experts We protect your environment just as we protect our own](https://expel.com/meet-the-soc-experts/)
        *   [Auto remediation We stop threats before they stop you](https://expel.com/auto-remediation/)
        *   [Detection Coverage Detect threats that slip between gaps in your tools](https://expel.com/detection-coverage/)
        *   [Expel Intel Cybersecurity intelligence, threat data, and research](https://expel.com/intel/)

*   [Coverage](https://expel.com/solutions/) 
    *   Attack surface  
        *   [Cloud](https://expel.com/solutions/cloud-security/)
        *   [Email](https://expel.com/solutions/email-threat-detection/)
        *   [Endpoint](https://expel.com/solutions/endpoint-security-monitoring/)
        *   [Identity](https://expel.com/solutions/identity-security/)
        *   [Network](https://expel.com/solutions/secure-company-network/)
        *   [SaaS](https://expel.com/solutions/secure-saas-applications/)

    *   Environment use cases  
        *   [Amazon Web Services (AWS)](https://expel.com/solutions/aws-cloud-security/)
        *   [Google Cloud](https://expel.com/solutions/google-cloud-security/)
        *   [Kubernetes](https://expel.com/solutions/kubernetes-mdr-security/)
        *   [Microsoft](https://expel.com/solutions/microsoft-mdr-security/)
        *   [Oracle Cloud Infrastructure (OCI)](https://expel.com/solutions/oracle-cloud-security/)
        *   [SIEM](https://expel.com/solutions/optimize-your-siem-security/)
        *   [Tech integrations](https://expel.com/integrations/)

*   [Resources](https://expel.com/resources/) 
    *   Resource Center  
        *   [Briefs & Datasheets](https://expel.com/resources/?type=briefs-datasheets)
        *   [Case studies](https://expel.com/resources/?type=case-studies)
        *   [ebooks & Whitepapers](https://expel.com/resources/?type=ebooks-whitepapers)
        *   [Podcasts](https://expel.com/resources/?type=podcasts)
        *   [Reports](https://expel.com/resources/?type=reports)
        *   [Tools](https://expel.com/resources/?type=tool)
        *   [Videos](https://expel.com/resources/?type=video)
        *   [Webinars](https://expel.com/webinars/)
        *   [View all resources](https://expel.com/resources/)

    *   Knowledge Center  
        *   [Blogs](https://expel.com/blog/)
        *   [Cybersecurity glossary](https://expel.com/cyberspeak/)

    *   Featured  
        *   [Forrester Wave](https://expel.com/forrester-wave/)
        *   [Gartner® Market Guide for MDR](https://expel.com/gartner-mdr-market-guide/)
        *   [Expel's 2026 Annual Threat Report Transforms real-life cybersecurity lessons into actionable insights for security operators](https://expel.com/annual-threat-report/)

*   [Company](https://expel.com/about/) 
    *   About Expel  
        *   [About Us](https://expel.com/about/)
        *   [Careers](https://expel.com/about/careers/)
        *   [Equity, Inclusion & Diversity](https://expel.com/about/eid/)

    *   In the news  
        *   [Newsroom](https://expel.com/about/newsroom/)
        *   [News](https://expel.com/resource-type/news/)
        *   [Press releases](https://expel.com/resource-type/press-release/)

    *   Partners  
        *   [Partner Program](https://expel.com/partner-program/)
        *   [Incident Response](https://expel.com/partner-program/incident-response/)
        *   [Find a partner](https://expel.com/partner-program/partners/)

*   [Plans & Packages](https://expel.com/mdr-packages/)
*   [Schedule a demo](https://expel.com/request-demo/)

[BLOG](https://expel.com/blog/) | [RAPID RESPONSE](https://expel.com/blog/category/rapid-response/)

# Incident report: From CLI to console, chasing an attacker in AWS

[Subscribe](javascript:void(0))

×

By Britton Manahan, [David Blanton](https://expel.com/blog/author/david-blanton/), [Kyle Pellett](https://expel.com/blog/author/kyle-pellett/), [Brian Bahtiarian](https://expel.com/blog/author/brian-bahtiarian/)

April 5, 2022 • 6 minute read

[](https://twitter.com/share?url=https%3A%2F%2Fexpel.com%2Fblog%2Fincident-report-from-cli-to-console-chasing-an-attacker-in-aws%2F&text=Incident+report%3A+From+CLI+to+console%2C+chasing+an+attacker+in+AWS)

[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fexpel.com%2Fblog%2Fincident-report-from-cli-to-console-chasing-an-attacker-in-aws%2F&title=Incident+report%3A+From+CLI+to+console%2C+chasing+an+attacker+in+AWS)

[](https://www.reddit.com/submit?url=https%3A%2F%2Fexpel.com%2Fblog%2Fincident-report-from-cli-to-console-chasing-an-attacker-in-aws%2F&title=Incident+report%3A+From+CLI+to+console%2C+chasing+an+attacker+in+AWS)

![Image 8: alt=""](https://expel.com/wp-content/uploads/2022/2022/04/thumbnail-500x300-a24-aws.png)

Recently, our SOC detected unauthorized access into one of our customer’s Amazon Web Services (AWS) environments. The attacker used a long-term access key to gain initial access. Once they got in, they were able to abuse the AWS Identity and Access Management (IAM) service to escalate privileges to administrative roles and create two new users and access keys — creating a foothold in their environment. However, we stopped them before the attacker was able to get any further.

In this post, we’ll walk you through how we spotted unauthorized access, the investigative steps we took to understand what the attacker did in AWS, and share our lessons learned and key takeaways from the incident.

## Quick background

Before we tell you how it went down, for this customer we’re ingesting AWS CloudTrail logs and applying our own custom detections. This customer did not have AWS GuardDuty enabled for their monitored AWS accounts — nor did we have any visibility beyond the AWS control plane.

## Our initial lead

Our first clue into the incident was an AWS alert based on CloudTrail logs for a console login from an IAM user originating from an atypical country.

From the AWS alert (screenshot below), our SOC was able to extract the following details about the console login:

*   The authentication originated from Indonesia
*   The type of AWS account was an IAM user
*   Multi-factor authentication (MFA) was not used for the authentication

![Image 9: AWS alert.](blob:http://localhost/444a53fb171dc01df822819aa6d098d5)

The details about the AWS console login prompted our SOC to ask the following questions:

*   Does this IAM user typically login from Indonesia?
*   Why is this IAM user authenticating to the console directly and not via an identity provider?
*   Why wasn’t MFA used?

These questions combined certainly raised our suspicion.

SOC pro-tip: IAM accounts typically have long-term access keys associated with them. You’ll see these long-term access keys start with “AKIA.” Most of the AWS incidents we detect were the result of a publicly exposed long-term access key.

The first step in our investigative process was to understand what happened after the successful AWS console login. We used one of our bots, [Ruxie™](https://expel.com/services/managed-detection-response/), to gain some more insight. As a quick refresher, our robot Ruxie (yes – we give our robots names) automates investigative workflows to surface up more details to our analysts.

We used Ruxie to list the most recent interesting API calls from the AWS account in the initial lead (interesting in this context is mostly anything that isn’t Get*, List*, Describe*, and Head*). API calls that are sometimes associated with attacker activities in AWS are highlighted in orange. We highlight these actions in orange to provide a visual cue to our analysts that something may be amiss here.

![Image 11: API list from a AWS alert with assistance of Ruxie. ](blob:http://localhost/a0b9003506b01b2157415e2b7b03b683)

The list of API calls returned by Ruxie showed us that the source IP address associated with the atypical console login also issued API calls to [CreateUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateUser.html), [CreateAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccessKey.html), and [AttachUserPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachUserPolicy.html). For the AWS defenders out there, it’s important to note that AWS accounts are assigned [temporary access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-unique-ids) when authenticating to the AWS console (these access keys typically start with “ASIA”).

Now this activity really has our attention. But why?

The CreateUser API call is used to create a new IAM user. The CreateAccessKey API call creates a new long-term access key for a specific user. AttachUserPolicy attaches a specified policy to a specified user.

Therefore, an attacker can use these API calls to:

*   Create a new IAM user
*   Create a new long-term access key for the user
*   Attach a highly privileged policy to the user for elevated access

This series of API calls can give an attacker persistent and elevated access in an AWS environment — yep, this activity certainly has our attention.

The next question our SOC asked was, “where does this IAM user typically authenticate from?” Ruxie to the rescue. Ruxie provided our analysts with a list of login activity by region and frequency for the IAM user listed in our lead alert.

Bottom line? Logins from Indonesia are highly suspicious.

![Image 13: Login activity by Ruxie.](blob:http://localhost/34a1f5258e5b3d91c7b52bc4abfc2bd1)

Recently authenticated regions Ruxie action for the source IAM user

OK, so at this point we have an IAM user logging in to the AWS console, from a location we’ve confirmed is atypical, and that account is issuing API calls to create new users, long-term access keys, and to attach highly privileged policies to users for elevated access.

At this point our SOC declared an incident, issued a recommendation to our customer to reset the (**arn:aws:iam::123456789012:user/comp_user1**) account credentials, and in parallel began working to answer:

*   How did the attacker obtain AWS console creds?
*   What else did the attacker do in AWS?

## How did the attacker obtain AWS console creds?

The next step in our investigative process was to get a more detailed timeline of all AWS API calls issued by the source IP address associated with the lead alert for the console login. This investigative step helps us better understand the actions performed by the attacker.

![Image 15: API calls in AWS triage timeline](blob:http://localhost/8a251718e6afbf060d0b9458b247fbe8)

API calls in AWS triage timeline

When examining the detailed timeline of API calls, the attacker first issued a [ListUsers API](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUsers.html) call using the **arn:aws:iam::123456789012:user/comp_user2** IAM user from the AWS command line interface (aws-cli). Note that this is a different IAM user from the lead alert. We inferred the **arn:aws:iam::123456789012:user/comp_user2** IAM user was also compromised since the API call originated from the same IP address recorded in the console login. More on this in a second.

Next, the attacker issued two calls to the [UpdateLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateLoginProfile.html) API; one for the **arn:aws:iam::123456789012:user/comp_user1** IAM user (succeeded) and one for the **arn:aws:iam::123456789012:user/comp_user2** IAM user (failed with the NoSuchEntityException reason).

 Finally, CloudTrail logs recorded a ConsoleLogin from the **arn:aws:iam::123456789012:user/comp_user1** account.

So as a quick recap, our investigation revealed the attacker took the following steps to gain access to the AWS console:

*   Used the AWS access keys for **arn:aws:iam::123456789012:user/comp_user2** to issue a ListUsers API call. 
    *   The results of the ListUsers API call returned **arn:aws:iam::123456789012:user/comp_user1** in the results.

*   Issued an API call to UpdateLoginProfile to change the AWS console password for the **arn:aws:iam::123456789012:user/comp_user1** account.
*   Authenticated into the AWS console using the **arn:aws:iam::123456789012:user/comp_user1**account.

It’s our working theory that the AWS access keys for the **arn:aws:iam::123456789012:user/comp_user2** account were discovered by the attacker in a publicly available code repository.

## What else did the attacker do in AWS?

SOC pro-tip: At this point in our investigation, CloudTrail logs indicate the attacker has access to the AWS console for this customer. Therefore, we’re expecting to see attacker activity recorded from different IP addresses associated with AWS. (Don’t exclude these in your search!)

Immediately following the authentication to the AWS console, the attacker issued the following API calls:

*   CreateUser
*   CreateAccessKey
*   AttachUserPolicy
*   [CreateLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateLoginProfile.html)

This allowed the attacker to create two new IAM users with accompanying long-term access keys and attached a policy that allowed one of the new users to create and change their AWS console password. For one of the newly created IAM user accounts, the attacker issued an AttachUserPolicy API call to attach an [AdministratorAccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator) policy to the newly created IAM user — allowing the attacker to elevate their privileges in AWS.

Lastly, the attacker used one of the newly created IAM users to make a call to the [RequestServiceQuotaIncrease](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/request-service-quota-increase.html) API in order to increase the EC2 quota. It’s our opinion that this action was taken in preparation for starting multiple large EC2 instances for cryptocurrency mining. It is at this point that we worked with the customer to begin remediation.

Crisis averted!

Here’s the final play-by-play of the actions taken by the attacker in AWS mapped to the MITRE ATT&CK framework:

![Image 17](blob:http://localhost/2ad3ad0069952af35f55b61c12501a2c)

MITRE tactics mapped to AWS API calls

You can check out additional AWS API calls we’ve seen associated with attacker activity in our [AWS mind map](https://expel.com/blog/mind-map-for-aws-investigations/).

## Remediation in AWS

With the scope of the compromise understood, we provided our customer with the following remediation recommendations:

1.   Delete the two created accounts and accompanying access keys for **arn:aws:iam::123456789012:user/created_user1**and **arn:aws:iam::123456789012:user/created_user2**
2.   Deactivate the long term access keys associated with the **arn:aws:iam::123456789012:user/comp_user1** and **arn:aws:iam::123456789012:user/comp_user2** IAM users
3.   Reset the AWS console password for the **arn:aws:iam::123456789012:user/comp_user1** and **arn:aws:iam::123456789012:user/comp_user2** IAM users

We also recommended that the customer ensure AWS access keys are not being accidentally released to the public and implement least privilege with regards to AWS users. Additionally, we recommended the customer implement MFA for IAM user AWS console authentications.

## Lessons learned

What stood out the most in this incident was the attacker’s technique to use an exposed long-term access key to gain access to the AWS console — potentially for ease of access and persistence. Simply put, the attacker wants to go from the aws-cli to the AWS console. To achieve this, the attacker issued API calls UpdateLoginProfile or CreateLoginProfile from an IAM user. We now have a detection based on CloudTrail logs that alerts our SOC anytime we see these specific API calls originating from an IAM user where the User-Agent is the aws-cli. We’ve added some additional logic to reduce benign noise associated with AWS IP addresses.

We’re also exploring additional detections based on CloudTrail logs where we see newly created IAM users issue API calls to [RequestServiceQuotaIncrease](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/request-service-quota-increase.html) to increase the EC2 quota. This could be a signal of potential unauthorized activity in EC2.

While we detected unauthorized activity early in the attack lifecycle, we’re a learning organization and always looking for opportunities to improve our detection and response capabilities in AWS.

Tags

[AWS](https://expel.com/blog/tag/aws/) / [tech stack](https://expel.com/blog/tag/tech-stack/) / [threat landscape](https://expel.com/blog/tag/threat-landscape/)

### Table of Contents

[Quick background](https://expel.com/blog/incident-report-from-cli-to-console-chasing-an-attacker-in-aws/#quick-background)

[Our initial lead](https://expel.com/blog/incident-report-from-cli-to-console-chasing-an-attacker-in-aws/#our-initial-lead)

[How did the attacker obtain AWS console creds?](https://expel.com/blog/incident-report-from-cli-to-console-chasing-an-attacker-in-aws/#how-did-the-attacker-obtain-aws-console-creds)

[What else did the attacker do in AWS?](https://expel.com/blog/incident-report-from-cli-to-console-chasing-an-attacker-in-aws/#what-else-did-the-attacker-do-in-aws)

[Remediation in AWS](https://expel.com/blog/incident-report-from-cli-to-console-chasing-an-attacker-in-aws/#remediation-in-aws)

[Lessons learned](https://expel.com/blog/incident-report-from-cli-to-console-chasing-an-attacker-in-aws/#lessons-learned)

![Image 19: thumbnail for Expel MDR demo](https://expel.com/wp-content/uploads/2026/03/mdr-demo-thumbnail-nb.png)

###### Expel MDR in action

See exactly how we find and eliminate threats before they become your problem.

[Watch a demo](https://expel.com/on-demand-mdr-demo/)

## Post navigation

[Last Previous](https://expel.com/blog/attack-trend-alert-email-scams-targeting-donations-to-ukraine/)

[Next Next](https://expel.com/blog/the-dinner-that-started-it-all-with-expels-new-ciso/)

[Blog home](https://expel.com/blog/)

## Related Articles

Previous

[![Image 20: Active exploitation notice: React2Shell critical vulnerability (CVE-2025-55182)](blob:http://localhost/346dadc7249b4f18bcd4f1d0d397bce6)](https://expel.com/blog/security-alert-axios-npm-supply-chain-attack/)

###### [Rapid response](https://expel.com/blog/category/rapid-response/)

[### Security alert: Axios npm supply chain attack](https://expel.com/blog/security-alert-axios-npm-supply-chain-attack/)
The Axios npm package suffered a supply chain attack from March 30-31. The malicious packages are no longer active, but here's what you need to know.

[![Image 22: Active exploitation notice: React2Shell critical vulnerability (CVE-2025-55182)](blob:http://localhost/346dadc7249b4f18bcd4f1d0d397bce6)](https://expel.com/blog/notepad-supply-chain-incident/)

###### [Rapid response](https://expel.com/blog/category/rapid-response/)

[### Notepad++ supply chain incident](https://expel.com/blog/notepad-supply-chain-incident/)
The developer of Notepad++ disclosed an incident where actors identified a means to tamper with the delivery of automatic updates.

[![Image 24: Active exploitation notice: React2Shell critical vulnerability (CVE-2025-55182)](blob:http://localhost/346dadc7249b4f18bcd4f1d0d397bce6)](https://expel.com/blog/security-alert-critical-unauthenticated-rce-vulnerabilities-in-ivanti-epmm/)

###### [Rapid response](https://expel.com/blog/category/rapid-response/)

[### Security alert: Critical unauthenticated RCE vulnerabilities in Ivanti EPMM](https://expel.com/blog/security-alert-critical-unauthenticated-rce-vulnerabilities-in-ivanti-epmm/)
Two zero-day command injection vulnerabilities affecting Ivanti EPMM are currently being actively exploited: CVE-2026-1281 and CVE-2026-1340.

[![Image 26: Active exploitation notice: React2Shell critical vulnerability (CVE-2025-55182)](blob:http://localhost/346dadc7249b4f18bcd4f1d0d397bce6)](https://expel.com/blog/active-exploitation-notice-react2shell-critical-vulnerability-cve-2025-55182/)

###### [Rapid response](https://expel.com/blog/category/rapid-response/)

[### Active exploitation notice: React2Shell critical vulnerability (CVE-2025-55182)](https://expel.com/blog/active-exploitation-notice-react2shell-critical-vulnerability-cve-2025-55182/)
A React2Shell critical vulnerability (CVE-2025-55182) is under active exploitation. Here's what you need to know and how to identify it.

Next

[View All Articles](https://expel.com/blog/)

![Image 28: logo-linkedin--Streamline-Pixel](blob:http://localhost/e8a57f4972516a1d3218894eabc89576)

12950 Worldgate Drive, Suite 200

 Herndon, VA 20170

[(844) 397-3524](tel:8443973524)

[![Image 30: logo-linkedin--Streamline-Pixel](blob:http://localhost/e8a57f4972516a1d3218894eabc89576)](https://twitter.com/ExpelSecurity)[![Image 32: logo-linkedin--Streamline-Pixel](blob:http://localhost/e8a57f4972516a1d3218894eabc89576)](https://youtube.com/@expelsecurity)[![Image 34: logo-linkedin--Streamline-Pixel](blob:http://localhost/e8a57f4972516a1d3218894eabc89576)](https://www.linkedin.com/company/expel)

#### Why Expel

*   [Why Expel?](https://expel.com/why-expel/)
*   [Tech integrations](https://expel.com/integrations/)
*   [Customers](https://expel.com/customers/)
*   [Plans & Packages](https://expel.com/mdr-packages/)

#### Services & Platform

*   [Managed Detection and Response (MDR)](https://expel.com/services/managed-detection-response/)
*   [Managed SIEM](https://expel.com/services/managed-siem/)
*   [Phishing](https://expel.com/services/phishing/)
*   [Threat hunting](https://expel.com/services/threat-hunting/)
*   [24×7 Security Operations](https://expel.com/security-operations-center-soc/)
*   [AI & Automation Engine](https://expel.com/ai-automation/)
*   [Workbench™ Operations Platform](https://expel.com/workbench-operations-platform/)

#### Company

*   [About us](https://expel.com/about/)
*   [Equity, Inclusion & Diversity](https://expel.com/about/eid/)
*   [Careers](https://expel.com/about/careers/)
*   [Newsroom](https://expel.com/about/newsroom/)
*   [Resources](https://expel.com/resources/)
*   [Blog](https://expel.com/blog/)
*   [Webinars](https://expel.com/webinars/)
*   [Cyberspeak glossary](https://expel.com/cyberspeak/)
*   [Expel Intel](https://expel.com/intel/)

#### Solutions

*   [Security data lake](https://expel.com/solutions/security-data-lake/)
*   [Cloud](https://expel.com/solutions/cloud-security/)
*   [Email](https://expel.com/solutions/email-threat-detection/)
*   [Endpoint](https://expel.com/solutions/endpoint-security-monitoring/)
*   [Identity](https://expel.com/solutions/identity-security/)
*   [Network](https://expel.com/solutions/secure-company-network/)
*   [SaaS](https://expel.com/solutions/secure-saas-applications/)
*   [SIEM](https://expel.com/solutions/optimize-your-siem-security/)
*   [Amazon Web Services (AWS)](https://expel.com/solutions/aws-cloud-security/)
*   [Google Cloud](https://expel.com/solutions/google-cloud-security/)
*   [Kubernetes](https://expel.com/solutions/kubernetes-mdr-security/)
*   [Microsoft](https://expel.com/solutions/microsoft-mdr-security/)
*   [Oracle Cloud Infrastructure (OCI)](https://expel.com/solutions/oracle-cloud-security/)

Also of Interest

*   [AWS MITRE ATT&CK: Expel Mind Map Kit](https://expel.com/mitre-attack-in-aws-toolkit/)
*   [GCP Incident report: Spotting an attacker in...](https://expel.com/blog/incident-report-spotting-an-attacker-in-gcp/)
*   [Compromised AWS Access Keys](https://expel.com/resource/inside-an-investigation-compromised-aws-access-keys/)

[Privacy](https://expel.com/notices/) | [Compliance](https://expel.com/security-compliance/) | [Terms](https://expel.com/terms-of-use/) | [EMEA Reseller Customer Terms](https://expel.com/terms-of-use/reseller-customers-emea/) | [North America Reseller Customer Terms](https://expel.com/terms-of-use/reseller-customers-north-america/) | [System Status](https://status.expel.io/) | Cookie settings

© 2026 Expel, Inc. All Rights Reserved