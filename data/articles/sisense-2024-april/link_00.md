Title: Why CISA is Warning CISOs About a Breach at Sisense

URL Source: https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/

Published Time: Tue, 14 Apr 2026 19:40:22 GMT

Markdown Content:
# Why CISA is Warning CISOs About a Breach at Sisense – Krebs on Security

Advertisement

[![Image 1](https://krebsonsecurity.com/b-keeper/17.png)](https://www.keepersecurity.com/free-data-breach-scan.html?utm_source=Krebs&utm_medium=display+ad&utm_campaign=Krebs_ads)

Advertisement

[![Image 2](https://krebsonsecurity.com/b-doppel/14.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=deepfake)

[](http://twitter.com/briankrebs)[](https://krebsonsecurity.com/feed/)[](https://www.linkedin.com/in/bkrebs/)

[![Image 3: Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[](http://twitter.com/briankrebs)[](https://krebsonsecurity.com/feed/)[](https://www.linkedin.com/in/bkrebs/)

[Skip to content](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#content "Skip to content")

*   [Home](https://krebsonsecurity.com/)
*   [About the Author](https://krebsonsecurity.com/about/)
*   [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Why CISA is Warning CISOs About a Breach at Sisense

April 11, 2024

[33 Comments](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comments)

The **U.S. Cybersecurity and Infrastructure Security Agency** (CISA) said today it is investigating a breach at business intelligence company **Sisense**, whose products are designed to allow companies to view the status of multiple third-party online services in a single dashboard. CISA urged all Sisense customers to reset any credentials and secrets that may have been shared with the company, which is the same advice Sisense gave to its customers Wednesday evening.

![Image 4](https://krebsonsecurity.com/wp-content/uploads/2024/04/sisense.png)

New York City based Sisense has more than a thousand customers across a range of industry verticals, including financial services, telecommunications, healthcare and higher education. On April 10, **Sisense Chief Information Security Officer Sangram Dash** told customers the company had been made aware of reports that “certain Sisense company information may have been made available on what we have been advised is a restricted access server (not generally available on the internet.)”

“We are taking this matter seriously and promptly commenced an investigation,” Dash continued. “We engaged industry-leading experts to assist us with the investigation. This matter has not resulted in an interruption to our business operations. Out of an abundance of caution, and while we continue to investigate, we urge you to promptly rotate any credentials that you use within your Sisense application.”

In its alert, CISA said it was working with private industry partners to respond to a recent compromise discovered by independent security researchers involving Sisense.

“CISA is taking an active role in collaborating with private industry partners to respond to this incident, especially as it relates to impacted critical infrastructure sector organizations,” the sparse alert reads. “We will provide updates as more information becomes available.”

![Image 5](https://krebsonsecurity.com/wp-content/uploads/2024/04/cisa-sisense.png)

Sisense declined to comment when asked about the veracity of information shared by two trusted sources with close knowledge of the breach investigation. Those sources said the breach appears to have started when the attackers somehow gained access to the company’s Gitlab code repository, and in that repository was a token or credential that gave the bad guys access to Sisense’s Amazon S3 buckets in the cloud.

Customers can use Gitlab either as a solution that is hosted in the cloud at Gitlab.com, or as a self-managed deployment. KrebsOnSecurity understands that Sisense was using the self-managed version of Gitlab.

Both sources said the attackers used the S3 access to copy and exfiltrate several terabytes worth of Sisense customer data, which apparently included millions of access tokens, email account passwords, and even SSL certificates.

The incident raises questions about whether Sisense was doing enough to protect sensitive data entrusted to it by customers, such as whether the massive volume of stolen customer data was ever encrypted while at rest in these Amazon cloud servers.

It is clear, however, that unknown attackers now have all of the credentials that Sisense customers used in their dashboards.

The breach also makes clear that Sisense is somewhat limited in the clean-up actions that it can take on behalf of customers, because access tokens are essentially text files on your computer that allow you to stay logged in for extended periods of time — sometimes indefinitely. And depending on which service we’re talking about, it may be possible for attackers to re-use those access tokens to authenticate as the victim without ever having to present valid credentials.

Beyond that, it is largely up to Sisense customers to decide if and when they change passwords to the various third-party services that they’ve previously entrusted to Sisense.

Earlier today, a public relations firm working with Sisense reached out to learn if KrebsOnSecurity planned to publish any further updates on their breach (KrebsOnSecurity posted a screenshot of the CISO’s customer email to both [LinkedIn](https://www.linkedin.com/posts/bkrebs_there-is-something-potentially-huge-popping-activity-7183982303784620033-T3wd?utm_source=share&utm_medium=member_desktop) and [Mastodon](https://infosec.exchange/@briankrebs/112249710611213991) on Wednesday evening). The PR rep said Sisense wanted to make sure they had an opportunity to comment before the story ran.

But when confronted with the details shared by my sources, Sisense apparently changed its mind.

“After consulting with Sisense, they have told me that they don’t wish to respond,” the PR rep said in an emailed reply.

**Update, 6:49 p.m., ET:** Added clarification that Sisense is using a self-hosted version of Gitlab, not the cloud version managed by Gitlab.com.

Also, Sisense’s CISO Dash just sent an update to customers directly. The latest advice from the company is far more detailed, and involves resetting a potentially large number of access tokens across multiple technologies, including Microsoft Active Directory credentials, GIT credentials, web access tokens, and any single sign-on (SSO) secrets or tokens.

The full message from Dash to customers is below:

“Good Afternoon,

We are following up on our prior communication of April 10, 2024, regarding reports that certain Sisense company information may have been made available on a restricted access server. As noted, we are taking this matter seriously and our investigation remains ongoing.

Our customers must reset any keys, tokens, or other credentials in their environment used within the Sisense application.

Specifically, you should:

 – Change Your Password: Change all Sisense-related passwords on http://my.sisense.com

 – Non-SSO:

 – Replace the Secret in the Base Configuration Security section with your GUID/UUID.

 – Reset passwords for all users in the Sisense application.

 – Logout all users by running GET /api/v1/authentication/logout_all under Admin user.

 – Single Sign-On (SSO):

 – If you use SSO JWT for the user’s authentication in Sisense, you will need to update sso.shared_secret in Sisense and then use the newly generated value on the side of the SSO handler.

 – We strongly recommend rotating the x.509 certificate for your SSO SAML identity provider.

 – If you utilize OpenID, it’s imperative to rotate the client secret as well.

 – Following these adjustments, update the SSO settings in Sisense with the revised values.

 – Logout all users by running GET /api/v1/authentication/logout_all under Admin user.

 – Customer Database Credentials: Reset credentials in your database that were used in the Sisense application to ensure continuity of connection between the systems.

 – Data Models: Change all usernames and passwords in the database connection string in the data models.

 – User Params: If you are using the User Params feature, reset them.

 – Active Directory/LDAP: Change the username and user password of users whose authorization is used for AD synchronization.

 – HTTP Authentication for GIT: Rotate the credentials in every GIT project.

 – B2D Customers: Use the following API PATCH api/v2/b2d-connection in the admin section to update the B2D connection.

 – Infusion Apps: Rotate the associated keys.

 – Web Access Token: Rotate all tokens.

 – Custom Email Server: Rotate associated credentials.

 – Custom Code: Reset any secrets that appear in custom code Notebooks.

If you need any assistance, please submit a customer support ticket at https://community.sisense.com/t5/support-portal/bd-p/SupportPortal and mark it as critical. We have a dedicated response team on standby to assist with your requests.

At Sisense, we give paramount importance to security and are committed to our customers’ success. Thank you for your partnership and commitment to our mutual security.

Regards,

Sangram Dash

 Chief Information Security Officer”

_This entry was posted on Thursday 11th of April 2024 04:48 PM_

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/)[Data Breaches](https://krebsonsecurity.com/category/data-breaches/)[The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[Nicholas Weaver](https://krebsonsecurity.com/tag/nicholas-weaver/)[Sangram Dash](https://krebsonsecurity.com/tag/sangram-dash/)[Sisense breach](https://krebsonsecurity.com/tag/sisense-breach/)[U.S. Cybersecurity and Infrastructure Security Agency](https://krebsonsecurity.com/tag/u-s-cybersecurity-and-infrastructure-security-agency/)

Post navigation

[← Twitter’s Clumsy Pivot to X.com Is a Gift to Phishers](https://krebsonsecurity.com/2024/04/twitters-clumsy-pivot-to-x-com-is-a-gift-to-phishers/)[Crickets from Chirp Systems in Smart Lock Key Leak →](https://krebsonsecurity.com/2024/04/crickets-from-chirp-systems-in-smart-lock-key-leak/)

## 33 thoughts on “Why CISA is Warning CISOs About a Breach at Sisense”

1.   oakgrove [April 11, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608056)
“If they are telling people to rest credentials”

rest -> reset

 
2.   RipNoLonger [April 11, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608057)
Almost makes me wonder if some of these companies aren’t deliberately mishandling very sensitive information.

 This is conspiratorial, but wouldn’t it be logical for a foreign agency to sell a central dashboard to collect as many credentials as possible?

How can they be that stupid to not encrypt every single bit of customer data – not just security info but everything (company names, addresses, etc.)?

 
    1.   [Huera](http://na/)[April 11, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608061)
Good point there. A honeypot in reverse.

 
    2.   Anon Software Engineer [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608112)
The problem was someone checked a secret (password, API key, TLS certificate private key, etc.) into a GIT repository.

 Unfortunately, software engineers make mistakes like this all of the time. A lot of people think computer security is easy and therefore any breach is the result of incompetence, or malice. Usually, that is not the case. Here are the big three problems:

1) People (including software engineers and operations people/sys admins/dev ops people) do not care

 2) People do not know better

 3) People do not want to put in the effort

 4) People do not want to learn

 5) People make mistakes

Solving these problems is going to be very hard and there are no easy answers.

Also, encryption is not a panacea because you still have to store a key to decrypt the data. Hackers can and will exploit security vulnerabilities to get access to the decryption key. Once they have the key, they will get the encrypted data. A good example of this I know of one company where people used to store encrypted TLS certificates in GIT. About 50% of these encrypted certificates could be easily decrypted because people choose poor passwords. The organization solved this problem by forcing people to store secrets securely.

 
        1.   Another Anon Software Engineer [April 15, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608246)
Your items 1-4 are really quite the assertion.

 

3.   Arūnas [April 11, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608058)
“The former (leaving Amazon credentials in your Git archive) is bad but forgivable.”

Not forgivable. The thing with Git is that once provided, information is hard to delete. Even if deleted, these credentials *will be there* in commit history.

 
    1.   Vall [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608086)
This is one more example of why you should *never* trust *anyone* with your sensitive information.

Instead, self-host as much as possible, and always encrypt everything.

Your future self you thank you for that.

 
        1.   Anon Software Engineer [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608113)
Unfortunately, self-hosting is probably not any better. In order for self-hosting to be better, the person doing the work has to really understand the software being hosted, and they have to consistently their infrastructure. This means they have to install security patches promptly, setup their firewalls correctly, segment their network properly, make sure they have configured the software correctly, backup the data securely (what happens if the house burns down?), etc.

My guess is most self hosters will have the same problems as professionals. The professionals have the advantage of more resources and usually have better people. An example is professional organizations are much more likely to notice they have been breached.

 

    2.   William [April 14, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608202)
It is possible to remove accidentally-included files by installing and using git-filter-repo. The full process of redaction/sanitization is extremely difficult (convoluted) and dangerous (destructive). You will need to do several dry-run tests first, make certain that you use inverted paths so that you are only deleting the offending file/s, and **make certain that there are backups™**.

Again: make certain that there are backups before doing anything. Make certain that everyone else has pushed their changes to the repo before doing anything. Make certain that everyone else has completely deleted their copy of the repo from their local disk before doing anything.

At the end of the process the entire repository has been:

 * purged of unwanted files

 * including any reference to their initial import

 * all of the commit hashes have been changed

Pushing all the changes to your master repo is an absolute pain (very convoluted). It’s easier to move the original repo to one side, upload to a new repo, and then have everyone else download from the new redacted/sanitized repo.

Assuming that you are keeping your own in-house repo: remember that your backup tapes etc have not been redacted/sanitized.

Assuming that you are using github / whoever: anything pushed may linger there “virtually” for months. To get that purged you need to contact github / whoever staff.

How long will this take? How big is your repo? Mine was not huge so I have no baseline to offer.

You may find it much easier to get to a known good state – remove the offending file/s – and start a new git repo with this known good state as a new baseline. YMMV regarding throwing away masses of history.

Good luck.

 

4.   TruthBeTold [April 11, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608059)
This is a bit surprising for an Israeli based company with their traditional focus on security but it sounds like Sisense has been in some turmoil now for a couple of years. Perhaps this was a deliberate insider? The company has been through a couple cycles of reorgs and mass layoffs.

 
5.   [Huerta](http://na/)[April 11, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608060)
Clear as mud, thanks Sisense.

 
6.   anon [April 11, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608063)
It’s still unclear if on-prem instances are affected, hoping to find out as we’re working with a customer on remediations and possibly taking precautions that aren’t necessary.

 
    1.   anon2anon [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608093)
On-prem should not be at risk unless…someone like specifically shared secrets to the on-prem with Sisense

 
    2.   anon2anon [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608094)
On-prem should not be at risk unless…someone like specifically shared secrets to the on-prem with Sisense

 

7.   Emilio [April 11, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608067)
For the record, S3 encryption would’ve not helped at all. Let’s just get that clear. Encryption in the cloud is more of a data access control rather than a data protection control. If you’re storing encrypted objects (encryption prior to storage) in S3, that’s a different story.

 
    1.   [Daniel](http://non/)[April 11, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608068)
Depends on how keys are stored although some cloud services namely Bitwarden and protonmail claim to have zero-knowledge of your keys.

 
    2.   Cyber Rockstar Ninja 10x /s [April 11, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608069)
I took Nick’s quoted remark about “S3 without using encryption on top of it” to mean encryption of the data prior to storage in S3. He knows what he’s talking about so it seems to be the fairest interpretation. To your point, folks looking to protect data in S3 buckets should heed both your warning and Nick’s.

 
        1.   an_n [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608097)
There’s S3 server-side vs client-side. S-S has 3 keymgr options, AWS, C3, or SSE-C.

 C-S is not used as frequently. I’d assume they’re NOT encrypting beyond S3’s S-S,

 whether he “knows what he’s doing” or not it’s the most common configuration and

 “S3 without using encryption on top” taken at face value = NOT encrypted beyond S3.

 If it were, would this alleged breach even matter? They’d only have garbage strings.

 
            1.   DH [April 16, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608277)
If you’re running a pure-AWS environment (which I assume Sisense was), then the specifics of the encryption are probably not relevant anyway. If they had access to an IAM role via stolen credentials, that role presumably had access to the encryption primitive as well as the S3 bucket. Either they were using AES256 S3 encryption (in which case no access is needed), S3 KMS encryption (in which case the role almost certainly had access to the KMS key as well as the S3 bucket), or client side encryption. In the case of client side encryption, the client side is also executing in AWS and the client key is likely also stored in AWS somewhere (either Secrets Manager or something like CloudHSM if you’re getting fancy). It’s possible that the attacker had access to a role w/ S3 access but not Secrets Manager access, but more likely that the compromised role had access to both. So overall, I think Weaver’s comment is a bit silly. They were likely using encryption, but it wasn’t a relevant control against disclosure of the credentials that had access to the data & the key.

 
                1.   an_n [April 16, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608308)
“They were likely using encryption, but it wasn’t a relevant control against disclosure of the credentials that had access to the data & the key.”

 Well described. Eggs in single basket = shell thickness is no help.

 

8.   [Catwhisperer](https://happycattech.com/)[April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608074)
The ramifications of preforming that list are manifold, and few but a systems admin are going to understand some of it. Some of the Active Directory suggestions, just as an example, have the potential of shutting down the organization, if there is a mistake or problem. All one can say is JFC… BTW, when will CFO’s and CEO’s realize that we are at war?

 
    1.   Anon Software Engineer [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608114)
If you are a competent system administrator or operations person, you can easily preform all of those actions.

 

9.   Mmmm [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608078)
It would be good to understand what is in S3 files.

 Total size indicates that, most likely there is a lot of raw client data and keys can be only the tip of the iceberg

 
10.   Dave M. [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608087)
First, I know nothing on the subject. When I saw the list of what customers should do I can only think that very few will perform all of these tasks in a timely manner. I wonder how long it would take to have meetings and discussions in a corporation to discuss the impact to their users that these changes are going to have, scheduling downtime in order to avoid loss of yearly bonuses, as well as affecting the CEOs vacation schedule.

 
    1.   Anon Software Engineer [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608115)
All of the tasks boil down to changing passwords. They are not hard to do and better organizations regularly rotate them (i.e. change non-user passwords periodically).

 

11.   ben [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608100)
I make it a rule to never provide third-party credentials to another service. So far, so good.

 
    1.   Anon Software Engineer [April 12, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608116)
That works until you want two services to work together. Once you need that functionality, you will have to give one service access to the other.

 

12.   Bob [April 13, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608141)
“At Sisense, we give paramount importance to security and are committed to our customers’ success.”

 Evidently not.

 
13.   Office ally [April 15, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608211)
It’s always a good practice for organizations to stay vigilant, maintain robust cybersecurity measures, and promptly respond to any security advisories or warnings from trusted sources like CISA.

 
    1.   Wannabe Techguy [April 15, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608230)
I’m not a security guy, but this all makes sense. Dare I say “common” sense? But, I am curious, why is CISA “trusted”?

 
        1.   Fr00tL00ps [April 15, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608260)
CISA is the federal agency responsible for cybersecurity and infrastructure security in the United States under the remit of the Dept. of Homeland Security.

 Unless you are a conspiracy theorist, why wouldn’t you ‘trust’ them?

 And if not, who would you ‘trust’ to publish security advisories or cyber related warnings to the general public?

 

14.   Fr00tL00ps [April 15, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608258)
CISA is the federal agency responsible for cybersecurity and infrastructure security in the United States under the remit of the Dept. of Homeland Security.

 Unless you are a conspiracy theorist, why wouldn’t you ‘trust’ them?

 And if not, who would you ‘trust’ to publish security advisories or cyber related warnings to the general public?

 
    1.   Fr00tL00ps [April 16, 2024](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/#comment-608306)
Oops. This was a reply to Wannabe Techguy above. Pls ignore.

 

Comments are closed.

Advertisement

[![Image 6](https://krebsonsecurity.com/b-keeper/19.png)](https://www.keepersecurity.com/free-data-breach-scan.html?utm_source=Krebs&utm_medium=display+ad&utm_campaign=Krebs_ads)

Advertisement

Mailing List

[Subscribe here](https://krebsonsecurity.com/subscribe/)

Search KrebsOnSecurity

Search for: 

Recent Posts

*   [Russia Hacked Routers to Steal Microsoft Office Tokens](https://krebsonsecurity.com/2026/04/russia-hacked-routers-to-steal-microsoft-office-tokens/)
*   [Germany Doxes “UNKN,” Head of RU Ransomware Gangs REvil, GandCrab](https://krebsonsecurity.com/2026/04/germany-doxes-unkn-head-of-ru-ransomware-gangs-revil-gandcrab/)
*   [‘CanisterWorm’ Springs Wiper Attack Targeting Iran](https://krebsonsecurity.com/2026/03/canisterworm-springs-wiper-attack-targeting-iran/)
*   [Feds Disrupt IoT Botnets Behind Huge DDoS Attacks](https://krebsonsecurity.com/2026/03/feds-disrupt-iot-botnets-behind-huge-ddos-attacks/)
*   [Iran-Backed Hackers Claim Wiper Attack on Medtech Firm Stryker](https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wiper-attack-on-medtech-firm-stryker/)

[](https://krebsonsecurity.com/2024/04/why-cisa-is-warning-cisos-about-a-breach-at-sisense/)

Story Categories

*   [A Little Sunshine](https://krebsonsecurity.com/category/sunshine/)
*   [All About Skimmers](https://krebsonsecurity.com/category/all-about-skimmers/)
*   [Ashley Madison breach](https://krebsonsecurity.com/category/ashley-madison-breach/)
*   [Breadcrumbs](https://krebsonsecurity.com/category/breadcrumbs/)
*   [Data Breaches](https://krebsonsecurity.com/category/data-breaches/)
*   [DDoS-for-Hire](https://krebsonsecurity.com/category/ddos-for-hire/)
*   [DOGE](https://krebsonsecurity.com/category/doge/)
*   [Employment Fraud](https://krebsonsecurity.com/category/employment-fraud/)
*   [How to Break Into Security](https://krebsonsecurity.com/category/how-to-break-into-security/)
*   [Internet of Things (IoT)](https://krebsonsecurity.com/category/internet-of-things-iot/)
*   [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/)
*   [Ne'er-Do-Well News](https://krebsonsecurity.com/category/neer-do-well-news/)
*   [Other](https://krebsonsecurity.com/category/other/)
*   [Pharma Wars](https://krebsonsecurity.com/category/pharma-wars/)
*   [Ransomware](https://krebsonsecurity.com/category/ransomware/)
*   [Russia's War on Ukraine](https://krebsonsecurity.com/category/russias-war-on-ukraine/)
*   [Security Tools](https://krebsonsecurity.com/category/security-tools/)
*   [SIM Swapping](https://krebsonsecurity.com/category/sim-swapping/)
*   [Spam Nation](https://krebsonsecurity.com/category/spam-nation/)
*   [Target: Small Businesses](https://krebsonsecurity.com/category/smallbizvictims/)
*   [Tax Refund Fraud](https://krebsonsecurity.com/category/tax-refund-fraud/)
*   [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)
*   [Time to Patch](https://krebsonsecurity.com/category/patches/)
*   [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

Why So Many Top Hackers Hail from Russia

[![Image 7](https://krebsonsecurity.com/wp-content/uploads/2017/06/computered-580x389.png)](https://krebsonsecurity.com/2017/06/why-so-many-top-hackers-hail-from-russia/)

 © Krebs on Security - [Mastodon](https://infosec.exchange/@briankrebs)