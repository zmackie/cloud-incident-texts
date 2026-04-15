---
title: Hackers have turned PolitiFact's website into a trap for your PC
url: "https://web.archive.org/web/20200806102838/https://www.washingtonpost.com/news/the-switch/wp/2017/10/13/hackers-have-turned-politifacts-website-into-a-trap-for-your-pc/"
author: Brian Fung
published: 2017-10-13
source_type: archive
source_domain: web.archive.org
cleanup_method: llm
---

PolitiFact has been an invaluable resource for debunking politicians' misstatements and falsehoods. But now, it seems, some unknown actor is trying to profit off the website's popularity — by hooking visitors' computers into a virtual currency mining operation.
The hack was discovered Friday by security researcher Troy Mursch, who noticed that visiting Politifact.com caused his computer's CPU to run at its maximum capacity.
The anomaly left telltale signs of Coin Hive — a piece of code that can be installed on websites that, when active, diverts unused computational power on visitors' computers toward generating a Bitcoin-like currency called Monero. Under ordinary circumstances, said Mursch, Coin Hive is used by some websites as an alternative to advertising. But in the case of PolitiFact, somebody has programmed the site to run multiple versions of Coin Hive simultaneously, basically bringing any visitor's computer to a processing halt.
The phenomenon was soon confirmed by security journalist Brian Krebs.
The issue may be related to a third-party ad provider, said Aaron Sharockman, executive director of PolitiFact, which is owned by the Tampa Bay Times.
“It's frustrating,” he said. “I'm escalating now with our ad and IT folks and I'll get back to you.”
Virtual currencies such as Monero run on digital “coins” that get created when one or more computers that are controlled by a person successfully solve a math problem. Throwing more computational power at the problem means solving it faster — and the more efficiently you can be awarded a new coin.
Forcing PolitiFact visitors to participate in this operation at such a scale — in many cases without their knowledge or consent — makes this use of Coin Hive malicious, said Mursch. In some cases, turning off JavaScript or using an ad-blocker could help thwart the code, but not always, given how quickly variants of the software can be created.
This isn't the first time we've seen Coin Hive being deployed on major websites. The premium cable channel Showtime was recently discovered to have been running the script, though it has since been deleted from the site. The peer-to-peer filesharing site the Pirate Bay has also experimented with it.
To track the status of PolitiFact's Coin Hive problem, Mursch set up a tool to monitor whether the code was still present. By about 4 p.m. Eastern on Friday, it appeared as though PolitiFact had scrubbed the offending software from its site. “The source of the problem was identified and removed We are reviewing how malicious code got on the site and taking necessary steps to secure the site from bad actors,” a statement from PolitiFact said.
