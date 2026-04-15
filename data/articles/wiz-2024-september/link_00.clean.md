---
title: Uncovering Hybrid Cloud Attacks Part 2 – The Attack
url: "https://www.wiz.io/blog/uncovering-hybrid-cloud-attacks-part-2-the-attack"
author: Yotam Meitar
published: 2024-09-04
source_type: article
source_domain: www.wiz.io
cleanup_method: llm
---

# Uncovering Hybrid Cloud Attacks Part 2 – The Attack

in this second part of the series, we’ll share the details of a real-world sophisticated, long-term attack in the cloud.

[Yotam Meitar](https://www.wiz.io/authors/yotam-meitar)

September 4, 2024

Effective response to cloud and hybrid attacks can be uniquely challenging. In this three-part series, we discuss how implementing intelligence-driven contextualized incident response allows defenders to turn attackers’ advantages in the cloud against them and respond more effectively to threats.

After introducing the concept in [part one](https://www.wiz.io/blog/uncovering-hybrid-cloud-attacks-part-1-addressing-the-speed-of-cloud-attacks), in this second part of the series, we’ll share the details of a real-world sophisticated, long-term attack in the cloud. In part three, we’ll dive into a step-by-step analysis of the response efforts to the same attack, highlighting practical takeaways for effective incident response.

To protect the victim organization’s identity, certain details of the attack have been modified and combined with other attacks seen in the wild. However, every stage of the presented case study was performed by real attackers and responders. By first analyzing the attack from the attacker’s perspective, we can see how intelligence-driven incident response can be leveraged to defeat even the most sophisticated attacks.

While we naturally cannot say for certain what attackers were thinking at every stage, the eventual forensic investigation and incident response efforts allow us to reconstruct an accurate attack timeline. Understating the key stages in this timeline is crucial to understanding the complications faced by the victim organization in performing incident response.

## [](https://www.wiz.io/blog/uncovering-hybrid-cloud-attacks-part-2-the-attack)Initial Access and Lateral Movement to the Cloud

Having identified the target organization as their desired victim, attackers initiated a wide social media phishing campaign targeting company employees. In this case, employees in the victim organization’s IT and security departments were targeted first, presumably to provide attackers highly privileged access from the first stages of their operation. Clever social engineering was used to convince these employees to download and execute malicious payloads concealed in a variety of technical programs and data files.

This approach initially paid off in a surprising way, as a cloud dev-ops engineer executed the malicious payload on their personal home computer which contained no sensitive company information. This turned out to be a lucky break for attackers, as the unmanaged home device lacked the EDR installed on corporate devices which may have prevented execution of the malicious payload. Having full control of this personal device became key to this attack’s persistent nature and difficult response.

As the attack occurred during the height of the COVID-19 pandemic, the victim organization had recently transitioned hundreds of employees to working from home. Among other solutions, this entailed enabling employees to use their personal devices to connect remotely to company resources leveraging Citrix. Unfortunately, this allowed attackers to extract valid Citrix session cookies from the compromised employee laptop and successfully hijack a valid privileged session into the corporate network. This session contained direct RDP access to a jump server used to access and manage the company’s production AWS environment. From this server attackers were able to extract highly privileged AWS access keys and proceed to the main phase of the attack.

## [](https://www.wiz.io/blog/uncovering-hybrid-cloud-attacks-part-2-the-attack)Wide-Scale Cloud Compromise

Once access to the main production cloud environment was established, attackers moved in two parallel directions very quickly. Within hours, they began exfiltrating data from S3 storage buckets and sensitive RDS databases containing client data, as well as installing reverse shells on EC2 instances in multiple VPCs. The speed at which this phase of the attack was executed leaves little doubt that much of it was automated leveraging pre-existing cloud reconnaissance scripts and techniques.

Unlike destructive attacks such as ransomware which usually reveal their existence by performing encryption, wiping data or taking down systems, this attack was purely a data-theft operation. Attackers were clearly content with maintaining their access to sensitive data, remaining under the radar of the victim organization’s security teams for well over a year.

![Image 12](blob:http://localhost/fb4ce946eefa3101f0d46517e170ea54)

In addition to successfully exfiltrating highly sensitive organizational data and establishing a robust foothold in the cloud environment, attackers were also diligent in covering their tracks. Deleting local OS logs from compromised EC2 instances to prevent analysis of logins and executed commands and modifying S3 and RDS audit policies to prevent the organization from knowing exactly which data was being accessed, significantly increased their ability to maintain stealth. When the organization finally realized something may be wrong, the attack had been going on for over 17 months. Fig. 1 depicts a high-level overview of the attack.

## [](https://www.wiz.io/blog/uncovering-hybrid-cloud-attacks-part-2-the-attack)Detection and Repeated Re-Entry

A key advantage working for attackers was highly effective persistence. This was a hybrid attack including three distinct and separate environments: the initially compromised employee home, the corporate on-premises environment compromised through Citrix and the jump server, and finally the targeted production cloud environment. The hybrid nature of the attack made it extremely difficult for company incident responders to remediate. Whenever they would eradicate certain parts of the threat by changing credentials or quarantining machines, they would later discover that attackers had re-emerged in the environment. Instead of a standard eradication and remediation effort, incident responders were faced with a frustrating game of whack-a-mole.

From the attackers’ perspective, this must have been gratifying and even amusing. Once their access to AWS was revoked, they simply acquired new access through the compromised on-premises jump server, and continued exfiltrating sensitive data.

Even when their access to the jump server was eradicated, all they had to do was simply go back to the compromised employee laptop, wait for a new session on the jump server, and they were back in.

A crucial element which made this strategy so effective was the attackers’ patience. Instead of immediately attempting to regain lost access to sensitive data after each eradication and remediation attempt, attackers would wait for the storm to pass, allow the organization to assume a false sense of security, and only then return and establish their access. This back-and-forth continued for several months before a comprehensive investigation finally revealed the full scope of the attack.

This case study highlights the effectiveness of hybrid on-prem/cloud attacks. The ability to perform malicious activities with speed and automation in the cloud while relying on robust persistence in multiple environments enables attackers to further exploit an already uneven playing field to their advantage. While these attacks may seem daunting, they are certainly beatable.

In the [final part of this series](https://www.wiz.io/blog/uncovering-hybrid-cloud-attacks-part-3-the-response) we’ll share the real-world response efforts to this sophisticated attack, focusing on the ways intelligence-driven incident response saved the day for the victim organization.
