Title: Security update

URL Source: https://www.uber.com/newsroom/security-update/

Published Time: Tue, 14 Apr 2026 18:53:47 GMT

Markdown Content:
# Security update

[Skip to main content](https://www.uber.com/newsroom/security-update/#main)

[Uber Newsroom](https://www.uber.com/us/en/newsroom/)
*   [News](https://www.uber.com/us/en/newsroom/)
*   [About us](https://www.uber.com/us/en/about/)
*   [Leadership](https://www.uber.com/us/en/about/leadership/)
*   [Media assets](https://assets.uber.com/d/k4nuxdZ8MC7E)
*   More 

    *   No results

*    EN
*   [Help](https://help.uber.com/)
*   [Log in](https://auth.uber.com/login-redirect?next_url=https://www.uber.com)
*   Sign up[Ride![Image 1: undefined](https://tb-static.uber.com/prod/udam-assets/80bb7bdd-6cf4-4053-94c5-2e4e53d9d5f6.svg)](https://m.uber.com/looking/)[Drive & deliver![Image 2: undefined](https://tb-static.uber.com/prod/udam-assets/d4ca3837-f9df-473b-9099-85505187cb2a.svg)](https://drivers.uber.com/)[Uber Eats![Image 3: undefined](https://tb-static.uber.com/prod/udam-assets/839bd4f4-306c-4b1b-b0e8-ab9cc8fd65c7.svg)](https://ubereats.com/login-redirect/)[Business![Image 4: undefined](https://tb-static.uber.com/prod/udam-assets/0d73ead7-7739-4bb3-b79b-ded048dba1e1.svg)](https://business.uber.com/)  

[Uber Newsroom](https://www.uber.com/us/en/newsroom/)
*   [Log in](https://auth.uber.com/login-redirect?next_url=https://www.uber.com)
*   Sign up[Ride![Image 5: undefined](https://tb-static.uber.com/prod/udam-assets/80bb7bdd-6cf4-4053-94c5-2e4e53d9d5f6.svg)](https://m.uber.com/looking/)[Drive & deliver![Image 6: undefined](https://tb-static.uber.com/prod/udam-assets/d4ca3837-f9df-473b-9099-85505187cb2a.svg)](https://drivers.uber.com/)[Uber Eats![Image 7: undefined](https://tb-static.uber.com/prod/udam-assets/839bd4f4-306c-4b1b-b0e8-ab9cc8fd65c7.svg)](https://ubereats.com/login-redirect/)[Business![Image 8: undefined](https://tb-static.uber.com/prod/udam-assets/0d73ead7-7739-4bb3-b79b-ded048dba1e1.svg)](https://business.uber.com/)  

September 16, 2022

Security update

![Image 9: Uber Team](https://www.uber.com/newsroom/security-update/)

UT

Uber Team

**September 19, 10:45am PT**

While our investigation is still ongoing, we are providing an update on our response to last week’s security incident.

**What happened?**

An Uber EXT contractor had their account compromised by an attacker. It is likely that the attacker purchased the contractor’s Uber corporate password on the dark web, after the contractor’s personal device had been infected with malware, exposing those credentials. The attacker then repeatedly tried to log in to the contractor’s Uber account. Each time, the contractor received a two-factor login approval request, which initially blocked access. Eventually, however, the contractor accepted one, and the attacker successfully logged in.

From there, the attacker accessed several other employee accounts which ultimately gave the attacker elevated permissions to a number of tools, including G-Suite and Slack. The attacker then posted a message to a company-wide Slack channel, which many of you saw, and reconfigured Uber’s OpenDNS to display a graphic image to employees on some internal sites.

**How did we respond?**

Our existing security monitoring processes allowed our teams to quickly identify the issue and move to respond. Our top priorities were to make sure the attacker no longer had access to our systems; to ensure user data was secure and that Uber services were not affected; and then to investigate the scope and impact of the incident.

Here are some of the key actions we took, and continue to take:

*   We identified any employee accounts that were compromised or potentially compromised and either blocked their access to Uber systems or required a password reset.
*   We disabled many affected or potentially affected internal tools.
*   We rotated keys (effectively resetting access) to many of our internal services.
*   We locked down our codebase, preventing any new code changes.
*   When restoring access to internal tools, we required employees to re-authenticate. We are also further strengthening our multi-factor authentication (MFA) policies.
*   We added additional monitoring of our internal environment to keep an even closer eye on any further suspicious activity.

**What was the impact?**

The attacker accessed several internal systems, and our investigation has focused on determining whether there was any material impact. While the investigation is still ongoing, we do have some details of our current findings that we can share.

First and foremost, we’ve not seen that the attacker accessed the production (i.e. public-facing) systems that power our apps; any user accounts; or the databases we use to store sensitive user information, like credit card numbers, user bank account info, or trip history. We also encrypt credit card information and personal health data, offering a further layer of protection.

We reviewed our codebase and have not found that the attacker made any changes. We also have not found that the attacker accessed any customer or user data stored by our cloud providers (e.g. AWS S3). It does appear that the attacker downloaded some internal Slack messages, as well as accessed or downloaded information from an internal tool our finance team uses to manage some invoices. We are currently analyzing those downloads.

The attacker was able to access our dashboard at HackerOne, where security researchers report bugs and vulnerabilities. However, any bug reports the attacker was able to access have been remediated.

Throughout, we were able to keep all of our public-facing Uber, Uber Eats, and Uber Freight services operational and running smoothly. Because we took down some internal tools, customer support operations were minimally impacted and are now back to normal.

**Who is responsible?**

We believe that this attacker (or attackers) are affiliated with a hacking group called [Lapsus$](https://www.theverge.com/22998479/lapsus-hacking-group-cyberattacks-news-updates), which has been increasingly active over the last year or so. This group typically uses similar techniques to target technology companies, and in 2022 alone has breached Microsoft, Cisco, Samsung, Nvidia and Okta, among others. There are also [reports](https://www.techmeme.com/220918/p7#a220918p7) over the weekend that this same actor breached video game maker Rockstar Games. We are in close coordination with the FBI and US Department of Justice on this matter and will continue to support their efforts.

**Where do we go from here?**

We’re working with several leading digital forensics firms as part of the investigation. We will also take this opportunity to continue to strengthen our policies, practices, and technology to further protect Uber against future attacks.

* * *

**September 16, 10:30am PT**

While our investigation and response efforts are ongoing, here is a further update on yesterday’s incident:

*   We have no evidence that the incident involved access to sensitive user data (like trip history).
*   All of our services including Uber, Uber Eats, Uber Freight, and the Uber Driver app are operational.
*   As we shared yesterday, we have notified law enforcement.
*   Internal software tools that we took down as a precaution yesterday are coming back online this morning.

* * *

**September 15, 6:25pm PT**

We are currently responding to a cybersecurity incident. We are in touch with law enforcement and will post additional updates here as they become available.

Category

Safety

Related Articles

6 articles

![Image 10](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8xZjA0M2E3Ni04Y2Y2LTUyYTctOWMwYS1kM2I0NThiMDM5N2IuanBn)

Safety

[Driving Change: Moving Forward Together](https://www.uber.com/us/en/newsroom/driving-change-moving-forward/)

December 11, 2025

[](https://www.uber.com/us/en/newsroom/driving-change-moving-forward/)

![Image 11](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy84ZDEzMmNiOC0yMTgwLTVkM2ItOTI2OS0zYjcwMzFhYzU4N2EuanBn)

Safety

[Strengthening our processes to verify driver and courier identity in the US](https://www.uber.com/us/en/newsroom/courier-identity-us/)

October 16, 2025

[](https://www.uber.com/us/en/newsroom/courier-identity-us/)

![Image 12](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy81ZmE3NDdlYS0wYTlmLTRjOWYtOTRhOC1hNDUyMjlhNjBlYjkucG5n)

Safety

[Uber’s record on safety is clear](https://www.uber.com/us/en/newsroom/ubers-safety-record/)

August 6, 2025

[](https://www.uber.com/us/en/newsroom/ubers-safety-record/)

![Image 13](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy8xZDAwZDgxYS1jMDdmLTVhZDQtOTI3YS03ZjM3NGVlNzM1MTYuanBn)

Safety

[Coming Soon: Women Preferences](https://www.uber.com/us/en/newsroom/women-preferences/)

July 23, 2025

[](https://www.uber.com/us/en/newsroom/women-preferences/)

![Image 14](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy81YzQ4NmEwZS1lOGI5LTU4NjEtOTRlOS1jODhkZmMyZmRiMDAucG5n)

Safety

[Hope Rides: Uber and Alliance for HOPE International Partner to Help Survivors Access Support](https://www.uber.com/us/en/newsroom/hope-rides-uber-and-alliance-for-hope-international/)

July 23, 2025

[](https://www.uber.com/us/en/newsroom/hope-rides-uber-and-alliance-for-hope-international/)

![Image 15](https://cn-geo1.uber.com/image-proc/crop/resizecrop/udam/format=auto/width=407/height=0/srcb64=aHR0cHM6Ly90Yi1zdGF0aWMudWJlci5jb20vcHJvZC91ZGFtLWFzc2V0cy80N2Q0NDYzMy05YmE5LTQ0YWQtYmYzOC01NDMxNmY1OGYxZjEucG5n)

Safety

[St. Louis Tornado Emergency Response](https://www.uber.com/us/en/newsroom/st-louis-tornado-emergency-response/)

June 7, 2025

[](https://www.uber.com/us/en/newsroom/st-louis-tornado-emergency-response/)

## Select your preferred language

[English](https://www.uber.com/us/en/newsroom/security-update/)

*   [News](https://www.uber.com/us/en/newsroom/)  
*   [About us](https://www.uber.com/us/en/about/)  

*   [Leadership](https://www.uber.com/us/en/about/leadership/)  
*   [Media assets](https://assets.uber.com/d/k4nuxdZ8MC7E)  
*   [Help](https://help.uber.com/)  

EN

## Select your preferred language

[English](https://www.uber.com/us/en/newsroom/security-update/)

[## Ride](https://m.uber.com/looking/)

[## Drive & deliver](https://drivers.uber.com/)

[## Uber Eats](https://ubereats.com/login-redirect/)

[## Business](https://business.uber.com/)

[## Drive & deliver](https://drivers.uber.com/)

[## Ride](https://m.uber.com/login-redirect)

[## Uber Eats](https://ubereats.com/login-redirect/)

[## Uber for Business](https://business.uber.com/)

[## Manage account](https://account.uber.com/)

[## Sign out](https://auth.uber.com/login/logout)