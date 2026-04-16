Title: Trouble in Paradise

URL Source: https://blog.darklab.hk/2021/07/06/trouble-in-paradise/

Published Time: 2021-07-06T09:26:55+00:00

Markdown Content:
# Trouble in Paradise | Dark Lab

[](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/#)[](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/)

[](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/#)
#### Menu

*   [About Dark Lab](https://blog.darklab.hk/about/)
*   [Insights](https://blog.darklab.hk/)

[](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/#)Search for: 

[Skip to content](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/#content)

# [Dark Lab](https://blog.darklab.hk/)

## Insights from Hong Kong's largest group of technical cyber security professionals.

[](https://blog.darklab.hk/)

![Image 1](https://blog.darklab.hk/wp-content/uploads/2020/06/cropped-jared-arango-1-mh6u3qegq-unsplash-2.jpg)

# Trouble in Paradise

[Posted on July 6, 2021](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/)by [darklabhk](https://blog.darklab.hk/author/darklabhk/)

![Image 2](https://i0.wp.com/blog.darklab.hk/wp-content/uploads/2021/07/Cloud-compromise.jpg?resize=1000%2C267&ssl=1)
## **A case study of Cloud compromise**

Many organisations are increasingly moving to cloud solutions to solve their hosting needs, but outsourcing workload should not imply outsourcing security as well. The importance of security the cloud was recently highlighted by targeting of Microsoft Azure environments by Nobellium, the threat actor behind the SolarWinds Orion compromise. The threat actor notably exploited stolen SAML certificates for [vertical movement](https://www.microsoft.com/security/blog/2020/12/28/using-microsoft-365-defender-to-coordinate-protection-against-solorigate/#Tracking-the-cross-domain-Solarigate-attack), a rarely seen technique. Even without novel techniques, less sophisticated cybercriminal threat actors can also pose a threat to companies’ services in the cloud. Indeed, this week’s supply chain compromise operation by REvil is [suspected](http://huntress.com/blog/rapid-response-kaseya-vsa-mass-msp-ransomware-incident)to have been launched from a compromised web server hosted on AWS.

### **The Incident**

Recently, DarkLab’s incident response team has helped a South Asian client in the media sector to remediate an incident involving multiple cloud environments breaches, a case study we think can help organisations better plan for secure implementations of their cloud environments.

The incident originated from a likely exploitation of a known remote code execution [vulnerability](https://blog.orange.tw/2019/02/abusing-meta-programming-for-unauthenticated-rce.html)in a Jenkins instance, an open source software development automation server. The server was hosted in an Amazon Web Service (AWS) environment and had a hardcoded root access key. With that, the threat actor was able to roam the compromised environment undetected for four months. Logs availability has been an issue due to the lack of CloudTrail log retention but we know that the threat actor created multiple IAM user accounts and accessed internal data, including those stored in S3 buckets via the free Windows client S3 Browser.

Their primary intent, however, was to use the victim as a jumping spot to identify other targets vulnerable to the same Jenkins RCE and move laterally to their servers. They did so by deploying Linux and Windows virtual machines in new EC2 instances in the compromised environment to scan and exploit external IP addresses. The did so using T.2 micro sizing to avoid spikes in usage and remain hidden. The attacker deployed the additional EC2 instances in a different AWS region than that used by the victim, an anomaly that we suggest organisations monitor for.

A deeper dive into the system log of the Linux VMs shows that the attacker likely used Shodan to identify other vulnerable Jenkins instances online, suggesting their targeting was likely opportunistic. Similarly, analysis of the IP addresses used by the attacker to access our client – most of them AWS instances themselves – suggests the attack likely originated from multiple other compromised organisations.

From AWS, the threat actor managed to access a FTP server within a parallel Google Cloud Platform (GCP) environment. For this, they used a compromised hard-coded credential found in one of the configuration files in their BitBucket repository, also suspected to be compromised. After thorough environment and users’ enumeration, the attacker was able to obtain the password for another G-Suite user account, which they used to access data in the GCP environment and Google Drive.

Shortly after accessing the GCP, threat actors attempted to cover their tracks by deleting the company’s entire production environment, all hosted on AWS, and the backup copies. Fortunately, AWS retained some copies of the deleted backups which were able to provide to the victim organisation.

However, while the victim restored their AWS system they were not aware to reset the root access key. Unsurprisingly, the attacker quickly re-established a presence in their cloud and a few days later they re-deleted the production environment, although no ransom demand was recorded. This was when our incident response team was called to help.

### **Assessment**

Our investigation suggested that the threat actor behind this campaign is likely operating opportunistically and with a relatively low technical know-how. We often found traces of internet searches for open source tools or “how to” techniques. Nonetheless, such an actor could still pose significant operational damage to a large company by deleting their production environment.

The incident shows how even relatively unsophisticated threat actors are adopting an island-hopping approach by abusing imperfect implementations of commercial cloud platforms. Companies should ensure that standard security practices, like rotating passwords or access keys, monitoring suspicious activities, and prompt patching, are also applied to cloud environments.

### **What’s next?**

Our experience suggests that this was not an uncommon attack path for adversaries targeting cloud environments. Monitoring for common attack vectors can help indeitifyuing supicious behaviour earlier and contain an incident before it is too late.

Below are some monitoring metrics mapped against Mitre ATT&CK tactics that we recommend organisations implement to AWS Config, Lambda, or their choice of CSPM platforms for automated detection and remediation.

_Feel free to contact us at [threatintel at darklab dot hk] for the full set of 50 custom MITRE-based rules on AWS_

**Tactic****Technique (custom)****Log Source**
Initial access AWS user login failed multiple times CloudTrail
Initial access Multiple worldwide successful console login GuardDuty
Initial access Potential Web scanning activities with multiple web server 400 error from same the source IP Web access log
Privilege Escalation AWS “AssumeRole” from rare external AWS account CloudTrail
Discovery AWS potential IAM enumeration Activities CloudTrail
Defense Evasion/ Persistence Create/Update managed policy with excessive permission CloudTrail

Impact AWS Access Key Enabled CloudTrail
Exfiltration Egress rule added to a security group CloudTrail

Feel free to contact us at [**darklab dot cti at hk dot pwc dot com**] for any further information.

[Cloud](https://blog.darklab.hk/tag/cloud/)[Incident Response](https://blog.darklab.hk/tag/incident-response/)[Threat Intelligence](https://blog.darklab.hk/tag/threat-intelligence/)

# Post navigation

[Not Token for Granted](https://blog.darklab.hk/2021/03/30/not-token-for-granted/)

[What to expect in 2022](https://blog.darklab.hk/2022/01/20/what-to-expect-in-2022/)

### Leave a Reply[Cancel reply](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/#respond)

[](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/)

#### Topics

[0-day](https://blog.darklab.hk/tag/0-day/)[CTO](https://blog.darklab.hk/tag/cto/)[Cyber Threat Operations](https://blog.darklab.hk/tag/cyber-threat-operations/)[DarkLab](https://blog.darklab.hk/tag/darklab/)[Dark Web](https://blog.darklab.hk/tag/dark-web/)[Data Exfiltration](https://blog.darklab.hk/tag/data-exfiltration/)[Deep and Dark Web](https://blog.darklab.hk/tag/deep-and-dark-web/)[Hong Kong](https://blog.darklab.hk/tag/hong-kong/)[Incident Response](https://blog.darklab.hk/tag/incident-response/)[LockBit](https://blog.darklab.hk/tag/lockbit/)[Macau](https://blog.darklab.hk/tag/macau/)[MFA](https://blog.darklab.hk/tag/mfa/)[MITRE](https://blog.darklab.hk/tag/mitre/)[MITRE ATT&CK](https://blog.darklab.hk/tag/mitre-attck/)[MITRE TTP](https://blog.darklab.hk/tag/mitre-ttp/)[Ransomware](https://blog.darklab.hk/tag/ransomware/)[Ransomware-as-a-Service](https://blog.darklab.hk/tag/ransomware-as-a-service/)[Threat Intelligence](https://blog.darklab.hk/tag/threat-intelligence/)[TTP](https://blog.darklab.hk/tag/ttp/)[Zero Day](https://blog.darklab.hk/tag/zero-day/)

#### Previous posts

*   [March 2026](https://blog.darklab.hk/2026/03/)(1)
*   [February 2026](https://blog.darklab.hk/2026/02/)(1)
*   [September 2025](https://blog.darklab.hk/2025/09/)(1)
*   [July 2025](https://blog.darklab.hk/2025/07/)(1)
*   [June 2025](https://blog.darklab.hk/2025/06/)(1)
*   [May 2025](https://blog.darklab.hk/2025/05/)(1)
*   [April 2025](https://blog.darklab.hk/2025/04/)(2)
*   [January 2025](https://blog.darklab.hk/2025/01/)(2)
*   [August 2024](https://blog.darklab.hk/2024/08/)(1)
*   [April 2024](https://blog.darklab.hk/2024/04/)(2)
*   [November 2023](https://blog.darklab.hk/2023/11/)(1)
*   [October 2023](https://blog.darklab.hk/2023/10/)(1)
*   [September 2023](https://blog.darklab.hk/2023/09/)(1)
*   [June 2023](https://blog.darklab.hk/2023/06/)(1)
*   [April 2023](https://blog.darklab.hk/2023/04/)(1)
*   [March 2023](https://blog.darklab.hk/2023/03/)(1)
*   [January 2023](https://blog.darklab.hk/2023/01/)(1)
*   [November 2022](https://blog.darklab.hk/2022/11/)(1)
*   [October 2022](https://blog.darklab.hk/2022/10/)(2)
*   [September 2022](https://blog.darklab.hk/2022/09/)(1)
*   [July 2022](https://blog.darklab.hk/2022/07/)(1)
*   [April 2022](https://blog.darklab.hk/2022/04/)(2)
*   [March 2022](https://blog.darklab.hk/2022/03/)(1)
*   [February 2022](https://blog.darklab.hk/2022/02/)(1)
*   [January 2022](https://blog.darklab.hk/2022/01/)(1)
*   [July 2021](https://blog.darklab.hk/2021/07/)(1)
*   [March 2021](https://blog.darklab.hk/2021/03/)(5)
*   [February 2021](https://blog.darklab.hk/2021/02/)(1)
*   [November 2020](https://blog.darklab.hk/2020/11/)(1)
*   [October 2020](https://blog.darklab.hk/2020/10/)(1)
*   [September 2020](https://blog.darklab.hk/2020/09/)(1)
*   [August 2020](https://blog.darklab.hk/2020/08/)(1)
*   [June 2020](https://blog.darklab.hk/2020/06/)(2)
*   [May 2020](https://blog.darklab.hk/2020/05/)(1)
*   [March 2020](https://blog.darklab.hk/2020/03/)(1)

© DarkLab 2021

Search for: 

## Discover more from Dark Lab

Subscribe now to keep reading and get access to the full archive.

Type your email…

Subscribe

[Continue reading](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/#)

[](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/#)[](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/#)

Loading Comments...

Write a Comment... 

Email (Required) Name (Required) Website 

[](https://blog.darklab.hk/2021/07/06/trouble-in-paradise/#)

![Image 3](https://pixel.wp.com/g.gif?v=ext&blog=179046809&post=459&tz=8&srv=blog.darklab.hk&hp=atomic&ac=2&amp=0&j=1%3A15.8-a.1&host=blog.darklab.hk&ref=&fcp=0&rand=0.5781975989451577)