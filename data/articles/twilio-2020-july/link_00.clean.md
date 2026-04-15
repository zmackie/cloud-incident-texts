---
title: "Incident Report: TaskRouter JS SDK July 2020"
url: "https://web.archive.org/web/20210813010417/https://www.twilio.com/blog/incident-report-taskrouter-js-sdk-july-2020"
published: 2020-07
source_type: archive
source_domain: web.archive.org
cleanup_method: llm
---

Twilio believes the security of our customers’ accounts is of paramount importance and when an incident occurs that might threaten that security, we tell you about it.
What happened?
On Sunday July 19th, we became aware of a modification that had been made to a Javascript library that we host for our customers to include in their applications. A modified version of the TaskRouter JS SDK was uploaded to our site at 1:12 PM PDT (UTC-07:00). We received an alert about the modified file at approximately 9:20 PM PDT and replaced it on our site around 10:30 PM PDT. The modified version may have been available on our CDN or cached by user browsers for up to 24 hours after we replaced it on our site.
The TaskRouter JS SDK is a library that allows customers to easily interact with Twilio TaskRouter, which provides an attribute-based routing engine that routes tasks to agents or processes. Due to a misconfiguration in the S3 bucket that was hosting the library, a bad actor was able to inject code that made the user’s browser load an extraneous URL that has been associated with the Magecart group of attacks. This solely affected v1.20 of the TaskRouter JS SDK.
Within 15 minutes of becoming aware of the attack, our product and security teams had convened to contain and remediate the incident. Approximately an hour after the initial alert, we had replaced the bad version of the library and locked down the permissions on the S3 bucket.
We have no evidence at this time that any customer data was accessed by a bad actor. Furthermore, at no time did a malicious party have access to Twilio’s internal systems, code, or data.
For reasons we explore deeper in this analysis, we do not believe this was an attack targeted at Twilio or any of our customers. Instead, this attack appears to be opportunistic and related to a large and well-known campaign to find and exploit open AWS S3 buckets on the Internet for financial gain.
Lastly, while Twilio Flex uses TaskRouter to provide routing of interactions to agents, Flex customers were not impacted by this issue. Twilio Flex uses a different SDK for TaskRouter, does not load it from the public site, and bundles it as part of a single JS file for flex-ui
.
How did it happen?
We had not properly configured the access policy for one of our AWS S3 buckets. One of Twilio’s S3 buckets is used to serve public content from the domain twiliocdn.com
. We host copies of our client-side JavaScript SDKs for Programmable Chat, Programmable Video, Twilio Client, and Twilio TaskRouter on that domain, but only v1.20 of the TaskRouter SDK was impacted by this issue.
While we serve these files to users via CloudFlare’s CDN, they are also available directly from the S3 bucket. We have a set of access policies configured for each path where the files are stored and we had not properly configured the access policy for the path storing the TaskRouter SDK.
Prior to our response to this incident, the S3 access policy for the path that stored v1.20 of taskrouter.min.js
looked like this:
{
"Sid": "AllowPublicRead",
"Effect": "Allow",
"Principal": {
"AWS": "*"
},
"Action": [
"s3:GetObject",
"s3:PutObject"
],
"Resource": "arn:aws:s3:::media.twiliocdn.com/taskrouter/*"
}
That meant that anybody on the Internet could read and write to that specific path. And, on July 19th, at 1:12 PM PDT, someone using the TOR anonymizing network put a modified version of taskrouter.min.js
into that path.
During our incident review, we identified that this path was not initially configured with public write access when it was added in 2015. We implemented a change 5 months later while troubleshooting a problem with one of our build systems and the permissions on that path were not properly reset once the issue had been fixed.
What have we done since then?
Our immediate response steps were to validate the report, contain the impact by locking down the bucket, and upload a clean version of the library to the bucket path. After we completed our initial remediation, we began to investigate two areas in more depth:
- Were there any additional S3 buckets that had bucket policies that made them publicly writable? Were there any additional SDKs that may have been similarly impacted? We conducted a thorough audit of our AWS S3 buckets and found that there were other buckets with improper write settings. One was a backup of the original bucket and had a copy of the access policy. The other buckets we identified did not store production or customer data, and we found no evidence of tampering with them. None of Twilio’s other hosted SDKs had been impacted.
- What was the origin of the malicious JavaScript file? What was the intent of the attacker? Looking at publicly available information, we identified two indicators that link the attack to Magecart (discussed more below). Given how quickly the various links used in these attacks are deprecated and rotated and since the script itself doesn’t execute on all platforms, we can’t definitively tell what impact any individual user might have experienced.
Magecart Behavior
Our investigation of the javascript that was added by the attacker leads us to believe that this attack was opportunistic because of the misconfiguration of the S3 bucket. We believe that the attack was designed to serve malicious advertising to users on mobile devices.
The first indicator we identified is a cookie called jqueryapi1oad
(numeral 1 instead of lowercase letter “L”). This indicator is related to a known malvertising campaign. The script that the attacker added sets this cookie in the browser and then makes a request to a URL embedded in the script. (hxxps://gold[.]platinumus[.]top/track/awswrite?q=dmn)
. That request returns a page with another URL as its only content.
While the URL returned by the first request has changed since we began our investigation, we captured the target that it had been set to (hxxp://presratrasiverin[.]tk/index/?4021528806835)
. The dot-tk toplevel domain is one of the most prevalent domains used by malicious actors because the domains can be obtained for free.
The script returned by the dot-tk URL redirects the user to some other sites, attempts to prevent the user from using their browser back button, and opens new targets transparently. This script also specifically attempts to gather data about the size of the user’s touchscreen and uses events that are targeted at mobile devices. This behavior, along with the indicators, are consistent with a malvertising campaign associated with the Magecart group of attacks targeted at users of mobile devices.
What are we doing to prevent this in the future?
During our incident review, we identified a number of systemic improvements that we can make to prevent similar issues from occurring in the future. Specifically, our teams will be engaging in efforts to:
- Restrict direct access to S3 buckets and deliver content only via our known CDNs.
- Improve our monitoring of S3 bucket policy changes to quickly detect unsafe access policies.
- Determine the best way for us to provide integrity checking so customers can validate that they are using known good versions of our SDKs.
What do you need to do?
If you downloaded a copy of v1.20 of the TaskRouter JS SDK between July 19th, 2020 1:12 PM and July 20th, 10:30 PM PDT (UTC-07:00), you should re-download the SDK immediately and replace the old version with the one we currently serve. You can check the integrity of the TaskRouter JS SDK by running the following command on your copy of taskrouter.min.js
:
diff <(openssl dgst -sha384 -binary taskrouter.min.js | openssl base64 -A) <(printf "n+W3iUCPkW2u64HjqHqOaSFKB6k4BIYw4Fy8BuxDNkrWcCvd9fwnyZKwYjkxqphy")
If your application loads v1.20 of the TaskRouter JS SDK dynamically from our CDN, that software has already been updated and you do not need to do anything.
