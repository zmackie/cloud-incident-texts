---
title: The anatomy of ransomware event targeting data residing in Amazon S3
url: "https://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/"
author: Megan O'Neil, Kyle Dickinson, Karthik Ram
published: 2023-02-06
source_type: article
source_domain: aws.amazon.com
cleanup_method: llm
---

# The anatomy of ransomware event targeting data residing in Amazon S3

Ransomware events have significantly increased over the past several years and captured worldwide attention. Traditional ransomware events affect mostly infrastructure resources like servers, databases, and connected file systems. However, there are also non-traditional events that you may not be as familiar with, such as ransomware events that target data stored in [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/). There are important steps you can take to help prevent these events, and to identify possible ransomware events early so that you can take action to recover. The goal of this post is to help you learn about the AWS services and features that you can use to protect against ransomware events in your environment, and to investigate possible ransomware events if they occur.

_Ransomware_ is a type of malware that bad actors can use to extort money from entities. The actors can use a range of tactics to gain unauthorized access to their target’s data and systems, including but not limited to taking advantage of unpatched software flaws, misuse of weak credentials or previous unintended disclosure of credentials, and using social engineering. In a ransomware event, a legitimate entity’s access to their data and systems is restricted by the bad actors, and a ransom demand is made for the safe return of these digital assets. There are several methods actors use to restrict or disable authorized access to resources including a) encryption or deletion, b) modified access controls, and c) network-based Denial of Service (DoS) attacks. In some cases, after the target’s data access is restored by providing the encryption key or transferring the data back, bad actors who have a copy of the data demand a second ransom—promising not to retain the data in order to sell or publicly release it.

In the next sections, we’ll describe several important stages of your response to a ransomware event in Amazon S3, including detection, response, recovery, and protection.

## Observable activity

The most common event that leads to a ransomware event that targets data in Amazon S3, as observed by the [AWS Customer Incident Response Team (CIRT)](https://aws.amazon.com/blogs/security/welcoming-the-aws-customer-incident-response-team/), is unintended disclosure of [Identity and Access Management (IAM)](https://aws.amazon.com/iam/)[access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html). Another likely cause is if there is an application with a software flaw that is hosted on an [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instance with an attached IAM instance profile and associated permissions, and the instance is using [Instance Metadata Service Version 1 (IMDSv1)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html). In this case, an unauthorized user might be able to use [AWS Security Token Service (AWS STS) session keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) from the IAM instance profile for your EC2 instance to ransom objects in S3 buckets. In this post, we will focus on the most common scenario, which is unintended disclosure of static IAM access keys.

## Detection

After a bad actor has obtained credentials, they use AWS API actions that they iterate through to discover the type of access that the exposed [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) has been granted. Bad actors can do this in multiple ways, which can generate different levels of activity. This activity might alert your security teams because of an increase in API calls that result in errors. Other times, if a bad actor’s goal is to ransom S3 objects, then the API calls will be specific to Amazon S3. If access to Amazon S3 is permitted through the exposed IAM principal, then you might see an increase in API actions such as s3:ListBuckets, s3:GetBucketLocation, s3:GetBucketPolicy, and s3:GetBucketAcl.

## Analysis

In this section, we’ll describe where to find the log and metric data to help you analyze this type of ransomware event in more detail.

When a ransomware event targets data stored in Amazon S3, often the objects stored in S3 buckets are deleted, without the bad actor making copies. This is more like a data destruction event than a ransomware event where objects are encrypted.

There are several logs that will capture this activity. You can [enable AWS CloudTrail event logging for Amazon S3 data](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.html), which allows you to review the activity logs to understand read and delete actions that were taken on specific objects.

In addition, if you have enabled [Amazon CloudWatch metrics for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-dimensions.html) prior to the ransomware event, you can use the sum of the BytesDownloaded metric to gain insight into abnormal transfer spikes.

Another way to gain information is to use the region-DataTransfer-Out-Bytes metric, which shows the amount of data transferred from Amazon S3 to the internet. This metric is enabled by default and is associated with your AWS billing and usage reports for Amazon S3.

For more information, see the AWS CIRT team’s [Incident Response Playbook: Ransom Response for S3](https://github.com/aws-samples/aws-customer-playbook-framework/blob/main/docs/Ransom_Response_S3.md), as well as the other publicly available response frameworks available at the [AWS customer playbooks](https://github.com/aws-samples/aws-customer-playbook-framework) GitHub repository.

## Response

Next, we’ll walk through how to respond to the unintended disclosure of IAM access keys. Based on the business impact, you may decide to create a second set of access keys to replace all legitimate use of those credentials so that legitimate systems are not interrupted when you deactivate the compromised access keys. You can deactivate the access keys by using the IAM console or through automation, as defined in your incident response plan. However, you also need to document specific details for the event within your secure and private incident response documentation so that you can reference them in the future. If the activity was related to the use of an IAM role or temporary credentials, you need to take an additional step and [revoke any active sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html). To do this, in the IAM console, you choose the **Revoke active session** button, which will attach a policy that denies access to users who assumed the role before that moment. Then you can delete the exposed access keys.

In addition, you can use the [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) dashboard and event history (which includes 90 days of logs) to review the IAM related activities by that compromised IAM user or role. Your analysis can show potential persistent access that might have been created by the bad actor. In addition, you can use the IAM console to look at the IAM credential report (this report is updated every 4 hours) to review activity such as access key last used, user creation time, and password last used. Alternatively, you can use [Amazon Athena](https://aws.amazon.com/athena/) to [query the CloudTrail logs](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html) for the same information. See the following example of an Athena query that will take an IAM user Amazon Resource Number (ARN) to show activity for a particular time frame.

```text
SELECT eventtime, eventname, awsregion, sourceipaddress, useragent
FROM cloudtrail
WHERE useridentity.arn = 'arn:aws:iam::1234567890:user/Name' AND
-- Enter timeframe
(event_date >= '2022/08/04' AND event_date <= '2022/11/04')
ORDER BY eventtime ASC
```

Plain text

## Recovery

After you’ve removed access from the bad actor, you have multiple options to recover data, which we discuss in the following sections. Keep in mind that there is currently no _undelete_ capability for Amazon S3, and AWS does not have the ability to recover data after a delete operation. In addition, many of the recovery options require configuration upon bucket creation.

### S3 Versioning

Using versioning in S3 buckets is a way to keep multiple versions of an object in the same bucket, which gives you the ability to restore a particular version during the recovery process. You can use the [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) feature to preserve, retrieve, and restore every version of every object stored in your buckets. With versioning, you can recover more easily from both unintended user actions and application failures. Versioning-enabled buckets can help you recover objects from accidental deletion or overwrite. For example, if you delete an object, Amazon S3 inserts a delete marker instead of removing the object permanently. The previous version remains in the bucket and becomes a noncurrent version. You can restore the previous version. Versioning is not enabled by default and incurs additional costs, because you are maintaining multiple copies of the same object. For more information about cost, see the [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/) page.

### AWS Backup

Using [AWS Backup](https://aws.amazon.com/backup/) gives you the ability to create and maintain separate copies of your S3 data under separate access credentials that can be used to restore data during a recovery process. AWS Backup provides centralized backup for several AWS services, so you can manage your backups in one location. AWS Backup for Amazon S3 provides you with two options: _continuous backups_, which allow you to restore to any point in time within the last 35 days; and _periodic backups_, which allow you to retain data for a specified duration, including indefinitely. For more information, see [Using AWS Backup for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/backup-for-s3.html).

## Protection

In this section, we’ll describe some of the preventative security controls available in AWS.

### S3 Object Lock

You can add another layer of protection against object changes and deletion by enabling [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) for your S3 buckets. With S3 Object Lock, you can store objects using a write-once-read-many (WORM) model and can help prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely.

### AWS Backup Vault Lock

Similar to S3 Object lock, which adds additional protection to S3 objects, if you use AWS Backup you can consider enabling [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html), which enforces the same WORM setting for all the backups you store and create in a backup vault. AWS Backup Vault Lock helps you to prevent inadvertent or malicious delete operations by the AWS account root user.

### Amazon S3 Inventory

To make sure that your organization understands the sensitivity of the objects you store in Amazon S3, you should inventory your most critical and sensitive data across Amazon S3 and make sure that the appropriate bucket configuration is in place to protect and enable recovery of your data. You can use [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html) to understand what objects are in your S3 buckets, and the existing configurations, including encryption status, replication status, and object lock information. You can use resource [tags](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) to label the classification and owner of the objects in Amazon S3, and take automated action and apply controls that match the sensitivity of the objects stored in a particular S3 bucket.

### MFA delete

Another preventative control you can use is to enforce [multi-factor authentication (MFA) delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html) in S3 Versioning. MFA delete provides added security and can help prevent accidental bucket deletions, by requiring the user who initiates the delete action to prove physical or virtual possession of an MFA device with an MFA code. This adds an extra layer of friction and security to the delete action.

### Use IAM roles for short-term credentials

Because many ransomware events arise from unintended disclosure of static IAM access keys, AWS recommends that you use IAM roles that provide short-term credentials, rather than using long-term IAM access keys. This includes using [identity federation](https://aws.amazon.com/identity/federation/) for your developers who are accessing AWS, using IAM roles for system-to-system access, and using [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) for hybrid access. For most use cases, you shouldn’t need to use static keys or long-term access keys. Now is a good time to audit and work toward eliminating the use of these types of keys in your environment. Consider taking the following steps:

1.   Create an inventory across all of your AWS accounts and identify the IAM user, when the credentials were last rotated and last used, and the attached policy.
2.   Disable and delete all AWS account root access keys.
3.   Rotate the credentials and apply MFA to the user.
4.   Re-architect to take advantage of temporary role-based access, such as IAM roles or IAM Roles Anywhere.
5.   Review attached policies to make sure that you’re enforcing least privilege access, including removing wild cards from the policy.

### Server-side encryption with customer managed KMS keys

Another protection you can use is to implement [server-side encryption with AWS Key Management Service (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) and use [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) to encrypt your S3 objects. Using a customer managed key requires you to apply a specific key policy around who can encrypt and decrypt the data within your bucket, which provides an additional access control mechanism to protect your data. You can also centrally manage AWS KMS keys and audit their usage with an audit trail of when the key was used and by whom.

### GuardDuty protections for Amazon S3

You can enable [Amazon S3 protection in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html). With S3 protection, GuardDuty monitors object-level API operations to identify potential security risks for data in your S3 buckets. This includes findings related to anomalous API activity and unusual behavior related to your data in Amazon S3, and can help you identify a security event early on.

## Conclusion

In this post, you learned about ransomware events that target data stored in Amazon S3. By taking proactive steps, you can identify potential ransomware events quickly, and you can put in place additional protections to help you reduce the risk of this type of security event in the future.

If you have feedback about this post, submit comments in the**Comments** section below. If you have questions about this post, start a new thread on the [Security, Identity and Compliance re:Post](https://repost.aws/tags/TAEEfW2o7QS4SOLeZqACq9jA/security-identity-compliance) or [contact AWS Support](https://console.aws.amazon.com/support/home).

**Want more AWS Security news? Follow us on [Twitter](https://twitter.com/AWSsecurityinfo "Twitter").**

![Image 1: Author](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2021/08/24/Megan-ONeil-Author.jpg)

### Megan O’Neil

Megan is a Principal Specialist Solutions Architect focused on threat detection and incident response. Megan and her team enable AWS customers to implement sophisticated, scalable, and secure solutions that solve their business challenges.

![Image 2: Karthik Ram](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2021/12/06/Ramanujam.K-3223-3.jpg)

### Karthik Ram

Karthik is a Senior Solutions Architect with Amazon Web Services based in Columbus, Ohio. He has a background in IT networking, infrastructure architecture and Security. At AWS, Karthik helps customers build secure and innovative cloud solutions, solving their business problems using data driven approaches. Karthik’s Area of Depth is Cloud Security with a focus on Threat Detection and Incident Response (TDIR).

![Image 3: Kyle Dickinson](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2023/02/06/Kyle_Headshot.png)

### Kyle Dickinson

Kyle is a Sr. Security Solution Architect, specializing in threat detection, incident response. He focuses on working with customers to respond to security events with confidence. He also hosts AWS on Air: Lockdown, a livestream security show. When he’s not – he enjoys hockey, BBQ, and trying to convince his Shitzu that he’s in-fact, not a large dog.
