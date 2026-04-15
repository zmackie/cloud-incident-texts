---
title: Timehop discloses July 4 data breach affecting 21 million
url: "https://techcrunch.com/2018/07/09/timehop-discloses-july-4-data-breach-affecting-21-million/"
author: Natasha Lomas
published: 2018-07-09
source_type: article
source_domain: techcrunch.com
cleanup_method: llm
---

# Timehop discloses July 4 data breach affecting 21 million

[Natasha Lomas](https://techcrunch.com/author/natasha-lomas/)

2:08 AM PDT · July 9, 2018


[Timehop](https://techcrunch.com/tag/timehop/)has disclosed a security breach that has compromised the personal data (names and emails) of 21 million users (essentially its entire user base). Around a fifth of the affected users — or 4.7M — have also had a phone number that was attached to their account breached in the attack.

The startup, whose service plugs into users’ social media accounts to resurface posts and photos they may have forgotten about, says it discovered the attack while it was in progress,at 2:04 US Eastern Time on July 4, and was able to shut it down two hours, 19 minutes later — albeit, not before millions of people’s data had been breached.

According to its preliminary [investigation](https://www.timehop.com/security/technical) of the incident, the attacker first accessed Timehop’s cloud environment in December — using compromised admin credentials, and apparently conducting reconnaissance for a few days that month, and again for another day in March and one in June, before going on to launch the attack on July 4, during a US holiday.

Timehop publicly disclosed the breach in a [blog post](https://www.timehop.com/security)on Saturday, several days after discovering the attack.

It says no social media content, financial data or Timehop data was affected by the breach — and its blog post emphasizes that none of the content its service routinely lifts from third party social networks in order to present back to users as digital “memories” was affected.

However the keys that allow it to read and show users their social media content were compromised — so it has all keys deactivated, meaning Timehop users will have to re-authenticate to its App to continue using the service.

“If you have noticed any content not loading, it is because Timehop deactivated these proactively,” it writes, adding: “We have no evidence that any accounts were accessed without authorization.”

It does also admit that the tokens could “theoretically” have been used for unauthorized users to access Timehop users’ own social media posts during “a short time window” — although again it emphasizes “we have no evidence that this actually happened”.

“We want to be clear that these tokens do not give anyone (including Timehop) access to Facebook Messenger, or Direct Messages on Twitter or Instagram, or things that your friends post to your Facebook wall. In general, Timehop only has access to social media posts you post yourself to your profile,” it adds.

“The damage was limited because of our long-standing commitment to only use the data we absolutely need to provide our service. Timehop has never stored your credit card or any financial data, location data, or IP addresses; we don’t store copies of your social media profiles, we separate user information from social media content — and we delete our copies of your “Memories” after you’ve seen them.”

In terms of how its network was accessed, it appears that the attacker was able to compromise Timehop’s cloud computing environment by targeting an account that had not been protected by multifactor authentication.

That’s very clearly a major security failure — but one Timehop does not explicitly explain, writing only that:“We have now taken steps that include multifactor authentication to secure our authorization and access controls on all accounts.”

Part of its formal incident response, which it says began on July 5, was also to add multifactor authentication to “all accounts that did not already have them for all cloud-based services (not just in our Cloud Computing Provider)”.So evidently there was more than one vulnerable account for attackers to target.

Its exec team will certainly have questions to answer about why multifactor authentication was not universally enforced for all its cloud accounts.

For now, by way of explanation, it writes: “There is no such thing as perfect when it comes to cyber security but we are committed to protecting user data. As soon as the incident was recognized we began a program of security upgrades.” Which does have a distinct ‘stable door being locked after the horse has bolted’ feel to it.

It also writes that it carried out “the introduction of more pervasive encryption throughout our environment” — so, again, questions should be asked why it took an incident response to trigger a “more pervasive” security overhaul.

Also not entirely clear from Timehop’s blog post: When/if affected users were notified their information has been breached.

The company posed the blog post disclosing the security breach to its Twitter account [on July 8](https://twitter.com/timehop/status/1016090564427681792).But prior to that its Twitter account was only noting that some “unscheduled maintenance” might be causing problems for users accessing the app…

> We are currently doing some unscheduled maintenance on Timehop. You may have some issues accesing the app until further notice. Please follow this account for updates. Thank you for your patience!
> 
> 
> — Timehop (@timehop) [July 8, 2018](https://twitter.com/timehop/status/1015965323986694144?ref_src=twsrc%5Etfw)

> UPDATE: maintenance is still in progress. You can expect ongoing outages as we complete this work. Apologies for any inconvenience
> 
> 
> — Timehop (@timehop) [July 8, 2018](https://twitter.com/timehop/status/1016069919971201024?ref_src=twsrc%5Etfw)

We’ve reached out to the company with questions and will update this post with any response.**Update:**A Timehop spokesman says individual users are being notified as they log back in to the app.

“An email to the entire user base is in the works for today,” he tells TechCrunch. “[It] took some time to get our send grid account ready for that many emails as we are not a big email sender in general.”

In terms of the reasons behind the multifactor fail, the spokesman said it’s still investigating why there was a security lapse “as we do in general make use of it”. “But this employee was here for so long, from back when we were just a baby company, so it seems something got overlooked,” he adds.

In its blog about the incident, Timehop says that at the same time as it was working to shut down the attack and tighten up security,company executives contacted local and federal law enforcement officials — presumably to report the breach.

Breach reporting requirements are baked into Europe’s recently updated data protection framework, the [GDPR](https://techcrunch.com/2018/01/20/wtf-is-gdpr/), which puts the onus firmly on data controllers to disclose breaches to supervisory authorities — and to do so quickly — with the regulation setting a universal standard of within 72 hours of becoming aware of it (unless the personal data breach is unlikely to result in “a risk to the rights and freedoms of natural persons”).

Referencing GDPR, Timehop writes: “Although the GDPR regulations are vague on a breach of this type (a breach must be “likely to result in a risk to the rights and freedoms of the individuals”), we are being pro-active and notifying all EU users and have done so as quickly as possible. We have retained and have been working closely with our European-based GDPR specialists to assist us in this effort.”

The company also writes that it has engaged the services of an (unnamed)cyber threat intelligence company to look for evidence of use of the email addresses, phone numbers, and names of users being posted or used online and on the Dark Web — saying that “while none have appeared to date, it is a high likelihood that they will soon appear”.

Timehop users who are worried the network intrusion and data breach might have impact their “Streak” — aka the number Timehop displays to denote how many consecutive days they have opened the app — are being reassured by the company that “we will ensure all Streaks remain unaffected by this event”.
