---
title: "OPA Deep Dive - Tim Hinrichs, Styra & Torin Sandall, Styra"
source: "https://www.youtube.com/watch?v=Uj2N9S58GLU"
author:
  - "[[CNCF [Cloud Native Computing Foundation]]]"
published: 2019-11-22
created: 2026-09-17
description: "Join us for Kubernetes Forums Seoul, Sydney, Bengaluru and Delhi - learn more at kubecon.io Don't miss KubeCon + CloudNativeCon 2020 events in Amsterdam March 30 - April 2, Shanghai July 28-30 and B"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Uj2N9S58GLU)

Join us for Kubernetes Forums Seoul, Sydney, Bengaluru and Delhi - learn more at kubecon.io  
  
Don't miss KubeCon + CloudNativeCon 2020 events in Amsterdam March 30 - April 2, Shanghai July 28-30 and Boston November 17-20! Learn more at kubecon.io. The conference features presentations from developers and end users of Kubernetes, Prometheus, Envoy, and all of the other CNCF-hosted projects  
  
OPA Deep Dive - Tim Hinrichs, Styra & Torin Sandall, Styra  
  
Come to this session for a deep dive on some exciting new features in the OPA project presented by the co-creators. This session will have plenty of time for Q&A!  
  
https://sched.co/Uafr

## Transcript

**0:00** · all right hi everybody thanks for coming to the open deep dive on at 5:20 on Wednesday right before the all attendee party so we're gonna talk about something very exciting day which is policy that's my favorite way to kind of unwind so I'm Tauron I'm an engineer at styro

**0:21** · and I'm one of the co-creators of open policy agent and I'm joined here by Tim who can introduce himself how y'all doing Tim Hendricks the CTO it's Tyra one of the co-creators of OPA as well so what we thought we'd do today is kind of talk a little bit about Oakland given an overview for people that might have kind of heard about it for the first time at

**0:42** · this conference and then we thought we'd do a bit of a use case deep dive and do some live coding and then kind of talk about some new features that you know we've been working on and that we plan to work on in the near future so just as like a just to get a gauge like how how many people here have heard about OPA for the first time at this conference all right all right that's a pretty good pretty good number how many of you have had heard of it before and had tried it out okay some and how many of you are

**1:12** · like maybe running it somewhere in production okay a few all right so I think this is going to be a useful session for everybody in the room so you know we talked about this a little bit in the keynote like kind of why OPA exists right and I think that like when you look at the modern kind of like cloud native like ecosystem there's just a lot of choice out there right and it feels like there's like this never-ending list of new projects to do

**1:43** · with you know CI CD and micro services and you know databases and programming languages and runtime platforms and so on right and so if you work in a large enterprise or a large organization that's just like a fact of life if you're if you're an architect or a platform engineer or somebody you know a security engineer you just have to deal with this this diversity and the the

**2:08** · challenge is that every single one of those these kind of projects typically ends up almost reinventing the wheel when it comes to policy and authorization and the result of that is is kind of an overall security posture that's hard to assess and a kind of system that's harder to control and then on top of that you know a lot of the like the older systems that help you kind of control access we're not really designed for you know modern environments that are typically very dynamic where workloads are ephemeral where they come and go and where they're

**2:37** · kind of like operating in a self-service fashion right so this was sort of the problem that we that we saw when we before we started the project and and so that's why we we thought you know let's let's try to fix this and so we we basically created the open policy agent as a way to give you a tool that you could leverage to really you know improve how systems are managed right so

**2:58** · instead of you know putting policies on wiki's or in spreadsheets you know we said there's a better way of doing this and so you know we started the open policy agent and we we released it four years ago the links to change that's nice and and yeah and so like over the

**3:15** · last you know couple years we've seen a lot of different integrations get built for open and these are all examples of integrations where people are actually running them in production right so you know you hear lots about how people are using open for kubernetes around admission control you hear lots about how people are using it for micro service API authorization but there's a long tail of use cases as well where people you know use open to control access to sensitive data in in different

**3:40** · kind of data lake environments where they use it in CI CD pipelines to you know impose best practices on on applications and configuration we even have people that use open to restrict SSH access to servers all right so you know open really is being used to unify policy across the stack one of the

**4:00** · things that we just recently launched was this little integration index on the open website so we're trying to kind of collect all of the integrations that we know about into one place where you can kind of go and browse and see see them there and in kind of one place and search for them and filter and just see what's out there because I think a lot of the time people think Oh open purpose-built for kubernetes or it only does kubernetes but the fact is that it's kind of widely applicable and and this is kind of showing off a little bit in the in the integration index actually this this screenshots out of data it looks slightly different now there's been some new additions recently so you

**4:32** · know what is Opa Opa is a general-purpose policy engine and so what that means is that you can kind of like use it to offload policy decision-making from your software now the reason we call it general-purpose is because it works with all these different kinds of software so you know whether you're talking about kubernetes or envoy or Linux Pam you know you can

**4:53** · take OPA and you can use it to basically help enforce policy or authorization decisions in those in those technologies the way that that OPA typically works with it's typically used is that services like software is integrated with it to query OPA for policy decisions when they're needed so for example if you were building a micro service and that micro service exposed an HTTP API then any time the service received an HTTP request it would be programmed to call it - OPA and ask should this HTTP request be allowed and

**5:25** · open would take the rules and and whatever other data that were required for the policy decision and it would evaluate the the query against those that those policies and produce a decision which would send back to the service to get enforced so the core thing you're kind of doing here is you're decoupling policy decision-making from policy enforcement now one of the

**5:45** · one of the design decisions that we made when we started the project which is an important one was that OPA wasn't gonna be coupled to any project or domain specific data model and so inside of these policy queries you can actually supply arbitrary JSON data you can supply any JSON value you want so this

**6:04** · can be a pod it could be a representation of an HTTP API request so it contain things like the method and the path and the headers and so on or it could be a representation of you know an ssh connection into a server and then similarly the decision that OPA sends back to the service to be enforced can also be any JSON value so we have a

**6:24** · simple API access control use case it could be true or false but it could be any JSON value so you know it could be a string it could be an error message it could be a set of strings it could be a set of error messages or it could be like a you know a complex JSON object so when people first deployed OPA for admission control and kubernetes they would just have a policy that would generate the admission review structure and send that back and that's like a deeply nested JSON object right so with

**6:51** · OPA it's kind of like just JSON coming in JSON being evaluated and JSON going out and so this is why we call it general premise now obviously your your your policies have to understand the semantics of the input right they need to understand that that's a pod represented in JSON and they need to make sense of that and similarly your your service needs how it needs to know the semantics of the the decision coming back but on its own OPA doesn't and that's why it's that's why it's general-purpose that's why you can use it for all of these different use cases

**7:24** · so what OPA actually gives you at a high level is kind of summarized here that the kind of core thing that it provides is a high-level declarative language for expressing policy in and what that language is really good at doing is helping you write rules that answer questions that are relevant to policy so things like can this user perform this operation on this resource you know which invariants does this workload you

**7:49** · know would this workload violate if it were to be deployed or you know which records am i Amaya labs or is is is a user allowed to see and so since this since we're you know operating with JSON everywhere OPA the language has kind of built-in mechanisms for you know doing everything you'd expect with large complex hierarchical data so you can kind of like dot into complex objects you can do scans over arrays you know

**8:14** · you can you can do all kinds of things when it comes to actually using OPA you can either run it you can use it as a library it's written go so you can embed it quite easily into into go services and applications or you can run it as as a daemon and the daemon is designed to be as lightweight as possible so you can use it as a sidecar or a host level daemon or if you want to stand it up as a service you can but the way that we think of OPA as the like kind of creators of it is that it's meant to be used as a host local cache for policy decision-making so we recommend that you take OPA and you run it as close to the

**8:44** · thing that needs decision-making as possible the reason why we recommend that you do that is because if every single time OPA has to or the service has to get a decision it has call out over the network then you know you like you're gonna pay a performance hit for that right there's gonna be extra latency introduced into the request path and if you're dealing with say like a micro service architecture where you know several micro services might be involved in the servicing of a top-level request then that starts to add up also importantly if every time

**9:15** · you have to make a decision you have to call out over the network then you're gonna be your availability is gonna be impacted by the network it's gonna be impacted by the machine where hope is running on and so you know the model that we recommend that you use is like you run Oprah as close to service as possible to reduce the impact on latency and reduce the impact on availability now in order to make it possible to run it like that we made certain design

**9:39** · initiatives and one of those is that on its own open doesn't kind of bring any database into the picture so you can deploy OPA it'll keep all of the policy and data that it uses to evaluate decisions in memory and when you ask it for a decision it's not going to call out over the network to get anything else on its own so all the decision-making can happen locally on that node now we do have mechanisms where you can like call out on the fly inside the policy if you want but we recommend that as much as possibly you you avoid trying to do that if you don't need to now obviously if you have a

**10:10** · bunch of oppa's running around in your infrastructure and they're all storing policy and data in memory you know you need some way to manage them you need a source of truth for the policy and the data and so open exposes a set of management api's that let you do things like distribute policy down to it so we have this thing called the bundle api where basically you can configure OPA to periodically call out to a remote HTTP endpoint and request the latest version of a set of policy and data and then OPA

**10:40** · will you know the service will respond and send that that gzipped our wall containing Rago files and json files down to open and it'll it'll activate them we also have api's for visibility though so we have like a status api that you can configure to receive status updates from OPA they tell tell you the

**10:57** · version of the bundle that's the the bundles that have been activated or whether there were any errors trying to activate the last version that it that it got and then we also have a what we call the decision log api so the session log is basically a record of all the policy decisions they've been made by OPA over the past few minutes let's say so every time you ask OPA for a policy decision it keeps a little record of that in memory and what it'll do is

**11:22** · it'll periodically upload those records to a remote HTTP endpoint and the the powerful thing there is that inside those decision log records you have the full extent of the input data the input JSON that was supplied to OPA in the policy query you also have the revision of the policy bundle and you have the decision that was made so you have a full record of the policy decision making process and so you can send that up you can use it for audit purposes it's useful for a lot of other things like debug and test as well and so the

**11:50** · last thing I'd mention here is that OPA also kind of embodies this idea of policy as code and so it's got a kind of a rich tool chain that helps you build test and debug your policies we have like an interactive shell that you can use to run queries interact with policies kind of experiment with them we have a test framework so you can write like unit tests for your policies and verify that they're correct before you go off and deploy them it's something that we recommend that people do when they when they're writing policy because it's you know you want to make sure that it's correct we had one user that was like taking OPA and they were they had to ship it to a customer and run it in an air-gapped

**12:22** · environment for a hedge fund and the ability that like to test their policies up front and gain you know confidence in the correctness before they handed this off into like an air-gapped environment where they weren't gonna be able to go in and change anything was like instrumental in their success so the test framework is a really powerful thing that you can you can use with OPA we also have like IDE into extensions so

**12:42** · there's a vs code plug-in that you can use to kind of develop the policies you can do interactive evaluation you can run tests you can get coverage it's quite useful and we also have other things like tracing and profiling that are more sort of advanced all right so this one I hand it over to Tim who's going to do a little bit of a use case deep dive so take it away thank you all

**13:05** · right so real quick we're gonna do a deep dive on kubernetes gives you sort of an example of how the integration works we saw it in the abstract a moment ago so we'll see how that works with kubernetes specifically and then we'll go ahead and do some live coding that's always fun for the audience all

**13:26** · right so this is sort of a zoom in on kubernetes we've heard a moment ago how any service whether it's kubernetes or otherwise is going to be asking OPA for decisions from time to time now in the Cooper Nettie's case this happens every time someone tries to create update or delete a resource on the cluster and so

**13:48** · as I would expect many people here already know inside of the kubernetes api server there's a there's an entire pipeline that every request goes through it starts with authentication who are you then goes on on to authorization auerbach and then finally goes to admission and at admission control there

**14:06** · are now validating web hooks there are mutating web hooks as well but there are web hooks that you can set up and that is where OPA integrates so in this world every time a new request comes into the cluster that request makes its way down to admission let's say and the kubernetes api server hands that request

**14:23** · over to OPA and then I'll show you an example of this in a moment and then OPA makes the decision is this authorized or not and it returns an admission review response that admission review response includes error messages that get returned to the user all right this is a pretty standard this is the standard integration and and there are different ways of embodying this but but that's what we're gonna see so that is OPA and then what we're gonna do now is flip over and do a little bit of live coding ok so let's do this all

**14:59** · right all right anytime that I am writing any sort of policy the first thing I do is I grab a sample of the input that's going to be handed over to OPA so in this case from kubernetes that would be an admission review request and

**15:18** · so here on the right hand side you can see that written a job JSON what I'm actually opening here is the Rago playground I forgot to mention this so this is a purpose-built editor that that is available that allows you to not only do syntax highlighting and evaluation of policy but it also allows you to share that policy with others and that's really helpful if you ever jump on a slack which we encourage definitely and you have questions put it in the playground it's much easier to exchange ideas and tips over over the playground so on the

**15:50** · right-hand side that we see the input that oppa is going to receive in this particular example for those of you who haven't seen an admission review object before this is the way it works the request there is where all the actions that it gives you a kind here it's got

**16:06** · the usual group version kind as you would expect it tells you what namespace the object belongs to if it's belongs to a namespace and then here under object is where we see what we would typically think of as the object that we're handing over the kubernetes api server so it's got metadata here it's got its got aspect because this is after all a pod it's got the containers there within

**16:30** · the spec it's got the init containers that's great and it's got an operation just create in this case alright so that's an example of the input that's going to come into the OPA and now our job as policy authors is to go ahead and write whatever policy we care about right and so in this example what we're gonna do is ensure that all the images that show up in a pod come from a trusted registry that registry is Huli calm alright so the way we're gonna get

**17:00** · this started is that we know what the input is and so I as an author there's a little bit of boilerplate for often for kubernetes I won't bother showing you the boilerplate but what I will show you is that is the core of the logic and the core of that logic at the end of the day is going to be we're going to be writing denies statements and so as you would expect with OPA it's a policy language we expect to be able to write a bunch of allows and denies so let's go ahead and start that here in OPA you're writing a

**17:26** · number of different rules we're here we're just going to write it deny and the first thing we're going to do is we're going to check that in fact we're only going to be applying this rule to pods and so how do we do that well input here is a keyword for OPA it is assigned to that value that you see on the right hand side and so if I do input dot request kind

**17:47** · kind then I can check that that is actually equal to pot all right input table request icon another everybody I would expected kind of guess what that's going to do it does that you'd expect alright so first we know it's a pod and now we want to check that all images come from this trusted registry well how are we going to do that well we're gonna start the same way we're gonna start dotting down through that object in order to grab the list of containers that exist so input dot request dot object dot spec dot containers well if

**18:19** · we kind of look at that okay so that's a that's an array of containers great okay but now we have an array of containers so we don't want to dot down through it anymore we need to iterate all right how are we gonna iterate well we're gonna iterate with some alright so we're gonna say that here there is some I and then we're

**18:39** · going to go ahead and actually grab after that I the image name so for each of the elements in this containers array we have an image field so we'll go ahead and grab it and we'll assign it to a variable image name and now we just need

**18:55** · to check that this that if this image name fails to start with Huli calm then in fact we want to deny right so not starts with starts with is what we call a built-in and OPA it's just a some pre-built code that helps us do things like string manipulation and the like image name is Hui comm alright let's

**19:17** · give it let's give it a try they may see any bugs we're good I think okay we're good alright let's go to try it isn't late it's late fine all right so let's go ahead here and hit this evaluate button and resize the window so we can see the result oh wonderful all right deny is true so why is the night true because if we look at the containers there's an image here engine X it does not come from hooli comm so that is denied this is sort of incomplete though because what we all know is that we want more information back than simply no try

**19:48** · again what we want to be able to do is return error messages and so the way that we do that is that we go ahead and add a term deny instead of a boolean verge open can return decisions that are not just true false not just boolean's but could return any JSON object we're gonna actually turn deny into basically a set think of a set is basically an array but here what we're going to do then is we're going to turn deny into a set and we're going to do and we're going to return a set of error messages back to the user so as printf pod

**20:22** · contains an image from an untrusted registry the and do image name and name all right that's right

**20:40** · all right wonderful okay so now we've got little bit more information deny your pod contains an image from okay it's Engine X as we would expect that's wonderful that's great oh and this is typically how we write policies for kubernetes we do actually turn return a set and then that met those error messages get sent back to the to the user but there's a bug anybody see it

**21:02** · just a head nod that's true that's very good that's a very deep question though work work I mentioned this earlier if we look at the input containers is one of

**21:18** · the fields under spec but so is init containers look okay so we should be checking both the containers in the init containers let's say so one way to do this is to just take this rule and we can make a copy of it and then we can just go in here and change containers to

**21:34** · init containers and then we should be good of course that's not well let's see if it work okay well that's great so now we get to answers pod that's engine X and busy box I didn't really show you but busy box is one of the init containers okay so that's okay fine but at the same

**21:53** · time nobody if you're writing code would copy and paste like that so what we might want to do is actually go ahead and add an abstraction here so one of the interesting things is that with OPA allow and and I are not keywords they're just they're just more variables you just get to make them whatever you want and so in addition to that we can we can build our own we can build a helper here called container of ste we're gonna make it another set and what we're going to do is we're going to make this true of all of the containers as well as the

**22:24** · init containers so if we do C equals of I and I should make that a some okay so now what we're saying here is go ahead and grab all the containers and the object go ahead and grab all of the init containers and the object and now I've got this set containers which I can use however I like but I'm gonna use it inside of the rule so let's give this guy I don't need him anymore and so

**22:57** · now instead of this I'm gonna do input it's gonna be let's just do container C and let's just do it this way I see that image name see that image yes see what so we see some see some I just see oh thank ya air programming okay great okay

**23:20** · so now assuming this is all right evaluate it hopefully it'll work one of the things that's happening here is that when I hit evaluate I'm actually evaluating all of those symbols in the in the policy and so what you see is output here as containers is coming in why because that was a symbol defined in the in the package down below we also see deny and denies also defined in the package one of the things we use all the time here is that we can go ahead and highlight portions of the policy in order to do a partial evaluation of it

**23:49** · it was a wrong poor choice of words there if we want to evaluate just a part of the policy then we can do it that way if you like and I'll I will stop here very quickly you can even highlight entire fragments of the policy and ask for an evaluation and there are different reasons for doing that but we're running on time okay

**24:15** · oh okay let's go through that all right let's switch I'll get it back over to Turin to start talking about new features great thanks Tim so you know what we announced at the keynote was this new ability to take Rago policies and

**24:31** · basically compile them into webassembly and actually before I get into this you know a bunch of the things we're going to talk about right now might seem a little bit like weird but they're all kind of like around this idea of improving the performance of policy evaluations that's sort of the theme that we have right now is to kind of you know sort of deliver a bunch of optimizations that really allow open to be used in some new ways that are quite interesting so what we added in the most

**24:55** · recent what we completed in the most recent release was like an incremental set of work to be able to take Rago policies and compile them down into webassembly webassembly is this standard instruction format for a virtual machine that's supported by the major browsers it allows you to take arbitrary code and get it compiled down and have it run in the browser so you can write you know a front-end in go or rust or whatever but it also supports this idea of a non web embedding and there are all these different products and companies and projects they're adding kind of web

**25:26** · assembly runtimes into there into the into the code so that they can be extended or you know support kind of like new new new new types of applications and so we thought would be great if we could leverage those those existing web assembly runtimes with OPA and so we started working on this and so now what you can do is you can use OPA to take your policies and compile them into web assembly there are two ways of kind of doing this one is just on the command line so you can give OPA basically the the policies it could be one or more policies and then a query to

**25:58** · to compile and then what open does is it basically takes that that query and those policies and it generates a plan and then it compiles that plan into a web assembly binary so this is something you'd probably end up doing in your development environment or in a CI environment whenever the policies change and then the idea is that you'll take those webassembly executables and you'll

**26:19** · publish them somewhere so they can be downloaded just like you do today with with regular OPA bundles but now instead of just shipping the raw Ray go down to the opus or the enforcement points I should say you send down these these wasum executables

**26:35** · so today we have support for like a node J s SDK so if you want to try to experiment with with this functionality that's right a kind of recommend you start is play around with it inside of node J s but in the two or three days that after we kind of talked about this and announced it somebody already started working on a c-sharp SDK as well so you know in the future we plan to have SDKs for C C++ C sharp JVM and on

**27:01** · and on there are some things that are kind of like missing today and so the plant improvements right now are around extending support for built-in functions out of out-of-the-box you can implement the built-in functions inside of the the host language the host environment if

**27:16** · you want to but obviously you don't wanna have to do that you know every single time and so we're gonna try to have more built-in functions support it out of the box as much as possible and then we're also gonna focus on on the the SDK side which will involve like adding support for the management API is right so that you can kind of have an out-of-the-box way of getting policies distribute it down to your enforcement points that's webassembly one thing that that

**27:39** · hasn't been worked on but work that we're planning to do is improve support for partial evaluation in OPA so partial evaluation is a feature that we added in in 2018 and it's got a lot of interesting applications but what it does is it basically allows you to take a policy and then kind of evaluate it to produce a new policy that's much simpler and faster to execute so for example

**28:03** · here we have a policy that says allow is true if any one of the the ackles in this data set match the input and so here what we're basically doing is we're just searching over this large ackles this this Ackles array and we're seeing if any of those match the input action resource user now obviously if that array gets really big we're still doing a linear scan and so the evaluation times going to go up and so I'll talk about how that works in a second but the important thing to notice here is that before the policy gets evaluated certain

**28:34** · pieces of the policy may be already known right so in this case data tackles is already known right it may be shipped down to OPA along with the policy itself right so the permissions are updated it would just get sent down to open the input though is a little bit different right that's unknown that changes on every single policy query and so what partial evaluation does is it kind of lets us pre evaluate the policy and remove a lot

**28:58** · of the complexity in it and simplify it into a into a format that's that's easier for oppa to understand and easier for it to optimize and so if you ran partial evaluation on this policy and you said that input was the unknown then it would produce something like on the on the right-hand side here it would give you back a set of queries that are just simple equality operations and the

**29:17** · cool thing about these equality operations is that oppa can understand them and it can build an index out of out of these these statements so that when you actually go to ask you know should this thing be allowed it doesn't have to scan over all the Ackles it can quickly look up the one the the statements that machen elite those so you'd get basically constant time evaluation today there are some like

**29:39** · limitations in partial evaluation in oppa so there's certain parts of the language that we can't partially evaluate and so the plan of the next few months will be to kind of like extend the coverage of partial evaluation to cover things like array and set comprehensions that only depend on unknown values so those will just get partially evaluated out and then we're also going to add support for the whiff keyword inside the language today if it if open counters any of those while it's partially evaluating the policy that it just saves them off and you get them in the result and so that doesn't really have any benefit I think that's it so

**30:12** · then let me let Tim kind of talk about complexity analysis where we out of it says zero zero but I don't know what that last digit is all right I'll make this super fast the other thing that we're looking at and this is again our very early it's something that is going to happen more so than it has happened is to do some automated complexity analysis so one of the things we've learned from writing lots and lots of policies is that there are quite obviously very different classes of policies like there are some for example the the one that we did a moment ago

**30:45** · where we're walking over all of the containers in the pod that run in time linear in the size of the input there are others though like for example if you were going to check if a label exists they're gonna run in time in time constant in the in the size of it of the input and so one of the things we're looking at is being able to automatically detect at least when we

**31:08** · can detect it when the pilot which class the policy belongs to and the benefit there is then that as like a cluster level administrator you could say well all of my namespace level administrators you can put policies in but only if they run in time linear in the size of the input so that's kind of where we're going with that and that's something that we can do because it was declarative because it's not turning complete that you just typically wouldn't see in a programming language yeah all right well thank you all for

**31:38** · coming we yep I think maybe we can ask your questions for as long until they kick us out but oh that's good okay so they're saying we have seven minutes there's plenty of time for questions yes

**31:56** · yes yeah so yeah that that is a thing that exists there's a built in today called HTTP send you can go and use that to head an external HTTP server as tauren mentioned at the beginning or at some point we don't recommend that unless you really need to and there are legitimate cases where there's really no other alternative rather than getting data fresh if the data comes out of a terabyte or a petabyte size database or

**32:25** · and you therefore can't replicate it into OPA or if the data is changing very frequently then and you always have to have the the latest and greatest there's not much else you can do so we do have initial support for that but as we've mentioned architectural II the goal is to avoid that push open to the edge give it all the information it needs to make decisions so that every decision can be made completely on opis own yes support

**32:57** · oh sorry we should repeat the question support for validating cryptographic signatures yeah so if you go to the so like JSON web tokens or what are you what are you thinking

**33:12** · yeah so we do have built-in support we have built-in functions to verify signatures on JSON web tokens today's we support RSA and and and other algorithms we don't have like primitives to just do that on an I like a straight leg on a array of bytes but built-in functions

**33:30** · are actually like the easiest way to contribute to opus so if you have a have a use case where you think oh this would be a lot easier like I was talking to somebody earlier today and they wanted to do something that involved bit manipulation like and and that that's not something that's particularly fun to do today in in Rago so I said yeah I mean please you know if you have use cases that require built-ins please submit a patch

**34:18** · I mean I think the well sorry the question was security context for example show up in a large number of kubernetes resources it'd be great if there were some helper libraries or the like that would allow people to write policy over all of those sort of

**34:46** · simultaneously yeah so certainly building those kinds of libraries is great and that's another good place where you can contribute so if you have ideas about libraries that would be great that that would be certainly we'd love to see that I think one thing that we've hesitated on is that with especially in the kubernetes case with CR DS people could invent things that we just don't know or understand and so at the end of the day like having a library

**35:15** · could give people a sense of security because they do false sense of security thank you when in fact they need to understand what is covered by that and what is not so that would be the the pros and cons there yeah yeah the

**35:43** · question is do we have guidelines on when you should use like a cloud providers I am versus OPA specifically around kubernetes yeah so

**36:01** · yeah so kubernetes you know it has role based access control right and and that is typically I think where people use where where I am comes in is when you're talking about authorization and like we're not trying to say that OPA should replace role based access control in any way our back solves you know some

**36:18** · portion of your your your use cases but there's sort of a long tail of things they need to be able to lock down and and you know the example the Tim game gave is not something that you can express and with role based access control or with I am or anything like that right so they're two are kind of complementary if you can express it in an I am that that's that's good but there's tons of things that you can't express and that you need something like hope before

**36:56** · what question is we pointed out using OPA for admission control has anybody ever used OPA for authentication authentication o for authorization okay yeah so for authorization a couple of times yeah we've heard people doing this it's possible there are web hooks for that yeah there's a there's a blog post from some folks at Daimler that run a

**37:23** · fairly large number of clusters and they ran into a problem where they want to just Express a blacklist basically for add authorization time as opposed to having to like whitelist the use case was like you know you want to grant developers access to every name space except cube system right it's pretty painful to do if you've got namespaces coming up all the time because you need to constantly be creating these are back objects and so you know open just lets you express that blacklist very easily so there are use cases for it however you can't dynamically configure authorization web hooks today it's a it's a cluster setup

**37:54** · thing and it's also risky to run like the authorizer on top of Kubb like because it creates this this loop so it's definitely possible if people do it but you need to have more control over your clusters than you get in some cases

**38:27** · question is well what happens if the input that comes in is malformed for example you dot down through an object that into a field that doesn't exist yeah so today this is actually a case where what we do today is just we think of all of the the conditions in a rule as that as conditions so if you were to say input request foo and a kubernetes object that would be something that we

**38:57** · look at as a condition if that if that field does not exist then the body of that rule fails it is it is effectively false roughly speaking so what we do is that that we don't return null we just the the value of that expression becomes

**39:15** · what we call undefined and then undefined propagates so there's a negation that will flip it undefined to true but otherwise undefined propagate so if you say if input dot whatever foo and input out whose not defined equal seven then the whole thing is undefined and then the the body just doesn't evaluate it true yeah that's a good question

**39:50** · so the question is are we gonna use a full are we gonna require a full y'see interface I don't know how many people in this room know what Y Z is it's a like us it's a standard that's emerging for like the system call interface basically for webassembly executables the answer is that right now the the compiled blossom policies don't have any external dependencies except for memory you need to give them an some memory to work with but yeah so they're they're kind of free on their own so you don't have to worry about that

**40:42** · question is for the bundle API how fine tunable is it and then part two was and then what happens when the bundle API actually pulls down data does it just replace everything so answer the first part is yes it's tunable you can figure how often the bundle API runs and therefore how often it pulls down fresh a fresh bundle and then for the second one oppa does support multiple bundles so it sort of has a scope when you

**41:09** · download the bundle that says here's the here's the part of the policy and data that gets replaced by this bundle yeah okay

**41:44** · so the question is whether or not you can run OPA and envoy together and and still have like a higher level control plan that's involved and I think the answer is yes when you you kind of

**41:59** · like just configure the the envoy filter basically to talk to OPA like with sto they do provide a CRT that lets you do that so it like works well there I don't know about ambassador specifically I will mention that there are there's a talk tomorrow from Yelp about how they're using open an envoy so if you are interest in that use case I'd recommend checking that out because they're doing it in a lot of different laces

**42:39** · sorry can you can you repeat the question

**42:58** · questions as I understood it was we support Jason as input today could we potentially support some binary format coming in as input all right yeah that's what I heard okay so yeah so yeah so when we say JSON we just mean kind of like any kind of complex hierarchical structured data when you run open as a daemon it exposes an HTTP API that allows you to ask it for policy decisions and that API only supports JSON today if you embed open as a library and go you could have you could

**43:28** · have like protobuf you know serialize things coming into that service and then getting passed into OPA that's that's actually how the Envoy plugin works we have a flavor of OPA for specifically integrating with Envoy yeah there's there yeah all right you've been patient

**44:09** · good question it was most of the examples are validating examples or were just accepting or rejecting a new or updated resource can you do anything around mutation and potentially provisioning so one other talk I'll call out here is tomorrow at 5:00 one yeah

**44:31** · same time goldman sachs is going to be talking about how they're doing provisioning for example provisioning auerbach in when a new name space is created they're using open to do that so i'd recommend that so yes it's possible and there's a you'll see me up again so

**44:49** · that one that reckon and then mutation yes other than yes yeah you can do it with with opa and it's on the roadmap with gate keepers something that we're kind of like discussing right now so alright well thank you very much \[Applause\]