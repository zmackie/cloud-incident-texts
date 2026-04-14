Title: AWS Ransomware

URL Source: https://dfir.ch/posts/aws_ransomware/

Published Time: 2024-02-21

Markdown Content:
# AWS Ransomware | dfir.ch

[](https://dfir.ch/)- [x] 

*   [Home](https://dfir.ch/)
*   [Posts](https://dfir.ch/posts/)
*   [Talks](https://dfir.ch/talks/)
*   [Tweets](https://dfir.ch/tweets/)
*   |

[](https://dfir.ch/posts/aws_ransomware/#)

# AWS Ransomware

 21 Feb 2024 

**Table of Contents**
*   [Background](https://dfir.ch/posts/aws_ransomware/#background)
*   [Reconnaissance](https://dfir.ch/posts/aws_ransomware/#reconnaissance)
*   [Deletion of Buckets](https://dfir.ch/posts/aws_ransomware/#deletion-of-buckets)
*   [You call it recovery - I call it scam](https://dfir.ch/posts/aws_ransomware/#you-call-it-recovery---i-call-it-scam)
*   [Summary](https://dfir.ch/posts/aws_ransomware/#summary)

## Background

A customer contacted us reporting that an attacker had deleted several AWS S3 buckets (before allegedly downloading the data). Subsequently, the attacker left a ransom note (depicted below, sensitive information has been redacted). In this blog, we examine a recovery binary left behind by the attackers after deleting the buckets and show that the binary is nothing more than a red herring to increase the pressure on the victim.

```
!!! WARNING !!! !!! WARNING !!! !!! WARNING !!! !!! WARNING !!!
 
To recover your lost files and avoid leaking it:
 
Send us 0.2 Bitcoin (BTC) to our Bitcoin addresses 
Price is not standard, depend on your data.
 
Contact us by email to confirm 
restore@<redacted>.com
 
example: 
1Krx5mJNqW8[...]
13o2MSsNNDP[...]
 
Linux
tar xzvf recoveryAKIAZ5ESTHWPHSNVAXZ7.tgz
chmod +x recovery
./recovery
 
You need to be authenticated into aws-cli with credentials to perform restore
run -> aws configure and authenticate if you are not already !
Once the recovery starts, you need to be sure your connection does not drop, your computer does not crash
 
Once you contact us we will explain how to avoid further attacks.
 
Contact us by email to confirm and attach file warning.txt
restore@<redacted>.com
 
 
AKIA S3 backup
 
Your files are downloaded and backed up on our servers. If we dont receive your payment in the next 5 days, we 
will sell your files to the highest bidder or use them otherwise or permanently deleted. We also extract sensitive informations.
```

Another version of this ransom note, lacking the recovery component, has been uploaded to [VirusTotal](https://www.virustotal.com/gui/file/3f759783fc0e6ec98a6e5d7c87336a87e5281fd1029ee3f8c7f2bb75299d140b/detection). It was initially submitted on January 29, 2024, from France, matching roughly our timeline.

## Reconnaissance

We traced the initial actions of the attacker back to January 18, 2024, when they executed two standard reconnaissance commands against the AWS Simple Email Solution (SES) and Amazon Simple Storage Service (S3):

*   _GetSendQuota_
*   _ListBuckets_

[Invictus-IR](https://www.invictus-ir.com/) created [a CSV file](https://gist.github.com/invictus-ir/2e892e19aad49eafe449fae91b2ff25b#file-cloudtrail-csv) with interesting CloudTrail events from [another ransomware incident in the cloud](https://www.invictus-ir.com/news/ransomware-in-the-cloud). It is highly recommended that defenders and SOC members check their security monitoring for these event names, as these events could tell that an attacker has access to an AWS endpoint.

![Image 1: Important CloudTrail event logs](https://dfir.ch/images/aws/cloud_trail.png)

Figure 1: Important CloudTrail event logs

## Deletion of Buckets

On February 5th 2024, the attacker utilized the command _DeleteBucket_ to erase all buckets, leaving behind the previously mentioned ransom note. Before the deletion of the buckets, the following commands were recorded in the CloudTrail logs:

*   _GetBucketVersioning_ (see Figure 1 - versioning was not enabled)
*   _GetBucketReplication_
*   _GetBucketObjectLockConfiguration_
*   _GetBucketLogging_
*   _GetBucketRequestPayment_
*   _GetAccelerateConfiguration_

## You call it recovery - I call it scam

Within the ransom note, the following three Linux commands are mentioned:

*   tar xzvf recoveryBYESZ2ESTHWPWHDRAXZ7.tgz
*   chmod +x recovery
*   ./recovery

The attacker placed the archive (recoveryBYESZ2ESTHWPWHDRAXZ7.tgz) in the same folder as the ransom note, including a text file called _aws.txt_. The complete archive includes numerous unrelated folders containing Linux libraries, C source code files, Python files, etc., to boost the archive size and give the archive a more ‘serious’ touch.

Focusing only on the recovery part, we read the following statement inside the ransom note:

_You need to be authenticated into aws-cli with credentials to perform restore run -> aws configure and authenticate if you are not already ! Once the recovery starts, you need to be sure your connection does not drop, your computer does not crash_

**Analysis of the binary**

The recovery binary (called simply _recovery_, see above) was initially [uploaded to VirusTotal](https://www.virustotal.com/gui/file/3440b4fc74f51d5104deb38924ec821f7f7b8ecd585667f84d4743dd305eb2ba/detection) on February 2nd, 2024. Upon launching the recovery binary, it prompts us for the AWS key. Subsequently, the binary informs us that it verifies the account information and prints details about it.

```shell
Welcome to AWS recovery
Please enter your AWS: malmoeb
Please enter your AWS key: malmoeb_key
Checking ...
Account Information:
    "UserId": "AIDAZ[...]",
    "Account": "6810[...]",
    "Arn": "arn:aws:iam::6810:user/<redacted>"
Creating folder: dfir
Total number of files: 240
Total size (GB): 5.00 GB
```

After entering the AWS key, the binary indicates it is checking something. However, based on the strace output (see my post about using [strace for Linux malware analysis](https://dfir.ch/posts/strace/)), the code sleeps for five seconds (the number 5 was passed on as an argument to the system call [clock_nanosleep](https://man7.org/linux/man-pages/man2/clock_nanosleep.2.html)).

```shell
write(1, "Checking ...\n", 13)          = 13
clock_nanosleep(CLOCK_REALTIME, 0, {tv_sec=5, tv_nsec=0}, 0x7ffeb42cb290) = 0
```

Upon further examination of this behavior, we discover a call to the _sleepRandom()_ function, directing the binary to sleep for a random duration. This aligns with the observed behavior in the strace output.

![Image 2: Welcome to AWS recovery](https://dfir.ch/images/aws/checking.png)

Figure 2: Welcome to AWS recovery

The _sleepRandom()_ function utilize the _sleep()_ function under the hood:

![Image 3: sleepRandom() function](https://dfir.ch/images/aws/sleepRandom.png)

Figure 3: sleepRandom() function

The aforementioned account information was retrieved from the file _aws.txt_, which was included within the “recovery package” alongside the recovery binary. Below is a mockup version of the file:

```shell
$ cat aws.txt 
Account Information:
{
    "UserId": "AIDAZ",
    "Account": "6810",
    "Arn": "arn:aws:iam::6810:user/malmoeb"
}

Buckets for the user with access key 2345:
2022-09-02 18:55:18 dfir

Folder Names:
dfir

Folder: dfir
Number of files: 240
Total size (GB): 5.00 GB

Total number of files: 240
```

Here is an excerpt from the strace output, showing the process of reading the aws.txt file ([openat()](https://linux.die.net/man/2/openat) followed by [read()](https://linux.die.net/man/3/read)):

```shell
openat(AT_FDCWD, "aws.txt", O_RDONLY)   = 3
fstat(3, {st_mode=S_IFREG|0664, st_size=355, ...}) = 0
read(3, "Account Information:\n{\n    \"User"..., 4096) = 355
clock_nanosleep(CLOCK_REALTIME, 0, {tv_sec=2, tv_nsec=0}, 0x7ffeb42cb290) = 0
write(1, "Account Information:\n", 21)  = 21
[...]
```

The binary generates a new directory ([mkdir](https://linux.die.net/man/2/mkdir)) and places randomly named files within it. The [openat()](https://linux.die.net/man/2/openat) syscall is used again, but this time, unlike above, the parameter _O\_CREAT_ is passed to the function - _If pathname does not exist, create it as a regular file._

```shell
mkdir("dfir", 0777)                     = 0
clock_nanosleep(CLOCK_REALTIME, 0, {tv_sec=0, tv_nsec=738335000}, NULL) = 0
chdir("dfir")                           = 0
openat(AT_FDCWD, "recoveryqbhcdarzow.bkp", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 4
close(4)                                = 0
openat(AT_FDCWD, "recoverykkyhiddqsc.bkp", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 4
close(4)                                = 0
[...]
```

Upon revisiting the binary in [Ghidra](https://ghidra-sre.org/), we observe that the following two functions are responsible for creating files and folders:

*   _createFoldersFromFile();_
*   _displayFileInfo();_

To create the folders, the binary reads the bucket names from the aws.txt file and generates a folder for each bucket.

![Image 4: createFoldersFromFile()](https://dfir.ch/images/aws/creating_folders.png)

Figure 4: createFoldersFromFile()

The total number of files and the total file size are calculated exclusively from the information provided in the aws.txt file - the binary does not connect to the Internet or AWS.

![Image 5: displayFileInfo(](https://dfir.ch/images/aws/total_files.png)

Figure 5: displayFileInfo()

Similar to verifying the AWS access key, the downloading process is a red herring, as evidenced by the strace log.

```shell
write(1, "Downloading [\r[                 "..., 95) = 95
clock_nanosleep(CLOCK_REALTIME, 0, {tv_sec=1, tv_nsec=0}, 0x7ffeb42cb2c0) = 0
```

While executing the binary, after displaying the “Downloading” message, the terminal prints the following message: “Download has been paused - please make payment.” Upon investigating the download functionality of the binary, it was obvious that not a single line of code initiates a network connection to check keys, buckets, or access rights.

![Image 6: Download has been paused](https://dfir.ch/images/aws/downloading.png)

Figure 6: Download has been paused

The _Download has been paused_ message is yet another red herring, tricking the victim into paying the ransom. The user is prompted to enter the Transaction ID/Hash of the paid ransom, however, once again, the binary does nothing with the information entered by the user besides increasing the pressure on the victim.

Finally, the “downloading” of the data will continue, showing the user how much time is left until completion.

![Image 7: Transaction ID/Hash](https://dfir.ch/images/aws/hash.png)

Figure 7: Transaction ID/Hash

```
[                 ] 0.00% Speed: 550.00 K/s ETA: 405:13:56
[                 ] 0.00% Speed: 550.00 K/s ETA: 405:13:54
```

The analysis of the binary has shown that nothing is checked behind the curtains; not a single domain is contacted, nor was a network connection done.

![Image 8: Time until recovery is finished](https://dfir.ch/images/aws/speed.png)

Figure 8: Time until recovery is finished

[ELF DIGEST](https://twitter.com/elfdigest), the non-profit Linux malware analysis service, also does not find any trace of network connections. [Here](https://elfdigest.com/report/3440b4fc74f51d5104deb38924ec821f7f7b8ecd585667f84d4743dd305eb2ba) is the report from which we took the screenshot (requires a user name).

![Image 9: Report from ELF Digest()](https://dfir.ch/images/aws/elfdigest.png)

Figure 9: Report from ELF Digest

## Summary

The network traffic analysis showed that the attackers most likely stole solely 2 GB of data, compared to the over 1 TB of data available on the bucket. Thus, a restore would not have been possible anyway. The whole “recovery” binary is just a neat trick the attackers use to trick the victims into paying the ransom. The analysis with a dynamic approach (strace) and a static one (Ghidra) proved successful, allowing us to quickly gain insights into the binary.

[](https://dfir.ch/posts/aws_ransomware/)[](https://buymeacoffee.com/malmoeb "Buymeacoffee")[](https://twitter.com/malmoeb "Twitter")[](https://www.linkedin.com/in/stephan-berger-59575a20a/ "Linkedin")[](https://infosec.exchange/@malmoeb "Mastodon")[](https://bsky.app/profile/malmoeb.bsky.social "Bluesky")

 © 2025 . Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome). [](https://dfir.ch/posts/aws_ransomware/# "Go to top")