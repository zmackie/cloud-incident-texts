Title: Effective AWS Incident Response: Examples and Recommendations

URL Source: https://www.kroll.com/en/insights/publications/cyber/effective-aws-incident-response

Published Time: 2023-04-14

Markdown Content:
# Effective AWS Incident Response | Kroll

[![Image 1: Kroll Logo](https://edge.sitecorecloud.io/krollllc17bf0-kroll6fee-proda464-0e9b/media/Logos/KROLL_SVG_RGB.svg?h=27&iar=0&w=132)](https://www.kroll.com/en)

[Contact us](https://www.kroll.com/en/contactus)[Hotlines](https://www.kroll.com/en/hotlines)

1.   [Home](https://www.kroll.com/en)
2.   /
3.   [Publications](https://www.kroll.com/en/publications)
4.   Effective AWS Incident Response: Examples and Recommendations

# Effective AWS Incident Response: Examples and Recommendations

![Image 2: profile](https://www.kroll.com/_next/image?url=https%3A%2F%2Fwww.kroll.com%2Fplaceholder.png&w=256&q=75)

Ivan Iverson

[![Image 3: alex-cowperthwaite](https://edge.sitecorecloud.io/krollllc17bf0-kroll6fee-proda464-0e9b/media/Kroll-Images/Expert-Headshot/Kroll-Expert/alex-cowperthwaite.jpg?h=585&iar=0&w=468) Alex Cowperthwaite Technical Director of Research and Development Cyber and Data Resilience](https://www.kroll.com/en/our-experts/alex-cowperthwaite)

![Image 4: profile](https://www.kroll.com/_next/image?url=https%3A%2F%2Fwww.kroll.com%2Fplaceholder.png&w=256&q=75)

Lucas Donato

![Image 5: profile](https://www.kroll.com/_next/image?url=https%3A%2F%2Fwww.kroll.com%2Fplaceholder.png&w=256&q=75)

Ivan Iverson

[![Image 6: alex-cowperthwaite](https://edge.sitecorecloud.io/krollllc17bf0-kroll6fee-proda464-0e9b/media/Kroll-Images/Expert-Headshot/Kroll-Expert/alex-cowperthwaite.jpg?h=585&iar=0&w=468) Alex Cowperthwaite Technical Director of Research and Development Cyber and Data Resilience](https://www.kroll.com/en/our-experts/alex-cowperthwaite)

![Image 7: profile](https://www.kroll.com/_next/image?url=https%3A%2F%2Fwww.kroll.com%2Fplaceholder.png&w=256&q=75)

Lucas Donato

![Image 8: profile](https://www.kroll.com/_next/image?url=https%3A%2F%2Fwww.kroll.com%2Fplaceholder.png&w=256&q=75)

Ivan Iverson

*   1
*   2
*   3

April 14, 2023

Share

[https://www.linkedin.com/sharing/share-offsite/url=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Feffective-aws-incident-response](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Feffective-aws-incident-response "Linkedin")[mailto:?subject=Effective%20AWS%20Incident%20Response%3A%20Examples%20and%20Recommendations&body=https%3A%2F%2Fwww.kroll.com%2Fen%2Fpublications%2Fcyber%2Feffective-aws-incident-response](mailto:?subject=effective%20aws%20incident%20response%3a%20examples%20and%20recommendations&body=https%3a%2f%2fwww.kroll.com%2fen%2fpublications%2fcyber%2feffective-aws-incident-response "Email")

The use of Amazon Web Services (AWS) in organizations around the world is prolific. The platform accounted for 31% of total cloud infrastructure services spend in Q2 2022, growing by [33%](https://www.computerweekly.com/news/252523412/Global-cloud-infrastructure-spend-hits-623bn-during-Q2-2022) annually.

Despite its widespread use, many organizations still fail to consider the nuances of incident response in AWS. The volume and nature of incidents Kroll has identified occurring in this environment highlight a significant lack of industry understanding about how AWS works from a security and investigative perspective and an enduring misconception that AWS itself will protect the client “out of the box.”

In this article, we outline the main areas of compromise in AWS, tools and techniques to use when [investigating incidents](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html) and the steps organizations can take to manage and mitigate them.

## Key Areas of Compromise in AWS

Broadly, the two main areas of compromise in AWS are:

*   The AWS account
*   The AWS environment

These should be considered separately because, while an adversary may have compromised an organization’s AWS account, they don’t necessarily have the power to affect its AWS environment. This means that although the adversary may not be able to undertake actions such as spinning up EC2 instances or taking keys, they can complete others, such as Bitcoin mining—a common issue in AWS.

Typically, adversaries in an AWS account are easier to identify and mitigate against through tools such as CloudTrail. Conversely, if an AWS environment is compromised, it typically presents a bigger challenge.

## The Domain of the Incident Will Dictate Tools and Techniques

Security incidents in AWS can occur in three domains for which organizations are responsible: service, infrastructure and application. The choice of resources to use when investigating an incident in AWS will be defined by the domain they occur in:

*   **Service**

 Incidents in the service domain have the potential to impact an organization’s AWS account, Identity and Access Management (IAM) permissions, billing and other aspects. Organizations may need to respond to an event using AWS API mechanisms. If there are root causes associated with configuration or resource permissions, they may need to use related service-oriented logging. Because there is less control in this domain than in the others, there are fewer options to manage it with cloud tools. However, there are some options with some of the popular services such as S3.
*   **Infrastructure**

 Incident response in the infrastructure domain can include network- or data-related activity, such as the traffic to Amazon EC2 instances within the Virtual Private Cloud (VPC). Incident response in this context can involve retrieving and restoring incident-related data and interacting with the operating system of an instance. Many tools can be used in the process, including AWS API mechanisms for a snapshot of the file system and others which allow direct interaction with the file or operating system.
*   **Application**

 Security incidents in the application domain can occur in the application code and in software deployed to the services or infrastructure. Organizations should include the application domain in their cloud threat detection and response runbooks.

## Identifying AWS Security Incidents

A number of resources and approaches support the detection of security-related events in the AWS cloud environment:

**Logs and Monitors:**Utilize AWS logs through Amazon CloudTrail, Amazon S3 access logs and VPC Flow Logs, as well as security monitoring services such as Amazon GuardDuty, Amazon Detective and AWS Security Hub. You can also use monitors such as Amazon Route 53 health checks and Amazon CloudWatch alarms. Another approach is to use Windows Events, Linux syslog logs and other application-specific logs, and log to Amazon CloudWatch using CloudWatch agents.

**Changes in Billing Activity:**Be vigilant about any unexpected changes in billing activity as they can indicate a change within the operating environment indicative of a security event. Billing reports can be a useful source of timeline and causality evidence when trying to identify data exfiltration events. How or Why? Because moving data out of AWS has a direct impact on data volume and virtualization cycles which affect costs incurred. Most environments have a fairly level cost pattern based on averaged data volume in- and out-flows, in addition to averaged system demands for resources and processing. When irregularities occur, such as data exfiltration or data copying at scale, this can cause identifiable spikes in costs.

**Threat Intelligence:**Third-party threat intelligence, such as that provided by Kroll through our Global Threat Intelligence team, can provide valuable insight when correlated with data gained through other logging and monitoring tool sources. Often with Digital Forensics and Incident Response, the value of findings is not in the specific logs or artifacts by themselves, but in the combination—the telling of the story with context and supporting facts.

**AWS Security Hub and AWS Systems Manager Agent (SSM):**AWS Security Hub gives organizations a comprehensive view of high-priority security alerts and compliance status across AWS accounts in one place, aggregating, organizing and prioritizing security alerts from different AWS services. AWS Security Hub also enables organizations to create custom insights from multiple sources, as well as continuously monitoring an environment using automated compliance checks based on the AWS best practices and industry standards followed by individual organizations.

AWS Systems Manager Agent (SSM) is a further tool that enables the remote administration of EC2s. It gives administrators a range of available actions, such as extraction and preservation of logging for analysis.

## AWS Incident Response Case Studies

The main type of security incident that takes place in AWS is the compromise of credentials or taking keys. Other common types of incidents include areas exposed to the internet that have not been patched and public buckets and S3 buckets causing data leakage. Below, we outline two incident response cases our experts have worked on.

### Over-Permissioned Access Leading to Website Redirection

In one AWS incident worked on by Kroll, a company working with our client organization was compromised. This third party had over-permissioned access which meant that misuse of the account allowed for broader access than intended or needed. As a result, the federated user account was leveraged by the threat actor in order to move to the other environment and start leveraging access. They affected changing the domain name system to redirect the client organization’s website and email. This incident was resolved by changing passwords, blocking IPs, reviewing logs and returning local admins to their original configuration.

### Compromise of an Internal Network

In another investigation Kroll was retained on, a sophisticated [intrusion lifecycle](https://www.kroll.com/en/insights/publications/cyber/kroll-intrusion-lifecycle)was identified and examined, in which the threat actors compromised the client’s own internal network, laterally moving into the cloud and recovering the keys from both ends of the encryption. They persisted in the environment for a number of years, observing, gathering and exfiltrating over time.

Kroll addressed the persistence mechanisms and compromise through deployment of its Responder Managed Detection and Response (MDR) service, leveraging endpoint agents on-premises and in the cloud via an endpoint detection response (EDR) solution. Our team gained enterprise-wide visibility and identified footholds, compromised accounts and back doors, allowing for a coordinated, joint Kroll and client global threat actor ejection during what Kroll surmised was the threat actor’s real-life sleep cycle. The result was a completely successful kick-out. The ongoing Kroll investigation later revealed and determined how the adversaries had entered the environment originally, as well as how they had been quietly entering, traversing and exfiltrating information from the global enterprise. Kroll’s findings also identified how frequently and the different types of mechanisms they were using. The investigative lifecycle process took about a month and involved a broad-ranging and cooperative approach. Kroll’s client was then able to set up a replicated environment and complete a cutover to plan and run their migration, one of the advantages of the cloud.

## Key Recommendations for Minimizing Attacks in AWS

While traditional incident response approaches can provide a helpful starting point, our experts share some considerations for responding to attacks specifically in AWS.

 Prioritize containment: When addressing incidents in AWS, many organizations tend to focus on recovery because of the pressure to restore business continuity. While this is understandable, it means the preservation of logs either does not happen or is put at risk. We recommend that organizations focus their first stage of response on their initial triage, including containment, and then scale.

**Use IAM Effectively:** IAM plays a vital role in reducing attacks in the AWS environment. However, organizations need to be aware it presents a level of complexity due to the range of services it should cover and the many types of permissions involved.

**Be Vigilant About Logs:** We recommend that organizations retain their logs for at least as long as is required by law or regulatory frameworks. Make sure you have appropriate CloudTrail set up in advance and that logs are exported to the relevant tool.

**Use Frameworks to Manage Logs:** As managing data logs is a critical aspect of AWS incident response, organizations should choose a framework focused on log types and set out how long to keep them. These include:

*   **The Well-Architected Framework**

 The AWS Well-Architected Framework outlines concepts, design principles and architectural best practices for designing and running workloads in the cloud.
*   **The CIS Benchmark**

 Developed by cybersecurity professionals, CIS Benchmarks are a collection of best practices for securely configuring IT systems, software, networks and cloud infrastructure. The cloud provider benchmarks address security configurations for AWS and other public clouds, covering guidelines for configuring IAM, system logging protocols, regulatory compliance safeguards and other areas.
*   **NIST Cybersecurity Framework**

 The NIST Framework integrates industry standards and best practices to help organizations manage their cybersecurity risks. It provides a common language to enable employees and others to develop a shared understanding of their cybersecurity risks. While not cloud-specific, the framework is applicable to AWS.

Choice of framework should be defined by organizational needs, such as the type of data you’re protecting, how long you want to keep it for and the associated costs. It is also important to take into account the laws and regulations your organization is required to meet.

As well as the frameworks outlined above, the [MITRE ATT&CK framework](https://attack.mitre.org/matrices/enterprise/cloud/) relates to security incidents in AWS to help organizations understand and prepare for attacks. While it isn’t a checklist, it provides a useful taxonomy of how an attacker might operate.

## Maximizing Incident Response in AWS

AWS offers significant business advantages for organizations but, due to the potential risks, the appropriate level of attention must be paid to security and [incident response planning](https://www.kroll.com/en/services/cyber/incident-response-recovery/incident-response-plan-development). This isn’t always easy to achieve in-house. To reduce accidental data exposures and prevent unauthorized access to your cloud environment, organizations need the right telemetry, skills and bandwidth to properly [monitor and hunt for threats](https://www.kroll.com/en/insights/publications/cyber/defending-against-cloud-security-threats).

With frontline insights gained through handling thousands of cyber incidents, many of which require cloud incident response expertise, and through extensive cloud security assessments as part of migrations, optimizations and transformation projects, Kroll is uniquely positioned to assist.

Connect with our team via our [24x7 security hotlines](https://www.kroll.com/en/hotlines)or [contact page](https://www.kroll.com/en/contactus).

[Stay Ahead with Kroll](https://www.kroll.com/en/services)

[Cyber and Data Resilience](https://www.kroll.com/en/services/cyber)
Kroll merges elite security and data risk expertise with frontline intelligence from thousands of incident responses and regulatory compliance, financial crime and due diligence engagements to make our clients more cyber- resilient.

[Learn more](https://www.kroll.com/en/services/cyber)

[24x7 Incident Response](https://www.kroll.com/en/services/cyber/incident-response-recovery/incident-response)
Kroll is the largest global IR provider with experienced responders who can handle the entire security incident lifecycle.

[Learn more](https://www.kroll.com/en/services/cyber/incident-response-recovery/incident-response)

[Incident Response & Recovery](https://www.kroll.com/en/services/cyber/incident-response-recovery)
Kroll’s elite security leaders deliver rapid responses for over 3,000 incidents per year and have the resources and expertise to support the entire incident lifecycle, including litigation demands. Gain peace of mind in a crisis.

[Learn more](https://www.kroll.com/en/services/cyber/incident-response-recovery)

[Computer Forensics](https://www.kroll.com/en/services/cyber/incident-response-recovery/computer-forensics)
Kroll's computer forensics experts ensure that no digital evidence is overlooked and assist at any stage of an investigation or litigation, regardless of the number or location of data sources.

[Learn more](https://www.kroll.com/en/services/cyber/incident-response-recovery/computer-forensics)

[Cyber Risk Retainer](https://www.kroll.com/en/services/cyber/enterprise-risk-retainer/cyber-incident-response-retainer)
Kroll delivers more than a typical incident response retainer—secure a true cyber risk retainer with elite digital forensics and incident response capabilities and maximum flexibility for proactive and notification services.

[Learn more](https://www.kroll.com/en/services/cyber/enterprise-risk-retainer/cyber-incident-response-retainer)

![Image 9](https://www.kroll.com/_next/image?url=https%3A%2F%2Fedge.sitecorecloud.io%2Fkrollllc17bf0-kroll6fee-proda464-0e9b%2Fmedia%2FProject%2FKroll%2FKroll%2FKroll_New_Footer_Full_Image.jpg%3Fh%3D1000%26iar%3D0%26w%3D2000&w=3840&q=100)

Kroll is headquartered in New York with offices around the world.

Get to know us

[About Us](https://www.kroll.com/en/about-us)[Services](https://www.kroll.com/en/services)[Insights](https://www.kroll.com/en/insights)[Our Values](https://www.kroll.com/en/about-us#values)[Client Stories](https://www.kroll.com/en/client-stories)[Careers](https://careers.kroll.com/en)[Find an Expert](https://www.kroll.com/en/our-experts)[Locations](https://www.kroll.com/en/global-locations)[Media Inquiry](mailto:mediarelations@kroll.com?subject=media-inquiry)

Helpful Links

[Accessibility](https://www.kroll.com/en/accessibility)[Code of Conduct](https://www.kroll.com/en/code-of-conduct)[Cookies Policy](https://www.kroll.com/en/cookies-policy)[Cookies Preference Center](https://www.kroll.com/en/insights/publications/cyber/effective-aws-incident-response#cookies-preference-center)[Data Privacy Framework](https://www.kroll.com/en/data-privacy-framework-policy)[Disclosure](https://www.kroll.com/en/disclosure)[Kroll Ethics Hotline](https://www.integritycounts.ca/)[Licensing](https://www.kroll.com/en/licensing)[Modern Slavery Statement](https://edge.sitecorecloud.io/krollllc17bf0-kroll6fee-proda464-0e9b/media/Assets/PDFs/kroll-slavery-and-human-trafficking-statement-2024.pdf)[Privacy Policy](https://www.kroll.com/en/privacy-policy)

One World Trade Center 285 Fulton Street, 31st Floor

New York, NY 10007

[+1 212 593 1000](tel:+1 212 593 1000)

[https://www.facebook.com/wearekroll](https://www.facebook.com/wearekroll "Facebook")[https://www.instagram.com/wearekroll/#](https://www.instagram.com/wearekroll/# "Instagram")[https://www.linkedin.com/company/kroll/](https://www.linkedin.com/company/kroll/ "LinkedIn")[https://x.com/KrollWire](https://x.com/KrollWire "Twitter")[https://www.youtube.com/c/kroll](https://www.youtube.com/c/kroll "Youtube")

Choose your region:Global

Get Your Weekly Heads-Up

Join our newsletter for the latest risk and financial trend analysis in your industry.

[SIGN UP](javascript:;)

© 2026 Kroll, LLC. All rights reserved. Kroll is not affiliated with Kroll Bond Rating Agency, Kroll OnTrack Inc. or their affiliated businesses. [Read more](https://www.kroll.com/en/terms-of-use). 

Return To Top