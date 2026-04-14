Title: When a Zero Day and Access Keys Collide in the Cloud: Responding to the SugarCRM Zero-Day Vulnerability

URL Source: https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/

Published Time: 2023-08-10T00:00:00+00:00

Markdown Content:
# When a Zero Day and Access Keys Collide in the Cloud: Responding to the SugarCRM Zero-Day Vulnerability

[![Image 1: Logo](https://unit42.paloaltonetworks.com/wp-content/uploads/2021/07/PANW_Parent.png)](https://www.paloaltonetworks.com/)

[![Image 2: Unit42 Logo](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/unit42-logo-white.svg)](https://unit42.paloaltonetworks.com/)

Menu

*   [Tools](https://unit42.paloaltonetworks.com/tools/)
*   [ATOMs](https://unit42.paloaltonetworks.com/atoms/)
*   [Security Consulting](https://www.paloaltonetworks.com/unit42)
*   [About Us](https://unit42.paloaltonetworks.com/about-unit-42/)
*   [**Under Attack?**](https://start.paloaltonetworks.com/contact-unit42.html)

[](https://www.paloaltonetworks.com/unit42)

![Image 3: x close icon to close mobile navigation](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/x-black.svg)[![Image 4: unit42 logo](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/unit42-logo-dark.svg)](https://www.paloaltonetworks.com/unit42)![Image 5: magnifying glass search icon to open search field](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/search-black.svg)

*   [](https://www.paloaltonetworks.com/unit42)
*   [About Unit 42](https://www.paloaltonetworks.com/unit42/about)
*   [Services](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/#)

 ![Image 6: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)Services 

[Assess and Test Your Security Controls](https://www.paloaltonetworks.com/unit42/assess)

 

    *   [AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment)
    *   [Attack Surface Assessment](https://www.paloaltonetworks.com/unit42/assess/attack-surface-assessment)
    *   [Breach Readiness Review](https://www.paloaltonetworks.com/unit42/assess/breach-readiness-review)
    *   [BEC Readiness Assessment](https://www.paloaltonetworks.com/unit42/assess/business-email-compromise)
    *   [Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment)
    *   [Compromise Assessment](https://www.paloaltonetworks.com/unit42/assess/compromise-assessment)
    *   [Cyber Risk Assessment](https://www.paloaltonetworks.com/unit42/assess/cyber-risk-assessment)
    *   [M&A Cyber Due Diligence](https://www.paloaltonetworks.com/unit42/assess/mergers-acquisitions-cyber-due-diligence)
    *   [Penetration Testing](https://www.paloaltonetworks.com/unit42/assess/penetration-testing)
    *   [Purple Team Exercises](https://www.paloaltonetworks.com/unit42/assess/purple-teaming)
    *   [Ransomware Readiness Assessment](https://www.paloaltonetworks.com/unit42/assess/ransomware-readiness-assessment)
    *   [SOC Assessment](https://www.paloaltonetworks.com/unit42/assess/soc-assessment)
    *   [Supply Chain Risk Assessment](https://www.paloaltonetworks.com/unit42/assess/supply-chain-risk-assessment)
    *   [Tabletop Exercises](https://www.paloaltonetworks.com/unit42/assess/tabletop-exercise)
    *   [Unit 42 Retainer](https://www.paloaltonetworks.com/unit42/retainer)

[Transform Your Security Strategy](https://www.paloaltonetworks.com/unit42/transform)

    *   [IR Plan Development and Review](https://www.paloaltonetworks.com/unit42/transform/incident-response-plan-development-review)
    *   [Security Program Design](https://www.paloaltonetworks.com/unit42/transform/security-program-design)
    *   [Virtual CISO](https://www.paloaltonetworks.com/unit42/transform/vciso)
    *   [Zero Trust Advisory](https://www.paloaltonetworks.com/unit42/transform/zero-trust-advisory)

[Respond in Record Time](https://www.paloaltonetworks.com/unit42/respond)

    *   [Cloud Incident Response](https://www.paloaltonetworks.com/unit42/respond/cloud-incident-response)
    *   [Digital Forensics](https://www.paloaltonetworks.com/unit42/respond/digital-forensics)
    *   [Incident Response](https://www.paloaltonetworks.com/unit42/respond/incident-response)
    *   [Managed Detection and Response](https://www.paloaltonetworks.com/unit42/respond/managed-detection-response)
    *   [Managed Threat Hunting](https://www.paloaltonetworks.com/unit42/respond/managed-threat-hunting)
    *   [Managed XSIAM](https://www.paloaltonetworks.com/cortex/managed-xsiam)
    *   [Unit 42 Retainer](https://www.paloaltonetworks.com/unit42/retainer)

[![Image 7](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/logo-unit-42.svg) UNIT 42 RETAINER Custom-built to fit your organization's needs, you can choose to allocate your retainer hours to any of our offerings, including proactive cyber risk management services. Learn how you can put the world-class Unit 42 Incident Response team on speed dial. Learn more](https://www.paloaltonetworks.com/unit42/retainer)

*   [Unit 42 Threat Research](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/#)

 ![Image 8: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)Unit 42 Threat Research 

[Unit 42 Threat Research](https://unit42.paloaltonetworks.com/)

 

    *   [Threat Briefs and Assessments Details on the latest cyber threats](https://unit42.paloaltonetworks.com/category/threat-research/)
    *   [Tools Lists of public tools released by our team](https://unit42.paloaltonetworks.com/tools/)
    *   [Threat Reports Downloadable, in-depth research reports](https://www.paloaltonetworks.com/resources?q=*%3A*&_charset_=UTF-8&fq=PRODUCTS0_DFACET%3Apan%253Aresource-center%252Fproducts0%252Funit42-managed-detection-and-response&fq=RC_TYPE_DFACET%3Apan%253Aresource-center%252Frc-type%252Fresearch)

[THREAT REPORT 2026 Unit 42 Global Incident Response Report Read now](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report)

[THREAT BRIEF Russia-Ukraine Cyberattacks: How to Protect Against Related Cyberthreats Including DDoS, HermeticWiper, Gamaredon, Website Defacement Learn more](https://unit42.paloaltonetworks.com/preparing-for-cyber-impact-russia-ukraine-crisis/)

[THREAT REPORT Highlights from the Unit 42 Cloud Threat Report, Volume 6 Learn more](https://www.paloaltonetworks.com/resources/research/unit-42-cloud-threat-report-volume-6)

*   [Partners](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/#)

 ![Image 9: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)Partners 

Partners 

 

    *   [Threat Intelligence Sharing](https://www.paloaltonetworks.com/unit42/threat-intelligence-partners)
    *   [Law Firms and Insurance Providers](https://www.paloaltonetworks.com/unit42/incident-response-partners)

[THREAT REPORT 2026 Unit 42 Global Incident Response Report Read now](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report)

[THREAT BRIEF Russia-Ukraine Cyberattacks: How to Protect Against Related Cyberthreats Including DDoS, HermeticWiper, Gamaredon, Website Defacement Learn more](https://unit42.paloaltonetworks.com/preparing-for-cyber-impact-russia-ukraine-crisis/)

[THREAT BRIEF Operation Falcon II: Unit 42 Helps Interpol Identify Nigerian Business Email Compromise Ring Members Learn more](https://unit42.paloaltonetworks.com/operation-falcon-ii-silverterrier-nigerian-bec/)

*   [Resources](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/#)

 ![Image 10: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)Resources 

Resources 

 

    *   [Research Reports](https://www.paloaltonetworks.com/resources?q=*%3A*&_charset_=UTF-8&fq=PRODUCTS0_DFACET%3Apan%253Aresource-center%252Fproducts0%252Funit42-managed-detection-and-response&fq=RC_TYPE_DFACET%3Apan%253Aresource-center%252Frc-type%252Fresearch)
    *   [Webinars](https://www.paloaltonetworks.com/resources?q=*%3A*&_charset_=UTF-8&fq=PRODUCTS0_DFACET%3Apan%253Aresource-center%252Fproducts0%252Funit42-managed-detection-and-response&fq=RC_TYPE_DFACET%3Apan%253Aresource-center%252Frc-type%252Fwebinar)
    *   [Customer Stories](https://www.paloaltonetworks.com/unit42/customer-stories)
    *   [Datasheets](https://www.paloaltonetworks.com/resources?q=*%3A*&_charset_=UTF-8&fq=PRODUCTS0_DFACET%3Apan%253Aresource-center%252Fproducts0%252Funit42-managed-detection-and-response&fq=RC_TYPE_DFACET%3Apan%253Aresource-center%252Frc-type%252Fdatasheet)
    *   [Videos](https://www.paloaltonetworks.com/resources?q=*%3A*&_charset_=UTF-8&fq=PRODUCTS0_DFACET%3Apan%253Aresource-center%252Fproducts0%252Funit42-managed-detection-and-response&fq=RC_TYPE_DFACET%3Apan%253Aresource-center%252Frc-type%252Fvideo)
    *   [Infographics](https://www.paloaltonetworks.com/resources?q=*%3A*&_charset_=UTF-8&fq=PRODUCTS0_DFACET%3Apan%253Aresource-center%252Fproducts0%252Funit42-managed-detection-and-response&fq=RC_TYPE_DFACET%3Apan%253Aresource-center%252Frc-type%252Finfographic)
    *   [Whitepapers](https://www.paloaltonetworks.com/resources?q=*%3A*&_charset_=UTF-8&fq=PRODUCTS0_DFACET%3Apan%253Aresource-center%252Fproducts0%252Funit42-managed-detection-and-response&fq=RC_TYPE_DFACET%3Apan%253Aresource-center%252Frc-type%252Fwhitepaper)
    *   [Cyberpedia](https://www.paloaltonetworks.com/resources?q=*%3A*&_charset_=UTF-8&fq=PRODUCTS0_DFACET%3Apan%253Aresource-center%252Fproducts0%252Funit42-managed-detection-and-response&fq=RC_TYPE_DFACET%3Apan%253Aresource-center%252Frc-type%252Farticle)

Industries

    *   [Financial Services](https://www.paloaltonetworks.com/industry/unit42-financial-services)
    *   [Healthcare](https://www.paloaltonetworks.com/industry/unit42-healthcare)
    *   [Manufacturing](https://www.paloaltonetworks.com/industry/unit42-manufacturing)

[THREAT REPORT 2026 Unit 42 Global Incident Response Report Read now](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report)

[ANALYST REPORT Unit 42® named a Leader in the 2025 IDC MarketScape for Worldwide IR Services. See our difference](https://start.paloaltonetworks.com/idc-incident-response-marketscape-2025)

*   [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/#)
*   [Under Attack?](https://start.paloaltonetworks.com/contact-unit42.html)

[![Image 11: palo alto networks logo icon](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/logo-default.svg)![Image 12: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/#)

Search

 All 
*   [Tech Docs](https://docs.paloaltonetworks.com/search#q=unit%2042&sort=relevancy&layout=card&numberOfResults=25)

[English](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/#)

*   [English](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)
*   [Japanese](https://unit42.paloaltonetworks.com/ja/sugarcrm-cloud-incident-black-hat/)

*   [Threat Research Center](https://unit42.paloaltonetworks.com/ "Threat Research")
*   [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
*   [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")

[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
# When a Zero Day and Access Keys Collide in the Cloud: Responding to the SugarCRM Zero-Day Vulnerability

![Image 13: Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 13 min read 

Related Products

[![Image 14: Next-Generation Firewall icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced Threat Prevention](https://unit42.paloaltonetworks.com/product-category/advanced-threat-prevention/ "Advanced Threat Prevention")[![Image 15: Next-Generation Firewall icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Next-Generation Firewall](https://unit42.paloaltonetworks.com/product-category/next-generation-firewall/ "Next-Generation Firewall")[![Image 16: Prisma Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud](https://unit42.paloaltonetworks.com/product-category/prisma-cloud/ "Prisma Cloud")[![Image 17: Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

*   ![Image 18: Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    *   [Margaret Kelley](https://unit42.paloaltonetworks.com/author/margaret-kelley/)

*   ![Image 19: Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)Published:August 10, 2023 
*   ![Image 20: Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    *   [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
    *   [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
    *   [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

*   ![Image 21: Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    *   [Black Hat](https://unit42.paloaltonetworks.com/tag/black-hat/)
    *   [CVE-2023-22952](https://unit42.paloaltonetworks.com/tag/cve-2023-22952/)
    *   [SugarCRM](https://unit42.paloaltonetworks.com/tag/sugarcrm/)
    *   [Zero-day](https://unit42.paloaltonetworks.com/tag/zero-day/)

*   [![Image 22: Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/?pdf=download&lg=en&_wpnonce=8dfc6c694c "Click here to download")
*   [![Image 23: Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/?pdf=print&lg=en&_wpnonce=8dfc6c694c "Click here to print")

[Share![Image 24: Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/# "Click here to share")
*   [![Image 25: Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/# "Copy link")
*   [![Image 26: Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=When%20a%20Zero%20Day%20and%20Access%20Keys%20Collide%20in%20the%20Cloud:%20Responding%20to%20the%20SugarCRM%20Zero-Day%20Vulnerability&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fsugarcrm-cloud-incident-black-hat%2F "Share in email")
*   [![Image 27: Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fsugarcrm-cloud-incident-black-hat%2F "Share in Facebook")
*   [![Image 28: LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fsugarcrm-cloud-incident-black-hat%2F&title=When%20a%20Zero%20Day%20and%20Access%20Keys%20Collide%20in%20the%20Cloud:%20Responding%20to%20the%20SugarCRM%20Zero-Day%20Vulnerability "Share in LinkedIn")
*   [![Image 29: Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fsugarcrm-cloud-incident-black-hat%2F&text=When%20a%20Zero%20Day%20and%20Access%20Keys%20Collide%20in%20the%20Cloud:%20Responding%20to%20the%20SugarCRM%20Zero-Day%20Vulnerability "Share in Twitter")
*   [![Image 30: Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](https://www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fsugarcrm-cloud-incident-black-hat%2F "Share in Reddit")
*   [![Image 31: Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=When%20a%20Zero%20Day%20and%20Access%20Keys%20Collide%20in%20the%20Cloud:%20Responding%20to%20the%20SugarCRM%20Zero-Day%20Vulnerability%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fsugarcrm-cloud-incident-black-hat%2F "Share in Mastodon")

## [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Executive Summary

While the SugarCRM CVE-2023-22952 zero-day authentication bypass and remote code execution vulnerability might seem like a typical exploit, there’s actually more for defenders to be aware of. Because it’s a web application, if it’s not configured or secured correctly, the infrastructure behind the scenes can allow attackers to increase their impact. When a threat actor understands the underlying technology used by cloud service providers, they can accomplish a great deal if they can gain access to credentials that have the right permissions.

During the past year, Unit 42 responded to multiple cases where the SugarCRM vulnerability [CVE-2023-22952](https://nvd.nist.gov/vuln/detail/CVE-2023-22952) was an initial attack vector that allowed threat actors to gain access to AWS accounts. This was not due to a vulnerability in AWS, and it could have happened with any cloud environment. Instead, the threat actors took advantage of misconfigurations to expand their access after initial compromise.

This article maps out various attacks against AWS environments following the [MITRE ATT&CK Matrix](https://attack.mitre.org/) framework, wrapping up with multiple prevention mechanisms an organization can put in place to protect themselves. Some of these protections include taking advantage of controls and services provided by AWS, cloud best practices, and ensuring sufficient data retention to catch the full attack.

The complexity of these attacks shows how it’s important to set your logging and monitoring to detect any unauthorized AWS API calls, even if they’re seemingly innocuous. If threat actors are allowed to gain a foothold, this can lead to much more daunting activity that is not always traceable. One size does not fit all in cloud security, but these attacks highlight key areas to focus on to make sure you're ready to defend against those attacks when they come.

Palo Alto Networks customers receive protections from the attacks described in this article in the following ways:

*   Organizations can engage the [Unit 42 Incident Response](https://start.paloaltonetworks.com/contact-unit42.html) team for specific assistance with this threat and others.
*   [Prisma Cloud](https://docs.paloaltonetworks.com/prisma/prisma-cloud) can provide alerting and mitigation solutions for the use-cases reported within this blog.
*   [Next-Generation Firewall](https://docs.paloaltonetworks.com/ngfw) with the [Advanced Threat Prevention](https://docs.paloaltonetworks.com/advanced-threat-prevention/administration) security subscription can help block the attacks.

**Related Unit 42 Topics**[**AWS**](https://unit42.paloaltonetworks.com/tag/aws/)**,**[**Cloud**](https://unit42.paloaltonetworks.com/category/cloud/)

## [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)MITRE ATT&CK Matrix

We’re framing the walk-through for these incidents with the MITRE ATT&CK Matrix, which is comprised of fourteen different tactics that describe the various components of a cybersecurity attack. With the various cases we responded to, nine of those fourteen tactics described the threat actor activity. Those nine were initial access, credential access, discovery, lateral movement, execution, exfiltration, privilege escalation, persistence and defense evasion.

## [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Case Walk Through

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Initial Access – CVE-2023-22952

The initial attack vector of these AWS account compromises was the zero-day SugarCRM vulnerability, [CVE-2023-22952](https://nvd.nist.gov/vuln/detail/CVE-2023-22952). SugarCRM is a customer relationship management platform that focuses on cross-team collaboration. The product has users in many different verticals due to their wide range of product features.

CVE-2023-22952 was published by NIST National Vulnerability Database on Jan. 11, 2023, with a base score of 8.8. This vulnerability allows threat actors to inject custom PHP code through the SugarCRM email templates module due to missing input validation.

To understand why the threat actors targeted SugarCRM for these attacks, it’s helpful to know that there is a wide range of sensitive data such as email addresses, contact information and account information in SugarCRM customer databases. If it was compromised, threat actors would either choose to sell this information directly or extort their victims to get more money.

By leveraging this vulnerability in SugarCRM, a threat actor can gain direct access to the underlying servers running this application due to the remote execution component of the vulnerability. In the cases we responded to, these servers were Amazon Elastic Cloud Compute (EC2) instances with long-term AWS access keys stored on the hosts, allowing the threat actors to expand their access. Since these organizations were hosting their infrastructure in the cloud, it opens different attack vectors for the threat actors than would be present with on-premises hosting.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Credential Access

Once the threat actors gained access to the EC2 instances, they successfully compromised long-term AWS access keys that existed on the host. Regardless of whether the computer exists on-premises or in the cloud, if a person uses the AWS command-line interface (CLI), they can choose to store temporary or permanent credentials used for the authentication within a credentials file stored on the host (as shown in Figure 1 below, which includes the file path).

In the cases we observed, these plain-text credentials existed on the compromised hosts, which allowed the threat actors to steal them and start using the access keys for discovery activity.

![Image 32: Image 1 is two lines of code. These are the file paths for credentials in AWS.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/08/word-image-129566-1-2.png)

Figure 1. File paths for credentials file location.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Discovery

Before the threat actors performed any scanning activity, they first ran the command [GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html). GetCallerIdentity is the AWS version of [whoami](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/whoami). It returns various information about the entity that performed the call such as the user ID, account and [Amazon Resource Name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) (ARN) of the principal associated with the credentials used to sign the request, as shown in Figure 2. The user ID is a unique identifier of the entity that performed the call, the account is the unique 12-digit identifier of the AWS account the credentials belong to, and the ARN includes the account ID and human-readable name of the principal performing the call.

![Image 33: Image 2 is a screenshot of the response to GetCallerIdentity. It is three lines in total, and includes the user ID, the account, and the ARN. An ARN is the acronym for the Amazon Resource Name.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/08/word-image-129566-2-2.png)

Figure 2. Example GetCallerIdentity response.

Once the threat actor knew a little more about the credentials they compromised, they began their scanning activities. They utilized the tools Pacu and Scout Suite to gain a better understanding of what resources existed within the AWS account. Pacu is an open-source AWS exploitation framework, and it is designed to be the Metasploit equivalent in the cloud. Scout Suite is a security auditing tool used for security posture assessments of cloud environments.

In some of the cases we responded to, we saw Pacu already existed on hosts from previous penetration tests. Scout Suite was not something we saw downloaded onto the compromised EC2 instances, but we knew it was used based on the user agents associated with the threat actor activity. Both of these tools provide a lot of information for threat actors to get a lay of the land for the AWS account they’ve compromised.

In the cases, these tools scanned a variety of traditional services such as the following:

*   [EC2](https://aws.amazon.com/ec2/)
*   [IAM](https://aws.amazon.com/iam/)
*   [RDS](https://aws.amazon.com/rds/)
*   [S3](https://aws.amazon.com/s3/)
*   [SNS](https://aws.amazon.com/sns/)
*   [SES](https://aws.amazon.com/ses/)
*   [Lambda](https://aws.amazon.com/lambda/)

The threat actors also performed other discovery calls against services that would not necessarily be expected that provided helpful information to the attackers, such as the [Organizations service](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) and [Cost and Usage](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) service.

[AWS Organizations](https://aws.amazon.com/organizations/) provides companies with a centralized place to manage multiple AWS accounts and resources. When reviewing the threat actor activity in the CloudTrail logs, three Organizations API calls stood out. The first call was [ListOrganizationalUnitsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOrganizationalUnitsForParent.html), which lists out all the [Organizational Units](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/) (OUs).

From there, the threat actors ran [ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html) which returns all the account IDs associated with each of those OUs. The final call that provided the threat actor with the most useful information was the [DescribeOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeOrganization.html) API call. This event returns the master account ID as well as the master account email address associated with that account. With that information, the threat actors have enough to attempt to log in as the Root user for that account.

The final discovery call of interest involved the Cost and Usage service. The threat actors performed various [GetCostandUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsage.html) calls (shown in Figure 3) and the response returned information about the general costs within the compromised account (shown in Figure 4).

Defenders need to be aware that threat actors can determine how active an account is by understanding the cost within a cloud account. If the total cost in an account is large, it might be easier for them to spin up new resources undetected, because the cost might not stand out.

On the other hand, if there is very little spending in an account, a couple new resources could stand out a lot more. Account owners with less spending might also have tighter notifications around cost, which would potentially trigger alerts when the threat actors create new resources.

![Image 34: Image 3 is a screenshot of the request parameters for GetCostandUsage. It includes the time period with start and end dates; the granularity, which is monthly; and the metrics, which include the blended cost, unblended cost, and usage quantity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/08/word-image-129566-3-2.png)

Figure 3. Example GetCostandUsage request parameters.

![Image 35: Image 4 is a screenshot of the GetCostandUsage response. It includes results by time including the time period with start and end dates; the totals for blended cost with amount and unit; usage quantity with amount and unit; unblended cost with amount and unit, and estimated groups.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/08/word-image-129566-4-2.png)

Figure 4. Example GetCostandUsage response.

Both the Organizations and Cost and Usage API calls are great examples of how the attack surface is different in the cloud. By using these innocuous looking API calls, threat actors gained a ton of information about the account structure and usage without performing a lot of suspicious activity that might trigger an alert.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Lateral Movement/Execution/Exfiltration – RDS

In the incidents we observed, once threat actors finished scanning the environment, they had enough information to narrow their activity from discovery across the whole account to taking actions on various services starting with the [Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html) (RDS). The threat actors moved laterally from the compromised SugarCRM EC2 instances to the RDS service and started executing commands to create new RDS snapshots from the various SugarCRM RDS databases. The creation of these snapshots resulted in no downtime of the original RDS databases.

From there, the attackers modified pre-existing security group rules that already allowed SSH inbound, and they added port 3306 for MySQL traffic. The threat actors then moved to exfiltration, creating brand new databases from the snapshots, making them public and attaching the modified security groups. Finally, they modified the newly created RDS databases by changing the master user password, which would allow them to log in to the databases.

To understand whether any exfiltration of data occurred, in the cases that had virtual private cloud [(VPC) flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) enabled, we could use the logs to see how many bytes of data left the environment. With the cases that did not have VPC flow logs enabled, we were limited in our findings of data exfiltration.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Lateral Movement/Execution – EC2

After the RDS activity, the threat actors again moved laterally back to the EC2 service and made some changes. The first thing the threat actors did was create new [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMIs) from the running SugarCRM EC2 instances, and from there they ran the [ImportKeyPair](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html) command to import their public key pair that they created with a third-party tool. With these tasks complete, the threat actors proceeded to create new EC2 instances. The threat actors also attached existing security groups to the EC2 instances that allowed inbound port 22 access from any IP address, as shown in Figure 5.

![Image 36: Image 5 is a screenshot of an example security group, allowing port 22 access.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/08/word-image-129566-5-2.png)

Figure 5. Example security group allowing port 22 access.

The threat actors created EC2 instances in the same regions that the organizations used for the rest of their normal infrastructure. They also switched regions to a geographically new area, and created a new security group that allowed port 22 SSH traffic from any IP address. The threat actors then imported another key pair. Since the threat actors switched to a different region, the key pair had to be reimported even if it was the same key pair used in other regions.

After finishing the setup, they created a new EC2 instance, but this time they used a public AMI available on the AWS Marketplace**.** This EC2 instance activity shows the importance of enabling security services such as GuardDuty in all regions, to have visibility into all that is happening within an AWS account. As a proactive measure, organizations can disable unused regions as well.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Privilege Escalation – Root

For the privilege escalation portion of these attacks, the threat actors did not attempt to create new IAM users like we have seen in other cases. They instead opted for attempting to login as the Root user. Despite using information they obtained from the Organizations calls made during the discovery phase, the threat actors still failed to successfully log in as the Root user. Root login attempts are fairly noisy, so these failed Root logins stood out in the CloudTrail logs, as shown in Figure 6.

![Image 37: Image 6 is a screenshot of many lines of code. It is an example of a failed Root login from the CloudTrail logs.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/08/word-image-129566-6-2.png)

Figure 6. Example failed Root login from CloudTrail logs.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Persistence – Regions

Beyond attempting to log in with the Root account, the threat actors did not try much in the way of persistence. The clearest attempt at persistence was the creation of EC2 instances in different regions than the organizations normally used to host their infrastructure. Similar to the Root login attempts, these new EC2 instances stood out in the CloudTrail logs. However, it can be easy to miss stuff when reviewing resources in the console, as it's a fair amount of work to switch regions and track down all resources created, as cloud environments get larger.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Defense Evasion

Once a threat actor compromises an AWS account, they have a finite amount of time before the account owners detect that they have an issue. In order to stay under the radar, the threat actors deployed resources in non-standard regions. However, they also turned the EC2 instances on and off throughout their time in the environments.

There are a couple of reasons why a threat actor might choose to do this. The first reason is to decrease their visibility. On the EC2 instance page in the AWS console, it defaults to showing only _running_ EC2 instances. Unless a user is actively trying to review non-running EC2 instances, at an initial glance, the new EC2 instances created by the threat actors would be missed once they are placed in a stopped state.

The second reason they might choose to do this is that stopping these resources also avoids incurring extra costs in the organization’s account. If the organizations have tight notifications around costs, threat actors stopping the resources they created minimizes costs and helps prevent triggering a cost alert, which is another way they could evade defenses.

Other than creating resources in different regions and stopping the resources they created, the threat actors did not attempt other defense evasion techniques such as stopping CloudTrail logging or disabling GuardDuty.

## [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Remediation

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Access Keys

There are four main remediation actions that organizations can take to protect themselves against these types of attacks in the future. The first one revolves around access keys. It’s vital for organizations to [protect their access keys](https://docs.aws.amazon.com/accounts/latest/reference/credentials-access-keys-best-practices.html), as we often see them being the root cause of AWS compromises.

There is never a good reason to use long-term access keys on EC2 instances. Instead, use EC2 Roles and the temporary credentials that are present in the Instance Metadata Service (IMDS). Also, make sure to only use IMDSv2, which protects against server-side request forgery (SSRF) attacks.

We recommend creating a cleanup process for any long-term access keys stored in the credentials files on the hosts. This can be accomplished by asking users to clean up those files when they have completed their work, or by creating an organizational-level process that automatically cleans up these files.

We also recommend that the access keys are rotated and deleted on a schedule. The longer an access key lives, the more chance it has of being compromised. Consistently rotating them and deleting unused keys proactively protects the AWS account. This whole process can be automated and helps keep access key security in check.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Least-Privileged IAM Policies

The only reason that these threat actors were able to accomplish all that they did in these attacks was because of the expansive permissions that the organizations gave to the IAM User principal on the SugarCRM host. These IAM Users that were present on the hosts needed some AWS permissions, but those should have been narrowly scoped to only include exactly what the application using the permissions needed. And these organizations were not alone in this situation – according to our [Cloud Threat Report, Volume 6](https://www.paloaltonetworks.com/resources/research/unit-42-cloud-threat-report-volume-6), 99% of cloud users, roles, services, and resources were granted excessive permissions, which were left unused.

You can use AWS Access Analyzer to examine the historical usage of APIs by a particular IAM principal and automatically generate an access policy that restricts its access to only those APIs that it has used in the time period of your choice.

It might be easier to write overly permissive policies, but it is certainly worth the effort to write narrowly scoped permissions to better protect your AWS account.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Monitoring Root

Another remediation step we recommend to these organizations is to set up monitoring around the Root account. This account should only be used in an environment for a couple account management tasks that _require_ Root, which maintains this as a high-fidelity alert to help secure the most valuable account. We also recommend always enabling multifactor authentication on Root and making sure it is protected with a long password.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Logging and Monitoring

The final remediation we recommend to these organizations is to make sure they have the correct logging configured. [CloudTrail](https://aws.amazon.com/cloudtrail/) and [GuardDuty](https://aws.amazon.com/guardduty/) should both be enabled in all regions and logs sent to a centralized location.

When it comes to GuardDuty, the alerts should be sent to a team that will respond based on the alert severity. In our cases where the organization had GuardDuty enabled, we saw that GuardDuty caught these access key compromises fairly early on in the attack. This is an easy way to help protect your accounts.

We also recommend for organizations to enable VPC flow logs to help catch any data exfiltration that might take place. These logs are extremely helpful when troubleshooting network connectivity issues. And with all of these different services, it’s important to make sure to have a good retention period for the data. Regardless of the environment, compromise can happen anywhere, and it’s vital to make sure logs are retained long enough to catch the full attack.

## [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Conclusion

Even though the threat actors were able to accomplish a lot in these attacks, we saw that there’s some great remediation steps organizations can put in place to better protect themselves. Since access keys are the most common initial attack vector, try to avoid the use of long-term access keys when possible. In AWS, this means using EC2 Roles, IAM Roles Anywhere or Identity Center integration for developer workstations. Another layer to protect those keys is setting up monitoring around abnormal usage. With these attacks, the threat actors performed abnormal API calls, which is all detectable with long-tail log analysis.

It’s also imperative to do basic least-privilege analysis so that code running inside or outside the cloud has only the permissions it needs to do its job.

You always want to make sure that you’re monitoring your cloud accounts for abnormal activity in addition to monitoring access keys. In AWS this can look like monitoring various services such as CloudTrail, VPC flow logs and S3 server access logs. If services within your cloud account are being accessed by or reaching out to new and unusual IP addresses over abnormal ports, you want to make sure your monitoring is configured to alert on this activity. Also, if your organization has sensitive data in S3 buckets, monitoring S3 server access logging to note abnormal calls to the bucket helps proactively find attacks.

And finally, the threat actors were able to accomplish all that they did in these cases because of the lack of granular permissions. If these compromised access keys that belonged to IAM Users had fewer permissions, that would have stopped the threat actors in their tracks.

## [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Product Protections

Palo Alto Networks customers can leverage a variety of product protections and updates to identify and defend against this threat.

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

*   North America Toll-Free: 866.486.4842 (866.4.UNIT42)
*   EMEA: +31.20.299.3130
*   APAC: +65.6983.8730
*   Japan: +81.50.1790.0200

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Prisma Cloud

[Prisma Cloud](https://docs.paloaltonetworks.com/prisma/prisma-cloud) can provide alerting and mitigation solutions for the use-cases reported within this blog in the following ways:

*   Prisma Cloud [Anomaly Policies](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin/prisma-cloud-policies/anomaly-policies) can be deployed to detect instances running in out of use AWS regions, as well as detecting suspicious IAM credential usage through AI/ML algorithmic functionality.
*   Prisma Cloud’s [Attack Path Policies](https://www.paloaltonetworks.com/blog/prisma-cloud/mitre-attck-for-cloud-improve-threat-detection/) can also detect lateral movement and privilege escalation attacks against the EC2 instances described within this blog.

Prisma Cloud uses the MITRE ATT&CK framework as the guiding principle for developing detection and risk mitigation capabilities.

### [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Next-Generation Firewalls and Prisma Access With Advanced Threat Prevention

[Next-Generation Firewall](https://docs.paloaltonetworks.com/ngfw) with the [Advanced Threat Prevention](https://docs.paloaltonetworks.com/advanced-threat-prevention/administration) security subscription can help block the attacks via the following Threat Prevention signature: [93591](https://threatvault.paloaltonetworks.com/?query=93591).

### Cortex XDR

[Cortex XDR for cloud](https://www.paloaltonetworks.com/cortex/cloud-detection-and-response) provides SOC teams with a full incident story across the entire digital domain by integrating activity from cloud hosts, cloud traffic and audit logs, together with endpoint and network data.

## [](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)Indicators of Compromise

IPs:

*   13[.]90.77.93
*   31[.]132.2.66

User Agents:

*   Boto3/1.26.45 Python/3.9.2 Linux/6.0.0-2parrot1-amd64 Botocore/1.29.45
*   Boto3/1.7.61 Python/3.5.0 Windows/ Botocore/1.10.62
*   aws-cli/1.19.1 Python/3.9.2 Linux/6.0.0-2parrot1-amd64 botocore/1.29.58
*   aws-cli/1.18.69 Python/3.5.2 Linux/4.4.0-1128-aws botocore/1.16.19
*   Scout Suite/5.12.0 Python/3.9.2 Linux/6.0.0-2parrot1-amd64 Scout Suite/5.12.0

_Updated August 16, 2023, at 1:45 p.m. PT to add Cortex protections information._

Back to top

### Tags

*   [Black Hat](https://unit42.paloaltonetworks.com/tag/black-hat/ "Black Hat")
*   [CVE-2023-22952](https://unit42.paloaltonetworks.com/tag/cve-2023-22952/ "CVE-2023-22952")
*   [SugarCRM](https://unit42.paloaltonetworks.com/tag/sugarcrm/ "SugarCRM")
*   [Zero-day](https://unit42.paloaltonetworks.com/tag/zero-day/ "zero-day")

[Threat Research Center](https://unit42.paloaltonetworks.com/ "Threat Research")[Next: NodeStealer 2.0 – The Python Version: Stealing Facebook Business Accounts](https://unit42.paloaltonetworks.com/nodestealer-2-targets-facebook-business/ "NodeStealer 2.0 – The Python Version: Stealing Facebook Business Accounts")

### Table of Contents

### Related Articles

*   [Threat Insights: Active Exploitation of Cisco ASA Zero Days](https://unit42.paloaltonetworks.com/zero-day-vulnerabilities-affect-cisco-software/ "article - table of contents")
*   [Active Exploitation of Microsoft SharePoint Vulnerabilities: Threat Brief (Updated August 12)](https://unit42.paloaltonetworks.com/microsoft-sharepoint-cve-2025-49704-cve-2025-49706-cve-2025-53770/ "article - table of contents")
*   [Threat Brief: Multiple Vulnerabilities Including Zero-Day Remote Unauthenticated API Access – CVE-2023-35078 – in Ivanti Endpoint Manager Mobile (Updated)](https://unit42.paloaltonetworks.com/threat-brief-cve-2023-35078/ "article - table of contents")

## Related Resources

![Image 38: Pictorial representation of remote code execution in AI and machine learning libraries. Close-up of a woman wearing glasses and focusing intently on a computer screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/05_Vulnerabilities_1920x900-786x368.jpg)

[![Image 39: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 13, 2026[#### Remote Code Execution With Modern AI/ML Formats and Libraries](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/)
*   [Apple](https://unit42.paloaltonetworks.com/tag/apple/ "Apple")
*   [CVE-2025-23304](https://unit42.paloaltonetworks.com/tag/cve-2025-23304/ "CVE-2025-23304")
*   [CVE-2026-22584](https://unit42.paloaltonetworks.com/tag/cve-2026-22584/ "CVE-2026-22584")

[Read now ![Image 40: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/ "Remote Code Execution With Modern AI/ML Formats and Libraries")

![Image 41: Pictorial representation of CVE-2025-55182 (React) and CVE-2025-66478 (Next.js). Close-up of a digital display on electronic equipment with illuminated text reading "SYSTEM HACKED" in red, set against a blurred background of blue and red lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/12/02_Vulnerabilities_1920x900-786x368.jpg)

[![Image 42: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)December 12, 2025[#### Exploitation of Critical Vulnerability in React Server Components (Updated December 12)](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/)
*   [Cobalt Strike](https://unit42.paloaltonetworks.com/tag/cobalt-strike/ "Cobalt Strike")
*   [CVE-2025-55182](https://unit42.paloaltonetworks.com/tag/cve-2025-55182/ "CVE-2025-55182")
*   [CVE-2025-66478](https://unit42.paloaltonetworks.com/tag/cve-2025-66478/ "CVE-2025-66478")

[Read now ![Image 43: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/ "Exploitation of Critical Vulnerability in React Server Components (Updated December 12)")

![Image 44: Pictorial representation of an authentication coercion attack. Panoramic view of a city skyline at night, featuring vibrant light beams from skyscrapers and a deep blue sky.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/07_Vulnerabilities_1920x900-786x368.jpg)

[![Image 45: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)November 10, 2025[#### You Thought It Was Over? Authentication Coercion Keeps Evolving](https://unit42.paloaltonetworks.com/authentication-coercion/)
*   [Mimikatz](https://unit42.paloaltonetworks.com/tag/mimikatz/ "Mimikatz")
*   [PrintNightmare](https://unit42.paloaltonetworks.com/tag/printnightmare/ "PrintNightmare")
*   [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")

[Read now ![Image 46: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/authentication-coercion/ "You Thought It Was Over? Authentication Coercion Keeps Evolving")

![Image 47: Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 48: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)March 23, 2026[#### Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication/)
*   [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
*   [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
*   [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")

[Read now ![Image 49: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Image 50: Pictorial representation of BeyondTrust vulnerability CVE-2026-1731. Digital art depicting a stylized mountain range with vibrant blue and red hues. The peaks are accentuated by glowing particles and an abstract, starry backdrop, creating a futuristic landscape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/14_Overview_1920x900-786x368.jpg)

[![Image 51: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)February 19, 2026[#### VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability (CVE-2026-1731)](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/)
*   [Bash](https://unit42.paloaltonetworks.com/tag/bash/ "bash")
*   [CVE-2026-1731](https://unit42.paloaltonetworks.com/tag/cve-2026-1731/ "CVE-2026-1731")
*   [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")

[Read now ![Image 52: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/ "VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability (CVE-2026-1731)")

![Image 53](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/AdobeStock_1020436911-786x440.jpeg)

[![Image 54: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)February 17, 2026[#### Critical Vulnerabilities in Ivanti EPMM Exploited](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/)
*   [CVE-2026-1281](https://unit42.paloaltonetworks.com/tag/cve-2026-1281/ "CVE-2026-1281")
*   [CVE-2026-1340](https://unit42.paloaltonetworks.com/tag/cve-2026-1340/ "CVE-2026-1340")
*   [Ivanti](https://unit42.paloaltonetworks.com/tag/ivanti/ "Ivanti")

[Read now ![Image 55: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/ "Critical Vulnerabilities in Ivanti EPMM Exploited")

![Image 56: Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 57: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)February 6, 2026[#### Novel Technique to Detect Cloud Threat Actor Operations](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)
*   [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
*   [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
*   [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")

[Read now ![Image 58: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Image 59: Pictorial representation of CVE-2025-0921. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/06_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![Image 60: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 30, 2026[#### Privileged File System Vulnerability Present in a SCADA System](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/)
*   [CVE-2025-0921](https://unit42.paloaltonetworks.com/tag/cve-2025-0921/ "CVE-2025-0921")
*   [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
*   [SCADA](https://unit42.paloaltonetworks.com/tag/scada/ "SCADA")

[Read now ![Image 61: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/ "Privileged File System Vulnerability Present in a SCADA System")

![Image 62: Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![Image 63: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 20, 2026[#### DNS OverDoS: Are Private Endpoints Too Private?](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)
*   [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
*   [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")

[Read now ![Image 64: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Image 65: Pictorial representation of MongoBleed, CVE-2025-14847. Digital image featuring a glowing padlock icon superimposed on a background of streaming blue binary code, symbolizing cybersecurity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/AdobeStock_233494953-786x429.jpeg)

[![Image 66: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)January 13, 2026[#### Threat Brief: MongoDB Vulnerability (CVE-2025-14847)](https://unit42.paloaltonetworks.com/mongobleed-cve-2025-14847/)
*   [CVE-2025-14847](https://unit42.paloaltonetworks.com/tag/cve-2025-14847/ "CVE-2025-14847")
*   [MongoDB](https://unit42.paloaltonetworks.com/tag/mongodb/ "MongoDB")

[Read now ![Image 67: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/mongobleed-cve-2025-14847/ "Threat Brief: MongoDB Vulnerability (CVE-2025-14847)")

![Image 68: Pictorial representation of remote code execution in AI and machine learning libraries. Close-up of a woman wearing glasses and focusing intently on a computer screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/05_Vulnerabilities_1920x900-786x368.jpg)

[![Image 69: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 13, 2026[#### Remote Code Execution With Modern AI/ML Formats and Libraries](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/)
*   [Apple](https://unit42.paloaltonetworks.com/tag/apple/ "Apple")
*   [CVE-2025-23304](https://unit42.paloaltonetworks.com/tag/cve-2025-23304/ "CVE-2025-23304")
*   [CVE-2026-22584](https://unit42.paloaltonetworks.com/tag/cve-2026-22584/ "CVE-2026-22584")

[Read now ![Image 70: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/ "Remote Code Execution With Modern AI/ML Formats and Libraries")

![Image 71: Pictorial representation of CVE-2025-55182 (React) and CVE-2025-66478 (Next.js). Close-up of a digital display on electronic equipment with illuminated text reading "SYSTEM HACKED" in red, set against a blurred background of blue and red lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/12/02_Vulnerabilities_1920x900-786x368.jpg)

[![Image 72: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)December 12, 2025[#### Exploitation of Critical Vulnerability in React Server Components (Updated December 12)](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/)
*   [Cobalt Strike](https://unit42.paloaltonetworks.com/tag/cobalt-strike/ "Cobalt Strike")
*   [CVE-2025-55182](https://unit42.paloaltonetworks.com/tag/cve-2025-55182/ "CVE-2025-55182")
*   [CVE-2025-66478](https://unit42.paloaltonetworks.com/tag/cve-2025-66478/ "CVE-2025-66478")

[Read now ![Image 73: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/ "Exploitation of Critical Vulnerability in React Server Components (Updated December 12)")

![Image 74: Pictorial representation of an authentication coercion attack. Panoramic view of a city skyline at night, featuring vibrant light beams from skyscrapers and a deep blue sky.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/07_Vulnerabilities_1920x900-786x368.jpg)

[![Image 75: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)November 10, 2025[#### You Thought It Was Over? Authentication Coercion Keeps Evolving](https://unit42.paloaltonetworks.com/authentication-coercion/)
*   [Mimikatz](https://unit42.paloaltonetworks.com/tag/mimikatz/ "Mimikatz")
*   [PrintNightmare](https://unit42.paloaltonetworks.com/tag/printnightmare/ "PrintNightmare")
*   [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")

[Read now ![Image 76: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/authentication-coercion/ "You Thought It Was Over? Authentication Coercion Keeps Evolving")

![Image 77: Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 78: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)March 23, 2026[#### Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication/)
*   [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
*   [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
*   [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")

[Read now ![Image 79: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Image 80: Pictorial representation of BeyondTrust vulnerability CVE-2026-1731. Digital art depicting a stylized mountain range with vibrant blue and red hues. The peaks are accentuated by glowing particles and an abstract, starry backdrop, creating a futuristic landscape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/14_Overview_1920x900-786x368.jpg)

[![Image 81: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)February 19, 2026[#### VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability (CVE-2026-1731)](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/)
*   [Bash](https://unit42.paloaltonetworks.com/tag/bash/ "bash")
*   [CVE-2026-1731](https://unit42.paloaltonetworks.com/tag/cve-2026-1731/ "CVE-2026-1731")
*   [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")

[Read now ![Image 82: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/ "VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability (CVE-2026-1731)")

![Image 83](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/AdobeStock_1020436911-786x440.jpeg)

[![Image 84: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)February 17, 2026[#### Critical Vulnerabilities in Ivanti EPMM Exploited](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/)
*   [CVE-2026-1281](https://unit42.paloaltonetworks.com/tag/cve-2026-1281/ "CVE-2026-1281")
*   [CVE-2026-1340](https://unit42.paloaltonetworks.com/tag/cve-2026-1340/ "CVE-2026-1340")
*   [Ivanti](https://unit42.paloaltonetworks.com/tag/ivanti/ "Ivanti")

[Read now ![Image 85: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/ "Critical Vulnerabilities in Ivanti EPMM Exploited")

![Image 86: Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 87: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)February 6, 2026[#### Novel Technique to Detect Cloud Threat Actor Operations](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)
*   [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
*   [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
*   [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")

[Read now ![Image 88: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Image 89: Pictorial representation of CVE-2025-0921. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/06_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![Image 90: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 30, 2026[#### Privileged File System Vulnerability Present in a SCADA System](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/)
*   [CVE-2025-0921](https://unit42.paloaltonetworks.com/tag/cve-2025-0921/ "CVE-2025-0921")
*   [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
*   [SCADA](https://unit42.paloaltonetworks.com/tag/scada/ "SCADA")

[Read now ![Image 91: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/ "Privileged File System Vulnerability Present in a SCADA System")

![Image 92: Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![Image 93: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 20, 2026[#### DNS OverDoS: Are Private Endpoints Too Private?](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)
*   [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
*   [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")

[Read now ![Image 94: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Image 95: Pictorial representation of MongoBleed, CVE-2025-14847. Digital image featuring a glowing padlock icon superimposed on a background of streaming blue binary code, symbolizing cybersecurity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/AdobeStock_233494953-786x429.jpeg)

[![Image 96: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)January 13, 2026[#### Threat Brief: MongoDB Vulnerability (CVE-2025-14847)](https://unit42.paloaltonetworks.com/mongobleed-cve-2025-14847/)
*   [CVE-2025-14847](https://unit42.paloaltonetworks.com/tag/cve-2025-14847/ "CVE-2025-14847")
*   [MongoDB](https://unit42.paloaltonetworks.com/tag/mongodb/ "MongoDB")

[Read now ![Image 97: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/mongobleed-cve-2025-14847/ "Threat Brief: MongoDB Vulnerability (CVE-2025-14847)")

![Image 98: Pictorial representation of remote code execution in AI and machine learning libraries. Close-up of a woman wearing glasses and focusing intently on a computer screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/05_Vulnerabilities_1920x900-786x368.jpg)

[![Image 99: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 13, 2026[#### Remote Code Execution With Modern AI/ML Formats and Libraries](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/)
*   [Apple](https://unit42.paloaltonetworks.com/tag/apple/ "Apple")
*   [CVE-2025-23304](https://unit42.paloaltonetworks.com/tag/cve-2025-23304/ "CVE-2025-23304")
*   [CVE-2026-22584](https://unit42.paloaltonetworks.com/tag/cve-2026-22584/ "CVE-2026-22584")

[Read now ![Image 100: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/ "Remote Code Execution With Modern AI/ML Formats and Libraries")

![Image 101: Pictorial representation of CVE-2025-55182 (React) and CVE-2025-66478 (Next.js). Close-up of a digital display on electronic equipment with illuminated text reading "SYSTEM HACKED" in red, set against a blurred background of blue and red lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/12/02_Vulnerabilities_1920x900-786x368.jpg)

[![Image 102: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)December 12, 2025[#### Exploitation of Critical Vulnerability in React Server Components (Updated December 12)](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/)
*   [Cobalt Strike](https://unit42.paloaltonetworks.com/tag/cobalt-strike/ "Cobalt Strike")
*   [CVE-2025-55182](https://unit42.paloaltonetworks.com/tag/cve-2025-55182/ "CVE-2025-55182")
*   [CVE-2025-66478](https://unit42.paloaltonetworks.com/tag/cve-2025-66478/ "CVE-2025-66478")

[Read now ![Image 103: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/ "Exploitation of Critical Vulnerability in React Server Components (Updated December 12)")

![Image 104: Pictorial representation of an authentication coercion attack. Panoramic view of a city skyline at night, featuring vibrant light beams from skyscrapers and a deep blue sky.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/07_Vulnerabilities_1920x900-786x368.jpg)

[![Image 105: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)November 10, 2025[#### You Thought It Was Over? Authentication Coercion Keeps Evolving](https://unit42.paloaltonetworks.com/authentication-coercion/)
*   [Mimikatz](https://unit42.paloaltonetworks.com/tag/mimikatz/ "Mimikatz")
*   [PrintNightmare](https://unit42.paloaltonetworks.com/tag/printnightmare/ "PrintNightmare")
*   [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")

[Read now ![Image 106: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/authentication-coercion/ "You Thought It Was Over? Authentication Coercion Keeps Evolving")

*   ![Image 107: Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
*   ![Image 108: Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Image 109: Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)![Image 110: Enlarged Image](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)

![Image 111: Newsletter](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/unit42-footer-subscribe-desktop.png)

![Image 112: UNIT 42 Small Logo](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/palo-alto-logo-small.svg) Get updates from Unit 42 
## Peace of mind comes from staying ahead of threats. Subscribe today.

Your Email 
Subscribe for email updates to all Unit 42 threat research.

 By submitting this form, you agree to our [Terms of Use](https://www.paloaltonetworks.com/legal-notices/terms-of-use "Terms of Use") and acknowledge our [Privacy Statement.](https://www.paloaltonetworks.com/legal-notices/privacy "Privacy Statement")

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

Invalid captcha!

 Subscribe ![Image 113: Right Arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/right-arrow.svg)![Image 114: loader](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-loader.svg)

[](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/)

## Products and Services

*   [AI-Powered Network Security Platform](https://www.paloaltonetworks.com/network-security)
*   [Secure AI by Design](https://www.paloaltonetworks.com/ai-security)
*   [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security)
*   [AI Access Security](https://www.paloaltonetworks.com/sase/ai-access-security)
*   [Cloud Delivered Security Services](https://www.paloaltonetworks.com/network-security/security-subscriptions)
*   [Advanced Threat Prevention](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention)
*   [Advanced URL Filtering](https://www.paloaltonetworks.com/network-security/advanced-url-filtering)
*   [Advanced WildFire](https://www.paloaltonetworks.com/network-security/advanced-wildfire)
*   [Advanced DNS Security](https://www.paloaltonetworks.com/network-security/advanced-dns-security)
*   [Enterprise Data Loss Prevention](https://www.paloaltonetworks.com/sase/enterprise-data-loss-prevention)
*   [Enterprise IoT Security](https://www.paloaltonetworks.com/network-security/enterprise-device-security)
*   [Medical IoT Security](https://www.paloaltonetworks.com/network-security/medical-device-security)
*   [Industrial OT Security](https://www.paloaltonetworks.com/network-security/medical-device-security)
*   [SaaS Security](https://www.paloaltonetworks.com/sase/saas-security)

*   [Next-Generation Firewalls](https://www.paloaltonetworks.com/network-security/next-generation-firewall)
*   [Hardware Firewalls](https://www.paloaltonetworks.com/network-security/hardware-firewall-innovations)
*   [Software Firewalls](https://www.paloaltonetworks.com/network-security/software-firewalls)
*   [Strata Cloud Manager](https://www.paloaltonetworks.com/network-security/strata-cloud-manager)
*   [SD-WAN for NGFW](https://www.paloaltonetworks.com/network-security/sd-wan-subscription)
*   [PAN-OS](https://www.paloaltonetworks.com/network-security/pan-os)
*   [Panorama](https://www.paloaltonetworks.com/network-security/panorama)
*   [Secure Access Service Edge](https://www.paloaltonetworks.com/sase)
*   [Prisma SASE](https://www.paloaltonetworks.com/sase)
*   [Application Acceleration](https://www.paloaltonetworks.com/sase/app-acceleration)
*   [Autonomous Digital Experience Management](https://www.paloaltonetworks.com/sase/adem)
*   [Enterprise DLP](https://www.paloaltonetworks.com/sase/enterprise-data-loss-prevention)
*   [Prisma Access](https://www.paloaltonetworks.com/sase/access)
*   [Prisma Browser](https://www.paloaltonetworks.com/sase/prisma-browser)
*   [Prisma SD-WAN](https://www.paloaltonetworks.com/sase/sd-wan)
*   [Remote Browser Isolation](https://www.paloaltonetworks.com/sase/remote-browser-isolation)
*   [SaaS Security](https://www.paloaltonetworks.com/sase/saas-security)

*   [AI-Driven Security Operations Platform](https://www.paloaltonetworks.com/cortex)
*   [Cloud Security](https://www.paloaltonetworks.com/cortex/cloud)
*   [Cortex Cloud](https://www.paloaltonetworks.com/cortex/cloud)
*   [Application Security](https://www.paloaltonetworks.com/cortex/cloud/application-security)
*   [Cloud Posture Security](https://www.paloaltonetworks.com/cortex/cloud/cloud-posture-security)
*   [Cloud Runtime Security](https://www.paloaltonetworks.com/cortex/cloud/runtime-security)
*   [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud)
*   [AI-Driven SOC](https://www.paloaltonetworks.com/cortex)
*   [Cortex XSIAM](https://www.paloaltonetworks.com/cortex/cortex-xsiam)
*   [Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr)
*   [Cortex XSOAR](https://www.paloaltonetworks.com/cortex/cortex-xsoar)
*   [Cortex Xpanse](https://www.paloaltonetworks.com/cortex/cortex-xpanse)
*   [Unit 42 Managed Detection & Response](https://www.paloaltonetworks.com/cortex/managed-detection-and-response)
*   [Managed XSIAM](https://www.paloaltonetworks.com/cortex/managed-xsiam)

*   [Threat Intel and Incident Response Services](https://www.paloaltonetworks.com/unit42)
*   [Proactive Assessments](https://www.paloaltonetworks.com/unit42/assess)
*   [Incident Response](https://www.paloaltonetworks.com/unit42/respond)
*   [Transform Your Security Strategy](https://www.paloaltonetworks.com/unit42/transform)
*   [Discover Threat Intelligence](https://www.paloaltonetworks.com/unit42/threat-intelligence-partners)

## Company

*   [About Us](https://www.paloaltonetworks.com/about-us)
*   [Careers](https://jobs.paloaltonetworks.com/en/)
*   [Contact Us](https://www.paloaltonetworks.com/company/contact-sales)
*   [Corporate Responsibility](https://www.paloaltonetworks.com/about-us/corporate-responsibility)
*   [Customers](https://www.paloaltonetworks.com/customers)
*   [Investor Relations](https://investors.paloaltonetworks.com/)
*   [Location](https://www.paloaltonetworks.com/about-us/locations)
*   [Newsroom](https://www.paloaltonetworks.com/company/newsroom)

## Popular Links

*   [Blog](https://www.paloaltonetworks.com/blog/)
*   [Communities](https://www.paloaltonetworks.com/communities)
*   [Content Library](https://www.paloaltonetworks.com/resources)
*   [Cyberpedia](https://www.paloaltonetworks.com/cyberpedia)
*   [Event Center](https://events.paloaltonetworks.com/)
*   [Manage Email Preferences](https://start.paloaltonetworks.com/preference-center)
*   [Products A-Z](https://www.paloaltonetworks.com/products/products-a-z)
*   [Product Certifications](https://www.paloaltonetworks.com/legal-notices/trust-center/compliance)
*   [Report a Vulnerability](https://www.paloaltonetworks.com/security-disclosure)
*   [Sitemap](https://www.paloaltonetworks.com/sitemap)
*   [Tech Docs](https://docs.paloaltonetworks.com/)
*   [Unit 42](https://unit42.paloaltonetworks.com/)
*   [Do Not Sell or Share My Personal Information](https://panwedd.exterro.net/portal/dsar.htm?target=panwedd)

![Image 115: PAN logo](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/pan-logo-dark.svg)

*   [Privacy](https://www.paloaltonetworks.com/legal-notices/privacy)
*   [Trust Center](https://www.paloaltonetworks.com/legal-notices/trust-center)
*   [Terms of Use](https://www.paloaltonetworks.com/legal-notices/terms-of-use)
*   [Documents](https://www.paloaltonetworks.com/legal)

Copyright © 2026 Palo Alto Networks. All Rights Reserved

*   [![Image 116: Youtube](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/youtube-black.svg)](https://www.youtube.com/user/paloaltonetworks)
*   [![Image 117: Podcast](https://www.paloaltonetworks.com/content/dam/pan/en_US/images/icons/podcast.svg)](https://www.paloaltonetworks.com/podcasts/threat-vector)
*   [![Image 118: Facebook](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/facebook-black.svg)](https://www.facebook.com/PaloAltoNetworks/)
*   [![Image 119: LinkedIn](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/linkedin-black.svg)](https://www.linkedin.com/company/palo-alto-networks)
*   [![Image 120: Twitter](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/twitter-x-black.svg)](https://twitter.com/PaloAltoNtwks)
*   EN Select your language  

![Image 121: Play](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-play-icon.svg)![Image 122: Pause](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-pause-icon1.svg)![Image 123: Minimize](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-minimize.svg)![Image 124: Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)Your browser does not support the video tag. 

### Default Heading

[Read the article ![Image 125: Right Arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/right-arrow.svg)](https://unit42.paloaltonetworks.com/sugarcrm-cloud-incident-black-hat/# "Right Arrow Icon")

Seekbar 

![Image 126: Play](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-play-icon.svg)![Image 127: Pause](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-pause-icon1.svg)

![Image 128: Volume](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-volume.svg)

Volume 

![Image 129: Minimize](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-minimize.svg)