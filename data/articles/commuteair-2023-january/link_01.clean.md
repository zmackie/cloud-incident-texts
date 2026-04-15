---
title: "EXCLUSIVE: U.S. airline accidentally exposes 'No Fly List' on unsecured server"
url: "https://www.dailydot.com/debug/no-fly-list-us-tsa-unprotected-server-commuteair/"
author: Mikael Thalen
published: 2023-01-19
source_type: article
source_domain: www.dailydot.com
cleanup_method: llm
---

# EXCLUSIVE: U.S. airline accidentally exposes ‘No Fly List’ on unsecured server

By [Mikael Thalen](https://www.dailydot.com/author/mikael-thalen)

3:43 PM CST on January 19, 2023

![Image 4: leaked tsa no fly list](https://lede-admin.dailydot.com/wp-content/uploads/sites/69/2023/01/tsa2.jpg?w=2880)

[trekandshoot/Shutterstock](https://www.shutterstock.com/image-photo/los-angeles-california-march-24-suitcase-186375977)

An unsecured server discovered by a security researcher last week contained the identities of hundreds of thousands of individuals from the U.S. government’s Terrorist Screening Database and “No Fly List.”


Located by the Swiss hacker known as maia arson crimew, the server, run by the U.S. national airline CommuteAir, was left exposed on the public internet. It revealed a vast amount of company data, including private information on almost 1,000 CommuteAir employees.

Analysis of the server resulted in the discovery of a text file named “NoFly.csv,” a reference to the subset of individuals in the Terrorist Screening Database who have been barred from air travel due to having suspected or known ties to terrorist organizations.

The list, according to crimew, appeared to have more than 1.5 million entries in total. The data included names as well as birth dates. It also included multiple aliases, placing the number of unique individuals at far less than 1.5 million.

On the list were several notable figures, including the recently freed Russian arms dealer Viktor Bout, alongside over 16 potential aliases for him.

The aliases comprised different, common misspellings of his last name and other versions of his first name, as well as different birthdays. Many of the birthdays aligned with the recorded date Bout was born.

Suspected members of the IRA, the Irish paramilitary organization, were also on the list.

Another individual, according to crimew, was listed as 8 years old based on their birth year.

Many entries on the list were names that appeared to be of Arabic or Middle Eastern descent, although Hispanic and Anglican-sounding names were also on the list. Numerous names included aliases that were common misspellings or slightly altered versions of their names.

"It's just crazy to me how big that Terrorism Screening Database is and yet there is still very clear trends towards almost exclusively Arabic and Russian sounding names throughout the million entries,” crimew said.

“Over last 20 years, the U.S. citizens that we’ve seen targeted for watchlisting are disproportionately Muslim and people of Arab or Middle Eastern and South Asian descent,” said Hina Shamsi, director of the National Security Project at the American Civil Liberties (ACLU).“Sometimes it’s people who dissent or have what are seen as unpopular views. We’ve also seen journalists watchlisted.”

In a statement to the Daily Dot, TSA said that it was “aware of a potential cybersecurity incident with CommuteAir, and we are investigating in coordination with our federal partners.”

The FBI declined to answer specific questions about the list to the Daily Dot.

In a statement to the Daily Dot, CommuteAir said that the exposed infrastructure, which it described as a development server, was used for testing purposes.

CommuteAir added that the server, which was taken offline prior to publication after being flagged by the Daily Dot, did not expose any customer information based on an initial investigation.

CommuteAir also confirmed the legitimacy of the data, stating that it was a version of the “federal no-fly list” from roughly four years prior.

“The server contained data from a 2019 version of the federal no-fly list that included first and last names and dates of birth,” CommuteAir Corporate Communications Manager Erik Kane said. “In addition, certain CommuteAir employee and flight information was accessible. We have submitted notification to the Cybersecurity and Infrastructure Security Agency and we are continuing with a full investigation.”

CommuteAir is a regional airline based out of Ohio. In June 2020, CommuteAir replaced ExpressJet as the carrier for its United Express Banner, a regional branch of United, which runs shorter flights.

In remarks to the Daily Dot, crimew said that they had made the discovery while searching for Jenkins servers on the specialized search engine Shodan. Jenkins provides automation servers that aid in the building, testing, and deployment of software. Shodan is used throughout the cybersecurity community to locate servers exposed to the open internet.

The server also held the passport numbers, addresses, and phone numbers of roughly 900 company employees. User credentials to more than 40 Amazon S3 buckets and servers run by CommuteAir were also exposed, said crimew.

The Terrorism Screening Database, according to the FBI, is a list of individuals shared across government departments to prevent the kind of intelligence lapses that occurred prior to 9/11. Within that is the smaller, more tightly controlled No Fly List. Individuals in the Terrorism Screening Database can be subject to certain restrictions and given additional security screening.Individuals explicitly on the No Fly List are barred from boarding aircraft in the United States.

“This country has a massive, bloated watchlisting system that can stigmatize people—including Americans—as known or suspected terrorists based on secret standards and secret evidence without a meaningful process to challenge government error and clear their names,” Shamsi said. “The categories of people watchlisted seem every expanding, never constricting … The consequences are significant and have real harms for people's lives. There’s the obvious stigma and embarrassment and life hardships of being unable to fly in our modern age, to being singled out, to being searched. We’ve had mothers and fathers stigmatized and embarrassed in front of their children.”

Estimates of both the Terrorism Screening Database and the No Fly List have long been made. The Terrorism Screening Database was been estimated to contain up to 1 million entries, with the No Fly List reportedly much smaller.

When asked for clarification, CommuteAir said it was specifically the No Fly List subset they hosted, which means it could potentially be much larger than previously reported.

But an expert familiar with the contours of the No Fly List cautioned that a list that size may be the larger Terrorism Screening Database and not the smaller No Fly List.

The Intercept in 2014 [previously reported](https://theintercept.com/2014/08/05/watch-commander/) that the No Fly List held more than 47,000 names. In 2016, Sen. Dianne Feinstein (D-Calif.) suggested that over [81,000 people](https://www.feinstein.senate.gov/public/_cache/files/f/b/fb745343-1dbb-4802-a866-cfdfa300a5ad/BCD664419E5B375C638A0F250B37DCB2.nctc-tsc-numbers-to-congress-06172016-nctc-tsc-final.pdf) were on the list.

Although the list is highly secretive and rarely leaks, it is not considered a classified document due to the number of agencies and individuals that need access to it.

In a declaration to the ACLU, G. Clayton Grigg, at the time the Deputy Director for Operations of the Terrorist Screening Center, [said](https://www.aclu.org/sites/default/files/field_document/253%20Declaration%20of%20G%20Clayton%20Grigg_0.pdf) that while the list does contain classified national security information, "maintaining the TDSB as a sensitive but unclassified system allows for law enforcement screening officers .... to use the identifying information from the TSDB even though they may not possess Secret or Top Secret security clearances.”

The discovery by crimew is not the first time an unsecured version of the Terrorist Screening Database has been exposed online. Security researcher Volodymyr “Bob” Diachenko found a detailed copy of the [terrorism watchlist](https://www.linkedin.com/pulse/americas-secret-terrorist-watchlist-exposed-web-report-diachenko/?_ga=2.68694546.2038757569.1673977369-402314082.1673977369) with 1.9 million entries in 2021.

Names provided to Diachenko by the Daily Dot matched entries on the list he obtained, although Diachenko never received official confirmation his list was genuine.

The No Fly List has routinely been criticized by privacy and civil liberties experts. The ACLU successfully sued to allow citizens to challenge their inclusion on the list. However, more work needs to be done to improve transparency with the list, Shamsi said.

“It is already a massive and bloated system, and growth is exactly the kind of thing that happens when you have a vague and over-broad system of what’s essentially government surveillance based on suspicion and without due process … At the bare minimum, if the government is to use watchlists, it must have narrow and specific public criteria [for entry] and apply rigorous public procedures for reviewing, updating, and removing dubious entries.”

**Update:**In the wake of the leaked TSA No Fly List, Rep. Dan Bishop (R) [called](https://www.cnn.com/2023/01/21/politics/congress-dan-bishop-investigate-tsa-no-fly-list-breach/index.html) on Congress to investigate the matter.
