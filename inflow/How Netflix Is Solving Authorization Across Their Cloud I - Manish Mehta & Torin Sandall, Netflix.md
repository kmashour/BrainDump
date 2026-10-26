---
title: "How Netflix Is Solving Authorization Across Their Cloud [I] - Manish Mehta & Torin Sandall, Netflix"
source: "https://www.youtube.com/watch?v=R6tUNpRpdnY"
author:
  - "[[CNCF [Cloud Native Computing Foundation]]]"
published: 2017-12-15
created: 2026-09-17
description: "How Netflix Is Solving Authorization Across Their Cloud [I] - Manish Mehta & Torin Sandall, NetflixSince 2008, Netflix has been on the cutting edge of cloud-based microservices deployments. In 2017,"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=R6tUNpRpdnY)

How Netflix Is Solving Authorization Across Their Cloud \[I\] - Manish Mehta & Torin Sandall, Netflix  
  
Since 2008, Netflix has been on the cutting edge of cloud-based microservices deployments. In 2017, Netflix is recognized as one of the industry leaders at building and operating “cloud native” systems at scale. Like many organizations, Netflix has unique security requirements for many of their workloads. This variety requires a holistic approach to authorization to address “who can do what” across a range of resources, enforcement points, and execution environments.  
  
In this talk, Manish Mehta (Senior Security Software Engineer at Netflix) and Torin Sandall (Technical Lead of the Open Policy Agent project) will present how Netflix is solving authorization across the stack in cloud native environments. The presentation shows how Netflix enforces authorization decisions at scale across various kinds of resources (e.g., HTTP APIs, gRPC methods, SSH), enforcement points (e.g., microservices, proxies, host-level daemons), and execution environments (e.g., VMs, containers) without introducing unreasonable latency. The presentation includes a deep dive into the architecture of the cloud native authorization system at Netflix as well as how authorization decisions can be offloaded to an open source, general-purpose policy engine (Open Policy Agent).  
  
This talk is targeted at engineers building and operating cloud native systems who are interested in security and authorization. The audience can expect to take away fresh ideas about how to enforce fine-grained authorization policies across stackthe cloud environment.  
  
About Manish Mehta  
Manish Mehta is Senior Security Software Engineer at Netflix, Los Gatos, CA. He has designed and developed solutions around secure bootstrapping, authentication (service and user), and authorization for cloud-native infrastructure. His professional interests and expertise are cyber security in general, and specifically in security solutions anchored in cryptography. He holds M.S. and Ph.D. in Computer Science from Univ. of Missouri - Kansas City and has authored several research and conference publications.  
  
About Torin Sandall  
Torin Sandall is the technical lead of the recent open source Open Policy Agent (OPA) project. He has spent 10 years as a software engineer working on large-scale distributed systems projects. Prior to working on the Open Policy Agent project, Torin was a senior software engineer at Cyan Inc. (acquired by Ciena Corp.) where he designed and developed core components of their SDN/NFV platform such as modelling languages as well services for resource orchestration and topology discovery. Torin has recently given talks on policy-related topics in Kubernetes at ContainerDaysPDX and LinuxCon Beijing as well as the Kubernetes Community Meeting and the Kubernetes SF meetup.  
Join us for KubeCon + CloudNativeCon in Barcelona May 20 - 23, Shanghai June 24 - 26, and San Diego November 18 - 21! Learn more at https://kubecon.io. The conference features presentations from developers and end users of Kubernetes, Prometheus, Envoy and all of the other CNCF-hosted projects.

## Transcript

### Intro

**0:00** · my name is Manish Mehra I am a security engineer at little-known company called Netflix and my projects I've been there for about four years and my projects involved secure bootstrapping PKI secrets management authentication and authorization authorization is something you're going to talk today of co-presenter turin hi everybody so my

**0:22** · name is torn sandal I'm the tech lead of the open policy agent project which we're going to talk about in this presentation I've also contributed to kubernetes and ISTE oh I love golang and high quality software so take it away ammunition all right let's get started so before we start talking about the

### Background - Definitions

**0:42** · main topic here I want to just get some background definitions out of my way using an example so let's say if I'm trying to send a request to my bank and say transfer $1,000 from account X to account Y in this particular case the bank is going to perform two steps one it is going to first verify the identity of the requester that's me that that is what we call an authentication and then verify that the requester this identity

**1:15** · is authorized to perform the requested operation that's authorization or Z now for some of you it may be really obvious but I cannot tell you how many times I get into conversations where people confuse these two things and then the conversation goes nowhere so hopefully I start off with this background definitions so we're going to talk about bullet number two not one all right now

**1:43** · one more thing I would like to say is these two steps do not need to be tied together they do not need to happen within one system they could be completely decoupled in fact I will go one step further and say if you tie them together sooner or later you're gonna lose your flexibility if you have interested in that statement you meet me afterwards I can go into deeper conversations there so some more

### Background - Netflix Architecture

**2:09** · background about Netflix's architecture so this is a very very simplified high level view of Netflix's architecture there are customers we have our bag back hand we are a cloud provider partners and then of course the CD and that basically stores your movies and shows that gets you the bytes as quick as possible to your TV now we are

**2:33** · going to focus on this big empty box today which is our back-end that runs all our control plane what we have there is a CI CD pipeline container orchestration system workflow management systems which are very similar to kubernetes if you in in many ways and I think this morning you probably caught dance keynote she she's the director who

**2:58** · manages the team under spinnaker so these are these are all the systems that basically drive and launch all the applications and workloads then we have these applications that are basically some sort of API gateway personalization account management key management legal encoding of movies and all those things and then we also have some sort of bad jobs or periodic on-demand tasks which are run in containers through our container management system called Titus now we also have some internally hosted

**3:30** · services like for storage or real-time data streaming and then we of course have employees or contractors which who are responsible to to bring these applications together and run them maintain them now this all looks simple and not maybe not too different from your setup but then things get

**3:52** · challenging when this happens they want to talk to each other right of course there are other interactions where applications go and talk to the cloud provider resources like you know storage in case of AWS it will be s3 or database or queueing but we are going to today focus only on that the interaction within within the control plane so all

**4:19** · these applications all these services are hosted by us and controlled by us now when they don't want to talk to each other you want to make sure that they have an opportunity to decide who gets to talk to them at what level so of course as I said we're not talking

**4:36** · about authentication a lot of people say when you have Network reach ability that's all we need you have network reach abilities that means somebody is authorized to talk to you not really so first of all that's not authentication and authorization is definitely not so what you want to do is you want to go much granular level not just the network reach ability but for I'll give an example so what if one of

**5:00** · these services is a rest-based service then you want to control exactly who gets to cal call what rest endpoint right so let's define this kind of problem like I just give an example of rest but it doesn't mean anything because this is a very very diverse back-end where we have rest based services G RPC

### AuthZ Problem

**5:20** · based services there's some services that have their own custom binary protocol has nothing to do with any standardization so how do you solve ODS e problem in a world like that where you have such a diverse set of services they have random different protocols that they use the random different resources that they host and is being called by people and services right so if once you

**5:44** · do that and you try to solve that problem you have to first define that problem and with this kind of diversity it feels very general so the only best thing I could do with that kind of problem at hand was come up with this definition we need a simple way to define and enforce rules that read something like this identity I can or

**6:11** · cannot perform operation Oh on resource are for all combinations of i/o and are in your ecosystem that sounds like boiling an ocean right however this problem needs to be solved because if you have any subset of this i io and R and then you have one solution for that you're gonna end up having nine solutions in your ecosystem and luscom visibly and control completely so that was not

**6:43** · an option we had to have one system that would take if not 100% like majority of your combinations of IO and R that is identities of operations and resources now just before you start building something like this you have to have your guiding principles and requirements in place so we wanted to make sure that we write down all these things before we actually propose something so first

### Design Considerations

**7:12** · thing first I don't know if you cut a dance keynote today but she did talk about like how company culture impacts tech as in the the solutions you build and it sometimes goes the other way as well where whatever you build also impacts the culture but in this particular case because this is an authorization system in a cloud native environment where you want to make things self-serve because what we have

**7:37** · at culture like core of our culture is something called freedom and responsibility where all our engineers all developers all teams are free to do whatever they want whatever it is the whatever is best for their own service now in this environment when they have their ownership of their own service they are also required to define who

**7:59** · gets to talk to their service at what level so if if a solution is not giving them that kind of freedom it's not going to fly in a company like Netflix so first thing first we have to make sure that the solution works with the company's culture second resource type as I mentioned we don't have one resource type we don't have we don't want to just do a solution for rest services or JRPG

**8:23** · of services so remember I'm talking about random stuff here not even rest and G RPC as in some sort of API cause I'm talking SSH access to so for example if you have a VM and you need a CH access into a system SSH becomes your resource right so it's not just the API call is SSH - so identities a lot of

**8:46** · identity authorization system that you will see around there mostly are back and they are LDAP based or you know some sort of ad based the the problem there is now you have to have accounts and mostly most of those systems are designed for users but here you have incoming identities that can be users and users can also be like full-time employees contractors and then you can have software which can be bad jobs which can be containers running

**9:17** · services or some of the VMs running services so all these collars need to be identified and supporting underlying protocols so as I said it could be HTTP G RPC completely custom binary protocols implementation languages so freedom responsibility again where people are free to use whatever language they prefer I mean there could be religious war about this where you know Java Scala node till Ruby Python rust all right

**9:48** · latency I think this is one of the one of the one of the requirements that I really had to think through and has actually big impact on the architecture we ended up coming with so think about a Kafka cluster right which basically has a bunch of nodes and each node has thousand requests per second now if you

**10:10** · go back to your queueing theory a little bit if your authorization decision on every request to put or get from a Kafka topic takes more than one millisecond you are thrashing you're you you you went over your service rate right that means your authorization decision has to be made in sub-millisecond otherwise you're not even serving right so in this particular case can you even think about an authorization decision that requires a network roundtrip you cannot so some

**10:40** · of these things you had to be considered flexibility of rules I think this is where touring we'll talk more about but once you have all these resources today you know your use cases today but that doesn't mean you you know and you can predict everything that is going to come next week so if your rule engine or if

**10:58** · your the way you write your policies is is hard-coded and does I actually allow you to write it in a way that it feels more like a language then you you can really restrict yourself in future so we wanted to make sure that flexibility of rule is is there and the last one I call capture of intent what I mean by this is basically when people are self served they tend to

**11:23** · make mistake they're not malicious they just didn't have their coffee right they think they did something but that's not exactly what they actually ended up writing in policy so is there is there any way to basically make sure that we give them the freedom but not enough rope to hang themselves so this is what we came up with where I think I would say at this point we will go one by one but look at service a on the bottom left

### High-level Architecture

**11:49** · and service B on the bottom right service a is a VM that is running is application code and you see a little box called G agent and on the right you have a pod which has application code and another container in the same part which is authorization agent so let's look at this architecture one by one what happens so here you have policy

**12:12** · portal where engineers or developer team team members go and go write their own policies for their own services it's a UI based system and they're able to create policies delete policies reorder the rules inside the policies and then there are sometimes we have to give some override mechanisms to you know some critical teams like you know say cops and for insects and and stuff like that and all the policies are version and stored in the database now sometimes you

**12:43** · have to write policies based on data that is not necessarily in coming from your request its from external data now for example let's say if you had a rest-based service and you say slash admin / anything is only accessible by owner of this app now in that particular

**13:02** · case you need to find out who the owner of a given app is that mapping between app and app owner is coming from some external source so in this case it could be application ownership database right or another example is okay I had this application and this application is only meant to be used by finance team okay who's in the finance

**13:24** · team that information about user verse and finance team needs to come from somewhere else probably employee management database so now you are writing all these policies and you need facts source of truth for all this information and needs to come from somewhere else so depending on in future how many different types of policies you write you may have fetch data from multiple sources so we have a concept called aggregator whose job it is to basically fetch all this data from different sources and keep it fresh then

**13:54** · there's a concept of distributor which basically pulls all the policies and related data from aggregator and keeps it hot now the difference between aggregator and distributor is distributor is fairly scalable because it keeps everything in memory you can slice and dice it and put it in different let's say cloud provider account for security and stuff like that and then you have these distributors as

**14:21** · the name says starts distributing all these policies and relevant data to the authorization agents now what happens is the authorization agents are able to then synchronously download all this information and keep it hot so you see the red arrows right there are the what I call hot path where the request comes in to the application it is going to the authorization agent and come back with the answer now I mentioned something about the latency see here that we are

**14:52** · not making a network round-trip the authorization agent is sitting on there it's right there in case of part it's still probably like right right next to each other so you're not spending a real network round term now if you do mean little bit into the

### AuthZ Agent Internals

**15:08** · agent itself it has two parts like hot path and the a synchronous part so hard part is the gray part where you the application is making a request for authorization decision whatever request you received for whatever resource is going to pass that information to to the Aged attitude to the policy engine you

**15:27** · see here we are using open policy agents engine Torian is going to talk more about it and then we have a slow path or a synchronous path which is the blue path which is downloading all this information periodically from distributors now this is all like

### Example Setup

**15:44** · architecture in T so let's take a one can concrete example in a familiar-looking setup alright so think about a very very simple rest-based payroll system and it basically has only two rest endpoints that it exposes one get salary second update salary right

**16:02** · now you want to write an authorization policy for this particular app this is what you want to write employees can read their own salaries and then salaries of anybody who reports to them right so in this case let's say Bob reports to Alice now when Bob reports to Alice Bob is able to get it his own salary but Alice is able to get her own salary and then Bob salary - this is what you want to achieve then you want to have report generator bad job some bad job kicks off every I don't know week a weekly basis and write some sort

**16:35** · of country some numbers you want to give that report generator app permission to read anybody's salary so you want something like this get charlie start and then you have let's say performance review app that is you know I don't know

**16:51** · kicks it yearly six monthly whatever your company does and goes and updates that salary of course you don't want to give access to employees to to write and post their own update salary so you say all right only that application has access to the post API at this point I'm

**17:12** · going to have handed over to Turin who will explain how all this magic happens within OPA okay thanks Manish okay so ministers gave a great overview of how Netflix is solving authorization at scale across their stack and what I think really resonates for me and for a lot of us here today is that is that so many

**17:32** · organizations are trying to solve authorization and policy enforcement at scale across all these different kinds of resource types and execution environments and languages and providers and so on now what I also really like is this desire for a general purpose solution that solves for all of these different combinations in a holistic way across the stack and so this is what we set out to do when we created the open policy agent project so

### Open Policy Agent (OPA)

**17:56** · the open policy agent or OPA as we like to call it is an open source general purpose policy engine what that means is that you can take OPA and you can apply it to any system at any layer of the stack and what you get when you use OPA is this purpose-built engine that you can use to offload policy decisions to so the idea or the way this would work is that say you're building this this service that exposes an HTTP API well

**18:21** · you would take that service and you would integrate it with OPA to execute a query against OPA when it wants to enforce access controls over who can access or who can do what via the API in that query you would supply a bunch of input like the method and the path and the headers and maybe the body and so on and then open would take that input that query and it would combine it with the policies and the data and so on and it would evaluate all of that to produce an answer like a Lauer deny which we then send back your service so that it could be enforced now

**18:50** · open itself is implemented in go and it's designed to be as lightweight as possible so you can take it and you can run it as a sidecar next to your your application or you can run it as a host level daemon or you can embed it directly into your application as a library just like Netflix is doing now I

**19:08** · said it's lightweight and the reason for that is because basically all of the policies and data that OPA uses for evaluation are kept in memory so it doesn't introduce any kind of runtime dependencies at deployment time so it doesn't depend on an external database or an external service or anything like that everything's cached in memory now

**19:23** · in addition to the the core evaluation engine that OPA gives you OPA also provides a suite of tooling that you can use to develop your policies locally so it gives you like an interactive shell to experiment with and debug policies it gives you a test framework to codify you know unit tests over it over your policies and so on now the core thing

**19:42** · that OPA gives you though is this is this high-level declarative policy language and we call that language Rago and what Rago does is it gives you the ability to write express policy as code and so what that looks like when you use Rago you write a bunch of rules in this declarative language and they answer the rules exist to answer questions or make decisions like you know can user X perform operation Y on resource Z so we

**20:06** · thought we would do is step through this example that minish set up and show how you would use OPA to enforce it so the policy in English is fairly simple it says that you know employees are allowed to read their own salary and then any button and then they can also read the salary of anybody who reports to them so let's look at how you would actually use / to enforce this so when you're using

### Example Policy (in English)

### OPA: Rules

**20:27** · open to enforce policy what you're mainly thinking about doing is writing rules they make decisions over some data and the language that OPA gives you to do that is purpose-built for writing policy and reasoning over arbitrary data and the reason for that is because when you're thinking about policy what you're thinking about is data and logic and so what you really want is a language that lets you focus on exactly that and so that's what the language is purpose-built for and so what we're

**20:53** · going to do is create a rule called allow and that rule is going to allow requests if the employee is trying to read their own salary now in order to make that decision of whether or not to allow that request or not we're going to need some data to make the decision over and so the service is going to provide some input and you can see an example of that on the on the Left so provides the the method and the path and then the authenticated user making the request and then we're gonna have the rule use that data to make a decision so you can understand this rule or you can read it as basically allow is true if the input

**21:25** · method matches get and input dot path matches get salary ID and input user matches ID now the interesting thing about this example is that that ID value is actually a variable and so that variable is going to be bound when oppa evaluates the rule to a single value across all of those expressions and so for example in the in the second expression in the rule it's going to get bound to Bob in the path and then in the

**21:49** · third expression that's going to act as like an equality check so it's gonna see whether or not the input user matches Bob and in this case it would and so the request would be allowed okay so now we're going to add another rule called allow again to handle this second case where someone is requesting the salary of an employee who reports to them and so this rules can have exactly the same structure we're going to match on the path and match on the method but

### OPA: Context-aware

**22:12** · this time we need to do something a little bit different and so the input data to the policy engine would be exactly the same it's exactly the same but we're gonna make use of additional data or context that's held in Opa and so in this case we see an example of the data on the left and so we've got the management chain saying that Bob reports to Alice and Ken and Alice reports to Ken and then what we're going to do is use that data or that context to decide whether or not to allow the request and so that's exactly what's happening in the third and fourth expression in this

**22:39** · rule so the third expression looks up the management chain for a given user and then the fourth expression searches over that management chain to see if the input user is is a manager ok and so at this point we've actually codified the entire policy using OPA but there are a couple other things that I want to point out before I head back to Manish so the

**22:58** · first thing is that in this case we have this logic that determines whether or not one user is a manager of another and while it's relatively simple you may want to have this logic reused throughout your policies and so you don't want to duplicate it you don't repeat yourself all the time and so what you want to go to do is share and reuse that and so to do that OPA gives you the ability to compose policy and what that means is that you can basically take logic and you can split it you can factor it into separate rules or separate functions and then you can call those rules or functions from from other rules and functions and so in this case

### OPA: Composable

**23:28** · we're going to do just that we're going to take the the check to for manager for managers and we're going to pull that out into a separate function that will return true if a is a manager of B and then all you do is just update the original rule obviously so what I haven't shown here though is that all of these these policies are actually contained in packages and so they're actually namespace just like you'd be used to in a in a standard programming language like NGO or Python or whatever and so that ensures that these policies are namespace correctly and that they don't run into collisions the second

### OPA: Resource-agnostic

**23:59** · thing I want to point out is that OPA is completely resource agnostic so it's not coupled to any domain specific model and this is the main reason why we can say that its general purpose because regardless of whether or not you're writing policy over HTTP api's or Kafka or SSH it's all just data to Opa Opa doesn't care matter it's all just data now obviously

### OPA: Performance

**24:23** · if you're thinking about enforcing access control in HTTP API is or message brokers your performance is going to be absolutely key and so this is something that we've designed for from the very beginning of the project and so for example if you take OPA and you try to use it to enforce a role based access control policy where the policy basically has to search for bindings that match the authenticated user and then find roles that match those bindings you see latencies of around 10 to 20 microseconds in the worst case but the really cool thing here is that even as the data set grows

**24:55** · the latency remains relatively stable and so for example in the second row there the data set that the engine actually has to search over is about six orders of magnitude larger than the first one so it scales very very nicely okay and so while you can take open today and you can use it to enforce authorization policies in your services

**25:15** · you can also use it to enforce a variety of other kinds of policies throughout the stack so for example we have integrations and we've shown how you can use it to enforce admission control policies workload placement policies management policies rights elevation and more now to do that you don't have to start from scratch because we've got a bunch of great tutorials on the website and we have a number of pre-built integrations that you can use out of the box for projects like kubernetes and docker and sto and of course we've got many more coming so I just want to say

**25:48** · that you know we're very excited about the open policy agent project because it provides this reusable building block to the community to into the ecosystem and it helps solve fundamental security problems like authorization across the stack because ultimately at the end of the day we all need a way to control who can do what throughout our systems so before I head back to Manish I just like to point out when everybody at the repo please check it out give us your stars and we also have a demo booth in the vendor area so if you're interested this kind of thing and you want to see a demo please come on by and say hi ok back to

**26:20** · you all right thanks Tori so oppa is amazing has a lot of flexibility and as you saw some of the policy snippets it's not that hard from syntax perspective however we're talking about a company like Netflix which has hundreds of teams here and then they remember go back to the original requirement of self-serve so I have to make this system self sir so these teams are very competent and

### Capturing Intent

**26:53** · everything but sometimes they forget their coffee so I really don't want them to write any complex looking code so what we had to do was basically make sure that that their life is as easy as possible when they're starting to write their policies so what we ended up doing where's take two steps so first step was we we built a UI on top of this OPA

**27:19** · language so the complexity of the language is hidden from them so I'll give you an example here for the it's an animated thing I don't know if it's very visible but this is the UI that does the exact same thing as underneath it basically converts the UI action into OPA policy so in this particular case all I'm doing is saying that this post endpoint is only accessible should be only accessible by performance review application right and then that this is

**27:52** · this is what people this is what I call capturing intent their intent is to just allow this particular application this hopefully very intuitive UI allows them to do that without making much mistakes and then if I make a second example of the get salary endpoint it's slightly more complex because has more than one rules has more than one rule because you have employee then you have manager and then you have the report generator application so in this particular case you have three rules and as you see the

**28:25** · animation is trying to do very similar stuff that OPA was showing is just that it's in UI format right fortunately in this particular case all these three rules are not overlapping so order of those rules won't matter however the the way we write policies is basically if you have ever had pleasure of configuring IP table in the past you basically have all these specific rules at the top and the generic rooms at the bottom so you can catch everything here so the way we have made this is the UI allows you to

**28:57** · arrange your rules the way you want and it will be executed in the order it was listed so that that helps write policies in a way that you know you intent will take all the questions so one more thing

**29:15** · we had to do was yes this is good and dandy but it still doesn't actually answer the question did you capture the intent because the intent is only with the person who's actually making these rules so they know in plain English what they wanna achieve but they don't actually know exactly what they did is going to perform what they think they did right so the second step we took was basically we built in unit testing mechanism in this UI so what we did and

**29:42** · fortunately I don't have screen shot for that at this point but what we ended up doing is we said okay you want to write this policy you finished writing the policy and then you write a test for it as in whatever you think you did this test should pass so you can have positive use positive unit S or negative

**30:01** · unit test and then before you actually save your policy and it gets pushed into product production it will run all the unit tests and only when this they pass your policy will be updated in the production now what happens is policy is

**30:16** · written six months later somebody wants to go and add one rule to it and they completely forget all all the intents that they had six months back so these unit tests will save their day because the unit tests are saved with the version of that policy so all the as soon as you update the policy all these unit tests that you had thought about they will run before they actually the policy is pushed into production so yeah we don't want to be a gate keeper as Diane mentioned this morning but we do want to provide the guardrails and this built in.you unit test is basically the

**30:46** · guard will let me build on top of the UI so just to summarize everything here we basically have this very diverse back-end which has all these services that are reusing random different protocols and have all these different resources that they host and they have clients that look like people and jobs and and and viens bad

### Summary

**31:09** · jobs running in containers whatnot so we had to first solve your authentication problem which we did and then once we had that we had to make sure that the the authorization system is flexible and extensible now latency was also a big deal so we I think Tory showed some numbers from opus perspective and when we did our own benchmark this was basic

**31:31** · policies could easily be done in less than 0.2 milliseconds so which works for Kafka if it was for Kafka for me it probably works for all the other services at this point inside Netflix at Netflix calcio dating coordinating updates is very hard so if you had like any kind of hard-coded rule mechanism and not using language based evaluation

**31:55** · engine you're going to have really hard time overtime to push out any sort of updates once you have language based system it is very easy to support new kind of use cases and then obviously for being culturally successful in a company like Netflix your solution has to provide something that is goes well with freedom and responsibility so having a self-serve system with a good UI and good guardrails will actually make this project very interesting and successful so in closing I would say that something

### Take Away

**32:28** · that you wanna take away is authorization is the fundamental security problem it is not new to cloud by the way it just cloud just makes it more interesting because the way it works and if you're not there yet if you're not there solving this problem yet you're gonna be there soon all right you can't just wish this one away because you know in the in our parents

**32:50** · days you had network security that was enough and definitely not enough in in cloud environment what I would say one more time is that if you are going to tackle this problem try to see how you can have a comprehensive solution rather than some hodgepodge of nine different authorization systems in your back end because the end of the day they don't talk to each other you don't have a common place that you can go and have some visibility it's going to be really messy and then you have open source projects like OPA

**33:22** · that you can make use of in fact I came to know about openly like earlier this year and this I I knew my requirements but as soon as I saw that I could switch my requirement even if let's say a language is not Turing complete it doesn't mean that it's not good enough it's still a language right so you you

**33:42** · should use go around look for open-source projects and make sure that if it fits your requirement you're you're able to get there faster and the last one I would say is you don't have to build this alone like you this problem is not necessarily new so a lot of people are thinking about it there's a very young community called Padme they had actually a session earlier today so if you are interested maybe you should get involved in community so that you can solve with other people and you may even end up learning something more about this problem and you may find some

**34:13** · more use cases you may not have thought about all right so thank you so much I think we can take couple of questions so question is what is is it available for public use what part yes so the open

### Questions?

**34:35** · policy agent that's totally open source it's been open source since day one it's a party license you can check it out on github the UI is so UI is purpose-built for Netflix at this point but I would say UI is very very specific to your use to your environment as well so and I don't think it's the biggest component of this whole project anyways so

**35:04** · how do I compare this project with HT initiative I will not try to compare this because I don't know a lot about this initiative about authorization but I would say one more thing remember I have to solve this problem for even SSH so I don't think each to others SSH right and we can we can talk later but I

**35:34** · mean this project started about a year back and I had not about heard about it still back then but yeah we can talk yeah so I should have mentioned that so

**35:49** · the question is does the distributor pick up only set of rules to send to an agent so we from day one we designed this system in a way that not only it sends the very very specific rules and only things that applicable to you but

**36:04** · the updates are Delta updates it's not sending everything anything that just change only those things are sent over the wire otherwise this will just become a mess you're right by the way we are right here for next 10 minutes or so and then if you have more questions so feel free to come by thank you so much for your time today I am I hope this was helpful