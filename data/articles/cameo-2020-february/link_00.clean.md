---
title: Celeb Shout-Out App Cameo Exposes Private Videos and User Data
url: "https://www.vice.com/en/article/akwj5z/cameo-app-exposed-private-videos-user-data-passwords"
author: Joseph Cox
published: 2020-02-20
source_type: article
source_domain: www.vice.com
cleanup_method: llm
---

# Celeb Shout-Out App Cameo Exposes Private Videos and User Data
# Celeb Shout-Out App Cameo Exposes Private Videos and User Data

By [Joseph Cox](https://www.vice.com/en/contributor/joseph-cox/ "Posts by Joseph Cox")

February 20, 2020, 3:23pm

Cameo, the increasingly popular app for paying celebrities to record short personal videos, exposed a wealth of user data including email addresses, hashed and salted passwords and phone numbers, and messages via a misconfiguration in its app. The site also has an issue where videos that are supposed to be private are actually available for anyone to find and download. Using the design flaw, Motherboard wrote basic code to build lists of ostensibly private videos filmed for users by celebrities such as Snoop Dogg, Ice T, and Michael Rapaport.

“I got some of the backed up user database,” the researcher who flagged multiple security and privacy issues with the app said. Motherboard granted the researcher anonymity to speak more candidly about a sensitive security incident.

Cameo launched in 2017 and in 2019 [raised $50 million in funding](https://variety.com/2019/digital/news/celebrity-50-million-series-b-1203252093/). Customers can pay as little as $50 for a shout-out, up to thousands of dollars. Last June the company recorded 300,000 transactions, an average of 2,000 a day, [TechCrunch reported](https://techcrunch.com/2019/06/25/cameo/).

A celebrity’s Cameo page includes reviews from previous customers. “Hilarious! Perfect video. Michael, you are the man!” one review left for Rapaport reads. The review adds that the clip was a “Private Cameo Video,” and does not provide a link to view the video itself.

**Do you work at Cameo? We’d love to hear from you. Using a non-work phone or computer, you can contact Joseph Cox securely on Signal on +44 20 8133 5190, Wickr on josephcox, OTR chat on jfcox@jabber.ccc.de, or email joseph.cox@vice.com.**

But due to a design flaw in the review system, it is possible to retrieve information to reconstruct the URL that goes to the video page itself, meaning the clips can be viewed even if the customer set them to private.

To test the issue, Motherboard wrote scripts to compile lists of videos that Cameo users had provided reviews for, including those that users had set as “private.” All of the videos were accessible.

Cameo may have designed its website and app to be as frictionless as possible; having links that don’t require a user to login to view them lets people share them easily with friends. For example, anyone with a link to a pending Cameo request can edit what the celebrity is asked to say or cancel the request, even if they didn’t originally commission it or pay for it.


To further verify that anyone with the link can view a video, Motherboard editor-in-chief Jason Koebler commissioned a Cameo video from comedian Gilbert Gottfried. In the video, which Motherboard explicitly set to “Don’t make this video public on Cameo,” Gottfried says “cybersecurity is becoming more and more relevant today, what with the apps, and viruses and hackers.” Motherboard senior staff writer Joseph Cox was then able to view the video publicly and download it.

Other aspects of Cameo show that the service is using off-the-shelf infrastructure to run its site. For example, the Cameo privacy policy is not hosted on the company’s own website, but is a Google Document. According to a video that the researcher provided which appears to show how Cameo trains celebrities to use the service, celebrities are told to send their completed Cameos to a bot on the messaging app Telegram.

One of the other issues the researcher found was that the Cameo app included credentials that they said allowed anyone to log into Cameo’s backend infrastructure. Specifically, the credentials granted access to Amazon S3 buckets used to store data, the researcher said.

The researcher said they used the credentials to access the servers “to verify what was accessible.” Motherboard decompiled both the latest version of the Android Cameo app as well as another from June 2018. The key was present in both, indicating that the credentials for Cameo’s servers could have been exposed for around two years, but it not clear if the keys allowed read and write access for that entire period. For legal reasons Motherboard did not access Cameo’s buckets themselves.

“I got some of the backed up user database.”

The researcher provided Motherboard with a sample of the data stored in Cameo’s backend, including user email addresses and messages. To verify some of the data Motherboard tried to create new accounts on Cameo with a random selection of the user email addresses in the file. This was not possible because the addresses were already linked to active accounts, indicating that the data does relate to genuine Cameo users.

One part of the data provided by the researcher appeared to include Ice-T’s personal email address. Ice-T did not respond to a request for comment.

“Cameo recently learned of a vulnerability in one of our databases from a third party security data researcher potentially affecting a limited amount of account holder data. Our team promptly fixed the issue. After thoroughly investigating the matter, we are currently not aware of any evidence indicating that anyone else other than the security researcher knew of or utilized the vulnerability. The trust of our community and data security are top priorities for Cameo. We are continuing to actively investigate the issue and continuously investing in data security,” Cameo said in a statement.

“As our investigation continues and as additional relevant information becomes available, we will update affected account holders. As always, Cameo will continue to review its security measures on an ongoing basis and take appropriate actions to keep our community safe,” the statement added.

Cameo confirmed the data included hashed and salted passwords and phone numbers, as well as email addresses and a number of non-public Cameo videos, perhaps referring to the internal clips the researcher provided to Motherboard.

On videos that users have set as private being discoverable, Cameo added, “A Cameo being classified as ‘private’ pertains to a specific Cameo not being posted on the Cameo platform (meaning the talent’s profiles or other pages). Cameo was designed for people to gift and share personalized videos from their favorite talent between friends and family. Both public and private Cameos are intended to be shared socially.”

The researcher said they contacted Cameo about the S3 issue last Friday, and received a response on Tuesday. Cameo said it has resolved the problem, and is in the process of notifying impacted users.

_Update: This piece has been updated to include more comment from Cameo._

**_Subscribe to our cybersecurity podcast, [CYBER](https://itunes.apple.com/gb/podcast/cyber/id1441708044?mt=2)._**
