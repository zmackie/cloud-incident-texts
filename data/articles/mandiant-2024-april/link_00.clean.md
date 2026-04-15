---
title: "SEC303 - Cloud compromises: Lessons learned from Mandiant investigations in 2023"
url: "https://assets.swoogo.com/uploads/3783545-66183eb421ec0.pdf"
published: "Thu, 11 Apr 2024 19:49:10 GMT"
source_type: pdf
source_domain: assets.swoogo.com
cleanup_method: fallback_heuristic
---

# Cloud compromises: 

Lessons learned from Mandiant investigations in 2023 03 Proprietary Google Cloud Next ‘24 

## Will Silverstone 

Senior Consultant Mandiant, Google Cloud 

## Omar ElAhdan 

Principal Consultant Mandiant, Google Cloud 04 Proprietary 

# Agenda 

Introduction and Overview 

2023 cloud compromise themes Common misconfigurations pillars 

Challenges, Case Studies, and Takeaways 

Wrap-Up 

Living off the land (in the cloud) Cloud attack surface Third party threats 

Foundational pillars 05 Google Cloud Next ‘24 Proprietary 

99% of organizations are running some sort of hybrid infrastructure (cloud + on-prem) .

Who does this apply to 

State of Cloud Threat Detection and Response Report - March 2023 06 Google Cloud Next ‘24 Proprietary 

# Significant Shifts 

2019-2021: Focus on Ransomware 

During this period, there was a rise in ransomware facilitated by the growing availability of Ransomware as a Service offerings 

During this period, ransomware began to lose ground to data theft and extortion as the primary driving factor for financial success 

2022-2023: Shift to Data Theft + Extortion 

Increase in intrusions involving data theft: 

M-Trends 2023 07 Google Cloud Next ‘24 Proprietary 

## What’s Changed 

● Lines between on-premise and cloud environments are blurred 

● Extended attack surface 

● Risk of third-party and external access 

● Attacks are multi-dimensional 

Organizations have migrated critical workloads to the cloud; however, they have not adapted their security mindset to this new landscape 08 Google Cloud Next ‘24 Proprietary 

# Background 

Living off the land Third party relationships Cloud attack surface 

Identity 

Resources 

Network 

Endpoints 

2023 Cloud Compromise Themes 

> Common Misconfigurations pillars

09 Google Cloud Next ‘24 Proprietary 

# Threat Actor Categorizations 010 Google Cloud Next ‘24 Proprietary 

Case studies and examples are drawn from our experiences and activities working for a variety of our clients, and do not represent our work for any one client or set of clients. In many cases, details have been changed to obscure the identity of our clients and individuals associated with our clients. 011 Proprietary Google Cloud Next ‘24 

# Living off the Land 

In Cloud Environments 012 Proprietary Google Cloud Next ‘24 

Living off the Land involves the abuse of native tools and processes on systems to blend in with normal system activities and operate discreetly with a lower likelihood of being detected or blocked because these tools are already deployed and trusted in the environment.” 

> CISA Joint Guidance: Identifying and Mitigating Living Off the Land Techniques 013 Proprietary

# Living off the Land (in the Cloud) 

Common tactics and techniques used in cloud environments: 

Abusing trusted service infrastructure 

Abusing of native cloud service provider tools 

Deploying infrastructure to blend in with legitimate traffic 

Abusing trusted locations to bypass MFA 014 Google Cloud Next ‘24 Proprietary 

# Abusing management tooling for cloud access 

Management Tooling and Platforms 

Code repository 

Collaboration Platforms Documentation Mobile Device Management 

Cloud Platform 

Incident Response Case Study #1 

Victim Organization Infrastructure 015 Google Cloud Next ‘24 Proprietary 

# Abusing management tooling for cloud access 

Management Tooling and Platforms 

Code repository 

Collaboration Platforms Documentation Mobile Device Management 

Compromised developer credentials to access code repository and architecture diagrams 

Exfiltrated privileged cloud session keys 

Pushed shell script to admin user’s endpoints 

Identified administrative credentials to single-factor MDM platform 

Decrypted secrets which included private keys, usernames, and passwords for production cryptocurrency wallets 

1

2

34

5

Transferred cryptocurrency to attacker controlled wallet 

Attacker Crypto Wallet 

6

Cloud Platform 

Incident Response Case Study #1 016 Google Cloud Next ‘24 Proprietary 

Identity 

Continually review and reduce privileged access 

Resources 

Scan for credentials in insecure locations 

Network 

Restrict access to management tooling from trusted locations only 

Endpoints 

Treat trusted service infrastructure as tier-0 

# Takeaways Google Cloud Next ‘24 Proprietary 

# Blending in to cloud services 

Victim Cloud Platform 

Virtual Machines 

Attacker Controlled Cloud Platform 

Abused self-service password reset to obtain credentials 

Performed reconnaissance and accessed cloud admin portal 

Created new VM to blend into normal traffic 

Modified firewall rules on cloud database 

Exfiltrated data 

1

2

3

4

5

6

SQL Database 

Accessed secret server hosted on cloud VM Exported all credentials and transferred to attacker controlled storage bucket 

Incident Response Case Study #2 018 Google Cloud Next ‘24 Proprietary 

Identity 

Harden password reset and MFA modification processes MFA everywhere including trusted locations 

Resources 

Targeted detections on resource creation/modifications outside of standard process 

Network 

Monitor uploads to external cloud storage 

Endpoints 

Restrict devices that can make critical modifications 

# Takeaways 019 Proprietary Google Cloud Next ‘24 

# Cloud Attack Surface Proprietary 

Credentials were the leading compromise factor in the cloud in 2023 

> Google Threat Horizons Report H1 2024 021 Proprietary

# “Extended” Cloud Attack Surface 

Common Challenges: Lack of identity tiering & separation 

Sprawl of keys and credentials 

Weak multi-factor authentication enforcement, registration, and visibility 022 Google Cloud Next ‘24 Proprietary 

Common Attacker TTPs  

> ●

Contact the helpdesk to reset an administrator’s credentials  

> ●

Installation of remote access tools to maintain persistence  

> ●

They creatively abuse legitimate administration tools  

> ○

Creating virtual machines within cloud environments  

> ○

Modifying firewall rules attached to virtual machines to allow direct RDP access  

> ○

Living off the land to move laterally with valid credentials (RDP, SSH, etc) 

Complete The Mission  

> ●

Data theft (Extortion)  

> ○

Mega  

> ○

Rclone  

> ○

Cloud Storage  

> ●

Ransomware Deployment 

Who they are  

> ●

Financially motivated threat cluster active since at least May 2022.  

> ●

Commonly gains initial access via stolen credentials obtained from SMS phishing operations.  

> ●

Also known as Scattered Spider (CrowdStrike) and Octo Tempest (Microsoft) 

Threat Actor Spotlight: 

# UNC3944 101 Google Cloud Next ‘24 Proprietary 

Attacker registers |organization|-helpdesk.com & |organization|-sso.com 

2

SMS-ishing Attack against users for credentials 

A non- privileged user enters credentials. Attacker uses valid token to log into Entra ID 

31

5

Password spraying attack against targeted and highly privileged admin accounts collected from Step 4 

6

Successful login and MFA registration against two accounts. Account 1 is a break glass account assigned Global Admin role in Entra ID. Account 2 is a PAM admin. 

789

Attacker registers virtual machine within Entra ID. Then logs into Defender to whitelist malware (RATs). Logs into Intune to deploy malware across fleet of endpoints. 

Logs into VPN and accesses credential-vault using compromised Account 2 (PAM admin). Retrieves Domain Admin and Vmware Root account credentials in clear-text. 

Moves laterally to on-premise AD and dumps the NTDS.dit. Then, moves to VMware Infrastructure and encrypts production ESXi Hosts. 

# Abusing Privileged Access 

Incident Response Case Study #3 

Entra ID 

Attacker logs into Entra ID and performs bulk user, group membership, and role assignment download 

4024 Google Cloud Next ‘24 Proprietary 

Identity 

Enforce Phishing-resistant Multi-Factor Authentication method(s) Develop custom detections against identity-based attacks (e.g., password spraying) 

Resources 

Review and disable default insecure configurations 

Network 

Restrict access to Tier 0 to/from Privileged Access Workstations 

Endpoints 

Restrict endpoint registration to endpoint management team(s) 

# Takeaways 025 Google Cloud Next ‘24 Proprietary 

## Personal Local Drive to AWS Ransomware 

AWS Administrator works remotely from home for a day 

AWS Administrator is in search for a new job. Receives a job offer via Email from a recruiter. Downloads job offer on personal laptop 

Creates test AWS access key and assigns Administrator role. Downloads csv with access key details and stores in local drive 

Attacker logs into AWS and executes ListBuckets commands across production AWS account 

Opening job offer on laptop executed malware, stole credentials and cookies stored on Google drive 4 months 

Attacker makes ~2000 requests to AWS API to: 

1. Downloaded all S3 Buckets and corresponding file objects 2. Delete all S3 Buckets 3. Then, created a “Ransomware” S3 Bucket 

Incident Response Case Study #4 026 Google Cloud Next ‘24 Proprietary 

Identity 

Resources 

Identify unusual operational activity Develop incident response plans & tactical playbooks/runbooks 

Endpoints 

Restrict access from managed endpoints only 

# Takeaways 

Identity 

Determine whether long-lived credentials are required Limit the scope of programmatic keys 

Keep an inventory and audit how they’re being used 027 Proprietary Google Cloud Next ‘24 

# Third Party 028 Google Cloud Next ‘24 Proprietary 

# Third Party Threat Landscape 

Client A 

Limited security enforcement for third-party access 

Lack of visibility into trusted third-party software 

Client B Client C 

Professional and Technology Service Providers 

Supply Chain Compromise Mergers and Acquisitions 

Third Party Threat Vectors 

Common cloud challenges: 

Inconsistent security configurations and integrations 029 Google Cloud Next ‘24 Proprietary 

Victim Organization On-Premise Data Center 

Cloud Environment 

Ransomware GPO propagates resulting in mass encryption across data centers and cloud environment 

Logs into a cloud-based single-factor VDI solution 

Breaks out to virtual host and disables installed EDR agent 

Moves laterally to an on-premise Domain Controller 

Creates a GPO that deploys ransomware across the domain 

4 63 5

7

Other regional data centers 

## Third Party to Cloud Compromise 

Third Party Software Service Provider 

1

Compromises third party, steals credentials, and sells them on dark web 

2

Identifies victim credentials as part of dataset 

Incident Response Case Study #5 030 Google Cloud Next ‘24 Proprietary 

Identity 

● Segment third-party accounts from organizational identity store 

● Require “Just-In-Time” access 

Resources 

● Inventory third party access and software dependencies 

● Monitor external attack surface. 

Network 

● Restrict and monitor trusted networks with access to resources and workloads 

Endpoints 

● Apply endpoint security standards to Virtual Desktops and published applications 

# Takeaways 031 Google Cloud Next ‘24 Proprietary 

# Wrap-Up 032 Google Cloud Next ‘24 Proprietary 

# Attack Surface Reduction 

Identity 

Resources 

Network 

Endpoints 

Let's talk through foundational hardening controls to reduce overall attack surface across your cloud and hybrid environments 033 Google Cloud Next ‘24 Proprietary 

# Secure Your Identities 

Continually review and reduce privileged access 

Implement just-in-time access for privileged accounts 

Segment privileged accounts 

Privileged Account Management Multi-Factor Authentication 

Enforce strong / phishing-resistant MFA methods 

Restrict and monitor MFA device self-registration and modifications 

Enhance controls for accounts that cannot use MFA 

Credential Management 

Enforce long and complex passwords 

Monitor for leaked credentials 

Identify and validate security controls for password reset self-service methods 034 Google Cloud Next ‘24 Proprietary 

# Secure Your Resources 

Implement network restrictions to restrict access to trusted locations 

Use local accounts and enforce strong MFA 

Ingest logs from trusted service infrastructure and develop custom detections 

Trusted Service Infrastructure Backup Services 

Isolate backups via identity and network segmentation 

Monitor for modifications to retention and purge policies 

Configuration Management 

Leverage infrastructure-as-code to deploy cloud resources and restrict manual modifications 

Prevent and detect resources allowing public access 

Develop remediation playbooks 035 Google Cloud Next ‘24 Proprietary 

# Secure Your Network 

Automate external unauthenticated scans of public IPs, domains, and CIDR IP ranges 

Review and remediate identified vulnerabilities 

Identify attack paths into cloud environments 

Attack Surface Remote Access 

Hunt for remote access tools through EDR, firewall logs, and asset inventory 

Restrict remote access to only required identities and enforce strong authentication 

Validate the integrity of endpoints accessing the network 

Segmentation 

Segment cloud and on-premise environments 

Enforce egress allow-listing policy for all servers and critical assets 

Align playbooks that allow for the quick segmentation and isolation of environments 036 Google Cloud Next ‘24 Proprietary 

# Secure Your Endpoints 

Disable legacy configurations allowing credential or identity exposure (e.g., WDigest) 

Detect and block endpoint credential theft methods 

Enforce unique local admin account passwords 

Identity Exposure Privileged Access 

Use Privileged Access Workstations (PAWs) for administrative tasks 

Block all privileged access except from trusted devices 

Treat device management platforms as Tier 0 

Endpoint Management 

Restrict self-enrollment capabilities 

Implement compliance policies to validate certificate installation, EDR installation, OS and patch level 

Restrict access to resources from managed and compliant devices only 037 Google Cloud Next ‘24 

Attack surface reduction requires a multi-layered approach across the layers of an organization’s managed identities, resources, networks, and endpoints Thank you 

038 Proprietary 040 Google Cloud Next ‘24 Proprietary 

# Continue your learning journey! 

Sessions 

SEC205 - Cloud security threat briefing with Mandiant 

SEC131 - Address retail security challenges with AI 

Innovators Hive Training 

IHWS201 - Investigating a Compromised GKE Service Account: Hands-on Incident Response in Google Cloud 

Demo in Showcase 

SCSEC-101 - Threat intelligence and Mandiant consulting Google Cloud Next ‘24 Proprietary 

Tap into special offers 

designed to help you 

implement what you learned at Google Cloud Next. 

Scan the code to receive personalized guidance from one of our experts. 

Or visit g.co/next/24offers 

# Ready to build what’s next?
