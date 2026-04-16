Title: Two real-life examples of why limiting permissions works: Lessons from AWS CIRT | Amazon Web Services

URL Source: https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/

Published Time: 2023-08-31T07:03:48-07:00

Markdown Content:
# Two real-life examples of why limiting permissions works: Lessons from AWS CIRT | AWS Security Blog

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

[Skip to Main Content](https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/#aws-page-content-main)

[](https://aws.amazon.com/?nc2=h_home)

*       Filter: All                
*    

*   English 
*   [Contact us](https://aws.amazon.com/contact-us/?nc2=h_ut_cu) 
*   [AWS Marketplace](https://aws.amazon.com/marketplace/?nc2=h_utmp) 
*   Support  
*   My account  

*   [](https://aws.amazon.com/?nc2=h_home)

*   Search

    Filter: All                
*   [Sign in to console](https://console.aws.amazon.com/console/home/?nc2=h_si&src=header-signin)
*   [Create account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_su&src=header_signup)

AWS Blogs

*   [Home](https://aws.amazon.com/blogs/)
*   Blogs 
*   Editions 

## [AWS Security Blog](https://aws.amazon.com/blogs/security/)

# Two real-life examples of why limiting permissions works: Lessons from AWS CIRT

by Richard Billington on 31 AUG 2023 in [Best Practices](https://aws.amazon.com/blogs/security/category/post-types/best-practices/ "View all posts in Best Practices"), [Intermediate (200)](https://aws.amazon.com/blogs/security/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance")[Permalink](https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/)[Comments](https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/#Comments)[Share](https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/#)

*   [](https://www.facebook.com/sharer/sharer.php?u=https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/)
*   [](https://twitter.com/intent/tweet/?text=Two%20real-life%20examples%20of%20why%20limiting%20permissions%20works%3A%20Lessons%20from%20AWS%20CIRT&via=awscloud&url=https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/)
*   [](https://www.linkedin.com/shareArticle?mini=true&title=Two%20real-life%20examples%20of%20why%20limiting%20permissions%20works%3A%20Lessons%20from%20AWS%20CIRT&source=Amazon%20Web%20Services&url=https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/)
*   [](mailto:?subject=Two%20real-life%20examples%20of%20why%20limiting%20permissions%20works%3A%20Lessons%20from%20AWS%20CIRT&body=Two%20real-life%20examples%20of%20why%20limiting%20permissions%20works%3A%20Lessons%20from%20AWS%20CIRT%0A%0Ahttps://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/)

Welcome to another blog post from the [AWS Customer Incident Response Team (CIRT)](https://aws.amazon.com/blogs/security/welcoming-the-aws-customer-incident-response-team/)! For this post, we’re looking at two events that the team was involved in from the viewpoint of a regularly discussed but sometimes misunderstood subject, _least privilege_. Specifically, we consider the idea that the benefit of reducing permissions in real-life use cases does not always require using the absolute minimum set of privileges. Instead, you need to weigh the cost and effort of creating and maintaining privileges against the risk reduction that is achieved, to make sure that your permissions are appropriate for your needs.

To [quote](https://www.youtube.com/watch?v=KJiCfPXOW-U&t=2183s) VP and Distinguished Engineer at Amazon Security, [Eric Brandwine](https://aws.amazon.com/blogs/security/aws-security-profiles-eric-brandwine-vp-and-distinguished-engineer/), “Least privilege equals maximum effort.” This is the idea that creating and maintaining the smallest possible set of privileges needed to perform a given task will require the largest amount of effort, especially as customer needs and service features change over time. However, the correlation between effort and permission reduction is not linear. So, the question you should be asking is: How do you balance the effort of privilege reduction with the benefits it provides?

Unfortunately, this is not an easy question to answer. You need to consider the likelihood of an unwanted issue happening, the impact if that issue did happen, and the cost and effort to prevent (or detect and recover from) that issue. You also need to factor requirements such as your business goals and regulatory requirements into your decision process. Of course, you won’t need to consider just one potential issue, but many. Often it can be useful to start with a rough set of permissions and refine them down as you develop your knowledge of what security level is required. You can also use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to provide a set of permission guardrails if you’re using [AWS Organizations](https://aws.amazon.com/organizations/). In this post, we tell two real-world stories where limiting [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) permissions worked by limiting the impact of a security event, but where the permission set did not involve maximum effort.

## Story 1: On the hunt for credentials

In this AWS CIRT story, we see how a threat actor was unable to achieve their goal because the access they obtained — a database administrator’s — did not have the IAM permissions they were after.

### Background and AWS CIRT engagement

A customer came to us after they discovered unauthorized activity in their on-premises systems and in some of their AWS accounts. They had incident response capability and were looking for an additional set of hands with AWS knowledge to help them with their investigation. This helped to free up the customer’s staff to focus on the on-premises analysis.

Before our engagement, the customer had already performed initial containment activities. This included rotating credentials, revoking temporary credentials, and isolating impacted systems. They also had a good idea of which federated user accounts had been accessed by the threat actor.

The key part of every AWS CIRT engagement is the customer’s ask. Everything our team does falls on the customer side of the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), so we want to make sure that we are aligned to the customer’s desired outcome. The ask was clear—review the potential unauthorized federated users’ access, and investigate the unwanted AWS actions that were taken by those users during the known timeframe. To get a better idea of what was “unwanted,” we talked to the customer to understand at a high level what a typical day would entail for these users, to get some context around what sort of actions would be expected. The users were primarily focused on working with [Amazon Relational Database Service (RDS)](https://aws.amazon.com/rds/).

### Analysis and findings

For this part of the story, we’ll focus on a single federated user whose apparent actions we investigated, because the other federated users had not been impersonated by the threat actor in a meaningful way. We knew the approximate start and end dates to focus on and had discovered that the threat actor had performed a number of unwanted actions.

After reviewing the actions, it was clear that the threat actor had performed a console sign-in on three separate occasions within a 2-hour window. Each time, the threat actor attempted to perform a subset of the following actions:

*   [CreateAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccessKey.html) — Create a new AWS secret access key
*   [CreateLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateLoginProfile.html) — Create a console password for a given IAM user
*   [UpdateAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccessKey.html) — Change an access key from inactive to active (or vice versa)
*   [DeleteAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccessKey.html) — Delete an access key pair
*   [PutRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePolicy.html) — Add or update an inline IAM policy
*   [CreatePolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicyVersion.html) — Create a new version of an existing managed policy

> **Note:** This list includes only the actions that are displayed as readOnly = false in [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), because these actions are often (but not always) the more impactful ones, with the potential to change the AWS environment.

This is the point where the benefit of permission restriction became clear. As soon as this list was compiled, we noticed that two fields were present for **all** of the actions listed:

```text
"errorCode": "Client.UnauthorizedOperation",
"errorMessage": "You are not authorized to perform this operation. [rest of message]"
```

Plain text

As this reveals, every single non-readOnly action that was attempted by the threat actor was denied because the federated user account did not have the required IAM permissions.

### Customer communication and result

After we confirmed the findings, we had a call with the customer to discuss the results. As you can imagine, they were happy that the results showed no material impact to their data, and said no further investigation or actions were required at that time.

What were the IAM permissions the federated user had, which prevented the set of actions the threat actor attempted?

The answer did not actually involve the absolute minimal set of permissions required by the user to do their job. It’s simply that the federated user had a role that didn’t have an Allow statement for the IAM actions the threat actor tried — their job did not require them. Without an explicit Allow statement, the IAM actions attempted were denied because IAM policies are Deny by default. In this instance, simply not having the desired IAM permissions meant that the threat actor wasn’t able to achieve their goal, and stopped using the access. We’ll never know what their goal actually was, but trying to create access keys, passwords, and update policies means that a fair guess would be that they were attempting to create another way to access that AWS account.

## Story 2: More instances for crypto mining

In this AWS CIRT story, we see how a threat actor’s inability to create additional [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instances resulted in the threat actor leaving without achieving their goal.

### Background and AWS CIRT engagement

Our second story involves a customer who had an AWS account they were using to test some new third-party software that uses [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/). This customer had [Amazon GuardDuty](https://aws.amazon.com/guardduty/) turned on, and found that they were getting GuardDuty alerts for [CryptoCurrency:EC2/BitcoinTool](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#cryptocurrency-ec2-bitcointoolb) related findings.

Because this account was new and currently only used for testing their software, the customer saw that the detection was related to the Amazon ECS cluster and decided to delete all the resources in the account and rebuild. Not too long after doing this, they received a similar GuardDuty alert for the new Amazon ECS cluster they had set up. The second finding resulted in the customer’s security team and AWS being brought in to try to understand what was causing this. The customer’s security team was focused on reviewing the tasks that were being run on the cluster, while AWS CIRT reviewed the AWS account actions and provided insight about the GuardDuty finding and what could have caused it.

### Analysis and findings

Working with the customer, it wasn’t long before we discovered that the 3 rd party Amazon ECS task definition that the customer was using, was unintentionally exposing a web interface to the internet. That interface allowed unauthenticated users to run commands on the system. This explained why the same alert was also received shortly after the new install had been completed.

This is where the story takes a turn for the better. The AWS CIRT analysis of the [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) logs found that there were a number of attempts to use the credentials of the Task IAM role that was associated with the Amazon ECS task. The majority of actions were attempting to launch multiple Amazon EC2 instances via RunInstances calls. Every one of these actions, along with the other actions attempted, failed with either a Client.UnauthorizedOperation or an AccessDenied error message.

Next, we worked with the customer to understand the permissions provided by the Task IAM role. Once again, the permissions could have been limited more tightly. However, this time the goal of the threat actor — running a number of Amazon EC2 instances (most likely for surreptitious crypto mining) — did not align with the policy given to the role:

```text
{
    "Version": "2012-10-17",
    "Statement": [
        {
          "Effect": "Allow",
          "Action": "s3:*",
          "Resource": "*"
        }
    ]
}
```

Plain text

AWS CIRT recommended creating policies to restrict the allowed actions further, providing specific resources where possible, and potentially also adding in some conditions to limit other aspects of the access (such as the [two Condition keys launched recently](https://aws.amazon.com/blogs/security/how-to-use-policies-to-restrict-where-ec2-instance-credentials-can-be-used-from/) to limit where Amazon EC2 instance credentials can be used from). However, simply having the policy limit access to [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) meant that the threat actor decided to leave with just the one Amazon ECS task running crypto mining rather than a larger number of Amazon EC2 instances.

### Customer communication and result

After reporting these findings to the customer, there were two clear next steps: First, remove the now unwanted and untrusted Amazon ECS resource from their AWS account. Second, review and re-architect the Amazon ECS task so that access to the web interface was only provided to appropriate users. As part of that re-architecting, an Amazon S3 policy similar to “[Allows read and write access to objects in an S3 bucket](https://docs.amazonaws.cn/en_us/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html)” was recommended. This separates Amazon S3 bucket actions from Amazon S3 object actions. When applications have a need to read and write objects in Amazon S3, they don’t normally have a need to create or delete entire buckets (or versioning on those buckets).

## Some tools to help

We’ve just looked at how limiting privileges helped during two different security events. Now, let’s consider what can help you decide how to reduce your IAM permissions to an appropriate level. There are a number of resources that talk about different approaches:

The first approach is to use Access Analyzer to help generate IAM policies based on access activity from log data. This can then be refined further with the addition of [Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) elements as desired. We already have a couple of blog posts about that exact topic:

*   [IAM Access Analyzer makes it easier to implement least privilege permissions by generating IAM policies based on access activity](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/)
*   [Use IAM Access Analyzer to generate IAM policies based on access activity found in your organization trail](https://aws.amazon.com/blogs/security/use-iam-access-analyzer-to-generate-iam-policies-based-on-access-activity-found-in-your-organization-trail/)

The second approach is similar, and that is to reduce policy scope based on the last-accessed information:

*   [Review last accessed information to identify unused EC2, IAM, and Lambda permissions and tighten access for your IAM roles](https://aws.amazon.com/blogs/security/review-last-accessed-information-to-identify-unused-ec2-iam-and-lambda-permissions-and-tighten-access-for-iam-roles/)

The third approach is a manual method of creating and refining policies to reduce the amount of work required. For this, you can begin with an appropriate [AWS managed IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or an AWS provided example policy as a starting point. Following this, you can add or remove Actions, Resources, and Conditions — using wildcards as desired — to balance your effort and permission reduction.

An example of balancing effort and permission is in the IAM tutorial [Create and attach your first customer managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html). In it, the authors create a policy that uses iam:Get* and iam:List:* in the Actions section. Although not all iam:Get* and iam:List:* Actions may be required, this is a good way to group similar Actions together while minimizing Actions that allow unwanted access — for example, iam:Create* or iam:Delete*. Another example of this balancing was mentioned earlier [relating to Amazon S3](https://docs.amazonaws.cn/en_us/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html), allowing access to create, delete, and read objects, but not to change the configuration of the bucket those objects are in.

In addition to limiting permissions, we also recommend that you set up appropriate detection and response capability. This will enable you to know when an issue has occurred and provide the tools to contain and recover from the issue. Further details about performing incident response in an AWS account can be found in the [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.html).

There are also two services that were used to help in the stories we presented here — [Amazon GuardDuty](https://aws.amazon.com/guardduty/) and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/). GuardDuty is a threat detection service that continuously monitors your AWS accounts and workloads for malicious activity. It’s a great way to monitor for unwanted activity within your AWS accounts. CloudTrail records account activity across your AWS infrastructure and provides the logs that were used for the analysis that AWS CIRT performed for both these stories. Making sure that both of these are set up correctly is a great first step towards improving your threat detection and incident response capability in AWS.

## Conclusion

In this post, we looked at two examples where limiting privilege provided positive results during a security event. In the second case, the policy used should probably have restricted permissions further, but even as it stood, it was an effective preventative control in stopping the unauthorized user from achieving their assumed goal.

Hopefully these stories will provide new insight into the way your organization thinks about setting permissions, while taking into account the effort of creating the permissions. These stories are a good example of how starting a journey towards least privilege can help stop unauthorized users. Neither of the scenarios had policies that were least privilege, but the policies were restrictive enough that the unauthorized users were prevented from achieving their goals this time, resulting in minimal impact to the customers. However in both cases AWS CIRT recommended further reducing the scope of the IAM policies being used.

Finally, we provided a few ways to go about reducing permissions—first, by using tools to assist with policy creation, and second, by editing existing policies so they better fit your specific needs. You can get started by checking your existing policies against what [Access Analyzer would recommend](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/), by looking for and removing overly permissive wildcard characters (*) in some of your existing IAM policies, or by implementing and refining your SCPs.

If you have feedback about this post, submit comments in the**Comments** section below. If you have questions about this post, [contact AWS Support](https://console.aws.amazon.com/support/home).

**Want more AWS Security news? Follow us on [Twitter](https://twitter.com/AWSsecurityinfo "Twitter").**

![Image 1: Richard Billington](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2023/08/22/RichardBillington_Headshot_160x120.jpg)

### Richard Billington

Richard is the Incident Response Watch Lead for the Asia-Pacific region of the AWS Customer Incident Response Team (a team that supports AWS Customers during active security events). He also helps customers prepare for security events using event simulations. Outside of work, he loves wildlife photography and Dr Pepper (which is hard to find in meaningful quantities within Australia).

 TAGS: [AWS Incident Response](https://aws.amazon.com/blogs/security/tag/aws-incident-response/), [Incident response](https://aws.amazon.com/blogs/security/tag/incident-response/), [least privilege](https://aws.amazon.com/blogs/security/tag/least-privilege/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/), [Threat Detection & Incident Response](https://aws.amazon.com/blogs/security/tag/tdir/)

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

# CCBA-Footer

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

Amazon is an equal opportunity employer and does not discriminate on the basis of protected veteran status, disability or other legally protected status.

[](https://twitter.com/awscloud)[](https://www.facebook.com/amazonwebservices)[](https://www.linkedin.com/company/amazon-web-services/)[](https://www.instagram.com/amazonwebservices/)[](https://www.twitch.tv/aws)[](https://www.youtube.com/user/AmazonWebServices/Cloud/)[](https://aws.amazon.com/podcasts/?nc1=f_cc)[](https://pages.awscloud.com/communication-preferences?trk=homepage)

*   [Privacy](https://aws.amazon.com/privacy/?nc1=f_pr)
*   [Site terms](https://aws.amazon.com/terms/?nc1=f_pr)
*   [Your Privacy Choices](https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/#)
*   [Cookie Preferences](https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/#)

© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.