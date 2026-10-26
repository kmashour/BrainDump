---
title: "Open Policy Agent Deep Dive – Tim Hinrichs & Torin Sandall, Styra (Intermediate Skill Level)"
source: "https://www.youtube.com/watch?v=4mBJSIhs2xQ"
author:
  - "[[CNCF [Cloud Native Computing Foundation]]]"
published: 2018-05-07
created: 2026-09-24
description: "Want to view more sessions and keep the conversations going?  Join us for KubeCon + CloudNativeCon North America in Seattle, December 11 - 13, 2018 (http://bit.ly/KCCNCNA18) or in Shanghai, November 1"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=4mBJSIhs2xQ)

Want to view more sessions and keep the conversations going? Join us for KubeCon + CloudNativeCon North America in Seattle, December 11 - 13, 2018 (http://bit.ly/KCCNCNA18) or in Shanghai, November 14-15 (http://bit.ly/kccncchina18).  
  
Open Policy Agent Deep Dive – Tim Hinrichs & Torin Sandall, Styra (Intermediate Skill Level)  
  
"About Torin  
Torin Sandall is the technical lead of the open source Open Policy Agent project. Torin has spent his 10 years as a software engineer working on large-scale distributed systems projects. Torin has recently given talks on policy-related topics in Kubernetes at KubeCon, ContainerDaysPDX, Kubernetes meetups, and more. Prior to working on the Open Policy Agent project, Torin was a Senior Software Engineer at Cyan (acquired by Ciena) where he designed and developed core components of their SDN/NFV platform. Some examples of previous talks: How Netflix Is Solving Authorization At Scale (CloudNativeCon US 17): https://youtu.be/R6tUNpRpdnY?t=1041 Enforcing Bespoke Policies in Kubernetes with Admission Controllers (CloudNativeCon US 17): https://www.youtube.com/watch?v=llDI8VvkUj8 CNCF project proposal for OPA: https://github.com/cncf/toc/pull/71  
  
About Tim  
Tim Hinrichs is the CTO and Co-founder of Styra. For the last 15 years, he designed and built policy languages across different domains, most recently the CNCF Open Policy Agent and prior to that OpenStack Congress. Before Styra he worked as a kernel developer at VMware on Nicira's network virtualization product, and before that did his PhD in policy languages at Stanford University."  
Join us for KubeCon + CloudNativeCon in Barcelona May 20 - 23, Shanghai June 24 - 26, and San Diego November 18 - 21! Learn more at https://kubecon.io. The conference features presentations from developers and end users of Kubernetes, Prometheus, Envoy and all of the other CNCF-hosted projects.  
  
Join us for KubeCon + CloudNativeCon in San Diego November 18 - 21. Learn more at https://bit.ly/2XTN3ho. The conference features presentations from developers and end users of Kubernetes, Prometheus, Envoy and all of the other CNCF-hosted projects.

## Transcript

### Introduction to OPA

**0:00** · all right so I think we're gonna go ahead and get started this is an oppa deep dive the open policy agent so I wanted to first get a sense of what everybody knows about oppa so who here knows what oppa is okay good just about

**0:16** · everybody perfect how many people stop by our booth and okay and how many people went Torrens intro to oppa okay so probably most people about half have seen the demo so today what we're gonna focus on is sort of the language introduction so going deeper into the language we touched on that at the demo at the booth Turin touched on it at the at his presentation yesterday so we're

**0:43** · just gonna spend the whole time today talking about writing policy and how you do that with oppa why because that's the thing that you'll do most often right and so well that's we're gonna go through today my name is Tim Hendricks I'm one of the maintainer zuv oppa Turin has been very busy this week so we decided to have me go ahead and give this talk I've built a number of these policy systems over the last 15 years that's what I do and so and more importantly I guess I've

**1:08** · been using oppa for maybe writing policy 10 hours a week for the last I don't know how many months so I do this fairly frequently alright so and I'd like this to be pretty any are interactive so we've got a microphone of a microphone here which makes it a little bit more awkward but but go ahead and ask questions throughout and and and and please make this fun for everybody okay all right so I just want to make sure that everybody is on the same page here and give you this brief overview of oppa right the goal of oppa is or at least

### OPA Architecture

**1:38** · what oppa is is it is a domain agnostic a general purpose policy system right what that means is it you can use open to solve policy and authorization problems that any layer of your software stack right and here are some examples of the kinds of integrations that we've done with oppa we've done integrations with kubernetes to do admission control with linux to allow you to control who

**1:57** · can SSH into a server who can run sudo commands with docker to allow you to control what kinds of containers people can run with terraform to control what changes someone could make to for example a public cloud you can use OPA to express policy and authorization over micro sir Chris API is right everytime it microservice receives an API call is that authorized or not and that's what Netflix has used before all right so

**2:22** · that's the goal of over the goal of Opel is sort of this realization that we're doing policy and authorization and all these different layers of the stack today but the problem is that we're using different mechanisms to enforce those authorization policies what OPA aims to do is provide a single way a single language for expressing policy to all these different enforcement points a single toolset a single user experience right so that's the overall goal of OPA when you go to use OPA two policy enable a project or service and that's its goal right its goal is to make it very easy

**2:52** · to add rich fine-grained context or policy to an existing project or service so when you go to do that there are three steps three conceptual things that you're gonna want to think about the first of which is how do you integrate OPA with that external project how do you integrate OPA with kubernetes or with Linux or with terraform the second thing that you're gonna do is author policy and that's what we're gonna spend most of the time here today talking about and then after that you're gonna think about managing OPA which is a whole bunch of stuff around how do you deploy it how do you how do you retrieve policies audit decisions behind our

**3:22** · health we're not going to touch on that at all today what we are going to do is touch a little bit on how you integrate because integration and understanding how OPA interacts with each of these systems with each of these enforcement points is actually pretty important for understanding how you write policy all right and then we're gonna go and spend most of the time talking about the policy language and and what it provides for you all right so after we talk a bit about how policies are invoked by that external system once you've done an integration then we'll talk we've sort of broken this up into different kinds of policies and so I don't know if we'll get through

**3:53** · all of this today but these are slides we'll make them available this is sort of our training deck on the open language ok so how do our policies invoked how does the system work once it's been integrated with OPA ok so the service up above is whatever we were talking about kubernetes or Linux or whatever and then every time that that service needs an authorization or a policy decision it's going to ask OPA for that decision and the way it does that is that OPA is has an HTTP server built into it and the reason for that is

### Policy Invocation

**4:25** · it conceptually architectural II what want to have happen is that oppa is running on the same server as the service that you're integrating with and the reason that's important is because we want to guarantee that for authorization and policy decisions that that service can always get policy decisions in a highly performant highly available way right authorization is one of those key functionalities where if suddenly you cannot get authorization decisions that service up there becomes

**4:50** · a brick right it does not know what to do so we need to ensure that the service has highly available or highly performant authorization and policy decisions and for that we ensure oppa runs on the same server as the service right no worry about network partitions or network latency all right now at the same time that oppa exposes an HTTP server so that when the service / localhost hits the HTTP server in in oppa the way it does that is that when

**5:17** · that service asks for a decision it does a single HTTP POST all right and that single HTTP POST requires that you provide a policy name which is part of the URL and then the service provides a bunch of input and that input represents whatever the service knows that that it needs a decision about and we're going to go through an example in just a moment but the important thing to realize here is that when that service provides input to oppa the input is always JSON and what I mean here is that

**5:42** · it is arbitrary JSON it is an arbitrary JSON object oppa does not know or care what that object that it's sent represents when oppa once an oppa makes a decision and it makes that decision using logic which is the Rago is policy and an external data then it returns a 200 and n sends the result back to the service now the important thing to keep in mind here is that the input is JSON that we sent to oppa and the output is JSON that oppa sends back and that's important not because of serialization but because conceptually oppa only requires that the input in the output be JSON and that's why it works for any domain on the planet that's why it works

**6:17** · for all of those systems that we saw earlier one other important point here is that policy decisions are arbitrary JSON which means that they're not simply true/false answers right they're not simply authorization answers they can be answers that return let's say a host name which is a string or a rate limit which is a number or an array which is maybe the clusters that you'd like to deploy a workload to or a dictionary maybe that's a JSON patch that you'd like to apply to a Cooper he's pod before it's released into the wild right so oppa is a general purpose policy system which means it works for any domain and also it it returns policy decisions that are more than simply boolean true false answers

**6:52** · all right here's an example to drive this to make sure this is super clear all right this is an example drawn from the HTTP API authorization space right so imagine we've got a micro service and every time that micro service receives an API call it checks with OPA to see whether it's authorized or not in order for that to happen the the request that the service sends to OPA is a post at as you can see there HTTP ozzie allow that HTTP ozzie is is the policy name effectively and then the input that it provides is an encoding and JSON of the

### Simple Policies Example

**7:20** · API that that micro service wants an authorization decision about right so in this case there's a method there's a path and there's a user right which is sort of an obvious encoding of an API then there's a policy inside of OPA that makes a decision as to whether or not this API call is authorized in this case what we see is that there's a package called HTTP LZ and that corresponds exactly to the first part of that policy

**7:45** · name in the URL there in orange and then what we're gonna do is here we're gonna say that this that we're gonna this policy actually says that every API is authorized as long as the input as long as the user is Bob all right so there's some policy like that and this is a super simple one we're gonna go into more detail about how you write these and then what respond what open returns is just result is true right this this request is allowed yes

**8:16** · yeah good question so the question was can open the outside world and get additional information that it may need in order to make a decision what you see over there on the right hand side is there's that data segment alright so oppa does have an API that allows you to inject arbitrary data into oppa the idea there being that you sort of precache all of the requests that you might make to an external service inside of oppa right so that's one way that oppa gets additional information beyond what's put into the input another way that is common especially in this micro service API case is that people will

**8:48** · when they handle authentication they will put external information like that would come out of LDAP or ad into a jot token and then hand that jok token to oppa as part of the input and so that's another common way that people will get external information that you need to make policy decisions into oppa there's a third mechanism which is very new and we're not recommending to anybody use it yet but there is this functionality and oppa that we're trying out which during policy evaluation it you can go out and hit an external database for HTTP server yeah good question okay so any other any

**9:22** · questions about invoking policy all right so so sorry one thing I'll drive home here is it this input in this example has a method path and user that is the right thing to do let's say for HTTP API authorization but oppa does not know or care what any of those fields mean the method the path of the user does not care at all if this were SSH maybe the input would be a user and some other metadata about the server right what's reach region is it in is it for prod etcetera if this were a kubernetes example then the input that you give to opal would be like a user maybe the API

**9:53** · that that user is calling like create pod and then another field which is like the the yam well description of that pod that we've all seen and know and love from kubernetes okay so open does not know or care what that input is and that's why it works for any domain okay we had a question here

**10:16** · yes no it does not it does not store mutable state OPA is entirely stateless well it's not entirely stateless the decisions it makes are entirely based on the state that it has you could like from outside go and like after the service gets a decision it could push new state into OPA through that JSON we've not reckoned we've not recommended that another question yeah a question is can we secure communication between servers and OPA yes mutual TOS anything else okay good all

**10:51** · right so first kind of policies we're gonna look at we were calling simple here lack of a better term and and the idea here is that any when you're writing policy the first thing you think about is what is the input that's coming into this policy in order for me to make a decision right and so in this example we've shown micro-service api's and this was exactly the same example we just talked through now the first thing you need to do in order to sort of make a decision about this particular input is

### Policy Language Basics

**11:16** · what well you have to need you have to be able to look up the values it showed up in the input right so you may need to look up well the the what is the method what is the user what is the path and if you see there on the right-hand side that's how you do it you do in the obvious way input here is a key word in OPA and it what it does is it's the root of that JSON document that was handed into OPA as input and now once you can look up different values you need to be able to compare them so input method

**11:40** · equals get is doing the ava's sing and put dot path of zero that's referencing the first array element inside of the path field that we're given as input and then input that user does not equal input that method is doing what you would expect we've got 50 operators they go beyond simple equality checks inside of OPA and what I'm doing when I'm writing policy day-in and day-out is I usually have that open in a tab in my browser all right OPA also lets you

**12:06** · assign variables as you might expect you have common logic and and and so using those kind of intermediate temporary variables is valuable here path : equals input path is doing the obvious thing it's it's creating a new variable called path and it's assigning at the value of input path once you have those intermediate variables it is just a variable that holds a JSON object and you can use that just like any other JSON object you can dereference it with array indexes dot into it like a dictionary and so on and so forth when you start looking at the

**12:37** · documentation one of the things that we'll say we'll start using terms like a head and a body so of a rule right so a rule here is just an assertion a statement that makes a policy decision so in this rule we're just saying that allow is true exactly when the input method is again the input user is Bob all right now the rule sorry every rule has a head in the body and you'll see that in the docs and so here the the first part of it is the rule head allows true the name of the rule here is allow and the value is true one thing that we

**13:08** · do is that there is a default or implicit assumption that if you do not tell us what the type of the variable is what the value is that you're assigning it in the head then then by default you're saying that that should be true and that's why we can write these simple a while statements that you saw before the rule body is everything inside those curly braces and then all of the statements inside the rule body are ANDed together all right I think that's here yes they're ANDed together if you want an or oh sorry in this statement what we're saying is it allow is true if

**13:38** · and put-down method is get and the and the user requesting making the API request is Bob if you want to have an or than you write multiple statements right this is what you would expect you can use the same rule head multiple times just like you would expect first simple

**13:57** · allow and anon rules language and and then there's a question here which is well suppose you've got 10 or a hundred or a thousand of these allow statements what happens if none of them apply what does the value of allow in that case and by default allow or any other variable is undefined if none of the rules apply to it now of course that's not always what you want and so there is a key word here within OPA that allows you to specify what the default value of any of these variables is and that is here here

**14:28** · we have an example where we say default of allow equals false syntax is what you might expect you just stick a default in turn and on the front of an assignment all right you can only use one default / / rule and oppa will complain and tell you if you've made that made a mistake there alright the one of the common things that that people ask is well I you know this is I'm used to writing programs all the time I'm used to writing functions to factor out common logic so it can open do that the answer is yes so let's

### Functions and Modularization

**15:00** · look at a slightly different input this time path is represented as a string here instead of an array as we had previously and that's sort of the the thing that you might expect out of the gate um and now we have a rule and when we write this rule to encode the same logic that we had before we need to do some string manipulation to actually parse that URL and and pull out the

**15:21** · components of it to do whatever checking that we need to do ok and so what you see here is that this what's in this box is just some very common string manipulation and if you had ten ten different allow statements you'd have to repeat that string manipulation logic in each and every one of those rules well obviously oppa has accounted for

**15:39** · this and in the language what we allow you to do is create a function and this is a function that means is basically the same thing as any function in any programming language here split path is a function that we've defined it just encapsulate that common logic now functions actually turn out to simply be rules that take arguments all right so all the same things that I said about rules a moment ago apply to functions as well you can use the same function name in multiple rules as you see up here and

**16:10** · the only real restriction here is that when you do an evaluation there's only one answer that ever comes out of a function right as you would expect

**16:28** · yeah so the question here is what is what is the semantics in terms of ordering so does it just evaluate top to bottom in terms of the rules does it stop once it's found one what happens there so the with oppa order the order

**16:43** · in which you write statements is completely irrelevant so you can write them in any order and the meaning of the the language the meaning of your policy remains the same there are constructs that if you want to have ordering put in place and you can in fact do that so we don't cover that here but there's an else keyword that allows you to simply chain things together and then so you can do that kind of thing it's yes

**17:07** · what's that Oh regular expressions yeah so one of those or one or two of the operators that we have and in that list of 50 handles regular expressions yes yes

**17:36** · across open deployments uh-huh yeah oh sorry the question was is there an easy way to share common functions across different open deployments one of the

**17:52** · things we'll see a little later is that OPA does allow you to create multiple policies and then you can import one policy from another just like you wouldn't Python or any programming language and so that would allow you to share a common function let's say across multiple policies for sure now in terms of sharing it across multiple oppa like deployments you would have to replicate the policies there yeah okay oh yeah

**18:21** · okay I forgot to mention here so this equals true trick where you don't have to write equals true is the same for functions as it is for rules great okay so enough for functions one of the things that I already mentioned because it came up in a question is that one of the cool things about opens it you can use external context information about what's going on the world in order to make policy decisions so for so for

### External Data Integration

**18:43** · kubernetes the integration that we did this is incredibly valuable and we use this for example what we do when with kubernetes is we load into OPA all of the information all the metadata about the pods and all the namespaces that exist and so when you're making an admission control decision with an OPA you can use all the information about what the other pods are in order to make an authorization or an admission control decision so for example if you wanted to say in OPA that in every namespace there can be at most one pod called default

**19:13** · then you can do that but obviously you can't do that if you don't have all the information about what the other pods and all the other namespaces actually are so when we do the integration with OPA we are injecting into OPA all the information from kubernetes has about the other pods the way that you do that is that you run again it's a very simple one-liner HTTP call where you put at a particular path again it's sort of the name that you'd like to associate with this data and then the body of the put is simply the json object that you want

**19:44** · to be there right so super simple to load any any kind of context on the planet and this is incredibly powerful because it means that like again you can use data about kubernetes or you can use data about a calendar you can use data about anything on the planet to make policy decisions yeah yeah so the

**20:04** · question is how do you keep it in sync and the answer is that has to happen outside of OPA right OPA allows you to inject it and so then it depends a bit on what system you're integrating with how you how you keep that up to date right so like ad for example has a way you can you can listen to deltas and then you could push those into OPA coober kubernetes has a similar thing and you can set up a watch to get a stream of updates and you can keep keep up to date that way but that is a code that is specific to the integration that you're doing and so that that just has to live outside of it well yeah yes so

**20:42** · that's really limited by your by memory right there's no open doesn't really know or care obviously if you start trying to shove a terabyte of data into OPA you should think real hard about whether that's a that's a good idea all of the policies and data and open are stored in memory and so and that's a you know a design decision that we made because for us OPA is really this host local cache to ensure that other service that needs authorization decisions can get them very quickly and so we just put put all that in memory yeah

**21:18** · what was the first part if there are means of people or pre-processing well again the thing that's yeah so the question is can you pre process data before you push it into oppa one of the goals of oppa is to allow you to push just any arbitrary raw JSON in so that you can make authorization decisions about that using that data and so we don't require anything other than it's got to be JSON so if you want to do pre-processing then then you would do that outside of oppa and then and push it in and JSON one of the things that you'll see in the language if I may not remember to hit on

**21:54** · this again but one of the things you can do with the language is do is introduce sort of virtual JSON documents that allow you to sort of say well look the data that comes in is not in a great form for me to write policy over and so what you can do is sort of insert a layer these virtual documents between the raw data that comes in and the policies that you'd actually like to write and then so doing you can do a little bit of that ETL yeah in the back

**22:42** · yes so like you're talking about Oh sir the question is have we thought about adding documentation functionality so that somebody who doesn't know the internals of of the policy can have some idea as to what it's what its semantics are so yeah so this is something on the list where yeah it'd be great if we had you know some like Javadoc kind of functionality where as you write policy you annotate the policy and then the tool will spit out nice Docs for that so yeah that's just on the list having done it we'd love contributions so if you have ideas yeah yeah yeah so it's a good

**23:23** · question I'm not gonna demo here we didn't demo it yesterday but there is functionality inside of OPA to say give me a trace of the decision that you made and then we even for awhile tried to go and and sort of prune that trace down to like the minimal that you actually needed to understand why the decision was made the way it was but that's in there and again it needs some work so if you're we'd love to help yes

**23:56** · so yeah question was can you can you merge data and when you send it into OPA so there is a JSON patch so you can use that to just push deltas in and then again in the policy language if you were trying to actually merge data like you had you know users from ad and users from LDAP and you wanted all users then you can express that idea within the policy language using a virtual document

**24:20** · and then write your policy on top of that that virtual document yeah okay Wow lots of questions good all right is there a question is is there a way to index the data so yes index to the data itself we did have that for a while I

**24:38** · think we've removed it recently we just need to put it back in but yes in terms of performance there is this question once you start shoving arbitrary JSON in there you do want to make sure that it's going to perform the the way you want and there are some just basic tricks when we've worked with people in the past what we've said is it's like look just use a dictionary to do you know constant time lookup so that we're not doing linear scans of like arrays and that has typically been enough but yes

**25:04** · there is indexing like reverse indexing doing static analysis over the policies to figure out what indexes are appropriate and then building those lazily over during evaluation yes yeah so the question is can you enforce schema on the data coming in during policy evaluation and again this is another one on our wish list so please help us out not today one of the observations that we've made though is that from the services point of view if even assuming that once we

**25:35** · have this sort of schema checking in place on the inputs then you know imagine the service gives opis and bad data it still needs an authorization decision right like we can't forget that that thing assumes it is going to get a decision back so once we have the schema checking in there we can get an error and then it's like what does it do right I don't know and so but yes schema

**25:55** · checking something that we're gonna do the one thing that we do do today is we do type inference over all the policy that exists and so as and so you know it'll figure out things like well you're referencing a field that doesn't exist or you're using a string what when it's really a number and so we do that kind of thing so all we need to do is now add the schema declarations for the inputs and the what we call the base documents which is this data over here that we're injecting and then we'll be able to do full analysis over everything yeah the

**26:29** · question is if there's an an error on one of the rules how does that get returned to the sender so there are different cases right like so opah is pretty forgiving in the language itself so if you like dot into a dictionary and that dictionary doesn't have that field it'll just go ahead and say well that's undefined like that that particular rule is undefined and so then it will continue evaluation because there may very well be another rule that permits or denies that request

**26:54** · so one of the so you so the return values that you can get out of OPA are effectively of a JSON value you can get undefined and then and then you can get an error yeah okay let me give you a

**27:09** · quick example of how you use context once you've injected it into OPA here the idea is that now on the left-hand side in addition to input we also have this data and and we're and I'm using the term data because data is another keyword inside of OPA so if you're trying to reference the information that comes in as part of the input you use the keyword input if you're trying to

**27:28** · reference information that's been injected via context you use the keyword data so over here on the right-hand side what you see is that the first allow statement is just using input the second allowed statement and what that's saying is that users can access their own salary so here we're just doing a check over inputs the second statement is saying that HR can access any salary and and the reason that's important is because HR is like who is a member of HR is not information that comes in with the API call right it's just not there and so you need that external context in order to make a decision and so for that the way we do that is we just here we're assigning user a temporary variable and

**28:04** · we're looking up inside the data dot users dictionary which is the the bit over here on the left we're indexing into this dictionary whatever the input dot user value actually is and so then the the user variable here is a JSON object which includes one of these one of these dictionaries here that have the department inside and so then when we say user dot Department equals HR whoops

**28:29** · that's doing what you would expect all right so whether the the data comes in from input or comes in as data you sort of you have different routes but all the operations are exactly the same

**28:52** · remember oh sorry the question was it looks like the first rule returns true the second rule returns false remember that the semantics here is that the the rule only returns true if the body holds if the body is true then the head becomes true so the first rule let's say it evaluates to true the second rule does not evaluate to false it evaluates to nothing undefined and then we or those two together and we get true yeah so yeah yes

**29:30** · yeah so so if I'm sorry the question was what happened if the rules give you conflicting results so what you could do here so to make this case you could say allow equals true if the first one a lot of equals false if the second one right let's just say wouldn't in code what we said here but imagine that that was a kind of rule that we had so one thing that we do is we say we recommend not doing that unless you absolutely have to

**29:59** · but in that case if you got an actual conflict we would say that's an error now what you could do and what maybe you're thinking of is what people often will do is will write allow rules and deny rules you can do that here but then what you need to do is open doesn't know about allowing deny are not keywords for OPA and so when that when that micro-service asks for the answer to a

**30:23** · policy decision it will ask for let's say allow and so if you want to use allow and deny you need to write the logic that says how to resolve those conflicts to return a single value for allow we've got an example this later so maybe that's the best way to illustrate that yes very good question give me 30

**30:50** · seconds I'm sorry the question was are is there anything like loops and and and and then that's the answer okay so here's a summary I'm not gonna bore you with the details you can read this if you want alright so now we're gonna move on to the more interesting section which is policies with iteration all right so

### Policies with Iteration

**31:11** · we've talked about dictionaries quite a bit all the examples really have used mainly dictionaries but what about arrays imagine we've got an array now that comes in as the input or as part of data and now in order to make an authorization decision I need to be able to find an element in that array all right now given what I've shown you so far it's a it's it's really difficult to figure out how to write this right so imagine that we somehow so here's a here's an array on the left hand side and data it's it's a list of resources each of which has an ID and an owner okay and then the input that comes in is a use and a resource and what we want to know

**31:46** · and what we want to say is that this this input is allowed exactly when that user is the owner of the resource that they are requesting access to all right and what that means is that we have to like effectively iterate over the elements and that resources array to figure out if that user owns the resource that he is requesting now imagine to start that we know magically that the the that it's the first array element that we need to check and it's only the first array elements that we need to check what would the logic be that we would write for this allows

**32:19** · statement well you see that on the right-hand side what you see here is that allow is going to be true if the resources at element 0 so if the input resource the resource being requested is the same as the resource ID at element 0 and the data resources array and the input and the user requesting the resource needs to be the same as the owner at the at the zeroth element of the data resources array right so that's the logic that you would write if you knew that the the resource you cared

**32:49** · about was at element 0 of the array all right but we don't know it's a 0 at element 0 it might be element 1 and so you could imagine repeating that allows statement if it was element 1 all right

**33:04** · if the resource here that was at element 1 now the obvious problem here is that we don't know which element of the array we need to look at and so that list of allow statements would actually be infinite what opal laws you to do instead of writing an infinite policy is to replace that that index with a variable and so instead of writing that whole long list of allowed statements you can simply inject a variable into the array index and now implicitly what

**33:36** · this says is that allow is true if for some index the body of that statement is true if for some index what I said earlier was true all right what what oppan does when it sees a variable without a value is it implicitly it automatically does iteration it automatically walks over all of the possible values for that index variable and if it finds one we're the bots that

**34:06** · makes the body true then it says the body as a whole is true and it returns yes oh the question is is this autom automatic problematic if you make a mistake okay so there's a lot of language constructs where if you use

**34:26** · them accidentally you would there would be a problem yes so yes if you accident intended here to to assign index to a value and then you you forgot to actually do that assignment then yes but this is how you can do it eration you can do iteration like conceptually what's happening here is what oppa always does and this is a universally the semantics is that it finds an assignment is that the head of a rule is true if there is some assignment to the variables in that body that make the body as a whole true that's what it's always doing that is it semantics

**35:01** · question oh yeah so the question is instead of using a random variable name what if you used underscore two to ask for iteration yeah you're jumping ahead I think there's yes you see you can use the underscore if you don't want to invent a new variable name then you can use the underscore okay questions here yeah yes

**35:40** · so if you see the same variable in multiple places within a rule it must be assigned the same value yes yes

**36:04** · the question is if you had a hundred of these allow rules each of which has variables and required an iteration does it run all through all of the possible indexes for one rule and then going to the next rule or does it sort of interleave them that's an implementation question now but but conceptually you shouldn't have to care one of the goals of oppa's to allow you to focus on the logic and the data and allow the performance optimizations leave those to leave those 200 yeah there's no way

**36:43** · sorry the question is what happens if the data changes during evaluation that can't happen yeah yes there is we've got a slide for that near the end it's a little tricky you've got to use the old trick back from when would we have learned this back for the old trick where if you want to do if you want to ask for everything it's equivalent to saying it's not the case that there exists one that's not true yes yes and and yes you can do the full

**37:20** · arbitrary quantifier alternation here yeah so another good so the question was during evaluation if what happens once it finds an answer and so again that's a that's a performance sort of optimization question it's not a semantic question right so today I you know one of the things in our list is to actually have it stopped early once it's

**37:50** · found an answer both but I don't think that happens today there are other things that we found in terms of performance that are more important than than that one yes always question does

**38:08** · rule evaluation have zero side effects and I immediately said always and that's ideally correct there is that list of 40 of built-ins of operators all of which today are side-effect free we have talked to people who have embedded open as a library and they added built-ins that do things in the world and we've heard of that again that's not the intent of OPA all side-effects should have an outside by the service yes yes

**38:46** · question is are there testing tools yes unit open does have a unit test framework and so you can write tests I don't think I have any examples here but you write tests then literally in this rule language and then there's a way to like mock out input there's one more how do you return data so when so when the service is asking for a policy decision that system can ask for let's say allow in which case it gets true/false there

**39:20** · are other as hopefully we'll see there are that you can define virtual documents where when the when the outside service asks for the the value of that document it could be an array or a set or a dictionary or a number yeah okay we should continue all right one important thing here is that despite the fact that I motivated iteration with arrays you can use open to iterate over anything right so at the top here we've got an example where we're iterating over both the array indexes and values you can also iterate over dictionary keys and values you can it doesn't

**39:55** · matter whether you're iterating over the input document or the data document and then oh we just left and then here is your underscore so if you don't want to bother inventing new variables all the time to do it eration you can use an underscore and unlike all the other variable names you can use multiple underscores within a single rule and those are all distinct variables all

### Virtual Documents & Conclusion

**40:19** · right here's the observation but just because we're using iteration doesn't mean we don't doesn't mean that we no longer have the problem of duplicated logic and so in this example we've got logic duplicated that is actually searching for administrators for who is an admin and so we want to avoid duplicating that logic here as well because iteration is special or it

**40:47** · requires some special constructs we do have a special constructs for for eliminating duplicate logic inside of when we have iteration so in this example we've pulled out that common Lodge and we've created what we're calling a virtual document that defines a set in this case of administrators and so this particular search that we factored out is is iterating over all the users and

**41:12** · finding all of those that are administrators and then storing that result in what we're calling the admin variable okay so admin over here is the set Bob and Charlie and obviously sets for an extension to JSON when we render them and return them they look like arrays

**41:32** · there are different syntaxes for virtual sets so here at the top is a rule syntax and this is defining admin again as the set of all users that are admins you can equivalently write that that rule as using set comprehension syntax and these two are entirely equivalent the one on the bottom is something that especially if you use use Python that is going to look really familiar there is a slight

**41:57** · distinction between these two syntaxes though which is that the rule syntax supports an or so you could write multiple statements that all that you Union together to compute the the admin set or as a set comprehension syntax you can't do that all right

**42:17** · likewise in addition to to building virtual documents that are sets or arrays you can build a dictionary that's a virtual that's virtual and here again it's pretty much the same thing the only difference between this in the set is that in the head of the rule here instead of simply writing admin of username we did we write an assignment

**42:37** · that says admin of user name equals user dot Department and again you've got a rule syntax for this for which you can you can sort of write multiple copies of the of the rule in order to create a Union across all of those dictionaries and then there's a dictionary comprehension syntax below which is more familiar if you've used Python questions here

**43:04** · how're we doing on time I got one minute okay well okay so let me see what else I should cover here okay let me finish this so we've actually seen two cases

**43:20** · where duplicated logic gets factored out one of which is to use functions the other of which is to use these virtual documents so what are the trade offs the clear trade-off here is that virtual documents support iterations so if you define virtually a dictionary you can use iteration just like I talked about earlier you can iterate over the keys over the values of the keys end values you can you can fix the value and find all the keys that that that that are assigned to that value with a function on the other hand it's like a function from a traditional programming language and while you can when you apply that

**43:53** · function like down here if we want to look up bob's department we would write admin of Bob just like you would expect but what we can't do then is is ask give me all of the give me all of the people whose Department is HR you just can't do that with a function alright so it may seem as though virtual Docs support iteration functions don't and so therefore virtual Docs are completely superior to functions why use functions at all and the answer is well virtual documents must always be finite

**44:20** · functions on the other hand can be infinitely large in the sense that and in for a long time we we just had virtual docks without any functions whatsoever but then what we found time and time again is that we had string manipulation that we needed to factor out and string manipulation for example this split path function on the right hand side is something that is infinite right you can hand it any string that you like and it will actually do the string manipulation and return result handed any URL of which there are infinitely many and then this function will will parse that URL and return all

**44:51** · of the segments in the path all right I think that's covered my minute we've had lots of questions throughout so let's go ahead and wrap up so there's another section here I will post these slides online and this is where you see how to deal with modularity multiple policies and how you import one policy into another and the like alright thank you all \[Applause\]