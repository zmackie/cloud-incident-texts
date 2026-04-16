---
title: Subpoena tracking platform blames outage on AWS social engineering attack
url: "https://www.theregister.com/2025/10/02/subpoena_tracking_platform_outage_blamed/"
author: Connor Jones
published: 2025-10-02
source_type: article
source_domain: www.theregister.com
cleanup_method: llm
---

# Subpoena tracking platform blames outage on AWS social engineering attack
## Software maker Kodex said its domain registrar fell for a fraudulent legal order

![Image 11: icon](https://www.theregister.com/design_picker/d518b499f8a6e2c65d4d8c49aca8299d54b03012/graphics/icon/vulture_red.svg)[Connor Jones](https://www.theregister.com/Author/Connor-Jones "Read more by this author")

 Thu 2 Oct 2025  //  17:04 UTC 

A software platform used by law enforcement agencies and major tech companies to manage subpoenas and data requests went dark this week after attackers socially engineered AWS into freezing its domain.

Kodex Global said its website, portal, API, and some email services were rendered unavailable on October 1 between 08:54-12:47 EDT. AWS is the domain registrar for Kodex Global.

[![Image 13: guy in suit talks on phone outside office](https://regmedia.co.uk/2022/09/28/shutterstock_haha_business.jpg?x=174&amp;y=115&amp;crop=1) ## 'Impersonation as a service' the next big thing in cybercrime READ MORE](https://www.theregister.com/2025/08/21/impersonation_as_a_service/)

While Kodex didn't explicitly name AWS in its [public update](https://www.kodexglobal.com/update-of-outage-on-october-1-2025) on the outage, [cyber sleuths](https://x.com/vxdb/status/1973374428869280232) identified that attackers attempted to transfer the domain to a different registrar.

"While threat actors claimed responsibility for the disruption, ownership was never transferred; it was the registrar who improperly froze our domain as a result of the fraudulent legal order," the company [claimed](https://www.kodexglobal.com/update-of-outage-on-october-1-2025).

"No credentials were compromised, no customer data was accessed, and Kodex itself was never breached. At no point did the threat actors have access to, or compromise the confidentiality of, customer data or internal systems."

A spokesperson at AWS told _The Register_: "We quickly resolved the matter as soon as we were made aware of the error and are taking steps to ensure that it doesn't happen again."

If the attackers had been more successful, the potential consequences could have seen them intercept Kodex's emails, potentially accessing sensitive information, or taking control of accounts with access to [MFA](https://www.theregister.com/2025/06/17/aws_enforces_mfa_root_users/) authentication resets, among other things.

*   [AWS forms EU-based cloud unit as customers fret about Trump 2.0](https://www.theregister.com/2025/06/03/aws_european_sovereign_cloud/)
*   [How $20 and a lapsed domain allowed security pros to undermine internet integrity](https://www.theregister.com/2024/09/11/watchtowr_black_hat_whois/)
*   [All your DNS were belong to us: AWS and Google Cloud shut down spying vulnerability](https://www.theregister.com/2021/08/06/aws_google_dns/)
*   [Apple network traffic takes mysterious detour through Russia](https://www.theregister.com/2022/07/27/apple_networking_traffic_russia_bgp/)

According to Kodex, its software is used by more than 15,000 government agencies worldwide, as well as a host of major tech companies, including AT&T, Binance, Bumble, Discord, Hinge, Match Group, OpenAI, Yahoo, and more.

Somewhat ironically, the social engineering attack that led to its outage came mere hours after Kodex issued a warning about law enforcement agencies and local government that also had their [domains](https://www.theregister.com/2025/07/05/spain_domains_phishing/) compromised.

The attacks targeted organizations in the US, various countries in South America, and Greece, according to a company [LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7378811873737003009/). ®
