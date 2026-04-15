Title: how to completely own an airline in 3 easy steps

URL Source: https://maia.crimew.gay/posts/how-to-hack-an-airline/

Published Time: 2023-01-19T00:00:00.000Z

Markdown Content:
# how to completely own an airline in 3 easy steps

# maia blog

[home](https://maia.crimew.gay/)|[blog](https://maia.crimew.gay/posts/)|[citations](https://maia.crimew.gay/citations/)|[contact](https://maia.crimew.gay/contact/)|[shop](https://shop.crimew.gay/)|[sample packs](https://maia.crimew.gay/samples/)

![Image 1: a glitchy edited photo of an airplane](https://maia.crimew.gay/img/posts/how-to-hack-an-airline/cover.jpg)

Jan 19, 2023(updated Jan 22, 2023)4 minutes to read by maia arson crimew in [leak](https://maia.crimew.gay/posts/tagged/leak/), [security](https://maia.crimew.gay/posts/tagged/security/), [infosec](https://maia.crimew.gay/posts/tagged/infosec/), [jenkins](https://maia.crimew.gay/posts/tagged/jenkins/), [aviation](https://maia.crimew.gay/posts/tagged/aviation/), [nofly](https://maia.crimew.gay/posts/tagged/nofly/)

# how to completely own an airline in 3 easy steps

**and grab the TSA nofly list along the way**
_note: this is a slightly more technical* and comedic write up of the story covered by my friends over at dailydot, which you can read [here](https://www.dailydot.com/debug/no-fly-list-us-tsa-unprotected-server-commuteair/)_

_i say slightly since there isnt a whole lot of complicated technical stuff going on here in the first place_

## step 1: boredom

like so many other of my hacks this story starts with me being bored and browsing [shodan](https://shodan.io/) (or well, technically [zoomeye](https://www.zoomeye.org/), chinese shodan), looking for exposed [jenkins](https://jenkins.io/) servers that may contain some interesting goods. at this point i've probably clicked through about 20 boring exposed servers with very little of any interest, when i suddenly start seeing some familar words. "[ACARS](https://en.wikipedia.org/wiki/ACARS)", lots of mentions of "crew" and so on. lots of words i've heard before, most likely while binge watching [Mentour Pilot](https://youtube.com/c/MentourPilotaviation) YouTube videos. jackpot. an exposed jenkins server belonging to [CommuteAir](https://en.wikipedia.org/wiki/CommuteAir).

![Image 2: zoomeye search for x-jenkins](https://maia.crimew.gay/img/posts/how-to-hack-an-airline/zoomeye.jpg)

## step 2: how much access do we have really?

ok but let's not get too excited too quickly. just because we have found a funky jenkins server doesn't mean we'll have access to much more than build logs. it quickly turns out that while we don't have anonymous admin access (yes that's quite frequently the case [god i love jenkins]), we do have access to build workspaces. this means we get to see the repositories that were built for each one of the ~70 build jobs.

## step 3: let's dig in

most of the projects here seem to be fairly small spring boot projects. the standardized project layout and extensive use of the resources directory for configuration files will be very useful in this whole endeavour.

the very first project i decide to look at in more detail is something about "ACARS incoming", since ive heard the term acars before, and it sounds spicy. a quick look at the resource directory reveals a file called `application-prod.properties` (same also for `-dev` and `-uat`). it couldn't just be that easy now, could it?

well, it sure is! two minutes after finding said file im staring at [filezilla](https://filezilla-project.org/) connected to a [navtech](https://www.navblue.aero/) sftp server filled with incoming and outgoing ACARS messages. this aviation shit really do get serious.

![Image 3: a photo of a screen showing filezilla navigated to a folder called ForNavtech/ACARS_IN full of acars messages, the image is captioned like a meme with "this aviation shit get serious"](https://maia.crimew.gay/img/posts/how-to-hack-an-airline/this-aviation-shit-get-serious.jpg)

here is a sample of a departure ACARS message:

![Image 4: screenshot of a terminal showing what an ACARS RCV file shows like](https://maia.crimew.gay/img/posts/how-to-hack-an-airline/acars-sample.jpg)

from here on i started trying to find journalists interested in a probably pretty broad breach of US aviation. which unfortunately got peoples hopes up in thinking i was behind the TSA problems and groundings a day earlier, but unfortunately im not quite that cool. so while i was waiting for someone to respond to my call for journalists i just kept digging, and oh the things i found.

as i kept looking at more and more config files in more and more of the projects, it dawned on me just how heavily i had already owned them within just half an hour or so. hardcoded credentials there would allow me access to navblue apis for refueling, cancelling and updating flights, swapping out crew members and so on (assuming i was willing to ever interact with a SOAP api in my life which i sure as hell am not).

i however kept looking back at the two projects named `noflycomparison` and `noflycomparisonv2`, which seemingly take the TSA nofly list and check if any of commuteair's crew members have ended up there. there are hardcoded credentials and s3 bucket names, however i just cant find the actual list itself anywhere. probably partially because it seemingly always gets deleted immediately after processing it, most likely specifically because of nosy kittens like me.

![Image 5: heavily redacted example of a config file from one of the repositories](https://maia.crimew.gay/img/posts/how-to-hack-an-airline/config-example.jpg)

fast forward a few hours and im now talking to [Mikael Thalen](https://twitter.com/MikaelThalen), a staff writer at dailydot. i give him a quick rundown of what i have found so far and how in the meantime, just half an hour before we started talking, i have ended up finding AWS credentials. i now seemingly have access to pretty much their entire aws infrastructure via `aws-cli`. numerous s3 buckets, dozens of dynamodb tables, as well as various servers and much more. commute really loves aws.

![Image 6: two terminal screenshots composed together showing some examples of aws buckets and dynamodb tables](https://maia.crimew.gay/img/posts/how-to-hack-an-airline/aws-overview.jpg)

i also share with him how close we seemingly are to actually finding the TSA nofly list, which would obviously immediately make this an even bigger story than if it were "only" a super trivially ownable airline. i had even peeked at the nofly s3 bucket at this point which was seemingly empty. so we took one last look at the noflycomparison repositories to see if there is anything in there, and for the first time actually take a peek at the test data in the repository. and there it is. three csv files, `employee_information.csv`, `NOFLY.CSV` and `SELECTEE.CSV`. all commited to the repository in july 2022. the nofly csv is almost 80mb in size and contains over 1.56 million rows of data. this HAS to be the real deal (we later get confirmation that it is indeed a copy of the nofly list from 2019).

holy shit, we actually have the nofly list. holy fucking bingle. what?! :3

![Image 7: me holding a sprigatito pokemon plushie in front of a laptop screen showing a very blurry long csv list in vscode](https://maia.crimew.gay/img/posts/how-to-hack-an-airline/weed-cat-crimes.jpg)

with the jackpot found and being looked into by my journalism friends i decided to dig a little further into aws. grabbing sample documents from various s3 buckets, going through flight plans and dumping some dynamodb tables. at this point i had found pretty much all PII imaginable for each of their crew members. full names, addresses, phone numbers, passport numbers, pilot's license numbers, when their next [linecheck](https://icadet.com/aviation-term/line-check/) is due and much more. i had trip sheets for every flight, the potential to access every flight plan ever, a whole bunch of image attachments to bookings for reimbursement flights containing yet again more PII, airplane maintenance data, you name it.

i had owned them completely in less than a day, with pretty much no skill required besides the patience to sift through hundreds of shodan/zoomeye results.

## so what happens next with the nofly data

while the nature of this information is sensitive, i believe it is in the public interest for this list to be made available to journalists and human rights organizations. if you are a journalist, researcher, or other party with legitimate interest, the data is available for access (upon request) [via DDoSecrets](https://ddosecrets.org/wiki/No_Fly_List).

[if you enjoyed this or any of my other work feel free to support me on my ko-fi. this is my main source of income so anything goes a long way, and monthly contributions help tremendously with budgeting. <3](https://ko-fi.com/nyancrimew)

### related posts

*   [#### infosec company owned completely by 4chan user](https://maia.crimew.gay/posts/optimeyes-leak/)May 10, 2023 2 minutes to read by maia arson crimew in [leak](https://maia.crimew.gay/posts/tagged/leak/), [security](https://maia.crimew.gay/posts/tagged/security/), [infosec](https://maia.crimew.gay/posts/tagged/infosec/), [jenkins](https://maia.crimew.gay/posts/tagged/jenkins/), [analysis](https://maia.crimew.gay/posts/tagged/analysis/) **risk visualize deez nuts**
*   [#### so i guess i hacked samsung?!](https://maia.crimew.gay/posts/i-hacked-samsung/)Apr 1, 2024 3 minutes to read by maia arson crimew in [bug bounty](https://maia.crimew.gay/posts/tagged/bug-bounty/), [leak](https://maia.crimew.gay/posts/tagged/leak/), [security](https://maia.crimew.gay/posts/tagged/security/), [infosec](https://maia.crimew.gay/posts/tagged/infosec/), [jenkins](https://maia.crimew.gay/posts/tagged/jenkins/), [cloud](https://maia.crimew.gay/posts/tagged/cloud/) **it's not quite xz but at least my grandma knows what samsung is**
*   [#### KittenSec leaks romanian and EU government data](https://maia.crimew.gay/posts/kittensec-opromania/)Jul 30, 2023 1 minute to read by maia arson crimew in [leak](https://maia.crimew.gay/posts/tagged/leak/), [security](https://maia.crimew.gay/posts/tagged/security/), [infosec](https://maia.crimew.gay/posts/tagged/infosec/), [politics](https://maia.crimew.gay/posts/tagged/politics/) **a promising new kitten on the block**

![Image 8: a small white kitten with black spots walking across the screen](https://maia.crimew.gay/img/walkingkitten_crop.png)

[atom/rss feed](https://maia.crimew.gay/feed.xml)|[ko-fi](https://ko-fi.com/nyancrimew)|[tumblr](https://tumblr.com/nyancrimew)|[twitter](https://twitter.com/awawawhoami)|[fediverse](https://soc.tuxpaintadventures.com/@maia)|[bluesky](https://bsky.app/profile/crimew.gay)|[instagram](https://instagram.com/nyancrimew)|[letterboxd](https://letterboxd.com/nyancrimew/)|[soundcloud](https://soundcloud.com/nyancrimew)|[last dot federated states of micronesia](https://last.fm/user/nyancrimew)|[github](https://github.com/nyancrimew)|[analytics](https://umami.crimew.gay/share/M77OUJ83Q4qBcOjZ/maia.crimew.gay)

credits: maia kitten art by [vai5000](https://twitter.com/vai5000_), pixel art maia kitten by [A. Marmot](https://twitter.com/_Anunnery) and pointer following kitten code from [adryd325/oneko.js](https://github.com/adryd325/oneko.js)

[![Image 9: maia crimew](https://maia.crimew.gay/badges/maia.crimew.gay.png)](https://maia.crimew.gay/)[![Image 10: 88x31](https://maia.crimew.gay/badges/88x31.gif)](https://cyber.dabamos.de/88x31)![Image 11: don't click here](https://maia.crimew.gay/badges/noclick.gif)![Image 12: acab](https://maia.crimew.gay/badges/acab.gif)[![Image 13: arch linux](https://maia.crimew.gay/badges/archlinux.gif)](https://archlinux.org/)[![Image 14: versary town](https://maia.crimew.gay/badges/versarytown.png)](https://versary.town/)[![Image 15: goop house](https://maia.crimew.gay/badges/goop.gif)](https://goop.house/)![Image 16: anarchy now](https://maia.crimew.gay/badges/anarchynow.gif)![Image 17: sleepy zone](https://maia.crimew.gay/badges/sleepy.png)![Image 18: kitten's corner](https://maia.crimew.gay/badges/kitten88.gif)[![Image 19: oat.zone](https://maia.crimew.gay/badges/oatzone.gif)](https://oat.zone/)![Image 20: slimes now](https://maia.crimew.gay/badges/slimesnow.png)![Image 21: slugcat](https://maia.crimew.gay/badges/slugcat.png)[![Image 22: sinewave](https://maia.crimew.gay/badges/sinewave.gif)](https://sinewave.cyou/)![Image 23: non-binary pride](https://maia.crimew.gay/badges/nonbinary.png)![Image 24: queer pride](https://maia.crimew.gay/badges/queer.png)![Image 25: piracy now](https://maia.crimew.gay/badges/piracy.gif)[![Image 26: utsuho rocks](https://maia.crimew.gay/badges/utsuhorocks.png)](https://utsuho.rocks/)[![Image 27: ilwag.com](https://maia.crimew.gay/badges/ilwagbannersmol.png)](https://ilwag.com/)[![Image 28: solely](https://maia.crimew.gay/badges/solely.png)](https://arciniega.one/)[![Image 29: les.bi](https://maia.crimew.gay/badges/lesbi.png)](https://les.bi/)[![Image 30: adryd](https://maia.crimew.gay/badges/adryd.png)](https://adryd.com/)[![Image 31: notnite](https://maia.crimew.gay/badges/notnite.png)](https://notnite.com/)[![Image 32: aspyn.gay](https://maia.crimew.gay/badges/aspyn.gif)](https://aspyn.gay/)[![Image 33: mallory](https://maia.crimew.gay/badges/mallory.png)](https://bunny.gift/)[![Image 34: besties](https://maia.crimew.gay/badges/besties.gif)](https://besties.house/)[![Image 35: glauca digital, domains, hosting, dns](https://maia.crimew.gay/badges/glauca.gif)](https://glauca.digital/)

[sleepy.zone](http://sleepy.zone/) webring!
*   [tayxm](https://tayxm.neocities.org/)
*   [maia](https://maia.crimew.gay/)
*   [sadgirlsclub](https://sadgirlsclub.wtf/)