This communication is to keep you informed about the latest status of our security incident on May 31, 2017, and what we’re doing about it. Our goal from the start of this incident has been to provide the most comprehensive set of remediation steps to our customers as possible based on the facts available, and at this stage of our review we do not anticipate any significant changes to this list.
As we have shared in more detail in our previous communication, we know that a threat actor used one of our AWS keys to gain access to our AWS platform via API from an intermediate host with another, smaller service provider in the US. OneLogin staff detected the intrusion and within minutes shut down the affected instances as well as the compromised AWS keys to stop the intrusion and confirmed there were no other active threats.
We have implemented several improvements to strengthen our infrastructure to help mitigate the risk of future intrusion. In consultation with AWS, external cybersecurity experts, and in collaboration with key customers with relevant expertise, we have focused our attention on the following areas:
- Fine-tune monitoring of AWS API endpoint signals
- Strengthen AWS key management
- Enhance infrastructure and application encryption
- Expand threat hunting activities
- Create additional in-app risk mitigation tools
Looking forward, we continue to examine options to further harden our platform and to add new foundational capabilities to provide our customers additional security and control over their data.
Updated post, June 1, 2017
As we communicated yesterday, we recently detected that a malicious actor had obtained access to our US operating region. Although our review is ongoing and the facts subject to change, we wanted to provide you with an update about the facts we know thus far.
Method of attack
Our review has shown that a threat actor obtained access to a set of AWS keys and used them to access the AWS API from an intermediate host with another, smaller service provider in the US. Evidence shows the attack started on May 31, 2017 around 2 am PST. Through the AWS API, the actor created several instances in our infrastructure to do reconnaissance. OneLogin staff was alerted of unusual database activity around 9 am PST and within minutes shut down the affected instance as well as the AWS keys that were used to create it.
Customer impact
The threat actor was able to access database tables that contain information about users, apps, and various types of keys. While we encrypt certain sensitive data at rest, at this time we cannot rule out the possibility that the threat actor also obtained the ability to decrypt data. We are thus erring on the side of caution and recommending actions our customers should take, which we have already communicated to our customers.
Going forward
OneLogin’s investigation is ongoing, and is aided by independent third-party security experts, as well as law enforcement. We will update this when there is more information we can share, as appropriate. We thank you again for your continued support.
Original post, May 31, 2017 Security Incident
Today we detected unauthorized access to OneLogin data in our US data region. We have since blocked this unauthorized access, reported the matter to law enforcement, and are working with an independent security firm to determine how the unauthorized access happened and verify the extent of the impact of this incident. We want our customers to know that the trust they have placed in us is paramount.
While our investigation is still ongoing, we have already reached out to impacted customers with specific recommended remediation steps and are actively working to determine how best to prevent such an incident from occurring in the future and will update our customers as these improvements are implemented.
For more information on our security practices, see our Compliance Page.
Alvaro Hoyos,
Chief Information Security Officer