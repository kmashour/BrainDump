---
title: "Disaster Recovery for your Kubernetes Clusters [I] - Andy Goldstein & Steve Kriss, Heptio"
source: "https://www.youtube.com/watch?v=qRPNuT080Hk"
author:
  - "[[CNCF [Cloud Native Computing Foundation]]]"
published: 2017-12-15
created: 2026-06-23
description: "Disaster Recovery for your Kubernetes Clusters [I] - Andy Goldstein & Steve Kriss, HeptioIt’s 3am. Your pager is beeping. Your Kubernetes cluster is down. Don’t panic - we’ve got you covered. In thi"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=qRPNuT080Hk)

Disaster Recovery for your Kubernetes Clusters \[I\] - Andy Goldstein & Steve Kriss, Heptio  
  
It’s 3am. Your pager is beeping. Your Kubernetes cluster is down. Don’t panic - we’ve got you covered. In this talk, we’ll describe a variety of disaster scenarios you may encounter. We’ll arm you with the knowledge you need to overcome them. Whether you’re a systems administrator, application developer, or end user, after this talk you’ll walk away with a thorough understanding of Kubernetes disaster recovery, including:  
  
A disaster recovery overview  
\- Strategies for Kubernetes  
\- Comparisons to federation and high availability  
\- Which components to back up vs recreating from scratch  
  
How to minimize your time to recovery  
\- Automate cluster creation and infrastructure configuration  
\- Back up and quickly restore your cluster applications, workloads, and persistent volumes using tools such as Heptio Ark  
  
How to handle specific disaster scenarios  
\- Losing nodes  
\- Recovering from bad configuration updates  
\- Cloud provider outages  
  
About Andy Goldstein  
Andy Goldstein is an engineer at Heptio where he works on tooling to make operating Kubernetes clusters easier, and he also contributes to Kubernetes. Prior to his current role, Andy worked on Kubernetes and OpenShift at Red Hat. Andy lives in Rockville, MD, with his wife, two children, and two noisy cats.  
  
About Steve Kriss  
Steve Kriss is a systems engineer at Heptio working on building tools and products to help Kubernetes users be successful, and has been a contributor to upstream Kubernetes as well as a member of the Kubernetes release team in the past. Steve recently relocated to Seattle from New York and is still trying to find a good bagel.  
Join us for KubeCon + CloudNativeCon in Barcelona May 20 - 23, Shanghai June 24 - 26, and San Diego November 18 - 21! Learn more at https://kubecon.io. The conference features presentations from developers and end users of Kubernetes, Prometheus, Envoy and all of the other CNCF-hosted projects.

## Transcript

### Intro

**0:00** · hello and welcome I'm Andy Goldstein I'm Steve Chris and we are here to talk to you about disaster recovery for your kubernetes clusters a little bit about ourselves I'm a staff systems engineer at hep tio I have been programming for a long time I started with Commodore 64 basic and I'm now up using go and I've been a kubernetes contributor since 2014 and I am the hub do work team lead and I'm Steeve Chris I'm a Senior Systems Engineer at hep Tia I work on hep do arc with Andy and I've been in the past a

**0:35** · contributor to upstream kubernetes and also a member of the release team and in a past life I was an enterprise IT engineer so I certainly have some experience with the challenges of designing implementing and testing dr strategies alright can I get a show of hands how many of you manage clusters in production alright and how many of you have a disaster recovery strategy excellent and how many of you have actually used it to recover from

**1:05** · something ok a few of you so let's talk about what is it that you want in your IT infrastructure what you want is a collection of servers and services and applications that are all running perfectly well you've got your monitoring in place and all of your checkmarks are green because everything is running great but before we get to that so you want to sleep soundly at night because everything is running

**1:34** · correctly but what actually happens well at some point no matter how good your infrastructure is no matter how excellent your network is something is gonna go wrong you'll probably get a page or a phone call or a slack notification and you're gonna have to deal with it and in the short term you're probably not going to be very happy but that's ok because we're going to give you some ideas around how you

### What happens when things go wrong

**2:03** · can do disaster recovery for your kubernetes clusters so the first thing you need to do is probably do some rebuilding and some of the tools that we're going to today hopefully we'll help you with that so before we get into talking about dr4 kubernetes I want to do a quick review of what dr might look like in a more traditional IT setting so in the old world we had a pretty strong correspondence between an app and a server and so typically we would deploy a single app onto a single server now that application might be made up of multiple components and the server might

### Traditional disaster recovery

**2:39** · be virtual it might be physical but regardless there was a very strong correspondence between the application and the server and so if we ever had a disaster and we needed to recover the service for the application we need to be able to bring back the server with all of the same software configuration

**2:56** · and data as it had before and so typically the way that we would do this is we would take full backups of our server on a regular basis a nightly basis typically and if we ever had a disaster and the server went down we do a full restore from our backup bring up a new server that was essentially identical to the old one and this would enable us to restore the service for our application in the new world with kubernetes things look a little bit different than that and so now when you're running a kubernetes cluster you don't just have one server you have one

### Kubernetes Clusters

**3:31** · or more masters which are running the kubernetes control plane you have many nodes which are running again some kubernetes components as well as all of your containerized workloads and then you also have a net CD cluster which may be running in or outside of your kubernetes cluster but this is actually storing all your your kubernetes state information and so let's take a look at what's inside each of those a little bit more so within the master we have first

**3:58** · of all the kubernetes api server and this is the entry point for creating or fetching information about kubernetes state we have a scheduler which is responsible for deciding which nodes pods should run on we have a controller manager which is going to be running the core control loops to constantly push

**4:18** · the state of the kubernetes cluster towards the desired state and then we have NCD which is our persistent store of state information kubernetes and then we also potentially have some CNI pods and a cube proxy which are going to help with all the the networking and communication concerns and then on the nodes we also have cube

**4:38** · proxy and the CNI pods for networking beyond that we have all of your containerized workloads in the form of pods and so as we start to think about how to design a dr strategy for for this new kubernetes environment we really need to think about where is this state within this environment which components are stateful and which are stateless and so if we think about where state is it's

**5:04** · really in two places within this system and the first is obviously at CD that CD is the persistent store of all of the kubernetes state information contains all the specs for your deployments your services your config maps and your secrets etc and the second is in your persistent volumes for your applications so if you have workloads that are using volumes to store persistent data we obviously have a lot of state here and so these are really the key components that we need to focus on and make sure that we have robust backup strategies so that we can restore this data in the case of a failure

**5:39** · if we think about the masters and the nodes themselves that are running the core kubernetes components they're really basically stateless and so this means that if we as long as we can quickly bring up new versions of those in the case of a failure we don't really need to restore from an exact copy of the previous version of them we can spin up a new cluster and as long as we can restore our @cd data and our persistent volume data we'll be able to restore service to our applications so let's talk about master and no disaster

### Master and No Disaster Recovery

**6:11** · recovery like Steve said they're basically stateless you may have some of these that are unhealthy maybe they're running okay for the most part but you're getting some alerts you've got a disc that is flaky a network card that's not performing correctly so there's some tools you can use to take these out of service cube control has a couple of features Gordon and Drain that you'll

**6:35** · probably want to add to your toolbox Gordon allows you to mark a No is unschedulable so any new pods that are created will not be assigned to whatever node you've cordoned and drain goes one step further and will actually evict any pods that are running on a node that you're trying to take out of service and once you've done that as Steve said you want to very quickly be able to provision a replacement master or node so how do you do that automate

**7:06** · it now unfortunately we are not going to be able to tell you the one and only one way to automate recovering Andry provisioning a master or a node or a cluster because you all have opinions you have IT departments who say we're using ansible or we're using chef where we're using puppet so we can't tell you what to use but we are strongly encouraging you to automate the creation of masters nodes and clusters one thing to keep in mind is that there is a teeny

**7:37** · tiny amount of state that is necessary to preserve and those are the certificates that are used for the components in the cluster to talk to each other so when you're cubelets talk to the master or to the API servers and when the controller manager talks to the API servers there typically are SSL certificates that are used and these things you want to maintain and retain and incorporate into your automation so that when you have your ansible or your chef or your puppet and you're using that to automate provisioning all of

**8:08** · these instances you want to bring your certificates with you so that you don't lose them if you do lose them you have to regenerate them or get new ones and you potentially could have an outage in that situation and I do want to highlight that recovering the masters and the nodes is not really the crux of the disaster recovery problem stateful data is what we're really here about so let's talk about EDD CD first there's a few different ways that you can approach disaster recovery for ED CD the first

**8:39** · two are similar at the block level you could take a backup of the partition or the disk where the @ CD data directory resides this is where all of your EDD State is and with something like this if you lose one of your members if you have a highly available etsy D cluster and you definitely should if you restore from either the block device or at the file system level you just take a backup of the directory and restore it when your

**9:09** · member comes back online it will get a delta of the data that happened in the cluster since it was offline so the the surviving members will send a snapshot of what it needs to catch up and so your cluster can become whole again another option is to use sed control they have a great feature as part of the exit III API to be able to take a snapshot of your @cd database and at some point in

**9:39** · the future restore it that's someone you've got to be a little bit careful with though because if you do a snapshot and restore when you restore it ends up creating a brand new at CD cluster so this effectively means you will have an outage if you go this route but it's a good tool to have in the event that you have a total total outage you can certainly recover some of your @cd state this way assuming you have backups and then the fourth option here which is our favorite is using kubernetes itself to

**10:10** · get the information out of the API server about what's running in the cluster so the API machinery special interest group spent a lot of time building a discovery mechanism so you can go to your queue brandies api server as a client and you can say what are all of the api groups that exist and within each API group what are all other resources that exist so you can look at the core API and you can see that there are pods and deployments and our pods and secrets etc you can go to the apps API and see all the deployments and this

**10:44** · is something it's very easy to write just a loop you can iterate through everything and say tell me all the data that you have so what about persistent volumes because presumably if you've got stateful workloads in a kubernetes cluster you probably are using persistent volumes for that unfortunately I don't have a great answer here at least for a generic one because some of your data

### Persistent volumes

**11:10** · might be in cloud provider specific persistent volumes EBS volumes Azure managed disks GCE persistent disks etc so there's nothing in kubernetes that right now allows you to say take a snapshot of my PV there's a proposed a set of api's to do that but they're not available yet so if you've got kubernetes in production and you've got persistent volumes maybe you've got some tooling that you've written to do it but unfortunately you can't rely on

**11:40** · kubernetes for that and there's other volume types as well beyond just the cloud provider ones NFS volumes anything that can come in from a flex volume so how do you back those up again it tends to be roll-your-own but we have a better solution we'll get to that in a minute here with Steve yeah so I'd like to talk to you now about an open source tool we built called hep do arc and its purpose is to help with backing up some of that stateful data that we've talked about within your kubernetes cluster so what exactly does hep do arc do so it has two

### Heptio ARC

**12:18** · core features and the first one is that it enables you to backup and restore your kubernetes api objects now Andy just talked to us about some of the different options for backing those up in terms of what's in at CD and we use in our kubernetes discovery API for accessing all of that information and creating backups of it as well as restoring it in the case of a disaster and we do this for a few reasons and Andy started to talk about some of

**12:43** · the pros and cons there but you know one of the reasons we think the discovery API makes a lot of sense is that if you're running in a managed kubernetes provider you may not have access to the underlying at CD cluster and so using at CD CTL to take snapshots may not even be a feasible option for you additionally arc and using the discovery API gives you a lot of fine-grained control over what types of resources you backup so with that CD backups it's

**13:14** · really kind of all or nothing and if you want to restore your cluster you basically have to restore this state of the entire cluster if using the API though you have all the controls that it provides you in terms of filtering by namespace filtering by resource types filtering by label selectors and so we enable this all through arc and additionally if you are

**13:36** · backing up at CD directly you you don't get the benefit of being able to capture all the information that is stored for extension API mechanisms so if you have an extension API server as part of your cluster odds are that the data to support that is actually stored in a separate at CD cluster this is the recommendation for for how to design these extension mechanisms and so if you're backing up at CD you're not going to capture that information but if you use the discovery API this will actually aggregate all of that information about extension API servers and so you can just back that information up directly

**14:09** · into your your arc backup or whatever other backup mechanism you have and so we believe that the the discovery API makes a lot of sense here for accessing that information so our ques is the discovery API to to pull that all out of your cluster and it creates a tarball that stores all this information and places the backup in the object storage system of your choice now the second big feature that arc has

**14:34** · is that it will actually backup and restore your persistent volumes for you assuming you're on one of the supported cloud provider platforms and as Andy mentioned a minute ago we we use the snapshot API is that the cloud providers offer for taking backups of volumes arq out-of-the-box supports the three major public clouds but as we'll see in a minute we also have an easy way to extend the functionality of arc to support the platform of your choice so as long as there's an API for you to take backups arc can easily integrate with that now beyond those two big

**15:10** · features we have another of a number of other features that make it really easy for you to use so we support scheduled backups so rather than having to go manually create a backup you can simply configure the information you'd like to back up through our set of schedule and have those run on an automated basis over time additionally as I mentioned a

**15:31** · minute ago we support complex filtering both when you take a backup of information as well as when you do a restore of that information back into a cluster so you can filter based on the namespaces you want to backup based on the resource types and based on label selectors and so often we see that users will take a backup of their entire cluster so that they have all the information and when they go to do a restore they may do it on a namespace by namespace basis or they may only restore components that match a

**16:02** · certain label selector and so this gives you a lot of control over how you recover the information into your target cluster additionally we give you the ability to restore in two different namespaces than you backed up from and so this is really useful for use cases where maybe you have an existing namespace and you want to create a clone of it maybe for testing purposes so that you can fiddle with some configuration or maybe you have other use cases that require you to change the namespace arc makes that really easy to do now we also design

**16:36** · dart to be very extensible we recognize that we can't meet everyone's needs out of the box and so we want to give users the ability to extend our to meet their needs and so the first of these mechanisms is what's called hooks and hooks are basically a way for you as the the user of Arc to define scripts that need to be run within your pods immediately before or immediately after or backing up those pods and so a great

**17:03** · example is this is if you're if you have a pub that's running that's using a persistent volume and prior to executing a backup of that volume you actually need to freeze the file system to ensure you get a consistent backup arc makes it really easy to plug in an FS freeze command before the backup and similarly and unfreeze command right after the backup the second major way that we allow you to extend arc is through what's called plugins and so there are sort of two major categories of plugins that we support currently the first one

**17:33** · has to do with with cloud providers and so there are there are kind of two core cloud provider api's that arc relies on the first one is object storage which is where we actually store the tarball that contains all of your your @cd data and the second one is block storage and this is what allows you to take snapshots of your volumes and restore them later on and so we have a plug-in model which allows you to define your own implementations for both of these

**18:00** · and to very easily plug it into the arc server at runtime so that you can extend arc to run on your platform of choice and this doesn't require you to submit PRS to the arc the core our code base doesn't require you to recompile or maintain your own component container images the second major category of plugins is what are called item actions and we support these on both backup and restore and so these are little bits of

**18:26** · functionality that run as each item is being backed up or restored they're different from hooks in that they're not actually scripts that are being executed within your pods they're being run by the arcs server and they allow you to potentially call out to external systems to take certain actions or they allow you to actually mutate the item that you're backing up or restoring so if you need to added some annotations to items as you're backing them up add labels or

**18:52** · maybe you want to actually modify the spec as you're restoring your backup into a new cluster we make it really easy for you to plug in your own logic to do this all right so we have a demo hopefully the demo gods are with us today okay so on our script here so this

### Demo

**19:16** · is all alive so first thing we're gonna do is show you what namespaces we have and we have typical ones you'd see default cube public cube system we also have hep-c Oh arc which is where arc is running and we are using rook for dynamic provisioning for persistent volumes today so we're gonna start by deploying a simple nginx application and you'll see that this creates a namespace a PVC a deployment and a service so if we take a look at what the PVC looks like this is a rook block storage class and it is bound and

**19:51** · we are going to be storing the logs for nginx in this persistent volume so here is the PV similarly you'll see that it's bound to nginx logs and if we take a look at the deployment we want one replicas and we have one running and here is the pot so everything deployed great for us here and we're gonna go ahead and take a look at this service so we see it's got a cluster IP so let's go ahead and talk to nginx looks pretty straightforward so

**20:24** · the next thing we're gonna do here is hit it 10 more times just to get some extra traffic in the logs and we'll go ahead and exec into the nginx container so that we can see we've got a couple files in here access log bout a kilobyte nothing in the error log yet and now let's actually look at this access log so we're gonna exec into the container and take a look at that file and pretty vanilla access log we've got the initial request that we made and then the 10 after so let's create a backup it's this

**20:58** · simple you just say arc backup create give it a name and then whatever filters you want in this case we're only going to select the nginx namespace and it's done so we have an arc backup the data is available in object storage for this demo we're using Mineo deployed into the cluster but in a real world scenario you probably would want to have your data backed up outside of your cluster so it's time for a disaster we're gonna go ahead and delete the nginx namespace this will delete all of the components that we just deployed including the persistent volume that was

**21:34** · dynamically provisioned one of the great things about arc is that it can walk from the pod to the persistent volume claim to the persistent volume to figure out that there is a relationship between 3 and make sure that we backup everything that we need to be backing up alrighty so our name space has been deleted here I will prove that to you so you can see we do not have an engine x namespace anymore and just to show you that there's no longer a PV anymore that is gone we can't find it so let's go ahead and use Ark to restore

**22:09** · the backup that we just took and while this is happening I will say that when the backup was going what Steve described about doing an FS freeze before and after the snapshot was taken was exactly what we had or do today so our restore is done let's go ahead and take a look we have a PVC it's bound using the rook block storage class again and we have PV similarly so this is just going to show everything that we had before but the the individual names for anything that has a generated name like

**22:44** · the pods for example this has a different name than it did before and everything is running fantastic let's go to the service this is a different IP than we had for and we'll go ahead and take a look at that file system and again this is the log file system from the persistent volume that are stored

**23:07** · still has about a kilobyte that is wonderful let's go ahead and take a look at that file it's all of our data so we have not lost anything and just to show that we can augment it we'll go ahead and curl it another time and take a look at the file size and the file one more time so you'll see that 1045 has gone up to 1140 and if we take a look at the

**23:35** · file one last time you'll see that we had a series of requests from 20 past the hour and then the last one from 23 minutes so our backup was successful our restores was successful and we were able to continue using the data that was in the volume that we recovered and that's the end of the demo oh let me get this

**24:00** · back there we go great thanks Andy for the demo so I'd like to say please come join us in the art community so Andy and I obviously both work at hep do but Ark is completely open-source we have a number of external contributors who have been working on Ark since the initial release and so we'd love to have you come join us whether it's to provide feedback on arc whether it's to provide real-world use cases that you're using it for or whether you'd like to add features yourself please come talk to us so we're easily accessible through

### Join us

**24:29** · github or through slack we have a slack channel in the kubernetes org we have a Google Group if you'd like to subscribe for release notifications and we're on Twitter as well so please come join us and we really are looking for your input we have so many ideas about backup and recovery but I'm

**24:48** · sure you have more and specific needs so please do come and find us whether it's today or next week next month we would appreciate the input and at this point if anyone has any questions we would be happy to answer them why don't you come up to the mics I think everyone will be able to hear that'd be great take one over girl sure go ahead so in this case if you restore back a copy that doesn't include

### What happens if the backup doesnt include the pod

**25:20** · data about a pod that like happened to survive whatever outage you had what happens to that pod so is the question if the the backup didn't include the pod and then there was a restore yeah exactly um best effort for what happens I mean if you were expecting that pod to be running and it's it's not in your backup and it certainly won't be in your recovery so you just need to be careful

**25:47** · with what how you spec out your backups and make sure that you know your label selector is appropriate to match your pods and whatever else you need or you don't use label selectors and you just say I want to backup everything okay cool thanks does that answer your question sort of sort of it's sort of a kubernetes very specific question like if there are pods running on your machines that are kubernetes manages or

**26:14** · rather just containers that aren't part of pods that kubernetes knows about will kubernetes kill those or let them continue or like so kubernetes will not touch any containers that it's not responsible for okay and so similarly if you have contain that you are running manually and then you do an arc back up in an arc restore you don't know anything about those containers because kubernetes doesn't okay it doesn't like wipe and recreate okay no the cubelet will leave them untouched cool thanks sure table 1 over here right

### How to monitor a backup

**26:49** · what's the appropriate way to monitor whether a backup was successful or failed really it's a good question so we have logs that are stored per backup so when we start doing a backup you'll see that it's in progress and when the backup has completed or failed you'll be able to retrieve those logs and see what the problems were is there any way you can add like a status hook or something to just say you know just call this service web hoax script whatever to be like this didn't work that's a really good idea and it's

**27:24** · actually in line was something we are planning on doing which is in addition to the pod hooks that Steve mentioned we do want to have just overall backup level hooks so when it starts send up a web hook when it finishes what it was successful or a failure send out a notification as well yeah I don't care if it's successful just just just that it's it the other thing to note is that backups restores and and many of the other crew arc concepts are CR DS within kubernetes and so you always have the option to write a watch on the CR DS themselves and look for for failures in

**27:57** · the status that's a good pattern for now cool thank you okay so great presentation in the multi classic cig we're looking at disaster recovery use cases and trying to figure out how to do that and it's just curious whether you'd seen anybody do this particular scenario where you have like a primary cluster and a secondary cluster and something that monitors if the primary cluster goes down and then uses you know arc to basically you know

**28:27** · launch what was running on the primary on the secondary that's a very good question I don't think we've heard any specific requests around that but one of the things that is on our roadmap is being able to take a backup that was in say one region if you're on a cloud and be able to migrate that over to a different region and restore over there so that potentially could play into what you're looking to do but I think art could definitely fit into that picture in terms of monitoring and automating moving the data from cluster cluster as

**29:02** · needed and I would I would also add to that that because because Ark uses CR G's you always have the option to write a layer yourself on top of Ark that's monitoring the health of your primary cluster and if there is a disaster you can write code to basically create a restore CR D in your secondary cluster and automatically restore objects into that so that's that's something you can very easily do around arc school thanks is very helpful building block sure okay

### What causes Heptio to fail

**29:32** · I'm wondering like what are preconditions that might cause arc to fail like I asked a question before it gave me an idea what if let's say you toured that a namespace or you lost the namespace that you had backed up and you wanted to restore it but for some reason somebody brought that namespace up and maybe had some of the resources created already what would happen if I did a restore sure so what art does right now is it will try to create every single

**30:02** · object that you've specified as part of the restore and if it encounters any conflicts it logs it as a warning right or it puts it in the status as a warning right now so it's very visible when you see that the restore has completed it'll tell you if there were any errors which would be catastrophic it'll tell you if there any warnings such as there was a conflict at the present we just record

**30:24** · that fact so if there's something that's already pre-existing in the namespace we won't touch it in the future what we'd like to do is make it pluggable so that you can say on a conflict here is custom logic to run to make the decision do i patch what's in there already with what i have do I accept what's already there or do I replace what's there what came from the backup are there any types of resources that don't behave so well than when they're restored from a backup as if you know compared to just being created yes the one that I can think of

### Types of resources that dont behave well

**30:56** · off the top of my head load balancer services those depend on the UID of the service and that's not a field that is something you can mutate or set it's set by the API server itself so if you have a load balancer API service tied to say an amazon ELB if you take a backup and you do a restore you're gonna get a different one unfortunately and hopefully we can work with the community to see if we can solve that how are you typing so fast so I've got

**31:28** · to thank Joe Beda for finding his script on github I think it's called demo magic where all of that was a real demo I just was hitting Enter to get it to type for me okay thanks thank you go ahead in the middle every time so

### Performance

**31:55** · we'll go as fast as the API server will let us right now we aren't setting the QPS on the client so I believe the default is about five requests a second which certainly could be slow if you have a lot of data we do plan to make that configurable and then as far as the PV snapshots go it's as fast as your

**32:17** · cloud provider or whatever you're using can do the snapshots over here so just to tie in to the last two comments it'll be great to see it run faster actually because it takes a couple hours to do a restore something event of a major outage they'll be pretty difficult for us and you know our at CD size about 850 Meg's two to 3,000 pods and a whole ton

**32:43** · of config maps that helm leaves behind and the other thing is so what are we doing about load balancers because that's a major impediment to restore I have been involved in a little bit of discussion about that with the community I honestly don't know where it currently stands but we will be following up with that Thanks

**33:08** · I so my questions related to previous ones also how well does it interface with other things that are managing resources like if I do a home deploy it's kind of keeping track of what resources are part of the chart and something horrible happens everything goes away I restore using arc if I do another helm deploy will it pick up

### Resource Management

**33:32** · correctly or will try to start a whole new thing I'm not intimately familiar with helm but the way that our backups and restores generally work is we backup the majority of the object we may strip off status for example and then most of our objects we restore as is there's a couple of exceptions here and there so if there are certain pieces of data that

**33:59** · you need that we're accidentally stripping off or not on purpose then police file an issue if you find problems and will correct them okay great thanks I think we have time for one more over here so to answer the question earlier for load balancers there's actually an open PR to set the load balancer name which cloud providers use to look up load balancers so then they will be out here they'd be able to restore then and not rely on the UID for a name that's open so if you want to go comment on that PR we're trying to figure out a good way but also for a

**34:30** · question for arc what about resources managed outside of kubernetes like DNS to have a hook for if you need to have a new load balancer like right now to have DNS be able to update as well to have like an outside hook I think that's a great idea I would be happy to talk more about exactly where the hook would fit in and feel free to file github issue and then we can talk about it thanks thank you everyone I think we're about out of time thanks everyone