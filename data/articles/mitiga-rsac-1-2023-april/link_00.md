Title: Please Read

URL Source: https://static.rainfocus.com/rsac/us23/sess/1664697541032001cak3/finalwebsite/2023_USA23_AIR-T02_01_It%E2%80%99s_Getting_Real__Hitting_the_Fan_2023_Edition_Real_World_SaaS_Attacks_1682607053333001zlzZ.pdf?_gl=1*trgj4t*_ga*MjAwODIwNzYxLjE2NzA0MzUzODQ.*_ga_Q3JZKF3KQM*MTY4MzYzODkzMS44My4xLjE2ODM2NDEwMTQuNTkuMC4w

Published Time: Thu, 27 Apr 2023 14:50:54 GMT

Number of Pages: 54

Markdown Content:
SESSION ID: 

> #RSAC

It ’s Getting Real & Hitting the Fan 

2023  Edition 

Real World SaaS Attacks 

> AIR -T02

OFER MAOR 

> CTO, Mitiga
> @OferMaor #RSAC

Disclaimer 

Presentations are intended for educational purposes only and do not replace independent professional 

judgment. Statements of fact and opinions expressed are those of the presenters individually and, 

unless expressly stated to the contrary, are not the opinion or position of RSA Conference ™ or any other 

co -sponsors. RSA Conference does not endorse or approve, and assumes no responsibility for, the 

content, accuracy or completeness of the information presented. 

Attendees should note that sessions may be audio - or video -recorded and may be published in various 

media, including print, audio and video formats without further notice. The presentation template and 

any media capture are subject to copyright protection.   

> ©2023 RSA Conference LLC or its affiliates. The RSA Conference logo and other trademarks are proprietary. All rights reserved.
> 2#RSAC

Speaker 

> 3

@OferMaor 

ofer@mitiga.io 

Linkedin.com /in/ ofermaor 

CTO & Co -Founder, Mitiga 

Over  25  Years in Cybersecurity 

Hacker at Heart 

CloudSec &  AppSec  (Daytime) 

Incident Response  (Nights & Weekends) 

Pioneer of IAST #RSAC 

About Mitiga 

4

Mitiga provides  next -gen  Cloud and SaaS 

incident response solutions  to simplify 

and accelerate investigation and recovery. 

Forensics Data 

& Automation 

Incident Command 

Center 

Fastest Time 

to Recovery 

Incident 

Readiness 

Breach Investigation  Faster 

than  Humanly Possible 

Continuous, Proactive 

Breach Investigation 

IR 2 ==  Zero Cost  Critical 

Incident Response #RSAC 

Introduction 

> 5

Today ’s

Talk:  Learn about SaaS breaches 

through real -world stories 

1

Realize how the right 

breach response can reduce 

impact and prevent loss 

2

Understand what you can today 

to become more resilient and 

be ready for breaches 

3

SaaS Breaches are here! 

Breaches are inevitable  World is moving to SaaS #RSAC 

## The Cost of Cloud (&SaaS) Breaches 

Source:  Cost of Data Breach Report  2022 , IBM #RSAC 

Breach Cost Continues to Rise  – 4.35 M$ 

7 

> Source: Cost of Data Breach Report 2022 , IBM

Average total cost of a data breach #RSAC 

Breac hes  Moving to Cloud & SaaS 

8 

> Source: Cost of Data Breach Report 2022 , IBM

What best 

describes your 

IT operating 

model? 

Did the data 

breach occur in 

the cloud? #RSAC 

Cloud Breaches Cost More! 

9

Average cost of a cloud -based data breach based on cloud model  

> Source: Cost of Data Breach Report 2022 , IBM #RSAC

It ’s Not Your First (or Last) Rodeo …

10 

Source: Cost of Data Breach Report  2022 , IBM 

Was this your 

first data 

breach? #RSAC 

## Identity Theft is King 

MFA ( 2FA)  is  dead !#RSAC 

Initial Attack Vector  – Identity >  33 %

12 

In  2022 , the most common initial attack 

vectors were compromised credentials 

at  19 % of breaches,  phishing  at  16 %

of breaches,  cloud misconfiguration 

at  15 % of breaches and  vulnerability in 

third -party software  at  13 % of breaches. 

The report saw the same order of the top 

four initial attack vectors.  

> Source: Cost of Data Breach Report 2022 , IBM #RSAC

The Death of MFA  – MFA Push Fatigue 

> 13 13 #RSAC

The Death of MFA  – Adversary in the Middle 

> 14
> Source: Microsoft #RSAC

## Phishing,  AiTM , BEC 

Incident # 1#RSAC 

BEC Leveraging AitM MFA Persisteny Campaign 

> 16
> Source: Tech Target #RSAC

Suspicious Email 

17 

Foobar  The company receiving the funds in the transaction 

Foobar  legal  The law firm representing  Foobar 

Buyer  The company conducting the transaction 

Buyer legal  The law firm of the Buyer #RSAC 

The BEC Scheme 

> 18 #RSAC

Incident Timeline 

19 

July  20 

July  21 -30 

Aug  1

Aug  1-2

Reconnaissance 

Persistence & Handoff 

Attack Execution 

• Creating  MFA  persistency  by  adding  authenticator 

• Transfering  credentials to US -based  team 

• Registration of fake domains for BEC 

• Logging in (US Team) to identify last email in thread 

• ”Reply To ” from fake domain with attempted bank change 

Initial Access  • DocuSign  phishing  email 

• Adversary  in  the  Middle MFA Circumvention (Singapore IP Address) 

• Session  transferred to another location (Dubai) 

• Browsing through  O365  – Outlook & Sharepoint 

• Identifying correspondance on an upcoming transaction #RSAC 

Phishing Email 

> 20

- Targeted!  CFO/CEO  only 

- Very well -crafted DocuSign 

- Leveraging recommended whitelisting for 

dse@docusign.net #RSAC 

Succesfull AiTM Phishing 

> 21 #RSAC

Creating new Authenticator 

> 22 #RSAC

No MFA Challenge Needed! 

23 

Accessing the 

security  portal 

Adding the 

authenticator !

No  MFA  check !

Previously  satisfied #RSAC 

## Multi -SaaS Ransomware 

Incident # 2#RSAC 

Initial Notification 

> 25

Anonymous Tip: 

You have been spear -phished! #RSAC 

Initial investigation discovers two fake login registrations 

okta -foobar.com  (Sep  27 )

foobar -okta.com  (Sep  28 )

Identifies one breached account, of a CSR, and blocks it 

Initial Investigation (by Customer) 

> 26

#RSAC 

Limited Containment? 

27 

585 GB+ 

nature of your business 

presence of a proficient security team 

Nope 

You didn ’t stop anything. 

We ’ve been in here for  24  hours #RSAC 

The Heat is On! 

28 

publication of the data on our leak site 

we are not an entity which is sanctioned by OFAC 

of third parties such as your employees, clients and majority shareholders. 

we may need to contact your family members to make our demands clear. 

inconvenience those present inside the exfiltrated data #RSAC 

Major Incident Declared 

How did 

they  get in ?

> 29

What data 

do  they have ?

What is still 

compromised ?#RSAC 

Initial Access  – Phishing , MFA Fatigue x  2

> 30

- MFA Fatigue ( 6 Total Attempts) 

- New MFA Device Registration 

- Hiding sign -in emails (mailbox rule) 

- Exfiltrating Data #RSAC 

All Your SaaS are Belong to Us 

> 31 #RSAC

What Exactly was Compromised? 

• Identifying SSO application access ( Forensics) 

• For each application (~ 15 ): 

– Identify available/relevant forensics data/logs 

– Establish a timeline of activities by attacker 

– Determine actual data exfiltrated 

• Create a full timeline and data exfiltration map 

> 32 #RSAC

What Exactly was Compromised? 

> 33

Prove theft of  20 GB vs  585 GB  claimed by attacker #RSAC 

Ransom (Extortion) Negotiations 

> 34

# $3,000,000 

# $250,000 

- Forensics Investigation 

- Negotiator 

- Executive Support #RSAC 

## GitHub Source Theft 

Incident # 3#RSAC 

Incident Timeline 

36 

January  9th 

January  11 th 

Threat Actor Abuse 

Containment  • Abnormal access to AWS identified 

• Keys blocked, then rotated (History stays forever in GitHub) 

Initial Comprommise  • Developer accidentally merges company git repo to personal one (public) 

• Two AWS keys exposed 

• Key obtained (timing unknown) 

• One of the AWS Keys used for initial reconnaissance #RSAC 

Response  – Investigate/Hunt 

• Identify access to compromised repo 

• Compare I Ps against known usage 

• Perform a Threat Hunt 

– Figure out what would an attacker do 

– Investigate forensics to refute 

– Determine next steps 

• Contain  – Disable/Rotate Keys 

> 37 #RSAC

## CI/CD SaaS Exposure 

The Circle/CI Breach #RSAC 

Circle CI Breach 

> 39 #RSAC

What is the Potential Damage? 

> 40 #RSAC

Investigating  CircleCI 

> 41

What to look for 

We recommend to check for action that 

could be abused by threat actors, such as: 

Access: 

- user.logged_in 

Persistence: 

- project.ssh_key.create 

- project.api_token.create 

- user.create #RSAC 

AWS Example 

42 

Search for events that the  CircleCI  user 

shouldn ’t be performing. For instance, 

suspicious reconnaissance actions, such as: 

• ListBuckets 

• GetCallerIdentity 

Search for  AccessDenied  Events 

Activity originating from devices: 

• IP address that was not observed 

before possibly from abnormal 

countries, Proxy providers or VPNs 

• Programmatic  UserAgents , such as 

boto 3 and  CURL 

1

2

3#RSAC 

## Public Resource Sharing 

## for AWS Data Exfiltration  

> Incident # 4(Cloud) #RSAC

Discovered via Threat Hunting 

> 44 #RSAC

Investigation Uncovers Additional Attacks 

> 45 #RSAC

Investigation & Response 

Initial Access Vector 

Investigation 

AccessKey has not been 

rotated for over  2 years! 

Insufficient log retention 

for root cause analysis 

> 46

Containment 

& Eradication 

Rotation of AccessKey 

Removal of all public AMIs 

created by  threat  actor 

Investigation of content 

in shared AMIs 

Impact  – Minimal 

No substantial data 

has been leaked #RSAC 

## Preparing for SaaS Incidents 

(Cloud ones too …)#RSAC 

So,  What Can We Do? 

48 

SaaS Breaches are here! 

Breaches are inevitable  World is moving to SaaS 

Turn on and start collecting logs 

& forensics from critical SaaS apps, 

including Productivity Suites & IDPs. 

1 2 3

Collect Data  Prepare  Reduce TTR 

Create the right plans, tools, capabilities 

and team, to be ready to deal with 

SaaS breaches when they occur. 

Perform both proactive and 

reactive forensics investigation 

of SaaS apps logs and incidents. #RSAC 

Collect Forensics SaaS (& Cloud) Data 

> 49

Productivity Suites Identity Providers 

SaaS Apps Cloud Service Providers #RSAC 

Prepare an IR Team 

50 

Source: Cost of Data Breach Report  2022 , IBM 

Average cost of a data breach with incident 

response (IR) team and IR plan testing 

Impact of XDR technologies on 

average cost of a data breach #RSAC 

Reduce Time to Recover 

51 

Source: Cost of Data Breach Report  2022 , IBM 

Average cost of a data breach based on data breach lifecycle 

Average time to identify 

and contain a data breach #RSAC 

Cloud Sec Maturity  → Time to Recover 

52 

Source: Cost of Data Breach Report  2022 , IBM 

State of security maturity in the cloud environment  Average time to identify and contain a data 

breach by cloud security maturity level #RSAC 

Apply What You Learned Today! 

> 53

1

Next Week: 

Understand Your 

SaaS Exposure 

Identify your critical SaaS apps 

Assess the scope of your 

productivity suite 

Assess the breadth 

of your IDP & SSO 

Next Month: 

Build Your Forensics 

Data Readiness 

Identify available 

forensics data 

Start collecting data 

(Data Lake / SIEM / etc.) 

Map missing 

forensics data 

And Then …

Don ’t Stop There! 

Finalize data collection 

Develop playbooks, skills 

and automation for critical 

apps investigation 

Perform threat hunting on IDP 

and critical SaaS assets 

2 3SESSION ID: 

> #RSAC

Thank You! 

Q&A 

AIR -T02 

OFER MAOR 

CTO, Mitiga 

@OferMaor