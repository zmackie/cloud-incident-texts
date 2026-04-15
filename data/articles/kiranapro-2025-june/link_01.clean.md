---
title: "KiranaPro Crisis Explained: Ex-Employee's Revenge Move that Paralysed the App"
url: "https://www.outlookbusiness.com/start-up/explainers/kiranapro-crisis-explained-ex-employees-revenge-move-that-paralysed-the-app"
author: Shashank Bhatt
published: 2025-06-10
source_type: article
source_domain: www.outlookbusiness.com
cleanup_method: llm
---

# KiranaPro Crisis Explained: Ex-Employee’s Revenge Move that Paralysed the App

Grocery‑tech startup KiranaPro suffered a major data wipe when a disgruntled ex-employee gained root access to AWS and GitHub, deleting critical code and user data. The team is restoring from backups, investigating the insider attack, and pursuing legal action

[Shashank Bhatt](https://www.outlookbusiness.com/author/shashank-bhatt)

One of the worst nightmares of a start‑up founder is losing their sacred data accumulated over years of building the firm and failing to deliver the services to their users on which the entire system is based. For [grocery‑tech start‑up](https://www.outlookbusiness.com/news/quick-commerce-captures-nearly-half-of-kirana-sales-market-projected-to-hit-40-billion-by-2030)KiranaPro, this nightmare became reality last week when the founder confirmed that all its app data, including the firm’s app code and its servers, had been wiped.

The outage, initially speculated to be a cyberattack, later turned out to be insider sabotage by a trusted ex‑employee.

## Crisis

On June 3, KiranaPro co-founder and CEO Deepak Ravindran told TechCrunch that the attackers destroyed critical data on the company’s servers, including the app code and user information such as names, mailing addresses and payment details.

As per initial reports, the breach occurred via a former employee’s account, with KiranaPro’s CTO Saurav Kumar noting that the attack likely happened between May 24 and May 25.

Despite using Google Authenticator for multi‑factor authentication on AWS, the authentication code had been changed before executives attempted to log in. Upon access, KiranaPro employees found that all Elastic Compute Cloud (EC2) instances had been deleted.

“We can only log in through the IAM account, through which we can see that the EC2 instances don’t exist anymore, but we are not able to get any logs or anything because we don’t have the root account,” Kumar said.

KiranaPro has reached out to GitHub support to identify the attacker’s IP addresses. Ravindran also mentioned that the start‑up is in the process of filing cases against former employees who have not submitted their credentials for accessing GitHub logs.

## Insider Sabotage

On June 6, Ravindran stated in a LinkedIn post that KiranaPro’s internal investigation into the data‑wipe crisis revealed it was not an external cyberattack but an act of sabotage by a former employee seeking revenge.

Ravindran shared the name of the ex‑employee and stated that all remedies had been implemented to resolve the issue amicably, avoiding a legal battle.

KiranaPro also contacted GitHub support to identify the attacker’s IP addresses and is pursuing actions against former employees who have not provided credentials for accessing GitHub logs.

By June 9 and 10, deeper investigations confirmed that the sabotage was perpetrated by a “trusted” ex‑employee, reportedly named Lava Kumar, who deliberately deleted critical systems after being laid off. This revelation solidified the insider nature of the incident, highlighting the severe risks of disgruntled former employees retaining access to sensitive systems.

## Recovery Efforts

Recently, Ravindran told TechCrunch that the GitHub data was restored using a backup provided by one of their employees, and the start‑up regained access to its AWS account along with its customer data.

Both Ravindran and Kumar confirmed the [AWS account](https://www.outlookbusiness.com/corporate/aws-announces-230m-investment-to-global-generative-ai-accelerator-for-early-stage-start-ups)was protected by MFA, but neither could explain how the account was accessed, as nobody else had access to Ravindran’s phone, which generated the MFA codes.

Ravindran claimed that the customer data stored in the AWS cloud remained intact and was not accessed by any third parties, nor was it downloaded by the former employee. “Because if that is the case, I will get its notification by email or anything,” he said.

While the service was disrupted, the app remained online in a limited capacity and is in the process of being rebuilt from scratch with fresh code and restored infrastructure.

Nonetheless, Ravindran stated that KiranaPro has sufficient evidence to file a formal complaint with the police, though the start‑up’s investigation is ongoing.

## Delayed Salaries

In addition to the data crisis, media reports, including an initial report by The CapTable, have highlighted significant operational challenges at KiranaPro, detailing how several current and former employees have gone without pay for weeks or months.

Screenshots reviewed by Moneycontrol showed unanswered emails and vague responses to requests for final dues. Ravindran did not dispute these claims, acknowledging the salary delays.

“Some of the employees did not get their salaries on time, because we did not process the payments and internal approvals on schedule. It is my mistake, and I again apologize for it,” he said. He added, “We have just hired a CFO three weeks ago and are fixing things step by step.”

Ravindran noted that most dues for current employees were partially cleared on June 5, and nearly all former employees have been paid, following the company’s recent financial stabilisation.
