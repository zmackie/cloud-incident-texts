---
title: A Technical Analysis of the Capital One Cloud Misconfiguration Breach
url: "https://cloudsecurityalliance.org/blog/2019/08/09/a-technical-analysis-of-the-capital-one-cloud-misconfiguration-breach"
author: Josh Stella
published: 2019-08-09
source_type: article
source_domain: cloudsecurityalliance.org
cleanup_method: llm
---

# A Technical Analysis of the Capital One Cloud Misconfiguration Breach

Published 08/09/2019


_This article was originally published on Fugue's blog [here](https://www.fugue.co/blog/12-ways-cloud-upended-it-security-and-what-you-can-do-about-it)_

_By Josh Stella, Co-founder & Chief Technology Officer,_[_Fugue_](https://www.fugue.co/blog)

This is a technical exploration of how the Capital One breach might have occurred, based on the evidence we have from the [criminal complaint.](https://www.justice.gov/usao-wdwa/press-release/file/1188626/download) I want to start by saying that I deeply respect the Capital One cloud team, and have friends on it. They've been leaders in cloud computing, and what happened to them could have happened to nearly anyone. I'm also not criticizing Amazon Web Services (AWS)⁠—my previous employer. They offer secure services and I have nothing but respect for them. The purpose of this post is to explore a combination firewall/IAM/S3 attack to illustrate some of the dangers of cloud misconfigurations that every organization on cloud should heed.

In order to write this, I analyzed the technical details of the FBI complaint, and then formed a hypothesis of how the attack might have taken place. I then simulated the attack in my development account, so that I could provide specific details in this post.

## The facts as we know them

We have a smattering of information on the attack from the FBI complaint, and from social media posts by the alleged attacker. It appears that the attacker used Tor and IPredator in combination to obfuscate her identity, and through those services, discovered a misconfigured firewall in the Capital One AWS environment. What isn't clear is whether this was a targeted attack on Capital One, or an opportunistic attack upon finding the misconfiguration.

Many articles have been written on the possible motivations and biography of the attacker, so I'll leave those aside to focus on the technical specifics. There were four different elements to the attack that we know about:

*   Misconfigured firewall
*   Gaining access to an EC2 instance
*   Getting IAM role access to S3
*   S3 bucket discovery and duplication.

Each of the above are explored in some detail below.

## How the hack could have happened

We have some details, but really not that many, and therefore I employed a fair amount of speculation and interpretation of the facts that we do have. I'll clearly state when I'm speculating as we walk through the steps of the attack below. The diagram below shows my sandbox environment where I simulated some aspects of the Capital One breach.

The environment contains:

1.   a basic VPC network
2.   a Security Group that allows HTTP(S) and SSH
3.   a private S3 Bucket
4.   two IAM Roles - one with S3 access, and one without
5.   An EC2 Instance with a public IP address, with the IAM Role that doesn’t have S3 access

![Image 6](https://blog.cloudsecurityalliance.org/wp-content/uploads/sites/3/2019/08/inline-misconfiguration-exploit-sandbox.jpg)
My goal was to go from shell access of the EC2 instance, to the ability to access and copy the S3 data in the private buckets.

Before we go into detail on the various steps, it’s worth pointing out that the FBI gained access via a tip to a GitHub hosted file that contained the IP address of a server, along with three commands:

_"Capital One determined that the April 21 File contained code for three commands, as well as a list of more than 700 folders or buckets of data."_ We’ll go into some detail on each of these commands, and what they might have been and the possible strategy used by the attacker.

### Step one: misconfigured firewall

According to the FBI Complaint, _"A firewall misconfiguration permitted commands to reach and be executed by that server, which enabled access to folders or buckets... (III.A.10)"_

This suggests that the firewall was external to the server vs. a local firewall, though it isn't explicit. While there are many firewall virtual appliances available on AWS, generally this would be a Security Group. It seems that a dangerous port was left open on whichever firewall type was in use, and this might have been the initial opening for the attack. It's possible that an SSH port was opened for a maintenance window, or perhaps the server in question was left over from development efforts and no longer in use. Another possibility is that the server was running an application such as MongoDB or ElasticSearch that require an open port to function, but which should never have been exposed to the Internet via the firewall. Whatever the details, the attacker found a path into the CapitalOne cloud computing infrastructure.

### Step two: gaining access to an EC2 instance

Based on the FBI complaint’s description of the compromised entity as a “server” and that the attacker was able to extract IAM credentials from it, it appears that an EC2 Instance was then breached. This might have been an application or OS vulnerability⁠—we simply don't know. For the purposes of my simulation of the attack, I assumed the attacker gained shell access, but not root access to the instance, as all the remaining steps only require basic shell access to successfully complete.

### Step three: getting IAM role access to S3

_..."CapitalOne determined that the first command, when executed, obtained the security credentials for an account known as ***-WAF-Role that, in turn, enabled access to certain of Capital One's folders at Cloud Computing Company. (III.A.11)"_

Much of the "action" in this breach was via IAM role access to private S3 buckets, seemingly via AWS CLI commands from the compromised server. Much has been made of the name of the role in the press to date, but there is no solid evidence that this server was itself a WAF. It is common to “borrow” IAM roles in dynamic AWS environments (it’s not a great practice, but it is a common one), and also as will be shown below, policy associations can be changed and often have “Role” in the name, as shown in the example below. Perhaps this server was just something left around without tags to bring it up on management tooling dashboards. I’ve rarely seen a sizable AWS account without orphaned resources laying around one place or another.

If the server was itself a WAF, and intentionally had read/write access to buckets and objects in those buckets containing PII data, that was a naive defense strategy for the obvious reasons⁠—notably that a single firewall misconfiguration would be able to breach all architectural defenses to the sensitive data. This isn't the only explanation for the breach however, and I suspect that there was more to it, using IAM and EC2 features designed for flexibility, but potentially misused to grant additional privileges.

Given that they are describing the "first command", I think it's reasonable to assume that they are referring to an AWS CLI script. If the EC2 instance already had access to S3, the attacker would have only needed to execute something like:

> curl [http://169.254.169.254/latest/meta-data/iam/securi...](http://169.254.169.254/latest/meta-data/iam/security-credentials/DemonstrationEC2Role)

This command retrieves the current IAM temporary credentials from the role from the EC2 instance metadata. The output looks like this:

![Image 7](https://blog.cloudsecurityalliance.org/wp-content/uploads/sites/3/2019/08/Screen-Shot-2019-08-05-at-1.04.03-PM.png)
_Where the access key and secret access key are replaced with *'s and the token corrupted to protect the innocent._

This is all that would be needed to access the S3 buckets and their content.

But there is another possibility as to what that "first command" did, and everyone who uses AWS needs to be aware of it. If the compromised server did not have access to the private S3 buckets, but did have permissions to list and attach IAM policies, the attacker could have used these capabilities to essentially go shopping for a set of credentials that would provide this access. Since IAM permissions often have no relationship to IP-level network access controls, and the AWS services connect via IAM, these roles and policies form a sort of alternate network that needs to be secured just as a traditional network does. IAM becomes a primary means of “lateral movement” within the cloud environment.

The command below, for example, replaces one set of IAM permissions with another:

> aws ec2 replace-iam-instance-profile-association --association-id iip-assoc-00facaf2870f3bcc9 --iam-instance-profile Name=DemonstrationEC2Role

which returns the following, showing that I’ve successfully replaced the existing IAM permissions for the ones in the DemonstrationEC2Role policy:

![Image 8](https://blog.cloudsecurityalliance.org/wp-content/uploads/sites/3/2019/08/Screen-Shot-2019-08-05-at-1.04.15-PM.png)
Other useful commands for such a fishing expedition include:

> aws iam list-roles

> aws iam list-policies

> aws iam list-instance-profiles

These do what it says on the tin⁠—enumerate the catalogue of available IAM resources an attacker might want to use once they have shell on an EC2 instance.

In this example, I replaced a limited IAM profile with one with additional permissions to S3. We cannot discount that the attacker executed a similar approach in the Capital One breach. Whether or not this was the case, it's a critical capability to keep in mind when you configure IAM roles for your EC2 instances⁠—especially public facing ones—as IAM permissions can effectively "jump" to private resources in your environment.

In either scenario, the attacker gained access to the credentials needed to retrieve information from S3 and to duplicate that information.

### Step four: S3 bucket discovery and duplication

_"Capital One determined that the third command (the "Sync Command"), when executed, used the ***-WAF-Role to extract or copy data from those folders or buckets in Capital One's storage space for which the ***-WAF-Role account had the requisite permissions. (III.A.11)"_

This suggests the use of the AWS CLI command `aws s3 sync`, so I think it's more evidence that the attacker gained shell access to the EC2 instance and used the AWS CLI to perform these commands. What isn't clear is how the attacker knew which S3 buckets to perform the sync on, but if the IAM role used had adequate permissions, it's pretty simple to list all the buckets accessible via that role. This highlights the danger of a single IAM role having this broad of S3 permissions, as even at this point, without the ability to discover the target buckets, the attacker would not have likely been able to capture much if any data.

## Recommendations

1.   Constantly monitor for overly permissive Security Groups or any other access mechanism from 0.0.0.0/0. Checking on provisioning is necessary, but not nearly good enough. Cloud infrastructure is created and modified via API, which means that it is often drifting over time as different teams and people interact with it.
2.   Apply the principle of least privilege and ruthlessly limit IAM roles to what is absolutely necessary for the business function of the resource using that role. In the case of S3, you might consider different public end points for read and write operations, with different IAM roles that cannot perform the other function. Eliminate all production use cases where S3 bucket listing is enabled, in favor of shared secrets or other mechanisms.
3.   Don't allow EC2 instances to have IAM roles that allow attaching or replacing role policies in any production environments.
4.   Ruthlessly clean up unused cloud resources (especially servers and S3 buckets) left over from prior development or production debugging efforts.
5.   Include cloud infrastructure misconfiguration in your pen testing efforts. Use outside pen testers and make sure they are knowledgeable about how to find and exploit cloud misconfigurations.

Read more industry insights from the team at Fugue [here](https://www.fugue.co/blog).
