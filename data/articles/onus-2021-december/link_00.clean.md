---
title: The attack on ONUS – A real-life case of the Log4Shell vulnerability
url: "https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability"
author: Trung Nguyen
published: 2021-12-28
source_type: article
source_domain: cystack.net
cleanup_method: llm
---

# The attack on ONUS – A real-life case of the Log4Shell vulnerability


# The attack on ONUS – A real-life case of the Log4Shell vulnerability


Trung Nguyen


[Đọc bản tiếng Việt tại đây](https://cystack.net/research/cuoc-tan-cong-vao-onus-goc-nhin-ky-thuat-tu-lo-hong-log4shell)

[Log4Shell](https://en.wikipedia.org/wiki/Log4Shell)has recently been a nightmare (probably the worst one for now) to businesses. ONUS, a client of ours, was an unfortunate victim. As their security partner, CyStack informed ONUS of the risks right after Log4Shell came to light; when the attack actually happened, we supported them in finding the root cause and coming up with quick yet comprehensive responses. In this post, we will provide the timeline and analysis of this incident.

## TLDR; (Too long; didn’t read)

[ONUS](https://goonus.io/), one of the biggest cryptocurrency platforms in Vietnam, was hacked several days ago. The cybersecurity incident at ONUS started with a Log4Shell vulnerability in their payment software provided by [Cyclos](https://www.cyclos.org/) but later escalated due to misconfigurations and mistakes in granting permissions at AWS S3. Attackers took advantage of the vulnerability in the Cyclos software to attack even before the vendor could inform and provide patch instructions for its clients. ONUS patched the vulnerability as soon as Cyclos warned, but it was too late. As a result, 2 million ONUS users’ information including EKYC data, personal information, and password hash was leaked.

## Timeline

**09/12/2021**, the Log4Shell vulnerability was published. Being aware of the seriousness of this vulnerability, we immediately informed our partners and clients of the risks associated. At that time, ONUS was carefully monitoring their system security but they did not know that Cyclos was among the software affected by the Log4Shell vulnerability.

**11-13/12/2021,** the attackers exploited the Log4Shell vulnerability on a Cyclos server of ONUS and left backdoors behind. We will analyze how we knew that in the next sections.

**14/12/2021**, Cyclos notified ONUS of the vulnerability and issued [instructions to patch the vulnerability](https://forum.cyclos.org/viewtopic.php?p=12374&sid=c8f5ff3a23e64a7bd6d042cb76ed387f#%20p12374). ONUS immediately patched the vulnerability according to those instructions.

**23/12/2021,**while monitoring the system, CyStack detected some abnormal activities and informed ONUS. When ONUS confirmed that the user data in the AWS S3 had been deleted, we immediately planned and executed incident responses. Because the target was AWS S3, we tracked all access keys related to compromised buckets and found that several services were affected including those of Cyclos. The keys were deactivated shortly after.

**24/12/2021**, the attackers sent a ransom request of $5M USD to ONUS via Telegram. ONUS rejected the request and [disclosed this attack to their users](https://www.facebook.com/groups/goonus.io/permalink/502395264509595). CyStack confirmed that the Log4Shell vulnerability of Cyclos was the root cause and we started checking all Cyclos nodes to find and remove backdoors.

**25/12/2021**, the attackers posted about the leak to [a hacking forum](https://raidforums.com/Thread-SELLING-Vietnamese-ONUS-formerly-VNDC-full-database-eKYC-images-videos-and-mores)

**28/12/2021,**a researcher nicknamed **Wjbuboyz**informed ONUS of another issue in configuring S3 that might lead to reading arbitrary files. This issue did not belong to the original attack but it was part of a series of potential incidents that could happen to ONUS so, on behalf of ONUS, we would like to mention this contribution here and sincerely thank **Wjbuboyz** for the information. This issue was also fixed shortly after.

## How did the attack happen?

As we have mentioned, the hacked targets were S3 buckets; therefore, we narrowed down the scope of the investigation by identifying services that interacted with those buckets and found a cluster of Cyclos services that might be the root cause of the attack.

Checking the access log in that cluster, we saw that Log4Shell payloads were used to establish connections to the server **45.147.230.219 (0x2d93e6db)** at port 82. The vendor has not confirmed the vulnerable modules of Cyclos but we believe that the vulnerability was exploited in the following way:

![Image 8](https://s.cystack.net/resource/home/content/28190936/1.png)![Image 9](https://s.cystack.net/resource/home/content/28190954/2.png)
The history command also showed that the attackers’ commands were successfully executed. They managed to forward the content of the **stdout/stderr** to the destination server **45.147.230.219**which is the same with what the access log showed.

![Image 10](https://s.cystack.net/resource/home/content/28191006/9.png)
The reason why they read _cyclos.properties_ is that this file contains AWS credentials. The most serious mistake of ONUS is that ONUS granted the _AmazonS3FullAccess_ permission to the access key which allowed attackers to compromise and easily delete all of the S3 buckets.

![Image 11](https://s.cystack.net/resource/home/content/28191018/8.png)
Also on these servers, ONUS had a script to periodically back up the database to S3 which contained the database hostname and username/password as well as backup SQL files. As a consequence, the attackers could access the ONUS database to get user information.

![Image 12](https://s.cystack.net/resource/home/content/28191119/7.png)
To facilitate access, the attackers downloaded and ran a backdoor on the server. This backdoor was named _kworker_ for the purpose of disguising as the Linux operating system’s kworker service. Analyzing this backdoor also helped us to know more about the attackers, which we will show in detail in the next section.

![Image 13](https://s.cystack.net/resource/home/content/28191135/6.png)
## Analyzing the backdoor

The _kworker_ backdoor obtained was written in Golang 1.17.2 and built for Linux x64. It was used as a tunnel connecting the C&C server and the compromised server via SSH protocol (a wise way to avoid detection!).

Upon starting, it created a SSH connection with the credentials as follows:

*   host: 45.147.230.219
*   port: 81
*   password: kim
*   user: peter

![Image 14](https://s.cystack.net/resource/home/content/28191150/10.png)![Image 15](https://s.cystack.net/resource/home/content/28191159/11.png)
SOCKS connection used as a backup when SSH is down has the credentials as follows:

*   user: peter
*   password: kim
*   tag: peter kim

When running, the backdoor continuously sent **stdout/stderr** data to the C&C server as well as continuously received commands from it.

![Image 16](https://s.cystack.net/resource/home/content/28191207/12.png)

Getting data from stdout/stderr

![Image 17](https://s.cystack.net/resource/home/content/28191220/13.png)

Executing the received commands

![Image 18](https://s.cystack.net/resource/home/content/28191230/14.png)

Reading files

The backdoor might have been created by the attackers themselves for this particular attack based on the go-socks5 library.

![Image 19](https://s.cystack.net/resource/home/content/28191236/5.png)
## Identifying the attackers

The attackers’ method of concealing their identities was relatively sophisticated. The IP addresses we have collected appear to be from VPN service providers. However, you can recognize an interesting point right away in the following screenshots.

![Image 20](https://s.cystack.net/resource/home/content/28191244/3.png)![Image 21](https://s.cystack.net/resource/home/content/28191249/4.png)
Yes, the attackers seem to be Vietnamese!

## Patching the vulnerabilities

CyStack recommended ONUS to remediate vulnerabilities and improve their security by:

*   Patching the Log4Shell vulnerability in Cyclos according to the instructions of the vendor
*   Deactivating all leaked credentials of AWS
*   Granting permissions properly to AWS keys that can access AWS S3 buckets and other services
*   Blocking public access to all sensitive S3 buckets and requiring tokens to access the certain objects

ONUS has made lots of efforts in securing their system, for example by collaborating with security partners and joining [Bug Bounty programs](https://whitehub.net/programs/onus/), but they still could not be exempt from the Log4Shell vulnerability. We are concerned that similar incidents will happen or are happening elsewhere; we hope that this post can provide you with some insights as well as some measures against this vulnerability.

_Trung Nguyen, Son Nguyen, Chau Ha, Chau Nguyen, Khoi Vu, Duong Tran from CyStack Security Team_
