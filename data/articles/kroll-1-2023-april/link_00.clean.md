---
title: "Effective AWS Incident Response: Examples and Recommendations"
url: "https://www.kroll.com/en/insights/publications/cyber/effective-aws-incident-response"
author: Ivan Iverson, Alex Cowperthwaite, Lucas Donato
published: 2023-04-14
source_type: article
source_domain: www.kroll.com
cleanup_method: llm
---

# Effective AWS Incident Response: Examples and Recommendations

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
