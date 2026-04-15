---
title: Education giant Pearson hit by cyberattack exposing customer data
url: "https://www.bleepingcomputer.com/news/security/education-giant-pearson-hit-by-cyberattack-exposing-customer-data/"
author: Lawrence Abrams
published: 2025-05-08
source_type: article
source_domain: www.bleepingcomputer.com
cleanup_method: llm
---

# Education giant Pearson hit by cyberattack exposing customer data


# Education giant Pearson hit by cyberattack exposing customer data

 By 
###### [Lawrence Abrams](https://www.bleepingcomputer.com/author/lawrence-abrams/)

*   May 8, 2025
*   04:14 PM


Education giant Pearson suffered a cyberattack, allowing threat actors to steal corporate data and customer information, BleepingComputer has learned.

Pearson is a UK-based education company and one of the world’s largest providers of academic publishing, digital learning tools, and standardized assessments. The company works with schools, universities, and individuals in over 70 countries through its print and online services.

In a statement to BleepingComputer, Pearson confirmed they suffered a cyberattack and that data was stolen, but stated it was mostly "legacy data."


"We recently discovered that an unauthorized actor gained access to a portion of our systems," a Pearson representative confirmed to BleepingComputer.

"Once we identified the activity, we took steps to stop it and investigate what happened and what data was affected with forensics experts. We also supported law enforcement's investigation. We have taken steps to deploy additional safeguards onto our systems, including enhancing security monitoring and authentication."

"We are continuing to investigate, but at this time we believe the actor downloaded largely legacy data. We will be sharing additional information directly with customers and partners as appropriate."

Pearson also confirmed that the stolen data did not include employee information.


## An exposed GitLab token

This statement comes after sources told BleepingComputer that threat actors compromised Pearson's developer environment in January 2025 through an exposed GitLab Personal Access Token (PAT) found in a public .git/config file.

A .git/config file is a local configuration file used by Git projects to store configuration settings, such as a project name, email address, and other information. If this file is mistakenly exposed and contains access tokens embedded in remote URLs, it can give attackers unauthorized access to internal repositories.

In the attack on Pearson, the exposed token allowed the threat actors to access the company's source code, which contained further hard-coded credentials and authentication tokens for cloud platforms.

Over the following months, the threat actor reportedly used these credentials to steal terabytes of data from the company's internal network and cloud infrastructure, including AWS, Google Cloud, and various cloud-based database services such as Snowflake and Salesforce CRM.

This stolen data allegedly contains customer information, financials, support tickets, and source code, with millions of people impacted.

However, when BleepingComputer asked Pearson about whether they paid a ransom, what they meant by "legacy data," how many customers were impacted, and if customers would be notified, the company responded that they would not be commenting on these questions.

Pearson [previously disclosed](https://plc.pearson.com/en-GB/news-and-insights/news/cyber-security-incident-involving-pdri)in January that they were investigating a breach of one of their subsidiaries, PDRI, which is believed to be related to this attack.

Scanning for Git configuration files and exposed credentials has become a common method for threat actors to breach cloud services.

Last year,[Internet Archive was breached](https://www.bleepingcomputer.com/news/security/internet-archive-hacked-data-breach-impacts-31-million-users/) after threat actors discovered an [exposed Git configuration file](https://www.bleepingcomputer.com/news/security/internet-archive-breached-again-through-stolen-access-tokens/) containing an authentication token for the company's GitLab repositories.

For this reason, it is critical to secure ".git/config" files by preventing public access and to avoid embedding credentials in remote URLs.
