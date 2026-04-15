---
title: Responding to an attack in AWS
url: "https://awstip.com/responding-to-an-attack-in-aws-dae857806aa7"
author: Invictus Incident Response
published: 2023-01-19
source_type: article
source_domain: awstip.com
cleanup_method: llm
---

# Responding to an attack in AWS

A case study — Part 2


![Image 4](https://miro.medium.com/v2/resize:fit:700/1*5f1q3KOZ674EW7JG2DgS6A.jpeg)

## Introduction

This is the second of a three-part blog series written by [Cado Security](https://www.cadosecurity.com/) and [Invictus Incident Response](https://invictus-ir.com/), where we are investigating an incident that was discovered during an account audit of an Amazon environment.

## Background

In part [one](https://medium.com/aws-tip/responding-to-an-attack-in-aws-9048a1a551ac), we’ve shown through the analysis of AWS logs that account DevOps1-bpvbp had been used to create an unknown account DevOps3 on 26 Oct 2022 at 21:29:03 UTC. Additionally the DevOps1-bpvbp account had initiated a StartSession which provided a connection to EC2 instance i-08e56d6b6c0439daf using Session Manager, at 21:29:53 UTC.

## Investigative Questions

We will continue the investigation analysis to answer the following questions:

*   What actions were performed on the host?
*   Are there other traces of suspicious activity?

## Approach

As mentioned in the previous blog, we are focusing on the phases **Acquisition** and **Processing & Analysis** steps. Using Cado Response those phases look more like **Acquisition & Processing** and **Analysis**

## Acquisition & Processing

To start off using the Cado platform, investigations are compartmentalised as Projects, using the UI for the platform we created a project and acquired EC2 instance i-08e56d6b6c0439daf.


![Image 5](https://miro.medium.com/v2/resize:fit:700/0*_zxf-98VefGvKAJO)

Cado Response acquisition

A disk image is created from a snapshot of the volume attached to the instance _i-08e56d6b6c0439daf_ and automatically processed giving the analyst access to a super timeline and file content.

## Analysis

From previous analysis, we know that the AWS Session Manager initiated session took place at 2022–10–26 21:29:03, so that will be the pivot point.

As this is a Linux system we will start with the _secure_ log file, the file shows that between Oct 26 21:29:53 and Oct 26 21:36:03 there was activity for the users ssm-user and ec2-user. ssm-user is the user account associated with SSM Session Manager and ec2-user is the default user for Amazon Linux systems and the time of the account being accessed lines up with the log analysis.

_secure_ log shows session start and session close timestamps:

![Image 6](https://miro.medium.com/v2/resize:fit:700/1*m1EnzOFZ74sBNDby5xBGOg.png)

Linux secure log

Now we have a time window of interest. Using the search function in Cado paltform, we want to see what activity took place on _i-08e56d6b6c0439daf_ between Oct 26 21:29:53 and Oct 26 21:36:03 so let’s add a timestamp range 2022–10–26 21:28:00 to 2022–10–26 21:38:00 to the search:

![Image 7](https://miro.medium.com/v2/resize:fit:700/0*UrL2P5qVoKjAQuAE)

AWS SSM generates quite a lot of log events which results in a lot of noise so we removed those entries from the timeline search, reducing the number of events from 227 to 57:

![Image 8](https://miro.medium.com/v2/resize:fit:700/0*ZTk7QCtuV7ncatvT)

Along with the _secure_ log, the _audit_ log tracks user logon activity, here we can see the ssm-user is linked to audit entry USER_ACCT which is triggered when a user-space user account is modified.

![Image 9](https://miro.medium.com/v2/resize:fit:700/0*4hMoSIYSv5_DUwEF)

So our Investigative Questions are:

*   What actions were performed on the host?
*   Are there other traces of suspicious activity?

Timeline Analysis and file content can help answer these questions.

![Image 10](https://miro.medium.com/v2/resize:fit:700/0*njlb66o24Dxranlt)

Between 21:29:53 and 21:36:04 we have events that show an AWS SSM interactive session had started; the associated ssm-user switched user to the default Amazon Linux2 account ec2-user which initiated a new bash session. All of this takes place under the process ID 32627 directly linking the ssm-user and ec2-user accounts to the attacker activity. The ec2-user _known-hosts_ file was accessed and a file named staff.txt was created in the ec2-user’s default directory.

Next step is to review the _bash\_history_ files for ssm-user and ec2-user to identify any commands the attacker has executed.

![Image 11](https://miro.medium.com/v2/resize:fit:700/0*1taOdzz4jP1FNuM_)

The screenshot above is from using the Cado platform to view the contents of ssm-user’s _bash\_history_ file. The command seen within the file doesn’t have an associated timestamp, however, in our timeline there is log evidence that indicates that sudo command was executed to switch user to ec2-user during the attacker’s session.

![Image 12](https://miro.medium.com/v2/resize:fit:700/0*bb6c9qJRrdcqabBL)

The screenshot above shows the contents of ec2-user’s _bash\_history_ file. Again, the commands seen within the file don’t have timestamps, however in our timeline we did see the ec2-user’s _known\_hosts_ file being accessed, so there is a good indication the ssh commands are linked to the attacker’s session. Also in our timeline we can see the file staff.txt was created during the attacker’s session which is likely to be the result of the scp command.

The other commands seen at the beginning and end of of the bash_history file are also interesting:

![Image 13](https://miro.medium.com/v2/resize:fit:700/1*odc3f0JwSBsaMeEsCFrJkA.png)

The first command in the code box above, shows the Instance MetaData Service (IMDS) being used to extract information regarding the Virtual Private Cloud (VPC) Id. The VPC Id is then used in conjunction with the aws command line tool to provide detailed information of the security group that the instance belongs to, in particular looking for port 22 entries, port 22 is commonly associated with SSH. This could be seen as a method to perform network discovery to find other hosts that can be used for lateral movement.

The last two commands in the bash_history file:

![Image 14](https://miro.medium.com/v2/resize:fit:700/1*lFiUQjyXdhayajjG_iceSg.png)

show the aws command line to create a S3 bucket and the file staff.txt was copied to it. This could be seen as staging data for exfiltration.

Our analysis of _i-08e56d6b6c0439daf_ has found that the scope of our investigation has extended to another system within the network, 10.0.8.25, using the AWS console we identified that within the Security Group that IP address corresponds to an EC2 instance with ID _i-020e722274233c7f2_ and our Investigative Questions carry over to that host:

*   What actions were performed on the host?
*   Are there other traces of suspicious activity?

Again we start the analysis again with the _secure_ log file:

![Image 15](https://miro.medium.com/v2/resize:fit:700/1*8pY5rPnxvSXujgA7ViPLUg.png)

We can see the timings for the ssh connection line up with the findings from our analysis of _i-08e56d6b6c0439daf_.

Using the same time window and a filter to show LOGIN and USER from the audit log along with the rest of the system and user events gives 53 events for further analysis.

Due to the configuration of this system, user executed commands are saved to the audit log, the commands are HEX encoded and the Cado platform automatically decodes them to the attacker executed the following commands:

![Image 16](https://miro.medium.com/v2/resize:fit:700/0*mM00eMOrAOQQLbmi)

![Image 17](https://miro.medium.com/v2/resize:fit:700/1*89XNhaP0NyYHTL-ugvppMw.png)

These commands show the attacker was very much interested in information from the staff table in the postgres database. Returning to the timeline we can see that after the last command was executed /tmp/staff.txt was created:

![Image 18](https://miro.medium.com/v2/resize:fit:700/0*dHntMUdsZOmF7XY7)

We now have two systems that have references to the file staff.txt, as we are working with a disk image we can view the content of the file staff.txt from both systems.

From _i-020e722274233c7f2_:

![Image 19](https://miro.medium.com/v2/resize:fit:700/0*QSIX5v5DCKSDxr_i)

and from _i-08e56d6b6c0439daf_:

![Image 20](https://miro.medium.com/v2/resize:fit:700/0*RoFfXGgT1ykbAS3r)

We can see that the file SHA256 hash and content are the same for both files on both systems.

The last section section of timeline analysis for _i-020e722274233c7f2_ shows the attacker’s ssh session terminating followed by another ssh session starting and terminating within the same minute:

![Image 21](https://miro.medium.com/v2/resize:fit:700/0*bUjW62CPMfbTMBXJ)

We know from the ec2-user _bash\_history_ file there was an scp command executed after the SSH session which ties in with the timeline.

Let’s look at the investigative questions and where we stand.

**What actions were performed on the host?**

So, to recap, we’ve performed analysis of _i-08e56d6b6c0439daf_ and _i-020e722274233c7f2_ and identified that during the attacker’s AWS Session Manager session:

*   IMDS and aws command line tool were used to perform network discovery to identify other hosts for lateral movement;
*   connected to another hots _i-020e722274233c7f2_ for additional suspicious activity _._

**Are there other traces of suspicious activity?**

*   a database table was dumped to a file named staff.txt;
*   copied the database dump file staff.txt file from _i-020e722274233c7f2_ to _i-08e56d6b6c0439daf_; and
*   created a new s3 bucket and copied the database dump file staff.txt to it.

What happened to the database dump file staff.txt and how did the attacker get access to the account DevOps1-bpvbp? All will be revealed in the final part of this blog series 🙂

## About Cado Security

Cado Security is _the_ cloud investigation and response automation company. The Cado platform leverages the scale, speed and automation of the cloud to effortlessly deliver forensic-level detail into cloud, container and serverless environments.

## About Invictus Incident Response

We are an incident response company specialised in supporting organisations facing a cyber attack. We help our clients stay undefeated!

[🆘](https://emojikeyboard.org/copy/SOS_Sign_Emoji_%F0%9F%86%98) Incident Response support reach out to cert@invictus-ir.com or go to [https://www.invictus-ir.com/247](https://www.invictus-ir.com/247)

[📧](https://emojikeyboard.org/copy/E-Mail_Symbol_Emoji_%F0%9F%93%A7) Questions or suggestions contact us at info@invictus-ir.com
