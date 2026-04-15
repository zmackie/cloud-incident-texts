Title: Tales from the cloud trenches: The Attacker doth persist too much, methinks | Datadog Security Labs

URL Source: https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/

Published Time: 2025-05-13T00:00:00Z

Markdown Content:
# Tales from the cloud trenches: The Attacker doth persist too much, methinks | Datadog Security Labs

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

# Tales from the cloud trenches: The Attacker doth persist too much, methinks

May 13, 2025

*   [aws](https://securitylabs.datadoghq.com/articles/?tag=aws)
*   [threat detection](https://securitylabs.datadoghq.com/articles/?tag=threat_detection)

*   [twitter](https://twitter.com/share?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-the-attacker-doth-persist-too-much%2F&text=Tales%20from%20the%20cloud%20trenches%3A%20The%20Attacker%20doth%20persist%20too%20much%2C%20methinks "twitter")
*   [reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-the-attacker-doth-persist-too-much%2F "reddit")

![Image 1: Tales From The Cloud Trenches: The Attacker Doth Persist Too Much, Methinks](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/hero.png?auto=format&h=712&dpr=1)

on this page

*   [Key points and observations](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#key-points-and-observations)
*   [Routine attacker tactics](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#routine-attacker-tactics)
*   [Notable tactics](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#notable-tactics)
    *   [Persistence as a service with API Gateways and Lamba function](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#persistence-as-a-service-with-api-gateways-and-lamba-function)
    *   [ConsoleLogin events from Telegram IP addresses](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#consolelogin-events-from-telegram-ip-addresses)
    *   [Disabling trusted access for organization-level services](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#disabling-trusted-access-for-organization-level-services)
    *   [Persistence through AWS Identity Center (AWS SSO)](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#persistence-through-aws-identity-center-aws-sso)

*   [Summary of attacker activity](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#summary-of-attacker-activity)
*   [Detection opportunities](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#detection-opportunities)
*   [How Datadog can help](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#how-datadog-can-help)
*   [Indicators of compromise](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#indicators-of-compromise)

[![Image 2: Martin McCloskey](https://securitylabs.dd-static.net/img/authors/martin_mccloskey.png?auto=format&w=48&h=48&dpr=2&q=75) Martin McCloskey Senior Detection Engineer](https://securitylabs.datadoghq.com/articles/?author=Martin_McCloskey)

As a result of a recent threat hunt, we observed attacker activity originating from a leaked long-term AWS access key (`AKIA*`). Within a 150-minute period, we detected five distinct IP addresses attempting to leverage this access key to perform malicious techniques, tactics, and procedures (TTPs). This post presents several techniques that, to our knowledge, have never been reported in the wild.

## [Key points and observations](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#key-points-and-observations)

*   A long-term AWS access key associated with an IAM user in an AWS organization management account was exposed.
*   We observed follow-up activity from this access key for a number of tactics, including both common and innovative ones.
*   Previously unreported tactics involve creating "persistence-as-a-service" infrastructure, creating AWS Identity Center users, and disabling organization-level services.

## [Routine attacker tactics](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#routine-attacker-tactics)

We observed several tactics that attackers commonly [use in cloud intrusions](https://securitylabs.datadoghq.com/articles/?s=tales%20from%20the%20trenches). We list them below for the sake of completeness but don't analyze them in further detail:

*   [SES enumeration](https://securitylabs.datadoghq.com/cloud-security-atlas/attacks/using-ses-to-send-spam/) through API calls such as [GetAccount](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetAccount.html), [ListIdentities](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentities.html), and [GetSendQuota](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendQuota.html).
*   [Attempt to create an EC2 security group](https://securitylabs.datadoghq.com/articles/following-attackers-trail-in-aws-methodology-findings-in-the-wild/#creating-security-groups) called `Administratorsz` with the description `We Are There But Not Visible`, which has been [attributed](https://unit42.paloaltonetworks.com/javaghost-cloud-phishing/) to the JavaGhost group.
*   [Creation of several IAM users](https://securitylabs.datadoghq.com/cloud-security-atlas/attacks/creating-new-iam-user/), subsequently granted administrative permissions either directly through `AttachUserPolicy` or indirectly through `AttachGroupPolicy`. The attacker sometimes attempted to [create a login profile](https://stratus-red-team.cloud/attack-techniques/AWS/aws.persistence.iam-create-user-login-profile/) on the IAM user to facilitate using the AWS console.
*   [Generating temporary STS credentials from long-lived access keys](https://stratus-red-team.cloud/attack-techniques/AWS/aws.persistence.sts-federation-token/), which allows an attacker to authenticate to the AWS console even from long-lived credentials.

## [Notable tactics](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#notable-tactics)

Besides the common techniques listed above, we observed new tactics that have never been reported before (to the best of our knowledge).

### [Persistence as a service with API Gateways and Lamba function](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#persistence-as-a-service-with-api-gateways-and-lamba-function)

In one case, the attacker created a Lambda function named `buckets555` and attached its execution role to a new policy `AWSLambdaBasicExecutionRole-b69e3024-5a7f-4fff-a576-cf54fc986b93`. They then created an HTTP API Gateway, and a Lambda function trigger so the function would automatically get invoked when an HTTP request to a specific URL is sent. We later determined that this Lambda function ran code with the capability to create IAM users dynamically, on demand.

This effectively creates a "persistence-as-a-service" mechanism: The attacker, even after the compromised credentials are revoked, is able to perform external HTTP requests to the API Gateway and dynamically create further malicious IAM users.

[![Image 3](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/backdoor-as-a-service.png?auto=format&w=800&dpr=1.75)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/backdoor-as-a-service.png?auto=format)
### [ConsoleLogin events from Telegram IP addresses](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#consolelogin-events-from-telegram-ip-addresses)

As part of this attack, we identified several `ConsoleLogin` events in a short amount of time from the IP address `149.154.161[.]235`, which belongs to the ASN `Telegram Messenger Inc`. This indicates that part of the attacker's operations are based on Telegram.

At first sight, it may seem unusual that the ConsoleLogin events themselves would originate from the Telegram IP space. We believe that after compromising long-lived credentials, the attacker may have a Telegram bot automatically generating sign-in URLs for the AWS console. The Telegram preview service would then follow this link and generate ConsoleLogin events.

### [Disabling trusted access for organization-level services](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#disabling-trusted-access-for-organization-level-services)

In one case, the attacker authenticated to the AWS Console and navigated to the **Services** tab under the AWS Organizations service and began to disable the integration of six AWS services.

[![Image 4](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/aws-console.png?auto=format&w=800&dpr=1.75)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/aws-console.png?auto=format)
In CloudTrail, this is recorded with the API call [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html). The attacker disabled [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) for the following services:

*   `access-analyzer.amazonaws.com` (IAM Access Analyzer)
*   `account.amazonaws.com and am.amazonaws.com` (AWS Account Management)
*   `member.org.stacksets.cloudformation.amazonaws.com` (CloudFormation StackSets)
*   `ssm.amazonaws.com` (AWS Systems Manager)
*   `tagpolicies.tag.amazonaws.com` (Tag Policies)

We were unable to discern what the attacker’s intent was with this action, as this only affects new AWS accounts, and the order in which the attacker disabled these services is the way they are presented in the AWS console. One theory is that the attacker intended to eventually add a new AWS account to the organization, which may have allowed them to evade some security controls so they could act on their objective.

### [Persistence through AWS Identity Center (AWS SSO)](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#persistence-through-aws-identity-center-aws-sso)

AWS Identity Center is a cloud-based identity and access management solution that enables centralized user access control across AWS accounts and integrated applications. Actions taken in Identity Center require access to an organization’s management AWS account.

We observed the attacker enumerating the SSO instance to look at SSO configurations, users, groups, and applications. Afterward, they created a group called `secure` and a user called `Secret`, which the attacker added to their group, and assigned a new permission set to that group.

Following this, the attacker updated two configuration options within the SSO instance. First, they modified the [MFA configuration](https://docs.aws.amazon.com/singlesignon/latest/userguide/mfa-getting-started.html) of the SSO instance to allow themselves to sign in without MFA. They then extended the session duration for [Amazon Q Developer](https://docs.aws.amazon.com/singlesignon/latest/userguide/90-day-extended-session-duration.html) to 90 days, indicating a likely intent to leverage this service in the future.

Later, we observed a successful [sign-in event](https://docs.aws.amazon.com/singlesignon/latest/userguide/understanding-sign-in-events.html) associated with a password-only sign-in flow for the newly created user `Secret`.

## [Summary of attacker activity](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#summary-of-attacker-activity)

TA0001 - Initial Access

 - [T1078.004 - Valid Accounts](https://attack.mitre.org/techniques/T1078/004/)

TA0007 - Discovery

 - [T1078.004 - Valid Accounts](https://attack.mitre.org/techniques/T1078/004/)

 - [T1526 - Cloud Service Discovery](https://attack.mitre.org/techniques/T1526/)

TA0003 - Persistence

 - [T1098.001- Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001/)

 - [T1098.003- Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003/)

 - [T1036.003 - Cloud Account](https://attack.mitre.org/techniques/T1136/003/)

TA0006 - Credential Access

 - [T1556.006 - Multi-Factor Authentication](https://attack.mitre.org/techniques/T1556/006/)

TA0040 - Impact

 - [T1485 - Data Destruction](https://attack.mitre.org/techniques/T1485/)

## [Detection opportunities](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#detection-opportunities)

Here are some suggestions to help to identify this type of activity:

*   Identify creation/modification actions of a login profile.
*   Identify the attachment of the managed policy `arn:aws:iam::aws:policy/AdministratorAccess` and `arn:aws:iam::aws:policy/AmazonSESFullAccess`.
*   Identify unusual console logins from unexpected networks like Telegram.
*   Identify attempts to enumerate AWS SES settings and configurations.
*   Activity from a long-term access key is generally rare.
*   Identify attempts to create a new IAM user from Lambda.
*   The user agent will contain the string `exec-env/AWS_Lambda`.
*   Identify updates to your AWS IAM Identity Center configuration.
*   Look for changes to MFA settings `requestParameters.configurationType:APP_AUTHENTICATION_CONFIGURATION`.
*   Identify `GetFederationToken` API calls with a highly privileged policy attached.
*   Identify `DisableAWSServiceAccess` API calls disabling the integration of AWS services.
*   Identify the deletion of a high number of Lambda functions.
*   Identify EC2 security group creations with the name `Java_Ghost` or description `We Are There But Not Visible`.

All of these detection ideas should be assessed within the context of your environment.

## [How Datadog can help](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#how-datadog-can-help)

Datadog [Cloud SIEM](https://www.datadoghq.com/product/cloud-siem/) and [Cloud Security Management (CSM)](https://www.datadoghq.com/product/cloud-security-management/) come with the following out-of-the-box rules to identify suspicious activity relevant to these attacks in an AWS environment. The Cloud SIEM rules help identify potential threats, while the CSM rules help identify overprivileged identities. [Long-lived access keys](https://www.datadoghq.com/state-of-cloud-security/#1) tend to carry a higher risk of being associated with a compromise.

*   [AWS SES discovery attempt by long-term access key](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-ses-quota-discovery-long-term-access-key/)
*   [Possible privilege escalation via AWS login profile manipulation](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-iam-login-profile-manipulated/)
*   [AWS IAM Identity Center SSO configuration updated](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-sso-update-configuration/)
*   [Anomalous number of AWS Lambda functions deleted](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-lambda-anomalous-deletion-of-lambda-functions/)
*   [Temporary AWS security credentials generated for user](https://docs.datadoghq.com/security/default_rules/aws-cloudtrail-federation-token-generation/)
*   [AWS IAM AdministratorAccess policy was applied to a user](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-iam-apply-privilegedpolicy-to-user/)
*   [AWS console login without MFA](https://docs.datadoghq.com/security/default_rules/aws-cloudtrail-console-login-no-mfa/)
*   [AWS Java_Ghost security group creation attempt](https://docs.datadoghq.com/security/default_rules/cloudtrail-create-security-group-java-ghost/)
*   [AWS IAM AmazonSESFullAccess policy was applied to a user](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-iam-apply-sesfullaccess-to-user/)
*   [AWS IAM AdministratorAccess policy was applied to a group](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-iam-apply-privilegedpolicy-to-group/)
*   [AWS IAM User created with AdministratorAccess policy attached](https://docs.datadoghq.com/security/default_rules/cloudtrail-createuser-then-attach-admin-policy/)
*   [Amazon SES enumeration attempt by previously unseen user](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-ses-enumerated/)
*   [IAM users should not have both Console access and Access Keys](https://docs.datadoghq.com/security/default_rules/aws-iam-user-iam-users-should-not-have-both-console-access-and-access-keys/)
*   [IAM users should not have the 'AdministratorAccess' policy attached](https://docs.datadoghq.com/security/default_rules/aws-iam-user-iam-users-should-not-have-the-administratoraccess-policy-attached/)
*   [Multi-factor authentication should be enabled for all IAM users with console access](https://docs.datadoghq.com/security/default_rules/hsh-y5w-hxe/)

## [Indicators of compromise](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/#indicators-of-compromise)

IP Addresses used

```
129.146.24[.]173
134.199.148[.]132
103.131.213[.]89
80.85.141[.]238
54.95.125[.]167
149.154.161[.]235
103.131.213[.]89
182.185.156[.]45
```

Created IAM user names:

```
adminslabs
buckets488
s3s684
git-lab965
git-lab555
```

Created IAM role names:

```
LambdaExecutionRole
buckets555-role-c6s4hhdi
curdfunctionsme-role-zw1zxamc
```

Created IAM group name:

```
Administrators
```

Created Lambda function names:

```
buckets555
curdfunctionsme
```

Lambda function SHA256:

```
HAPq9EReJVEC5gLavtc/gyd5vZtd9eiUGF932t0jBxY= (1c03eaf4445e255102e602dabed73f832779bd9b5df5e894185f77dadd230716)
HXGHpm9uGbfTRsBh2YwHKSlF5xxwrAggliHsuoD3OGY= (1d7187a66f6e19b7d346c061d98c07292945e71c70ac08209621ecba80f73866)
```

Created IAM Identity Center user name:

```
Secret
```

Created IAM Identity Center group name:

```
secure
```

*   [twitter](https://twitter.com/share?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-the-attacker-doth-persist-too-much%2F&text=Tales%20from%20the%20cloud%20trenches%3A%20The%20Attacker%20doth%20persist%20too%20much%2C%20methinks "twitter")
*   [reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-the-attacker-doth-persist-too-much%2F "reddit")

## Did you find this article helpful?

## Subscribe to the Datadog Security Digest

Get the latest insights from the cloud security community and Security Labs posts, delivered to your inbox monthly. No spam.

Email* 

By submitting this form, you agree to the[Privacy Policy](https://www.datadoghq.com/legal/privacy/)and[Cookie Policy](https://www.datadoghq.com/legal/cookies/)

SUBMIT

### Thank you for subscribing!

## Related Content

[![Image 5: Hidden in Plain Sight: Abusing Entra ID Administrative Units for Sticky Persistence](https://securitylabs.dd-static.net/img/abusing-entra-id-administrative-units/hero.jpg?auto=format&w=447&dpr=1) research Hidden in Plain Sight: Abusing Entra ID Administrative Units for Sticky Persistence](https://securitylabs.datadoghq.com/articles/abusing-entra-id-administrative-units/)[![Image 6: Amplified exposure: How AWS flaws made Amplify IAM roles vulnerable to takeover](https://securitylabs.dd-static.net/img/amplified-exposure-how-aws-flaws-made-amplify-iam-roles-vulnerable-to-takeover/amplified-exposure-hero.png?auto=format&w=447&dpr=1) research Amplified exposure: How AWS flaws made Amplify IAM roles vulnerable to takeover](https://securitylabs.datadoghq.com/articles/amplified-exposure-how-aws-flaws-made-amplify-iam-roles-vulnerable-to-takeover/)[![Image 7: An analysis of a TeamTNT doppelgänger](https://securitylabs.dd-static.net/img/emergingthreats_hero_globe.png?auto=format&w=447&dpr=1) research An analysis of a TeamTNT doppelgänger](https://securitylabs.datadoghq.com/articles/analysis-of-teamtnt-doppelganger/)[![Image 8: A confused deputy vulnerability in AWS AppSync](https://securitylabs.dd-static.net/img/appsync-vulnerability-disclosure/hero.png?auto=format&w=447&dpr=1) research A confused deputy vulnerability in AWS AppSync](https://securitylabs.datadoghq.com/articles/appsync-vulnerability-disclosure/)

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