Title: BrowserStack analysis: unpatched inactive machine compromised by shel…

URL Source: http://archive.today/rsmmS

Published Time: 2022-09-23T02:28:51Z

Markdown Content:
# BrowserStack analysis: unpatched inactive machine compromised by shellshock vulnerability

## BrowserStack analysis: unpatched inactive machine compromised by shel…

![Image 1](https://archive.ph/rsmmS/0fa47cc7394166fd0a83ab64b0f77b6f8499e94e/scr.png)archived 23 Sep 2022 02:28:51 UTC

[archive.today webpage capture](https://archive.today/)Saved from no other snapshots from this url 23 Sep 2022 02:28:51 UTC
All snapshots**from host**[www.databreaches.net](https://archive.ph/www.databreaches.net)
[Webpage](https://archive.ph/rsmmS)[Screenshot](https://archive.ph/rsmmS/image)
[![Image 2](blob:https://dgk1xndcng818h.archive.ph/0095f2913a45ffc2ba2762a56693c174)share](https://archive.ph/rsmmS/share)[![Image 3](blob:https://dgk1xndcng818h.archive.ph/c920c8751caf1ccb063b9881e33e394a)download .zip](https://archive.ph/download/rsmmS.zip)[![Image 4](blob:https://dgk1xndcng818h.archive.ph/34817325a0d7d1f06fd7ff31004902df)report bug or abuse](https://archive.ph/rsmmS/abuse)[![Image 5](blob:https://dgk1xndcng818h.archive.ph/0d198433ea69bbd3ce4e0e2b0d36beb3)Buy me a coffee](https://buymeacoffee.com/glizzykingdreko)

[![Image 6: close](blob:https://dgk1xndcng818h.archive.ph/68ba013c93c8e68f51ccd3f3cb926e2b)](https://archive.ph/rsmmS)

Reddit

VKontakte

Twitter

Pinboard

Livejournal

short link

long link

markdown

html code

wiki code

[](https://archive.ph/o/rsmmS/https://www.databreaches.net/)

[# DataBreaches.net](https://archive.ph/o/rsmmS/https://www.databreaches.net/)The Office of Inadequate Security

Toggle navigation

*   [News](https://archive.ph/o/rsmmS/https://www.databreaches.net/news/)
*   [Breach Laws](https://archive.ph/o/rsmmS/https://www.databreaches.net/state-breach-notification-laws/)
*   [About](https://archive.ph/o/rsmmS/https://www.databreaches.net/about/)
*   [Donate XMR](https://archive.ph/o/rsmmS/https://www.databreaches.net/donate-xmr/)
*   [Contact](https://archive.ph/o/rsmmS/https://www.databreaches.net/contact/)
*   [Privacy](https://archive.ph/o/rsmmS/https://www.databreaches.net/privacy-policy/)
*   [Transparency Reports](https://archive.ph/o/rsmmS/https://www.databreaches.net/transparency-reports/)
*   [__](javascript:null)Search for:  

[](https://archive.ph/o/rsmmS/https://www.databreaches.net/)

[# DataBreaches.net](https://archive.ph/o/rsmmS/https://www.databreaches.net/)The Office of Inadequate Security

Toggle navigation
*   [News](https://archive.ph/o/rsmmS/https://www.databreaches.net/news/)
*   [Breach Laws](https://archive.ph/o/rsmmS/https://www.databreaches.net/state-breach-notification-laws/)
*   [About](https://archive.ph/o/rsmmS/https://www.databreaches.net/about/)
*   [Donate XMR](https://archive.ph/o/rsmmS/https://www.databreaches.net/donate-xmr/)
*   [Contact](https://archive.ph/o/rsmmS/https://www.databreaches.net/contact/)
*   [Privacy](https://archive.ph/o/rsmmS/https://www.databreaches.net/privacy-policy/)
*   [Transparency Reports](https://archive.ph/o/rsmmS/https://www.databreaches.net/transparency-reports/)
*   [](javascript:null)Search for:  

# BrowserStack analysis: unpatched inactive machine compromised by shellshock vulnerability

[Home](https://archive.ph/o/rsmmS/https://www.databreaches.net/ "DataBreaches.net")/BrowserStack analysis: unpatched inactive machine compromised by shellshock vulnerability

# BrowserStack analysis: unpatched inactive machine compromised by shellshock vulnerability

*   __ November 12, 2014
*   __[Dissent](https://archive.ph/o/rsmmS/https://www.databreaches.net/ "Visit Dissent’s website")

_BrowserStack sent DataBreaches.net the following analysis, which is being emailed to all their users:_

> As you may already know, BrowserStack experienced an attack on 9th November, 2014 at 23:30 GMT during which an individual was able to gain unauthorized access to some of our users’ registered email addresses. He then tried to send an email <[http://pastebin.com/i788JT76](https://archive.ph/o/rsmmS/pastebin.com/i788JT76)> to all our registered users, but he was only able to reach less than 1% (our estimate is 5,000 users). The email contained inaccurate information, even claiming that BrowserStack would be shutting down.
> 
> 
> 
> When we realized this, our only concern was to protect our users. This involved temporarily taking down the service, as we scrutinized each component carefully. This inconvenienced our users for several hours, and for that we are truly sorry.
> 
> 
> 
> ***What happened?***
> 
> 
> 
> BrowserStack application servers run using Amazon Web Services. The configuration is vast, consisting of thousands of servers. One of these was an old prototype machine, which was the target of the breach.
> 
> 
> 
> The machine had been running since before 2012, and was not in active use. It was penetrated using the shellshock vulnerability, and since it was no longer in active use, it did not have the appropriate patch installed.
> 
> 
> 
> The old prototype machine had our AWS API access key and secret key. Once the hacker gained access to the keys, he created an IAM user, and generated a key-pair. He was then able to run an instance inside our AWS account using these credentials, and mount one of our backup disks. This backup was of one of our component services, used for production environment, and contained a config file with our database password. He also whitelisted his IP on our database security group, which is the AWS firewall.
> 
> 
> 
> He began to copy one of our tables, which contained partial user information, including email IDs, hashed passwords, and last tested URL. His copy operation locked the database table, which raised alerts on our monitoring system. On receiving the alerts, we checked the logs, saw an unrecognized IP, and blocked it right away. In that time, the hacker had been able to retrieve only a portion of the data. Finally, using this data and the SES credentials, he was able to send an email to some of our users.
> 
> 
> 
> ***What was the extent of the damage?***
> 
> 
> 
> Our database logs confirmed that user data was partially copied, but no user test history was compromised. Therefore all user data remains wholly intact. Most crucially, *credit card details were not compromised*, as we only store the last 4 digits of the credit card number, and all payment processing takes place through our payment processing partner. All user passwords are salted, and encrypted with the powerful bcrypt algorithm, which creates an irreversible hash which cannot be cracked. However, as an added precaution, we suggest that users change their BrowserStack account passwords.
> 
> 
> 
> We were able to verify the actions of the hacker using AWS CloudTrail, which confirmed that no other services were compromised, no other machines were booted, and our AMIs and other data stores were not copied.
> 
> 
> 
> In addition, our production web server logs indicate that we were experiencing shellshock attempts, but they failed because the production web server has the necessary patches to foil all such attempts.
> 
> 
> 
> ***Points in the email***
> 
> 
> 
> We would now like to address the points raised in the email. The hacker quoted three paragraphs from our Security documentation, as follows:
> 
> 
> 
> – *after the restoration process is complete, the virtual machines are guaranteed to be tamper-proof.* → Our restoration process is indeed amper-proof. When we create a test machine from scratch, we take a snapshot. After every user session, the test machine is restored to it original state using that snapshot. Even if a previous user manages to install a malicious software, it is always erased due to the restoration process.
> 
> 
> 
> – *The machines themselves are in a secure network, and behind strong firewalls to present the safest environment possible.*→ Every single machine has an OS firewall, in addition to the hardware network firewalls we use. On EC2, we use security groups as an equivalent safety measure. We also use industry-standard brute force-throttling measures.
> 
> 
> 
> – *At any given time, you have sole access to a virtual machine. Your testing session cannot be seen or accessed by other users, including BrowserStack administrators. Once you release a virtual machine, it is taken off the grid, and restored to its initial settings. All your data is destroyed in this process. *→ The application ensures that a machine is allocated to only one person at a time, and VNC passwords are randomly generated for each session. Thus, even our administrators cannot see your test session.
> 
> 
> 
> With respect to the plaintext passwords on the VMs, this is certainly not the case, as we moved to key-based authentication years ago. Moreover root login is disabled in our SSH configuration.
> 
> 
> 
> Both the passwords mentioned, ‘nakula’ and ‘c0stac0ff33’, were indeed in use a couple of years ago during our prototyping phase, and thus were present in the old prototype machine that was hacked. ‘nakula’ was previously our VNC password, and was hashed. However, unlike the hash used for the user passwords, this hash is much weaker. This was due to a limitation in VNC protocol, and we had overcome this liability by regenerating a new password for every session, and thus ‘nakula’ has not been in use for years. ‘c0stac0ff33’ was one of our system user passwords on the prototype machine, before we moved to key-based authentication.
> 
> 
> 
> It is true that we still run our VNC server on port 5901, but we do not believe that it is a security vulnerability because a current password is still required for access. As mentioned before, the passwords are changed every test session.
> 
> 
> 
> ***Where did we go wrong?***
> 
> 
> 
> All our servers, running or not, whether in active use or not, should have been patched with the latest security upgrades and updates including the shellshock one. Moreover, servers not in active use should have been stopped and the server shouldn’t have had the AWS keys.
> 
> 
> 
> Additionally, our communication could have been better. Instead of intermittent updates, we preferred to present a complete, honest picture of the attack to our users once our analysis was done.
> 
> 
> 
> ***Security measures taken to mitigate and prevent further incidents***
> 
> 
> 
> – After taking down the service, we revoked all the existing AWS keys and passwords, and generated new ones immediately, as an added security measure.
> 
>  – Subsequently, we went through all the SSH logs, web server logs, as well as AWS Cloud Trail logs, to ensure that no more damage was done.
> 
>  – We are migrating all backups to encrypted backups, and removing all unencrypted ones.
> 
>  – We have also put in several additional checks and alerts, which are triggered on specified AWS actions. As a precautionary measure we have also created new VM snapshots and have replaced all the existing ones.
> 
>  – To prevent further incidents, we are in the process of evaluating certain VPC/VPN options to enhance our security measures.
> 
>  – We’re going to have a security audit conducted by an external, independent agency.
> 
> 
> 
> Once again we apologise for the inconvenience. BrowserStack is deeply committed to providing the best and most secure testing infrastructure for our users. We will be forging ahead with exciting new releases in the next few weeks and look forward to continue serving you.
> 
> 
> 
> We have a trace and the IP of the hacker. We will be in touch with authorities soon to register an official complaint. Thank you for the support and understanding we have received over the last few days.
> 
> 
> 
> Regards,
> 
>  Adithya Chadalawada
> 
>  www.browserstack.com

### Related Posts:

*   [BrowserStack not shutting down, but email addresses were…](https://archive.ph/o/rsmmS/https://www.databreaches.net/browserstack-not-shutting-down-but-email-addresses-were-hacked/)
*   [Yahoo Says No Data Stolen in Shellshock Hack](https://archive.ph/o/rsmmS/https://www.databreaches.net/yahoo-says-no-data-stolen-in-shellshock-hack/)
*   [Database of Pakistani web site users exposed by hackers](https://archive.ph/o/rsmmS/https://www.databreaches.net/database-of-pakistani-web-site-users-exposed-by-hackers/)
*   [Glassdoor 'Carelessly' Exposed 600K Users' Emails, Suit Says](https://archive.ph/o/rsmmS/https://www.databreaches.net/glassdoor-carelessly-exposed-600k-users-emails-suit-says/)
*   [Finnish travel service hacked; thousands of users' passwords…](https://archive.ph/o/rsmmS/https://www.databreaches.net/finnish-travel-service-hacked-thousands-of-users-passwords-and-e-mail-addresses-exposed/)

*   [__](https://archive.ph/o/rsmmS/https://twitter.com/intent/tweet?text=BrowserStack%20analysis:%20unpatched%20inactive%20machine%20compromised%20by%20shellshock%20vulnerability&url=https://www.databreaches.net/browserstack-analysis-unpatched-inactive-machine-compromised-by-shellshock-vulnerability/)
*   [__](https://archive.ph/o/rsmmS/https://www.databreaches.net/browserstack-analysis-unpatched-inactive-machine-compromised-by-shellshock-vulnerability/)
*   [__](https://archive.ph/o/rsmmS/https://www.linkedin.com/shareArticle?mini=true&url=https://www.databreaches.net/browserstack-analysis-unpatched-inactive-machine-compromised-by-shellshock-vulnerability/&title=BrowserStack%20analysis:%20unpatched%20inactive%20machine%20compromised%20by%20shellshock%20vulnerability&source=&summary=BrowserStack%20sent%20DataBreaches.net%20the%20following%20analysis,%20which%20is%20being%20emailed%20to%20all%20their%20users:%20As%20you%20may%20already%20know,%20BrowserStack%20experienced%20an%20attack%20on%209th%20November,%202014%20at%2023:30%20GMT%20during%20which%20an%20individual%20was%20able%20to%20gain%20unauthorized%20access%20to%20some%20of%20our%20users%E2%80%99%20registered%20email%20addresses.%20He%20then%20tried%20to%20send%20an%20email%20%3Chttp://pastebin.com/i788JT76%3E%20to%20all%20our%20registered%20users,%20but%20he%20was%20only%20able%20to%20reach%20less%20than%201%25%20(our%20estimate%20is%205,000%20users).%20The%20email%20contained%20inaccurate%20information,%20even%20claiming%C2%A0that%20BrowserStack%20would%20be%20shutting%20down.%20When%20we%20realized%20this,%20our%20only%20concern%20was%20to%20protect%20our%20users.%20This%20involved%20temporarily%20taking%20down%20the%20service,%20as%20we%20scrutinized%20each%20component%20carefully.%20This%20inconvenienced%20our%20users%20for%20several%20hours,%20and%20for%20that%20we%20are%20truly%20sorry.%20*What%20happened?*%20BrowserStack%20application%20servers%20run%20using%20Amazon%20Web%20Services.%20The%20configuration%20is%20vast,%20consisting%20of%20thousands%20of%20servers.%20One%20of%20these%20was%20an%20old%20prototype%20machine,%20which%20was%20the%20target%20of%20the%20breach.%20The%20machine%20had%20been%20running%20since%20before%202012,%20and%20was%20not%20in%20active%20use.%20It%20was%20penetrated%20using%20the%20shellshock%20vulnerability,%20and%20since%20it%20was%20no%20longer%20in%20active%20use,%20it%20did%20not%20have%20the%20appropriate%20patch%20installed.%20The%20old%20prototype%20machine%20had%20our%20AWS%20API%20access%20key%20and%20secret%20key.%20Once%20the%20hacker%20gained%20access%20to%20the%20keys,%20he%20created%20an%20IAM%20user,%20and%20generated%20a%20key-pair.%20He%20was%20then%20able%20to%20run%20an%20instance%20inside%20our%20AWS%20account%20using%20these%20credentials,%20and%20mount%20one%20of%20our%20backup%20disks.%20This%20backup%20was%20of%20one%20of%20our%20component%20services,%20used%20for%20production%20environment,%20and%20contained%20a%20config%20file%20with%20our%20database%20password.%20He%20also%20whitelisted%20his%20IP%20on%20our%20database%20security%20group,%20which%20is%20the%20AWS%20firewall.%20He%20began%20to%20copy%20one%20of%20our%20tables,%20which%20contained%20partial%20user%20information,%20including%20email%20IDs,%20hashed%20passwords,%20and%20last%20tested%20URL.%20His%20copy%20operation%20locked%20the%20database%20table,%20which%20raised%20alerts%20on%20our%C2%A0monitoring%20system.%20On%20receiving%20the%20alerts,%20we%20checked%20the%20logs,%20saw%20an%20unrecognized%20IP,%20and%20blocked%20it%20right%20away.%20In%20that%20time,%20the%20hacker%20had%20been%20able%20to%20retrieve%20only%20a%20portion%20of%20the%20data.%20Finally,%20using%20this%20data%20and%20the%20SES%20credentials,%20he%20was%20able%20to%20send%20an%20email%20to%20some%20of%20our%20users.%20*What%20was%20the%20extent%20of%20the%20damage?*%20Our%20database%20logs%20confirmed%20that%20user%20data%20was%20partially%20copied,%20but%20no%20user%20test%20history%20was%20compromised.%20Therefore%20all%20user%20data%20remains%20wholly%20intact.%20Most%20crucially,%20*credit%20card%20details%20were%20not%20compromised*,%20as%20we%20only%20store%20the%20last%204%20digits%20of%20the%20credit%20card%20number,%20and%20all%20payment%20processing%20takes%20place%20through%20our%20payment%20processing%20partner.%20All%20user%20passwords%20are%20salted,%20and%20encrypted%20with%20the%20powerful%20bcrypt%20algorithm,%20which%20creates%20an%20irreversible%20hash%20which%20cannot%20be%20cracked.%20However,%20as%20an%20added%20precaution,%20we%20suggest%20that%20users%20change%20their%20BrowserStack%20account%20passwords.%20We%20were%20able%20to%20verify%20the%20actions%20of%20the%20hacker%20using%20AWS%20CloudTrail,%20which%20confirmed%20that%20no%20other%20services%20were%20compromised,%20no%20other%20machines%20were%20booted,%20and%20our%20AMIs%20and%20other%20data%20stores%20were%20not%20copied.%20In%20addition,%20our%20production%20web%20server%20logs%20indicate%20that%20we%20were%20experiencing%20shellshock%20attempts,%20but%20they%20failed%20because%20the%20production%20web%20server%20has%20the%20necessary%20patches%20to%20foil%20all%20such%20attempts.%20*Points%20in%20the%20email*%20We%20would%20now%20like%20to%20address%20the%20points%20raised%20in%20the%20email.%20The%20hacker%20quoted%20three%20paragraphs%20from%20our%20Security%20documentation,%20as%20follows:%20%E2%80%93%20*after%20the%20restoration%20process%20is%20complete,%20the%20virtual%20machines%20are%20guaranteed%20to%20be%20tamper-proof.*%20%E2%86%92%20Our%20restoration%20process%20is%20indeed%20amper-proof.%20When%20we%20create%20a%20test%20machine%20from%20scratch,%20we%20take%20a%20snapshot.%20After%20every%20user%20session,%20the%20test%20machine%20is%20restored%20to%20it%20original%20state%20using%20that%20snapshot.%20Even%20if%20a%20previous%20user%20manages%20to%20install%20a%20malicious%20software,%20it%20is%20always%20erased%20due%20to%20the%20restoration%20process.%20%E2%80%93%20*The%20machines%20themselves%20are%20in%20a%20secure%20network,%20and%20behind%20strong%20firewalls%20to%20present%20the%20safest%20environment%20possible.*%E2%86%92%20Every%20single%20machine%20has%20an%20OS%20firewall,%20in%20addition%20to%20the%20hardware%20network%20firewalls%20we%20use.%20On%20EC2,%20we%20use%20security%20groups%20as%20an%20equivalent%20safety%20measure.%20We%20also%20use%20industry-standard%20brute%20force-throttling%20measures.%20%E2%80%93%20*At%20any%20given%20time,%20you%20have%20sole%20access%20to%20a%20virtual%20machine.%20Your%20testing%20session%20cannot%20be%20seen%20or%20accessed%20by%20other%20users,%20including%20BrowserStack%20administrators.%20Once%20you%20release%20a%20virtual%20machine,%20it%20is%20taken%20off%20the%20grid,%20and%20restored%20to%20its%20initial%20settings.%20All%20your%20data%20is%20destroyed%20in%20this%20process.%20*%E2%86%92%20The%20application%20ensures%20that%20a%20machine%20is%20allocated%20to%20only%20one%20person%20at%20a%20time,%20and%20VNC%20passwords%20are%20randomly%20generated%20for%20each%20session.%20Thus,%20even%20our%20administrators%20cannot%20see%20your%20test%20session.%20With%20respect%20to%20the%20plaintext%20passwords%20on%20the%20VMs,%20this%20is%20certainly%20not%20the%20case,%20as%20we%20moved%20to%20key-based%20authentication%20years%20ago.%20Moreover%20root%20login%20is%20disabled%20in%20our%20SSH%20configuration.%20Both%20the%20passwords%20mentioned,%20%E2%80%98nakula%E2%80%99%20and%20%E2%80%98c0stac0ff33%E2%80%99,%20were%20indeed%20in%20use%20a%20couple%20of%20years%20ago%20during%20our%20prototyping%20phase,%20and%20thus%20were%20present%20in%20the%20old%20prototype%20machine%20that%20was%20hacked.%20%E2%80%98nakula%E2%80%99%20was%C2%A0previously%20our%20VNC%20password,%20and%20was%20hashed.%20However,%20unlike%20the%20hash%20used%20for%20the%20user%20passwords,%20this%20hash%20is%20much%20weaker.%20This%20was%20due%20to%20a%20limitation%20in%20VNC%20protocol,%20and%20we%20had%20overcome%20this%20liability%20by%20regenerating%20a%20new%20password%20for%20every%20session,%20and%20thus%20%E2%80%98nakula%E2%80%99%20has%20not%20been%20in%20use%20for%20years.%20%E2%80%98c0stac0ff33%E2%80%99%20was%20one%20of%20our%20system%20user%20passwords%20on%20the%20prototype%20machine,%20before%20we%20moved%20to%20key-based%20authentication.%20It%20is%20true%20that%20we%20still%20run%20our%20VNC%20server%20on%20port%205901,%20but%20we%20do%20not%20believe%20that%20it%20is%20a%20security%20vulnerability%20because%20a%20current%20password%20is%20still%20required%20for%20access.%20As%20mentioned%20before,%20the%20passwords%20are%20changed%20every%20test%20session.%20*Where%20did%20we%20go%20wrong?*%20All%20our%20servers,%20running%20or%20not,%20whether%20in%20active%20use%20or%20not,%20should%20have%20been%20patched%20with%20the%20latest%20security%20upgrades%20and%20updates%20including%20the%20shellshock%20one.%20Moreover,%20servers%20not%20in%20active%20use%20should%20have%20been%20stopped%20[%E2%80%A6])
*   [__](https://archive.ph/o/rsmmS/pinterest.com/pin/create/button/?url=https://www.databreaches.net/browserstack-analysis-unpatched-inactive-machine-compromised-by-shellshock-vulnerability/&description=BrowserStack%20sent%20DataBreaches.net%20the%20following%20analysis,%20which%20is%20being%20emailed%20to%20all%20their%20users:%20As%20you%20may%20already%20know,%20BrowserStack%20experienced%20an%20attack%20on%209th%20November,%202014%20at%2023:30%20GMT%20during%20which%20an%20individual%20was%20able%20to%20gain%20unauthorized%20access%20to%20some%20of%20our%20users%E2%80%99%20registered%20email%20addresses.%20He%20then%20tried%20to%20send%20an%20email%20%3Chttp://pastebin.com/i788JT76%3E%20to%20all%20our%20registered%20users,%20but%20he%20was%20only%20able%20to%20reach%20less%20than%201%25%20(our%20estimate%20is%205,000%20users).%20The%20email%20contained%20inaccurate%20information,%20even%20claiming%C2%A0that%20BrowserStack%20would%20be%20shutting%20down.%20When%20we%20realized%20this,%20our%20only%20concern%20was%20to%20protect%20our%20users.%20This%20involved%20temporarily%20taking%20down%20the%20service,%20as%20we%20scrutinized%20each%20component%20carefully.%20This%20inconvenienced%20our%20users%20for%20several%20hours,%20and%20for%20that%20we%20are%20truly%20sorry.%20*What%20happened?*%20BrowserStack%20application%20servers%20run%20using%20Amazon%20Web%20Services.%20The%20configuration%20is%20vast,%20consisting%20of%20thousands%20of%20servers.%20One%20of%20these%20was%20an%20old%20prototype%20machine,%20which%20was%20the%20target%20of%20the%20breach.%20The%20machine%20had%20been%20running%20since%20before%202012,%20and%20was%20not%20in%20active%20use.%20It%20was%20penetrated%20using%20the%20shellshock%20vulnerability,%20and%20since%20it%20was%20no%20longer%20in%20active%20use,%20it%20did%20not%20have%20the%20appropriate%20patch%20installed.%20The%20old%20prototype%20machine%20had%20our%20AWS%20API%20access%20key%20and%20secret%20key.%20Once%20the%20hacker%20gained%20access%20to%20the%20keys,%20he%20created%20an%20IAM%20user,%20and%20generated%20a%20key-pair.%20He%20was%20then%20able%20to%20run%20an%20instance%20inside%20our%20AWS%20account%20using%20these%20credentials,%20and%20mount%20one%20of%20our%20backup%20disks.%20This%20backup%20was%20of%20one%20of%20our%20component%20services,%20used%20for%20production%20environment,%20and%20contained%20a%20config%20file%20with%20our%20database%20password.%20He%20also%20whitelisted%20his%20IP%20on%20our%20database%20security%20group,%20which%20is%20the%20AWS%20firewall.%20He%20began%20to%20copy%20one%20of%20our%20tables,%20which%20contained%20partial%20user%20information,%20including%20email%20IDs,%20hashed%20passwords,%20and%20last%20tested%20URL.%20His%20copy%20operation%20locked%20the%20database%20table,%20which%20raised%20alerts%20on%20our%C2%A0monitoring%20system.%20On%20receiving%20the%20alerts,%20we%20checked%20the%20logs,%20saw%20an%20unrecognized%20IP,%20and%20blocked%20it%20right%20away.%20In%20that%20time,%20the%20hacker%20had%20been%20able%20to%20retrieve%20only%20a%20portion%20of%20the%20data.%20Finally,%20using%20this%20data%20and%20the%20SES%20credentials,%20he%20was%20able%20to%20send%20an%20email%20to%20some%20of%20our%20users.%20*What%20was%20the%20extent%20of%20the%20damage?*%20Our%20database%20logs%20confirmed%20that%20user%20data%20was%20partially%20copied,%20but%20no%20user%20test%20history%20was%20compromised.%20Therefore%20all%20user%20data%20remains%20wholly%20intact.%20Most%20crucially,%20*credit%20card%20details%20were%20not%20compromised*,%20as%20we%20only%20store%20the%20last%204%20digits%20of%20the%20credit%20card%20number,%20and%20all%20payment%20processing%20takes%20place%20through%20our%20payment%20processing%20partner.%20All%20user%20passwords%20are%20salted,%20and%20encrypted%20with%20the%20powerful%20bcrypt%20algorithm,%20which%20creates%20an%20irreversible%20hash%20which%20cannot%20be%20cracked.%20However,%20as%20an%20added%20precaution,%20we%20suggest%20that%20users%20change%20their%20BrowserStack%20account%20passwords.%20We%20were%20able%20to%20verify%20the%20actions%20of%20the%20hacker%20using%20AWS%20CloudTrail,%20which%20confirmed%20that%20no%20other%20services%20were%20compromised,%20no%20other%20machines%20were%20booted,%20and%20our%20AMIs%20and%20other%20data%20stores%20were%20not%20copied.%20In%20addition,%20our%20production%20web%20server%20logs%20indicate%20that%20we%20were%20experiencing%20shellshock%20attempts,%20but%20they%20failed%20because%20the%20production%20web%20server%20has%20the%20necessary%20patches%20to%20foil%20all%20such%20attempts.%20*Points%20in%20the%20email*%20We%20would%20now%20like%20to%20address%20the%20points%20raised%20in%20the%20email.%20The%20hacker%20quoted%20three%20paragraphs%20from%20our%20Security%20documentation,%20as%20follows:%20%E2%80%93%20*after%20the%20restoration%20process%20is%20complete,%20the%20virtual%20machines%20are%20guaranteed%20to%20be%20tamper-proof.*%20%E2%86%92%20Our%20restoration%20process%20is%20indeed%20amper-proof.%20When%20we%20create%20a%20test%20machine%20from%20scratch,%20we%20take%20a%20snapshot.%20After%20every%20user%20session,%20the%20test%20machine%20is%20restored%20to%20it%20original%20state%20using%20that%20snapshot.%20Even%20if%20a%20previous%20user%20manages%20to%20install%20a%20malicious%20software,%20it%20is%20always%20erased%20due%20to%20the%20restoration%20process.%20%E2%80%93%20*The%20machines%20themselves%20are%20in%20a%20secure%20network,%20and%20behind%20strong%20firewalls%20to%20present%20the%20safest%20environment%20possible.*%E2%86%92%20Every%20single%20machine%20has%20an%20OS%20firewall,%20in%20addition%20to%20the%20hardware%20network%20firewalls%20we%20use.%20On%20EC2,%20we%20use%20security%20groups%20as%20an%20equivalent%20safety%20measure.%20We%20also%20use%20industry-standard%20brute%20force-throttling%20measures.%20%E2%80%93%20*At%20any%20given%20time,%20you%20have%20sole%20access%20to%20a%20virtual%20machine.%20Your%20testing%20session%20cannot%20be%20seen%20or%20accessed%20by%20other%20users,%20including%20BrowserStack%20administrators.%20Once%20you%20release%20a%20virtual%20machine,%20it%20is%20taken%20off%20the%20grid,%20and%20restored%20to%20its%20initial%20settings.%20All%20your%20data%20is%20destroyed%20in%20this%20process.%20*%E2%86%92%20The%20application%20ensures%20that%20a%20machine%20is%20allocated%20to%20only%20one%20person%20at%20a%20time,%20and%20VNC%20passwords%20are%20randomly%20generated%20for%20each%20session.%20Thus,%20even%20our%20administrators%20cannot%20see%20your%20test%20session.%20With%20respect%20to%20the%20plaintext%20passwords%20on%20the%20VMs,%20this%20is%20certainly%20not%20the%20case,%20as%20we%20moved%20to%20key-based%20authentication%20years%20ago.%20Moreover%20root%20login%20is%20disabled%20in%20our%20SSH%20configuration.%20Both%20the%20passwords%20mentioned,%20%E2%80%98nakula%E2%80%99%20and%20%E2%80%98c0stac0ff33%E2%80%99,%20were%20indeed%20in%20use%20a%20couple%20of%20years%20ago%20during%20our%20prototyping%20phase,%20and%20thus%20were%20present%20in%20the%20old%20prototype%20machine%20that%20was%20hacked.%20%E2%80%98nakula%E2%80%99%20was%C2%A0previously%20our%20VNC%20password,%20and%20was%20hashed.%20However,%20unlike%20the%20hash%20used%20for%20the%20user%20passwords,%20this%20hash%20is%20much%20weaker.%20This%20was%20due%20to%20a%20limitation%20in%20VNC%20protocol,%20and%20we%20had%20overcome%20this%20liability%20by%20regenerating%20a%20new%20password%20for%20every%20session,%20and%20thus%20%E2%80%98nakula%E2%80%99%20has%20not%20been%20in%20use%20for%20years.%20%E2%80%98c0stac0ff33%E2%80%99%20was%20one%20of%20our%20system%20user%20passwords%20on%20the%20prototype%20machine,%20before%20we%20moved%20to%20key-based%20authentication.%20It%20is%20true%20that%20we%20still%20run%20our%20VNC%20server%20on%20port%205901,%20but%20we%20do%20not%20believe%20that%20it%20is%20a%20security%20vulnerability%20because%20a%20current%20password%20is%20still%20required%20for%20access.%20As%20mentioned%20before,%20the%20passwords%20are%20changed%20every%20test%20session.%20*Where%20did%20we%20go%20wrong?*%20All%20our%20servers,%20running%20or%20not,%20whether%20in%20active%20use%20or%20not,%20should%20have%20been%20patched%20with%20the%20latest%20security%20upgrades%20and%20updates%20including%20the%20shellshock%20one.%20Moreover,%20servers%20not%20in%20active%20use%20should%20have%20been%20stopped%20[%E2%80%A6]&media=)
*   [__](https://archive.ph/o/rsmmS/https://www.linkedin.com/shareArticle?mini=true&url=https://www.databreaches.net/browserstack-analysis-unpatched-inactive-machine-compromised-by-shellshock-vulnerability/&title=BrowserStack%20analysis:%20unpatched%20inactive%20machine%20compromised%20by%20shellshock%20vulnerability&source=&summary=BrowserStack%20sent%20DataBreaches.net%20the%20following%20analysis,%20which%20is%20being%20emailed%20to%20all%20their%20users:%20As%20you%20may%20already%20know,%20BrowserStack%20experienced%20an%20attack%20on%209th%20November,%202014%20at%2023:30%20GMT%20during%20which%20an%20individual%20was%20able%20to%20gain%20unauthorized%20access%20to%20some%20of%20our%20users%E2%80%99%20registered%20email%20addresses.%20He%20then%20tried%20to%20send%20an%20email%20%3Chttp://pastebin.com/i788JT76%3E%20to%20all%20our%20registered%20users,%20but%20he%20was%20only%20able%20to%20reach%20less%20than%201%25%20(our%20estimate%20is%205,000%20users).%20The%20email%20contained%20inaccurate%20information,%20even%20claiming%C2%A0that%20BrowserStack%20would%20be%20shutting%20down.%20When%20we%20realized%20this,%20our%20only%20concern%20was%20to%20protect%20our%20users.%20This%20involved%20temporarily%20taking%20down%20the%20service,%20as%20we%20scrutinized%20each%20component%20carefully.%20This%20inconvenienced%20our%20users%20for%20several%20hours,%20and%20for%20that%20we%20are%20truly%20sorry.%20*What%20happened?*%20BrowserStack%20application%20servers%20run%20using%20Amazon%20Web%20Services.%20The%20configuration%20is%20vast,%20consisting%20of%20thousands%20of%20servers.%20One%20of%20these%20was%20an%20old%20prototype%20machine,%20which%20was%20the%20target%20of%20the%20breach.%20The%20machine%20had%20been%20running%20since%20before%202012,%20and%20was%20not%20in%20active%20use.%20It%20was%20penetrated%20using%20the%20shellshock%20vulnerability,%20and%20since%20it%20was%20no%20longer%20in%20active%20use,%20it%20did%20not%20have%20the%20appropriate%20patch%20installed.%20The%20old%20prototype%20machine%20had%20our%20AWS%20API%20access%20key%20and%20secret%20key.%20Once%20the%20hacker%20gained%20access%20to%20the%20keys,%20he%20created%20an%20IAM%20user,%20and%20generated%20a%20key-pair.%20He%20was%20then%20able%20to%20run%20an%20instance%20inside%20our%20AWS%20account%20using%20these%20credentials,%20and%20mount%20one%20of%20our%20backup%20disks.%20This%20backup%20was%20of%20one%20of%20our%20component%20services,%20used%20for%20production%20environment,%20and%20contained%20a%20config%20file%20with%20our%20database%20password.%20He%20also%20whitelisted%20his%20IP%20on%20our%20database%20security%20group,%20which%20is%20the%20AWS%20firewall.%20He%20began%20to%20copy%20one%20of%20our%20tables,%20which%20contained%20partial%20user%20information,%20including%20email%20IDs,%20hashed%20passwords,%20and%20last%20tested%20URL.%20His%20copy%20operation%20locked%20the%20database%20table,%20which%20raised%20alerts%20on%20our%C2%A0monitoring%20system.%20On%20receiving%20the%20alerts,%20we%20checked%20the%20logs,%20saw%20an%20unrecognized%20IP,%20and%20blocked%20it%20right%20away.%20In%20that%20time,%20the%20hacker%20had%20been%20able%20to%20retrieve%20only%20a%20portion%20of%20the%20data.%20Finally,%20using%20this%20data%20and%20the%20SES%20credentials,%20he%20was%20able%20to%20send%20an%20email%20to%20some%20of%20our%20users.%20*What%20was%20the%20extent%20of%20the%20damage?*%20Our%20database%20logs%20confirmed%20that%20user%20data%20was%20partially%20copied,%20but%20no%20user%20test%20history%20was%20compromised.%20Therefore%20all%20user%20data%20remains%20wholly%20intact.%20Most%20crucially,%20*credit%20card%20details%20were%20not%20compromised*,%20as%20we%20only%20store%20the%20last%204%20digits%20of%20the%20credit%20card%20number,%20and%20all%20payment%20processing%20takes%20place%20through%20our%20payment%20processing%20partner.%20All%20user%20passwords%20are%20salted,%20and%20encrypted%20with%20the%20powerful%20bcrypt%20algorithm,%20which%20creates%20an%20irreversible%20hash%20which%20cannot%20be%20cracked.%20However,%20as%20an%20added%20precaution,%20we%20suggest%20that%20users%20change%20their%20BrowserStack%20account%20passwords.%20We%20were%20able%20to%20verify%20the%20actions%20of%20the%20hacker%20using%20AWS%20CloudTrail,%20which%20confirmed%20that%20no%20other%20services%20were%20compromised,%20no%20other%20machines%20were%20booted,%20and%20our%20AMIs%20and%20other%20data%20stores%20were%20not%20copied.%20In%20addition,%20our%20production%20web%20server%20logs%20indicate%20that%20we%20were%20experiencing%20shellshock%20attempts,%20but%20they%20failed%20because%20the%20production%20web%20server%20has%20the%20necessary%20patches%20to%20foil%20all%20such%20attempts.%20*Points%20in%20the%20email*%20We%20would%20now%20like%20to%20address%20the%20points%20raised%20in%20the%20email.%20The%20hacker%20quoted%20three%20paragraphs%20from%20our%20Security%20documentation,%20as%20follows:%20%E2%80%93%20*after%20the%20restoration%20process%20is%20complete,%20the%20virtual%20machines%20are%20guaranteed%20to%20be%20tamper-proof.*%20%E2%86%92%20Our%20restoration%20process%20is%20indeed%20amper-proof.%20When%20we%20create%20a%20test%20machine%20from%20scratch,%20we%20take%20a%20snapshot.%20After%20every%20user%20session,%20the%20test%20machine%20is%20restored%20to%20it%20original%20state%20using%20that%20snapshot.%20Even%20if%20a%20previous%20user%20manages%20to%20install%20a%20malicious%20software,%20it%20is%20always%20erased%20due%20to%20the%20restoration%20process.%20%E2%80%93%20*The%20machines%20themselves%20are%20in%20a%20secure%20network,%20and%20behind%20strong%20firewalls%20to%20present%20the%20safest%20environment%20possible.*%E2%86%92%20Every%20single%20machine%20has%20an%20OS%20firewall,%20in%20addition%20to%20the%20hardware%20network%20firewalls%20we%20use.%20On%20EC2,%20we%20use%20security%20groups%20as%20an%20equivalent%20safety%20measure.%20We%20also%20use%20industry-standard%20brute%20force-throttling%20measures.%20%E2%80%93%20*At%20any%20given%20time,%20you%20have%20sole%20access%20to%20a%20virtual%20machine.%20Your%20testing%20session%20cannot%20be%20seen%20or%20accessed%20by%20other%20users,%20including%20BrowserStack%20administrators.%20Once%20you%20release%20a%20virtual%20machine,%20it%20is%20taken%20off%20the%20grid,%20and%20restored%20to%20its%20initial%20settings.%20All%20your%20data%20is%20destroyed%20in%20this%20process.%20*%E2%86%92%20The%20application%20ensures%20that%20a%20machine%20is%20allocated%20to%20only%20one%20person%20at%20a%20time,%20and%20VNC%20passwords%20are%20randomly%20generated%20for%20each%20session.%20Thus,%20even%20our%20administrators%20cannot%20see%20your%20test%20session.%20With%20respect%20to%20the%20plaintext%20passwords%20on%20the%20VMs,%20this%20is%20certainly%20not%20the%20case,%20as%20we%20moved%20to%20key-based%20authentication%20years%20ago.%20Moreover%20root%20login%20is%20disabled%20in%20our%20SSH%20configuration.%20Both%20the%20passwords%20mentioned,%20%E2%80%98nakula%E2%80%99%20and%20%E2%80%98c0stac0ff33%E2%80%99,%20were%20indeed%20in%20use%20a%20couple%20of%20years%20ago%20during%20our%20prototyping%20phase,%20and%20thus%20were%20present%20in%20the%20old%20prototype%20machine%20that%20was%20hacked.%20%E2%80%98nakula%E2%80%99%20was%C2%A0previously%20our%20VNC%20password,%20and%20was%20hashed.%20However,%20unlike%20the%20hash%20used%20for%20the%20user%20passwords,%20this%20hash%20is%20much%20weaker.%20This%20was%20due%20to%20a%20limitation%20in%20VNC%20protocol,%20and%20we%20had%20overcome%20this%20liability%20by%20regenerating%20a%20new%20password%20for%20every%20session,%20and%20thus%20%E2%80%98nakula%E2%80%99%20has%20not%20been%20in%20use%20for%20years.%20%E2%80%98c0stac0ff33%E2%80%99%20was%20one%20of%20our%20system%20user%20passwords%20on%20the%20prototype%20machine,%20before%20we%20moved%20to%20key-based%20authentication.%20It%20is%20true%20that%20we%20still%20run%20our%20VNC%20server%20on%20port%205901,%20but%20we%20do%20not%20believe%20that%20it%20is%20a%20security%20vulnerability%20because%20a%20current%20password%20is%20still%20required%20for%20access.%20As%20mentioned%20before,%20the%20passwords%20are%20changed%20every%20test%20session.%20*Where%20did%20we%20go%20wrong?*%20All%20our%20servers,%20running%20or%20not,%20whether%20in%20active%20use%20or%20not,%20should%20have%20been%20patched%20with%20the%20latest%20security%20upgrades%20and%20updates%20including%20the%20shellshock%20one.%20Moreover,%20servers%20not%20in%20active%20use%20should%20have%20been%20stopped%20[%E2%80%A6])
*   [__](https://archive.ph/o/rsmmS/www.reddit.com/submit/?url=https://www.databreaches.net/browserstack-analysis-unpatched-inactive-machine-compromised-by-shellshock-vulnerability/)
*   [__](https://archive.ph/o/rsmmS/https://www.databreaches.net/browserstack-analysis-unpatched-inactive-machine-compromised-by-shellshock-vulnerability/)

*   [Previous](https://archive.ph/o/rsmmS/https://www.databreaches.net/moving-toward-a-new-health-care-privacy-paradigm/)
*   [Next](https://archive.ph/o/rsmmS/https://www.databreaches.net/police-detail-alleged-theft-of-ids-by-former-umass-memorial-employee/)

### About the author: [Dissent](https://archive.ph/o/rsmmS/https://www.databreaches.net/ "Visit Dissent’s website")

Comments are closed.

## Browse by News Section

Browse by News Section 

## Latest News Stories

*   [DESORDEN leaks more data from Indonesia; “Indo data is officially worthless”](https://archive.ph/o/rsmmS/https://www.databreaches.net/desorden-leaks-more-data-from-indonesia-indo-data-is-officially-worthless/)
*   [Morgan Stanley to pay $35 million fee for ‘astonishing’ customer data disposal practices](https://archive.ph/o/rsmmS/https://www.databreaches.net/morgan-stanley-to-pay-35-million-fee-for-astonishing-customer-data-disposal-practices/)
*   [AU: ‘One of the most serious cyberattacks’: Customer data exposed in Optus hack](https://archive.ph/o/rsmmS/https://www.databreaches.net/au-one-of-the-most-serious-cyberattacks-customer-data-exposed-in-optus-hack/)
*   [Sierra College investigating scope of latest ransomware incident](https://archive.ph/o/rsmmS/https://www.databreaches.net/sierra-college-investigating-scope-of-latest-ransomware-incident/)
*   [Wolfe Clinic notifies patients of Eye Care Leaders breach](https://archive.ph/o/rsmmS/https://www.databreaches.net/wolfe-clinic-notifies-patients-of-eye-care-leaders-breach/)
*   [LockBit ransomware builder leaked online by “angry developer”](https://archive.ph/o/rsmmS/https://www.databreaches.net/lockbit-ransomware-builder-leaked-online-by-angry-developer/)
*   [ALPHV/BlackCat ransomware family becoming more dangerous](https://archive.ph/o/rsmmS/https://www.databreaches.net/alphv-blackcat-ransomware-family-becoming-more-dangerous/)
*   [SIM Swapper Abducted, Beaten, Held for $200k Ransom](https://archive.ph/o/rsmmS/https://www.databreaches.net/sim-swapper-abducted-beaten-held-for-200k-ransom/)
*   [UK: Six UK schools hit by cyberattack on multi-academy trust](https://archive.ph/o/rsmmS/https://www.databreaches.net/uk-six-uk-schools-hit-by-cyberattack-on-multi-academy-trust/)
*   [UK: Email blunder sees school send details of vulnerable children to all pupils](https://archive.ph/o/rsmmS/https://www.databreaches.net/uk-email-blunder-sees-school-send-details-of-vulnerable-children-to-all-pupils/)

Search for: 

## High Praise, Indeed!

“You translate “Nerd” into understandable “English” — Victor Gevers of GDI Foundation, talking about DataBreaches.net

## Please Donate

If you can, please donate XMR to our Monero wallet because the entities whose breaches we expose are definitely not supporting our work and are generally trying to chill our speech!

![Image 7: Donate- Scan QR Code](https://dgk1xndcng818h.archive.ph/rsmmS/b68729c0695972e862f4c769bfbc46b6ac9524b0.png)

45tom5wrGBrCyLAspSsBsnA7PjSLtyT3LG9RaKSszqJmF4yzq5DPknXJqWJ2tL2b5WddEhwVXWyWfRoRD6AfYGAFFxUidN8

## For Privacy News and Breaches

See my other site, [PogoWasRight.org](https://archive.ph/o/rsmmS/www.pogowasright.org/) Find me on [Twitter](https://archive.ph/o/rsmmS/https://twitter.com/PogoWasRight).

© 2009 – 2022, DataBreaches.net and DataBreaches LLC. All rights reserved. Do not republish or repost without written permission.

## Transparency Report

As of August 19, 2022 this site has not received any government requests for information on site visitors or those who provide information to this site. Read more [here](https://archive.ph/o/rsmmS/https://www.databreaches.net/transparency-reports/).

*   [__](https://archive.ph/o/rsmmS/https://twitter.com/PogoWasRight)
*   [__](mailto:info@databreaches.net)
*   [__](https://archive.ph/o/rsmmS/https://www.databreaches.net/feed/)

 Powered by [WordPress](https://archive.ph/o/rsmmS/wordpress.org/). Designed by [Magee Themes](https://archive.ph/o/rsmmS/www.mageewp.com/). 

![Image 8: Light](blob:https://dgk1xndcng818h.archive.ph/bc71f0b007213a1f48ae60a6aa11d11e)![Image 9: Dark](blob:https://dgk1xndcng818h.archive.ph/49a7b52e015d91457b6531ac625fcc5a)

 

[0%](https://archive.ph/rsmmS#0%)
[](https://archive.ph/rsmmS#5%)
[10%](https://archive.ph/rsmmS#10%)
[](https://archive.ph/rsmmS#15%)
[20%](https://archive.ph/rsmmS#20%)
[](https://archive.ph/rsmmS#25%)
[30%](https://archive.ph/rsmmS#30%)
[](https://archive.ph/rsmmS#35%)
[40%](https://archive.ph/rsmmS#40%)
[](https://archive.ph/rsmmS#45%)
[50%](https://archive.ph/rsmmS#50%)
[](https://archive.ph/rsmmS#55%)
[60%](https://archive.ph/rsmmS#60%)
[](https://archive.ph/rsmmS#65%)
[70%](https://archive.ph/rsmmS#70%)
[](https://archive.ph/rsmmS#75%)
[80%](https://archive.ph/rsmmS#80%)
[](https://archive.ph/rsmmS#85%)
[90%](https://archive.ph/rsmmS#90%)
[](https://archive.ph/rsmmS#95%)
[100%](https://archive.ph/rsmmS#100%)