---
title: Disclosure of Security Incidents on imToken
url: "https://archive.ph/bRjXi"
author: Ben
published: 2018-06-09
source_type: archive
source_domain: archive.ph
cleanup_method: llm
---

# Disclosure of Security Incidents on imToken


**Security Level:** Medium

**Affected version:** 2.0 Beta/RC version

**Affected users:** Users having installed 2.0 Beta version starting from March 21, 2018 to 10:30am June 9, 2018 (UTC+8)

**Overview of the incident:** the hackers reset passwords through emails and obtained the Amazon AWS web account for our 2.0 Beta server. After discovering the unusual incident, our operation and maintenance staff immediately cut it off, and analyze and assess such incident with our security expert - SlowMist team.**Based on the assessment, it was a security breach by hackers, but as**imToken**is a decentralized wallet, it would not cause any risk to your assets, however,the hacker may have obtained certain device data of 2.0 Beta testers.**

#### **Description of the Incident**

At 02:11 am 9 June 2018 (UTC+8), an anonymous user reset our log-in password of Amazon AWS by e-mail, where our 2.0 Beta servers are hosted. At 10:00 am 9 June 2018 (UTC+8), our operation and maintenance staff found the unusual incident and cut off the connection to AWS, the Company has established the emergency team and worked with security team - SlowMist team - to investigate and assess the incident.

#### **Analysis of Cause**

Being a decentralized wallet service provider with a large user base, imToken has been the prime target for attacks including Phishing, Sniffing, Challenge Collapsar, and DDOS. imToken team has always been prepared for attacks in the past but unfortunately, email account exposed imToken to our first ever security breach. The emergency response team is currently investigating the root cause of the hack on email account, which subsequently enabling the hackers to gain access to our AWS account.

**Emergency Response Plan**

Upon discovery of the intrusion, the Company set-up an emergency response team consisting of 14 members to strategise on the immediate course of actions.

*   Terminated access to AWS, reset passwords and authorisation setting on all services.

*   Collaboration with SlowMist, a third party professional security auditing team to investigate the cause of the incident.

*   All employees executed self-inspection on risk exposure, resetting passwords and authorisation setting on all devices under the scrutiny of our Chief Security Officer.

*   Comprehensive assessment of scope of risk exposures, preparation for course of actions.

#### **Impact on users and response measures**

Affected users are limited to those who have installed our 2.0 Beta international version, totaling 36,000 devices, 73,000 corresponding wallet addresses and 10,000 subscribed emails.Device ID is an anonymous information and the wallet address is a public information on the blockchain system, both of which can’t cause damages to the users.The only thing the hacker can use is the subscribed email address.Therefore, the worst scenario would be that, after obtaining such data, the hacker may send “Phishing emails” to users, and thus we have already sent anti-Phishing emails warning to the affected users: “Please note that, you shall not disclose private key of your wallet to anyone and by doing this, you can safely control your assets.”

#### **Importance of Security**

We regretfully apologise for this incident as wallet security has always been our top priority. We are making progress in many aspects to build a better imToken, including software structure architecture, decentralized mechanisms, users education, comprehensive testing and assessments, internal protocol implementations and risk management. This incident has reminded us to strive to make a better imToken, facilitating free flow of value without compromising on the security of assets.

**Some of the security implementations from imToken**

*   Deeper collaboration with security experts like SlowMist and Cure53.

*   Open Source: open sourcing the core codes of imToken after second round audit by Cure53 (a German security audit team).

*   Bug Bounty: imToken will launch a bug bounty program, encouraging white hats to participate and help improve the security of imToken wallet.

*   Information Alliance: forming an alliance with industry partners, leveraging on different expertises to build up a shared risk database, strive to discover, inform and resolve potential risks in the industry.

If you require further clarifications or have any comment, please let us know via support@token.im.

Ben,

Founder and CEO of imToken
