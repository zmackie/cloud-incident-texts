Title: CloudKeys in the Air: Tracking Malicious Operations of Exposed IAM Keys

URL Source: https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/

Published Time: 2023-10-30T00:00:00+00:00

Markdown Content:
# CloudKeys in the Air: Tracking Malicious Operations of Exposed IAM Keys

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
*   [Services](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/#)

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

*   [Unit 42 Threat Research](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/#)

 ![Image 8: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)Unit 42 Threat Research 

[Unit 42 Threat Research](https://unit42.paloaltonetworks.com/)

 

    *   [Threat Briefs and Assessments Details on the latest cyber threats](https://unit42.paloaltonetworks.com/category/threat-research/)
    *   [Tools Lists of public tools released by our team](https://unit42.paloaltonetworks.com/tools/)
    *   [Threat Reports Downloadable, in-depth research reports](https://www.paloaltonetworks.com/resources?q=*%3A*&_charset_=UTF-8&fq=PRODUCTS0_DFACET%3Apan%253Aresource-center%252Fproducts0%252Funit42-managed-detection-and-response&fq=RC_TYPE_DFACET%3Apan%253Aresource-center%252Frc-type%252Fresearch)

[THREAT REPORT 2026 Unit 42 Global Incident Response Report Read now](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report)

[THREAT BRIEF Russia-Ukraine Cyberattacks: How to Protect Against Related Cyberthreats Including DDoS, HermeticWiper, Gamaredon, Website Defacement Learn more](https://unit42.paloaltonetworks.com/preparing-for-cyber-impact-russia-ukraine-crisis/)

[THREAT REPORT Highlights from the Unit 42 Cloud Threat Report, Volume 6 Learn more](https://www.paloaltonetworks.com/resources/research/unit-42-cloud-threat-report-volume-6)

*   [Partners](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/#)

 ![Image 9: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)Partners 

Partners 

 

    *   [Threat Intelligence Sharing](https://www.paloaltonetworks.com/unit42/threat-intelligence-partners)
    *   [Law Firms and Insurance Providers](https://www.paloaltonetworks.com/unit42/incident-response-partners)

[THREAT REPORT 2026 Unit 42 Global Incident Response Report Read now](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report)

[THREAT BRIEF Russia-Ukraine Cyberattacks: How to Protect Against Related Cyberthreats Including DDoS, HermeticWiper, Gamaredon, Website Defacement Learn more](https://unit42.paloaltonetworks.com/preparing-for-cyber-impact-russia-ukraine-crisis/)

[THREAT BRIEF Operation Falcon II: Unit 42 Helps Interpol Identify Nigerian Business Email Compromise Ring Members Learn more](https://unit42.paloaltonetworks.com/operation-falcon-ii-silverterrier-nigerian-bec/)

*   [Resources](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/#)

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

*   [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/#)
*   [Under Attack?](https://start.paloaltonetworks.com/contact-unit42.html)

[![Image 11: palo alto networks logo icon](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/logo-default.svg)![Image 12: white arrow icon pointing left to return to main Palo Alto Networks site](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/arrow-right-black.svg)](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/#)

Search

 All 
*   [Tech Docs](https://docs.paloaltonetworks.com/search#q=unit%2042&sort=relevancy&layout=card&numberOfResults=25)

[English](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/#)

*   [English](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)
*   [Japanese](https://unit42.paloaltonetworks.com/ja/malicious-operations-of-exposed-iam-keys-cryptojacking/)

*   [Threat Research Center](https://unit42.paloaltonetworks.com/ "Threat Research")
*   [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
*   [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")

[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
# CloudKeys in the Air: Tracking Malicious Operations of Exposed IAM Keys

![Image 13: Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 15 min read 

Related Products

[![Image 14: Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Image 15: Prisma Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud](https://unit42.paloaltonetworks.com/product-category/prisma-cloud/ "Prisma Cloud")

*   ![Image 16: Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    *   [William Gamazo](https://unit42.paloaltonetworks.com/author/william-gamazo/)
    *   [Nathaniel Quist](https://unit42.paloaltonetworks.com/author/nathaniel-quist/)

*   ![Image 17: Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)Published:October 30, 2023 
*   ![Image 18: Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    *   [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
    *   [Cybercrime](https://unit42.paloaltonetworks.com/category/cybercrime/)
    *   [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

*   ![Image 19: Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    *   [AWS](https://unit42.paloaltonetworks.com/tag/aws/)
    *   [Cryptojacking](https://unit42.paloaltonetworks.com/tag/cryptojacking/)
    *   [Exposed credentials](https://unit42.paloaltonetworks.com/tag/exposed-credentials/)
    *   [GitHub](https://unit42.paloaltonetworks.com/tag/github/)

*   [![Image 20: Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/?pdf=download&lg=en&_wpnonce=57e8089dbf "Click here to download")
*   [![Image 21: Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/?pdf=print&lg=en&_wpnonce=57e8089dbf "Click here to print")

[Share![Image 22: Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/# "Click here to share")
*   [![Image 23: Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/# "Copy link")
*   [![Image 24: Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=CloudKeys%20in%20the%20Air:%20Tracking%20Malicious%20Operations%20of%20Exposed%20IAM%20Keys&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fmalicious-operations-of-exposed-iam-keys-cryptojacking%2F "Share in email")
*   [![Image 25: Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fmalicious-operations-of-exposed-iam-keys-cryptojacking%2F "Share in Facebook")
*   [![Image 26: LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fmalicious-operations-of-exposed-iam-keys-cryptojacking%2F&title=CloudKeys%20in%20the%20Air:%20Tracking%20Malicious%20Operations%20of%20Exposed%20IAM%20Keys "Share in LinkedIn")
*   [![Image 27: Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fmalicious-operations-of-exposed-iam-keys-cryptojacking%2F&text=CloudKeys%20in%20the%20Air:%20Tracking%20Malicious%20Operations%20of%20Exposed%20IAM%20Keys "Share in Twitter")
*   [![Image 28: Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](https://www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fmalicious-operations-of-exposed-iam-keys-cryptojacking%2F "Share in Reddit")
*   [![Image 29: Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=CloudKeys%20in%20the%20Air:%20Tracking%20Malicious%20Operations%20of%20Exposed%20IAM%20Keys%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fmalicious-operations-of-exposed-iam-keys-cryptojacking%2F "Share in Mastodon")

## Executive Summary

Unit 42 researchers have identified an active campaign we are calling EleKtra-Leak, which performs automated targeting of exposed identity and access management (IAM) credentials within public GitHub repositories. AWS detects and auto-remediates much of the threat of exposed credentials in popular source code repositories by applying a special quarantine policy — but by manually removing that automatic protection, we were able to develop deeper insights into the activities that the actor would carry out in the case where compromised credentials are obtained in some other way.

In those cases, the threat actor associated with the campaign was able to create multiple AWS Elastic Compute (EC2) instances that they used for wide-ranging and long-lasting cryptojacking operations. We believe these operations have been active for at least two years and are still active today.

We found that the actor was able to detect and use the exposed IAM credentials within five minutes of their initial exposure on GitHub. AWS’s automatically applied quarantine policy limited the actor’s ability to operate, but by removing that policy we gained deep insight into the design and automation behind this campaign.

This finding and our broader research specifically highlights how threat actors can leverage cloud automation techniques to achieve their goals of expanding their cryptojacking operations.

We will discuss the threat actor’s operation and how we architected our Prisma Cloud HoneyCloud project to detect and monitor the operation. The HoneyCloud project is a Prisma Cloud Security team research operation to expose a fully compromisable cloud environment that is designed to monitor and track any malicious operations that occur. Prisma Cloud uses this project to gather intelligence about potential attack path scenarios and threat actor operations in an attempt to provide defensive solutions for our cloud customers.

During our monitoring of the cryptojacking pool used in the EleKtra-Leak operation, Aug. 30-Oct. 6, 2023, we found 474 unique miners that were potentially actor-controlled Amazon EC2 instances. Because the actors mined Monero, a type of cryptocurrency that includes privacy controls, we cannot track the wallet to obtain exact figures of how much the threat actors gained.

The threat actor appears to have used automated tools to continually clone public GitHub repositories and scan for exposed Amazon Web Services (AWS) IAM credentials. The threat actor also appeared to blocklist AWS accounts that routinely expose IAM credentials, in what we believe to be an effort to prevent security researchers from following their operations. The threat actors might have perceived them to be obvious honey traps.

To counter this protective operation, we automated the creation of randomized AWS and user accounts with targeted overly-permissive IAM credentials. This allowed us to track the actor’s movements. We committed this information to a randomly generated GitHub repository that publicly exposed the researcher’s IAM credentials.

According to the Unit 42 [Cloud Threat Report Volume 7](https://www.paloaltonetworks.com/prisma/unit42-cloud-threat-research), 83% of organizations expose hard-coded credentials within the production code repositories. The report offers recommendations that organizations can use to improve security around IAM credentials.

We also close this article with a few general [recommendations](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/#post-130743-_sshnnhvjr7q2) that can help protect against the threat actor activity described here. Finally, it is critical that all users of cloud resources understand the cloud [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/). In short, users and organizations are responsible for any configurations, patching, maintenance and security monitoring for their cloud applications, IAM policies and used resources. Build responsibly.

Palo Alto Networks customers receive protection from this type of issue through the features described here in the following ways:

*   The [Prisma Cloud Secrets Security module](https://www.paloaltonetworks.com/prisma/cloud/secrets-security) can detect and block secrets prior to and post-exposure in repositories, validating them for AWS IAM credentials to determine if they are privileged and therefore have a higher impact when exposed.
*   [The Prisma Cloud continuous integration and continuous delivery (CI/CD) module](https://www.paloaltonetworks.com/prisma/cloud/ci-cd-security) can detect misconfigurations, vulnerabilities and the exposure of secrets within public and private infrastructure as code (IaC) repositories such as GitHub. This module can also track the malicious actions of compromised GitHub actions and workload runners.
*   By monitoring GitHub audit events such as cloning GitHub repositories, the CI/CD module can detect the events discussed within this article and protect organizations from adversaries taking advantage of exposed IAM credentials.
*   Palo Alto Networks [Cortex XDR for cloud](https://www.paloaltonetworks.com/cortex/cloud-detection-and-response) leverages data from cloud hosts, cloud traffic and audit logs and combines them with endpoint and network data. This dataset allows XDR to detect unusual cloud activity that correlates with known TTPs such as cloud compute credentials theft, cryptojacking and data exfiltration.

**Related Unit 42 Topics**[**Cloud**](https://unit42.paloaltonetworks.com/category/cloud/), **[Cryptojacking](https://unit42.paloaltonetworks.com/tag/cryptojacking/)**

## [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)The CloudKeys Operation

As Unit 42 researchers working with Prisma Cloud’s security research team, we initiated a project dedicated to monitoring leaked IAM credentials within public GitHub repositories. We did so in an attempt to find active threats leveraging these exposed and vulnerable IAM credentials.

During the investigation, we found a threat actor monitoring for and using exposed AWS keys for cryptomining operations. We are calling this campaign EleKtra-Leak, in reference to the Greek cloud nymph Electra and the usage of Lek as the first three characters in the passwords used by the threat actors. While this kind of cryptojacking activity is not new, this particular operation and its associated indicators lead us to believe that EleKtra-Leak has been active since at least December 2020.

In [research dating back to 2021](https://intezer.com/blog/research/a-rare-look-inside-a-cryptojacking-campaign-and-its-profit/), Intezer issued a report that we believe to be related to EleKtra-Leak. However, it shows the threat actor using different initial access tactics and techniques for leveraging cloud services. Specifically, the actor compromised exposed Docker services (as opposed to scanning and using exposed IAM credentials within GitHub) as we will discuss in this article. The linking factor between these two campaigns is the threat actor using the same customized mining software.

## [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)Background

From a research perspective, one of the challenges of purposefully leaking AWS keys is that once the threat actor identifies them, the keys can be easily attributed to the corresponding [AWS account](https://docs.aws.amazon.com/cli/latest/reference/sts/get-access-key-info.html). We found that the actor can likely recognize frequently recurring AWS account IDs, blocking those account IDs from future attacks or automation scripts. Because of this, we designed a novel investigation architecture to dynamically create and leak AWS keys that are non-attributable. We will discuss this more in the [second section](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/#post-130743-_76r6dq5c40u0) of this article.

Attackers have increased their usage of GitHub as an initial vector of compromise over the years. One powerful feature of GitHub is that it enables the capability to list all public repositories, which is very helpful for its users to easily track developments in topics of interest. This allows developers – and unfortunately threat actors – to track new repositories in real time.

Given this capability, we selected GitHub as the platform for our experiment in leaking AWS keys. We wrote the plaintext leaked keys to a file in a newly created GitHub repository that we randomly selected and cloned from a list of public GitHub repositories. We leaked the AWS keys to a randomly created file inside of the cloned repository and then deleted them after they were successfully committed.

We immediately deleted the leaked keys once they were committed to the repository, to avoid the innate appearance of trying to lure threat actors. Initially, the IAM keys were encoded in Base64. However, no threat actor found the keys, even though tools like [trufflehog](https://github.com/trufflesecurity/trufflehog) can find exposed Base64 IAM keys.

We believe that the identified threat actor is not using tools capable of decoding Base64-encoded credentials at this time. One of the reasons for this is probably because those tools are sometimes noisy and generate many false positives.

We followed up by experimenting with leaking AWS keys in cleartext, which the threat actor did find. These were written in cleartext and hidden behind a past commit in a random file added to the cloned repo.

## [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)GitHub Scanning Operations

When we exposed the AWS keys in GitHub, GitHub's [secret scanning](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning) feature discovered them, and then GitHub programmatically notified AWS about the exposed credentials. This resulted in AWS automatically applying a quarantine policy to the user associated with the keys, called [AWSCompromisedKeyQuarantine](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCompromisedKeyQuarantine.html). This policy prevents a threat actor from performing certain operations, as AWS automatically removes the ability to successfully leverage AWS IAM and EC2 among other API service operations associated with the exposed IAM credential.

Initially, we left the AWS AWSCompromisedKeyQuarantine policy in place, passively monitoring the actor's reconnaissance operations as they tested the exposed keys. Later, as we will discuss in a [following section](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/#post-130743-_76r6dq5c40u0), we intentionally replaced the AWS quarantine policy with the original overly-permissive IAM policy to gain further visibility into the full campaign operation.

It is important to note that the AWS quarantine policy was applied not because the threat actor launched the attack, but because AWS found the keys in GitHub. We believe the threat actor might be able to find exposed AWS keys that aren’t automatically detected by AWS and subsequently control these keys outside of the AWSCompromisedKeyQuarantine policy. According to our evidence, they likely did. In that case, the threat actor could proceed with the attack with no policy interfering with their malicious actions to steal resources from the victims.

Even when GitHub and AWS are coordinated to implement a certain level of protection when AWS keys are leaked, not all cases are covered. We highly recommend that CI/CD security practices, like scanning repos on commit, should be implemented independently.

We also found other potential victims of this campaign who attackers might have targeted in a different manner than what we discuss in this article.

In the case of our experiment with leaked keys, the actor started their operations within four minutes after AWS applied the quarantine policy. Figure 1 shows the timeline of these activities.

![Image 30: Image 1 is a timeline of the attacker’s movements presented as a table. The columns are eventName, userAgent and time. The events begin and end in August 2023 in a very short timespan (minutes). ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/10/word-image-130743-1-2.png)

Figure 1. Attacker’s operation timeline.

The last line in Figure 1 above shows that, starting with the [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) event AttachUserPolicy, AWS applied the quarantine policy at timestamp 13:30:22. Just four minutes later, at 13:34:15, the actors began their reconnaissance operations using the AWS API DescribeRegions. CloudTrail is an auditing tool that records the actions and events that occur within configured cloud resources.

## [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)Actor Operation Architecture

Figure 2 shows the overall threat actor automation architecture. GitHub public repositories are scanned in real time and once the keys are found, the attacker’s automation operation starts.

![Image 31: Image 2 is a diagram of the Operation CloudKeys architecture. Three GitHub icons point to a VPN. From the VPN an arrow points to the threat actor. Three nested boxes demonstrate the architecture: AWS cloud > Honey organization management AWS account, Honey AWS account. Inside the Homey AWS account is the IAM and designed policy, as well as three availability zones. From one of the availability zone is the XMR and the Drive encrypted payload. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/10/word-image-130743-2-2.png)

Figure 2. Operation CloudKeys architecture.

Figure 3 shows that the threat actor starts by performing an AWS account reconnaissance operation.

![Image 32: Image 3 is a table of the AWS account reconnaissance performed by the threat actor. Different actions include DescribeAccountAttributes, DescribeInstanceTypeOfferings, DescribeInstanceTypes and so on. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/10/word-image-130743-3-2.png)

Figure 3. Actor AWS reconnaissance.

After the reconnaissance operation, the threat actor creates AWS security groups (as shown in Figure 4) before finally launching multiple EC2 instances per region across any accessible AWS region.

![Image 33: Image 4 is a table of the security groups modified by the threat actor. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/10/word-image-130743-4-2.png)

Figure 4. Modifying security groups and launching the first EC2 Instance.

The data we collected shows indications that the actor’s automation operation is behind a VPN. They repeated the same operations across multiple regions, generating a total of more than 400 API calls and taking only seven minutes, according to CloudTrail logging. This indicates that the actor is successfully able to obscure their identity while launching automated attacks against AWS account environments.

### [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)Launch Instances and Configurations

Part of the automation, once the AWS keys were found, included threat actors running instances across different regions. Figure 5 shows statistics about the instance types and their distribution across multiple regions.

The threat actors used large-format cloud virtual machines to perform their operations, specifically c5a.24xlarge AWS instances. It is common practice for cryptomining operations to use large-format cloud instances, as they will facilitate higher processing power, allowing cryptojackers to mine more cryptocurrency in a shorter period of time.

![Image 34: Image 5 is a table of instance type statistics and their distribution. The rows are requestParameters.instanceType, awsRegion and count. The regions include AP Northeast, EU Central, EU West, US East among others. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/10/word-image-130743-5-2.png)

Figure 5. Instantiated AWS EC2 instance types across regions.

To instantiate Amazon EC2 instances, the threat actor used the RunInstance API. This API has a parameter for accepting AWS Cloud-Init scripts. The Cloud-Init scripts are executed during the instance startup process. The threat actor used this mechanism to automate the EC2 instance configuration and perform the desired actions.

The user data is not logged in CloudTrail logs. To capture the data, we performed a forensic analysis of the EC2 volumes.

As shown in Figure 6, the mining automation operation displayed the user data automatically during the miner's configuration of the EC2 upon start-up.

![Image 35: Image 6 is a screenshot of many lines of code. It is the configurations script for the mining operation.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/10/word-image-130743-6-2.png)

Figure 6. Miner’s configuration script.

Figure 7 shows the payload was stored in Google Drive. Note that Google Drive URLs are anonymous by design. It is not possible to map this URL to a Google Cloud user account. The downloaded payload was stored encrypted and then decrypted upon download, as shown on line 6.

The payload was a known mining tool, and the hash can be correlated to previous research where we believe [the same actor used publicly exposed Docker services](https://intezer.com/blog/research/a-rare-look-inside-a-cryptojacking-campaign-and-its-profit/) to perform cryptojacking operations. We also identified reports of submissions to VirusTotal with the same hash and using the same naming convention for persistence (“appworker”), as shown in Figure 7.

![Image 36: Image 7 is a table of known crypto mining binaries that share the same meta-data. The columns are date, name, source, and country.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/10/word-image-130743-7-2.png)

Figure 7. Known cryptomining binaries sharing the same metadata.

The type of Amazon Machine Images (AMI) the threat actor used was also distinctive. The identified images were private and they were not listed in the AWS Marketplace. Figure 8 shows the following AMI instances’ IDs were used.

![Image 37: Image 8 is a table of the private AMI image IDs and their count. The table columns are requestParameters.instancesSet.items().imageid. and Count. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/10/word-image-130743-8-2.png)

Figure 8. Listing of the private AMI image IDs.

Some of those images are Ubuntu 18 versions. We believe that all of these indicators of compromise (IoCs) point to this being a long-running mining operation that dates back to at least 2020.

## [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)Mining Operation Tracking

As mentioned above, the EC2 instances received their mining configurations through the EC2 user data. The configuration contained the Monero wallet address each miner used to deliver its mined Monero.

Given the architecture of the operation, it is possible for us to speculate that the wallet address was used uniquely for AWS mining operations. If that is the case, every worker connected to the pool represents an individual Amazon EC2 instance.

The mining pool that the threat actor used for this operation was the SupportXMR mining pool. Mining pools are used in cryptomining operations as workspaces for multiple miners to work together to increase the chances of earning cryptocurrency rewards. When the rewards are granted, the proceeds are evenly distributed among the miners who contributed to the pool.

Given that the SupportXMR service only provides time-limited statistics, we monitored the wallet and pulled mining statistics for multiple weeks. Figure 9 shows the number of unique miners (likely representing resources stolen from targets of this campaign).

![Image 38: Image 9 is a column graph of the unique XMR miners starting August 30, 2023 and continuing to October 6, 2023. The blue trend line shows a slow rise across the three months. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/10/word-image-130743-9-2.png)

Figure 9. Statistics for the number of XMR miners.

In total, 474 unique miners appeared between Aug. 30, 2023, and Oct. 6, 2023. We can interpret this as 474 unique Amazon EC2 instances that were recorded performing mining operations during this time period. Because the actors mined Monero, a type of cryptocurrency that includes privacy controls, we cannot track the wallet to obtain exact figures of how much the threat actors gained.

Given that the actor was using a virtual private network (VPN) and Google Drive-exported documents to deliver payloads, it is difficult to perform geolocation analysis. We are continuing to monitor this mining campaign. This aligns with a trend that [Unit 42](https://unit42.paloaltonetworks.com/cloaked-ursa-online-storage-services-campaigns/) has observed of attackers using trusted business applications to evade detection.

## [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)The Research Architecture

To conduct our research, the Prisma Cloud Security Research team created a tool called HoneyCloud, a fully compromisable and reproducible cloud environment that provides researchers with the following capabilities:

*   Tracking malicious operations
*   Following cloud threat actor movements
*   Discovering new cloud attack paths
*   Building better cloud defense solutions.

We created a semi-random AWS infrastructure using IaC templates for [Terraform](https://www.terraform.io/), which is an IaC provisioning tool to manage and maintain cloud infrastructure. This tool allowed us to create and destroy the infrastructure using timed scheduling in combination with human analysis.

Researchers implemented a Terraform design as a direct result of our previous AWS account ID being added to the attacker’s blocklist. The design introduced certain amounts of randomness in the generated AWS accounts and its freshly created infrastructure aided us in avoiding the threat actors’ operations to match or identify previous IAM credential leaks.

We also designed the Terraform automation to use different types of IAM policies (i.e., more or less restrictive IAM permissions) according to the activity the threat actor was executing in the AWS account.

One of the largest obstacles we experienced during this investigation was how fast AWS reacted in applying the quarantine policy to prevent malicious operations. AWS applied the quarantine policy within two minutes of the AWS credentials being leaked on GitHub.

The AWS quarantine policy would have successfully prevented this attack. However, after analyzing the mining operation, we found additional mining instances that appear to be potential victims of this campaign –perhaps because the keys were exposed in a different way or on a different platform.

In the case of our research, we were forced to overwrite the quarantine policy to ensure we could track the threat actor’s operation. To perform this operation, we created a separate monitoring tool to restore the original overly-permissive AWS security policy we intended to be compromised.

## [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)Automated AWS Cloud Generation

Figure 10 shows the overall IaC architecture for exposing AWS IAM credentials and subsequently monitoring the actions taken against them.

![Image 39: Image 10 is a diagram of the cloning and monitoring of GitHub repos using AWS. Three GitHub icons in a green field, a randomly selected repro, are cloned with AWS keys. From there an arrow points to the three nested boxes that demonstrate the architecture: AWS cloud > Honey organization management AWS account containing the AWS Lambda, the Simple Storage Service standard and the containers. An arrow points from the containers to inside the Homey AWS account containing the IAM and designed policy, as well as three compute zones.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/10/word-image-130743-10-2.png)

Figure 10. Cloning and monitoring GitHub repositories using AWS.

The IaC template for the designed architecture was responsible for randomly selecting GitHub repositories, cloning and leaking the AWS IAM keys as past commits in random files. On the AWS side, new AWS accounts were dynamically created for each iteration of the IaC template execution, using the same AWS management organization and centralized CloudTrail log storage.

We also developed and deployed an additional lambda function in the AWS management account that functioned as a monitor to collect infrastructure changes and track IAM user policy changes.

One of the main objectives of the IaC template was to keep the AWS infrastructure components as random as possible to avoid being blocked by the threat actor. Another objective was to allow the infrastructure to be destroyed on a regular and precise basis to start new environments and variables quickly and systematically. In this way, the threat actor could only perceive the AWS IAM keys as part of an entirely new AWS environment and not a research environment.

## [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)Conclusion

We discovered a threat actor’s operation that scanned for exposed AWS IAM credentials within public GitHub repositories. We found that the threat actor can detect and launch a full-scale mining operation within five minutes from the time of an AWS IAM credential being exposed in a public GitHub repository.

The operation we found has been in action since at least 2020. Despite successful AWS quarantine policies, the campaign maintains continuous fluctuation in the number and frequency of compromised victim accounts. Several speculations as to why the campaign is still active include that this campaign is not solely focused on exposed GitHub credentials or Amazon EC2 instance targeting.

We developed a semi-automatic IaC Terraform architecture to track the operations of this threat actor group. This included the dynamic creation of AWS accounts designed to be compromised and destroyed.

Palo Alto Networks has shared these findings, including file samples and indicators of compromise, with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org/).

## [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)Recommendations

### [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)AWS Quarantine Policies

When we initially exposed AWS IAM credentials within our decoy GitHub repositories, AWS successfully quarantined the exposed IAM credential using the AWS policy AWSCompromisedKeyQuarantineV2. This policy [denies access](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCompromisedKeyQuarantineV2.html) to several AWS services, including the following:

*   EC2
*   S3
*   IAM
*   Lambda
*   Lightsail

This quarantining operation was initiated by AWS within minutes of the exposed IAM credential being committed to the GitHub repository. It is critical that this quarantine policy remains in place to ensure that potential attackers do not leverage sensitive cloud data, services and resources.

Organizations that do inadvertently expose AWS IAM credentials should immediately revoke any API connections made using this credential. The organization should also remove the AWS IAM credential from their GitHub repository and new AWS IAM credentials should be generated to fulfill the desired functionality. We highly recommended that organizations use short-lived credentials to perform any dynamic functionality within a production environment.

### [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)GitHub Enterprise Repository Clone Monitoring

For threat actors to detect and capture AWS IAM credentials within GitHub repositories, they first need to clone the targeted repository to view its contents. GitHub Enterprise accounts maintain the feature of [auditing clone events](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise) that occur on associated GitHub repositories.

Using this feature would allow a security team to monitor for potentially malicious operations targeted against their GitHub repositories. For Personal (or free) accounts, the ability to audit actions performed within the repository is limited and auditing clone events is not possible. You can [learn more about the various types of GitHub accounts and their capabilities](https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts).

GitHub Enterprise accounts are highly recommended for any organization publishing tools, applications or content, as they provide several auditing capabilities that can greatly assist in maintaining the security of your organization’s code repositories.

### [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)Prisma Cloud

The [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) CI/CD module can alert GitHub repository owners about potentially malicious events, such as the following:

*   Exposed IAM credentials
*   Cloned repository events
*   The presence of misconfigured or vulnerable code
*   Compromised workload runners

This will allow organizations to maintain visibility and security over their public code repositories.

[Prisma Cloud Code Security](https://www.paloaltonetworks.com/prisma/cloud/cloud-code-security)can also scan, detect and automatically mitigate vulnerabilities and misconfigurations, including the exposure of hard-coded credentials in developer IDEs, as pre-commit and pre-receive hooks in repositories, preventing credential exposure at the source.

[Prisma Cloud Anomaly Detection](https://docs.prismacloud.io/en/classic/cspm-admin-guide/prisma-cloud-policies/anomaly-policies) can detect anomalous compute provisioning activity through unusual entity behavior analytics ([UEBA](https://docs.prismacloud.io/en/classic/cspm-admin-guide/manage-prisma-cloud-administrators/define-prisma-cloud-enterprise-settings)), traffic from suspicious [crypto miner activity](https://docs.prismacloud.io/en/compute-edition/22-12/admin-guide/runtime-defense/incident-types/crypto-miners) and [cryptomining DNS](https://www.paloaltonetworks.co.uk/blog/prisma-cloud/dns-based-threat-detection/) request activity. Additionally, Prisma Cloud can trigger suspicious [Tor network traffic](https://www.paloaltonetworks.com/blog/prisma-cloud/threat-detection-using-tor-networks/), a tactic often employed by threat actors.

[Prisma Cloud CIEM](https://www.paloaltonetworks.com/prisma/cloud/cloud-infrastructure-entitlement-mgmt) can help mitigate risky and over-privileged access by providing:

*   Visibility, alerting, and automated remediation on risky permissions
*   Automatic findings of unused permissions with Least-privilege access remediations

Prisma Cloud Threat Detection capabilities can alert on various identity-related anomalous activities such as unusual usage of credentials from inside or outside of the cloud.

Prisma Cloud can also perform runtime operation monitoring and provide governance, risk and compliance (GRC) requirements for any component associated with their cloud environment.

### [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)Cortex XDR

[Cortex XDR for Cloud](https://www.paloaltonetworks.com/resources/techbriefs/cortex-xdr-for-cloud) provides SOC teams with a full incident story across the entire digital domain by integrating activity from cloud hosts, cloud traffic and audit logs together with endpoint and network data. Cortex leverages all this data to detect unusual cloud activity that correlates with known TTPs such as cloud computing credential theft, cryptojacking and data exfiltration.

## [](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)Indicators of Compromise

#### Encrypted Document:

*   Backup.tib

 SHA256: 87366652c83c366b70c4485e60594e7f40fd26bcc221a2db7a06debbebd25845

#### Miner Hash

*   Appworker

 SHA256: 240fe01d9fcce5aae311e906b8311a1975f8c1431b83618f3d11aeaff10aede3

#### Script Hashes

*   EC2 User Data

 SHA256: 2f0bd048bb1f4e83b3b214b24cc2b5f2fd04ae51a15aa3e301c8b9e5e187f2bb

#### Domains

*   XMR Pool Address: pool[.]supportxmr[.]com:443

#### Monero Wallet Address

*   82sdgJwuAMTF6w76Q7KrN4jJL72v23gvf9K2favHYHKxCNP4UabmBsJMwAVGWDLYagW5UmykC2D1zaMoQegZLy2bF9ynM1E

_Updated Oct. 30, 2023, at 12:20 p.m. PT to add additional Prisma Cloud protections._

_Updated Nov. 6, 2023, at 12:07 p.m. PT to add clarifying language to the executive summary._

Back to top

### Tags

*   [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
*   [Cryptojacking](https://unit42.paloaltonetworks.com/tag/cryptojacking/ "cryptojacking")
*   [Exposed credentials](https://unit42.paloaltonetworks.com/tag/exposed-credentials/ "exposed credentials")
*   [GitHub](https://unit42.paloaltonetworks.com/tag/github/ "GitHub")

[Threat Research Center](https://unit42.paloaltonetworks.com/ "Threat Research")[Next: When PAM Goes Rogue: Malware Uses Authentication Modules for Mischief](https://unit42.paloaltonetworks.com/linux-pam-apis/ "When PAM Goes Rogue: Malware Uses Authentication Modules for Mischief")

### Table of Contents

### Related Articles

*   [Cracks in the Bedrock: Agent God Mode](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/ "article - table of contents")
*   [Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/ "article - table of contents")
*   [Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/ "article - table of contents")

## Related Resources

![Image 40: Pictorial representation of 01flip ransomware written in Rust. Digital artwork of a pixelated U.S. dollar bill disintegrating into small blocks against a blue data matrix background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/12/05_Ransomware_Category_1920x900-786x368.jpg)

[![Image 41: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)December 10, 2025[#### 01flip: Multi-Platform Ransomware Written in Rust](https://unit42.paloaltonetworks.com/new-ransomware-01flip-written-in-rust/)
*   [Bitcoin](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")
*   [CL-CRI-103](https://unit42.paloaltonetworks.com/tag/cl-cri-103/ "CL-CRI-103")
*   [Cryptocurrency](https://unit42.paloaltonetworks.com/tag/cryptocurrency/ "Cryptocurrency")

[Read now ![Image 42: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/new-ransomware-01flip-written-in-rust/ "01flip: Multi-Platform Ransomware Written in Rust")

![Image 43: Pictorial representation of malicious LLMs. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/AdobeStock_1270203474-786x440.jpeg)

[![Image 44: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)November 25, 2025[#### The Dual-Use Dilemma of AI: Malicious LLMs](https://unit42.paloaltonetworks.com/dilemma-of-ai-malicious-llms/)
*   [Credential Harvesting](https://unit42.paloaltonetworks.com/tag/credential-harvesting/ "Credential Harvesting")
*   [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")
*   [LLM](https://unit42.paloaltonetworks.com/tag/llm/ "LLM")

[Read now ![Image 45: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/dilemma-of-ai-malicious-llms/ "The Dual-Use Dilemma of AI: Malicious LLMs")

![Image 46: Pictorial representation of Gh0st RAT malware. A woman analyzes code on a computer screen in an office setting, with another individual working in the background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/04_Security-Technology_Category_1505x922-718x440.jpg)

[![Image 47: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)November 14, 2025[#### Digital Doppelgangers: Anatomy of Evolving Impersonation Campaigns Distributing Gh0st RAT](https://unit42.paloaltonetworks.com/impersonation-campaigns-deliver-gh0st-rat/)
*   [DLL Sideloading](https://unit42.paloaltonetworks.com/tag/dll-sideloading/ "DLL Sideloading")
*   [Gh0st Rat](https://unit42.paloaltonetworks.com/tag/gh0st-rat/ "Gh0st Rat")
*   [PDNS](https://unit42.paloaltonetworks.com/tag/pdns/ "PDNS")

[Read now ![Image 48: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/impersonation-campaigns-deliver-gh0st-rat/ "Digital Doppelgangers: Anatomy of Evolving Impersonation Campaigns Distributing Gh0st RAT")

![Image 49: Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 50: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)March 23, 2026[#### Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication/)
*   [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
*   [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
*   [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")

[Read now ![Image 51: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Image 52: Pictorial representation of the APT Boggy Serpens. An illustrated blue snake is highlighted by a red circle against a night sky. The constellation serpens.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/Boggy-Serpens.png)

[![Image 53: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)March 16, 2026[#### Boggy Serpens Threat Assessment](https://unit42.paloaltonetworks.com/boggy-serpens-threat-assessment/)
*   [Advanced Persistent Threat](https://unit42.paloaltonetworks.com/tag/advanced-persistent-threat/ "Advanced Persistent Threat")
*   [Boggy Serpens](https://unit42.paloaltonetworks.com/tag/boggy-serpens/ "Boggy Serpens")
*   [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")

[Read now ![Image 54: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/boggy-serpens-threat-assessment/ "Boggy Serpens Threat Assessment")

![Image 55: Pictorial representation of Muddled Libra, aka Scattered Spider. A vibrant illustration of the Libra zodiac sign, featuring a stylized balance scale overlaid with a prominent Libra symbol. The background is a starry night sky with shades of purple and blue, suggesting a cosmic theme.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/03-1-Muddle-Libra-1920x900-1-786x368.png)

[![Image 56: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/threat-actor-groups.svg)Threat Actor Groups](https://unit42.paloaltonetworks.com/category/threat-actor-groups/)February 10, 2026[#### A Peek Into Muddled Libra’s Operational Playbook](https://unit42.paloaltonetworks.com/muddled-libra-ops-playbook/)
*   [Muddled Libra](https://unit42.paloaltonetworks.com/tag/muddled-libra/ "Muddled Libra")
*   [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")
*   [Scattered Spider](https://unit42.paloaltonetworks.com/tag/scattered-spider/ "Scattered Spider")

[Read now ![Image 57: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/muddled-libra-ops-playbook/ "A Peek Into Muddled Libra’s Operational Playbook")

![Image 58: Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 59: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)February 6, 2026[#### Novel Technique to Detect Cloud Threat Actor Operations](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)
*   [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
*   [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
*   [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")

[Read now ![Image 60: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Image 61: Pictorial representation of a group of individuals discussing an idea with a whiteboard.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/02_Listicle_Overview_1920x900-786x368.jpg)

[![Image 62: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/)February 3, 2026[#### Why Smart People Fall For Phishing Attacks](https://unit42.paloaltonetworks.com/psychology-of-phishing/)
*   [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
*   [Phishing](https://unit42.paloaltonetworks.com/tag/phishing/ "phishing")

[Read now ![Image 63: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/psychology-of-phishing/ "Why Smart People Fall For Phishing Attacks")

![Image 64: Pictorial representation of threat groups from Russia. The silhouette of a bear and the Ursa constellation inside an orange abstract planet. Abstract, stylized cosmic setting with vibrant blue and purple shapes, representing space and distant planetary bodies.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/Ursa-Russia-B-1920x900-1-786x368.png)

[![Image 65: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/)January 29, 2026[#### Understanding the Russian Cyberthreat to the 2026 Winter Olympics](https://unit42.paloaltonetworks.com/russian-cyberthreat-2026-winter-olympics/)
*   [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
*   [IoT](https://unit42.paloaltonetworks.com/tag/iot/ "IoT")
*   [Russia](https://unit42.paloaltonetworks.com/tag/russia/ "Russia")

[Read now ![Image 66: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/russian-cyberthreat-2026-winter-olympics/ "Understanding the Russian Cyberthreat to the 2026 Winter Olympics")

![Image 67: Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![Image 68: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 20, 2026[#### DNS OverDoS: Are Private Endpoints Too Private?](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)
*   [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
*   [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")

[Read now ![Image 69: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Image 70: Pictorial representation of 01flip ransomware written in Rust. Digital artwork of a pixelated U.S. dollar bill disintegrating into small blocks against a blue data matrix background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/12/05_Ransomware_Category_1920x900-786x368.jpg)

[![Image 71: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)December 10, 2025[#### 01flip: Multi-Platform Ransomware Written in Rust](https://unit42.paloaltonetworks.com/new-ransomware-01flip-written-in-rust/)
*   [Bitcoin](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")
*   [CL-CRI-103](https://unit42.paloaltonetworks.com/tag/cl-cri-103/ "CL-CRI-103")
*   [Cryptocurrency](https://unit42.paloaltonetworks.com/tag/cryptocurrency/ "Cryptocurrency")

[Read now ![Image 72: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/new-ransomware-01flip-written-in-rust/ "01flip: Multi-Platform Ransomware Written in Rust")

![Image 73: Pictorial representation of malicious LLMs. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/AdobeStock_1270203474-786x440.jpeg)

[![Image 74: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)November 25, 2025[#### The Dual-Use Dilemma of AI: Malicious LLMs](https://unit42.paloaltonetworks.com/dilemma-of-ai-malicious-llms/)
*   [Credential Harvesting](https://unit42.paloaltonetworks.com/tag/credential-harvesting/ "Credential Harvesting")
*   [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")
*   [LLM](https://unit42.paloaltonetworks.com/tag/llm/ "LLM")

[Read now ![Image 75: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/dilemma-of-ai-malicious-llms/ "The Dual-Use Dilemma of AI: Malicious LLMs")

![Image 76: Pictorial representation of Gh0st RAT malware. A woman analyzes code on a computer screen in an office setting, with another individual working in the background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/04_Security-Technology_Category_1505x922-718x440.jpg)

[![Image 77: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)November 14, 2025[#### Digital Doppelgangers: Anatomy of Evolving Impersonation Campaigns Distributing Gh0st RAT](https://unit42.paloaltonetworks.com/impersonation-campaigns-deliver-gh0st-rat/)
*   [DLL Sideloading](https://unit42.paloaltonetworks.com/tag/dll-sideloading/ "DLL Sideloading")
*   [Gh0st Rat](https://unit42.paloaltonetworks.com/tag/gh0st-rat/ "Gh0st Rat")
*   [PDNS](https://unit42.paloaltonetworks.com/tag/pdns/ "PDNS")

[Read now ![Image 78: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/impersonation-campaigns-deliver-gh0st-rat/ "Digital Doppelgangers: Anatomy of Evolving Impersonation Campaigns Distributing Gh0st RAT")

![Image 79: Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 80: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)March 23, 2026[#### Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication/)
*   [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
*   [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
*   [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")

[Read now ![Image 81: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Image 82: Pictorial representation of the APT Boggy Serpens. An illustrated blue snake is highlighted by a red circle against a night sky. The constellation serpens.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/Boggy-Serpens.png)

[![Image 83: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)March 16, 2026[#### Boggy Serpens Threat Assessment](https://unit42.paloaltonetworks.com/boggy-serpens-threat-assessment/)
*   [Advanced Persistent Threat](https://unit42.paloaltonetworks.com/tag/advanced-persistent-threat/ "Advanced Persistent Threat")
*   [Boggy Serpens](https://unit42.paloaltonetworks.com/tag/boggy-serpens/ "Boggy Serpens")
*   [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")

[Read now ![Image 84: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/boggy-serpens-threat-assessment/ "Boggy Serpens Threat Assessment")

![Image 85: Pictorial representation of Muddled Libra, aka Scattered Spider. A vibrant illustration of the Libra zodiac sign, featuring a stylized balance scale overlaid with a prominent Libra symbol. The background is a starry night sky with shades of purple and blue, suggesting a cosmic theme.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/03-1-Muddle-Libra-1920x900-1-786x368.png)

[![Image 86: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/threat-actor-groups.svg)Threat Actor Groups](https://unit42.paloaltonetworks.com/category/threat-actor-groups/)February 10, 2026[#### A Peek Into Muddled Libra’s Operational Playbook](https://unit42.paloaltonetworks.com/muddled-libra-ops-playbook/)
*   [Muddled Libra](https://unit42.paloaltonetworks.com/tag/muddled-libra/ "Muddled Libra")
*   [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")
*   [Scattered Spider](https://unit42.paloaltonetworks.com/tag/scattered-spider/ "Scattered Spider")

[Read now ![Image 87: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/muddled-libra-ops-playbook/ "A Peek Into Muddled Libra’s Operational Playbook")

![Image 88: Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![Image 89: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)February 6, 2026[#### Novel Technique to Detect Cloud Threat Actor Operations](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)
*   [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
*   [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
*   [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")

[Read now ![Image 90: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Image 91: Pictorial representation of a group of individuals discussing an idea with a whiteboard.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/02_Listicle_Overview_1920x900-786x368.jpg)

[![Image 92: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/)February 3, 2026[#### Why Smart People Fall For Phishing Attacks](https://unit42.paloaltonetworks.com/psychology-of-phishing/)
*   [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
*   [Phishing](https://unit42.paloaltonetworks.com/tag/phishing/ "phishing")

[Read now ![Image 93: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/psychology-of-phishing/ "Why Smart People Fall For Phishing Attacks")

![Image 94: Pictorial representation of threat groups from Russia. The silhouette of a bear and the Ursa constellation inside an orange abstract planet. Abstract, stylized cosmic setting with vibrant blue and purple shapes, representing space and distant planetary bodies.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/Ursa-Russia-B-1920x900-1-786x368.png)

[![Image 95: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/)January 29, 2026[#### Understanding the Russian Cyberthreat to the 2026 Winter Olympics](https://unit42.paloaltonetworks.com/russian-cyberthreat-2026-winter-olympics/)
*   [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
*   [IoT](https://unit42.paloaltonetworks.com/tag/iot/ "IoT")
*   [Russia](https://unit42.paloaltonetworks.com/tag/russia/ "Russia")

[Read now ![Image 96: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/russian-cyberthreat-2026-winter-olympics/ "Understanding the Russian Cyberthreat to the 2026 Winter Olympics")

![Image 97: Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![Image 98: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)January 20, 2026[#### DNS OverDoS: Are Private Endpoints Too Private?](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)
*   [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
*   [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")

[Read now ![Image 99: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Image 100: Pictorial representation of 01flip ransomware written in Rust. Digital artwork of a pixelated U.S. dollar bill disintegrating into small blocks against a blue data matrix background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/12/05_Ransomware_Category_1920x900-786x368.jpg)

[![Image 101: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)December 10, 2025[#### 01flip: Multi-Platform Ransomware Written in Rust](https://unit42.paloaltonetworks.com/new-ransomware-01flip-written-in-rust/)
*   [Bitcoin](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")
*   [CL-CRI-103](https://unit42.paloaltonetworks.com/tag/cl-cri-103/ "CL-CRI-103")
*   [Cryptocurrency](https://unit42.paloaltonetworks.com/tag/cryptocurrency/ "Cryptocurrency")

[Read now ![Image 102: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/new-ransomware-01flip-written-in-rust/ "01flip: Multi-Platform Ransomware Written in Rust")

![Image 103: Pictorial representation of malicious LLMs. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/AdobeStock_1270203474-786x440.jpeg)

[![Image 104: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)November 25, 2025[#### The Dual-Use Dilemma of AI: Malicious LLMs](https://unit42.paloaltonetworks.com/dilemma-of-ai-malicious-llms/)
*   [Credential Harvesting](https://unit42.paloaltonetworks.com/tag/credential-harvesting/ "Credential Harvesting")
*   [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")
*   [LLM](https://unit42.paloaltonetworks.com/tag/llm/ "LLM")

[Read now ![Image 105: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/dilemma-of-ai-malicious-llms/ "The Dual-Use Dilemma of AI: Malicious LLMs")

![Image 106: Pictorial representation of Gh0st RAT malware. A woman analyzes code on a computer screen in an office setting, with another individual working in the background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/04_Security-Technology_Category_1505x922-718x440.jpg)

[![Image 107: category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)November 14, 2025[#### Digital Doppelgangers: Anatomy of Evolving Impersonation Campaigns Distributing Gh0st RAT](https://unit42.paloaltonetworks.com/impersonation-campaigns-deliver-gh0st-rat/)
*   [DLL Sideloading](https://unit42.paloaltonetworks.com/tag/dll-sideloading/ "DLL Sideloading")
*   [Gh0st Rat](https://unit42.paloaltonetworks.com/tag/gh0st-rat/ "Gh0st Rat")
*   [PDNS](https://unit42.paloaltonetworks.com/tag/pdns/ "PDNS")

[Read now ![Image 108: Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/impersonation-campaigns-deliver-gh0st-rat/ "Digital Doppelgangers: Anatomy of Evolving Impersonation Campaigns Distributing Gh0st RAT")

*   ![Image 109: Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
*   ![Image 110: Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Image 111: Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)![Image 112: Enlarged Image](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)

![Image 113: Newsletter](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/unit42-footer-subscribe-desktop.png)

![Image 114: UNIT 42 Small Logo](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/palo-alto-logo-small.svg) Get updates from Unit 42 
## Peace of mind comes from staying ahead of threats. Subscribe today.

Your Email 
Subscribe for email updates to all Unit 42 threat research.

 By submitting this form, you agree to our [Terms of Use](https://www.paloaltonetworks.com/legal-notices/terms-of-use "Terms of Use") and acknowledge our [Privacy Statement.](https://www.paloaltonetworks.com/legal-notices/privacy "Privacy Statement")

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

Invalid captcha!

 Subscribe ![Image 115: Right Arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/right-arrow.svg)![Image 116: loader](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-loader.svg)

[](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/)

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

![Image 117: PAN logo](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/pan-logo-dark.svg)

*   [Privacy](https://www.paloaltonetworks.com/legal-notices/privacy)
*   [Trust Center](https://www.paloaltonetworks.com/legal-notices/trust-center)
*   [Terms of Use](https://www.paloaltonetworks.com/legal-notices/terms-of-use)
*   [Documents](https://www.paloaltonetworks.com/legal)

Copyright © 2026 Palo Alto Networks. All Rights Reserved

*   [![Image 118: Youtube](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/youtube-black.svg)](https://www.youtube.com/user/paloaltonetworks)
*   [![Image 119: Podcast](https://www.paloaltonetworks.com/content/dam/pan/en_US/images/icons/podcast.svg)](https://www.paloaltonetworks.com/podcasts/threat-vector)
*   [![Image 120: Facebook](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/facebook-black.svg)](https://www.facebook.com/PaloAltoNetworks/)
*   [![Image 121: LinkedIn](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/linkedin-black.svg)](https://www.linkedin.com/company/palo-alto-networks)
*   [![Image 122: Twitter](https://www.paloaltonetworks.com/etc/clientlibs/clean/imgs/social/twitter-x-black.svg)](https://twitter.com/PaloAltoNtwks)
*   EN Select your language  

![Image 123: Play](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-play-icon.svg)![Image 124: Pause](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-pause-icon1.svg)![Image 125: Minimize](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-minimize.svg)![Image 126: Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)Your browser does not support the video tag. 

### Default Heading

[Read the article ![Image 127: Right Arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/right-arrow.svg)](https://unit42.paloaltonetworks.com/malicious-operations-of-exposed-iam-keys-cryptojacking/# "Right Arrow Icon")

Seekbar 

![Image 128: Play](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-play-icon.svg)![Image 129: Pause](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/player-pause-icon1.svg)

![Image 130: Volume](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-volume.svg)

Volume 

![Image 131: Minimize](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-minimize.svg)