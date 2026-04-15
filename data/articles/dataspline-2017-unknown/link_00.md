Title: At listen.dev, we are building a tool for proactive security monitoring and threat detection in CI/CD workflows to secure software releases from supply chain threats.

URL Source: https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712

Published Time: 2024-07-18T14:45:12.721Z

Markdown Content:
# Detection & Response for Modern Linux Workloads | Umar Sikander

Agree & Join LinkedIn

By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy).

[Skip to main content](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712#main-content)[LinkedIn](https://www.linkedin.com/?trk=public_post_nav-header-logo)
*   [Top Content](https://www.linkedin.com/top-content?trk=public_post_guest_nav_menu_topContent)
*   [People](https://www.linkedin.com/pub/dir/+/+?trk=public_post_guest_nav_menu_people)
*   [Learning](https://www.linkedin.com/learning/search?trk=public_post_guest_nav_menu_learning)
*   [Jobs](https://www.linkedin.com/jobs/search?trk=public_post_guest_nav_menu_jobs)
*   [Games](https://www.linkedin.com/games?trk=public_post_guest_nav_menu_games)

[Sign in](https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&fromSignIn=true&trk=public_post_nav-header-signin)[Join now](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_nav-header-join)[![Image 1](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712)](https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&fromSignIn=true&trk=public_post_nav-header-signin)

# Umar Sikander’s Post

[![Image 2: View profile for Umar Sikander](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712)](https://ca.linkedin.com/in/umarsikander?trk=public_post_feed-actor-image)

[Umar Sikander](https://ca.linkedin.com/in/umarsikander?trk=public_post_feed-actor-name)

 1y  Edited 

*   [Report this post](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting)

At [listen.dev](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2Flisten%2Edev&urlhash=qBRq&trk=public_post-text), we are building a tool for proactive security monitoring and threat detection in CI/CD workflows to secure software releases from supply chain threats. Why we built this: As friends and collaborators for over a decade, we've been working on various startup ideas in dev tools and infrastructure. In 2017, while building an ML ops toolkit on Kubernetes, we got hacked. During a pilot with a fintech customer, our cluster became victim to a crypto-jacking attack. As it turned out, a dependency in our container base image contained malware (a Monero miner) which triggered inside the customer's environment. Needless to say, we lost the customer and racked up a massive cloud bill as a tiny startup. This first-hand experience introduced us to one of the biggest challenges in software security today. The Problem: Modern engineering teams rely heavily on 3rd parties—from open source packages, base images and 3rd-party tooling to build & deploy software quickly. But this creates security blind spots exploited in modern supply chain attacks. Some high-profile cases targeting developer environments include: (1) event-stream: a malicious transitive dependency injected a wallet-drainer payload into the build process for CoPay’s bitcoin wallet (2) SolarWinds: a compromised build tool injected malicious code into downstream releases (3) Codecov: a bash uploader script inside the testing tool stole secrets when run in CI While most teams today incorporate some form of security scanning, it typically focuses on known vulnerabilities. In contrast, we detect zero-day threats and harden your build & release processes against malicious activity. With a focus on developer experience. Enter [listen.dev](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2Flisten%2Edev&urlhash=qBRq&trk=public_post-text): a tool to analyze the behavior of your GitHub Actions workflows and provide insights into anomalous and malicious behaviours. How it works: - Native integration via a simple workflow step. You can instrument your build, test, and release processes in any language or stack. - Observes low-level behaviors using eBPF (network, file, process signals) over each run - Detects anomalies and malicious activity using threat intelligence and out-of-the-box detections for known bads (e.g., info stealers making unknown network connections, reverse shells, tampering of builds etc.) - Offers in-line PR feedback with context, plugging into existing toolchains via webhook. Behind [listen.dev](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2Flisten%2Edev&urlhash=qBRq&trk=public_post-text) is a team of builders and OSS maintainers with years of experience in security observability and developer tools—having previously worked on eBPF runtime security projects like Falco and Tracee. We're seeking feedback from DevOps and security folks to help us improve. You can sign up for free at[https://lstn.dev/hn](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flstn%2Edev%2Fhn&urlhash=3VC0&trk=public_post-text), install our GitHub action in under a minute, and start monitoring your repos. We'd love to hear from you–any feedback and questions are welcome. To learn more see[https://docs.listen.dev](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fdocs%2Elisten%2Edev&urlhash=uK45&trk=public_post-text).

[![Image 3: listen.dev · Security Monitoring for GitHub Actions](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712) listen.dev · Security Monitoring for GitHub Actions listen.dev](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fwww%2Elisten%2Edev%2F&urlhash=qXL4&trk=public_post_feed-article-content)

[![Image 4](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712)![Image 5](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712)![Image 6](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712) 76](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_social-actions-reactions)[3 Comments](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_social-actions-comments)

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_like-cta)[Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_comment-cta)

 Share 
*   Copy
*   LinkedIn
*   Facebook
*   X

[![Image 7: Ghassan Ahmed, graphic](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712)](https://pk.linkedin.com/in/ghassan-ahmed-?trk=public_post_comment_actor-image)

[Ghassan Ahmed](https://pk.linkedin.com/in/ghassan-ahmed-?trk=public_post_comment_actor-name) 1y 

*   [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

👏

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_comment_like)[Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_comment_reply) 1 Reaction 

[![Image 8: Ali Sikander, graphic](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712)](https://pk.linkedin.com/in/ali-sikander-1178bb183?trk=public_post_comment_actor-image)

[Ali Sikander](https://pk.linkedin.com/in/ali-sikander-1178bb183?trk=public_post_comment_actor-name) 1y 

*   [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

Interesting! Would love to use this tool

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_comment_like)[Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_comment_reply) 1 Reaction 

[![Image 9: Muhammad Mustafa Kiani, graphic](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712)](https://pk.linkedin.com/in/muhammad-mustafa-kiani-247ba388?trk=public_post_comment_actor-image)

[Muhammad Mustafa Kiani](https://pk.linkedin.com/in/muhammad-mustafa-kiani-247ba388?trk=public_post_comment_actor-name) 1y 

*   [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

Interesting!

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_comment_like)[Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_comment_reply) 1 Reaction 

[See more comments](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_see-more-comments)
To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_feed-cta-banner-cta)

![Image 10](https://static.licdn.com/aero-v1/sc/h/5q92mjc5c51bjlwaj3rs9aa82)

![Image 11: Umar Sikander](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712)
3,066 followers

*   [21 Posts](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fin%2Fumarsikander%2Frecent-activity%2F&trk=public_post_follow-posts)

[View Profile](https://ca.linkedin.com/in/umarsikander?trk=public_post_follow-view-profile)[Follow](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2Fupdate%2Furn%3Ali%3Aactivity%3A7219713829528563712&trk=public_post_follow)

## Explore content categories

*   [Career](https://www.linkedin.com/top-content/career/)
*   [Productivity](https://www.linkedin.com/top-content/productivity/)
*   [Finance](https://www.linkedin.com/top-content/finance/)
*   [Soft Skills & Emotional Intelligence](https://www.linkedin.com/top-content/soft-skills-emotional-intelligence/)
*   [Project Management](https://www.linkedin.com/top-content/project-management/)
*   [Education](https://www.linkedin.com/top-content/education/)
*   [Technology](https://www.linkedin.com/top-content/technology/)
*   [Leadership](https://www.linkedin.com/top-content/leadership/)
*   [Ecommerce](https://www.linkedin.com/top-content/ecommerce/)
*   [User Experience](https://www.linkedin.com/top-content/user-experience/)

 Show more  Show less 

*   LinkedIn© 2026
*   [About](https://about.linkedin.com/?trk=d_public_post_footer-about)
*   [Accessibility](https://www.linkedin.com/accessibility?trk=d_public_post_footer-accessibility)
*   [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=d_public_post_footer-user-agreement)
*   [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=d_public_post_footer-privacy-policy)
*   [Your California Privacy Choices](https://www.linkedin.com/legal/california-privacy-disclosure?trk=d_public_post_footer-california-privacy-rights-act)
*   [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=d_public_post_footer-cookie-policy)
*   [Copyright Policy](https://www.linkedin.com/legal/copyright-policy?trk=d_public_post_footer-copyright-policy)
*   [Brand Policy](https://brand.linkedin.com/policies?trk=d_public_post_footer-brand-policy)
*   [Guest Controls](https://www.linkedin.com/psettings/guest-controls?trk=d_public_post_footer-guest-controls)
*   [Community Guidelines](https://www.linkedin.com/legal/professional-community-policies?trk=d_public_post_footer-community-guide)
*   
    *    العربية (Arabic) 
    *    বাংলা (Bangla) 
    *    Čeština (Czech) 
    *    Dansk (Danish) 
    *    Deutsch (German) 
    *    Ελληνικά (Greek) 
    *   **English (English)**
    *    Español (Spanish) 
    *    فارسی (Persian) 
    *    Suomi (Finnish) 
    *    Français (French) 
    *    हिंदी (Hindi) 
    *    Magyar (Hungarian) 
    *    Bahasa Indonesia (Indonesian) 
    *    Italiano (Italian) 
    *    עברית (Hebrew) 
    *    日本語 (Japanese) 
    *    한국어 (Korean) 
    *    मराठी (Marathi) 
    *    Bahasa Malaysia (Malay) 
    *    Nederlands (Dutch) 
    *    Norsk (Norwegian) 
    *    ਪੰਜਾਬੀ (Punjabi) 
    *    Polski (Polish) 
    *    Português (Portuguese) 
    *    Română (Romanian) 
    *    Русский (Russian) 
    *    Svenska (Swedish) 
    *    తెలుగు (Telugu) 
    *    ภาษาไทย (Thai) 
    *    Tagalog (Tagalog) 
    *    Türkçe (Turkish) 
    *    Українська (Ukrainian) 
    *    Tiếng Việt (Vietnamese) 
    *    简体中文 (Chinese (Simplified)) 
    *    正體中文 (Chinese (Traditional)) 

 Language 

![Image 12](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712)
## Sign in to view more content

Create your free account or sign in to continue your search

 Email or phone  

 Password  

Show

[Forgot password?](https://www.linkedin.com/uas/request-password-reset?trk=csm-v2_forgot_password) Sign in 

Sign in with Email

or

New to LinkedIn? [Join now](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fumarsikander_detection-response-for-modern-linux-workloads-activity-7219713829528563712-nODc&trk=public_post_contextual-sign-in-modal_join-link)

By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy).

[](https://www.linkedin.com/feed/update/urn:li:activity:7219713829528563712)