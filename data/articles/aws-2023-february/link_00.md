Title: The anatomy of ransomware event targeting data residing in Amazon S3 | Amazon Web Services

URL Source: https://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/

Published Time: 2023-02-06T11:07:51-07:00

Markdown Content:
# The anatomy of ransomware event targeting data residing in Amazon S3 | AWS Security Blog

## Select your cookie preferences

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Accept Decline Customize

## Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

### Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

### Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

- [x]  

Allowed

### Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

- [x]  

Allowed

### Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

- [x]  

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the[AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

Cancel Save preferences

## Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our[Cookie Notice](https://aws.amazon.com/legal/cookies/).

Allow cross-context behavioral ads Opt out of cross-context behavioral ads 

 

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form[here](https://pulse.aws/application/ZRPLWLL6?p=0).

For more information about how AWS handles your information, read the[AWS Privacy Notice](https://aws.amazon.com/privacy/).

Cancel Save preferences

## Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Dismiss

[Skip to Main Content](https://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/#aws-page-content-main)

[](https://aws.amazon.com/?nc2=h_home)

*       Filter: All                
*    

*   English 
*   [Contact us](https://aws.amazon.com/contact-us/?nc2=h_ut_cu) 
*   [AWS Marketplace](https://aws.amazon.com/marketplace/?nc2=h_utmp) 
*   Support 
*   My account 

*   [](https://aws.amazon.com/?nc2=h_home)
*   [re:Invent](https://reinvent.awsevents.com/?nc2=h_l1_f&trk=c775b40b-0f43-4b55-9eb1-a0ef0787360c)
*   Discover AWS 
*   Products 
*   Solutions 
*   Pricing 
*   Resources 

*   Search

    Filter: All                
*   [Sign in to console](https://console.aws.amazon.com/console/home/?nc2=h_si&src=header-signin)
*   [Create account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_su&src=header_signup)

AWS Blogs

*   [Home](https://aws.amazon.com/blogs/)
*   Blogs 
*   Editions 

## [AWS Security Blog](https://aws.amazon.com/blogs/security/)

# The anatomy of ransomware event targeting data residing in Amazon S3

by Megan O'Neil, Kyle Dickinson, and Karthik Ram on 06 FEB 2023 in [Intermediate (200)](https://aws.amazon.com/blogs/security/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance"), [Technical How-to](https://aws.amazon.com/blogs/security/category/post-types/technical-how-to/ "View all posts in Technical How-to")[Permalink](https://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/)[Comments](https://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/#Comments)[Share](https://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/#)

*   [](https://www.facebook.com/sharer/sharer.php?u=https://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/)
*   [](https://twitter.com/intent/tweet/?text=The%20anatomy%20of%20ransomware%20event%20targeting%20data%20residing%20in%20Amazon%20S3&via=awscloud&url=https://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/)
*   [](https://www.linkedin.com/shareArticle?mini=true&title=The%20anatomy%20of%20ransomware%20event%20targeting%20data%20residing%20in%20Amazon%20S3&source=Amazon%20Web%20Services&url=https://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/)
*   [](mailto:?subject=The%20anatomy%20of%20ransomware%20event%20targeting%20data%20residing%20in%20Amazon%20S3&body=The%20anatomy%20of%20ransomware%20event%20targeting%20data%20residing%20in%20Amazon%20S3%0A%0Ahttps://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/)

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

 TAGS: [Amazon S3](https://aws.amazon.com/blogs/security/tag/amazon-s3/), [AWS Backup](https://aws.amazon.com/blogs/security/tag/aws-backup/), [AWS security](https://aws.amazon.com/blogs/security/tag/aws-security/), [Cloud security](https://aws.amazon.com/blogs/security/tag/cloud-security/), [IAM](https://aws.amazon.com/blogs/security/tag/iam/), [KMS](https://aws.amazon.com/blogs/security/tag/kms/), [No more ransom](https://aws.amazon.com/blogs/security/tag/no-more-ransom/), [ransomware](https://aws.amazon.com/blogs/security/tag/ransomware/), [RBAC](https://aws.amazon.com/blogs/security/tag/rbac/), [s3 intelligent tiering](https://aws.amazon.com/blogs/security/tag/s3-intelligent-tiering/), [s3 security](https://aws.amazon.com/blogs/security/tag/s3-security/), [Security](https://aws.amazon.com/blogs/security/tag/security/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/), [SSE-KMS](https://aws.amazon.com/blogs/security/tag/sse-kms/)

* * *

### Resources

*   [AWS Cloud Security](https://aws.amazon.com/security?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-resources)
*   [AWS Compliance](https://aws.amazon.com/compliance?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-resources)
*   [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html?secd_ip5)
*   [Best Practices](https://aws.amazon.com/architecture/security-identity-compliance)
*   [Data Protection at AWS](https://aws.amazon.com/compliance/data-protection/)
*   [Zero Trust on AWS](https://aws.amazon.com/security/zero-trust/)
*   [Cryptographic Computing](https://aws.amazon.com/security/cryptographic-computing/)

* * *

### Follow

*   [Twitter](https://twitter.com/AWSsecurityinfo)
*   [Facebook](https://www.facebook.com/amazonwebservices)
*   [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
*   [Twitch](https://www.twitch.tv/aws)
*   [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-social)

[Create an AWS account](https://signin.aws.amazon.com/signup?request_type=register)

## Learn

*   [What Is AWS?](https://aws.amazon.com/what-is-aws/?nc1=f_cc)
*   [What Is Cloud Computing?](https://aws.amazon.com/what-is-cloud-computing/?nc1=f_cc)
*   [What Is Agentic AI?](https://aws.amazon.com/what-is/agentic-ai/?nc1=f_cc)
*   [Cloud Computing Concepts Hub](https://aws.amazon.com/what-is/?nc1=f_cc)
*   [AWS Cloud Security](https://aws.amazon.com/security/?nc1=f_cc)
*   [What's New](https://aws.amazon.com/new/?nc1=f_cc)
*   [Blogs](https://aws.amazon.com/blogs/?nc1=f_cc)
*   [Press Releases](https://press.aboutamazon.com/press-releases/aws)

## Resources

*   [Getting Started](https://aws.amazon.com/getting-started/?nc1=f_cc)
*   [Training](https://aws.amazon.com/training/?nc1=f_cc)
*   [AWS Trust Center](https://aws.amazon.com/trust-center/?nc1=f_cc)
*   [AWS Solutions Library](https://aws.amazon.com/solutions/?nc1=f_cc)
*   [Architecture Center](https://aws.amazon.com/architecture/?nc1=f_cc)
*   [Product and Technical FAQs](https://aws.amazon.com/faqs/?nc1=f_dr)
*   [Analyst Reports](https://aws.amazon.com/resources/analyst-reports/?nc1=f_cc)
*   [AWS Partners](https://aws.amazon.com/partners/work-with-partners/?nc1=f_dr)

## Developers

*   [Builder Center](https://aws.amazon.com/developer/?nc1=f_dr)
*   [SDKs & Tools](https://aws.amazon.com/developer/tools/?nc1=f_dr)
*   [.NET on AWS](https://aws.amazon.com/developer/language/net/?nc1=f_dr)
*   [Python on AWS](https://aws.amazon.com/developer/language/python/?nc1=f_dr)
*   [Java on AWS](https://aws.amazon.com/developer/language/java/?nc1=f_dr)
*   [PHP on AWS](https://aws.amazon.com/developer/language/php/?nc1=f_cc)
*   [JavaScript on AWS](https://aws.amazon.com/developer/language/javascript/?nc1=f_dr)

## Help

*   [Contact Us](https://aws.amazon.com/contact-us/?nc1=f_m)
*   [File a Support Ticket](https://console.aws.amazon.com/support/home/?nc1=f_dr)
*   [AWS re:Post](https://repost.aws/?nc1=f_dr)
*   [Knowledge Center](https://repost.aws/knowledge-center/?nc1=f_dr)
*   [AWS Support Overview](https://aws.amazon.com/premiumsupport/?nc1=f_dr)
*   [Get Expert Help](https://iq.aws.amazon.com/?utm=mkt.foot/?nc1=f_m)
*   [AWS Accessibility](https://aws.amazon.com/accessibility/?nc1=f_cc)
*   [Legal](https://aws.amazon.com/legal/?nc1=f_cc)

English

Back to top

Amazon is an Equal Opportunity Employer: Minority / Women / Disability / Veteran / Gender Identity / Sexual Orientation / Age.

[](https://twitter.com/awscloud)[](https://www.facebook.com/amazonwebservices)[](https://www.linkedin.com/company/amazon-web-services/)[](https://www.instagram.com/amazonwebservices/)[](https://www.twitch.tv/aws)[](https://www.youtube.com/user/AmazonWebServices/Cloud/)[](https://aws.amazon.com/podcasts/?nc1=f_cc)[](https://pages.awscloud.com/communication-preferences?trk=homepage)

*   [Privacy](https://aws.amazon.com/privacy/?nc1=f_pr)
*   [Site terms](https://aws.amazon.com/terms/?nc1=f_pr)
*   [Cookie Preferences](https://aws.amazon.com/blogs/security/anatomy-of-a-ransomware-event-targeting-data-in-amazon-s3/#)

© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.