Title: A blameless post-mortem of USA v. Joseph Sullivan

URL Source: https://magoo.medium.com/a-blameless-post-mortem-of-usa-v-joseph-sullivan-a137162f7fc9

Published Time: 2022-12-08T16:58:15Z

Markdown Content:
# A blameless post-mortem of USA v. Joseph Sullivan | by Ryan McGeehan | Starting Up Security | Medium

[Sitemap](https://magoo.medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://magoo.medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fstarting-up-security%2Fa-blameless-post-mortem-of-usa-v-joseph-sullivan-a137162f7fc9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://magoo.medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://magoo.medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://magoo.medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://magoo.medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fstarting-up-security%2Fa-blameless-post-mortem-of-usa-v-joseph-sullivan-a137162f7fc9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 1](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

[## Starting Up Security](https://medium.com/starting-up-security?source=post_page---publication_nav-6d3dc9a071e0-a137162f7fc9---------------------------------------)

·

[![Image 2: Starting Up Security](https://miro.medium.com/v2/resize:fill:38:38/1*klgju44lCEY1DZWakB1WNw.jpeg)](https://medium.com/starting-up-security?source=post_page---post_publication_sidebar-6d3dc9a071e0-a137162f7fc9---------------------------------------)
Guides for the growing security team

# A blameless post-mortem of USA v. Joseph Sullivan

[![Image 3: Ryan McGeehan](https://miro.medium.com/v2/resize:fill:32:32/0*3kOsPC2HwId9NCAA.jpg)](https://magoo.medium.com/@magoo?source=post_page---byline--a137162f7fc9---------------------------------------)

[Ryan McGeehan](https://magoo.medium.com/@magoo?source=post_page---byline--a137162f7fc9---------------------------------------)

32 min read

·

Dec 8, 2022

[](https://magoo.medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fstarting-up-security%2Fa137162f7fc9&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fstarting-up-security%2Fa-blameless-post-mortem-of-usa-v-joseph-sullivan-a137162f7fc9&user=Ryan+McGeehan&userId=cf87128497cb&source=---header_actions--a137162f7fc9---------------------clap_footer------------------)

--

1

[](https://magoo.medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa137162f7fc9&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fstarting-up-security%2Fa-blameless-post-mortem-of-usa-v-joseph-sullivan-a137162f7fc9&source=---header_actions--a137162f7fc9---------------------bookmark_footer------------------)

[Listen](https://magoo.medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Da137162f7fc9&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fstarting-up-security%2Fa-blameless-post-mortem-of-usa-v-joseph-sullivan-a137162f7fc9&source=---header_actions--a137162f7fc9---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*sa9K-gHJqNdPqpCNeVJMpQ.png)

Our industry deserves a complete retrospective into the incidents behind the criminal case against Uber’s former Chief Security Officer. We need more than opinions about an individual’s guilt.

Those who have been around long enough know that positive change is most efficient with a _clear_ and _blameless_ retrospective ([1](https://sre.google/sre-book/postmortem-culture/), [2](https://www.etsy.com/codeascraft/blameless-postmortems)). Blame is a shortcut that cheats us from learning opportunities, discourages cooperation, and generally promotes anti-patterns among people involved with future incidents. ([Pg. 431](https://library.oapen.org/bitstream/20.500.12657/26043/1/1004042.pdf))

Joe was formerly my direct manager at Facebook and is a friend. I know several witnesses in the case who are also friends. Many opinions have already been shared about his guilt, and I certainly have my own. I don’t believe Joe is a criminal, but my personal opinions about his guilt _don’t matter_. Opinions about individual guilt are _not helpful_ for anyone concerned with improving security organizations.

The incidents at Uber are something to learn from — we shouldn’t get off easy thinking a single person answers to this whole mess or that a conviction solved anything. There are several areas of tension to explore—notably, the boundaries of vulnerability disclosure to how responsibility lands across different teams during an incident.

I’ve spent months combing through every word of testimony in the USA v. Joseph Sullivan trial. My goal is to offer an in-depth analysis. A court filing through the court reporter (and a hefty fee!) was necessary for me to obtain transcripts before they were released to the public. I hope I have offered a comprehensive analysis as a result.

This essay hopes to follow a specific path: My goal is to completely exclude personal guilt and names from this essay. My analysis will treat this as an _accident_.

All information or analysis in this essay can be gleaned from [court proceedings, transcripts](https://www.courtlistener.com/docket/18414184/united-states-v-sullivan/), or public journalism. This essay contains no insider information. I have done my best to cite everything to page numbers and exhibits from court transcripts. According to the docket, the transcripts will become public on `2023–01–09`. That said, this effort is pretty thorough. I’m open to feedback and corrections.

Two methods guide my writing: An [investigative method](https://scrty.io/investigations) I’ve used throughout my career has shaped all of my incident response work for the last 15 years. I’ve also incorporated prompts from CAST analysis ([Nancy Leveson’s work with STAMP](https://library.oapen.org/bitstream/20.500.12657/26043/1/1004042.pdf)). All the results were then compiled into this essay.

If you’re new to my writing — I write a lot about large and small security organizations, particularly incident response, [here](http://scrty.io/).

Let’s get started!

## Contents

1.   **Takeaways:**If you’re short on time and attention span, just read this.
2.   **Timeline:**A detailed timeline with minimal opinion.
3.   **Hazards:**Describing events that contributed to hazards
4.   **Discussion:**Analysis of improvements applied to the hazards.

## Takeaways

The following section includes concise talking points resulting from my analysis of transcripts. The section after this is more matter-of-fact and heavily cites the trial transcript, if you’re looking for a more sequential rundown of events.

**Dual reporting introduces hazards.** Identify who is responsible for the legal _analysis_ and who is responsible for a legal _decision_ in an incident disclosure task. Reporting structures at Uber created several false assumptions held by the incident response team and harbored a fragile decision-making process.

**Straighten out executive interference.** A policy may identify the owner of a decision but ensure that accountability isn’t confused when a more senior executive becomes involved with that decision. Answer whether the involvement of an executive changed the decision-maker. Incident response policies identified a decision maker in Uber’s Legal organization, which eventually became confusing when the executive team was said to be involved.

**Distance disclosure analysis away from in-house counsel.** In-house counsel may have reporting structures or other incentives that make them partial to specific outcomes like there were at Uber. Counsel could err _away_ from disclosure based on the organizational structure where the analysis originates. Coordination can be expected from these in-house roles, but be wary of single points of in-house analysis and decision-making, even from a lawyer.

**Diversify the stakeholders performing disclosure analysis.**Multiple perspectives from legal and non-legal stakeholders can better inform a disclosure decision. Require _outside_ counsel to be involved. Name these roles specifically so assumptions are not made about their involvement. Multiple witnesses expressed frustration about a disclosure decision they weren’t involved with.

**Define authorized access.** Require good faith throughout an external disclosure, particularly when data is breached. Seek mediation, or sever contact when bad faith is suspected. Define how to escalate when criminal intent is observed and data is breached. A bounty payment was applied to conduct that should not have been considered authorized. What is demonstrated from this case is that retroactive authorization of access from a vulnerability disclosure is fraught when bad intent is shown in the disclosure process.

**Don’t mix bounties and investigations.**Using the bounty process as a means of attribution confused the mutual goodwill expected from both sides of a bounty program. The bounty process shouldn’t contain anyone suspected of bad faith, and the attribution of a researcher to a bounty platform should happen voluntarily by the researcher.

**Build and hold to rewarding**[**bounty tables**](https://docs.hackerone.com/programs/bounty-tables.html)**.** Bounties should have the option of being as rewarding as you can tolerate, allowing the disclosure of extreme risks. External parties should feel comfortable reporting issues without resorting to criminal tactics.

**Err towards disclosure.**Ask why you are not disclosing rather than the opposite. Find a public voice to disclose _near-miss_ situations. Only some things need to be an apologetic press release. Disclosures can educate. Educate the rest of us with high-risk research findings in your engineering blog, bug bounty platform, or other places, and signal your capabilities in responding to an incident. Incidents happen; how well did you respond?

## The Timeline

I am writing the timeline as a narrative with my analysis at a minimum. The following sections on hazards and recommendations will offer more of my opinions.

**_Reminder, no information comes from non-public or insider sources._**

The cited page numbers are from [fifteen volumes](https://www.courtlistener.com/docket/18414184/united-states-v-sullivan/?page=2) of trial transcripts ordered from the court reporter. They will be public in January 2023. Or, my citations are from exhibits that were verbally read off and cited in these transcripts. Exhibits are not yet accessible for review by the public unless their contents were read out loud during the trial.

### The 2014 Incident

An adversary discovered an Uber credential that was leaked in a GitHub Gist. Uber believes the adversary was on a [Comcast IP address, which pivoted to use a Scandinavian IP address behind a VPN](https://www.reuters.com/article/uk-uber-tech-lyft-hacking-exclusive/exclusive-in-lawsuit-over-hacking-uber-probes-ip-address-assigned-to-lyft-exec-sources-idUKKCN0S20D020151008)to exfiltrate several objects containing database prunes held in an S3 bucket on `2014–05–12`. (Pg. 374–375) These S3 objects contained about 50,000 records, including names and driver’s licenses. (Pg. 298)

A database prune redacts production data and generates datasets for local development so that employees can work with workable data that isn’t customer data. This pruning process was incomplete at removing sensitive data, putting customer data at risk. (Pg. 327, 384, 387, 761)

Uber made its first security engineering hire after the breach, but before it was detected in June 2014 (Pg. 754).

Also, The FTC began investigating Uber _before this breach_ was detected. They were interested in Uber [employee access to data](https://www.forbes.com/sites/kashmirhill/2014/10/03/god-view-uber-allegedly-stalked-users-for-party-goers-viewing-pleasure/?sh=6afc9cec3141) reported on `2014–10–03`. On `2014–11–20`, the FTC sent a preservation letter to Uber regarding their investigation (Exhibit 260, Pg. 297).

The breach remained undetected for an unknown period of months before an interview with an engineer at a competing company disclosed that an executive at their employer had a copy of an Uber database. Based on this suspicion, a small group of engineers was assembled to hunt for a breach. The hazardous gist was discovered and found to be an Uber data analysis script containing AWS key material. The exfiltration is assumed to be discovered while reviewing Cloudtrail logs related to the leaked credential. (Pg. 758)

Uber published a [blog post disclosing the breach](https://archive.ph/O9Toe) on `2015–02–27,` about five months after discovery. Uber later kicked off a John Doe Lawsuit to better attribute the adversary by [serving civil subpoenas to GitHub and Comcast](https://www.reuters.com/article/uk-uber-tech-lyft-hacking-exclusive/exclusive-in-lawsuit-over-hacking-uber-probes-ip-address-assigned-to-lyft-exec-sources-idUKKCN0S20D020151008).

After this disclosure, the FTC expanded its investigation into Uber on `2015–03–12` (Exhibit 2, Pg. 298).

Uber hired a CSO on `2015–04–02`. Uber also deployed a secrets management infrastructure called _Langley_ the same month. (Pg. 2581)

_For these following paragraphs: A quick reminder that I’m not a lawyer. We’re going to be talking about legal stuff anyway._

### FTC Investigation

An FTC investigation involves a [Civil Investigative Demand](https://www.ftc.gov/business-guidance/blog/2018/01/so-you-received-cid-faqs-small-businesses) (CID). This subpoena can demand interrogatories, document requests, and depositions. The FTC pushes to make a CID a collaborative process, so they “meet and confer” on things like deadlines and the scope of the demands. It’s still a subpoena, so it’s not an informal process despite their flexibility. Specific lawyers exist to counsel their clients through a CID. The FTC sent this CID to Uber on `2015–05–21`. (Exhibit 274)

Uber has in-house counsel, which I’ll reference as the _FTC Point of Contact Lawyer_. Both parties firmly stipulate throughout testimony that this individual is the lead on the FTC CID that Uber received and that the conversation with the FTC is coordinated by this lawyer (Pg. 1084).

Of specific importance is the definition of “_breach”_ within this demand. Consider that while the word _breach_ may be nebulous across many legal contexts — the word is defined explicitly in this CID (Pg. 1083)

> “Unauthorized access into the company’s systems or the personal information in the company’s files, including but not limited to the data breach from 2014.”

It goes further to say:

> “With respect to any breach or suspected breach, please provide the following information.”

Note that it doesn’t mention anything requiring exfiltration, the size of the breach, or other qualifiers that would make this less broad. The defense didn’t contest the breach definition during the trial.

There were eight total Uber responses to interrogatories on `2015–06–25`, `2015–07–31`, `2015–08–27`, `2015–09–25`, `2016–05–06`, `2016–08–30`, `2016–11–01`and `2016–12–21` in the trial.

Additionally, Security leadership flew out to present to FTC staff on `2016–03–23` (Pg 247).

On `2016–11–04`, the FTC deposed the CSO in person. (Pg. 234)

### The 2016 Breach

The adversaries in 2016 require some background before we continue the timeline. The discussion of their backgrounds is without timestamps, so this is a segue before we get back to the timeline.

The adversary included two individuals who were active in hacking forums. One of them testified about their access to large datasets of credentials (username/passwords) that they had developed for themselves (suggesting other breaches), traded for, or acquired through public leaks. They describe this database as having “over ten million” entries. (Pg. 848–859)

They had a script developed through a freelancer on Upwork, which would ingest emails and passwords and attempt to log into GitHub. The script outputs a log of whether a log-in was valid and _the GitHub organizations the account belongs to._

“Over a hundred thousand” successful log-ins were output by the adversary’s script. This output was matched with a list of “most visited websites,” which elevated Uber to the attention of the adversaries, along with other companies. (Pg. 850)

The adversaries may have had about 13 good log-ins for Uber. They accessed these GitHub accounts intending to find AWS credentials to get backups of databases and were previously experienced in doing this. The testimony sounds like they would use simple GitHub searches to surface these credentials. (Pg. 852)

They succeeded in finding several AWS credentials and loaded them into a tool called [_S3 Browser_](https://s3browser.com/). However, some credentials did not work for them. (Pg. 855)

From here, the adversary discovered hourly encrypted backups. They were unable to view these backups. They did not have the key required to decrypt them. (Pg. 857)

So, they reached out to a third person not identified in the trial. One of the adversaries sent this third person the leaked AWS keys. (Pg. 859) After a day or so, the third person indicated to the adversaries that there was an “interesting” object which one of the adversaries proceeded to download on `2014–05–12`. This was a database containing 50 million records. (Pg. 859–860)

> Note: The testimony is unclear on this date whether it was the initial AWS access, the third-party access, or the actual exfiltration.

These database objects were created outside the regular automated backup into the `cold-storage` bucket (_Naming has nothing to do with cryptocurrency, FYI_). Production regularly used client-side encryption to encrypt backups and store them in this bucket. However, backups could still be created outside of automation. In particular, an engineer created backups while decommissioning a service, writing them without encryption into the same bucket. (Pg. 777, 779, 1705–1706)

### Extortion

Shortly after, one of the adversaries decided to reach out to Uber and the other agreed.

On `2016–11–14` at 12:23 p.m. (Pg. 863), the adversaries emailed the Chief Security Officer from a ProtonMail address, believing it would be more private if law enforcement would reach out. The adversaries acknowledge in their testimony that the following process would be against the law. (Pg. 863–864)

> “I have found a major vulnerability in Uber. I was able to dump Uber database and many other things.”

Shortly after, the CSO forwards this to the head of product security (12:36 pm), and it is then forwarded to the manager in charge of bug bounty (12:43 pm). (Pg. 950-951)

Discussion with the adversary takes an ambiguous and extortive tone through the afternoon. Testimony shows that extortion was intended by the adversary and perceived as extortion by the response team. (Pg. 657, 892, 1066, 2485)

The adversary demonstrates their access to the bug bounty manager by sharing records from the exfiltrated data over the day. In particular, they share the manager’s historical password hashes from the data back to the manager. This is around 6:05 pm and 6:10 pm. (Pg. 876) The bug bounty manager becomes convinced there is a valid incident. (Pg. 964-965)

### Incident Response

A lot of things happen from here. The CSO, the CISO, the managers for Security Response and ThreatOps, and the Privacy Lawyer assigned to Security join the incident, among others from their teams. The adversary and incident were named “Preacher,” and a “Preacher Central Tracker” was created, a Google document with notes from everyone regarding the incident. (Exhibit 27–31, Pg. 605)

An employee dedicated to Security from the Communications org (Comms Employee) is looped into the incident. Escalation from the Comms Employee to their “A-Team” member happened at an undetermined time. (Pg. 2525, 2537)

From this point, it will serve us to discuss the role of the Privacy Lawyer in this organization. Both parties stipulated that the Privacy Lawyer reported to Security and Legal. The transcripts describe a dotted line hierarchy for the Privacy Lawyer through the Legal department up to the GC. (Pg. 1299, 1372)

Separately, there’s another reporting link through security directly to the CSO. Emails make it clear that this relationship is so that the Privacy Lawyer is still a function of the Legal organization, despite their reporting relationship to security. This complicated arrangement allowed privacy counsel to work full-time with security while reporting to the general counsel. (Pg. 526, 1299, 1377, 1600, 1374–1375, 1377, 1600)

In an email chain with the larger group, the CSO invokes the Privacy Lawyer by assigning them the investigation to have it performed at their discretion. (Pg. 1311)

From this point forward, all conversation with the adversary is made in collaboration with this larger group of incident responders and legal. In contrast, previously, it was strictly between the adversary and the bug bounty manager.

> A quick interjection of analysis from me: What is not described in the testimony are the particulars of the technical investigation — however, it’s assumed they had enough know-how to quickly hunt for the leaked AWS key in CloudTrail logs and confirm the disclosure.

The response process among this group determined `2016–11–15` at 8:30 pm that driver’s license numbers were exposed, and the Privacy Lawyer acknowledged that it triggered disclosure. (Exhibit 29, Pg. 1316)

The CSO notes that they are communicating this to the “A-Team,” representing a group of top-level executives who report to the CEO. (Exhibit 29, Pg. 636, 795–796, 835, 1317, 1353)

### Legal Analysis

A legal theory was produced about using employee agent exception and [nunc pro tunc](https://en.wikipedia.org/wiki/Nunc_pro_tunc) to postdate the interaction with the adversaries and fit the interaction as a bug bounty. Assuming the adversary continues cooperating, it’s authorized activity under this theory. (Pg. 1322)

The CSO updated the CEO on `2016–11–15`, at 1:26 a.m. over text and Facetime call. On `2016–11–15` at 10:52 p.m., the CSO confirmed that the breach was contained to the CEO. (Pg. 2003–2005) At 12:17 pm on the same day, the bug bounty manager confirms this with the adversary. (Pg. 885, 968) The team’s direction moved toward the attribution of the adversary. (Pg. 2003)

The manager for privacy lawyers was notified in passing on November 15th at 9:50 pm while reading a document related to the response effort. They double-checked whether they should be involved or if the Privacy Lawyer assigned to security was already involved. (Pg. 1898)

> Author interjection here: Extensive testimony occurred about the specific verbal interactions between some responders. “Who said what” is critical for the trial. In blameless retrospectives, we care about the process and actions taken. You might see a few pieces glossed over, which should not surprise you.

What’s not clear is who was taking ownership of the decision to proceed under this legal theory. A legal theory was produced, and the larger group (at the very least) perceived that the executive team decided to apply it. (Pg. 2105, 1320, 2003–2004, 2105, 2107)

Testimony is clear that the team began to stall with the adversary over communications so they would have more time to work on attribution. (Pg. 969)

The response team suggested a bounty of $10K to the adversary, which was rejected by the adversary with a counter of something in the six figures (Pg. 871, 873).

### Ongoing FTC Interactions

The FTC Point of Contact Lawyer is finalizing and delivering a response to the FTC around `2016–12–20`. (Pg. 412–413, 809, 1104-1106) In this response, language is included from a document developed by a security engineer on `2015–09–25` (Exhibit 292, Pg. 763-764):

> Similarly, starting in the spring of 2015, all database prune files stored in Uber’s Amazon S3 datastore have been client-side encrypted.

The engineer who worked on that document, the FTC Point of Contact Lawyer, the Legal Director for Privacy, and the CSO are on the thread. It is delivered to the FTC. (Pg. 765, 1105–1106)

This particular response proved hazardous. The response conveyed a statement to an interrogatory that _all database backups are encrypted._ This response occurred during the investigation of an incident where an unencrypted backup was accessed. (Pg. 396, 413–414, 763–765, 777, 779, 1705)

### Attribution

Two tactics are employed to encourage the adversaries to identify themselves or reveal more forensic data that might attribute to them. These tactics became contentious areas of litigation, but we can still review them.

First, the response team encouraged the adversary to present themselves to HackerOne. There was an expectation that the adversary might present themselves with properly attributable tax documentation or reveal attributable IP addresses in the process. The response team also worked with HackerOne to stall payments and bought more time for attribution and threat assessment opportunities to pan out. We’ll discuss a major one shortly. (Pg. 969)

The second was using NDA software (Adobe Sign) for the adversaries to sign. The team anticipated they might sign it with their real names or leak attributable IP addresses. (Pg. 277, 2300)

Later, the adversary purchased a stolen identity for registering with HackerOne and didn’t use their real names on the NDA. (Pg. 1712–1713)

However, both tactics successfully advanced attribution — they both revealed an IP address that eventually achieved the attribution goal. (Pg. 278, 2306–7, 1749)

The actual language of the NDA and the applicability of being authorized under bug bounty became a quagmire of legal analysis to determine whether it was appropriate to apply this legal theory to a bug bounty.

On `2016–12–05` at 2:17 pm, the adversaries sent a more aggressive threat:

> Please remember that the contract states all data will be deleted once the money is paid. The ball is in your court. _(Pg. 913)_

Uber instructed HackerOne to release the payment shortly after, on `2016–12–08`to an unattributed adversary (Pg. 982, 1325, 1443, 1871–1872).

### Attribution Completes

The attribution efforts continued. We don’t have significant timestamps on this part of the testimony, but it roughly sequences as follows.

First, the most critical IP address belonged to a Florida based hosting provider. ThreatOps contacted the hosting provider and informed them of abuse on their servers. The hosting provider was responsive and gave their customer 48 hours to reply to the complaint before handing over registrant information. Shortly after, the customer reached out, who itself was a VPS service. This VPS customer (located at the hosting provider) got in touch with Uber and agreed to hand over the server that the adversary was using, who was a customer of theirs.

This customer (of the VPS, who was a customer of the Hosting Provider) was Uber’s adversary. (`Host->VPS->adversary`)

While confusing, this interaction resulted in a complete forensic snapshot (memory and all) of the adversary’s server delivered to ThreatOps. (Pg 1716–1717, 1723, 2311-2323)

There were several observations from this server: A new email address used by the adversary, names of other victim companies, and an observation that Uber’s data was deleted from this particular server after they had requested it to be, but without the adversary's knowledge that Uber would be able to see whether deletion would happen.

The adversary’s VPS email address became a new lead. The email address was found in a data breach forum asking other members for a hash (unrelated to the incident) to be cracked. Another forum member took the job and cracked the hash, asking for payment over bitcoin to a visible wallet address. A transaction for the requested amount to that address was observable on the blockchain. ThreatOps could associate the sender’s wallet address (presumably owned by their adversary) with another third email address in threat intelligence data. Specifics weren’t explained in the testimony. This final email address was strongly tied to the real identity of Uber’s adversary in ways that were not explored but seemingly had lower operational security. (Pg. 1725)

Uber then contacted the (entirely attributed) adversaries on `2017–01–02` and flew out specialized employees to have face-to-face conversations with them. (Pg. 2447) Those employees assessed the character of the adversaries and directly asked them about their motives and actions during the incident. (Pg. 2311) In doing so, one adversary lied about two facts: the status of the deletion of Uber data and omitted that a third hacker had been involved. However, that adversary later admits to deleting the data to free up hard drive space. (Pg 937) Both adversaries also signed new NDAs with their real names during this interaction.

### FTC Interactions Resumed

Around `2017–04–07`, the FTC Point of Contact Lawyer, the Legal Director for Privacy, the CSO, and the General Counsel discussed a letter urging the FTC to close their 2.5-year investigation. The group agrees to deliver it. (Pg. 1609)

On `2017–06–20`, the [previous CEO resigned](https://www.nytimes.com/2017/06/21/technology/uber-ceo-travis-kalanick.html).

## Get Ryan McGeehan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

- [x] 

Remember me for faster sign in

 

An internal investigation began using an outside law firm around `August 2017` into matters unrelated to the 2016 breach. Investigators learned of the breach in the course of their investigation. Interviews of the responders follow. (Pg. 595, 817)

The [new CEO](https://www.uber.com/newsroom/ubers-new-ceo-3/) was announced on `2017–08–30`.

The (new) CEO eventually learns of the incident. The CSO briefed the CEO sometime in September 2017. (Exhibit 623, Pg. 1773, 1785 )

The CEO launched a re-investigation with an outside security firm and [disclosed it publicly](https://www.uber.com/en-CA/newsroom/2016-data-incident/) on `2017–11–21`.

## Hazards

This section introduces more analysis from myself.

**The encryption scheme for database backups was bypassed:** All automated backups were client-side encrypted, but manual engineering work bypassed this backup pipeline. Backups were created in plaintext.

**MFA did not protect GitHub accounts:** There’s some nuance to this because an organization-wide MFA policy feature from GitHub did not exist at the time of the attack.

**A credential was stored in a GitHub repository:** A rule of thumb is to keep credentials and secrets securely stored so that it’s doubtful to end up in an engineer’s copy/paste buffer. The infrastructure to make this happen (Langley) was launched shortly after the incident in April 2015. (Pg. 2614) However, we’ll see that this wasn’t enough.

**2013 credential (“**`genghis`**") was never rotated:** The 2016 incident involved a credential that had existed without rotation since 2013 and went unrotated through the mitigation work of the 2014 breach. (Pg. 629) Even if `genghis` were stored in Langley, it was exposed in this repository.

**IAM Policy allowed remote access to**`genghis`**:** While this is not directly addressed in the testimony, we can deduce that it was possible because an “anonymous” VPN could make calls to the AWS API with the credential. This mitigation is not always feasible, but it's a standard mitigation win against remote attacks. The mitigation is discussed in exhibits. (Exhibit 467, Pg. 2014–2016)

Additionally, roles may have been leveraged instead of credentials — allowing AWS resources, services, and employees to assume roles in place of distributing credentials through source code or anywhere else. This is difficult to critique without knowing more about how things were architected at the time.

**Exfiltration was not detected:** Detection engineering is difficult to critique as an outsider. There were a few detection opportunities for this attack, but it can be debated how reliable they may be. First, the adversary used the “S3 Browser” tool with stolen credentials against the AWS API. It’s unclear if the adversary made any User Agent String configurations to their installation, but this user agent does not belong in most production environments. It’s a loud signal. Similar alternative AWS clients (cloudberry, elasticwolf, s3 browser) are attacker favorites and announce themselves in CloudTrail logs. Next, the IP address making these commands was from a strange VPN. If engineering patterns are architected correctly, odd IP addresses like this appearing can be detected more quickly, especially if there are IAM policies against them (as previously mentioned). Again, this is hard to critique without all the information.

**There was no outreach to Law Enforcement:** Testimony is clear that Law Enforcement outreach was on the table only if attribution and cooperation were not possible. The response team successfully attributed the adversary and believed the adversaries cooperated, thus taking law enforcement outreach off the table for them. Additionally, response team members testified that they’d believe a law enforcement response to a bug bounty participant would harm the credibility of their bounty program.

**There was no outreach to the Public:** The legal theory employed here was that there was no data breach because the threat actor was retroactively authorized after cooperating with the investigative team. That’s not an accurate legal explanation, and I am not a lawyer. Testimony indicates that this opinion led to several decisions that resulted in no public disclosure.

**There was no outreach to the FTC:** Similarly, the FTC Civil Investigative Demand gave an additional definition of the word “Breach” in its subpoena. The legal theory was that this particular incident did not meet this definition for reasons previously explained.

**Bug bounty was used to accommodate bad-faith actors:** The submitter, in this case, was anonymous, perceived to be extorting the company, and had exfiltrated data that would trigger disclosure law and regulation. The legal theory provided steps to check all the boxes and fit this into a non-disclosable incident, but the requirements in the FTC CID were debated to be broader than this.

The FTC generally disagreed that “bug bounty” could be applied to authorize a data breach retroactively. (Pg. 515–517)

The FTC is transparent in its testimony that this is a complicated problem they had not yet encountered. This was the first time they had seen this legal theory applied. (Pg. 517)

**Stakeholders in Legal were not informed of the incident:** While the CSO informed the “A-Team,” this did not mean to include every single A-Team member. The CSO’s escalation solely included the CEO, described as “A-Team.” The General Counsel was on the A-Team and was not informed. (Pg. 1608)

Additionally, the Privacy Manager who with a dotted-line to the Privacy Lawyer also did not inform the General Counsel because they were only aware of the incident in passing (Pg 1433, 1932, 2514). After ensuring that the incident was delegated to the Privacy Lawyer, they did not track it closely. In retrospect, it can’t be predicted whether a large loop of employees would have led to different disclosure decisions.

There appears to be confusion around the obligations of a Deputy General Counsel role that the CSO held (Pg. 1648). Testimony shows that it intended to allow the CSO to provide counsel and create a reporting relationship between the CSO and the GC. However, testimony also makes it clear that only a little else changed. What is implied is that this may not have created GC-like obligations for the CSO. (Pg. 1592, 1648)

The Privacy Lawyer brought up the incident in a team staff meeting, but again, in passing as a status update without any escalation. (Pg. 1435)

A critical stakeholder, The FTC Point of Contact Lawyer, was unaware of the incident (Pg. 1107). The FTC Point of Contact Lawyer was a peer on the Privacy Team, with the Privacy Lawyer accountable for the disclosure decision.

Important to discuss at this point is the broad perception that the CSO notified the “A-Team.” The A-Team includes the General Counsel. As previously discussed, only the CEO was involved in the discussion.

The CSO was also a “Deputy General Counsel” (DGC), which may have bolstered this perception of GC oversight. However, the DGC role was testified to singularly be to counsel the CEO, with a reporting role to the GC for only this function (Pg. 1592, 1648). These contributors may have increased the perception that the rest of the Legal organization was notified.

Further, the Comms Employee shared documents with the Privacy Manager related to the incident. (Pg. 1898)

While the Privacy Lawyer was peers with the FTC Point of Contact Lawyer, it’s possible that they perceived the incident was well distributed through both of the Privacy Lawyer’s direct managers and the General Counsel who was assumed to be making the disclosure decision.

**The interrogatory responses were overly broad and not corrected.**

An older document written by engineers from 2015 included broad language that claimed _all_ new database backups were client-side encrypted, which was then used in a draft by the FTC Point of Contact Lawyer to respond to an interrogatory. Using an overly inclusive statement (“all”) was hazardous. (Exhibit 292, Pg. 763–765 & Exhibit 455, Pg. 806–808)

Only automated backups were client-side encrypted, and the incident involved what appears to be a manual bypass of backup automation by engineers decommissioning old services (Pg. 777, 779, 1705). There was security engineering representation in crafting this response and participation in the thread that decided to release the message. This response was then sent to the FTC on `2016–12–22` (Pg. 1201)

**The letter urging to close the investigation should not have been sent.**

Legal stakeholders discussed a letter to the FTC intending to persuade them to close their investigation. The legal theory applied to the 2016 breach kept the incident from being considered in the decision to send the letter. The email thread discussing the decision to send this letter only had one participant aware of the 2016 incident. (Exhibit 563, Pg. 418, Pg. 1216 )

**Legal analysis, disclosure options, and decisions needed to be clarified.**

We must be very clear about the anatomy of decisions when we analyze how a decision came to be.

First, remember that we make _decisions_ from a set of _options_.

The _option_ to not disclose the incident was created (a legal theory) when the Privacy Lawyer was asked for a legal analysis of the incident. The theory was escalated to the CSO and CEO.

The _perception_ of where the decision is made is essential for our retrospective.

The decision was _perceived_ to be made by the A-Team, the CSO, and the Privacy Lawyer… depending on who was testifying.

Incident Response policy documents identify the Privacy Lawyer as the stakeholder intended to decide on disclosure. (Pg. 1168–1170, 1175, 1647, 2455, 2461–2462)

However, the Privacy Lawyer was informed that the “A-Team” was involved with the decision and that the legal theory was presented to them. The “A-Team” includes the General Counsel. (Pg. 1324)

Several response team members were aware of the CSO’s conversations with the CEO or the A-Team. (Pg. 586, 635, 796, 1317, 710)

Reporting structures for the CSO and Privacy Lawyer have multiple paths back to the legal organization, further blurring how information could have been propagated across the organization. Dual reporting chains create efficiencies in some organizations, but in this case, assumptions needed to be more consistent during an escalation.

## Discussion

Let’s briefly acknowledge some things that went right.

*   The response to the breach was rapid, with remediation within 24 hours.
*   Escalation was defined in the incident response policy.
*   Secrets management infrastructure was available during the response for key rotation.
*   The adversary was attributed.
*   Legal was immediately contacted for disclosure advice and was present throughout the incident.
*   The CEO was immediately notified.
*   Comms was immediately notified, and escalation happened within comms all the way to the A-Team.

Still, we’re not happy with the outcome. We will discuss major areas where improvements can be made.

### **Breach Disclosure**

A breach disclosure failure happens when a breach occurs, and disclosure is inaccurate, delayed, or doesn’t happen at all.

This section targets how breach disclosure decisions were made. The organization acted as though the executive team made a fully convened decision not to disclose, and we need to mitigate that from happening again. We’ll discuss this in terms of an incident response plan.

Security is responsible for incident analysis. Legal is responsible for legal analysis. Legal must rely on external counsel for this analysis. Otherwise, we risk communication hazards. Confusing and boutique reporting relationships exacerbate those hazards. The pressure to provide legal advice to your direct manager was also a factor here.

The incident also saw some bystander effect. CC’ing a peer organization on a document, updating folks in a status meeting, or assuming others will run decisions up their dual management chains wasn’t enough to prevent this outcome. In addition to the security response team being aware:

*   The CSO escalated to the CEO
*   The CSO assigned the incident to the Privacy Lawyer with dual reporting to Security and Legal.
*   The Privacy Lawyer mentioned the incident at a status meeting.
*   The Privacy Lawyer briefly mentioned the incident to their (Legal) dotted-line manager.
*   The CISO escalated to Comms.
*   Comms looped in their direct management, who escalated to their “A-Team”, and shared their plans with Legal. (Pg. 2537)

How did all of this coordination still create a bystander effect?

These escalations needed to be improved to gain the attention of the FTC Point of Contact, who had a stake in disclosing to the FTC. Remember, the Privacy Lawyer felt that the “A-Team” was involved. Comms felt the Privacy Lawyer took point for the decision. Legal felt that the Privacy Lawyer took point on the incident and didn’t involve itself further. The CSO assigned the case to the Privacy Lawyer who reports to the GC through a dotted line. The GC who is also on the “A-Team” that was supposed to be informed, but only the CEO within the “A-Team” was informed.

This is circular and confusing. These otherwise typical incident response escalations didn’t include everyone necessary.

The individual or group assigned with disclosure analysis should be responsible for coordinating the enumeration and risk assessment of disclosure options with multiple pre-identified stakeholders and not making the _decision_ and just coordinating the _options_ and the recommendation from those stakeholders.

The policy can identify stakeholders like the CEO, a particular board member, CSO, comms, General Counsel, in-house or outside counsel, regulatory liaisons, or even sales leads.

Otherwise, we miss the complete picture of risks and harbor conflicting risk analyses. The goal is to collect risks and options from more stakeholders.

Next, codify how and when these stakeholders are notified. It can’t be on every trivial incident. Every case of account takeover or fraud does not require a committee meeting. Write clear conditions and severity into the policy to answer that question and limit noise.

The steps to communicate a severe incident to a larger committee are essential. Confused escalation was a hazard in this incident. The existing policy appointed a single lawyer for legal analysis. That created the perception of a decision-maker. We want to avoid confusion and relieve the point person of making a decision. Instead, they’re responsible for escalating to stakeholders and coordinating a decision.

Most importantly, define _precisely_ what authorized activity is and how it relates to disclosure policies. Consider scenarios where good-faith research is disclosed that obtained user data. Policies that err toward disclosure are more straightforward when you plan where you’ll disclose ahead of time. Maybe they can be efficiently disclosed on a bug bounty platform, an engineering blog, or elsewhere. Near-miss issues can be disclosed without embarrassment so long as they have the right audience.

A point of confusion this essay cannot resolve is whether unauthorized access can become _authorized_ in hindsight when a company learns about access from research activity. This is a common scenario — a researcher discovers an impactful vulnerability and accesses data, disclosing it shortly afterward. Was the initial access _authorized_ at the time, or in hindsight? Is it a _breach_ up until the disclosure takes place? Does it become a breach (again) if the disclosure takes a u-turn toward extortion? At what points do we risk the misprision of justice?

This case explores this question well, but I can’t answer them as I’m not a lawyer. The adversary had demonstrated criminal intent throughout. The prosecution argued that it was _unauthorized._ Tabletop these situations ahead of time with your policies and with legal counsel. As mentioned before, the FTC also acknowledged in testimony that this is new territory for them.

Lastly, require a meeting with a concrete _decision_ on disclosure. Make sure all evidence and disclosure options are available at the meeting. The decision cannot be passed around from a game of telephone or assumptions. There needs to be a meeting, and the decision maker needs to know they are the decision maker.

### **Infrastructure Security**

This section discusses technical failures that the attackers leveraged.

In both the 2014 and 2016 cases: the policies attached to that credential permitted access over an “anonymous” VPN. A `sourceIPAddress` restriction applied with an IAM policy may have been helpful. However, some networks cannot cleanly identify and allow their defined networks to take advantage of this policy without friction. This mitigation is briefly mentioned in the testimony, so it was on the radar at the time. (Pg. 2015)

Both incidents also involved engineering access to infrastructure secrets. The 2014 incident did not have the infrastructure to manage secrets. An in-house system called Langley was built in response to the 2014 incident to manage secrets and assist with client-side encryption of automated backups. These systems aim to keep credentials out of source code and copy/paste buffers.

However, while credentials seem to have been put into Langley, the credential abused in the 2016 incident was not rotated after loading it into secrets management. This meant it was a leaked secret that was loaded into secrets management.

While this is a miss that led to an incident — The existence of Langley was still an improvement in the event of an incident for the ability to rotate the secrets it held. Presumably, they could still use Langley to rotate the leaked secret. The lesson is to rotate credentials after loading them into a secret management system. Then you have the confidence that they’re no longer relied on in places that don’t benefit from secret management.

Regular, automated backups were encrypted client-side with secrets managed by Langley into a bucket called `cold-storage`. However, a few backups in this bucket were outside the normal backup process - a one-off to decommission a service (Pg. 777, 779, 1705). Those backups were in plaintext. This process did not respect the automated process and was discovered by the 2016 adversaries.

Products and tooling exist to search for plaintext data resembling your customer data. Creating an S3 policy to encrypt all written objects is possible, too. Alerting on manual AWS backup commands may be feasible to find and fix ad-hoc backup use cases.

Neither incident made use of role-based access with IAM. The underlying infrastructure patterns at the time of each incident are unclear, but architecting systems for role-based access reduces the overall exposure of credentials. We can’t apply retrospectives to these patterns without knowing more about what could have been prioritized at the time.

### **Vulnerability Disclosure**

Vulnerability Disclosure fails when vulnerabilities are exploited, publicly disclosed instead of coordinated, or not disclosed at all.

_Why wasn’t the 2014 vulnerability disclosed to Uber?_ There are extensive accusations that the CTO of a competitor made the original discovery of the leaked AWS credential that was exploited. Granted that this is true, it’s unlikely that it would have been disclosed unless another individual was incentivized to find it first and disclose it.

The 2016 vulnerability leading to the incident is different. The 2016 vulnerability _was technically_ disclosed to Uber. Extortion is a corner case where exploitation and disclosure happen simultaneously. The muscles of a vulnerability disclosure program are still relevant in an extortion scenario. The extortive origin of the disclosure still requires a quick follow-up, like any critical submission. So while the 2016 issue was technically discovered and disclosed to Uber, the 2014 issue was not.

_Why wasn’t the 2016 incident reported over more proper channels?_ A more noble researcher could have found the same vulnerable GitHub account and reported it.

However, the breach involved many steps that would be difficult to see in a more noble bug bounty submission.

To perfectly replicate the findings behind the extortive disclosure, another researcher must access the GitHub account and disclose their access. Further, they would have to identify the leaked IAM credential, discover the `cold-storage` bucket, _and then_ identify the plaintext backup database (requiring exfiltration). Then, we'd have to expect them to report this whole chain of issues before stopping to report something earlier in the chain.

An equivalent disclosure of the breach through good faith research would be considered _very_ aggressive.

Can our expectations around security research and disclosure change so we can confidently allow disclosures like this involving the entire attack chain? That’s a difficult question. It’s better to consider that maybe the research ecosystem can improve to a point where some of the earlier attack steps could be disclosed more reliably before an adversary comes along. There are ways to encourage this as a company supporting the bug bounty community, but this is a large area of improvement with many inputs outside of what a single blue team can manage.

The Bug Bounty aspect of the vulnerability disclosure had confused goals with the investigation, making it unclear to outside investigators what the purpose of the bounty was. The routing of extortion to bug bounty also chilled the prospect of working with law enforcement. Law enforcement was an option for the team. Several response members acknowledged their hesitation in sending law enforcement after someone participating in the bug bounty program. They feared that the program would die altogether.

The bounty program did not immediately reject a submission that didn’t play by the rules. A rigid policy requiring good faith actors could mitigate this. Testimony brought up practices shared at other companies — if the researcher doesn’t play by the rules, the researcher is out of luck. Applying a policy like this still might not have been effective because the bounty activity was confused with investigative goals. Though, a stricter policy may have brought up hesitation to use the bug bounty program as a means of investigation.

A long shot is whether the bug bounty program could have been rewarding enough to encourage responsible behavior. While unlikely, a strict bounty table that allowed for exceptional findings would have created that possibility. Of course, had the researcher gone that route, disclosing the research to the FTC would still have been appropriate.

### Detection

Detection has failed when an incident occurs without being detected through preferred channels.

In 2014, the remote IP connecting to the AWS API was not discovered. That would have required configuration with S3 logging and observability into Cloudtrail logging when it occurred, along with alerting on IAM network exceptions.

In 2016, GitHub did not detect or prevent the ATO into an engineer’s account. Long-established practices in [ATO mitigation](https://github.com/magoo/AuthTables) have existed that could have stopped this, but companies rarely take these steps for UX gains. MFA could have been enforced, or email-based verification could have happened for new networks on the account. These are expensive product choices, and I won’t get too deep into those tradeoffs for GitHub, [but in 2023 they’re going full MFA](https://techcrunch.com/2022/05/04/github-will-require-all-users-who-contribute-code-to-enable-two-factor-authentication-by-the-end-of-2023/).

The compromised account belonging to the engineer did not have a multifactor setup on their account. Though, in 2016, GitHub organizations had no way to enforce MFA for all accounts within an organization. This has since changed, possibly pushed forward by this incident. Now you can enforce MFA on an organization. At the time, the incident response efforts forced ~400 employees from GitHub until they could enable 2FA (Pg. 615).

Credential scanning tools could have detected credentials in source code — only if these repositories were known to the security team.

There are two glaring misses upon the use of the leaked credential by the adversary:

First, remote API access was possible with a leaked credential. There was no IAM restriction to prevent unauthorized networks from accessing the API with this credential.

Second, the adversary used an “S3 Browser” tool unseen in production environments I’ve worked in and almost exclusively an indicator of a breach in typical tech company CloudTrail logs. Let’s assume the adversary didn’t change their User Agent; it is a glaring detection miss. However, there is testimony about the adversary’s dedication to OpSec — so we can’t be sure they took this step.

Next, there are general exfiltration detections you can prepare for specific S3 buckets. These are either very high signals or not useful at all. It depends on usage patterns you have for backups and S3 in general, so we can’t be firm on whether this is a good action item.

### **Incident Response**

An incident response fails when the incident cannot be identified, investigated, contained, mitigated, or remediated.

The timeline and actions are clear. The team gets an A+ on the technical response if we put aside other concerns that happen downstream. The testimony largely agrees with this, so we’re probably not getting a clear picture of where things could have improved. Technical response wasn’t a focus of litigation.

### **Attribution**

Attribution capability fails when a threat actor cannot be attributed or the wrong threat actor is attributed.

Mixing up attribution efforts with contract language and bug bounty was too aggressive. It was clear at the time that the whole team believed these were effective tactics for attribution. However, testimony made it clear that some of the team anticipated breach disclosure and law enforcement follow-up. Once a payment went out, it was a bell that could not be unrung. Disclosure needed to happen after this step was taken.

Attribution efforts _strictly succeeded._ The methods used by the team were later dragged through the mud in litigation — but _they worked_ in discovering the home addresses of both threat actors. This creates a complex problem where we either have to exert restraint on using more active methods to identify a threat actor (_Pay money, follow the money_) unless there is a clear-as-day policy that acknowledges that disclosure or law enforcement pursuit is inevitable after being forced to go this route.

## Conclusion

If you remove personal guilt from analysis, you’ll notice organizational causation contributing to the non-disclosure of the 2016 incident. We can’t forget that blameless post-mortem leads to lessons we can all learn and use to improve ourselves… if we’re open to discussing this series of incidents this way. Thanks!

[Ryan McGeehan](http://twitter.com/magoo) writes about security on [scrty.io](https://scrty.io/)

[Security](https://magoo.medium.com/tag/security?source=post_page-----a137162f7fc9---------------------------------------)

[Organizational Culture](https://magoo.medium.com/tag/organizational-culture?source=post_page-----a137162f7fc9---------------------------------------)

[Legal](https://magoo.medium.com/tag/legal?source=post_page-----a137162f7fc9---------------------------------------)

[](https://magoo.medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fstarting-up-security%2Fa137162f7fc9&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fstarting-up-security%2Fa-blameless-post-mortem-of-usa-v-joseph-sullivan-a137162f7fc9&user=Ryan+McGeehan&userId=cf87128497cb&source=---footer_actions--a137162f7fc9---------------------clap_footer------------------)

--

[](https://magoo.medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fstarting-up-security%2Fa137162f7fc9&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fstarting-up-security%2Fa-blameless-post-mortem-of-usa-v-joseph-sullivan-a137162f7fc9&user=Ryan+McGeehan&userId=cf87128497cb&source=---footer_actions--a137162f7fc9---------------------clap_footer------------------)

--

1

[](https://magoo.medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa137162f7fc9&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fstarting-up-security%2Fa-blameless-post-mortem-of-usa-v-joseph-sullivan-a137162f7fc9&source=---footer_actions--a137162f7fc9---------------------bookmark_footer------------------)

[![Image 5: Starting Up Security](https://miro.medium.com/v2/resize:fill:48:48/1*klgju44lCEY1DZWakB1WNw.jpeg)](https://medium.com/starting-up-security?source=post_page---post_publication_info--a137162f7fc9---------------------------------------)

[![Image 6: Starting Up Security](https://miro.medium.com/v2/resize:fill:64:64/1*klgju44lCEY1DZWakB1WNw.jpeg)](https://medium.com/starting-up-security?source=post_page---post_publication_info--a137162f7fc9---------------------------------------)

[## Published in Starting Up Security](https://medium.com/starting-up-security?source=post_page---post_publication_info--a137162f7fc9---------------------------------------)

[1.4K followers](https://magoo.medium.com/starting-up-security/followers?source=post_page---post_publication_info--a137162f7fc9---------------------------------------)

·[Last published Oct 8, 2025](https://magoo.medium.com/starting-up-security/writing-a-risk-scenario-bdbe6e20bfcb?source=post_page---post_publication_info--a137162f7fc9---------------------------------------)

Guides for the growing security team

[![Image 7: Ryan McGeehan](https://miro.medium.com/v2/resize:fill:48:48/0*3kOsPC2HwId9NCAA.jpg)](https://magoo.medium.com/@magoo?source=post_page---post_author_info--a137162f7fc9---------------------------------------)

[![Image 8: Ryan McGeehan](https://miro.medium.com/v2/resize:fill:64:64/0*3kOsPC2HwId9NCAA.jpg)](https://magoo.medium.com/@magoo?source=post_page---post_author_info--a137162f7fc9---------------------------------------)

[## Written by Ryan McGeehan](https://magoo.medium.com/@magoo?source=post_page---post_author_info--a137162f7fc9---------------------------------------)

[2.9K followers](https://magoo.medium.com/@magoo/followers?source=post_page---post_author_info--a137162f7fc9---------------------------------------)

·[186 following](https://magoo.medium.com/@magoo/following?source=post_page---post_author_info--a137162f7fc9---------------------------------------)

Writing about risk, security, and startups at [scrty.io](http://scrty.io/)

## Responses (1)

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--a137162f7fc9---------------------------------------)

![Image 9](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://magoo.medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fstarting-up-security%2Fa-blameless-post-mortem-of-usa-v-joseph-sullivan-a137162f7fc9&source=---post_responses--a137162f7fc9---------------------respond_sidebar------------------)

Cancel

Respond

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----a137162f7fc9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a137162f7fc9---------------------------------------)

[About](https://magoo.medium.com/about?autoplay=1&source=post_page-----a137162f7fc9---------------------------------------)

[Careers](https://magoo.medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a137162f7fc9---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----a137162f7fc9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a137162f7fc9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a137162f7fc9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a137162f7fc9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a137162f7fc9---------------------------------------)