Title: Tales from the cloud trenches: Raiding for AWS vaults, buckets and secrets | Datadog Security Labs

URL Source: https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/

Published Time: 2024-06-19T00:00:00Z

Markdown Content:
# Tales from the cloud trenches: Raiding for AWS vaults, buckets and secrets | Datadog Security Labs

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

# Tales from the cloud trenches: Raiding for AWS vaults, buckets and secrets

June 19, 2024

*   [aws](https://securitylabs.datadoghq.com/articles/?tag=aws)
*   [threat detection](https://securitylabs.datadoghq.com/articles/?tag=threat_detection)

*   [twitter](https://twitter.com/share?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets%2F&text=Tales%20from%20the%20cloud%20trenches%3A%20Raiding%20for%20AWS%20vaults%2C%20buckets%20and%20secrets "twitter")
*   [reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets%2F "reddit")

![Image 1: Tales From The Cloud Trenches: Raiding For Aws Vaults, Buckets And Secrets](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/hero.png?auto=format&h=712&dpr=1)

on this page

*   [Key points and observations](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#key-points-and-observations)
*   [Attacker activity: Pivoting on IP addresses and enumerating vaults, buckets, and secrets](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#attacker-activity-pivoting-on-ip-addresses-and-enumerating-vaults-buckets-and-secrets)
    *   [Notable AWS service: S3 Glacier](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#notable-aws-service-s3-glacier)
    *   [Notable network infrastructure: CloudFlare WARP VPN](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#notable-network-infrastructure-cloudflare-warp-vpn)
    *   [Notable user agent: Signing API requests](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#notable-user-agent-signing-api-requests)

*   [Summary of attacker activity](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#summary-of-attacker-activity)
*   [Detection opportunities](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#detection-opportunities)
*   [How Datadog can help](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#how-datadog-can-help)
*   [Conclusion](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#conclusion)
*   [Indicators of compromise](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#indicators-of-compromise)

[![Image 2: Martin McCloskey](https://securitylabs.dd-static.net/img/authors/martin_mccloskey.png?auto=format&w=48&h=48&dpr=2&q=75) Martin McCloskey Senior Detection Engineer](https://securitylabs.datadoghq.com/articles/?author=Martin_McCloskey)

In this post, we explore a campaign we've witnessed in the wild across several AWS environments. Specifically, we will be reporting on attacker techniques that we've noticed from a cluster of malicious IP addresses targeting AWS Secrets Manager, AWS S3 and AWS S3 Glacier.

## [Key points and observations](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#key-points-and-observations)

*   We observed malicious automated activity attempting to enumerate victims’ AWS secrets, S3 buckets, and S3 Glacier vaults.
*   While we cannot confirm the initial access vector, based on the use of long-term access keys (AKIA) and the automated activity, we surmise that the attacker was likely using leaked access keys.
*   The attacker was using a mix of [residential proxies](https://medium.com/spur-intelligence/residential-proxies-the-legal-botnet-that-nobody-talks-about-4470cae7e3c) and a VPN client, specifically the [Cloudflare Warp VPN](https://developers.cloudflare.com/warp-client/).
*   The attacker was using an unusual user agent that indicated they were signing their own AWS API requests, something we have not observed in previous attacks.
*   Despite successfully being able to list objects in several S3 buckets, there were no follow-up data exfiltration attempts that we could observe, even though S3 data events were enabled.

## [Attacker activity: Pivoting on IP addresses and enumerating vaults, buckets, and secrets](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#attacker-activity-pivoting-on-ip-addresses-and-enumerating-vaults-buckets-and-secrets)

Over a period from 2024-05-23 to 2024-05-27, we identified abnormal behavior in a customer’s AWS environment during a threat hunt. We observed the IP address `148[.]252.146.75` attempting the API calls `ListSecrets` and `ListVaults` in a single AWS environment. Our IP addresses are enriched by internal and external [threat intelligence sources](https://docs.datadoghq.com/security/threat_intelligence/). We were able to enrich the IP address in question to determine that it was potentially a residential proxy on the Vodafone network (a UK mobile provider).

Pivoting on this IP address, we were able to identify additional activity in another AWS environment, which included attempts to enumerate AWS S3 buckets with the `ListBuckets` API call and then determine their contents by using the `ListObjects` API call across any available buckets. Based on the event times we observed, we are confident that this activity was automated.

We did not identify any follow-up actions to retrieve secrets (`GetSecretValue` or `BatchGetSecretValue`) or retrieve objects from S3 buckets (`GetObject`). We were able to confirm that S3 data events were enabled.

There are a couple of reasons why an attacker may not exfiltrate data after discovering:

*   They are running a broad automated campaign against many AWS environments, and as such may assess what data is available before attempting to exfiltrate.
*   They may be testing what level of access an AWS identity has to determine resale value in a marketplace.

### [Notable AWS service: S3 Glacier](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#notable-aws-service-s3-glacier)

While AWS S3 is a common target for attackers, this is the first time we have observed an attacker targeting data stored in [S3 Glacier](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/amazon-s3-glacier.html) vaults, which are well suited for backup data storage. While we only observed failed enumeration attempts, based on available AWS documentation, we assume we would see two subsequent [Initiate Job](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html) API calls after enumeration, one to retrieve a list of the available vault archives, and the second to retrieve the specific archive. An archive can then be downloaded using the [Get Job Output](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-job-output-get.html) API call.

```json
"awsRegion": "us-west-2",
  "evevntName": "ListVaults",
  "eventCategory": "Management",
  "level": "Error",
  "eventVersion": "1.08",
  "eventSource": "glacier.amazonaws.com",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "error": {
    "kind": "AccessDenied",
    "message": "User: arn:aws:iam::<ACCOUNT ID>:user/<IAM USER> is not authorized to perform: glacier:ListVaults on resource: arn:aws:glacier:us-west-2:<ACCOUNT ID>:vaults/ because no identity-based policy allows the glacier:ListVaults action"
  },
```

### [Notable network infrastructure: CloudFlare WARP VPN](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#notable-network-infrastructure-cloudflare-warp-vpn)

Attackers commonly use VPNs to mask their true geo-location. The Cloudflare WARP client is a free VPN (subscription models are available) that allows the user to tunnel their traffic through Cloudflare’s network. A possible advantage for an attacker in using this client is that AWS API calls from Cloudflare may appear less suspicious on the surface in comparison with some of the hosting providers used by other VPN services.

[![Image 3](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/cloudflare_warp_client.png?auto=format&w=600&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/cloudflare_warp_client.png?auto=format)
### [Notable user agent: Signing API requests](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#notable-user-agent-signing-api-requests)

```bash
python-requests/<requests version> auth-aws-sigv4/<library version>
```

Based on this [code snippet](https://github.com/andrewjroth/requests-auth-aws-sigv4/blob/master/requests_auth_aws_sigv4/__init__.py#L130), the user agent identified in this attack is likely to have been generated by the Python library [requests-auth-aws-sigv4](https://pypi.org/project/requests-auth-aws-sigv4/). . This library allows the user to sign AWS API requests manually. In the automated attacks we have observed in the [past](https://securitylabs.datadoghq.com/articles/following-attackers-trail-in-aws-methodology-findings-in-the-wild/), the user agents typically indicate the use of the AWS CLI or Boto3 (AWS SDK for Python). AWS uses [Sigv4](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) to sign API requests. This signing is handled automatically by Boto3. At this time, we have been unable to discern a specific reason why the attacker would want to manage this manually, but this may be a good indicator of suspicious activity in your environment if the usage of this library is not expected.

## [Summary of attacker activity](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#summary-of-attacker-activity)

Discovery:

*   [T1580 - Cloud Infrastructure Discovery](https://attack.mitre.org/techniques/T1580/)
*   [T1619 - Cloud Storage Object Discovery](https://attack.mitre.org/techniques/T1619)

[![Image 4](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/attacker-activity.png?auto=format&w=800&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/attacker-activity.png?auto=format)
## [Detection opportunities](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#detection-opportunities)

Enumeration techniques on commonly used services like AWS S3 and AWS Secrets Manager can be difficult to detect with a high confidence. Here are some suggestions to help to identify this type of activity:

*   Use indicators in the [IoC section](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#indicators-of-compromise) to detect this specific campaign. If you are able, it may be helpful to enrich IP addresses for the specific WARP client if API calls from CloudFlare are expected.
*   Identify `ListSecret`/`ListVault` API calls across multiple regions in a short time period. In the data we have, the attacker attempted to run each of these API calls across 17 regions in under a minute.
*   Identify spikes in `AccessDenied` errors for the following API calls: `ListSecrets`, `ListBuckets`, `ListObjects`, ‘`ListSecrets`. In circumstances where the attacker does not have the correct permissions, there may be an anomalous spike in `AccessDenied` errors.

## [How Datadog can help](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#how-datadog-can-help)

Datadog [Cloud SIEM](https://www.datadoghq.com/product/cloud-siem/) and [Cloud Security Management (CSM)](https://www.datadoghq.com/product/cloud-security-management/) come with the following out-of-the-box rules to identify suspicious activity relevant to these attacks in an AWS environment. The Cloud SIEM rules help identify potential threats, while the CSM rules help identify long-lived or stale access keys. [Long-lived access keys](https://www.datadoghq.com/state-of-cloud-security/#1) tend to carry a higher risk of being associated with a compromise.

*   [A user received an anomalous number of `AccessDenied` errors](https://docs.datadoghq.com/security/default_rules/9el-i95-dnl)
*   [Compromised AWS IAM User Access Key](https://docs.datadoghq.com/security/default_rules/yqe-gyj-js8)
*   [Access keys should be rotated every 90 days or less](https://docs.datadoghq.com/security/default_rules/bcz-prk-dr6)
*   [Inactive IAM access keys older than 1 year should be removed](https://docs.datadoghq.com/security/default_rules/r1s-kud-79s)

## [Conclusion](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#conclusion)

During the development of this blog, Lacework released a [blog](https://www.lacework.com/blog/detecting-ai-resource-hijacking-with-composite-alerts) detailing the same campaign. They captured additional AWS API calls indicating that the target of the campaign may have been Amazon Bedrock and the possible misuse of LLM resources.

We think this campaign warrants a closer look by detection and response teams as the exfiltration of production LLM data and resources from your cloud environment could be highly impactful to business operations.

## [Indicators of compromise](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets/#indicators-of-compromise)

| Indicator |
| --- |
| 104[.]28.231.254 (python-requests/2.20.0 auth-aws-sigv4/0.7, python-requests/2.31.0 auth-aws-sigv4/0.7) |
| 148[.]252.146.75 (python-requests/2.20.0 auth-aws-sigv4/0.7, python-requests/2.32.2 auth-aws-sigv4/0.7) |
| 104[.]28.242.246 (python-requests/2.31.0 auth-aws-sigv4/0.7) |
| 104[.]28.200.1 (python-requests/2.31.0 auth-aws-sigv4/0.7) |
| 2a09[:]bac5:37aa:d2::15:1c2 (python-requests/2.32.2 auth-aws-sigv4/0.7) |
| 2a09[:]bac5:37ab:163c::237:3a (python-requests/2.32.2 auth-aws-sigv4/0.7) |
| 104[.]28.232.2 (python-requests/2.32.2 auth-aws-sigv4/0.7) |
| 104[.]28.200.6 (python-requests/2.32.2 auth-aws-sigv4/0.7) |

*   [twitter](https://twitter.com/share?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets%2F&text=Tales%20from%20the%20cloud%20trenches%3A%20Raiding%20for%20AWS%20vaults%2C%20buckets%20and%20secrets "twitter")
*   [reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-raiding-for-vaults-buckets-secrets%2F "reddit")

## Did you find this article helpful?

## Subscribe to the Datadog Security Digest

Get the latest insights from the cloud security community and Security Labs posts, delivered to your inbox monthly. No spam.

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