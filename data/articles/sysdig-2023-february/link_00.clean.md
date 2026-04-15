---
title: "SCARLETEEL: Operation leveraging Terraform, Kubernetes, and AWS for data theft"
url: "https://sysdig.com/blog/cloud-breach-terraform-data-theft/"
author: Alberto Pellitteri
published: 2023-02-28
source_type: article
source_domain: sysdig.com
cleanup_method: llm
---

[< back to blog](https://sysdig.com/blog)

# SCARLETEEL: Operation leveraging Terraform, Kubernetes, and AWS for data theft

The Sysdig Threat Research Team recently discovered a sophisticated cloud operation in a customer environment, dubbed SCARLETEEL, that resulted in stolen proprietary data. The attacker exploited a containerized workload and then leveraged it to perform privilege escalation into an AWS account in order to steal proprietary software and credentials. They also attempted to pivot using a Terraform state file to other connected AWS accounts to spread their reach throughout the organization.

This attack was more sophisticated than most, as it started from a compromised Kubernetes container and spread to the victim's AWS account. The attackers also had knowledge of AWS cloud mechanics, such as Elastic Compute Cloud (EC2) roles, Lambda serverless functions, and Terraform. The end result wasn't just a typical [cryptojacking](https://sysdig.com/learn-cloud-native/detection-and-response/what-is-cryptojacking) attack. The attacker had other, more malicious motives: the theft of proprietary software.

Cyberattacks in the cloud have [increased by 56%](https://news.sophos.com/en-us/2022/11/29/the-reality-of-smb-cloud-security-in-2022) over the past year. Obtaining persistence in the cloud, exfiltrating sensitive data, and creating new resources such as EC2 instances for use in cryptomining are the most common motives. Such resources can have a serious impact on an organization's cloud bills. But more espionage-focused motives are also alive and well.The reality is that attackers can use your cloud resources for more than just cryptomining.

The sophisticated attack we witnessed has many facets that underlie the complexity of securing a cloud-based infrastructure. [Vulnerability management](https://sysdig.com/blog/vulnerability-assessment) alone won't address everything. Instead, there are a number of tools that can reduce your risk from advanced threats, including virtual machine, [cloud security posture management (CSPM)](https://sysdig.com/solutions/cspm), [cloud infrastructure entitlement management (CIEM)](https://sysdig.com/learn-cloud-native/cloud-security/what-is-cloud-infrastructure-entitlements-management-ciem), runtime threat detection, and secrets management.

### Overview

This infographic shows the main steps in the kill chain. Let's first show the attack at a high level, then provide greater detail of each step.

[![Image 49: SCARLETEEL overview](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c4553c3177d680abcabe_image-45-1170x439.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c4553c3177d680abcabe_image-45-1170x439.png)

*   Step 1: The attacker gained **initial access** by exploiting a public-facing service in a self-managed Kubernetes cluster hosted inside an AWS cloud account.
*   Step 2: Once the attacker gained access to the pod, the malware was able to perform two initial actions during **execution**:
    *   Launch a cryptominer in order to **make money or provide a distraction**.
    *   Obtain**credential access**through a worker's temporary credentials in [Instance Metadata Service (IMDS) v1](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) to enumerate and collect information on its behalf using the cluster role permissions. Due to excessive granted permissions, the attacker was able to:
        *   **Enumerate AWS resources**.
        *   **Find credentials** of other identity and access management (IAM) users both set as Lambda environment variables and pushed in plain text to Amazon Simple Storage Service (S3) buckets.

*   Step 3: The attacker used the credentials found in the previous step to **move laterally**. They directly contacted the AWS API, further enumerated the account, and proceeded with **information gathering** and **data exfiltration**. During this step, they were able to:
    *   Disable CloudTrail logs to evade detection.
    *   Steal proprietary software.
    *   Find the credentials of an IAM user related to a different AWS account by discovering Terraform state files in S3 buckets.

*   Step 4: The attacker used the new credentials to **move laterally** again, repeating the attack and their kill chain from the other AWS account they found. Fortunately, in this case they were not able to enumerate resources, since all of the AWS API requests they attempted **failed due to a lack of permissions**. 

### Technical analysis

## Initial access – container compromise

The attacker found and exploited an internet-exposed service deployed in a Kubernetes cluster. Once they accessed the container, they started performing different actions to proceed with their attack.

The first action we recorded was the downloading and launching of a miner in order to steal some memory cycles. This is a common practice in automated container threats, as reported in our "[2022 Cloud-Native Threat Report](https://sysdig.com/resources/reports/2022-cloud-native-threat-report)." As you can see here, the attacker launched the script miner.sh in order to run an XMRig executable, along with the miner configuration file config_background.json.

[![Image 50: config_background.json](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac93_image-46-1170x167.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac93_image-46-1170x167.png)

[![Image 51: Malicious binary detected](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac87_image-47.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac87_image-47.png)

[![Image 52: cryptojacking xmrig](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac8d_image-48.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac8d_image-48.png)

The purpose of the attack went far beyond cryptomining, however. Either cryptomining was the attacker's initial goal and the goal changed once they accessed the victim's environment, or cryptomining was used as a decoy to evade the detection of data exfiltration. During the installation of the cryptominer, we observed a bash script running simultaneously on the container to enumerate and extract additional information in the environment, such as credentials.

In order to find credentials, the attacker directly accessed IMDS. IMDS v1 is the version used by default when creating older versions of self-managed clusters or EC2 instances in AWS. It's used to configure and manage machines.

Retrieving AWS temporary security credentials bound to the EC2 instance role from IMDS v1 is a very well-known practice that we've covered in previous [blog posts](https://sysdig.com/blog/lateral-movement-cloud-containers). The attacker may discover the IAM role bound to the worker instance running:

and later obtain the AccessKeyId, SecretAccessKey, and temporary token:

Looking at the malicious request to IMDS v1, we also found a request to a lesser-known internal endpoint described as "internal use only" and explained in [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instancedata-data-categories.html).

The screenshot below shows how the attacker targeted both the instance metadata endpoints and what commands were executed by the malicious script in order to grep and retrieve the IAM role keys.

[![Image 53: Metadata IAM role keys](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac9e_image-49-1170x776.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac9e_image-49-1170x776.png)

Once collected, it is possible to use those credentials for a short period of time in order to run operations on behalf of the impersonated IAM role, calling the AWS API directly. Using [CloudTrail logs](https://sysdig.com/blog/cloud-log-management-cloudwatch-vs-cloudtrail), you can see the first API calls from the attacker using the cluster role:

[![Image 54: Cloudtrail logs](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4aca4_image-50-1170x597.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4aca4_image-50-1170x597.png)

The attacker ran some AWS actions to gain persistence on the AWS platform, trying to create new users, groups, and bind new access keys to existing IAM users. Fortunately, all of these executions were denied because of a lack of permissions on the account the attacker was using.

Unfortunately, the AWS cluster role was [misconfigured with excessive read permissions](https://sysdig.com/blog/iam-security-misconfiguration). The original intent was to allow the reading of a specific S3 bucket, but the permissions allowed the role to read everything in the account, which enabled the attacker to gain further knowledge of the AWS account, including Lambda.

## Discovery – AWS cloud

Once the attacker obtained initial access into the cloud account, they started gathering information about the resources deployed in the AWS account. The activities reported in the table below are just some of the API requests recorded in the AWS account.

[![Image 55: S3 log cloudtrail](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac8a_image-51-1170x95.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac8a_image-51-1170x95.png)

[![Image 56: Lambda cloudtrail log](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4aca7_image-52-1170x574.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4aca7_image-52-1170x574.png)

During these scraping operations, the attacker focused their efforts on the most used AWS services: Serverless Lambda functions and S3 buckets.

#### Lambda function enumeration – stolen proprietary code and software

As we pointed out in [this article](https://sysdig.com/blog/exploit-mitigate-aws-lambdas-mitre), Lambda functions and other serverless functions are commonly used to execute custom code without worrying about the infrastructure underneath, leaving a lot of flexibility for end users.

There were different Lambda functions in the affected AWS account, mainly related to account automation.

The attacker started to enumerate and retrieve all of the Lambda functions located in a specific region in the AWS account using the proper API call. For example, you can use the AWS command below to list the functions. Behind the scenes, it is just REST API calls, so there are many ways to accomplish this task.

After obtaining the list of functions, the attacker tried to dig deeper by downloading the Lambda code. Calling the following AWS API, they were able to get the code location so that they could download the code that makes up the Lambda. In this case, the Lambda function held proprietary software and the keys needed to execute it.

Using curl or wget commands, the attacker successfully exfiltrated the Lambda code and stole proprietary code and software from the Lambda functions. There was also evidence that the attacker executed the stolen software.

They took the time to look at the Lambda function's environment variables and find additional AWS credentials related to IAM users in the same account, using a command similar to:

As you will see in the next steps of the attack, adversaries used the credentials found here to retry enumeration with the new user, hoping for new findings or to evaluate possible privilege escalation inside the account.

#### S3 bucket enumeration

Amazon S3 is a widely popular storage service that allows users to store and retrieve data.

Attackers often target resources and files stored in S3 buckets to extract information and credentials. In the past, many breaches have exploited misconfigured S3 buckets or S3 buckets left open to the public without passwords or security measures. During this particular attack, the attacker was able to retrieve and read more than 1 TB of information, including customer scripts, troubleshooting tools, and logging files.

[![Image 57: Listbuckets api call Cloudtrail](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac96_image-53-1170x221.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac96_image-53-1170x221.png)

CloudTrail does not log data events for objects stored in S3 buckets unless such functionality is explicitly requested. In this case, that functionality was not turned on, which makes it impossible to see information about the access of specific objects. However, we are certain that the attacker went through the buckets looking for sensitive data. To speed up their pursuit without consuming their available storage, they may have used tools like TruffleHog to immediately obtain new AWS user credentials and continue lateral movement in the cluster.

The 1 TB of data also included logging files related to Terraform, which was used in the account to deploy part of the infrastructure. These Terraform files will play an important part in the later step where the attacker tried to pivot to another AWS account.

## Defense evasion – disable CloudTrail logging

Once the attacker accessed the cloud account, they attempted to disable CloudTrail logs inside the compromised account. As you can see from the screenshot below, the attacker succeeded in disabling some of the logs configured in the account because of extra permissions assigned to one of the users compromised in the previous steps.

[![Image 58: StopLogging Cloudtrail defense evasion](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac84_image-54-1170x233.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac84_image-54-1170x233.png)

As a result of this action, we could not retrieve additional attack evidence. When reviewing account permissions, it is critical to keep the ability to disable or delete security logs to as few users as possible. Deletion shouldn't even be possible in most situations without a solid backup solution.

### Credential access – Terraform state files

[Terraform](https://github.com/hashicorp/terraform) is an open source infrastructure as code (IaC) tool used to deploy, change, or create infrastructures in cloud environments.

In order for Terraform to know which resources are under its control and when to update and destroy them, it uses a state file named _terraform.tfstate_ by default. When Terraform is integrated and automated in continuous integration/continuous delivery (CI/CD) pipelines, the state file needs to be accessible with proper permissions. In particular, the service principal running the pipeline needs to be able to access the storage account container that holds the state file. This makes shared storage like Amazon S3 buckets a perfect candidate to hold the state file.

However, Terraform state files contain all data in plain text, which may contain secrets. Storing secrets anywhere other than a secure location is never a good idea, and definitely should not be put into source control!

The attacker was able to list the bucket available and retrieve all of the data. Examining the data with different tools such as [Pacu](https://github.com/RhinoSecurityLabs/pacu) and [TruffleHog](https://github.com/trufflesecurity/trufflehog) during the [incident investigation](https://sysdig.com/blog/guide-kubernetes-forensics-dfir), it was possible to find both a clear-text IAM user access key and secret key in the _terraform.tfstate_ file inside of an S3 bucket. Here is a screenshot from TruffleHog.

[![Image 59: Terraform s3 bucket leak credentials](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac90_image-55-1170x267.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac90_image-55-1170x267.png)

These IAM credentials are for a second connected AWS account, giving the attacker the opportunity to move laterally to spread their attack throughout the organization.

## Lateral movement – AWS account

With the new credentials acquired, the attacker restarted their enumeration and information-gathering process to determine whether they could gain additional resources from inside this additional compromised account. In addition, CloudTrail recorded suspicious activities in the connected AWS account mentioned above.

The attacker tried to perform enumeration on different AWS resources in the connected cloud account. Fortunately, the IAM user was very well scoped, so all of the requests failed due to a lack of permissions, leaving just the harmless _GetCallerIdentity_ API, which is permitted by default.

[![Image 60: Lateral movement AWS account](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac99_image-56-1170x597.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877c45d51848dde3bc4ac99_image-56-1170x597.png)

### Recommendations

The attack reported here is a clear indication of how threat actors are trying to reach the cloud as a main goal. It all started with a compromised service, although the attacker tried to move laterally in the cloud as soon as they obtained valid credentials to find valuable information such as proprietary code. They also tried to pivot to other cloud accounts to get more and more.

Here are some main takeaways that can help you be more careful:

*   **Patch and apply a vulnerability management cycle to your application** and public-facing container. You will be aware of what you have exposed and can prioritize patching activities.
*   **Use**[**IMDS v2**](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) instead of IMDS v1. The enhancement version requires session-oriented requests to add defense in depth against unauthorized metadata access. Moreover, to ensure that only authorized pods can assume specific IAM roles in your clusters, adopt the [principle of least privilege](https://sysdig.com/blog/cspm-least-privilege-principle) and use **IAM roles for service accounts (IRSA)** whenever possible. IRSA limits access to resources and reduces the risk of unauthorized access. Pods that are not authorized will stick to the IMDS settings.
*   **Don't underestimate the power of read-only access _._**Even read-only in specific AWS resources like Lambda functions means data exfiltration or credential harvesting. Scoping the [read-only access](https://sysdig.com/blog/containers-read-only-fileless-malware) on just the needed resources is fundamental to keep your account safe.
*   **Monitor the stale objects in your cloud account**. Unused permissions, even if old and never used, can be dangerous and cost you a lot in the event of a compromise. Being aware of stale objects and periodically assessing the cloud object should be mandatory. 
*   **Terraform is a great tool, but it needs to be handled with care**. Adopt the best practices and store the state file in a secure location. Using key management services (KMSs) like [AWS KMS](https://aws.amazon.com/kms), [GCP KMS](https://cloud.google.com/security-key-management), or [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault), it's possible to keep the secret safe and encrypt or decrypt the secrets once needed. 

### Attack summary and conclusion

To recap, the SCARLETEEL attack started with the exploitation of a vulnerable pod. The attacker used the identity related to the IAM role associated with the node where the pod was running. Then they exploited that role to do enumeration in the cloud, search for sensitive information, and steal proprietary software. Once they discovered new credentials, they leveraged those to gain persistence and try to obtain more privileges.

The measures taken in order to secure the environment following discovery of the attack included disabling and removing users' access keys and secret access keys; securing vulnerable applications after conducting some audits and penetration tests; limiting access to sensitive S3 buckets through the use of restrictive policies; and adopting extra measures of least privilege to reduce the potential attack surface and prevent lateral movement activities in the cloud.

In this sophisticated attack, we saw how far an attacker can go as the result of compromising a vulnerable application with a lack of adequate security measures. This event reiterated what we all already knew. First, zero trust and the principle of least privilege are important, and if you implement them, you will reduce the likelihood of compromise. Second, strong detections and alerts should help you catch these activities before an attacker gets too deep.

### IoCs

**IP Addresses:**

*   80[.]239[.]140[.]66
*   45[.]9[.]148[.]221
*   45[.]9[.]148[.]121
*   45[.]9[.]249[.]58

For additional IoCs associated with this campaign, [please visit our GitHub page](https://github.com/sysdig/STRT/tree/main/iocs).
