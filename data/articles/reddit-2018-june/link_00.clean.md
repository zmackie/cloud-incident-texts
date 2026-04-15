---
title: We had a security incident. Here's what you need to know.
url: "https://www.reddit.com/r/announcements/comments/93qnm5/we_had_a_security_incident_heres_what_you_need_to/"
author: KeyserSosa
published: 2018-08-01
source_type: article
source_domain: www.reddit.com
cleanup_method: llm
---

# We had a security incident. Here's what you need to know.

**TL;DR**: A hacker broke into a few of Reddit’s systems and managed to access some user data, including some current email addresses and a 2007 database backup containing old salted and hashed passwords. Since then we’ve been conducting a painstaking investigation to figure out just what was accessed, and to improve our systems and processes to prevent this from happening again.

**What happened?**

On June 19, we learned that between June 14 and June 18, an attacker compromised a few of our employees’ accounts with our cloud and source code hosting providers. Already having our primary access points for code and infrastructure behind strong authentication requiring two factor authentication (2FA), we learned that SMS-based authentication is not nearly as secure as we would hope, and the main attack was via SMS intercept. We point this out to encourage everyone here to move to token-based 2FA.

Although this was a serious attack, the attacker did not gain write access to Reddit systems; they gained read-only access to some systems that contained backup data, source code and other logs. They were not able to alter Reddit information, and we have taken steps since the event to further lock down and rotate all production secrets and API keys, and to enhance our logging and monitoring systems.

Now that we've concluded our investigation sufficiently to understand the impact, we want to share what we know, how it may impact you, and what we've done to protect us and you from this kind of attack in the future.

**What information was involved?**

Since June 19, we’ve been working with cloud and source code hosting providers to get the best possible understanding of what data the attacker accessed. We want you to know about two key areas of user data that was accessed:

*   **All Reddit data from 2007 and before including account credentials and email addresses**

    *   _What was accessed:_ A complete copy of an old database backup containing very early Reddit user data -- from the site’s launch in 2005 through May 2007. In Reddit’s first years it had many fewer features, so the most significant data contained in this backup are account credentials (username + salted _hashed_ passwords), email addresses, and all content (mostly public, but also private messages) from way back then.

    *   _How to tell if your information was included:_ We are sending a message to affected users and resetting passwords on accounts where the credentials might still be valid. If you signed up for Reddit after 2007, you’re clear here. Check your PMs and/or email inbox: we will be notifying you soon if you’ve been affected.

*   **Email digests sent by Reddit in June 2018**

    *   _What was accessed:_ Logs containing the email digests we sent between June 3 and June 17, 2018. The logs contain the digest emails themselves -- they [look like this](https://i.redd.it/dtdpfncm6dd11.png). The digests connect a username to the associated email address and contain suggested posts from select popular and safe-for-work subreddits you subscribe to.

    *   _How to tell if your information was included:_ If you don’t have an email address associated with your account or your “email digests” user preference was unchecked during that period, you’re not affected. Otherwise, search your email inbox for emails from [noreply@redditmail.com](mailto:noreply@redditmail.com) between June 3-17, 2018.

As the attacker had read access to our storage systems, other data was accessed such as Reddit source code, internal logs, configuration files and other employee workspace files, but these two areas are the most significant categories of user data.

**What is Reddit doing about it?**

Some highlights. We:

*   Reported the issue to law enforcement and are cooperating with their investigation.

*   Are messaging user accounts if there’s a chance the credentials taken reflect the account’s current password.

*   Took measures to guarantee that additional points of privileged access to Reddit’s systems are more secure (e.g., enhanced logging, more encryption and requiring token-based 2FA to gain entry since we suspect weaknesses inherent to SMS-based 2FA to be the root cause of this incident.)

**What can you do?**

First, check whether your data was included in either of the categories called out above by following the instructions there.

If your account credentials were affected and there’s a chance the credentials relate to the password you’re currently using on Reddit, we’ll make you reset your Reddit account password. Whether or not Reddit prompts you to change your password, think about whether you still use the password you used on Reddit 11 years ago on any other sites today.

If your email address was affected, think about whether there’s anything on your Reddit account that you wouldn’t want associated back to that address. You can find instructions on how to remove information from your account on this [help page](https://www.reddithelp.com/en/categories/using-reddit/your-reddit-account/removing-your-reddit-data).

And, as in all things, a strong unique password and [enabling 2FA](https://www.reddithelp.com/en/categories/using-reddit/your-reddit-account/how-set-two-factor-authentication) (which we only provide via an authenticator app, not SMS) is recommended for all users, and be alert for potential phishing or scams.
