---
title: Full Analysis of the PREMINT Attack Incident
url: "https://www.chaincatcher.com/en/article/2076680"
author: Go+ Security
published: 2022-07-18
source_type: article
source_domain: www.chaincatcher.com
cleanup_method: llm
---

# Full Analysis of the PREMINT Attack Incident

**Summary:** The biggest lesson for developers from this attack is that since the web3.0 world cannot exist independently from web2.0, it will inevitably endure the same types of attacks as web2.0. 


_Author: Go+ Security_

On July 17 at 16:00 (UTC+8), [premint.xyz](http://premint.xyz/) was attacked by hackers, resulting in the theft of some users' NFTs. After the incident, GoPlus security analysts quickly conducted a comprehensive analysis and provided security advice from the perspectives of ordinary investors and developers.

### Attack Process

*   The attacker exploited the [premint.xyz](http://premint.xyz/) website by injecting malicious JS scripts. When users performed regular operations, the malicious code was executed, tricking users into signing the authorization operation setApprovalForAll(address,bool). After obtaining the authorization, the attacker stole users' NFTs and other assets.

### Attack Principle

*   When users visit [https://www.premint.xyz/](https://www.premint.xyz/), the website loads the following JS resource file [https://s3-redwood-labs.premint.xyz/theme/js/boomerang.min.js](https://s3-redwood-labs.premint.xyz/theme/js/boomerang.min.js).

![Image 45: image](https://www.chaincatcher.com/upload/image/20220718/1658118010708905.jpg)

*   This file was injected by hackers with a script that loads another attack script file hosted on a fake domain owned by the hackers ([s3-redwood-labs-premint-xyz.com](http://s3-redwood-labs-premint-xyz.com/)) [https://s3-redwood-labs-premint-xyz.com/cdn.min.js?v=1658050292559](https://s3-redwood-labs-premint-xyz.com/cdn.min.js?v=1658050292559). This script contained interactions to deceive users into granting authorization (currently inaccessible).
*   When users performed the regular Verifying your wallet ownership signature (i.e., signing in), this script was triggered, replacing the original verification signature with a transaction that authorized the attacker to transfer users' high-value NFTs. Once this transaction was signed, the assets would be stolen. (Note: The attack script may also deceive users into granting ERC20 token authorization, but since the script is currently inaccessible, we cannot ascertain this.)

### Difficult to Defend Against

*   This attack is likely the hardest for ordinary users to defend against and the easiest to fall victim to.
*   All C-end interactions of the attack occurred on the official Premint website, which easily lulled users into a false sense of security, as people generally assume that official websites are safe.
*   The process of tricking users into signing transactions occurred during the normal signature verification process. Most users do not check the signature details in their wallets (most users do not know how to determine if a signature is safe and, due to trust in the official site, easily overlook the potential risks), making the attack process very covert.

### Where is the Vulnerability?

*   You may wonder why the official Premint website had attack code; this is because the JS resource files hosted on S3 (AWS's object storage service) were compromised and tampered with by hackers.

*   As for why it was compromised, based on existing information, we suspect that there was a misconfiguration in S3, leading to unauthorized access to the Bucket, allowing attackers to list, read, or write to the S3 bucket at will, thus tampering with the JS resource files.

*   The most puzzling aspect of the entire process is that the hacker's attack was discovered at 16:00 (UTC+8) on the 17th, but until 22:00 (UTC+8) on the same day, the Premint official team still had not corrected the attacked JS file, and the boomerang.min.js file still contained the injected malicious script. The page continued to load the hacker's attack script file, although this malicious script itself was no longer accessible (the attack domain [s3-redwood-labs-premint-xyz.com](http://s3-redwood-labs-premint-xyz.com/) is no longer accessible). This state lasted for six hours, making it difficult to determine if the script would reactivate and cause greater losses.

![Image 46: https://api2.mubu.com/v3/document_image/625cf51f-48e4-4ce1-a75c-2fec70925cdc-13536382.jpg](https://api2.mubu.com/v3/document_image/625cf51f-48e4-4ce1-a75c-2fec70925cdc-13536382.jpg)

![Image 47: https://api2.mubu.com/v3/document_image/625cf51f-48e4-4ce1-a75c-2fec70925cdc-13536382.jpg](https://api2.mubu.com/v3/document_image/625cf51f-48e4-4ce1-a75c-2fec70925cdc-13536382.jpg)

### Insights

**Insight 1: What should ordinary investors do? If the official website is unreliable, how can we avoid being deceived?**

*   This attack can be considered a "first encounter kill" for many users who are not technically savvy, as they are 100% likely to fall victim, given that no one would suspect the official website of fraud. However, upon careful consideration, all on-chain transactions must be signed by the wallet, so by paying attention to the signature content, risks can still be identified.
*   Many blockchain users have a very bad habit of performing operations in their wallets without conscious thought, except for adjusting gas fees. In fact, the confirmation information before signing contains a lot of critical content. GoPlus Security advises that everyone must carefully confirm before any signing operation.
*   Taking this attack as an example. When users sign in to Premint for verification, since it is only for information verification and there is no need for on-chain transactions, the initiated Signature Request should only contain Origin information (the requester), the user's address, Nounce information, and possibly some additional return information. As shown below (since [https://www.premint.xyz/](https://www.premint.xyz/) is currently offline, we use Opensea as an example):

![Image 48: https://api2.mubu.com/v3/document_image/93cdd40a-7733-4fc9-9c61-5beac6e8b84f-13536382.jpg](https://api2.mubu.com/v3/document_image/93cdd40a-7733-4fc9-9c61-5beac6e8b84f-13536382.jpg)

*   However, for the transaction signature that was tampered with after being injected with an attack, since it needs to be on-chain, the transaction will present more information in the form of a contract call. For example, in an NFT authorization using setApprovalForAll, it will show where the transaction took place (as shown in etherscan), what method was called (setApprovalForAll), who the authorized party is, and how much ETH was consumed.

![Image 49: https://api2.mubu.com/v3/document_image/26a99589-6d89-49d8-8f89-c0c25cfd24ad-13536382.jpg](https://api2.mubu.com/v3/document_image/26a99589-6d89-49d8-8f89-c0c25cfd24ad-13536382.jpg)

*   Looking back, based on screenshots contributed by netizens, we can see that after Permint was injected with an attack, although the operation prompt was for signature verification, the actual transaction pulling the wallet signature was entirely the on-chain setApprovalForAll, which completely matches the above image. A little observation would reveal that there is a problem here.

![Image 50: image](https://www.chaincatcher.com/upload/image/20220718/1658118106401457.jpg)

*   In fact, various contract calls, transferring ETH (or other native coins), transferring tokens, etc., have different signature information in wallets. All investors should understand these differences to avoid losses when encountering such attacks. GoPlus Security strongly recommends that everyone simulate the operation process to understand the various signature information (as long as the transaction is not sent out, there will be no costs incurred, and there is no tuition fee for learning). Once you learn to look at signature information, you will basically avoid almost all phishing, injection, and fraud attacks.
*   Do not be lazy; learning is the only way to ensure your safety.

**Insight 2: What should developers do? How can we avoid injection attacks?**

*   The biggest insight for developers from this attack is that since the web3.0 world cannot exist independently of web2.0, it will inevitably endure the same attack methods as web2.0. Merely ensuring security at the contract level is not enough; all traditional security preparations must be in place, as any small oversight can lead to significant losses.
*   Additionally, when encountering such issues, immediate repair or isolation is necessary. If there is a sense of complacency and the risk source is not addressed promptly, being ridiculed by security analysts is a minor issue; if the attack method is still usable, losses can continue to accumulate, which is a major issue.
