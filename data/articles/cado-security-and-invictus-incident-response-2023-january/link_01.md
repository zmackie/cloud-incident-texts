Title: Responding to an attack in AWS

URL Source: https://awstip.com/responding-to-an-attack-in-aws-dae857806aa7

Published Time: 2023-01-19T13:02:29Z

Markdown Content:
# Responding to an attack in AWS. A case study — Part 2 | by Invictus Incident Response | AWS Tip

[Sitemap](https://awstip.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 1](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## AWS Tip](https://awstip.com/?source=post_page---publication_nav-b4c1e34ed5e-dae857806aa7---------------------------------------)

·
Follow publication

[![Image 2: AWS Tip](https://miro.medium.com/v2/resize:fill:76:76/1*LXqMmX8rKuWEc3D_apZ1rQ.jpeg)](https://awstip.com/?source=post_page---post_publication_sidebar-b4c1e34ed5e-dae857806aa7---------------------------------------)
Best AWS, DevOps, Serverless, and more from top Medium writers.

Follow publication

# Responding to an attack in AWS

[![Image 3: Invictus Incident Response](https://miro.medium.com/v2/resize:fill:64:64/1*F9s4GC6fkzA4zjWCkKYgbw.png)](https://invictus-ir.medium.com/?source=post_page---byline--dae857806aa7---------------------------------------)

[Invictus Incident Response](https://invictus-ir.medium.com/?source=post_page---byline--dae857806aa7---------------------------------------)

Follow

7 min read

·

Jan 19, 2023

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Faws-tip%2Fdae857806aa7&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&user=Invictus+Incident+Response&userId=e992e39417b7&source=---header_actions--dae857806aa7---------------------clap_footer------------------)

3

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fdae857806aa7&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---header_actions--dae857806aa7---------------------bookmark_footer------------------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Ddae857806aa7&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---header_actions--dae857806aa7---------------------post_audio_button------------------)

Share

A case study — Part 2

Press enter or click to view image in full size

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

Press enter or click to view image in full size

![Image 5](https://miro.medium.com/v2/resize:fit:700/0*_zxf-98VefGvKAJO)

Cado Response acquisition

A disk image is created from a snapshot of the volume attached to the instance _i-08e56d6b6c0439daf_ and automatically processed giving the analyst access to a super timeline and file content.

## Analysis

From previous analysis, we know that the AWS Session Manager initiated session took place at 2022–10–26 21:29:03, so that will be the pivot point.

As this is a Linux system we will start with the _secure_ log file, the file shows that between Oct 26 21:29:53 and Oct 26 21:36:03 there was activity for the users ssm-user and ec2-user. ssm-user is the user account associated with SSM Session Manager and ec2-user is the default user for Amazon Linux systems and the time of the account being accessed lines up with the log analysis.

_secure_ log shows session start and session close timestamps:

Press enter or click to view image in full size

![Image 6](https://miro.medium.com/v2/resize:fit:700/1*m1EnzOFZ74sBNDby5xBGOg.png)

Linux secure log

Now we have a time window of interest. Using the search function in Cado paltform, we want to see what activity took place on _i-08e56d6b6c0439daf_ between Oct 26 21:29:53 and Oct 26 21:36:03 so let’s add a timestamp range 2022–10–26 21:28:00 to 2022–10–26 21:38:00 to the search:

Press enter or click to view image in full size

![Image 7](https://miro.medium.com/v2/resize:fit:700/0*UrL2P5qVoKjAQuAE)

AWS SSM generates quite a lot of log events which results in a lot of noise so we removed those entries from the timeline search, reducing the number of events from 227 to 57:

Press enter or click to view image in full size

![Image 8](https://miro.medium.com/v2/resize:fit:700/0*ZTk7QCtuV7ncatvT)

Along with the _secure_ log, the _audit_ log tracks user logon activity, here we can see the ssm-user is linked to audit entry USER_ACCT which is triggered when a user-space user account is modified.

Press enter or click to view image in full size

![Image 9](https://miro.medium.com/v2/resize:fit:700/0*4hMoSIYSv5_DUwEF)

So our Investigative Questions are:

*   What actions were performed on the host?
*   Are there other traces of suspicious activity?

Timeline Analysis and file content can help answer these questions.

Press enter or click to view image in full size

![Image 10](https://miro.medium.com/v2/resize:fit:700/0*njlb66o24Dxranlt)

Between 21:29:53 and 21:36:04 we have events that show an AWS SSM interactive session had started; the associated ssm-user switched user to the default Amazon Linux2 account ec2-user which initiated a new bash session. All of this takes place under the process ID 32627 directly linking the ssm-user and ec2-user accounts to the attacker activity. The ec2-user _known-hosts_ file was accessed and a file named staff.txt was created in the ec2-user’s default directory.

Next step is to review the _bash\_history_ files for ssm-user and ec2-user to identify any commands the attacker has executed.

Press enter or click to view image in full size

![Image 11](https://miro.medium.com/v2/resize:fit:700/0*1taOdzz4jP1FNuM_)

The screenshot above is from using the Cado platform to view the contents of ssm-user’s _bash\_history_ file. The command seen within the file doesn’t have an associated timestamp, however, in our timeline there is log evidence that indicates that sudo command was executed to switch user to ec2-user during the attacker’s session.

Press enter or click to view image in full size

![Image 12](https://miro.medium.com/v2/resize:fit:700/0*bb6c9qJRrdcqabBL)

The screenshot above shows the contents of ec2-user’s _bash\_history_ file. Again, the commands seen within the file don’t have timestamps, however in our timeline we did see the ec2-user’s _known\_hosts_ file being accessed, so there is a good indication the ssh commands are linked to the attacker’s session. Also in our timeline we can see the file staff.txt was created during the attacker’s session which is likely to be the result of the scp command.

The other commands seen at the beginning and end of of the bash_history file are also interesting:

Press enter or click to view image in full size

![Image 13](https://miro.medium.com/v2/resize:fit:700/1*odc3f0JwSBsaMeEsCFrJkA.png)

The first command in the code box above, shows the Instance MetaData Service (IMDS) being used to extract information regarding the Virtual Private Cloud (VPC) Id. The VPC Id is then used in conjunction with the aws command line tool to provide detailed information of the security group that the instance belongs to, in particular looking for port 22 entries, port 22 is commonly associated with SSH. This could be seen as a method to perform network discovery to find other hosts that can be used for lateral movement.

## Get Invictus Incident Response’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

- [x] 

Remember me for faster sign in

 

The last two commands in the bash_history file:

Press enter or click to view image in full size

![Image 14](https://miro.medium.com/v2/resize:fit:700/1*lFiUQjyXdhayajjG_iceSg.png)

show the aws command line to create a S3 bucket and the file staff.txt was copied to it. This could be seen as staging data for exfiltration.

Our analysis of _i-08e56d6b6c0439daf_ has found that the scope of our investigation has extended to another system within the network, 10.0.8.25, using the AWS console we identified that within the Security Group that IP address corresponds to an EC2 instance with ID _i-020e722274233c7f2_ and our Investigative Questions carry over to that host:

*   What actions were performed on the host?
*   Are there other traces of suspicious activity?

Again we start the analysis again with the _secure_ log file:

Press enter or click to view image in full size

![Image 15](https://miro.medium.com/v2/resize:fit:700/1*8pY5rPnxvSXujgA7ViPLUg.png)

We can see the timings for the ssh connection line up with the findings from our analysis of _i-08e56d6b6c0439daf_.

Using the same time window and a filter to show LOGIN and USER from the audit log along with the rest of the system and user events gives 53 events for further analysis.

Due to the configuration of this system, user executed commands are saved to the audit log, the commands are HEX encoded and the Cado platform automatically decodes them to the attacker executed the following commands:

Press enter or click to view image in full size

![Image 16](https://miro.medium.com/v2/resize:fit:700/0*mM00eMOrAOQQLbmi)

Press enter or click to view image in full size

![Image 17](https://miro.medium.com/v2/resize:fit:700/1*89XNhaP0NyYHTL-ugvppMw.png)

These commands show the attacker was very much interested in information from the staff table in the postgres database. Returning to the timeline we can see that after the last command was executed /tmp/staff.txt was created:

Press enter or click to view image in full size

![Image 18](https://miro.medium.com/v2/resize:fit:700/0*dHntMUdsZOmF7XY7)

We now have two systems that have references to the file staff.txt, as we are working with a disk image we can view the content of the file staff.txt from both systems.

From _i-020e722274233c7f2_:

Press enter or click to view image in full size

![Image 19](https://miro.medium.com/v2/resize:fit:700/0*QSIX5v5DCKSDxr_i)

and from _i-08e56d6b6c0439daf_:

Press enter or click to view image in full size

![Image 20](https://miro.medium.com/v2/resize:fit:700/0*RoFfXGgT1ykbAS3r)

We can see that the file SHA256 hash and content are the same for both files on both systems.

The last section section of timeline analysis for _i-020e722274233c7f2_ shows the attacker’s ssh session terminating followed by another ssh session starting and terminating within the same minute:

Press enter or click to view image in full size

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

[Cloud](https://medium.com/tag/cloud?source=post_page-----dae857806aa7---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----dae857806aa7---------------------------------------)

[AWS](https://medium.com/tag/aws?source=post_page-----dae857806aa7---------------------------------------)

[Incident Response](https://medium.com/tag/incident-response?source=post_page-----dae857806aa7---------------------------------------)

[Dfir](https://medium.com/tag/dfir?source=post_page-----dae857806aa7---------------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Faws-tip%2Fdae857806aa7&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&user=Invictus+Incident+Response&userId=e992e39417b7&source=---footer_actions--dae857806aa7---------------------clap_footer------------------)

3

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Faws-tip%2Fdae857806aa7&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&user=Invictus+Incident+Response&userId=e992e39417b7&source=---footer_actions--dae857806aa7---------------------clap_footer------------------)

3

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fdae857806aa7&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---footer_actions--dae857806aa7---------------------bookmark_footer------------------)

[![Image 22: AWS Tip](https://miro.medium.com/v2/resize:fill:96:96/1*LXqMmX8rKuWEc3D_apZ1rQ.jpeg)](https://awstip.com/?source=post_page---post_publication_info--dae857806aa7---------------------------------------)

[![Image 23: AWS Tip](https://miro.medium.com/v2/resize:fill:128:128/1*LXqMmX8rKuWEc3D_apZ1rQ.jpeg)](https://awstip.com/?source=post_page---post_publication_info--dae857806aa7---------------------------------------)

Follow

[## Published in AWS Tip](https://awstip.com/?source=post_page---post_publication_info--dae857806aa7---------------------------------------)

[11.6K followers](https://awstip.com/followers?source=post_page---post_publication_info--dae857806aa7---------------------------------------)

·[Last published 2 days ago](https://awstip.com/building-an-automated-aws-security-advisor-rag-with-aws-bedrock-and-opensearch-serverless-43941ab13024?source=post_page---post_publication_info--dae857806aa7---------------------------------------)

Best AWS, DevOps, Serverless, and more from top Medium writers.

Follow

[![Image 24: Invictus Incident Response](https://miro.medium.com/v2/resize:fill:96:96/1*F9s4GC6fkzA4zjWCkKYgbw.png)](https://invictus-ir.medium.com/?source=post_page---post_author_info--dae857806aa7---------------------------------------)

[![Image 25: Invictus Incident Response](https://miro.medium.com/v2/resize:fill:128:128/1*F9s4GC6fkzA4zjWCkKYgbw.png)](https://invictus-ir.medium.com/?source=post_page---post_author_info--dae857806aa7---------------------------------------)

Follow

[## Written by Invictus Incident Response](https://invictus-ir.medium.com/?source=post_page---post_author_info--dae857806aa7---------------------------------------)

[630 followers](https://invictus-ir.medium.com/followers?source=post_page---post_author_info--dae857806aa7---------------------------------------)

·[1 following](https://medium.com/@invictus-ir/following?source=post_page---post_author_info--dae857806aa7---------------------------------------)

We are an incident response company specialised in supporting organisations facing a cyber attack. We help our clients stay undefeated!

Follow

## No responses yet

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--dae857806aa7---------------------------------------)

![Image 26](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---post_responses--dae857806aa7---------------------respond_sidebar------------------)

Cancel

Respond

## More from Invictus Incident Response and AWS Tip

![Image 27: Email Forwarding Rules in Microsoft 365](https://miro.medium.com/v2/resize:fit:679/format:webp/1*Aa8QGNL_tSJ5LHax2BY2dg.png)

[![Image 28: Invictus Incident Response](https://miro.medium.com/v2/resize:fill:20:20/1*F9s4GC6fkzA4zjWCkKYgbw.png)](https://invictus-ir.medium.com/?source=post_page---author_recirc--dae857806aa7----0---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[Invictus Incident Response](https://invictus-ir.medium.com/?source=post_page---author_recirc--dae857806aa7----0---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[## Email Forwarding Rules in Microsoft 365 ### The ultimate guide to analysing and understanding email forwarding rules in the Unified Audit Log (UAL)](https://invictus-ir.medium.com/email-forwarding-rules-in-microsoft-365-295fcb63d4fb?source=post_page---author_recirc--dae857806aa7----0---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

Feb 20, 2023

[1](https://invictus-ir.medium.com/email-forwarding-rules-in-microsoft-365-295fcb63d4fb?source=post_page---author_recirc--dae857806aa7----0---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---author_recirc--dae857806aa7----0-----------------explicit_signal----57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F295fcb63d4fb&operation=register&redirect=https%3A%2F%2Finvictus-ir.medium.com%2Femail-forwarding-rules-in-microsoft-365-295fcb63d4fb&source=---author_recirc--dae857806aa7----0-----------------bookmark_preview----57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

![Image 29: I Used HashMaps Every Day for 4 Years. Then Google Asked Me One Question and I Had Nothing.](https://miro.medium.com/v2/resize:fit:679/format:webp/1*_Jx2wtXeXTQGMJyhmaeb5w.png)

[![Image 30: AWS Tip](https://miro.medium.com/v2/resize:fill:20:20/1*LXqMmX8rKuWEc3D_apZ1rQ.jpeg)](https://awstip.com/?source=post_page---author_recirc--dae857806aa7----1---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

In

[AWS Tip](https://awstip.com/?source=post_page---author_recirc--dae857806aa7----1---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

by

[The Speedcraft Lab](https://medium.com/@speedcraft21?source=post_page---author_recirc--dae857806aa7----1---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[## I Used HashMaps Every Day for 4 Years. Then Google Asked Me One Question and I Had Nothing. ### Four years of daily use and I never once looked inside it. Here’s what the silence on that call taught me about the difference between…](https://awstip.com/i-used-hashmaps-every-day-for-4-years-then-google-asked-me-one-question-and-i-had-nothing-cda4e050d1ba?source=post_page---author_recirc--dae857806aa7----1---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

Mar 16

[16](https://awstip.com/i-used-hashmaps-every-day-for-4-years-then-google-asked-me-one-question-and-i-had-nothing-cda4e050d1ba?source=post_page---author_recirc--dae857806aa7----1---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---author_recirc--dae857806aa7----1-----------------explicit_signal----57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcda4e050d1ba&operation=register&redirect=https%3A%2F%2Fawstip.com%2Fi-used-hashmaps-every-day-for-4-years-then-google-asked-me-one-question-and-i-had-nothing-cda4e050d1ba&source=---author_recirc--dae857806aa7----1-----------------bookmark_preview----57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

![Image 31: Amazon Data Engineer Interview Question — Data Engineer III](https://miro.medium.com/v2/resize:fit:679/format:webp/1*V3SPk2OZJYiiPPnBidZf2A.jpeg)

[![Image 32: AWS Tip](https://miro.medium.com/v2/resize:fill:20:20/1*LXqMmX8rKuWEc3D_apZ1rQ.jpeg)](https://awstip.com/?source=post_page---author_recirc--dae857806aa7----2---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

In

[AWS Tip](https://awstip.com/?source=post_page---author_recirc--dae857806aa7----2---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

by

[Mohit Daxini](https://medium.com/@mohitdaxini75?source=post_page---author_recirc--dae857806aa7----2---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[## Amazon Data Engineer Interview Question — Data Engineer III ### Modern data-driven applications often allow users to filter data dynamically. Whether it’s an e-commerce dashboard, analytics platform, or…](https://awstip.com/amazon-data-engineer-interview-question-data-engineer-iii-a6b8201ab6dc?source=post_page---author_recirc--dae857806aa7----2---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

Mar 18

[](https://awstip.com/amazon-data-engineer-interview-question-data-engineer-iii-a6b8201ab6dc?source=post_page---author_recirc--dae857806aa7----2---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---author_recirc--dae857806aa7----2-----------------explicit_signal----57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa6b8201ab6dc&operation=register&redirect=https%3A%2F%2Fawstip.com%2Famazon-data-engineer-interview-question-data-engineer-iii-a6b8201ab6dc&source=---author_recirc--dae857806aa7----2-----------------bookmark_preview----57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

![Image 33: Automated Forensic analysis of Google Workspace](https://miro.medium.com/v2/resize:fit:679/format:webp/0d702cbfe9920e00e94464660874e97b36b08e18a7844ad35d0d5cd2de2ef897)

[![Image 34: Invictus Incident Response](https://miro.medium.com/v2/resize:fill:20:20/1*F9s4GC6fkzA4zjWCkKYgbw.png)](https://invictus-ir.medium.com/?source=post_page---author_recirc--dae857806aa7----3---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[Invictus Incident Response](https://invictus-ir.medium.com/?source=post_page---author_recirc--dae857806aa7----3---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[## Automated Forensic analysis of Google Workspace ### Follow us | LinkedIn | Twitter |GitHub](https://invictus-ir.medium.com/automated-forensic-analysis-of-google-workspace-859ed50c5c92?source=post_page---author_recirc--dae857806aa7----3---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

Aug 16, 2022

[](https://invictus-ir.medium.com/automated-forensic-analysis-of-google-workspace-859ed50c5c92?source=post_page---author_recirc--dae857806aa7----3---------------------57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---author_recirc--dae857806aa7----3-----------------explicit_signal----57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F859ed50c5c92&operation=register&redirect=https%3A%2F%2Finvictus-ir.medium.com%2Fautomated-forensic-analysis-of-google-workspace-859ed50c5c92&source=---author_recirc--dae857806aa7----3-----------------bookmark_preview----57ca0114_725f_4a8d_9f0d_20ae314faa43--------------)

[See all from Invictus Incident Response](https://invictus-ir.medium.com/?source=post_page---author_recirc--dae857806aa7---------------------------------------)

[See all from AWS Tip](https://awstip.com/?source=post_page---author_recirc--dae857806aa7---------------------------------------)

## Recommended from Medium

![Image 35: A futuristic 3D visualization of two massive data centers — one blue for Microsoft and one purple/green for OpenAI — separated by a glowing orange tectonic crack and severed fiber optic cables.](https://miro.medium.com/v2/resize:fit:679/format:webp/1*rRInK1ARZKPmpBnF4fxLKw.png)

[![Image 36: ILLUMINATION](https://miro.medium.com/v2/resize:fill:20:20/1*AZxiin1Cvws3J0TwNUP2sQ.png)](https://medium.com/illumination?source=post_page---read_next_recirc--dae857806aa7----0---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

In

[ILLUMINATION](https://medium.com/illumination?source=post_page---read_next_recirc--dae857806aa7----0---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

by

[Somya Golchha](https://medium.com/@jainsomya2510?source=post_page---read_next_recirc--dae857806aa7----0---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[## The Microsoft-OpenAI Divorce Is Official: Inside the $250 Billion Betrayal ### GPT-5 is already being retired, and Satya Nadella just made his move. The “partnership” of the century is entering its terminal phase.](https://medium.com/illumination/the-microsoft-openai-divorce-is-official-inside-the-250-billion-betrayal-822073eba64e?source=post_page---read_next_recirc--dae857806aa7----0---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

Feb 18

[101](https://medium.com/illumination/the-microsoft-openai-divorce-is-official-inside-the-250-billion-betrayal-822073eba64e?source=post_page---read_next_recirc--dae857806aa7----0---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---read_next_recirc--dae857806aa7----0-----------------explicit_signal----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F822073eba64e&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fillumination%2Fthe-microsoft-openai-divorce-is-official-inside-the-250-billion-betrayal-822073eba64e&source=---read_next_recirc--dae857806aa7----0-----------------bookmark_preview----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

![Image 37: Hacking Microsoft IIS: From Recon to Advanced Fuzzing](https://miro.medium.com/v2/resize:fit:679/format:webp/1*YpG66o4sP1IYfsZCgVgv7Q.jpeg)

[![Image 38: InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:20:20/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---read_next_recirc--dae857806aa7----1---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

In

[InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---read_next_recirc--dae857806aa7----1---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

by

[𝙇𝙤𝙨𝙩𝙨𝙚𝙘](https://lostsec.medium.com/?source=post_page---read_next_recirc--dae857806aa7----1---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[## Hacking Microsoft IIS: From Recon to Advanced Fuzzing ### A hands-on guide covering IIS recon, shortname testing and advanced fuzzing used in real bug bounty hunting.](https://infosecwriteups.com/hacking-microsoft-iis-from-recon-to-advanced-fuzzing-013989524fe2?source=post_page---read_next_recirc--dae857806aa7----1---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

Feb 21

[8](https://infosecwriteups.com/hacking-microsoft-iis-from-recon-to-advanced-fuzzing-013989524fe2?source=post_page---read_next_recirc--dae857806aa7----1---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---read_next_recirc--dae857806aa7----1-----------------explicit_signal----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F013989524fe2&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-microsoft-iis-from-recon-to-advanced-fuzzing-013989524fe2&source=---read_next_recirc--dae857806aa7----1-----------------bookmark_preview----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

![Image 39: Don’t Become a DevOps Engineer in 2026!](https://miro.medium.com/v2/resize:fit:679/format:webp/1*jbajxX_SZsz_WdtxVW1Xtw.png)

[![Image 40: Dhanush N](https://miro.medium.com/v2/resize:fill:20:20/1*g-aoUi88UKMpAxezY9NcmQ.png)](https://dhanushnehru.medium.com/?source=post_page---read_next_recirc--dae857806aa7----0---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[Dhanush N](https://dhanushnehru.medium.com/?source=post_page---read_next_recirc--dae857806aa7----0---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[## Don’t Become a DevOps Engineer in 2026! ### Stop writing YAML. Stop babysitting pipelines. The game has fundamentally changed.](https://dhanushnehru.medium.com/dont-become-a-devops-engineer-in-2026-f2e94541e700?source=post_page---read_next_recirc--dae857806aa7----0---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

Mar 2

[18](https://dhanushnehru.medium.com/dont-become-a-devops-engineer-in-2026-f2e94541e700?source=post_page---read_next_recirc--dae857806aa7----0---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---read_next_recirc--dae857806aa7----0-----------------explicit_signal----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff2e94541e700&operation=register&redirect=https%3A%2F%2Fdhanushnehru.medium.com%2Fdont-become-a-devops-engineer-in-2026-f2e94541e700&source=---read_next_recirc--dae857806aa7----0-----------------bookmark_preview----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

![Image 41: The Bug Bounty Automation Stack That Can Generate $10K+ (Open Source Tools Only)](https://miro.medium.com/v2/resize:fit:679/format:webp/1*LDxbtzfpSDt7WwGGCjRdhw.png)

[![Image 42: System Weakness](https://miro.medium.com/v2/resize:fill:20:20/1*gncXIKhx5QOIX0K9MGcVkg.jpeg)](https://systemweakness.com/?source=post_page---read_next_recirc--dae857806aa7----1---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

In

[System Weakness](https://systemweakness.com/?source=post_page---read_next_recirc--dae857806aa7----1---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

by

[BugHunter’s Journal](https://medium.com/@bughuntersjournal?source=post_page---read_next_recirc--dae857806aa7----1---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[## The Bug Bounty Automation Stack That Can Generate $10K+ (Open Source Tools Only) ### Automation doesn’t find bugs. Automated workflows combined with manual validation do. While beginners waste time running Nuclei on random…](https://systemweakness.com/the-bug-bounty-automation-stack-that-can-generate-10k-open-source-tools-only-93ed3e8b3ee7?source=post_page---read_next_recirc--dae857806aa7----1---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

Dec 17, 2025

[5](https://systemweakness.com/the-bug-bounty-automation-stack-that-can-generate-10k-open-source-tools-only-93ed3e8b3ee7?source=post_page---read_next_recirc--dae857806aa7----1---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---read_next_recirc--dae857806aa7----1-----------------explicit_signal----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F93ed3e8b3ee7&operation=register&redirect=https%3A%2F%2Fsystemweakness.com%2Fthe-bug-bounty-automation-stack-that-can-generate-10k-open-source-tools-only-93ed3e8b3ee7&source=---read_next_recirc--dae857806aa7----1-----------------bookmark_preview----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

![Image 43: If You Understand These 5 AI Terms, You’re Ahead of 90% of People](https://miro.medium.com/v2/resize:fit:679/format:webp/1*qbVrf-wO9PYtthAj6E4RYQ.png)

[![Image 44: Towards AI](https://miro.medium.com/v2/resize:fill:20:20/1*JyIThO-cLjlChQLb6kSlVQ.png)](https://pub.towardsai.net/?source=post_page---read_next_recirc--dae857806aa7----2---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

In

[Towards AI](https://pub.towardsai.net/?source=post_page---read_next_recirc--dae857806aa7----2---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

by

[Shreyas Naphad](https://medium.com/@shreyasnaphad?source=post_page---read_next_recirc--dae857806aa7----2---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[## If You Understand These 5 AI Terms, You’re Ahead of 90% of People ### Master the core ideas behind AI without getting lost](https://pub.towardsai.net/if-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319?source=post_page---read_next_recirc--dae857806aa7----2---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

Mar 29

[199](https://pub.towardsai.net/if-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319?source=post_page---read_next_recirc--dae857806aa7----2---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---read_next_recirc--dae857806aa7----2-----------------explicit_signal----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc7622d353319&operation=register&redirect=https%3A%2F%2Fpub.towardsai.net%2Fif-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319&source=---read_next_recirc--dae857806aa7----2-----------------bookmark_preview----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

![Image 45: I Stopped Using ChatGPT for 30 Days. What Happened to My Brain Was Terrifying.](https://miro.medium.com/v2/resize:fit:679/format:webp/1*z4UOJs0b33M4UJXq5MXkww.png)

[![Image 46: Level Up Coding](https://miro.medium.com/v2/resize:fill:20:20/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---read_next_recirc--dae857806aa7----3---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

In

[Level Up Coding](https://levelup.gitconnected.com/?source=post_page---read_next_recirc--dae857806aa7----3---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

by

[Kusireddy](https://medium.com/@kusireddy?source=post_page---read_next_recirc--dae857806aa7----3---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[## I Stopped Using ChatGPT for 30 Days. What Happened to My Brain Was Terrifying. ### 91% of you will abandon 2026 resolutions by January 10th. Here’s how to be in the 9% who actually win.](https://levelup.gitconnected.com/i-stopped-using-chatgpt-for-30-days-what-happened-to-my-brain-was-terrifying-70d2a62246c0?source=post_page---read_next_recirc--dae857806aa7----3---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

Dec 28, 2025

[492](https://levelup.gitconnected.com/i-stopped-using-chatgpt-for-30-days-what-happened-to-my-brain-was-terrifying-70d2a62246c0?source=post_page---read_next_recirc--dae857806aa7----3---------------------917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fawstip.com%2Fresponding-to-an-attack-in-aws-dae857806aa7&source=---read_next_recirc--dae857806aa7----3-----------------explicit_signal----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F70d2a62246c0&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fi-stopped-using-chatgpt-for-30-days-what-happened-to-my-brain-was-terrifying-70d2a62246c0&source=---read_next_recirc--dae857806aa7----3-----------------bookmark_preview----917b0bf3_8806_486e_b8e3_772e68f0902b--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--dae857806aa7---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----dae857806aa7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----dae857806aa7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----dae857806aa7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----dae857806aa7---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----dae857806aa7---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----dae857806aa7---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----dae857806aa7---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----dae857806aa7---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----dae857806aa7---------------------------------------)