---
title: Booking management platform FlexBooker leaks 3.7 million user records
url: "https://therecord.media/booking-management-platform-flexbooker-leaks-3-7-million-user-records/"
author: Catalin Cimpanu
published: 2022-01-06
source_type: article
source_domain: therecord.media
cleanup_method: llm
---

[Catalin Cimpanu](https://therecord.media/author/catalin-cimpanu)January 6th, 2022

# Booking management platform FlexBooker leaks 3.7 million user records

[FlexBooker](https://www.flexbooker.com/), a company that provides a cloud-based online scheduling and booking service, has exposed the personal details of more than 3.7 million users.

The incident took place in December 2021 after a threat actor compromised one of the company's Amazon Web Services (AWS) accounts, according to Australian security researcher Troy Hunt.

The threat actor used the account to collect 9.5 million records from the company's AWS infrastructure, data that was eventually leaked online on a forum dedicated to trading hacked data.

Hunt, who operates Have I Been Pwned, a service that indexes hacked data, said that he received a copy of the stolen files, which turned out to contain information on more than 3.7 million unique users.

> New breach: Online booking service FlexBooker had 3.7M accounts breached last month. Data included email addresses, names, phone numbers and for some accounts, partial credit card data. 69% were already in [@haveibeenpwned](https://twitter.com/haveibeenpwned?ref_src=twsrc%5Etfw)[https://t.co/LGaAnj1hUA](https://t.co/LGaAnj1hUA)
> 
> — Have I Been Pwned (@haveibeenpwned) [January 6, 2022](https://twitter.com/haveibeenpwned/status/1478980347631001602?ref_src=twsrc%5Etfw)

According to Hunt, this data contained real names, email addresses, phone numbers, and for a small number of accounts, password hashes and partial credit card information.

These users are most likely unaware that their data was leaked online. Affected users are persons who made online reservations on the websites of doctors, accountants, barbers, mechanics, and others, all of whom used FlexBooker's services to manage online bookings.

Hunt's Have I Been Pwned service is currently sending emails with a notification about the exposure to all those who had an email address included in the leak.

A FlexBooker spokesperson did not return a request for comment.

This is the second major breach that Hunt has added to his Have I Been Pwned service this week after the Aussie researcher also indexed 7.5 million user records that leaked from music[mixtape service DatPiff](https://twitter.com/haveibeenpwned/status/1478273588402659330). The DatPiff data also leaked last month, on the same forum as the FlexBooker breach.
