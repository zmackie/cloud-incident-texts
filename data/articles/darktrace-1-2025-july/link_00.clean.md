---
title: "Defending the Cloud: Stopping Cyber Threats in Azure and AWS with Darktrace"
url: "https://www.darktrace.com/blog/defending-the-cloud-stopping-cyber-threats-in-azure-and-aws-with-darktrace"
author: Alexandra Sentenac
published: 2025-07-08
source_type: article
source_domain: www.darktrace.com
cleanup_method: llm
---

# Stopping cloud threats in Azure and AWS with Darktrace

[Blog](https://www.darktrace.com/blog)

/

[Identity](https://www.darktrace.com/primary-topics/identity)

/

July 8, 2025

# Defending the Cloud: Stopping Cyber Threats in Azure and AWS with Darktrace

This blog examines three real-world cloud-based attacks in Azure and AWS environments, including credential compromise, data exfiltration, and ransomware detonation. Learn how Darktrace’s AI-driven threat detection and Autonomous Response capabilities help organizations defend against evolving threats in complex cloud environments.

[![Image 47](https://www.darktrace.com/blog/defending-the-cloud-stopping-cyber-threats-in-azure-and-aws-with-darktrace) Written by Alexandra Sentenac Cyber Analyst](https://www.darktrace.com/people/alexandra-sentenac)

Inside the SOC

Darktrace cyber analysts are world-class experts in threat intelligence, threat hunting and incident response, and provide 24/7 SOC support to thousands of Darktrace customers around the globe. _Inside the SOC_ is exclusively authored by these experts, providing analysis of cyber incidents and threat trends, based on real-world experience in the field.

![Image 48](https://www.darktrace.com/blog/defending-the-cloud-stopping-cyber-threats-in-azure-and-aws-with-darktrace)

Written by

Alexandra Sentenac

Cyber Analyst



## Real-world intrusions across Azure and AWS

As organizations pursue greater scalability and flexibility, cloud platforms like [Microsoft Azure and Amazon Web Services (AWS)](https://www.darktrace.com/cyber-ai-glossary/aws-cloud-security-vs-azure-cloud-security) have become essential for enabling remote operations and digitalizing corporate environments. However, this shift introduces a new set of security risks, including expanding attack surfaces, misconfigurations, and compromised credentials frequently exploited by threat actors.

This blog dives into three instances of compromise within a Darktrace customer’s Azure and AWS environment.

1.   The first incident took place in early 2024 and involved an attacker compromising a legitimate user account to gain unauthorized access to a customer’s Azure environment. 
2.   The other two incidents, taking place in February and March 2025, targeted AWS environments. In these cases, threat actors exfiltrated corporate data, and in one instance, was able to detonate [ransomware](https://www.darktrace.com/cyber-ai-glossary/ransomware) in a customer’s environment.

## Case 1 - Microsoft Azure

![Image 59: Simplified timeline of the attack on a customer’s Azure environment.](https://cdn.prod.website-files.com/626ff4d25aca2edf4325ff97/686d6eaed7c45b1772ffc7aa_Screenshot%202025-07-08%20at%2012.16.54%E2%80%AFPM.avif)

Figure 1: Simplified timeline of the attack on a customer’s Azure environment.

In early 2024, Darktrace identified a cloud compromise on the Azure cloud environment of a customer in the Europe, the Middle East and Africa (EMEA) region.

### Initial access

In this case, a threat actor gained access to the customer’s cloud environment after stealing access tokens and creating a rogue virtual machine (VM). The malicious actor was found to have stolen access tokens belonging to a third-party external consultant’s account after downloading cracked software.

With these stolen tokens, the attacker was able to authenticate to the customer’s Azure environment and successfully modified a security rule to allow inbound SSH traffic from a specific IP range (i.e., securityRules/AllowCidrBlockSSHInbound). This was likely performed to ensure persistent access to internal cloud resources.

### Detection and investigation of the threat

[Darktrace / IDENTITY](https://www.darktrace.com/products/identity) recognized that this activity was highly unusual, triggering the “Repeated Unusual SaaS Resource Creation” alert.

[Cyber AI Analyst](https://www.darktrace.com/cyber-ai-analyst) launched an autonomous investigation into additional suspicious cloud activities occurring around the same time from the same unusual location, correlating the individual events into a broader [account hijack incident.](https://www.darktrace.com/cyber-ai-glossary/account-takeover)

![Image 60](https://cdn.prod.website-files.com/626ff4d25aca2edf4325ff97/68a46b318e3a7cb2ae27fbc6_Number%20Of%20Events.avif)

Figure 3: Surrounding resource creation events highlighted by Cyber AI Analyst.

![Image 61](https://cdn.prod.website-files.com/626ff4d25aca2edf4325ff97/68a46b7847b14372520fabf4_Number%20Of%20Events.avif)

Figure 4: Surrounding resource creation events highlighted by Cyber AI Analyst.

“Create resource service limit” events typically indicate the creation or modification of service limits (i.e., quotas) for a specific Azure resource type within a region. Meanwhile, “Registers the Capacity Resource Provider” events refer to the registration of the Microsoft Capacity resource provider within an Azure subscription, responsible for managing capacity-related resources, particularly those related to reservations and service limits. These events suggest that the threat actor was looking to create new cloud resources within the environment.

Around ten minutes later, Darktrace detected the threat actor creating or modifying an Azure disk associated with a virtual machine (VM), suggesting an attempt to create a rogue VM within the environment.

Threat actors can leverage such rogue VMs to hijack computing resources (e.g., by running cryptomining malware), maintain persistent access, move laterally within the cloud environment, communicate with command-and-control (C2) infrastructure, and stealthily deliver and deploy malware.

### Persistence

Several weeks later, the compromised account was observed sending an invitation to collaborate to an external free mail (Google Mail) address.

Darktrace deemed this activity as highly anomalous, triggering a compliance alert for the customer to review and investigate further.

The next day, the threat actor further registered new multi-factor authentication (MFA) information. These actions were likely intended to maintain access to the compromised user account. The customer later confirmed this activity by reviewing the corresponding event logs within Darktrace.

## Case 2 – Amazon Web Services

![Image 62: Simplified timeline of the attack on a customer’s AWS environment](https://cdn.prod.website-files.com/626ff4d25aca2edf4325ff97/686d6fb3fb97cae5ab569bcf_Screenshot%202025-07-08%20at%2012.21.11%E2%80%AFPM.avif)

Figure 5: Simplified timeline of the attack on a customer’s AWS environment

In February 2025, another cloud-based compromised was observed on a UK-based customer subscribed to Darktrace’s Managed Detection and Response (MDR) service.

### How the attacker gained access

The threat actor was observed leveraging likely previously compromised credential to access several AWS instances within customer’s Private Cloud environment and collecting and exfiltrating data, likely with the intention of deploying ransomware and holding the data for ransom.

### Darktrace alerting to malicious activity

This observed activity triggered a number of alerts in Darktrace, including several high-priority Enhanced Monitoring alerts, which were promptly investigated by Darktrace’s Security Operations Centre (SOC) and raised to the customer’s security team.

**The earliest signs of attack observed by Darktrace** involved the use of two likely compromised credentials to connect to the customer’s Virtual Private Network (VPN) environment.

### Internal reconnaissance

Once inside, the threat actor performed internal reconnaissance activities and staged the Rclone tool “ProgramData\rclone-v1.69.0-windows-amd64.zip”, a command-line program to sync files and directories to and from different cloud storage providers, to an AWS instance whose hostname is associated with a public key infrastructure (PKI) service.

The threat actor was further observed accessing and downloading multiple files hosted on an AWS file server instance, notably finance and investment-related files. This likely represented data gathering prior to exfiltration.

Shortly after, the PKI-related EC2 instance started making SSH connections with the Rclone SSH client “SSH-2.0-rclone/v1.69.0” to a RockHoster Virtual Private Server (VPS) endpoint (193.242.184[.]178), suggesting the threat actor was exfiltrating the gathered data using the Rclone utility they had previously installed. The PKI instance continued to make repeated SSH connections attempts to transfer data to this external destination.

### Darktrace’s Autonomous Response

In response to this activity, **Darktrace’s Autonomous Response capability intervened, blocking unusual external connectivity to the C2 server via SSH, effectively stopping the exfiltration of data.**

This activity was further investigated by Darktrace’s SOC analysts as part of the MDR service. The team elected to extend the autonomously applied actions to ensure the compromise remained contained until the customer could fully remediate the incident.

### Continued reconissance

Around the same time, the threat actor continued to conduct network scans using the Nmap tool, operating from both a separate AWS domain controller instance and a newly joined device on the network. These actions were accompanied by further internal data gathering activities, with around 5 GB of data downloaded from an AWS file server.

The two devices involved in reconnaissance activities were investigated and actioned by Darktrace SOC analysts after additional Enhanced Monitoring alerts had triggered.

### Lateral movement attempts via RDP connections

Unusual internal RDP connections to a likely AWS printer instance indicated that the threat actor was looking to strengthen their foothold within the environment and/or attempting to pivot to other devices, likely in response to being hindered by Autonomous Response actions.

**This triggered multiple scanning, internal data transfer and unusual RDP alerts in Darktrace**, as well as additional Autonomous Response actions to block the suspicious activity.

### Suspicious outbound SSH communication to known threat infrastructure

Darktrace subsequently observed the AWS printer instance initiating SSH communication with a rare external endpoint associated with the web hosting and VPS provider Host Department (67.217.57[.]252), **suggesting that the threat actor was attempting to exfiltrate data to an alternative endpoint after connections to the original destination had been blocked.**

Further investigation using open-source intelligence (OSINT) revealed that this IP address had previously been observed in connection with SSH-based data exfiltration activity during an [Akira ransomware](https://www.darktrace.com/blog/akira-ransomware-how-darktrace-foiled-another-novel-ransomware-attack) intrusion [1].

Once again, connections to this IP were blocked by Darktrace’s Autonomous Response and subsequently these blocks were extended by Darktrace’s SOC team.

The above behavior generated multiple Enhanced Monitoring alerts that were investigated by Darktrace SOC analysts as part of the Managed Threat Detection service.

![Image 63: Enhanced Monitoring alerts investigated by SOC analysts as part of the Managed Detection and Response service.](https://cdn.prod.website-files.com/626ff4d25aca2edf4325ff97/686d70380ec6f8c994a3ea56_Screenshot%202025-07-08%20at%2012.23.29%E2%80%AFPM.avif)

Figure 5: Enhanced Monitoring alerts investigated by SOC analysts as part of the Managed Detection and Response service.

### **Final containment and collaborative response**

Upon investigating the unusual scanning activity, outbound SSH connections, and internal data transfers, Darktrace analysts extended the Autonomous Response actions previously triggered on the compromised devices.

As the threat actor was leveraging these systems for data exfiltration, all outgoing traffic from the affected devices was blocked for an additional 24 hours to provide the customer’s security team with time to investigate and remediate the compromise.

Additional investigative support was provided by Darktrace analysts through the Security Operations Service, after the customer's opened of a ticket related to the unfolding incident.

![Image 64: Simplified timeline of the attack ](https://cdn.prod.website-files.com/626ff4d25aca2edf4325ff97/686d706c1372dd9a07c80e4a_Screenshot%202025-07-08%20at%2012.24.21%E2%80%AFPM.avif)

Figure 8: Simplified timeline of the attack 

Around the same time of the compromise in Case 2, Darktrace observed a similar incident on the cloud environment of a different customer.

### Initial access

On this occasion, the threat actor appeared to have **gained entry into the AWS-based Virtual Private Cloud (VPC) network****via a**[**SonicWall**](https://www.darktrace.com/blog/inside-akiras-sonicwall-campaign-darktraces-detection-and-response)**SMA 500v EC2 instance allowing inbound traffic on any port**.

The instance received HTTPS connections from three rare Vultr VPS endpoints (i.e., 45.32.205[.]52, 207.246.74[.]166, 45.32.90[.]176).

### Lateral movement and exfiltration

Around the same time, the EC2 instance started scanning the environment and attempted to pivot to other internal systems via RDP, notably a DC EC2 instance, which also started scanning the network, and another EC2 instance.

The latter then proceeded to transfer more than 230 GB of data to the rare external GTHost VPS endpoint 23.150.248[.]189, while downloading hundreds of GBs of data over SMB from another EC2 instance.

![Image 65: Cyber AI Analyst incident generated following the unusual scanning and RDP connections from the initial compromised device.](https://cdn.prod.website-files.com/626ff4d25aca2edf4325ff97/686d70a1318b6e8880f836c8_Screenshot%202025-07-08%20at%2012.25.14%E2%80%AFPM.avif)

Figure 7: Cyber AI Analyst incident generated following the unusual scanning and RDP connections from the initial compromised device.

The same behavior was replicated across multiple EC2 instances, whereby compromised instances uploaded data over internal RDP connections to other instances, which then started transferring data to the same GTHost VPS endpoint over port 5000, which is typically used for Universal Plug and Play (UPnP).

### What Darktrace detected

Darktrace observed the threat actor uploading a total of 718 GB to the external endpoint, after which they detonated ransomware within the compromised VPC networks.

**This activity generated nine Enhanced Monitoring alerts in Darktrace, focusing on the scanning and external data activity, with the earliest of those alerts triggering around one hour after the initial intrusion**.

**Darktrace’s Autonomous Response capability was not configured to act on these devices**. Therefore, the malicious activity was not autonomously blocked and escalated to the point of ransomware detonation.

## Conclusion

This blog examined three real-world compromises in customer cloud environments each illustrating different stages in the attack lifecycle.

The first case showcased a notable progression from a SaaS compromise to a full cloud intrusion, emphasizing the critical role of anomaly detection when legitimate credentials are abused.

The latter two incidents demonstrated that while early detection is vital, the ability to autonomously block malicious activity at machine speed is often the most effective way to contain threats before they escalate.

Together, these incidents underscore the need for continuous visibility, behavioral analysis, and machine-speed intervention across hybrid environments. Darktrace's AI-driven detection and Autonomous Response capabilities, combined with expert oversight from its Security Operations Center, give defenders the speed and clarity they need to contain threats and reduce operational disruption, before the situation spirals.

_Credit to Alexandra Sentenac (Senior Cyber Analyst) and Dylan Evans (Security Research Lead)_

## References

[1] [https://www.virustotal.com/gui/ip-address/67.217.57.252/community](https://www.virustotal.com/gui/ip-address/67.217.57.252/community)

### Case 1

#### **Darktrace / IDENTITY model alerts**

IaaS / Compliance / Uncommon Azure External User Invite

SaaS / Resource / Repeated Unusual SaaS Resource Creation

IaaS / Compute / Azure Compute Resource Update

#### **Cyber AI Analyst incidents**

Possible Unsecured AzureActiveDirectory Resource

Possible Hijack of Office365 Account

### Case 2

#### **Darktrace / NETWORK model alerts**

Compromise / SSH Beacon

Device / Multiple Lateral Movement Model Alerts

Device / Suspicious SMB Scanning Activity

Device / SMB Lateral Movement

Compliance / SSH to Rare External Destination

Device / Anomalous SMB Followed By Multiple Model Alerts

Device / Anonymous NTLM Logins

Anomalous Connection / SMB Enumeration

Device / New or Uncommon SMB Named Pipe Device / Network Scan

Device / Suspicious Network Scan Activity

Device / New Device with Attack Tools

Device / RDP Scan Device / Attack and Recon Tools

Compliance / High Priority Compliance Model Alert

Compliance / Outgoing NTLM Request from DC

Compromise / Large Number of Suspicious Successful Connections

Device / Large Number of Model Alerts

Anomalous Connection / Multiple Failed Connections to Rare Endpoint

Unusual Activity / Internal Data Transfer

Anomalous Connection / Unusual Internal Connections

Device / Anomalous RDP Followed By Multiple Model Alerts

Unusual Activity / Unusual External Activity

Unusual Activity / Enhanced Unusual External Data Transfer

Unusual Activity / Unusual External Data Transfer

Unusual Activity / Unusual External Data to New Endpoint

Anomalous Connection / Multiple Connections to New External TCP Port

**Darktrace / Autonomous Response model alerts**

Antigena / Network / Significant Anomaly / Antigena Enhanced Monitoring from Server Block

Antigena / Network / Manual / Quarantine Device

Antigena / MDR / MDR-Quarantined Device

Antigena / MDR / Model Alert on MDR-Actioned Device

Antigena / Network / Significant Anomaly / Antigena Enhanced Monitoring from Client Block

Antigena / Network / Significant Anomaly / Antigena Alerts Over Time Block

Antigena / Network / Insider Threat / Antigena Network Scan Block

Antigena / Network / Significant Anomaly / Antigena Significant Server Anomaly Block

Antigena / Network / Insider Threat / Antigena SMB Enumeration Block

Antigena / Network / Significant Anomaly / Antigena Controlled and Model Alert

Antigena / Network / Significant Anomaly / Antigena Significant Anomaly from Client Block

Antigena / Network / External Threat / Antigena Suspicious Activity Block

Antigena / Network / Insider Threat / Antigena Internal Data Transfer Block

#### **Cyber AI Analyst incidents**

Possible Application Layer Reconnaissance Activity

Scanning of Multiple Devices

Unusual Repeated Connections

Unusual External Data Transfer

### Case 3

#### Darktrace / NETWORK model alerts

Unusual Activity / Unusual Large Internal Transfer

Compliance / Incoming Remote Desktop

Unusual Activity / High Volume Server Data Transfer

Unusual Activity / Internal Data Transfer

Anomalous Connection / Unusual Internal Remote Desktop

Anomalous Connection / Unusual Incoming Data Volume

Anomalous Server Activity / Domain Controller Initiated to Client

Device / Large Number of Model Alerts

Anomalous Connection / Possible Flow Device Brute Force

Device / RDP Scan

Device / Suspicious Network Scan Activity

Device / Network Scan

Anomalous Server Activity / Anomalous External Activity from Critical Network Device

Anomalous Connection / Download and Upload

Unusual Activity / Unusual External Data Transfer

Unusual Activity / High Volume Client Data Transfer

Unusual Activity / Unusual External Activity

Anomalous Connection / Uncommon 1 GiB Outbound

Device / Increased External Connectivity

Compromise / Large Number of Suspicious Successful Connections

Anomalous Connection / Data Sent to Rare Domain

Anomalous Connection / Low and Slow Exfiltration to IP

Unusual Activity / Enhanced Unusual External Data Transfer

Anomalous Connection / Multiple Connections to New External TCP Port

Anomalous Server Activity / Outgoing from Server

Anomalous Connection / Multiple Connections to New External UDP Port

Anomalous Connection / Possible Data Staging and External Upload

Unusual Activity / Unusual External Data to New Endpoint

Device / Large Number of Model Alerts from Critical Network Device

Compliance / External Windows Communications

Anomalous Connection / Unusual Internal Connections

Cyber AI Analyst incidents

Scanning of Multiple Devices

Extensive Unusual RDP Connections

### MITRE ATT&CK mapping

(Technique name – Tactic ID)

#### _Case 1_

Defense Evasion - Modify Cloud Compute Infrastructure: Create Cloud Instance

Persistence – Account Manipulation

#### _Case 2_

Initial Access - External Remote Services

Execution - Inter-Process Communication

Persistence - External Remote Services

Discovery - System Network Connections Discovery

Discovery - Network Service Discovery

Discovery - Network Share Discovery

Lateral Movement - Remote Desktop Protocol

Lateral Movement - Remote Services: SMB/Windows Admin Shares

Collection - Data from Network Shared Drive

Command and Control - Protocol Tunneling

Exfiltration - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol

### _Case 3_

Initial Access - Exploit Public-Facing Application

Discovery - Remote System Discovery

Discovery - Network Service Discovery

Lateral Movement - Remote Services

Lateral Movement - Remote Desktop Protocol

Collection - Data from Network Shared Drive

Collection - Data Staged: Remote Data Staging

Exfiltration - Exfiltration Over C2 Channel

Command and Control - Non-Standard Port

Command and Control – Web Service

Impact - Data Encrypted for Impact

### **List of IoCs**

_IoC  Type Description + Probability_

193.242.184[.]178 - IP Address - Possible Exfiltration Server

45.32.205[.]52 - IP Address - Possible C2 Infrastructure

45.32.90[.]176 - IP Address - Possible C2 Infrastructure

207.246.74[.]166 - IP Address - Likely C2 Infrastructure

67.217.57[.]252 - IP Address - Likely C2 Infrastructure

23.150.248[.]189 - IP Address - Possible Exfiltration Server
