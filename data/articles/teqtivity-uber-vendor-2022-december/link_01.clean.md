---
title: Uber suffers new data breach after attack on vendor, info leaked online
url: "https://www.bleepingcomputer.com/news/security/uber-suffers-new-data-breach-after-attack-on-vendor-info-leaked-online/"
author: Lawrence Abrams
published: 2022-12-12
source_type: article
source_domain: www.bleepingcomputer.com
cleanup_method: llm
---

# Uber suffers new data breach after attack on vendor, info leaked online


# Uber suffers new data breach after attack on vendor, info leaked online

 By 
###### [Lawrence Abrams](https://www.bleepingcomputer.com/author/lawrence-abrams/)

*   December 12, 2022
*   01:30 PM

![Image 35: Uber security incident](https://www.bleepstatic.com/content/hl-images/2022/09/16/Uber-bkg.jpg)

_Update below: Uber shared further information with BleepingComputer on how its data was stolen in a breach on Teqtivity, which provides asset management and tracking services for the company.

 Added statement from TripActions, who said their data was not exposed._

Uber has suffered a new data breach after a threat actor leaked employee email addresses, corporate reports, and IT asset information stolen from a third-party vendor in a cybersecurity incident.

Early Saturday morning, a threat actor named 'UberLeaks' began leaking data they claimed was stolen from Uber and Uber Eats on a hacking forum known for publishing data breaches.


The leaked data includes numerous archives claiming to be source code associated with mobile device management platforms (MDM) used by Uber and Uber Eats and third-party vendor services.

The threat actor created four separate topics, allegedly for Uber MDM at uberhub.uberinternal.com and Uber Eats MDM, and the third-party Teqtivity MDM and TripActions MDM platforms.

![Image 37: Uber data leaked on a hacking forum](https://www.bleepstatic.com/images/news/security/d/data-breaches/u/uber/third-party-vendor/forum-post.jpg)

**Uber data leaked on a hacking forum**

_Source: BleepingComputer_

Each post refers to a member of the Lapsus$ hacking group who is believed to be responsible for numerous high-profile attacks, including a[September cyberattack on Uber](https://www.bleepingcomputer.com/news/security/uber-hacked-internal-systems-breached-and-vulnerability-reports-stolen/)where threat actors gained access to the internal network and the company's Slack server.

BleepingComputer has been told that the newly leaked data consists of source code, IT asset management reports, data destruction reports, Windows domain login names and email addresses, and other corporate information.

One of the documents seen by BleepingComputer includes email addresses and Windows Active Directory information for over 77,000 Uber employees.

While BleepingComputer initially thought this data was stolen during the September attack, Uber told BleepingComputer it believes it is related to a security breach on a third-party vendor.

“We believe these files are related to an incident at a third-party vendor and are unrelated to our security incident in September. Based on our initial review of the information available, the code is not owned by Uber; however, we are continuing to look into this matter.” - Uber.

Security researchers who have analyzed the leak told BleepingComputer that the leaked data is related to internal Uber corporate information and does not include any of its customers.

However, we are told that the leaked data contains enough detailed information to conduct targeted phishing attacks on Uber employees to acquire more sensitive information, such as login credentials.

Therefore, all Uber employees should be on the lookout for phishing emails impersonating Uber IT support and confirm all information directly with IT admins before responding to such emails.

BleepingComputer has reached out to Uber, TripActions, and Teqtivity with further questions regarding the incident but has not received a reply at this time.

## Uber data was stolen in Teqtivity breach

Following the publishing of this story, Uber has shared that threat actors stole its data in a recent breach on Teqtivity, which it uses for asset management and tracking services.

Uber referred us to a[Teqtivity data breach notification](https://www.teqtivity.com/breach-notification-statement/)published this afternoon, which explains that a threat actor gained access to a Teqtivity AWS backup server that stores data for its customers.

This allowed the threat actor to access the following information for companies using their platform.

*   Device information: Serial Number, Make, Models, Technical Specs
*   User Information: First Name, Last Name, Work Email Address, Work Location details

Uber told BleepingComputer that the source code leaked on the hacking forum was created by Teqtivity to manage Uber's services, explaining the many references to the ride-sharing company.

Uber has also reiterated that the Lapsus$ group was not related to this breach, even though the forum posts reference one of the threat actors associated with the group.

While the forum posts state that they breached 'uberinternal.com,' Uber has said that they have not seen any malicious access to their systems.

"The third-party is still investigating but has confirmed that the data we've seen to date came from its systems, and to date we have not seen any malicious access to Uber Internal systems," Uber told BleepingComputer.

## Update: TripActions data not exposed

TripActions told BleepingComputer that they have investigated the incident and no corporate or customer data was exposed during the attack on Teqtivity.

The full statement can be read below:

"On December 12, 2022, TripActions learned of a [security incident](https://www.teqtivity.com/breach-notification-statement/)involving Teqtivity, a third-party vendor.

Following investigations by both TripActions and Teqtivity, it has been determined that no TripActions data was exposed as part of this security incident nor were TripActions customers impacted as part of this security incident. TripActions does not maintain an MDM. We will continue to monitor the situation." - TripActions.

_Update 12/12/22: Added further information from Uber about the Teqtivity breach.

 Update 12/13/22: Added statement from TripActions._
