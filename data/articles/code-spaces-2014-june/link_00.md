Title: Hacker Puts Hosting Service Code Spaces Out of Business

URL Source: https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/

Published Time: 2014-06-18T21:09:11+00:00

Markdown Content:
# Hacker Puts Hosting Service Code Spaces Out of Business | Threatpost

[](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/#)[Threatpost](https://threatpost.com/)

*   [Podcasts](https://threatpost.com/microsite/threatpost-podcasts-going-beyond-the-headlines/)
*   [Malware](https://threatpost.com/category/malware-2/)
*   [Vulnerabilities](https://threatpost.com/category/vulnerabilities/)
*   [InfoSec Insiders](https://threatpost.com/microsite/infosec-insiders-community/)
*   [Webinars](https://threatpost.com/category/webinars/)

*   [](https://www.facebook.com/Threatpost/ "Facebook")
*   [](https://twitter.com/threatpost/ "Twitter")
*   [](https://www.linkedin.com/company/threatpost/ "LinkedIn")
*   [](https://www.youtube.com/user/threatpost "YouTube")
*   [](https://feedly.com/threatpost "Feedly")
*   [](https://www.instagram.com/Threatpost/ "Instagram")
*   [](https://threatpost.com/feed "RSS")

 Search

*   [Hacker Exploits NAS Vulnerabilities to Mine $620K in Dogecoin Previous article](https://threatpost.com/hacker-exploits-nas-vulnerabilities-to-mine-620k-in-dogecoin/106756/)
*   [Possible TrueCrypt Fork in the Works Next article](https://threatpost.com/possible-truecrypt-fork-in-the-works/106769/)

# Hacker Puts Hosting Service Code Spaces Out of Business

![Image 1](https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2014/06/07021258/shutterstock_173668979.jpg)

[![Image 2](https://media.threatpost.com/wp-content/uploads/sites/103/2021/06/10095238/avatar_def-60x60.png)](https://threatpost.com/author/michael/)

Author: [Michael Mimoso](https://threatpost.com/author/michael/)

June 18, 2014  5:09 pm

2 minute read 

**Share this article:**

*   [](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/#)
*   [](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/#)

Cloud-based code-hosting service Code Spaces announced today it was going out of business after a hacker deleted most of its machines, customer data and backups.

Code Spaces, a code-hosting and software collaboration platform, has been put out of business by an attacker who deleted the company’s data and backups.

Officials wrote a lengthy [explanation and apology](http://www.codespaces.com/) on the company’s website, promising to spend its current resources helping customers recover whatever data may be left.

“Code Spaces will not be able to operate beyond this point, the cost of resolving this issue to date and the expected cost of refunding customers who have been left without the service they paid for will put Code Spaces in an irreversible position both financially and in terms of ongoing credibility,” read the note. “As such at this point in time we have no alternative but to cease trading and concentrate on supporting our affected customers in exporting any remaining data they have left with us.”

The beginning of the end was a DDoS attack initiated yesterday that was accompanied by an intrusion into Code Spaces’ Amazon EC2 control panel. Extortion demands were left for Code Spaces officials, along with a Hotmail address they were supposed to use to contact the attackers.

“Upon realization that somebody had access to our control panel, we started to investigate how access had been gained and what access that person had to the data in our systems,” Code Spaces said. “It became clear that so far no machine access had been achieved due to the intruder not having our private keys.”

Code Spaces said it changed its EC2 passwords, but quickly discovered the attacker had created backup logins, and once recovery attempts were noticed, the attacker began deleting artifacts from the panel.

“We finally managed to get our panel access back, but not before he had removed all EBS snapshots, S3 buckets, all AMI’s, some EBS instances and several machine instances,” Code Spaces said. “In summary, most of our data, backups, machine configurations and offsite backups were either partially or completely deleted.”

“In summary, most of our data, backups, machine configurations and offsite backups were either partially or completely deleted.”

[Amazon Web Services](https://aws.amazon.com/security/) customers are responsible for credential management. Amazon, however, has built-in support for two-factor authentication that can be used with AWS accounts and accounts managed by the AWS Identity and Access Management tool. AWS IAM enables control over user access, including individual credentials, role separation and least privilege.

Within 12 hours, Code Spaces went from a viable business to devastation. The company reported that all of its svn repositories—backups and snapshots—were deleted. All EBS volumes containing database files were also deleted. A few old svn nodes and one git node were left untouched, the company said.

A [cache](http://webcache.googleusercontent.com/search?q=cache:q-d4D3mJjaAJ:www.codespaces.com/features+&cd=1&hl=en&ct=clnk&gl=us) of Code Spaces services includes promises of full redundancy and that code is duplicated and distributed among data centers on three continents.

“Backing up data is one thing, but it is meaningless without a recovery plan, not only that a recovery plan – and one that is well-practiced and proven to work time and time again,” Code Spaces said. “Code Spaces has a full recovery plan that has been proven to work and is, in fact, practiced.”

**Share this article:**

*   [Cloud Security](https://threatpost.com/category/cloud-security/)
*   [Hacks](https://threatpost.com/category/hacks/)

### [Suggested articles](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/#)

[![Image 3](https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2020/12/24143857/2021_digits-540x270.jpg)](https://threatpost.com/2021-cybersecurity-trends/162629/)
## [2021 Cybersecurity Trends: Bigger Budgets, Endpoint Emphasis and Cloud](https://threatpost.com/2021-cybersecurity-trends/162629/)

Insider threats are redefined in 2021, the work-from-home trend will continue define the threat landscape and mobile endpoints become the attack vector of choice, according 2021 forecasts.

January 3, 2021

[1](https://threatpost.com/2021-cybersecurity-trends/162629/#comments)

[![Image 4](https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2020/11/23134526/Ransomware-Webinar-Cover-Image-540x270.png)](https://threatpost.com/ransomware-getting-ahead-inevitable-attack/162655/)
## [What’s Next for Ransomware in 2021?](https://threatpost.com/ransomware-getting-ahead-inevitable-attack/162655/)

Ransomware response demands a whole-of-business plan before the next attack, according to our roundtable of experts.

December 31, 2020

[2](https://threatpost.com/ransomware-getting-ahead-inevitable-attack/162655/#comments)

[![Image 5: underground market pricing](https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2019/04/08145106/Dark-web-540x270.jpg)](https://threatpost.com/rdp-server-access-payment-card-data-in-high-cybercrime-demand/162476/)
## [Dark Web Pricing Skyrockets for Microsoft RDP Servers, Payment-Card Data](https://threatpost.com/rdp-server-access-payment-card-data-in-high-cybercrime-demand/162476/)

Underground marketplace pricing on RDP server access, compromised payment card data and DDoS-For-Hire services are surging.

December 21, 2020

[![Image 6: Cybersecurity for your growing business](https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2022/09/05095106/cybersecurity_336_300x2.jpg)](https://www.kaspersky.com/small-to-medium-business-security/cloud?reseller=gl_KES-Cloud-ThreatPost_awarn_ona_smm__all_b2b_some_ban_______&utm_source=threatpost&utm_medium=sm-project&utm_campaign=gl_KES-Cloud-ThreatPost_kk0084&utm_content=banner&utm_term=gl_threatpost_organic_w84uo46uhuoqivv)

### InfoSec Insider

*   [![Image 7](https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2022/04/29082135/cloud-digital-64x64.png)](https://threatpost.com/secure-move-cloud/180335/ "Securing Your Move to the Hybrid Cloud")
## [Securing Your Move to the Hybrid Cloud](https://threatpost.com/secure-move-cloud/180335/)

August 1, 2022 
*   [![Image 8](https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2016/12/06095327/01_intro_iot-e1520348007355-64x64.png)](https://threatpost.com/physical-security-maintenance/180269/ "Why Physical Security Maintenance Should Never Be an Afterthought")
## [Why Physical Security Maintenance Should Never Be an Afterthought](https://threatpost.com/physical-security-maintenance/180269/)

July 25, 2022 
*   [![Image 9](https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2019/06/20122305/Ransomware-64x64.jpg)](https://threatpost.com/contis-costa-rica/180258/ "Conti’s Reign of Chaos: Costa Rica in the Crosshairs")
## [Conti’s Reign of Chaos: Costa Rica in the Crosshairs](https://threatpost.com/contis-costa-rica/180258/)

July 20, 2022 
*   [![Image 10](https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2018/07/19123143/Security_Cyber_Insurance-64x64.jpg)](https://threatpost.com/war-impact-cyber-insurance/180185/ "How War Impacts Cyber Insurance")
## [How War Impacts Cyber Insurance](https://threatpost.com/war-impact-cyber-insurance/180185/)

July 12, 2022 
*   [![Image 11: Cutting Through the Noise from Daily Alerts](https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2021/08/03142545/Cutting-Through-the-Noise-from-Daily-Alerts-64x64.png)](https://threatpost.com/rethinking-vulnerability-management/180177/ "Rethinking Vulnerability Management in a Heightened Threat Landscape")
## [Rethinking Vulnerability Management in a Heightened Threat Landscape](https://threatpost.com/rethinking-vulnerability-management/180177/)

July 11, 2022 

[![Image 12: Cybersecurity for your growing business](https://kasperskycontenthub.com/threatpost-global/files/2022/09/cybersecurity_336_500x2.jpg)](https://www.kaspersky.com/small-to-medium-business-security/cloud?reseller=gl_KES-Cloud-ThreatPost_awarn_ona_smm__all_b2b_some_ban_______&utm_source=threatpost&utm_medium=sm-project&utm_campaign=gl_KES-Cloud-ThreatPost_kk0084&utm_content=banner&utm_term=gl_threatpost_organic_w84uo46uhuoqivv)

[Threatpost](https://threatpost.com/)
[The First Stop For Security News](https://threatpost.com/)

*   [Home](https://threatpost.com/)
*   [About Us](https://threatpost.com/about-threatpost/)
*   [Contact Us](https://threatpost.com/contact-us/)
*   [RSS Feeds](https://threatpost.com/rss-feeds/)

*   Copyright © 2026 Threatpost
*   [Privacy Policy](https://threatpost.com/privacy-policy/)
*   [Terms and Conditions](https://threatpost.com/tos/)

*   [](https://www.facebook.com/Threatpost/ "Facebook")
*   [](https://twitter.com/threatpost/ "Twitter")
*   [](https://www.linkedin.com/company/threatpost/ "LinkedIn")
*   [](https://www.youtube.com/user/threatpost "YouTube")
*   [](https://feedly.com/threatpost "Feedly")
*   [](https://www.instagram.com/Threatpost/ "Instagram")
*   [](https://threatpost.com/feed "RSS")

### Topics

*   [Black Hat](https://threatpost.com/category/bh/)
*   [Breaking News](https://threatpost.com/category/breaking-news/)
*   [Cloud Security](https://threatpost.com/category/cloud-security/)
*   [Critical Infrastructure](https://threatpost.com/category/critical-infrastructure/)
*   [Cryptography](https://threatpost.com/category/cryptography/)
*   [Facebook](https://threatpost.com/category/facebook/)
*   [Government](https://threatpost.com/category/government/)
*   [Hacks](https://threatpost.com/category/hacks/)
*   [IoT](https://threatpost.com/category/iot/)
*   [Malware](https://threatpost.com/category/malware-2/)
*   [Mobile Security](https://threatpost.com/category/mobile-security/)
*   [Podcasts](https://threatpost.com/category/podcasts/)
*   [Privacy](https://threatpost.com/category/privacy/)
*   [RSAC](https://threatpost.com/category/rsac/)
*   [Security Analyst Summit](https://threatpost.com/category/sas/)
*   [Videos](https://threatpost.com/category/videos/)
*   [Vulnerabilities](https://threatpost.com/category/vulnerabilities/)
*   [Web Security](https://threatpost.com/category/web-security/)

[](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/#)[Threatpost](https://threatpost.com/)

*   [](https://www.facebook.com/Threatpost/ "Facebook")
*   [](https://twitter.com/threatpost/ "Twitter")
*   [](https://www.linkedin.com/company/threatpost/ "LinkedIn")
*   [](https://www.youtube.com/user/threatpost "YouTube")
*   [](https://feedly.com/threatpost "Feedly")
*   [](https://www.instagram.com/Threatpost/ "Instagram")
*   [](https://threatpost.com/feed "RSS")

### Topics

*   [Cloud Security](https://threatpost.com/category/cloud-security/)
*   [Malware](https://threatpost.com/category/malware-2/)
*   [Vulnerabilities](https://threatpost.com/category/vulnerabilities/)
*   [Privacy](https://threatpost.com/category/privacy/)

[Show all](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/#)

*   [Black Hat](https://threatpost.com/category/bh/)
*   [Critical Infrastructure](https://threatpost.com/category/critical-infrastructure/)
*   [Cryptography](https://threatpost.com/category/cryptography/)
*   [Facebook](https://threatpost.com/category/facebook/)
*   [Featured](https://threatpost.com/category/featured/)
*   [Government](https://threatpost.com/category/government/)
*   [Hacks](https://threatpost.com/category/hacks/)
*   [IoT](https://threatpost.com/category/iot/)
*   [Mobile Security](https://threatpost.com/category/mobile-security/)
*   [Podcasts](https://threatpost.com/category/podcasts/)
*   [RSAC](https://threatpost.com/category/rsac/)
*   [Security Analyst Summit](https://threatpost.com/category/sas/)
*   [Slideshow](https://threatpost.com/category/slideshow/)
*   [Videos](https://threatpost.com/category/videos/)
*   [Web Security](https://threatpost.com/category/web-security/)

### Authors

*   [Elizabeth Montalbano](https://threatpost.com/author/elizabethmontalbano/)
*   [Nate Nelson](https://threatpost.com/author/natenelson/)

### Threatpost

*   [Home](https://threatpost.com/)
*   [About Us](https://threatpost.com/about-threatpost/)
*   [Contact Us](https://threatpost.com/contact-us/)
*   [RSS Feeds](https://threatpost.com/rss-feeds/)

 Search

*   [](https://www.facebook.com/Threatpost/ "Facebook")
*   [](https://twitter.com/threatpost/ "Twitter")
*   [](https://www.linkedin.com/company/threatpost/ "LinkedIn")
*   [](https://www.youtube.com/user/threatpost "YouTube")
*   [](https://feedly.com/threatpost "Feedly")
*   [](https://www.instagram.com/Threatpost/ "Instagram")
*   [](https://threatpost.com/feed "RSS")

[](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/#)

InfoSec Insider

### Infosec Insider Post

Infosec Insider content is written by a trusted community of Threatpost cybersecurity subject matter experts. Each contribution has a goal of bringing a unique voice to important cybersecurity topics. Content strives to be of the highest quality, objective and non-commercial.

[](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/#)

Sponsored

### Sponsored Content

Sponsored Content is paid for by an advertiser. Sponsored content is written and edited by members of our sponsor community. This content creates an opportunity for a sponsor to provide insight and commentary from their point-of-view directly to the Threatpost audience. The Threatpost editorial team does not participate in the writing or editing of Sponsored Content.

We use cookies to make your experience of our websites better. By using and further navigating this website you accept this. Detailed information about the use of cookies on this website is available by clicking on [more information](https://threatpost.com/web-privacy-policy/).

ACCEPT AND CLOSE