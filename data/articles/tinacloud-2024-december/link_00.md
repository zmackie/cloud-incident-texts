Title: TinaCloud: Public Disclosure of Security Breach | TinaCMS Blog

URL Source: https://tina.io/blog/2024-12-tinacloud-public-disclosure-security-breach

Markdown Content:
# TinaCloud: Public Disclosure of Security Breach | TinaCMS Blog

[Loving Tina? us on GitHub 0.0k](https://github.com/tinacms/tinacms)

We use cookies to improve your experience. By continuing, you accept our [cookie policy](https://tina.io/privacy-notice).

Accept All Reject All

Manage cookies

[](https://tina.io/)

![Image 1: English Flag](https://tina.io/_next/image?url=%2Fflags%2Fen.png&w=48&q=75)

[My TinaCloud](https://app.tina.io/)
*   TinaCMS
    *   [Home](https://tina.io/tinacms)
    *   [Docs for TinaCMS](https://tina.io/docs)
    *   [Videos](https://www.youtube.com/c/tinacms)
    *   [Showcase](https://tina.io/showcase)
    *   [What's New in TinaCMS](https://tina.io/whats-new/tinacms)

*   TinaDocs
    *   [Home](https://tina.io/tinadocs)
    *   [Docs for TinaDocs](https://tina.io/tinadocs/docs)

*   TinaCloud
    *   [Pricing](https://tina.io/pricing)
    *   [Enterprise](https://tina.io/enterprise)
    *   [Quickstart](https://app.tina.io/quickstart)
    *   [What's New in TinaCloud](https://tina.io/whats-new/tinacloud)

*   [Editorial Workflow](https://tina.io/editorial-workflow)
*   Community
    *   [Events](https://tina.io/events)
    *   [Certifications](https://tina.io/certifications)
    *   [Awesome TinaCMS](https://github.com/tinacms/awesome-tinacms)
    *   [Discord](https://discord.com/invite/zumN63Ybpf)
    *   [Support](https://tina.io/docs/support)
    *   [Forum](https://github.com/tinacms/tinacms/discussions)
    *   [Roadmap](https://tina.io/roadmap)

*   About
    *   [About Tina](https://tina.io/about)
    *   [Compare TinaCMS](https://tina.io/compare-tina)
    *   [Blog](https://tina.io/blog)
    *   [Examples](https://tina.io/examples)
    *   Contact Us

[](https://tina.io/)

[](https://tina.io/)
*   TinaCMS 
    *   [Home](https://tina.io/tinacms)
    *   [Docs for TinaCMS](https://tina.io/docs)
    *   [Videos](https://www.youtube.com/c/tinacms)
    *   [Showcase](https://tina.io/showcase)
    *   [What's New in TinaCMS](https://tina.io/whats-new/tinacms)

*   TinaDocs 
    *   [Home](https://tina.io/tinadocs)
    *   [Docs for TinaDocs](https://tina.io/tinadocs/docs)

*   TinaCloud 
    *   [Pricing](https://tina.io/pricing)
    *   [Enterprise](https://tina.io/enterprise)
    *   [Quickstart](https://app.tina.io/quickstart)
    *   [What's New in TinaCloud](https://tina.io/whats-new/tinacloud)

*   [Editorial Workflow](https://tina.io/editorial-workflow)
*   Community 
    *   [Events](https://tina.io/events)
    *   [Certifications](https://tina.io/certifications)
    *   [Awesome TinaCMS](https://github.com/tinacms/awesome-tinacms)
    *   [Discord](https://discord.com/invite/zumN63Ybpf)
    *   [Support](https://tina.io/docs/support)
    *   [Forum](https://github.com/tinacms/tinacms/discussions)
    *   [Roadmap](https://tina.io/roadmap)

*   About 
    *   [About Tina](https://tina.io/about)
    *   [Compare TinaCMS](https://tina.io/compare-tina)
    *   [Blog](https://tina.io/blog)
    *   [Examples](https://tina.io/examples)
    *   Contact Us

*   [My TinaCloud](https://app.tina.io/)![Image 2: English Flag](https://tina.io/_next/image?url=%2Fflags%2Fen.png&w=48&q=75)

# TinaCloud: Public Disclosure of Security Breach

By**Matt Wicks**December 23, 2024

## [Overview of the Incident](https://tina.io/blog/2024-12-tinacloud-public-disclosure-security-breach#overview-of-the-incident)

On 15th December 2024, TinaCMS identified unauthorized activity involving compromised AWS access keys. These keys were exploited to send unauthorized emails (targeting the general French community, not Tina customers specifically) using our Amazon Simple Email Service (SES) infrastructure.

![Image 3: A screenshot of one of the phishing emails](https://assets.tina.io/06bcd49e-f919-4e53-a2c4-77f656491c7d/img/blog/2024-12-tinacloud-public-disclosure-security-breach/phishing-email.png)

Figure: The emails sent were in French

As an automated measure, the impacted key was revoked. Afterwards, our team confirmed the extent of the incident using CloudTrail logs, investigated root cause, and took steps (described below) to secure our systems.

Outbound email functionality, including user invitations, was impacted. This has since been resolved.

We apologize for this, and we are confident that it won’t happen again.

## [Incident Details](https://tina.io/blog/2024-12-tinacloud-public-disclosure-security-breach#incident-details)

Incident start: 13th December 2024, 16:33 GMT+11

Time of Detection: 15th December 2024, 19:05 GMT+11

Type of Incident: Unauthorized use of AWS access keys

Services Impacted:

*   Amazon SES (email sending) 
*   User invitation workflows relying on outbound email 

Nature of Access:

*   AWS access keys with root permissions were compromised and misused 

Verification:

*   CloudTrail logs were used to confirm which systems and services were accessed during the incident 

## [Root Cause Analysis](https://tina.io/blog/2024-12-tinacloud-public-disclosure-security-breach#root-cause-analysis)

The unauthorized access was traced to a vulnerability in our CI/CD pipeline. During the build process, a step in the GitHub Actions workflow inadvertently wrote the GitHub Actions Runner’s environment variables, including sensitive AWS access keys, to a JavaScript file.

The JavaScript file containing the keys was subsequently deployed and served publicly as part of TinaCloud, allowing attackers to obtain the access keys directly from the front-end code.

## [Impact Assessment](https://tina.io/blog/2024-12-tinacloud-public-disclosure-security-breach#impact-assessment)

**Customer Data:**

✅ Based off CloudTrail logs, there was no evidence of unauthorized access to customer data. This includes content databases, end user login information, access to application secrets.

**Affected Systems:**

⚠️ Amazon SES for email-sending functionality

**User Impact:**

❌ Temporary suspension of email services impacted workflows, including user invitations

## [Actions Taken](https://tina.io/blog/2024-12-tinacloud-public-disclosure-security-breach#actions-taken)

1.   ✅ Done - Revoked all access keys: All compromised and legacy AWS access keys were revoked immediately 
2.   ✅ Done - Verification of access: CloudTrail logs were reviewed to identify and confirm systems accessed by the unauthorized actor 
3.   ✅ Done - Confirmed security controls: MFA (Multi-Factor Authentication) is enabled on all user accounts that have console access Revoked access to all unnecessary users 
4.   ✅ Done - Suspension of email sending: Outbound email services were temporarily suspended whilst we were ascertaining root cause and AWS’s review. Services have now been restored. 
5.   ✅ Done - CI/CD AWS access: Authentication for the GitHub Actions has been upgraded from long lived Access Keys to OIDC 
6.   ✅ Done - Build process: The build process was reviewed, and the handling of environment variables was updated. The use of process.env was replaced with import.meta, following best practices outlined in [Vite’s documentation](https://vite.dev/config/shared-options.html#define), to prevent sensitive data from being exposed in build artifacts. 
7.   ✅ Done - Repository secrets audit: A thorough audit of all GitHub repositories is being conducted to identify any other sensitive information that may have been inadvertently exposed in past builds or commits 
8.   ✅ Done - Hardened IAM policies: IAM policies tied to CI/CD systems have been reviewed and updated to ensure adherence to least privilege principles, removing unnecessary permissions, especially those with root or administrative access 
9.   ✅ Done - IP allow listing for AWS access: AWS IAM role usage has been restricted to trusted IP ranges, particularly for CI/CD systems and other sensitive operations 
10.   ✅ Done - Continuous monitoring and alerts: Continuous monitoring tools like Amazon GuardDuty, AWS CloudTrail Insights, and AWS Security Hub will be implemented to detect and alert on suspicious activity, such as new access key creation or unusual IP access 
11.   [TODO] Automated security scans: Automated tools will be integrated into the CI/CD pipeline to proactively detect secrets or vulnerabilities during code builds 

## [Advice to Tina Customers](https://tina.io/blog/2024-12-tinacloud-public-disclosure-security-breach#advice-to-tina-customers)

1.   Report suspicious emails: If you received unauthorized or suspicious emails from TinaCMS, please report them to [security@tina.io](mailto:security@tina.io) 
2.   Verify email origin: Ensure any emails claiming to be from TinaCMS are legitimate 
3.   Stay updated: Follow our official communication channels for real-time updates 

## [Contact Information](https://tina.io/blog/2024-12-tinacloud-public-disclosure-security-breach#contact-information)

For questions, concerns, or further information, please contact:

*   Email: [security@tina.io](mailto:security@tina.io) 
*   Website: [https://tina.io/security](https://tina.io/security) 

TinaCMS remains committed to protecting our systems and maintaining transparency.

🦙 The Tina herd

Last Edited: August 18, 2025

[Last Page ##### Enhanced Security for TinaCloud: Multi-Factor Authentication is Here](https://tina.io/blog/two-factor-authentication)

## Join the Herd!

Join our coding community for the latest tips and news.

Subscribe

[](https://tina.io/)

Product

[Showcase](https://tina.io/showcase)[TinaCloud](https://app.tina.io/)[How Tina Works](https://tina.io/docs/product-tour)[Roadmap](https://tina.io/roadmap)[Compare Tina](https://tina.io/compare-tina)

Resources

[Blog](https://tina.io/blog)[Documentation](https://tina.io/docs)[Examples](https://tina.io/examples)[Support](https://tina.io/docs/support)[Media](https://tina.io/media)

What's New

[TinaCMS](https://tina.io/whats-new/tinacms)

[TinaCloud](https://tina.io/whats-new/tinacloud)

Use Cases

[Agencies](https://tina.io/agencies)

[Documentation](https://tina.io/documentation)

[Teams](https://tina.io/cms-for-teams)

[Jamstack CMS](https://tina.io/jamstack-cms)

Benefits

[MDX](https://tina.io/mdx-cms)

[Markdown](https://tina.io/markdown-cms)

[Git](https://tina.io/git-cms)

[Editorial Workflow](https://tina.io/editorial-workflow)

[Customization](https://tina.io/flexible-cms)

[Seo](https://tina.io/seo)

Integrations

[Astro](https://tina.io/astro)

[Hugo](https://tina.io/hugo-cms)

[NextJS](https://tina.io/nextjs-cms)

[Jekyll](https://tina.io/jekyll-cms)

## Join the Herd!

Join our coding community for the latest tips and news.

Subscribe

[](https://tina.io/)

[![Image 4: GitHub](https://tina.io/github-mark-white.svg)](https://github.com/tinacms/tinacms)[![Image 5: X](https://tina.io/logo.svg)](https://x.com/tinacms)[![Image 6: Discord](https://tina.io/icon_clyde_white_RGB.svg)](https://discord.com/invite/zumN63Ybpf)[![Image 7: YouTube](https://tina.io/youtube-logo-white1.svg)](https://www.youtube.com/@TinaCMS)[![Image 8: LinkedIn](https://tina.io/LinkedIn_icon-white1.svg)](https://www.linkedin.com/company/tinacms)[![Image 9: Facebook](https://tina.io/svg/facebook-logo.svg)](https://www.facebook.com/profile.php?id=61572968406294)

[Security](https://tina.io/security)[Telemetry](https://tina.io/telemetry)[Terms of Service](https://tina.io/terms-of-service)[Privacy](https://tina.io/privacy-notice)[License](https://github.com/tinacms/tinacms/blob/master/LICENSE)Contact Us

© TinaCMS 2019–2026

[TinaCMS is maintained by, Australia's leading software consultants](https://www.ssw.com.au/)