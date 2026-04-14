GotRoot! AWS root Account Takeover
This write-up details how I was able to escalate privileges to the Nature’s Basket AWS root account starting as an unauthenticated user.
TL;DR
Give me a quick description please!
What was the vulnerability?
Public S3 bucket leaking sensitive configuration files with hardcoded access credentials.
What was the attack path?
Unauthenticated User to Cloud Root Account Takeover:
Open S3 bucket -> Server backend code -> Hardcoded AWS keys in configuration file -> GotRoot!
Was users personal data breached?
The AWS root account had complete access over all of NB’s cloud assets including EC2 instances, RDS instances, databases, S3 buckets, etc. where users personal data may have been stored. So there is a chance of data breach if this has been exploited by an attacker previously.
Attack Path
Interesting, details please!
Step 1: Google dorks revealed Natures basket’s “gnbdevcdn” open bucket:
Step 2: gnbdevcdn bucket was found to be world readable. A quick search revealed hardcoded credentials and AWS access keys:
Step 3: Gathered credentials were enumerated for permissions. First user account “gnbrobosoft” found with limited access.
Step 4: GotRoot!! Second gathered credentials found with root user access:
Step 5: An audit user account was set-up and access to the console was verified.
Attack success! From Unauthenticated user to Complete Cloud Account Takeover.
Bonus!
Created a map showing some of Natures Basket’s cloud resources using cloudmapper:
Thanks for reading!
Disclosure timeline
[+] 12 July 2020: Issue first reported to Natures Basket (NB) team with detailed report
[+] 15 July 2020: Request for updates. NB team asks to re-share the details, re-shared
[+] 16 July 2020: Update from NB team, issue being verified
[+] 25 July 2020: Request for updates. No reply received.
[…] Access restricted for some of the sensitive files
[+] 22 August 2020: Request for updates. Informed NB team about my intention for public disclosure.
[+] 25 August 2020: Report disclosure