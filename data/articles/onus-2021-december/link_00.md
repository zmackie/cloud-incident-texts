Title: The attack on ONUS – A real-life case of the Log4Shell vulnerability

URL Source: https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability

Markdown Content:
# The attack on ONUS – A real-life case of the Log4Shell vulnerability

[](tel:+842471099656)

[![Image 1: CyStack logo](https://cystack.net/images/logo-black.svg)](https://cystack.net/)
*   Products & Services Products & Services
*   Solutions Solutions
*   [Pricing Pricing](https://cystack.net/pricing)
*   Company Company
*   Resources Resources

Schedule a Free Consultation

![Image 2: En](https://cystack.net/icons/EN.svg)
en

###### Table of Contents

[TLDR; (Too long; didn’t read)](https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability#tldr-(too-long-didn't-read))[Timeline](https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability#timeline)[How did the attack happen?](https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability#how-did-the-attack-happen)[Analyzing the backdoor](https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability#analyzing-the-backdoor)[Identifying the attackers](https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability#identifying-the-attackers)[Patching the vulnerabilities](https://cystack.net/research/the-attack-on-onus-a-real-life-case-of-the-log4shell-vulnerability#patching-the-vulnerabilities)

###### Subscribe for weekly updates

- [x] I agree with [Terms of Service](https://cystack.net/terms-of-service)and[Privacy Policy](https://cystack.net/privacy) of CyStack 

Subscribe to Newsletter

###### Share

![Image 3: CyStack logo social](https://cystack.net/images/blog/Facebook.svg)![Image 4: CyStack logo social](https://cystack.net/images/blog/Twitter.svg)![Image 5: CyStack logo social](https://cystack.net/images/blog/Linkein.svg)

Threats & Research
# The attack on ONUS – A real-life case of the Log4Shell vulnerability

![Image 6: CyStack image](https://secure.gravatar.com/avatar/5e1e19d9b81295eeafdbc4175f18cc5b99a688411b0b5a2189c63881dff568b1?s=48&d=mm&r=g)

Trung Nguyen

Hacker. Builder. Educator. On a mission to make the internet safer.|April 1, 2026

Reading Time:  6 minutes![Image 7](https://s.cystack.net/resource/home/content/28191355/log4j.png)
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

## Related posts

![Image 22: Analysis of Suspected Malware Linked to APT-Q-27 Targeting Financial Institutions](https://s.cystack.net/resource/home/content/04073915/Cystack-post-ENG-Mid.png)

[###### Analysis of Suspected Malware Linked to APT-Q-27 Targeting Financial Institutions](https://cystack.net/research/malware-linked-apt-q-27)

February 4 2026|Threats & Research

Reading Time:  12 minutes Đọc bản tiếng Việt tại đây Overview Context In mid-January 2026, CyStack’s security team observed anomalous activity on a corporate […]

![Image 23: Flash Loan Attack](https://s.cystack.net/resource/home/content/24111518/Flash-Loan-Attack.png)

[###### Flash Loan Attack](https://cystack.net/research/flash-loan-attack)

June 27 2022|Threats & Research

Reading Time:  7 minutes Mở đầu Flash Loan Attack là một hình thức tấn công DeFi đã xuất hiện từ lâu, gây ra rất […]

![Image 24: Cuộc tấn công vào ONUS &#8211; Góc nhìn kỹ thuật từ lỗ hổng Log4Shell](https://s.cystack.net/resource/home/content/05070552/log4j.png)

[###### Cuộc tấn công vào ONUS – Góc nhìn kỹ thuật từ lỗ hổng Log4Shell](https://cystack.net/research/cuoc-tan-cong-vao-onus-goc-nhin-ky-thuat-tu-lo-hong-log4shell)

April 1 2026|Threats & Research

Reading Time:  7 minutes Read the English version here Log4Shell hiện đang là một cơn ác mộng (có lẽ là tồi tệ nhất cho […]

![Image 25: CyStack logo](https://cystack.net/images/logo-black.svg)![Image 26: CyStack logo](https://cystack.net/v4/images/layout/footer/LogoTagLine.svg)

Follow us on

[![Image 27: Facebook](https://cystack.net/v4/images/layout/footer/Facebook.svg)](https://www.facebook.com/cystacksecurity)[![Image 28: Twitter](https://cystack.net/v4/images/layout/footer/X.svg)](https://x.com/cystacksecurity)[![Image 29: Linkedin](https://cystack.net/v4/images/layout/footer/Linkedin.svg)](https://www.linkedin.com/company/cystacksecurity)[![Image 30: Tiktok](https://cystack.net/v4/images/layout/footer/Tiktok.svg)](https://www.tiktok.com/@cystack)

#### Vietnam Office

*   Tan Hong Ha Complex, 317 Truong Chinh, Hanoi, Vietnam.
*   (+84) 247 109 9656

#### Canada Office

*   2376 Dundas St W, Toronto, Ontario M6P 0C1, Canada.
*   (+1) 437 361 5461

#### Security Testing & Assessment

[* Penetration Testing](https://cystack.net/spotlight/pentest)[* Red Teaming](https://cystack.net/red-teaming)[* CyStack VulnScan](https://cystack.net/vulnscan)

[* WhiteHub](https://whitehub.net/)[* Cloud Audit](https://cystack.net/services/infrastructure)[* Blockchain Audit](https://cystack.net/services/blockchain-protocol-audit)

#### Data Protection

[* CyStack Endpoint](https://cystack.net/products/endpoint)[* Locker](https://locker.io/)

[* Data Leak Detection](https://cystack.net/data-leak-detection)

#### Security Operations

[* Vulnerability Management](https://cystack.net/services/vulnerability-management)[* SOC](https://cystack.net/services/security-monitoring)

[* Digital Forensics (DFIR)](https://cystack.net/services/incident-response)[* Training & Consulting](https://cystack.net/services/security-training)

#### Company

[* About CyStack](https://cystack.net/about)[* Brand](https://cystack.net/brand)

[* Contact](https://cystack.net/contact)[* Careers](https://cystack.net/careers/open-roles)

*   Newsroom

#### Resource

[* Blog](https://cystack.net/blog)[* Research](https://cystack.net/research)

[* Projects](https://cystack.net/projects)[* Customers](https://cystack.net/customers)

[* Support](https://cystack.net/)

![Image 31: ISO](https://cystack.net/v4/images/layout/footer/ISOMobile.svg)ISMS ISO [27001:2022](https://www.iafcertsearch.org/certification/qTm2LqNtmRfkC6RIQvFvSJ0i) and Quality Management Standard ISO [9001:2015](https://www.iafcertsearch.org/certification/Jpfz2Xe3847JELEKCSzp7DGt) Compliance

© 2026 CyStack

![Image 32: ISO](https://cystack.net/v4/images/layout/footer/ISO.svg)ISMS ISO [27001:2022](https://www.iafcertsearch.org/certification/qTm2LqNtmRfkC6RIQvFvSJ0i) and Quality Management Standard ISO [9001:2015](https://www.iafcertsearch.org/certification/Jpfz2Xe3847JELEKCSzp7DGt) Compliance

© 2026 CyStack
[* Terms of Use](https://cystack.net/terms-of-service)[* Security](https://cystack.net/security)[* Privacy](https://cystack.net/privacy)