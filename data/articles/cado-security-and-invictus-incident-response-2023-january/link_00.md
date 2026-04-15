Title: Responding to an attack in AWS

URL Source: https://awstip.com/responding-to-an-attack-in-aws-9048a1a551ac

Published Time: 2023-01-06T11:47:02Z

Markdown Content:
# Responding to an attack in AWS. A case study — Part 1 | by Invictus Incident Response | AWS Tip

[Sitemap](https://awstip.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 1](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## AWS Tip](https://awstip.com/?source=post_page---publication_nav-b4c1e34ed5e-9048a1a551ac---------------------------------------)

·
Follow publication

[![Image 2: AWS Tip](https://miro.medium.com/v2/resize:fill:76:76/1*LXqMmX8rKuWEc3D_apZ1rQ.jpeg)](https://awstip.com/?source=post_page---post_publication_sidebar-b4c1e34ed5e-9048a1a551ac---------------------------------------)
Best AWS, DevOps, Serverless, and more from top Medium writers.

Follow publication

# Responding to an attack in AWS

[![Image 3: Invictus Incident Response](https://miro.medium.com/v2/resize:fill:64:64/1*F9s4GC6fkzA4zjWCkKYgbw.png)](https://invictus-ir.medium.com/?source=post_page---byline--9048a1a551ac---------------------------------------)

[Invictus Incident Response](https://invictus-ir.medium.com/?source=post_page---byline--9048a1a551ac---------------------------------------)

Follow

7 min read

·

Jan 6, 2023

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Faws-tip%2F9048a1a551ac&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&user=Invictus+Incident+Response&userId=e992e39417b7&source=---header_actions--9048a1a551ac---------------------clap_footer------------------)

26

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9048a1a551ac&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---header_actions--9048a1a551ac---------------------bookmark_footer------------------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D9048a1a551ac&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---header_actions--9048a1a551ac---------------------post_audio_button------------------)

Share

A case study — Part 1

Press enter or click to view image in full size

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*70yg7hHQARVXOZc02r0bqw.jpeg)

## Introduction

We are passionate about incident response in the cloud, therefore we decided to share some of our knowledge based on a recent IR case in AWS. This 3-part blog series is written by [Cado Security](https://www.cadosecurity.com/) and [Invictus Incident Response](https://invictus-ir.com/).

## Background

An incident was discovered during an account audit of the Amazon environment of a client. A new super user account was found and no one recognised it which triggered an incident. In this blog we will walk through the incident using cloud native logging and leveraging Cado Response platform for our investigation.

## Investigative questions

*   When was the account created?
*   How was the account created?
*   What actions were performed with the account?
*   Are there other traces of suspicious activity?

### Approach

We will follow the standard steps of the computer incident handling guide as a refresher there are four steps:

1.   Preparation
2.   **Acquisition**
3.   **Processing & Analysis**
4.   Post-Incident activity

For the purpose of this blog series we will focus on the two phases in bold, acquisition and processing & analysis.

**Acquisition**For acquisition of log data we use our open-source script Invictus-AWS ([GitHub](https://github.com/invictus-ir/Invictus-AWS)). Invictus-AWS can be run in an AWS organisation or AWS account to automatically enumerate the AWS configuration in use and the enabled logging. The script will also pull all the available logging within an AWS organisation/account. This script was executed and an S3 bucket was created containing all the available logs which looks like this:

![Image 5](https://miro.medium.com/v2/resize:fit:325/1*Gu5pOqfR-aD9oMxX8BcIKQ.png)

Invictus-AWS output

**Processing**As we can see in the picture above, there is default logging CloudTrail, but also additional logging such as VPC flow logs and S3 audit logging. To start our investigation we’ll first process the CloudTrail log for analysis. For analysis we use a combination of the jq**(**[GitHub](https://stedolan.github.io/jq/)**)**command line tool and Splunk([Website](http://splunk.com/)).

With jq we don’t need to parse the data, you can directly query json data. For example to open the CloudTrail log and to just see the EventTime and EventName we can use the following query:

> jq . cloudtrail.json

Press enter or click to view image in full size

![Image 6](https://miro.medium.com/v2/resize:fit:700/1*YZeEEwAtfIZav-iU2hS4Gw.png)

JQ can also do advanced filtering and searching, it’s very quick, however the query language can be a bit challenging and reading information from the console isn’t always the easiest for analysis. So let’s switch over to loading the logs in Splunk, we will use jq to manipulate our data to make sure Splunk understands it.

Step 1 — Extract CloudTrail event field

In the first step we will extract the CloudTrailEvent field from the Cloudtrail.json file. This field contains the whole event in json format.

> `cat cloudtrail.json| jq -r ‘.Events[].CloudTrailEvent’ > cloudtrailevents.json`

Step 2 — Load the events in Splunk

To load the json file in Splunk, set the sourcetype to _cloudtrail\_json_ and make sure to add the below in your **props.conf(**[reference](https://docs.splunk.com/Documentation/Splunk/Latest/Admin/Propsconf)**)** file to parse the CloudTrail events.

### props.conf ###

[cloudtrail_json]

DATETIME_CONFIG =

INDEXED_EXTRACTIONS = json

KV_MODE = none

LINE_BREAKER = ([\r\n]+)

NO_BINARY_CHECK = true

TIMESTAMP_FIELDS = eventTime

disabled = false

pulldown_type = true
Once you’ve loaded in your data it should look similar to this:

Press enter or click to view image in full size

![Image 7](https://miro.medium.com/v2/resize:fit:700/1*ylvcCyorVdQzq2CPipRUbQ.png)

**Analysis**At the start of an incident response engagement there’s often a known indicator or fact where you can start your investigation from. In this case it is the unknown account **DevOps3**. Remember we have to answer the following questions:

1.   When and how was the account created?
2.   What actions were performed with the account?
3.   Are there other traces of suspicious activity?

### When and how was the account created?

So let’s see if we can determine more about that account and its creation in the CloudTrail log. We will simply search for the account name and sort on the oldest event first to see what the first time this account was mentioned.

## Get Invictus Incident Response’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

- [x] 

Remember me for faster sign in

 

The first event we find related to the user is the **CreateUser**event which is to be expected for the first event for a new account. This log entry in CloudTrail contains a lot of information for our incident response.

> search used: index=name_of_index DevOps3 |table eventTime,eventName,requestParameters.userName,sourceIPAddress,sessionCredentialFromConsole,userIdentity.arn

Press enter or click to view image in full size

![Image 8](https://miro.medium.com/v2/resize:fit:700/1*7z92n4EkjJ1QX-O_WmlhDQ.png)

We can see the name of the newly created user account in the requestParameters.userName and the userIdentity.arn that requested this account to be created. The field **sessionCredentialFromConsole** is set to true meaning this account was created from the AWS management console ([reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html)). We can also see the user account **DevOps1-bpvpb**and the associated access key that created this account. After our initial search we can answer the first two investigative questions:

**When was the account created?**

Creation Time: 26–10–2022 at 21:29:03 

(all times in CloudTrail are in UTC)

**How was the account created?**Created by: DevOps1-bpvbp

Creation method: AWS management console

Let’s dig in a bit more on the account that created the account. Because the creation of the account was performed through the management console the logs don’t show the external IP address used for this action. But we do know the activity occured from the management consolse. In AWS we can filter specifically on management console logins. If we filter on eventName=ConsoleLogin ([reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html)) with account DevOps1-bpvpb we see the following event 6 minutes prior to the creation of the new account:

> search used: index=name_of_index eventName=ConsoleLogin DevOps1-bpvbp

Press enter or click to view image in full size

![Image 9](https://miro.medium.com/v2/resize:fit:700/1*Y20B3yzOcIaK4ZiyBcISZA.png)

The most relevant fields have been underlined, we can see that this user did not have MFA enabled. We can also see the source IP address from where the user logged in on the console. Now we have a more clear picture on what has happened:

Creation Time: 26–10–2022 at 21:29:03 

Created by: DevOps1-bpvbp

Creation method: AWS management console

IP-address used: 185.195.232.111

### What actions were performed with the account?

Now we can try to determine what activities occurred with the newly created account. To get an idea on what activity occurred within an AWS environment we can search for the user account and create a table of the eventNames generated in CloudTrail for this account.

> search used: index=name_of_index devops3 |stats count by eventName

Press enter or click to view image in full size

![Image 10](https://miro.medium.com/v2/resize:fit:700/0*Erx7zn2H4CK3cdq1)

There’s only one event related to that account, which is its creation. At this point we are able to answer the third investigation question. At this point it’s guessing what the threat actors intentions are for the newly created account, one of the options is to use it as a persistence method.

**What actions were performed with the account?**No actions performed with the DevOps3 account

### Are there other traces of suspicious activity?

Let’s now switch over to analysing the activity of DevOps1-bpvbp, the account that created DevOps3 to determine if there’s additional suspicious activity using this account.

The first step is searching for activity for that account around the timeperiod of the attack:

> `search used: index=name_of_index DevOps1-bpvbp |table _time, eventSource,eventName,userIdentity.arn`

So within the same minute that the user account DevOps3 was created a StartSession([reference](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartSession.html)) event was recorded with the same account.

> StartSession, initiates a connection to a target (for example, a managed node) for a Session Manager session. Returns a URL and token that can be used to open a WebSocket connection for sending input and receiving outputs.

When we inspect the event we can see additional details as to what happened:

![Image 11](https://miro.medium.com/v2/resize:fit:445/1*wYrRoZhwnRvBWMWYBc1WaA.png)

Based on the event we can conclude that a session was started from the account DevOps1-bpvbp towards an instance with identifier i-08e56d6b6c0439daf. Again this activity occurred from within the management console, that’s why we can’t use the source IP address to find this event. At this point in our investigation we are going to investigate what happened on that specific instance to determine if this is malicious activity. We can no longer rely on just the CloudTrail logs as they don’t record all activity that occur from within a host.

Coming soon… part 2, where we will start investigating the instance with the Cado Security platform.

**PS:**The AWS account ID and the source IP address were changed for the screenshots in this blog.

## About Cado Security

Cado Security is _the_ cloud investigation and response automation company. The Cado platform leverages the scale, speed and automation of the cloud to effortlessly deliver forensic-level detail into cloud, container and serverless environments.

## About Invictus Incident Response

We are an incident response company specialised in supporting organisations facing a cyber attack. We help our clients stay undefeated!

[🆘](https://emojikeyboard.org/copy/SOS_Sign_Emoji_%F0%9F%86%98) Incident Response support reach out to cert@invictus-ir.com or go to [https://www.invictus-ir.com/247](https://www.invictus-ir.com/247)

[📧](https://emojikeyboard.org/copy/E-Mail_Symbol_Emoji_%F0%9F%93%A7) Questions or suggestions contact us at info@invictus-ir.com

[AWS](https://medium.com/tag/aws?source=post_page-----9048a1a551ac---------------------------------------)

[Cloud Security](https://medium.com/tag/cloud-security?source=post_page-----9048a1a551ac---------------------------------------)

[Incident Response](https://medium.com/tag/incident-response?source=post_page-----9048a1a551ac---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----9048a1a551ac---------------------------------------)

[Cloudtrail](https://medium.com/tag/cloudtrail?source=post_page-----9048a1a551ac---------------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Faws-tip%2F9048a1a551ac&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&user=Invictus+Incident+Response&userId=e992e39417b7&source=---footer_actions--9048a1a551ac---------------------clap_footer------------------)

26

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Faws-tip%2F9048a1a551ac&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&user=Invictus+Incident+Response&userId=e992e39417b7&source=---footer_actions--9048a1a551ac---------------------clap_footer------------------)

26

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9048a1a551ac&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---footer_actions--9048a1a551ac---------------------bookmark_footer------------------)

[![Image 12: AWS Tip](https://miro.medium.com/v2/resize:fill:96:96/1*LXqMmX8rKuWEc3D_apZ1rQ.jpeg)](https://awstip.com/?source=post_page---post_publication_info--9048a1a551ac---------------------------------------)

[![Image 13: AWS Tip](https://miro.medium.com/v2/resize:fill:128:128/1*LXqMmX8rKuWEc3D_apZ1rQ.jpeg)](https://awstip.com/?source=post_page---post_publication_info--9048a1a551ac---------------------------------------)

Follow

[## Published in AWS Tip](https://awstip.com/?source=post_page---post_publication_info--9048a1a551ac---------------------------------------)

[11.6K followers](https://awstip.com/followers?source=post_page---post_publication_info--9048a1a551ac---------------------------------------)

·[Last published 2 days ago](https://awstip.com/building-an-automated-aws-security-advisor-rag-with-aws-bedrock-and-opensearch-serverless-43941ab13024?source=post_page---post_publication_info--9048a1a551ac---------------------------------------)

Best AWS, DevOps, Serverless, and more from top Medium writers.

Follow

[![Image 14: Invictus Incident Response](https://miro.medium.com/v2/resize:fill:96:96/1*F9s4GC6fkzA4zjWCkKYgbw.png)](https://invictus-ir.medium.com/?source=post_page---post_author_info--9048a1a551ac---------------------------------------)

[![Image 15: Invictus Incident Response](https://miro.medium.com/v2/resize:fill:128:128/1*F9s4GC6fkzA4zjWCkKYgbw.png)](https://invictus-ir.medium.com/?source=post_page---post_author_info--9048a1a551ac---------------------------------------)

Follow

[## Written by Invictus Incident Response](https://invictus-ir.medium.com/?source=post_page---post_author_info--9048a1a551ac---------------------------------------)

[630 followers](https://invictus-ir.medium.com/followers?source=post_page---post_author_info--9048a1a551ac---------------------------------------)

·[1 following](https://medium.com/@invictus-ir/following?source=post_page---post_author_info--9048a1a551ac---------------------------------------)

We are an incident response company specialised in supporting organisations facing a cyber attack. We help our clients stay undefeated!

Follow

## Responses (1)

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--9048a1a551ac---------------------------------------)

![Image 16](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---post_responses--9048a1a551ac---------------------respond_sidebar------------------)

Cancel

Respond

[![Image 17: Akshay Chauhan](https://miro.medium.com/v2/resize:fill:32:32/1*JMemMl6tBgVLLDVpg04yWg.jpeg)](https://medium.com/@axayyk.?source=post_page---post_responses--9048a1a551ac----0-----------------------------------)

[Akshay Chauhan](https://medium.com/@axayyk.?source=post_page---post_responses--9048a1a551ac----0-----------------------------------)

[Feb 4, 2025](https://medium.com/@axayyk./very-informative-thanks-for-sharing-fc516fa74847?source=post_page---post_responses--9048a1a551ac----0-----------------------------------)

Very Informative!!! Thanks for Sharing.

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Ffc516fa74847&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40axayyk.%2Fvery-informative-thanks-for-sharing-fc516fa74847&user=Akshay+Chauhan&userId=2d08d7cf7ab2&source=---post_responses--fc516fa74847----0-----------------respond_sidebar------------------)

--

Reply

## More from Invictus Incident Response and AWS Tip

![Image 18: Email Forwarding Rules in Microsoft 365](https://miro.medium.com/v2/resize:fit:679/format:webp/1*Aa8QGNL_tSJ5LHax2BY2dg.png)

[![Image 19: Invictus Incident Response](https://miro.medium.com/v2/resize:fill:20:20/1*F9s4GC6fkzA4zjWCkKYgbw.png)](https://invictus-ir.medium.com/?source=post_page---author_recirc--9048a1a551ac----0---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[Invictus Incident Response](https://invictus-ir.medium.com/?source=post_page---author_recirc--9048a1a551ac----0---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[## Email Forwarding Rules in Microsoft 365 ### The ultimate guide to analysing and understanding email forwarding rules in the Unified Audit Log (UAL)](https://invictus-ir.medium.com/email-forwarding-rules-in-microsoft-365-295fcb63d4fb?source=post_page---author_recirc--9048a1a551ac----0---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

Feb 20, 2023

[1](https://invictus-ir.medium.com/email-forwarding-rules-in-microsoft-365-295fcb63d4fb?source=post_page---author_recirc--9048a1a551ac----0---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---author_recirc--9048a1a551ac----0-----------------explicit_signal----1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F295fcb63d4fb&operation=register&redirect=https%3A%2F%2Finvictus-ir.medium.com%2Femail-forwarding-rules-in-microsoft-365-295fcb63d4fb&source=---author_recirc--9048a1a551ac----0-----------------bookmark_preview----1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

![Image 20: I Used HashMaps Every Day for 4 Years. Then Google Asked Me One Question and I Had Nothing.](https://miro.medium.com/v2/resize:fit:679/format:webp/1*_Jx2wtXeXTQGMJyhmaeb5w.png)

[![Image 21: AWS Tip](https://miro.medium.com/v2/resize:fill:20:20/1*LXqMmX8rKuWEc3D_apZ1rQ.jpeg)](https://awstip.com/?source=post_page---author_recirc--9048a1a551ac----1---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

In

[AWS Tip](https://awstip.com/?source=post_page---author_recirc--9048a1a551ac----1---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

by

[The Speedcraft Lab](https://medium.com/@speedcraft21?source=post_page---author_recirc--9048a1a551ac----1---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[## I Used HashMaps Every Day for 4 Years. Then Google Asked Me One Question and I Had Nothing. ### Four years of daily use and I never once looked inside it. Here’s what the silence on that call taught me about the difference between…](https://awstip.com/i-used-hashmaps-every-day-for-4-years-then-google-asked-me-one-question-and-i-had-nothing-cda4e050d1ba?source=post_page---author_recirc--9048a1a551ac----1---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

Mar 16

[16](https://awstip.com/i-used-hashmaps-every-day-for-4-years-then-google-asked-me-one-question-and-i-had-nothing-cda4e050d1ba?source=post_page---author_recirc--9048a1a551ac----1---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---author_recirc--9048a1a551ac----1-----------------explicit_signal----1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcda4e050d1ba&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fi-used-hashmaps-every-day-for-4-years-then-google-asked-me-one-question-and-i-had-nothing-cda4e050d1ba&source=---author_recirc--9048a1a551ac----1-----------------bookmark_preview----1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

![Image 22: Amazon Data Engineer Interview Question — Data Engineer III](https://miro.medium.com/v2/resize:fit:679/format:webp/1*V3SPk2OZJYiiPPnBidZf2A.jpeg)

[![Image 23: AWS Tip](https://miro.medium.com/v2/resize:fill:20:20/1*LXqMmX8rKuWEc3D_apZ1rQ.jpeg)](https://awstip.com/?source=post_page---author_recirc--9048a1a551ac----2---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

In

[AWS Tip](https://awstip.com/?source=post_page---author_recirc--9048a1a551ac----2---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

by

[Mohit Daxini](https://medium.com/@mohitdaxini75?source=post_page---author_recirc--9048a1a551ac----2---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[## Amazon Data Engineer Interview Question — Data Engineer III ### Modern data-driven applications often allow users to filter data dynamically. Whether it’s an e-commerce dashboard, analytics platform, or…](https://awstip.com/amazon-data-engineer-interview-question-data-engineer-iii-a6b8201ab6dc?source=post_page---author_recirc--9048a1a551ac----2---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

Mar 18

[](https://awstip.com/amazon-data-engineer-interview-question-data-engineer-iii-a6b8201ab6dc?source=post_page---author_recirc--9048a1a551ac----2---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---author_recirc--9048a1a551ac----2-----------------explicit_signal----1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa6b8201ab6dc&operation=register&redirect=https%3A%2F%2Fawstip.com%2Famazon-data-engineer-interview-question-data-engineer-iii-a6b8201ab6dc&source=---author_recirc--9048a1a551ac----2-----------------bookmark_preview----1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

![Image 24: Automated Forensic analysis of Google Workspace](https://miro.medium.com/v2/resize:fit:679/format:webp/0d702cbfe9920e00e94464660874e97b36b08e18a7844ad35d0d5cd2de2ef897)

[![Image 25: Invictus Incident Response](https://miro.medium.com/v2/resize:fill:20:20/1*F9s4GC6fkzA4zjWCkKYgbw.png)](https://invictus-ir.medium.com/?source=post_page---author_recirc--9048a1a551ac----3---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[Invictus Incident Response](https://invictus-ir.medium.com/?source=post_page---author_recirc--9048a1a551ac----3---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[## Automated Forensic analysis of Google Workspace ### Follow us | LinkedIn | Twitter |GitHub](https://invictus-ir.medium.com/automated-forensic-analysis-of-google-workspace-859ed50c5c92?source=post_page---author_recirc--9048a1a551ac----3---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

Aug 16, 2022

[](https://invictus-ir.medium.com/automated-forensic-analysis-of-google-workspace-859ed50c5c92?source=post_page---author_recirc--9048a1a551ac----3---------------------1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---author_recirc--9048a1a551ac----3-----------------explicit_signal----1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F859ed50c5c92&operation=register&redirect=https%3A%2F%2Finvictus-ir.medium.com%2Fautomated-forensic-analysis-of-google-workspace-859ed50c5c92&source=---author_recirc--9048a1a551ac----3-----------------bookmark_preview----1aa72ae2_f6e1_4b69_8fa0_60cf2919cc37--------------)

[See all from Invictus Incident Response](https://invictus-ir.medium.com/?source=post_page---author_recirc--9048a1a551ac---------------------------------------)

[See all from AWS Tip](https://awstip.com/?source=post_page---author_recirc--9048a1a551ac---------------------------------------)

## Recommended from Medium

![Image 26: Don’t Become a DevOps Engineer in 2026!](https://miro.medium.com/v2/resize:fit:679/format:webp/1*jbajxX_SZsz_WdtxVW1Xtw.png)

[![Image 27: Dhanush N](https://miro.medium.com/v2/resize:fill:20:20/1*g-aoUi88UKMpAxezY9NcmQ.png)](https://dhanushnehru.medium.com/?source=post_page---read_next_recirc--9048a1a551ac----0---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[Dhanush N](https://dhanushnehru.medium.com/?source=post_page---read_next_recirc--9048a1a551ac----0---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[## Don’t Become a DevOps Engineer in 2026! ### Stop writing YAML. Stop babysitting pipelines. The game has fundamentally changed.](https://dhanushnehru.medium.com/dont-become-a-devops-engineer-in-2026-f2e94541e700?source=post_page---read_next_recirc--9048a1a551ac----0---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

Mar 2

[18](https://dhanushnehru.medium.com/dont-become-a-devops-engineer-in-2026-f2e94541e700?source=post_page---read_next_recirc--9048a1a551ac----0---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---read_next_recirc--9048a1a551ac----0-----------------explicit_signal----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff2e94541e700&operation=register&redirect=https%3A%2F%2Fdhanushnehru.medium.com%2Fdont-become-a-devops-engineer-in-2026-f2e94541e700&source=---read_next_recirc--9048a1a551ac----0-----------------bookmark_preview----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

![Image 28: How to Master AWS Security in 2026](https://miro.medium.com/v2/resize:fit:679/format:webp/1*Em7z67Y5AZ9xtH6JSsfuAg.png)

[![Image 29: Taimur Ijlal](https://miro.medium.com/v2/resize:fill:20:20/1*MGJd3DuWu5hAKz0H2bxEig.png)](https://taimurcloud123.medium.com/?source=post_page---read_next_recirc--9048a1a551ac----1---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[Taimur Ijlal](https://taimurcloud123.medium.com/?source=post_page---read_next_recirc--9048a1a551ac----1---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[## How to Master AWS Security in 2026 ### How to go from zero to AWS security expert — without chasing services or certs](https://taimurcloud123.medium.com/how-to-master-aws-security-in-2026-aa92a4a995b4?source=post_page---read_next_recirc--9048a1a551ac----1---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

Dec 20, 2025

[3](https://taimurcloud123.medium.com/how-to-master-aws-security-in-2026-aa92a4a995b4?source=post_page---read_next_recirc--9048a1a551ac----1---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---read_next_recirc--9048a1a551ac----1-----------------explicit_signal----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Faa92a4a995b4&operation=register&redirect=https%3A%2F%2Ftaimurcloud123.medium.com%2Fhow-to-master-aws-security-in-2026-aa92a4a995b4&source=---read_next_recirc--9048a1a551ac----1-----------------bookmark_preview----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

![Image 30: The Bug Bounty Automation Stack That Can Generate $10K+ (Open Source Tools Only)](https://miro.medium.com/v2/resize:fit:679/format:webp/1*LDxbtzfpSDt7WwGGCjRdhw.png)

[![Image 31: System Weakness](https://miro.medium.com/v2/resize:fill:20:20/1*gncXIKhx5QOIX0K9MGcVkg.jpeg)](https://systemweakness.com/?source=post_page---read_next_recirc--9048a1a551ac----0---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

In

[System Weakness](https://systemweakness.com/?source=post_page---read_next_recirc--9048a1a551ac----0---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

by

[BugHunter’s Journal](https://medium.com/@bughuntersjournal?source=post_page---read_next_recirc--9048a1a551ac----0---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[## The Bug Bounty Automation Stack That Can Generate $10K+ (Open Source Tools Only) ### Automation doesn’t find bugs. Automated workflows combined with manual validation do. While beginners waste time running Nuclei on random…](https://systemweakness.com/the-bug-bounty-automation-stack-that-can-generate-10k-open-source-tools-only-93ed3e8b3ee7?source=post_page---read_next_recirc--9048a1a551ac----0---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

Dec 17, 2025

[5](https://systemweakness.com/the-bug-bounty-automation-stack-that-can-generate-10k-open-source-tools-only-93ed3e8b3ee7?source=post_page---read_next_recirc--9048a1a551ac----0---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---read_next_recirc--9048a1a551ac----0-----------------explicit_signal----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F93ed3e8b3ee7&operation=register&redirect=https%3A%2F%2Fsystemweakness.com%2Fthe-bug-bounty-automation-stack-that-can-generate-10k-open-source-tools-only-93ed3e8b3ee7&source=---read_next_recirc--9048a1a551ac----0-----------------bookmark_preview----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

![Image 32: If You Understand These 5 AI Terms, You’re Ahead of 90% of People](https://miro.medium.com/v2/resize:fit:679/format:webp/1*qbVrf-wO9PYtthAj6E4RYQ.png)

[![Image 33: Towards AI](https://miro.medium.com/v2/resize:fill:20:20/1*JyIThO-cLjlChQLb6kSlVQ.png)](https://pub.towardsai.net/?source=post_page---read_next_recirc--9048a1a551ac----1---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

In

[Towards AI](https://pub.towardsai.net/?source=post_page---read_next_recirc--9048a1a551ac----1---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

by

[Shreyas Naphad](https://medium.com/@shreyasnaphad?source=post_page---read_next_recirc--9048a1a551ac----1---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[## If You Understand These 5 AI Terms, You’re Ahead of 90% of People ### Master the core ideas behind AI without getting lost](https://pub.towardsai.net/if-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319?source=post_page---read_next_recirc--9048a1a551ac----1---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

Mar 29

[202](https://pub.towardsai.net/if-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319?source=post_page---read_next_recirc--9048a1a551ac----1---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---read_next_recirc--9048a1a551ac----1-----------------explicit_signal----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc7622d353319&operation=register&redirect=https%3A%2F%2Fpub.towardsai.net%2Fif-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319&source=---read_next_recirc--9048a1a551ac----1-----------------bookmark_preview----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

![Image 34: AWS Billed Us an Extra $4,200 Last Quarter. Here Are the 3 Charges Nobody Warned Us About.](https://miro.medium.com/v2/resize:fit:679/format:webp/1*7Tz8RO6bUk3KmECPaOi2nw.png)

[![Image 35: That Infrastructure Guy](https://miro.medium.com/v2/resize:fill:20:20/1*rv1Cq9w7HsmGX7A6asAd4g.jpeg)](https://medium.com/that-infrastructure-guy?source=post_page---read_next_recirc--9048a1a551ac----2---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

In

[That Infrastructure Guy](https://medium.com/that-infrastructure-guy?source=post_page---read_next_recirc--9048a1a551ac----2---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

by

[Heinan Cabouly](https://medium.com/@heinancabouly?source=post_page---read_next_recirc--9048a1a551ac----2---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[## AWS Billed Us an Extra $4,200 Last Quarter. Here Are the 3 Charges Nobody Warned Us About. ### And one of them just doubled in March 2026.](https://medium.com/that-infrastructure-guy/aws-billed-us-an-extra-4-200-last-quarter-here-are-the-3-charges-nobody-warned-us-about-e95fbcaef87e?source=post_page---read_next_recirc--9048a1a551ac----2---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

Apr 7

[2](https://medium.com/that-infrastructure-guy/aws-billed-us-an-extra-4-200-last-quarter-here-are-the-3-charges-nobody-warned-us-about-e95fbcaef87e?source=post_page---read_next_recirc--9048a1a551ac----2---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---read_next_recirc--9048a1a551ac----2-----------------explicit_signal----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fe95fbcaef87e&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthat-infrastructure-guy%2Faws-billed-us-an-extra-4-200-last-quarter-here-are-the-3-charges-nobody-warned-us-about-e95fbcaef87e&source=---read_next_recirc--9048a1a551ac----2-----------------bookmark_preview----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

![Image 36: AWS Security Agent-Penetration Testing Overview](https://miro.medium.com/v2/resize:fit:679/format:webp/1*k_Dy0HjTRluVKOyd6w2idQ.png)

[![Image 37: AWS in Plain English](https://miro.medium.com/v2/resize:fill:20:20/1*6EeD87OMwKk-u3ncwAOhog.png)](https://aws.plainenglish.io/?source=post_page---read_next_recirc--9048a1a551ac----3---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

In

[AWS in Plain English](https://aws.plainenglish.io/?source=post_page---read_next_recirc--9048a1a551ac----3---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

by

[Sena Yakut](https://senayakut.com/?source=post_page---read_next_recirc--9048a1a551ac----3---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[## AWS Security Agent-Penetration Testing Overview ### AWS Security Agent-Penetration Testing Overview](https://aws.plainenglish.io/aws-security-agent-penetration-testing-overview-e05cc62ce4f6?source=post_page---read_next_recirc--9048a1a551ac----3---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

Jan 10

[3](https://aws.plainenglish.io/aws-security-agent-penetration-testing-overview-e05cc62ce4f6?source=post_page---read_next_recirc--9048a1a551ac----3---------------------69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-9048a1a551ac&source=---read_next_recirc--9048a1a551ac----3-----------------explicit_signal----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fe05cc62ce4f6&operation=register&redirect=https%3A%2F%2Faws.plainenglish.io%2Faws-security-agent-penetration-testing-overview-e05cc62ce4f6&source=---read_next_recirc--9048a1a551ac----3-----------------bookmark_preview----69f3bb6c_c98a_45d6_b18d_9914f0613f00--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--9048a1a551ac---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----9048a1a551ac---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----9048a1a551ac---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9048a1a551ac---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9048a1a551ac---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----9048a1a551ac---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9048a1a551ac---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----9048a1a551ac---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9048a1a551ac---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----9048a1a551ac---------------------------------------)