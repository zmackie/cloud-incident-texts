---
title: Otelier data breach exposes info, hotel reservations of millions
url: "https://www.bleepingcomputer.com/news/security/otelier-data-breach-exposes-info-hotel-reservations-of-millions/"
author: Lawrence Abrams
published: 2025-01-17
source_type: article
source_domain: www.bleepingcomputer.com
cleanup_method: llm
---

# Otelier data breach exposes info, hotel reservations of millions


# Otelier data breach exposes info, hotel reservations of millions

 By 
###### [Lawrence Abrams](https://www.bleepingcomputer.com/author/lawrence-abrams/)

*   January 17, 2025
*   03:17 PM


Hotel management platform Otelier suffered a data breach after threat actors breached its Amazon S3 cloud storage to steal millions of guests' personal information and reservations for well-known hotel brands like Marriott, Hilton, and Hyatt.

The breach first allegedly occurred in July 2024, with continued access through October, with the threat actors claiming to have stolen amost eight terabytes of data from Otelier's Amazon AWS S3 buckets.

In a statement to BleepingComputer, Otelier confirmed the compromise and said it is communicating with impacted customers.


"Our top priority is to safeguard our customers while enhancing the security of our systems to prevent future issues," Otelier told BleepingComputer.

"Otelier has been in communications with its customers whose information was potentially involved. In response to this incident, we hired a team of leading cybersecurity experts to perform a comprehensive forensic analysis and validate our systems."

"The investigation determined that the unauthorized access was terminated. In order to help prevent a similar incident from occurring in the future, Otelier disabled the involved accounts and continues to work to enhance its cybersecurity protocols."

Otelier, previously known as MyDigitalOffice,is a cloud-based hotel management solution used by over 10,000 hotels worldwide to manage reservations, transactions, nightly reports, and invoicing.

The company is or has been used by many well-known hotel brands, including Marriott, Hilton, and Hyatt, whose data is present in the stolen information.

## Breached through stolen credentials

The threat actors behind the Otelier breach told BleepingComputer that they initially hacked the company's Atlassian server using an employee's login. These credentials were stolen through[information-stealing malware,](https://www.bleepingcomputer.com/news/security/global-infostealer-malware-operation-targets-crypto-users-gamers/)which has become the bane of corporate networks over the past few years.

When BleepingComputer asked Otelier to confirm this information, a company representative said they could not share any further comments on the incident. However, BleepingComputer found on the[Flare threat intelligence platform](https://flare.io/)Otelier employee information that had been stolen by infostealer malware.

The threat actors say they used these credentials to scrape tickets and other data, which contained further credentials to the company's S3 buckets.

Using this access, the hackers claimed to have downloaded 7.8TB of data from the company's Amazon cloud storage, including millions of documents belonging to Marriott that were in S3 buckets managed by Otelier. These documents include nightly hotel reports, shift audits, and accounting data.

Marriott has confirmed to BleepingComputer that Otelier's cyberattack has impacted them and suspended automated services while Otelier completes its investigation. The company stresses that none of its systems were breached in this attack.

"Once we were made aware of this incident involving Otelier, we immediately contacted the vendor, which works with numerous hotel companies, and confirmed that they were working with cyber security experts to investigate a security incident that impacted their systems," a Marriott spokesperson told BleepingComputer.

"Marriott has also taken appropriate precautions, including suspending the automated services provided by Otelier until the completion of their investigation, and those services remain suspended."

The threat actor says they attempted to extort Marriott, thinking the S3 buckets belonged to them, and left ransom notes requesting payment in cryptocurrency not to leak the data. However, no communication was made, and they said they lost access in September after credentials were rotated.

While Marriott told BleepingComputer that there are no indications that sensitive information was stolen in the breach, samples of the stolen data shared with BleepingComputer and Have I Been Pwned's Troy Hunt contain hotel guests' personal information.

The small samples seen by BleepingComputer include a broad range of data, including hotel guest reservations, transactions, employee emails, and other internal data.

Some of the personal information exposed includes hotel guests' names, addresses, phone numbers, and email addresses.

The stolen data also includes information and email addresses related to Hyatt, Hilton, and Wyndham. BleepingComputer contacted Hyatt and Hilton about the breach but did not receive a response.

Troy Hunt told BleepingComputer that he received an extensive set of data, with the reservations table containing 39 million rows and a users table with 212 million.

Hunt says that despite the large set, he found 1.3 million unique email addresses, as many are repeated.

The exposed personal information is being added to [Have I Been Pwned](https://haveibeenpwned.com/), allowing anyone to check if their email address is in the exposed data. Hunt removed email addresses generated by Booking.com and Expedia.com during reservations, leaving a total of 437,000 unique email addresses impacted by the breach.

The good news is that passwords and billing information do not appear to have been stolen in the attack, but threat actors could still use this information in targeted phishing attacks.

Therefore, you should be on the lookout for suspicious emails impersonating hotel brands impacted by this breach.

_Update 1/19/24: Added more information about it being added to Have I Been Pwned._
