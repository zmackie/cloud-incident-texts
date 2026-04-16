---
title: 20/20 Eye Care Network and Hearing Care Network notify 3,253,822 health plan members of breach that deleted contents of AWS buckets
url: "https://www.databreaches.net/20-20-eye-care-network-and-hearing-care-network-notify-3253822-health-plan-members-of-breach-that-deleted-contents-of-aws-buckets/"
author: Dissent
published: 2021-06-01
source_type: article
source_domain: www.databreaches.net
cleanup_method: llm
---

# 20/20 Eye Care Network and Hearing Care Network notify 3,253,822 health plan members of breach that deleted contents of AWS buckets

Posted on [June 1, 2021](https://databreaches.net/2021/06/01/20-20-eye-care-network-and-hearing-care-network-notify-3253822-health-plan-members-of-breach-that-deleted-contents-of-aws-buckets/) by [Dissent](https://databreaches.net/author/dissent/)

**20/20 Eye Care Network, Inc**. is a managed vision care company in Florida that offers administrative services to health plans. **20/20 Hearing Care Network** expands those services into hearing care.

On May 28, 20/20’s Chief Compliance Officer notified the Maine Attorney General’s Office of an incident in which their Amazon AWS S3 buckets were accessed and data deleted. As they describe it in their notification to those affected:

> On January 11, 2021, 20/20 was alerted to suspicious activity in its Amazon Web Services (“AWS”) environment. In response, access credentials to the AWS environment were reviewed and deactivated/reset, and other responsive security measures were immediately put into place. In response to the deletion event, 20/20 promptly notified the FBI. After reviewing available evidence, the investigation determined that on January 11, 2021, data was potentially removed from the S3 buckets hosted in AWS and all the data in the S3 buckets was then deleted. The forensic investigation continued, and in late February, 20/20 determined the data could have potentially included information about some or all health plan members for whom it had records.
> 
> 
> At this time, 20/20 has notified the relevant health plans believed to have been impacted as a result of this event. Subsequently, an exhaustive review to determine what specific data may be at risk and to whom that information relates was conducted. Upon completion of the review and verification of the data, 20/20 notified individuals and relevant regulators as soon as possible.
> 
> 
> The information that could have been subject to unauthorized access includes name, address, Social Security number, member identification number, date of birth, and health insurance information.

It appears that they could not conclusively determine what/which data had been accessed and possibly exfiltrated and what data had been deleted, but it sounds like all the data in the buckets was deleted.

The total number of persons affected nationwide was reported as 3,253,822. Those being offered free credit monitoring services are being offered 12 months of credit monitoring, identity restoration services, and fraud consultation through TransUnion.

The incident is somewhat shrouded in confusion. What actually happened, and what was the motivation of the threat actor? Their report to the state coded the incident as “insider wrongdoing,” but there is nothing in the notification to affected members to indicate that the entities suspected a rogue employee was responsible. So was this a threat actor like “Meow” just maliciously deleting the contents of misconfigured s3 buckets, or were data stolen for future misuse? We do not seem to have clear answers.

DataBreaches.net has emailed their compliance officer to seek clarification on why they reported this as “insider wrongdoing” and will update this post when a reply is received.
