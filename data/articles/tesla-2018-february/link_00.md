Title: Hackers Hijacked Tesla's Cloud to Mine Cryptocurrency

URL Source: https://www.wired.com/story/cryptojacking-tesla-amazon-cloud/

Published Time: 2018-02-20T17:06:46.844-05:00

Markdown Content:
# Hackers Hijacked Tesla's Cloud to Mine Cryptocurrency | WIRED

Privacy Center

Currently, only residents from GDPR countries and certain US states can opt out of Tracking Technologies through our Consent Management Platform. Additional options regarding these technologies may be available on your device, browser, or through industry options like AdChoices. Please see our Privacy Policy for more information.

Social Media

- [x] On

These cookies are set by a range of social media services that we have added to the site to enable you to share our content with your friends and networks. They are capable of tracking your browser across other sites and building up a profile of your interests. This may impact the content and messages you see on other websites you visit. If you do not allow these cookies you may not be able to use or see these sharing tools.

* * *

Essential

- [x] On

This website uses essential cookies and services to enable core website features and provide a seamless user experience. These cookies and services are used to facilitate features such as navigation, remember user preferences, and ensure the security of the website.

* * *

Targeted

- [x] On

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

* * *

Performance

- [x] On

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

* * *

Functional

- [x] On

This website uses functional cookies and services to remember your preferences and choices, such as language preferences, font sizes, region selections, and customized layouts. They enable this website to offer enhanced and personalized functionalities.

* * *

Audience Measurement

- [x] On

We use audience measurement cookies in order to carry out aggregated traffic measurement and generate performance statistics essential for the proper functioning of the site and the provision of its content (for example to measure performance, to detect navigation problems, to optimization technical performance or ergonomics, to estimate server power needed and to analyse content performance). The use of these cookies is strictly limited to measuring the site's audience. These cookies do not allow the tracking of navigation on other websites and the data collected is not combined or shared with third parties. You can refuse the use of this cookie by switching off the slider to the right.

OK

English Deutsch Español Français Italiano 日本語 繁體中文

en

[Privacy Policy](https://www.condenast.com/privacy-policy)

[Powered by](https://ethyca.com/?utm_source=fides_consent&utm_medium=referral&utm_campaign=cmp_backlinks&utm_term=home)

[Skip to main content](https://www.wired.com/story/cryptojacking-tesla-amazon-cloud/#main-content)

[](https://www.wired.com/)

[SECURITY](https://www.wired.com/category/security/)

[POLITICS](https://www.wired.com/category/politics/)

[THE BIG STORY](https://www.wired.com/category/big-story/)

[BUSINESS](https://www.wired.com/category/business/)

[SCIENCE](https://www.wired.com/category/science/)

[CULTURE](https://www.wired.com/category/culture/)

[REVIEWS](https://www.wired.com/category/gear/)

[](https://www.wired.com/)

[Newsletters](https://www.wired.com/newsletter?sourceCode=hamburgernav)

[Security](https://www.wired.com/category/security/)

[Politics](https://www.wired.com/category/politics/)

[The Big Story](https://www.wired.com/category/big-story/)

[Business](https://www.wired.com/category/business/)

[Science](https://www.wired.com/category/science/)

[Culture](https://www.wired.com/category/culture/)

[Reviews](https://www.wired.com/category/gear/)

More

[The Big Interview](https://www.wired.com/the-big-interview/)[Magazine](https://www.wired.com/magazine/)[Events](https://www.wired.com/tag/wired-events/)[WIRED Insider](https://www.wired.com/collection/wiredinsider/)[WIRED Consulting](https://www.wired.com/tag/wired-consulting/)

[Newsletters](https://www.wired.com/newsletter?sourceCode=hamburgernav)

[Podcasts](https://www.wired.com/podcasts/)

[Video](https://www.wired.com/video/)

[Livestreams](https://www.wired.com/livestreams)

[Merch](https://shop.wired.com/)

[Search](https://www.wired.com/search/)

[Sign In](https://www.wired.com/auth/initiate?redirectURL=%2Fstory%2Fcryptojacking-tesla-amazon-cloud%2F&source=VERSO_NAVIGATION)

[Sign In](https://www.wired.com/auth/initiate?redirectURL=%2Fstory%2Fcryptojacking-tesla-amazon-cloud%2F&source=VERSO_NAVIGATION)

[Lily Hay Newman](https://www.wired.com/author/lily-hay-newman/)

[Security](https://www.wired.com/category/security)

Feb 20, 2018 5:06 PM

# Hack Brief: Hackers Enlisted Tesla's Public Cloud to Mine Cryptocurrency

The recent rash of cryptojacking attacks has hit a Tesla database that contained potentially sensitive information.

![Image 1: Image may contain Medication and Pill](https://media.wired.com/photos/5a8c7c087b7bd44d86b88075/3:2/w_2560%2Cc_limit/tesla_cryptojacking-01.png)

Tesla joins the ever-growing list of companies targeted by cryptojacking hackers.Hotlittlepotato

Save this story

Save this story

Cryptojacking only really coalesced as a [class of attack](https://www.wired.com/story/cryptojacking-cryptocurrency-mining-browser/) about six months ago, but already the approach has evolved and matured into a ubiquitous threat. Hacks that co-opt computing power for illicit cryptocurrency mining now target a diverse array of victims, from individual consumers to massive institutions—[even industrial control systems](https://www.wired.com/story/cryptojacking-critical-infrastructure/). But the latest victim isn't some faceless internet denizen or a Starbucks in Buenos Aires. It's [Tesla](https://wired.com/tag/tesla).

Researchers at the cloud monitoring and defense firm RedLock [published](https://blog.redlock.io/cryptojacking-tesla) findings on Tuesday that some of Tesla's Amazon Web Services cloud infrastructure was running mining malware in a far-reaching and well-hidden cryptojacking campaign. The researchers disclosed the infection to Tesla last month, and the company quickly moved to decontaminate and lock down its cloud platform within a day. The carmaker's initial investigation indicates that data exposure was minimal, but the incident underscores the ways in which cryptojacking can pose a broad security threat—in addition to racking up a huge electric bill.

The Hack

RedLock discovered the intrusion while scanning the public internet for misconfigured and unsecured cloud servers, a practice that more and more defenders depend on as [exposures from database misconfigurations](https://www.wired.com/story/amazon-s3-data-exposure/) skyrocket.

Trending Now

[](https://www.wired.com/story/cryptojacking-tesla-amazon-cloud/)

"We got alerted that this is an open server and when we investigated it further that’s when we saw that it was actually running a Kubernetes, which was doing cryptomining," says Gaurav Kumar, chief technology officer of RedLock, referring to the popular open-source administrative console for cloud application management. "And then we found that, oh, it actually belongs to Tesla." You know, casual.

The attackers had apparently discovered that this particular Kubernetes console—an administrative portal for cloud application management—wasn't password protected and could therefore be accessed by anyone. From there they would have found, as the RedLock researchers did, that one of the console's "pods," or storage containers, included login credentials for a broader Tesla Amazon Web Services cloud environment. This allowed them to burrow deeper, deploying scripts to establish their cryptojacking operation, which was built on the popular Stratum bitcoin mining protocol.

Who’s Affected?

RedLock says it's difficult to gauge exactly how much mining the attackers accomplished before being discovered. But they note that enterprise networks, and particularly public cloud platforms, are increasingly popular targets for cryptojackers, because they offer a huge amount of processing power in an environment where attackers can mine under the radar since CPU and electricity use is already expected to be relatively high. By riding on a corporate account as large as Tesla's, the attackers could have mined indefinitely without a noticeable impact.

> The Tesla infection shows not only the brazenness of cryptojackers, but also how their attacks have become more subtle and sophisticated.

From a consumer perspective, Tesla's compromised cloud platform also contained an S3 bucket that seemed to house sensitive proprietary data, like vehicle and mapping information and other instrument telemetry. The researchers say that they didn't investigate what information could have been exposed to the attackers, as part of their commitment to ethical hacking.

A Tesla spokesperson said in a statement that the risk was minimal: “We addressed this vulnerability within hours of learning about it. The impact seems to be limited to internally-used engineering test cars only, and our initial investigation found no indication that customer privacy or vehicle safety or security was compromised in any way.”

Still, data about test cars alone could be extremely valuable coming from a company like Tesla, which works on next-generation products like driverless automation.

The RedLock researchers submitted their findings through Tesla's bug bounty program. Elon Musk's company awarded them more than $3,000 for the discovery, which RedLock donated to charity.

How Serious Is This?

This incident itself is just one example in an ever-growing list of high-profile cryptojacking compromises. Just last week, researchers from the security firm Check Point said that attackers made more than $3 million by mining Monero on the [servers of the popular web development application](https://www.bleepingcomputer.com/news/security/hacker-group-makes-3-million-by-installing-monero-miners-on-jenkins-servers/) Jenkins. The Tesla infection is particularly noteworthy, though, because it shows not only the brazenness of cryptojackers, but also how their attacks have become more subtle and sophisticated.

RedLock's Kumar notes that the Tesla attackers were running their own mining server, making it less likely that it would land on malware-scanner black lists. The mining malware also communicated with the attacker's server on an unusual IP port, making it less likely that a port scanner would detect it as malicious. And the obfuscation techniques didn't stop there. The attack communications all happened over SSL web encryption to hide their content from security-monitoring tools, and the mining server also used a proxy server as an intermediary to mask it and make it less traceable.

Most Popular

*   [![Image 2: Meta Is Warned That Facial Recognition Glasses Will Arm Sexual Predators](https://media.wired.com/photos/69dd120fd5415cb89341a838/1:1/w_120%2Ch_120%2Cc_limit/undefined)](https://www.wired.com/story/meta-ray-ban-oakley-smart-glasses-no-face-recognition-civil-society/#intcid=_wired-right-rail_ea2284f3-29ad-43a3-af8e-d223f2481eaf_popular4-2) Artificial Intelligence   [Meta Is Warned That Facial Recognition Glasses Will Arm Sexual Predators](https://www.wired.com/story/meta-ray-ban-oakley-smart-glasses-no-face-recognition-civil-society/#intcid=_wired-right-rail_ea2284f3-29ad-43a3-af8e-d223f2481eaf_popular4-2)By Dell Cameron      
*   [![Image 3: The Internet's Most Powerful Archiving Tool Is in Peril](https://media.wired.com/photos/69d9793c27ad448072aa787f/1:1/w_120%2Ch_120%2Cc_limit/undefined)](https://www.wired.com/story/the-internets-most-powerful-archiving-tool-is-in-mortal-peril/#intcid=_wired-right-rail_ea2284f3-29ad-43a3-af8e-d223f2481eaf_popular4-2) Artificial Intelligence   [The Internet's Most Powerful Archiving Tool Is in Peril](https://www.wired.com/story/the-internets-most-powerful-archiving-tool-is-in-mortal-peril/#intcid=_wired-right-rail_ea2284f3-29ad-43a3-af8e-d223f2481eaf_popular4-2)By Kate Knibbs      
*   [![Image 4: Staunch Trump Supporters Are Now Asking if He’s the Antichrist](https://media.wired.com/photos/69d83e91a6b1cf7dff37c069/1:1/w_120%2Ch_120%2Cc_limit/undefined)](https://www.wired.com/story/staunch-trump-supporters-are-now-asking-if-hes-the-antichrist/#intcid=_wired-right-rail_ea2284f3-29ad-43a3-af8e-d223f2481eaf_popular4-2) Politics   [Staunch Trump Supporters Are Now Asking if He’s the Antichrist](https://www.wired.com/story/staunch-trump-supporters-are-now-asking-if-hes-the-antichrist/#intcid=_wired-right-rail_ea2284f3-29ad-43a3-af8e-d223f2481eaf_popular4-2)By Makena Kelly      
*   [![Image 5: A Lot of Shops Won't Fix Electric Bikes. Here's Why](https://media.wired.com/photos/69d931c00318a0f74a550c2d/1:1/w_120%2Ch_120%2Cc_limit/undefined)](https://www.wired.com/story/why-is-it-so-hard-to-fix-an-electric-bike/#intcid=_wired-right-rail_ea2284f3-29ad-43a3-af8e-d223f2481eaf_popular4-2) Gear   [A Lot of Shops Won't Fix Electric Bikes. Here's Why](https://www.wired.com/story/why-is-it-so-hard-to-fix-an-electric-bike/#intcid=_wired-right-rail_ea2284f3-29ad-43a3-af8e-d223f2481eaf_popular4-2)By Stephanie Pearson      
*         

RedLock says the attackers obtained free proxying services and the SSL certificate from the internet infrastructure firm Cloudflare, which offers these free services to make web security and privacy tools accessible to anyone, but grapples with the ways they can be abused by bad actors.

The good news about attackers investing time and energy to conceal their operations is that it means that first-line defensive efforts are working. But it also means that the payoff for executing the hacks makes it worth deploying those advanced maneuvers. Within months, cryptojacking has decidedly reached this phase. "The big thing to note here is the fact that public cloud is quickly becoming a target, specifically because it’s an easy target," says RedLock vice president Upa Campbell. "The benefit of the cloud is agility, but the downside is that the chance of user error is higher. Organizations are really struggling."

Jumping Cryptojacks

*   We've [come a long way since the early days of cryptojacking](https://www.wired.com/story/cryptojacking-cryptocurrency-mining-browser/), way back in the heady days of 2017
*   As bad as the Tesla incident was, [cryptojacking attacks on critical infrastructure are an even bigger cause for alarm](https://www.wired.com/story/cryptojacking-critical-infrastructure)
*   Tesla probably already had enough of a headache [trying to ramp up its Model 3 production](https://www.wired.com/story/tesla-model-3-production-problems-elon-musk-feb-2018/)

[![Image 6](https://media.wired.com/photos/65e835799fa4c1a0001881a9/1:1/w_90%2Cc_limit/Lily%2520Newman.jpg)](https://www.wired.com/author/lily-hay-newman/)

[Lily Hay Newman](https://www.wired.com/author/lily-hay-newman/) is a senior writer at WIRED focused on information security, digital privacy, and hacking. She previously worked as a technology reporter at Slate, and was the staff writer for Future Tense, a publication and partnership between Slate, the New America Foundation, and Arizona State University. Her work ... [Read More](https://www.wired.com/author/lily-hay-newman)

Senior Writer

*   [](https://www.twitter.com/lilyhnewman)

Topics[Tesla](https://www.wired.com/tag/tesla/)[cryptocurrency](https://www.wired.com/tag/cryptocurrency/)[hacking](https://www.wired.com/tag/hacking/)[cloud](https://www.wired.com/tag/cloud/)[databases](https://www.wired.com/tag/databases/)

Read More

[![Image 7: Google Now Lets You Change Your Gmail Address. Here’s How](https://media.wired.com/photos/69bc909af05d6225e8611af5/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/how-to-change-your-gmail-address/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[Google Now Lets You Change Your Gmail Address. Here’s How](https://www.wired.com/story/how-to-change-your-gmail-address/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

You’ve probably had the same Gmail address for years. Now, it’s easy to make a name change without worrying about the transition.

Reece Rogers

[![Image 8: Tech Companies Are Trying to Neuter Colorado’s Landmark Right-to-Repair Law](https://media.wired.com/photos/69b86b74be9e27104c501c7c/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/tech-companies-are-trying-to-neuter-colorados-landmark-right-to-repair-law/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[Tech Companies Are Trying to Neuter Colorado’s Landmark Right-to-Repair Law](https://www.wired.com/story/tech-companies-are-trying-to-neuter-colorados-landmark-right-to-repair-law/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

A bill in Colorado is a glimpse into the future of how corporations are working to limit the freedom people have to make their own fixes and upgrades.

Boone Ashworth

[![Image 9: I Tested the MacBook Neo and the MacBook Air. Here's Which One You Should Buy](https://media.wired.com/photos/69c6b14c2e33b7e4cae4cc2b/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/macbook-neo-vs-macbook-air/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[I Tested the MacBook Neo and the MacBook Air. Here's Which One You Should Buy](https://www.wired.com/story/macbook-neo-vs-macbook-air/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

After conducting long-term testing on both the MacBook Neo and MacBook Air, I have a good idea who should buy which laptop.

Luke Larsen

[![Image 10: How to Back Up Your Life With Hard Drives, Cloud-Based Services, and More](https://media.wired.com/photos/69d03b9326dd2d3a7ba902f2/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/how-to-back-up-your-digital-life/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[How to Back Up Your Life With Hard Drives, Cloud-Based Services, and More](https://www.wired.com/story/how-to-back-up-your-digital-life/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

Backups are boring, but they’ll save your bacon. Here’s how to make sure your data lives on, even when your PC doesn’t.

Scott Gilbertson

[![Image 11: CBP Facility Codes Sure Seem to Have Leaked Via Online Flashcards](https://media.wired.com/photos/69cd6ca0af7e6758a42bc66b/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/cbp-facility-codes-sure-seem-to-have-leaked-via-online-flashcards/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[CBP Facility Codes Sure Seem to Have Leaked Via Online Flashcards](https://www.wired.com/story/cbp-facility-codes-sure-seem-to-have-leaked-via-online-flashcards/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

The Quizlet flashcards, which WIRED found through basic Google searches, seem to include sensitive information about gate security at Customs and Border Protection locations.

Sammy Sussman

[![Image 12: Who Needs Tow Trucks? Portable Jump Starters Will Get You Home Without One](https://media.wired.com/photos/69c6c4fb24f02ff7dc20961d/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/best-portable-jump-starters/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[Who Needs Tow Trucks? Portable Jump Starters Will Get You Home Without One](https://www.wired.com/story/best-portable-jump-starters/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

The new crop of portable jump starters means you'll never be stuck waiting on a tow. Here are the devices we'd trust.

Matthew Korfhage

[![Image 13: You Can Soon Buy a $4,370 Humanoid Robot on AliExpress](https://media.wired.com/photos/69d81392ce1f65d162ddb2f0/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/unitree-r1-humanoid-robot-for-sale-on-aliexpress/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[You Can Soon Buy a $4,370 Humanoid Robot on AliExpress](https://www.wired.com/story/unitree-r1-humanoid-robot-for-sale-on-aliexpress/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

Unitree is bringing its R1 to international markets. It arrives with some aerobatic capabilities and an entry-level price, but the question of what you'd actually do with it remains open.

Marco Trabucchi

[![Image 14: Politicians Are Spending More Money on Security as They Increasingly Become Targets](https://media.wired.com/photos/69d55a00ee39d7f1d370552d/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/political-campaign-security-spending/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[Politicians Are Spending More Money on Security as They Increasingly Become Targets](https://www.wired.com/story/political-campaign-security-spending/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

Political candidates are purchasing more home alarms, bulletproof vests, and other protections amid rising fears of political violence.

Maddy Varner

[![Image 15: Your Vape Wants to Know How Old You Are](https://media.wired.com/photos/69c5e00d3d62f10d14ab0ce6/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/your-vape-wants-to-know-how-old-you-are/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[Your Vape Wants to Know How Old You Are](https://www.wired.com/story/your-vape-wants-to-know-how-old-you-are/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

Companies hope that biometric age-verification tech in cartridges could put flavored vapes back in business. But it's unlikely to solve the real problems.

Boone Ashworth

[![Image 16: The Dumbest Hack of the Year Exposed a Very Real Problem](https://media.wired.com/photos/69d4e951d8b67218cd4b81ad/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/crosswalk-city-hack-cybersecurity-lessons/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[The Dumbest Hack of the Year Exposed a Very Real Problem](https://www.wired.com/story/crosswalk-city-hack-cybersecurity-lessons/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

Last April, a hacker hijacked crosswalk announcements to mimic Mark Zuckerberg and Elon Musk. Records obtained by WIRED reveal how unprepared local authorities were.

Paresh Dave

[![Image 17: This App Makes Even the Sketchiest PDF or Word Doc Safe to Open](https://media.wired.com/photos/69c4791716bb3ee95a674db0/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/dangerzone-app-for-safe-pdfs-word-docs/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[This App Makes Even the Sketchiest PDF or Word Doc Safe to Open](https://www.wired.com/story/dangerzone-app-for-safe-pdfs-word-docs/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

When somebody sends you a document as an attachment, don't just open it. Use the free tool Dangerzone to scrub it clean of any malevolent code. Here's how it works.

Justin Pot

[![Image 18: Anthropic’s Mythos Will Force a Cybersecurity Reckoning—Just Not the One You Think](https://media.wired.com/photos/69b889e1574a3bb21dfe778a/16:9/w_640%2Cc_limit/undefined)](https://www.wired.com/story/anthropics-mythos-will-force-a-cybersecurity-reckoning-just-not-the-one-you-think/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

[Anthropic’s Mythos Will Force a Cybersecurity Reckoning—Just Not the One You Think](https://www.wired.com/story/anthropics-mythos-will-force-a-cybersecurity-reckoning-just-not-the-one-you-think/#intcid=_wired-article-bottom-recirc-bkt-a_f49925c9-5856-417f-8f26-47e8a66997de_closr)

The new AI model is being heralded—and feared—as a hacker’s superweapon. Experts say its arrival is a wake-up call for developers who have long made security an afterthought.

Lily Hay Newman

[![Image 19: WIRED](https://www.wired.com/verso/static/wired-us/assets/logo-reverse.svg)](https://www.wired.com/)

WIRED is obsessed with what comes next. Through rigorous investigations and game-changing reporting, we tell stories that don’t just reflect the moment—they help create it. When you look back in 10, 20, even 50 years, WIRED will be the publication that led the story of the present, mapped the people, products, and ideas defining it, and explained how those forces forged the future. WIRED: For Future Reference.

More From WIRED

*   [Subscribe](https://www.wired.com/subscribe/)
*   [Newsletters](https://www.wired.com/newsletter?sourceCode=HeaderAndFooter)
*   [Livestreams](https://www.wired.com/livestreams)
*   [Travel](https://www.wired.com/tag/travel/)
*   [FAQ](https://www.wired.com/about/faq/)
*   [WIRED Staff](https://www.wired.com/about/wired-staff/)
*   [WIRED Education](https://www.wirededucation.com/)
*   [Editorial Standards](https://www.wired.com/about/wired-on-background-policy/)
*   [Archive](https://archive.wired.com/t/storefront/storefront)
*   [RSS](https://www.wired.com/about/rss-feeds/)
*   [Site Map](https://www.wired.com/sitemap/)
*   [Accessibility Help](https://www.wired.com/about/accessibility-help/)

Reviews and Guides

*   [Reviews](https://www.wired.com/category/gear/)
*   [Buying Guides](https://www.wired.com/category/gear/buying-guides/)
*   [Streaming Guides](https://www.wired.com/tag/culture-guides/)
*   [Wearables](https://www.wired.com/tag/wearables/)
*   [Coupons](https://www.wired.com/tag/coupons/)
*   [Gift Guides](https://www.wired.com/tag/gift-guides/)

*   [Advertise](https://www.condenast.com/brands/wired)
*   [Contact Us](https://www.wired.com/about/feedback/)
*   [Manage Account](https://www.wired.com/account/profile)
*   [Jobs](https://www.wired.com/about/wired-jobs/)
*   [Press Center](https://www.wired.com/about/press/)
*   [Condé Nast Store](https://condenaststore.com/)
*   [User Agreement](https://www.condenast.com/user-agreement/)
*   [Privacy Policy](http://www.condenast.com/privacy-policy#privacypolicy)
*   [Your California Privacy Rights](http://www.condenast.com/privacy-policy#privacypolicy-california)

© 2026 Condé Nast. All rights reserved. _WIRED_ may earn a portion of sales from products that are purchased through our site as part of our Affiliate Partnerships with retailers. The material on this site may not be reproduced, distributed, transmitted, cached or otherwise used, except with the prior written permission of Condé Nast.[Ad Choices](http://www.aboutads.info/)

###### Select international site

United States
*   [Italia](https://www.wired.it/)
*   [Japón](https://wired.jp/)
*   [Czech Republic & Slovakia](https://www.wired.cz/)

*   [](https://www.facebook.com/wired/)
*   [](https://twitter.com/wired/)
*   [](https://pinterest.com/wired/)
*   [](https://www.youtube.com/user/wired/)
*   [](https://instagram.com/wired/)
*   [](https://www.tiktok.com/@wired?lang=en)

Privacy Information

![Image 22](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=0e577465-6bac-4249-951b-38c473c8b951&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=378e8738-216b-4553-9e39-081b32670e46&pt=Hackers%20Hijacked%20Tesla%27s%20Cloud%20to%20Mine%20Cryptocurrency%20%7C%20WIRED&tw_document_href=https%3A%2F%2Fwww.wired.com%2Fstory%2Fcryptojacking-tesla-amazon-cloud%2F&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1776235657493.816031158388352197&txn_id=ogyql&type=javascript&version=2.3.52)![Image 23](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=0e577465-6bac-4249-951b-38c473c8b951&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=378e8738-216b-4553-9e39-081b32670e46&pt=Hackers%20Hijacked%20Tesla%27s%20Cloud%20to%20Mine%20Cryptocurrency%20%7C%20WIRED&tw_document_href=https%3A%2F%2Fwww.wired.com%2Fstory%2Fcryptojacking-tesla-amazon-cloud%2F&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1776235657493.816031158388352197&txn_id=ogyql&type=javascript&version=2.3.52)

![Image 24](https://bat.bing.com/action/0?ti=4015762&tm=gtm002&Ver=2&mid=982af004-55a6-4214-804e-a6d359646e85&bo=1&sid=fe385170389611f19b84c1fe351a8024&vid=fe386590389611f1a0ecdb39a15f85bf&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=800&sh=600&sc=24&tl=Hackers%20Hijacked%20Tesla%27s%20Cloud%20to%20Mine%20Cryptocurrency%20%7C%20WIRED&kw=tesla,cryptocurrency,hacking,cloud,databases&p=https%3A%2F%2Fwww.wired.com%2Fstory%2Fcryptojacking-tesla-amazon-cloud%2F&r=&lt=1810&evt=pageLoad&sv=2&cdb=AQAS&rn=923372)

![Image 25: dot image pixel](https://sp.analytics.yahoo.com/sp.pl?a=10000&d=Wed%2C%2015%20Apr%202026%2006%3A47%3A37%20GMT&n=0&b=Hackers%20Hijacked%20Tesla%27s%20Cloud%20to%20Mine%20Cryptocurrency%20%7C%20WIRED&.yp=10200402&f=https%3A%2F%2Fwww.wired.com%2Fstory%2Fcryptojacking-tesla-amazon-cloud%2F&enc=UTF-8&yv=1.16.6&ec=PageView&et=PageView&tagmgr=gtm)