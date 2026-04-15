Title: "Securing a SaaS Company's AWS Environment After a Breach"

URL Source: https://badshah.io/case-studies/saas-aws-breach/

Published Time: 2025-04-15T00:00:00+05:30

Markdown Content:
# Securing a SaaS Company's AWS Environment After a Breach | Chandrapal Badshah

[![Image 1: Chandrapal Badshah](https://badshah.io/images/logo2.png)](https://badshah.io/)

[](https://badshah.io/case-studies/saas-aws-breach/#)[](https://badshah.io/case-studies/saas-aws-breach/#)

*   [H o m e](https://badshah.io//)
*   [B l o g](https://badshah.io//blog)
*   [C a s e S t u d i e s](https://badshah.io//case-studies)
*   [T a l k s](https://badshah.io//talks)
*   [T r a i n i n g s](https://badshah.io//trainings)
*   [F r e e b i e s](https://badshah.io//freebies)
*   [C o n t a c t](https://badshah.io//#contact-section)

[](https://www.linkedin.com/in/bnchandrapal "LinkedIn")[](https://github.com/0xbadshah "GitHub")[](https://www.youtube.com/@CloudSecurityClub "YouTube")[](https://cloudsecurity.club/ "Newsletter")

# Securing a SaaS Company's AWS Environment After a Breach

A growing SaaS company contacted me after a serious AWS breach. The attacker accessed staging and production accounts with administrator privileges and caused significant damage:

*   Compromised databases
*   Critical resources and backups deleted
*   Data exfiltration

By the time the CTO called me in, DevOps team contained the breach.

The team recreated resources in a new AWS account. But significant damage was done - production disrupted for a week (in simple terms, no revenue), 1000+ developer hours gone and data exfiltrated.

While the company contained the breach, they needed help to identify the root cause and prevent similar incidents in future.

The company had _frustrating_ experiences with cloud auditing companies for Cloud Incident Response, which led them to contact me through my [discovery call page](https://topmate.io/chandrapal) for an independent review of the incident’s root cause.

### What led to this incident?

After analyzing CloudTrail logs the attacker’s initial entry to cloud environment was evident - Leaked access keys belonging to IAM user with excessive IAM permissions (`AdministratorAccess`).

A few other architectural issues made it difficult to detect, contain, and investigate the incident:

*   All production resources (EC2 machines, backups, etc.) were in a single account.
*   The production account was also the AWS Organization’s management account.
*   Not all crucial logs were enabled, like VPC flow logs. The enabled ones, like CloudTrail management and data logs, were sent to an S3 bucket in the same production account.
*   CI/CD systems used production IAM user credentials to deploy, but the CI/CD system was hosted in a non-production account (with lenient access control).
*   All RDS databases were on public subnets with public IPs, and access was controlled using security groups.

Two significant issues in the people & process part were:

*   IAM credentials for applications were shared among team members.
*   All developers’ SSH keys were added to the same Linux user. Their SSH sessions and executed commands were not recorded.

Due to the above architectural and process issues combined with an IAM key leak with AdministratorAccess privileges, the attacker had access to nearly everything and can laterally move from staging to production account.

**Note:** These issues contributed to the breach once the attacker got access to hardcoded credentials. The SaaS company also had security best practices implemented, such as using AWS Identity Center for developer login, and enabled GuardDuty, SecurityHub, and Config.

### Attacker Tactics

After investigating the incident, I found the following tactics used by attackers:

*   Used VPN IP addresses to hide their origin
*   Used custom scripts to enumerate all resources across all regions
*   Modified database security groups to allow ingress from their VPN IPs
*   Reset master RDS database passwords for access
*   Exfiltrated S3 bucket content using S3 Sync command
*   Stopped CloudTrail and deleted logs from the CloudTrail bucket
*   Found Deletion Protection on resources (EC2, RDS, etc), turned off the setting and then deleted the resources

### How Better Security Controls Could Have Hindered the Attacker

The leak of a privileged IAM user’s key was the entry point to the cloud account, but the breach’s impact also lies on cloud architecture.

Few security measures that could have prevented certain attacker tactics and/or reduced the breach’s impact are:

*   **Don’t attach Administrator policy to any IAM user** - The path to least privilege in cloud (for any company with few years of cloud presence) begins with identifying most risky IAM entities and cutting down permissions to the most necessary ones while preventing creation of new risky IAM entities. Tools like [Cloudsplaining](https://github.com/salesforce/cloudsplaining) can be a good start.
*   **Use multi-accounts instead of ABAC on a single account to isolate resources** - A single account is operationally easier to manage. However, segregating prod and non-prod resources (especially S3, Route53 Zones, IAM, etc) is tricky. Implementing and maintaining an effective ABAC is more challenging than account level segregation. Use [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) service to manage multiple accounts.
*   **Create a [CloudTrail Org Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) instead of individual trails** - This trail saves logs from all AWS accounts to a single S3 bucket in an account designated for storing logs. 
    *   **Enable [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) on logging buckets** - This prevents log tampering and deletion, even by privileged users. Use a suitable S3 Object Lock mode for your requirements.

*   **Enable VPC flow, CloudTrail, and S3 logs** - Logs help identify attack patterns and evaluate incident blast radius. Without logs, it’s impossible to prove or disprove any hypothesis. S3 logs are expensive, so enable them for critical buckets.
*   **Backups and logs should be sent to different AWS accounts** - These resources help investigate and recover from incidents and must not be stored in accounts where incidents are anticipated.
*   **Use SCPs & RCPs to prevent sensitive actions and setup trusted perimeter** - [SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) help prevent attacker tactics like deleting critical buckets, modifying or stopping CloudTrail, etc. [RCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) help prevent unknown accounts from assuming (backdoored) IAM roles and circumventing SCPs using attacker-controlled AWS accounts. 
    *   **Don’t host anything on the AWS Org management account** - [SCPs and RCPs don’t apply on management accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html). Also, setup delegated admin to child accounts and reduce management account logins.

*   **Implement external solution for SSH access** - Open Source tools like [Teleport](https://goteleport.com/) grant SSH access to EC2s and offer functionality like saving all sessions and commands executed by users.
*   (Optional, from my experience) **Don’t host databases on public subnets with public IPs** - Security groups can control network access to databases and EC2 instances with public IPs, but if developers change them directly from the Console, it’s easy to misconfigure and expose to unintended CIDR ranges. If it’s not possible to migrate an existing DB from public to private, implement detection on changes to important security groups.

A report with detailed analysis of incident, the contributing factors, root cause and pragmatic security controls like the above was shared with the client.

Additionally, a _customized 90-day action plan_ was shared to help prevent similar breaches in the future and strengthen their AWS security.

### Notes to Security Teams

**GuardDuty failed to detect C&C servers:** I found a few IPs from CloudTrail Event Logs which executed sensitive actions such as DeleteTrail. GuardDuty raised a Low Severity alert about the CloudTrail being stopped. However, it never alerted about those IPs. [VirusTotal](https://www.virustotal.com/gui/) and [Abuse.ch](https://hunting.abuse.ch/) listed them as known C&C servers. If you have enabled GuardDuty, maintain your [own threat list](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html) to get notified about traffic to C&C servers.

**Scraping CloudTrail Events History could take a lot of time:** Even though CloudTrail logs can be deleted in S3 bucket, the CloudTrail management events of last 90 days is available under [CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). But there’s a catch - there’s a [ratelimit for `LookupEvents`](https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail) - 2 API requests per second per region. Each API request to `LookupEvents` fetches 50 events. If you have millions of CloudTrail events, downloading them takes considerable time before investigation. So, always protect your CloudTrail logs in S3 buckets and make it harder to tamper them. Download logs from Event History in worst case scenario.

* * *

What’s most concerning in the post-analysis of this breach?

This breach occurred despite the company having implemented several AWS security best practices – including AWS Identity Center, GuardDuty, SecurityHub, and Config.

(However, I need to mention they were not properly configured.)

Is your cloud environment hiding similar risks?

Are you sure the cloud security controls are properly setup?

Don’t wait for a catastrophic breach to find out.

**Schedule a [discovery call](https://topmate.io/chandrapal) today!** I’ll help to:

*   find cloud architectural security issues unique to your environment
*   detect exploitable misconfigurations
*   implement effective cloud security controls

so you don’t end up facing similar breach in your company.

[](https://www.linkedin.com/in/bnchandrapal "LinkedIn")[](https://github.com/0xbadshah "GitHub")[](https://www.youtube.com/@CloudSecurityClub "YouTube")[](https://cloudsecurity.club/ "Newsletter")

 © 2026 **Chandrapal Badshah**. All rights reserved