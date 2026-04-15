---
title: Security Incident Update
url: "https://web.archive.org/web/20210620143023/https://www.imperva.com/blog/ceoblog/"
author: Kunal Anand, Chris Hylen
published: 2019-08-27
source_type: archive
source_domain: web.archive.org
cleanup_method: llm
---

Hi everyone,
Please find below a detailed update on the security incident from Kunal Anand, our Chief Technology Officer. From the moment we discovered this incident, we established and have held ourselves to the following key principles:
- To do the right thing for all of our constituents,
- To be fact and data driven – and to share what we know, when we know it to be true,
- To live up to our company values and leadership
I hope you find this update informative.
Sincerely,
Chris
Security Incident Update
By Kunal Anand, Chief Technology Officer, Imperva
Before we get into the details and what we’ve learned, I’d like to share a direct message from all of us here at Imperva for our customers and partners: we regret that this incident occurred and have been working around the clock to learn from it and improve how we build and run Imperva. Security is never “done” and we must continue to evaluate and improve our processes every single day. Our vision remains the same: to lead the world’s fight on behalf of our customers and their customers to keep data and applications safe from cybercriminals. Now, more than ever, we commit to our vision, where data and applications are kept safe.
On August 27, 2019, Imperva announced a security incident that affected a subset of our Cloud WAF customers. We’ve conducted a thorough investigation with internal security teams as well as outside forensics specialists to determine the root cause. In the spirit of transparency, I’d like to share more insights into what happened, the attack chain that led to the exfiltration of information from a database snapshot, what we’ve learned, and how we’ve improved our IT and product security posture.
What Happened (TL;DR)
Our investigation identified an unauthorized use of an administrative API key in one of our production AWS accounts in October 2018, which led to an exposure of a database snapshot containing emails and hashed & salted passwords.
How It Happened
I’ll start by going back to 2017 when our Cloud WAF, previously known as Incapsula, was under significant load from onboarding new customers and meeting their critical demands. That year, our product development team began the process of adopting cloud technologies and migrated to AWS Relational Database Service (RDS) to scale our user database.
Some key decisions made during the AWS evaluation process, taken together, allowed information to be exfiltrated from a database snapshot. These were: (1) we created a database snapshot for testing; (2) an internal compute instance that we created was accessible from the outside world and it contained an AWS API key; (3) this compute instance was compromised and the AWS API key was stolen; and (4) the AWS API key was used to access the snapshot.
Corrective Actions
The steps we have taken since this incident to improve our security protocols include: (1) applying tighter security access controls; (2) increasing audit of snapshot access; (3) decommissioning inactive compute instances; (4) rotating credentials and strengthening our credential management processes; (5) putting all internal compute instances behind our VPN by default; and (6) increasing the frequency of infrastructure scanning.
Key Questions
I’d like to directly answer some common questions that our teams have been asked over the past few weeks by our customers and partners. As you can imagine, we were unable to answer many of these questions at the time of the announcement as we were operating under a fluid threat model and were very early in our investigation.
How did Imperva learn about the exfiltration?
On August 20, 2019 we received a data set from a third-party requesting a bug bounty. Upon initial review, we immediately activated our incident response teams and subsequently notified our customers.
Was the exfiltration the result of a product vulnerability?
No, the data exfiltration was not the result of a Cloud WAF product vulnerability or a vulnerability in any of our other products.
When did the exfiltration happen?
Based on a detailed log analysis, the data exfiltration occurred in October 2018. The dataset was from a snapshot as of September 15, 2017.
How do you know the dataset was from September 15, 2017?
We compared the SQL dump in the provided dataset to our snapshots and found a match. As of this post, we can say that the elements of customer data defined above were limited to Cloud WAF accounts prior and up to September 15, 2017. Databases and snapshots for our other product offerings were not exfiltrated.
What was in the dataset?
We conducted an extensive analysis and found the following items in the dataset: email addresses, hashed and salted passwords, API keys, and TLS keys. In compliance with GDPR, we contacted the appropriate global law enforcement organizations and regulators. It took several weeks to comprehensively and accurately detail the contents in the dataset.
Could this happen again today?
No, the security processes we had for the vulnerable compute instance and database snapshots are not representative of our current controls. Both issues would be flagged today in a net-new deployment: 1) new instances are created behind our VPN by default, 2) we have monitoring and patching programs in place, and 3) we have processes to decommission unused and non-critical compute instances.
Has there been any account abuse related to this security incident?
We have since gone back and looked for malicious activity, leveraging threat intelligence feeds in conjunction with audit logs (see product security update below), related to accounts in the dataset. Thus far, we have not found any malicious behavior targeting our customers (logins, rule changes, etc.) and have implemented procedures to continue monitoring for such activity. We remain vigilant, however, and will continue to monitor for malicious behavior.
Did Imperva deploy its Database Activity Monitoring (DAM) product to monitor these database snapshots?
In 2017, our DAM solution did not support AWS RDS. At the time, our product relied on an agent-based architecture that could not install in any Platform as a Service (PaaS) database solution, which is part of the reason we developed and launched a beta for Cloud Data Security (CDS) earlier this year. We have been using it to help us monitor and perform asset discovery for our Cloud WAF product. CDS was not implemented until after the incident had taken place.
Security Incident Workstreams and New Controls
When we activated our incident response teams, we officially created the following 10 internal workstreams to manage the investigation 24×7:
- Project management and coordination among our global offices, internal advisors, and external advisors, which enabled us to progress on a “follow the sun” model
- Initial discovery, customer + regulatory notices
- Engage external vendors
- Forensics work streams
- Product enhancements to accelerate the roadmap for delivering security controls (see product security update below)
- Assisting customers with remediations (“white glove support”)
- Changes to better secure internal development and backend environments
- Enhanced pen-testing and scanning the environment for vulnerabilities
- Incorporate learnings into security program
- Ongoing communications: employees, customers, partners, analysts, shareholders, government regulators, and law enforcement
These workstreams resulted in initiatives to improve both our IT and product security posture. I’d like to walk through both and touch on specific initiatives.
IT Controls & Processes
- Our immediate reaction to kick off workstreams and task forces could not have happened if we had not prepared an incident response team ahead of time. We’ve developed internal playbooks over the years to assist in process management. While every situation is different, it helps to have guidelines to follow.
- We performed an emergency rotation of all administrative keys across all of our AWS environments. In addition, we increased the frequency of all key rotations for administrative and non-administrative accounts.
- In Q2 2018, we enforced SSO and multi-factor authentication in our AWS management console. While this change would not have prevented the API key access that occurred, it was a significant step in improving our access management controls.
- While we perform routine penetration tests, we kicked off and executed an emergency analysis to try and identify similar potential additional vulnerabilities. We did not uncover any additional vulnerabilities.
- The compute instance in question plus other unused and experimental instances discovered as part of the investigation were archived to preserve logs, and subsequently decommissioned.
- While we enabled AWS CloudTrail and GuardDuty and ingested those log events in our SIEM two years ago, we are being more proactive today and are getting those events forwarded into our UEBA, including VPC NetFlow logs. We’ve created alerts and workflows around key events. We have also developed SOC dashboards to monitor and alert on malicious activity at the customer account level (API and management console). These leverage our product’s built-in audit logs (see product security below).
- In general, we used this opportunity to audit and tighten all security group ACLs and VPC ingress/egress rules.
- We also perform daily scans and audit checks of S3 buckets. We believe it is important to do this to prevent any unauthorized exposures in the future.
Product Security
- Earlier this year, we rolled out SSO for our management console. This was a capability that was requested by our biggest enterprise customers, and today we have customers that use multi-factor authentication in conjunction with SSO to access their Cloud WAF management.
- We forced a password change, increased the minimum password complexity, and decreased the time to rotate passwords. The latter two were planned for a future release but were subsequently prioritized and their implementations accelerated as a result of this incident. All have been released to GA in Cloud WAF.
- Our Cloud WAF has always generated audit log events for management and API activity. Post-incident, we used these audit logs to look for malicious behavior via our Attack Analytics product. Our plan was always to make the audit function available to customers in a future release. We prioritized this capability post-incident and it is now GA in the product. Customers can download full audit reports for Cloud WAF that include logins, password changes, rule changes, and dozens of other event types. These reports can be generated via the management console and API.
- We integrated our Attack Analytics product to analyze hosts and IP addresses in Cloud WAF rules and access controls. What this means is that we are leveraging our own IP reputation and threat intelligence feeds to call out malicious activity in key rules and policies and alert customers about this in real-time.
Key Takeaways
Finally, I wanted to share a few reflections of what we’ve collectively learned over the past few weeks.
First and foremost, when an organization responds to a security incident, we strongly believe that they should operate honestly and transparently with all of their stakeholders (employees, customers, partners, shareholders, etc.). We communicated quickly and early in the investigation process to ensure our customers could make informed decisions and act on the security measures we were recommending. Those recommendations resulted in our customers changing more than 13,000 passwords, rotating over 13,500 SSL certificates, and regenerating over 1,400 API keys. Our CEO, Chris Hylen, shared it front and center via a public blog post, was personally involved in the investigation leadership, and made calls to clients and partners to provide updates. When developing our internal playbooks, we kept coming back to the theme of being transparent. As a result, our key customers and partners told us they appreciated our openness and sincerity.
Second, there is a natural tension between the desire to share newly discovered information with customers, and the need of an investigation to progress in a forensic and regimented manner. Our approach to balance this tension is to focus on being fact-driven in our communications to employees, customers, partners and the community, which continues to mean that we must confirm findings and assessments (and take actions to protect all of our customers) in order to responsibly share additional details.
Third, we used our company’s globally distributed nature to our advantage, and our incident response vendor, Aon Cyber Solutions, did the same. We established rotating incident response centers in our US and Israel locations that worked around the clock on critical forensics, remediations and customer support. Our workstreams contained cross-functional stakeholders across different time zones and met multiple times a day, every day, for several weeks. Being a distributed company allowed us to move faster as we established a “follow the sun” model. Workstreams had deliverables and specific formats for producing a work product, which made things efficient to manage and stitch together.
Fourth, we take ownership of the fact that the incident was a result of our choices, actions we took and failed to take before, during, and after our database migration. We recommend all organizations take the time to fully understand the shared responsibility of deploying and managing applications and data in Infrastructure as a Service (IaaS) solutions. As mentioned above, we’ve incorporated the key learnings to change the way we holistically think about and manage our own Secure Software Development Lifecycle (SSDLC).
[See our original post about this security incident in the August 27, 2019 blog below.]
I want to share details about a security incident at Imperva that resulted in a data exposure impacting our Cloud Web Application Firewall (WAF) product, formerly known as Incapsula. In this situation, we will do our best to honor the following principles:
- To do the right thing for all of our constituents
- To be fact and data driven – and to share what we know, when we know it to be true
- To live up to our company values and leadership expectations
We want to be very clear that this data exposure is limited to our Cloud WAF product. Here is what we know about the situation today:
- On August 20, 2019, we learned from a third party of a data exposure that impacts a subset of customers of our Cloud WAF product who had accounts through September 15, 2017.
- Elements of our Incapsula customer database through September 15, 2017 were exposed. These included:
- email addresses
- hashed and salted passwords
And for a subset of the Incapsula customers through September 15, 2017:
-
- API keys
- customer-provided SSL certificates
We continue to investigate this incident around the clock and have stood up a global, cross-functional team. Here are the actions we have taken:
- We activated our internal data security response team and protocol, and continue to investigate with the full capacity of our resources how this exposure occurred.
- We have informed the appropriate global regulatory agencies.
- We have engaged outside forensics experts.
- We implemented forced password rotations and 90-day expirations in our Cloud WAF product.
- We are informing all impacted customers directly and sharing the steps we are taking to safeguard their accounts and data, and additional actions they can take themselves.
We recommend the following security measures as a matter of good practice for all of our customers:
- Change user account passwords for Cloud WAF (https://my.incapsula.com)
- Implement Single Sign-On (SSO)
- Enable two-factor authentication
- Generate and upload new SSL certificate
- Reset API keys
We profoundly regret that this incident occurred and will continue to share updates going forward. In addition, we will share learnings and new best practices that may come from our investigation and enhanced security measures with the broader industry. Imperva will not let up on our efforts to provide the very best tools and services to keep our customers and their customers safe.
If you have additional questions, please reach out to securityincident@imperva.com.
