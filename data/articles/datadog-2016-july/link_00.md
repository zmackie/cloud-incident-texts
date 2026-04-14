Update 2016-08-18
As we previously reported, we detected unauthorized activity in our production infrastructure on 2016-07-08. See below for our initial notice.
What happened?
We traced the intrusion to the leak of an AWS access key and a SSH private key that were used by our automated provisioning and release systems. By using those particular keys together the attacker gained unauthorized access to three of our AWS EC2 instances and a subset of our AWS S3 buckets. Those AWS resources included user credentials for the Datadog service, service metadata, and credentials shared with Datadog for third-party integrations. Forensics show the attacker activity commenced on 2016-07-07 at 19:44 UTC and ceased on 2016-07-08 at 06:18 UTC. We began our response on 2016-07-08 at 14:46 UTC.
What did your immediate response include?
We quarantined the affected instances and preserved forensic evidence. As previously noted, we rebuilt compromised systems and mitigated known vulnerabilities. We engaged a globally recognized incident response and forensics firm, and an independent incident response consultant, Ryan McGeehan, to assist with our response activities and coordination with our integration partners.
Have your recommendations changed?
No, in-line with our prior post and communications, we continue to recommend that customers revoke or rotate any credentials shared with Datadog prior to 2016-07-08.
What are you doing now?
In addition to applying lessons-learned to our internal security practices, our longer term efforts will include deprecating customer AWS key based authentication in favor of the already available IAM role delegation and working with our SaaS integration partners to strengthen integration patterns whenever possible. As a Datadog user, you should expect some changes in these areas in the future.
We can’t overstate how grateful we are to our SaaS integration partners for their hard work and support throughout our incident response, and of course to our customers and users for their efforts and patience as we dealt with this issue.
Should you have any questions or require assistance contact us at support@datadoghq.com.
2016-07-08 Security Notice
Dear users,
Last night we sent email notifications regarding a security incident that took place within our server infrastructure on 2016-07-08. While our team is working on the technical and forensics aspects of the incident response, we want to be fully transparent with you regarding our current status and help you protect your own infrastructure.
You’ll find answers to some of the questions you may have below.
Again, we apologize for the inconvenience and extra work this represents, and are committed to assist you through this process.
Andrew Becherer
Chief Security Officer
Most importantly, what should I do now?
We strongly recommend that you immediately revoke or rotate any credentials in use in your Datadog account as described in our email.
For AWS users, Datadog supports two mechanisms of integration. As you update AWS integration credentials we strongly encourage the use of AWS IAM Role Delegation. This stronger method of AWS integration prevents the sharing of security credentials, such as access keys, between accounts.
Are the emails I received today from Datadog legitimate?
We sent two emails:
A password reset notice that was sent to all users with a stored password (Google Auth and SAML users aren’t affected)
A security notice that was sent to all admin users, instructing them to rotate / revoke credentials stored in Datadog
If you have any concerns about the legitimacy of any email you have received from Datadog know that you can reset your password by directly visiting our site at https://app.datadoghq.com.
What happened to my Datadog password?
Passwords are stored using bcrypt with a unique salt, but out of caution we have invalidated all stored Datadog passwords (Google Auth and SAML users aren’t affected). You can reset a new password at https://app.datadoghq.com.
What is the scope of the incident?
We have detected unauthorized activity associated with a handful of production infrastructure servers, including a database that stores user credentials. A user also has reported unsuccessful attempts to use AWS credentials shared with Datadog. To err on the side of caution, we are recommending revocation of all credentials shared with Datadog.
What about the Datadog agents running on my servers?
Any Datadog agents running on your servers are not affected by this incident. They were designed to never receive any data or code from our servers. They are also isolated from our own infrastructure, only ever communicating outbound from your instances to us via HTTPS. Our agents do not send local credentials to Datadog servers for storage.
What is the current status of the Datadog infrastructure?
Datadog is currently operational. We have rebuilt all identified compromised systems and additional infrastructure. Any known vulnerabilities have been mitigated.
Will I get a post-mortem? What will you do to make sure it doesn’t happen again?
We’re still piecing together the attack and we have brought in third party incident response and forensics experts. We expect forensics to continue well into next week. A post-mortem and longer term plans will follow.