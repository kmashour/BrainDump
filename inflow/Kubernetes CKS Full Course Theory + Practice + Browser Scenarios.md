---
title: "Kubernetes CKS Full Course Theory + Practice + Browser Scenarios"
source: "https://www.youtube.com/watch?v=d9xfB5qaOfg&t=2s"
author:
  - "[[Killer Shell]]"
published: 2024-01-15
created: 2026-09-25
description: "Certified Kubernetes Security Specialist (CKS) preparation!!!! USE Ubuntu 24.04 instances instead of the 20.04 shown in the video !!!This course does not include the 2024 changes and missing topic"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=d9xfB5qaOfg)

Certified Kubernetes Security Specialist (CKS) preparation!  
  
!!! USE Ubuntu 24.04 instances instead of the 20.04 shown in the video !!!  
  
This course does not include the 2024 changes and missing topics are: Cilium, PodSecurityStandards and SBOM. But these are included on https://killer.sh/cks and https://killercoda.com/killer-shell-cks.  
  
I will present each CKS topic in a simple and visual way. We'll run through various practical hands-on challenges.  
You'll setup own CKS cluster in which you'll learn, simple install scripts are provided.  
Instead of creating your own cluster you can also use the in-browser playground for mostly everything: https://killercoda.com/killer-shell-cks/scenario/playground.  
There are additional in-browser interactive scenarios to further study and harden your knowledge!  
  
Killercoda Scenarios: https://github.com/killer-sh/cks-course-environment/blob/master/Scenarios.md  
Section Resources: https://github.com/killer-sh/cks-course-environment/blob/master/Resources.md  
Github: https://github.com/killer-sh/cks-course-environment  
Slack Community: https://killer.sh/slack (channel cks)  
  
Chapters:  
00:00:00 Introduction and Welcome  
00:02:50 K8s Security Best Practices  
00:13:07 Create your course K8s cluster  
00:35:49 Crictl instead of Docker  
00:38:02 Foundation - Kubernetes Secure Architecture  
00:57:27 Foundation - Containers under the hood  
01:18:12 Cluster Reset  
01:18:53 Cluster Setup - Network Policies  
01:46:54 Cluster Setup - GUI Elements  
02:02:06 K8s Docs Version  
02:02:48 Cluster Setup - Secure Ingress  
02:23:54 Cluster Setup - Node Metadata Protection  
02:34:13 Cluster Setup - CIS Benchmarks  
02:47:47 Cluster Setup - Verify Platform Binaries  
02:58:23 Cluster Hardening - RBAC  
03:31:26 Cluster Hardening - Exercise caution in using ServiceAccounts  
03:49:06 Cluster Hardening - Restrict API Access  
04:17:25 Cluster Hardening - Upgrade Kubernetes  
04:38:59 Microservice Vulnerabilities - Manage Kubernetes Secrets  
05:26:44 Microservice Vulnerabilities - Container Runtime Sandboxes  
05:55:19 Microservice Vulnerabilities - OS Level Security Domains  
06:12:01 Microservice Vulnerabilities - mTLS  
06:27:12 Cluster Reset  
06:27:54 Open Policy Agent (OPA)  
07:07:33 Supply Chain Security - Image Footprint  
07:29:37 Supply Chain Security - Static Analysis  
07:52:39 Supply Chain Security - Image Vulnerability Scanning  
08:06:26 Supply Chain Security - Secure Supply Chain  
08:32:01 Runtime Security - Behavioral Analytics at host and container level  
09:16:36 Runtime Security - Immutability of containers at runtime  
09:34:24 Runtime Security - Auditing  
10:06:46 System Hardening - Kernel Hardening Tools  
10:45:41 System Hardening - Reduce Attack Surface  
11:05:20 CKS Simulator  
  
Please expect this course to take more time than just the recorded hours. For most topics you'll need some time to implement the scenarios yourself. Also breaks (hours or even days) between sections/topics should be advised to prevent brain implosion :)  
  
You should already have some Kubernetes Administrator knowledge before attending this course. And if you like to attend the real CKS exam you need to hold a valid CKA certification. But I also do some recap of CKA knowledge at the beginning, so no worries if your knowledge is a bit stale.  
  
Would you like to support this course? Consider subscribing to the Killercoda PLUS membership, even if just for a month! https://killercoda.com/pricing  
  
Happy learning,  
Team Killer Shell  
  
#kubernetes #k8s #cks #security #devops #devsecops #container #docker #linux

## Transcript

### Introduction and Welcome

**0:02** · welcome to the killer shell cks preparation course this is a full preparation course for the certified kubernetes security specialist it includes all the theory with practical Hands-On challenges I'm Kim I'm going to be your trainer and I'm kubernetes certified in all possible ways I'm creator of the killer shell simulators which are realistic simulators of the ckad the cka and also the cks

**0:30** · I'm kubernetes trainer developer and writer and also software engineer by heart and I work with various companies from mediumsized to large sized and as kubernetes trainer and contractor and what I learned during all this time is that I love teaching I love diving into topics complex topics for days or weeks just to then break them down into their Essentials and teaching these two people in an easy and visual way for example by

**1:00** · doing presentations workshops or talks and that's why I'm excited that I can teach you this now about the cks and you might have seen the topics about the cks what it's about it's for example about cluster setup system hardening supply chain security we will dive together into every of these topics so we study

**1:22** · the theory and we do it in a way where I give you presentations in a simple and visual way like 5 to 10 minutes presentations about every topic everything you need to know followed by Hands-On challenges which we will do together where you get that practical knowledge how do we do the Hands-On challenges during this course well we will do them by working with a kubernetes cluster and you will work with your own kubernetes cluster it should be set up with Cube ADM it's a very simple cluster just two virtual machines one Master One worker and we

**1:55** · will set it up together it's very simple we only have to run two scripts one on the master one on the worker and the cluster is running we will use this cluster and set it up on Google cloud and we walk through this on every step if you have never worked with Google Cloud it doesn't matter it is very simple easy and free we only use Google

**2:16** · Cloud for the virtual machine so if you would like to create that cluster anywhere else you can create it anywhere where you can create two virtual machines and then you simply run the install scripts one on Master One on worker and your cluster is running so this course includes all Theory with practical Hands-On challenges and I hope you as excited as I am I definitely love all the kubernetes certifications especially the cks and I would love if you attend this course with

### K8s Security Best Practices

**2:52** · me tetes security best practices the idea of this talk is now to provide you with an overview about various kubernetes security aspects and these are important when you work with a kubernetes cluster and production and these are also important when it comes to the kubernetes cks exam so for this

**3:15** · we will talk about security principles in general we talk about kubernetes security categories and about the best practices in kubernetes when it comes to security so security is complex and it is a process this as a general thing

**3:32** · security combines many different things it's not just one thing that we have to do and suddenly boom we have our security environments change which means security cannot stay in a certain state for a long time security has to adapt constantly to changing environments and

**3:50** · yes attackers usually have the advantage because they decide when they attack it could be at the middle of the night and they pick what to attack it could be the weak Link in our chain so because of this let's have a look at General Security principles that are good to follow there's for example defense in depth which means we should have multiple layers of security and redundancy is good the least privilege means if we for

**4:21** · example assign a pot a service account some privileges using role base access control then these should be the least privileges because yeah if someone manages to run as that pot and execute commments at least it only has the least

**4:38** · Privileges and we should also talk about limiting the attack surface which means even limiting or removing the possibilities for any attacker to even exploit anything in our system so redundancy is good right but

**4:55** · only insecurity you might have heard the drive principle don't repeat yourself this is important for application development definitely but when it comes to security then redundancy is a good thing let's have a look at an example so we have our kubernetes cluster and here is actually an attacker which likes to attack something in our cluster that

**5:15** · could be the first level of defense and this could be reducing the attack surface okay we reduce the attack surface which means we for example removed unnecessary applications from our system implemented some firewall rules reduced the attack surface so this

**5:31** · already keeps a lot of attackers away but our attacker right now manages to even find something exploitable and break through then let's say we have even another security layer implemented which again prevents many attackers from even reaching further but that one attacker still manages to break through this redundant security layer and now

**5:50** · hits another security layer of us the least privileged one so even if the attacker now gained access let's say to a pot at least that pot runs with least Privileges and the attacker can't really do a lot of harm so that's the idea of a layouted defense system now let's talk about the kubernetes security categories so on the

**6:15** · bottom there is the host operating system security which is most probably a Linux operating system and that itself should already have a certain level of security because on top of this we then install our kubernetes cluster so this could be the kubernetes cluster security and our kubernetes consist of components and these run as processes on that host operating system and then on top of this

**6:41** · we have the application security which means our containers and our pots that run in kubernetes so if you use a managed kubernetes service like for example from Google or AWS then the bottom two categories should already be done by that cloud provider and we then only have to look at application security but if we manage our own kubernetes cluster and if we look towards the Cs certification then all of

**7:10** · these three categories are important and that's why we will now have a look into each of these categories and look into some best practices and examples of what should be considered and implemented so let's have a look at the host operating system security at first so when it

**7:28** · comes to this then we should consider that kubernetes nodes should only do one thing they should only do kubernetes and not anything else this means we should also reduce the attack Surface by removing unnecessary applications and also keeping everything up to date we

**7:46** · should probably consider using runtime security tools to help us with this and we should find and identify malicious processes and as well restricting identity management user and SS AG access to these machines just as a few examples what should be done on the bottom level on the host operating

**8:09** · security so now we install kubernetes on top of our operating system so we come to kubernetes Cluster security and here we have different components and these should all be running secure and also up todate so as a few examples we have the API server the cuet or atcd as components and we should restrict R access to these or even external access so external access to API server or even

**8:36** · etcd should be restricted unless definitely necessary and for example if we have a look at the cuet um the cuet doesn't have to communicate directly with etcd right the API server has to communicate with etcd so we can restrict and confine this already on on the network level we should use authentication authorization and as well admission controllers and we will learn later that every request coming into the API server

**9:06** · will actually run through authentication authorization and admission controllers and for admission controllers there is for example the note restriction admission controller which actually manages what the CET can do in regards to the API server and well the possibilities are endless we can even create custom policies and enforce these in our cluster for example using Opa the

**9:31** · open policy agent and we should also look into enabling audit logging and we do this extensively in this course and there are also security benchmarking tools like CRS which provide us with recommendations of how to run our

**9:49** · components secure let's have a look at an example of the kubernetes cluster security we have our kubernetes cluster we have atcd our c Central Key Value store and now we have a pot and that pot doesn't really run secure and an attacker actually manages to escape out of that pot into the host operating system of the worker node which runs our pot now let's say the attacker is able to communicate with ETD directly this is already not good

**10:21** · and what can we do to secure this well so at CD should be encrypted at rest so that means the file system where it's persisted is encrypted that's a good thing to do we should probably restrict access to at CD anyway so this means the

**10:36** · worker note where that pot is running shouldn't be able to communicate with etcd anyway because it doesn't have to and we should look into encrypting traffic between components like the API server and ET CD so that no one can listen so ET CD security is very important because ETD has everything regarding our cluster the complete State and all all of our secrets and credentials as well now let's talk about the third

**11:06** · layer of kubernetes security the application security and here we should talk about secrets we should use secrets we should never use any hardcoded credentials inside our Docker containers or in our pot declarations we should use role based Access Control to restrict access

**11:26** · we should probably look into container sand boxing which means we can put our containers into a sand box and then create like another security layer between these and the host operating system we should talk about container hardening which means reducing the attack surface of containers running them as a user and not as rude and for example having a readon file system which would ensure that a

**11:52** · container is actually immutable and cannot be changed during runtime vulnerability scanning is Big which should be done constantly to find noun vulnerabilities in all the images that we use in our cluster and mtls or the use of service measures which makes the use of mtls very easy should be considered so that the traffic inside our cluster between our applications should be

**12:24** · encrypted so there's a great talk kubernetes security best practices and the link of this is also in the resources section of this video definitely a great talk which we used a lot for the inspiration for this talk and with this we come to the end of this

**12:40** · introduction we talked about a few security principles we talked about security categories in kubernetes and we talked about some of the kubernetes best practices that should be considered well this should have only been like an introduction for you into the whole kubernetes security to so that you know what might be coming at you and what will be coming at you throughout this course and for the cks

### Create your course K8s cluster

**13:08** · preparation one of the first things that we should do now is to get your kubernetes cluster up and running one cluster which you can use for the whole cks preparation course and in which you can study all the topics and solve all the Hands-On challenges that will be provided to you so this will be about the course cluster

**13:32** · setup and for this we talk about the necessary specifications of that cluster and then we run through everything that's necessary the g-cloud registration and the g-cloud cluster creation so we use Google cloud g-cloud in this course and we highly suggest that you do it as well it is free it's very easy and we run through all the steps so even if you have never worked with cloud or Google Cloud before don't worry it's very easy convenient and this

**14:00** · is not Google Cloud specific right we only use Google Cloud for the virtual machines and nothing more so you can set this cluster up also everywhere else you like but we use Google cloud and we can also only answer a question then to Google Cloud so let's first talk about that cluster and the specifications that we will need for this course well it

**14:24** · will be a very simple cluster okay the cluster will only consist of two virtual machines one and two and the first one will be our master and we call it the ckss master and the other one will be our worker and we call it the cks worker both will have the very same specifications they will run on yuntu they will have at least 50 gigs of disc two CPUs and 4 GB of RAM so that's it we

**14:53** · will create the virtual machines like this and then we provide you with one script script install Master which you run on the master node and one script install worker which you run on the worker Noe and that's it so the links for this are also already in the resources of this video so if you want to go ahead and say I don't want to set up this cluster um in Google Cloud you want to do it yourself you only need to create these two virtual machines and then run these scripts on master and on worker and the cluster is up and running

**15:26** · and this will also be the setup with which you have to work in the actual exam you will work with various clusters and always with one master and one worker note which means this will be a proper preparation so we suggest to

**15:41** · stick along because we will now jump into setting this cluster up together in Google Cloud welcome to this Hands-On session and well this might be the first Hands-On session in this course you recognize it on top there's the Hands-On logo and every time you see that one you know you have to stop just listening and

**16:07** · start to listen and also get your keyboard ready we will now create in this Hands-On session a Google Cloud account if you already have a Google Cloud account feel free to just log into that one now and skip this video and directly head to the next one I don't have my Google Cloud account ready yet and I guess you neither so head to

**16:30** · console. cloud.google.com the link is also in the resources of this video and now we are required to log in using our Google account so we need a Google account to log into Google Cloud if you don't have a Google account yet then there should be a form which simply allows you just a few steps to create a Google account otherwise select your Google account right now I select mine and lock into to that

**17:07** · one there we go and our Google Cloud account was created for us if you lock in the very first time there's probably a few check boxes that you have to agree with but then you should be loged into your Google Cloud console and on top you see your free trial is waiting activate now to get $300 credit to explore Google Cloud products and this is what we will use so on the top right I click

**17:36** · activate there we go you select your country and agree to the terms and now you have to fill in some information on the step two like your address and you also have to add a

**17:54** · payment method so for the payment method it's important you won't be be charged nothing will be charged even if you go over the $300 credit it won't be automatically charged you have to actively go in and convert your account to an active account so that payments will be booked off okay so even when you add your credit card information here now nothing will be charged unless you say yes

**18:20** · please charge me Google I want to keep using it but these $300 credit will be more enough for this Co to test so go ahead fill in all these information I will do the same now and then we should start the free trial down

**18:39** · here and here we go my registration was completed thanks for signing up and I got the $300 free credit over the next 90 days but it says as well if you run out of credit don't worry you won't be built unless you turn on automatic billing so everything is free and you won't get charged got it so if you have

**19:02** · never worked with Google Cloud before it is very simple this is your console and on the left you see all the various services that Google offers we won't work with almost any of these because we don't use Google Cloud for Google Cloud we only use it for the virtual machines and you find them here on the compute engine so you can click on compute engine and this will almost always be the only page that we will be working

**19:37** · with and in this Hands-On session it's time now to install and configure the g-cloud console comment on your local terminal if you have this already done and it's set up with your Google Cloud account that you want to use for this course then you can skip this video and head to the next one otherwise follow me along and yeah you should be logged in to your Google Cloud account and it should look something like this and we

**20:09** · now would like to connect our terminal here I have my local terminal you should have a terminal open we want to connect that terminal to our Google Cloud account and for this we had to the link provided in the resources section of this video or you can simply Google for it installing Google Cloud SDK so do

**20:32** · this instructions are here whatever operating system you use I'm using Mac OS so what I will do is I will download the proper package so I copy the link and download

**20:54** · it I will extract it there we go we have a folder Google Cloud SDK and there we can actually now run the install.sh script to install it in our

**21:24** · system there we go I installed the Google Cloud SDK on my local system the next thing what we can do is we can simply run g-cloud there we go and this is the g-cloud comment and we can see there are various things that we can do with it but what we would like to do now is to run gcloud our login okay so we now have to

**21:56** · allow our log g-cloud comment to talk to our g-cloud console account for this simply type gcloud out login and it should direct you automatically maybe it opens your browser automatically with the correct link otherwise copy the link that will be provided to you here head to your

**22:22** · browser where you are logged in into your Google Cloud account open it confirm your account and there we see yes we will allow and you are now authenticated with the Google Cloud SDK we can test this okay we can test this by heading back to our local terminal and let's have a look for

**22:51** · g-cloud projects list there we go that's my project it was named my first project it has some ID that we see here and it should look similar for you and if you head to your browser and into your browser Google Cloud console then you see also on top my first project we have it here that's my first project and that's the ID which means our gcloud comment is now

**23:24** · connected to our g-cloud account but one thing that we still have to do is to set the project in our console so what we can do is we type actually

**23:42** · gcloud config set project and then simply copy your project ID gcloud config set project there we go update the property and now we can for example run something like g-cloud compute instances

**24:03** · list there we go zero items yet in the next video we'll actually create the instances which hold our cluster for now everything is set up so far and don't worry too much about these g-cloud comments the only thing that we will do throughout the majority of the course is to SSH into the instances and from then on it'll be kubernetes pure

**24:31** · in this Hands-On session we will now create the ckss course kubernetes cluster in Google Cloud we only use Google Cloud for their virtual machines their instances not for much more and for this we have to create two times the same virtual machine one time we call it ckss master and the other one we call it ckss worker a region you can select any

**24:58** · near you the machine type should be E2 medium and the boot dis should be Ubuntu with minimum of 50 GB of space so we now go ahead and do this through the web interface together in the resources section of this video there are also simply two g-cloud commands which you

**25:19** · can run which will create the virtual machines which is also nice if at a later stage you have to recreate your cluster you can simply run that one console comand and it will recreate your virtual machine right now you can also simply use the comments in the resources section or you walk with me now through the web interface which is great to get to know it as well and it's very easy after we created the virtual machines we only have to run the install Master

**25:49** · script on the master node and the install worker script on the worker note and the links to this the comments that we can simply run are also in the resources section of this video so very simple cluster setup and now let's go ahead and change to the browser where we should be logged in in our Google Cloud

**26:12** · console and our dashboard should look something like this what we need is on the left here the compute engine section and we can simply click on it what we could also do to reach this section is

**26:28** · we could type on top we could simply search for it for compute and then we see compute engine and select this and this will be the only service that we need Google Cloud for if you reach this page the first time then Google compute the API service might need to be enabled for you which might take one or two minutes otherwise here we are let's create our first virtual machine we call it cks master so simply

**27:00** · type the name ckss Master for region you can just leave it like this or select anyone near you there we go and then the serious should be E2 it is default selected here right now and then E2 medium right here so for me I can just

**27:18** · leave it like this right now and then if we scroll down then we can select the boot dis right now it is Debian so we click on change and we select yuntu just a little update please select yuntu 204 and not the version you see in the video because we have since updated the course and for the yunto version We select and for the dis 50 GB select

**27:49** · there we go scroll to the very bottom and click create that was it the instance will be created for us we now repeat the same thing again and create the Cs

**28:06** · worker so for name I choose seek as worker I select the region again anyone any region near you serus E2 machine type E2 medium the operating system we change it to yuntu and yuntu 50 gigs of

**28:30** · dis select and create and that should be it and let's give it one or two minutes until these are properly created and maybe pause the video till both your machines the Cs master and the SEC as worker are ready it is the case

**28:54** · for me now so that's it they have been created we can use them now there is like a browser SSH terminal here that we could use to directly SSH into the machines it is convenient but it's not nice for copy and pasting Etc so we don't suggest using this browser SS Edge terminal that's why we head to our terminal and we did set up our g-cloud console command already which means we can now do gcloud compute SSH

**29:26** · cks Master that's it g-cloud compute SSH cks Master which will provide us with SSH

**29:42** · access into the master node if this doesn't work for you right now it might be too early maybe wait 1 minute till your instance is ready so you're logged in with your username and and what we now have to do is sudoi to get root we will always work with root in this course and then head to the resources section of this

**30:09** · video and there you can copy a simple comment which installs the install Master sh script from our GitHub repository that should be it that should be run through it maybe takes a few minutes that should be it and we have to

**30:25** · do the very same for the worker node so I have another terminal tub up here on left will always be my master on the right will always be my worker and I do the very same now for the worker g-cloud compute SSH cks worker that's it g-cloud compute SSH cks

**30:53** · worker and as well I'll get root through sudoi and then I copy very important the different comment because we want to install the install worker Dosh on the worker note there we go and let's just wait until both scripts

**31:17** · finished and here we go my worker script run through same for my master and so the last thing that we have to do on the very bottom of your master node there should be a comment that you can copy the cube ADM join comment copy the whole thing with the hash on the back as well

**31:37** · copy it onto your worker note and execute it and this will now add our worker node as a kubernetes worker node to our kubernetes cluster there we go the node has joined the cluster that's it I head back to my master note and what I now actually can do is I simply log out once with exit and log in again

**32:04** · becoming root again and now I see I have colors and now I actually have a few um convenient comments installed for example the Alias K so I can run kg get node and I see my cluster is almost ready um the note is not ready yet but

**32:22** · we give it a minute so the install Master script and the install worker script also set up a little bit of convenient bash configuration which we can then use comfortable throughout this course for example also autoc completion should be enabled for the cube CTL and

**32:40** · there we go okay there we go our cluster is set up we see I'm on version 11 193 right now you might be on a on the later one depending when we updated our install scripts and you should have one cks master running and ready and one cks worker running and ready and we can for example have a look at all pots in the cluster and there we see already some kubernetes components our cluster is running and ready

**33:10** · awesome and one very simple addition that we still have to do make cluster accessible from the outside we will now open the ports 30,000 to 40,000 and this is simply done so that we for example later using our local machine can send request to not ports and these will reach not Port Services inside our own

**33:33** · cluster and for this simply head to your local terminal and exit the comment from the resources section of this video so you should now be on your local terminal and not on your master node not on your worker node on your local terminal because we run a g-cloud command we create a firewall rule we call it not ports and we allow TCP of the not ports

**33:57** · everything between 30,000 and 40,000 and there we go it has been created it has been done and it will be useful for the later upcoming handson sessions and one important thing to remember is to always stop your instances when you don't study anymore to save your free credits we can do this very easily in the Google Cloud console

**34:24** · and let's go ahead and let's do it now I'm in my Google Cloud console and I can simply mark my master and worker and on top I click on stop and I stop them after which Google will actually go ahead and stop these instances it will only stop these it will not delete these which means afterwards we can start them again but if right now we are still logged in using SSH then yes we see we got kicked

**34:53** · out of the master node and also got kicked out of the worker note this is expected great there we go both are stopped I can now go ahead and do anything else and let's say I'm coming back right now and I want to work again on the killer shell cks course I simply

**35:11** · Mark the instances again and click on start and they will be started again give it one or two minutes um after which you can log in again via SSH and everything will work again the kubernetes is running again worker node is added to the cluster and the cluster state is reproduced because of ETD

**35:33** · persistence so you can do this using the web interface very fast you can also do this via the g-cloud command for example by running g-cloud compute instances stop and g-cloud compute instances

### Crictl instead of Docker

**35:50** · start just a short information that we updated our kubernetes Cube ad M install scripts from not using Docker anymore but using container D okay from kubernetes version one22 Docker is actually not anymore supported but Docker containers will still run you can still build Docker images um you just run them then using the container D runtime we updated

**36:19** · various videos where we actually used Docker intensively before and we now use cctl and container D for example example um there might be still some videos which use Simple Docker for listing containers um instead of using Docker you can always then just use crect LPS and there should also be notices like this throughout this videos should you counter something where still something

**36:47** · doesn't work and we show how it's done in Docker um just let us know in the message system here or in slack and we update fast thanks so with the end of this section you should have your cluster up and running recreated two virtual machines in Google cloud and we connected to these using g-cloud which we simply use for easy SSH access into the machines we

**37:16** · can reset the machines if we need so at any point in time in this course you can simply delete an instance and create it again using the method and the script that we provided you and then you have your cluster again we don't depend on

**37:33** · previous things that we did in the course okay every new section can start with a blank and fresh Cube ADM cluster installed in the way that we installed using our scripts okay this is great there's no dependence on like earlier things that we implemented every new section starts from scratch and always stop your instances when you stop studying to save your free

### Foundation - Kubernetes Secure Architecture

**38:03** · credits the best way to start with the cks certification training is to have a little overview about the kubernetes architecture and especially about the secure aspect of the architecture and

**38:19** · this is exactly what we will do in this talk we talk about the kubernetes architecture from a top level View we have a look at the various components and also at the secure component communication so the idea is that after this talk we will all be on the same level regarding the information and knowledge about kubernetes and that helps us to then go together into the various cks topics and learn what will

**38:47** · be necessary for this let's have a look and let's start at a really simple view of what kubernetes can do for us so so this is our kubernetes that blue thing it has our beautiful kubernetes logo down here so what can kubernetes do for us well in a simple way we have containers and container information which we throw at kubernetes and it will run our container

**39:13** · most commonly still in Docker it's also possible in other container engines which we will also see later in this course so it can run a container in a container engine for us and then various things things around right like scheduling our containers efficiently keeping containers alive performing health checks allowing container

**39:36** · Communications and allowing common deployment tactics or even not that common deployment techniques through extensions and for example handle volumes attachments Etc so like various things to ease the workflow around container running and

**39:55** · scheduling so this is great this is why we all love kubernetes so let's have a look at how kubernetes does this under the hood and if we have our kubernetes cluster here and it runs our container here then it runs our container in a pot okay so a pot is a wrapper around a container and a pot can contain one or multiple containers so this is our container we

**40:22** · have it now here in Gray and we call the container app so this pot has one container app and it's running with Docker under the hood and we then tell kubernetes to run this container and we can for example do this using Cube CTL all right it's a common way to communicate with kubernetes using cctl but it is possible in different ways because in the end we communicate with the kubernetes API server so kubernetes

**40:53** · central part is the API server which makes it greatly extensible and reusable which also yeah um is one reason why kubernetes gain so much popularity so simply we contact the API server we can do it using Cube CTL and our API server then decides hey where should I even run this pot so right now we see that PO is running on node one so kubernetes can

**41:22** · have multiple nodes worker nodes which are ready to run our pots and then our pots contain the actual containers with our applications that will be run how does kubernetes work with nodes

**41:38** · or how does the API server work with nodes and communicate with noes it does so with the cuet so the cuet is the component which kind of converts an instance a virtual machine into a kubernetes node which can actually run pots so a cuet can can only do one

**41:58** · thing in a nutshell it can run pots and it gets the information of what ports to run from the API server um it can also communicate with the API server so it's a two-way communication for example if the pot is

**42:16** · starting and then it becomes ready then it changes its status and the CET can then communicate that status change towards the API server so here we have have the communication between the API server and the cubet there's also the scheduler which communicates with the API server and which is actually responsible for deciding okay I have a p which should be

**42:40** · running but it doesn't have a note assigned so in this case for example our Po got node one assigned by the kubernetes scheduler that's what the schedule for decides on which note will which pod run we have at CD which kind of can be seen as the database of kubernetes it is a key value storage and it holds the complete State

**43:04** · the whole state of the cluster is persisted in at CD and we can for example back up atcd and this will then back up our whole state and it can also be restored from a backup and the only component communicating with at CD is the API server we then also have the controller manager which contains various sub components and it has various control loops which checks various resources

**43:34** · okay for example like deployments or replica sets to make sure hey does that replica set has always the exact or the correct amount of pots running and if not then some pods will be killed or some pods will be created so they are like the control loops which keep all the resources alive

**43:56** · there's also the cloud controller manager which contains like Cloud specific um controller loops and applications for example if you run an cluster in openstack or on Google manage Cloud then you might have the control

**44:15** · loops running in the cloud controller manager so we also have the Q proxy which we see blinking here and the Q proxy communicates with the API server and it receive updates about Services created in kubernetes so a kubernetes service which allows for easy communication between pots a service is represented in the cube proxy component so a kubernetes service is nothing else

**44:44** · than IP table rules most commonly IP table rules there also other possibilities but most commonly IP table rules which are implemented on every note so whenever we create a new service or so updated service in kubernetes all Cube proxies on every note will implement this change by creating or updating IP table rules on each

**45:11** · note and if we have a look we can then call the control plane these are the control plane components over here and the data plane is then the control or the the uh the components over here running on our worker nodes

**45:27** · and well in that setup we can now also simply add a second node right and that second node also has a CET running it also has a q proxy running and in this case there's one pot running on that note and in this case it has two containers one called EP and one called SAR so just to show yes ports can run

**45:47** · multiple containers so this should simply give you a little overview about all the cuberes components what they task are how they communicate with each other and this should definitely get us started to then dive into the more and

**46:05** · various cks topics and we can have a look at the pot topot Communication in kubernetes and this is managed by the cni the container network interface and then there are various cni plugins which Implement that

**46:23** · interface and which actually create and manage the network infrastructure which manages the pot topot communication and one condition there is that every pot can communicate with every pot and another condition is that this can happen without not without network address translation so every poort can communicate with every other POD at least by default and this is also

**46:53** · the case if these pods are running on on different notes and this is made because that's like one the big things of kubernetes we don't want to think anymore about the worker nodes we don't want to think about our po has to run on a server like this node or our po has to

**47:10** · run on this node we only have our workloads our containers we want to scoll them at kubernetes and kubernetes then decides where to run them and it doesn't really matter at least by default where they run they can all communicate with each other and yes we will have a look later on how we can actually restrict this if

**47:35** · necessary now let's talk about the certificate Authority that we see here and the pki the public key infrastructure in kubernetes so the pki is nothing specific to kubernetes it is something very common in the world of the inter

**47:55** · internet and secure component and application communication and kubernetes adapts this as well which means we have a certificate Authority which watches over everything and this means that the certificate Authority is the trusted route of all certificates inside our

**48:14** · kubernetes cluster this also means that all cluster certificates are signed by this certificate Authority and this then allows components to validate each other so that components can be sure that they communicate with the proper identified

**48:33** · component and for example what does the ca do what kinds of certificate does the certificate Authority sign well for example the API server has a server certificate this will be signed or the cupet has a server certificate it also has a client certificate and we see this soon and for example the scheduler has a client certificate to communicate with the API server so there are various

**49:01** · certifications in kubernetes and let's have a look at an overview of these so we have our certificate Authority and for example we have the API server and it has a server certificate and it has a server certificate because it has clients like the controller manager which communicates with the API server so the controller manager needs to have a client certificate and the API server for this needs to have a server

**49:32** · certificate same for the scheduler the scheduler is a client of the API server and same for example for the cets the cets are clients to the API server the cets are actually also servers so the API server can actually using a client certificate can contact the CET so the CET also has a server certificate and we also have our at CD our key value store which has a server certificate and the API server can communicate with at CD

**50:06** · though at CD might be a bit of a special case because it might actually have its own certificate Authority and we will see this soon as well and I would say it's time for a

**50:23** · Hands-On session right I mean we can talk and talk and talk about all these various certificates and authorities or we can jump in and have a Hands-On practical look where these certificates actually are and get a better feel for everything so for this we will run through this list it's nine points but they will be very fast solved and it's a

**50:43** · Hands-On session so follow me along you should have your master note ready we will do this on our Master note and first thing is we will have a look for the certificate Authority so for this I'm on my Master note my cluster is running and ready and there's the directory kubernetes ATC kubernetes pki

**51:02** · and let's have a look what we find there there are various certificates and we see for example already the certificate Authority here so in that directory there are most of the certificates which we want to find but some are at a few different places so number one done what about the API server certificate well the API server certificate is for example here that's the API server certificate and then we also see the API server client

**51:32** · certificate to communicate with at CD and we also see the API server CET certificate client which means the API server uses this certificate to communicate with the cets running on a note so we have the API server certificate we have the API to at CD certificate number four we have the API to CET certificate we skipped the number three I see um no cheating here we still

**51:59** · have to do this one at CD server certificate let's have a look at the at CD server certificate and here we actually see there's a folder at CD so let's have a look what's inside that folder and there we actually see there's the server certificate for at CD here so

**52:16** · as far as I can count we already went to number five what about the Schuler towards the API so the Schuler is a client of the API so let's have a look so the schul has actually a config which is available under kubernetes schedular conf so open that file in your favorite editor Etc kubernetes schedu conf and

**52:41** · there we see it's actually a cube config and here we actually see if we scroll down that we actually see these are included here we have the client certificates for the scheduler to communicate with the kubernetes API

**52:57** · and I think we should have a look at number seven the controller manager as well and for the controller manager it is very simple there's a file is very similar there's this file under ATC kubernetes controller manager con and here as well open it have a look into it it is a cube config as well and um if we

**53:18** · scroll down then we see the user information and it has the certif certificate data actually included in the cont config file so where are we we did everything down to number seven what about number eight CET to API so the cuet client

**53:36** · certificate to communicate with the API well for this we could go on the master or the worker node and we can actually now on the master node can have a look at kubernetes and then cuet con so the cuet as well has a simple cuet configuration like a cube con and in

**53:55** · there as well like the other clients we actually see that the certificate data is actually different than the other clients it's actually not included but it's referenced by a path so we see that the certificate is actually here under this path and well the cubelet is able to run pots and what Cube ADM so the

**54:17** · setup with Cube ADM when you create a cutic cluster with Cube ADM what Cube ADM does is it runs various cuetes components already in parts so it uses the cubelet to run other kubernetes components like the API server like the schedul like the controller manager which means that in this setup the cuet

**54:37** · is also running on the master node so the master node uses the cuet to run other components which is great it makes it flexible but we can also have a look at the worker no so here have a different TP and I change to my worker node and on the worker node as well if I had to Etc kubernetes and then Cube um cubelet con

**54:59** · there we see that there's also a cube con and we also have the certificates under the same path so this is our worker node CET which is able to communicate with the kubernetes API what about the cuet server certificate so we know or we should know by now that the API server can also contact the cuet and for this let's have a look at the cuet ser

**55:26** · certificate and I'm on the worker node we can do the same on the master node and there's actually a folder in V liip CET and there's also a folder pki public key infrastructure and in there we actually see these are the referenced client certificates that we just saw like here that we just saw in that cuet con up here right be the client certificate and then we also have the server certificate here so I think this

**55:56** · should help you just as a little introduction into all these various certificates and pki and certificate Authority so now you have some like Hands-On session challenge where you were able to see this like in

**56:15** · action and with this we reach the end of this section and at the end of many sections we provide you with a few suggestions about links or conference talks if you like to dive a bit deeper into a topic but these are definitely not mandatory just if you're interested

**56:35** · of if you want to further Harden your knowledge so there's a great talk I can really suggest all you need to know about certificates in kubernetes link is in the resources section of this video there's also the kubernetes documentation page called kubernetes components which gives a great overview and there's as well the kubernetes documentation page pki certificates and

**57:02** · requirements and with this we will end this section we talked about the kubernetes architecture we talked about the various components and got hopefully a great overview about how they communicate with each other and in the component communication we also talked about the pki and the secure component communication and all the various certificates in our kubernetes class

### Foundation - Containers under the hood

**57:28** · containers under the hood with this section you will get to know containers much better and in much more detail because from a kubernetes security perspective it is important to understand what containers are how they work and how they interact with our operating systems and for this we will start with containers and images we then

**57:54** · have a look into to name spaces and c groups the kind of building blocks for containers and we also have a look into some Hands-On scenarios which should make these things more clear to us so container and image what is a

**58:11** · container what is an image let's start with a Docker file to explain this okay so we know explain this on the example of Docker containers because they're the most prevalent out there there are also other container systems but let's start with a docker file okay so a docka file is a simple script or text which defines how to build an image which means we can run docka build and Docker build will build our image then we have our image and the image could be described as a multi-layer binary representation of

**58:43** · state which we described in our Docker file from that image we can then create a container so using docka run we actually create a container and we could say that a a container is a running instance of an image and there can be multiple running instances of an image that there can be multiple containers of the same image also very common once we build our

**59:10** · image we actually push it into a container repository and then whenever we would like to run it we can actually Docker pull that image and then Docker run this image so that's as the simple difference between Docker file container image and the actual

**59:29** · container so what is a container down here we see Docker or container D so what is in general a container we could say a container is a collection of one or multiple applications they are bundled together and they actually include all their dependencies so they are bundled with all their libraries and the dependencies that they need to run but in the end a container process is

**59:55** · simply a process which runs on the Linux kernel with some restrictions because it cannot see everything it is kind of encapsulated and to understand this let's have a look at the broad

**1:00:12** · architecture on the bottom we have the hardware and on top of the hardware sits the Linux kernel and the Linux kernel actually provides a so-called CS call interface these CS calls or system calls like get PID or reboot will then be provided to libraries like gipc or

**1:00:33** · applications like Firefox or Cur and in this scenario this doesn't play a big difference if these applications run directly on the Linux kernel or containerized in a Docker container which we will see soon so in the end we have down here the kernel space which incl includes the Linux kernel and the csol interface and then up here we have the user space where our libraries and applications run and the sus interface is then the

**1:01:05** · possibility to communicate with the Linux kernel right and our applications can call the sus call interface directly or our applications can go through libraries which is often the case and then these libraries communicate with our CS call interface of the Linux curer so these physical interface can kind of be seen as an API from the Linux kernel to allow for communication with it and

**1:01:33** · then when we do some s calls then these will be reached down to the Linux kernel and the Linux kernel communicates with the hardware so we have to be we have to understand that our applications like Firefox even if it's containerized like here can perform direct sus calls to the

**1:01:52** · sus call interface let's have a look at this in another view we have the hardware on the bottom again here in yellow we have the Linux kernel and let's say we have an app1 process could be our Firefox process it's the app1 process and it is containerized it runs as a Docker container but this means that that process can still perform system calls against the host Linux kernel and the

**1:02:22** · very same thing could do another process let's call it app2 process which is running in a completely different Docker container and that app2 process could also perform sus calls to the very same Linux Kern so this is something important to understand that if we schedule many containers on one operating system like we do in kubernetes we have a worker node and depending on how many free resources there are we can schedule 10 20 100 pots

**1:02:51** · with various containers on that note which which means they all run on the same Linux kernel and they can all perform system calls to the same Linux kernel and down here again we have the kernel space and here we have the user space for our

**1:03:12** · applications so this means yes we can have one container which is wrapped in a kernel group and we'll have a look at these kernel groups we now simply call them kernel groups we'll have a look at these soon so we have our app one process we have our app2 process we have our app 3 process and the thing from the security perspective is that if these all run on the same Linux kernel and if these all can perform CIS calls to the Linux kernel then these all could also exploit

**1:03:42** · some Linux kernel bucks and there have been some in the future and there probably are some right now which means that it could be that there's not a too strong isolation between for example examp the app1 process and the app2 process if there is an exploit or some exploitable security issue in the Kel but we will explore this as well further in the cks training course this is right

**1:04:10** · now only as an overview of how containers work and how they run and how they interact with the operating system so what's the difference then between a container and a virtual machine so if we have a virtual machine then it has an operating system and a kernel and on top of this we actually simulate another operating system with another kernel which means our application process app process actually runs on a different kernel and not on

**1:04:39** · the host operating system kernel down here we have a look at containers on the left then it's a bit different we have our operating system we have our host kernel and our application process could directly run on that kernel or we wrap that application process in a kernel group we kind of containerize it we put it in a container but it means that application process still runs on the same kernel which means here on the left that kernel can actually directly

**1:05:10** · access the app process whereas here on the right that host kernel down here cannot access the app process at least directly it has to go through like a arbitrary binary layer of the simulator operating system so that's as a simple difference between containers and virtual machines and now let's have a look at Linux kernel Nam spaces Nam spaces isolate processes and

**1:05:41** · this is necessary because we want to create containers containers are simply processes on the same Linux kernel but we want to isolate them so we put them in namespaces there is for example the P ID namespace and the PID namespace isolates processes from each other one process cannot see others and for example process ID 10 can exist multiple times once in every

**1:06:08** · namespace there's the mount namespace which restricts access to mounts or root file system there's the network namespace which only LS access to certain network devices firewall routing rulle socket port numbers so not able to see all traffic or contact all endpoints so Network isolation and there's the username space which means a different set of user IDs is used and for example user zero root

**1:06:38** · inside one namespace can be different from user zero inside another namespace and this also means that the host root user zero is different than the user zero inside a container because of name

**1:06:54** · spaces so if we talk about container isolation and how containers and Docker containers are built then we have the name spaces to restrict what processes can see and by this we kind of simulate an isolation layer between these and we kind of create the containers through this and this can for example be restrict other processes users or file system access and then there are also cgroups and these cgroups restrict resource usage of processes and this can

**1:07:27** · for example be restricting the RAM memory usage dis usage or CPU usage and using these Nam spaces and these c groups we can create isolation container isolation and we can actually create

**1:07:45** · containers in this session we will have a look at container tools and the tools are Docker container D gasl Portman and we will actually build a very simple container using these tools so to have a short Overlook

**1:08:02** · what is Docker Docker is a container runtime and a tool for managing containers and images container D is a container runtime and it's slowly replacing Docker as a container runtime especially for kubernetes starting from version Wonder 22 where where Docker is not anymore supported creas CTL is a command line interface for CRI compatible container runtimes we talk about CRI compatible

**1:08:31** · later in this course in the end it's just a universal tool to work with different container run times cctl can work with Docker cctl can work with container D and other compatible ones and then potman is a tool for

**1:08:48** · managing containers and images right so we see Docker is a container runtime plus a management tool potman is only a management tool so we could for example use doer for everything or we use container d as our container run time and potman as our managing tools for like Building images Etc so let's go ahead and

**1:09:11** · create an image right so let's create a new Docker file and what we do is we start from Bash so this means there is already an existing image in this case a Docker image bash and we inherit everything from bash and what we do with this is we simply run one command ping with the argument killer. sh two lines this is

**1:09:44** · our Docker file really simple really small really straightforward we save this so here we have our Docker file so a Docker file is a text file that's it from this Docker file we can build an image a container image is a binary

**1:10:07** · representation and then from an image we can create containers and the container is an instanciation of an image okay so NE next let's go ahead and build an image from it using Docker so we can say docker build we give it a tag we call it simple in the current directory there we go and let's have a look do we have an

**1:10:37** · image so I list all images I grabed for simple and there's our image freshly created now we want to create an instanciation of that image we want to run that image as a container so we can simply do Docker run simply and here we see our simple ping command is executed in the bash

**1:11:02** · image and we can simply abort with contrl C that's Docker and a nutshell that's all Docker can do um now we do the very same thing with potman because as we saw here Docker is a tool for managing containers and images same as

**1:11:21** · pman I clear the screen and we now want to build the image so if I take the comment that we run Docker build teex simple we can simply replace Docker with potman and and this has been designed so potman has been designed from the interface that in most cases you can simply replace the name Docker with

**1:11:50** · pman so this means we can also say potman image LS and there we for example see our simple image freshly created and now I take the docker run simple command that we used from before and I replace Docker with potman run it and it's the very

**1:12:18** · same now let's also talk about cre CTL so cctl we can for example run or let's let's first have a look at Docker PS okay Docker PS shows all running Docker containers we don't see any running Docker containers right now because there are none okay we are on the master node installed via Cube ADM that means

**1:12:44** · there should be some containers there should be the the kubernetes control plane like the kubernetes API server controller manager there should be containers for this but we don't use loer anymore since kubernetes version 1.22 we use container D so what we can do here is we run cctl PS and here we

**1:13:02** · see our containers and if we have a look at the config of cctl then we actually see it's configured to communicate with the container D runtime so in this config it could also be that it's configured to talk to Docker or to another runtime so in this case what you see right here is we use cctl to communicate with

**1:13:29** · container D okay so I think this should give you a nice introduction into the different tools and a little bit into the Container build and run workflow that we can use throughout this

**1:13:47** · course in this Hands-On session we will now actually see Docker container isolation in action we will create two containers and check that their processes cannot see each other and we will then run them in the very same p namespace and see what

**1:14:06** · happens so it's the Hands-On session follow me along do the same thing on your master node we won't interact with kubernetes right now we will simply run Docker containers for this we can run a Docker container Docker run we give it a name first one is C1 we would like to run Ubuntu and we would like to run it detached let's do like this in detached mode yuntu and we execute sh and say

**1:14:37** · this simply sleeps one day okay we just created a yuntu container which sleeps one day and runs in the background we see here the ID we could now use the ID but because we gave it a name we can also use that name so we can simply do Docker XX C1 PS and then we see okay few processes

**1:14:59** · in that container very clean and here we actually have our sleep container running our sleep process running in that container let's do the same for a container named C2 and instead of sleeping one day we say we sleep 999 days there we go container created

**1:15:23** · and if we now EXA into that container then we also see three processes but we see they're different here we have that sleep one with 999 days and he we actually have that sleep one with one day so this means these processes run on the same Linux ker but these are isolated from each other because Docker automatically wraps these processes in nam spaces and if we now actually have a look if we now grab for processes called

**1:15:51** · Sleep on our host Linux system then we actually see we see both processes right we see the Sleep one day and we see the Sleep 999 days why because the container processes simply run on the same Linux kernel now let's actually delete the second container so we can simply do Docker RM C2 and forse our C2 container

**1:16:18** · is gun and we recreate the container again but with an addition we can actually Define the PID namespace and we set it to the namespace of an existing container called C1 okay so we create

**1:16:35** · the container C2 and with this little addition we now say this container will run in the very same P ID name spaces name space as container one let's run it there we go and let's have a look let's EXA into container C2

**1:16:55** · look for processes and yes there we actually see our own processes and the ones from the other container and if we now have a look at container run we run the same command for container one then we actually see both containers are now in the same PID Nam space and can see their same processes because of

**1:17:21** · this and this section gave us a nice little overview about what containers are and there's a very great talk by LZ rice what have namespaces done for you lately where she actually shows in a bit more detail and also practical how containers are created and what containers actually are in this section we talked about

**1:17:45** · containers in general we made a comparison towards virtual machines we talked about Linux kernel namespaces and c groups in the lunux kernel and we actually saw these in action by creating Docker

### Cluster Reset

**1:18:13** · containers just a simple reminder that at any point in time you can reset your cluster anytime you like you can delete your instances recreate them and create your cluster again because every new section in this course works with a fresh cluster this doesn't mean that you

**1:18:34** · have to work with a fresh cluster when a new section is coming but if for example something doesn't work for you like the solutions that we provide to you don't work then maybe try to reset and recreate your cluster because every new section is based on a fresh cluster installation

### Cluster Setup - Network Policies

**1:18:56** · network security policies very important and interesting topic in my opinion what we will do at first I'll go into detail what network policies are and how they work afterwards we will Define our own default deny policy following by various scenarios that we're going to implement after this you will understand network security policies what are they Network policies

**1:19:24** · well they are the firewall rules in kubernetes they are implemented by the cni by the container network interface which is installed in the cluster so like Calo or weave so if the cni um doesn't support network policies you can still create you KU resources but they just don't do anything they're not enforced they are created on namespace level they're only valid in one namespace we will see this later and well yeah they restrict Ingress and agress for a specific group of PODS

**1:19:54** · based on certain rules and conditions without network policy so if we have a vanilla kubernetes cluster then by default every pot can access every pot pots are not isolated and this is actually a feature from kubernetes right like it's one condition um that every pot in the cluster doesn't matter on which note it's scheduled every pot can communicate with every pot um without network address translation

**1:20:23** · so let's have a look at what network policies can do just in some graphical overview examples that we're going to run through before we go and look into yl and write our own yaml code right so if we have a Comm cluster we have three pots then we can create in the network policy we will create a pot selector for a certain group of pots based on their labels okay in Orange here and to these

**1:20:50** · pots based on the pot selector to these these pots will our Network policy rules applied then let's say we have another group of pots here so we specify another pot selector and now what we specify in our Network policy is that for that pot selector in Orange we allow policy type eress we allow outgoing traffic to these

**1:21:13** · pots okay should be really simple from a source pots we allow outgoing traffic to to another pot selector to these pots based on labels also possible same scenario but from or to this pot selector in Orange we allow incoming traffic so Ingress traffic from these pots also possible okay and if we have a look at this example right now then this pot one can only receive incoming traffic

**1:21:45** · from pots of this pot selector because as soon as you specify one network policy yet now in this case for example networ po of type Ingress then you restrict all other Ingress and you only allow that Ingress that you kind of WID listed in your network policies if there are no network policies then everything is a

**1:22:09** · lot another example instead of using a pot selector is also that we use a namespace selector so in this scenario for these bunch of pots based on the pot selector we allow incoming traffic from all pots in a certain namespace and what's also possible is to use an IP block definition where we say in this example now we allow these pots to have outgoing traffic to this IP address range and we could also specify

**1:22:38** · that this IP address range or that these pots can receive Ingress traffic from this IP address range okay and this we could do in two separate Network policies then they would be merged we're going to look at this uh in more detail but we could also create this in one network policy where we have actually rules for the agress and the

**1:23:04** · Ingress in the section before we had a look at Network policies for make a top overview um and we saw what they're like capable of in theory now we're going to look at one extensive example of a network policy in yaml and we dive into detail and explain every section so that you can create after words every kind of network policy that you kind of want this network policy we see kind Network policy is created in namespace default and we have a pot selector for

**1:23:33** · pots with the label ID front end okay so that means this netbar policy will be applied to pots with ID front end in namespace default now we have another um section here policy types policy types can receive an array of

**1:23:52** · entries Ingress or aress and this in this case we only specify aress this network policy that we see here right now is already a valid policy okay we could create that policy right now what does it do it denies all outgoing traffic from pots with label ID frontend in namespace default okay it denies all outgoing traffic because we said that this network policy is about outgoing traffic and we didn't specify any rules to allow any traffic this which means that this policy right now simply doesn't allow

**1:24:25** · any outgoing traffic so it prevents it disallows any outgoing traffic now let's allow some traffic same NE policy as before um we just extended it here on on the bottom and we will go now again through all the various things okay we have the PO selector on top as before ID front end will be applied this netback policy will be applied to these parts this netback policy is about about outgoing

**1:24:54** · traffic then we have the first outgoing traffic rule the first ESS Rule and this rule can be read as allow outgoing traffic to name space with label ID ns1 and Port 8 okay this array entry here we

**1:25:12** · see one here we see one here this means is one rule so this is the second rule down here the second eess rule this in blue is the first eress rule so the first eress rule has two entries the first entry is the two colon and the second entry is the ports colon and these two will be connected and okay so we have an agas rule we allow agas traffic if the Nam space towards the traffic goes has the label ID ns1 and the port is ad on

**1:25:47** · TCP now let's have a look at the second rule in purple down here we allow aggress two pots with label ID backend in the same name space why in the same Nam space because we didn't specify a namespace selector here then the same namespace will be will be taken um where the networ policy is applied to okay we we have two agas rules here the blue one and the purple one and these two rules will be connected or okay so we allow

**1:26:18** · aggress to namespace with label ID ns1 and Port ad or to Ports with label ID backend in the same Nam space now let's have a look what happens if we create multiple Network policies because it's possible to have multiple Network policies for the same pots for the same pot selector what happens then if a pot has more than one network policy well then they will be simply

**1:26:45** · merged the union of all netback policies is applied to that port and the order doesn't matter we have a look at it now what that actually means again we have the same network policy that we took apart uh before already we see uh we have our two rules our two agress rules down \[Music\] here now this netback policy example 2 a

**1:27:11** · only contains the first igoras rule like here okay and now we create another netback policy example 2 B which down here only contains the the Aras rule uh the second agas rule from down here okay and what you have to understand is that this rule that this network policy

**1:27:34** · example is the same as example to example 2 A Plus example 2 B merged because if we would create only this one and this one only the two on the right then they have the same pot selector for the same pots which means the rules which are array entries will simply be merged so appended and it would um result in in this exactly same network policy here on the

**1:28:08** · left we will now actually create our first Network policy it will be a default deny policy and that's good common practice to create default deny policies and then more policies to allow certain traffic and it's also important to no default deny policies for the ckss certification we will create a very simple scenario with one front end port one back end port and we check the connectivity between each before our Network policy after our Network policy and then afterwards we will extend our example further in more Hands-On

**1:28:39** · sessions you should have access to your master node your classer should be running you can see my master node my worker nodes are running we will now create a very simple scenario we just run four comments okay we simply create a front front end pot krun Front End image our belov engine X and the

**1:28:59** · same for back end k run backend image engine X now we expose balls we create cluster internal services so that it will be simple for us to check connectivity so we run K expose pot Front End we want to expose the pot Front End on Port 80 and we do the very

**1:29:19** · same for the port back end and if we have a look at pots and services we all we do everything in the default mpace we see we have our back end po front end po we have a backend service front end service very simple now we check the connectivity from front end to back end so we simply EXA into the front end p and run curl backend okay this works because backend is the

**1:29:44** · backend service which points to the back end Po and we have kubernetes DNS resolution and we see connectivity from front end to back end Works let's try the other way around K exit into back end Po and curl the front end and it works as well great now we will create our Network policy okay so create a new file in your favorite editor called default deny.

**1:30:20** · yo default deny. yo all right and we head to the documentation and steal examples simply search for Network \[Music\] policy and we can simply look for the

**1:30:39** · first example there's another section for default deny actually also here but we will simply work with an example and create it into a default deny policy so simply copy the copy the example code we will have a PO selector we will have the policy types we don't need the whole example we copy it okay we will actually first thing we will rename the network policy to default deny and the PO

**1:31:06** · selector we now say look it should be for all pots so we simply can leave it empty like this and here we have a default deny Network policy for Ingress and agress traffic save it and

**1:31:26** · created okay great now we can run the first EXA comment again from front end to back end and we see doesn't look that good anymore and we run the other EXA command

**1:31:43** · from back end to front end and we see it doesn't work anymore okay netback policies work our default deny policy works great and we set up this example and in the next Hands-On sessions we will then specifically allow certain traffic we will continue with our example and we will now allow front end parts to connect to backend Parts this means we will create one network policy to allow outgoing traffic from front end

**1:32:15** · and one netback policy to to allow incoming traffic from front end to backend and we do it based on P sele if you like feel free to go ahead pause the video Try It Yourself otherwise follow me along and see how I will try to implement it okay on my master note we still have the default deny Network policy it's still applied in the cluster we will now create a second policy called frontend doyo or the the file

**1:32:45** · called front and. yo and I'll head to the kubernetes documentation and I will steal that whole example that we see here and I'll adjust it to our needs okay here we are let's start from the very top I will change the name to front

**1:33:03** · end the pot selector um so the network policy will be applied to pods with label run front end because we created the pods with Cube CTL run they automatically get the labels run that policy let's have a look that policy will be from front end to back end so from front end we will allow egress outgoing traffic to back end which means I will delete the ESS here and um we need the PO selector so

**1:33:34** · what I will actually do I will delete the egress section here I will change this to egress we will allow so we allow egress we will now create our first ESS rule two and then we have already the PO select here that we can steal great so we'll allow igress

**1:33:57** · to run back end okay it's called front end it will be applied to Parts with run front end and will allow outgoing traffic to pots with back end all right let's create the front end Network policy angress okay okay it's called

**1:34:26** · ESS there we go we still have our exec commands here so what I try now kxc I connect from Front End curl back end okay and we see it doesn't work why doesn't it work well we can think right now that it doesn't work because the backend pots still don't low incoming traffic um from frontend Parts because our default deny po policy still

**1:34:55** · applies what we can do now is we will create another policy backend and for this we can simply copy front end to back end because they will be very similar and in the backend policy I will change the name I'll change it to backend this policy will now be applied to backend parts for the backend pods we allow incoming traffic so Ingress and we will create one Ingress rule from coming from CS with the label

**1:35:28** · front end okay let's have a look if we can create this one without any issues yes let's have a look if we can now connect from front end to back

**1:35:45** · end and we see it still doesn't work okay the thing now is that if we want our front end port to connect to the backend service then we need DNS resolution cluster internal DNS resolution but our default deny policy right now even denies DNS traffic on Port 53 so what we can do now is

**1:36:14** · actually we have a look at all pots and their IP addresses and we connect via IP address okay here we can see we have our backend po it has the label run back end front end po has the label run front end okay now what we do is we exec into frontend Po and we do

**1:36:36** · a curl not on the name but towards the IP address of the back end Po and we see it works just a short update if you actually would like to allow DNS resolution for example between front end and backend Parts you could extend your default Deni policy where you would allow some aress to the ports 53 TCP and

**1:37:02** · 53 UDP the link to an example of this is also in the resources section of this video okay and we also can try the other way around we will try to connect to the

**1:37:19** · front end part with the IP of the front end Po from the back end part and it doesn't work right because we only allowed one way we only allowed outgoing traffic from front end and incoming traffic into back end from front

**1:37:40** · end if you didn't manage to get it to run yourself maybe I was a bit too fast at some places you can also head to the course repository it's linked in the video resources Okay so so I'm in course content cluster set up Network policies and in network policies I'm in the front and backend example we can have a look there's also the default deny example that we used before and then the netback policies front and back end um there you

**1:38:05** · have the front end uh you can just copy it and it'll work and there's also the back end you can copy and it will work okay we will extend now our example a final time and we still have our front endend po our back end po the communication works and now we will actually create another pot Cassandra and we will allow back end to talk to Cassandra to our database pots and we

**1:38:35** · will do this by also creating a new namespace so the Cassandra pod will be running in a new namespace Cassandra and we will allow backend pods to have agress traffic to the namespace candra okay for this let's create um the new namespace create namespace Cassandra okay and we can

**1:39:02** · simply edit the namespace and apply some Nables labels to it okay we have metadata labels and we will apply the label namespace candra to it because when we work with network policies and namespace selectors it always works with labels so our Nam spaces in this case have to have

**1:39:26** · labels okay that's done then let's create a Cassandra pod in namespace Cassandra we run Cassandra image engine X just for testing here okay great let's have a look at that pot and the IP address of that pot so we do get po- or white there we

**1:39:53** · go and now we try to EXA from our backend pot and we will try to exec to that to curl that IP and we see it's not allowed why because we didn't specifically allow it yet okay if we have a look in our

**1:40:13** · backend policy then right now we then right now we actually don't allow any aggress traffic we only allow certain traffic but the default deny policy is still in place and the default deny policy still allows any outgoing traffic from any pot so what we have to do here now is to specifically allow outgoing

**1:40:36** · traffic to the namespace Cassandra and we can do this by saying that this policy will now also contain outgoing traffic

**1:40:58** · rules and I copy the whole um Ingress section and I rename it to agress and we now also allow agress to namespace selector um Cassandra so we allow to namespaces which have the namespace label NS Cassandra okay let's try this let's

**1:41:28** · apply our changes seems to be configured and let's try to run our Cur comment again and there we go it works okay so now we actually allowed the back end to connect to Cassandra we can go now even further and also Implement a default deny policy in the namespace Cassandra because we know

**1:41:57** · that's good practice right so what we do is we copy our default deny to default deny candra or or not default deny default is the Nam space so we call it candra

**1:42:19** · deny and what I changed is the name I call it here Cassandra deny and in the name space Cassandra okay we create the

**1:42:40** · one and we try to connect from our backend port to Cassandra again and we see it doesn't work we now have to explicitly allow Ingress coming from backend Parts into Cassandra okay for this what I do now is I simply copy the backend. yo and I call it cassandra.

**1:43:08** · yo and I edit it okay I changed the name to Cassandra that Network policy will be running in the namespace Cassandra it will be applied to pots with the label run Cassandra we will only allow incoming

**1:43:30** · traffic Ingress and we will allow incoming traffic um let's also do it by a namespace selector so we allow incoming traffic from namespace Nam space default okay so Cassandra Cassandra names space c candra we allow incoming traffic Ingress from the namespace with the label namespace ands

**1:44:02** · default let's create it let's run our exit command again and yeah it didn't work yet why well our default namespace doesn't have the label yet so I'll edit the default Nam space and I add the label ands

**1:44:26** · default and now it works okay so what we did in the whole scenario is we allowed one way of connection from front end to back end based on labels and then from back end to Cassandra based on namespace labels so the first one on pot labels the second one on namespace labels I think that's very a good base right now for Network policies and but if you like

**1:44:53** · you like to extend the scenario a little bit more you could restrict it a bit more right now the backend um can connect to Cassandra just based on the names space label you could also restrict it on pots right you could add an additional Port restriction that the connections from back end to Cassandra will only be allowed on Port 80 where the engine X is running by default in our scenario and also for this example that

**1:45:23** · we just did you can also find the solution in our gab repository Network policies example front and backend database there you have all files and you can just use them apply them and play around with them and the link to it is also um available in the resources

**1:45:40** · section of this video and to close the section Network policies I really recommend reading in this case through the document mentation so the link is in the resources but also simply go to the documentation Network policies and read through it it should make things should make more sense let's have have a look at the examples listed there as well and yeah well we talked about Network policies I hope you understand it now way better than before we talked

**1:46:11** · about aggress and Ingress rules you can have them in one network policy or in different ones then they will be merged you can have default Deni policies there's also a set C in the kubernetes documentation about it should you need it in the cks certification exam we white list allow then based on the default denies we create other policies which wi list allow some erress some Ingress rules and yeah we did it on various selectors like pot selectors and namespace

**1:46:49** · selectors control access to buoi elements in this section we will mainly talk about the dashboard in kubernetes we talk about methods of accessing these from the outside and we talk about how to restrict access to these just like as we might have to do in the kues cks

### Cluster Setup - GUI Elements

**1:47:14** · S so GUI elements and the dashboard they should only be exposed externally if needed okay and if you just need to access Services which run inside your cluster like the kubernetes dashboard then you can use tools like Cube C port forward or cube CTL proxy which we'll use so that's better than just exposing them via a not Port service or load balancer service there's the famous Tesla hack from 2018 which was actually caused by a

**1:47:43** · dashboard which had too many privileges and no role-based access control to uh mitigate and it was actually exposed to the Internet so whoever got access to it um had control over the whole cluster which is obviously very bad Cub proxy let's talk about Cub proxy so the main purpose of Cub proxy is that it creates a proxy server between your local host and the cube kubernetes API server so you can use the connection um

**1:48:13** · stored in your Cube config and the credentials to communicate with the API server just over HTTP okay so it's comfortable from your local machine for development or debugging and um if we have a look at CB proxy in an image we have our kubernetes

**1:48:29** · cluster running here we have our API server we have our Cube CTL it communicates secure with the API server and Cube CTL has the cube config with the credentials or at least access to our credentials which we use for connecting if we now create Cube C proxy on our local machine this means we can simply talk to our local machine on HTTP the port that we specified and then we can communicate with the kubernetes API and just send HTTP rest requests to

**1:49:02** · it Q CDL port forward is similar but like the main purpose is to forward trans um communication between your local host and a pot running inside the cluster so it is more generic than CBE C

**1:49:19** · proxy and it can be used for all TCP traffic and not just HTP traffic so if we have a look at a simple overview here for cube CTL port forward then we see our kubernetes cluster we have our API server as before and now we have the kubernetes dashboard running in a pot with a certain IP an internal cluster IP not reachable from the outside we have our CBE C connection

**1:49:43** · again which is secure to our API server and now on our local machine we can create CBE C port forward which will open a local port and on that TCP Port we can connect to our local host on that port and it will redirect the connection directly to the pot okay so this is the main purpose for ql port forward to communicate with a pot running in kubernetes if your API server is running

**1:50:09** · inside a pot in kubernetes then you can also use port forward to communicate with that pot right so it can be a bit Crossing there can be a bit crossing over between proxy and port forward but these are the main purposes to use these it's for sure if you want to have

**1:50:27** · the dashboard and you want to expose it externally without using Cube CTL then you should have some precautions like you could for example do it with an Ingress we will talk about engine X Ingress and securing engine X Ingress as well in this course and then you could have a simple um URL to your cluster like your custom domain SL dashboard and then redirect to the pot but if you do something like this then you have to implement some authentication here using elab um HTTP or or

**1:50:58** · Etc and with this let's move on to the Hands-On sessions we will now install the kubernetes dashboard and for this we should have access to our Master node our cluster should be running our master or worker should be running and ready and all we have to do is head to our favorite browser and search for kubernetes dashboard what we are looking for is the GitHub repository of the kubernetes dashboard we scroll a little bit down and we should see the cube C

**1:51:31** · command which we can simply copy and execute we see various resources where we created there's a new name space kubernetes dashboard and if we have a look into Do's dashboard and we have a look at the

**1:51:53** · pots and services then we can see we have a pot running with the kubernetes dashboard and we have a service kubernetes dashboard which is by default the cluster IP service okay the dashboard is installed and let's move on to use

**1:52:12** · it we will now do something which you should not do at home we will learn by bad example and we will make the dashboard available externally and over HTTP well we have the qns dashboard freshly installed in our cluster and we now want to edit the deployment okay so we do Cube CTL edit in the cuetes dashboard we want to edit a deployment and the deployment is called kubernetes

**1:52:43** · dashboard in there should be a section in these specs where we Define arguments okay and now to find the argument so we we want to enable HTTP insecure access for this we can head back to the GitHub kubernetes dashboard repository if we scroll all the way up there's a doc

**1:53:06** · section and in the doc section is a common section and there we have dashboard arguments okay so it's docs common dashboard arguments and if we scroll down then we see already okay there's an argument insecure Port insecure Port 9090 we move to our CDL edit and we edit

**1:53:34** · we add a new argument the insecure Port we say 90 90 what we also have to do is the autogenerate certificates this is for https access um and you can't have both HTTP and htps ACC access at the same time so we want to remove the autogenerate certificates argument we also need to adjust the livess probe down here otherwise with our changes the container will actually be killed so what we can do simplest is

**1:54:06** · we simply remove the livess probe completely for this example that's enough or we could actually adjust it as well so we can adjust the port to 9090 and the scheme to http save and let's have a look if we configured everything correctly what does the PO say the old one is terminating the new run is running great

**1:54:31** · this work great but if we have a look at the service running in the kubernetes dashboard the kubernetes dashboard service is still a cluster IP service we will now simply change this don't do it at home to a notep service okay so what do we do we simply edit the service and um down here we have cluster IP we change it to not Port okay and up here

**1:55:00** · we change the Target Port so the Target Port is the port of the port okay we enabled 9090 and here it's just the service the internal Service Port we can um or let's just change it to 9090 as well okay so so maybe pause the video we change the type to not Port of the service and the port section we change the port and the Target Port to

**1:55:31** · 9090 save it and let's have a look list the service again and we see it's now a not Port service and we actually have a not Port back here which we can use to connect to it so now we want to connect from the outside so from my local browser I go to my Google Cloud platform and I see my master node my worker node what I want is the external IP address of my worker note which you see here you can click we simply copy the IP

**1:56:05** · address and we type it in the browser there we go and we have to go back to our terminal to the not Port because we need the not Port right to connect to it so for me it's 30 695 I copy

**1:56:22** · it and there we go we have access to the kubernetes dashboard there's nothing to see nothing to display here um which means we have right now actually using the credentials that we use to connect to it it's actually quite secure because we are not allowed to see any of the resources yet okay let's continue with this setup in the next Hands-On sessions

**1:56:51** · we will now give more permissions to the default service account for the kubernetes dashboard and afterwards we will check some other dashboard arguments which might be interesting if we access the kubernetes dashboard now we configured it with insecure Port which means we can access it over HTTP and there's not even any authentication there's not even any lockin form display to us okay but the

**1:57:16** · default service account doesn't have much permissions and if we look at the top notifications here we can actually see that we connect by service Account kubernetes dashboard in kubernetes dashboard namespace we will now provide more permissions using Ro based Access Control we have a whole section about world based Access Control in this course now we're just going to do a short dive into it okay let's have a

**1:57:43** · look at these service accounts in kubernetes dashboard namespace and there we see a service account called kubernetes dashboard what we also do is we look at cluster roles by the name View and there we see a default existing cluster role in kubernetes is called view which allows to view all resources we will now assign

**1:58:07** · the cuties dashboard service account with the cluster Ro view by creating a role binding what we do for this is in namespace kubernetes dashboard we will create a row

**1:58:25** · binding we call the row binding insecure and we want to connect our service account service accounts are always referenced by namespace colon service account name which in this case is kubernetes dashboard colon kubernetes dashboard and we want to connect it with a cluster role called view okay I will now do a dry run so we

**1:58:51** · can have a look what will be executed we will create a r binding and we reference the cluster roll View and with we connect it with our service account in kubernetes dashboard namespace named kubernetes dashboard looking nice let's actually create the resource there we go and we will head back to our dashboard we will refresh it and we have a look at if something changed

**1:59:23** · if we now head to the kubernetes dashboard namespace on top here then we can actually see there are some resources because we now provided how the kubernetes dashboard service account only permissions inside the same namespace okay what we can also do to give even more access we could go ahead and not

**1:59:54** · create a row binding but create a cluster roll binding okay we can simply create a cluster roll binding insecure like this and now this means that the kubernetes dashboard service account has cluster wide view access means if we refresh and we now actually see on top

**2:00:17** · that we actually see a list of all namespaces and we can actually see that in the cube system namespace we now also have access to this finally we will now look at some interesting dashboard security arguments some we already work with so we can head to the dashboard arguments read me in the gab repository okay well there is the insecure Port one which we configured to configure uh to configure insecure access by HTTP and also skip the

**2:00:48** · Authentication there are um TLS SE file and TLS key file if you want to specify your own certificate otherwise for htps there's the autogenerate certificates one and if we scroll down there's also authentication mode which is by default

**2:01:06** · on token which means it's configured to use Ro based access control but it can also be configured to basic which means it's not using role based Access Control well and then there is the enable skip Lo in which if it's said to true then it skips login which is also not bad so you might have to configure or to to remove some of these in the

**2:01:28** · certification if you like to dive in a bit more there is the um a nice read me under docs user access control the access control read me which goes into the best suggestions of how to make your kubernetes dashboard secure I also linked to this read me in the resources section of this video well and just to recap um only expose your services

**2:01:51** · externally if you need to and if they are like protected um and force authentication restrict using role based access control and we learned how to change some of the arguments of the kubernetes dashboard when you work with the kubernetes documentation it is always important that you work with the correct version if you right now work with kubernetes 1.6 then you should go on top right and and select 1.6 same for 17 18 19 let's for example

### K8s Docs Version

**2:02:25** · select 1.19 we can actually see that URL here changed and there's a warning that we actually work with 1.9 which is not the latest stable so just always make sure with which version you are working in your cluster and that you then also read the proper documentation specific for that version

### Cluster Setup - Secure Ingress

**2:02:51** · Ingress objects with security control what will we talk about today first we'll talk about what an Ingress is how it works internally then we'll set up our own Ingress um with some redirection to internal services and finally we will secure this Ingress with TLS what is an Ingress well the kubernetes Ingress is very simple we will now simply talk about engine X Ingress but they're different ingresses

**2:03:21** · um and an engine X Ingress in kubernetes will create in the end a simple pot with an engine X running in it and the Ingress is a wrapper around it which then creates the engine X config running in that pot so it means we simply

**2:03:39** · create um yo resources like we usually do like an Ingress resource and by creating these Ingress resources the Ingress controller will actually generate the engine X config so we if everything goes well never have to touch the engine X config we just can configure it comfortably by creating an Ingress resource um because when we create an

**2:04:06** · Ingress we will have in the end a pot with engine X running in it we still have to make it reachable from the outside right and usually if you have an Ingress you want to have it because you want to have some some requests which come into your cluster from the outside and you want to redirect it on some conditions this means if you have an Ingress and through the engine X Ingress we have a pot with engine X running we still have to use a service okay and

**2:04:33** · because of this I just want to make a small recap about the kubernetes services and then we can jump um right into creating our own Ingress so the service in kubernetes these three main Services the first one is cluster IP service and the service always points to pots never to deployments or demon sets always point to pots via labels and a cluster IP service means that your pot has like a cluster internal IP and is reachable internally by that IP and also by a DNS name all

**2:05:06** · just cluster internally based on this we have the notep Pod service and I think it helps um to imagine it like a notep pod service creates a cluster IP service because internally a notp pod service works exactly like a cluster IP service with the addition that a nport service opens a port on every note and request coming into that Port

**2:05:31** · will be redirected to the cluster IP internal service okay so a not Port service makes a cluster IP service reachable from the outside if you create a notot service there will only be one service type notep right there won't be two Serv services but it helps to imagine it like this because internally a notep pod service works exactly like a clust IP

**2:05:55** · service and then we have the Lo balancer service and again a Lo balancer service creates a not pod service creates a class typy service because a Lo balancer service works exactly like a notepad service and exactly like a cluster IP service in addition the Lo balancer will

**2:06:11** · communicate with whoever created the cluster it might be Google Cloud AWS it might be yourself and whoever created the cluster um kubernetes can then communicate to to uh to the manager that it wants to create a load balancer for all the nodes

**2:06:28** · which have a open not Port so that's the only addition um to create the external load balancer to all the nodes which have an open port okay so much to the engine X Ingress and let's continue with the Hands-On session

**2:06:56** · we will now set up the engine X Ingress which we will later secure okay so what we will do we have our kubernetes cluster we will have our engine X Ingress and we will expose it via a notep pod service so that reest

**2:07:12** · from the outside can actually reach our Ingress and then we will Implement a path redirection on/ service one redirect to one cluster IP service and the pot and/ service 2 redirect to another cluster IP service and another pot okay so get your cluster

**2:07:30** · ready and follow me along you can see I'm on my master node my cluster yeah has a running master node a running worker node all perfect so the first thing we have to do is we have to install engine X Ingress for this head to the resources section there you find a simple comment you can run and and it installs the engine X Ingress controller yaml from our GitHub repository and you can also check the GitHub repository there's also an example for the Ingress resources which we can use in this

**2:08:02** · section and that should be it various resources have been created among these is a new namespace engine X Ingress and let's have a look what happened in that namespace if you look for pots and services in that namespace and we can see we have one pot which is the engine Ingress

**2:08:26** · engine x controller and this is the pot where engine X is actually running in um with some engine X configuration which is created for us and which we will create indirectly by creating an Ingress resource very soon we also see a

**2:08:43** · service Ingress engine x controller type not Port perfect if we look at our scenar scario that's what we want to have and the not Port has two ports so one for Port 80 one for 443 for https and um yeah so by default

**2:09:03** · everything seems already to be running we have a pot with engine X we have a notep pod so let's try it out what we do is we now want to have the external IP address of our worker note Okay so in my Google Cloud console

**2:09:20** · um I'm I see my CS worker I see the external IP address I can click here I copy the IP address and now what I actually want to do I want to connect to the cluster from the outside right and when we first set up the cluster we configured some firewall rules that it's possible um to

**2:09:41** · access from the outside on the Note ports that can be opened on the notes so what I will do in this terminal here this terminal now is on my local laptop okay and what I can do now is I simply do curl to the external IP of my worker not and I need the port so I

**2:10:03** · switch back to my master terminal and I copy the HTTP not \[Music\] Port run it perfect it's working okay we get a four four not found but um it's at least not a connection error which means we actually connect to the engine X Ingress which is running and setup next what we would like to do is

**2:10:31** · we want to extend the default configuration right we want to uh include SL service one and SL service 2 for this we will simply steal some engine X from the kubernetes documentation or instead of going along with me through the documentation you can also head again to the GitHub repository Link in the resources and just use the example that we have there so we head to the vetes

**2:11:03** · documentation we search for Ingress and scroll down a little bit there should be a nice example perfect we simply copy this example I'm in my master node I create a new file Ingress doyo there we are okay the first path we

**2:11:29** · change it to service one and we say so this is a path right a request comes in on path service one and we be redirected to a backend service named we name it as well service one on Port 80 okay and then we would like to duplicate this one for um for service

**2:11:56** · 2 I'm using Vim here but you can use any any editor that you like right and on top here we will call the Ingress secure Ingress okay that's just the name that we give our Ingress all right in more recent version of the engine X Ingress controller we actually also need to specify the Ingress class name as you see here so best to take it from the GitHub

**2:12:28** · repository we save it and we create the Ingress resource and here we can see our Ingress resource called secure Ingress so we kind of have these steps done now what's the left is um actually the services to which the Ingress can redirect to okay so we now create two simple pods with two simple services and then that whole scenario is already

**2:13:00** · done what I do is I simply create a simple pot so let's create a first pot um a simple po we call it pot one with image engine X and then we create a second pot with image httpd just that we keep the responses that they give us apart and then we create services or we expose our ports so we expose the Port Port

**2:13:31** · one port 80 and we give the service the name service one and we do the same thing for service two and this should be it okay um we

**2:13:48** · should have the whole scenario set up just as it is here so let's head to I head back to my main terminal you should do the same we repeat the curl command which means now we can pass service one and we see a default engine X welcome page from our P one we can repeat it for service two and we see that's the default page for the HTTP Apache po Okay so we created our

**2:14:18** · scenario and we can continue securing

**2:14:36** · it we will now continue to secure our Ingress via htps okay so all the request which reach our notep pod service and our engine X inest should be secured over htps okay if we had back to our master and we

**2:14:59** · can see here's our Ingress but if we have a look in the engine X Ingress Nam space and look at these service resources we see the not Port service and we see the not Port service has already two ports configured so there is already an https Port available that let

**2:15:17** · try it out right copy the um your not Port might be different copy the not port for the 4 Force remap Port go back to your local terminal and call your external IP address of your worker note with the not Port service for https run it and okay it says um that it

**2:15:45** · can't verify the certificate and when we we use c-k we can actually accept self-signed certificates and well it seems to work htps seems to be set up already what's happening there we run the comment again um with V for like um ver both action so we get more data and we have a look what happened okay what we see here now is

**2:16:13** · some information about the request and the response and the response from the server has a section about the server certificate okay and if you look at the server certificate CN the common name then we see it says kubernetes Ingress controller fake certificate okay if we don't configure any TLS certificate from

**2:16:35** · ourself then from some version it started that the engine X Ingress already creates a self-signed fake certificate okay what we would like to do is now to to change this to use our on certificate okay so for this we head back to the um Ingress

**2:16:56** · documentation and we can scroll down on the right menu and we see TLS and um well you can read through it if you like but in the end we have to create a secret which contains our certificate and our key and then we have to extend our and our Ingress configuration

**2:17:18** · and yeah reference at secret okay so first step let's create a secret which we will'll use for testing now we will also use a self-signed certificate and I actually um run the comment already so you can just stop the

**2:17:36** · video um type the comment off or I um we also add it to the resource section so it's a simple op SSL command which creates a certificate and a key and and um you won't have to uh memorize or use

**2:17:52** · these open SFL comments in the in the real certification you will work with given certificates or given comments that you just have to run when we execute the comment then the key will be generated and then for the certificate we have to enter some information but we can leave everything free only what we have to enter is the CN or the common name and the common name is now the domain name and we call our domain name which simply call it

**2:18:20** · secure ingress.com \[Music\] that's all that we have to do and then if we have a look we now have a certificate and we have a key and using that certificate and key we can create a secret in kubernetes okay create secret the help s side- is always helpful we see there's a type TLS

**2:18:51** · and we see an example comment on top here perfect we simply use this we call the secret also same as we call the Ingress secure Ingress we specify theer and the \[Music\]

**2:19:12** · key and if we look at our Ingress objects and our secret objects we now c a secret secure Ingress which holds our TLS certificate perfect now what we would like to do is we would like to edit our Ingress so open your Ingress yaml file on your master note and we would like to edit it for this we head back to the documentation and have a look how they do it we can see that there's a TLS section we simply copy it

**2:19:43** · and steal it again and for the host we now have to specify the same host name that we used to generate the certificate okay which is secure ingress.com and the secret name

**2:20:00** · which is now the kubernetes secret is secure Ingress okay so SSL certificates are always bound to one or more um common names which are represented in the certificate we also under the rulle section have to specify a host

**2:20:28** · now and the host name is the same secure ingress.com okay this should be the setup let's apply our

**2:20:44** · changes perfect we didn't make any mistakes that's that's great and now we can head back to our local terminal where we run curl and if we run curl just like before again then nothing will change if we look here the server certificate is still the very same fake certificate why

**2:21:09** · because if we look in our Ingress resource then we see we specify the domain name right now these whole um rules like the path rule SL service one the path rule SL service 2 only um works for this secure

**2:21:27** · ingress.com domain and only for this secure ingress.com domain we use our secure Ingress secret which contains our certificate so we have to actually contact that domain and what we can do in curl is is actually we now contact the domain I just copy the

**2:21:54** · external IP address of my worker not and I mean the domain doesn't exist right it doesn't belong to us it's a fake domain we could create a host entry now in/ Etc host for this domain name just for local testing or what curl also provides we can do the resolve argument we want to

**2:22:13** · resolve the domain name secure ingress.com and we have to pass the port here as well when we use it with curl and we want to resolve it to that IP address okay so this section in the back here uh

**2:22:28** · has the same effect as if we create a host entry for local testing so now we send our https request to that domain and let's have a look what happens um we see that the server output the server certificate now actually is a different one we see the CN is is exactly dcn um secure ingress.com which we created so the Ingress is now using

**2:22:54** · our certificate in the end we did set up the scenario just like we wanted our Ingress is now secured by TLS https and not just by the fake Ingress um certificate but by our fake certificate

**2:23:16** · okay well that's the end of the Ingress section you should definitely be comfortable with creating ingresses and working with and editing existing ingresses by creating secrets and then applying these secrets with the Ingress configuration if you do this and you manage this um then you should be fine when it comes to ingresses or securing ingresses in the

**2:23:46** · C protect node metad data and endpoints we will talk about node metad data when it comes to Cloud platforms what it is next we will actually access sensitive not metad data and finally we will restrict it using network policies Cloud platform note metadata

### Cluster Setup - Node Metadata Protection

**2:24:14** · what is this if we spin up virtual machines in a cloud provider of our choice Google Cloud AWS AIA then there's usually a metadata server which we don't manage which the cloud provider manages for us but the virtual machines are able to connect with this metadata server and get some information about the environment about the service account they use and there can be credentials and sensitive information to spin up um their

**2:24:44** · services so metadata service API is by default reachable from virtual machines it can contain Cloud credentials for VMS and not so sensitive information and this can mean for example data to provision the CET credentials on on a worker note so limiting the position uh the

**2:25:06** · permissions for instance credentials this is kind of outside of the scope of kubernetes This Means ensuring that the cloud instance account so the account which the instance can use to connect to the metadata server or to other apis um

**2:25:22** · that it only has the necessary permissions right and each cloud provider has a set of recommendations for it some maybe have good default settings for some you might have to adjust it but this is not in the hands of kubernetes and this goes too much into Cloud management um but it's just something that you should be aware

**2:25:44** · of restricting access using Network policies well if we have now a cloud account like uh in Google cloud like we actually have and um we build our own kubernetes cluster as we see here then we might have a worker node virtual machine right as we do we have one master and one worker and then in that

**2:26:07** · worker we have some pots running which are actually run as processes uh as Stocker containers and processes internally on the operator system and then by default these pots and containers can also contact the metadata server right so it's not even a matter that that someone has to break out of a container and then from the node contact the metadata server like even before this without usually with the default

**2:26:36** · configuration it's possible for pots to contact the metadata server and maybe to query sensitive information so what we can do with network policies is to allow certain parts to access these and to deny certain parts to access

**2:26:58** · these we will now access gcp Google Cloud metadata from an instance and from a pot for this I'm on my master note the cluster is ready as always and I'm actually on a Google Cloud page page called storing and retrieving instance metadata the link is in the resources section of this video

**2:27:24** · and this again accessing the metadata server the metadata server exists for most Cloud providers but it's it's different it's cloud provider depend on how to access it right it might be just the IP it might be a domain name that you have to create so it's dependent but here also you see caution a process can create the metadata URL a process that can create the metadata URL has access to all values in the metadata server so there are some examples so we can simply search for curl and I saw something

**2:27:56** · about quering discs exactly so we simply copy the comment executed and we see we we actually got a got a response and um we we get some information back so it's not really about the information that we get back right now it's simply the fact that we can connect to the metadata server

**2:28:18** · now we see that we can do it from the instance from the master instance it will work the same from the from the worker instance it's simply two virtual machines but now the thing is it also works from pots so we create a simple pot called engine X image engine X it already exists great um I simply exac into it get a shell and then run

**2:28:45** · the same comment and we see it works okay so by default we see now that pots can access the gcp metadata server just like

**2:29:00** · that we will now only allow certain parts having a certain label to access the endpoint for this we will create two Network policies which are actually in our GitHub repository the link is in the resources of this video I mean we have um already a big section about Network policy so we don't go very in very much into detail here and we simply create the two existing Network policies and have a look at them the first one we want to have a look at is the deny one so npcloud metadata

**2:29:33** · deny and here we see that we have a pot selector for everything so not just specific pots this will be for all pots in the namespace default it's about outgoing traffic and we have one outgoing traffic rule which means we allow outgoing traffic to all IP

**2:29:53** · addresses except the one of the metadata server okay and that IP address um we can see if we ping that one that's the IP address of the metadata Google internal server okay copy the network policy and create it I call the file deny. yo there we go it's already here and I will create

**2:30:23** · it there we go we exec back into our engine expert and we try to run curl again and it doesn't work okay this might be something that's a good procedure to do to deny CS to access the metadata server now we go ahead and look at the second one npcloud metadata allow here here we have a PO selector for roll metadata accessor and

**2:30:51** · these metadata accessor we allow We additionally allow aggress to IP block and then the IP of the um metadata server so this second one if you would only create this one alone then these pots would only have access to this IP address okay but if you create it in conjunction together with the deny one then pots will get this rule so they

**2:31:24** · can connect to everything except this one plus the other rule that they can connect to this one okay might be a bit confusing maybe pause the video and uh look at both and um just imagine that if the deny Network policy and the allow Network policy would be merged then the first rule would be invalidated by the second rule kind of so go ahead copy the allow Network policy I call it allow.

**2:31:58** · yo and create it great now if we have a look at the pots and their labels then we see right now it has the label run engine X and we would like to give it the label row metadata accessor to test so what we can do is K label pot and we say row metadata accessor K label po the

**2:32:33** · name is engine X there we go we check labels again and now our engine X po has the label row metadata accessor okay we EXA back into the but and we can see yes we can curl the metadata service and to verify that it actually works I going to remove the label again

**2:32:58** · so we see here in my pot I have the label row metadata accessor I will remove it again EXA back into the pot try to execute it again and it doesn't work okay so yeah play around with this a little bit um using this we were able to default deny for all pots the access

**2:33:19** · to the metadata endpoint and then simply allow it for certain parts having a certain L and just a quick recap to end this section we talked about Cloud metadata servers we talked about that they're different for every cloud provider how to access them usually it's possible to access them from every instance and usually instances need it as well if they have to spin up certain services but the access by default is also possible from pots which is usually not

**2:33:51** · needed and which should be restricted so it's something to think about and it's possible to restrict these for example using network

### Cluster Setup - CIS Benchmarks

**2:34:13** · policies CIS benchmarks use CIS benchmarks to review security configuration I will first give you a little introductional overview about what CS benchmarks are then we will jump right into a Hands-On session CS benchmarks in action and later on we will use Cube bench to investigate our cluster and to apply security

**2:34:36** · recommendations CIS benchmarks so CIS is the center for Internet Security and they provide best practices for security configuration of Target systems and they cover as of now more than 14 different technology groups which means not just kubernetes okay they have recommendations for for different software products and to site CIS benchmarks is developed through unic consensus based process comprised of cyber Security Professionals and subject matter experts around the world well if

**2:35:06** · that doesn't make you feel more secure then I don't know what will okay CIS benchmarks so CS benchmarks now just kubernetes because that's interesting for us they provide default kubernetes security rules we as administrators let's say we

**2:35:23** · administrator administrate our own cluster we can then just use these rules and use and apply them like if we have a cluster we set it up with Rancher or we set it up with Cube ADM we can use these rules and um apply them and then we now we have already a good security base right and if you want to adjust this then you can do it as well like if you're a big company and um like for example Google cloud and AWS they do this for their managed kubernetes solutions they use the C benchmarks as a

**2:35:54** · base they customize them and then they use and apply them Google does it a bit longer already and um they provide online a list so it's like transparent which rules they take which rules they maybe Define more strict to be and which rules they Define l strict to be right and then it's really transparent from security because security is best when it's transparent so I like this um yeah

**2:36:20** · and then you can see what rules are applied so if you are a company um which is pretty large enough and you want to customize the Cs benchmarks then you can do this as well before you apply them so that's the general idea of CIS

**2:36:38** · benchmarks okay in this Hands-On session we will actually download and investigate the kubernetes bench marks PDF okay so for this you have to head to your browser and search really difficult CIS benchmarks kubernetes and then you should see the website C CS security.org you click on kubernetes benchmarks and

**2:37:04** · download latest CIS benchmarks you can see for me right now it's version 160 just download the latest version for you and yes it is free but um just pause the video now fill in the information click the button wait for the email and then you can download the PDF pause the video do it now there you go you should have your PDF open you see I have the PDF open I'm

**2:37:29** · using version 160 and what should we do in the 10 on session check kubernetes version of your document what does this mean okay because it was a bit confusing because the numbers doesn't mean it doesn't have anything to do with the number of the kubernetes cluster kubernetes version that this is applied to okay so we scroll down a little bit um okay at

**2:37:52** · first we see the um the content of the document and the content is structured we see one are the control plane components Master node for example and if we scroll down um to section two we see section two is about at CD and then section four is about worker nodes right so that's how it's structured and then there are like various rules for the various components of kubernetes and if we scroll first are down there should be an overview section in the overview section you see this document is made for Cuties versions 116 and 118 we WR now work with kubernetes

**2:38:25** · 119 but um yeah I mean it doesn't it doesn't matter just just use if you work with a kubernetes version which is above or like one or two versions above um not that much should have changed okay and what's also important is that these rules are applied by the default configuration of cube ADM so wherever Cube ADM puts its configuration files this document uses this already and this is great because the cks um the Clusters that you use in the ckss certification are all configured

**2:38:58** · using Cube ADM okay and we also use Cube ADM in this course so that's all perfect okay now we just look at two example rules okay so in my document it's page 16 rule 111 it might be on a different page for you but the the rule number should be the same so I go to page 16 it's actually 17 for me okay let's just

**2:39:24** · have a look at one example rule okay just that you a bit com uh con that you get a bit used to how the documents are structured so we are at Master node configuration and 1.111 ensure that the API server po specification file permissions are set to 644 or more restrictive okay and then

**2:39:46** · you simply have a description what it is okay so we have to check some file permissions and then you have an audit so you can actually run this command to check what the file permissions are and then you check if it's less or more restrictive okay and if it's not like that then you see the comment that you can execute to fix it okay so you have a

**2:40:08** · comment to execute to check it and you have a commment to execute to fix it it's really simple okay um let's have a look at another example as well for me it's on page 208 for the worker note rule 4210 so page 208 rule 4210 ensure that the tlser file and TLS

**2:40:33** · private file arguments are set as appropriate okay and then for auditing we do a PS so we look at the process and we look with which parameters the process is run then we have a recommendation ation and then uh in the recommendation it says how we where we can change it we see in this config file we can change it what we should do and then we have to restart the service and do it like this okay

**2:40:58** · feel free to check a few rules out not at all do you have to remember any of the rules you don't have to apply these rules you don't even have to look at the PDF document in the um real cks certification right but you should just be comfortable with the structure and you should now um how to apply a rule you know how to how to maybe fix it like you you might be faced with a unsecure cluster you will be provided with some rules and then you have to to change and fix the

**2:41:28** · cluster um in the whole PDF you saw it was always structured right it was there was always a comment um how to check it and then an instruction how to fix it this could also be automated right this sounds like we don't have to even use a PDF document it sounds like like this could be something that a program could do as well for us and yes that's right we will do this in the next

**2:41:58** · section we will now use cubench run it on the master node and apply or check one rule and maybe fix it if it's not properly correctly configured right now what will we do okay we need to run Cube bench okay okay for this um just search

**2:42:18** · cubench GitHub it should be the aqua security cubench repository and in there in the read me you see various methods of installing it of running it but look at running inside the container okay not installing from a container look at running inside a container and there you see a very simple Docker command that you can run copy that command head to your master

**2:42:47** · not and um here you see um you can actually um pass a parameter to the container and this is like master or node right so if you're on the master you want to check your master node you should pass master if you want to check your worker note you should pass note um type your version uh 1.19 I'll do and

**2:43:09** · just run the comment okay you might I mean in the real world you might want to install it like you don't have to do this you don't have to install cubench in the cks certification you will either be provided with it or you you will just be provided with the rules so we run it and we see a summary down here 43 checks passed 12 failed 10 warnings okay 12

**2:43:31** · failed let's have a look scroll up a little bit and here we see a nice colorful overview and we see one failed rule is 1.12 okay you could now also check in your um let's actually do it let's check the rule 1.12 in the PDF

**2:43:53** · document that's the one ensure that the at CD data directory ownership is set to at CD at CD doesn't seem like it is okay so auditing we can have a look we can run that comment and there we see right now it is at root root at least for me and that version that I'm using right now what can we do to fix it let's have a look recommendation okay I going to run this

**2:44:25** · comment invalid user right let's simply add uh for testing uh at CD user okay this seems to work I going to run the check command again and it is at CD at CD and now we can can run the docker commment again so we run cubench

**2:44:50** · again and we see that 44 checks passed this looks better we scroll up and we can see that 1.1.2 the rule that we just checked pass now okay um yeah maybe you should be comfortable with Cube ADM like this um maybe just pick another rule maybe also lock into your worker note

**2:45:12** · and run the command then not with Master here but with note and maybe um fix the rule there as well on the on the ql for example okay well and yeah this shows you what Cube bench does it can check the rules

**2:45:30** · automatically for you and based on this I don't know you could for example implement this in your continuous integration system or just send it to someone who should work and fix on these security issues and to finish this session um just some remarks I would like to shortly show you the gcp CIS benchmarks so we can simply go to browser and um type in gcloud CS

**2:45:58** · benchmarks and we see a page from Google actually cloud.google.com CIS benchmarks and on that page they explain a little bit and if we scroll down then we actually see the um CIS benchmarks and the level and um if they passed or if they fail you know um and yeah and there

**2:46:18** · you see what they actually apply in their um GK as well like the default values for their gke cluster okay so this is like really interesting really transparent AWS followed as well probably I don't know about Asia or others but they will probably follow as

**2:46:37** · well if you are more interested there's a nice talk um by Martin white consistent security control so has benchmarks with explains it um a lot better the link is posted in the resources section there's also tool Docker bench if you're interested in it which um checks your Docker configuration I mean we will later touch on this as well because your kubernetes cluster is only secure if your container runtime is

**2:47:04** · secure itself we will work on on container level a bit more later so Docker bench might also be interesting not maybe not too interesting for the cks certification there it's more interesting to use Cube bench well and that's the end we learned what CS benchmarks are we learned how to use them with Cube bench like to check and we learned then based on the um CIS Benchmark recommendation to manually check and also to apply and fix and that's important for the certification to

**2:47:43** · now verify platform binaries we will shortly talk about heshes then we will download and verify some kubernetes binaries and finally we do the same from a kubernetes binary running inside a

### Cluster Setup - Verify Platform Binaries

**2:48:04** · container well if we have a file and we want to validate it we want to check that it's actually the file from the original Source what we can do is we can create create some kind of a fingerprint of that file right and a fingerprint of a file would then be called a hash there are different algorithms like sha or md5 you probably have heard about these These are kind of these are one-way algorithms so it means from a file you can calculate the hash but from a hash

**2:48:35** · you can't calculate the file back okay so it's kind of a compression algorithm and a loss for compression algorithm and yeah so what we can do to verify platform binaries which we'll do on the example of kubernetes is to check the hash value which is provided from The Trusted original source with the hash value that we create of the

**2:49:01** · file we will now download a kubernetes release from GitHub and then verify the downloaded files what you should do is you should head to your master note you should do Cube CDL get nodes and then you should check the kues version that you running I'm using 11 191 you might use a later version depending on which version we have in the course install scripts right now so remember that version and then head to github.com kubernetes kubernetes okay so on there

**2:49:35** · you should see releases or you can see here the text and if you click on text what you can do is simply open any tag release and then on top you can simply replace it you see what I do here I replace it with 1191 and there you go this is my release

**2:49:56** · version and then down here we see additional binary downloads are linked in the change lock change lock so click on there okay here we have the client binaries which are for example the cuet and then we have the server binaries and we would like to download the server B binaries okay so here we see the server binary file um amd64 server Linux and

**2:50:22** · here we actually see already a sha 512 hash which we would compare after downloading the file so copy the link head to your master note download it there we go okay downloaded the file

**2:50:39** · we have it here now what can we do to compare the hash value right we saw it it's hash sha 512 and there should be by default sha 512 some command on every Linux machine so we can just call it um

**2:50:56** · pass the file name and there we go we see the generated hash what can we do now to compare these hashes well we can have a short look with our eyes and say right now I check the beginning I check the end yes it looks fine but um we can also do it a bit more thoroughly so what I we usually do is I pass the output in a new file compare head into into the new file and

**2:51:25** · let me remove me for a second and here on uh top right I'll just Ed it so I only want to have the hash in that file right so I remove the rest of it and then I head to github.com to The

**2:51:43** · Trusted source and copy that hash paste it in and yes it looks very similar it looks fine but what we can also do is uh we simply output the compare file there we see both lines and then we pipe it into unic and then it only displays unique lines and then we see yes it only displays one which means these two are unique so what we did right now is we downloaded the release from kubernetes

**2:52:15** · from the server binaries the same one as of our kubernetes version installed and then we verified it with the provided hash from the original Source now it gets really interesting because now we want to compare the API server binary running inside our container with the one that we

**2:52:43** · downloaded for this we are on our Master node control plane and we downloaded the kubernetes server binaries and we should extract these which can take a little bit because in some they're actually quite

**2:53:11** · large and in that extracted folder we can actually have a look in the server directory bin directory and there we see for example the API server binary controller manager

**2:53:29** · Etc so we need to make sure to be able to compare this now that we have the proper version right so what we can actually do is we can simply run the cube API server binary attach version and we see I'm using version 1.22 do2 and I'm using that version because in my cluster on my master note right now that version is also running how can we find this out well in the

**2:54:01** · cube system namespace there should be a pot running for the API server there we go it's running as a static pod via Cube ADM manest and if we have a look at what image it's running then we actually see okay I'm also running right now version 1.

**2:54:26** · 122.2mi

**2:54:45** · there we go and what I do is I write it into a new file compare now we need for the comparison we need to have the shum of the binary running inside the container right so what can we do well we can try to exit into the

**2:55:08** · container and we try to get a shell doesn't seem to work we try to get a bash doesn't seem to work okay so these containers of the kubernetes components can be considered hardened already because they don't even include a shell they're probably kind of started From Scratch and only the actual binaries um pre-compiled from golang are

**2:55:32** · actually in that container and run so it's like really minimalistic so what can we do well we know that the API server is running as a pot on the on our not note on which we are right now so we can have a look using cctl and there we see it's running here which means we should also see the processes from that

**2:56:03** · container and there we go there we actually see the cube API server process and what we also see is the P ID of the process it might be a different P ID for you right using this p ID we can now actually access the file system through the proc directory so what what we can do is we have a look into proc then the P ID of our process and then in the root directory and there we see the actual the root file system of the

**2:56:34** · container so what can we do well let's search the whole root directory and look for the cube API server and there we have it so we can simply generate the sh sum for this one and append it to our compare file

**2:56:56** · now let's have a look in the compare file just from me looking at it it looks like it's the same value it's the same hush which pretty good but I can also go ahead and

**2:57:12** · clean this up a little bit remove the binary files there we go and if we pipe it into unique then we see it's actually just one line and there we go we compared the hashes and in this case the cube API server binary that we downloaded is exactly the same as the one that is running in our kubernetes API

**2:57:40** · server well this was a pretty short but for me interesting section we learned what hashes of files are we learned how to verify hashes um using the Sha 512 sum comment and then we even went a bit further and extracted a binary out of a running container and compared that binary as well to a um trusted Source um

**2:58:04** · this might be a bit outside of the scope of the ckss but well you never know what will be happen right

### Cluster Hardening - RBAC

**2:58:24** · Ro based Access Control very important very big topic I hope you're ready I'm definitely ready we will first talk about Ro based access control and I will explain it to you simply and Visually afterwards we will create a few scenarios and we also work with certificates and users Ro based exit control is a general

**2:58:45** · concept of regulating access to computer and network resources based on the roles of individual users within your organization kubernetes has it as well since early versions and it's enabled via the authorization mode string it's default always allow but there's also

**2:59:03** · the RO based access control which is if you have a cube ADM cluster it's enabled by default so we can use it to restrict access to resour ources when accessed by users or service accounts and we will talk about users and service accounts later as well but we will work with we always work with roles and role bindings and you always specify what is allowed and everything else is denied so you Whit list what is allowed there's no deny rules in Ro base Access Control in

**2:59:36** · kubernetes only access data or information that is necessary for the legitimate purpose so it's kind of the princip of Le least privilege which should always be in the back of our minds when we Define role based access control rules and let's talk about namespaced

**2:59:55** · and non-n namespaced resources before we jump into the RO Bas Access Control resources so kubernetes has Nam spaced and non-name spaced resources we can actually look at them um if we run Cube CTL API resources and then the namespace parameter true or false namespace resources are for example pots non-name space resources are for example nodes or persistent volumes and um yeah if we look at role

**3:00:23** · based access control then there we also have the namespaced role and the non-name spaced cluster role okay and the role and the cluster role they Define a set of permissions and the set of permissions can be can edit pots can read Secrets okay so we Define a set of

**3:00:42** · permissions then we have role binding and cluster role binding and with these bindings we Define who gets a set of permissions like bind a role or cluster role to something or someone so when we look at roles to

**3:00:59** · describe them we could ask the questions where are the permissions available okay so we Define a set of permissions and we say where it is available like when we Define a role then we Define a set of permissions which is available in one name space if we Define a cluster row then we Define a set of permissions which is available in all Nam spaces and also globally in the

**3:01:22** · cluster okay when we go to the right side with the bindings then we can ask the questions where is a set of permissions applied because if we use a role binding then it's applied in one namespace if we use a cluster role binding then it's applied in all Nam spaces using these four resources there

**3:01:43** · are various combinations of these and we will get into the valid combinations um just in a few slides ahead let's have a look at a role like like an example role we call it secret manager and it is in namespace blue

**3:02:03** · right under rules we have resources so this is about secrets and we are allowed to get watch and list Secrets now we create a second role which is very similar it's also called secret manager but it's available in namespace red okay we have one in namespace blue one in namespace red and the one in namespace red allows less it only allows

**3:02:27** · us to get Secrets whereas the other one allows us to get watch and list seets so using this we have the same role we have the same role with the same name secret manager in two name spaces but in every

**3:02:43** · name space um it allows different it has different permissions it allows us to have different actions right so a user can be secret manager in multiple namespaces but the permissions are different in each namespace now let's look at the example when using a cluster role now we have a cluster role secret manager instead of a role as before and it allows us to get

**3:03:08** · Secrets as you see there is no namespace in a cluster role because it's a nonn namespace resource source and this would allow us then a user can be secret manager in multiple Nam spaces but the permissions are the same in every namespace okay this just as like two examples two example usages between a rle and a cluster

**3:03:35** · rle if we look at a cluster rle then we have to be careful right we should be careful with cluster roles and cluster R bindings because because they apply to all current and future namespaced and non-n namespaced resources if you have three namespaces and you say yes my user should have access to all these three name spaces then you can create a cluster on a cluster role binding but you should be aware that as as soon as you add a new name space in the future

**3:04:02** · the user having that cluster R and cluster R binding will automatically get access to that namespace created in the future so be careful with cluster roles we now look at combinations okay we again have our four resources for robas Access Control we have a roll we have a cluster role we have a ro binding we have a cluster role binding how can we combine these okay we remember a role

**3:04:29** · defines a set of permissions and is this the set of permission is available in one name space we can combine the role with a role binding which means that that set of permissions is applied in a single name space okay set of permissions is available in a single name space is applied in a single name space this

**3:04:52** · works another combination is we Define a cluster rle so with a cluster rle we Define a set of permissions which is available in all Nam spaces and then we combine this with a cluster role binding which means the user has that set of permissions in all Nam spaces set of permissions is available in all namespaces set of misss is applied in all Nam

**3:05:17** · spaces another combination is we still have a cluster role set of permissions available in all namespaces we now apply it just in one or in a few Nam spaces right because the set of permission is available in all names spaces but we just apply it maybe in one Nam space or in to namespace by creating a r binding in all these namespaces

**3:05:46** · well is there another combination can we create or combine a role with a cluster Ro binding no we can't do this why well because a role defines a set of permissions which is only available in one namespace and if it's only available in one namespace then we can't apply it to all namespaces using a cluster Rob so these are the three combinations which are possible

**3:06:15** · permissions are additive which means um we always specify what is allowed everything else is denied so we wh list and permissions are additive which means let's have a look at a simple example okay let's say we have a cluster role in a cluster role binding which allows us to get and delete Secrets then we Define for the same user

**3:06:38** · we Define a role and a role binding in a certain name space which only allow us to get Secrets okay the result will be that the user is able to get and delete secrets in that namespace so even if for one namespace here we Define stricter Ro bindings or stricter

**3:07:01** · rules Ro based access control rules it doesn't restrict them right because as soon as the user has to get and delete Secrets as soon as he is allowed to do this you you can't create more restrictive roles

**3:07:17** · afterwards always test your robot access control rules just a reminder never never trust your uh your your skills just like that always verify we will do this in the Hands-On sessions and with that I would say let's move on we will now create a first simple scenario we will create two name spaces red and blue and we have a user Jane and

**3:07:42** · that user Jane should be secret manager in namespace red and blue but it will have different permissions in each so user Jane can only get secrets in namespace red and user Jane can only get and list secrets in namespace blue and we will test it using of can I okay we

**3:08:05** · should be on our Master note cluster ready as always first we will create the Nam spaces red and the namespaces the namespace blue there we go now user Jane can only get secrets in

**3:08:23** · namespace red okay for this we will create a rle and a ro binding okay whenever you have to create a rooll and a ro binding cluster R cruster roll binding in it ckss you should be comfortable just using Cube CTL don't go copy a roll from some some y place from the docs and then try to to edit it right it's way faster like this this so in namespace red Jane can only

**3:08:48** · get secrets so we create a row we name it secret manager and we specify the verb only get and the

**3:09:07** · resource is Secrets I will print out the yaml now just for us to see and there we see we will create a role um it call secret manager in names space red and resources secrets and verbs get great let's create

**3:09:33** · it and now we will create a ro binding to the user Jane So Ro binding is namespaced in the same namespace red recreate at a role binding we call it as well secret manager we specify the role re the role is secret manager and then we specify the user the user is Jane again for now I will do a dry run for us to inspect

**3:10:04** · this we create a ro binding it will be it will bind the role secret manager to the user chain that's what we want exactly this okay what else do we want to do before we start uh to test and to verify our our skills user Jane can only get and list secrets in namespace blue okay so kind of the same thing for namespace

**3:10:35** · blue what we do at first we create a row but in namespace blue create Ro we call it secret manager as well verb is get and we write another verb list because we say get and list secrets in namespace blue there we go and then we as well create a r binding also called secret manager in namespace

**3:11:07** · blue and that should be it the comment by the way you should be very comfortable with typing these and fast um but they're also in the resources section of this video okay now let's test it so there is K Cube C of can I okay and as always the help page already shows many useful examples we now want to test in namespace red can I

**3:11:39** · get Secrets as user J okay off can I yes I can do it can I do it as user Tom no can I can I delete Secrets as user Jane in namespace red no

**3:12:00** · can I list Secrets as user Jane in namespace red no but I should be able to list secrets in namespace blue as user Jane and I should be able to get secrets user Jan right and um what about other things can I can I get pots as user Jan no right because we defined that one set of permissions that the user is only able to do and everything else is

**3:12:32** · denied we will now create another scenario or extend the existing scenario by creating a cluster role one cluster rle binding and one role binding and and we introduce Jim to the game what will we do well we will create one cluster role deploy deleter which allows to delete deployments then we create or we allow Jane to delete deployments in all namespaces so we create a cluster role binding then for user JY we allow to

**3:13:03** · only delete deployments in namespace Red so we will create a r binding and we will test everything using or kis before first thing let's create a cluster roll deploy deleter which allows to delete deployments okay create cluster roll DH always helpful right we see various examples but it's the same thing as if we create a role as we did before so we specify a verb which means delete

**3:13:36** · and a resource which will be deployments and we have to give the cluster rer name so we call it deploy deleter right that's what we want to call it deploy deleter correct there we go it's created let's move on user Jane

**3:14:01** · can delete deployments in all namespaces so we now for user Jane create a cluster Ro binding for that cluster rle okay create cluster row binding we call it deploy deleter it is for user Jane and we specify the cluster row

**3:14:29** · deploy deleter there we go created next user gym can delete deployments only in namespace Red so we will create a role binding in namespace red for that cluster rle okay in namespace red create R

**3:14:51** · binding we call it deploy deleter for user gym and for cluster roll deploy deleter there you go okay let's test what we did here okay let's test for user Jane in namespace default or let's let's first without any namespaces k o can I delete

**3:15:24** · deployments as Jane yes I can can I do it in all name spaces yes I can can I do it in the default name space yes can I do it in the red name space yes can I delete pods

**3:15:40** · no right it's great Jane can delete deployments in all name spaces how does it look for user gym can user gym delete deployments in the default name space no can user gym delete deployments in all Nam spaces no can user gym delete Nam spaces delete deployments in namespace red yes there

**3:16:07** · we go okay you should get familiar with these maybe look also at the Y that's generated by the comments but usually if you have to create roles R bindings cluster roles cluster Ro bindings it's very easy to do this using Cube CTL and then to test it using cctl as well and the comments that we used in this section are also in the resources of this

**3:16:36** · video we will now talk about accounts in kubernetes so accounts in kubernetes there are service accounts and quote normal users service accounts are used usually by machines like pots to access the kubernetes API and service accounts are actually managed by kubernetes API which means there is a service account resource in kubernetes that can be created edited deleted for normal users

**3:17:03** · this is not the case there is no kubernetes user resource a user is simply someone who holds a certificate and this is done so that outside Services can easily integrate with the

**3:17:18** · kubernetes identity management so the identity management of cloud providers like AWS or Google Cloud simply have to issue certificates and to store and manage certificates and keys and can then use these to communicate with the kubernetes API so what is a normal user in kubernetes there is no kubernetes user resource a user is someone with a certificate and key so if we have a user

**3:17:42** · certificate a client certificate that it has to be signed by the certificate authority of the kubernetes cluster and we will see how it's done in the next slide and in that client certificate there will be the CN the common name entry and if it's set to Jane then the username is Jane and if you then send a

**3:18:03** · request to the API containing that certificate then you will register you will be able to execute comments under the user Jane and under the permissions that the user Jane has how can we get a certificate signed from kubernetes okay so the procedure would be first we will have to have a certificate signing request we simply create it with OP SSL and we will do it soon in um in a Hands-On session so we

**3:18:31** · create a certificate signing request then we can include the certificate signing request in a kubernetes resource which is called certificate signing request we send it to kubernetes kubernetes then uses the certificate Authority which it already has access to like the kubernetes API server has access to the certificate Authority the API kubernetes uses this then to signs the certificate updates the C certificate signing request

**3:19:01** · resource which then includes the um certificate and then we as a user can download it or we as an administrator can download it and distribute it to our users why like this it's not even necessary to have the API in the middle right if you have a certificate signing request all you have to have is the certificate Authority fire and then you can create the certificate but it it can be difficult

**3:19:31** · to manage and to distribute the certificate Authority like when you want to sign a certificate you may have to download the certificate Authority from a server and then use it and delete it afterwards so this is why kubernetes introduced the certificate signing request resource and process to make this more secure and more

**3:19:52** · easy okay just a minute something about leaks and invalidation so there is no way to invalidate a certificate once the certificate is issued it is valid as long as the expiry date okay so what

**3:20:08** · happens if a certificate has been leaked like a user reports my certificate has been stolen by someone what what can you do well what you can do is you could remove all access via robas access control so that the user doesn't have any more permissions in the cluster the username cannot be used anymore until the certificate expires is expired or you have to create a new certificate Authority for your cluster and reissue all certificates okay so

**3:20:39** · it's not the best procedure and it's not an easy procedure what has to happen if there has been a leak we will now authenticate as a normal user Jane with the cluster for

**3:20:56** · this we will create a certificate and key and authenticate as user Jane we will create certificate signing request we will sign it using the kubernetes API and then we will use it using the cube config to connect to the cues API so the steps will be the following first we will create a key using op SSL same we will create a certificate signing request then we will send this one to the API the API server will sign it for

**3:21:26** · us afterwards we download the signed certificate from the API and then we use it to communicate with the kubernetes API so try to follow along it's it's important to uh to understand this um the comment that we used here are also in the resources section okay what do we have to do well

**3:21:50** · first we have to generate a key so open SSL generate you don't have to know these open SSL comments by heart and there or you can also copy the op SSL comments from the resources section but just be comfortable with these so now we created a key and um now from that key we can create um certificate signing request jane.

**3:22:15** · CSR and in that Certificate signning request we can leave everything empty but when we come to the common name to the CN then as we learned this will be the username that we use to authenticate with kubernetes so it has to be

**3:22:30** · Jane there we go we have a certificate signing request and we have a key now we would like to create a kubernetes resource which is called certificate signing request so head to the kubernetes documentation and search for

**3:22:48** · it certificate signing request scroll down it should be a bit down till we see an example at first they talk about there we go here we see one they executed in one comment but we can simply copy the yl out of it I create a new file CSR yaml paste it

**3:23:11** · in okay we change the name to Jane and then the whole request um I will delete it because in the request field where I now have written to do there we have to paste the actual certificate signing request file base 64 encoded okay so I don't I'm not creating the resource right now what I now need to have is is the jane.

**3:23:44** · CSR base 64 encoded okay and what I can actually do to get this and the comment is also in um in the resources we can do base 64 but then we we still have the the new lines right so we can do- w0 and there we go copy it

**3:24:15** · edit the resource again paste it in the request section and that's it now we will create the resource the Certificate signning request resource it worked and we can

**3:24:33** · get csrs and there we see there's our J CSR and the condition is pending so now the idea is that the administrator um can approve that certificate signing request okay it's it's not automated just like this it's still secure in that sense so what we can do is K

**3:24:54** · certificate K certificate let me have a look approve can also have the help sections there is approve and deny but we want to approve it and we want to approve certificate Jane and if we look at the certificate signning request again then we see now the condition is approved

**3:25:16** · issued and if we get the certificate signing request from Jane as yo then we see now in the status section we have actually the certificate that's our certificate that we can use so copy it it's in base 64 so we Bas 64 decod it there we go looks great we paste it into a file called jane.

**3:25:41** · CS CRT for certificate and that was that was much of the procedure already so where are we we created a key we created a certificate signing request we send it to the API the API approved it for us we

**3:26:00** · downloaded the certificate from the API what we now have to do is to actually use the certificate and the key to connect to the commum API how can we do this well if we have a look in our Cube config we can actually do K config view

**3:26:16** · this is our Cube config file right now we have one cluster we have one context which connects a cluster with a user with the admin user and we only have one user down here the admin user so what we can do is we can create another user for Jane and another context for Jane which connects the user Jan with the cluster what we can do to do this is um take config set credentials and we call the credentials

**3:26:48** · Jane and then you specify the client key and it's jane. key and you specify the client certificate which is jane.

**3:27:00** · CT okay user Jane set if we have a look at K config view then we actually see nice we now have a user Jane down here as well with a client certificate and client key these are referenced to the files okay down here you see that we

**3:27:17** · actually have client certificate data entries which are redacted right now for security reasons if we want to actually include the values into our Cube config we can simply run the same command again set credentials with embed certificates there we go let's have a look at K config view the user was overwritten and we see now it's actually included in our Cube config file if we

**3:27:44** · want to see the raw values then we can do K config view-- raw right but this is enough for us right now now we need to have a context because we want to connect the user to the existing kubernetes cluster so same thing or similar thing we can do K config set context we call it Jane and we want to connect user Jane with cluster kubernetes done if we now do K config

**3:28:14** · get contexts then we see we have a context right now the admin context and the Jane context so we do K config use context Jane and now we are user Jane k get Nam spaces I'm not allowed to get Nam spaces why because by ro base Access Control we didn't give Jane any permissions to get Nam spaces do you remember what permissions Jane had well Jane should have permissions in namespace blue to

**3:28:45** · list secrets so let's have a look if we can get Secrets there we go we can get Secrets um we can also can we delete Secrets let's try to delete that secret no we have no permissions to do this so and here in the in the response we actually see user Jane cannot delete resource we can now also do k o can

**3:29:17** · I delete delete deployments there was like the deployment deleter can I delete deployments in all Nam spaces yes because we gave um through a cluster role and cluster role binding we gave user Jane that permission and then can can user Jane delete pots in all

**3:29:38** · namespaces no okay so we are now authenticated as user Jane with the kubernetes cluster and we did that whole scenario which should make it clear I suggest if you want to get a bit more familiar with it simply do the same thing with user gym okay just the same thing that we now did with Jane go through all these steps do it again with user JY and then you should have another entry for for for Jane and for Jim and

**3:30:06** · for the kubernetes admin in your Cube config and you can switch between the contacts and test out the permissions we reach the end of the role based Access Control section it was a big section it is an important topic if you like to go a bit further then I suggest to really read through the re using Ro based Access Control documentation page um we will also face

**3:30:33** · Ro based Access Control through out other Hands-On sessions and other topics because it's just a topic which is prevalent um almost everywhere when it comes to security what did we talk about well we talked about roles and cluster roles role bindings cluster role bindings so we know the roles Define a set of permissions and where it's available and then the bindings Define where this set

**3:31:00** · of permissions is applied we talked about combining roles and bindings we used cani testing we created user certificates and we used the certificate signing request when it is API

### Cluster Hardening - Exercise caution in using ServiceAccounts

**3:31:26** · signing we will now talk about service accounts and how to use service accounts secure with their default configurations for example first we'll dive into a little overview afterwards into some scenarios with service accounts and pots

**3:31:43** · and then we will actually limit service account permissions using role-based access control so in the robot Access Control SE section we already talked about it but accounts and kubernetes there are service accounts usually for machines they are managed by the kubernetes API there's a service account resource for normal users this is not the case a normal user is simply someone who holds a certificate and this way it's easy integrated with external identity management systems we will now talk about service

**3:32:14** · accounts well service accounts are names based there is usually always a default service account in every namespace which can be used by pots and the service account resource when it's created will also um there will also be a secret which we will access soon and that secret contains a token and that token can be used to talk to the kubernetes API and this we will do in the Hands-On session

**3:32:48** · soon we will now create a service account and use it in a pot and then to see what something like this could be used for is we use that service account or a token of that service account to connect to the kubernetes API from inside that pot for this first thing we can do we can list all service accounts and there we see a default service account so service accounts are Nam spaced and by

**3:33:20** · default in every namespace there is the default service account we now go ahead and create a new service account called accessor and sure enough there we see our freshly created service account accessor now with a service account tools or programs can

**3:33:46** · communicate with the kubernetes API and do whatever permissions that service account has how would anyone use now that service account to authenticate against the API well you need a token of that service account what you what we can do for this is we can say create token and then the name of the service

**3:34:15** · account and there we go a token was generated for us okay this is not a persisted token now it's just a temporary token that we can use and if we run that comment again then we will see that another token was generated but

**3:34:34** · for the same service account so what we can do now is we simply copy that token which is a jbt token and we paste it into any jbt expector inspector I'm for example on jv. and I paste it here and on the right

**3:34:55** · we see that this is for system service accounts default accessor exactly the one that we just created now a really common thing in kubernetes is that pots have access to

**3:35:13** · their service account inside the pot right like tools running inside the pot programs processes running inside the pot will have access to such a tot let's have a look at this for this first we should create a pot and let's call it accessor let's use our favorite image and we only want the yaml output so that

**3:35:43** · we can adjust it I now should have everything usable in here and there we go simple engine exper now under spec what we can do is

**3:36:02** · we can write service account name and just for the fun of it we now simply say test some name of a service account that doesn't exist okay so go ahead write service account name and then something that doesn't exist and let's try to create the

**3:36:25** · PO and we see error um service account default test does not exist and um yeah it just didn't work the P creation didn't work so let's get ahead and change this because when whenever a service account is specified in a PO it has to exist if no service account is specified then the default service account which by default exists in every namespace will be used so now we type here the name accessor of our service

**3:36:59** · account and let's recreate the part there we go no error this time our pod is running we now exit into that

**3:37:19** · pot there we go we are inside the pot where can we find that token now well by default kubernetes mounts the token into a specific directory so what we can do now is we list all mounts and simply search for something like service account there we go here we have a directory in which we should be able to

**3:37:44** · access service account files let's change into that directory and have a look we see a certificate Authority we see a nam space which will be the default Nam space so if we simply look at the file Nam space we see it contains default and we see a token file so if we now look in the token file then we see it contains a token this is not the same token like we

**3:38:16** · generated before right but it is a token from that same service account how can we check it let's go to a jbt inspector and have a look copy the token um if there's no new line break at the end make sure you don't copy any of the user information here so I copy this one I go back to the jbt inspector paste it in here and sure enough we also see it's from the accessor service account in the default namespace

**3:38:49** · great now what can we do with that information right there are some use cases where tools inside a pot processes inside a pot want to communicate to comm's API to do something you know or to even communicate with other pots or Services inside um the cluster

**3:39:12** · so now let's communicate from inside the pot let's contact the kubernetes API and let's identify as the service account accessor for this we can have a look at the environment variables that will be available by default in every port running in kubernetes and here we see that thees API is reachable under this address

**3:39:42** · so let's curl it using htps and we see a certificate issue because it is a custom certificate let's simply ignore it by using the K parameter and there we go we

**3:39:58** · now send a request to commus API and we get an error back forbidden whatever you want to do you don't have permissions but here we see something important we identify as system anonymous so the commun API doesn't see any

**3:40:14** · authentication information any authorization from us so it simply considers us system Anonymous let's try to change this right what we can do now is we pass um using curl a new header called

**3:40:36** · authorization and we will use a be to and here now we now we could simply copy that token and paste it in here like we need to send a token now right what we can also do using bash is we simply output

**3:40:55** · um anything in the token file in the local directory and this will be used now it's just easier to do it like this and sure enough we send the same request to the cumula API we get the same failer back for bidden but we see the kubernetes API authenticates us as

**3:41:16** · the default accessor service account now if we would now give that service account using role based Access Control some permissions for example to delete pods to create Services then we would be allowed to do this now from inside that pot running incub

**3:41:45** · ities we will now disable the amount of the service account token in a pot and you should always ask yourself the question does my pot really need to talk to the kubernetes API and the answer is most often no unless your pot really needs to

**3:42:03** · communicate with the kubernetes API listen to some resources and play like the part of like a kubernetes operator if that's the case then yes but usually if you're just running an application containerized in kubernetes then it's not necessary so there actually things to disable the auto amount of the service account token and if we had to this documentation Link in

**3:42:27** · the resources section there's the page configure service accounts for pots and if we scroll down a little bit then we actually see if we create a service account we created a service account before called accessor we can actually set autom Mount service account token to false this means every pot which uses this service

**3:42:49** · account will not Mount that token and what's also possible is to do it on a pot per pot basis okay so here in the pot we see that under spec we have automount service account token and this is what we will do we will now specify for our accessor P that it should not mount the service

**3:43:10** · account okay so we said aut to mount service account token to false we recreate the

**3:43:30** · pot and have a look if the service account then really didn't get mounted okay the new pot let's exec into the PO

**3:43:48** · again Mount grab service account doesn't look like it okay various other ones but not the service account one and we can also see this if we edit the PO accessor and if we scroll

**3:44:05** · down to the volume section then we actually see that there's like no volume specified for the service account okay we change this again we say Auto Mount service account token true we replace

**3:44:33** · again and we edit the Pod again and now we actually see that if we scroll down to the volume section that there is the automatically generated volume section for the token and in the container we should have a volume Mount exactly for this one okay so using this either on

**3:44:56** · service account level or on pot tobot basis you can actually disable the autom mounting of the service account we will now limit your service account permissions using robas access control to edit Resources by default all

**3:45:14** · pods use the default service account that service account by default doesn't have any permissions so it's fine but if all your pots use the default service account and someone simply gives that one service account more permissions it means that all your pods have this permission directly so it makes sense from application to application to create the own service accounts and make

**3:45:37** · the application PS use that service account we will now the accessor service account we will now give it some more permissions using rbas access control there's the existing cluster role edit it's a default role in kubernetes and we will create a cluster role binding to that cluster role for our service account and see what happens well there's our pot it runs with the accessor service account we now can test the permissions of the accessor service account can I

**3:46:09** · delete Secrets s and then to test the service account you write system holdon service account then the name space because service accounts are Nam spaced and

**3:46:27** · accessor I can't do it right now so now we want to create a cluster R binding so we do create cluster Ro binding I call it accessor we bind it to the cluster role edit which is a default one and we bind it to service account and now here in service account we only have to specify default colon accessor for the namespace and let's create it okay and we repeat our or can I comment and yes

**3:47:01** · okay this means that our service account accessor can now cluster wide edit resources and this is the case also from our po so if you like just as to to go a little bit further you could EXA back into that pot and try to contact the kubernetes API and actually um delete some secrets for example okay so a pot has always the

**3:47:30** · exact permissions as the service account that it's that it's using unless um you you don't Mount the service account by default which which is a good idea and if you multi service account then definitely restrict its permissions using role based Access Control to wrap this session up I shortly want to mention the principle of least privilege again always have that in the back of your mind when you create role-based access control

**3:48:02** · rules if you like to dive a bit more further then I suggest two pages of the kubernetes documentation actually man in service accounts and configure service accounts for pots links are in the resources section what did we talk about here well

**3:48:18** · we talked about service accounts we should know what service accounts are and that service accounts always come with a token in form of a secret which is automatically managed we looked into service accounts and pots how the service account tokens are actually mounted into pots how pots can use the service account token how we can prevent the mounting into pots if we we don't need it and how we can configure pots to run under different service accounts and

**3:48:45** · even how we can create our own service account and finally how we can use Ro based access control um with service

### Cluster Hardening - Restrict API Access

**3:49:06** · accounts restrict API access we will talk about the kues API and how to restrict access to it we talk about the reest workflow and especially about authentication authorization and admission afterwards we talk about different ways of how to connect to the kubernetes API and then about different ways how to restrict access to the kubernetes API the kubernetes API is the

**3:49:33** · central point of kubernetes and makes it reusable and extensible and is actually one one of the main reasons why kubernetes gained such popularity when we send a request to the kubernetes API which we do here right now we send a request to create a new po the request goes through three levels of

**3:49:55** · um where it has to pass in order for the request to be accepted so let's say the request to create a new pot it can be sent by human user it can be sent by a machine by a service account it will reach the API server and then the first step will be authentication so the kues API server may ask the question who are you who who are you actually do I now you who wants to execute this request

**3:50:21** · after that's done we will go into the authorization where the communties API server might ask a question hey are you even allowed to create pots okay so we have the action create and the resource pots and at this point of time we will ask is that user that we authenticated in the first step is that user even allowed to perform this action on this

**3:50:45** · resource if this is the case then we go into the last level of checks which is the admission controllers and there depending on what has been configured the question might be ask has the limit of pots been reached right there might have been a limit configured only that

**3:51:02** · certain amount of pots can be created in that namespace this is just one example of admission controllers there are various admission controllers you can write your own admission controllers you can install third party admission controllers there's for example the OPA the open policy agent which works as an admission controller where you can Define your customize and write your own policies so at this point in time in the admission controller we know that user is allowed to perform an action on a

**3:51:33** · resource but then there will be like additional checks on limits or customiz um rules applied and only if these three steps these three levels will be passed then the request will be executed by the kubernetes API so requests in general should always

**3:51:56** · or are always tied to either a normal user a service account or can also be treated as an anomymous request and every request must authenticate unless it will be done through the an ominous user and we will talk about the an ominous access or we will actually talk about it and we'll see it also in action in the Hands-On session restrictions so let's talk about

**3:52:19** · restrictions we will talk about restrictions in this section and one of the first one will be we shouldn't allow a ninous access we should probably close the insecure Port if it's enabled we shouldn't expose the API server to the outside if not necessary and we should restrict access from no to the API so noes can actually communicate with the API as well we we talk about this and

**3:52:45** · there's the note restriction admission controller which handles this outside of this section we should probably also think about preventing unauthorized access using Ro best Access Control we have a complete different section about this in this course we should maybe prevent pots from accessing the API we also talked about this in a different section where we can prevent the mounting of service account tokens in inside parts and we should probably put our API

**3:53:14** · server also behind the firewall only allow certain IP address ranges if we have to expose it externally but this is also outside of kubernetes and depends on where you set up your cluster and your

**3:53:30** · infrastructure an ominous access Theus API server can be configured with the anous off true or false argument and by this enable anous access or disable anous access so since 1.6 Comm is 1.6 anous access is

**3:53:47** · enabled by default if authorization mode other than always allow has been configured so but then for example if we use attribute based access control or role based access control then this still requires explicit authorization for the anous user okay so it is not completely open and insecure we will now enable and disable the anous access and test it so follow

**3:54:14** · me along head to your master note with your fresh and running ready kubernetes cluster what we will do now is we will have a look at the manifests directory where we configure the kubernetes uh API

**3:54:35** · server and we have a look if there is already a parameter configured which will specify the animous access and it is not the case so what we see here by default we

**3:54:51** · see that we have the authorization mode robas Access Control enabled this is great so let's have a look the parameter anous off is not defined yet so let's simply contact equ this API what we can do we are on the same server so we can simply um contact Local Host on the port

**3:55:13** · 6443 and we accept the self-signed certificate and we see hey this is a request was accepted it was just said that it's forbidden for the system an ominous user okay so this means our API server right now accepts request from anous user so we will now

**3:55:37** · disable this so head back into your Cube API server manifest and at the parameter an ominous off and set it to

**3:55:58** · false let's give it a bit of time until the API server will be rebooted with our new configuration we see it's container creating

**3:56:16** · still it's running not ready yet anyway let's repeat our curl command and there we see failer unauthorized okay and what we can do again is we head back into the Manifest and we set this to true so we allow it back we enable it back which means the API server will be rebooted

**3:56:54** · again there we go 6 seconds ago I reexecute the curl command and there we go an ominous access is enabled again so we saw how to enable and disable anous access and if you have to disable it then you know where to

**3:57:14** · look we will now talk about insecure access to communties API and first we're going to have a short overview we have our communties cluster with have the API server and we can send request to the API server for example using cctl so cctl simply also access the kubernetes API these should usually be protected um

**3:57:37** · via https and this this works because we have a client certificate which we send to the server and the server has also a server certificate which the client can check and we have our certificate Authority in the commes cluster which manages all these certificates this is how it should be done um when accessing the kubernetes API to be secure via https it is possible to configure the insecure port and insecure access okay by the insecure Port argument pented his API server this

**3:58:08** · will allow to send requests to the API over HTTP but in addition to this like this is already bad enough right people can could read the traffic when they intercept but in addition to this request sent to the insecure Port will also bypass authentication and authorization modules the admission controllers will still be enforced but skipping authentication authorization is definitely dangerous and should only be used for debugging purposes

**3:58:39** · we will now in this Hands-On session enable insecure access and port and use it okay follow me along head to your master note before we can test before we test anything we can actually send a request to Local Host Port 6443 we accept self

**3:59:00** · signed certificates and there we go we are forbidden but we authenticate as system anous so in our API server anous access is configured but we have to access it over HTTP what we can do is we head to our Cube API server manifest and

**3:59:18** · we actually see that there's already insecure Port configured but the port is set to zero which means it is disabled we will now set this to 8080 save we will have to wait for the kubernetes API server to boot up

**3:59:44** · again to be restarted and there we go it's restarted we can repeat the curl command from before everything still works on the https Channel but now we can also send an HTTP request to the insecure Port 0 and we actually see we have access to the whole API endpoints we skipped authentication and

**4:00:08** · authorization very dangerous um should only be enabled for debugging and if you know what you're doing and if you have to disable it simply find the argument and set the port to zero we will now have a look at the admin Cube config file on our Master note and the certificate information stored in it and we will use it to perform a manual API request this will

**4:00:35** · just make you more comfortable with how Cube City L and Cube config actually work to perform API requests so follow along head to your master note and if we type K config view then we see our config file the credentials are not included but we can type K config D- raw and this is simply

**4:00:57** · shows the same content as of the by default of the directory Cube config um do Cube config file Okay so what we want now is we want to create we want to extract the information okay so the first information we want to extract is from clusters the certificate Authority data okay here we see the base 64 encoded data so we want to write it base 64 decoded we want to um write it in plain text into a file CA so what I do is I

**4:01:30** · simply copy it I Echo it I type base 64 decode right there it is and I pipe the output in a file called CA easy now we will do the same for the

**4:01:47** · client certificate data so this will be the file CRT so I convert it I decode it and write it in the file CIT for the certificate and finally we also do it for the for the client key data so the Cent and key data will contain the key so I write it base 64 decoded into a

**4:02:16** · file called P okay we should have three files one with the certificate Authority one with the certificate and one with the key now let's have a look again at K config view um and here we have the server address okay so we can now the server

**4:02:37** · address I mean this is the uh local IP right this is the IP address of our Master server but we now have to connect using the IP address and not Local Host so that the server certificate from the API server is actually valid so if we send a request here without anything then we see well we got a connection but there's a certificate which we don't trust yet okay so what we can do is we actually

**4:03:02** · say okay we don't trust the certificate but we will have we will trust this certificate Authority and then we see yes using this certificate Authority the server certificate is accepted and trusted okay we are now authorized as system

**4:03:21** · anous now what we can also do is we can pass the certificate so the file is CT so we now want to pass our client certificate we want to authenticate as as the administrator user and

**4:03:39** · we see that we also need the key file belonging to it and there we go okay so using this comment using the certificate Authority using the certificate and key we out of the cube config we are now able to Simply perform API requests towards the kubernetes

**4:04:02** · API we will now make our API server reachable from the outside and we'll add actually send a request from our local terminal to the API server we will also copy the cube config from our Master node and then may make some small adjustments and then use this one locally okay head to your master note if you look at services in the default namespace and there the kubernetes service it's a cluster IP service we will simply edit it to be a not Port

**4:04:35** · service and as simple as this our kuties API should already be available for external access if we look at Services again and there we see 443 there's a not port for me it is 3046 it might be a different not port for you so have a look which one has been assigned to you and here open Michelle on my local machine so this when we see cks here is now my local machine and what we can do is we contact

**4:05:07** · the API server but we need the external IP address of one of our machines right so I'm here in my Google Cloud I see ckss worker I copy the external IP and at the very beginning in Google Cloud we created some firewall rules and when we set up the cluster together so that um

**4:05:27** · requests are allowed to come inside our instances on the notep so we opened all the not ports for traffic and there we go go it works okay I connect to the not Port of the external IP address of the worker node and I can actually contact the cuberes cluster it's just that the certificate is not accepted right now so I can simply accept the certificate and um I

**4:05:54** · am authorized as a ninous user next we would like to copy the cube config file from our Master note so we can do Cube config view D- raw and I'll simply mark everything and copy and paste it into a new file I call the file

**4:06:15** · conf this will be our new Cube config file we have file conf what we can do you should now have locally Cube CTL installed okay I have Cube CTL installed I also have the ls K so what I can do is K D- Cube config so with D- Cube config

**4:06:33** · you can actually specify just for that commment that you want to run you can specify that a different config file should be used so this is for me conf in the local directory and then I try to get name spaces and I see not much is happening

**4:06:50** · okay so what we will do is we will actually copy that URL that we used because under this URL we can now access the API server on our local machine okay so we copy it we head into the local Cube config and there we see that there's a different IP address specified and a different port because this Cube config Works locally on the master node we will change the

**4:07:24** · server seems I didn't copy it we copy it again the correct address there we go repeat the K get Nam space SP again okay what happened the certificate is not valid because the certificate is only valid for these IP addresses but we try to reach that IP address and the certificate which the server the kubernetes API server returns to us is not valid for this IP address we can

**4:07:57** · actually have a look on the master node and we can change into the um pki directories so /etc kubernetes pki private key infrastructure and in there we see various certificates for example we see the API server certificate which is this one

**4:08:24** · okay so what we can do um I post the comment as well in the resources section we can run open SSL to Simply inspect the the certificate so it is apis server

**4:08:46** · doert and text output okay we simply inspect that file and there we see that the names are actually so two IP addresses are allowed for this certificate but there's also it's also possible to call it ckss master or kubernetes so we can use these domain names when we want to when we would like to to verify the certificate

**4:09:14** · what can we do well I head back to my local terminal and what I actually do is I will create a hosts entry in my hosts file for this IP address again this IP address might be a different one for you this is the external IP address of the worker node or of your master

**4:09:36** · node we will create create a host entry for this IP and we call it kubernetes this means locally we can access the name kubernetes and it it will lead us to this IP address save it in our local Cube config file where

**4:09:55** · we still reference the IP address we now change the IP address to kubernetes and we run our comment again to get the name spaces and there we see we are now connected as the kubernetes administrator and we can connect to our kubernetes cluster from the outside so this is one possibility of make making the kubernetes API server reachable like via kubernetes VIA kubernetes not Port service and you would now to check if

**4:10:26** · the API server is actually exposed via a not port and you would also be able to change it back to a cluster IP service we will now talk about the node restriction admission controller so it's an admission controller so we work in the admission control section of a

**4:10:48** · request being accepted or denied and what does note restriction do note restriction is an admission controller it can be enabled by enable admission plugins note restriction and we will do this soon in the hands on session it limits the note labels a CET can modify and also it limits that coulet which runs on a worker node a CET kind of transforms an instance into a worker node and it it can communicate with the kubernetes API and the node restriction

**4:11:19** · limits that capability what a cuet can do okay it can then only modify certain labels and only modify labels it's its own node labels so not labels on other nodes and it can also only modify labels of PODS running on on itself on the on on the same note not on other notes why

**4:11:44** · has this been done and why is it necessary well to ensure a secure workload isolation via labels imagine you have certain nodes which run more secure they might have um some gvisor like container sand boxes installed and you want certain pots which need more security to only run on these nodes and you do it via note uh select and labels so now an intrusion

**4:12:11** · could come into the cluster and say hey I am a secure node right I'm a coulet I'm a secure coulet and it um and it would be possible to Simply tell the API yes I have that label run secure workload and then suddenly secure workload would be run on that note okay so this is to ensure secure workl isolation via labels no one can pretend to be a secure n and and schedule secure

**4:12:38** · parts we will now verify that the note restriction works and we do this on the worker note by using the cube BLS Cube config file to set some labels and to communicate with the kubernetes API first we will actually check the node restriction status uh on the master node so we'll be on the master node and we actually have a look in the Manifest of the kubernetes API server so SL say kubernetes manifest Cube API server yo

**4:13:07** · and in there we should already see enable admission plugins note restriction is enabled by default when we configure a cube ADM cluster all right let's head to our worker note to see in action what the node restriction admission controller actually enforces I'm on the worker Noe if on the worker Noe I run K config View and I see I have a I have no Cube CTL possibility I have

**4:13:38** · no Cube config to communicate with the API server but if we have a look there's actually in directory /c kubernetes cet.com there's a file which is a cube config for the cuet to communicate with the kubernetes API server okay so we can

**4:13:58** · now simply use this file by executing export and setting the variable Cube config equal the path and by setting the cube config variable now our local Cube CTL

**4:14:15** · will use this configuration so we can try something like K get namespaces we now communicate with the API we got a response back but we have no permissions we to to list the name spaces and we see we authenticate as user system node c as worker okay so we can now communicate with the kubernetes API as the worker node we are not allowed to get namespaces but we are allowed to get notes for example now let's try to set a label on the

**4:14:47** · master node okay so we type K label node we want to label a node cks Master we want to create a new label we call it cks test equal yes forbidden we are not allowed to modify the node ckss Master great node restriction restricts this this let's have a look if we can modify ourself so we modify we we add a label

**4:15:13** · to CS worker and it worked okay great now there are also restricted labels which we are not able to set even for ourselves okay and these start with note restriction. kubernetes doio I try now to set a label on

**4:15:40** · myself which starts with not restriction. and then following something and I see that I'm not allowed to modify these labels okay so the note restriction admission controller forbids a note to set labels starting with this

**4:15:58** · by themselves and this gives administrators the possibility to set really secure labels starting with this prefix and which gives the administrator the assurance that nodes can't remove or adjust these labels to maybe force some secure pods to run on

**4:16:24** · themselves to wrap the session up there's the kubernetes documentation page controlling access to the commus API it explains everything again and also has some examples it's very nice if you like to to to dive a bit more into it and we talked about various things so

**4:16:42** · you should be familiar that it's possible to connect from the outside to the API from pots to the API and also from nodes to the API where the CET has a cube config and this can be restricted using note restriction admission controller you should know how to enable and disable anonomous access on the API server same for insecure access and insecure Port very dangerous and you should generally be aware aware that there are certificates with which users authenticate towards the kubernetes

### Cluster Hardening - Upgrade Kubernetes

**4:17:25** · API update kubernetes frequently we all knew the time would come here it is let's jump right into it and update our kubernetes cluster we will talk about kubernetes release Cycles about possible version differences of kubernetes components and then in the Hands-On sessions we will actually upgrade our kubernetes cluster why why should we do this frequently well to get latest support security fixes Buck fixes and to stay up

**4:17:56** · toate for dependencies well if you run an outdated kubernetes version and there will be a security issue released then you can't fast update to the latest version which has the security Buck fix right it will take you too long so it has to be a continuous process of updating the cluster and trying to always stay up to date if we look at a kubernetes version like 192 then these are the major minor and

**4:18:25** · Patch version so it's like versioned by the sver semantic versioning and a minor version will be released every 3 months and there's no long-term support release okay that's why here on the left for higher if you if you administer a kubernetes cluster and it is large enough it has a lot of applications then just staying up to date can be a full-time position or even

**4:18:53** · more you have to always check your dependencies the resources might be expired you have to update your Helm chart the dependency of the helm charts if they are still compatible yes it can be quite some work well maintenance release branches for the most recent three minor releases so for example 119 118 117 these exist okay

**4:19:19** · so fixes including security fixes may be backported to those three release branches but not further okay so you always have the latest three versions which are supported and you should always look that you are in these

**4:19:36** · version renes well how do we do this how do we upgrade a cluster well in general we first update the master components so API server controller manager scheduler and then the worker components like Q plate Q proxy that's the general procedure and rule of thumb we could say

**4:19:58** · components should always have the same minor version as the API server so if the API server is on 1.9 all the other components should also be on 1.9 but there can be one version below that's the rule of thumb okay we we're going to go into detail but if you follow this rule then it should be fine okay let's have a look at possible version differences we have kubernetes 117 here 118 119 and here we have our

**4:20:27** · Master components and this is a we only show possible combinations now so we could for example update the API server to 1.8 this is possible and then we can update the schuer controller manager step by step afterwards okay so the master components they should always run on the same minor version okay but it is possible to have them one minor version below to allow for in place upgrades

**4:20:55** · else it would be difficult okay let's add the worker components cu cu proxy that should always be the same version and then we also add Cube CTL as our client for our administrator needs okay so this is a a valid combination we updated our Master components but our um worker components are still a bit

**4:21:20** · behind we can update Cube CTL Cube CTL can always be one version away from the API server okay so this is all possible so let's say we update Cube CTL to 1.19 already and now we probably should update the work ER components to 1.8 but we could also do this we could also update the control plane components to 1.19 and then update the cuet to 1.8 and then update the cuet to 1.9 okay so the

**4:21:51** · cuet um can be two minor versions under the API server it can be okay but just because it's possible doesn't mean that you maybe have to do it like this um but yeah now we are on 1.9 and all components are updated right so if we talk about the rule of thumb again if you follow this then components should be the same minor version as the API server or one below okay so if you

**4:22:20** · follow this then we should always be fine how to upgrade a Noe how to upgrade a single node Master node worker node well first you do a c cctl drain to safely evict all pots from the node and to Mark the node as scheduling disabled okay so this means scheduling disabled means no new pots will be scheduled on

**4:22:43** · that note and this could also be achieved using Cube C Cordon right but Cube CTL drain does this already so we run Cube CTL drain then we do the actual upgrade of the components and then we do an CBE c l un Cordon which will Mark the node unmark the node as scheduling disabled and new pots can get scheduled scheduled on it well just short Excursion doesn't

**4:23:08** · maybe have to do much with the ckss this is less security but more like reliability uh you should always look that your application can survive an upgrade right so your application should um be able to be removed your pot should

**4:23:23** · be able to be removed and recreated during the deployment but also if there's a node maintenance for example you can do this by adjusting the grace period which means how long does your pot stay in a terminating state to still work on existing requests or messages you can also hook in the pot life cycle events to control this in even more detail and there's also the pot disruption budget which specifies how many pots can be terminated um can be away from your deployment at a certain

**4:23:56** · time we will now upgrade a kubernetes cluster and first thing we have to do for this is we need to create an outdated cluster that we can then upgrade so we need to install an earlier version of kubernetes in our cluster we now have three possibilities how we can do this the easiest is we simply use the killer Coda

**4:24:22** · playground and in that playground we have two VMS and we can simply upgrade them with Cube ADM even if the playground is already on the latest minor version like 1.25 we can still upgrade the patch version version like here from 2 2 three because the upgrade

**4:24:40** · process should be the same if it's a minor version or if it's a patch version second option is we create completely new VMS but when we install when we run the install scripts we use the previous scripts instead of the latest scripts this is actually a really good option and even if you test it at first in the playground I still suggest after this you create new VMS with the previous script and then upgrade the minor

**4:25:09** · version third option is we can also simply install the previous scripts over our existing BMS in theory it should simply remove all old kubernetes components and install the new ones in the previous version but there can be errors and some users actually reported errors so I would suggest you do one or two I will

**4:25:33** · actually now go ahead and do the third option and and install the preview scripts over the existing BMS what will happen is in the git repository we usually install from the latest folder but we also have scripts in the previous folder that we will now run um on the notes and you can just go ahead and do this the comments for this are in the resources section so just go ahead to your control plane Master node

**4:26:03** · at first copy and paste and run the comment and then we let it run it will take a few minutes and we do the same on the \[Music\]

**4:26:19** · note there we go so these scripts will at first remove all previous kubernetes components and then reinstall the previous version and I'll not pause the video till the master node script has finished and you can do the same there we go my control plan script

**4:26:44** · is finished and this means that my not script also finished yes this looks good and now we did set up a completely new cluster so we have to join the node again into the cluster and we do this by copying the comment on the very bottom and executing it on the Note

**4:27:15** · this looks good now let's check the control plane for notes and there we go so this is for me the outdated cluster with which I'll now move on and work for the upgrade

**4:27:34** · task we will now go ahead and upgrade the control plan to one minor version up all the comments that I will use will be in the resources section but it's probably best for you to get used to the kubernetes documentation you can simply search for cube ADM upgrade and there you actually see a page with all the comments um if you try to follow this because you can use that page in the exam right so that will be pretty good

**4:28:04** · well let's get started so I have an outdated cluster for me right now the outdated version is 1.21 and we will update to 1.22 again the versions for you might be different just depending on our install scripts in the repository so first thing what should we do well we should probably drain the note so we simply drain the note we ignore demon

**4:28:46** · sets there we go and we can see that the control play note is scheduling disabled now what we would like to do is first we would like to install Cube ADM so let's upate updated first to get the

**4:29:06** · latest versions and then we will like to find the actual version from Cube ADM that we would like to install so what we can do is um appc show Cube ADM everything with

**4:29:22** · 1.22 and there we see the latest one is actually that one so we can copy this and then install that version but before we install um we might have to actually Mark the other packages

**4:29:39** · so that these won't get updated right because we want to update these later so what we can do is app Mark um hold uh Cube CTL and the C there we go and um I mean we can make sure also that the package that we want to install Cube ADM is not marked at the

**4:30:09** · moment it's not hold okay great so now we can go ahead and actually install to ADM in this specific

**4:30:28** · version and we can check the cube ADM version that seemed to have worked which means in the next step we can use Cube ADM upgrade plan to check our possible upgrades and there we see you can now apply the upgrade by executing the following comment and that's exactly what we will

**4:31:01** · do we will see currently installed version you see twitch will be updated this is exactly what we would like to

**4:31:21** · do let go ahead and pause the video till the comment has finished and mine has finished success your cluster was upgraded to 1. 122.5

**4:31:36** · enjoy and down here is a note now that your control plan is upgraded please proceed with upgrading your C blets and this is what we will do now so we will now upgrade also the celet and Cube CTL because if we check the cubelet

**4:31:57** · version and the cube CTL \[Music\] version and we can see that these are still on 1.21 so what do we do well we go ahead and unhold these at

**4:32:23** · first and then we install cuet in the same version as we installed Cube ADM

**4:32:56** · and there we go now we have to restart the CET

**4:33:13** · looking good so far let's have a look at Cube ADM upgrade plan again and there we see nothing to update right now seems to have been updated properly and finally if we have a look at the notes then we can also see that our control plan is up upgraded but it's still scheduling disabled so we should uncon it so that Parts can be scheduled on it

**4:33:43** · again here we go so much to upgrading our control plane let's move on to our node in the next video and now we'll go ahead and update the Note to match with the control plan version so that's the current situation we have a control plan Noe on the latest version and we still have an outdated

**4:34:13** · note so for this first we should probably go ahead and drain the node we ignore demon

**4:34:34** · sets and once done we will head to our note and on the note we will now install Cube ADM in the version so we first do an upgade update then we search again for the proper version stream from Cube

**4:35:02** · ADM which is this one and now same as on the control plane we first um hold the cube Le and Cube

**4:35:21** · CTR and we unhold Cube ADM in case it was hold and now we can go ahead and install Cube ADM in that specific version

**4:35:40** · and now here's a slight difference if we use Cube ADM for upgrading on a node we can simply run Cube ADM upgrade node and there we go now we want to go ahead and update the cubet package also as written down here so for this we should probably Mark Cube ADM as hold

**4:36:14** · again we unhold Cube and Cube CDR and now we can go ahead and install the cuet in that specific version that we would like say same for cube \[Music\]

**4:36:49** · C and we can hold B CET and CBE C again now let's go ahead and restart the CET

**4:37:10** · seems like something has worked let's head back to our control plane let's have a look what the notes say and there we go it looks pretty good just that our note is still marked schedule and disabled so we uncon it check again and this looks good hey

**4:37:35** · we upgraded a kubernetes cluster in my case from version 1.21 to 1 12022 and yeah in your case it might have been different versions but that should be

**4:37:52** · it and we actually did it we upgraded our kubernetes cluster if you have to do this in the exam then there's a great page in the documentation called upgrading Cube ADM clusters link is in the resources section of this video it contains really everything that you have to know and that you have to do during the exam when it comes to upgrading clusters if You' like to learn more about kubernetes versioning um which is kind of what we talked in the introduction of this section then

**4:38:23** · there's another great documentation page kubernetes version and version School support policy link as well in your resources and to wrap this up we talked about why we should upgrade frequency ly we talked about the kubernetes release cycles and version differences like possible version differences between the various different components of kubernetes and then we actually learned

**4:38:48** · how to upgrade a kubernetes cluster and that is definitely something that you should be able to do when it comes to the cks exam we will talk about secrets in kubernetes and first I'll give you a little overview about how secrets are managed and deployed into kubernetes afterwards we will create a simple secure secret scenario and afterwards we will try to hack these secrets out of that scenario so very fun session

### Microservice Vulnerabilities - Manage Kubernetes Secrets

**4:39:21** · today well what are secrets generally Secrets can be a lot of things they can be passwords API Keys credentials or more generally just information that's needed by an application let's have a look at the times before kubernetes let's say we have a simple server an instance and we have our application code and we would like to convert that application code into an application which is actually running on our server how would we do this well a

**4:39:53** · very common way is to submit the code into a repository and then to using some cicd pipelines deploy that application on the server what if we now have a secret and our application needs that secret like a database connection string right what could we do well we could actually include that secret in the application code submit it in the repository and deploy together with the application and everything is fine right it works but the issue is if that secret

**4:40:25** · is plain text then everyone has access to the secret who has access to the programming code right and you usually don't want every programmer to have access to the secrets you want to have it decoupled um it is still possible to encrypt these secrets and then decrypt them again on the application and that is still done today in in some applications right so from security perspective it might be okay but you still have them tightly coupled so every time you want to change a secret you have to actually go through

**4:40:54** · the whole deployment process um of your application so what you might be looking to is a decoupled way so we have our deployment workflow our application and we have a different workflow where we actually send the secret on the server and it might be stored on the server and then whenever the application needs it it will be passed to the application so we have a nice decoupled way and this is in general also the way

**4:41:22** · that kubernetes allows us to do things and to configure application in general let's say let's say we have a simple example we have our worker node our CET is running here we have an API server and we have our application code and we would like to have our application running in a pot inside our worker note how do we do this well we submit our code to our favorite repository and our cicd pipeline will be run and will contact the API server

**4:41:52** · which will then create or update our application and send the information to the cuet and the cuet will then run our application well how is this when we have a secret now well we will send the secret to the API server and it will be stored on the API server right it will be stored in atcd but it will be managed by the API server

**4:42:14** · and then when our application needs it the API server will actually communicate with the cuet and the cuet will then pass it to the application when needed okay so this is how kubernetes um offers us a nice decoupled way of managing Secrets outside of the deployment workflow of our applications

**4:42:38** · we will now create a simple secret scenario this scenario in our kubernetes cluster will contain a single pot called pot we will then create a secret called secret one which we will Mount by our file system into that pot then we create another secret called secret 2 which you make available via environment variable inside that pot

**4:43:02** · feel free to pause the video create that simple scenario you can create these secrets with any content doesn't really matter you should be in general very comfortable with creating secrets in different ways and making these available in pots in various ways and this is exactly what we will do now I head to my master note and I'll will first create the secrets so secret one

**4:43:27** · we run K create secret and then we can have a look in the help page we will create a generic Secret it's the name secret one and for the data from literal we say user is admin great and for the

**4:43:45** · second secret we set the password is 1 2 3 4 5 6 78 and we call it secret 2 okay we have our two Secrets created now what we would like to do is to mount the first secret via file system into the part and the second secret via environment variable inside the pot for this I will now

**4:44:08** · create a simple pot krun pot pot will be called pot we choose the image our beloved engine X but we only want to generate the yo exactly I pipe it into a file po.

**4:44:27** · yo and now we would like to extend this file feel free just to to type a just down if you you can do this I will head to my favorite page and to all our favorite page during the kubernetes exams the kubernetes documentation I search for secrets and on that secret page I will

**4:44:49** · see on the right side using Secrets s files from a pot this sounds very familiar with what we are trying to do here there we go we will create a volume section and then in every container where we want to have this volume we will actually create a volume Mount okay so I

**4:45:11** · copy copy all of this and I will adjust it the secret name will be the secret one and we will call the volume also secret 1 and we will mount it to /c secret 1 why not read only yes we can

**4:45:30** · leave it as read only now for the second Secret we would actually like to use the secret as environment variable and yes there are also various section about this so I can simply copy

**4:45:47** · one and the second secret contain the password so let's simply call it password the secret will be the secret to and the key that I gave it will be pass okay this looks fine to me let's have a look what kubernetes says about this something not right let's have a

**4:46:26** · look couldn't find key pass in secret one what did I do well yes exactly this secret here should be secret 2 we will Mount secret 2 as environment variable and we will use secret one as volume okay there we go let's try this

**4:46:58** · again container creating that looks better okay let's Let's test what we just did let's exec n inside the pot and grab for password and there we see our password we gave that environment variable the name password and it actually contains the value of our secret how about the other one we

**4:47:22** · mounted or we tried to mount at least our secret one how about this yes we actually see there's a SL edit secret one mounted let's have a look what what's happening in that directory there is actually a

**4:47:43** · file called user which is the key of our secret so we can cut it and there we see admin okay great we created this simple scenario it should be running for you best is if your secrets also are called secret one and secret 2 because for the next Hands-On session this will make things easier when we try to hack these

**4:48:12** · secrets in this Hands-On session we will investigate kubernetes secrets and how they are stored or accessible via our container runtime if we have our Master node control plane then we have at CD we have an API server and these secrets that we created before secret 1 and secret 2 are

**4:48:34** · actually stored in at CD Now when would we need these secrets well if there's for example a worker note and on that worker note there's the pot like the pot that we created before which consumes secret 1 and secret 2

**4:48:52** · then what happens well these secrets will actually wander through the API server to the cubelet on the worker node and to The Container runtime in this case container d and we will now have a look how we can access these secrets if we have access to the container runtime on our worker

**4:49:15** · node let's go ahead on the master node control plane if I have a look for pots then we see there's the pot that we created before and if we have a look where that pot is running well no wonder it's running on our only worker node so we move to that note and on that note we can now actually check for running containers so we use cctl BS and there we actually see our

**4:49:50** · pot is running now we also see the container ID so what we can actually do is cre CTL inspect container ID and wow there we got a lot of information in Json format about that

**4:50:08** · container so let's have a look let's scroll through a little bit if we see something interesting for example we should see an environment section and these are the environment variables passed into the container and there we see our

**4:50:29** · password so that's the environment variable and there we see all the information so if you have access root access usually which has access to the container run time then you can also see all the secrets which are passed through kubernetes to the pot into the Container

**4:50:47** · so that's the environment variable secret what about the mount because we mounted the other secret as volume so if you have actually look we see that there are mounts and there we actually see yes yes under the path Etc secret one

**4:51:08** · there's actually something mounted but we don't see the value here right so what we want to do now is we want to find the value of that container so we need to access the file system and what we can do for this is actually to find the process to find the P ID of the process and then find the file system so how can we do this well we can execute the inspect comment again and what I do is I pipe it into Vim

**4:51:39** · right and then in Vim I can actually search for the P ID and here we go okay so I find the PID I could have also just grabed it probably but here we get a little bit more context so that's my P will be a different one for you I copy it I look

**4:51:58** · for all processes for that P and there we go there we see the engine x master process and that makes sense because the example Port which consumes the secrets which we created is an engine xort okay so what can we do well we can actually use the magic proc directory for our

**4:52:20** · ID and check the root file system and there we go we have access to the root file system now if we remember where remounted it it should have been in at CD secret 1 there we go and there's a file user and if we output it then we see our admin value so here we

**4:52:47** · have the admin value and maybe I just run the inspect again repb for the password and there we see the password here as well okay so this should just show you um how

**4:53:06** · accessible Secrets actually are to The Container runtime this doesn't really mean that this is like a big security issue because usually if you have root access to a worker not you can usually access all the information of all the processes and by that of all containers and pots running on that n okay so it's not a security issue per se because

**4:53:31** · only um certain people people should have root access to a worker note anyway but if there is access leak or um credential leak and someone get access then by default that person can also access through the container runtime all the kubernetes

**4:53:54** · secrets we will now continue our secret hacking and we will investigate secrets and at CD our secrets are stored in at CD and we will now imagine that we gained access to at CD like we gained the credentials and we are able to connect directly to at CD and we will now try to access a secret value the value of secret 2 in at CD okay uh at CD

**4:54:18** · is running on the master node so we'll run onto the master node and there's actually the etcd control command and we execute it like this to use the version three um all the com ments that we use right now there are also in the resources section of this video and also the kubernetes documentation has some entry about this like for example when it comes to at CD backup and restore if we execute this then we see okay we can execute and run various

**4:54:50** · commments we can pass some parameters well what we can try to do is to run end point heals okay we just want to check the health status of ETD and there we actually see okay failed connection is drained unhealthy cluster we are not able to connect to at CD actually well let's have a look how we

**4:55:14** · can get the credentials to use right and if we have a look the API server is able to connect to at CD okay so we will now simply have a look at the API server how the API server does it and then we use the same credentials as the API server for this we will check our manifest directory of the cube API server and we grab it for anything that says at CD and there we go we have a CA we have a CT we have a key and we have servers great let's try to repeat our

**4:55:49** · endpoint Health comment but now we will also add the certificate certificate will be this one we will add the key key will be this one and we will add caer which is this

**4:56:14** · one there we go it worked our SD server is healthy successful this check worked we didn't specify any at CD servers like the API server does here it's not necessary because we could specify for at CD control we could specify the end points but you see here that the default value is already Local Host 2379 okay so we don't have to specify it

**4:56:40** · right now because we are on the same server and we can use the default value so what we can do instead of running endpoint HS we can actually run get and then we get a specific value out of the registry there's registry

**4:56:56** · secrets and then it depends on the kubernetes name space default and then secret to and there we go we see that's our secret we see there's actually the key pass and then here we actually see our password which we can access we can try the same for secret one and there we actually see our our admin and our user key and yeah

**4:57:21** · so we can actually see right now that in that setup as of now secrets are stored unencrypted in plantex values in at CD so this is the default default configuration when it comes to cube ADM clusters at least at the

**4:57:42** · moment and now it gets actually interesting because now we will encrypt at CD and especially secrets in ET CD at rest why do we want to do this well we probably saw it before if someone got access to etcd directly or the ETD file

**4:57:59** · system like the database then Secrets will by default be stored unencrypted and can be read in plain text which is not good so we would like to prevent this and how can we prevent this well the API server is the only component in kubernetes which talks to at CD so the API server will be responsible for encrypting and decrypting specific content how can we tell the API server to do this well we can do it by creating

**4:58:27** · an encryption configuration and then passing that encryption configuration via a new argument to the API server so the argument is encryption provider config and it then has to be a path to the file system where it is a file with

**4:58:44** · the kind encryption configuration and we will do this later in the Hands-On sessions now it is important to understand how the encryption configuration works it is really easy Once you understand it but let's go through it now so we have kind encryption configuration then we have resources resources so under resources resources we specify the kubernetes resources in this case Secrets which should be encrypted or decrypted by that

**4:59:12** · configuration and then the other important section is the provider section so provider section contains an array of one or multiple providers and we see the first one in this case is the identity provider the identity provider is kind of the default provider which means nothing is encrypted it is just plain text then we have for example two other examples here AAS which is an encryption method uh so we have as GCM and as CBC

**4:59:44** · okay so two encryption algorithms that this configuration um provides or can work with now it's important to understand that the encryption configuration Works in order so at least the provider section Works in order which means the first one is used for encryption when saving new resources okay so this configuration right now would store Secrets unencrypted not

**5:00:11** · encrypted because the first provider is the identity provider okay so new Secrets will be stored unencrypted just as by default but when you would like to read Secrets out of etcd then you can read unencrypted secrets you can read Secrets encrypted with as GCM and you can read Secrets encrypted with as CBC okay so

**5:00:35** · when you save the first provider will be used for encryption and if you read then you can read from all possible providers that you specified here so this gives a few possibilities let's have a look at another encryption configuration example here for example so what is happening here again it is only about secrets and

**5:00:57** · providers we have two providers the first one is as GCM and then we also have the kind of fallback identity provider okay so this means all new Secrets will be stored will be actually stored encrypted under as GCM and we can

**5:01:12** · read secrets from encrypted as GCM or unencrypted because we specify the identity provider if we wouldn't specify the identity provider here and there would be an unencrypted Secret in at CD then we couldn't read it then our API server would not be able to read it okay

**5:01:31** · so if we now want want to encrypt all secrets in at CD how could we do this well if until now we don't have any encryption configuration then we could create this encryption configuration and then simply run cctl

**5:01:47** · get all secrets from all Nam spaces and replace them like we we created down here and this would then cause that every new every Secret in our whole cluster will be recreated under the first provider section specified here which is asgc and if we want to have a look at the other way around let's say many secrets are encrypted or all secrets are even encrypted in at CD what if we would like to decrypt all secrets well we simply

**5:02:16** · create an encryption configuration which has under provider section the identity provider as first one because that will be used for new secrets and then we have our provider which can read the encrypted secrets in at CD so in this case it is this as CBC and then we also again run the comment to just recreate all secrets which means all secrets can be read unencrypted or from asbc and

**5:02:45** · they will be recreated and written unencrypted using the identity provider okay so so much to the encryption configuration it should be easy to understand but let's jump into a Hands-On session where we actually encrypt at CD and look at some secrets in this Hands-On challenge we will now encrypt secrets in at CD addressed and test and verify it so the general task will be encrypt all existing Secrets using as CBC provider

**5:03:19** · and a password of our choice if you like you can try it out yourself just go ahead because you should already know at least know theoretically how the encryption configuration Works otherwise follow me along because that's exactly what I will attempt to do now so on the

**5:03:37** · master note we now have to create an encryption configuration and pass it to the API server so a common procedure is to create a new directory in at CD kubernetes and pass it or mount it into the API server manifest so I create a new directory at CD and in that directory I create a new file ec. yaml which will stand for encryption

**5:04:06** · configuration now we head to the kubernetes documentation you can simply search for et CD encryption the link is also in the resources section of this video and if we scroll down then we see some examples that we already talked in some earlier sessions and here we see actually a small and simple example um encrypting your data so let's copy that

**5:04:31** · one and there we go so we create an encryption configuration and the first provider is AES CBC which is the same as in our task which means because it's the first provider all new Secrets will be encrypted using that provider and because we have two providers this means we can read Secrets encrypted as as CBC

**5:04:58** · or unencrypted using the identity provider and here we see that we now have to insert the Bas 64 encoded secret which is a simple key for encrypting and decrypting the data so let's create a key for this what we can do is um we

**5:05:18** · just need a base 64 encoded string so let's just choose our password our password could be password we could do it like this but one thing that you have to check is if you do it like this Echo password and then pipe it into Bas 64 then actually a new line

**5:05:37** · will be part of your password okay you can see it simply like this if you only Echo password you see it will Echo password but it will also output a new line which is back here so what you can do is you can pass you use the argument DN and there you see you only output password without a new line so we would actually like to do this base 64 and then and it so we copy that string and that will

**5:06:09** · be our password just paste it in here our password will be password save it great now we simply have that file now we have to pass that file into our API server so what we have to do is we have to edit in /c kubernetes manifest our Cube API

**5:06:29** · server manifest and we add a new configuration parameter here and that parameter is actually I mean in the exam you probably won't type it just like that let's head to the documentation and here we see it it is encryption provider

**5:06:52** · config and then it should be the path to that encryption file so for me or for you as well it will be ITC kubernetes um at CD and then ec. yo but we still have to mount that

**5:07:09** · directory into our API server for this let's head to the volumes on the very bottom and we see that this has been already done for for example the pki directory so we can simply copy it the volume section we Mount or we create a new volume for at CD and we call it at

**5:07:31** · CD so simply add a new host path volume you can simply copy one of the existing ones and then we have to do it as well for the volume Mount so here as well I see the volume mount for the pki for the kubernetes certifications I copy it and I simply change it to at CD and the name is at CD so just like that create a volume mount for at CD ITC cuetes at CD and that should be it

**5:08:05** · so let's save it and let's hope the API server will be coming back up and it is actually likely that our API server will not be starting again because there is still a misconfiguration in the encryption configuration and in my case I actually did another misconfiguration let me fix this there is a space missing

**5:08:27** · here let's do it like this so if you haven't done the same mistake as I did then your API server should still not be coming back up but at least there should be locks okay so you should be config um comfortable with misconfigured an API server it's not coming back up and then you go ahead and check the locks so you can go in VAR lock pots and there we go there we have the API server so we simply tail in the cube

**5:08:57** · API server directory whatever lock file is there and there we see a great message invalid value secret is not of the expected length got8 expected 16 24 or 32 so let's go ahead and fix

**5:09:18** · this in our encryption configuration right now this is our password and it's actually just the string password which is eight characters um let's change this so let's change our password to password password which should be 16 characters which is kind of twice as secure let's say and copy that b 64

**5:09:49** · string change our configuration with the updated password which now has the one of the the um accepted lengths we should restart our API server for which I simply move the Manifest out of the directory I check if there's no that there's no API server process running there we go and I move it back

**5:10:17** · in I wait for the API server to be coming back up and after giving it a minute or two the API server should be back up and we can have a look for example add Secrets

**5:10:33** · Let's test it okay so if we look at our configuration then our first provider is as CVC so when we create new Secrets they will be encrypted and we can read encrypted secrets and decrypt them or we can even read unencrypted Secrets Let's test this so we have the default secret here so we should still be able to read that secret although it is not encrypted

**5:11:07** · and yes it is the case we can read it and we see actually the certificate information in it now let's try to read that secret from at CD and for this you can head to the resources section there's actually a comment which you can use to read a secret and we used that

**5:11:25** · one before and you should be comfortable um yeah with with reading a secret out of ETD and actually in the kubernetes documentation on that page for encrypting data that you can actually scroll down and there's also a section here where it shows you how to read a secret out of ETD so you can save that page as a bookmark and access it fast during the exam so let's try to read

**5:11:53** · that default secret from the default service account out of at CD and there we see in this case the etcd client is not yet installed let's install the etcd client real fast and there we go we can read the secret out of ATD and we see the certificate content it is not encrypted

**5:12:20** · now let's create a new secret okay let's simply create a new secret a generic secret we call it very secure we Simply Save from literal credit card 1 2 3 4 okay we create a new secret very

**5:12:41** · secure it has been created now let's try to read that secret from ETD directly very secure and there we actually see we don't see the content okay and the content starts actually with KS and some information and there we actually see the algorithm that has been used to encrypt this secret so this secret is now stored encrypted in ET CD

**5:13:09** · but can we read it through the API server can the API server decrypt the secret for this we can have a look we can access the secrets through the API server just K get secret very secure and the yo and there we actually see the data as base 64 and if we output that data and coded then we actually see there's 1 2 3 4 so we have that secure

**5:13:37** · information right now so it seems to be working that new secrets that are created will be encrypted but existing secrets that are still unencrypted will remain unencrypted we can test this now by

**5:13:54** · again using the secret for the default service account and we simply delete it okay we say delete secret for the default token and then hash value and then there should be some amazing controller manager which recreates it and there we go okay we have a new secret that has been recreated for us and let's have a look can we get that

**5:14:22** · the value the data of that secret through the API server so KGET secret default token hash yl yeah yes we can still get it just as before but now the question is can we actually get it out of ETD can we read

**5:14:41** · it directly out of etcd let's have a look we run the etcd get command again and for that comment actually by the way so if you get then everything in etcd when it's configured with kubernetes will be stored under SL registry then slash type in this case secret then the namespace default and then the name of the resource in this case default token and then the hash and

**5:15:08** · here we see okay it doesn't work as before we see there's a lot of content and we see that it's encrypted using as CBC so this works okay so this works and if we now would like to go ahead and encrypt all secrets in our cluster what could we do well we can simply go ahead and delete all secrets and recreate all

**5:15:32** · secrets again but before we do this I would actually like to test something so I would like to change our encryption configuration and I would actually now like to comment the identity provider out okay so we will now only pass one provider only the as CVC one and then we see what will happen so go ahead in your encryption configuration comment out the identity provider enter save your file and restart your IPI

**5:16:07** · server I will do it by moving the file out of the Manifest directory and moving it back

**5:16:28** · in and really give it one or two minutes time to restart after which the API server should be back again there we go and we can now read all secrets or just some secrets well let's test these secrets from the default namespace so we get all secrets from the default namespace and we output as yaml and this

**5:16:52** · seems to work with for example our very secure secret we can read it and we see the data and as well for the default service account token we can just access the secret normally and unencrypted through the API server okay so the API server will actually decrypt these secrets for us right now but if we have a look at our encryption configuration then we see we only have one provider specified right now which means all new Secrets will be encrypted using the provider and we can also only

**5:17:24** · read Secrets which have been encrypted using that provider let's test this let's find a secret which already existed before our change for example in the cube system

**5:17:41** · namespace and there we already see there's an issue right we just want to look at secrets in the cube system namespace and we see internal error occurred unable to transform key no matching prefix found okay so right now our kubernetes API server is

**5:18:01** · actually not able to work with Secrets which have not been encrypted using that provider okay so what we can do is we should enable this again and move the API server or restart the API server

**5:18:23** · again give it one or 2 minutes and because I made a little bit of a Time jump right now my API server should be ready again there we go which also means because we kind of fixed the ETD config we should be able to read Secrets again from the cube system names space there we go but if you remember from the original task we should encrypt all existing Secrets using as CBC and

**5:18:53** · the password of our choice okay we already chose the password password password maybe not the best choice for production but we we still have to encrypt all existing Secrets using it because let's head to our encryption configuration let's have a look at it as of now our encryption configuration still has to look like this we still have to have the identity provider in it because there are still some unencrypted secrets in etcd and we saw it before if we remove it now we are

**5:19:23** · not able to read unencrypted secrets and we would like to remove it which means at first we have to encrypt all existing Secret Secrets how can we do it well we simply have to recreate all secrets and once we recreate a secret it will be created again which means it will be created using the first provider which which is our encryption provider so let's go ahead and encrypt all secrets

**5:19:50** · in kubernetes so what we can simply do is we get all secrets from all namespaces in the output in some output format like Jason or Y and then we pipe it and we recreate it so we replace it and then we say- F and whatever comes back so let's run it okay various Secrets have been

**5:20:21** · replaced Let's test this with one secret okay let's test this with one secret out of the cube system namespace let's choose one secret for example that one The Weave net token you can choose any secret out of the cube system namespace because we didn't work with these secrets so far so if I just get the secret like this then I'm able to read the secret content through the kubernetes API server which is already great and now I will try to use the at CD direct

**5:20:57** · access so what I have to do is I have to check the cube system namespace and then I specify weet token and the hash code and now I see that that one is actually encrypted and we see here in the infotext that it's actually encrypted using as CVC so as of now all secrets all existing secrets are

**5:21:23** · encrypted which means now we could go ahead and actually remove that line because we don't as of now we don't need the identity provider anymore in our cluster setup and with this we actually went ahead and encrypted secrets in at CD at

**5:21:44** · rest and we reach the end of the kubernetes secret section and you might ask yourself the question why do we even have config maps and secrets if Secrets by default are not encrypted so the idea in general is to have a SE operation of concern okay so config Maps should stay as they are they probably never have to be encrypted because they don't contain credential information but then we have secrets and for secrets we can decide to

**5:22:15** · implement a more secure way that way we don't have to encrypt all resources in our cluster because encrypting and decrypting resources can also cause problems so it might be easier to only do it for certain resources like Secrets which actually contain credential information which should be protected in a better way and for this there's the encryption

**5:22:40** · configuration right and we actually encrypted at CD using an encryption configuration but in production you kind of want to go even one step further like we used encryption configuration with a static key just on the local file system mounted into the API server that's not the best way to manage a key it only means if someone got access into at CD

**5:23:04** · that attacker cannot read the secrets but if the attacker got access to the control plane to the master component and is able to read the file system well that attacker is able to read the key and then use the key to encrypt data okay so in production production kubernetes security and secret encryption often depends on third party tools for example there's the KMS provider so it means you use like an external um key store to manage your key

**5:23:33** · and then to use that managed protected key to encrypt your ETD data but this won't be part or probably won't be part of the exam because it depends too much on third party tools as well there is Hashi cob vault

**5:23:50** · which does a different approach of secret management and which can also work with KMS or other key store providers and this in combination or just hhic cor world is actually something that is very common for production kubernetes clusters but yeah as of now um it depends highly on third party tools and this will be out of what will be required in the cuetes exam because in the cks exam it will be more from the plain kubernetes um perspective

**5:24:23** · and less depending on third party tools there's a kubernetes secret risk section in the kubernetes documentation link is in the resources section it's a very small section but maybe you should read through it again it just combines various things that we talked about here as well in one small

**5:24:47** · section if you like to go a bit further there's a great talk Bas 64 is not encryption a better story for kubernetes Secrets or even build secure apps faster without Secrets which goes in a little bit into third party tools and how they manage secrets so this is definitely important for production but probably not important for the actual cks xam so in this section we talked about what secrets are and how we can deploy

**5:25:19** · and use these in kubernetes we then also hacked some Secrets using at CD and Docker and this should just show us that by default where secrets are stored how they are passed to the application are they by default um secure or insecure

**5:25:37** · and we then actually also secured Secrets a bit more by storing them encrypted in at CD so when it comes to the exam the main focus should be that you should be able to work with kubernetes secrets from the API server right so you should be able to create secrets to mount secrets into pots to

**5:25:56** · change secrets and yeah make them available in various ways to Parts like mounting file system environment variables right um then the hacking part of Secrets you might be asked to read a secret out of etcd check if it's encrypted decrypted you might be asked to check some existing etcd encryption or actually to configure etcd to encrypt data using a specific provider which um

**5:26:25** · which will be given to you okay so that much about kubernetes secrets and see you at the next

**5:26:43** · one we will now talk about container runtime sandboxes when it comes to kubernetes security then we have to talk about the container runtime security because your applications and kubernetes are only as secure as the container

### Microservice Vulnerabilities - Container Runtime Sandboxes

**5:26:59** · runtime is secure okay and because of this we will now get into a little technical overview of what containers actually are how they communicate with the Linux kernel then we look at possible ways of breaking out of a container and finally we will look at container runtime sand boxes like gvisor and cutter containers containers are not contained

**5:27:22** · um something that should always be in the back of our minds right we might imagine the container is this steel container on a container ship and um it's hard to get in it's hard to get out but it's not like this right so we just have to remember that just because it runs in a container doesn't mean it is more protected let's have a look at what containers actually are okay we see here we have our operating system and our operating system has a kernel in yellow

**5:27:52** · and what happens to processes well processes run on the Kernel let's say on the Linux kernel and if we now have a container container and in that Docker container we have a process running app1 process then that process is actually running on the Linux kernel just as any other process on the operating system as well okay a process in a Docker container is simply running on the same

**5:28:18** · Linux kernel and it can communicate directly with the Linux kernel just as any other process the difference is that this process is wrapped in some kind of a kernel group we will now just call it kernel group in later sections we will actually go deeper into how containers

**5:28:36** · are actually created and if we now add a second Docker container and a third Docker container then we see they're all separated by being in their own kernel Group which makes them a container but the processes app1 process app2 process app3 processes they all run on the same Linux kernel and they can communicate with the same kernel and this means if

**5:29:02** · the F1 process manages to break out of its container of its kernel group and manages to access the kernel directly then it could through the kernel access all other processes running on that same kernel on that same machine as well so we don't have a strong isolation layer in a sense um if we think about virtual machines right if we think about virtual machines then we have a stronger isolation layer than when it comes to container

**5:29:34** · what is a sendbox let's talk about the term sendbox um from the technical sense right from the software development background or IT background what do you think of when you when you hear the the uh the word sandbox you could think of a playground when implementing an API or like a payment Gateway you get like a Sandbox environment to test your

**5:29:54** · application you could think about a simulated testing environment for example in your cicd pipeline you could think about of a development server which is called a Sandbox but here when we talk about sandbox we mean an additional security layer to reduce the attack

**5:30:14** · surface let's have a look at containers and system calls down here we have the hardware on top of the hardware we have our kernel let's say our Linux kernel and then we have a process right the app1 process it runs on the Linux kernel and it comp it can communicate with the Linux kernel directly by running system calls by the so-called system calls CIS calls the system calls can kind of be seen as an API which the kernel provides

**5:30:45** · for processes to communicate with it okay so the app1 process could for example call system calls like PS to see processes or to see the network interfaces or maybe even to reboot the system these are all system calls and we will in later sections also look at some of these system calls in more detail let's add another process we have our up app2 process it's another Docker container and it also can communicate

**5:31:13** · with the same Linux kernel and can execute system calls on it now let's talk about two terms let's talk about the kernel space so if you hear that something is running into kernel space or in user space then these are these two sections okay so the kernel space SP is kind of everything that arounds the kernel and it might include the system calls and then the user space is everything above which uses the system calls to communicate with the kernel so how can we now maybe

**5:31:43** · make this more secure how can we control the processes and maybe contain them a bit more well we could introduce sandboxes if we introduce sandb boxes at these positions and every container every process will get its own sandbox

**5:32:01** · so a Sandbox for every container this would mean that we don't allow the processes to communicate directly with the system calls offered by the kernel and which allows us to mitigate malicious things and to restrict the calls much more and in a in a better way so this is the idea of container runtime sandboxes well do they come for free no a Sandbox comes not for free why

**5:32:28** · I mean we introduce a new new layer of logic where our processes have to go through and this cost more resources right and generally um it might be better for smaller containers to use send boxes and if you have very large heavy containers it might create more

**5:32:45** · overload it is not good for zus call heavy workloads if you have a container uh and the process in your container is using various CIS calls of the kernel directly then using a Sandbox in between might not make sense and you don't have direct access to Hardware through the Cs call so this is also something to keep in mind so sandboxes might not be something for every application but usually for most application it might be a good idea to restrict

**5:33:20** · these time for a Hands-On session we will contact the Linux kernel from inside a container it might sound spectacular but you will see it is not so just follow me along head to your master note we create a simple pot with image engine X and we exec into this pot we will get a

**5:33:50** · bash there we go we are now inside the container let's contact theber not the kubernetes API let's contact the Linux kernel and we we simply do it by calling you name- R and what do we see here we actually get a kernel version back this actually executed the uname Cs call okay

**5:34:16** · and if we now head outside of the container and we are now again on the master node then we can execute it here as well and we see we get the same string back you right now have to believe believe that both these commands you named that- r on the Linux level and also on the pot level they executed a sis called call called un name and from this the actual version got returned and

**5:34:48** · we can actually use the S command so we write SRA uname dasr which will actually show which sus CS a process makes okay so we run s TR un name- R and there's a lot of output we don't have we don't go through this now extensively we actually have another section where we go into detail but we see for example things like close was called closes a CIS call

**5:35:17** · um we see things like uname okay and here the uname sis call was actually called and from this um the version was returned okay so here we saw in a simple way how a process inside a pot inside a container can actually contact with the Linux kernel via CIS

**5:35:46** · calls if you like you can Google Linux kernel dirty car and this is a famous Linux kernel exploit which worked on earlier kernel versions and you can try to find the exploit and maybe executed in in your pot in your container to see if it still works it probably won't because it was only effect in older versions but this is a nice example of

**5:36:08** · an exploit which actually uses race conditions in the Linux kernel to then gain more permission and root permissions and access the complete kernel and the

**5:36:24** · system we will now step a bit outside of Docker of our docker world and talk about different and other container engines and then when we do this we have to talk about the oci the open container initiative what is the oci well the oci

**5:36:41** · is a Linux Foundation project to design Open Standards for virtualization and what they do is they create and maintain a specification and that specification for run times for example defines what is a runtime what is an image what is a distribution and because there is now a specification for runtimes we can have interchangeable

**5:37:07** · runtime engines right so for example applications like the cubet can communicate with different container run times because they all use the same interface they all use the same specification and what the oci does as well is they create an actual runtime which is the Run C it's a binary and

**5:37:28** · that container runtime implements their own specification okay so they create a specification and a runtime which actually implements their own specification that's the oci let's have a look at a workflow if we have Docker on top well then Docker doesn't create containers directly Docker communicates through different layers like container D and then run C on the bottom okay so down here we see the runc the oci runtime which actually

**5:37:59** · implements the oci runtime specification and then runc communicates with lip container to create the actual containers let's have a look at the early days of kubernetes okay in the early days kubernetes was developed with a tight coupling of Docker and it took some time to to decouple this actually so in the early days we had the cupet and the CET was directly communicating with Docker shim Docker D container D run C okay these were the the early days

**5:38:32** · and through a lot of work and effort it was actually done to create the CRI in kubernetes the container runtime interface and the C the container runtime interface allows the CET to communicate with different run times right we still have the traditional way or Docker shim Docker D container D runc

**5:38:54** · but the CI allows it then without having to recompile the coulet like kind of plug and play allows to use things like cre container D container D run C or cryo runc or even container D directly and then a shim API underneath

**5:39:12** · and then the container runtime um sand boxes like cutter containers firecracker or gvisor how can we configure a cuet to use a different container runtime through the CRI well with the container runtime parameter and container runtime endpoint parameters and a CET um always

**5:39:33** · have to can only run at one point in time with one container runtime it can't run with stalker and directly with container D for example you have to choose one at at least at this point in

**5:39:50** · time cutter containers cutter containers is one container runtime sand box that can be used and let's talk shortly about it cutter containers okay how does cutter containers work cutter containers work with additional isolation with a light white virtual machine and individual kernels okay so this is important if we

**5:40:12** · have the Linux kernel down here we have one instance we have our Linux kernel and on that instance we have different containers running okay usually these would all simply be running in its own container rapper but communicating directly with the Linux kernel here we now see that for every container we have a different virtualization and in that

**5:40:33** · small virtual machine we have a different Linux kernel and in that kernel our process is running okay so we are now very far away from the traditional containers because every container now actually runs in its own virtual machine with its own Linux kernel completely abstracted from the original Linux

**5:40:56** · CER so cat containers provides a strong separation layer and an easy very easy way to create and manage these virtual machines like you we don't have to manage and create these ourselves it's all done for us just by running a container using the cutter containers runtime engine runs every container in its own private virtual machine and qo as default um but yeah it

**5:41:23** · needs virtualization right and so if you use a cloud like Google cloud and you create an virtual machine in instance then you can't just use Q emo and create more virtual machines inside this I mean it's possible but then you have to use things like nested nested virtualization which you have to enable in your instance when you create it or you might have to create instances of special type so that to keep in mind um it uses virtualization and in a in a modern Cloud where you already use Virtual machines it might not be as easy to

**5:41:58** · configure gisa from Google let's talk about gisa so gisa described itself as a user space kernel for containers in the beginning if you remember we talked about user space and kernel space okay and now we actually have a kernel which runs in user space bit confusing but we will see what this means soon it adds another layer of Separation

**5:42:25** · it is not hypervision machine based like C containers it simulates kernel CS calls with limited functionality what this means in the end is that Google actually with gvisor implemented its own kernel its own kernel in goang which accepts all the system calls that the normal Linux hn does but it accepts them in interface and then maybe transforms them maybe sorts them out maybe skip some and then communicates itself with the Linux ker

**5:42:58** · okay it runs in user space so separated from the actual Linux kernel and the runtime is called runc which it provides let's have a look at an image we see again independent user space kernel as they promote themselves well we have the hardware on bottom and then we have the in red the host kernel which is the Linux kernel okay on top of that we have gisa and then on top very top we see our application which can be our process running in our container our

**5:43:29** · container process will perform all possible Su calls against gvisor and then gvisor will just forward limited system calls change system calls to the actual Linux kernel so this also means that um exploits that might be released for the real Linux kernel won't work if you fire them against gvisor because it filters them out and it provides a very different new implemented interface on top of the Linux

**5:44:04** · kernel we will now create a runtime class for the runtime run SC which is gvisor what is a runtime class well a runtime class is a kubernetes resource which allows to specify a specific or a different runtime Handler like in our case runc and then we create the runtime class and the runtime class exists in the cluster and we can then say for specific pots we can say hey that pot should use that runtime class okay and if the note on which that pot is

**5:44:36** · running uh has um support for that runtime class then everything will work fine so let's have a look runc is not yet installed on our worker note but let's go ahead create a runtime class create a PO that uses it and see what happens and what will explode we will head to the kubernetes documentation and search for runtime class in there we scroll till we see a nice example which we can borrow okay I create a file rc.

**5:45:19** · yo let's remove the comments okay you see it's a very simple file we give it a name we call it gvisor and the actual Handler would in this case be runs C okay so this would be how you have to create a runtime class for gvisor if you would have to in the certification let's create it great let's have a look there we see

**5:45:53** · we have our runtime class gvisor it uses the Handler run SC let's create a pot we call the pot gisa we use image engine X and we only want to have the yo

**5:46:13** · file call it pot so we want to edit the pot okay we now want to say that this pot should actually use a different runtime it shouldn't use the default one it should use a different one for this we head back to the documentation scroll a bit down there's the usage section there we see okay under spec on pot level we can simply specify a runtime class

**5:46:40** · name um let's call the runtime class name test and let's see what happens we will try to create the PO and it will actually say hey rejected the runtime class test doesn't exist so when you create a port with a runtime class then your runtime class has to exist we just created a runtime class called gisa which exists which is running so this should work

**5:47:10** · now try to create the pot again this looks better there we see pot is container creating and we see the pot is actually has been scheduled to a worker note it's scheduled on a worker note is not running on a worker note it's stays in container creating let's have a look let's describe

**5:47:36** · it and there we actually see unknown runtime Handler runc is not supported if we would have installed gisa and runc on the worker not then this would work but in this case as it's not installed yet it doesn't work but you know how to create a runtime class and for gvisor you would create it using the Handler run SC in this Hands-On session we will now actually install gvisor run SC on our

**5:48:05** · worker note I would say this Hands-On session can be considered optional because we might destroy our worker note we might misconfigure it the install might fail and you have to completely recreate your worker note um if you're up for it awesome let's move along if not for the exam you should be fine with just the session that we did before where we create a PO and a runtime class class um yeah that

**5:48:30** · should be fine now in this Hands-On session what we will have in the end is our worker node with cuet which is already configured to use container D but we will now configure container D to use runc as well as runs gvisor by choice like if we create a pot with a certain runtime class from the session before we should still have a pot stuck in container creating why is it stuck in container creating well if we edit that

**5:49:05** · pot then we see it uses a specific runtime class gvisor and if we look that runtime class actually exists it uses the Handler runs C but if we describe the pot then we see the reason why it can't be created is no runtime for Runner C's

**5:49:32** · configured what we want to do now is to actually move to our worker node and on that worker node we now want to install gvisor for this there's a link in the resources section to the install script and we now have a short look at the install script in um the G repository we

**5:49:54** · also have a small example of the runtime class that we created and the pot and the install script just have a short look what it will do um we will actually install a specific version of gisa which works with the current kubernetes version of this course if you have issues and something doesn't work you can also try to use this line instead where you use the latest version so we install run SC binaries here and then we actually alter the container D

**5:50:27** · config where we actually here at the Run SC runtime availability okay and that's it we restart container D and that should be it so let's go ahead and install run that

**5:50:57** · script

**5:51:23** · I didn't see any crazy errors that sounds good let's check the status of container D looking okay we can check the status of the cubelet looking also okay I will head back to the master node to the control plane and check how our pot is doing and suddenly the pot is

**5:51:57** · running on the worker node and if we have a look and EXA into the pot then we can actually run un name-

**5:52:19** · R and here we see that the version so we are now in our pot in the container and we run a process which um communicates with the Linux kernel and in this case really simple just asks for the version of the Linux kernel and here we see it's 4.4.0 if we though have a look at the

**5:52:47** · notes then we see the kernel version running on that note is actually this and if you remember from the session before if you run this comment you name r if in a pot which is not running in gvisor then you actually get exactly that version back because you directly communicate with the Linux kernel now in our gvisor po we are actually in the gvisor sand box which means all s calls our processes in that container do won't

**5:53:19** · go directly to the host Linux kernel but they go through the gisa kind of emulated simulated CER which we can see on the version here what we can also do is we exit into that PO and we run um

**5:53:43** · dmsg and there we can actually see that gvisor was started looking good we installed gvisor and our pot container is running in a sandbox

**5:54:03** · well this was a long section but you might still be a little bit confused about the oci CRI and all the container runtime talk there's a great talk called making sense of the container runtime landscape I can really recommend it link is in the resources section if you like to dive a bit deeper into gvisor there's the talk sandboxing your containers with

**5:54:24** · gisa it talks a bit generally about sandboxing and and then on the example of jisa it's a talk by Google and then there's a talk cutter containers introduction and overview which goes into cutter containers uh which uses more the virtual machine

**5:54:42** · approach well we reached the end we talked about container send boxes we talked about containers in general and then how send boxes can um encapsulate these and then we talked about container D and cutter containers gvisor run SC and we actually created kubernetes runtime runtime classes and used them inside a

### Microservice Vulnerabilities - OS Level Security Domains

**5:55:19** · pot OS level security domains in this section we will jump into security contexts po security policies and we create various scenarios and Hands-On sessions where you follow along and where we create and use these let's

**5:55:37** · first start with security contacts so security contacts allow us to Define privilege and access control on pot level or container level and with this it allows us for example to specify the user and the group under which a process is running or if it's can run privileged or unprivileged what this means we'll talk about this soon for example we can Define Linux capabilities and much more if we now

**5:56:05** · have a look at a simple pot example which we see here it's just a simple pot spec then we see on top we have a security contexts this is like on pot level it will be um passed down to all containers in that pot and in this example we simply say it should run under a specific user uh under a specific group and we also talk about the fs group parameter that we can set here and then we see down here we have another security section where we actually for that single container we

**5:56:35** · overwrite the security contacts of of the pot or if on pot level there wasn't even a security contact then we just set it for that single container so in this example let's look at these three examples if we set or if if you are on a um on a Linux machine you can run the command ID which would show you your groups and your user ID and so the U ID the user ID that you see

**5:57:03** · from that comment that we was set by the runs user um section and the main group your main group ID will be set as run as group and then the supplementary group ID the groups section down here will be set with the fs group

**5:57:21** · section so there are some options that you can set as you see here but as always um it's always good to head to the documentation and have a look around so what I simply would do is search for security contacts and then there's actually a nice page security context for pot or container and it shows you

**5:57:43** · just examples and what is possible but also what I would like to show you is if you scroll a bit down set security context for a PO then it actually links to the pot security context object and it actually links to the kubernetes API reference okay and it shows you now it did jump a little bit I wasn't right let's search for pot security contexts contexts there we go

**5:58:09** · okay there we go so the section um that is possible to set in a pot is actually a pot security context and then in the API reference we see all the possible things and they all this um explained what it means so just as a short Excursion of uh how to use the API

**5:58:29** · reference maybe sometimes if you're unsure of what an attribute means and if you can use it in this Hands-On session we will create a simple Po and then using security context we will change the user and the group under which the container processes are running and we will verify this using some simple comments okay for this head to to your

**5:58:58** · favorite kubernetes cluster I'm on my master note and I will create a simple pot I call it pot let's use image busy box and we want to overwrite the command we want to keep it running by default busy box won't keep running we only want the yaml output

**5:59:21** · and that's why we use dry run into a file I call it po. yo and then we we can back here still pass the comment which we would like to execute I use sleep one day so that it keeps running for a bit it should be dry run client

**5:59:42** · exactly and there we go that's the AMOLED was created here we see the comment that keeps it running simple po busy box image let create it

**6:00:04** · it's running so we can exec into it and get a shell there we go we type ID then right now we see we are we are root and group root as well and we can also just create a simple file touch test and have a look and that file is also created for user roup and group root okay let's change this in our pot declaration we would now

**6:00:34** · like to set a security context and for this because we don't type anything ourselves uh in the real certification we will head to the kubernetes documentation search for security context and steal as much as we

**6:00:51** · can there we go let's copy this there we go we simply specify the user IDs under which it should run and this is now on pot level which means it will be applied to all containers we could also move this into that single container of us there we go let's update our

**6:01:26** · pot and it is running great we exec back into it we run ID and we see we are now user 1,000 and group 3000 and we do the very same thing for touch test oh and there we see in that directory where we are right now we don't even have write permissions which is great so if you

**6:01:49** · have a service running in that container and someone breaks out of that process at least um there are no root permissions and at least that person can't write anywhere on the file system or not at all places right but by default there's a temp folder so we CD into SLT and everyone should be allowed to create files in SLT at least in the busy box container and that version and there we see we created a new file and now it's user 1000 and group

**6:02:24** · 3,000 we will now extend our scenar scenario and force the container to run as nonroot by creating another security context okay for this the pot is still

**6:02:39** · running let's have a look at our current yaml declaration that's our pot we have the security context which actually defines the user in the group what we can do now is that for the container so on container level we will create a new security context and we can write run as non root and we

**6:03:05** · say true okay so this now means that this container is not allowed to run as root user let's save it we delete our pot and we create the pot again there we go let's have a look if the pot is running running the PO is running everything is good why

**6:03:32** · well because we Define that it runs as user 1000 which is not root user root is has the ID zero so what if we disable the security context on top let's disable it now so that means the only security context active is the one on container level which defines hey that container has to run as nonroot we save we delete the existing one we

**6:04:02** · create the new one and there we see create container config error the pot won't be created and if we describe the PO then we also see why container has run as nonroot and image will run as root so if

**6:04:24** · the busy box container itself the docker container itself would run as nonroot and this would go through as well okay so so this section doesn't mean that you also have to specify a run as user here you can specify it if the container that you're using doesn't run as user already

**6:04:51** · itself let's talk about privileged containers so by default Docker containers run unprivileged and it is possible to say that a specific container should run privileged for example to be able to access all the devices or to be able to run a Docker demon inside your container

**6:05:13** · for like nested Docker and how you would do it is when you run the docker run command you can simply pass D- privileged and then that container will run privileged so what does privileged mean privileged means that container user roote with the ID Z is directly mapped to the host user roote with the ID Z so

**6:05:35** · usually when you have containers one of container abstraction also means that you can have the same user IDs inside a container on outside on the host system you can have the same user IDs but it doesn't mean that they have the um the same permissions and are directly linked right so this is like a separation layer which means which is also why uh

**6:05:57** · container process can think it is rude but it's only roote inside the container but when we run it as privileged then this actually changed and there's a directly mapping between the users so by default in kubernetes as by default in Docker containers are not running privileged but as we see down here we can use a security context to change this and let's do this in the next Hands-On

**6:06:25** · session in this t on session very exciting we will now enable privileged mode inside the container and test this using this CTL with this CTL we can actually set kernel parameters at runtime if we have the proper permission to do this let's test this let's head to

**6:06:44** · our cluster the pot should be running your pot might not be running when if you're still on the state from the last hands on session so simply head back into your yaml declaration and enable the security context on top again so we say it runs as a user as a group and down here we say it has to run as nonroot that setup should be working right now your pot should be running and if you exec into the pot then we can now try to run the zus CTL so we say this

**6:07:18** · CTL kernel. host name set it to something read only file system h okay let's head back to our pot and let's try to change this so the read only file system is probably because we actually run the container as nonroot okay so what we

**6:07:44** · can do here is let's actually remove the whole section on top we don't need it anymore and let's comment out the security context on bottom so we simply want to run the pot straight As the container the box container wants us to okay so delete the Pod create the PO

**6:08:03** · again and exec into it let's try this again is this CTL kernel. host name attacker command there we still see read only file system hm so it was not just because of this we are not allowed right now even if we are root inside the container as we are right now like we can EXA back into it ID we are root right now we are still not allowed to perform

**6:08:33** · this let's enable privilege mode and see what happens then so in the security context for the container we will set privileged to true that should be it recreate the

**6:08:52** · PO exer back into it I D still shows no difference but if we now run the ZL colel hosta comment then we actually see that it worked and that we are now able to because of setting privileged mode to

**6:09:16** · true now let's continue with privilege escalation allow privilege escalation controls whether a process can gain more privileges than its parent process and we will see this soon in action as well

**6:09:31** · first let's have a look at a yaml declaration and we see an example security context down here where we said allow privilege escalation to false because by default kubernetes allows privilege escalation so before we talked about privileged now we talk about privilege escalation what does this mean well privileged as we said before privileged means that container user zero is directly mapped to host user zero so the

**6:09:59** · container then actually runs as root and has the same permissions as root privilege escalation means that a process can gain more privileges than its parent process we will now disable privilege escalation or the allow privilege escalation in our pot and verify this so if we are in our pot declaration then it looks like this right now now we set privilege true let's set this to

**6:10:33** · allow privilege escalation to True okay this is the default setting we now simply Define the default setting is default to true but let's do it like this and recreate the

**6:10:51** · pot and when we exec into the PO we can have a look at the magic proc directory we will talk about that proc directory also in another um section of this course and if we have a look there in one and status then we can actually see no new privileges is set to zero okay let's change this to

**6:11:25** · false recreate the PO and have a look again under proc one status and now we see no new privileges is set to one so this is how the allow privilege escalation setting can be

**6:11:55** · defined we should talk about Mutual TLS M TLS and for this we explain what this means and we also have a look into the pot topot communication we then talk about service measures and how they implement this and we also check out some scenarios about

### Microservice Vulnerabilities - mTLS

**6:12:23** · this so what is mtls mtls stands for Mutual authentication it is a two-way bilateral authentication which means that two parties can authenticate each other at the same time and by this create a secure two-way Communication

**6:12:45** · channel so let's have a look at kubernetes and the default situation there by default in kubernetes every pot can communicate with every pot and this is done unencrypted it is guaranteed by the cni the container network interface and the various cni plugins out there and well a common situation is that we have an Ingress which can accept traffic from the outside request will hit the Ingress and then these will be forwarded into our cluster and if that Ingress is

**6:13:18** · public facing then it's probably protected by https TLS and a common practice is also to perform TLS termination on the Ingress which means the traffic will be decrypted and then the decrypted traffic will be passed into our cluster very common

**6:13:37** · scenario now what if we have an attacker inside our cluster which manag to take over and component like a pot gain Privileges and is now able to intercept traffic perform a man in the middle attack and listen to traffic so for example like the traffic between Port one and Port two right now is unencrypted and the attacker could read everything now what mtls would do now in

**6:14:03** · kubernetes cluster is to encrypt all traffic which means that every pot has to have the ability to encrypt and decrypt traffic and then the encrypted traffic will be sent to other parts so this is a good goal and this is the main goal of mtls in

**6:14:22** · kubernetes so let's have a look how we could implement this between two parts how can we Implement mtls between two pots okay let's say we have pot one with one single container called app and the same for Port two also with one single container now these can communicate with each other right now just

**6:14:43** · unencrypted now we would like to encrypt the traffic so this app container would need to be able to encrypt traffic and then send the encrypted traffic to here and then this container would need to decrypt it traffic and then use the decrypted traffic for this port one

**6:15:00** · would need a client certificate Port two would need a server certificate so this is right now one way right the traffic goes from part one to part two and we also would need a certificate Authority which manages these certificates and watches over everything so now we have the one way for this and if part two

**6:15:20** · would also like to communicate secure with Port one then we also need the way back which means our po two needs a client certificate and our Port one needs a server certificate this way partt one can identify part two and part two can identify and verify partt

**6:15:38** · one and we will also probably like to rotate these certificates right we don't want to create a certificate and make it long lived like 10 years and then don't worry about it like what if a certificate get gets into the wrong hands so for this we probably also want to rotate the certificates where which makes everything a bit of overhead right if we only want our certificates to be shortlived like 10 minutes and rotate them very frequently which is good for security then this sounds like a lot of

**6:16:09** · work so we now see here four certificates but we could also do this actually by simply creating one certificate for every container right and this one certificate could then play the the client certificate as well as the server certificate but like having these displayed as single certificates

**6:16:33** · makes it more clear in the beginning I feel but still we need to have these certificates in every container how could we do this without creating too much overhead let's have a look at this so how many service measures do this is by using a proxy SAR

**6:16:53** · container here we now see that our app container would like to communicate with the app container of Port 2 and it's not longer doing this directly it's going through its S car container it's proxy container and this proxy container manages everything regarding mtls sends the encrypted traffic to another side car proxy container in part two which then decrypts the traffic and sends the decrypted traffic to the app container so that will be the the communication workflow now

**6:17:27** · and the great thing is that that proxy container could be managed externally and this means that we don't have to even touch and change our application container our application containers can simply run using HTTP they don't need to know about certificates they don't need to know about TLS they can concentrate on what they do the application logic

**6:17:49** · this means we extract all the mtls and the security into a side card container which we can then simply inject into every pot and they do it for us and this side car container here could be managed by an external manager and this external manager manages everything the certificate Authority creating these certificates rotating these certificates and this makes it really easy for us and this external manager could for example be a service mesh like stto or Linker D

**6:18:21** · so that's the way that stto does it for example using a side car proxy so now you might think how can that actually work if we have at the proxy how in a pot can it work that all the traffic suddenly goes through that proxy let's have a closer look at this so here we now see that the

**6:18:41** · application container the app container can't communicate directly with other pods everything will go through the proxy you could kind of say that the proxy is performing a man- inth the- middle attack to that application container right because the application container can still communicate with everyone else but it will all the traffic will be redirected through the proxy container and then actually at this place encrypted and decrypted so

**6:19:08** · this is for example possible by creating IP table rules to Route the traffic via the proxy and when the pot is created we could create an Enit container and an Enit container will run to completion at the initialization and only when all init containers are done with their work

**6:19:28** · then the application containers will run so we could create an init container which needs the net admin capability and could then Implement for example IB table rules to intercept all traffic and then the the proxy container would need to do all the magic to encrypt and decrypt and use the certificates so that is one possibility and that's for example how how sto manages to do it

**6:19:59** · in this Hands-On session we will now create a proxy SAR container in our po which has the net admin capability and with this we kind of simulate the way of how we could create such a proxy s side car and Implement rerouting rules in a pot let's have a look first we should create an application container so we simply create an application container image bash which pings Google all the time and this this simulates in our application so we do krun app image bash

**6:20:31** · we would like to overwrite the comment of that container we would only like to have the yaml because we would like to change it so we pass the yaml in a new file and the comment that we will override will be ping google.com this should create our skeleton that we can use now let's have a look what has been generated yes this looks great simple CT

**6:21:05** · with one container bash and it executes a commment to Ping Google okay let's create that PO and verify that it is

**6:21:20** · working it is running let's check the locks of that container and and there we see yes it is simply pinging Google our application is running now we would like to create a proxy site C for our application so we edit our yo file and

**6:21:39** · we add a new container section so what we can do now here is we simply call that container proxy we use the image Ubunto and we also use a commment and that should be executed for this we also use sh to run

**6:22:02** · a comment and the comment that we run now will be actually a bit hecky don't judge us for this we will now install AP tables and then run IP tables so write epet EPG get update at first then appg install IP tables without any interaction Dy and then we run IP tables to Simply list all available

**6:22:34** · rules right now and then we sleep one day at the end okay so what it should do is run an EPG get update install IP tables without any interaction then we run IP tables to see all the currently implemented rules and then we simply let that container sleep for one day okay let's execute this one and let's have a look what will happen so what I will do at first now is I will delete my running

**6:23:06** · container very fast with a grass period of zero there we go and I will create that pot again okay now we see we have two

**6:23:23** · containers great this seems to work and we see one is ready but we have the status error okay what happened let's describe our pot nothing seems to be wrong here the container itself started so let's check the locks of our appp and the container

**6:23:44** · proxy just like this and there we see okay great it actually did the up update and the install but down here when it tried to run tables we actually see permission denied you must be rude perhaps IP tables or your kernel needs to be upgraded so what we now have to do is to provide this container with some additional capabilities okay our proxy container needs capabilities to actually run and use IP tables like here for this

**6:24:19** · we should head to the kubernetes documentation and search for pot capabilities and we should find a page configure a security context for a port or container so this can be done using a security

**6:24:41** · context and if we search for net admin then we also see there's already a great example which we can use down here there's a container with a security context which adds the capabilities net admin and syst time so I simply copy

**6:24:57** · that one and use it and we only want to have the net admin so I remove these Sy time and it should look like this okay so our container proxy now has a security context where it adds the cap capability net admin let's go ahead and replace the PO I delete my PO and I create

**6:25:23** · it and now let's have a look if something changed both are running and it seems like balls are running and if we check the locks again of our proxy then we see nice it

**6:25:40** · runs through and now it actually did list the IP table rules the currently implemented ones not that many but it could now also use IP tables to implement new rules and this would work because in a PO both containers or all containers share the same Linux kernel Network

**6:26:07** · namespace and with this we reach the end of the mtls section if you like there's a great article by sto demystifying sto SAR injection model which explains how stto does it what did we talk about so we talked about mtls we talked about pot topot Communication in general we actually created a sar proxy container which has the net admin capability and could then for example use IP tables so at the

**6:26:37** · point of this recording we don't have any information that actual service measures like stto like link will be part of the ckss certification and we also have no information about what could be asked to actually Implement mtls because doing it on our own by ourselves could be a lot

**6:26:58** · of work but as soon as we get more information of what will be asked in the Cs we update this section and if you like you can help us with this as well and let us know if you have any ideas about

### Cluster Reset

**6:27:14** · this just a simple reminder that at any point in time you can reset your cluster anytime you like you can delete your instances recreate them and create your cluster again because every new section

**6:27:29** · in this course works with a fresh cluster this doesn't mean that you have to work with a fresh cluster when a new section is coming but if for example something doesn't work for you like the solutions that we provide to you don't work then maybe try to reset and recreate your cluster because every new section is based on a fresh cluster

### Open Policy Agent (OPA)

**6:27:54** · installation it's time for another exciting section and this time we will talk about the OPA the open policy agent which in general is an extension we can install into kubernetes which allows us to write

**6:28:11** · custom policies very customized policies for all our needs let's have a look first we will talk about what the actual Opa is and what the OPA gatekeeper is which we will use after words we will use the OPA gatekeeper to enforce certain labels on certain resources so we will write our own policy and we will also write a policy to regulate or to

**6:28:37** · enforce the pot replica account just some examples for us to get familiar with the allmighty OPA all right let's jump right into it first a little recap if we have the request workflow

**6:28:55** · from all the request hitting the API server then for example with an example request create a new po right so now at first we will go through the authentication step so the API server will ask hey who are you next we will go through the authorization step so we might ask are you allowed to create pods

**6:29:13** · and if the first two stages will be passed then we go to the admission controllers and if we for example have the OPA admission controller enabled then we might have configured a question that will be ask has the PO all required labels and if it has so it will be um applied and if it doesn't then the request will be denied okay and so the OPA plays here as the admission

**6:29:41** · controller so the OPA is an open- Source general purpose policy engine okay and that is important the OPA is not kubernetes specific so the OPA can be used as an general purpose policy agent for various applications but it gains popularity

**6:30:00** · also in kubernetes and it makes definitely sense to use it with kubernetes it offers easy implementation of policies using the so-called Rego language so it's like an specific language for creating policies which we'll test soon it works on the basis of Jon and yaml so that means we will write

**6:30:23** · policies and Force certain things based on Jason and Yo which makes it nice and easy when we work with kubernetes and in kubernetes when installed using the gatekeeper um it uses the admission controller as we said the beginning it hooks into the admission controllers and then every port creation has to pass through the OPA and only if the OPA says yes then it

**6:30:47** · will be allowed and it does not know Concepts like pots or deployments which is yes it only works on the basis of Jason and yo so that's just a little overview and introduction to the OPA and if we now look at the OPA gatekeeper then we can simply say that the OPA gatekeeper uses the open policy agent to make it easier to use with

**6:31:15** · kubernetes okay and it does so by creating custom resource definitions so the OPA gatekeeper will install custom resource definitions if in our cluster which we then can use and create um to easily interact with the OPA which is great and let's have a look at this custom resource definition that the OPA gatekeeper provides so the OPA

**6:31:41** · gatekeeper works with the concept of a constraint template and then a constraint okay so let's have a look at first at a constraint template so here we see we create a resource of kind constraint template and here we call it KS required labels so the idea is that

**6:32:00** · you create a template which is which can generally be used okay so we could say this template can be used to search for necessary labels that's what it can do and then we can create a constraint which actually uses our constraint template okay so if we look at the constraint template up here we see the name is KS required labels which means we can now create a new kubernetes resource of kind KS required

**6:32:31** · labels so by creating a constraint template we actually or Opa gatekeeper in the background actually creates for us a new custom resource definition which we then can use with the kind KS required labels so the constraint is kind of an implementation of a constraint template and this constraint is called Port must have gatekeeper um this could now for example

**6:33:01** · enforce that depost must have a certain label X okay so with the template we gave the general ground base search for necessary labels in some resource and then our actual constraint says okay pots must have label X and we could from

**6:33:21** · that constraint template we could create another implementation for example here we see it's the same kind KS required labels name spaces must have gatekeeper just our name that we gave it and that constraint might for example enforce that namespaces must have label y okay so that's the general idea you will create constraint templates and then you will create constraints which use your constraint

**6:33:53** · template it's time for our first Hands-On session in this section where we will actually install the OPI gatekeeper in our kubernetes cluster so follow me along head to your kubernetes cluster and what we should do at first is we should check if there are no more admission plugins enabled so

**6:34:16** · what we can have a look in the Manifest it it's say kubernetes manifest of the cube API server in there we should see the enable admission plugins we should only have the note restriction one enabled in there there shouldn't be any others if there are for you then remove these and

**6:34:37** · wait for your API server to be restarted after this we can continue and simply install the OPI gatekeeper it's simply yam resources kuber resources that we have to install and in the resources section of this video you actually find the link which you can simply copy and paste and there we go

**6:34:58** · various resources have been created and actually a namespace has also been created gatekeeper system and we also see that there was actually a validating web hook configuration okay what does this mean well let's also have a look in the namespace gatekeeper system and we have a look for pods and services there we actually see the gatekeeper control controller manager and we also see the service gatekeeper web hook service so

**6:35:30** · the validating web hook configuration allows to create an admission plugin if you will so without having to register it with the API server if we shortly head to the kubernetes documentation then we see there's a page Dynamic admission control what are admission web Hooks and there are two types of admission web hooks there is the valid dating admission web Hook and the mutating admission web hook okay so with

**6:35:58** · the admission web hooks it's like an admission controller every P if if you create an web hook your custom web hook like right now Opa keeper created it custom web hook for us if you create one then every port creation will pass through this web hook and kubernetes offers two possible ways of hooking into this system you can create a validating admission web hook which means you only validate a pot um specification so you

**6:36:29** · approve or deny it or you can also create a mutating admission Web book which means you can actually mutate a pot when you create a pot you can for example add some labels to it or if you create a deployment add a minimum replica account something like this right so the OPA works with the validating admission web hook and it works because we can or in a way that we

**6:36:55** · can create custom policies and the OPA will then for us communicate with kubernetes and deny or approve certain parts well and that should be it for this Hands-On session we installed Opa gatekeeper we will now actually create our first simple deny all Opa policy and

**6:37:19** · it's a deny all policy it will deny all ports from being created and we will convert it then into an approve all policy just to get familiar with this at the beginning for this head to your um kuties cluster and what we can

**6:37:34** · have a look at first we installed Opa so we can have a look at custom resource definitions and here we for example see okay we have for example constrainted templates so it's a custom resource definition so what we can do is we can have a look are there any objects of that type right now there are none so the idea again with Opa gatekeeper is you will create a template which can do General things and then you create constraints from that template and this is exactly what we will do now for this

**6:38:05** · head to the link in the resources section of this video which will lead you to our GitHub repository and in there we will have a look at first at the always deny template. yaml so let's have a first look we see that we create

**6:38:23** · a constraint template and it will be of our of the new gatekeeper custom resource definitions we give it a certain name and then down here we actually under the spec the C spec we actually see that we give it a kind KS always deny okay so this here on line

**6:38:42** · nine will actually mean that after we create this template Opa will create a new custom resource definition for us named KS always deny and once that's done we can create resources using KS

**6:38:57** · always deny s kind and here we can actually see that we um give some specifications some properties message type which we then can use in that new resource okay and so this is the template and if we head to the right side then you see there we create a constraint and that constraint is actually of that kind so here kind K is always deny same as here K is always deny we give it some name and we say

**6:39:26** · that this will be actually applied to pots in this case and here we have parameters message and we can pass some message into it okay so this is simply creating a custom resource definition implementation or resource and here we Define and here we actually see properties message type string here we actually Define the custom resource definition that will be created for us so that's all done in the in the back end by the OPA and on the bottom here you

**6:39:58** · actually see there's a Rego section okay and this here is written in the Rego language so the Rego language is a general purpose language for creating policies and it's very simple we see that we have here at the beginning we have a package K is always deny it's like the same name as uh the constraint template and then we have a violation

**6:40:21** · section um that violation section actually receives some parameters like a message and it will then later on actually output that message so important is that line the violation will be thrown so there will will be a violation if all conditions are true so

**6:40:41** · right now we have just one simple condition in there one is larger than zero which means that condition is true there are no more conditions which means the violation will be thrown and all pots will be denied when the PO will be denied it will be denied by throwing that message and that's exactly the message that you see here input parameters message that's exactly the message that we Define here okay if this is all confusing for you it will be more clear for you in a second we will now at first create the

**6:41:14** · template so simply copy the constraint template code and create a new file template.

**6:41:22** · yaml paste it and create it awesome and so we created a constraint template which means now we R if we run K get constraint templates then we actually see there is KS always deny so we now created a template and that template also

**6:41:50** · created a custom resource definition KS always deny for us so what we can do is we can simply say get KS always deny and right now we don't see any resources created yet okay this means but it means that the um custom resource definition has been created there can be objects of type KS always deny now we

**6:42:15** · will create a object of KS always deny simply by copying from the G repository the constraint so I copy the constraint I create a file constraint yl and I create that

**6:42:39** · constraint and now if we say k get KS always deny then we actually see there is our pot always deny so we created a template and we created a constraint that uses the template and the template what we saw should always throw a violation right we have a

**6:43:02** · look again here it should always throw violation one is always larger than zero so let's try it out let's run a pot so we run a simple pot of image engine X and there we see denied by pot always deny which is actually our constraint the message message is access denied admission web hook awesome that looks good now let's

**6:43:31** · change the message okay let's do easy and simple steps so for this we will edit our constraint and we will change the message from access tonight denight to no way or use whatever message you

**6:43:52** · like then we replace the constraint we try again to run a PO and we see the message is now no way okay and this means if you create your template dynamically like here the template we created it dynamically because we didn't hardcode the error message in here right we didn't hardcode it we allowed our constraint to Define

**6:44:23** · the error message and that's how you can create like custom and dynamic dynamic constraint templates uh which you can then use universally for like multiple cases now this works right now now let's also have a look if we can actually describe our custom resource definition okay our constraint so let's have a look at K describe okay it is always

**6:44:59** · deny and our one has the name po always deny we describe it and there's a lot going on so if we scroll a bit up then we see it actually has a status section and the status section is very very good to check because it has a violation section so we see there actually right now 13 total violations okay the OPA will only deny or allow new pot

**6:45:29** · Creations it won't by default it won't go and remove pots running pots in your cluster which are violating okay but imagine you have a running deployment and you restart a node and it will cause

**6:45:45** · some pots to have to be recreated then they will be going through the OPA and might be denied right so it's important if you create a new policy it's important to see okay which running pots will actually be affected so for us right now all running pots will be affected because we simply deny every

**6:46:07** · pot and we see this here in the violation section so in the violation section we actually see that there are like various resources which are running actually some gatekeeper ones themselves and if we scroll down and we actually see that even the API server would be violating against our policy now to finish this section let's change it simply to an approve all policy okay so for this we will edit our

**6:46:37** · template and in the template in the violation section you see one is larger than zero which is true and as I said before to to throw a violation every condition has to be true so let's simply add another condition one is larger than two which is false so we will now never throw a violation Let's test this let's replace the

**6:47:09** · template there we go and let's try to create a pod try to create a simple engine XP it's working amazing and let's describe our CAD is always deny put always deny constraint again and there

**6:47:28** · we go total violations are zero okay so this can be a way of you to getting familiar with it just do simple steps just test with this always deny always allow policy and then describe your constraint and check the violations and see how you

**6:47:51** · go we continue our Opa journey and in this Hands-On session we will create a policy which enforces that all namespaces created have to have the label cks okay for this we should probably clean up our server at first so if we still have on the previous sessions some constraints and some templates we should probably clean them up that's always good so I will delete the constraint and I will delete my template

**6:48:25** · I remove these files and now we can start again there's a link again in your resources section leading to our repository and we will now create actually the example from the namespace label section and let's have a short look through this okay we again create a constraint template on the left we call it KS required label so the idea here is

**6:48:51** · to create a general template which will require labels of objects and then we can use that template for different things and how it works is it again it allows us to pass some parameters we see here actually labels is now a type array so it allows us to pass various labels

**6:49:10** · let's have a look we actually have two implementations here um we have two constraints here so one for all Nam spaces must have cks label and one all pots must have cks label and if we open the pot one at first then we see it looks very similar to the one that we created before and we actually see here kind SPS and then at parameters we don't

**6:49:32** · pass a string now right now we actually pass an array right now an array with one entry with one string and this is exactly the array that we Define here and if we actually open the other file um because in this section we want to enforce all name spaces uh to have a certain label sure you can try the other one as well to enforce it on all pots it would be good if you try it as well but here we see the only difference here is actually the name that we gave it and um that it's now a kind namespace okay so with this we will create a general rule

**6:50:05** · that we can then use for namespaces for PS for labels and just pass some amount of required labels that they have to have otherwise they won't be created okay and if we have a look down here in our new template in the Rego section

**6:50:26** · then it looks a bit bigger right let's have a let's have a look what what's going on here so there's the violation section again and the violation section actually has this on top here and this simply means what will be actually returned as information from the violation so we again have a message

**6:50:44** · that will be returned if restore violation you must provide labels and we now actually pass the labels in that message that has to be provided which is great and then actually some more details about the the missing labels as we see here okay let's let's walk through it shortly so what we do here in line 23 we actually now actually look at the Json resource

**6:51:10** · uh of of whatever we create if we create a namespace then of a namespace okay and we can do this here under input review object so object will now be our namespace and in that namespace we can check the metadata labels okay and this

**6:51:26** · line will actually write all the provided labels of the namespace in provided so here in provided we have all the name spaces of that namespace all the labels of that namespace in required we will actually get all the required labels so we can actually get the input parameters via input parameters labels and this will then be all the labels that we specify here okay so we have the provided labels we have the required labels what we do next is we count so we get all the

**6:51:59** · missing ones okay so missing will be all required minus provided and then if we count how many missing there are then we can create actually our first condition so here we see our first and only condition if that condition is true the violation will be thrown it makes sense right if we count missing if there are any missing if we have more more missing than zero then a violation will be thrown the resource creation will be

**6:52:29** · prevented and the message will be you must provide the certain labels let's go ahead let's create the template at first copy it create a file template.

**6:52:46** · yo and create it do the same for the all NS must have cks so the NS must have cks constraint so create a file constraint yaml and there we go create the

**6:53:14** · constraint as well okay let's have a look at custom resource definition and here we actually see KS required labels our new custom resource definition and if we try to get the objects of KS requir levels then we see namespace must have ckss and as we learned we can describe

**6:53:38** · our resources to see the current violations why right let's do this let's describe KS required labels NS must have cks and and what do we see we actually have a status sometimes we have to wait a little bit for the OPA to actually

**6:54:02** · register our policy and run through all existing resources in the cluster to see the violations and there we go I read a little bit we see total violations five and here we now actually see the message you must provide labeled cks okay so we actually get an array of the labels that

**6:54:22** · that have to be provided and we have five violations and we actually have five Nam spaces okay so every Nam space right now has a violation because it doesn't set the label cks um let's change it let's edit the

**6:54:38** · default namespace and set the namespace or set a label ckss so in the metadata section we can simply type labels ckss amazing okay and we save this and now we have to

**6:54:59** · maybe wait a little bit we describe it again and there we see um the actually the update of that resource um went through the web hook the OPA web hook so every creation every updating every um deletion of um

**6:55:15** · resources in kubernetes will now go through Opa and then have to conform with our policies let's let's try to create a new namespace sh we okay create namespace test denied you must provide labels cks okay it will deny the labor creation

**6:55:37** · let's actually Advance this a little bit let's say namespaces must have the label cks and another label of your choice so we added the constraint and we now actually because we have an array we now actually say must have the um name the label Cs and the label team let's update let's save the file let's replace the constraint there we go

**6:56:03** · let's try to create test again and there we see you must provide labels and then we actually get an array of labels so it's very flexible and nice let's create a positive example right uh we want to try if our policy will actually allow any creation of namespaces so what I do

**6:56:24** · is I will create a simple namespace yaml and in there I'll set the required labels to make Opa happy cks amazing team killer shell all right let's try

**6:56:46** · to create that namespace and there we go namespace created awesome so maybe get a bit familiar with it maybe change it maybe also use our example to enforce Nam spaces on pots so working with namespaces is very simple and yeah should get you started with the OPA

**6:57:11** · gatekeeper in this Hands-On session we will enforce that all deployments have to have a minimum replica account very simple a recreate a deployment which doesn't specify the the minimum replica account it will be denied for this again we should probably clean up so what I will do is I will remove my constraint from before and I will remove my template from

**6:57:41** · before I will also delete the files okay this example um if we had to just open the link that is in the section of this video we are now in the deployment replica count example and let's walk through this also again fast we see that

**6:58:00** · the kind will be K as Min replica account our custom resource definition we now actually will pass an integer and on the right side where we actually see the constraint which will be applied to deployments we actually see that the parameter is a two so we require a minimum of two replicas in our

**6:58:20** · template in the radio section let's walks through it again there we see that we will get provided provided will read the input review object so the object will be our deployment and we will read spec replicas very simple just Json yo based validation then required we will get required from input parameters minimum which will be this and then we do missing is required

**6:58:47** · minus provided it will be already an integer so we can simply have our one and only condition missing has to be larger than zero if missing is larger than zero then we will throw a violation using this message okay let's go ahead and apply the template at

**6:59:16** · first my template has been created and I have the custom resource def definition KS Min replica count now I will create the

**6:59:41** · constraint constraint has been created now we can actually have a look at the objects of our custom resource definition there we go the deployment one and we can actually also describe it as before to see what has been happening

**7:00:02** · and it hasn't been evaluated yet because it's new so it hasn't been evaluated for existing deployments let's give it a second okay in the mean time let's maybe create a deployment let's try to create a deployment let's create a deployment test of image engine X and there we go denied

**7:00:27** · the request um deployment must provide one more replicas okay what can we do well we can generate the yaml and raise the replicas I create a file deploy doyo with the generated deployment I raas the replica to two and that should be it create the

**7:01:02** · deployment deployment has been created great let's run our describe commment again and there we actually see we have two violations so the violations will now be for existing deployments and we actually only have two violations in our cluster which means um for example that we have a deployment in namespace gatekeeper system and also gatekeeper controller manager because we require

**7:01:29** · one more replica so yeah that should be it for this section we saw how we can create a policy to enforce a minimum replica count on deployments I would like to show you now the Rego playground so the Rego playground is a place where you can actually write your policy code in Rego and test it very handy very nice I would also like to show you uh one more page actually GitHub repository with more gatekeeper policy examples where you can

**7:02:02** · investigate a little bit so the links that I show you now are in the resources section of this video as always and first thing the GitHub repository gatekeeper policies there are some examples where you can look through and get some ideas and there's for example one required namespace template so this is a template creating a kind KS required namespace and it actually requires so the object would will be passed um into that Rego

**7:02:32** · here we see the object can be can be a pot can be a deployment we actually inspect the metadata namespace we say the namespace has to be default otherwise you must or the namespace cannot be default um and otherwise develop violation will be thrown you must provide the namespace other than default which is a very nice policy I like that policy if you have a large cluster preventing people from creating resources in the default namespace can

**7:03:00** · keep things more clean second thing I would like to show you is the Rego playground okay and in Rego playground on the left you will write your Rego policy and then you can evaluate it with some input that you pass here there are already some kubernetes examples so we can scroll down and for example look at the hello world example and evaluate the one okay

**7:03:27** · and what we see here is actually an admission review will always be passed into Opa and then there's a request and there's a pot okay so this is now the kubernetes pot specification um in yamel declaration that we see here we have metad dat spec and let's have a look what does it do cost center code must start with CC code found fake code so this is about the labels we here it checks the labels and cost center so let's simply change this

**7:03:57** · to test and test and we see everything is fine no violation let's have a look at another example there's a nice one about image safety okay so also let's evaluate this one and there we see denied image MySQL comes from untrusted registry so what does this actually do we see we will check the spec um of all containers we check the image and then if the image

**7:04:25** · doesn't start with julie.com we will actually say image has to come from untrust or image comes from untrusted registry okay so right now from julie.com engine X here but he will see MySQL doesn't come from there okay so what we can do let's say what if you write okay it it should come from docka doio okay image docka musale comes from untrusted registry okay so if we write

**7:04:54** · pie.com then we see everything is fine okay let's change this back to docker.io and we have a violation again what we can do here as we learned a violation so this block is kind of like the violation block that we create in the OPA gatekeeper okay and everything in here should be the same as in gatekeeper so we see here there one condition not start with holly.com we we learned that a violation will be thrown when all the

**7:05:26** · conditions are true okay so it doesn't start with julie.com it doesn't start with docker.io which means we now allow jul.com docker.io but if we now say other. then we see comes from untrusted registry okay so this is a way to Simply create a policy to enforce s but image

**7:05:56** · Registries we reach the end of this section and there's a nice talk that I would like to show you if you have time and interest to dive a bit more deeper into it it actually gives you a nice overview about Opa policing your kubernetes clusters with open policy agent link is in the resources

**7:06:15** · section well we talked about Opa in general and I gave you an overview and maybe you should know that it might have to be pronounced Opa so some people pronounce it Opa some Opa I couldn't pronounce it Opa for now because it reminds me too much of the German word um Opa which means grandpa but yeah Opa

**7:06:36** · I call it Opa for now but once the pressure will be too hard from from you guys uh then I'll definitely change my pronunciation as well so we talked about Opa and we used the OPA gatekeeper custom resource def defs installed them in Artic cluster we created templates and constraints went through some examples and we got familiar with the Rego language and we actually also

**7:07:02** · checked out the Rego playground when it comes to the actual certification um yeah you never really know what will be asked of you but being comfortable with Opa and gatekeeper should be should be good and knowing about the web hog validating admission controllers admission controllers in general is a good idea but I mean you don't have to be a Rego writing expert right this is not what the um certification will be

### Supply Chain Security - Image Footprint

**7:07:33** · about in this section we will talk about Docker containers and their image footprint and for this we will jump right into containers and Docker and how they are built and how they work afterwards we will actually reduce the image footprint of a Docker container and we will also build a multistage build and finally we will secure our

**7:07:57** · Docker image according to the security best practices which you should know for the cks first let's talk about the difference between virtual machines and containers real short well we start with a host operating system we have a kernel on that we have a simulated operating system with its own kernel which then finally runs our application process if

**7:08:23** · we look how containers work it works a bit different we also start with a host operating system and the host kernel but on that host kernel there could already our process running or if we like to run it inside a container the process is simply wrapped into a kernel group and well the main difference you see on the left we only have one kernel and yes that kernel can access the app process inside that Docker container or

**7:08:50** · container in general very simple so it's a direct communication between the one kernel and the application process and if we look at the virtual machines then that host kernel cannot easily directly access the app process so the app process here can't communicate directly with the host

**7:09:11** · kernel and for containers well if we have one container we can have two containers we can have three containers and then all these app processes can't see each other by default because they're wrapped in kernel groups so they are like simulated they have like a simulated abstraction layer and but they all run on the same kernel on the same host kernel of the same host operating

**7:09:38** · system so how are containers built and especially Docker containers so Docker containers are built in layers okay you can have one or multiple layers and they all add up on each other so if if we now have a container which might have a base image as a layer then another image as a layer and then maybe some some tools that we installed and so on you know so

**7:10:02** · you can add many layers to a Docker container and it would then grow after while and they would all um add up on each other and let's have a look what these layers could mean here we have a very simple Docker container okay so we start with a BAS image we start with yuntu and then we actually run appg to

**7:10:27** · install in this case goang application and finally we execute a command so the first line from would does actually mean that we import existing layers not just one layer like we import many layers depending how many layers are in our base Ubuntu image and here we actually add a new layer with the Run command and if we have a look um from the docker documentation only the instructions run copy and add will create layers other

**7:10:59** · instructions create temporary intermediate images and do not increase the size of the build okay so in this case we will import layers as how many layers as the Ubuntu image has and then we actually add one new layer on top this is like one line that we add here so how can we reduce the the image

**7:11:22** · footprint and what what does it mean well let's say we have our image here and the only thing we do in our image is actually we will install curl okay so our image is about installing curl but we can't just use Curl without anything we have to have some kind of a base image so we would use a base image let's say engine X we use engine X as a base image but engine X itself might also

**7:11:46** · have a base image like if you create a Docker container you can start from scratch but most of the time you will start not from scratch with a base like we here we start not from scratch we start with engine X as a base and engine X itself might use Dean as a base and

**7:12:02** · the end size of our image will add up so the end size of our image will be the base image size plus the dpace image size plus whatever we installed on further layers and yeah in the Hands-On sessions we will actually see this in action

**7:12:24** · I hope you're ready because in this Hands-On section we will build our first Docker container maybe not your first in general but definitely the first one in this section we will actually look at an example goang Docker file and then we will reduce the image footprint by using a multi-stage build for this we should

**7:12:43** · have access to our favorite kubernetes cluster and please head to the link in the resources section there we will see our GitHub repository with our image foodprint sources and there's a Docker file so please copy the docker file content to your master note and do the very same for the very complex app

**7:13:19** · Dogo so on my master note I have my Docker file and I have the app. go well what can I do and what can you do to actually build the container or first let's have a look in the container what it actually does so it's a very simple one what we do is we base it on your buntu um we install an additional package go Lang go and then we actually copy the source code into the Container

**7:13:49** · which is only one file so so we just copy the app. go into the container and then we actually run the go build which will create an binary file which we then run okay let's try it out so what we can do is Docker build and we want to name our container app and our Docker file is in the local directory so we write a

**7:14:19** · DOT okay and here we can see what we saw in theory before pulling from library Ubuntu we so it's actually pulling a lot of layers down and then it's installing here we see our additional command it runs an update and um installs go and go and then we go further down and there we go it's installing actually go L

**7:14:57** · 113 my build has finished there we see successfully taged app latest well let's try it out let's run our container Docker run app and there we see all our app. go actually does is a y Loop which

**7:15:14** · always output the username root and the user ID zero great let's have a let's have a look at the size of our container right so what you guess what that size of that easy simple Loop is which simply outputs user information well it must be very small right let's have a look Docker image list we grab for our app container and there we see yes it's very small it's just 700 megabyte large and if we would

**7:15:45** · now like to distribute this container then yes everyone who likes it it could be everyone who likes to run it like for example kubernetes node um has to download all these layers you know unless they're already downloaded by some other container but this is definitely not a light white and nice image size well as our task says we

**7:16:06** · should reduce the image footprint via a multi-stage build let's do just this for this we will edit our Docker file and well what we now want to do is that we we don't don't want to change much of this because we just say Okay this whole section on top this will build our our

**7:16:29** · app executable right using goang so it will be our compiling our building container so what we can say is hey we want to only build that app executable

**7:16:44** · up here and then we actually want to have another container which simply executes it because it's executable and that's nice with with goang you know so what we can actually do is we can add another from section and we say for example from Alpine so Alpine is very much light white um it's it has less packages and everything around and it's very um small compared to yuntu so we can say from Alpine and then as we had here the copy command we copy a file a

**7:17:16** · local file from our local folder into the Container right what we can also do with copy is we can say copy from zero to Let's say/ app so this means that we actually copy from another stage from the stage zero

**7:17:36** · so this from section will start the first stage stage zero and this will start the second stage stage one or it will be our last stage actually so this will copy from our stage one the file slash app to the local

**7:17:57** · directory okay and what we do then is we simply execute it and what will happen is that actually the image the resulting image will always only contain the last stage so in

**7:18:14** · this case yes we will build at first this whole stage up here but once we build we start with the build here then this will only be in our um resulting image let's have a look how this works we will actually run our build command

**7:18:34** · again and there we see okay we didn't have to pull a lot because yuntu we still had in cash but we had to pull Alpine and we had to do some things okay let's try to run the container again there we see okay it runs just as before and if we have a look at the image

**7:18:56** · size and we see now it's actually 7 megabyte and it does the very same thing okay so it's it's very simple multi-stage build are very nice to yeah get rid of all the baggage that you might need for building and initialization to be left with a resulting container which is very small and can be very easily distributed

**7:19:23** · we already reduced the size of our image by a lot which is great now we'll look into securing and hardening our image and for this we will do four different things we'll start with using specific package versions if we head to our image then we see right now for Alpine so in our last build we actually see that there's no teex specified which means it

**7:19:49** · will always use the latest tech and that one can always be overwritten with any kind of version it is not really secure to do it like this for this we can for example head to Docker Hub search for Alpine and search for the releases and here just take any release itex

**7:20:09** · 3121 edit Here and Now Alpine should have a specific package version we could do it also for yuntu it should also be good to do it for yuntu and and for example here as well if you use any package manager to install package version you should always install proper versions why it's very reliable right like if at any point in three months you have to rebuild your container fast in

**7:20:33** · some pipeline to push it out and the container doesn't work because suddenly New Image versions will be pulled that's not good your container should always work and should always be able to re rebuild then if you have built your container and it's in your registry you should have other third party tools which search your containers for used image versions for example Alpine 3121

**7:20:57** · and if in the future Alpine 321 will have a security issue then we will be notified and then we go into the container and change it that's the workflow right but we shouldn't have to uh change the versions and find working versions at any time when we just want to build our container so let's build the thing and rerun it again again see if everything still works everything still works great we use specific package

**7:21:27** · versions don't run as root okay it's a good idea to don't run as root because if someone breaks out of our app process at least that person is not directly root so for this yeah the the solutions

**7:21:43** · are as as well in the resources section or GA repository so what you can do is like from there you can actually copy also the comment that I will write here now so what we do is a run comment and we simply do an add group so this is now line specific it depends like on the distribution where you based on so we add a group and we then it we call it app Group we will also add a new user we call it app user assign it to

**7:22:13** · the group app group with the home directory home app user and then then instead of copying to the local directory or to the current directory we can actually copy to the home app user directory so the bin file the executable will be in there and there we go okay so what we do

**7:22:36** · here now is here we add a new comment uh we add a new group and we add a new user and then we actually can use it so we specify user app user and from here on from that

**7:22:52** · line on everything else will be executed as this user so this process will then be running as the app user okay don't worry you won't have to write something like this yourself you know it's a kubernetes certification you don't have to be like that distribution specific but things like this you should know how to use a user and how um yeah to make the processes then run as the user let's build it let's run it and there we see it now runs as app user with the ID 100

**7:23:23** · and not as root user with the ID zero anymore don't run as root we did it make file system read only this is also great you can also do this in kubernetes right make your file system read only we learned about this like using security context but if you have already your Docker image hardened it's it's it's way better than than doing it um Justus in kubernetes it's it's good to do it the stage earlier so what you can do very simple what you do for example we could say that we change and we

**7:23:57** · remove the um the read or actually the writing permissions for/ Etc you know so you could now say you could now identify all directories that don't have to be written you know for example if you have an engine X running and it serves some HTML Pages then these HTML patches don't

**7:24:15** · have to be um writable they only have to be readable this means someone malicious who hacks into the Container can't easily change the HTML code that sered to other users for example but we now will simply remove the writing conditions for all users um from the/ ITC directory and we build great and we run and what we now actually can do we can do run minus D so

**7:24:45** · what we do here with Docker run minus D is we will run our app process in the background there we go and we actually get an ID that it's running and then we can actually say we would like to exec into that container and get a shell there we go and if we do an

**7:25:06** · LS then we actually see that/ ITC has the writing permissions removed okay so this will be a way how you can make um the file system read only

**7:25:22** · remove shell access well this is also a thing um if someone breaks into your container and there are already tools like shells and curl um with with with which you can like I don't know do further breakings and contact contact other services Etc then this might be good for intruders but it might not be good for the security of the container so what we could do is we could remove shell access let's have a look how would we do this well what we could do is up here as well

**7:25:54** · we could simply say um we could simply execute another run comand and it could be as simple as now simply removing the whole bin directory okay so we simply run RM RF bin directory let's have a

**7:26:11** · look what that does we build and there we go no such file or direct directory unknown so it seems to still need this yes it makes sense I mean what we do here is we delete everything from bin directory and here we see that we actually use something from the bin directory so what we should do is we should actually switch this and say that

**7:26:42** · after we used all the binaries that we need to build our container to set up everything um we could then say that afterwards we will remove everything let's give this a try that looks better um let's see if

**7:26:59** · everything still runs because that's important right we want to distribute our app our app still runs right what if we want to run our app again in the background there we go and if we now try to exit into our app using shell and we see hey there there's actually no shell there's actually no bash because we deleted everything okay so we did a few things to secure and Harden our

**7:27:32** · container we reach the end of another section now I would like to show you the docker best practices and I would really suggest to you to read through few of these at least um you will feel much more comfortable afterwards but we did also the main things in this course so if you know what we did you should be fine in the certification but if you had to best practices for writing Docker files link is also in the description

**7:27:59** · then you see various things you see for example multi-stage builds as we had um we see minimizing the number of of layers and it describes when the layer is created um it writes about the from and

**7:28:16** · that they also recommend using an Alpine image for example and they also write something nice yeah for example you always see run app get update and install in one layer so one

**7:28:32** · layer means one one line you know you have one run line you don't have one run update and then another run line install this is because they will be both in one layer and otherwise it could be that your update one is in a different layer than the install one and the install one would then always depend on an or could always depend on an outdated update layer might be difficult but they describe it here as well if you're interested it's very interesting you can uh read through it well um and what they

**7:29:06** · also write about is for example the user section that you should execute processes as a user so yeah we talked about reducing the image footprint we used actually also multistage builds and we secured images using various

### Supply Chain Security - Static Analysis

**7:29:37** · restrictions static analysis of user workloads a new section that we start today and yes before you're wondering I'm on my holiday there's the beach there's the ocean behind me but but even if I'm on holiday I will still record the videos for you no worries you can even hear the ocean if you're quiet okay if it's not the case then it might be because my microphone only picks up my voice my good microphone

**7:30:03** · okay let's jump right into the topics what we will talk about we will talk about static analysis what it is where is it used then we talk about a manual approach of Performing static analysis which you might have to do in the cks and we talk about tools for kubernetes and scenarios which might also be helpful in the exam static analysis what it is about so we could say in generally that static analysis looks at the source code and text files so it doesn't load binaries

**7:30:35** · and then performs like functional test on these it only looks at the source code and text files and passes them and then checks against certain rules maybe there are already like some provided Rules by a community collaboration but maybe it's simply our own rules that we write and then we can enforce these rules and this could mean that we stop our continuous integration pipeline we throw errors

**7:31:02** · Etc so what could be static analysis rules well for example it could be always Define resource request and limits and if our pot doesn't Define some then we won't deploy it or pots should never use the default service account and if they do then we will throw an error or we even don't deploy it at all so the rules depend on the use case

**7:31:27** · company and project right you can decide it in your company in your project you can decide what kind of rules should we have and how should we enforce them but in generally it should be said that it's never a good idea to store sensitive um information plain text in the cuetes yam files or in Docker files

**7:31:47** · themselves so let's have a look at a continuous integration Pipeline and where static analysis would fit in there so let's say we have some code we develop code probably on our local machine we write code then we commit the code and we probably push it into our git repository afterwards some build processes will start to run we might execute some tests and afterwards we deploy it and where do we deploy exactly

**7:32:17** · in our favorite containerization system called kubernetes so where could we do static analysis well we could actually do it at various points so we could for example do it here right so before we commit or even after we commit our code um we could have like local GI hooks which prevent us from pushing or prevent us even from committing if some certain static analysis rules haven't met we could do it here we can also do it maybe

**7:32:48** · before we build let's say at this point we have a Docker file and we want to build our containers our images um we could do static analysis of our Docker files and then even prevent the build or we could do it after the build in like a test phase like maybe we don't even have a build phase if this is a pipeline which only compiles kubernetes documents and deploys them then we might not even have a real build phase so we could do it like with the test phase and yeah so at these places we could probably do static analysis using different tools so

**7:33:22** · we also talk in this course about for example pot security policies and the Opa Opa and with the OPA what we learned we also can do some kind of static analysis because we Define rules which are based on Jason and yaml right it only looks at Jason and yaml so it only looks at the text files and then makes decisions of it um and the OPA actually provides like

**7:33:47** · a like a config tool which you can use just like this for static analysis in your pipeline and we will actually use this later but if you are PSP or your Opa runs admission controllers in kubernetes then it's not really considered static analysis anymore it's like it needs the binaries it needs the ecosystem of kubernetes to run but yeah in general it's a good idea to enforce your rules using static analysis early in your pipeline and also enforce it um

**7:34:20** · live functional in kubernetes using maybe Opa or PSPs to ensure that if something got deployed um and which didn't go through the pipeline then your rules will be still

**7:34:35** · enforced so let's have a look at some manual checks let's do a manual static analysis okay maybe pause the video have a look at that PO declaration and say if you see that there are something wrong well yes I see there's something wrong we run a command and we actually call some service and we pass the token and the tokens directly here okay so it's like a hardcoded token in our yamel file

**7:35:03** · not too good let's have a look at that one maybe pause again for a second and see what you say about this one does it look better well it might look better right we don't use the token directly here the hardcoded token but well well we we

**7:35:20** · still set an environment variable with a hardcoded token value which is our credential information right here what should we do what can we do better well have a look at that one how does that look maybe we pause the video again check this out it looks much better right we set the environment variable token we Ed the token here and well it

**7:35:43** · comes from a config map so I would say to this one as well it's better but no because we should probably use a secret here for storing our secret information like this I switch to the secret mode and this looks better um we use the token which comes mounted from a secret because a secret can be stored more secure than config Maps it might not be the case depending on how the cluster is set up but secrets are made for credentials and can be stored encrypted

**7:36:15** · so these are like some little things that you should look at should be able to identify when you look at kubernetes yo files or also Docker files there shouldn't be any secrets or tokens obviously hardcoded in

**7:36:32** · these and we will now talk about cubc on cub. cubc can offer us risk analysis for kubernetes resources it is open source it is opinionated which means in this case it actually only checks against a fixed set of rules which come from the security best practices for kubernetes and it can run in various ways as binary Docker container cbec Plugin or even later in our cluster as

**7:37:02** · admission controller there is a cuac web hook well cubc let's have a look if we head to the website cub. they even have like a live demo function and let's have a look we have like a very simple um kubernetes Port declaration here submit this yaml to cubc okay let's try it out

**7:37:24** · there we go we get some Json back and we actually see we have a score of one so it's like scoring base the higher the score the better we pass with a score of one points and we see we have one past rule so we got one point why um security

**7:37:41** · context read only file system okay so we set a read only file system great but there are like many things that it's still advised you know for example example um a service account name there we go we could set a service account name let's do this I head back to the example and what I can do service

**7:38:01** · account name not default let's run this again and what do we see additional Property Service account name is not allowed well I do it

**7:38:18** · in the container level and it should be on pot level you probably have noticed this there we go and suddenly we have a passing score of four and we see we get three points for setting a different service account and we see there are like various um preconfigured rules so it can be very nice and we will have a look at this also in the next Hands-On

**7:38:43** · session we will now use cubec ourselves on our master to perform static analysis on a simple pot which we will create and we will actually use the cuback public Docker image for this the link to it or the comment that you have to execute is also in the resources section of this video but first let's create a simple pot let's create a simple engine xport we only want the yaml of it though so we do a dry run and we pass it I pass it in a pot.

**7:39:16** · yaml file and have a a look what has been generated a beautiful simple engine export well now we would like to test it what's wrong with this pot according to cubec for this you can either head to the link in the resources section and run the docker run comand um it's also on the GitHub repository of cubc there's a comand um where where it says how you can run it just using Docker very simple very easy so do this

**7:39:49** · but. yo and yeah so what do we do we simply run cuback with a specific Tech version we do scan and ReRe from standard input which will be our pot. yo and there we go Jason returned various advice rules and we see a score of zero

**7:40:09** · we passed well nice we passed that's good though with a score of zero let's see if we can change this okay what could we do well let's have a look what could we do um security context run as nonroot okay let's set this we could do we change our pot and for the container we set a security context run as

**7:40:39** · nonroot which is very good because it forces that the container that we're running engine X will actually be run at nonroot or that we Define this as well using a security context setting to set

**7:40:55** · the actual user so we run the cube SEC comment again and let's have a look we still have a score of zero well that's not nice let me have a look what might have been done wrong security context run as nonroad right and the thing is uh

**7:41:15** · it only performs it was a great example it was not planned so it only performs static analysis right it doesn't um L like kubernetes binaries to pass the yaml if it's like proper yaml if we would have tried to apply this yaml with not rote it would have been denied by kubernetes right but because it only performs static analysis it's kind of dumb in a sense and only checks um for what it checks and not like for proper kubernetes syntax let's try this again

**7:41:46** · and here we see we now pass with a score of one and it doesn't suggest anymore to use the nonroot well you know how to use cubec if you have to and you will be provided with the comment how to run it or it will be already installed on your terminal and then it's up to you to fix some of the suggestions we will now have a look at conest from Opa the open policy agent so

**7:42:17** · we used Opa or Opa already in combination with gatekeeper in our kubernetes where had hooked into the admission controller Web Box and there we actually denied or allowed the creation of various kubernetes resources based on our custom rules that we wrote

**7:42:36** · so the open policy agent is definitely very powerful but it also provides a tool the con test which is a simple binary that we can run to unit test our kubernets configurations like as part of our static analysis anywhere in our pipeline or even simply locally before we even push our code into our repository it

**7:43:00** · uses the same Rego language as it does in combination with gatekeeper or in kubernetes and it would could look something like this right input kind we have a deployment and we check the spec and the spec of the pot is there a security context run as non-root and

**7:43:18** · then we say containers must run as non- rot so we would enforce this this is a very nice tool in combination you can use it for static analysis um before and then you can use Opa actually with admission controllers in your cluster and then you have guarantee of enforcing your policies and let's have a look at contest in the next Hands-On

**7:43:41** · session in this Hands-On session you will actually use con test to check a kubernetes ex example yaml file against certain rules and we'll do it together but follow me along you should have

**7:43:56** · access to your master note and we now actually have to check out the git repository of our course the comment that you can run is in the resources section or you can follow me along and just head to github.com killer shell ckss C environment and then to check out the code I copy the URL get clone repository there we go and now

**7:44:23** · we can have a look in CK C environment course content supply chain security and static analysis and in there is actually a folder for con test in there we see Docker and kubernetes two simple examples we will now actually check the kubernetes example and there we see three files

**7:44:48** · okay let's have a look at the deployment. yo so that's a very simple deployment that you see here nothing special about it just generated has all the necessary labels and that's about it okay and we would like to check this now for maybe any um mistakes based on our custom rules and our custom rules are actually in the policy folder and in there we have deployment.

**7:45:11** · Rego and here we see that's our favorite policy language Rego we have two rules first rule first rule checks at deployments and then the input we check at the deployments back and the pots spec and we check if the pots spec has a security context run as nonroot set otherwise we say containers must run as non root must not run as root the second policy is

**7:45:39** · input kind deployment um we check for the labels app and we say okay the app label has to be set for pot select well then there's a file runsh which is which contains the simple

**7:45:56** · comment you can run so you can just execute the script or you run that comment and what we simply do is a Docker run in our current directory and um we will actually run conf test con test with the common test and then our deploy doyo so let's have a look the image will be loaded and there we see two two tests one pass one failure okay what's the message containers must run must not run as root

**7:46:27** · okay let's try to change this so let's edit the deployment. yo and let's say that on the pot level we will actually say we will now add a security context with run s nonroot to

**7:46:46** · true and let's execute the commment again and there we go to pass right and let have a look at our policy file again and there we see okay um it actually requires us also to have the app label Why didn't it say anything about pot must provide app label for pot selectors well let's have a look at our deployment file and then we see okay we already have the app labels for the selector so

**7:47:18** · what we could do we could change this to test okay we change it to test we run the conf test again and there we see it fails containers must provide app label for Port selectors okay so this way you would now if you have to run conf test if there's like a simple Rego file that you have to run you would know how to change the kubernetes yaml file

**7:47:43** · accordingly so that the rules will pass great we will now continue with our conf test journey and do some static analysis on a Docker file well for this we head back

**7:47:59** · to our Master note and we checked out we cloned our course repository and we already had a look at the kubernetes folder now we have a look at the docker folder what do we see in there well we have a Docker file let's have a look at the docker file simple basic always used

**7:48:19** · example Docker file to build and run a goang application it will be a very large container because of the Ubuntu base image but anyway this should not matter right now we only do static analysis we are not building any container let's have a look in the policy folder we actually see there's

**7:48:41** · one base and there we actually see a deny list we have array okay we deny yuntu and we have a look we have actually a look in the docker file at the comment from okay when the comment is from in the docker file so we look at the from section in a Docker file and then we check if that list contains anything from our deny list so yuntu then we say unallowed image found makes sense we will forbid um to write from

**7:49:14** · yuntu and let's have a look in the comments section section so in the comment section we also have a deny list again and we actually check okay if the comment is now run so um doer run and then we check if it contains anything of our deny list then we say unallowed comments found okay simple

**7:49:36** · rules but powerful to use let's have a look there's also a runsh again which we can simply run and there we see two tests two failur okay let's have a look unallowed image found yuntu let's fix this let's go into the docker file and say okay we don't use

**7:49:56** · yuntu we use Alpine and again this right now would not work because EPG you can't use this with alpine right but we are not running Docker we are not testing the docker image we are not building the docker image we only performing static analysis

**7:50:13** · which means this should work now two tests one past one failer this looks better unallowed comments found okay app get installed there's an unallowed comment found let's have a look in the policy again for comments um we are not allowed to use any app to install any packages okay well actually

**7:50:37** · what we could do now we could say well maybe we want to allow this okay we want to allow appt so now we change the policy and see that the new policy will be applied if we run this again and there we see um two tests two pass so if you would have to run confest against a kubernetes file against a Docker file then the command will be provided for you and you would have then to fix based on the static analysis results you have to fix whatever has been

**7:51:11** · returned and to end this section maybe you want to play a bit again with Rego the policy language um the example that we that we gave you for Docker and kubernetes play around with these a little bit maybe don't use them on the deployment use them on a namespace and check what's happening but yeah and in the end you will perform a kubernetes certification which means you don't have to be a Rego programming language expert

**7:51:38** · just saying it like this what do we talk about well we talked about static analysis what it is in general and we talked about the manual approach so with the manual approach you should be able to look at yo files from kubernetes and identify okay this is not according to the kubernetes best practices security best practices same for Docker files you should look at a Docker file and see this is not according to the docker file

**7:52:04** · best practices security best practices okay and then you might have to run certain tools like cubc like conf test maybe even others but in the end you will be provided with a comment to run and then you have to interpretate the result and change the yamel files according so that they are more secure and more according to certain

### Supply Chain Security - Image Vulnerability Scanning

**7:52:39** · rules welcome back to another holiday edition I'm still on my favorite Beach but this doesn't stop me from talking to you about scanning images for noun vulnerabilities we will get a little introduction into what the topic means we talk about vulnerabilities in our images and also in dependencies and then we talk about tools that we can use to scan for vulnerabilities in

**7:53:06** · images let's Jump Right In image vulnerabilities what does this mean well image vulnerabilities I mean vulnerabilities could be in almost every application like in web servers uh running in our containers for example and vulnerabilities could for example be buffer overflows like famous one right where if you have an Apache running and that version is um exploitable by buffer overflow then you might you can send a specific request to that Apache service

**7:53:36** · and instead of just serving HTML it might do something else it might execute a comment on This Server it might create a new file on the server right and you can or people can then use this to write exploits so what could be the targets of

**7:53:52** · these vulnerabilities or exploits well any remotely accessible application in the container but also local application which are just installed in the container just any binaries that come with your base image uh if you have your base image your bundu and it comes with a lot of packages there could be security um vulnerabilities in any of

**7:54:11** · the installed dependencies so these could be the targets of this and the results could be well results could be for example privilege escalation information leak denial of service and various others so definitely something that's not good that we should look out for well let's have a look at Docker containers and at the layering of these and yeah we now Docker containers are built in layers and they are all stacked on top of each other and if we now say

**7:54:41** · Okay layer six that our custom layer we have a very simple Docker file which simply installs curl in a specific version in our layer six then well yeah curl in that version could have a security vulnerability but if we base our image of for example engine X in a specific version then also that engine X um in layer 4 which is our base image could

**7:55:05** · contain vulnerabilities and if that engine X is based on Ubuntu let's say in version 14 then Ubuntu itself could have vulnerabilities or like all the packages that yuntu comes with could have some so if we scan for vulnerabilities then we have to have tools which have a big database of noun vulnerabilities and which can actually scan all the binaries in our containers in all the

**7:55:31** · layers so non image vulnerabilities there are databases um just two examples here which collectively um gather information provide them release them and make known about these which is really great and then there are tools which use these databases and can simply scan various um binaries for their versions and then they know okay this version is known to have a vulnerability so the tool will output that there's a warning that there's an error something like this vulnerabilities can be discovered in our images and in our dependencies

**7:56:04** · and this can could for example be done doing the build like let's say we want to build our image and then we run a scanning tool which will maybe prevent the build if it finds vulnerabilities in the dependencies that we install or we could check this also at runtime right if our cluster is running with various pots and we want to check if maybe something from yesterday to today a new vulnerability was known in some of the images in some of the versions that we are running in our

**7:56:34** · cluster so if we have a look at uh continuous integration pipeline then we could write code we will commit it into we will push it into a repository we will build our Docker containers we test the containers maybe and we deploy these in our favorite contain containerization system um Dockers SW or maybe

**7:56:57** · kubernetes and well so where could we scan for non vulnerabilities well we could do it when we write our Docker files locally we could already do it there we could do it when we build in our pipeline our Docker files we could prevent the build there or at least output some warnings um we could also do it with when we deploy or before we

**7:57:19** · deploy our kubernetes yamel declaration we could check the images so there are different places where we could do it in our continuous integration pipeline but it's also possible to enforce certain Registries certain container Registries just say Okay docker.io is good this doio is not good

**7:57:39** · so we could restrict certain Registries for example using Opa or maybe using other admission controllers we could also extend this to certain images so we could use something like the OPA open policy agent to enforce or to deny

**7:57:56** · certain image versions um running in our kuber netics cluster and if we would like to do this at this point like live in our cluster then we could have a look at where this would be possible like this would be possible at for example the mutating web

**7:58:11** · hooks or the validating web hooks like if we have a request coming into the API and we go through authorization and authentication then we go into the admission controllers and there we have the mutating mutating admission and the validating admission web hook into which tools could for example hook and then prevent or even mutate some some image

**7:58:37** · versions but if we go back to the pipeline well if we have a pipeline it might make more sense um to check the images for non vulnerabilities at a different place right so if we have a pipeline then usually we build our Docker containers and usually we push these into a Docker registry of our choice a container registry and then it makes sense to outside of the continuous

**7:59:04** · integration outside of our pipeline to actually constantly check our images for non vulnerability so we will have our all our images in our registry and we constantly check that registry using different tools and that way we could

**7:59:20** · then send some alerts to like a team and say hey there are like now some non vulnerabilities and that in that image and then that team can go fix the image and then run through the pipeline again to deploy so this might be another good way on how to handle the con constant image scanning for

**7:59:44** · vulnerabilities we will talk now about two example tools that can be used for scanning one is CLA some facts about CLA it is an open source project it can perform static analysis of vulnerabilities in application containers just what we want it can adest vulnerability metadata from configured set of sources like these databases that collect the vulnerabilities that we talked about that is great and it provides an API so

**8:00:14** · CLA is definitely flexible it can be adjusted and greatly integrated in various systems but it's also a bit complex to set up it's not run command a one commment run everything works another one is trivy and trivy is also an open source project and it describes itself as a simple and comprehensive vulnerability scanner for containers and others and well it is

**8:00:40** · simple easy and fast as it says about itself as well and it is actually one command run all which we will see in the next Hands-On session in this Hands-On session we will now use trivy to check some public images and also to check our Cube API server image we will execute and run this on our Master note and we simply use Docker the comment for this is in the resources section and I will

**8:01:12** · actually head to the GitHub repository of trivy and when we scroll down there should be a Docker command from the quick start Docker and uh there we go they actually host it also on GitHub so we can simply do Docker run

**8:01:35** · prvy there we go and there we see we can pass some arguments let's say image and then engine X which means we would like to scan the image engine X for non abilities it will contact databases and download whatever is needed and there we go looks pretty crazy right now so sorry

**8:01:57** · for this but I have to reduce the font size you can't read this I'm sorry but we need to display that nice table properly so here we see various things on the left side we see the libraries like lip system D um there is lip SSL and then the um severity of it like low high medium and then we also see the ID

**8:02:21** · like cve and some number and there like various ones so what we see we see 100 11 Low 11 medium 25 High one critical interesting let's find the critical

**8:02:44** · one there we go Sam in in the library so this number the cve um you could also simply search for it and then then you find the result in some of the databases and then you actually see a proper description of it um of what it of what it does so that's

**8:03:05** · the general idea of image scanning with trivy and we can now for example say okay that engine X image seems to have a lot of n vulnerabilities but what about a specific version let's say 116 and then Alpine let's check for

**8:03:21** · Alpine so engine X 116 Alpine and there we see that looks less critical right we only have three medium ones five high Ones Still and what about I don't know is 119 still out let's check 118

**8:03:39** · Alpine and there we see um yeah we only have one non High vulnerability in there right now now let's go to our Cube API server and let's check um the image version which is running in there so I search for the API

**8:04:04** · server there we go and we would like to have the image version and there we go it's hosted on GCR and I'm using 11 193 it might be a different one for

**8:04:24** · you so let's have a look what it says about this one and there we go nothing known here what about an earlier one we could for example try

**8:04:44** · 117 unable to be found must probably be specific version let's try 1170 and there we go so in that one there are already like non vulnerabilities but in the one that we are running right now there were at least none I mean that's all about using trivy for scanning public images or images running inside your kubernetes

**8:05:12** · cluster and we reach the end of this section we talked about vulnerabilities in general what they mean why they're bad we talked about dependencies and there can be vulnerabilities in dependencies so if we base our image of

**8:05:27** · a large base like Ubuntu there's much more possibilities for viabilities because there are a large amount of dependencies we talked about public databases which collect and provide information about vulnerabilities and we talked about tools like CLA and trivy and we actually use trivy to scan and in

**8:05:48** · the certification well you should be comfortable with running a tool on command line you will be provided with the tool it will be pre-installed and pre-configured as well and then you have to do something with the result you have to interpret the result and maybe fix some existing images um change the package version of a vulnerable image to another one or remove some pots which run vulnerable images

### Supply Chain Security - Secure Supply Chain

**8:06:28** · we should talk about our supply chain and how we can secure the supply chain so for this we will talk about Supply chains what it means and what it means in kubernetes we talk about kubernetes and how it works with container Registries and we also have a look at validating and whitelisting images and

**8:06:49** · Registries so for this let's have a look at an example supply chain in a traditional way we might have some tools and we put them together using Manpower and maybe machines and we it results in a product we distribute the product to

**8:07:09** · the End customer so how does it look when it comes to a software supply chain well we might might still have some tools that we use and we perform software development which will result in an

**8:07:25** · product properly containerized and we will then distribute it we will release it in a registry and deploy it probably in kubernetes and finally the End customer can see it and well securing supply chain means that we want to be sure that the product that we built here and that we released here is actually the one that the customer will use right we want

**8:07:53** · to make sure of this and so for this we will mainly look at this so how can you be sure that the container um that you actually build with your product is also the one that is then released and used in kubernetes and how can you secure this and restrict this so how does kubernetes work with

**8:08:14** · Registries with with container Registries and let's have a look at first how Docker does this right so with Docker you can contact public Registries just like this and pull an image and but how about private Registries right your your internal applications in your company you probably don't want to have them in a public repository so if you try to pull from like a private registry which is protected you see here Docker pole private registry error X is denied

**8:08:44** · so we have to do you have to do a Docker login and afterwards the login is succeeded then you can pull from the private registry and then it works so very simple you have to log in using some credentials and then you can pull and run and use the containers and

**8:09:03** · images so how does it work in kubernetes well in kubernetes you also have to provide the login credentials if you want to work with a private registry and there you can actually create a secret of type docker registry and it contains your username password credentials and afterwards so at first you have to create the secret and then you have to actually also make the service accounts

**8:09:28** · that should run the pots with the images from the private registry then we have to add the image pull secret right that's how it works in kubernetes and afterwards we are able to pull from private Registries so that's definitely something to to keep in mind and which will already secure your applications in your private registry at

**8:09:55** · least it's time for Hands-On session and in this one we will list all image Registries used in the whole cluster and then use the image digest instead of the image teag for the cube API server okay for this we should head to our cluster and yeah try to find all try to list all images and their used Registries in the whole cluster for this I'll simply generate the yamel of all pots of all Nam spaces and grab by

**8:10:28** · image colon there we go let me filter this output a little bit that it looks nicer for us there we go bunch of pots bunch of images we see for example our at CD and our API server what about Registries so how many different Registries do we use well we use for example ks. gc.

**8:10:49** · Google container registry we also use docker.io and we don't specify anything here which will default to docker.io as well so two different Registries we use right now and in the later Hands-On session we also learn how to restrict these how to forbid these how to allow some what we would also like to talk about is the Tex okay so right now for the cube API server I'm using the tech

**8:11:22** · v193 and the thing with text is that text can be overwritten it's not always sure that behind this TCH will be the exact application version because text can be overwritten and changed so if you would like to do this for this let's have a look at the kubernetes API server which is running so generate the yaml for the API server p

**8:11:48** · there we go and on the very bottom in the status section so we in the status section we see there's a section container statuses and there we see our image yes with the b1193 version but we also see that this is translated into this digest okay so in the digest we see the registry we see the name and then we actually have here the digest which references the exact version that we would probably like to run right now as

**8:12:20** · of now this Tech points to this digest but it could change in the future so this just something that we have to keep in mind what we do right now is copy the whole digest path so with registry and name and then the digest copy it and we will now make the API server use that exact digest so for this we added the Manifest of the cube API server in Etc kubernetes manifest Cube API server

**8:12:50** · yo we search for the image used there we go right now we can see we use the verion so replace it with whatever we copied right and we save it and this should work let's hopefully uh let's hope for this and let's have a look if the cube API server Port is coming back up

**8:13:28** · container creating doesn't look too bad and it's running and if we actually have a look um I'll now simply edit the pot of the cube API server which is running and we have a look for the image and we see yes it's now using actually the image digest and referencing a very specific

**8:13:55** · version in this Hands-On session we will widel list some Registries using Opa and in the end we would like to only allow images from docker.io and ks. GCR do iio

**8:14:11** · for this head to the resources section of this video and copy the command that we list there to install Opa unless your Opa is still installed in your cluster simple commment that we have to run there we go and then head to the second link in the resources which should lead you to our repository where we have our supply

**8:14:37** · chain security and white listing Registries by the example of opa let's have a look at the template so again in Opa the OPA the open policy agent we always create a template which does a general thing and then from that template we create a constraint which kind of implements and uses this template so here we have a very simple template we call it KS trusted images it

**8:15:05** · will create a custom resource definition KS trusted images which we then can use to create a constraint and let's have a look at the violation section section right so what we do is we get the image from input um Al from from the object that will be a pot spec containers we get the image and

**8:15:27** · then we say not start with Docker Doo not start with KS gc. so the violation will be thrown if all conditions are true okay then a violation will be thrown and Port creation will be denied so if it doesn't start with docker.io and it doesn't start with ks. gc. then the violation will be thrown if it doesn't start with docker.io but it does start with ks.

**8:15:57** · GC then no violation will be thrown so much for the template and let's also have a look at the constraint constraint very very simple we simply use our custom resource definition and we say that it will be applied to pods so copy both copy both to your terminal I'll copy the constraint first create a new file constraint.

**8:16:31** · yaml and paste I'll do the same for the template create a file template.

**8:16:44** · yl and I'll first create the template and then create the constraint there we go and if we have a look at

**8:17:04** · templates at constrainted templates there we see our KS trusted images one and if we get our cust resource definition then we actually see that we have putt trusted images okay great and if you remember we can also describe our constraints to see

**8:17:28** · in the status section what's happening with violations Etc and right now status section doesn't have anything it might take a bit for like the current objects to verify in the cluster until then let's create a simple po shall we

**8:17:47** · let's create an engine X part with image engine X and there we see violation Deni the request not trusted image well we now always have to specify our image registry like this and then it works right and if we

**8:18:06** · have a look again in the template I'll just head back to the repository to the template well it's not something magic it just does like a string ring comparison starts with right you could Implement more magic like like if you want to also um allow like the default uh the defaulting back to the doo for example so this is simply how advanced you would like your policy to be but let's try a different one so what we could also do for example is my

**8:18:39** · registry. and there we see it doesn't work right let's have a look if actually um which one did we use ks. gc. if that one works as well so we check docker.io Works what about ks.

**8:18:55** · gc. already exists the PO I rename it and there we go it works so this is a great and simple way of using Opa to WID listing or you could also use it for blacklisting and let's have a look if we describe our resource again and and there we so we have two violations which are actually for

**8:19:20** · example also the the gatekeep in gatekeeper system there are two pots which um actually don't comply with our policy we will now talk about the image policy web hook and let's have a look at

**8:19:40** · an API server we have an API server and we can send API request to the API server API request might be please create a pot the API server can then either allow or deny that request we know this already it does so by authentication authorization and then also by contacting admission controllers and if we have enabled the image policy web hook admission controller then a request will also go

**8:20:08** · through this one and how does it work well it actually works by contacting an external service so this external service is then outside of the control of kubernetes right it depends on us to develop and this external service and to make sure it is running and that external service will then receive an object like a resource kind image review

**8:20:33** · and based on this the external service can yeah allow or deny it and an example document could look like this right simple Json kind image review we have a spec we get containers and based on this we can simply look at the value and then say yes we allow this or we deny this in any of our fa programming languages uh could be go could be python anything that can pass Json and also provide or

**8:21:01** · accept HTP requests and return response like that's that's how it will work and if the external service decides allow or deny then yeah the result will be passed back to the API server and then the API server will allow or deny the

**8:21:21** · request in this hands on session we will investigate the image policy web hook and we will use it up to the point where it calls an external service well the external service in our case won't exist so we kind of simulate that it is down and we see what happens when it's down but up to the point we still have to configure the image policy web hook register it with the API server and we actually see it in action we will actually see how it will deny P creation

**8:21:50** · okay for this you should head to your cluster your cluster should be clean this means if you still have Opa gatekeeper installed then best to remove it so you can simply call Cube c l delete and then the same URL that we used for installing and if that's done then we have to addit the Manifest of the kubernetes API server and in there we have to enable an additional admission plugin next to note

**8:22:20** · restriction this is the image policy web hook there we go simply add image policy web hook to enable admission plugins and save and I can tell you your API server will probably not be happy about it just like this we can wait for it to come up

**8:22:43** · but it probably never ever will so the thing is if you change some configuration in your Cube API server it's kind of like like dark mode you don't really see what's happening if you misconfigured something what we can do to check the locks is we can actually head to um V lock pots and then check or we check for

**8:23:03** · the folders in here and there we see there are like some folders so we can simply check for the cube API server one and now I'll do a tail and in there is a lock file and there we see nice image policy web hook error no config specified okay so for this we should actually now head to our root

**8:23:27** · directory and we should check out our course repository because in our course repository we already have an example configuration which we can use for this simply copy the command from the resources section to clone the repository and then there's a second convenient comment we can execute to copy our example directory to Etc

**8:23:55** · kubernetes admission and we will also change into that directory and have a look what's happening in there well we see a few files we see an admission config we see some certificates and then we see a cube config let's have a look at the admission config so that's the admission config for the image policy web hook which we also have to pass to the kuber netes API server so simply enabling the admission plugin didn't work as we saw

**8:24:25** · and in there we actually specify the path to the cube config file and the cube config file actually then manages the connection to our external service we will have a look at the cube config file after this we can um perform some

**8:24:40** · settings here as well and one interesting one is for example this one default allow false so this means that even if the connection is wrong or our external service is not available this right now means that all po creation will be denied okay so if we set it to true then and our external service is not reachable then we still allow pods to be created but right now we won't allow this so that's the default allow setting and if we have a look at the cube config there we go so the cube

**8:25:13** · config there's a cluster set section and clusters refers to the remote service so we see here we specify the remote service we actually simply call it external service on Port 1 2 3 4 and some path which is the URL of the remote service to query we also have the certificate Authority which we specify to verify the remote service and then we have a user section

**8:25:36** · and the user section refers to the API servers web hook configuration okay so we have the key and certificate for the web hook ad controller to use when communicating with the API server so that's how you configure it and if you faced with a config like this and something is wrong then you can for example check if the certificates if the path are correct or um if the URL is

**8:26:02** · correct depending on on the task that you are working on you know so this is the main configuration and then we only have these certificates here so now let's let's add the admission config yaml to the kubernetes API server manifest so we added our Cube API Over Manifest again and in there we can now actually specify another argument which is

**8:26:35** · admission control config file and this will be in ITC kubernetes admission and then the admission undor config yo okay so the thing is that path exists on

**8:26:57** · our Master node because we just created it we just had a look at that file but it doesn't yet exist in the container so we also have to um configure the proper volumes and the volume amounts I mean we we we use see already um like the PKR directory and for that one it has been already done so if we SC scroll down to the volume section down here then we actually see okay um there we go it's already done there's a host pass mount for the pki directory so we do the

**8:27:28** · same and for the admission directory okay so we have the path to the admission directory and we name it KS at Mission this naming is just our choice

**8:27:43** · right so we just do it here but um it could be any other name directory location and we specified the volume so we also have to specify volume Mount so we can also copy the existing one and rename it to the name KS admission and then we mount it inside the container also to um the admission directory okay

**8:28:06** · so that's the volume Mount that we have to configure and well that should be it let's have a look let's save the API server and let's see what's what's

**8:28:25** · happening I'll have a look if the API server will be booting up again there we go our API server is actually up because we received the response from our getp but we can

**8:28:40** · actually see that the API server is not in here uh it's not listed in here and this is actually because our admission controller right now is active and is preventing something in the background which will prevent the API server actually from from being seen here so let's create a part let's create a pot test image engine X and then we actually see okay forbidden why forbidden because post to this

**8:29:12** · URL no such host okay so this means right now that the image policy weboc admission controller is working we set it up and now it is depending on whatever the external service returns to us right and right now the external service

**8:29:31** · is not reachable so it will prevent any po creation so what we can do right now without developing a proper external service we can have a look at the admission config so we added our admission config and we simply said default allow to true and we have to reboot our kubernetes API server a safe way to do this is I simply comment out the admission control config

**8:30:04** · file and I check no more process running and then I enable it again okay Cube API server is running

**8:30:23** · again and if we have a look in Cube system namespace then we now also see okay our API server is back so something something is good again and if we now try to create a pot with image engine X then we see that it working okay so

**8:30:45** · definitely be comfortable with um registering the admission controller with the API server so you we need to enable the admission plugin we also need to specify the config path and then we now how to define the admission config like it has to point to a cube con and the cubec has to point to the external

**8:31:07** · service and that's about the image policy web hook what did we learn in this section we learned how kubernetes works with Registries with public Registries very easy but also with private Registries using a secret and we learned about image text and digests and that it's also possible to use digest instead of attch we then WID listed Registries using Opa and gatekeeper and finally we

**8:31:41** · also looked at the image policy web hook and we configured it and saw it in action actually denying po

### Runtime Security - Behavioral Analytics at host and container level

**8:32:02** · creation another day another topic or another hour another topic depending on how fast you walk through these well we talk now about behavioral Analytics at host and container level for this we will have a look at CIS calls and how processors use these we look at estr and

**8:32:24** · the magic proc directory and we also use tools in our Hands-On scenarios which help us to identify malicious processes in our system at host and at container level so let's have a look at the broad architecture well we have our Hardware on the bottom on top of that our Linux kernel and it provides a sus call interface example sus calls are for example get PID or reboot and who calls

**8:32:52** · the calls interface well it can be libraries or applications which run and well on the bottom here we have the kernel space and on the top our applications run in user space so applications can communicate

**8:33:10** · with the sus called interface directly like this or go through libraries right usually we go through libraries because we don't want to reinvent the wheel but it's possible to write a simple application which simply calls a Linux kernel sus call and then the sus call interface passes down the request to the

**8:33:31** · kernel and then further to the hardware and well in another section of this course we also talk about tools like set comp or EP armor which will actually lay between our user space and the sus call interface to filter out

**8:33:50** · specific sus calls and maybe to implement another protection layer so we talk about this also in this course but here it's more about calling the ssol interface directly from application processes and this would be the same now if Firefox or Co would run in containers right so let's have a look at another view here where we also have the hardware our kernel and then we have the system calls that can be performed from processes like Firefox in a container or curve in a container so it's in the end

**8:34:24** · the same thing because container processes by default without any sandboxing run directly on the same Linux CER so what are sus calls well there's a bunch of sus calls and let's have a look at some of these so the link is also in the description if you want to have a look there are actually a good bunch of these you see them all here for example you see I already had a look at the kill

**8:34:52** · one so there's like a kill system call which send signal to a process there's a reboot system call and there are like various system calls like for opening a file closing a file um changing file permissions you know so that's that's actually quite a bunch um that's described here and if you like you can

**8:35:14** · have a look through these and maybe look if you find some familiar ones but we will investigate these a bit more in the upcoming Hands-On sessions before we move into the Hands-On session we will talk shortly about what estess is so estess is a tool which intercepts and locks system calls made by a process and it usually comes pre-installed with various Linux distributions it can also lock and display signals received by a process so

**8:35:46** · it is very great for Diagnostics learning and debugging and to get started with s with estr we will have a look at estr and the ls command how many sus calls it makes so we will investigate what it does and we will find all sus calls and down here are some um some arguments that can be used which we might need okay so for this head to your master node and type

**8:36:13** · LS okay I'm in my root directory there's nothing going on here right now but I could for example do LS slash and then something will be returned so what happens there what kind of sus calls will be made well we can simply write s Trace in front of it and run it and there we go some large output so let's

**8:36:36** · scroll to the very top and let's walk through a few of these so all the calls that you see here are actually sus calls that were made so first is like exec ve and you see that actually the proper binary the proper path um was was executed and then access tries to access some file open at

**8:37:01** · will open the file you see in which mode like read only or different ones close these are all sus CS right here we see for example fad something that fad made and if we want to know what happened there we can can simply go to manual page look for fat system call and we see ah okay fat get file status okay so it tries to get the file status of some file and this happens a lot right it happens a lot before it's probably a lot of like initialization before even our proposed commment to list the um the

**8:37:34** · root directory is actually executed so and down here we see something okay so fad was made again and then right okay so there's a right cull so what does right do we can have a

**8:37:51** · look there we go right write to a file descriptor okay so this could probably also be standard output because here we see a right was made and there we see this is exactly the output that is provided to us when we run the comment right so that's what we can use to investigate what kind of ss calls have been made in which order which is really great from all processes and okay there's like a verose

**8:38:23** · mode we don't want to try it we already have enough output here but you can try it if you like but the others we talk soon CV count and summarize this could be nice so let's try this one so instead of running it like this we do it with c and W and then we see

**8:38:42** · nice it's a different kind of output where we actually see what kind of CIS calls have been made and how often okay so we see now for example excess has been made eight times and right right had been has been made two times and this way you can directly see okay should that process maybe even read anything you know and that's how you can directly investigate what a process

**8:39:10** · does and let's maybe have another short example I simply Echo hello in test in a new file test and if I output that file then I get the result back and if I run it with s Trace then we also see just as with the ls command before we see a lot and here we actually see that read was executed and read is assist call and it reads hello and then it writes hello probably to STD out

**8:39:48** · time for another Hands-On session in which we will also use S in a bit more detail than before and we also have a look at the slpr directory so let's talk about this one at first so the proc directory um contains information and connections to processes and the kernel we can use it to study and learn how processes work it's definitely also nice for this but it's also also important for configuration and administrative tasks it contains files that don't really exist right yet we can

**8:40:21** · access these so it's kind of that the files will be created once we access this so it's kind of a communication interface with the Linux kernel it receives the request to access a file and then provides us dynamically with the input for us it looks like it is just a proper file system it's it's pretty nice so what we will do in this Hands-On session well we will use S trce and the magic proc directory to investigate at

**8:40:50** · CD we will have a look to the CIS calls that the at CD process makes we will find all the open files and then we will try to read a secret value from the file system which is stored in at CD okay for this we head to our Master

**8:41:08** · node and let's have a look I mean we can have a look for the for ETD in Docker and we see yes ETD is running in Docker it's Cube ADM by default containerized as a static pot which also means it should be simply here running as a process and there we see at CD is running down here and for me the P ID is

**8:41:33** · 3502 so here we see again from the perspective of investigating CS calls it doesn't really matter if the process is running in a container or directly on the Linux system we can simply investigate it okay now we want we would like to use S trays um but before we only did estr and then we actually run a command right we execute a comand but we can also do it to actually have a look at running command so with P we can actually investigate a p ID or process P

**8:42:04** · ID so we do like this for me 3502 for you it might be different and there we go constant output of sus calls being made I interrupted now we can also use- F and here we see various ones so this

**8:42:22** · will also DF will also follow um subprocessor so follow Forks like we see here and okay let let's try the count and summarize again as well the CV here so we can also do this and we simply wait

**8:42:38** · one two seconds for everything to happen and we abort and then we see our statistics about how many sus calls at CD made and here we go we have a list of all these sus calls made and it definitely reads A Lot does it write a lot as well um right yes it writes a lot it reads A Lot okay interesting so for the first part list all sus calls that the running process at CD made we did this let's have a look at the second one find open files so which open files has

**8:43:09** · ET CD open or which files has ETD open and for this what was my P ID there we go 3502 is mine so I had to slpr c52 and I have a look and there we see various files okay so we are now in this magic proc directory and one file that we can for example look at we see it here already colorized it seems to be a link so let's have a look at the EXA

**8:43:37** · file and there we see it's the proper full path link to the actual bu inary that is being executed that's interesting and what would we like to do we would like to have a look at open files so there's a directory FD we can

**8:43:55** · have a look into it and there we see okay various things there we go so this is a list of all open files we see also a lot of open sockets in here you see something viip member okay some some temp file prob here and if we scroll down oh this looks interesting no number seven for me it's a folder number seven and oh it's actually a link called seven

**8:44:26** · to this file and snap DB DB sounds like database ATD is kind of a database that sounds interesting no let's have a look what's happening in there we can trade a little bit oh and there we see okay some binary out output um so what I simply did is like I tailed so to get the the last some last lines of that file and there we actually also see something that looks more like Jason or yo interesting let's have a look if

**8:44:56** · we can find something in that database so we would come to point three read a secret value from these open files okay for this let's create a secret okay create Secret

**8:45:13** · credit card or it's type generic he create secret generic credit card from literal and we say credit card is 1111 2222 3 3 3 3 4 444 I will do a dry run you don't have to do dry run just that we see what will be happening here this kind of secret will be created with our credit card highly secured using a very sec your Bas 64

**8:45:46** · encryption and okay let's create the secret there we go and what we can try now is to cut for me it was file seven and I grab for my credit card number let's have a look something in there binary file standard input okay so what we can do because it's a binary file we can use strings we pipe it into Strings and then we do our grab and there we go okay it actually found something and I now

**8:46:18** · simply tell grab to show me 10 lines before let's say 20 lines before the match and 20 lines after the match and there we see okay something actually is in here and there we see our credit card information and we actually see it stored in registry Secrets default credit card so this looks like at CD is actually not encrypted it simply writes data into a file on the file system and

**8:46:47** · yeah without encryption enabled we could simply pass it and look for credential information in this Hands-On session we continue our journey through the magic proc directory and for this we will create an Apache pod with a secret as environment variable just a simple secret value hardcoded as environment variable available in that pot and we

**8:47:12** · will then attempt to read that secret from the host file system and this should just give us a bit more Hands-On understanding of how processes containerized processes work and also with the proc directory so you heard the task create an apach pot with an environment variable of your choice name of your choice value of your choice we just have to find it later again so what I will do is krun a Pache image is 8

**8:47:44** · httpd we would only like to have the yanl generated for us please and we can simply add an environment variable section the name for me will be secret I

**8:48:05** · call it secret and the secret value will be this for me just choose anything of your liking and create the pot okay I have an Apache pod running

**8:48:24** · which means I can exit into it and check for the environment variables please do the same and verify that your environment variable is indeed mounted inside or not mounted but made available inside that container great now we would

**8:48:41** · like to have a look look at the proc directory for that Apache process that's running okay so what do we have to do for this let's have a look for the P of the Apache process which should be httpd nothing running did you catch the

**8:48:58** · error right if we have a look at the pots then we actually see that our pot is indeed running on our worker Noe so let's head to our worker note I'm now on the worker note let's have a look here for httpd there we go there are some processes we can also check if there's actually our pot running as a Docker container and yes it is great now we see some processes up here

**8:49:31** · um with the PS output could be a bit confusing there's also nice common PS3 so PS3 shows you the whole process tree um root processes subprocesses and minus P can actually also output then the P

**8:49:47** · IDs of the processes so we can run this yes it's a huge output it's a large output output but what we are only interested in is actually the container D process and here we see it already for me so I scroll a bit up to to check from

**8:50:03** · the beginning you see okay there's a root process and then we actually have container D our container runtime then container D shim and there we see something we have q proxy running weave is running let's scroll down and there we actually see okay container shim and then we have httpd running so that's our main HTTP process and then we have various sub processes so I simply copy that ID that P ID 28696 for me and for this we can check the proc

**8:50:35** · directory for this process again various files in here we can for example see the proper path by checking the Excel link we could also check again for open files um yeah we could have a short look for open files there definitely few open files there we go and there's also a file called Environ

**8:51:01** · and in Environ if we output the content then we can actually see here there's actually the environment variable and my secret value and you should also see your environment variable there and that secret value so just this as a little overview and remember Secrets as environment variables can be read from anyone who has access to the slpr directory on the host but I mean that's usually root processes and if someone

**8:51:30** · has root access to your node and to Docker then and that person can anyway read all the secret information in this Hands-On session we will use Falco but before we go into installing Falco actually we will have a little overview about what Falco is so Falco is a cloud native runtime security also Under the Umbrella of the cncf and it provides different areas of

**8:52:03** · expertise one is for example access so acccess means that it provides deep kernel tracing built on top of the Linux kernel so it has an overview about the processes running uh on that system on that host operating system and it can investigate their activity kernel activity CIS calls Etc so things that we did manually before and then based on this it can do things like asserting which means we can describe security rules against the system and there are also various default ones and this

**8:52:36** · allows us then to detect unwanted behavior and maybe create some locks notices about this and yeah there are also actions which can be taken there can be automated responses to security violations and there are also various existing rules apart from the default ones because in on the internet community-driven for various tools and use cases so let's go ahead and let's

**8:53:03** · install Falco on our worker note right we want to install it now natively on our worker node there are different ways um of How It's possible to install there there's actually also a page it's also linked in the resources section of the video auditing with Falco there's not much about Falco yet in the kubernets documentation but it also says so it can be installed stand alone it could be installed as a demon set as well so a demon set which runs a pot on every note and then that pot needs to have privilege access maybe Mount the whole

**8:53:33** · file system Etc it needs definitely more access but we will now do the Standalone FAL Co installation and for this you should head to your worker note and simply copy and execute the comments from our resources

**8:54:09** · section and after this it will be installed as a service so we can have a look at Falco status and there we see it's not loaded right now so we have to do service Falco start and then the status should show active and running okay and well we see

**8:54:30** · already some some information down here but if you are faced with a Falco install then usually by default there's a etc Falco directory so change into it and there we see already some folders with rules and there's the main configuration Falco do yaml so open that

**8:54:49** · one and if we have a look through here then we see for example that it lcks to CIS loog um so we should be able to see information in sus loocks we also have sus call event drop so there are like various things and here we see suslock output Ena true so here we know that it

**8:55:09** · will output to syslog it might be configured to to Output it to a different location delocks you know so what we can do now is in this case by default it outputs the Cs loog so let's have a look we tail cslog and we grab for Falco and there we see different things

**8:55:27** · initialization grade and here we actually see for example notice privilege container started okay so this is a an existing default Rule and here we actually see that one pot or container of weave Works which is responsible for creating the cni um yeah is running as privileged container and this simply outputs a warning which we could maybe further use

**8:55:53** · okay so we installed Falco and let's continue to use it in this Hands-On session we will use Falon to find malicious processes inside containers and we can actually simply use the default Falco rules and yeah use

**8:56:10** · these to identify for this on your worker note you should tail the suslock directory and grab for Falco events which I'm doing here right now and on our Master node we will now create a malicious pot and see what Falco will say about this and for this

**8:56:28** · we should still have a pot from the previous section and simple Apache pot you can simply use this or create a new one we don't need the environment variable section in here but it also doesn't hurt so that simple Apache pot should be running and let's get a shell into that one so exec into the Apache Po and we get a bash shell that's it we inside the

**8:56:51** · container let's have a look on the worker note what Falco has to say about this it has something to say about this notice a shell was spawned in a container with an unattached with an attached terminal and we have some information actually about the shell and also about the container ID so the docker container ID where this happened okay nice so Falco has already some existing rules to notice things like this let's head back into the pot and let's try to exit something

**8:57:22** · secure um like the ATC passwd file that we see some user information from inside the container and let's have a look if FAL has something to say about this not like this but what happens if we try to

**8:57:38** · edit the file okay there's no Vim so what I do is I Echo user and I simply append it to/ Etc passwd like this do the same simply write something into that file and then we see error file below um

**8:57:58** · SLC open for writing so so anything in SLC was open for writing which can be unusual in a container um if not if not wanted so it gives already some some information about things going on for example as well we could for example try to do an epet install something do an appet updates so this is like a Debian based package um could be any other package manager as well in Alpine for example a different one and here also we see error packet management process

**8:58:31** · launched in a container great so Falco already watches over a lot of things and it we can get the information from FAL what I would like to do now as well I mean we EXA into the PO and we did this manually but we can also have a look that it works if the container does it itself right and for this we can actually we could now add the comment section and execute a comment before we execute a Pache but we can also use um a

**8:59:01** · probe so like a liveness probe a Readiness probe which simply exx a command from time to time so I'm on the kubernetes documentation and I searched simply for live probe or Readiness probe and then there's this great page from which we can steal again some code so that we don't have to type it ourselves I will now simply steal a liveness probe which exits a comment which we would like to do there we go and what we will

**8:59:30** · do here is well let's simply run EP get update okay and initial delay seconds 5 period second five okay so every 5 Seconds um we will do this let's say every 3 seconds we will do this and

**8:59:51** · um well actually if it fails that that wouldn't be too nice it's the liess probe let's I do I'll change it to Readiness probe so just shortly the difference between a liveness probe and Readiness probe if a Readiness probe fails the container keeps running but the whole pot will get in a not ready state which means no new requests by kubernetes services will be redirected to that pot if a liveness probe fails

**9:00:22** · then it means that that specific container will be restarted so right now we don't really use Readiness probe for what it should be used we simply want to execute a commment EPG update let's try this so

**9:00:38** · what I will do is I will recreate the pot so I'll first delete the PO and then I will recreate the pot okay let's have a look if it's actually running it is running and then head to the worker note

**9:00:59** · and see what happens and there we actually see that now every I think 3 seconds we said um there's a process inside the container that tries to do something malicious so even without us manually doing it through an shell that we got under that container we see that Falco definitely knows about

**9:01:22** · it in this Hands-On session we will now look at some existing Falco rules of the default rules that Falco comes delivered with and in the real certification it is unlikely that you have to write your own rules but it is good to know to know where they are and have a look how they are structured so maybe it helps you debugging if something is not working properly for this we should be on our worker note where FAL was installed and

**9:01:48** · we have a look at Etc Falco there are various files and we look in the falcore rules. yaml at first and if we for example search for Wass spawned then we actually see a message that we saw before a shell was Bor in a container with an attached terminal right when we tried or when we actually successfully EXA into that pot container

**9:02:21** · and here we also see the variables the more information that is being output for us to then further investigate and here we see for example the container ID so this is simply how this works and if we see this is a rule it has a description it has a condition right that has to be met in order to be called and then we have our output and for priority we see actually that it's

**9:02:51** · notice so you can have a look maybe through some of the other rules you see they're always constructed like this and I would also like to show you the ks audit rules so open the ks audit rules.

**9:03:08** · yo and in there search for Etc and there we are already so there's a macro called sensitive volume Mount so it is possible to create rules which we see here rule section and it's possible to create macros okay so macros can be called by conditions of rules sections

**9:03:29** · and here we see the sensitive volume Mount marro and here we also have the condition if and here now we see pot volumes host path so here we now actually check a cuet object and if that one intersects so if it contains any of these then that Mar will be true right and here we have for example SL Etc so what does this mean so host path if a PO has a volume of type

**9:03:59** · host path then it means it mounts a volume from the node where it's running on so for us for example if a pot runs on the Seeker as worker then it can mount the complete root root directory of that note and then read everything right and for example under V Docker or

**9:04:19** · yeah under voka there for example all the um the locks of other containers so it's very sensitive information so this is this is the marod to identify and then we have a rule create sensitive Mount pot this will detect an attempt to

**9:04:38** · start a pot with a volume from a sensitive host directory example proc exceptions are made for noun trusted images okay this sounds great so the condition um in the condition we actually see that we call our macro which is defined up here and we say yeah if this is true the Marco and not and if the container

**9:05:02** · repository is not in a list of allowed images so some so we can actually provide a list where that um shouldn't be thrown and we see the priority is warning so it's not noticed anymore it's a bit higher and we actually see the source is K as audit okay so the whole file uh contains audit rules for

**9:05:23** · kubernetes which only work if kubernetes auditing is enabled so we talk about kubernetes auditing in a in a different section in this course but in generally it locks every API request that is made like create a pot change a pot and then locks all the yaml and this is why here for example we can also then have a look at the pot volumes host path to check the host path so yeah if you like have a look through these existing rules and

**9:05:55** · get a better understanding of it but as I said it's unlikely that you have to create your own rules but it's good to get a feeling for it maybe also change a rule you know change a rule to Output some more information and restart the Falco service and have a look if it worked

**9:06:13** · time for a very important Falco Hands-On session where we will now actually go ahead and change an existing rule so we will change a default existing rule from Falco to get a custom output format okay and the rule that we'll be looking at is a shell was borwn in a container with an attached terminal our wanted output format will be time comma username comma

**9:06:39** · container name comma container ID so kind of like a CSV format and the priority we want to have that it's priority warning if it's not warning yet then we have to change it okay for this let's go ahead first thing if we are on the worker note so far we have looked at Falco as a service so we can have a look Falco is running but we can also simply stop Falco and

**9:07:09** · when it's installed then we can can simply use file from command line just like this by running it there we go and we see already there are some rules some notices in this case um being

**9:07:24** · written okay great so now we want to cause that rule a shell was spawned in a container how can we do it well let's just create a pot exec into the pot and that should be already it so on the master note um from the previous sessions you might still have an Apache pod running if not simply create a very

**9:07:47** · simple Apache pod image httpd and it should be running and once it's running we can exit into it and try to get a shell which works there we go and if we head back to the worker then we actually see nice there we have it notice a shell was bond in a container with attached terminal and then we see various output here okay so this all is the output which we will

**9:08:18** · now adjust in this challenge so for this let's change into Etc Falco and let's have a look at some of these files so there are a bunch of files there might even be some custom files so what we can do is we simply copy some text of it and search for all files grab

**9:08:42** · dasr paste the text search in the current directory and there we see in Falco rules there is actually the one that we would like to change so we simply head into that

**9:08:59** · fire and search in here as well and there we go there we see our rule um it's called terminal shell in container we have a description we have a condition and we have the output and we would like to change the output if you have to do this in the exam you can go ahead unless it's specified otherwise and you could simply um addit that default file right maybe make a copy before in case you make mess something up but that's definitely possible but what we can also do is we simply copy everything so copy the whole

**9:09:32** · Rule and then we exit whim and we now actually have a look at Falco rules local file so in the Falco rules local.

**9:09:42** · yaml we can overwrite existing rules and if we open it then there is so far only a little bit of information text so we scroll to the very bottom and paste our rule there there we go so far so good first

**9:09:59** · thing that we notice is okay priority is notice and if we remember from our task we would like to change it to Priority warning so let's go ahead and and let's do this at first I simply remove notice and exchange it with warning there we go I run

**9:10:22** · Falco we see Falco is loading the default rules files and then the local rule files to override and let's cause on the master note let's cause that rule again to fire just by exiting back into that

**9:10:44** · pot and there we go now we see it's actually a warning so our change already worked now let's go ahead and perform the other changes necessary let's have a look we want to change the output format to time comma username comma container name comma container ID for this we addit the Falco rules

**9:11:11** · local again and simply change the output so we can in this case remove a lot of information okay um right now you can always see that there's like some variables which will be replaced with the actual value which is already great username is helpful we want to have the username I don't see anything about time right now so what I write at the beginning is simply time comma we still have to do this then next should be

**9:11:41** · username there we go username we have it here what do we have then container name let's have a look we have container doino let's try container.

**9:11:56** · name and then I think we still want to have the container ID back there I see the container ID so we reduce a lot of the default output information to Simply use the format that we would

**9:12:12** · like okay this looks already great but at the beginning we still need that timestamp for this we actually head to the Falco documentation so it's Falco org docs and then it's rules supported Fields here on the left side we see it here the link is also in the resources of this video and you will be able to access the fal Cod documentation during the exam as well so you could for example save that URL as bookmark and

**9:12:42** · access it fast during the exam let's have a look on that page supported fields for conditions and outputs here we see a lot of things um that that can be used right proc ID proc XA um the IDE of the process generating the event the first commment line argument these are all great things which we can if we like output for further information and we scroll down then we actually see here the um the event field class and what we can use is for example event.

**9:13:15** · time let's have a look at that one so I copy it paste it here and this should work let's also have a look at container section so I search for container and there we see various things we also wanted to have the container name we already have it what about

**9:13:38** · user there we see very things user.name that's the one that we also use so yeah have a look through these but you don't have to remember any of these because you can access these during the exam as well but this looks fine to me so I save it I run Falco and I head to the master node to cause that event

**9:14:03** · again and what do we see well the output format has been changed it is now exactly like we want we want to have the time the username the container name and the container ID just as specified

**9:14:23** · here okay and with this you should be able to alter existing Rules by specifying a different priority or output format and yeah you should be comfortable with doing this in the exam so maybe go ahead and we see here for example there's a notice about privilege container started with like a default output of information just go ahead and overwrite that rule again as well so that you have some more experience with

**9:14:56** · it we talked about behavioral analytics on host and container level if you like to dive a bit deeper I have a few suggestions for talks one talk what have sus calls done for you lately very great talk into CS calls what they means how they're implemented by list rice I can definitely suggest this one Link in the

**9:15:18** · resources section another one if you like to dive a bit more into Falco get a general perspective of it there's also an introduction into Falco and Link also in the resources and to wrap this up we talked about system calls what CIS calls are

**9:15:34** · and how they play a role in pots containers and processes and from the host operator system it doesn't really matter if they are running processes directly on the host or in containers and Falco which we used also can for example um check container processes as well as normal processes running on that system and then we also used estray and the magic proc directory for some manual

**9:16:03** · investigation into malicious processes and for Falco we also looked at changing existing rules like being able to overwrite them in the local rule definition file to maybe change the lock level or even the output format so that's definitely something to know for the exam as

### Runtime Security - Immutability of containers at runtime

**9:16:38** · well we should talk about your containers are they really immutable in this section we talk about immutability of containers at runtime for this I give you a little introduction about immutability in general and then we talk about enforcing immutability on container and pot level

**9:17:00** · and we will have some handon scenarios to ensure that a pot's containers are actually immutable so so what does immutability mean well we could say simply a container won't be modified during its

**9:17:18** · lifetime and let's have a look what mutable means at first to explain immutability a bit further so mutable would mean for example if we have a virtual machine then at any point in time we could SSH onto that virtual machine we would stop our application we would update our application we would upload the new application version and we would start that application again it's a very still common but a few years ago very common process where we update

**9:17:48** · our instances in place with our um new application version and often also done by SSH let's have a look at the immutable version of this well this would mean we would create a new virtual machine image we would delete the old virtual machine instance and we would create a new virtual machine instance from the new image version which contains our new application this could be an example as

**9:18:16** · for an immutable example and if we now replace all the VM names with containers then this is still true as well right um we could SSH for mutable into our container and stop the application and start it again um but usually for immutable it is done just

**9:18:37** · like this we will create a new container image and then we delete the old container instance or the old pot and then we create a new pot with the new container so in the containerized world it is already um very common to go the

**9:18:53** · immutable way that we see here on the right and this is great because we always know the state right um here on the left if we do this for a year and with many deployments we don't actually know in which state our application actually is did some someone lock onto it manually and edit some config files we don't know this whereas with immutable we always know the state of

**9:19:19** · our container or do we we'll have a look into this why should we do this why should we do immutable well it allows us for to use Advanced deployment methods that come for example with kubernetes it allows us easy roll back more reliability and also better security at least on the container level because at any point in time we can simply um remove a container throw it away and create a new one and we then know the state we know there's like no

**9:19:52** · other malicious processes running in it and yeah that's the advantages of immutability and of containers in general and that's also why containers gained so much popularity in these current times

**9:20:12** · what could we do to ensure that our containers are actually immutable well this could start already on the Image level right like when we write for example our Docker file we could remove bashes and shells we could make the file system read only or only certain parts read writable and we could run the whole thing as a user and as a nonroot these are things that we should definitely do they are good practices to create your image your Docker file already hardened and

**9:20:45** · immutable but what if we have no control of the container image well you could always create an image and base it on the one that you would like to change but if we can't if or if we don't have the possibility to it or if we are too lazy to do this we can also do some things in kubernetes so let's have a look at a few possibilities what about making manual changes to a container using the comment right we could execute a custom comment so let's have a look at the pot startup timeline our pot starts which means our

**9:21:18** · app container will start and then our app container runs whatever has been specified to run as comment and we could simply overwrite that comment right instead of WR um executing only engine X we execute also another comment or various comments or a script which in this case removes the writable permissions from various folders so we could do this it might be hecky but uh it it would work let's have a look at a at another even more hecky way maybe um let's have

**9:21:50** · a look at the startup probe do things with a startup prob so our pot starts again our app container starts and the app container is running and then we could configure a startup probe and a startup probe is actually similar to a liveness probe and a Readiness probe so when a startup probe is configured then no Readiness probe or liveness probes will be executed until the startup probe

**9:22:16** · succeeded so it's kind of it can be used to ensure um that that everything just starts running once your application is running okay so usually a startup probe will query the same Endo as a liveness probe and when a startup probe fails then the container will be restarted same as with livess prob we could hack this a little bit and use a start probe to actually do changes right so we could actually say our startup probe will run a comment um to make the file system

**9:22:48** · read only or do other things and then these start probe succeeds we will return through and then our app container starts to run so it is possible but just because it's possible it doesn't mean that we should do it or have to do it like this another way maybe a better way would be to enforcing read only root file system using security context and

**9:23:12** · or pot security policies so with pot security policies we have a different section about this in these C we could enforce that all ports have to um run as a readon root file system using their security context so we could do this for example which might be a better way one thing I would still like to talk about is what about moving logic to the init container so let's say okay we now have an immutable container and our app

**9:23:43** · container and it's actually it has a readon file system it it can't Rite anywhere what we can also do is if our pot starts we could have an init container so let's say an init container starts and the init container will start before the application container and it will run through and only when it is run through and it is ended then the application container starts and containers in a pot can

**9:24:08** · communicate via a volume so we could add a volume to the PO and then say we give our Enit container read write permissions to that volume at the beginning and for example this could be we have a PHP application and it needs initially to create some caches and then

**9:24:25** · afterward simply serve the file so we could say we generate the cach in our init container and we give our init container readr permission to the volume and then our app container itself is already hardened and it can also only read from that volume where the caches are already generated so this is a possibility um if you want to remove even more writable access for example from from the application container you could move logic into an init

**9:24:58** · container and it's time for Hands-On session and in this one we will use a St probe to remove the executables touch and Bash from a container for this let's create a pot called immutable image a pachy httpd and we would like to edit the yaml of it so let's generate it k run

**9:25:25** · immutable image htpd and we only interested in the yamamo code pass it in the file of your choice let's have a look at it great let's create it let's create it and have a look what it does it's running let's exit into it get a bash here we go I'll run touch test and

**9:25:56** · it created a new file test touch works okay great touch works that was the whole idea of it now we would like to edit our p declaration and for this we will actually in our only container that we have right now we would now like

**9:26:15** · to write a stup probe which simply removes touch okay for this we can head to the C documentation search for startup probe or livess probe Readiness probe you should find a page which looks oddly similar to this one probably and we scroll down a little bit and there we see a liveness probe session that that we can steal so they are very similar uh

**9:26:42** · in their configuration so we can simply copy the liveness probe one and then change the name to Startup prop there we go and the commment that we will execute will be remove bin touch there we go let's say initial delay seconds uh one and period seconds we can leave it like this all right let's let's try this

**9:27:15** · well we should probably delete the part the old one it's still running and then recreate it with our changes there we \[Music\] go and we exec into it try to run touch and it does work anymore okay crazy I know we removed a binary from that but now let's finish this Hands-On session and remove bash and see what

**9:27:46** · happens then so for this let's simply change our part declaration our startup probe that it removes bin fash just like

**9:28:04** · this delete the PO recreate the PO and EXC into the pot still works and let's try this again there we go so the startup probe took like a second and I was able to ex into it before it was executed and now we see no executable bash found not possible to exit into the pot using

**9:28:33** · bash in this Hands-On session we will now actually ensure that our pot and container is immutable by enforcing a readon root file system by setting a security context on container level to make file system read only and then we will also ensure that some directories are still writable using an empty deer

**9:28:55** · volume okay let's go ahead and we should still have a PO running uh called immutable we should have the PO yo if you still have the startup probe from a previous session then remove it and all we want want to have is a simple pot with one container httpd image and we now will actually

**9:29:15** · create a security context so at on um container level a security context and then we use read only root file system true there you go do it like this add a security context and read only root file system set it to

**9:29:43** · True save the file delete the existing po if it still exists and then create the PO and then exec into it error from server connection broken and our pot is

**9:30:03** · actually in a crash loop back off let's see if we can get get some information about it let's check some locks of that container all right what do we have here our Apache is not able to start we have a readon file system could not create something in user local pat2 locks all

**9:30:27** · right so what we would like to do now is to allow that container to right into that directory and we can do this using an MTD volume which we create so we have to change our pot declaration to create an MTD volume and then Mount that volume under the necessary path okay for this we can head to the cuetes documentation and look for volumes simply search for empty

**9:30:59** · deer and down here we have empty deer there we go and there's an example great

**9:31:20** · okay we don't have to rename it we can uh call it cach volume I just have to check what the path was again it was sluser local Apache to and

**9:31:37** · logs so it should be like this okay so we create an mty deer um volume we call it cache volume and then in our container we create a volume Mount under that path that needs to be writable and yeah we use the cach volume for that mount let's try it out Delete the old one recreate it check the

**9:32:07** · status it's running let's exec into it and here we see I now can't we have the touch command again we didn't remove it but I can create I can't create files because it's a readon file system but if we have a look under the actual path that a Pache needs then we see we can actually create files and there's also an hbd PhD which the

**9:32:37** · process did create so if you come from a Docker world and you might be familiar that you can do something like this you can do Docker run read only so you can run a container read only and then you can also specify temporary file system Roots U like here then SL run in which the container is able to write okay so you you can use this in combination there are some talks about bringing this also

**9:33:05** · through another conflict parameter into kubernets so if you use a security context and you enforce readon root file system that you can then specify with another argument also some writable um directories but as of now a solution is to use an empty D volume for this like we did and as we reach the end of this

**9:33:27** · section we should also shortly mention role based access control because it always we should ensure using rased access control that only certain people can even edit a pods back or exac into a pot to then even do things that's also something that should be considered when talking about immutability in general

**9:33:46** · and yes so what did we talk about we talked about immutability in general we talked about it on a container Image level like in the docker file where it should be done or most of it should be done and then we can also do it on pot level via security context and we can enforce this also cluster wide using pot security policies or even other admission controller Frameworks like open policy agent and we also mentioned role-based Access

### Runtime Security - Auditing

**9:34:25** · Control audit logs and auditing in kubernetes definitely my most favorite topic of all I might say this about every topic so it's definitely my my top three of all favorite topics and for this we will go into an introduction into the whole thing we will then set up and configure audit locks in the API server and we will also investigate the access history of some resources by some users by looking at the audit

**9:34:55** · locks there is a kubernetes API have you heard that kubernetes has an API I hope you have heard that kubernetes has an API and if we create pods or updated deploy employment or read Secrets then these will all be handled as API requests to the kubernetes API and we can then ask the kubernetes API to Simply Save all the request and data and

**9:35:22** · metadata into a data store which then holds our audit locks and we are able to access it so we have a history of all API requests made these are the audit locks now you know everything you have to know about audit locks but this video goes on for a bit longer which is why we continue there will be a bit more about it let's ask the question why do we even need audit locks right so it's from

**9:35:49** · security perspective it's very interesting because it allows us to answer questions like did someone access an important secret while it was not protected let's say we realized there was a secret and during two months it was not properly protected by robust Access Control to Broad access so we could actually check who access access this secret through the kubernetes API during that time period we could also ask when was the last time that user X did access cluster y or we could

**9:36:20** · ask does my custom resource definition work properly okay so this might not have something to do directly with security but it is it can be nice for debugging if you create applications and services that interact extensively with the kubernetes API and kubernetes resources so as you see definitely useful to have so we have a kubernetes API which receives API requests and saves these in audit locks and we can access these so

**9:36:52** · we can decide how much and which audit locks we would actually like to lock and first and foremost we should have a look at stages because request run through stages when it comes to audit logging in commun API and these stages are request reest received response started response complete and panic okay and we can

**9:37:17** · actually create an audit policy and in that audit policy we can then create or set these stages so any of these stages which we would actually even like to lock so before we jump further into audit policy let's have a look at the four stages and what they do and what they actually mean each request can be recorded with an Associated stage the known stages are

**9:37:50** · request receive the first one the stage for events generated as soon as the audit Handler which is the API server audit Handler receives the request before it is delegated down to the Handler chain response started once the response headers are sent Okay so the API server

**9:38:09** · received the request and already sends the response but only the headers okay so once the response headers are sent but before the response body is sent it makes only sense for long running requests like watch like if you watch um for certain objects then you might send the request to watch but the response will be delayed then there's also response complete the the response body has been completed and no more bytes will be sent so the response has been sent has been completed or Panic which means events

**9:38:42** · generated when a panic occurred so these are these stages and we can decide which of these stages do we even want to save data off so what data to store what events should be recorded and what data should these contain well if we have many API

**9:39:01** · requests then we will have much data to store it's a simple simple logic right and the thing is the API request won't just be done by us typing qctl runp you know there are like various Services communicating with fpi the CET communicates with the kubernetes API so the the notes send requests and various components and maybe you have other um third party controllers in your system that communicate with the API so there is a lot of data um being

**9:39:33** · generated so for this we can create an audit policy again and we will soon see an example of such an audit policy and um so yeah at first we said we can Define the audit policy we can Define the stages and now we can also Define levels so let's have a look at four levels that also exist so there's the level none which means don't lock events

**9:40:00** · that match this rule there's the metadata level lock request metadata there's the request which locks the the metadata and request body and then there's request response lock the metadata request body and response body okay so these are the four levels that we can also Define in our audit policy to restrict the amount of data

**9:40:26** · that is being stored what events should be recorded and what data should these contain we Define this by creating an audit policy and now let's have a look at an example ex Le audit policy there we go that's an audit policy can see kind policy and then on very first we for example see omit stages and here we say we don't want any data from the stage request

**9:40:54** · received which is like the first um the first stage that it runs through okay so in this example we say no data from request received then we have our rule section and we see our first rule which means no read action so we don't want to lock anything so we specify level none don't lock anything when the verb is get

**9:41:15** · watch or list okay then let's have a look at the second rule lock nothing regarding events so again level none if it's about a resource events okay so this means if we have an audit event um this is now the kubernetes resource events so if for

**9:41:36** · example our action is get events we send the request get events then it will go in here and it will go out because the first rule will will be matching and we don't loog anything with get okay so get events will get in here and then go go out here but if we for example say

**9:41:54** · delete events then the first rule won't catch but the second rule will catch because it's delete events it is about events level none we will jump out here okay so this is is it's it's processed in order let's have a look at the third rule lock nothing coming from some groups we can also restrict this like we don't want to hear any noise coming from worker notes being sent for example request response so this is

**9:42:21** · similar to the one that we have here now it is about secrets and we say okay when we reach here we would like to lock the request body and the response body and the metadata of Secrets we have to think about that this will be generated in locks and the locks might be distributed to different logging systems and in this case with this rule we will save not only metadata

**9:42:48** · but also request body and response body of Secrets which means our secret values will be contained in the locks might not be something that we have to do but in this example it's just done like this and then on the very end we have a catch all rule which means for everything that didn't uh fit before we will lock metad

**9:43:07** · dat level and yes as I mentioned before so these are checked in order the first matching rule sets the audit level of the event so where should we store all that

**9:43:24** · data okay let's say we created a really broad audit policy which stores almost everything that that it can where should we store all the data well there are different backends they're called backends audit backends and the simplest one will be Json files it will simply be in Json files there can also be um a

**9:43:43** · maximum size set and there can be like a rotation set like a lock rotation and Json files will be the format that you will have to work with most probably in the ckss certification there's also things like web hook which allows like external API access and also a dynamic backend like audit Sync API but in general the audit backends allow us to then in any format that we would like to

**9:44:12** · yeah send it further to our login systems like fluentd like filebeat and or like elastic search because it will be a large amount of data and further logging systems to manage this amount of data is definitely useful but yeah we will concentrate on the logging into Json files now finally let's have another

**9:44:35** · Overlook overview about everything that we just talked about so we have a kubernetes API it creates audit logs because we tell it to and we then can decide which audit locks should be saved and we can decide this by talking about these stages at first so the request when it comes to audit logs runs to different stages like request received response started

**9:45:03** · response complete and panic so we Define the stage that we would like to lock then we also Define the level for example for something we don't want to lock anything only metadata metadata and request body or metadata request body and response body so kind of everything and we can also Define for which event content we only want to save

**9:45:31** · something right we could say we only want to save something for pots we don't want to save any for secret for get events we only want to um save the request body and for delete events we want to save the request response and metadata okay so using these things we can then actually by creating an audit policy we can actually um exactly describe what kind of data should be

**9:46:04** · saved in this Hands-On session you will configure the API server to store audit locks in Json format and it's definitely important that you know how to do it yourself with a fresh Cube ADM cluster you might have to do it in the Cs as well for this we should head to our Master note and we create a new folder under SLC kubernetes we call it

**9:46:30** · audit we now just call it audit but um we could name it to anything we like we for example see there's also the pki directory already which is mounted into the cube API server po we will do the same soon with the audit folder but in

**9:46:47** · that audit folder we will now create a file called policy. yo and this will be our audit policy the one that we will work with now and for this um head to the resources section of this video there we link to our GitHub repository in the audit in section and there is a file the

**9:47:09** · first file we work with is the policy simple everything policy simple everything and we can simply copy these four lines and have a look at these we Define a policy and we only have a rule section and we only have one entry level metadata which means we lock everything on meta data level which also means we lock nothing we lock no request bodies no repon bodies okay this is done great next we would

**9:47:42** · like to enable auditing in our manifests so for this edit your Cube API server manifest and if you have to do this in the certification then you can search for auditing into kubernetes documentation and there's a section which actually

**9:48:08** · for lock backends and there we actually see all the different things that we have to enable and the mounts that we could use well you can definitely do this also go through the documentation and try to set it up yourself might be good for you but we also added a file in our GitHub repository in the same folder called Cube API server enable auditing yo so

**9:48:31** · it's just an example where we see what we actually have to do and then we just copy this over and have a look that it works okay so if this is our Cube API server manifest that we see here then at first what we have to do is we have to specify an audit policy file this is the file that we just created with our simple policy what we also have to do is

**9:48:55** · to specify the lock path so where should our locks actually be stored and this will be then our Json locks in this format we can specify the max sign of these locks and we actually specify Max backups which means this is kind of our lock rotation so we will store five backups of this file and well we have to make this

**9:49:19** · folder available inside our container which means there should be some volumes and some mounts so if I scroll down then we actually see we we should add a new volume poost path and then we should Mount this volume as well okay so go ahead and edit your kubernetes API server manifest using these additions that we have to do and I do the same

**9:49:56** · now so I added the arguments already on top we enable it and now I'll go at the volume New horsep Path volume and the volume

**9:50:19** · Mount so make sure the volume Mount won't be read only right because our API server has to write the locks into it okay that should be it let's save it and once you're done save it as well and let's hope our API server will be coming back

**9:50:59** · up and if I am now in my folder I'm on my master note now so in SLC kubernetes audit um suddenly there's a locks directory and the API server is also up and I see a file and we can tail that file output it and then we see W various things happening this looks good and we

**9:51:23** · stop this for example and we can see okay we have one example entry here this is like a lock entry it looks like Json we can see this is level metadata great we only want to lock metad data um there is some messages some authorization methods Etc and we will have a look at these events in a bit but this should be done for you you should have the same result there should be the locks file the lock file should be filled with locks and your kubernetes API server should be configured to store audit locks in Json

**9:51:56** · format in this Hands-On session we will now create a kubernetes secret and then investigate the Json audit logs that have been generated because of this well our audit logging should already be set up and we have our audit log file and if we have a look at it then various things will be generated we

**9:52:18** · will now create a secret so create a secret named very secure with any value and then we have a look okay create secret generic very secure and I will say user is

**9:52:39** · admin simple as this okay let's have a look in the audit locks so I simply grab for very secure in the audit locks and there we see there's an entry and what we can do we now simply have a look at it so every entry in the audit loog file is one line so it's like Json formatted but it will be in one line so to find one entry you can simply do a line grab

**9:53:05** · right let's have a look at that one now in a better format which we can read nicer so that you are just familiar a little bit with the format of that file so it is an event kind event and not another kubernetes event there are also other kubernetes events but this is an audit event as we see here in the API version We lock metadata level metadata we only lock metadata as of now as specified in our audit policy stage

**9:53:34** · response complete so the response was completely sent it was about creating verb was creating who did it so we have a user section here kubernetes admin we were admin when we did this yes and we also see the groups and the object reference what which object was it about well it was about secrets in the default namespace and the secret was called very secure okay there we go and um some more

**9:54:00** · information about it and this is metadata level okay so if we would have another level specified and there might be more information in this and now let's have a look what we could do if what what what will happen if we edit the secret so let's simply go and edit our existing

**9:54:25** · secret let's maybe add some more data like a password and I will simply copy the same base 64 value it doesn't matter average value so just change something on the secret save it and then search the audit locks again for it and then we see some more things were happening so feel free to have a look through some of these and get familiar um with how the Json audit logs are usually

**9:55:01** · structured and now it gets interesting in this Hands-On session we now want to restrict the lock data with our audit policy so right now the audit policy that we created it locks everything on metadata level and we now want to extend that audit policy to customize this to our needs we don't want to lock anything

**9:55:24** · from stage request received we don't want to lock anything from get watch or List verbs from secrets we only want to lock metadata level and then everything else we would like to lock on request response level when you go ahead and you change the your audit policy you can follow this procedure these steps right change the audit policy file disable audit locking in API server

**9:55:57** · and wait until it restarts enable audit logging in API server again wait till it restarts and then there are two possibilities if the API server doesn't restart so if thei Server doesn't start then we can check the vlock pods Cube system Cube API server the directory for locks for information because it will contain details um why our audit policy wasn't

**9:56:24** · accepted otherwise we can test our changes instead of disabling audit logging in the API server and enabling it again you could also move the cube API server manifest out of the directory and move it back into the Manifest directory so I suggest you have all the information you need go ahead and try to work and work on your audit policy and implement the changes as described

**9:56:54** · here I will now go ahead and do the same thing feel free to follow me along and simply or simply verify what you have done so what I would do if I faced with this task in the cks certification I would have to this documentation auditing and look for an example where we can as always steal as much as possible and there we already have an extensive example which probably contains everything that we need what do we need we don't want to

**9:57:25** · lock anything from stage request received and there we go we already have it here so we can use omit stages like this and if you want if you have to um

**9:57:41** · if you don't want to lock anything from a specific stage you can also see there's an example here here you can also have it in a rule right so even for a specific rule you can om it in stage but we now want to do it for everything so we can use it outside the rule section so do it like this comit stage

**9:58:02** · request received lock everything else on metadata level this sounds already um almost like this one but not on metadata levels but reest response so I use this one and change it to request response

**9:58:17** · which means we have already our catch all Rule and now we have to create a few other rules what do we need nothing from get watch and list verbs okay for this I have a look if there's an example which uses verbs already and there we have one awesome I simply copy this I can remove this there we go nothing from

**9:58:50** · get list and watch right nothing from get watch list there we go that should be it first rule and the one here from secrets we only want to lock metadata level okay let's have a look so I will look for something where resources is used I can simply use this one as well and or there we have already one with metadata level I copy this

**9:59:30** · one and it is about secrets well let's have a look we don't want to lock anything from request received nothing from get list watch from Secrets only metadata level and from request response everything else okay um for the weird case that I didn't make an error I will now insert an error in my file like

**10:00:03** · this save it and have have a look I will now edit my kues API server manifest and I will simply comment out the audit policy file line there we go I'll wait a bit for the API server to come up

**10:00:33** · again and it comes up again and now I enable audit logging again you can do it this as well with moving the file out of the Manifest directory and moving it back in but as far as I know simply restarting the pot doesn't work okay so now the API server probably

**10:00:59** · won't come up because I added an error in there so we can have a look into V log pods and there we actually see there are two API server entries I want the latest one of

**10:01:24** · these let's try this one no let's try the other one there we go okay down here I see

**10:01:39** · there's an error which shows could not find expected yaml error in that file okay so if you create an audit policy and you're not sure why the API server doesn't come up then there should be some messages in the locks for you okay so I remove my errors I edit the Manifest again comment out the AUD policy file save it and now wait for the API server to

**10:02:12** · comeing back

**10:02:31** · up there we go now I enable the audit policy file again and I really hope my API server will come up and I don't have another error in that file I have another look it looks okay to me I mean we copied most of it

**10:02:58** · so not that of a challenge it came back up awesome now if I tell my locks and we see there's actually much going on and there we see they already some logs having a bit more data let's see if we can find

**10:03:28** · one and let's have a look at one here we go Json formatted the thing now it is event again level request response stage response complete who sent this oh controller manager sent this interesting what was this about we have an object reference we see it's of this

**10:04:01** · API Group um of name controller manag manager in this namespace leases it was about leases so and then we actually now because it's reest response level right um we actually see that there's the whole object so it's an object lease it's of that API version we have the whole metad data and we have the whole

**10:04:23** · crazy managed fields that were added recently we have the whole spec um and this is the object from the request and then we see the object from the response so there might be more um added fields for example to it you know and yeah that's the the whole the whole thing so I would say you can if you like

**10:04:48** · go a bit ahead and verify all of the rules search through the loocks and verify that there's actually nothing from stage request received and yeah verify the others as well and again you should be comfortable with creating your own audit policy and simp simply use the example from the documentation and if there are errors make sure to check the lock directories so we did it we actually talked about auditing in kubernetes but

**10:05:20** · if you don't trust all the things that I Tau you here today or if you like to dive even a bit deeper into the topic I can recommend auditing in kubernetes 101 a great talk link is in the resources section of this video we talked about

**10:05:36** · what audit locks are why they are very useful why they are maybe even necessary in some setups we learned how we can enable them in the API server and you should be able to configure the API server for audit logging yourself in the exam sure you can use the documentation for it you should be able to filter the

**10:05:59** · audit locks by creating an audit policy or by editing an existing audit policy and again kuet documentation has great examples for this and we also learned how to investigate some of the audit logs to maybe investigate who accessed what secret or what other resource so you should be able to do this as well and you won't have a nice Json format um

**10:06:23** · available in the exam that's why the exam questions will also be presented in a way where it's not necessary to have ajacent formata on hand

### System Hardening - Kernel Hardening Tools

**10:06:47** · it's probably a good idea to talk about kernel hardening tools and what these mean in combination with kubernetes for this we'll get a simple overview what kernel hardening tools are what it means and then we look into app armor and we use it in Docker and kubernetes and we also look in set comp and use it in Docker and kubernetes in various Hands-On sessions if we have a look at container isolation so how are containers built on

**10:07:20** · top of the Linux kernel how are processors isolated well we know that we have Nam spaces and they restrict what processes can see so for example a process in a container is restricted by the other processes that it can see the other users in the system or file system access and then we also have cgroups which restrict the resource usage of processes for example Ram CPU or dis

**10:07:48** · space and we know that if we have our simple architecture like the hardware layer Linux kernel the SS call interface our libraries and our applications then we know that our applications our processes like Firefox C they could also simply run in containers and they can communicate directly with the csol interface in the kernel space right so we have the kernel space we have the user space our applications can through

**10:08:17** · libraries call with the csol interface or they can do it directly right and our containerized application process like curl here could run in a container it doesn't really matter from the perspective of the Linux kernel normally without any sandboxing container processes and call

**10:08:35** · directly communicate directly with the CIS call interface and then the CIS call interface will pass the request or communicate directly with the Linux kernel and pass request down further to the hardware so if we now talk about kernel hardening then we have to talk about that every process can communicate with the susol interface directly and we might want to restrict this right and for restricting this we can Implement another layer between the application

**10:09:05** · ation and libraries running in user space between our processes and the sus call interface and for this we can for example use SEC comp and app armor so to go further ahead we will actually look into app armor and SEC comp and use these as well in the Hands-On sessions and first we will have a look into app

**10:09:32** · armor let's talk about app armor and what app armor can do for us to create another security layer between our applications and system functionality so let's have a look let's say we have any kind of application process here on the left and then these can usually access system functionality like file system other processes network interfaces and what we can do now with app armor is that we create some kind of Shield between our processes and these

**10:10:06** · functionalities and then we only allow certain things and disallow others right and how can we control this well we control this by creating profiles so we could create an armor profile for Firefox and in that profile we Define what Firefox can do and what Firefox cannot do and then we could for example also create a profile for a kubernetes

**10:10:33** · component like the cuet running on a node it is a simple process running on the system and if app armor is installed and configured we could also create a profile for the cuet for example so that's the general idea of how to work with app armor and when we work with profiles then we can put profiles in different modes so let's talk about the three modes available the first one is unconfined which means a process can

**10:11:05** · Escape nothing is enforced then there's the complain mode which means processes can escape but it will be locked if they do so and we could then further investigate the locks and our logging infrastructure and then there's the enforce mode which means processors cannot Escape they cannot do more things

**10:11:27** · than we allow them to do in their EP armor profiles so when EP armor is in installed on the system then it comes with a few main commments for the command line which we can execute so for example there's AA status to show all profiles and their status there's gen

**10:11:48** · Prof to generate a new profile for an application we can complain so put a profile in complain mode put a profile in enforce mode and then log Prof we will also have a look at this one updates a profile according to the application needs based on the locks okay so this as a general overview

**10:12:10** · about app armor and let's jump into the Hands-On session in this Hands-On session you will get more familiar with app armor and we do this by creating a simple app armor profile for curl on our worker

**10:12:28** · note so for this head to your worker note because most of this configuration will now happen on the worker nod where our actual workloads will run and when on the worker node we will try to curl so simply curl any URL that you would like and have a

**10:12:47** · look if it works yes it works curl can communicate outside and we actually get a response back from the server with a location redirect to https so it's fine C can communicate to the outside now let's create an app armor profile for it and for this at first let's have a look at some of the app armor comments that exist already there we go and there we have for example the AA status so run AA

**10:13:15** · status and let's have a look at the output so the AA status says app armor profile is loaded which is great which is it which is is the case by default in Ubuntu and we have 25 profiles loaded 20

**10:13:31** · in enforce mode and then we see okay there are various profiles for for example one for TCP dump and we have a few in complain mode and we have none in unconfined okay so we have 25 right now let's create another one and for this we can actually or we should actually create a few more tools at first so the

**10:13:55** · tools that we should install are the app are more utils so simply type app get install app armor utils there we go and if we check now then we see we have a few more comments available and what we would like to do now is we would like to use the Gen Prof comment so n AA gen Prof for generating

**10:14:24** · a new profile and we would like to do this for curl okay so simply gen Prof for Cur and now what app armor can do is armor can look at what the process actually needs and then create the profile around it okay so the idea is to

**10:14:43** · use an application like you normally would and app armor creates automatically the profile for it and then if in the future the application suddenly does something that is not normal then it will be denied so what it

**10:14:59** · here can do we have two choices now we it can scan the system logs for for app armor events or we say no nothing don't allow anything right now and let's do this let's do F so press F there we go finish generating a profile so a profile has been generated let's check it out let's try to run curl again curl any

**10:15:22** · website again and there we see could not resolve host but it did work before okay so something has been prevented now which is great now let's have a look at the profile so we can now run again AA status to see all the profiles and if we scroll to the top then we actually see now 26 profiles are loaded and we should see our curl profile here let's have a look at the actual profile as well okay so the profiles are

**10:15:55** · located in ETC app armor D in that folder and if we have a look okay there are various profiles and there we see our user bin curl by default named after the full path to the process we can have a look in user bin Cur and then we see okay that's the default profile that has been generated okay let's just accept it like this for now and but now we would actually like for curl to allow its normal ways it's

**10:16:30** · normal doing right and what we actually did before by running curl so by running this okay by running curl killsh we actually caused CIS locks so our CIS locks were filled with app armor entries that a process tried to do something that is not allowed and these locks can app arm more used now to automatically update a profile for us so to update a profile we can say AA lock

**10:16:59** · Prof okay so AA lock Prof will check the locks and then update a profile according to the logs if we agree so run a loog Prof and there you see we have something about the profile user bin Cur okay they have been changes detect in the S loog and it would like to use

**10:17:19** · something like this open SSL yeah it's probably a good idea right so we will type A for allow and let's have a look that seems to be all the changes right would we like to save them yes so I type S for changing and there we go our profile has been updated let's have a look let's have a look in our profile if it has been updated and yes it has been changed right so now um some more uh

**10:17:49** · dependencies have been included okay has been updated let's have a look and there we go it's working again we can communicate with the server and yeah so this is the general process of how to use app armor it is very comfortable and convenient because it can automatically update and create app armor profiles for your applications

**10:18:20** · for you in this Hands-On session we now introduce Docker into the game and we will create an engine X Docker container that uses an app armor profile and we will actually download and install an app armor profile and installing a profile is also something that you should now how to do we will do

**10:18:44** · everything again on our worker note and for downloading the profile so simply head to the link in the resources section it will lead you to our GitHub repository and let's have a look so that's an app armo profile and that's like a default Docker engine X profile and we see the name of the profile is listed here in line four so it will be it is a profile it is named Docker engine X and under that name we can then later use that profile so what does it do well it for example denies some raw

**10:19:17** · networking it denies access to some directories and it denies for example access to the shell and yeah few things like this okay so it's a default one it is unlikely that you have to change or write your own profile in the exam but

**10:19:34** · you might have to work with profiles install them and then actually make pots used profiles but we'll do this later we now do it on Docker level at first to slowly get into it so copy the file simply copy the content and then we create a new file on the worker note and we'll create a new file in the app armor D directory and we call it Docker engine X just like

**10:20:06** · that paste it in there and that should be it so now how can we install an profile that we just downloaded or that we just found that we were provided with well there's also a link in the resources section which leads you to the kubernetes documentation and it is a bit hidden there is some information about it in the kubernetes documentation and we scroll down so there's a page about app armor and what they do here there's like

**10:20:33** · a screen somewhere there's an example there we go and they have like a crazy bash script um how you can install a profile on various notes it won't be necessary to do something like this in the exam you will always work with one worker and one master note but here you see the comment that's executed is actually app armor paa we simply copy that one and then execute it for theault path

**10:21:04** · of that profile there we go and then we can check with AA status again what are we having we now have 27 profiles loaded and there we have the docker engine x one and we actually see there's a Docker default one as well which comes by default with an app armor installation okay now let's use these profiles and let's see what will happen what we can do is doer run engine

**10:21:32** · X just like that to run an engine X container right what we can also do is with doer run we can specify Security Options and we can then say app armor and then we specify the profile let's say we now use for example the docker default profile to run engine X and now it runs under the docker default profile and now let's run it

**10:22:05** · under the docker engine X profile like this and then we see okay some things were already prevented right we see something like permission denied but it seems the container is still running something is still working so what we can do we simply run it with the option minus D for detaching now we have an ID and we can exec into that ID just like that so Docker exec and then the ID

**10:22:38** · and then we execute sh there we go and in there we can now try for example to do some things so like touch something in/ root doesn't work permission denied we can touch something here that works and what didn't work for example calling sh from inside the container didn't work because if we have a look at the profile that we were installing and we saw here a few things

**10:23:08** · were forbidden a few folders were forbidden things like this okay so now our process inside the container is running with an app armor profile now what we can do as well is to see that it didn't work under the default profile for example or that it did work under the default profile so let's run again a detached container with the docker default app armor

**10:23:36** · profile let's EXA into that one get a shell and now inside there we can call a shell for example and let's have a look and we can also touch something create a new file in that directory okay

**10:23:56** · so we saw how we can install an app armor profile and we can use it with a Docker container and using a app armor profile directly with a Docker container is probably not something that you have to do in the certification but I think it's nice to see how to use app armor with a process then how to use it in a Docker container and next we will actually go and use it in a kubernetes

**10:24:19** · pot and finally we reached the point we waited so long where we can actually use app armor together with kubernetes but before we do this in the Hands-On session let's talk about a few Rec requirements if we would like to do this if we would like to use f armor with kubernetes we have to make sure that our container runtime has support for ab

**10:24:43** · armor in our case we use Docker it has support for it if you use another one just be aware that it needs to support app armor app armor needs to be installed on every node right we only have one worker Noe where app armor is running and configured if you have multiple nodes to schedule your pods then it needs to be installed on everyone and and also the profile that you would like to use needs to make be made available on every note just like we installed the profile before on one note it has to be done on every

**10:25:16** · note and then we say a armor profiles are enabled are specified on per container basis not per pot basis per container and we do this using annotations and with this we will start the Hands-On session where we will create a pot which uses an app armor profile and the app armor profile which we will use is the simple Docker engine X profile that we installed before so we

**10:25:47** · will create a pot a simple engine export running on our worker node and then we configure an armor profile which kind of creates a bubble around our pot and then only allows the container and the processes inside that pot to do certain

**10:26:04** · things all right that's the idea let's go ahead and implement it follow me along for this first we should create a simple engine export for this we should do it on our Master node so I simply create a pot called secret or let's call it secure it's a secure pot it should run with an N armor profile image engine X and we need to edit the yamama of it

**10:26:39** · so we generate a very boiler plate beautiful pot specification there we go and we add annotations under metadata what kind of annotation do we need well for this we head to the kubernetes documentation and you can simply search for app armor which will lead you to this beautiful page and on

**10:27:04** · here we should see on the right side menu something like pot annotation there we go specifying the profile a container will run with exactly what we need here we have the key let's copy the key and paste it in our specification replace the container name with our container name app armor profiles will be container specific so our only container is called secure back

**10:27:33** · here so we would specify for this one the app armor profile and then we for the value we have to use the profile reference and for the profile reference we see here we use Local Host and then the profile name like this and for the profile name let's

**10:27:52** · say hello let's create a profile that doesn't exist I hope there's no profile called hello and let's try to create the PO with an annotation where the profile doesn't exist there we see it's blocked and if we describe that part do we see a reason for this waiting

**10:28:19** · blocked there we go cannot enforce app armor profile hello is not loaded okay it might it might mean that on that note where that pot is scheduled now that profile doesn't exist right and for us it is actually the case so let's go ahead and change this in the PO declaration we change it to Docker engine X like that and remember that that name is not

**10:28:46** · the file name but it is the name that is specified in that profile right so when we head to the profile shortly then we see here profile Docker engine X that's the actual name that can be used for that profile okay save the file and update that P so I delete the P at

**10:29:13** · first recreate it let's have a look if this it works so we can EXA into it using Cube CTL there we go and if we try to run s

**10:29:31** · then we see actually permission deny and if we try to touch a file in the root folder then we also see permission denied and this has the same effect as when we use the profile manually with our Docker container if you like feel free to remove The annotation run the engine x p again and you should see that

**10:29:52** · these commands and these file access should work again we will now talk about second comp what is setcom well setcom stands for secure Computing mode it is a security facility in the Linux kernel and it restricts the execution of CIS calls made by processes let's have a

**10:30:19** · closer look what this actually means if we have an application process here on the left then these can usually execute any kind of CIS call we see here on the right and with set comp the idea is now that we can restrict what kind of s calls can be made like here we forbid exac or get PID and if our process tries

**10:30:43** · to call these then the process will actually be killed and only specific ones are allowed to be called and this is actually how set comp was originally created Secom originally only allows these specific four calls exit Zig

**10:31:03** · return read and write and for write also only writing to already open file descriptor so the idea was that an application at a certain point says now apply SEC comp and from that point only these four CIS calls were allowed let's have a look at how that looked in some C code no worries you don't really have to understand it you don't have to write any c but let's have a look at a very basic program right at

**10:31:34** · a certain point of time we in our program can decide okay from now on I don't need to call any other sis calls I made already the sis calls from now on I'm only allowed for read write exit and Zig return because I as application developer know my application right and this way if later on my application gets exploited by a buffer overflow or something else and some malicious code

**10:32:02** · tries to call another sus call then the process will simply be killed that's the idea of second and here we see now marked in red that it tries to call get P ID and this will actually kill the process so here you see in the print line you should not see this because Secom jumps in now Secom is also nowadays often

**10:32:28** · combined with BPF filters and then you will read it as Secom BPF and this allows then for more fine grade control which CS CS are actually allowed which ones are forbidden and we can see this for example here where we in the beginning we create we do in set comp init we create like the CTX variable then we add some secum rules to it in this case also the read write Zig return and exit group

**10:32:57** · and we allow these okay so we kind of create a profile a setcom profile and then at a certain point now above the red marked here we actually say set comp lot so we lot our profile which means that this now marked the get P ID will

**10:33:13** · not work because the process will be killed and we will not read this print line down here so that's the idea where Secom came from and I think it's very nice to understand it and nowadays we can also use it in the um containerized world and with kubernetes as well it's time for Hands-On session where we will get to know set comp a little bit better and we do this by creating a Docker container an engine X stocking container which uses a sec comp

**10:33:47** · profile follow me along we will do everything on our worker note and first thing we have to download to create an profile a seccom profile and the link is in the resources section of the video there's a default setcom profile which we can use and if we have a look through

**10:34:06** · then we scroll a bit down it's pretty large then we see there are like various CIS call names in here already right there we go and if we scroll down then we see like there are different conditions for example P trays um allow but there maybe

**10:34:22** · some conditions like Min kernel version so feel free to have a look through it but again it's very unlikely that in the certification you have to create a seccom profile or change a profile you might have to use one and create containers using it so let's copy the whole thing okay let's copy the whole content head to our worker node and I simply create a file default.

**10:34:51** · Json paste it in and there we go we have our profile now what we can do with Docker is we now we can do Docker run engine X just like that B and we can also specify using the security op parameter we can now say second and then our file default.

**10:35:09** · Json we want to run engine X have a look okay it looked like it worked doesn't look that much different now let's have a look in our profile and let's actually change our profile what we can do is we

**10:35:29** · can search for right because we know engine X wants to write some locks so let's search for the right there we go there's the right sus call let's remove it from the list just like that okay I only know have right EV here and so I

**10:35:50** · remove the right entry save it try to run it again and there we see error unknown it didn't work okay so now we know that we apply a Secom profile in our Docker container using the security opt

**10:36:12** · argument and the time has come where we now actually use saom in kubernetes and we will create an engine expert and assign a set comp profile to it for this first step should be we have to install a seccom profile in our tuplet right so for this let's head to our worker note Here We Go From The Sessions before we actually have the default.

**10:36:35** · Json profile so how can we make it available for the cubelet to use well we have to put it in a proper directory to find out that directory we go to the C documentation and search simply for C blet set comp there we see the argument reference

**10:36:59** · for the CET and if you search for setcom and we see there actually an argument which can be passed but we don't have to because the default value is this folder so I simply copy it and try to CD into it doesn't exist so we can create that directory there we go and we then copy or I can simply move our profile into that directory

**10:37:33** · there we go and it should be now in that directory okay what can we do next well we should probably create a PO that uses this profile and for this we should still have a part from our app armor session if you don't have one don't worry simply create a simple po simple engine XP and recall it secure here and what we have to do well let's

**10:38:07** · head to the kubernetes documentation I will now remove the app armor annotations here so that's a simple po we use let's enable Secom for that pot for this we head to the Cs documentation and simply search for SEC comp and there

**10:38:24** · we should see restrict a container CIS CS with secon there we go okay let's have a look create a pot with a setcom profile there we go for this called auditing okay and here we actually see

**10:38:42** · that starting from 119 it's possible to say this in a security context and before it was possible to do it with an annotation and here we actually see this is a bit different than The annotation that has been used in the app armor when activating app armor because app armor you had to do it for every container and here you actually do it for the whole pot okay so this now is for the whole pot but let's have a look we are in 1.19

**10:39:12** · so we can simply create a security context which should then enable on Local Host the profiles audit Json let's have a look so I copied the security context section and on pot level we do it like this and our one okay let's let's leave it like audit let's create it and see what happens if a profile doesn't exist at first okay so we now try to load the profile audit.

**10:39:42** · Json it shouldn't exist so let's try let's see what happens um I will delete my pot in case it still

**10:39:59** · runs and then I create it let's have a look what will happen create container error this looks actually great so let's describe it for some more information and there we see failed to generate Security Options for container secure fail to generate that no such

**10:40:25** · file or directory audit Json expected exactly what we wanted to see so we change back into it and use the security context to change it to default. Json so this now references the actual file name if you remember for app armor it actually references the profile name so we call it default.

**10:40:49** · Json and let's have a look I will delete the PO and recreate it again container creating create container error let's have a look at describe

**10:41:13** · again there we see so it tries to load it from V liip cuet Secom profiles default Json okay so we also specified default a folder profile under it but here we actually um copied it directly in v lip cuet St comp so I simply go ahead and actually

**10:41:37** · change this here so the profiles is not necessary so it should Simply Be default ad Json and then in that folder that has been specified in the CET where we simply use the default one right

**10:41:54** · now delete the part recreate the part run container error I think this looks better right this looks better and if you now have a look at some locks that we might see there's nothing and if we describe that

**10:42:16** · pot then we see cannot be started cannot start and already running container unknown okay this looks like an restriction error it sounds similar to what we had when we tried to run an engine X container using docker so let's head back to our worker note so on my worker Noe I will now actually edit that profile and I will scroll down because if you remember we removed the

**10:42:51** · right there we go the WR s call so what I now simply do is I add back in the right CS call just like that I save it I delete my PO and recreate

**10:43:19** · it and it's running okay it's running so this means that our Secom profile has been activated and yeah so you should be able to activate a Secom profile as you see we did it with a security context now you should also be able to install a setcom profile by copying it in the proper directory the directory might have been changed using the coulet argument that we just saw and well you can enable profiles using the security

**10:43:50** · context since 119 and before you could do it V an annotation that's all we have for this section about kernel hardening tools like Amor and sa comp and the talk that I can really highly recommend you is what have sus calls Done For You Lately by Liz rice and in that one she explains

**10:44:17** · practically by creating a little application containerizing it using kernel hardening tools she explains what CS calls are and how they work another talk by Aon Jones introduction to fire jail at Armor and as Linux it is a long talk it goes a little bit into the philosophy behind these tools and it is definitely not necessary for the cks just in general if you're interested in this kind of

**10:44:47** · topic what did we talk about well we talked about sus calls in general how they work what they are we then talked about at Armor and at Armor profiles we talked about setcom and also setcom profiles we then used these in Docker to to see how they actually work how they can be used and then more importantly we use them in kubernetes and you should be able to create pods which use existing setcom profiles which use existing app armor profiles so you can use it during using um annotations or with set comp

**10:45:19** · also using security context and you should be able to install app armor profiles and set comp profiles on worker notes

### System Hardening - Reduce Attack Surface

**10:45:42** · this section will be about reducing the attack surface of our host operating system so we will step a bit outside of kubernetes and work on the Linux operating system so we will look at the host

**10:45:59** · operating system footprint what it means we look look for example at identity management user groups and for example at network access so in general we will work with a few of the common Linux command line tools that we should be familiar with when it comes to these points and if we have a look what does the tech surface mean so a tech surface can be everything that is exposed and that can contain security risks which

**10:46:27** · could be exploited by some malicious code right and if we want to have a few categories and these could be applications it could be networking and it could be identity management so when it comes to Applications then applications should always be kept up to date if we count the Linux kernel to it then yes the Linux kernel should also be always up to date and we should remove

**10:46:51** · not needed packages because any package if you have an FTP server running and you don't need it it shouldn't be there this belongs to reducing the attack surface for Network working it could be checking open ports and closing ports um putting something behind a firewall like the API server that it's not reachable from the outside identity management restricting user permissions or running applications and processes as user and not as root so let's talk about nodes in

**10:47:22** · kubernetes okay so we we have for example two worker nodes here so in general we can say that nodes should only have one purpose they should only run the kubernetes components could be the master component on a master node could be the Q blade and the Q proxy like the the worker components on a worker node um and this means we should remove unnecessary services so that means if we install if we use a default Ubunto image and just run with Cube admr cluster on it it might not be the ideal setup note recycling is something good

**10:47:54** · so nodes should be Emeral like containers so at any time you should be able to get rid of a worker node and then replace it with another one it would be even better if it would be created from images which means you don't have to create them in place you simply have images from which you create your new virtual machines and that way if they can be recycled at any time um then it's also possible to do it fast if necessary like if there's an issue with one of the worker nodes and you are already trained in your workflow to

**10:48:25** · constantly or often replace your worker noes then if the time comes and you have to fast re recycle a work or note because there has been some security risk for example then your workflow is already in place and you can do it in a fast way so this has a general overview of how nodes should be considered in

**10:48:45** · kubernetes when it comes to Linux distributions like yuntu like sentes there are various ones and the thing with these is that they often include a number of services sure they have to be comfortable they want to fight for their users right they want to create a large user base and this is all often done by offering a lot of comfort and included

**10:49:05** · services to the user so these are meant to help but widen the attack surface sure and the more existing and running Services the more convenient it is but also yeah it might open the doors for more ACH surface and we and in the certification will be focusing on

**10:49:28** · yuntu so let's simply have a look at a few comments and let me jump in a few Hands-On sessions to use these you should probably have heard and worked with netstat to see the open ports the open connections for Redhead is a different command but here we we use yuntu and you can also use lsof for it

**10:49:50** · and you can also use lsof for other things you can look for open ports which process listens to which Port but you can also check for open files for example which process has which files open it's it's very handy running Services you probably have worked with these services so like system control system CTL status CET and

**10:50:13** · you can stop services start services and also list all available services in case you should deactivate a service which is not needed and then the PS command to see running processes and yeah that one should be a really common one and in the next Hands-On sessions we will have a look at some of these in this Hands-On session we will completely disable the service snapd by using system CT snapd just as an example

**10:50:43** · service that we now picked out and it is from Snappy pronounced like a service like a package manager service which right now comes by default install with yuntu so for this we head to our Master node and let's first check the status of that service so we can run system control status snapd there we see it's active and running so what we can do is for example we can stop it and now it is

**10:51:10** · stopped we can also use system CTL to list all services and we can do it with list units so we write system CTL list units there we go there's a lot and we can for example rep for

**10:51:30** · snapd and there we see that it found some entries for it and I think we can also filter it by what is it by type service so that we actually only get the services so there we see it's only that service and we can also say only State

**10:51:49** · running there we go so we stopped it so it's not running anymore let's try to start it and see if it comes back there we go so we can do it like list units might be helpful to to find a service but the filtering that we did here now is definitely not necessary so

**10:52:11** · let's completely disabled it for this we can simply stop it there we go and then we can just say disable and this means the service is disabled and would for example not be started as well when rebooting the system so you should simply be comfortable with starting services stop Services maybe dising services using system CTL and also checking these

**10:52:39** · status in this Hands-On session we will now install and investigate services and we will simply use the two example services vsftpd and Zamba and for this head to your master note run EP get update followed by appet install vs ftpd and Zamba just like

**10:53:15** · that and it has been installed and we actually see that something has been done with system d as well they maybe have been installed as services so let's have a look at system CTL status vsftpd

**10:53:30** · here we go is up and running and Status Zamba or or it will be SMB D there we go it is actually not loaded so let's try to start it and now started it and now it seems

**10:53:47** · to be running okay so we installed the processes we checked their status and let's have a look at the processes okay so you might have used PS before so what we can simply do is PS grab vs ftpd there we go and here we actually see the P ID we see that the process is running as root and here we see what has been happening what has been actually started let's do the same for smbd and

**10:54:18** · here we see that actually a few processes have been started they run as root as well and here we see the PS of these also so okay processes have been started great what might these processes do well let's check for network interfaces so we can type netstat for example using plnt like plan and run it

**10:54:41** · and there we see okay various things are going on let's have a look we for example see our Zamba smbd and we see that it is actually listening stayed listening on Port 445 here and what else do we see as well we have vsftpd down here and we see Port

**10:55:02** · 21 okay this looks great so far so this should simply show you when you install a service how you can check the status how you can check the processes how you can check the the ports like net and for example if you would like to find an application that listens on a specific port for example something like 445 then

**10:55:25** · you can grab for it and then you see ah okay so it might be the smbd process that running on that Port so what we can do as well now we can go ahead this goes now definitely outside of what um needs to be done but for example we can have a look at the Zamba config just we do an example change now there is like a interfaces setting somewhere there we go interface so we can set the interface to

**10:55:59** · this one so we just comment this out so that it listens on Local Host instead of all the interfaces that we saw before so if we have a look here then it listens to all the interfaces right and what can we do well let's have a look add system

**10:56:18** · control and then we say restart smbd let's have a look to the status it seems to be running let's have a look at process again or let's have a look at net again actually we want to see if something changed on the

**10:56:41** · interfaces and here will see nothing has changed yet something else I had to change in that config I think B interfaces only yes okay I

**10:56:58** · restart the service I Run net that again and here we see yes now Zamba is only listening on the local interface on Port 445 okay this just as a simple demonstration you don't have to know the service uh Zamba you don't have to know the service vs ftpd just if you're not familiar with it or if you have not been familiar with this so far then it might be helpful for you to get a bit yeah used to these

**10:57:28** · tools okay in this hand on session it's now time for you to get active and to actively reduce the attack service of your master node for this find and disable the application that is listening on Port 21 so pause the video go ahead and do it

**10:57:48** · and I'll do the same now so first thing we should probably run NAD and have a look which application is actually listening on Port 21 and then we see what well that's the VSS ftpd that looks familiar we might have installed it recently we could also use lsof so lsf for interfaces and then for

**10:58:12** · 21 and there we also see that it's FTP vs ftpd and we also see the P so both are possible so now we could have a look okay how is that tool installed so I would go ahead and have a look it's probably running as a service so system control list units type service and grab for FTP and there

**10:58:42** · I see VSS ftpd is a service yes so I can do system CTL status BS ftpd and I see it is running so I stop it I verify it's not running anymore and I actually

**10:59:01** · disable it completely and now I can run my net stat again and see nothing is listening anymore on Port 21 these are different these are the pids that we see here from another process and if I run lsof again then we see nothing is listening on that Port okay so we

**10:59:23** · disabled and removed an application that was listenting on a specific port so this Hands-On session should simply make you a little bit more comfortable with Linux users on the command line if

**10:59:39** · you have already Linux experience and you locked into some servers and change users then you can definitely skip this one so let's investigate Linux users for a bit when we on our Master note then we are root because at some point in time we change into root using sud sudoi but let's have a look right now who we really are we can type who am I I am root okay good to now now let's have

**11:00:05** · a look at all the existing users in the system for this we can have a look at file HC pass and we see there are various users for example there's one for me and d d d data is a common one and we have root up here and we actually see it has ID zero

**11:00:23** · that's root and we also always see that there's a bash or there's actually passed no bash so that user won't be able to lock in using the command line so there's for example a user yuntu that we see here right now so let's try to log in s Ubuntu so can do s

**11:00:44** · Ubuntu and then we ask who am I we see we are now yuntu and what if we would like to become root again well we could do sud sudoi and now we are root again because user yuntu is allowed to become root through sudo or run root comments

**11:01:05** · under sud sudo so let's have a look at processes if we now have a look at processes all the bash processes in the system then we see okay there are a few bash processes there for example one for me Kim it has a low P ID which means it was probably started at the beginning so we have one here we have a fur root and we have one for yuntu as well so that's the idea right now um if you log in as a user and you start processes like bash then these will be run under that user

**11:01:36** · so now we have like four bash processes here so I exit again and I exit out of root which means I'm yuntu again we are now in a little bit of inception layering here I execute the commment and now we see we only have three bash processes left there's one for yuntu for example and if we exit again and look

**11:01:59** · again for the processes bash then we see there are only two processes there's the Kim one and then there's the root one and well yeah that's just a little introduction for you to processes and users and how you can find out which process runs under which user and let's

**11:02:23** · for example create a new user as well let's say we want to have a new user test so we simply say add user test we create a new password test test we can we can fill this in we can uh leave this empty that's all right so now we created a new user test let's have a look and file Etc pass VD there

**11:02:45** · we seees our new user it has automatically um assigned an directory a home directory and we also have a bash which means okay let's try to log in as user test there we go and as root you can log into every user without using a password because you are rude right but now we are user test can we confirm this

**11:03:08** · yes we are user test what if we would like to log in as user yuntu well we would have to have a password right so as a normal user you can't simply log into any other user account as rude you can well if as rude we can then let's simply try to become root right we are test user test now let's try to become root let now we have to typee in our password to become root and we are not allowed because we are not in the so-called sudas file which

**11:03:40** · defines allowances for executing comments as rot or even becoming root so we can exit out of again and we are root again and well this was just a simple introduction for you in case you weren't that familiar yet with Linux users and how to use them and switch between them on the command

**11:04:04** · line and we reach the end of this section in which we talked about the attack surface of our host operating system of our precious nodes our kubernetes noes our Master noes our worker noes which should only have one reason that should only run our kubernetes components and we looked at applications and services we can using

**11:04:29** · system control we can list existing Services we can stop Services check the status and we can even disable Services we looked at networking and ports which means using netet and lsof we are able to identify processes which are listening on specific ports then we see the command name of it and we see the P ID so yeah we can then identify the

**11:04:53** · service and stop the service and we also looked a bit into users and identity management which means we we can switch between users and we can also identify if a process is running as rude or as a different

### CKS Simulator

**11:05:21** · user I'm very happy to tell you that you're almost at the very end of your cks preparation Journey now it's time to talk about the Killer shell simulator you will get access to two cks simulator sessions which will be identical so they will have the same set of questions the very same content the idea is that you

**11:05:42** · should be already prepared so you should already be comfortable and prepared just as you would going into the real exam and then you go to the killer shell simulator and start your first simulator session try your best you probably fail a little bit and then you study the solutions after you tried the best on your own after your first simulator session you probably realize that there are some topics where you still have to study and learn a little bit and you can do so from these Solutions but also you

**11:06:11** · can come back to this course and watch some of our sections our videos our Hands-On sessions in this course again before you then head back to the simulator where you can start your second simulator session and after this you should be well prepared for the real cks exam