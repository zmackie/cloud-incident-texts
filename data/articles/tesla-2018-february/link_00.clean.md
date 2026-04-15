---
title: "Hack Brief: Hackers Enlisted Tesla's Public Cloud to Mine Cryptocurrency"
url: "https://www.wired.com/story/cryptojacking-tesla-amazon-cloud/"
author: Lily Hay Newman
published: 2018-02-20
source_type: article
source_domain: www.wired.com
cleanup_method: llm
---

[Lily Hay Newman](https://www.wired.com/author/lily-hay-newman/)

[Security](https://www.wired.com/category/security)

Feb 20, 2018 5:06 PM

# Hack Brief: Hackers Enlisted Tesla's Public Cloud to Mine Cryptocurrency

The recent rash of cryptojacking attacks has hit a Tesla database that contained potentially sensitive information.

Cryptojacking only really coalesced as a [class of attack](https://www.wired.com/story/cryptojacking-cryptocurrency-mining-browser/) about six months ago, but already the approach has evolved and matured into a ubiquitous threat. Hacks that co-opt computing power for illicit cryptocurrency mining now target a diverse array of victims, from individual consumers to massive institutions—[even industrial control systems](https://www.wired.com/story/cryptojacking-critical-infrastructure/). But the latest victim isn't some faceless internet denizen or a Starbucks in Buenos Aires. It's [Tesla](https://wired.com/tag/tesla).

Researchers at the cloud monitoring and defense firm RedLock [published](https://blog.redlock.io/cryptojacking-tesla) findings on Tuesday that some of Tesla's Amazon Web Services cloud infrastructure was running mining malware in a far-reaching and well-hidden cryptojacking campaign. The researchers disclosed the infection to Tesla last month, and the company quickly moved to decontaminate and lock down its cloud platform within a day. The carmaker's initial investigation indicates that data exposure was minimal, but the incident underscores the ways in which cryptojacking can pose a broad security threat—in addition to racking up a huge electric bill.

The Hack

RedLock discovered the intrusion while scanning the public internet for misconfigured and unsecured cloud servers, a practice that more and more defenders depend on as [exposures from database misconfigurations](https://www.wired.com/story/amazon-s3-data-exposure/) skyrocket.
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

RedLock says the attackers obtained free proxying services and the SSL certificate from the internet infrastructure firm Cloudflare, which offers these free services to make web security and privacy tools accessible to anyone, but grapples with the ways they can be abused by bad actors.

The good news about attackers investing time and energy to conceal their operations is that it means that first-line defensive efforts are working. But it also means that the payoff for executing the hacks makes it worth deploying those advanced maneuvers. Within months, cryptojacking has decidedly reached this phase. "The big thing to note here is the fact that public cloud is quickly becoming a target, specifically because it’s an easy target," says RedLock vice president Upa Campbell. "The benefit of the cloud is agility, but the downside is that the chance of user error is higher. Organizations are really struggling."

Jumping Cryptojacks

*   We've [come a long way since the early days of cryptojacking](https://www.wired.com/story/cryptojacking-cryptocurrency-mining-browser/), way back in the heady days of 2017
*   As bad as the Tesla incident was, [cryptojacking attacks on critical infrastructure are an even bigger cause for alarm](https://www.wired.com/story/cryptojacking-critical-infrastructure)
*   Tesla probably already had enough of a headache [trying to ramp up its Model 3 production](https://www.wired.com/story/tesla-model-3-production-problems-elon-musk-feb-2018/)
