Title: Tales from the cloud trenches: Unwanted visitor | Datadog Security Labs

URL Source: https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/

Published Time: 2024-12-11T00:00:00Z

Markdown Content:
# Tales from the cloud trenches: Unwanted visitor | Datadog Security Labs

[Security Labs](https://securitylabs.datadoghq.com/)

*   [ARTICLES](https://securitylabs.datadoghq.com/articles/ "ARTICLES")
*   [CLOUD SECURITY ATLAS](https://securitylabs.datadoghq.com/cloud-security-atlas/ "CLOUD SECURITY ATLAS")
*   [NEWSLETTER](https://securitylabs.datadoghq.com/newsletters/ "NEWSLETTER")
*   [ABOUT](https://securitylabs.datadoghq.com/about/ "ABOUT")

*   [ARTICLES](https://securitylabs.datadoghq.com/articles/ "ARTICLES")
*   [CLOUD SECURITY ATLAS](https://securitylabs.datadoghq.com/cloud-security-atlas/ "CLOUD SECURITY ATLAS")
*   [NEWSLETTER](https://securitylabs.datadoghq.com/newsletters/ "NEWSLETTER")
*   [ABOUT](https://securitylabs.datadoghq.com/about/ "ABOUT")

research

# Tales from the cloud trenches: Unwanted visitor

December 11, 2024

*   [aws](https://securitylabs.datadoghq.com/articles/?tag=aws)
*   [threat detection](https://securitylabs.datadoghq.com/articles/?tag=threat_detection)

*   [twitter](https://twitter.com/share?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-unwanted-visitor%2F&text=Tales%20from%20the%20cloud%20trenches%3A%20Unwanted%20visitor "twitter")
*   [reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-unwanted-visitor%2F "reddit")

![Image 1: Tales From The Cloud Trenches: Unwanted Visitor](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-unwanted-visitor/hero.png?auto=format&h=712&dpr=1)

on this page

*   [Key points and observations](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#key-points-and-observations)
*   [Attacker activity](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#attacker-activity)
*   [Summary of attacker activity](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#summary-of-attacker-activity)
*   [Detection opportunities](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#detection-opportunities)
*   [How Datadog can help](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#how-datadog-can-help)
*   [Conclusion](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#conclusion)
*   [Indicators of compromise](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#indicators-of-compromise)

[![Image 2: Oren Margalit](https://securitylabs.dd-static.net/img/authors/oren_margalit.jpeg?auto=format&w=48&h=48&dpr=2&q=75) Oren Margalit Detection Engineer](https://securitylabs.datadoghq.com/articles/?author=Oren_Margalit)

Amazon Simple Email Service (SES) is a common target for attackers to send out spam or phishing emails. In this post, we explore specific techniques regarding persistence within AWS SES that we have observed used by an attacker. What made this intrusion notable was the attacker's use of an external account under their control to assume a role within the victim's environment.

## [Key points and observations](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#key-points-and-observations)

*   The attacker used an AWS account that they controlled in order to persist in the victim's environment.
*   The attacker used the VPN provider VPN Jantit to perform the activity in the victims environment.
*   The attacker used several methods to obscure their activity and used temporary credentials to create backdoors, such as new users and roles.

## [Attacker activity](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#attacker-activity)

As a result of a recent threat hunt, we observed an attacker targeting an AWS environment with a long-term access key (AKIA). The observed technique involved creating a federated session using a compromised IAM identity to gain access to the console. Tools such as [Pacu](https://github.com/RhinoSecurityLabs/pacu) and [AWS_Consoler](https://github.com/NetSPI/aws_consoler) are often utilized by attackers to generate sign-in tokens for this purpose.

[![Image 3](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-unwanted-visitor/attacker-flowchart.png?auto=format&w=800&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-unwanted-visitor/attacker-flowchart.png?auto=format)
One of the first actions was to call `GetFederationToken`. We see this action from attackers who want to convert their CLI access to console access. We often see attackers attempt to use this API call to generate temporary credentials needed to switch from CLI to console access. We believe that makes it easier for the attacker to perform other actions within the targeted AWS environment.

The name requested by the attacker can be anything, and the credentials generated are separate from the original compromised IAM identity, making it more difficult to track the attacker.

```json
"eventSource": "sts.amazonaws.com",
  "eventName": "GetFederationToken",
  "requestParameters": {
    "durationSeconds": 3600,
    "name": "admin",
    "policy": {
      "Version": "2012-10-17",
      "Statement": [{
          "Sid": "Stmt1",
          "Effect": "Allow",
          "Action": "*",
          "Resource": "*"}]}},
  "useragent": "Boto3/1.35.70 md/Botocore#1.35.70 ua/2.0 os/windows#11 md/arch#amd64 lang/python#3.12.6 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.35.70"
```

The attacker then generated an AWS Console sign-in link using GetSigninToken

```json
"eventSource":"signin.amazonaws.com",
"eventName":"GetSigninToken",
"additionalEventData":{"MobileVersion":"No","MFAUsed":"No"},
"useragent":"Python-urllib/3.12"
```

```json
"eventSource":"signin.amazonaws.com",
"eventName":"ConsoleLogin",
"eventType":"AwsConsoleSignIn",
"additionalEventData":{"MobileVersion":"No","MFAUsed":"No"},
"useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
"arn":"arn:aws:sts::redacted:federated-user/admin"
```

To help avoid detection, the attacker used their console access to create a new role named `SupportAWS`.This shows the attacker using names that look legitimate to avoid detections. They then attached a policy to that role that allows them to assume it from an attacker-controlled account `713521355166`. This persistence mechanism, while uncommon, has been covered previously in a [blog](https://www.invictus-ir.com/news/the-curious-case-of-dangerdev-protonmail-me) by Invictus IR.

```json
"eventName": "CreateRole",
  "eventSource": "iam.amazonaws.com",
  "requestParameters": {
    "assumeRolePolicyDocument": {
      "Version": "2012-10-17",
      "Statement": [{
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Principal": {
            "AWS": "713521355166"},
          "Condition": {}}]},
    "roleName": "SupportAWS",
    "description": ""},
  "arn": "arn:aws:sts::redacted:federated-user/admin"
```

Following this, the attacker attached the policy `AdministratorAccess` to the `AWSSupport` role. This ensures the role will have the requisite privileges to achieve the attacker’s objectives.

```json
"eventName":"AttachRolePolicy"
"eventSource":"iam.amazonaws.com"
"requestParameters":{
    "policyArn":"arn:aws:iam::aws:policy/AdministratorAccess",
    "roleName":"SupportAWS"}
"arn":"arn:aws:sts::redacted:federated-user/admin"
```

The attacker then assumed the role via the `713521355166` account, authenticated as an IAM user named`adminprod`. This action appeared to take place in the console, generating API calls like `SwitchRole` and `AssumeRole`.

```json
"eventName":"SwitchRole",
"eventSource":"signin.amazonaws.com",
"additionalEventData":{
    "SwitchFrom":"arn:aws:iam::713521355166:user/adminprod",
    "RedirectTo":"https://us-east-1.console.aws.amazon.com/console/home?nc2=h_ct&region=X&src=header-signin#"},
```

With access to the `SupportAWS` role, the attacker focused on creating another layer of persistence by creating an IAMuser, `supdev`, with a login profile that had the [AdministratorAccess policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html) attached.

```json
"eventName":"CreateUser",
"eventSource":"iam.amazonaws.com",
"arn":"arn:aws:sts::redacted:assumed-role/SupportAWS/adminprod",
"requestParameters":{
    "userName":"supdev"}
```

```json
"eventName":"CreateLoginProfile",
"eventSource":"iam.amazonaws.com",
"arn":"arn:aws:sts::redacted:assumed-role/SupportAWS/adminprod",
"requestParameters":{
    "userName":"supdev",
    "passwordResetRequired":true}
```

```json
"eventName":"AttachUserPolicy",
"eventSource":"iam.amazonaws.com",
"arn":"arn:aws:sts::redacted:assumed-role/SupportAWS/adminprod",
"requestParameters":{
    "policyArn":"arn:aws:iam::aws:policy/AdministratorAccess",
    "userName":"supdev"}
```

The attacker then pivoted to the user `supdev`, accessing the console twice from two different regions in a short time period.

```json
"eventSource":"signin.amazonaws.com",
"eventName":"ConsoleLogin",
"eventType":"AwsConsoleSignIn",
"additionalEventData":{"MobileVersion":"No","MFAUsed":"No"},
"useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
"arn":"arn:aws:iam::redacted:user/supdev"
```

Based on the API calls we observed, the attacker navigated to the AWS SES service, potentially checking the capabilities of the SES service in the victim’s AWS account, like whether it was in a sandbox, had configured sending limits, etc.

There were no actions following this to indicate that the attacker sent any spam or phishing emails. We suspect that either the attacker would have potentially returned at a later date to perform actions upon objectives, or they were planning on reselling this access to other actors in the market for an AWS SES account capable of sending out mass spam or phishing emails.

The following day we observed the same IP attempting the `GetAccount` API call across multiple regions from the original long-term access key. This indicated the use of automated tooling on the behalf of the attacker.

AWS SES enumeration API calls used:

*   GetAccount
*   ListEmailIdentities
*   ListIdentities
*   GetSendQuota

## [Summary of attacker activity](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#summary-of-attacker-activity)

TA0007 - Discovery

*   [T1580 - Cloud Infrastructure Discovery](https://attack.mitre.org/techniques/T1580/)
*   [T1619 - Cloud Storage Object Discovery](https://attack.mitre.org/techniques/T1619)

TA0003 - Persistence

*   [T1098.001- Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001/)
*   [T1098.003- Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003/)

TA0005 - Defense Evasion

*   [T1078.004 - Valid Accounts](https://attack.mitre.org/techniques/T1078/004/)

## [Detection opportunities](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#detection-opportunities)

This intrusion had a heavy focus on persistence and privilege escalation. Here are some suggestions to help to identify this type of activity:

*   Identify creation/modification actions of a login profile.
*   Identify the attachment of the managed policy `arn:aws:iam::aws:policy/AdministratorAccess`.
*   Identify multiple console logins from different networks in a short period of time. 
    *   You could also look at authentications from multiple regions.

*   Identify attempts to enumerate AWS SES settings and configurations. 
    *   Activity from a long-term access key is generally rare.

*   Identify the creation of a new role that allows assuming it from a different account.
*   Identify unusual assumed roles from external AWS accounts.
*   Identify `GetFederationToken` API calls with a high privilege policy attached.

All of these detection ideas should be assessed within the context of your environment.

All of these detection ideas should be assessed within the context of your environment.

 You can use [Stratus Red Team](https://github.com/DataDog/stratus-red-team/) to reproduce attack techniques used by this attacker, including:

*   [Create an administrative IAM User](https://stratus-red-team.cloud/attack-techniques/AWS/aws.persistence.iam-create-admin-user/)
*   [Create a backdoored IAM Role](https://stratus-red-team.cloud/attack-techniques/AWS/aws.persistence.iam-create-backdoor-role/)
*   [Generate temporary AWS credentials using GetFederationToken](https://stratus-red-team.cloud/attack-techniques/AWS/aws.persistence.sts-federation-token/)
*   [Create a Login Profile on an IAM User](https://stratus-red-team.cloud/attack-techniques/AWS/aws.persistence.iam-create-user-login-profile/)
*   [Enumerate SES](https://stratus-red-team.cloud/attack-techniques/AWS/aws.discovery.ses-enumerate/)

## [How Datadog can help](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#how-datadog-can-help)

Datadog [Cloud SIEM](https://www.datadoghq.com/product/cloud-siem/) and [Cloud Security Management (CSM)](https://www.datadoghq.com/product/cloud-security-management/) come with the following out-of-the-box rules to identify suspicious activity relevant to these attacks in an AWS environment. The Cloud SIEM rules help identify potential threats, while the CSM rules help identify overprivileged identities.

*   [AWS SES discovery attempt by long-term access key](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-ses-quota-discovery-long-term-access-key/)
*   [Possible privilege escalation via AWS login profile manipulation](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-iam-login-profile-manipulated/)
*   [Temporary AWS security credentials generated for user](https://docs.datadoghq.com/security/default_rules/aws-cloudtrail-federation-token-generation/)
*   [AWS IAM AdministratorAccess policy was applied to a user](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-iam-apply-privilegedpolicy-to-user/)
*   [New AWS account seen assuming a role into AWS account](https://docs.datadoghq.com/security/default_rules/aws-iam-new-aws-account-assumerole/)
*   [AWS ConsoleLogin without MFA triggered Impossible Travel scenario](https://docs.datadoghq.com/security/default_rules/aws-cloudtrail-console-logins-impossible-travel-no-mfa/)
*   [IAM users should not have both Console access and Access Keys](https://docs.datadoghq.com/security/default_rules/aws-iam-user-iam-users-should-not-have-both-console-access-and-access-keys/)
*   [IAM users should not have the 'AdministratorAccess' policy attached](https://docs.datadoghq.com/security/default_rules/aws-iam-user-iam-users-should-not-have-the-administratoraccess-policy-attached/)
*   [Multi-factor authentication should be enabled for all IAM users with console access](https://docs.datadoghq.com/security/default_rules/hsh-y5w-hxe/)

## [Conclusion](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#conclusion)

What made this intrusion notable was the attacker’s use of an external account under their control to assume a role within the victim's environment. Typically, intrusions involving AWS SES begin with long-term access keys and are confined to entities within the compromised account. However, leveraging a role assumed from outside the organization demonstrates that attackers are evolving their tactics to evade detection. While the persistence behaviors observed were not entirely new, they were unique due to the combination of temporary credentials, the creation of a new user and role, and the continued use of the initially compromised identity.

## [Indicators of compromise](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-unwanted-visitor/#indicators-of-compromise)

IP Address used

```
116.251.217[.]107  
203.78.112[.]7  
203.78.112[.]220  
203.78.113[.]126  
203.78.112[.]196  
108.174.195[.]216  
203.78.112[.]110  
140.213.191[.]20  
203.78.112[.]171  
140.213.52[.]53  
203.78.113[.]72  
140.213.52[.]15  
203.78.113[.]195
```

Attacker AWS account:

```
713521355166
```

Created user names:

```
supdev
```

Created role name:

```
SupportAWS
```

*   [twitter](https://twitter.com/share?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-unwanted-visitor%2F&text=Tales%20from%20the%20cloud%20trenches%3A%20Unwanted%20visitor "twitter")
*   [reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-unwanted-visitor%2F "reddit")

## Did you find this article helpful?

## Subscribe to the Datadog Security Digest

Get the latest insights from the cloud security community and Security Labs posts, delivered to your inbox monthly. No spam.

Email* 

By submitting this form, you agree to the[Privacy Policy](https://www.datadoghq.com/legal/privacy/)and[Cookie Policy](https://www.datadoghq.com/legal/cookies/)

SUBMIT

### Thank you for subscribing!

## Related Content

[![Image 4: Hidden in Plain Sight: Abusing Entra ID Administrative Units for Sticky Persistence](https://securitylabs.dd-static.net/img/abusing-entra-id-administrative-units/hero.jpg?auto=format&w=447&dpr=1) research Hidden in Plain Sight: Abusing Entra ID Administrative Units for Sticky Persistence](https://securitylabs.datadoghq.com/articles/abusing-entra-id-administrative-units/)[![Image 5: Amplified exposure: How AWS flaws made Amplify IAM roles vulnerable to takeover](https://securitylabs.dd-static.net/img/amplified-exposure-how-aws-flaws-made-amplify-iam-roles-vulnerable-to-takeover/amplified-exposure-hero.png?auto=format&w=447&dpr=1) research Amplified exposure: How AWS flaws made Amplify IAM roles vulnerable to takeover](https://securitylabs.datadoghq.com/articles/amplified-exposure-how-aws-flaws-made-amplify-iam-roles-vulnerable-to-takeover/)[![Image 6: An analysis of a TeamTNT doppelgänger](https://securitylabs.dd-static.net/img/emergingthreats_hero_globe.png?auto=format&w=447&dpr=1) research An analysis of a TeamTNT doppelgänger](https://securitylabs.datadoghq.com/articles/analysis-of-teamtnt-doppelganger/)[![Image 7: A confused deputy vulnerability in AWS AppSync](https://securitylabs.dd-static.net/img/appsync-vulnerability-disclosure/hero.png?auto=format&w=447&dpr=1) research A confused deputy vulnerability in AWS AppSync](https://securitylabs.datadoghq.com/articles/appsync-vulnerability-disclosure/)

## work with us

We're always looking for talented people to collaborate with

featured positions

*   [Engineering Manager - Security Incident Response (EMEA) Security - Engineering](https://careers.datadoghq.com/detail/7339331/?gh_jid=7339331)
*   [Manager I, Engineering - Platform Trust & Safety Security - Engineering](https://careers.datadoghq.com/detail/7646952/?gh_jid=7646952)
*   [Engineering Manager I, Core Observability, Paris Security - Engineering](https://careers.datadoghq.com/detail/7727662/?gh_jid=7727662)
*   [Manager I, Security Engineering - Vulnerability Management Security - Engineering](https://careers.datadoghq.com/detail/7748975/?gh_jid=7748975)
*   [Senior Security Engineer, Security Incident Response Team (SIRT) Security - Engineering](https://careers.datadoghq.com/detail/7761259/?gh_jid=7761259)
*   [Staff Application Security Engineer Security - Engineering](https://careers.datadoghq.com/detail/7777798/?gh_jid=7777798)

We have 8 positions

[view all](https://careers.datadoghq.com/all-jobs/?parent_department_Engineering%5B0%5D=Engineering&child_department_Engineering%5B0%5D=Global%20Information%20Security)

© Datadog 2026

*   [TERMS](https://www.datadoghq.com/legal/terms/ "TERMS")
*   [PRIVACY](https://www.datadoghq.com/legal/privacy/ "PRIVACY")
*   [COOKIES](https://www.datadoghq.com/legal/cookies/ "COOKIES")

*   [twitter](https://www.twitter.com/datadoghq/ "twitter")
*   [rss](https://securitylabs.datadoghq.com/rss/feed.xml "rss")