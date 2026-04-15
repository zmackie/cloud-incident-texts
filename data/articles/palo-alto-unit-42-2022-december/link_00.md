Title: Compromised Cloud Compute Credentials: Case Studies From the Wild

URL Source: https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/

Published Time: 2022-12-08T00:00:00+00:00

Markdown Content:
# Compromised Cloud Compute Credentials: Case Studies From the Wild

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
*   [Services](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/#)

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

*   [Unit 42 Threat Research](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/#)

 ![Image 8: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)Unit 42 Threat Research 

[Unit 42 Threat Research](https://unit42.paloaltonetworks.com/)

 

    *   [Threat Briefs and Assessments Details on the latest cyber threats](https://unit42.paloaltonetworks.com/category/threat-research/)
    *   [Tools Lists of public tools released by our team](https://unit42.paloaltonetworks.com/tools/)
    *   [Threat Reports Downloadable, in-depth research reports](https://www.paloaltonetworks.com/resources?q=*%3A*&_charset_=UTF-8&fq=PRODUCTS0_DFACET%3Apan%253Aresource-center%252Fproducts0%252Funit42-managed-detection-and-response&fq=RC_TYPE_DFACET%3Apan%253Aresource-center%252Frc-type%252Fresearch)

[THREAT REPORT 2026 Unit 42 Global Incident Response Report Read now](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report)

[THREAT BRIEF Russia-Ukraine Cyberattacks: How to Protect Against Related Cyberthreats Including DDoS, HermeticWiper, Gamaredon, Website Defacement Learn more](https://unit42.paloaltonetworks.com/preparing-for-cyber-impact-russia-ukraine-crisis/)

[THREAT REPORT Highlights from the Unit 42 Cloud Threat Report, Volume 6 Learn more](https://www.paloaltonetworks.com/resources/research/unit-42-cloud-threat-report-volume-6)

*   [Partners](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/#)

 ![Image 9: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)Partners 

Partners 

 

    *   [Threat Intelligence Sharing](https://www.paloaltonetworks.com/unit42/threat-intelligence-partners)
    *   [Law Firms and Insurance Providers](https://www.paloaltonetworks.com/unit42/incident-response-partners)

[THREAT REPORT 2026 Unit 42 Global Incident Response Report Read now](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report)

[THREAT BRIEF Russia-Ukraine Cyberattacks: How to Protect Against Related Cyberthreats Including DDoS, HermeticWiper, Gamaredon, Website Defacement Learn more](https://unit42.paloaltonetworks.com/preparing-for-cyber-impact-russia-ukraine-crisis/)

[THREAT BRIEF Operation Falcon II: Unit 42 Helps Interpol Identify Nigerian Business Email Compromise Ring Members Learn more](https://unit42.paloaltonetworks.com/operation-falcon-ii-silverterrier-nigerian-bec/)

*   [Resources](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/#)

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

*   [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/#)
*   [Under Attack?](https://start.paloaltonetworks.com/contact-unit42.html)

[![Image 11: palo alto networks logo icon](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/logo-default.svg)![Image 12: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/#)

Search

 All 
*   [Tech Docs](https://docs.paloaltonetworks.com/search#q=unit%2042&sort=relevancy&layout=card&numberOfResults=25)

[English](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/#)

*   [English](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)
*   [Japanese](https://unit42.paloaltonetworks.com/ja/compromised-cloud-compute-credentials/)

*   [Threat Research Center](https://unit42.paloaltonetworks.com/ "Threat Research")
*   [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
*   [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")

[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
# Compromised Cloud Compute Credentials: Case Studies From the Wild

![Image 13: Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 9 min read 

Related Products

[![Image 14: Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Image 15: Prisma Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud](https://unit42.paloaltonetworks.com/product-category/prisma-cloud/ "Prisma Cloud")[![Image 16: Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

*   ![Image 17: Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    *   [Dror Alon](https://unit42.paloaltonetworks.com/author/dror-alon/)

*   ![Image 18: Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)Published:December 8, 2022 
*   ![Image 19: Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    *   [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
    *   [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

*   ![Image 20: Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    *   [AWS](https://unit42.paloaltonetworks.com/tag/aws/)
    *   [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/)
    *   [Cryptocurrency mining](https://unit42.paloaltonetworks.com/tag/cryptocurrency-mining/)
    *   [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/)
    *   [IAM](https://unit42.paloaltonetworks.com/tag/iam/)

*   [![Image 21: Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/?pdf=download&lg=en&_wpnonce=57e8089dbf "Click here to download")
*   [![Image 22: Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/?pdf=print&lg=en&_wpnonce=57e8089dbf "Click here to print")

[Share![Image 23: Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/# "Click here to share")
*   [![Image 24: Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/# "Copy link")
*   [![Image 25: Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Compromised%20Cloud%20Compute%20Credentials:%20Case%20Studies%20From%20the%20Wild&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fcompromised-cloud-compute-credentials%2F "Share in email")
*   [![Image 26: Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcompromised-cloud-compute-credentials%2F "Share in Facebook")
*   [![Image 27: LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcompromised-cloud-compute-credentials%2F&title=Compromised%20Cloud%20Compute%20Credentials:%20Case%20Studies%20From%20the%20Wild "Share in LinkedIn")
*   [![Image 28: Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcompromised-cloud-compute-credentials%2F&text=Compromised%20Cloud%20Compute%20Credentials:%20Case%20Studies%20From%20the%20Wild "Share in Twitter")
*   [![Image 29: Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](https://www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcompromised-cloud-compute-credentials%2F "Share in Reddit")
*   [![Image 30: Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Compromised%20Cloud%20Compute%20Credentials:%20Case%20Studies%20From%20the%20Wild%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fcompromised-cloud-compute-credentials%2F "Share in Mastodon")

## [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)**Executive Summary**

Cloud breaches often stem from misconfigured storage services or exposed credentials. A growing trend of attacks specifically targets cloud compute services to steal associated credentials and illicitly gain access to cloud infrastructure. These attacks could cost targeted organizations both in terms of unexpected charges for extra cloud resources added by the threat actor, as well as time required to remediate the damage.

This blog highlights two examples of cloud compute credentials attacks in the wild. While the initial access phase is important, we will focus on the post-breach actions executed during the attack, and share the flow of these two attacks against the cloud infrastructure. The [attack flows](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/#post-125981-_fueofwtqb3rq) show how threat actors abuse stolen compute credentials to pursue a variety of attack vectors (such as cryptomining, data theft, etc.) and abuse cloud services in unexpected ways.

To detect the attacks described below, cloud logging and monitoring best practices as outlined by Amazon Web Services ([AWS](https://aws.amazon.com/blogs/mt/aws-cloudtrail-best-practices/)) and [Google Cloud](https://cloud.google.com/logging/docs/audit/best-practices) are essential, as they provide visibility into activity at the cloud infrastructure level. This emphasizes how important it is to follow Amazon Web Services and Google Cloud logging and monitoring best practices.

Palo Alto Networks helps organizations address security issues in the cloud with [Cortex XDR for cloud](https://www.paloaltonetworks.com/cortex/cloud-detection-and-response), which detects cloud attacks such as cloud compute credentials theft and [Prisma Cloud](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin/prisma-cloud-iam-security), which manages identity entitlement with least privilege entitlements.

Related Unit 42 Topics[Cloud](https://unit42.paloaltonetworks.com/category/cloud/), [phishing](https://unit42.paloaltonetworks.com/tag/phishing/), [cloud security](https://unit42.paloaltonetworks.com/tag/cloud-security/), [coin miner](https://unit42.paloaltonetworks.com/tag/coin-miner/)

## [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)**Key Principle of Working in the Cloud**

Before diving in, we should understand a very basic and important rule of working in the cloud. An entity, whether a human or a [compute workload](https://www.webopedia.com/definitions/workload/), needs legitimate and associated credentials to access a cloud environment at the infrastructure level. The credentials are used for authentication (to verify the entity’s identity) and authorization (to verify what the entity is allowed to do).

As a best practice, when a compute workload executes API calls in the cloud (e.g., to query a storage service), the workload’s associated credentials should be dedicated only to it. They should also be used only by that workload or human, and not by anyone else.

As we will see in both examples, an important security principle that can help reduce risk in cloud compute credentials attacks is [least privilege access](https://www.paloaltonetworks.com/cyberpedia/what-is-least-privilege-access). In particular, this means that the privileges associated with those credentials should be scoped down to the minimum set actually required by the code using them.This limits the actions an attacker can take when compute credentials are stolen.

## [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)**Attack Case 1: Compromised AWS Lambda C**redentials Led to Phishing Attack

An attacker was able to execute API calls on the behalf of the [Lambda](https://aws.amazon.com/lambda/features/#:~:text=AWS%20Lambda%20is%20a%20serverless,cart%20on%20an%20ecommerce%20website.) function by stealing the Lambda’s credentials. This allowed the attacker to execute multiple API calls and enumerate different services in the cloud environment, as shown in Figure 1. While most of these API calls were not allowed due to lack of privileges, the attack resulted in a phishing attack launched from a AWS Simple Email Service (SES) that the threat actor created.

![Image 31: Image 1 is a screenshot of Amazon Web Services showing a branch diagram of an attacker impersonating a Lambda function by stealing the Lambda’s token inside the cloud environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image-23.png)

Figure 1. An attacker enumerating the cloud environment using a compromised Lambda function’s credentials.

This phishing attack not only resulted in unexpected costs for the organization, it also exposed other organizations to extra risk as well.

While the outcome of this attack caused substantial impact, it could have been greater. In this case the victim didn’t have an active SES, but if they had, the attacker could have abused it to launch an attack on the victim’s organization or they could even have used a legitimate email account for the phishing attack.

Due to the variety of cloud services used by organizations, it can be difficult to predict where a cloud attack will end. Going from cloud to phishing was not necessarily an expected path.

### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)Attack Flow

An attacker was able to exfiltrate the Lambda’s environment variables and export them into their attacking machine (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN).

As the credentials were exfiltrated, the attack was launched with the following steps:

#### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)> WHOAMI - 2022-05-20T20:35:49 UTC

The attack started with the GetCallerIdentity command. This command is equivalent to whoami, as it provides information about the entity the credentials are associated with. From the response, the attacker can gain additional information such as the account ID and the credentials type that was stolen. They cannot, however, determine anything about the privileges associated with the identity.

#### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)> Identify and Access Management (IAM) Enumeration - 2022-05-20T20:35:55 UTC

The next phase of the attack was an identity and access management (IAM) enumeration. IAM is considered to be a crown jewel for an attack. By gaining access to IAM, an attacker can elevate permissions and gain persistence on the victim’s account.

The IAM enumeration included two API calls, which were denied due to lack of permissions:

*   ListAttachedRolePolicies
*   ListRolePolicies

It is fair to assume that the attacker noticed the lack of permission and therefore terminated the IAM enumeration after only two commands (possibly to avoid making unnecessary noise).

#### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)> General Enumeration 2022-05-20T20:39:59 UTC

After failing to enumerate IAM, the attacker started an enumeration on different services in different regions. This technique is much noisier as the attacker is trying to learn the architecture of the targeted account and, more importantly, gain access to sensitive information that could exist in the cloud account.

Some of the main services and API calls that were executed were:

Storage Enumeration

*   ListBuckets
*   GetBucketCors
*   GetBucketInventoryConfiguration
*   GetBucketPublicAccessBlock
*   GetBucketMetricsConfiguration
*   GetBucketPolicy
*   GetBucketTagging

EC2 Enumeration

*   GetConsoleScreenshot
*   GetLaunchTemplateData
*   DescribeInstanceTypes
*   DescribeBundleTasks
*   DescribeInstanceAttribute
*   DescribeReplaceRootVolumeTasks

Network Enumeration

*   DescribeCarrierGateways
*   DescribeVpcEndpointConnectionNotifications
*   DescribeTransitGatewayMulticastDomains
*   DescribeClientVpnRoutes
*   DescribeDhcpOptions
*   GetTransitGatewayRouteTableAssociations

Logging Enumeration

*   GetQueryResults
*   GetBucketLogging
*   GetLogRecord
*   GetFlowLogsIntegrationTemplate
*   DescribeLogGroups
*   DescribeLogStreams
*   DescribeFlowLogs
*   DescribeSubscriptionFilters
*   ListTagsLogGroup

Backup Enumeration

*   GetPasswordData
*   GetEbsEncryptionByDefault
*   GetEbsDefaultKmsKeyId
*   GetBucketReplication
*   DescribeVolumes
*   DescribeVolumesModifications
*   DescribeSnapshotAttribute
*   DescribeSnapshotTierStatus
*   DescribeImages

SES Enumeration

*   GetAccount
*   ListIdentities

General Enumeration

*   DescribeRegions
*   DescribeAvailabilityZones
*   DescribeAccountAttributes

#### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)> Backdoor 2022-05-20T20:43:22 UTC

While failing to enumerate IAM, the attacker tried (unsuccessfully) to create a new user by executing the CreateUser command.

#### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)> From the Cloud to a Phishing Attack 2022-05-20T20:44:40 UTC

As most of the API calls during the enumeration resulted in permission denied, the attacker was able to successfully enumerate SES. Therefore, the attacker launched a phishing attack by abusing the cloud email service, which included executing commands such as VerifyEmailIdentity and UpdateAccountSendingEnabled.

#### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)> Defense Evasion 2022-05-20T23:07:06 UTC

Finally, the attacker tried to hide some of his activities by deleting the SES identity by executing the DeleteIdentity command.

## [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)Additional Insights for Detection

A very important indicator of compromise (IoC) for this attack was the IP address 50.82.94[.]112.

API calls from the Lambda function are typically executed from its IP with the credentials (including AccessKeyId) that were generated for the Lambda. Therefore, every API call with that AccessKeyId is considered to be the Lambda function. However, during the attack, the threat actor was able to steal the Lambda's credentials, allowing the attacker to impersonate it.

Because of this, the IP is the key IoC as it is the way to detect that this is not the Lambda. The attacker was using the stolen credentials to impersonate and execute API calls on behalf of the Lambda function, but they were doing so from an IP address that wasn't attached to the Lambda, nor did it belong to the cloud environment.

## [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)Attack Case 2: A Compromised Google Cloud App Engine Service Account Deploying Cryptomining Instances

An attacker was able to steal the credentials for a Google Cloud App Engine service account (SA). There are many ways that attackers can accomplish this that are not necessarily related to any vulnerability in the cloud service provider. In many cases, for example, users store credentials in insecure locations or use easily guessed or brute-forced passwords.

In this case, the stolen SA was the default SA, which had a highly privileged role (Project Editor). This allowed the threat actor to launch an attack that ended with the creation of multiple high-core CPU virtual machines (VMs) for cryptomining purposes, as shown in Figure 2.

![Image 32: Image 2 is a screenshot of an attacker using a compromised app engine service account to find multiple cloud instances to mine.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image-24.png)

Figure 2. An attacker abusing a compromised App Engine SA to allocate multiple cloud instances for mining.

When the threat actor launched thousands of VMs in the victim’s environment, it significantly increased their expected costs. Even if someone had noticed an attack like this in their environment after a short period of time, it would still have had a substantial cost impact.

### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)Attack Flow

Google App Engine is a Google Cloud fully managed serverless platform, and the service account is the token. When the user creates an App Engine instance, the cloud provider creates a default SA and attaches it to the created App Engine.

This App Engine default SA has the editor role in the project. The editor role is highly privileged, which is a key factor the attacker took advantage of. This role allowed execution of high-privilege API calls, such as the following:

*   Compute workload launch
*   Firewall (FW) rule modification
*   SA key creation

#### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)> Privilege Escalation 2022-06-16T12:21:17.624 UTC

The attack started with an attempt to escalate privileges. As mentioned above, by default the App Engine’s SA has editor permissions on the project. With these permissions, the attacker tried to add the compute/admin role by adding the following object into the IAM policy:

![Image 33: Image 3 is a screenshot of 3 lines of code where the threat actor adds an object into the IAM policy in order to add an admin role.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image-25.png)

As we can see, the appspot in the SA domain prefix indicates this SA belongs to an App Engine service.

#### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)> Allow Any/Any 2022-06-16T12:21:29.406 UTC

Next the attacker modified the FW rules on the project level. First, the attacker attempted to create a subnet (named default). Then, the attacker added the rule below into that subnet:

![Image 34: Image 4 is a screenshot of 12 lines of code where the threat actor has tried to create a subnet named “default” and is now adding a rule below that in the subnet to allow for cryptocurrency mining.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image-26.png)

This action furthers the attacker’s goal of [mining cryptocurrency](https://www.paloaltonetworks.com/blog/security-operations/stopping-cryptojacking-attacks-with-and-without-an-agent/). To enable unlimited cryptocurrency mining, the attacker removed any limitation on the networking level.

It is important to note the priority field. By setting this to zero, the attacker’s rule is set to the highest priority, meaning it will take effect first in the order of the existing FW rules.

#### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)> An Army of Miners 2022-06-16T12:21:38.916 UTC

Once setup was complete, the main phase of the attack began, launching VMs in multiple regions.

While the attacker could have created high CPU machines, in this case the attacker instead created a standard VM (e.g., n1-standard-2) equipped with four high performance GPUs (e.g., nvidia-tesla-p100):

![Image 35: Image 5 is a screenshot of many lines of code demonstrating how the threat actor created standard virtual machines, creating more than 1,600 in total.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/image4-1.png)

Overall, more than 1,600 VMs were created during this attack.

#### [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)> Backdoor 2022-06-16T13:25:56.037 UTC

The attacker assumed the SA key used for the attack would be detected and revoked, and therefore created multiple SA keys (for later usage) by executing the google.iam.admin.v1.CreateServiceAccountKey API call.

## [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)Additional Insights for Detection

As in the first case we discussed, the IP is an important IoC. In this case, the attack was launched from multiple IPs (nine different IPs overall), some of which were active Tor exit nodes.

Again, we expect the App Engine’s SA to be used from an IP within the cloud environment. It definitely should not be used from a Tor exit node.

Firewall rule modification is a common and popular technique used in attacks like these. Many organizations enforce network traffic rules that deny access to active mining pools, so attackers must modify firewall rules to accomplish their goals.

Lastly, by editing a network named default, the attacker tried to avoid detection. Unless this option is disabled, by default each new project is created with a default network. It seems the attacker was trying to take advantage of this, thus avoiding having to create their own network.

## [](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)**Conclusion**:**Compute Token Theft** Is a**Growing Threat**

The theft of a compute workload’s token is the common denominator for both cases we’ve discussed. While both examples above involve serverless services, this attack vector is relevant to all compute services.

It is important to emphasize that this type of attack could occur from different attack paths – including application vulnerabilities or zero-day exploits such as [Log4Shell](https://www.paloaltonetworks.com/log4shell) – not only from misconfigurations or poor cloud security posture management (CSPM).

To handle such attacks, cloud audit logs are essential, both for detection and for investigation and response (IR). Cloud audit monitoring is even more critical for serverless workloads where agents cannot be installed, thus making it harder to stop such attacks.

Logging and monitoring best practices provided by [AWS](https://aws.amazon.com/blogs/mt/aws-cloudtrail-best-practices/) and [Google Cloud](https://cloud.google.com/logging/docs/audit/best-practices) give clear guidance for how to prevent such cases. The AWS [GuardDuty](https://aws.amazon.com/guardduty/) service could also help with detecting and alerting on similar attacks, such as [EC2 instance credentials used from another AWS account](https://aws.amazon.com/about-aws/whats-new/2022/01/amazon-guardduty-ec2-instance-credentials-aws-account/). An additional prevention method is to [configure an interface endpoint policy for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-endpoints.html#vpc-endpoint-policy) to limit the usage of Lambda only within a VPC.

Palo Alto Networks customers receive protections from compute token theft with:

*   [Cortex XDR for cloud](https://www.paloaltonetworks.com/cortex/cloud-detection-and-response), which provides SOC teams with a full incident story across the entire digital domain by integrating activity from cloud hosts, cloud traffic, and audit logs together with endpoint and network data.
*   [Prisma Cloud](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin/prisma-cloud-iam-security), which assists organizations in managing identity entitlement, addresses the security challenges of managing IAM in cloud environments. Prisma Cloud IAM security capabilities automatically calculate effective permissions across cloud service providers, detect overly permissive access, and suggest corrections to reach least privilege entitlements.

Find out how you can protect your organization from cloud environment attacks with [Unit 42 Cloud Incident Response](https://www.paloaltonetworks.com/resources/datasheets/cloud-incident-response-at-a-glance) services to investigate and respond to attacks and [Cyber Risk Management Services](https://www.paloaltonetworks.com/unit42/assess) to assess your security posture before an attack takes place.

**Learn How to Detect Cloud Threats at Ignite ’22**

 Attend the session “[Unearth advanced threats using your network and cloud data](https://reg.paloaltonetworks.com/flow/paloaltonetworks/ignite22/sessioncatalog/page/view?search.sessiontracks=option_1662500129090&_ga=2.42431329.511218743.1666629774-446934889.1594421039&tab.day=20221214),” at Palo Alto Networks Ignite ’22, the security conference of the future, to find out how to detect compromised cloud compute tokens. Our researchers will show you how to investigate and respond to cloud attacks with a live demonstration. [Register now!](https://reg.ignite.paloaltonetworks.com/flow/paloaltonetworks/ignite22/start/page/main)

Back to top

### Tags

*   [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
*   [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/ "Cloud Security")
*   [Cryptocurrency mining](https://unit42.paloaltonetworks.com/tag/cryptocurrency-mining/ "Cryptocurrency mining")
*   [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
*   [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")

[Threat Research Center](https://unit42.paloaltonetworks.com/ "Threat Research")[Next: Vice Society: Profiling a Persistent Threat to the Education Sector](https://unit42.paloaltonetworks.com/vice-society-targets-education-sector/ "Vice Society: Profiling a Persistent Threat to the Education Sector")

### Table of Contents

### Related Articles

*   [Cracks in the Bedrock: Agent God Mode](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/ "article - table of contents")
*   [Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/ "article - table of contents")
*   [Double Agents: Exposing Security Blind Spots in GCP Vertex AI](https://unit42.paloaltonetworks.com/double-agents-vertex-ai/ "article - table of contents")

## Related Cloud Cybersecurity Research Resources

![Image 36: Futuristic illustration with glowing neon lights and advanced technology motifs, depicting cloud computing and data flow through interconnected networks. The scene is highlighted by hovering digital clouds and dynamic, illuminated linear structures, set in a dramatic, blue and orange color scheme.](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/03_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 37: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)July 22, 2025[#### Cloud Logging for Security and Beyond](https://unit42.paloaltonetworks.com/cloud-logging-for-security/)
*   [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
*   [Azure](https://unit42.paloaltonetworks.com/tag/azure/ "Azure")
*   [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")

[Read now ![Image 38: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cloud-logging-for-security/ "Cloud Logging for Security and Beyond")

![Image 39: Pictorial representation of serverless tokens in the cloud. East Asian woman examining data on multiple screens in a high-tech environment, surrounded by digital graphics and code.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/07_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 40: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)June 13, 2025[#### Serverless Tokens in the Cloud: Exploitation and Detections](https://unit42.paloaltonetworks.com/serverless-authentication-cloud/)
*   [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
*   [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
*   [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")

[Read now ![Image 41: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/serverless-authentication-cloud/ "Serverless Tokens in the Cloud: Exploitation and Detections")

![Image 42: Pictorial representation of ELF-based malware like NoodleRAT, Winnti, SSHdInjector, Pygmy Goat and AcidPour. Vibrant futuristic cityscape with glowing neon lines, clouds, and a dramatic sky at twilight.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 43: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)June 10, 2025[#### The Evolution of Linux Binaries in Targeted Cloud Operations](https://unit42.paloaltonetworks.com/elf-based-malware-targets-cloud/)
*   [Linux Malware](https://unit42.paloaltonetworks.com/tag/linux-malware/ "Linux Malware")
*   [Endpoint](https://unit42.paloaltonetworks.com/tag/endpoint/ "endpoint")

[Read now ![Image 44: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/elf-based-malware-targets-cloud/ "The Evolution of Linux Binaries in Targeted Cloud Operations")

![Image 45: Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 46: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)March 23, 2026[#### Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication/)
*   [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
*   [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
*   [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")

[Read now ![Image 47: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Image 48: Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 49: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)February 6, 2026[#### Novel Technique to Detect Cloud Threat Actor Operations](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)
*   [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
*   [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
*   [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")

[Read now ![Image 50: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Image 51: Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![Image 52: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 20, 2026[#### DNS OverDoS: Are Private Endpoints Too Private?](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)
*   [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
*   [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")

[Read now ![Image 53: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Image 54: Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 55: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)October 24, 2025[#### Cloud Discovery With AzureHound](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)
*   [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
*   [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
*   [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")

[Read now ![Image 56: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

![Image 57: Pictorial representation of a gift card fraud campaign. A glowing skull and crossbones on a circuit board.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/07_Cybercrime_Category_1920x900-786x368.jpg)

[![Image 58: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)October 22, 2025[#### Jingle Thief: Inside a Cloud-Based Gift Card Fraud Campaign](https://unit42.paloaltonetworks.com/cloud-based-gift-card-fraud-campaign/)
*   [CL‑CRI‑1032](https://unit42.paloaltonetworks.com/tag/cl-cri-1032/ "CL‑CRI‑1032")
*   [Microsoft](https://unit42.paloaltonetworks.com/tag/microsoft/ "Microsoft")
*   [Phishing](https://unit42.paloaltonetworks.com/tag/phishing/ "phishing")

[Read now ![Image 59: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cloud-based-gift-card-fraud-campaign/ "Jingle Thief: Inside a Cloud-Based Gift Card Fraud Campaign")

![Image 60: Pictorial representation of a vibrant cityscape emerging from a sea of clouds under a sunset sky.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/09/02_Cloud_cybersecurity_research_Category_1505x922-718x440.jpg)

[![Image 61: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/)October 7, 2025[#### Responding to Cloud Incidents: A Step-by-Step Guide From the 2025 Unit 42 Global Incident Response Report](https://unit42.paloaltonetworks.com/responding-to-cloud-incidents/)
*   [Cloud Infrastructure Protection](https://unit42.paloaltonetworks.com/tag/cloud-infrastructure-protection/ "Cloud Infrastructure Protection")
*   [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/ "Cloud Security")
*   [Unit 42 Incident Response Report](https://unit42.paloaltonetworks.com/tag/unit-42-incident-response-report/ "Unit 42 Incident Response Report")

[Read now ![Image 62: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/responding-to-cloud-incidents/ "Responding to Cloud Incidents: A Step-by-Step Guide From the 2025 Unit 42 Global Incident Response Report")

![Image 63: Pictorial representation of model namespace reuse. A vibrant digital illustration featuring a glowing cloud icon with a padlock, symbolizing cloud security technology, set against a backdrop of glowing circuit lines in blue and orange.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/05_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 64: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)September 3, 2025[#### Model Namespace Reuse: An AI Supply-Chain Attack Exploiting Model Name Trust](https://unit42.paloaltonetworks.com/model-namespace-reuse/)
*   [Azure](https://unit42.paloaltonetworks.com/tag/azure/ "Azure")
*   [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")
*   [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")

[Read now ![Image 65: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/model-namespace-reuse/ "Model Namespace Reuse: An AI Supply-Chain Attack Exploiting Model Name Trust")

![Image 66: Futuristic illustration with glowing neon lights and advanced technology motifs, depicting cloud computing and data flow through interconnected networks. The scene is highlighted by hovering digital clouds and dynamic, illuminated linear structures, set in a dramatic, blue and orange color scheme.](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/03_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 67: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)July 22, 2025[#### Cloud Logging for Security and Beyond](https://unit42.paloaltonetworks.com/cloud-logging-for-security/)
*   [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
*   [Azure](https://unit42.paloaltonetworks.com/tag/azure/ "Azure")
*   [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")

[Read now ![Image 68: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cloud-logging-for-security/ "Cloud Logging for Security and Beyond")

![Image 69: Pictorial representation of serverless tokens in the cloud. East Asian woman examining data on multiple screens in a high-tech environment, surrounded by digital graphics and code.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/07_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 70: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)June 13, 2025[#### Serverless Tokens in the Cloud: Exploitation and Detections](https://unit42.paloaltonetworks.com/serverless-authentication-cloud/)
*   [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
*   [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
*   [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")

[Read now ![Image 71: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/serverless-authentication-cloud/ "Serverless Tokens in the Cloud: Exploitation and Detections")

![Image 72: Pictorial representation of ELF-based malware like NoodleRAT, Winnti, SSHdInjector, Pygmy Goat and AcidPour. Vibrant futuristic cityscape with glowing neon lines, clouds, and a dramatic sky at twilight.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 73: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)June 10, 2025[#### The Evolution of Linux Binaries in Targeted Cloud Operations](https://unit42.paloaltonetworks.com/elf-based-malware-targets-cloud/)
*   [Linux Malware](https://unit42.paloaltonetworks.com/tag/linux-malware/ "Linux Malware")
*   [Endpoint](https://unit42.paloaltonetworks.com/tag/endpoint/ "endpoint")

[Read now ![Image 74: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/elf-based-malware-targets-cloud/ "The Evolution of Linux Binaries in Targeted Cloud Operations")

![Image 75: Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 76: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)March 23, 2026[#### Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication/)
*   [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
*   [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
*   [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")

[Read now ![Image 77: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Image 78: Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 79: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)February 6, 2026[#### Novel Technique to Detect Cloud Threat Actor Operations](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)
*   [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
*   [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
*   [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")

[Read now ![Image 80: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Image 81: Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![Image 82: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 20, 2026[#### DNS OverDoS: Are Private Endpoints Too Private?](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)
*   [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
*   [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")

[Read now ![Image 83: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Image 84: Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 85: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)October 24, 2025[#### Cloud Discovery With AzureHound](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)
*   [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
*   [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
*   [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")

[Read now ![Image 86: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

![Image 87: Pictorial representation of a gift card fraud campaign. A glowing skull and crossbones on a circuit board.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/07_Cybercrime_Category_1920x900-786x368.jpg)

[![Image 88: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)October 22, 2025[#### Jingle Thief: Inside a Cloud-Based Gift Card Fraud Campaign](https://unit42.paloaltonetworks.com/cloud-based-gift-card-fraud-campaign/)
*   [CL‑CRI‑1032](https://unit42.paloaltonetworks.com/tag/cl-cri-1032/ "CL‑CRI‑1032")
*   [Microsoft](https://unit42.paloaltonetworks.com/tag/microsoft/ "Microsoft")
*   [Phishing](https://unit42.paloaltonetworks.com/tag/phishing/ "phishing")

[Read now ![Image 89: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cloud-based-gift-card-fraud-campaign/ "Jingle Thief: Inside a Cloud-Based Gift Card Fraud Campaign")

![Image 90: Pictorial representation of a vibrant cityscape emerging from a sea of clouds under a sunset sky.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/09/02_Cloud_cybersecurity_research_Category_1505x922-718x440.jpg)

[![Image 91: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/)October 7, 2025[#### Responding to Cloud Incidents: A Step-by-Step Guide From the 2025 Unit 42 Global Incident Response Report](https://unit42.paloaltonetworks.com/responding-to-cloud-incidents/)
*   [Cloud Infrastructure Protection](https://unit42.paloaltonetworks.com/tag/cloud-infrastructure-protection/ "Cloud Infrastructure Protection")
*   [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/ "Cloud Security")
*   [Unit 42 Incident Response Report](https://unit42.paloaltonetworks.com/tag/unit-42-incident-response-report/ "Unit 42 Incident Response Report")

[Read now ![Image 92: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/responding-to-cloud-incidents/ "Responding to Cloud Incidents: A Step-by-Step Guide From the 2025 Unit 42 Global Incident Response Report")

![Image 93: Pictorial representation of model namespace reuse. A vibrant digital illustration featuring a glowing cloud icon with a padlock, symbolizing cloud security technology, set against a backdrop of glowing circuit lines in blue and orange.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/05_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 94: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)September 3, 2025[#### Model Namespace Reuse: An AI Supply-Chain Attack Exploiting Model Name Trust](https://unit42.paloaltonetworks.com/model-namespace-reuse/)
*   [Azure](https://unit42.paloaltonetworks.com/tag/azure/ "Azure")
*   [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")
*   [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")

[Read now ![Image 95: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/model-namespace-reuse/ "Model Namespace Reuse: An AI Supply-Chain Attack Exploiting Model Name Trust")

![Image 96: Futuristic illustration with glowing neon lights and advanced technology motifs, depicting cloud computing and data flow through interconnected networks. The scene is highlighted by hovering digital clouds and dynamic, illuminated linear structures, set in a dramatic, blue and orange color scheme.](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/03_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 97: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)July 22, 2025[#### Cloud Logging for Security and Beyond](https://unit42.paloaltonetworks.com/cloud-logging-for-security/)
*   [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
*   [Azure](https://unit42.paloaltonetworks.com/tag/azure/ "Azure")
*   [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")

[Read now ![Image 98: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cloud-logging-for-security/ "Cloud Logging for Security and Beyond")

![Image 99: Pictorial representation of serverless tokens in the cloud. East Asian woman examining data on multiple screens in a high-tech environment, surrounded by digital graphics and code.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/07_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 100: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)June 13, 2025[#### Serverless Tokens in the Cloud: Exploitation and Detections](https://unit42.paloaltonetworks.com/serverless-authentication-cloud/)
*   [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
*   [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
*   [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")

[Read now ![Image 101: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/serverless-authentication-cloud/ "Serverless Tokens in the Cloud: Exploitation and Detections")

![Image 102: Pictorial representation of ELF-based malware like NoodleRAT, Winnti, SSHdInjector, Pygmy Goat and AcidPour. Vibrant futuristic cityscape with glowing neon lines, clouds, and a dramatic sky at twilight.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 103: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)June 10, 2025[#### The Evolution of Linux Binaries in Targeted Cloud Operations](https://unit42.paloaltonetworks.com/elf-based-malware-targets-cloud/)
*   [Linux Malware](https://unit42.paloaltonetworks.com/tag/linux-malware/ "Linux Malware")
*   [Endpoint](https://unit42.paloaltonetworks.com/tag/endpoint/ "endpoint")

[Read now ![Image 104: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/elf-based-malware-targets-cloud/ "The Evolution of Linux Binaries in Targeted Cloud Operations")

*   ![Image 105: Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
*   ![Image 106: Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Image 107: Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)![Image 108: Enlarged Image](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)

![Image 109: Newsletter](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/unit42-footer-subscribe-desktop.png)

![Image 110: UNIT 42 Small Logo](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/palo-alto-logo-small.svg) Get updates from Unit 42 
## Peace of mind comes from staying ahead of threats. Subscribe today.

Your Email 
Subscribe for email updates to all Unit 42 threat research.

 By submitting this form, you agree to our [Terms of Use](https://www.paloaltonetworks.com/legal-notices/terms-of-use "Terms of Use") and acknowledge our [Privacy Statement.](https://www.paloaltonetworks.com/legal-notices/privacy "Privacy Statement")

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

Invalid captcha!

 Subscribe ![Image 111: Right Arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/right-arrow.svg)![Image 112: loader](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-loader.svg)

[](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/)

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

![Image 113: PAN logo](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/pan-logo-dark.svg)

*   [Privacy](https://www.paloaltonetworks.com/legal-notices/privacy)
*   [Trust Center](https://www.paloaltonetworks.com/legal-notices/trust-center)
*   [Terms of Use](https://www.paloaltonetworks.com/legal-notices/terms-of-use)
*   [Documents](https://www.paloaltonetworks.com/legal)

Copyright © 2026 Palo Alto Networks. All Rights Reserved

*   [![Image 114: Youtube](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/youtube-black.svg)](https://www.youtube.com/user/paloaltonetworks)
*   [![Image 115: Podcast](https://www.paloaltonetworks.com/content/dam/pan/en_US/images/icons/podcast.svg)](https://www.paloaltonetworks.com/podcasts/threat-vector)
*   [![Image 116: Facebook](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/facebook-black.svg)](https://www.facebook.com/PaloAltoNetworks/)
*   [![Image 117: LinkedIn](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/linkedin-black.svg)](https://www.linkedin.com/company/palo-alto-networks)
*   [![Image 118: Twitter](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/twitter-x-black.svg)](https://twitter.com/PaloAltoNtwks)
*   EN Select your language  

![Image 119: Play](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-play-icon.svg)![Image 120: Pause](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-pause-icon1.svg)![Image 121: Minimize](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-minimize.svg)![Image 122: Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)Your browser does not support the video tag. 

### Default Heading

[Read the article ![Image 123: Right Arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/right-arrow.svg)](https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/# "Right Arrow Icon")

Seekbar 

![Image 124: Play](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-play-icon.svg)![Image 125: Pause](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-pause-icon1.svg)

![Image 126: Volume](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-volume.svg)

Volume 

![Image 127: Minimize](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-minimize.svg)