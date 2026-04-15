---
title: LexisNexis confirms data breach at Legal & Professional arm, some customer records affected
url: "https://www.theregister.com/2026/03/04/lexisnexis_legal_professional_confirms_data/"
author: Connor Jones
published: 2026-03-04
source_type: article
source_domain: www.theregister.com
cleanup_method: llm
---

#### [Cyber-crime](https://www.theregister.com/security/cyber_crime/)
# LexisNexis confirms data breach at Legal & Professional arm, some customer records affected
## Crooks claim 2 GB haul from AWS instance via React2Shell exploit

![Image 11: icon](https://www.theregister.com/design_picker/d518b499f8a6e2c65d4d8c49aca8299d54b03012/graphics/icon/vulture_red.svg)[Connor Jones](https://www.theregister.com/Author/Connor-Jones "Read more by this author")

 Wed 4 Mar 2026  //  16:04 UTC 

Data analytics giant LexisNexis has confirmed its Legal & Professional division suffered a data breach days after the Fulcrumsec cybercrime crew claimed responsibility for the hack.

Following an investigation, LexisNexis told _The Register_ the matter is now contained, and that neither its products nor its services were ever compromised, although the company was forced to bring in a third-party digital forensics crew to manage the cleanup.

A spokesperson said only "a limited number of servers" were accessed, and the data stored on them was "mostly legacy, deprecated data from prior to 2020."

This included customer names, user IDs, business contact information, products used, customer surveys with respondent IP addresses, and support tickets.

"The impacted information did not contain Social Security numbers, driver's license numbers, or any other sensitive personally identifiable information; credit card, bank accounts, or any other financial information; active passwords; or customer search queries, customer client or matter information, or customer contracts," the spokesperson added.

"We take our responsibility to safeguard customer information extremely seriously and have informed impacted current and previous customers of this matter. We are continuing to investigate and have implemented containment and remediation steps, in coordination with our expert cybersecurity forensic firm."

LexisNexis did not comment on the scale of the breach, although Fulcrumsec offered its take on this amid efforts to publicly shame the company.

Per the criminals' listing, which claims to contain a little more than 2 GB of company data, Fulcrumsec reckons it exfiltrated the files from a LexisNexis AWS instance by exploiting a vulnerable React container - specifically, an unpatched [React2Shell vulnerability](https://www.theregister.com/2025/12/18/react2shell_exploitation_spreads_as_microsoft/).

The listing claims the data dump includes 400,000 cloud user profiles, complete with personally identifiable information (PII) points, including names, emails, and phone numbers.This is unverified. It also claims more than 118 appeared to belong to US government staff, including federal judges, DoJ attorneys, SEC staff, and court clerks.

*   [Turns out most cybercriminals are old enough to know better](https://www.theregister.com/2026/03/03/turns_out_most_cybercriminals_are/)
*   [Cybercriminals swipe 15.8M medical records from French doctors ministry](https://www.theregister.com/2026/03/03/french_medical_leak/)
*   [Ransomware crims forced to take off-RAMP as FBI seizes forum](https://www.theregister.com/2026/01/28/fbi_seizes_ramp_forum/)
*   [Death, torture, and amputation: How cybercrime shook the world in 2025](https://www.theregister.com/2025/12/28/death_torture_and_amputation_how/)

Among the other files are 17 VPC databases and more than 430 VPC database tables, 536 Redshift tables, 3.9 million database records, and 53 secrets swiped from AWS Secrets Manager, Fulcrumsec claims.

The cyber crew alleges it leaked more than 21,000 customer account records belonging to government agencies, insurance companies, law firms, and universities.

Further, it claims more than 300,000 records included in the dump pertain to customer contracts, revealing which products individual organizations pay for, the associated renewal dates, and pricing tiers.

"This is the complete commercial relationship database," Fulcrumsec wrote. "If you wanted to know exactly what Gibson Dunn pays for Lexis Advance, or what the SEC subscribes to, or which Newsdesk package the Ellen MacArthur Foundation uses – it is all here."

As always, criminals' assertions should be taken with a pitch of salt. ®
