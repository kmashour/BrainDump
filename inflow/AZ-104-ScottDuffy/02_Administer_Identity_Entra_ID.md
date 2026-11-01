---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "02"
title: "Module 02: Administer Identity (Microsoft Entra ID)"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 02: Administer Identity (Microsoft Entra ID)

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** Entra ID (Azure AD), Free vs Premium P1/P2, Custom Domains, Users, Groups, Licenses, Administrative Units, Devices, Bulk Operations, External Users, SSPR  
**Line Range:** Lines 650 – 3861 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


## 🏛️ Section: Introduction to Azure Active Directory (Azure AD or Microsoft Entra ID)



### 📺 Lesson: Assignment: Create a Budget


[No transcript available for this lecture]


## 🏛️ Section: Manage Microsoft Entra users and groups



### 📺 Lesson: Udemy Video Player


Instructor: So, before we get into the content,
I just wanna take a minute here to talk
about the Udemy Video Player.
In the bottom left of the screen is the speed control
and if you think I'm talking too fast or talking too slow,
you can change the speed of that down in the left.
On the right is the captions,
and if you want to see the text
of what I'm saying at the bottom of the video,
you can choose either the English language captions
or in another language.
If you want to see a transcript,
there's also a transcript button, and so you can see
on the side of the screen the script of this video.
Finally, reviews are the lifeblood of this course,
so if you do choose to leave a review,
I would be so grateful.
This will help other students to find this course
in search.
If you're not ready to leave a review,
you can click the ask me later button
or ask me at the end of the course.
Both options are available to you,
but if you are willing to leave a review,
thank you so much for that.
I really do appreciate it.
Thanks for being a student.
If there's something that I can do
to make your experience better, please let me know
in the Q&amp;A section of the course, thank you.


## 🏛️ Section: Manage role-based access control (RBAC)



### 📺 Lesson: AZ-104 STUDY GUIDE - FREE PDF DOWNLOAD


[No transcript available for this lecture]


## 🏛️ Section: Manage subscriptions and governance



### 📺 Lesson: AZ-104 30-Day Study Plan


[No transcript available for this lecture]


## 🏛️ Section: Configure access to storage



### 📺 Lesson: Frequently Asked Questions


[No transcript available for this lecture]


## 🏛️ Section: Manage data in Azure storage accounts



### 📺 Lesson: Amazing Microsoft Resources


[No transcript available for this lecture]


## 🏛️ Section: Configure Azure files



### 📺 Lesson: Overview of Azure Services


Scott: So, in this video and the videos that follow,
we're gonna talk a very high level,
30,000-foot overview
of Microsoft Azure components as a whole.
Throughout this course,
we're gonna get into a lot of details.
I'm gonna talk about each
of these things one by one in several videos.
But right now, I just wanna spend some time
looking at the services that Microsoft Azure offers
from a very high level overview.
This is the concepts,
especially the ones that are relevant to this exam.
Now, I should say that if you have some background in Azure,
this is gonna make a lot of things easier.
If you've taken and passed the AZ-900 exam
or watched my AZ-900 fundamentals course,
or Microsoft themselves have a series
of free online courses relating to Azure fundamentals
on their Microsoft Learn website,
the concepts I'm about to talk about
are going to build upon those
and maybe be a bit of a refresher for those.
And as we go through the course,
we're obviously gonna fill in a lot of those details.
I should point out that not all the subjects
we're gonna talk about in this video
and the videos that follow will be on this exam.
First of all, the exam objectives
do change from time to time,
not as often now as they used to,
but it's still possible
that Microsoft will remove something or add something.
That's why it's so important to go to the official exam page
to make sure what the latest requirements are,
make sure the date hasn't changed.
Now, the first thing I would start off
by saying is I believe there are three core services
that sort of underpin so much of what we're gonna talk about
as an Azure administrators in this course.
These are virtual machines,
virtual networking, and storage.
Now, I used to say
these are like the three legs of the stool,
and almost anything that you want to do
is going to be some mixture of these three things.
Even we talk about Platform-as-a-Service
in terms of app services,
or we talk about SQL server in a virtual machine,
and things like that, these are all parts
that rely on the underlying infrastructure,
and that's why I think these things
are the three core services.
And we're gonna talk about
each of these three in the next video.
We'll talk about virtual machines
and app services, and things like that.
I also wanna add that something that's often overlooked,
which is identity services, specifically Microsoft Entra.
So, the concept of identity,
who has the ability to even see that something exists?
Who has the ability to control something?
It's sort of weaved into every service,
every product that Microsoft Azure offers.
So, you're gonna find as you go through your journey,
sometimes you won't have
the right permissions to do something.
You'll have to circle back, grant yourself those permissions
or application that you're trying
to do doesn't have permissions.
And these are gonna be fundamental elements as well.
But beyond the three machines,
networking, storage, services,
we also have this concept of identity.
So, in this next set of videos,
we're gonna talk about these things,
virtual machines, virtual networking, storage,
and a lot of other Microsoft Azure services
that we're going to encounter
in this course and in our careers.
So, come back for that.


## 🏛️ Section: Azure Virtual Machines



### 📺 Lesson: Overview of Azure VM and App Services


So let's talk about some of the services
that overall can be considered Azure compute.
The first service that we'll talk about
is the virtual machine.
Now, virtual machines
are Azure's Infrastructure as a Service offering,
or IaaS for short.
You can deploy either Windows or Linux virtual machines,
you can connect to them via RDP or SSH,
and you'll be able to treat these machines
just as if they're a physical server.
But it actually isn't a complete server,
it's a virtualized server,
or a server that has been split up into segments
that individual customers like ourselves can use.
Now, just like in real-life,
virtual machines must be placed on a network.
In the case of Azure, it's called a virtual network,
and you have the ability to arrange them in various ways,
depending on your needs.
So if you put them in an availability set,
you can arrange so that they're not gonna be all taken down
for maintenance at the same time.
If you were to put them into availability zones,
you're protecting against building-level outages,
such as power outages and internet outages,
you can place them behind load balancers
to provide maximum availability to your customers,
et cetera.
Since they are the operating systems
of either Windows or Linux,
you have administrative connectivity to them,
you can install whatever software you wish,
just as if you had a server in the back room.
So you have the full control to install whatever you need.
And it usually can only take a few minutes
from the time that you start the process
of starting a virtual machine or creating a virtual machine
until it is provisioned and it's ready to go for you.
So, within 10 minutes, you can have a VM of your own.
Now there are other services in Azure
that are made up of virtual machines behind the scenes.
And so, for instance, the Azure Batch service
lets you run large-scale parallel jobs.
So let's say you are a drug-maker
and you need to run a large-scale test
of a particular chemical reaction, you need to model that,
you can have hundreds of virtual machines
running the same task and reporting their results
back to some central location,
that would be a typical batch job.
We have the concept of scale sets, or VMSS for short,
which lets you automatically scale VMs in and out,
so if you have two or four or eight
or 16 virtual machines running,
they all serve the clients independently
and you can add to them if you need more capacity.
We're gonna talk about the details of each of this
as we get into those sections of the course.
You have containers like Azure Kubernetes Service, or AKS,
that is a fully-managed Kubernetes environment,
those run on virtual machines, but they run as nodes,
and there's an orchestrator that manages them.
And, finally, you have a service called Service Fabric,
which is a platform for building microservices,
although, it is used less often these days.
Now that we live in a containerized world,
containers are way more popular for microservices
than Service Fabric.
Not all of these are going to be on the exam,
so I'll point that out.
Next up, we'll talk about app services.
Now, Azure App Services is fully-managed platform
for running web apps or containers
without managing the underlying server.
So it's really an abstraction on top of a virtual machine.
You can also choose Windows or Linux operating system
for app services,
although with that abstraction,
the difference matters a little bit less.
It supports a wide range of frameworks,
such as .NET, Java, Node.js, and others.
App services also add a number of built-in benefits,
like auto-scaling, deployment slots,
continuous integration, continuous deployment,
and even compatibility with Visual Studio.
These are going to be on the exam,
these two topics, of course.
So that's it for the compute services
we'll cover at this high-level,
I guess that we have individual sections and videos
covering them later in the course.
Next up, we're gonna talk about storage.


## 🏛️ Section: Automate deployment of resources by using templates



### 📺 Lesson: Overview of Azure Storage and Data Services


Next up, we'll talk about storage.
Now, the first type of storage
is sometimes called unmanaged storage,
or just a storage account in Azure.
One of the great features of this is
you can have almost unlimited amount of data
in these things.
It's scalable into the petabytes range,
and, if you fill that up,
you can certainly create more storage accounts.
So it's really an expandable storage option
even for on-premises applications.
Now, within a general purpose storage account,
there are four types of data that you can store
all within the same storage account.
They are blobs, queues, tables, and file share.
We are gonna get into blobs and file shares in this course.
Queues and tables are not covered by this exam.
Now, storage accounts are highly scalable
with built-in redundancy options,
so you can have local storage redundancy
or even global storage redundancy.
And, in terms of access,
you can have either hot, or cool, or cold,
or even archive tiers,
which allows you to pay different amounts,
either a little bit more expensive, a little bit cheaper,
based on how frequently data is accessed.
And there is such a thing as a managed storage account,
mostly for virtual machine hard disk.
And what we've been talking about on this screen is
the unmanaged version,
which is the most common, obviously.
Now, the other way to store data in Azure is
using a database,
or what I'm calling data services.
We can further categorize that
between the relational SQL databases
and the non-relational NoSQL databases.
On the SQL side, you have Azure SQL Database
managed instance,
or you can even install and run
your own SQL Server software inside a virtual machine.
Those are your options on the relational side.
We also have the non-relational options,
and primarily Cosmos DB,
and all the different types of ways
you can store non-relational data in that database.
There are also open-source options as well,
but they're not gonna be talked about as much.
Now, we've got Big Data solutions,
so the primary one being Synapse Analytics.
That is what used to be called SQL Data Warehouse
many, many years ago.
That is for data warehousing, obviously, and reporting.
And one of the up-and-coming options is called
PostgreSQL Flexible Server.
So PostgreSQL is one of the in enterprise-grade,
open-source options,
the Flexible Server being a Microsoft-managed product,
and Microsoft is constantly coming out with new features.
Every few months, you'll see that they've released
something new for Flexible Server.
Just be aware that these things exist.
None of this on this screen is on this exam.
The storage stuff is,
the database stuff is not,
but we do need to know, when you're creating applications,
that you do have lots of database options to choose from.


## 🏛️ Section: The Benefits of Azure Bicep



### 📺 Lesson: Overview of Azure Networking Services and Microservices


Instructor: Next up, we'll talk
about what are called microservices,
and in some instances can be truly
called serverless or event-driven programming.
So microservices is this concept
of multiple small applications
all working together to perform a job.
And so instead of having one big
monolithic program with millions
of lines of code,
you might have 10 or 15 small programs
that can be operated independently,
scaled independently, updated independently.
It makes it easier for maintenance,
and you can deploy them
in a cloud service like Azure.
Now, oftentimes in modern times,
these are done within containers.
And so Azure Container Apps is one
of the popular options for deploying containers.
We talked about Kubernetes
under the VM abstractions section
a couple of videos ago,
but Container Apps
is the Microsoft managed container service.
We can also put API management.
Now API management is basically a front end
for your existing APIs.
It allows a bunch of different
throttling documentation.
You can block certain requests,
change the headers, lots of different services
within API management.
I would put that in terms
of API based microservices in this category.
Container instances are smaller
standalone containers, but you can certainly
count them in with microservices.
Finally, I'd already mentioned Service Fabric.
It plays a smaller role within Azure
and is not on the test, of course.
Now on the serverless side,
or you can even call it event-driven,
you've got services like Azure functions
and Logic Apps, which are great
for reactive event-driven tasks.
And these are not on the exam.
Now lastly, I'll talk about networking.
Now, networking in Azure is a major
responsibility for administrators,
and of course it's gonna be important
for performance, for security,
for routing and monitoring.
So how we configure networking is going
to be part of this role.
So I'm gonna break networking.
Networking is a big topic.
There's dozens and dozens
and dozens of services
under this category in Azure.
So I've decided to break it off
into four major categories.
You can have the connectivity part of networking,
security, delivery, and monitoring.
So we'll talk about all of those four separately.
So in terms of connectivity,
connectivity is about how Azure resources talk
to each other or to the internet.
So within this section, we're gonna work
with virtual networks,
which are networks within Azure
that are used to connect resources.
You could have DNS services
peering between networks.
And possibly hybrid connections,
VPN gateways are an ExpressRoute.
Now many of these are not on the exam.
Some of the advanced topics like ExpressRoute
and virtual WAN in will not appear on the exam.
But virtual networking
is a fundamental understanding
of how machines communicate with each other.
And DNS is there as well.
Next up, we'll talk about security.
So Microsoft Azure clearly provides
powerful tools to secure networks.
You've got Network Security Groups
for controlling traffic in and out
of subnets and virtual machines.
Private Link lets you access services privately.
You've got services
like Distributed Denial of Service attack protection,
Azure Firewall, and the web application firewall
that add layers of defense
between the internet and your services.
And finally, I did mention before Azure Bastion,
which allows secure browser-based RDP
or SSH access without even needing
to provision a public IP address
for your servers.
A firewall is more advanced and is not going
to be covered on this exam.
Next up, we'll talk about
what I would consider delivery services.
These are the various helpers
within Azure that help you
to deliver your services.
So CDN, there are standalone CDNs
within Azure as well as built-in CDNs
in a service like Azure Front Door.
Now, Azure Front Door is Microsoft's modern CDN
and global load balancing solution in one.
We can also mention Traffic Manager,
which is a DNS based routing.
Application Gateway is a layer seven traffic manager,
and we'll talk about that.
We have videos in this course on that.
As well as Load Balancer,
which is for traffic distribution
at the networking layer, layer four.
So you should understand the basics
of these things, obviously.
And we're gonna talk about them
extensively in the course.
The last element of networking we'll talk
about is monitoring.
Now monitoring is key to keeping things running.
Azure provides tools like Network Watcher
for diagnostics, logs and metrics for visibility
and Packet Capture for deep troubleshooting.
These services are critical for understanding
what's happening in your virtual networks
and for resolving issues.
Obviously in a cloud-based environment,
you've got millions of customers.
Microsoft has control of the architecture
and the infrastructure.
So it's really tricky trying to figure out
how A is connecting to B
and why this port needs
to be open, et cetera.
So there's a lot of different services for that,
and that is covered on this test.
Now, this is just scratching the surface.
There are hundreds of other services.
Azure offers way more than what we've covered.
AI services, DevOps,
messaging platforms and more.
But as an Azure administrator,
your focus is on managing
and maintaining core infrastructure.
And once you've mastered the fundamentals,
then you can start to specialize
and get into some of these other areas
based on your role or based on interests.
So that's my 30,000 foot overview
on the services offered
in cloud computing in Azure.
As we get into the next section
and into this course, we're gonna dive
into many of these in much, much more details.
So let's keep going.


## 🏛️ Section: Manage Azure VM



### 📺 Lesson: Programming or Scripting on the Exam


-: So from time to time in a role as an Azure administrator,
you might have to write some code
in order to do some automations
to save yourself some time on repetitive tasks
and that might lead you to wonder, for the AZ 104 exam,
is there any programming on the AZ 104 test?
The good answer is that there's not any programming
in the sense of coding .NET, Java, any of the API calls.
This is not a developer test, not even a DevOps test,
but there is some scripting that you're gonna need to know.
So scripting is the form of PowerShell or CLI.
Now, in terms of going to access Azure resources,
the most common way that we're going to do that
in this course is through the Azure portal.
And you might even find through your role,
through your job, that you might find yourself
using the portal most of all as well
and that's perfectly fine.
But there is a couple of other methods
that you can access the Azure resources
running on your account.
There's a few even beyond this,
beyond .NET SDK and there's a REST API,
but I'm want to talk specifically
about the two scripting languages,
of PowerShell and Bash CLI.
The other types of what I would consider to be programming,
which is really just being able to read a JSON,
which is part of ARM templates
and is also returned when we do some CLI commands,
we're gonna see JSON as the results
and so I don't really consider that programming,
but being able to read the output of JSON
is probably a good skill to practice for this job as well.
So we might have a fundamental question
in terms of you just want to skip scripting.
Learning how to do scripting a PowerShell or CLI,
this seems like a waste of time.
It isn't, really, in terms of your job.
You might want to learn some scripting
just so you can do some stuff in an automated manner.
So when it comes to managing your Azure resources,
you may need to create virtual machines, modify
virtual machines, check the status of things, et cetera,
and having to remember those commands
in your head could be a little burden.
Having to remember a multiple step process
does introduce the possibility of error.
So if you've got a 15-step process
to create a virtual machine,
then you may get some steps backwards
and it's gonna take a longer time.
So there's a lot of good arguments
for introducing some automation,
some scripts into your repertoire
in terms of having stuff that you use on a daily basis
that helps you manage a complicated Azure environment.
Another good use for scripts is that you can check them
into some type of source control or central repository
and that way, other people can share in your scripts
and you can actually track the changes over time.
So if you were using one particular set of scripts
all of last year to create a set of virtual machines
and then you make a little tweak to it
because of a new feature or because of an enhancement,
then you can see when that change happened
in your source control repository.
Again, the source control should always contain
the latest version of scripts as well.
So there's no hunting around to see
who has a more updated version of the script
based on the date and time of the modification of the file.
Scripts do reduce errors and so if you are frequently
doing something, just being able to run
a little command line utility is going
to be a big benefit to you as opposed to,
again, having to remember all of the tasks.
Now this is little talked about,
but I also find scripts to be a form of documentation.
And so when you are asking, "Hey, how do we go and do this?"
Looking at the way that the script does it
is probably the most up-to-date answer to that question.
If you have a script that you use on a regular basis
or your team uses on a regular basis,
then you don't need to write flowery language,
you don't need to have Microsoft Word files
that are describing your process.
You can see the process, you can see the variables,
you can see the order of operations.
Code is a form of documentation if you can read the code.
Now, like I said, Azure portal is the most frequent way
that we're going to access the Microsoft Azure
in this course and maybe even in your job.
The URL for that, if you don't know, is portal.azure.com.
Now when it comes to the exam, the AZ 104 exam,
it is also worth asking how will Microsoft test me
on my Azure knowledge?
So there has been, over the years,
what's called performance-based labs.
And so sometimes within the Microsoft exam,
Microsoft will provide you a real,
working Azure environment for you to go in
and ask you to perform a series of tasks.
And then you're just gonna follow exactly what they say.
If they say, go and create a virtual network
and give the network this name and create the subnets
and have the subnets named this
with the following address ranges,
then you're going to follow those tasks specifically.
Now, the good news about the performance-based labs
is that it doesn't matter exactly where you click
and how long it takes you to create this task.
Maybe you don't know exactly where the SSL setting is
and so you have to click a couple of things to find it.
I find that to be a much more forgiving method.
So you can use the portal, you can use
the PowerShells' command line, you can use CLI command line
and as long as you do the task,
the virtual network with this name
and this address range is created,
then you're going to get the credit for that.
I should point out that performance labs
are not on every exam.
I've heard they're bringing them back.
Sometimes they go away if they're having challenges with it.
So performance-based labs are a hit-and-a-miss,
whether you're going to see it or not.
The second way that they'll test you
is sometimes you'll find code is part of a question.
So you'll go and you'll look at a question
and it'll say, "Which of the following lines
of code completes this script?"
And you'll see 10 lines of a script with one line missing
and you're gonna have to look at the A, B, C and D answers
and pick which is the line that would work
to complete what the script is trying to do.
So even though you don't have to write code,
you do have to read code and comprehend
what it's doing and understand what's missing.
Only about half of the exam is multiple choice questions.
The other half are going to be more innovative styles
and one of the styles that Microsoft loves
is this drag-and-drop style
where you would have some items on the left of the screen
and you're gonna drag them with your mouse
onto the right of the screen
and it may be the parameter name of a script.
So script is trying to do something
and some parameter name is missing
and you're gonna pick the parameter name
from the left and drag it over to the right.
So that's the kind of question you might see as well.
Now Microsoft does have PowerShell
and Azure Bash CLI environments within their portal
and we'll talk about this in a second,
but you can see this greater than sign
and underscore right on the Azure portal
and that's gonna lead you to a command line utility
within your browser.
So you click this, you have to create a storage account
the first time you do it, but once you've done that,
you'll be taken into either a Bash command line
or a PowerShell command line based on your choice
and you can switch between them.
So here is the example of a PowerShell command line.
Good, interesting thing about PowerShell command line
is it does accept Bash CLI commands.
So this PowerShell command line is bilingual.
As you can see in the PowerShell commands,
you can actually enter PowerShell commands
such as PSVersion table, .PSVersion and you'll get.
So this is a fairly up-to-date version of PowerShell,
including the Azure components for PowerShell.
And once again, that is on the greater than
and underscore within the Azure portal,
the Azure Cloud Shell.
So let's just sum up, this has been a longer video
and I appreciate your patience.
Let's just sum up my advice in terms
of studying for PowerShell.
Again, you do not actually get to choose
between different scripting languages
and so it is in your best interest
to know a little bit of PowerShell, a little bit of CLI.
I do have a video coming up talking about
how you learn the commands
without having to really study them.
And so you don't get to choose scripting language,
so that's one thing to know.
I do recommend that you get lots of hands on practice
and so as we go through this course,
I'm gonna put lots of demos in this course
for the portal and the occasional
PowerShell and CLI demo as well.
Absolutely, I recommend that you have
your own Azure account, whether it's the free account
or your company account and go ahead
and get a lot of practice inside the portal,
'cause really learned by doing
is one of the strongest forms of learning.
When you are taking the exam,
let's say the exam gives you 120 minutes
to do about 50 or more or less questions,
if your exam contains performance labs,
and not all of them do, but if it does,
then one of the things that I hear people say
is they wish they had more time
and so they could spend 100 of their 120 minutes
doing the multiple choice in the regular testing section
and then they're left with only half an hour
to do the performance labs.
And you really have to hope that things go perfectly,
that the portal is running fast that day,
that your resources are being created
in a very timely manner.
As you know and you will find out
going through the Azure portal,
sometimes you go and you create a resource
that, in the past, takes one or two minutes
and you catch it at the wrong time
and it takes five minutes or 10 minutes.
So leave yourself time for the labs,
because you would hate to run out of time
because Azure is slow that day and that does happen.


## 🏛️ Section: Create and configure an Azure App Service



### 📺 Lesson: Memorizing PowerShell and CLI Commands


So in this lesson
we're going to demystify the command line tools in Azure.
Now I know what you're thinking.
Memorizing hundreds of commands sounds like a nightmare,
but here's the secret: you don't have to.
Microsoft has built in a really predictable naming system
for both the CLI and PowerShell.
Honestly, once you spot the pattern,
you can guess 90% of the commands that you'll ever need.
I want to show you this in action.
I've got my terminal open here, the Azure Cloud Shell,
and I'm starting with the CLI,
which is the Bash command line.
We'll talk about PowerShell in a second.
The pattern here is super simple.
The commands always start with the letters az
followed by a space, and then the service name.
So in this case I'll choose vm.
And finally a verb, what you want to do.
So watch this, I wanna see all of my virtual machines.
So I type az vm list and hit Enter.
And there they are in JSON format.
So did you see that pattern?
I'll do that again.
We do az vm list and that will show the VMs.
Now what if I want to create a VM?
Well, the command, as you might guess is az vm create,
followed by all of the required parameters.
If you want to delete the VM, well, you can guess.
So it's incredibly consistent across not only VMs,
web apps, and other types of resources.
So there is a hierarchy of commands here.
The middle word is what changes and then the verb.
Now sometimes the service name is a bit longer.
So vm is the simple one.
But what if we wanna show virtual networks?
Well, virtual networks actually is a subcommand of networks.
So I'm gonna say az network vnet list.
So you'll see it's two words for the service name.
So network is the broad category
and vnet is the specific item
but still ends in that word list.
Now if we switch over to PowerShell, I'm gonna say Switch.
So it's gonna start up a whole new session.
It's not the same as the CLI session.
It's now a PowerShell session.
One interesting thing I should mention is that
PowerShell in the Cloud Shell supports CLI commands.
So I can say az vm list in PowerShell and it would work,
but that's not a PowerShell command.
Another interesting thing is now that I'm logged in,
I have to set my session,
my context to the subscription
that's relevant to where my VM is.
And so I'm going to say Set-AzContext
just to get to the right subscription.
Okay, I'm gonna say Clear.
Alright, so the equivalent to az vm list is Get-AzVM.
So you'll notice that the verb comes first
with a hyphen Az and then the object of the verb.
So instead of az vm list, it's Get-AzVM.
And now I can see the virtual machine that is running.
Now PowerShell doesn't have the create command,
it has the New command.
So if I was to want to create a new virtual machine,
the command is New-AzVM,
and if I was to want to remove it, it's Remove-AzVM.
So you'll see, even though the words are a bit different,
the syntax is fairly consistent.
So the pattern is verb, which is like Get or New,
Az and then the noun.
So Get-AzKeyVault will be an example
or Get-AzVirtualNetwork.
So when you're in the exam,
or even if you're just working in the real world
and you forget a command, don't panic.
Just think about the pattern.
If you need to retrieve something, you start with Get-Az.
If you need to make something, it's New-Az.
It's that simple.
So go try this on your own.
Go start up the Cloud Shell in the Azure portal.
You can type, a convenient helper is called Get-Command.
And if you want to look at anything that has AzVM in it,
you can just put asterisk around it and say AzVM.
And you can see all the list of commands
and the version that has been installed for that.
So Get-Command is your helper for PowerShell,
and it's that simple.


## 🏛️ Section: Azure Container Instances and Container Apps



### 📺 Lesson: Details about PowerShell and CLI for Managing Azure


All right, so let's talk
about the various command line utilities
that we're gonna see on this exam
and in this course.
Now you may be very aware of PowerShell.
PowerShell is a command line
that is usually included with Windows.
This is not the Windows terminal
or the Windows command line.
This is specifically a tool called PowerShell.
Now some versions of Windows come
with a thing called Windows PowerShell.
If you go to your Windows startup menu
and start typing PowerShell,
maybe you're going to see Windows PowerShell.
That's an older version of PowerShell.
We do not want to be using Windows PowerShell.
What we want is a version that is called PowerShell 7.
Again, most recent versions of Windows 10 and 11,
for instance, do come with PowerShell,
but go check to see
what version of PowerShell that you have.
PowerShell is also a cross platform tool,
so we're not just talking about Windows here,
we're also talking about Linux and OSX, of course.
So PowerShell 7, if you're going to use PowerShell
as your command line tool, is a cross platform thing.
Now, there is also an environment
for people used to the Unix and Linux standard called CLI.
This is also sometimes called Bash,
although I understand Bash itself is its own language.
But CLI is an Azure tool for Linux system,
but it's also cross platform.
If you want to use the CLI app on a Windows system
that's available, you can go and download it.
Again, Bash CLI is native
to these Linux operating systems and OSX,
but is also available for Windows.
So beyond the PowerShell and CLI,
we do need to have Azure modules installed
inside of these tools to make it so
that we can use the Azure command line
with our Azure environments.
Now, if you want to avoid installing anything,
or maybe you're not even allowed
to install anything on your local machine,
there is the Azure Cloud Shell.
So you could either get to it with its own URL
or if you go to the Azure portal,
there's this greater than sign
with a little underscore in the top bar of the Azure portal.
And if you click on that, you get the Azure Cloud Shell.
It's a terminal inside your browser window.
You can run Azure commands.
This is an example of the Get-AzVM commandlet
that is going to return to you
all of your running virtual machines.
But this is an example of a Azure command
inside of the cloud shell.
Now, if you prefer to use a Bash,
you can also use this other...
Wait.
3, 2, 1.
Now one of the great things about PowerShell is
that it is supports the CLI commands.
So within the cloud Shell if you type AzVM list,
that is a CLI command, but we are still in PowerShell
and it still works.
So PowerShell within the Cloud Shell is cross platform
in terms of language.
So let's talk specifically about PowerShell itself.
Long, long time ago, many moons ago,
there used to be this module called AzureRM.
And if you've been around since then
and you're using AzureRM,
well, that's just totally being deprecated by now,
you should be using the AZ module.
Just to be clear, you cannot have both AzureRM and AZ
running on the same system
within the same version of PowerShell.
And so you have to upgrade, you have to uninstall AzureRM
and get up to the AZ module.
Now you can have a PowerShell,
different versions of PowerShell running on your system.
So if you do need both for whatever reason,
you can have one of your PowerShells having the AzureRM
and one of your PowerShells having AZ.
There's really no point, in this year and beyond,
there's really no point having AzureRM.
So you should have it.
So your assignment at this point is to make sure you have,
if you're gonna use PowerShell as your command line,
make sure you have the latest version of PowerShell
and the latest AZ module.
In the next video, I will go through, I'm gonna demo to you
how to download PowerShell, the latest version
and how to install the AZ module.
You may have had an older version of PowerShell,
a PowerShell six
that was cross-platform called PowerShell Core.
Again, I would refer that you use PowerShell 7.
So that is the latest one.
They keep coming up with new versions.
So I put 7.X just 'cause whatever's the latest version
of PowerShell you should be using.
Once you've got the latest version of PowerShell,
then you're gonna be installing the AZ module
and you, say, install hyphen module.
And that's going to you say slash name or hyphen name AZ.
That's going to install the AZ module.
If you already have the module, there's an update module
that you can run that will update it to the latest version.
Once you've got the PowerShell installed
and you've got the latest AZ module, you do need
to connect your version of PowerShell to your Azure account.
And that is a login type process,
that is Connect-AzAccount.
We'll demo that.
So if you want this to be running local,
you could use the PowerShell, like I said, or the CLI.
Again, cloud shell is a perfectly fine way to do stuff,
if you've got scripting to do, you could do it
with the cloud shell or you can run it local.
So if you want to run stuff local
or you have the ability, I say your assignment is
to get the latest version of PowerShell.
We're going to talk about that in the next video.
I do have a link to the website
for that coming up.
And then you are also going to install
the latest AZ module as well.
We do have to run PowerShell in administrator mode
in order to make these changes,
and I'll show you how to do that.
Right click, PowerShell, run as administrator,
and then install the AZ module or update it, as I mentioned.
So this is a good point in the course to pause the video,
pause the course, go download the latest, and install it.


## 🏛️ Section: Manage Virtual Networking



### 📺 Lesson: Live Demo: Installing PowerShell Core with Az Module


All right.
So as I said in the last video,
we're gonna be wanting to run PowerShell 7
in Administrator mode.
So on Windows 11 here, I've typed the word PowerShell,
and I'm brought up to the right version.
And when I start PowerShell,
I can see the word Administrator
in the status bar at the top,
and I can see it says PowerShell 7.5.4.
And so, I searched the web for PowerShell 7,
and I like this GitHub link,
so that's what I'm gonna choose.
Now, I don't necessarily wanna run the pre-released version.
So, on the PowerShell releases tab, I'm gonna scroll down,
and the latest version...
Actually, if I say releases/latest, is 7.5.4.
So I confirmed that I do have the latest release
running on my local.
Now, you can see that there are versions to download
for Linux, Arm, and other chips,
we have OSX, Windows, both 64-bit and the old x86.
If I was to reinstall this,
I would choose the Windows 64 MSI,
'cause it's the simplest installer for me.
Of course, you can choose any of these packages
as they're appropriate to you.
You can also choose to download the source code
and package it yourself, if that's what you want.
Let's download that and install it
to get the latest if you don't have it.
So now that we have
the latest version of PowerShell installed,
the next thing to check is the Az module.
I'm using the Get-InstalledModule commandlet
with the -Name Az in order to see what I have,
and I have version 14.5 running on this system.
So doing a quick check of the PowerShell Gallery
shows me that the latest version of the Az module
is now 15.1.0.
Do keep in mind
that they do release these pretty much monthly,
so, by the time you watch this,
there could be a more recent version.
But I am gonna want to install
the most latest version of this on my local.
Now, we could probably just simply say
Install-Module -Name Az,
and that would be enough,
but we also want it to allow it to overwrite it
if it already exists, which it does not.
But I'm going to have these AllowClobber and -Force commands
to add to it.
So what it's gonna do is download the latest 15.1 version
of Az from the repository,
and we're gonna watch it as it installs.
Now it does download it a module at a time,
and it does it in alphabetical order,
so we can sort of guess how far along,
it also has this progress bar to give us an idea.
So we'll let that run.
So now when I run the Get-InstalledModule commandlet,
I'll see both versions, 14.5 and 15.1, in my case.
Remember, I said in the last video
that they can run side by side.
The way that it works is if you run some type of commandlet,
it's going to do it in the latest version
is the one that it's gonna select.
And you can specify specific versions,
but if you don't specify the version,
it'll pick the latest one, and that's fine too.
So last example is we're going to choose
this Connect-AzAccount.
And this is going to let us log in to Azure,
and it's gonna pop up with a login option,
and we're going to be able to choose whichever,
or log in with a account if we haven't logged in before.
Now, it actually does offer me all of the subscriptions
that I have available.
So I can pick one of them,
and then I'm logged in with the subscription
and the tenant that I'm requiring.
So let's just test it.
I'm gonna say Clear.
So I'm gonna try a command, like Get-AzResourceGroup.
You'll see there's an auto-complete.
If I hit the right arrow, it will accept the suggestion,
and hit Enter.
And I can see all of the resource groups I have
on this subscription.
So we have a working local version of PowerShell
with the Az module.


## 🏛️ Section: Implement and manage virtual networking



### 📺 Lesson: Switching to Another Subscription


NOTE
This file was generated by Descript
Now for most of you watching this, you
may only have a single subscription,
in which case you don't really have to
worry about choosing which subscription
to use in a command line context.
But in this video, I want to talk
about switching between different
subscriptions if you have more than one.
Now I'm in PowerShell on my local machine,
and I've already connected to Azure.
As you can see, it's warning
me that it contains more
than one active subscription.
It's chosen one by default,
and if I want to change it, I
have to use this SetAZContext.
So, in order for me to do that, I'm
going to have to use a GetAZSubscription.
And that's going to list me all
of my existing subscriptions.
So I'll do that.
And it does come back
with three options for me.
So I want to use this set AZ context.
in the past, I've been able to, you
know, create a context variable and.
use the get subscription with the right
ID, we can actually just pass in the
ID of the one that we want to use.
So I can copy this ID for this,
Azure sponsorship subscription and
just pass it into set AZ context
dash subscription and pass in the ID
of the subscription and hit enter.
And from that point, I will be
working against this tenant.
And if I list resources, create
resources, modify things, it will
be with this context, pretty simple.


## 🏛️ Section: Configure name resolution



### 📺 Lesson: What is Microsoft Entra ID (used to be Azure Active Directory)?


Instructor: One of the first concepts
we're going to have to deal with in this course
is the concept of identity and identity management.
Now, Microsoft recently made a huge switch
in the branding of their identity products,
which used to be called Azure Active Directory
and has now been renamed to Entra ID.
So basically, you're going to find a mixture
in the internet in general,
perhaps even in this course where I mention Azure AD.
And what you should be thinking about
is it's now called Entra ID.
Even I'm still getting used to
thinking about this product as Entra,
because I've been calling it Azure AD
for seven plus years now.
So the concept of identity
within Azure and identity management
is sort of one of the central tenets of security.
Good security policy means having good identity management.
The identity is what you're going to hand out to your users,
their ID and password,
or maybe you're gonna create a multifactor authentication
so there's additional elements beyond password,
but basically you're gonna need a system
to manage the back end of people's identities
and to secure that.
And so in Microsoft Azure,
the native platform is called Entra.
Now, Entra is derivative
of one of the most successful identity management products
in the world of Microsoft Active Directory.
So Active Directory, not to be confused now with Entra,
is the on-premises identity management.
It is handling networks, objects,
users, groups on-premises.
There's no cloud involved in a Microsoft Active Directory.
And so what Microsoft did was they extended that concept
into the cloud with Azure Active Directory,
and now with Entra.
And so Entra is a cloud native version
of handling users, groups and identity in the cloud.
Now, there is a lot of similarities
between Microsoft Active Directory and now Entra.
Think of it as having a lot of overlap,
but they're not replaceable, interchangeable products.
You cannot just get rid of your company's on-premises AD
and turn everything into Entra accounts
without a lot of effort in terms of doing that,
making your whole business
into a hybrid environment, et cetera.
All right,
and they don't have overlapping features and functions.
There's some overlapping features and functions,
but there's some things that on-premises AD does
that cloud AD doesn't.
So for instance, there's some protocols
that work not over the internet,
so they're not compatible with HTTP or TCP.
That would be Kerberos or LDAP and things like that,
where those are not compatible features
over the broad internet.
And so that's why we had to use internet compatible methods.
And so that is where you get protocols like OAuth and SAML.
And so in this section and the videos that follow,
we're gonna get into talking about Entra,
how you are provided one
when you set up a brand new account,
what you can do with it
in terms of managing users and groups,
how applications, custom applications
that you develop can use Entra
to manage the identity of their users
and do authentication through that,
as well as third party products
such as Dropbox and OneDrive
that you can validate through Entra
to give people access to certain files and folders
in third party products.
So Entra is a huge topic and there's a lot of moving parts.
It's gonna be very difficult for me
to give you a full overview of Entra in a single video.
And so in this video
and the video that follows,
we're gonna be talking about all the different ways
that we can do identity and access management
in the cloud using Entra.


## 🏛️ Section: Secure access to virtual networks



### 📺 Lesson: Microsoft Entra ID (used to be Azure AD) - Free vs Premium


Instructor: Let's talk about
the different pricing options for Microsoft Entra.
Now, Microsoft Entra does have a free tier.
So, when you do create a brand new Microsoft Azure account,
you'll be given a tenant,
and that tenant is going to be free at first.
It is included with Microsoft Cloud subscriptions
such as Azure, Microsoft 365, and others.
And so, if we scroll down here to the bottom,
we can see the free edition included with a subscription
of a commercial online service
such as Azure, Dynamics 365, Intune, Power Platform,
and others in countries where it's available.
All right, so you can get a free tier
with Microsoft Entra,
and that's how you're going to basically start.
Now, what Microsoft does with their free tier
is they basically lets you create a lot of users and groups.
So, they are not limiting you
in terms of the number of users you can create,
things like that, it's not a very limited plan,
but what they do do is restrict you
when it comes to some of those advanced features.
And so, for instance, if you're running on the free tier,
then there is no SLA for Entra.
So, if you are relying on this as a production service,
then you don't have any contractual thing to fall back on.
Now, this makes sense because the SLA
is a financial agreement that Microsoft will refund you
part of your monthly fees
if they fail to meet certain service levels.
So, when it's free, of course there's no refund,
but there is no guarantee in terms of quality of service.
When it comes to some of these advanced features,
like if we look at logging and reporting,
there's gonna be advanced security reports
that are not included in the free tier.
When it comes to multi,
maybe the biggest one is multifactor authentication.
This used to be not included
and over the years, Microsoft has done this
so that administrators are included
and now it is included on the free tier.
But you'll see some of these features
like conditional access and continual access evaluation,
things like that are not part of the free tier.
So, I'm gonna scroll back up here.
So, the free tier is quite useful to a lot of people,
it just doesn't have an SLA
and then you don't get some of these AI
or other advanced features.
The next step, you have what's called a P1 subscription.
That is a $6 a month per user.
Now, you are going to assign
which users are part of your subscription.
So, for instance, you may have 1,000 users,
but maybe you only need 100 of them
to have some of these advanced features.
And so, you can select
which users get the P1 at $6
and which ones remain as free users.
And finally, P2 is the higher tier level of that
for $9 a month.
We'll talk about what are included
in P1 and P2 in a second.
Now, there is this additional
Microsoft ID Governance level
that wasn't necessarily available before,
but basically it's an advanced set
of identity governance capabilities.
You have to be an existing P1 or P2 user
and special pricing is available for P2.
We don't have to maybe pay the $7 a month
if you're already paying $9 a month.
So, let's scroll down here
and we got the free tier on the left
and we've got the P1 and P2 here.
We can see for most of the stuff, authentication,
federation, which is using external identity providers,
like your business partners,
you can do that any tier.
Single sign on, the authentication like SAML and OAUTH,
which are these internet valid things.
So, you can use your Entra account
for software as a service apps sign on.
Now, app level groups
is not available in the free tier.
The Microsoft Defender,
so the anti-virus anti-malware protection
not available for this tier
if you're not on P1 or P2.
I said the service level agreement.
RBAC is available for all three users and groups,
like I said, unlimited users and groups
are up to the service level limits
outlined in Microsoft's documentation for that.
But when you need something like dynamic groups,
so let's say you want to dynamically add users
to a group based on certain properties
or setting up expiration policies for group membership,
things like that,
well, that's not available in the free tier.
Using cloud sync.
So, synchronizing your on-premises active directory
with your in-cloud Entra ID
so users have the same user ID and password in the cloud
as they do on-premises, that's included in all three.
There are some monitoring for that called connect health,
which monitors the connection,
not included in the free tier.
Cross-tenant user synchronization,
it's an advanced feature, not included in the free tier.
Another thing that becomes a very useful,
it's what's called self-service password reset.
And this is allowing users in the cloud
to modify their passwords,
and then that goes back to the active directory on premises,
that's called a write-back.
So, let's say you do have this single sign on,
users are using their corporate ID
and password in the cloud,
and then they've forgotten their password,
they need to do a password reset.
That all happens in the cloud,
and that password gets written back on premises
so that when they change their password,
it gets updated in the what you would call
the root database.
Bunch of search and reporting,
self-service group management,
self-service entitlement management.
These are all advanced features,
you see this going up to the P2 level for that.
A lot of these advanced features like conditional access,
conditional access basically lets you have
different sign-in policies depending on certain conditions.
So, let's say this,
the user is clearly accessing your account
from inside your office,
you might have very relaxed sign-in policies.
If they are accessing their account from a country
that you do not have an office in,
maybe you have additional security policies
for those types of access,
you can do all that in continual.
Access, conditional access, not available for the free tier.
All right, going down.
Now, we get into these,
let's call them AI or these advanced threat managements
where you have conditional access that the computer
has determined this user's behavior has been pretty risky.
So, let's say the user
has tried to access a number of accounts with an IP address,
finally gets access to your account,
that might be blocked
because they've engaged in some risky behavior.
Well, that is an AI pattern recognition type thing,
that is a P2 level.
All of these device level filters, application filters,
like you don't want them signing on
to your Entra if they have certain,
if they're accessing it
from an out-of-date version of Android.
Like that could be a condition that you have,
has to be up-to-date version of the operating system,
things like that.
Risky accounts will be something where,
let's say the user has not signed in for three years.
Well, that could be a risky account
'cause if they do sign in,
we should basically prompt them
for some additional information
to prove who they are since it's been so long.
That would be an account that may have been hacked
if it hasn't been signed in for many years.
And to be able to investigate a risk,
that's a P2 feature as well.
Now, we can see here that all of these,
well, provisioning is specific to P1 and P2.
Access reviews, so that's a P2 feature.
That is basically every six months every year
users need to certify
that they still need access to certain resources.
So, you're putting the burden back on the user to say, "Yes,
I absolutely still need access to this directory,
or I need access to this account, or what have you,"
that's a P2 feature.
Now, we can see some of these new premium features,
machine learning access reviews,
and entitlement management with verified ID,
I'll show you that in a second.
Lifecycle, identity governance dashboard,
so Microsoft is providing more value
at the top end of identity management, obviously.
So, as you can see,
there are certain features you only get from P1 or P2.
And so, what you're gonna find
is if you're running on a free account,
then you might not be able to click
on a particular menu item,
it's gonna say, "You must upgrade in order to see this."
And you're gonna have to, there are free trials,
you can only use this once.
So, if you've done the free trial before,
you can't do a second free trial.
And so, you'll see those,
and don't worry too much about that,
will be covered in the videos.


## 🏛️ Section: Configure load balancing



### 📺 Lesson: Managing Multiple Directories


-: So in this video we're gonna be talking
about managing more than one tenant.
So we have these concepts of account, tenant,
and subscription, and they are three independent things.
The account or the user is either a person or a program.
So it is the email address and the password
that you use to log into the Azure portal
that makes you a user or an account.
Sometimes you have MFA enabled
and that's part of the authentication process as well.
Applications can also have a user concept,
and that's called a managed identity,
where they use identity managed by active directory
to do their work under the permissions
that have been granted to that identity.
It's probably bad practice for an application to
use a real person's credentials 'cause as soon
as you change the password, it breaks the application.
As soon as the person quits their job or is let go,
then the application's gonna stop working when
the account is disabled.
So make unique users for your applications,
called managed identity.
A completely separate concept is the tenant.
And so the tenant is the organization,
it's the business, it's the corporation.
Tenants have domain names usually,
either you have one assigned to you
or you can assign an existing one to Azure Active Directory.
You cannot assign the same domain name to
multiple active directory tenants.
And so if you're gonna choose example.com,
no other Azure ID account can have that as the domain name.
Basically Azure ID is managing the domain that
you provide it.
And so as we're saying,
you basically have to have a tenant in order to do anything,
in order to log into Azure, do any kind of work,
you do require a tenant.
Now the third concept is a subscription.
That is the billing arrangement.
You can have a free subscription, pay as you go,
enterprise agreement,
you work with a vendor like a CSP type of arrangement,
many different types of subscriptions, that is independent
to your tenant, independent to your user.
Now subscriptions can of course be assigned to tenants.
Not every tenant has one.
So I can create a tenant that doesn't have a subscription
and therefore can't create any resources inside of it,
or tenants can even have more than one subscription.
So anytime you create a resource
you are asked to choose the subscription.
That's because tenants can have more than one subscription.
And it's not restricted to having a single account.
So you can assign any number of accounts
to your tenant and they have different roles, everything
from being an owner, contributor, reader, and hundreds
of smaller subdivisions of those types of roles.
So that is the concept of subscription, tenant, and user.


## 🏛️ Section: Monitor and troubleshoot virtual networking



### 📺 Lesson: Heads Up: Changes to Entra ID Tenant Creation


Instructor: So this is a heads up
that the way that we create
Microsoft Entra ID tenets has changed
and it is gonna affect this course
and how you learn active directory
and identity as a service within Microsoft Azure.
So let's go into Microsoft Entra ID as an example.
I have a pay as you go account.
And in the past I've been teaching this course
and other courses, I've been able to create
what used to be called Azure active directory tenants.
Now it's called Microsoft Entra ID tenants.
I was able to create an unlimited number of them.
You can see here a dozen tenants
that I've created in the past, not including
the one that I use as my default directory,
but it was pretty easy to create them
and it didn't cost anything.
Now, if I go into the create
to create a new tenant under this account,
I do not have the ability to create a new tenant.
It's grayed out and I cannot select it.
The only tenant that I can create
is what's called a B2C tenant, business to consumer.
What this is, is using third party services,
such as LinkedIn or Microsoft to do the authentication
for your users for your apps.
So you could use social media accounts
for users to log into your apps using B2C tenant
to authenticate with the third party service
like Microsoft or LinkedIn or Google or others.
And then by that way, you would be able to authenticate them
and you let them give access to your app.
But Entra ID is the one that we focus on in this course,
and as of right now, I cannot create
any new Entra ID tenants.
Customers must own a paid license
to create Microsoft Entra tenant.
Now, I do have an account
that has a Microsoft 365 paid license.
So this is the account I use to pay for a Microsoft Office
and Excel and things like that.
Now, I don't have an Azure subscription on this account,
but interestingly enough, I can go into Entra ID.
I can say manage tenants.
This is the tenant associated with this account,
and I can say create.
And now you'll see Microsoft Entra ID is enabled
and the B2C option is disabled.
You must have a subscription in order to use a B2C.
Very, very interesting that there's these filters now
to create one or the other
based on whether you have a paid account
or you have a subscription or you have neither.
So in the following videos, I'm gonna show you
how I go through creating a Microsoft Entra ID tenant,
but realize that you might not be able to do it
based on how much money and how regularly you pay
Microsoft and for what services.
My understanding is you can have
a Microsoft 365 subscription.
You can have Enterprise plan
or some type of volume licensing, something like that.
Okay, so there are certain requirements
in order to be able to get Entra ID.
I have a 365 subscription on this account.
So in the following videos, I'm gonna go through
and create a new tenant.
The reason I would do this
is if you wanted to be the global administrator to a tenant
and then be able to create groups,
create users, create reviews,
go through all of the advanced P1 and P2 settings.
Whereas maybe you have an account
that is not a global administrator.
Maybe you are just a developer
or a user within your company's plan.
So if you're using your company's tenant,
then you might not be the right level
in order to get to use the advanced services.
This particular tenant is upgraded to the P2 status.
But you'll see here I am a global administrator.
So I have full access.
I do not need to create a new tenant
in order to go through this course.
But if you're not the global administrator,
then maybe you do need to create a tenant
to go through this course.
Problem now is that you probably can't.
So that's just a heads up
so that you don't go wondering why your interface
is different than mine
is because this is a Microsoft 365 account
and I can create a tenant through it.


## 🏛️ Section: Monitor resources by using Azure Monitor



### 📺 Lesson: Create Entra ID (used to be Azure AD)


Lecturer: So in this video, we're going to go through
the process of creating a brand new
Azure Active Directory tenant.
Now, as I said in the last video,
you don't have to create a new tenant
because chances are if you have created a user,
then you have a tenant at your disposal.
Now, you may not be the owner of the tenant.
So let's say your corporation has a tenant
and they've added you as a user.
And so you just have maybe very limited privileges
to that tenant until you're in the position
of being a global administrator.
And so we're gonna create a tenant so that
you can be the global administrator to your own tenant
as opposed to being just a user in someone else's tenant.
But like I said, if you have a free account
or a pay-as-you-go account and you've been assigned a tenant
by Microsoft and you are a global administrator,
then you don't really need to create a second tenant.
But I'm gonna go through that process anyways.
Now I'm on the home screen within the Azure portal.
And everyone's home screen's gonna look a little different.
I do have quite a few resources in my account already,
and these are sort of the most recent
services that I've visited.
And yours are gonna obviously be different.
So we're gonna have to find this
Azure Active Directory entryway.
Now I have it pinned to my menu.
Now let's talk a second about this menu.
There's a menu that in my case is pinned to the left
and I can just expand it and contract it.
Some other people might have a hamburger menu
in the top left and that becomes a flyout.
That is settled under the settings, this gear icon.
If we look at the appearance and startup,
we can see that my menu is docked,
but you might have a flyout menu,
and have different colors and themes and contrasts.
And when I log in, I'm taken to the dashboard.
You might be taken to your home screen, et cetera.
And I have a default directory.
So this gear icon under Appearance
is where you're going to find your settings.
So I'm gonna go into Azure Active Directory.
Now what you could do is go into all services
and start typing Active DIR and then you'll see this here.
I have it pinned to the menu,
and that's done through this star.
There's a little star, which is to set a favorite.
So however you get there, you find this pyramid
and you get into Azure Active Directory.
I'm gonna minimize the menu again
so we can maximize the space.
Now I'm gonna go through the management of a directory
in a later video, but what we're concerned with
is creating of a new directory.
So we're gonna go under this gear icon in here.
It's called manage tenants.
And we can see, like I said,
I've been creating tenants for a few years now.
You may only have the one single tenant.
It could be that you're a user of it.
It could be that you're an owner of it.
Anyways, we're going to go under create
and we're gonna create a new tenant.
For this choice, we're gonna choose
the Azure Active Directory default.
We'll talk about B2C later.
We'll go under configuration.
Now the tenant represents the organization in the cloud.
So technically what you want is your company
to have its own tenant, and in this case,
this is gonna be a test or dev tenant.
You can call it whatever you want.
Now, Microsoft is gonna assign this on microsoft.com domain
and so you're gonna have to come up
with a unique domain that no one else has used,
and we're gonna have to find if that's taken.
Someone's already using this.
Now the other thing, of course, is where the tenant,
the tenant, again, is a physical instance
that contains these resources.
You can choose somewhere else to contain the resources.
Now, depending on your country, your region,
you might have different laws around data protection.
If you're a European, you want your data to be stored
within a European data center, things like that.
So make sure that you choose the country
that's the most appropriate for your organization.
You can see here, even though I chose my country in Canada,
Canada doesn't have a active directory tenant data storage.
And so that'll be stored in the United States.
If I say create, now that's gonna create me a tenant.
Now it's obviously asking me to prove
that I am not a robot, which is fair enough.
It does take a few minutes to create a tenant.
Like I said, it's spinning up an instance
to contain these resources.
So we're gonna let that.
So it was very simple.
You just had to give it your organization name,
you had to give it a unique domain name,
and choose your region and then solve
the little CAPTCHA, and Bob's your uncle.
So next video, when this is created, we're going to
get into the management of our brand new tenant.


## 🏛️ Section: Implement backup and recovery



### 📺 Lesson: Switch Between Entra ID (used to be Azure AD) Tenants


Instructor: And I'm taken directly into my new tenant.
Now, like I said, does it really matter
that you are using your default tenant
which you are an administrator of,
or you're using this test tenant
that you're the administrator of?
The only thing that matters is that you have
administrative privilege to the tenant
that you are playing with to learn this course.
All right, so we're inside the tenant
and this overview screen obviously gives us
the lay of the land.
We only have the one user, which would be us.
There's no groups, applications,
or devices registered to this tenant.
And we can see some other information.
Now, this tenant ID is used in some scripts and things.
So, you will from time to time be asked
for a tenant ID when you are trying to do something
in PowerShell or CLI or something like that.
So, this is where you would go
in the overview screen to grab that.
You can see that I am on the free license of Azure AD,
and at some point we're gonna get into using features
of Azure AD that requires a premium license.
So, the free license does have some limitations.
I won't talk about them right this second,
but soon enough we'll talk about the reasons
to pay for Azure AD.
Now, Active Directory in Azure is basically, like I said,
it's an identity service
and the main purpose is to manage users.
If I go under the user's tab,
you can see that I am the only user.
My type is member, which means that I'm not
an external user, I am a proper user.
If I click on this, I can see that this,
there's no information on me, there's no name or title,
but I could have various informations on me.
The real thing that I'm interested at this point is my role.
I'm the only user of this.
I created it and my role is as of global administrator.
So, global administrator is the top level security role
within an Azure AD context.
That means I can create any user, any group.
I've got full and unlimited permissions,
and I can create users that also have permissions.
Okay, it's a built in role.
Now, later on in this course, we should be talking
about custom roles, and so being able to create
your own hybrid type of administrator that has access
to some things and not others, that would be a custom role.
This is a built-in role.
All of your Azure AD tenants must have
one global administrator.
You can have more than one,
but you can't have less than one.
So, it looks like our tenant was created successfully here.
The last thing that I'm gonna talk about in this video
is the concept of switching tenants.
So, right now I'm logged in as myself
and everything that I do is under this dev tenant.
Like we saw before, there's no subscription for this tenant,
and so I can't create resources.
I can go back into Azure Active Directory.
I can create users, groups and all of these things.
Now, what if I wanted to switch back to my original tenant?
Or in your case, you want to switch to the tenant,
from the tenant that you are the global administrator
back to your company's tenant,
where you may just be less of administrator or a user.
So, as you saw this gear icon says manage tenants
and I can choose one of these tenants
and just say switch, right?
That would certainly, again, reset my context here
and everything I'll be doing is from
my default directory in this case.
There's another way to do this.
If you go to your profile picture
which could be a, you know, a gray ghost,
in the top right there is a switch directory link,
and then you're given a list of favorites.
And so you can see the stars here
where I've set some as my favorite,
or you can go under all directories
and you can then switch tenants through that method as well.
So, it makes very straightforward
and simple to switch between tenants
if you've got, again, some users
and groups over here and some users over there,
your role being different in each, et cetera.
So, very straightforward to switch tenants.
So, going forward, like I said, you want to be in the tenant
that you're the administrator, so that you can go through
and do some of these things.
In the next video, we're going to jump
into the requirements of the exam again,
into managing roles, domains, and things like that.
So, come back for that.


## 🏛️ Section: AZ-104 Last Minute Study Review



### 📺 Lesson: Trial Upgrade to Premium P2


Instructor: Well, you'll remember, in a previous video,
I compared the differences between the free tier
of Azure Active Directory and the premium P2
as well as the Office 365 tiers.
So we're gonna find lots of limitations
when it comes to this active directory
if we're not on a premium plan.
For an example, I can assign roles to administrators
that are built-in roles,
but I cannot create what are called custom roles
because again, I'm not on the premium P1 or P2 tier.
So if this is your first time playing around with P1 or P2,
you can click this kind of link which says,
get a free trial.
There's many ways to get to here, but I'm in the roles
and administrators section of the Azure AD
and I can click this banner
and you would see the offers here
for a couple of different free trials.
And maybe you want to try this P2 tier.
And again, this is gonna get us access to custom roles,
it's gonna get us access to extra types
of multifactor authentication,
it's gonna get us access to some
of the artificial intelligence elements
of defeating hackers and things like that.
So we can click activate.
Now, in my case, I'm gonna click activate
and it's going to reject me
because I've done the free trial already
and it's not possible to do the free trial more than once.
So I'm gonna have have to pay
to get this account onto the P2 tier
to demonstrate the rest of the videos.
But the rest of you, majority of you, should be able
to just click the activate button
and move on to you get 30 days access
to the premium features of Azure AD.
So when you're ready to learn about that,
click the activate button, and get access to that.


## 🏛️ Section: Wrap Up



### 📺 Lesson: Purchase Upgrade to Entra ID (used to be Azure AD) P2 After Free Trial


Narrator: So since I'm unable to update
this tenant to AD Free, I've been forced to pay
for Azure Premium P2.
The way that I did that, was I went
into the Microsoft Admin Center
and there's a way of basically, purchasing products,
you can see, add more products, in this marketplace.
Go under all products and look under security.
And then you can see all the different options,
including the P1 option and the P2 option.
Now I've already gone through the process.
I purchased the P2 option, okay?
Now the challenge I have here is that the tenant
that I used to purchase it is not the same tenant
that we've been using to demonstrate this.
This is my business, Little Oliver Consulting Tenant.
So, what I've done here is I'm gonna have to switch
from the default directory to
my Little Oliver Consulting Tenant.
I added this user, my scottscourse@outlook.com user
to the tenant as a global administrator.
And so if I say, switch, fingers crossed,
as a user, don't have to re-log in under any new identity.
But I do have global administrator access
to an Azure AD premium P2 tenant.
And right now I'm paying for this access,
but it's worth it obviously,
in order to be able to demonstrate to you all
of the various things you can do
under premium subscription for Azure AD.
So just to keep in mind, I've switched to a new tenant.
Hopefully yours is much simpler than this,
but in case you are wondering, once your free trial is over,
how do you switch to premium P2?
Then you do have to go under buy.
You have to basically purchase a license
and then there's a way to do that.
And that link is at the top of the free trial here
under purchase services.


### 📺 Lesson: Add Custom Domains


-: So, you'll remember when we created this tenant,
that, we basically had to choose a tenant name,
and that tenant name goes as part
of the fully qualified domain name for the tenant.
And you might think, well what's the implication of this?
Like where does this domain come into play?
Well, yeah, there's going to be some internal code,
when you need to access your active directory
in a program in order to do authentication of users.
Nobody's gonna see the domain that's being connected to.
But what does happen is when you go to try to add a user
to your domain and you wanna say, Okay
let's start adding native users part of my organization.
So I want to add, you know, Joe Smith as being a user.
Well, the only domain we have available
to us is this custom, this default domain
my dev tenants sc 300.microsoft.com in my case.
And there are no other domains and I cannot specify one.
So like, if your you know, company is example.com
and your user is joeSmith@example.com, you can't set
this up without configuring active directory for the domain.
And so in this video, we're going to add your
company's domain as a custom domain to your tenant.
Go, we're gonna get out of the user space
and go back up here.
Now, right under manage we see a custom domain names option
and the default domain is here.
But let's say we wanna add our company domain.
In my case it's get cloud skills.com
Now I'm using a domain that I have control of
because then we're gonna have to validate that
we own the domain and we'll go through that process.
So you're gonna add your company's domain name
into this custom domain and say add.
But in order to prove that we own it, we do need
to add either a TXT domain record or an MX record.
TXT record is pretty straightforward.
Now, if you don't have control of this domain
let's say you are an employee of Get cloud skills.com
and you don't know where the domain registration happens,
then you're gonna have to work with whoever does have that.
So this record needs to be added to the domain registrar.
Now I use a company called Name Cheap.
And so I'm gonna have to go into my domain registrar
under Get cloud skills.
I can say manage under the DNS section and I'm gonna have to
add a TXT record to that section.
So it says here, TXT record host name is @ Sign this
and a ttl.
So go back to name Cheap and I'm gonna see add new record
TXT Host is that paste in that value?
They wanted 3,600, I'm gonna leave it as automatic
it doesn't really matter.
And so that's been added.
Now, there is a thing with domains that is
called propagation, where you update your
Registrar but that doesn't get pushed
into the global Name registry for between 12 and 24 hours.
And then, you know, takes a while
from there to propagate to other Cashes.
Now it's possible that Microsoft
doesn't have this domain cash anywhere
and it needs to end
up going directly to my domain registrar to get that.
So let's see, verify successfully verified even
though the status is unverified.
So I was able to, in those few minutes
verify this domain to go back here
and we can see get cloud skills.com is now verified.
Now the one thing you might wanted to
at this point is to set your new custom domain as a primary.
So, if you click on it and you can say Make Primary
and then the old on microsoft.com domain goes away.
And anytime you refer to this
you can refer to it using your custom domain name.
I'm not gonna do that right now
but if you wanted to make it primary
if you didn't like this setup, you wanted to go away
you can certainly make this your primary domain
and it would be what's shown everywhere
including the overview page.
So that means I can go back to users
and go to add a user and I can add
in Joe Smith and choose the Get cloud skills domain
and start to fill in some information.
So, in this way, we haven't gotten
into talking about adding users, but we can see
that we can customize the domain name through this.
And now we've got a Azure active directory
that will allow us to work
with this domain name because we verified ourselves.
So that's how you add a custom domain.


### 📺 Lesson: Note on the recent Exam Changes


[No transcript available for this lecture]


### 📺 Lesson: Manage Azure AD / Microsoft Entra ID Users


Instructor: Okay, so let's say
that we just getting started.
We've created a brand new tenant for ourselves
that we are the global administrator of.
Or if we just created a brand new Azure account
we were given a tenant that we are
the global administrator of, either or.
And so we are looking at the screen, you know,
you might have again have this Azure free tier
and I'm working within the AD premium P2
so I can demonstrate everything to you.
Now the underlying concept,
so Azure Active Directory is an identity management service.
And so the identities that it's managing
are both users and applications
'cause applications can have identities as well
for security purposes.
But in the case of users, we're talking about individuals
who have been granted access
to some resources within the Azure Cloud platform.
Now when I created this, it imported a couple of users
from my existing tenant and I just recently added myself
this Scott's course account to manage this tenant.
We can see here at the top right
I'm logged in as this user.
And so even though I'm not natively part of that tenant
I've been added as an external guest
to be a manager of this tenant.
So you can create multiple users, you can either
just go into new user and create the user.
You can invite external identities
to be part of your tenant and as I said previously
you can synchronize with active directory on premises,
Windows active directory and import a subset
of your users from your company into Azure AD.
So what we're gonna do with the purpose of demonstration
is we're gonna create a user.
So I'm going under, under the user's tab
I'm going new user, create a user.
Alright, so I'm just gonna pick to create a user template.
Now in this particular case, I'm working within a domain
that I already own
and has already been set up as a custom domain.
You might have an Azure assigned domain
the something.onmicrosoft.com.
So every tenant has this on microsoft.com domain by default.
And we will get into talking about custom domains
and then you'll be able to use your own domain, okay?
So let's just create it using the default domain,
this on microsoft.com.
Users have to have a unique name.
So this is testuser1
and you can see there's an @ symbol between it.
So the username when they log in is gonna be
testuser1@certpracticenet.onmicrosoft.com.
This is my tenants domain.
You're gonna have your own domain.
And then I can call this test user, test user.
Now that's all that's required
in order to create a user.
I don't have to assign the password.
I can auto-generate the password.
And I don't have to assign a role
or fill out any of the other details.
This is all optional.
So I'm gonna say create.
So it's gonna go off, it's successfully created
and I can refresh.
It might take a few seconds
for the Azure portal to get the news.
And there we are.
Test user is now a member of this tenant.
Now the free tier might just be sufficient for your needs
because this free tier supports up to 500,000 objects
and that includes users, groups and contacts,
but plenty of room for users and groups
within the free tier.
Now this user, again, it's a user role
it has zero permissions.
All it can do is it can log into Azure and that's it.
It has no permissions to see anything, do anything,
affect anything is basically it's just acknowledgement
that is existing as a user and that's it.
So we've just created a user.
Now, if we wanted to
we could do various things to this user.
We'll go onto the properties section and we can see
that we have the ability to see all of its settings
where it belongs and things like that.
If I go into edit properties, I can go back
and change the name, change the display name for this
add various credentials and things like that.
And finally, if this user forgets their password,
or in fact we had it auto generate the password
and we would then need to reset the password
in order for them to be able to log into this at all.
So here is basically how you add and edit a user.
Now, at some point you might find this gets filled
with test accounts
and you're trying testuser1 testuser2.
When you're done, you can easily select the user
and just say delete and clean up your mess afterwards.
So deleting a user is pretty straightforward as well.
So now we've shown how we can create users.


### 📺 Lesson: Manage Azure AD / Microsoft Entra ID Groups


Lecturer: All right, so the purpose of this next lesson,
I'm gonna create some new users.
I'm gonna create three students,
and I'm gonna create three teachers
called Student 1, Student 2, Student 3,
and Teacher 1, Teacher 2, and Teacher 3.
All right, so I have now,
I have three students and three teachers.
Now, when you get lots and lots of users,
hundreds of users or thousands of users
operating on them becomes tricky.
You know, it gets confusing.
It's hard to manage.
And so Azure AD provides a couple of different ways
to operate on users in bulk.
One of the ways that is offered is what's called a group.
So in Azure AD a group is a collection of users
who have been given specific access permissions
to resources in the Azure cloud platform.
So in my example that I'm just going through,
I created three students and three teachers,
what I can do is I can create a student group.
It's a security group.
So I'm gonna call this the Student Group.
And I have to select members for it,
so I'm gonna go into under no members selected
and I'm gonna say student.
And I have Student 1, Student 2, Student 3,
and I can select them as so.
So now I have one security group
that contains all of the students.
And I'm gonna create similarly a teacher group,
and I'm going to select Teacher 1, 2, and 3,
and see Create.
So by default, assigning people to a group
doesn't actually grant them any new permissions.
It's just an organization structure.
You saw when I created the group
that there is an option to allow me
to assign roles to the group,
and in this way I could then use the group
as a way of assigning permissions,
but without that being selected,
the group is just an organization structure, okay?
So now I have my groups.
Now there's another type of group
that's called a dynamic group.
We can see here that Microsoft
is having some trouble as I'm writing this
in terms of their dynamic group membership.
But if I create a group,
and instead of choosing the assigned type,
so let's say I create a group called First In The Class,
and instead of creating a group
that has an assigned membership,
I can create a group that's dynamic based on a query.
So this is the type of group you could do based on,
for instance, people that are in the same department.
And so if somebody is new is added to the department,
they can be automatically added
to a related group using this query.
So I'm gonna say add dynamic query.
And let's say I'm gonna choose the display name
as being the property I want to operate on
and I'm gonna say contains as the operator and say 1.
All right?
So if the user display name contains the number 1,
that should make them part of this First In The Class group.
And in the context of what I've already created,
Teacher 1 and Student 1 will fulfill this.
Now this is rather useless
in terms of creating a group based on display name,
but you could have groups for disabled users.
You could have groups for departments or countries.
You could have group based on job title.
You could see all of the various properties
that are available.
If those properties have values in your system,
then you can create dynamic membership groups
that automatically add and remove people
based on dynamic rules.
But as we can see from the banner
Microsoft is currently having trouble with that feature,
and so I'm not gonna be able to demonstrate that
other than we have this First In The Class group
that should have two members
when this feature is working again.
Now we can see a context here on the left
of what you can do with groups.
Now I already disabled
or I didn't enable the authentication aspect,
but I can enable Privileged Identity Management rules
on these, and we'll talk about that later in this course.
We can do access reviews on a particular group.
So let's say we want to review
the permissions that students have.
Well, we can assign an access review process
to the student group,
and so all members of the student group
would be up for review.
We can see audit logs.
We can do bulk operations on these groups.
So groups are just a way of organizing users
based on either a fixed assignment or on dynamic assignment.


### 📺 Lesson: Manage Azure AD / Microsoft Entra ID Licenses


Presenter: So in this video, we're gonna readdress
the concept of a license within Azure AD.
Now, in a previous video, we did compare the free version,
the Office 365 license P1 and P2 licenses
to see what features are in each,
and as a result, I have upgraded
to the P2 tier on my own Azure AD tenant.
So what I'm gonna do, I'm gonna review the license,
and I do have to actually assign licenses to my users.
So if I go into the AD on the left, I go under licenses,
and I'm gonna go on the left under all products.
So we can see on this screen that I have two licenses
that I paid for.
I have my Microsoft 365 apps, which is, you know,
Office, and Outlook, and PowerPoint, and things like that,
and now I have this Azure Active Directory Premium P2.
Now, I only purchased one license for that.
Again, it's a monthly charge or a yearly charge per user.
Now, you may have noticed that we have gone
into the user's tab and we've created, right?
Three teachers, three students.
I've got my original user.
I have myself in my course teaching.
So there are, you know, six or seven or nine users
at this point, but I only purchased one license.
That's because you don't have to assign a license
to a user that doesn't need it.
If we go under license features, we can see all
of the features of Azure AD, and we can see that
some of these things are available for only the free license
and some of them are unlimited if you paid for it.
So I have paid for one license,
so the feature is available for me,
but if I have users that need any of these features,
then I should pay for and assign a license for them.
So let's look at an example here, okay?
So self-service password reset is one of the features
that's available for this purchase,
and we'll talk about this actually in the following video,
but in order for users to be able to manage
their own passwords, you have to pay for that.
Otherwise, they have to call your help desk or call you
and say, "I need my password changed,"
and you would do it through a password reset
on the user profile screen.
But to have that functionality enabled,
this is going to be a paid feature.
So I would have to again, basically assign a license
to the users that I want to have this type of feature.
Now, multifactor authentication
for administrative roles is included in the free tier.
We saw that, but multifactor authentication
for phone and SMS is a paid feature.
The multifactor authentication that's free is
for the Microsoft Authenticator app, I believe.
So all of these conditional access, identity protection,
privilege identity management,
if the users require these features,
they need to have a license,
so I'll show you how to do that.
We're gonna go back to the top here,
and we're gonna go under users,
and for now, I'm going to assign my premium license
to my guest account that I'm using here,
which is a global administrator on this account.
So I go under this account,
and I go under licenses,
and you'll see that this account does not have any licenses,
so I say assignments.
So now I'm shown the two licenses that I'm paying for
on this tenant, the Microsoft 365 license
and Azure Active Directory.
I want to assign the Azure ADP2 license to this one user,
so I'll select it.
I do get options here for,
I can unselect it, which I won't do.
Now, I already know when I say save
that this is going to give me an error,
but I'm gonna do it anyways.
It says license assignment failed.
I'm gonna click the failure notice,
and I'm gonna see it says,
"License cannot be assigned to a user
without usage location specified."
Now, the reason this error occurs is because certain regions
of the world have certain restrictions on software
that Microsoft can provide.
As you might understand,
there are legal restrictions in certain countries,
and so this user is going to have to have
a location specified, so I'm gonna go back into the users,
I'm going to select myself,
I'm gonna say edit properties,
and if I scroll a bit, I'm going to see
a dropdown called Usage Location.
So I'm gonna pick that this user, which is me,
is located in Portugal, and I'm going to say save.
So now I've successfully updated the user.
If I go back to licenses,
back to assignments, Azure P2, say save,
then I get the message license assignment succeeded,
so that's a pretty straightforward error.
So now I have a user that is eligible to use
some of these services such as access reviews,
privileged identity management,
and some of those advanced Azure features
in terms of security and things like that,
again, this is on a per account basis.
But the good news then is that you can entirely have tons
and tons of free accounts that don't need these features,
and you can only pay if you choose
for the users that really require them,
and that allows you to save money
by only paying for what you're gonna use.
So that's how you manage licenses within Azure AD.


### 📺 Lesson: Administrative Units


Instructor: So we really haven't talked about
the concept of roles yet
and role-based access control.
There's a whole separate section following this section
talking about roles and permissions.
But in this video we're gonna move on to talk about
what's called administrative units.
Now this is an interesting concept.
What I'm gonna do before we continue is I'm going to
assign a role to the teachers that gives them some kind
of permissions within our Azure active directory.
So I'm gonna look at the help desk role.
Azure is pretty slow today.
So there's a help desk role
and I'm going to assign the three teachers,
1, 2 and 3 into the help desk role.
Now, all you need to know right now
is that this gives them certain permissions
to be able to let's say, reset the password of the students.
Okay? Now, the way that I've set this up right now
is each teacher can be a help desk user
for all of the other users in AD.
There's no differentiation
between which teacher can help which students right now.
So it's almost like a role for your whole company
is that these people all have equal access
to all users within your Azure AD, okay?
Now, the concept of an administrative unit
is a way of segregating these permissions
into some type of logical separation.
So you can delegate administrative permissions
and control over specific areas of the directory
to specific administrators.
In practicality, what this allows you to do is
have certain administrative users, in this case
the help desk users, to only be able to affect certain part
of your organization, not the entire organization.
So this is really a segregation of administrators
into pairs where they do their work.
Now this makes logical sense
if you have your whole company,
let's say you've got 10,000 users
in this Azure active directory
but they're broken into different departments.
And so you have your customer service department,
you have your marketing department,
you have your sales team on the front lines,
and you may have different help desk users
helping each of them.
They're on the floor with them,
they work side by side together with them
but you don't necessarily want your help,
your customer service help desk to be touching
the sales team's accounts.
So this is a way of segregating it.
So let's create an administrative unit.
I'm gonna call this the...
Let's call this classroom 1
'cause we're dealing with students and teachers.
So this is the classroom 1 administrative unit
and which roles are we going to grant access
to AD for this?
So let's see this password administrator role
and we're gonna say teacher 1.
So we've got classroom 1
and we've got teacher 1 who's a password administrator.
Now, classroom 1 exists
and teacher is the password administrator for classroom 1
but classroom 1 doesn't have any members.
So I'm gonna put student 1 in classroom 1.
And so now teacher 1 can change the password
for student 1.
You see what I mean?
So this administrative unit allows you
to segregate which administrative users can work
with which parts of your organization.
And of course it doesn't have to be only users
that you're dealing with.
Maybe your teacher can work with groups.
We talked about groups earlier, and so maybe
teacher 1 is the administrator for the student group
but they can't touch any other teacher account.
So hopefully you can see that administrative units
allows you to segregate your active directory such that
certain administrators only have permissions
to work on certain areas.


### 📺 Lesson: Manage Devices


Host: So the next concept within Azure AD
that we'll talk about is the concept of a device.
Now, this might seem strange,
we're talking about users in groups and roles,
but what's a device?
Well, devices represent and manage the physical devices
used by users that access organization's resources.
So if you're logging into your applications
from your work computer inside the office,
well that would be represented in here as a device.
If you're working from home
or working from your phone or from another device,
as long as you're authenticating through Azure
that will be listed as a device.
Now, in my example here
I don't have any devices that are managed.
They're all unmanaged devices.
So what does it mean that a device is managed?
Well, a managed device
you could have certain minimum standards
in terms of encryption, password requirements,
that you have to have an antivirus running
or malware protection.
You can set certain organizational standards
and say that only devices that meet these standards
can access this application.
The devices are also used
in some of the other security features,
such as conditional access.
So we haven't talked about conditional access yet,
but conditional access allows you to restrict access
to your applications based on a number of factors.
It could be the geographical location of the user,
it could be that they're using a pre-approved device.
So let's say the person is logging into your network
using their company laptop
and you know that it's their company laptop
and it follows all of the minimum standards
for a versioning, security, encryption, all those things.
Well then you can not require multifactor authentication
if that person is using that registered device.
But if they're using their home laptop
and it doesn't meet those standards, then you can ensure
that you can enable multifactor authentication.
So conditional access allows you to have certain rules
based on certain features
and so the devices that people use
can be sets of those features.
So here's an example of, again,
these are the devices that are associated with this tenant
and they're all, happen to be Windows devices
and we can see various information about the OS,
the name of the device,
what OS version that they're running,
which user is using the device, when it was registered,
and when the last activity was observed.
Right now, these are all unmanaged devices.
If I wanted to,
I could select my computer,
and well, for instance, in this particular case,
I can disable the device altogether.
Now we can see a limited set of settings here,
the main one under the device settings.
So right off the bat, we can basically allow users
or deny them the ability to even join their devices.
We can require multifactor authentication
in order for the device to be registered or joined
and maximum number of devices per user here.
Okay, we can even manage BitLocker keys within Azure AD.
So it's a pretty simple setting,
just a tracking of the devices people are using
to access your applications
and then being able to restrict access, block access,
or even require multifactor authentication
using the conditional access feature
which we haven't talked about,
based on whether they're using a recognized device or not.


### 📺 Lesson: Bulk Operations


Instructor: Now, given that Azure Active Directory
can handle hundreds of thousands of users and groups,
and devices and all the things like this,
we're definitely dealing with a lot of data.
And so Microsoft has added
what are called bulk operations features
to a lot of their screens.
So for instance, it would be tedious
if you had to create 2,500 student accounts.
But what you can do is use the bulk create feature
to upload a CSV file containing the students.
Now, there is a CSV template,
so if I download it I can see this template.
Now, I can open it up in Excel
and I can see that there is display name, username,
password, stuff like that.
So I'm gonna fill out some samples here,
so just give me a second.
All right, so I have created 10 additional students
in this CSV format.
Filled out some basic information,
even gave the usage location.
And I'm gonna have to save this again as a CSV file.
Now I'll be able to pick that CSV
and create those 10 users.
I'll say Submit.
Click here to view the status.
So the completed with no errors,
10 records have been inserted.
So if I go back to All users
then I will see that I have 10 new students
part of this class.
So that is the bulk operations.
We will also similarly be able to do operations
any time you are likely to need
to work with lots and lots of records,
like assigning members to groups.
Then we're gonna have a very similar situation
where there's a CSV template and then we can upload that
and we can bulk assign members to groups.


### 📺 Lesson: External Users


Instructor: So we saw when we were creating users
that we had in this particular case,
two choices of domain names
when we were choosing the username.
So in my particular case, it's either my custom domain
which is certpractice.net,
or the Azure assigned domain
which is certpractice.commicrosoft.com.
But what happens if you want to assign access
to someone from outside your domain?
This could be a business partner,
this could be a external user,
like somebody that works from home as a contractor
who does not have a email address
within your domain, because the email is important.
This is how they're going to reset their own password.
This is how you're going to basically invite them
to be part of applications and things like that.
So the concept of inviting external users
is called a guest user.
So we can see that that's called not create user,
but invite user.
Invite a new guest user to collaborate
with your organization.
The user will be emailed an invitation
that they can accept in order to begin collaboration.
So a guest user is an external user
who's granted access to your organization's resources.
Typically, these are partners, vendors, and contractors
who you need to collaborate with.
To give access to maybe
only specific resources in your organization.
You don't wanna add them to your Azure, I'm sorry,
your non Azure active directory.
You do not want them to have an account on your AD,
but you still do need to work with them
in your applications and to give access to resources.
So these are called guest users,
and like I said, they'll be given an invitation
and they have to accept the invitation
in order for this to work.
And you can assign them permissions.
Just like you assign permissions to your own users.
They have to, if for instance, they're caught
by multifactor authentication,
they would still have to go through MFE
or conditional access.
So they follow the same security standards
as your own users.
They're just not part of your domain.
So for, let's give an example here,
let's say I want to invite myself,
but not my cert practice email.
I wanna invite my Hotmail account.
So I'm gonna make up, this is my made up Hotmail,
and it's gonna be .hotmail.com.
So don't email me there.
That's not a real address, but in this way,
this person will get invited, get an email
and they'll get invited to join this domain
and then I can cert assign them permissions.
Now, you also get the chance to,
let's say they don't want just an invitation to pop up,
you wanna say,
"Hey Scott, this is for that special project
"we will start working on next week."
All right?
So you can assign a certain message for them to accept this.
Again, you can go ahead and say
this is not just a ordinary user.
This, it could be, typically you're not
gonna give them administrator permissions,
but it could be let's say in this case
application developer would be a perfect example here.
So I already know that I want this made up Hotmail account
to be part of the application developer.
And maybe I already know that these are,
this is on the teachers side.
That's their role
and I can allow them to sign in.
I can set their users location.
This is again, critical for licensing and et cetera,
and say invite.
And once I do that, it's going to fire off an email
to this address with these things.
And then these people
can choose to join your organization.


### 📺 Lesson: Self Service Password Reset


Instructor: So I've previously mentioned in this course,
that for the Azure free tier users,
if they were to have problems
with their user ID and password,
they would need to contact someone in your organization,
an administrative user, to be able to reset their password.
And so, you would have to come in here
and say reset password,
and then they'd be able to make progress.
For administrative users,
Microsoft already enforces
this multifactor authentication for one,
and that means that self-service password reset
would be available for administrative users already.
So, what is self-service password reset?
Well, if we go into our active directory tenant
and we go under manage and we go under password reset,
we'll see a fairly simple screen that allows us to choose
whether we allow users to reset their own passwords.
By default, it's set to none,
so users are not allowed to set their own passwords.
You can select specific groups.
Now, this is a use of groups here.
We can say that teachers
are allowed to reset their own password,
or we can enable it for everyone.
And once again,
you're gonna need licenses for people
who fall into this group.
I'm gonna cancel out that.
Now, when you read this blue text here that says,
"This applies only to end users.
"Admins are always enabled for self-service password reset
"and are already required to use
"two factor authentication to reset their password."
So in actual fact, I only have one license.
I've assigned it to an admin user,
and so this doesn't really apply.
But let's say I could set that to all,
if I ever do get more licenses,
those users could reset their password.
So how this works is when a user is prompted,
let's say you're using Azure Active Directory
as the login front end to your application,
and they're presented
with the Azure Active Directory login screen
and they can't remember their password,
then they should be able to say, "Forgot password."
It's a quite common feature from login screens.
And then, they'll be taken through a process
of verifying their identity
and then being able to modify their password.
Now I did mention before that sometimes
the users are synchronized
with your on-premises active directory
through a process called AD Connect.
And so you have an option,
and we'll talk about AD Connect, I think, later on,
but you have an option when setting up Ad Connect
to do the password pushback.
So when they do update their password,
if they are a on-premises user,
having those passwords passed back through
to the main AD is an option,
if you do set up AD Cloud Sync or AD Synchronization.
Anyways, so self-service password reset
allows users to reset their passwords
without requiring the help of a user.
And if the user,
you could even have a password policy,
where the password expires
after nine months or six months,
and then they can go through and reset their password
without having to contact phone support.
And they must go through multifactor authentication
in order to reset their password.

