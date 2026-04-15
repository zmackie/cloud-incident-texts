---
title: Responding to an attack in AWS. A case study — Part 1
url: "https://awstip.com/responding-to-an-attack-in-aws-9048a1a551ac"
author: Invictus Incident Response
published: 2023-01-06
source_type: article
source_domain: awstip.com
cleanup_method: llm
---

# Responding to an attack in AWS


A case study — Part 1


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


![Image 7](https://miro.medium.com/v2/resize:fit:700/1*ylvcCyorVdQzq2CPipRUbQ.png)

**Analysis**At the start of an incident response engagement there’s often a known indicator or fact where you can start your investigation from. In this case it is the unknown account **DevOps3**. Remember we have to answer the following questions:

1.   When and how was the account created?
2.   What actions were performed with the account?
3.   Are there other traces of suspicious activity?

### When and how was the account created?

So let’s see if we can determine more about that account and its creation in the CloudTrail log. We will simply search for the account name and sort on the oldest event first to see what the first time this account was mentioned.


The first event we find related to the user is the **CreateUser**event which is to be expected for the first event for a new account. This log entry in CloudTrail contains a lot of information for our incident response.

> search used: index=name_of_index DevOps3 |table eventTime,eventName,requestParameters.userName,sourceIPAddress,sessionCredentialFromConsole,userIdentity.arn


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
