---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "10"
title: "Module 10: Administer Monitoring and Log Analytics"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 10: Administer Monitoring and Log Analytics

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** Azure Monitor Architecture, Diagnostic Settings, VM Insights, Log Analytics Workspace, Kusto Query Language (KQL) Queries, Metric Alerts, Traffic Management Lab  
**Line Range:** Lines 17390 – 18183 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


### 📺 Lesson: Overview of Azure Monitor


Instructor: So the last major objective of the exam
is to monitor and maintain Azure resources.
It's worth 10 to 15% of the overall score.
That major objective is broken into two sub-objectives,
monitor resources in Azure
and implement backup and recovery.
In this section of the course,
we're gonna be talking about monitoring of resources.
This includes metrics, loggings, analyzing
and querying logs, alert rules, network watcher,
and configuring and interpreting monitoring
of these various Azure services.
So I flip over to the Azure portal,
and if I'm on the homepage here,
I can see that there is a tool called Monitor.
You're gonna find it, I have it favorited
and it's in my menu on the left here.
Or you can go under all services
and if you type monitor,
you can see Azure Monitor as a service.
Okay.
Now, Azure Monitor is a centralized dashboard
that contains all of the diagnostics, logging, metrics
for all of these associated services.
It can even work with external servers if you're running
in different locations on premises or in different clouds
if you have the right agent running.
And we'll deal with that.
We're talking about virtual machines.
I'm gonna start off going down here under the insights
and we can see a list of all the services
that Azure Monitor can support.
The first one is applications, web apps, app services.
Now the app services use a tool called App Insights
or Application Insights in order to extract the metrics
and the diagnostics from apps services
and put it into a workspace where Azure Monitor can access.
Virtual machines can also be monitored
from within Azure Monitor,
virtual machines like Windows or Linux.
Virtual machines often require an agent to be installed,
a piece of software installed on the virtual machine
that will then extract the performance and health data
and send it back to Azure Monitor via a log workspace.
So when you have a virtual machine,
you are going to basically install a piece of software.
Now what we can do is, like I said, if we had Azure VMs,
we can basically turn them
from being not monitored to monitored.
I don't have any configured right now.
but we'll do with that.
It also supports logging and diagnostics
for storage accounts, and you can actually see transactions
against your storage accounts, the end-to-end latency,
the server latency relating to certain storage accounts,
determining which storage accounts
are running close to capacity, et cetera.
So you get some information out
of your storage account here.
It works with Kubernetes containers.
So you can install, again, like an agent
to extract data from a Kubernetes cluster
and get the CPU in memory,
and that's the stuff that comes with AKS.
But you get more comprehensive data
by enabling monitoring services to extract the data.
Now, there used to be separate tools
for monitoring networks,
and now that's integrated into Azure Monitor.
So if you want check about traffic over a virtual network
or whether one potential network can talk to another,
let's say you have two networks that are appeared
and you want to test that,
you can see that there is actually diagnostic toolkit
and you can troubleshoot and do various things
starting from here.
We can also see a map of our VNets within our account.
Since I don't have any VMs, I don't have any VNets,
and so the topology isn't gonna do as much,
but if you want to see a visual diagram of your servers
and networks and connections,
you can see that under topology.
Seems like the SQL database monitor tool has been in preview
for many, many years.
So authentication issue is interesting.
So you can obviously use a monitor
to access Azure SQL database data
and get that into Azure Monitor.
So it supports Cosmos DB, Key Vaults, Azure Cash for Redis,
Stack HCI, Service Bus is now in preview and a few others.
So that is just getting performance
and health data out of these related services.
Azure Monitor also deals
with what are called diagnostic logs.
So if you go under settings and diagnostic settings,
we can see a bunch of the services in our account,
and then we can say that most of them
don't have diagnostics enabled.
All right, if I have this particular storage account,
blob containers got diagnostics enabled,
but I don't have it on the storage account as a whole
or any of the other like queues or tables
or files or things like that.
Now you can go if you are in a particular service,
let's flip over to a storage service,
so I go to say storage,
if I go under the storage account,
you'll see in any service really,
going down under monitoring,
we can see diagnostic settings has its own tab.
Now, like I said, I do have diagnostics enabled
for the blob here, but I don't have it enabled
at the account level.
And so I can click on that and say add diagnostic setting.
And this is simply to get the transaction logs
from this storage account.
I can say send to Log Analytics, give this a name,
and this is now gonna start collecting
log data from this storage account
and send it into the log analytics where Azure Monitor
can then report on it.
So we're gonna talk about, in this section of the course,
we're gonna talk about logs
and we're gonna talk about running queries
and things like that.
So we'll get into some of these other interesting elements
of Azure Monitor in the next video
and the videos that follow.


### 📺 Lesson: Enabling Diagnostics for Resources


Instructor: I've created a couple of more resources
to play with here.
I've created a virtual machine
and I created another web app.
Now I'm in the Azure Monitor
and under settings, diagnostic settings,
and I filtered it to a specific resource group
to make it clearer.
And we can see the types of resources
that we can enable diagnostics on.
So we can enable diagnostics on a network interface card.
We can enable it on the public IP address
of a virtual machine,
and as well as the network security group.
Now, what we're missing from this list
is the virtual machine itself and the web app itself, okay?
So these are just the ancillary objects
that get created alongside of the primary resources.
So let's look at an example.
If I wanted to track the traffic coming in and out
of a virtual machine, I can track that
through the network interface.
Network interface is not gonna know anything
about the CPU utilization or the memory utilization
of the VM it's attached to,
but it is going to know about traffic.
So I can say Add Diagnostics,
and I just want to grab all of the metrics for this,
and I'm gonna call this a diag2,
and I'm gonna send it to a log analytics workspace.
Now notice I can also additionally send it
to a storage account, send it through the event hub
to be processed by some listener
or some other third party solution.
So I have up to four destinations
for the metrics coming from this network interface card.
So I'm gonna choose that and click Save.
But I'm also interested in the performance
of the actual virtual machine.
So I'm gonna go back to the resource group.
I'm gonna find the virtual machine, which is here.
So we go under monitoring.
Now we can have application insights on a VM
just like we have on Azure App Services.
So that is an option
that will track application level events.
So if you have software running in your VM,
then you're going to be able to get that data outta the VM
using app Insights.
We also have diagnostic settings.
Now, Azure Monitor already collects basic metrics like CPU,
disk in network without any additional software.
This is just a native function of Azure VMs.
But if you want more insights into the VM,
you need to enable what is called guest level metrics
and using an agent.
So this is a piece of software installed on the VM
that collects this.
So it has to have a storage account to access this.
And so I did create a storage account
specifically for this purpose.
And I'm gonna say enable guest level monitoring.
Now, that's obviously going to be take a little while,
because it's gonna have to install the software,
and then it's gonna to have to restart the VM.
It's a disruptive event,
so we're just gonna let that install and restart.
Alright, so we do have
the Azure Diagnostics installed on this VM at this point.
Now we still have this option of installing insights
to get that out of the virtual machine as well,
which can be enabled here.
Now let's flip over to the app service that I created.
So go into the resource group
and I created an app service.
And if we go down under monitoring and diagnostics settings,
we can see that we can collect certain types of diagnostics
from the app service.
This is HTTP logs,
app service console logs, application logs.
So if your app puts out stuff to the console
or pops out stuff to the app log
within Windows event viewer, you can get that access.
So who's logging in securely or failing
and things like that.
So let's add diagnostics for our app service.
Now in these types of situations,
we can pick which ones we want and which ones we don't want.
So let's say we don't care about the access or audit stuff,
but we do care about the HTTP logs
and the console logs, et cetera.
Again, we can send that to Log Analytics Workspace
and say Save.
And so, we can see there's a few different ways
that we can enable diagnostics.
One from within Monitor and also for additional services
within the services themselves under diagnostic settings.
For applications, you often have the choice
between application insights
as well as lower level HTTP logs
and CPU and metrics and things like that.


### 📺 Lesson: Azure Monitor and VM Insights


Narrator: So we saw in the last video
that for virtual machines, we can turn on diagnostics
in order to get the various operating system level metrics
outside of the virtual machine.
The other thing we might be interested in is the logs,
and the logs are accumulated through
what is called Insights.
Actually, Microsoft is migrating from a Log Analytic agent
into a VM Insights agent.
So if I go into VM Insights
and I say Configure Insights,
I'm gonna see that I have a virtual machine
and Insights is not enabled.
Now, I can quickly click this button to enable Insights.
We can also, if you remember from the last video,
go into the VM under monitoring,
we could go down to Logs even,
or to Insights and say Enable.
So this is directly feeding data
from the virtual machine to an Azure Monitor agent.
Now, the agent needs to be installed on the VM.
So this is a little disruptive in terms of installing
piece of software on the VM in order to collect Insights.
Now you'll see that it says for Azure virtual machines,
the CPU disk and up and down state does come out of the box.
You don't need this for that very, very basic data,
but if you want additional monitoring capabilities,
that's when you need to install this agent.
So I think that the agent is actually installed,
my notification told me the deployment succeeded.
So let's flip back to Azure Monitor
under VM Insights to say Configure Insights.
And now we'll see that the VM has gone
from being not monitored to being monitored.
I will point out that these agents sometimes need updates.
And so you might see a button on this screen
if the agent is particularly out of date
and wants you to manually trigger agent to be updated.
So that could appear here.
So now, besides collecting the metrics data,
we are also collecting Log data from that server.
Log data often would appear in Windows, at least,
in a Windows event interface,
like if you're familiar
with the Windows event viewer at all.
Then you can see that there are Windows logs,
Application Logs and, you know, Security Logs,
and System Logs and things like that.
And so you're basically using an agent
to extract these logs from the VM itself
into the monitor that we can then run queries on.
So that's gonna take time to reproduce data.
We're gonna talk about Kusto queries in a moment,
but that's all you need to do in order to extract
some of these application and system event logs
out of Windows, at least,
and into Azure Monitor for centralized monitoring.


### 📺 Lesson: Running Basic Kusto Queries on Logs


Instructor: All right, so we do have a couple of things
that are collecting diagnostics,
the virtual machine and app service,
the network interface card.
So, first thing we're gonna look at
is this concept of metrics.
So, metrics really is the easiest thing to explain
because it's the CPU, the data in, data out,
number of requests, things like that.
When I go into Metrics, I do have to choose a resource.
So, it starts with choosing the subscription
and then going down, we can choose the resource type.
So, I want to choose the App Service, let's say.
And then, to choose the actual resource,
so I'll choose this web app.
And you can see I've got one selected scope
and I can say Apply.
And now, we can see what we're talking about
when it comes to metrics.
So, metrics really is centered around a graph
and we can choose, when we do the Metric dropdown,
we can see that there's a couple of dozen options.
Everything from memory working set, number of connections,
CPU time, data in, data out, even the garbage collections,
various error states from 400 errors, 200 success,
which is not 200 success,
but, you know, 201, 202,
where there's no body response, et cetera.
IO bytes per second, things like that.
So, I'm gonna go in and choose the CPU time
and I can see whether I want to count the number of CPU,
which doesn't really make sense,
but the sum, the minimum, the maximum.
Right now we're on a very long timescale,
it's a 24-hour graph
and so we got nothing because the app didn't exist
and then we have a sudden spike of CPU time.
And so, let's focus on the past 30 minutes of CPU time.
I can also choose the granularity.
So, I can see, I wanna see the last 30 minutes
and I wanna see it down to the minutes.
So, now I can see a few minutes of CPU graphs
and we can see how many milliseconds of CPU was used.
Now that might not be entirely useful,
I believe there is a...
Let's look at the number of requests.
So, this is the web app that I was playing with.
And you can see I did sort of a spike of eight requests
in a single minute
and then a few more the minute after and now nothing.
So, this is how we're getting access
to looking at the basic metrics of an app.
Now, it doesn't have to be an app service,
I can change the scope here, right?
I can go to, let's say for example,
now you can't choose resources that are of a different type.
You can't put a web app and a VM on the same graph.
So, I'm gonna remove this one scope
and I'm gonna add in the virtual machine
as its own second thing, say Apply.
Select a metric.
I can see that I want a percentage of CPU utilization
and we're still in the 30 minute.
And we saw that there was a spike
when the VM was created up to 50% CPU.
And now the CPU is 2%, 1%
'cause nothing's really happening with that virtual machine.
So, this is a centralized location
where we can get various data about our resources.
Now, beyond metrics,
you might wanna be interested in the various logs
that a resource puts off.
So, log analytics goes,
and we can do run queries under the Logs section.
So, once again, we have to select the scope.
I'm gonna pick that scope.
And we can pick
the entire subscription.
But what I'm gonna do
is I'm going to just drill down a little bit,
I'm gonna go into the resource group.
Now, when selecting a scope,
I can select pretty much any resource
or resource level inside.
So, I can select the subscription,
I can select the resource group, the storage account,
the type of data being stored in the storage account,
things like that.
We can see the VMs in here, we can see the app services.
So, this is gonna allow me to run queries against this data.
Now, for the sake of this demo,
I'm gonna choose the entire subscription.
So, I have a Pay-As-You-Go subscription, had it forever,
and I'm gonna choose that entire subscription and say Apply.
Now, it's gonna be easier if I minimize this menu
and make sure this menu is open.
Now, every type of resource within Azure
that collects diagnostics and logs
has different table names.
So, on the left here we see this tab called table,
and I can look under app services
and I can see the incoming HTTP requests of an app service
as well as AzureActivity and AzureMetrics.
AzureActivity and AzureMetrics are sort of common tables.
You'll see this under a lot of services.
So, let's say if we go under
Load Bouncers has AzureActivity,
virtual machines has activity and metrics,
but it also has one called Heartbeat.
And once per minute,
a log is created in this log analytics once per minute,
and that's called the heartbeat
and that goes in the heartbeat table.
Now, I don't think one of the things that the log query
suffers more than the metrics
is the lag between the time that the logs are collected
and the job runs to process the logs for this.
So, even though I've had a VM
that's probably been running for half an hour at this point,
I'm gonna run this
and you're gonna see that it's giving me this error even,
it can't even find such a table called Heartbeat.
So, even though the VM does exist
and we have diagnostics turned on,
it's way too early for the data to have been processed.
I'm gonna go under AzureActivity.
Now, AzureActivity is, like I said, it's a common table
to many different of these service types.
And if I just want to,
let's look at the last four hours.
So, there's this time range
and I can filter myself down and say Run.
Then, I'm gonna see things that I've done
against my account in the last four hours.
And I can even see that the current time
is close to 10:30,
but the last activity that was recorded was 8:40.
So, it's about two hours,
just under two hours behind processing this.
So, like I said, it's not a real-time log processor,
but it'll catch up.
So, you'll see I just entered the table name AzureActivity
and double clicked it,
it went into this window, hit Run,
and I'm getting results.
This is very much like SQL Server Management Studio
where you have a query window
and you can write with SQL server
you write SQL queries and you can execute them
and see the results.
Well this is not SQL, this is called Kusto,
K-U-S-T-O, or Kusto Query Language, KQL.
So, Kusto is its own query language,
but very similar to SQL.
And you have tables
and you can basically write queries and get results.
So, let's say I wanted to filter these results.
I've got 12 results
from this AzureActivity query
in the last four hours.
Let's say I wanted to filter it down,
I could put a where clause,
I could put a group by, I could do various things.
One of the things that it's worth looking at
is this Queries tab.
And so, Queries is some pre-built queries
that Microsoft is offering that might be interesting.
So, for instance, let's look at under Virtual machines,
if I wanted to see Computer with missing updates,
I'm going to clear out this window
and click on Computer with missing updates.
Now, I can see that it's pulling from a table called Update,
then there's this pipe symbol and the where clause.
And then there's basically, this is again KQL language
in order to do sorting and things like that.
Say I don't want that one,
I can erase it, Malware detection.
And again, it's gonna check this ProtectionStatus table
and do a where clause and even a summarize
in order to see if there's any threats detected.
So, they have these pre-built queries.
You can build your own, you can modify them,
you can save them, okay?
You can write alerts based on the results of this,
stuff like that.
So, this Azure Monitor
allows you to look at the log tables,
the diagnostic logs
from all your services where it's enabled,
and you can look at the raw data
in terms of looking at the contents of the table.
And you can write queries
or even use some of the prebuilt queries
to get the contents of this.
So, here's one, it says Show logs from AzureActivity,
and you can see it's only gonna pull the last 10 records
on order of TimeGenerated,
so I know that's gonna work.
So, this is how you can use Azure Monitor
to help you in terms of finding problems,
diagnosing problems, and things like that.


### 📺 Lesson: LAB: Implement Traffic Management with Load Balancer and Application Gateway


Instructor: So this video is gonna be a little bit
of a different video in that, what I'm gonna do is I'm going
to the official Microsoft learning GitHub
for this exam, AZ-104,
and we're going to go through one of the labs together.
And so right now this,
obviously Microsoft has official training for AZ-104.
It's often very expensive from official training partners,
but they do make their labs available
and this is a public repository.
So what I'm gonna do is I'm going to go to the GitHub,
this link to labs
and we're gonna look at the traffic management lab
because this is the one that deals with load balancers
and application gateway.
And that could be very interesting to see in action.
So this is the HTML friendly version
of Traffic Management Lab.
Now I'm gonna warn you in advance
that this is gonna take a little bit, so almost an hour
to get through the work
of provisioning some VMs in putting some load balancers
in front of it and application gateway.
So if you don't have that kind of time
or you want to continue on with the lessons
and not really go through a lab simulation, then feel free
to mark this video as complete and skip to the next one.
But if you do wanna see Azure in action,
maybe you don't have access to it yourself
or you just wanna see these things get created,
let's get through that together.
So the scenario is that there's a public website
and you want to load balance incoming public requests.
You need to have images
and videos from different virtual machines.
We saw this creating an application gateway that you can,
filter based on path.
You've got a level four load balancer
and a level seven load balancer that you can choose from.
All right, so I have gone ahead and downloaded the files.
The GitHub repository contains both the template
and the JSON files.
So I've downloaded that to my machine
and we are going to go into the portal now
and we're gonna go through this together.
So the first thing it has us do is
to find deploy custom template,
which is one of the first things we need to do.
So we're gonna deploy the virtual machines.
We're gonna say build your own
and we're going to say load file.
And I've chosen the VMs template .JSON
from my local machine.
We do have to save.
And then we're going to go to the parameters.
There's a parameter file, we're going to load file for that.
And I'm going to say save.
Now we are gonna be responsible for a few things,
making sure the subscription is correct,
choosing a resource group.
So I'm going to create a new resource group for this.
And as of 2013,
Microsoft no longer provides passwords in any
of their template examples.
So we do have to give the admin user here a password.
All right, now this is going to try
to create VMs of a certain size.
And so we do need to have,
let's look at what's being created here.
If I hit the create button, it's gonna try
to deploy VMs
and it's going
to see if my subscription has those available.
There are obviously limits to the number
of VMs on free plans
and also on some of the pay as you go,
you can run into those limits.
So let's keep an eye out for that.
Now we do have to wait for all of this to be created.
It's gonna take about five minutes.
So let's let this run.
Now we can't see what's going on here.
There's a network security group, one virtual network,
three network interface cards, three virtual machines,
and now it's running some deployment code
in a virtual machine extension,
probably a PowerShell script.
You can actually go look at the arm template
as a fun exercise
and we can see that it is running this PowerShell script
in order to get IIS set up.
So that's successfully deployed, we think.
Let's go to the resource group.
All right, easy step one.
Now the next step has us creating a Azure load balancer.
We're gonna take two of these VMs, zero and one
and put them behind a standard load balancer.
So let's look for load balancers.
We're gonna say create,
put this into our resource group.
We're gonna deploy this in the same region
as the virtual machines.
We're gonna choose the standard load balancer.
Keep in mind the basic is retiring not too long from now.
It's a public load balancer.
And we're gonna leave this deployed in the region.
There is the option for global load balancer, even though
we don't need that in this particular case.
All right, so now we need a public IP address for this.
So we're going to create one, it's called this name.
We need an IP address
and we need to create a new public IP address.
Give it a name.
Well I'll leave it as not zonal.
So basically regional static standard safe.
And now I'm gonna say save again.
So now we are gonna have a frontend.
This is where we put the virtual machines
in the backend pool.
So we're going to create a backend pool, give it a name,
put it into the existing VNET,
choose by network interface card.
And we're going to add VM zero and VM one, not a VM two.
Say add.
We can say save.
Next up we are gonna talk about the inbound rules.
Now according to the lab instructions, we are not going
to add the inbound rules right now.
We're just gonna say review and create
and then click create.
So let's do that.
So we do have to wait for this to deploy
and we'll wait for that to happen.
So that deployed and now we can see go to resource.
And under settings we're going
to add our load balancing rules.
So we have our frontend, we have our backend.
Now we need a way of connecting the two.
So I'm gonna say add, give it a name.
We're gonna choose the frontend.
We're gonna choose the backend.
For TCP port 80.
And we're gonna make sure that it's a straight through
from port 80 inbound to port 80 in the backend.
We do need to create a health probe.
It's mandatory.
So we're going to say create new.
And that is a TCP Health probe.
All it's doing is it's checking
that this port can be opened.
It's not making a connection,
it's not pulling data from the server,
it's opening the port if the port can be opened
every five seconds, then that's considered a healthy server.
We're not gonna enable session persistence,
leave all of these with their defaults.
Now one thing it wants us to do according
to the instructions, is to grab the public IP address
from the frontend configuration page
and open a browser window and navigate to that address.
So it says now hello world from VM one,
it's gonna say VM zero or VM one,
because those are the only two servers.
It might take a few refreshes in order to get it
to say zero,
but eventually it will eventually say zero.
All right, so the next set
of instruction's talking about the application gateway,
we're actually pretty well going through this.
So what we are going to do now is we're going to
provide layer seven load balancing, which is
basically at the application level it can analyze the path
of an HTTP request
and make decisions based
on which domain name you're going to
or what path along a server.
So the level four load balancer cannot do that.
So let's go ahead and create a application gateway.
Now in this case, what we're going to do
is have our application gateway direct traffic
to VM one or VM two in this backend pool.
So I'm gonna follow the instructions.
So it says to me to go to virtual networks.
So virtual networks.
Go into VNET one.
And we do need, the application gateway
needs its own subnet it.
It cannot have any other devices running on the subnet.
So we could have to create a application gateway subnet.
And I'm going to follow the settings
that it's asking me to place.
So I'm going to say here for slash 27.
So that's what it's asking for
and that's what I will provide here.
And then I can just say add.
Now we do need to go into application gateways
and we're gonna create an application gateway.
We're going to put this into our lab,
give it a name, it's gonna be the same region all along
standard V2.
We're not gonna do a scaling, minimum instances of two.
And we're just gonna deploy this to zone one
according to the requirements of the lab.
So we already have the virtual network
and we already have the subnet ready to go.
Next, we go to the frontend.
We need a public IP address
for our application gateway.
And so we'll choose that.
We say, okay.
Next we need our backend.
So we're gonna give it a name.
And what we're gonna do is we're gonna
choose virtual machines as our backend.
And we're gonna choose NIC one and NIC two
again according to the instructions.
Okay, so those are the two ones not zero.
So now we can say add.
And now we want a second backend pool.
This is gonna be the one that will have images.
And again, following instructions, it's telling us
to choose NIC one.
And a third backend pool.
This one's gonna be the one for videos.
Now we need to set up the rules in order for traffic to come
through the frontend to go to one of these three pools.
So we're gonna start with priority 10.
Listener has to have a name, protocol 80.
We've been dealing with basic listener.
Switch over to the backend targets
and we're gonna choose the application gateway backend pool.
And we are gonna have to create a new set of settings
'cause this is mandatory and it doesn't exist.
So we'll just leave the default settings,
no cookie affinity, no connection draining.
Now we do need to have multiple targets
for this path based rules.
So we're gonna say add multiple targets.
For the images, we call this images,
we're gonna choose the settings that we just created
and we're gonna send it to the images target.
And we're gonna do it again for the videos.
So for the video path,
we're gonna call this videos.
It's gonna be the same rule
and we're gonna do the video target.
So we're gonna add that as our routing rule.
We don't need to have tags
and we can say review and create.
Now, application gateway takes a few minutes,
load balancer, quite quick.
Application gateway actually does take five to 10 minutes.
So we're just going to say create
and then we'll let that run.
We're almost done.
So maybe Microsoft's gotten better at this,
but that was about four and a half minutes.
That's not too bad.
All right, so we're going to go
to the application gateway that we just created
and we're going to go under monitoring
and we're gonna look at backend health.
And we have our various resources.
Remember we have three backend pools,
but those are only pointing to two resources.
So one and two, two and one.
They're all healthy.
Now if we go to the frontend public IP address,
so we can copy that.
So this is going to the frontend of the application gateway.
So remember it should be between servers one and two,
and there we see one and two.
But it also handles image
that comes from one and it also comes from handles video.
And that should come from two.
So in this lecture,
reviewing the lab from the official Microsoft AZ-104 course
Implement Traffic Management,
which you could find, we were able
to create a load balancer, standard load balancer
that points to two machines, zero and one
to presumably display a website.
And we also implemented the gateway pointing to machines one
and two to also display a website and also distinguish
between servers based on the path being presented,
which could help with traffic management.
Last thing we're gonna do
before going is we're gonna delete all of the resources.
So I'm gonna go to the resource group
and I'm gonna say delete resource group.
Thanks for watching.
Let's continue on.

