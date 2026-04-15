---
title: Auditing identity activity for NOBELIUM and MagicWeb in AWS
url: "https://www.clearvector.com/blog/auditing-identity-activity-for-nobelium-and-magicweb-in-aws/"
author: John Laliberte, Andrew Davis, Phil Puleo
published: 2022-08-25
source_type: article
source_domain: www.clearvector.com
cleanup_method: llm
---

# Auditing identity activity for NOBELIUM and MagicWeb in AWS

Security

# Auditing identity activity for NOBELIUM and MagicWeb in AWS

Aug 25, 2022 • min read

![Image 35](https://cdn.prod.website-files.com/68b89f4a45c21a6505438dba/68f6c3d175270baedb7cc9ba_2022082501.cv.door.avif)

Earlier this week [Microsoft researchers](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/?ref=www.clearvector.com/blog) discovered NOBELIUM abusing identities and credentialed access to maintain persistence and facilitate covert access. In AWS environments, the [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html?ref=www.clearvector.com/blog) (formerly AWS SSO), enables customers to use ADFS as an identity source (an external identity provider (IdP)).

If you have an AWS environment with ADFS configured as your IdP, and NOBELIUM compromised your ADFS server with MagicWeb, NOBELIUM may have moved laterally into your AWS environment at some point, masquerading as one of your valid users to perform further malicious activity and persist indefinitely.

## Our recommendation

In addition to following the guidance from Microsoft, ClearVector recommends additional actions if you have, or if you are not sure if you have, an AWS environment with ADFS configured as your IdP. ClearVector recommends additional actions in two main areas:

1.   Review your identity source configuration in the AWS IAM Identity Center
2.   Audit high risk activity in AWS for all ADFS users

### Manual review process

**_Review identity source configuration in the IAM Identity Center_**

1.   Log in and navigate to the IAM Identity Center
2.   Click Settings -> Identity source -> Actions -> Manage authentication
3.   Review the identity provider metadata and SAML certificates
    1.   In the identity provider metadata field:
        1.   IdP sign-in URL: Typical value ends in /adfs/ls
        2.   IdP issuer URL: Typical value ends in /adfs/services/trust

    2.   In the "Manage SAML 2.0 certificates" section, there may be references to a CN of ADFS signing

Figure 1 shows example settings from the IAM Identity Center.

![Image 36](https://cdn.prod.website-files.com/68b89f4a45c21a6505438dba/68f6c3e4091bfe8c61ec573b_2022082407.settings.avif)

**_Figure 1 - Example settings for ADFS in the IAM Identity Center_**

**_Search for and audit high risk activity for all ADFS users_**

This process will vary based on your own internal processes. If you store CloudTrail data, ClearVector recommends manually searching and correlating in three main areas:

1.   Find the roles used by AWS SSO, both current and historic
    1.   Note that finding the historic (deleted) roles are not easily found by calling an API. This typically requires analysis of data over time as roles could now be deleted.
    2.   These roles typically start with "AWSReservedSSO_", followed by the permission set name and further specific identifiers
    3.   The roles typically have an ARN similar to:
        1.   arn:aws:iam::_aws account id_:role/aws-reserved/sso.amazonaws.com/AWSReservedSSO__

2.   Correlate who (users) from ADFS assumed the AWS SSO roles both current and historic
    1.   Note that finding who (users) historically assumed roles is not easily found by calling an API. This typically requires analysis of data over time as users could now be deleted.
    2.   The names and ARNs of these users depend on the specifics of the SAML, ADFS, and SSO setup. Therefore, one method is to audit and correlate the use of the API call AssumeRoleWithSAML.

3.   Manually review what activity might be malicious
    1.   This involves manual review and analysis of all activity performed by the ADFS users (#1 above) and any roles assumed by these users (#2 above). This analysis may extend beyond the control plane, and must include activity within the IAM Identity Center itself.

### Review process with ClearVector

[ClearVector](https://www.clearvector.com/)is purpose-built to make the adversary's job extremely difficult and enable realtime intelligence and control over the identities operating in your environment. Especially in situations where attacks are identity-driven, such as this NOBELIUM backdoor, [Lapsus$](https://en.wikipedia.org/wiki/Lapsus$?ref=www.clearvector.com/blog), or the [Cisco Talos breach](https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html?ref=www.clearvector.com/blog), traditional detection and response does not work. Although you can remove the backdoor, you still need to quickly go back in time, determine what the attacker did, and isolate the activity.

Using our [CloudDVR capability](https://www.clearvector.com/solutions/detection-and-response-teams), Figure 2 shows a possible NOBELIUM actor using credentials obtained for an ADFS user through MagicWeb, over a ~20 minute interval. Our identity engine makes it easy to see that this actor logged into AWS via the ADFS IdP and blocked all future executions of a Lambda function, causing a DoS for the business. In addition, our risk engine flagged this activity as a high notification to review. If configured within ClearVector, you would also see this notification in Slack or Teams.

![Image 37](https://cdn.prod.website-files.com/68b89f4a45c21a6505438dba/68f6c3e4091bfe8c61ec573f_2022082405.entity.avif)

**_Figure 2 - Activity for an ADFS user in AWS in ClearVector_**

This post will be updated as we learn any additional relevant information. **Do not hesitate to**[**reach out**](https://www.clearvector.com/company/contact) if you need help analyzing the ADFS activity in your AWS environment!

‍
