---
title: A recent security incident involving Dropbox Sign
url: "https://sign.dropbox.com/blog/a-recent-security-incident-involving-dropbox-sign"
author: Dropbox Sign team
published: 2024-06-21
source_type: article
source_domain: sign.dropbox.com
cleanup_method: llm
---

# A recent security incident involving Dropbox Sign

by

Dropbox Sign team

June 21, 2024

_On April 24th, we became aware of unauthorized access to the Dropbox Sign (formerly HelloSign) production environment. Upon further investigation, we discovered that a threat actor had accessed Dropbox Sign customer information. We believe that this incident was isolated to Dropbox Sign infrastructure, and did not impact any other Dropbox products. We’ve reached out to all users impacted by this incident who needed to take action, with step-by-step instructions on how to further protect their data. Our security team also reset users’ passwords, logged users out of any devices they had connected to Dropbox Sign, and is coordinating the rotation of all API keys and OAuth tokens. Please read on for additional details and an FAQ._

On April 24th, we became aware of unauthorized access to the Dropbox Sign (formerly HelloSign) production environment. Upon further investigation, we discovered that a threat actor had accessed data including Dropbox Sign customer information such as email addresses, user names, phone numbers and hashed passwords, in addition to general account settings and certain authentication information such as API keys, OAuth tokens, and multi-factor authentication.

For those who received or signed a document through Dropbox Sign, but never created an account, email addresses and names were also exposed. Additionally, if you created a Dropbox Sign or HelloSign account, but did not set up a password with us (e.g. “Sign up with Google”), no password was stored or exposed.

Our investigation has concluded, and we found no evidence of unauthorized access to the contents of customers’ accounts (i.e. their documents or agreements), or their payment information.

From a technical perspective, Dropbox Sign’s infrastructure is largely separate from other Dropbox services. That said, we thoroughly investigated this risk and all available evidence indicates that this incident was isolated to Dropbox Sign infrastructure, and did not impact any other Dropbox products.

## What happened and our response

When we became aware of this issue, we launched an investigation with industry-leading forensic investigators to understand what happened and mitigate risks to our users.

Based on our investigation, a third party gained access to a Dropbox Sign automated system configuration tool. The actor compromised a service account that was part of Sign’s back-end, which is a type of non-human account used to execute applications and run automated services. As such, this account had privileges to take a variety of actions within Sign’s production environment. The threat actor then used this access to the production environment to access our customer database.

In response, our security team reset users’ passwords, logged users out of any devices they had connected to Dropbox Sign, and is helping customers rotate all API keys and OAuth tokens. We reported this event to data protection regulators and law enforcement.

## What we’re doing next

At Dropbox, our number one value is to be worthy of trust. We hold ourselves to a high standard when protecting our customers and their content. We didn’t live up to that standard here, and we’re deeply sorry for the impact it caused our customers.

After discovering this incident, we worked around the clock to mitigate risk to our customers. We reached out to all users impacted by this incident who need to take action, with step-by-step instructions on how to further protect their data.

We’ve concluded our investigation of this incident, and are conducting an extensive review to understand how we can protect against this kind of threat in the future. We are grateful for our customers’ partnership, and we’re here to help all of those who were impacted by this incident.

To contact us about this incident, please reach out to us [here](https://faq.hellosign.com/hc/en-us/requests/new).

## Customer FAQ

**I’m a Sign customer - what has Dropbox done to protect me and what do I need to do?**

*   Along with our forensic investigation vendor, we concluded our investigation of this incident. We found no evidence of unauthorized access to the contents of users’ accounts (i.e. their documents or agreements).
*   We’ve expired your password and logged you out of any devices you had connected to Dropbox Sign to further protect your account. The next time you log in to your Sign account, you’ll be sent an email to reset your password. We recommend you do this as soon as possible.
*   If you’re an API customer, to ensure the security of your account, you’ll need to rotate your API key by generating a new one, configuring it with your application, and **deleting**your current one. As an additional precaution, we’ll be restricting certain functionality of API keys while we coordinate rotation. **_Only_** signature requests and signing capabilities will continue to be operational for your business continuity. Once you rotate your API keys, restrictions will be removed and the product will continue to function as normal. [Here](https://developers.hellosign.com/api/reference/authentication/#generate-new-api-key) is how you can easily create a new key.
*   Customers who use an authenticator app for multi-factor authentication should [reset](https://faq.hellosign.com/hc/en-us/articles/360025164091-Two-Factor-Authentication-Google-Authenticator) it. Please delete your existing entry and then reset it. If you use SMS, you do not need to take any action.
*   If you reused your Dropbox Sign password on any other services, we strongly recommend that you change your password on those accounts and utilize multi-factor authentication when available.

**If I have a Sign account linked to my Dropbox account, is my Dropbox account affected?**

*   No. Based on the investigation and all available evidence, this incident was isolated to Dropbox Sign infrastructure, and did not impact any other Dropbox products.
*   However, if you reused your Dropbox Sign password on any other services, we strongly recommend that you change your password on those accounts and utilize multi-factor authentication when available. Instructions on how to do this for your Dropbox Sign account can be found [here](https://faq.hellosign.com/hc/en-us/articles/360025164091-Two-Factor-Authentication-Google-Authenticator). 

**I’m a Sign API customer. Was my customers’ data exposed as well?**

*   Names and email addresses for those who received or signed a document through Dropbox Sign, but never created an account, were exposed. 

**How have you communicated about this incident?**

*   We reached out to all impacted users who needed to take action. All users who had authentication-related data exposed (i.e., hashed password or API keys) have been notified.
*   For the vast majority of users affected by this incident, the only data exposed was name, email address, and basic account data. We have not contacted users who had no authentication-related data exposed.
*   While we’re confident we understand the full scope of this incident at this time, if we determine that other types of personal information were compromised, we will promptly notify impacted customers or update this post as appropriate.

**I’m an API customer, what more can I do to review activity on my account?**

*   We’ve begun rolling out new Admin reporting features within the Dropbox Sign product. We’ve already made it easier for customers to generate a compliance report encompassing all their API keys linked to their team’s accounts requiring rotation (specifically, deletion of all API keys generated before May 1, 2024, 1:30PM PT, and subsequent creation of new API keys). [Learn more](https://developers.hellosign.com/docs/reports/overview/).
*   On May 15, 2024, we rolled out two additional compliance reports: _Log In Activity_ and _API Call Activity_.
    *   With the _Log In Activity_ report, you’ll be able to effortlessly audit the Dropbox Sign log in activity for all your accounts. This includes details like the log in type, IP address, and device used.
    *   The _API Call Activity_ report will empower you to track every API call made by all your accounts. You’ll have insights into crucial information such as the IP address and user agent used for each API request.

**Have you notified data protection regulators?**

*   Yes. We notified our lead supervisory authority in the EU, the Irish Data Protection Commission. We are also in contact with other regulators as appropriate.

**Is your investigation complete?**

*   Yes.

**How did the threat actor get access?**

*   Using an access token that had been compromised.

**When did the threat actor first gain access?**

*   Based on our investigation, we believe that the threat actor first gained access on April 19, 2024.

**When was the last observed threat actor activity?**

*   April 20, 2024.

**Was this a ransomware event?**

*   No. We have not detected any malware being introduced into our system.

**What preventative measures is Dropbox taking to reduce the risk of this kind of incident?**

*   We’re conducting a thorough review of this incident and are in the process of implementing additional technical measures designed to reduce the likelihood of this type of event from reoccurring. Given that these are security measures, we cannot disclose them in detail.


_May 3, 2024 update: edited list of customer information to clarify that email addresses were involved, not emails._

_June 21, 2024 update: updated to reflect that our investigation has concluded. We expect this to be our final update._
