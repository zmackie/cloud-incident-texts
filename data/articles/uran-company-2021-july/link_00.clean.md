---
title: Clear and Uncommon Story About Overcoming Issues with AWS
url: "https://web.archive.org/web/20221205145546/https://topdigital.agency/clear-and-uncommon-story-about-overcoming-issues-with-aws/"
source_type: archive
source_domain: web.archive.org
cleanup_method: llm
---

This article is created to show how the Uran Company overcame the hacking of the AWS account through SES using a compromised API key with maximum privileges.
“In the long run, we shape our lives, and we shape ourselves. The process never ends until we die. And the choices we make are ultimately our own responsibility.” ― Eleanor Roosevelt.
A person will never stop learning from their own mistakes, and we’d like to share our story with you, showing the choices we made at Uran Company and how they helped us learn.
We are a loyal Amazon Web Services customer with a massive history behind our backs. As well, not so long ago, we launched our own startup and became a part of the AWS credit program, which gave us a certain amount of credits. We consider ourselves advanced AWS users, we use most of the services they provide, like RDS, EC2, S3, SQS, IAM, EFS, VPC, API Gateway, WAF, SES and many others, comply with all security measures, use two-factor authentication and keys with limited privileges.
Seems like the stories about hacking should not happen to us…
Nevertheless, life can happen. One day, we receive a notification that the account has been blocked due to the launch of several dozen instances of the maximum configuration on it.
An experienced AWS user at this stage may notice that a lot of similar articles have been going through thematic resources for many years, and we are not telling anything new, but this is not entirely true, our case turned out to be non-standard.
Honestly, everything was standard regarding the hacking process: trying to be helpful, led us to this situation. So, we let our friend use our AWS SES service for his old (outdated) Drupal site hosted on another resource, which didn’t have an opportunity to update and afterward got hacked through SES using a compromised API key with maximum privileges.
Somewhere there in the depths of hacked Drupal, there was an API key. After finding this key, the attackers’ script launched the creation of EC2 instances of the top configuration and the cryptocurrency mining began.
It is all understandable and as mentioned above was described not even once, but the weird thing happened afterward. Amazon blocked the account and sent a message to the billing console to repay the charged thousands of dollars, but there are solid zeros, apparently, the credits we mentioned above paid off the debt, but the system was not ready for such a case.
Regardless of the fact that the AWS business support is supposed to be 24/7, it was not that supportive and fast. They were silent for a WEEK! We constantly wrote, ordered callbacks, etc., but in return, we received complete ignore and silence which was extremely frustrating.
We searched for the communities and people who had the same kind of situation on Facebook & LinkedIn. Finally, we found two AWS representatives in our region, and they agreed to help.
Thanks to Them for That!
After their help, the support started responding, our console got unblocked, and we were given the opportunity to remove unnecessary EC2s, after which the account was unfrozen.
Generally speaking, all this situation, except for hypothetical invoices, which were covered by loans and which Amazon, we hope, will return to us, did not turn out to be a big problem. We had alternative AWS accounts, where the necessary services were deployed, the transition to them was done quickly and painlessly.
But take a minute and try to imagine, you are a startup company in the same kind of situation, you got 168 hours of downtime – 1 week of absolute suspense, all your data is there and all your work as well, how can this affect your company? Will you lose some of your clients or not? And will you be able to continue working once the issue is fixed? No one can predict.
The best way to stay away from this kind of issue is simply always following the safety requirements and keeping a copy of your data on different clouds and accounts, because you never know what can happen next. However, it doesn’t always depend on you as we can see from the story, so don’t trust companies when they say we have 24/7 support, situations are different and no one is safe.
This issue, mistake or however we can call it, made us learn a few but very valuable lessons and the most important one is to always be on top of everything, because even a small change or mistake can influence your company tremendously.
