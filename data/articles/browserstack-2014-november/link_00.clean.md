---
title: "BrowserStack analysis: unpatched inactive machine compromised by shellshock vulnerability"
url: "http://archive.today/rsmmS"
author: Dissent
published: 2014-11-12
source_type: archive
source_domain: archive.today
cleanup_method: llm
---

# BrowserStack analysis: unpatched inactive machine compromised by shellshock vulnerability
# BrowserStack analysis: unpatched inactive machine compromised by shellshock vulnerability


# BrowserStack analysis: unpatched inactive machine compromised by shellshock vulnerability

*   __ November 12, 2014
*   __[Dissent](https://archive.ph/o/rsmmS/https://www.databreaches.net/ "Visit Dissent’s website")

_BrowserStack sent DataBreaches.net the following analysis, which is being emailed to all their users:_

> As you may already know, BrowserStack experienced an attack on 9th November, 2014 at 23:30 GMT during which an individual was able to gain unauthorized access to some of our users’ registered email addresses. He then tried to send an email <[http://pastebin.com/i788JT76](https://archive.ph/o/rsmmS/pastebin.com/i788JT76)> to all our registered users, but he was only able to reach less than 1% (our estimate is 5,000 users). The email contained inaccurate information, even claiming that BrowserStack would be shutting down.
> 
> 
> 
> When we realized this, our only concern was to protect our users. This involved temporarily taking down the service, as we scrutinized each component carefully. This inconvenienced our users for several hours, and for that we are truly sorry.
> 
> 
> 
> ***What happened?***
> 
> 
> 
> BrowserStack application servers run using Amazon Web Services. The configuration is vast, consisting of thousands of servers. One of these was an old prototype machine, which was the target of the breach.
> 
> 
> 
> The machine had been running since before 2012, and was not in active use. It was penetrated using the shellshock vulnerability, and since it was no longer in active use, it did not have the appropriate patch installed.
> 
> 
> 
> The old prototype machine had our AWS API access key and secret key. Once the hacker gained access to the keys, he created an IAM user, and generated a key-pair. He was then able to run an instance inside our AWS account using these credentials, and mount one of our backup disks. This backup was of one of our component services, used for production environment, and contained a config file with our database password. He also whitelisted his IP on our database security group, which is the AWS firewall.
> 
> 
> 
> He began to copy one of our tables, which contained partial user information, including email IDs, hashed passwords, and last tested URL. His copy operation locked the database table, which raised alerts on our monitoring system. On receiving the alerts, we checked the logs, saw an unrecognized IP, and blocked it right away. In that time, the hacker had been able to retrieve only a portion of the data. Finally, using this data and the SES credentials, he was able to send an email to some of our users.
> 
> 
> 
> ***What was the extent of the damage?***
> 
> 
> 
> Our database logs confirmed that user data was partially copied, but no user test history was compromised. Therefore all user data remains wholly intact. Most crucially, *credit card details were not compromised*, as we only store the last 4 digits of the credit card number, and all payment processing takes place through our payment processing partner. All user passwords are salted, and encrypted with the powerful bcrypt algorithm, which creates an irreversible hash which cannot be cracked. However, as an added precaution, we suggest that users change their BrowserStack account passwords.
> 
> 
> 
> We were able to verify the actions of the hacker using AWS CloudTrail, which confirmed that no other services were compromised, no other machines were booted, and our AMIs and other data stores were not copied.
> 
> 
> 
> In addition, our production web server logs indicate that we were experiencing shellshock attempts, but they failed because the production web server has the necessary patches to foil all such attempts.
> 
> 
> 
> ***Points in the email***
> 
> 
> 
> We would now like to address the points raised in the email. The hacker quoted three paragraphs from our Security documentation, as follows:
> 
> 
> 
> – *after the restoration process is complete, the virtual machines are guaranteed to be tamper-proof.* → Our restoration process is indeed amper-proof. When we create a test machine from scratch, we take a snapshot. After every user session, the test machine is restored to it original state using that snapshot. Even if a previous user manages to install a malicious software, it is always erased due to the restoration process.
> 
> 
> 
> – *The machines themselves are in a secure network, and behind strong firewalls to present the safest environment possible.*→ Every single machine has an OS firewall, in addition to the hardware network firewalls we use. On EC2, we use security groups as an equivalent safety measure. We also use industry-standard brute force-throttling measures.
> 
> 
> 
> – *At any given time, you have sole access to a virtual machine. Your testing session cannot be seen or accessed by other users, including BrowserStack administrators. Once you release a virtual machine, it is taken off the grid, and restored to its initial settings. All your data is destroyed in this process. *→ The application ensures that a machine is allocated to only one person at a time, and VNC passwords are randomly generated for each session. Thus, even our administrators cannot see your test session.
> 
> 
> 
> With respect to the plaintext passwords on the VMs, this is certainly not the case, as we moved to key-based authentication years ago. Moreover root login is disabled in our SSH configuration.
> 
> 
> 
> Both the passwords mentioned, ‘nakula’ and ‘c0stac0ff33’, were indeed in use a couple of years ago during our prototyping phase, and thus were present in the old prototype machine that was hacked. ‘nakula’ was previously our VNC password, and was hashed. However, unlike the hash used for the user passwords, this hash is much weaker. This was due to a limitation in VNC protocol, and we had overcome this liability by regenerating a new password for every session, and thus ‘nakula’ has not been in use for years. ‘c0stac0ff33’ was one of our system user passwords on the prototype machine, before we moved to key-based authentication.
> 
> 
> 
> It is true that we still run our VNC server on port 5901, but we do not believe that it is a security vulnerability because a current password is still required for access. As mentioned before, the passwords are changed every test session.
> 
> 
> 
> ***Where did we go wrong?***
> 
> 
> 
> All our servers, running or not, whether in active use or not, should have been patched with the latest security upgrades and updates including the shellshock one. Moreover, servers not in active use should have been stopped and the server shouldn’t have had the AWS keys.
> 
> 
> 
> Additionally, our communication could have been better. Instead of intermittent updates, we preferred to present a complete, honest picture of the attack to our users once our analysis was done.
> 
> 
> 
> ***Security measures taken to mitigate and prevent further incidents***
> 
> 
> 
> – After taking down the service, we revoked all the existing AWS keys and passwords, and generated new ones immediately, as an added security measure.
> 
>  – Subsequently, we went through all the SSH logs, web server logs, as well as AWS Cloud Trail logs, to ensure that no more damage was done.
> 
>  – We are migrating all backups to encrypted backups, and removing all unencrypted ones.
> 
>  – We have also put in several additional checks and alerts, which are triggered on specified AWS actions. As a precautionary measure we have also created new VM snapshots and have replaced all the existing ones.
> 
>  – To prevent further incidents, we are in the process of evaluating certain VPC/VPN options to enhance our security measures.
> 
>  – We’re going to have a security audit conducted by an external, independent agency.
> 
> 
> 
> Once again we apologise for the inconvenience. BrowserStack is deeply committed to providing the best and most secure testing infrastructure for our users. We will be forging ahead with exciting new releases in the next few weeks and look forward to continue serving you.
> 
> 
> 
> We have a trace and the IP of the hacker. We will be in touch with authorities soon to register an official complaint. Thank you for the support and understanding we have received over the last few days.
> 
> 
> 
> Regards,
> 
>  Adithya Chadalawada
> 
>  www.browserstack.com
