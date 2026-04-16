---
title: "npm security update: Attack campaign using stolen OAuth tokens"
url: "https://github.blog/2022-05-26-npm-security-update-oauth-tokens/"
author: Greg Ose
published: 2022-05-26
source_type: article
source_domain: github.blog
cleanup_method: llm
---

# npm security update: Attack campaign using stolen OAuth tokens

npm’s impact analysis of the attack campaign using stolen OAuth tokens and additional findings.


[Greg Ose](https://github.blog/author/gregose/ "Posts by Greg Ose")·[@gregose](https://github.com/gregose)

 May 26, 2022 | Updated June 2, 2022 

_As of June 2, 2022, GitHub has completed directly notifying all impacted users for whom we were able to detect abuse from the attack on npm. If you have not received a notification directly from GitHub, we do not have evidence that your data was accessed by the attacker._

On April 15, we published [a blog](https://github.blog/2022-04-15-security-alert-stolen-oauth-user-tokens/) detailing an attack campaign utilizing stolen OAuth user tokens issued to two third-party GitHub.com integrators, Heroku and Travis CI. The npm organization on GitHub.com was impacted by this campaign and we have been actively investigating the impact of this attack on npm since April 12. Today, we are sharing details of what we’ve learned during our investigation and an additional, though unrelated, finding impacting npm. Below is a brief summary; read on to learn more.

*   Using stolen OAuth user tokens originating from two third-party integrators, Heroku and Travis CI, the attacker was able to escalate access to npm infrastructure and obtain the following from files exfiltrated from npm cloud storage: 
    *   A backup of skimdb.npmjs.com containing data from April 7, 2021, with the following information: 
        *   An archive of user information from 2015. This contained npm usernames, password hashes, and email addresses for roughly 100k npm users.
        *   All private npm package manifests and package metadata as of April 7, 2021.

    *   A series of CSVs containing an archive of all names and version numbers (semVer) of published versions of all npm private packages as of April 10, 2022.
    *   Private packages from two organizations.

*   Based on log and event analysis as well as package hash verification, GitHub is currently confident that the actor did not modify any published packages in the registry or publish any new versions to existing packages.
*   Following an internal discovery and additional investigation unrelated to the OAuth token attack, GitHub discovered a number of plaintext user credentials for the npm registry that were captured in internal logs following the integration of npm into GitHub logging systems. This issue was mitigated and logs containing the plaintext credentials were purged prior to the attack on npm. 

## [Unauthorized access to npm infrastructure from stolen OAuth user tokens](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/#unauthorized-access-to-npm-infrastructure-from-stolen-oauth-user-tokens)

On April 12, GitHub Security began an investigation that uncovered evidence that an attacker abused stolen OAuth user tokens issued to two third-party OAuth integrators, Heroku and Travis CI, to download data from dozens of GitHub.com organizations. One of the victim organizations impacted was npm. We do not believe the attacker obtained these tokens via a compromise of GitHub or its systems because the tokens in question are not stored by GitHub in their original, usable formats. GitHub’s initial blog post and subsequent updates regarding the attack campaign can be found on our [blog](https://github.blog/2022-04-15-security-alert-stolen-oauth-user-tokens/).

Following the discovery of npm’s initial compromise, GitHub investigated the impact to npm. Based on this analysis, we have evidence the actor was able to access internal npm data and npm customer information. Read on to learn more.

### [What happened](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/#what-happened)

Using their initial foothold of OAuth user tokens for GitHub.com, the actor was able to exfiltrate a set of private npm repositories, some of which included secrets such as AWS access keys.

Using one of these AWS access keys, the actor was able to gain access to npm’s AWS infrastructure.

With access to npm’s AWS infrastructure, the actor was able to exfiltrate an older backup of the skimdb.npmjs.com mirror, which included metadata and package manifests for all public and private packages in the npm registry as of April 7, 2021. This exfiltrated data includes READMEs, package version histories, maintainer email addresses, and package install scripts, but does NOT include the actual package artifacts, i.e., the tarballs themselves.

This database backup also contained an archive of npm user information from 2015. We identified that approximately 100k npm user login details, including account names, email addresses, and password hashes, were part of this archive. The password hashes in this archived data were generated using PBKDF2 or salted SHA1 algorithms previously used by the npm registry. These weak hashing algorithms have not been used to store npm user passwords since the npm registry began using bcrypt in 2017. Passwords belonging to the impacted users have been reset and we are in the process of notifying these users via email directly. As of [March 1, 2022](https://github.blog/2022-02-01-top-100-npm-package-maintainers-require-2fa-additional-security/), the npm registry has enabled email verification on all accounts that do not have 2FA enabled. With this additional protection, it would not be possible to compromise any npm account without access to the account’s associated email address (or, second factor if 2FA is enabled).

In our investigation, we also determined that the actor exfiltrated a set of npm inventory CSV files containing directory listings of the S3 buckets storing packages for the npm registry. These files exposed private package names and published versions as stored on the npm registry as of April 10, 2022.

Finally, the actor exfiltrated a small subset of private package contents belonging to two specific organizations. GitHub has notified these two impacted customers of their exposure directly.

Since the attacker had access to S3 resources that store npm package contents, we also investigated the integrity of these packages on the npm registry. Based on log and event analysis as well as package hash verification run on all versions of all packages, GitHub is currently confident that the actor did not modify any published packages in the registry or publish any new versions to existing packages.

### [What information was involved](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/#what-information-was-involved)

*   Approximately 100k npm usernames, password hashes, and email addresses from a 2015 archive of user information.
*   All private package manifests and metadata as of April 7, 2021.
*   Names and the semVer of published versions of all private packages as of April 10, 2022.
*   Private packages from two organizations.

### [What GitHub is doing](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/#what-github-is-doing)

Passwords belonging to the impacted users of the accessed database backup have been reset and these users are being notified. The two organizations that had private packages stolen were notified immediately after analysis confirmed the activity. Over the next few days, we will directly notify those with exposed private package manifests, metadata, and private package names and versions. We will also update this blog post when all notifications have been sent. If you did not receive any of these emails from us, we do not have evidence that your data was accessed by the attacker.

## [Plaintext credentials stored in internal logs](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/#plaintext-credentials-stored-in-internal-logs)

Unrelated to the OAuth token attack, we also recently internally discovered the storage of plaintext credentials in GitHub’s internal logging system for npm services. We mitigated this issue and purged the logs containing the plaintext credentials prior to this attack on npm. Our initial and current investigation has concluded that only internal GitHub employees had access to this data at the time of exposure. While this involved no known compromise, user privacy and security are essential for maintaining trust, and we want to remain transparent even about events like these that go against security best practices. It is in that spirit that we’re providing the information below.

### [What happened](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/#what-happened)

GitHub recently discovered that a subset of npm service logs stored in our internal logging system contained data that was not properly sanitized to remove credentials received in requests to npm services. These logs included npm access tokens and a small number of passwords used in attempts to sign in to npm accounts. While not used to authenticate to npm services, we also identified a small set of GitHub Personal Access Tokens that were sent by users to npm that were also logged in these internal systems. While this logging of credentials goes against our security best practices, GitHub or npm did not experience a compromise or data breach that would have exposed these logs containing plaintext credentials.

### [What information was involved](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/#what-information-was-involved)

Internal finding of plaintext credentials in logs:

*   npm access tokens and a small number of plaintext passwords used in attempts to sign in to npm accounts, as well as some GitHub Personal Access Tokens sent to npm services.

### [What GitHub is doing](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/#what-github-is-doing)

Upon discovery of plaintext credentials in our internal logging system, GitHub immediately identified the specific unsanitized logs and searched across all npm logs for plaintext credentials to identify similar issues in additional npm services. We mitigated all impacted services and improved our logging sanitization. We then purged all affected logs from our system. Over the next few days, we will directly notify affected users of the plaintext passwords and GitHub Personal Access Tokens based on our available logs. We will update the blog post when all notifications have been sent. We are also performing an internal assessment to determine how we can better prevent events of this nature in the future.

## [What you can do](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/#what-you-can-do)

While we have notified users with information confirmed accessed by the actor, if you would like to rotate your npm tokens, you can do so by following the instructions located here: [https://docs.npmjs.com/revoking-access-tokens](https://docs.npmjs.com/revoking-access-tokens)

If you would like to reset your password, you can do so by following this link: [https://www.npmjs.com/forgot](https://www.npmjs.com/forgot).

Please feel free to reach out to us with any additional questions or concerns through the following contact form: [https://www.npmjs.com/support](https://www.npmjs.com/support).

* * *
