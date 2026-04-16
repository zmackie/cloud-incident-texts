---
title: Indian grocery startup KiranaPro was hacked and its servers deleted, CEO confirms
url: "https://techcrunch.com/2025/06/03/indian-grocery-startup-kiranapro-was-hacked-and-its-servers-deleted-ceo-confirms/"
author: Jagmeet Singh
published: 2025-06-03
source_type: article
source_domain: techcrunch.com
cleanup_method: llm
---

# Indian grocery startup KiranaPro was hacked and its servers deleted, CEO confirms

[Jagmeet Singh](https://techcrunch.com/author/jagmeet-singh/)

8:46 AM PDT · June 3, 2025


Indian grocery delivery startup [KiranaPro](https://www.kirana.pro/) has been hacked and all its data has been wiped, the company’s founder confirmed to TechCrunch.

The destroyed data included the company’s app code and its servers containing banks of sensitive customer information, including their names, mailing addresses, and payment details, KiranaPro co-founder and CEO Deepak Ravindran told TechCrunch.

The company’s app is online but cannot process orders, TechCrunch has found.

Launched in December 2024, KiranaPro operates as a buyer app on the [Indian government’s Open Network for Digital Commerce](https://techcrunch.com/2024/08/22/indias-open-commerce-network-expands-into-digital-lending/), allowing customers to purchase groceries from their local shops and nearby supermarkets.

KiranaPro has 55,000 customers, with 30,000-35,000 active buyers across 50 cities, who collectively place 2,000 orders daily, according to the company. Unlike a typical grocery delivery app, KiranaPro offers a voice-based interface that allows users to place orders from local shops using voice commands in languages such as Hindi, Tamil, Malayalam, and English.

The startup planned to expand to 100 cities in the next 100 days before the incident happened, Ravindran said.

On May 26, KiranaPro executives became aware of the incident while logging into their Amazon Web Services account. Hackers gained access to KiranaPro’s root accounts on AWS and GitHub, Ravindran told TechCrunch.

Ravindran shared a couple of screenshots of the GitHub security logs and a file containing a sample of activity logs around the time of the incident, suggesting that the hacking happened after someone gained access to their systems via a former employee’s account.

KiranaPro’s chief technology officer Saurav Kumar told TechCrunch that the hack happened around May 24-25.

The startup said it used Google Authenticator for multi-factor authentication on its AWS account. Kumar told TechCrunch that the multi-factor code had changed when they tried to log into their AWS account last week, and all their Electric Compute Cloud (EC2) services, which let clients access virtual computers to run their applications, were deleted.

“We can only log in through the IAM [Identity and Access Management] account, through which we can see that the EC2 instances don’t exist anymore, but we are not able to get any logs or anything because we don’t have the root account,” he said.

KiranaPro has reached out to GitHub’s support team to help identify the hacker’s IP addresses and other traces of the incident, said Ravindran.

Similarly, Ravindran told TechCrunch that the startup is filing cases against its former employees, who he said had not submitted their credentials for accessing their GitHub accounts to check their logs.

It is unclear how the attack happened. Some of the biggest cyberattacks in recent years, such as [LastPass](https://techcrunch.com/2022/12/22/lastpass-customer-password-vaults-stolen/), [Change Healthcare](https://techcrunch.com/2024/06/21/change-healthcare-confirms-ransomware-hackers-stole-medical-records-on-a-substantial-proportion-of-americans/), and [Snowflake](https://techcrunch.com/2024/06/07/snowflake-ticketmaster-lendingtree-customer-data-breach/), were caused by credential theft, such as through [password-stealing malware](https://techcrunch.com/2025/01/31/techcrunch-reference-guide-to-security-terminology/#infostealers) installed on an employee’s laptop, and missing or unenforced multi-factor authentication.

The companies were ultimately responsible for enforcing the security of their own systems, including whether their employees must use multi-factor authentication, and terminating accounts of former employees who no longer work at their company.

KiranaPro counts Blume Ventures, Unpopular Ventures, and Turbostart among its institutional venture backers, as well as Olympic medalist PV Sindhu and BCG MD Vikas Taneja among its angel investors. The company has a team of 15 employees located in Bengaluru and Kerala.
