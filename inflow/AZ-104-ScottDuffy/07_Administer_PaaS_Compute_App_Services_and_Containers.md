---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "07"
title: "Module 07: Administer PaaS Compute (App Services, Containers & Apps)"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 07: Administer PaaS Compute (App Services, Containers & Apps)

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** App Service Plans, Web App Creation & Settings, Scaling Up/Out, Deployment Slots, Backups, Custom Domains, TLS/SSL, App Service VNet Integration, ACI Container Instances, Container Groups, Azure Container Apps, ACR, Docker Pull/Push  
**Line Range:** Lines 11787 – 13978 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


### 📺 Lesson: Introduction to App Services


Instructor: Now in this section of the course,
we're gonna be talking about Azure App services
and specifically Web Apps.
Now we've been talking about virtual machines up till now
and a virtual machine is pretty easy to understand.
It is a virtual representation of a physical server.
You either have a Windows or a Linux server.
You can remote or SSH into it.
You have full control, you can install software,
you can navigate to any directory.
It's your machine to do with what you wish.
The Azure App service is a little different.
To demonstrate, I'm gonna go into this creator resource.
An app service is basically an abstraction above hardware
where you don't have control over the actual hardware.
You don't even really know
what the characteristics are of the hardware,
but you have no access to it.
But you just upload your code
and your configuration for that code and Azure will run it.
So think of it as a, you know, a way for you to upload code
and not to have to be concerned about managing a server.
Now, to get to Web App, we got here,
right here on the getting started screen,
but we can scroll down to the last category called Web.
And we can see that we have Logic Apps,
we have Web Apps, Apps Service Plan, we'll talk about that.
Now, like I said, Web Apps, one of the...
I'll tell you the advantages of Web Apps, first of all.
So a Web App is, got lots of extra deployment tools.
It's got built-in integration into Microsoft Visual Studio,
got integration into Azure DevOps, into GitHub actions.
And basically it's an environment that's waiting to go
and you just simply upload your code.
And there's a lot of appeals to that.
It is very similar to running code
in an already running IIS environment.
So you've got a server
and you've got IIS Web server installed,
and you're just plopping your code into a directory.
It's already configured and ready to go,
and you're going to have a website ready to go.
Now you may have heard other terms
like Mobile app and API app,
those are all just Web Apps.
API app is a Web App that doesn't have a user interface
but simply communicates in XML or JSON.
Mobile App is a backend app
that integrates with a mobile on the front end
and can also do things like,
notifications to Apple, iOS and Google Android.
So it's all covered by Web App.
So, we're gonna demonstrate...
I'm gonna go and create a Web App coming up
and we're gonna then demonstrate how this works.
We're gonna look into the settings,
look into the integrations.
How easy it is to get code into a Web App
compared to what you would do for a VM.
So in this section we're talking about Web Apps.


### 📺 Lesson: Create a Web App / App Service


All right.
So in this video we're going to create our first web app.
I'm going to go into the Create a Resource button here.
And web app is one of the most popular services.
So it's right on the Getting Started screen I'm going to say create.
Now we can see a familiar wizard like interface where we've got multiple tabs to fill out.
Here.
Every resource needs to be put against a subscription, which is the billing unit, and every resource
has to be put into a resource group, which is sort of like an organizational structure.
So we're going to call this Azure AD New Web app.
Now recently this concept of a web app name has changed.
It's always been preferably globally unique because you have this dot Azure websites dot net extension
that signifies to you that whatever you type here needs to be globally unique.
One of the challenges, of course, is that there are millions of Azure customers, millions of web
apps.
And so it's going to be very difficult for you to find a web app name that is globally unique and has,
you know, without some sort of like additional numbers thrown in or something to make it unique.
And so what Microsoft has done is they've got this preview feature which will randomly append some letters
and numbers to whatever you type to make it unique.
Now, in practice, people are not using this dot Azure websites dot net as the public facing domain
name.
So you're going to register your own custom domain and then use a CNAME record to point to this.
And so this is sort of a behind the scenes public URL.
So for instance I can put AZ side new web app as my name as well.
And you can see that it's appended this hyphen c and f k, h, blah blah blah in order to make it unique.
Also recently, Microsoft has changed the types of code that are supported within a web app.
I'll talk about the three types of code.
Now.
A static web app is basically a static website that contains files, not code.
These are HTML files, JavaScript, CSS, images, videos, things that you upload once and do not execute.
They are just served to the client browser a container.
Containers are huge within cloud computing and within the Microsoft Azure environment, and web apps
can run containers.
So if you have a Docker image of an application, you can choose a container app and deploy it into
a web app wrapper, if you will.
Finally, you have this code, which is the traditional web app.
Microsoft Azure Web apps contain the runtimes for a number of different stacks.
I'm going to open this here.
We're going to see all of the dotnet nine preview eight six the old ASP.Net.
If you're still using that Java, Node.js, PHP and Python, they are no longer supporting Go or Ruby.
So now depending on the operating system or the runtime stack you choose, you can choose an operating
system.
So dotnet is cross-platform.
You have the choice between Windows and Linux.
Um, Java 21 is cross-platform, for example.
So um.
I guess Python is Linux only as an example.
So depending on the the runtime you choose you get a choice of operating system.
Now this in practical terms does not really affect the running of your application, except if you are
dependent on Linux file folder structures and certain Linux specific formatting for text files and things
like that.
You get to choose a region, just like with virtual machines.
You can put it into United States, Canada, one of the 60 plus regions around the world.
Now the key here.
So we've we've sort of named this web app and we've chosen the code that it's going to run.
But this requires a hosting plan or called an app service plan.
I'm being suggested a new one here.
It's a standard plan.
You can sort of see it's got 1.75GB memory, one virtual CPU, very basic level of pricing plan.
If I wanted to pick a different one, there's this explore pricing Plans button, and I can see from
a hardware view the comparison between, um, the free basic premium isolated standard, now standard
is now listed under legacy.
They are discouraging people from choosing standard because what they want you to do is choose between
sort of the basic plans, which are dev test options and production plans, which are premium, and
you can see premium P0, P1, P2, P3 and then some of the Mv3 type extensions with um app services.
The performance.
You don't get to choose the hardware, but you do get to choose what is called a performance.
Uh, a Q which is the, um, which is sort of like a computing unit, which is an approximation of the
relative performance.
You could say that the basic B1 has a 100 rating under AQ and premium is 195.
You would expect premium to run at 95% faster than the basic tier for the same single instance.
Now, the expectation with App Services is that you will scale by running multiple instances.
So you're not just running a single P1 P3 instance, you are running two or 3 or 4 of them to get that
scaling for your app.
We can see the pricing on the right.
Now, one thing that might stick out to you is there is a free tier.
So if you're just interested in trying this out, it's not a serious app.
It's just for development purposes.
You can set this up as a free tier.
Perfectly acceptable.
You only get one gigabyte of memory and one gigabyte of storage, but it's something you can try your
app on.
There's also a shared plan, which is also cheaper.
Only 12 CAD or 10 USD a month and it goes up from there.
So like the cheapest premium P0 v3 is 155 Canadian, probably 120 USD more or less.
So I'm going to start here with the free.
The free plan just for demonstration purposes.
And we can show you how to scale that in a future lecture.
Now you do need the premium plan in order to get something such as redundancy.
So if I was to choose premium v3, you'll see that I can do app in terms of um zones.
Right.
Apps.
App zones.
Application zones for your apps disabled by default.
So I'm going to go back to the free tier for that.
All right then we'll go on the next video.
We'll talk about deployment options.


### 📺 Lesson: Github Actions and Virtual Networking


All right, so we're still in the process of creating an app.
I'm actually going to switch it from the free plan to the standard plan.
As you can see, you can deploy either a back end database like MySQL or even Azure Cache with standard
and above.
So I'm going to say next deployment.
Now the concept of continuous deployment integrates with GitHub and GitHub actions.
And so if I was to integrate with GitHub I can basically select a repository in a branch.
And whenever code gets checked in and committed to that branch, the web app is going to download the
code and deploy it.
Okay.
So we can sort of see here that this will automatically update your website whenever you've got code
that's checked in.
If I wanted to enable traditional windows authentication within IIs, I can do it from here.
Disabled by default.
Which means anyone can access your website.
On the networking tab we have the option.
Just like with VMs of attaching this web app to a virtual network.
So I would have to either create one or have one ready in the same region.
And what that will do is require that people have access to the virtual network in order to get access
to the web app.
It would put the control of the traffic in your hands with nsgs and firewalls and things like that.
So I'm not going to turn on network injection.
This is a public facing website not connected to any virtual network.
As for monitoring, Microsoft Azure uses the Application Insights in order to code your application
and get some trace diagnostics out.
I usually turn that off because I don't use it.
I would turn it on if you specifically need it.
And what you're going to get with this is an Application Insights instance which will collect data from
your application.
Again, this is like tracing, uh, any kind of exceptions and errors that your code requires.
You do have the option of defender for cloud, which is Microsoft's Anti-hacking solution for cloud.
You have to have a subscription for that.
We'll skip over the tags.
This allows you to put metadata against this.
I'll go right to review and create.
You can see for my S1 plan it's estimating this much per month.
This is fairly comparable to the cost of a VM with the same performance.
In my experience, you're not saving money, but it's not really costing you anything extra to run your
app in this configuration.
We have all the settings that we've chosen and now I can say create.
So let's let that go off and run.


### 📺 Lesson: Web Apps Deployment Options


So it says the deployment is complete.
We can go into the web app under operation details, the deployment details, and we can see that it
takes less than a minute, around 37 seconds for the actual web app to deploy.
The App Service plan in which the web app executes is only 14 seconds, so less than a minute for the
whole thing to be created.
I'm going to click this go to resource button.
So this is the web app that we created.
Now you'll see the status is running.
Remember we gave it a name and Azure appended random letters and numbers to it to make it unique.
So I'm going to copy this URL.
That's the URL of my website.
Now if I paste that URL into a web browser, I can see it says your app is running and waiting for your
content, so it's just a default page.
There's no code that I've deployed, it's just the default.
I'm running standard S1, one instance of S1 on a windows operating system in east US.
Everything that I requested has been created.
Now, one thing I wanted to show you is how to get code into this website.
How to deploy.
If I go into the deployment center here under deployment menu, it's going to give me a bunch of options
for doing deployment.
Now you'll see under continuous deployment we talked about GitHub and GitHub actions a second ago.
But there's also Bitbucket.
You can have a local git repository Azure Repos, which is their um solution for deployments and even
manual deployments through external git.
Okay.
Those are deployment options.
I can also use FTP as to FTP the code into the Azure Web app.
So if your um, your IDE uses FTP as a deployment option, This is an option built into Visual Studio,
and Microsoft's Visual Code Editor is the ability to push code into web apps, so you don't need any
of this in order to push code into a web app from those Microsoft tools.
Another cool thing to show you on the deployment side are what's called deployment slots.
Now, by default, when you create a web app, you have a single slot which is production.
And so whenever you deploy code into your web app, it goes straight live there.
It doesn't keep a copy of what was there before.
It goes straight over, overwrites it, and it's live immediately.
Now let's say you want to set up a situation where it's not live immediately.
Let's say you want to set up what they call sometimes staging.
Okay.
So you give it a name, you call it staging and it's going to create for you a URL that's separate than
your production URL for staging.
You can choose to copy the settings from the production app or not.
It's up to you.
So I'm going to say add.
And when this is done, I'm going to have the production spot, which is the URL with nothing appended.
And I'm going to have a staging spot which is the production URL with this staging appended.
We'll let that run.
So now I have two places to deploy my code.
So you can set up your continuous deployment to deploy to staging not to production.
Or you can do your publish profile within Visual Studio to publish to staging.
And when you manually push the publish button it goes here.
Then you can go to this URL and you can double check that it's okay.
Do a pretest before production sees it.
And then when you're ready let's say you've tested staging.
It's good.
There's no bugs.
You're happy.
You simply just hit swap and swap will take the staging code, push it to production and take the production
code and push it to staging.
So it's going to basically swap them exactly as it's called.
What this allows you to do then, is to stage your deployments by going first to a testing spot, testing
it, then when you're happy manually going to production, and then if something was to go wrong, let's
say you were not happy with something in production after doing this process, then you can swap it
back.
You have the old version of the code standing by in case you need it, and you don't have to deploy
the old version of the code in order to get that updated.
So this is a way of safely deploying code and safely rolling back the code if something was to go wrong.
No extra deployments required, it's just swapping the URLs.
Another cool feature is this concept of traffic percentage, which some people would call a B testing.
So let's say you want 10% of your traffic to go to the new code, 90% of the traffic to go to the old
code.
You could simply set up this 9010 traffic percentage.
And Azure will automatically send 10% of the traffic to this new area.
So this is a way of doing a small scale test in production with only some of your users for them to
see the new site.
Maybe you want 1% or 5% or 25%.
Then you can determine if there's any issues.
If you get tickets or you're getting phone calls or something's going wrong without affecting everybody
all at once.
So these are some of the features you get with web apps that you don't have with virtual machines without
a lot of manual effort And so the deployment options are some of the better options for using web apps.


### 📺 Lesson: Web App Settings


Instructor: So let's move on to the first setting,
that's called configuration.
Now, if you're at all familiar with setting up websites
in IIS on Windows server,
you might recognize some of these settings,
particularly on general settings.
For application settings and connection streams,
you may recognize this from setting up web apps
within Visual Studio, for instance.
So application settings allow you to separate out
the dynamic variables of an application from the code.
You necessarily don't want to have important settings
to be buried in the code somewhere.
And so some years ago, many years ago, in .NET,
you could create an app settings file,
and you could put any kind of variable
that could potentially be changed in the future in there.
So let's see, you wanna know
the number of rows on the report.
So I can say number of rows per report, and I can put 25,
and that could just be an application setting
that is passed into the application,
again from this settings file
as opposed to hard coding that.
Now this can also be used for sensitive things
such as API keys, user IDs and passwords,
and other things like that.
What .NET has done with the app services
is even allows you to put app settings
into the app service configuration,
therefore, you don't have the sensitive values
of an application stored in GitHub,
or in your source code repository.
So it's not even in the code,
and it's not even in the app settings file
that is stored alongside the code.
So for security reasons, you can store
the sensitive values here in the app settings.
So let's say, you have an API key
that is important for some third party app.
And so the API key is just a series of numbers,
and this value needs to be added
alongside any of your foreign API calls in your application.
You can put that into
your app services configuration setting,
and that'll get your application
can then call for that value,
and call this, yeah, API key,
and that way your developers don't have access
to some great secret that might be too sensitive
even for your devs to see, okay?
Connection strings obviously
for database related connection strings.
So again, they're not gonna be embedded in the code,
they're not gonna be embedded in the file
alongside the code.
They're going to be embedded here.
One of the things you can do do is
tie this to a deployment slot.
And so you can call this MainDB,
and you can call this, you know,
I don't have an app, a connection string,
ready, but whatever.
There's some connection string value server equals A,
user right equals B.
So you can store this here,
and this is particularly sensitive,
you can even tie this to the deployment slot.
So this is the production deployment slot setting,
and then you'll have a different one
for development and things like that.
On the general settings tab,
we're gonna see this is where the code stack
has chosen the value for .NET version or other versions.
You'll see integrated versus classic pipelines.
The minimum HTTP version,
whether web sockets is available to the application or not,
usually turned off cuz it's pretty powerful.
Always on availability for your app,
ARR affinity is whether the same user
is directed to the same instance of the app,
or they can be sent to any instance.
HTTPs only.
Other values like that all within the settings here.
Default documents you'll recognize from IIS as well,
where you can have Default.html, Default.htm, Default.asp.
These are the documents that will be accepted for the route
if you don't provide a file name in a url,
these are what it looks for in that directory.
And of course path mappings,
if we have virtual apps and directories
that publicly are called slash images,
but internally they're called something else.
Azure storage allows you to map
files or blob containers for use with your app.
I'm gonna hit to save on that.
So that's basically the configuration for creating a web.
You've got lots of little options in here
that are again very familiar for IIS options.


### 📺 Lesson: Scaling Up Web Apps


All right, so let's say you have a web app and you are not satisfied with its performance.
It's running slow.
You're running into some kind of limitations.
What do you do?
Well, what you're considering then is scaling your web app.
So right now we have this app service plan which is standard S1 one instance.
And let's say we're not happy with the performance.
And so we want to consider growing this plan to a higher level plan to take this single instance and
make it into a higher level plan is called scaling up.
And so if you go under the settings, the menu here under settings you'll see an option for scaling
up.
If you simply wanted to add more instances, that's called scaling out.
And we'll talk about that in the next video.
But let's talk about scaling up.
So if you recall when we were selecting this Microsoft has divided the two sets of plans into dev,
test or production.
You've got free shared or basic under dev test and all of the premium plans from P0 to P5 under production.
What I'm running under is a legacy plan standard S1.
Now if I simply wanted to get more CPU, more memory, but I was otherwise satisfied with the level
of performance, I could simply just upgrade to the S2 plan and I would get double the CPUs, double
the memory, same number of storage in terms of gigabytes, same limitation in terms of maximum instances
and same SLA promise.
Actually, if we go under the feature set, we can sort of see some of these other limitations.
So for instance under standard S2 I can only limit it to a rules based auto scaling, which we'll talk
about in a second.
Only ten daily backups.
Only five deployment slots.
And the zone redundant option is not available to me.
So I'm going to select the S2 plan.
I just say select and it's going to do that upgrade for me and that's been seamless.
So.
So within those seconds, it's now running on an S2 plan and hopefully my users never even noticed the
switch.
What they should notice is the increased performance.
Now likewise, if S2 is too powerful and I'm not using it to its full potential, I can also downgrade
to back to S1 if I so desired.
And that's pretty simple.
Do keep in mind also, when you're changing plans, you're also incurring more costs, so it's basically
roughly double the cost.
All right.
So that's pretty straightforward in terms of scaling up.
Now there are limitations of course.
So once you've gone from S1 to S2 to S3 and you've got the four CPUs and the seven gigabytes, well
then you're forced to go up into a premium plan.
So the S3 plan runs around $400 a month Canadian, which is about 350 US to get to the premium P3,
you'll see that it jumps to 1300 Canadian, which is around $1,000 US a month.
And then there's a limitation of a maximum 32 CPUs for premium P5 running $5,500 a month, roughly 5000
US a month.
Now, there's a problem here in that you end up with this single instance and a single point of failure.
So if this web app is not available and it isn't, replying isn't responding.
If there's network challenges or power challenges, then you are going to have, um, this limitation.
Your users are going to notice the problem.
So that's the limitation of scaling up is a maximum size for this.
And you're still getting the single point of failure um challenge.
So we're going to talk about scaling out, which will hopefully avoid the maximum size and the single
point of failure in the next video.


### 📺 Lesson: Manual and Automatic Scaling


All right.
So let's talk about the option of adding instances.
Now there are now three types of scaling options within Azure App Services.
The first one we'll talk about is the easiest.
It's a manual scale.
So I am on the scaling out option based on my standard S2 plan.
I can have up to ten instances total and I'm currently running one.
What is an instance?
Basically, you upload your web app into a single instance, and then when you grow it to two instances,
you'll have two servers, virtual servers looking to accept traffic and handling that traffic.
So think of it like cloning the app and having a second instance running.
You can do this manually by just going down here to the instance count, pulling the scale slider to
two or to three.
And if you say save then you are going to have Azure create two additional instances.
You can see the current instance count is three.
And what this does is it um it increases my cost.
So I'm paying on the S2 plan around $0.27 per hour, which is $198 per month.
Canadian.
Around 150 $160 US.
And now I'm doing that three times.
So that would be up to $500 US or $600 Canadian, because I have three copies of my app running.
So that is one way to scale your app.
Microsoft automatically takes care of having a load balancer in front.
So when I go to my domain name, let's go back up to here.
When I go here, there are three servers standing by to receive traffic to this web app.
And every time that I go there, it could be potentially a new server one, 2 or 3.
I'm going to refresh, refresh, refresh what we don't have enabled.
And we'll talk about that I don't know.
We probably talked about that in the configuration option is this concept of sticky sessions where you
can have um the same session affinity is on actually.
So if I was to turn session Affinity off, then basically you are going to get random server each time
session affinity being on it's always the same server.
So that's in the settings here.
So I'm now running I'm now running three instances of this app.
It may be too much for me, but I'm doing it manually.
Let's go back down to one.
Now there are two other scaling options and they're both forms of auto scaling.
So the first one now is called automatic scaling or elastic scaling.
It does require premium v2 or premium v3.
So if we go back out to scaling up and we go under features or yes, under features and we see auto
scale, it takes the premium P1, P2 and P3 plans have this elastic option.
So if I was to upgrade to premium.
P1 and then going to scaling out.
Then I do have this automatic option.
This is platform managed scaling.
So I'm just going to trust that Azure is going to take care of it.
I can um.
I can basically set limits.
So let's say no more than five.
additional instances on top of the one, and I have Azure taking care of this.
Okay.
The other option is rules based.
And so if I want to define what these rules are then I can say for CPU under custom Autoscale I can
say based on a metric, add a rule that for CPU percentage greater than 70%, increase CPU count by
one with a five minute cooldown, and it's going to do that measurement over a ten minute period.
So that's a scaling out rule.
Let's put the maximum to three here.
And then I can have the scaling in rule, which means when CPU percentage is less than say 20% then
I want to decrease the the count by one.
And so that is a scaling rule based on CPU percentage greater than 70 increased by one less than 20
decrease by one.
Right.
So this is another way of scaling.
It's called custom auto scaling or rules based.
And if I was to save this then this would also, um take care of the scaling of my app service.
Again.
You would have to use a virtual machine scale sets um to have something similar.
And scale sets don't take care of deploying your code.
You'd have to have scripts to deploy your code.
This is making a copy of your app, you know, one, 2 or 3 additional instances, and you don't have
to do anything and it just takes care of it for you.
So a lot easier in terms of scaling compared to virtual machines.


### 📺 Lesson: Backup Web Apps


Instructor: All right, so one
of the important things when we're dealing with the cloud,
we're dealing with apps and data is a concept of backups.
Now, Azure App Services come
with an automatic backup
if you're on any type of basic, standard, or premium plan,
and you can't configure that.
That's just something that you are given.
So you can see that this app that we just created,
the automatic backup happens every hour automatically.
And so I can just see the last four hours
of backups here.
I can pick to restore any of them.
Very simple interface
because backups just happen automatically.
If we go to the documentation here
we can see that for basic, standard, premium, and isolated,
we get up to 30 gigabytes for backup.
And any database that is related
to the application is not backed up.
You don't have to do anything.
There's no storage account that's required.
It happens hourly, not configurable.
They're gonna keep 30 days worth of backups
and you'll see that for the first three days,
you'll get three hourly backups
so 36 total backups, and then
for the first two weeks, you get a three hourly backups.
So every three hours.
And then for the last half of the month,
you'll get every six hours.
So the frequency of the backups, the retention is reduced
as the backups get older.
You can't download the backup and it's just a full backup.
As you can see, it's very simple.
It just comes with your storage account.
If this is not a satisfactory schedule for you
then you can do what is called a custom backup.
So custom backup does require configuration.
So you do have to configure the backup.
You have to either provide it
or create it a storage account
and then you can set the schedule
for the exact time and recurrence of your backup.
There's this that's on the basics tab here.
On the advanced tab,
then we can basically link to custom databases
like SQL Database or MySQL to get backups for that
as well as our App Services.
So as you can see, again, one of the advantages
of App Services is how tightly integrated it is
with some other Azure services, and that includes backups.


### 📺 Lesson: App Service Networking


Instructor: All right, so we have our web app
and I can click on the link
and it will take me to the web app.
Right now we haven't loaded any code in here
so we just get the default screen.
And if you remember when we created this web app
we had the option of turning on public networking,
or turning it off and turning on private networking
within Azure or not enabling that.
And so let's go look at some of those options.
'Cause it doesn't, we can change them once the app is live.
So, we're gonna go into settings and into networking.
And just to get myself a little bit more room
on this canvas, I'm going to hide the menu here.
And eventually we can see this setup here
from that shows us inbound traffic,
the web itself and outbound traffic.
And then these are just networking related settings of each.
So, on the inbound traffic,
manage access and incoming services,
we can get access restriction.
We go into access restriction.
This checkbox is what's gonna turn off
public access to the site.
So, if I was to save this
then that link to the site would no longer function, right?
So, this is basically blocking all incoming traffic.
We also have this option
of having, like an access control list,
which is a basic type of firewall to restrict traffic.
I can set the deny as default for this
and then I can say "add" in terms of an access control list.
And I can say my IP.
Give it a priority of 100.
And it's asking for an access address block.
And so, I can paste in my IP
and I can say, I think slash 32 is a single IP.
If I want to be a little more open
I can say slash 24, which is the entire C block.
If I wanted to have HGTP headers like X forwarded host,
or X Azure FDID, et cetera then I could paste this
and that will filter based on those headers.
But that's optional.
So, I can say add rule.
And now my personal computer here
should still have access to the application.
I'm gonna say save.
Traffic to unmatched rules to main site will be denied.
Absolutely.
Right? and now, if I go back
to the home screen to get the URL here,
this should work for me,
but it would not work for anyone else.
Or if I connect it to a VPN, it would not work either.
So, that's a way of basically firewalling your web app.
Which is, if it's a sensitive thing, could be a good idea.
Now, you'll see that the app
is running on its own IP address.
It's not dedicated.
So, I think there's an expectation that the domain
it's gonna come in across the domain.
But that's if you need to open a hole in your firewall
from inbound, from your traffic to a public IP address,
this is the IP address that you need to connect
to this web app.
On the other side, there are the IP addresses
that the app uses.
And there are many, right?
So, these are the current list of IP addresses
traffic from your app could use.
And so if you have to open a hole into your firewall
to allow inbound traffic then you have this laundry list
of IPs that could come from Azure web apps.
Now, if we wanted to use a custom domain,
custom domain has its own menu item as well,
but we could also manage it from this networking screen.
So, obviously having a custom domain
is part of the networking of your app.
Now, we mentioned private endpoints
and it's kind of outside the scope of this course
in terms of private endpoints.
But basically these are really restrictive.
You're setting up a endpoint from within the app
and then you're sending up an endpoint
from some other, it could be another app,
or it could be a virtual machine.
And those are the only two things allowed
to use that private endpoint.
It's a point to point connection
as opposed to opening up the entire virtual network
for an inbound request by IP address,
or opening up, you know, IP address based requests.
So, this is more direct in terms of
the ultimate level of privacy for two apps communicating.
Now, when it comes to outbound,
one of the things we can do
is we can attach this application to a virtual network.
Right now we don't have a virtual network
it's configured to.
We could choose one or create one.
We don't have any Vnets in this region.
We'd have to then create a VPN of sorts
or appearing to get onto a Vnet of another region.
But we could, and in within the outbound, set up this.
Now, that leads to the ability to set up routing.
You can set up outbound security rules
on your network security group
so that the app can't communicate
to certain destinations or over certain ports.
Or, you can even basically have this
network address translation
where the effectively it forces the traffic
to go over your site to site VPN.
So, instead of going out to the internet from within Azure
it goes out to the internet from your company network.
So, once you set this up for Vnet integration
you can do some routing
and basically control of the traffic.
Finally, in the bottom left here,
if our app is gonna need CDN services,
or even a global front door service,
that includes a CDN but could also include caching,
could also include load balancing.
Those types of services can be initiated from here,
although these are just gonna be links to those services
that you can then include this web app
as the backend pool to these services.
So as you can see within networking
it's basically just a portal
where you can set up all these things.
The main ones being the inbound restrictions
and the outbound restrictions
that could include firewalls, gateways,
network security groups, et cetera.


### 📺 Lesson: Map an existing custom DNS name to an App Service


Presenter: All right.
So now we're gonna look at this domain.
We have this default domain that was given to us.
Like I said before, it's quite unwieldy.
It's not something you're gonna wanna share with people.
So how would we add a custom domain to this?
So I'm gonna start off by going to the domains section.
If we go under settings and go to Custom domains,
we have two options, and one might be a bit surprising.
One is if we have an existing domain,
we can certainly add it.
There are some instructions.
So if we say all other domain service,
add a certificate later, we can have our domain here.
It's gonna give us the instructions
on how to go ahead and do that.
The other option is to buy the domain through Microsoft.
So just for app services,
they have this concept of an app service domain
and we can basically search for a domain.
You can see that it has a cost, so it's 11.99.
And if you choose something relatively unique
like thisismyuniquedomainname.com,
the domain is available.
Then I can go through the process of purchasing this domain
and it'll get associated to my app service.
Of course, the registrar requires your real information.
I think they all legally do.
And then it's associated with your instance
and you can choose to have a domain
that does not use a WWW,
so just thisismyuniquedomainname.com
or www.thisismyuniquedomainname.com or both.
So you can set that up.
Do you want to have auto renewal?
And do you wanna have privacy protection
so that your real information is not published
to the public?
You need to be an enterprise customer
in order to get this auto renewal.
So if I was to fill all of this out,
I could then use Microsoft to register for a domain,
but I'm not gonna do that.
I'm going to have a custom domain.
Now...
The thing about certificates, I do wanna show you
how to create a certificate for a custom domain.
So I'm gonna say, "Add certificate later."
Now I have a domain in mind for this,
but I need to register it first.
So I'm gonna register justademowebsite.com.
So I did it. I have justademowebsite.com.
And what I'm gonna do is enter that here.
Now you'll see that I have to add something
to the domain record
in order for Azure to recognize it.
So I'm gonna go into my DNS settings here
and I'm going to add an A record
for all hosts to this IP.
And I'm gonna put it on a short time to live.
Let's put it on a five minutes time to live
'cause I'm just playing around here.
That means that downstream
no one's gonna hold onto this information
for more than five minutes.
They'll always come back and see if it's changed.
The shorter the time to live,
the easier it is to make changes.
And the other option is this TXT record.
This proves that I own the domain.
So I'll add a new record.
I'll add a TXT record
because only I will be able to hopefully update this record.
Save changes.
Now what I need to do is validate this.
It's gonna go out to the web,
it's gonna go to my registrar and it's going to see
if these numbers match what it's expecting.
You can see the green check marks saying validation passed.
I'm gonna say, "Add."
All right, that was successful.
But our problem is that this website is HTTPS only,
and we currently don't have a security certificate
for this domain name.
So before we can actually test this domain,
we need to add a security certificate.
We'll do that in the next video.


### 📺 Lesson: Configure certificates and Transport Layer Security (TLS) for an App Service


Instructor: All right, let's say now we want to add
a security certificate to this domain.
Now remember when we signed up for this,
it came with HTTPS only, right?
That's the setting.
And when we go to the website,
we have absolutely no problem going to HTTPS
to get to the website.
That means there is a valid security certificate.
And if we look at the certificate viewer,
it is *.azurewebsites.net.
So there's a blanket certificate with a wild card
covering every Azure app service.
Millions of app services are covered by this one certificate
owned by Microsoft, and it has their own start and end date.
If they ever missed this end date,
lots of people would be having a bad day.
So here's the thing though,
that certificate does not cover our custom domain, okay?
Just the Azure websites on that,
not the domain that we registered.
So let's change the certificate so that our custom domain,
which is just a demowebsite.com, will work.
So when it comes to certificates, there are a few options.
Now, one is if you have a certificate authority,
or you are a certificate authority,
you can bring your own certificates.
So the .pfx files that we used to use for Windows
also will work in the web.
Also, this .cer, if you have that certificate standard,
then you could upload those into this site.
The other option
is using Microsoft Azure's managed certificates.
Now, this is free
and it's basically fully managed by App Service
in order for you to have site security.
So I'm gonna use a managed certificate
for my justademowebsite.com domain.
So I'm gonna click Add Certificate.
I only have the one custom domain.
It's going to generate a friendly name.
That's going to be part of the PFX file.
I can validate.
And if I say Add, it's going to then add this.
It's gonna generate a certificate for me
managed by App Service.
And it's gonna take a few minutes obviously
before I can use that domain name on this website.
Very easy to do this managed certificate.
So we'll let this run, and when it's done, we'll come back
and we'll see the certificate and we'll see it working.
So after a few minutes,
our certificate has been successfully created.
We go back to the custom domains section.
We can say that
we have adding a binding between the domain
and the certificate that we just created.
Now we have this option between the SNI certificate
and an IP-based certificate.
IP-based certificate basically binds the IP address
to the domain, and you can only have one certificate
dedicated to the dedicated IP address.
With the SNI protocol,
then you could have multiple certificates,
the same IP address,
and it's supported by most modern browsers.
So let's say we're gonna add that SSL binding
to get that domain working.
And so now we have this justademowebsite domain.
If I take the domain, put it into my web browser,
justademowebsite.com,
then I'm directed to my sample app
and then the domain stays.
So we've seen that it's not too difficult
to add a custom domain
if you have a custom domain to use or purchase one,
and then not that difficult to add a certificate
bound to this domain
so that you can then have a friendlier name
for your web app.


### 📺 Lesson: Introduction to Containers


So, in this section of the course,
we're gonna be talking about containers.
Now, in this video, we'll talk in general
about the benefits of using containers to deploy code,
and in more specifically, a brief overview
of the various ways
that Microsoft Azure supports containers.
So, what is a container?
The concept of a container
is that you're gonna take a piece of code
and you are going to package it,
including all of its dependencies,
everything that it needs to run in one image.
And then, you can deploy that image to development,
to staging, to production,
whether it's Azure or AWS or Google Cloud,
or in a VM or anywhere that you want to deploy it.
That image is unmodified
to being deployed everywhere it goes.
All you need to do is just modify the settings
that go along with the image.
Now, this is in contrast with traditional deployment,
where you would compile an application
with EXEs and DLLs and all of these things,
but then you would need to do a number of steps
to deploy that into various environments.
There might be some packages that it relies on,
like the .NET Framework,
or there might be some third-party software
and DLLs that are required,
and maybe even you need to flip a switch in the code
to go between deployment and production
and things like that.
So traditionally, deploying code is a very manual process.
You've compiled it,
and then when you go to deploy it,
it could take hours.
I can actually remember going back several years
before we had containers,
that we would do deployments into production,
and the deployment would start at midnight,
and we hoped to be done by 6:00 in the morning.
But oftentimes by 10:00 AM,
we were just finishing up.
And so, it was a eight or a 10-hour process
to deploy complicated applications in production.
Containers simplify this process.
So, it's really the benefits are along the deployments.
So within Microsoft Azure, you have a number of options
to deploy containers.
Now, perhaps the most famous and popular one
is called Kubernetes.
Now, Kubernetes started off as a Google standard,
a Google piece of software.
Google has released it,
and now it becomes the industry standard
for running complex enterprise applications as containers.
Fortunately for us, the AZ-104 course
no longer has questions about Kubernetes.
Microsoft has removed Kubernetes from the requirements.
So, we're not gonna cover Kubernetes
too much in this course,
but I'll tell you a little bit about Kubernetes.
One of its main features is that it runs in a cluster,
and you can actually tell that by the icon
where there are more than one server.
You at least have to have two servers or more
to run a Kubernetes cluster.
And there's an orchestrator,
which is like the traffic cop
who is controlling everything.
And then, you're running nodes on top of your clusters
and pods on top of your nodes,
and it's a really complicated environment.
But yet, it is, again, designed to be infinitely scalable
at the enterprise grade, things like that.
So, there's a special software called kubectl,
K-U-B-E C-T-L, that you use to control Kubernetes.
And again, it's not for basic, small, cheap projects.
It's a production version.
But Kubernetes is not the only container.
We have a simplified one called Container Instances
that is covered on the exam.
These are typically single-node instances
like you see in the icon.
There's only a single instance that's running your software,
but it's extremely simple to set up.
You have to provide a link to the image
when you're creating the instance.
And in only a few seconds or a few minutes,
you can have an instance running
and no special software required and things like that.
So, Container Instances is sort of the other end
of the scale.
I often look at this as being great for demos
for small internal applications,
something that does not require redundancy,
does not require five-nines of uptime.
So, Container Instances is obviously an option.
In the last year or so,
Microsoft has come up with a new service
called Container Apps.
And Container Apps provides
some of the flexibility of web apps
and the simplicity of Container Instances
and some features from Kubernetes.
So, Container Apps is sort of trying to be in this middle
between the complexity of a Kubernetes
and the simplicity of an Instance
and some of those features,
developer-level features of a web app.
And so, we're gonna talk about that in this course as well.
Now, I should also mention
that there are other technologies you might hear of
called Service Fabric being one.
This is not on the exam,
but this does have a container option.
Of course, you could create a virtual machine
and create a container, you know,
install Docker and create a container
on your own virtual machine.
You'd be entirely responsible for deploying that.
Containers on a virtual machine,
not on the exam as well.
And finally, I did mention web apps.
Web apps does have a container option.
So, if you go under App Services,
and to create a new web app,
you're given two options.
It's the code, which is the traditional web app
where you choose the underlying image,
like the software that's going on.
So if you want a .NET web app,
you choose that here.
And finally, you can have a container.
Container support both Linux and Windows options.
But like I said, this is a very simple way
to, if you create the container image on your own,
you can deploy it into a web app
and you have all of the flexibilities,
the scaling, the auto scaling,
the deployment slots,
things that web apps provide,
you can take advantage of as a container.
So, Azure is really providing lots of options.
There's pros and cons for each of these.
So, in this course and in this section of the course,
we're gonna be talking about Container Instances
and Container Apps and the scaling of those.
And we'll talk about container registry as well
as a related service.
So, stay tuned for that.


### 📺 Lesson: ACI Azure Container Instances


Instructor: So we talked at the beginning
of this section about the various types
of containers within Azure
and one of them is called Azure Container instances.
Now, we saw this briefly
when we were talking about scaling for AKS,
that you could burst scale into a container instance
and that container instances were both cheaper
and faster in terms of deployments.
And so in this video we're going
to create Azure Container instance or abbreviated as ACI.
We'll see how easy that is and the limitations of that.
So Microsoft does like to tout that this is one
of the fastest ways of deploying container apps
without having to manage underlying virtual machines
or having to use cube control or any of those things.
It's just quick and simple to deploy a container image.
Now, you could argue that Azure web apps
with containers is not difficult either,
but we'll we'll compare and contrast those two.
So let's start with container instances.
We'll go into the create a resource
and we see that container instances
is under containers and I'm gonna say Create.
And we do have to create a resource group,
So I'll call this AZ container and give it a name.
The name only has to be unique within the resource group.
We have to deploy it to a location,
so I'll deploy it to Canada Central.
Now, it does support availability zones
but since you're only deploying one of them,
you don't have the checkbox metaphor
where you can deploy two or three.
So if I do deploy to an availability zone
it's just gonna live in that one zone.
There is the difference between standard ACI
and a new trusted execution environment.
We saw this on VMs where you could choose
to deploy this trusted execution environment
and that was the default,
but that is a region specific and you can't choose it,
if it doesn't live in this exists in this region.
Now, that's pretty much it.
We do have to choose the image.
So we could have manually copied
the MCRmicrosoft.com URL here.
We could have an Azure container registry
of our own inside of Azure, or we could choose from a list
of quick start and we can see that in the quick start,
the Hello, World is one of them.
So I don't have to paste in the URL,
it's one of the options.
We also have a Linux web server called Engine X,
and a Windows Web Server, which is a server core.
So I'm going to deploy the Hello, World app
that we just saw for Kubernetes.
Now, it's going to be a very small server
one virtual CPU and 1.5 gigabyte memory,
but it's a Linux machine should not be a problem.
We do have the choice between public access, private access,
which is only for Linux and not for Windows or no access
and you're gonna have to add access
in order to get people to do it.
So we'll leave it as public access.
Now, we're going to have to come up with a DNS label
and so I'm gonna call this AZSJD app.
Now, it does actually create a scope for this
so I could choose, like even I could choose webapp
because it's going to to hash my tenant
and come up with a sort of a label to append to this.
I'll leave that by default.
I could turn that off or have a subscription level reuse
or resource group, tenants is fine.
Port 80 is fine as well,
I won't add the 443 port.
How does the container get restarted on failure?
It gets restarted always once it stopped or never.
I can mark it secure.
I'll leave all of these with the defaults.
So we'll skip over the Tags and we'll see review and create.
So this obviously the interface was a lot simpler
than Azure Kubernetes,
plus we've specified the image.
We don't have to deploy an image into it.
It's going to launch deployed.
So I'm gonna hit create.
So we can quickly see how long did
that take to deploy, operation details
and it took 41 seconds.
So that's a very quick way to get an image live.
I say go to resource
and like I said it has taken my tenant,
turned it into a unique string.
And so I can have webapp.mytenant, all of this.
It says running,
now if I go under settings and under Containers,
I can see that the image was pulled, pulling pulled
and that the image was started
and the current state is running.
So what I can do is open a new web browser here
and I can paste the URL into it and boom, right.
We have our container instance already loaded,
the app, this the Hello, World app loaded as well.
So that's as simple
as it is to deploy an Azure container instance.
Now, Azure container instances are great
for when you need a quick deployment.
You're not interested in complexity,
in terms of having multiple servers
and pods and scale sets and all of these things,
but there is limitations.
So like I said, we do have our single container
that's running right now, hasn't been restarted.
Now, there's not really any settings to speak of.
If we go under containers
we see you have the container, but it's not even clickable.
There's no properties here;
nothing that you can change in this Azure portal.
And that's sort of one of the downsides
is there's no scaling involved, right.
So it's not like you're gonna be able to scale up
and scale down and scale out you.
It could be public if you want,
but really it's limited.
And that's why people use this in conjunction
with an AKS instance where if you need to scale
it'll create you a container instance.
But that's the AKS is what handles the scaling.
It'll create it and it'll destroy it
when it's no longer needed and things like that.
So Azure container and says
as we saw, extremely simple, limited, quick,
and the one of the easiest ways
to deploy a container image live for testing demonstration,
Very simplistic purposes.


### 📺 Lesson: Scaling Azure Container Instances


Instructor: So I just wanted to create this quick video
to talk about scaling for Azure Container Instances.
The requirements for this exam says,
configure sizing and scaling for Azure Container Instances.
Now, there's only a couple of ways
that you can work with scaling
within Azure Container Instances.
As I said in the previous video,
when you create the instance, that's it.
It's a single running instance.
You have no control over the hardware.
And when you go into the Azure Container Instance overview
on the portal, you can't.
There's no auto scale.
There's no manual scale.
There's no way to modify what's running.
So in order to actually change the size
and the amount of resources available to a container,
you effectively have to redeploy the image
to a new Azure Container Instance.
As you can see, when you create an ACI,
you have this option for size.
And it says change size.
You have the number of CPU cores
that you can choose between 1 and 4.
And you have memory.
You can choose between 1 and 16.
Again, this cannot be modified
once you have launched this ACI.
And so one option is to launch a new ACI.
If you needed to go from 1 and 1.5 to 2 and 3,
you launch a brand-new ACI,
and then you can eliminate the old one.
And if you have this running
behind some kind of load bouncer
or something like that,
then you don't have to change the public IP address.
It's a really manual process.
And obviously you gotta script this,
and it's a little bit of effort.
What Microsoft does want you to do is
use something like AKS, the Kubernetes service,
that has the orchestrator.
Now, we've talked previously in this course
about burstable scaling into Azure Container Instances.
And so if you enable that option,
then what you get is what's called a Virtual Kubelet.
It's very similar to the Kubelet,
the Kube control application
that you can control your ACI using that,
again inside of AKS scaling.
So you have some more control.
The other option is container groups.
And then you could have multiple containers
running inside the group, et cetera.
So the standalone ACI instances,
you really don't have any automated or manual options
for scaling other than redeploying the container.
If you use some kind of orchestration method like AKS,
then obviously you have other options.
If you did everything manually,
you had your containers running behind a load bouncer,
you can add and remove containers
in a horizontal scaling method as you wish as well.
So scaling within Azure Container Instance is not easy.
Still doable.
Better to use a more complicated solution
like container apps or AKS.


### 📺 Lesson: ACI Container Groups


Instructor: So in this video,
we're gonna talk about container groups.
Container groups are a collection of containers
that are basically running in the same host.
So you can imagine you have a Azure container instance,
and it has more than one container running in that set.
It has one app name, you know,
a public IP address with a DNS name.
And that means that if they're running on the same host,
then they would have to have different ports.
And so you can have two apps running in the same host.
That makes it very convenient
for them to talk to each other.
You can have one that's private, one that's public.
There's a lot of advantages to having.
This is very analogous to pods,
the concept of pods within the AKS environment.
So for ACI, you can have container groups.
Now the problem that we will have
is that you can't create container groups
in the Azure portal.
It must be created within the command line.
So we're gonna go into a Bash CLI right now.
I'm going to pull this up.
And we're going to deploy a couple of test images
into a container group.
Now, we're gonna use a code editor.
Remember I said before, there is three of them.
You can have Vi, you can have Nano, or you can have code.
And we're gonna create a new file called azuredeploy.json.
This is a typical code editor view.
Now, I am copying this code.
I will put a link to this in the attachment,
the resource for this video.
All right.
So it does contain, it is an ARM template.
I'm gonna basically shift insert to paste the code in there,
and we'll take a look at this.
So this is a typical ARM template
and it has two containers.
One is ACI tutorial app,
which is the ACI Hello World that we've been dealing with,
and then there's also a sidecar app.
And so what it's doing is creating a resource
called ContainerInstance/ContainerGroups.
And we are passing in as properties the two containers.
One is the tutorial, the Hello World container,
and it's got port 80 and port 8080 open.
And the second one is the sidecar.
And you'll see there's no ports
that are being requested for the sidecar,
running in a Linux container.
And it's going to have a public IP address.
All right, there is a one single parameter,
but it does have a default, so that's fine as well.
So I'm gonna right click this and say save,
and right click it and say quit.
So now we have a deployment file.
And we have to do a couple of things in order to deploy it.
First thing we wanna do is create a resource group.
So AZ group create.
We give it a name.
It's gonna be myRg.
and we give it a location, eastus.
All right, so we have a brand new resource group, myRg.
And next we gotta do is do AZ deployment group creates,
and that's going to deploy
this json file that we just created
into the resource group we just created.
So I can say resource group, myRG,
and templates file is azuredeploy.jsun,
or whatever you named that file.
So this is going to deploy those two sample images
into two ACI instances running inside of a resource group,
running inside of a container group.
So we'll let that run.
So we have a successful deployment according to the output.
Let's clear this.
There's a couple of ways to look at this.
We can use the AZ container show command,
and choose myRg resource group
and my container group as the group.
And we can see the my container group is running,
and it it tells you which images are there,
the IP address that's available.
The other way we can look at this, of course,
is to, I'm gonna pull this down a little bit,
go into resource groups of the portal.
We can see myRg is there.
We can see my container group
is a container instance.
Plural.
And now we can go inside of here
and we can look at on the containers tab,
we can see there are two containers
in this container instance and they're both running.
If we really wanted to, we could go to the public IP address
and we can get the demo image.
Unfortunately, we can't load these sidecar app
because it's not exposed publicly, of course.
But in this way, we've created a container group,
which is a set of containers running in the same host.


### 📺 Lesson: Azure Container Apps


So in this lesson,
we're gonna dive into Azure Container Apps.
This is a relatively newer service.
It popped up around 2022
and made its way onto the AZ-104 exam shortly after.
You can think of container apps as the Goldilocks solution
for running containers in Azure.
On one hand, you have Azure Container Instances,
which are super simple
and lack advanced features.
On the other hand, you have the Azure Kubernetes Service,
which is incredibly powerful,
but comes with a ton of complexity,
managing nodes, clusters, and all that stuff.
So Azure Container Apps sits right in the middle.
It gives you serverless containers
with some of that Kubernetes power
like scalability and load balancing without the headache
of managing the underlying infrastructure.
So let's jump into the portal and see how to deploy one.
So if you're coming from the portal dashboard,
you can simply type container apps in the search bar,
or you can go into all services under Containers
and you'll see container apps there as well.
So I'm gonna click the Container App Creates button.
Now first, we're on the Basics tab
and we've all seen this before.
We need to pick the appropriate subscription for this
and pick the appropriate resource group.
And we have to give the app a name.
So I'll call this azurecontainer, one word.
Now you'll notice that you could deploy an Azure function,
developed externally and packaged as an image
into this container app.
We're not gonna address that right now.
We are going to deploy this as a container image.
And so either you bring your own container registry
or you build it from a Docker on your own system
and deploy it as an image.
You have the option of deploying the source code.
And so this introduces a new source code tab
where we can see where the image is going to come from.
So let's just deploy traditionally as an image.
So the first concept we're going to really deal with here
is this concept of the environment.
So this is like a secure boundary for your container app.
So you can create an environment
and deploy multiple container apps
into the same environment.
So I'm gonna create a new environment.
I'm gonna click the Create a new environment button.
Now you'll notice that I chose a region
on the previous tab there.
We do have to give the environment a name
or just accept the name that it's giving to us.
Now we also have options for zone redundancy
if we want this to be in the high availability category.
You'll recall talking about virtual machines
and we talked about zones.
This adds to the redundancy
and increases the high availability of the solution.
So if I need that, I can click Zone redundancy.
Next up, we can identify
whether we want to have customized hardware.
So if we know that we have a specific workload
that we're running on here,
then we can create a new workload profile.
The default that we're being offered
is a consumption profile,
and the environment always has one available
where it's basically scaling up to four CPUs,
eight gigabytes of memory,
and it allows it to scale to zero
and pay for only resources you use.
A typical consumption workload.
If we go on the Monitoring tab,
we're gonna see the traditional log analytics options.
So if we want the container app to log its usage
and be able to manage performance through log analytics,
then that's available.
We can send it directly to Azure Monitor,
and that will be a traditional diagnostic settings.
Or we can say we don't want logs saved anywhere.
They'll be streamed, but not saved.
We can certainly choose that for this demo.
And do we want this container app
to be available to the internet?
I do.
Do we wanna deploy it to a virtual network?
And I don't, right?
This is the traditional public internet.
Deploy it specifically to a network
or even using private endpoints.
So now I'm gonna Create for the environment.
So now on the Basics tab, everything looks good.
We have a brand new environment being created.
We're gonna deploy to this region.
Next, I'm gonna say Container.
Now this is where I identify the image that I want to use.
On this case, I will use a quick start image,
but if I have an Azure Container Registry,
I can choose from that and deploy an image that I've created
or a public Docker Hub image.
Let's pick one of the simple Hello World containers.
You'll notice that this Hello World
is asking to reserve a quarter of a CPU
and half a gig of memory.
Remember, when we created the work profile,
in the environment, we had a much larger four CPUs,
and I believe it was eight gigabytes of memory.
So we are using only a fraction of the memory
that we have available to us on this workload profile.
So this means we can deploy a number of these container apps
to the same environment
because they're only using a fraction
of the available space.
Now, since I want this to be publicly accessible,
we have ingress settings and those are set to enabled.
We want to accept external HTTP traffic over port 80.
Now, we don't need to define any tags for this,
and I'm gonna click Review and create for it to validate.
So the validation passed and I can click Create.
And that'll take a minute or two to create.
And that was pretty quick.
Let's look at how quick that did take.
If I go under Operation details for the app,
three minutes.
So we're gonna click on Go to resource.
And we're in the Container App Overview.
Now you'll see the application URL on the screen.
I'm gonna see Copy to clipboard to get that URL.
And if I paste that URL into a browser,
it says, "Your container app is running
with the Hello World image."
So that was successfully deployed.
So now let's go back to the portal
and look at the container app in the portal.
Let's see what makes this different
compared to an Azure Container Instance.
Under the Application menu,
we can click on Revisions
and we can see the details of what was deployed
to the container app.
Container app supports multiple revisions
of your app running at the same time.
So whereas we can use deployment slots,
in web apps, we can use revisions
to have multiple versions running
and have traffic diverted on an A/B test between them.
If I go to the left and click on Scale,
I can see the rule is being replicas zero,
max replicas 10 in this particular setup.
So it'll automatically scale between zero and 10 instances
based on the demand.
We can see that there's already been an HTTP scaler
that's been added to it.
But if I wanted to set up my own scale rules,
I can add the scale rules here.
So unlike the ACI, this can scale,
and it can scale based on the HTTP traffic
or even triggers such as the number of messages in a queue.
That is basically what they call KEDA, K-E-D-A,
Kubernetes event-driven autoscaling.
But you don't have to configure
anything Kubernetes-related to use it.
You get the scaling options as part of a container app.
So let's recap.
The Azure Container Apps gives you serverless,
scalable container platform that's enterprise-grade,
but also developer-friendly.
You get features such as autoscaling, ingress management,
and DAPR integration
without ever touching a Kubernetes cluster configuration.


### 📺 Lesson: Azure Container Registry (ACR)


Instructor: So we saw when we were creating
the container instances and the container apps
that we had the option of pulling the image
from a registry that we control
as opposed to the sample image.
And one example of that would be
the Azure Container Registry.
So Azure Container Registry is basically
a private container that lives in Azure
that you can store your images.
It's like a code repository, but you're not storing code.
You're storing compiled images for your containers.
It supports versioning, it supports types of security,
granting access to certain people to it.
Again, this is a private repository.
You have the choice of setting the particular
level of privacy that you want on your images.
It allows you to have tasks that do automated builds
and automated deployments.
Once you push something into the registry,
it can actually cut off some tasks.
So I'm here to create a container registry.
I'm putting it in my resource group,
I'm giving it a name, giving it a location.
Container registry does support availability zones,
which means that it gives you an additional layer
of availability if one particular data center
in a region is down.
If you've deployed this into several zones,
you would have a redundancy.
That's only available on the premium plan.
We have basic, standard, and premium options.
We can see from the Microsoft Learn website,
basic is more like a developer option.
It comes with a low amount of storage
and it's really for lower-usage scenarios.
Standard is the same as basic except it has higher
amount of storage and can pass through more images
in terms of its bandwidth.
It should satisfy most production scenarios.
And the premium registry has the highest amount of storage,
highest amount of concurrent operations,
and it also has geo replication so that you can have
a single registry across multiple regions,
and you can even use private links
so that it doesn't even have a public URL.
You have to set up this point-to-point connection
to restrict access to the registry,
and as we saw, then you could use
the availability zones as well.
So for the purpose of this demo,
I might as well just pick a basic registry.
Oh, in order to get this as a proxy
onto a network where I can have private access
versus public access, I do need to be
on the Premium SKU.
Customer Managed Key is only available on the Premium SKU.
And then I can save, review, and create.
So like I said, this is just like a container.
There's a certain amount of storage.
It can handle a certain amount of transactions
per second, et cetera, but it's tied
towards container images.
So I'm gonna say go to resource.
So on the basics here, you can see
I have 10 gigabytes to work with.
Obviously a low amount.
That would be restrictive if I wasn't
only just doing this for development.
So in the next video, I'm going to show you actually
how I will push an image into the repository
and pull an image out of the repository
as a demonstration of what a container registry can do.


### 📺 Lesson: ACR Demo


NOTE
This file was generated by Descript
So let's create a sample app that we can
then deploy to the container registry.
So what I'm going to do is I'm
in Visual Studio 2022 and I'm
going to create a new project.
Now there's many ways to get
images you could obviously
download from one of the public
repositories and image to your local.
I'm just going to create a
new app in visualstudio2022.
net core web app.
and I'm going to call
this docker sample app.
Now, remember that, on windows home
edition, you can't run windows containers.
You have to be the professional or
enterprise edition in order to do that.
so I've chosen Linux as the operating
system and it says enable docker.
So these two elements are the
key for this particular screen.
I'm running on NET 7, which
is a later version of NET.
I'm going to say create.
I do have Docker running.
The Docker engine is currently running.
I have a Windows subsystem for
Linux 2 installed and running.
So all of the prerequisites are there.
and now I have this, sample Docker app.
You can see in the debug Toolbar.
This says the green play button.
It says Docker.
So if I go to run this, it's going to
try to run it inside a Docker container.
In the container tools output, I
can see verified that it's running.
Docker Desktop is running a
deck, verifying it's Linux.
It does match Linux.
It's pulling in, the missing Docker image.
So I don't have NET 7 Docker image.
So it's downloading that.
And, It's ready.
Everything seems to be ready.
So if I wanted to, I could run this
in a debug mode locally, and this
will, compile the application, turn
it into an image, and put it into
a container on my local machine.
Now it says finished.
So let's do that.
I'm going to say, Go.
So it's going to try to
build this sample app.
I made no modifications to it, and
it's basically going to, created
this as a DLL, and now it's going
to create this as a Docker image.
And so it is running.
It says welcome, and it's
running under my local host.
So this is a docker container that has a
web listener and so running against this
port inside of docker on my local in a
command prompt, I can say docker container
LS, and I can see that my docker sample
app is running in a container on my local.
I can even see the port number 32768.
Great.
So right now we've proven that we've
got a, this is a Docker image, but this
is not exactly what we wanted to do.
What we want to do is we want to push
this into the container registry.
So under build, I'm
going to choose publish.
Now I've never published this before,
and so I'm publishing this to Azure.
It does say Docker container
registry, but that is obviously
a third party container registry,
and we're talking about Azure here.
So I choose Azure as a target.
And I could deploy directly to an
Azure Container App or an Azure
App Service, but I want to publish
to the Azure Container Registry.
So I say next.
Now I do have to log in, so you can
see here, we did not find subscription.
I do have to choose my subscription.
I'm going to validate my credentials here.
Alright, so, it's able to recognize my
account, my subscription now, and I can
find the Azure Container Registry that
we created and select how to build and
push the container so I can create the
container using.net, or I could build
the container using Docker desktop.
Now I do need to have a Docker file.
You can see there is a Docker
file, so I'll just do that.
Actually, at this point, it's
just created the profile.
So I'm going to say close.
And now I have to say publish.
So it's going to rebuild the app here.
You can see it's calling Docker
behind the scenes to rebuild it.
And now it's completed the build
and now it's starting to publish.
And what we're going to see here is it's
going to be uploading these files into
this Container registry at this URL,
you can see it's pushing.
That's a good sign.
Finally, it succeeded.
So apparently this is now sitting
in my Azure Container Registry.
So I can go into my
Azure Container Registry.
I can go down under services
and see repositories.
Haha, I'm authorized.
So this has been happening to people.
What we have to do is specifically
give ourselves reader access
to this repository, or in
this case, owner, I guess.
Go into Access Control,
Add Rule Assignment.
I'm going to give myself reader access.
Selected my own account, and I'm
going to say Review and Assign.
All right, so if I go back to our
repositories, I can see the Docker sample
app, and we just deployed one version,
so it's the latest tagged version.
So now we have an app in our repository.


### 📺 Lesson: Docker Pull and Push


NOTE
This file was generated by Descript
In this video, we're going to pull
a public image from the Docker
Hub and we're going to push it
into our private Azure repository.
So we're going to do a Docker pull
and followed by a Docker push.
Before we do that, I'm running
this in my PowerShell on my local.
So before we can connect, we
need to connect to Azure and then
connect to the container registry.
So I'm going to say connect
AZ account from my local here.
You don't have to do this
from the cloud shell.
And then I have to log in.
Authentication complete here.
Now I have more than one
Azure subscription, so I
do have to set my context.
So get AZ subscription
to get a list of them.
And then I'm going to say set
AZ context with the subscription
that I'm interested in here.
Alright, so I do have to connect
to the container registry as
well as being connected to Azure.
So it's connect azcontainerregistry
and just the name of the registry.
Azure is going to fully
qualify this for us.
It'll say log in, succeeded.
Now if it doesn't, sometimes you
do have to allow yourself what
is called admin user access.
If so, this checkbox on the
access keys if this doesn't work.
So now we're logged into Azure.
We're logged into the
Azure Container Registry.
So just to be safe, let's use the,
Docker login command in order to
authenticate Docker application with the.
Azure Repository.
And that says login succeeded.
Now we're going to go back to effectively
what is Docker and say Docker pull.
And we're going to get the, NGINX.
This is a very small, web browser client.
So web server, I mean, so Docker pull
NGINX, and you can see it's going
to a public registry to download.
the latest NGINX server.
All right, so that, pulled into my local.
Now, one thing we can do is we can run it.
So we can use the docker run command
and we can basically give the parameters
to say we want interactiveness IT on
port and we're going to use port 8080
mapping to port 80 within the container.
And we're going to start
the NGINX image locally.
So this is going to start up a
little web server on my machine.
In order to see that this is
running, I'm going to have to go into
localhost, and it's on port 8080.
So now we have NGINX, responding
to our little Docker server.
So we know that it worked.
We pulled the correct image.
I'm gonna say Ctrl C to stop
the server from running.
Alright,
now we're gonna use
the docker tag command.
And what this is gonna do,
it's going to add an alias.
So we have this local Nginx,
repository and we're going to add
to in your case, it's gonna be
different, but my A Z S JD demo.azure
cr.io and we're gonna call this.
EngineX.
And what this is going to do is it's
going to say this repository has
basically a, alternate location.
It's called the tagging and namespace.
All right, now that the, image has
been tagged with the remote server
name, you can now say docker push with
that same server name with azsjdemo.
azurecr.
io slash sample slash nginx.
I can say Push.
And it's now pushing.
You can see the work being done,
and the image has been apparently
pushed, and it's giving me the SHA 256.
If I go back to Azure Container Registry
under Repositories, Drumroll, there's
the samples slash NGINX repository
that we just pushed using PowerShell.

