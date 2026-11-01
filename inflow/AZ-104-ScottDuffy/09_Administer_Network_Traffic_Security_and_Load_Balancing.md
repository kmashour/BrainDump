---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "09"
title: "Module 09: Administer Network Traffic, Security and Load Balancing"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 09: Administer Network Traffic, Security and Load Balancing

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** Network Security Groups (NSGs), Effective Rules, Application Security Groups (ASGs), Network Watcher Diagnostics, Azure Standard Load Balancer, Backend Pools, Health Probes, Troubleshooting, Application Gateway v2  
**Line Range:** Lines 15755 – 17389 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


### 📺 Lesson: NSGs


Instructor: So you may have seen
when we were setting up virtual machines in the past,
there's a concept within Microsoft Azure
called network security groups.
Now, network security groups or NSGs
are a core way to control network access in Azure.
They act like a firewall,
using allow or deny rules based on things
like IP address port and protocol.
NSGs can be associated with either the subnet
or the network interface card or NIC.
And each rule includes a priority
and the rule with the lowest priority number
that matches will win.
So I'm in the Azure portal
and I've searched for network security groups.
I'm going to click create
and I've chosen a subscription
and you can choose a resource group.
I'm gonna put this into a ZVM, an existing resource group.
Now I'm gonna give it a name.
So in this case I'm gonna call it demo NSG.
And we have to choose a region.
Now this region should be the same as your subnet
or your virtual machine that you want
to associate this NSG with.
We don't need to deal with tags.
So we're creating a default basic NSG.
We're gonna say review and create and then create.
Now like I said, the network security group
acts like a firewall.
It's what's called an access control list.
And it contains both inbound
and outbound rules
that which traffic is allowed onto the network
and which traffic would be specifically denied.
Now you'll see from this that there are a set
of default rules.
So we already have three rules on the inbound
and three rules on the outbound that is given to us
that we can't control.
Let's look at them, I'm gonna go under settings
under inbound security rules to start,
and I'm gonna minimize this menu.
So we can see that there are three rules.
They are given the highest priorities.
So typically the rules that you create
will have lower numbers, thus higher priorities.
And they are that all traffic
from the virtual network is allowed.
All traffic from a load bouncer is allowed
and all other traffic is denied.
So if you have a network that's associated
with a default network security group
that you have not modified,
it's only gonna allow traffic from the virtual network
and the load bouncer.
It's not gonna allow any other traffic onto that network.
That is a access control list.
And you can see it's got port, protocol, source,
IP address or source destination address and the action.
So I'm gonna create one to just demonstrate this.
So let's imagine you want to allow
the RDP traffic onto your network.
So you've got an administrator has RDP, we're gonna say add,
and we're going to say either specific IP addresses
are allowed, my IP address,
so it can grab my IP address from my computer.
And that's the one that's only allowed.
The source port ranges can be any.
So let's allow traffic coming in from any range.
And in terms of the destination, it can be any server
that's running on the VNET,
but we're going to choose port 3389
which is the RDP port.
We could also choose RDP from this dropdown
to save ourselves from typing it.
You'll notice that RDP port 3389 is A TCP
and that is chosen for us.
We are gonna allow RDP traffic
and we have to give it a priority.
So the lower the number, the higher the priority,
and typically you're not gonna jam these together
like 100, 101, 102, 103.
You're gonna want some space so that you can be flexible.
So I'll leave this with the default 100 priority,
which is pretty high and we have to give it a name.
I'm gonna call it allow RDP.
So if I was to then click add,
right now this NSG is not associated with any network
or any network interface card.
But if I was to associate this with one of those two,
then RDP traffic from my computer
would be allowed over port 3389.
Okay? Now we also, I'm gonna go back to the NSG
menu here and we're gonna choose
outbound rules, and minimize that.
So you'll see by default
that the virtual network traffic is allowed
to communicate outbound within the virtual network.
So from VNET to VNET is allowed.
And any device on the machine on the network is allowed
to talk to the internet, that is allowed,
but all other traffic is denied.
So if we had
another computer on another VNET
or A VPN
or something like that, this is going
to basically be denied outbound.
So if we wanted to specifically allow certain traffic
outbound or deny traffic,
so let's say we want to block traffic
to the internet, then we would say add.
And we're going to say any source, that is any resource
that's already attached to this network.
And for destination, I'm gonna say service tag
and I'm gonna choose internet.
So that is any destination that is
outbound to the public internet.
And we're going to choose the HTTP traffic to block.
So let's say we wanna choose
port 80 blocking outbound,
and in this case we're denying that traffic, okay?
So we do not want this service
to talk to the internet.
Now I might use a higher number here
because if we have to allow traffic,
we would need to have lower numbers.
And we're gonna call this something
that makes sense to us, deny HGTP.
So now any network that this NSG is connected to
will not allow servers to talk
to public websites in secure port.
Okay? So that rule takes priority.
Alright, so that's an overview of NSGs.
Like I said, it can attach to the subnet
or to a network interface card.
Azure will evaluate both sets of rules together.
So if you have a NSG assigned to your subnet
and a different NSG assigned to your NIC card
then they're cumulative.
So every NSG comes with a default set of rules,
including deny all inbound and allow all outbound.
These all have high priority numbers
so your rules can be overridden.
And on the next video we're gonna talk about effective
security rules and we can verify
which rules are really applied.
NSGs are essential for secure access control in Azure
and is a core topic of this exam.


### 📺 Lesson: Implement Effective NSG Rules


Instructor: Now, in the previous video we created an NSG
and we added some custom inbound and outbound rules.
I mentioned that NSGs can be applied to both subnets
and network interface cards.
And Azure combines rules from both locations
to determine what's actually allowed or denied.
And these are called effective security rules.
So what I wanna do in this video,
is I'm going to create another NSG,
a different one,
and we're going to have a virtual machine
and we'll connect one NSG to the subnet
and a different NSG to the VM.
And then we'll look at the effective rules.
So I'm gonna create another NSG,
put it in the same group,
and I'll call it nsg2.
We'll say Create.
And in this second rule,
I'm going to allow port 80 inbound
onto this network
and we'll call this, we'll leave that as HTTPInbound.
And I also will allow RDP traffic,
as I did with the other one, from any source.
All right, so this rule has no restrictions on source
but allows HTTP traffic and RDP traffic.
Now, for this virtual machine, I'm specifically not going
to configure any inbound rules.
We'll skip over the data.
For NIC network security group, I'm gonna say None,
because we're gonna manually attach it.
And I'll just say Review + create.
And we'll let that be created.
All right, so let's go to the resource,
and we're gonna go under the Networking tab
and we're gonna look at the network interface.
And we can see that there's no network security group
currently associated with it.
So I'm going to associate one with it.
I'm gonna go into the network interface.
Remember, we said that we could associate
a network security group with either the network interface
or with the subnet.
So I'm gonna choose the demo-nsg
to associate with the network interface card.
And I'm gonna say Save.
And we can go back to the overview here
and we can see that we've got the virtual network subnet.
I'm gonna click on that.
And we're gonna go into the default subnet,
and we can choose the network security group from here
and we're gonna put nsg2, the other one there
and say Save.
So now what we have are NSG applying to the network
and an NSG applying to the card.
So now if I go back to the virtual machine under Networking
and I scroll, I can see both the network security group
attached to the subnet
as well as the network security group
attached to the network interface.
So both of them are listed separately.
We can see that there is again the tiny conflict
of HTTPInbound being allowed by one but not the other.
Now, we can see these rules in one convenient location
under the network interface card.
If we click the network interface name,
taken to the network interface,
then what we're looking for is under Help,
Effective security rules.
And this will tell us which NSGs are in effect
for this network interface.
And then using that information,
we can figure out why certain traffic is getting through
and certain traffic is not.
So we can see these are the two NSGs
that are associated with this network interface.
We can, from this convenient spot, view them,
and then we can even download a copy
which could help us diagnose,
let's say we know we're having trouble
getting port 80 through,
so if we focus just on the inbound traffic,
we can see that we do have a rule on nsg2 that allows it,
but we don't have a rule on the other NSG,
so Deny becomes the default.
So we can work out that there's a conflict here.
We can also do troubleshooting.
There's a section under Monitoring
that talks about network troubleshooting.
We can see why port 80 would be denied,
but we can also download the rules
and intuit that ourselves.
So, that is under Help, Effective security roles.
Hopefully that all makes sense.
Leave a question in the Q &amp; A section of the course
if you have any questions about NSGs.


### 📺 Lesson: Application Security Groups


Instructor: Now when we created
this network security group in the last video,
we created a couple of rules
and we allowed it to go to any destination.
So when we created these two port 80 and 443 rules,
we did not specify any particular destination.
What I'm gonna do is I'm going to delete those,
both of those rules,
and we're gonna re-add them
with a specific destination in mind.
Okay? So I'm gonna say Add New Rule,
and it's going to be the HTTP rule.
I'm gonna call this priority a thousand.
And instead of seeing destination Any,
I'm gonna specify an IP address, that's a destination.
Now this IP address supports what is called CIDR notation
with this /24 if you want.
But I'm going to, basically, copy the IP address
from our VM.
So if I go to my VM here,
I can see there's a couple of IP addresses.
One is a Public IP and one is a Private IP.
I'm gonna copy the Private IP just for this example
and I'm gonna paste it here.
And now we have traffic traveling from any source
to this specific VM over port 80.
And just for completeness,
I'm gonna add the other one as well.
So we're gonna see HTTPS,
IP address, same destination.
All right. So now I've re-added the rules
but the rules only allow traffic into that single VM, right?
This aznewtest VM is the only destination
allowed to receive traffic.
All other traffic over these ports
to other destinations will be denied.
Okay, now this gets...
This can be very hard to manage.
First of all, IP addresses can change.
And second of all, you're gonna end up
with this list of IP addresses.
Like I said before,
you want your NSGs to be minimized, the number of NSGs.
So let's say you only want three of them
even if you have 20 networks.
But if you're gonna start hard coding IP addresses in there,
the list of IP addresses gets, kind of, long
and then doesn't mean anything to you.
You look at this and what is that?
So there's a solution to that
called Application Security Groups.
So let's create...
Go to the top here and say Application security groups.
And an Application security group
is a logical grouping of resources
that can be a destination.
So I'm gonna say Create.
And I'm gonna make sure that is in my correct subscription.
I'm gonna put this into my NSG Resource group
and I'm gonna call this newasg, oops, asg.
And say Create.
And so, like I said, the Application security group
is a logical grouping of destinations.
And so it really is an abstraction.
I can add the IP addresses
into this application security group.
And then you only refer to the application security group
when you are creating the NSGs.
So you don't actually do anything
within the application security group resource.
We're gonna go back to the virtual machine.
So I go into virtual machine.
I'm gonna go back into the Networking tab.
And then under Application security groups
there's this link,
configure the application security groups.
It can be a part
of more than one application security group.
I probably should have named this something more readable.
So instead of newasg
I could have named this frontend websites.
And if I call this frontend websites,
then it would be clear to anyone who sees it
that this VM has a purpose.
Okay? So I add the VM to the Application security group.
Then, I can go back to the network security group
called newnsg, remember?
Under inbound security rules.
You can't unfortunately edit a rule
so I'm gonna delete this rule again.
And instead of specifying it by IP address
I'm gonna say Add.
And the destination
is gonna be the Application security group.
And then we can say the newasg.
And so this is the port 80 rule. Add.
So now instead of specifying it by IP
I specify it by application security group.
And then that becomes a lot more readable
in terms of understanding
that the intention is for traffic
to go to the frontend websites
as opposed to this by IP address.
Add the HTTPS one as well.
So the application security group
really is just an abstraction of the destination
instead of specifying a list of IP addresses,
which may or may not mean anything
to the person reading them and become unwieldy
when you're really trying to minimize
the number of network security groups,
and make it easier to manage and thus more secure.


### 📺 Lesson: Virtual Network Troubleshooting


Narrator: So we've seen that we can
create network security groups
to allow certain traffic inbound and outbound,
and deny certain traffic
inbound and outbound.
Diagnosing these issues can be a little challenging.
And fortunately, there are several tools in Microsoft Azure
to help you diagnose these issues.
I have a video later in this course talking about network
watcher and IP flow, and things like that.
The one I want to talk about right now is called
connection troubleshooter.
So we're in the virtual machine under network settings,
and I'm gonna scroll down on the menu under help,
under connection troubleshoot.
So let's say we've got this VM
and for whatever reason, it is not able
to do something we need it to do.
Connect to a server.
So it's gonna go from this virtual machine
outbound to another location.
So this is the source is this VM.
Now I'm gonna enter bing.com as the destination.
So this machine, for whatever reason,
cannot communicate with bing.com
and I need to know why,
I'm gonna choose TCP protocol.
Now, if I try Port 80,
we know this shouldn't work
because we're blocking Port 80,
specifically in the NSG.
So I entered Port 80 in the destination,
and I'm gonna say run diagnostic tests.
Now, the first time I run this,
it needs to deploy a tool to the VM, an agent,
so there would be a deployment involved.
But I've done this before.
So this is not doing the deployment right now.
So this is gonna take a couple of minutes,
but it's gonna try to communicate
with bing.com over Port 80.
Let's see what it says.
All right, so I scroll down
and we'll see that Port 80 has not been reachable.
It is blocked, and it tried 30 times
and it failed 30 times.
Now what we would expect then
is if we tried a different Port, like 443,
which is the secure port,
and run the test again,
this should succeed
because we're not blocking outbound Port 443.
And we let that run, we scroll down,
we see that it did work.
So it tried 66 probes, zero failed,
and we can see amazing latency of one millisecond
and maximum latency of two milliseconds.
So the performance is incredible,
but 443 worked because we don't block that port.
So we can use connection troubleshooter to see
what are the reasons why we can't connect one
thing to another.
Of course, if we had a virtual machine that we can try
to connect to,
we can just select it from a dropdown here.
So try connection troubleshooter.
If you ever wanna see why your machine can't connect
to something else that it needs to and it's failing.


### 📺 Lesson: Introduction to Load Balancing


Scott Duffy: So, in this set of videos,
we're gonna talk about a very interesting concept
and that is the concept of load balancing.
Now, you may have heard this term
and maybe you're intimately familiar with it,
but let's talk about it.
So, a load balancer is generally,
a device that usually evenly distributes traffic
that's coming in from somewhere
to multiple servers that are behind the load balancer.
So, you can think of the load balancer
like a traffic cop
or like somebody standing at the front of the passport line,
directing people that come to a specific person
that can help them.
So, you go to line number one, you go to line number two.
As the traffic comes in, there's a load balancer
to make sure that the lines are evenly distributed.
We can look at that in a technical way
with a graph like this.
So, in this graph we actually have two load balancers.
Traffic is coming in from the internet over port 80,
at the top.
Then we have our first load balancer called
the public load balancer.
We'll talk about that in a second.
And there are three web tier servers
behind the public load balancer.
And so the traffic comes in and is distributed to them
and then those servers themselves need to communicate
with some type of business tier.
And there's an internal load balancer
to distribute traffic over port 443,
between the web tier and the business tier.
So, as you can see,
there's a lot of redundancy built in this system.
If anything happens to one of these servers,
the system will continue to function.
So, when you're dealing with critical workloads,
a single virtual machine often will not suffice.
So, either you have a lot of traffic
and so you need to have multiple aisles open
to serve people,
or it is too important for there to be any closures.
So, if you think about public websites like microsoft.com,
the public facing website from Microsoft,
there are hundreds and thousands of servers
that are serving up the content from that site
because it's just too important for a single server
to be able to be responsible for it.
But if you have a non-critical workload,
let's say you have a server
that just runs a job once a month, you know,
collects the files from one directory
and copies them to the other,
if that's a single server's job,
then you don't necessarily need all that redundancy
just for this non-critical workload.
So, what kind of options do you have in the cloud
when you need more?
So, option number one
is that there's always this scale up option.
So, you can take the virtual machine that you're using
and you can find a bigger, more powerful virtual machine.
Microsoft Azure and all the cloud computing platforms
have a lot of options.
We saw earlier in this course
over 1000 virtual machine options
when you go to create a virtual machine.
So, if you're currently running a D2 instance
with eight gigs of ram and two virtual CPUs,
you can upgrade to the D4 instance with 16 gigs of ram
and four CPUs for double the price.
Or you can go up to eight or 16 or 32.
There are options to go higher
and the pricing is just purely double
when you double the power.
You can see it goes on beyond 32 all the way up
in this case to 96.
So, you can go up pretty high in terms of scaling up,
but this is not still the recommended way of scaling
when you have the need
for additional support for a busy server.
Now one of the conditions here
is when you reach that D96 server, you've got nowhere to go.
Okay, there's no D 128
or D 256 that's available.
There might be in the future,
but you're already running a very big powerful server.
So, there are a few downsides of using a single server
and I alluded to them before.
It is true in computers and technology
that sometimes you do need to reboot.
So, you do have a operating system update,
a security update,
the Azure itself needs to be updated
or on your side you have an application
that might not even require the operating system to reboot,
but you have to stop traffic
in order to upgrade an application to a new version
and quickly test it before you turn on traffic again.
So, either Microsoft Azure
or your own updates may require server downtime.
There's also this unexpected downtime
in terms of power outages, internet outages and others.
So, you could have a single rack
or the entire data center going offline
for a couple of hours
and that would be inconvenient to you as well,
as well finally, you may have a what's called a burst,
which is a in short, infrequent need for more power.
And so there's other ways of doing scaling
in terms of load balancing,
that are more convenient for traffic
that comes in suddenly
as opposed to having to go from a D4 server up to D64
and then back down to a D4
because you're getting one hour of unexpectedly high amount
of traffic into your application.
So, that was option one is just to scale up and down.
Option two is scaling out and in and out to be more precise.
So, this is the diagram we saw
at the beginning of this video
where you have three servers at the web tier
and three servers at the business tier.
It would be very easy to add a fourth or a fifth
or a sixth server to either of those tiers
if the demand for your application was to rise.
You're also going to see less risk
in terms of sudden downtime
and it's easier to even bring your application down
for Azure system updates or Windows updates
'cause you can do it one server at a time.
I did mention public and internal load balancers.
So, a public load balancer faces the public internet.
It accepts traffic over port 8443
or a public port
and then it distributes it to the backend VMs
by using the public,
load balancer has a public IP address
and this is often used for websites and web apps and APIs,
anything that is public facing.
The internal load balancer as the name applies,
accepts traffic within the virtual network.
It does not accept public traffic,
does not have a public IP address
and this is used for backend servers,
internal services like databases
or the middle tier of an application.
So, I mentioned before, if you do your scaling this way
with two or more servers behind a load balancer,
you get benefits and one of them is the uptime availability
of your entire application.
We saw before if one of those three servers went down,
application would still function,
even if two of those servers went down,
the application could still function.
Now maybe it would be slower or less performant,
but you could suffer minor outages
and still have uptime.
Microsoft provides what are called service level guarantees
or SLAs,
in terms of their promise for your virtual machine.
So, if you're using a single standalone virtual machine
without a load balancer,
and you choose one of the premium
or premium ultra discs,
they do have a uptime guarantee of 99.9%
for the premium SSD
in which you would get a 10% credit in a month
if they fail to meet that.
If it's worse and it's only 99% uptime, you get 25% credit.
And if in some disastrous way they only have 95%
or less uptime in a month
for a single standalone virtual machine,
they'll give you your money back for that month
for that virtual machine.
So, even without the load balancer,
you do get some type of service level agreement.
But when you start to use a load balancer
in particular an availability set,
then you are getting not just 99.9% guaranteed,
you're getting 99.95% guaranteed,
which may seem like a small jump of just 0.5%,
but that cuts your expected downtime in half
and you can see for 99 and 95,
as that remains in terms of your service credit.
When you're using zones,
two or more VMs in availability zone,
again that has to be probably behind a load balancer
or some type.
Then the uptime expectation goes to 99.99%,
which is a massive increase in the availability
for that service.
Obviously the more VMs you add,
then your expectations
should be to improve upon that even further.
Now within Microsoft Azure there are three
or four types of load balancers.
There is the Azure load balancer service.
So, the fact that it's named load balancer,
might make it a little confusing
when I talk about other types of load balancers.
There's another load balancer called an application gateway
and we'll talk about the difference of that in a second.
And finally, we have the front door service,
and that is a whole range of services bundled together
that is probably the recommendation
if you're looking at a very web facing property
and you want a variety of things like CDN
and load balancing across regions and things like that.
Front door service is probably going to be my default answer
unless there's a really good reason not to.
Like if there's a cost factor,
then you might choose one of the other services.
But if money is not mentioned in the question,
I might be leaning towards front door services being
what Microsoft recommends.
Now for the basic load balancer, there are different SKUs.
You may hear the basic SKU
and previous versions of this course, I mentioned it,
that has been deprecated.
So, you cannot create a basic SKU anymore from scratch,
although they still exist
and you'll never see this as being an answer on the test.
The standard SKU is now the option.
It has the service level agreement,
so it has its own service level agreement
on top of the virtual machines.
It supports a network address translation in terms of NAT,
you can do private links, it can do availability zones
and things like that.
For virtual network gateways there's another type
but that's not covered on this exam.
Now I've mentioned we saw with virtual machines
and availability set,
you get a certain amount of uptime guaranteed.
In an availability zone situation,
it's the most you can have in terms of availability.
So, if availability is your primary concern in the question,
then I would look for the availability zone answers,
and that could be standard load balancer.
That could also be application gateway.
So, when you're creating these load balancers
in an availability zone,
you're going to get a couple of options
to choose from when you're creating it.
One is what's called zonal,
Z-O-N-A-L,
and that means you're placing the availability load balancer
in a specific zone,
and then you're gonna need more than one
to put it into zone one and zone two and zone three.
So, you're talking about instances
of the load balancer.
For zone redundant,
this means that Microsoft takes care
of distributing it across zones
and that is a different, again, type of load balancer
that you get to choose from.
So, using load balancers allows you to build
what are called highly available multi-zone architectures.
Now I mentioned the types of load balancers.
There's distinction between them as well.
So, this, you're gonna look for this in the question.
And the Azure load balancer
is what's called a layer four load balancer
that operates at the network layer TCP or UDP.
That means it has no knowledge of HTTP protocol.
It cannot detect the domain name or the path.
It's not inspecting the packets,
it just understands TCP and ports.
And so if you need that kind of load balancer,
then you would go with the Azure load balancer.
If you need to understand paths,
let's say the video subdirectory
has its files on one server
and the images subdirectory
has its files on a different server,
that would be an application gateway.
Okay, so that's called a layer seven load balancer.
It operates at the application layer.
Finally, the front door service supports load balancing
as well as SSL offloading
and content delivery network support, things like that.
Now, I haven't mentioned the traffic manager service.
That counts as a load balancer technically,
but all it does is it manages
the Azure DNS
in a way that if the person types the domain name
into their browser,
it goes and does a DNS lookup of that name
and the Traffic Manager service
will give them a different answer
based on their geographical location
or some other algorithm.
So, Traffic Manager
doesn't really operate as a load balancer,
it operates outside of the cloud really,
and it's doing a DNS lookup providing different answers
to different people based on their location.
Anyways, this video got quite long,
but that's a good overview of load balancing
within Microsoft Azure.
Let's do a demo.


### 📺 Lesson: Setup Load Balancer


Instructor: One of the advantages of cloud computing,
is obviously the ability
to add and remove additional resources to an application,
depending on demand.
So, if you design your application such that,
it can run on one or more virtual machines,
you can easily add additional virtual machines,
which will add capacity to your application.
The way this is done, is either through
something like a virtual machine scale set,
or you can have individual virtual machines,
organized in an availability set or in availability zones.
But what you would need
is some type of way to distribute traffic,
in front of that, and that is called a load balancer.
So, let us create a load balancer.
So, I'm gonna go up to the search here,
and we can see load balancer is a service,
we don't have any load balancers currently.
There are multiple different types of load balancers
within Microsoft Azure.
We're gonna talk about this,
the Standard Load Balancer, here in this video.
And in the future video we'll talk about
application gateway, and other services.
So, right now we don't have any load balancers,
so let us create our first load balancer.
Now, like any resource within Azure,
we're gonna have this wizard interface here.
We're gonna have to create a resource group,
or put it into an existing resource group.
I'm gonna choose my,
one of my existing resource groups to put this in.
Let's give it a name.
So, azfirstlb,
as in a name.
You generally want your load balancers
to be running in the same region as your resources there.
Doesn't really make a lot of sense
to have your load balancer in North America,
and your virtual machines in Europe, for instance.
So, you'll wanna keep them close by.
So, I do have a VM running in Northern Europe
and so, I'm gonna keep my load balancer there as well.
Now you'll notice that there's this message here
for the SKU,
that the Basic Load Balancer is retiring,
in September, 2025.
So, if we pull in the documentation here,
we can see that the Basic Load Balancer will be retired,
and they want people to upgrade to a Standard Load Balancer
prior to the retirement date.
So, we're going to basically,
I think we're gonna go start looking at
Standard Load Balancers as being
the only type of load balancer we need to be concerned with.
There used to be a Basic Load Balancer.
Again, it still exists, but it's being retired,
and you should not consider it
for any type of use at this point.
Now you'll see that the Standard Load Balancer
has some additional features,
including the ability to have IP based backends.
What this means, is you could have
either public on-premises servers,
or servers running in a different cloud.
So, Amazon AWS or Google Cloud servers
with your load balancer being in front.
Now, like I said, you do typically want them to be
close by for latency and lag,
but it is possible to have a server of any type,
that is, at least it has an IP address,
that you can put as the back-end.
TCP, UDP protocols are both supported.
The Standard Load Balancer,
supports any virtual machine,
or a virtual machine scale set on a single virtual network.
The Basic Load Balancer required them to be,
in an availability set.
And so, this is, makes it a bit more convenient.
You'll see the Standard Load Balancer was required for SSL.
There was zone-redundant, zonal,
and non-zonal options available.
You could have your load balancer
deployed to different zones.
So, there is, like I said,
a lot of more features under Standard,
including having an SLA.
It does cost money,
and so, the basic is being retired.
Let's go back here.
So, I'm gonna do a
Standard Load Balancer.
Now you can see there is this concept
of a Gateway load balancer,
that could be a load balancer in front of
application gateways,
and other,
virtual-
Virtual networks gateways.
So, we're not going to worry about that in this video.
When we are dealing with public versus internal,
a public load balancer has a public IP address,
and the resources behind it,
typically you're gonna wanna hide from the public,
so they will have private IP addresses.
You do have the option of having an internal load balancer,
that does not have a public IP address,
and that means that only other servers running in the cloud,
would then have access to those resources.
I'm gonna let it have a public IP address.
And finally, you can see that we can deploy this
to a specific region,
or we can have this as a global load balancer,
that is not tied to a specific region,
even though it's deployed to a home region,
it is run in a global level, not to a regional level.
We'll just leave it as as a regional load balancer.
So, load balancers have, let's say three main components.
One is the front-end.
So, now we created this as a public load balancer.
So, that means we're gonna want to put
a public IP address in front of this.
The backend are the servers that are running behind it,
we're gonna deal with that in the next video.
And then there are the rules that dictate how traffic goes,
between the front-end and the back-end.
So, I'm gonna click on this, "Add a frontend IP".
We do have to give it a name,
and it can be sort of any name.
So, I'm just gonna say P-I-P.
You can have an IPV4 or IPV6.
As you know, they've been saying for about 20 years
that the IPV4 space is full.
And right now, I think all relevant
of Microsoft Services support are IPV6,
so, took a long time to get there,
but if you did wanna run IPV6, Azure fully supports it.
We can run, you'll be giving in a full IP address.
If we did have an IP prefix,
there's a whole thing within Azure
where you can set up your own range of IPs
and that's called an IP prefix.
We're gonna just leave it as the IP address.
I do need to create an IP address.
So, create new,
publicip,
and it's just gonna give me one,
I don't need a zone for this.
So, I'm gonna say this as being No Zone.
And again, there's no gateway involved.
So, we're just gonna say save.
So now, we have,
we're gonna have a load balancer with a front-end.
We're not gonna set up,
I'll do the back-end in the next video.
So, we're not gonna set up the backend pools just yet.
What I am gonna do, is I'm going to let this,
I'm gonna deploy this,
without any rules or without any backend pool.
So just say, review, and create, and save create.
So, we have a load balancer,
that has no servers and has no rules,
but we can modify it to have those,
and we'll do that in the next couple of videos.


### 📺 Lesson: Add VM to Backend Pool


Instructor: All right, so let's go and add
the VM that I have into the backend pool.
And we can set up rules and things.
So we have a load balancer here.
It has nothing in the backend pool, no rules.
You see that it's a standard load balancer.
And so, what we're gonna want to do is start to set it up.
Let's go to backend pools.
Now, a backend pool is a server or a group of servers,
usually has to be multiple in order
for this to make a lot of sense,
that are gonna handle the traffic that is coming
through the front end of the load balancer.
So you can imagine a user is on the internet.
And they type in www.website.com.
It hits the load balancer first.
And the load balancer has to decide
where to send the traffic.
You can have multiple backend pools,
so multiple groups of servers.
And you can set up different rules
to send the traffic to different servers.
So let's say you have one set of servers
that handles the website
and another set of servers that handles images,
and big files, PDFs, and videos, and things like that.
You can have those as two separate sets of servers,
two separate pools, and two sets of rules.
We're just gonna keep it simple right now.
We're just gonna add a new backend pool.
Give it a name, call it pool1.
And we're going to point this to our virtual network.
Like I said, I already have a VM.
It already exists.
And so, we're going to point it to that.
Now, you'll see that it says
network interface card as the default.
So this is using Microsoft Azure
to know that there's a network interface card.
Or I can define it by IP address.
If I knew the IP address, I could sort of define that.
Let's just keep it as network interface card.
I only have the one VM, so I'm gonna select that.
You'll see that it's got an internal IP address.
It's gonna choose that.
If you don't see your server,
it's probably something that is
like not running in the same region.
There's probably some other requirement
that needs to be fulfilled.
When we were dealing with basic load balancers,
you had to be part of an availability set.
And there was more restrictions in the standard.
It's a lot easier just pointed to the VM.
So I'm gonna say save.
Now, one thing that we don't have yet are rules.
So we have our single VM sitting in the backend pool.
But there's no way that traffic is gonna
get from the front end to the back end.
So we do have to create a rule.
And so, we're gonna call this lbrule1.
You can choose the existing front end address.
Choose the pool we just created.
Choose the protocol, which we'll choose TCP
in this case for port 80.
So any traffic coming over the HTTP port, port 80.
You could do port mapping at this thing.
But currently, we don't.
Now, there is this feature of health probes,
which is if we had multiple servers in the backend,
we could create a health probe
that would then identify servers that are having
health issues and take them out of the pool.
So if there's five servers,
four of them are great
and one of them is not responding to requests,
you could have your health probe exist
such that it removes that bad server.
I'm gonna skip that for now.
We're gonna allow all traffic to go to any server,
instead of having it what they used to call sticky sessions
where the client IP based on the protocol
and the IP and the port would go
to the same server every time.
We're gonna keep all the defaults here.
Now, it's important to know
that the rules have changed in Azure
in the last couple of years.
And virtual machines behind a load balancer
do not have access to the internet by default.
So we are going to have to...
If we want this server to have
access to the internet,
we're gonna have to create outbound rules
to allow the pool members to access the internet.
So while I'm gonna leave this as the default,
but we're not gonna create any outbound rules.
And so, this server is not gonna have access
to the internet at the current,
the way that it's set up currently.
Health probe, mandatory.
So let's create a health probe.
So this is called probe1.
And it's gonna check port...
It's just gonna do a TCP check on port 80.
So it'll open the port.
If the port itself is connecting,
then it's considered a success.
A lot of times you may want to do
a more sophisticated health check,
which is like an HTTP or an HTTPS check,
in which let's say you are checking
a specific HTML page that exists on your server.
And that's what determines that it's successful.
So you may have more sophisticated
success or failure criteria.
I'll leave it as a TCP check for now.
And then we can say save.
So that's it.
At the very least right now, we a front end IP address.
And if we navigate to this through our browser,
the traffic should flow through this load balancer
to the VM behind the scenes.
Now, in order for the VM behind the scenes to respond,
it has to have IIS set up, which I haven't done yet.
So we can't test this at this very second.
But the traffic should get through.
If you send traffic to the public IP address
of the load balancer,
the backend pool will receive the traffic
and be able to reply to it.


### 📺 Lesson: Create a Test Environment Quickly Using GitHub


Now Microsoft does a pretty good job of providing documentation.
You know, Microsoft Learn and GitHub resources.
I'm in GitHub right now under the Azure user and the Azure Quickstart Templates repository.
A link will be provided attached to this video.
The Quickstart templates are an easy way to find literally hundreds of examples that you can deploy
into Azure.
Now you can see here there's been 30,000 commits over the years.
And so this thing has just been growing and growing.
There's even a website for it.
I'm going to go into the Quickstarts submenu here subdirectory.
Now they've basically organized it according to the core technology here.
So we can see API management Quickstarts are under one area compute Quickstarts.
The CDN, any kind of thing that you want to learn, you can go and check out the Quickstarts and you'll
be able to find it.
For this example, I want to look for a load balancer load balancers under networking.
So it's Microsoft Network.
If I go into there so I can see under the networking quick starts.
Again.
There are dozens of things from Expressroute and firewall bastion service gateway.
So I want to find a load balancer.
I'm just going to do control F, and I know that there are different versions of that.
We've got IPv6 load balancer Cross-region load balancer.
The one that we're interested in is called load balancer standard create.
Now another cool thing about GitHub is in this quick starts.
There's just this button here that says Deploy to Azure.
There's also a visualize button.
So now I'm going to go and deploy this load balancer.
It's going to open up the portal.
And it's going to grab this quickstart template for me.
You can see that it's load balancer standard create from GitHub.
I do have to fill in some details.
I have to create a resource group for it.
So I can say.
New ELB put in his own resource group.
I'm going to choose a region for it.
I'm going to put this in East US two.
This project name basically is going to feed into the names of other resources.
So this is like a prefix that's used when creating all the other resources.
The location you can see the default is going to pull from the resource group location.
So this happens to be East US two.
I'll leave that for the virtual machines.
I have to give it user ID and password so we can see it's defaulting to standard D2's instance type,
which is pretty small, but that's fine with me.
I can say review and create.
And so I should be able to hit create.
Now this is basically deploying the quickstart template directly from GitHub.
And I think this is pretty cool the way that that found I found a resource that I want to play with
and I'm just able to hit deploy, provide some details and it goes off.
And does that work.
So this is one of the really cool things about ARM templates.
So while this is deploying and we can see the resources are being deployed here, let's go back to the
GitHub repository for ARM.
Those quickstart templates.
And like I said I think this ARM templates are really a neat way to deploy resources for testing.
I think there is a certain amount of ARM template knowledge required for this exam, and so it is probably
in your best interest to spend at least some of your time looking at the way that ARM templates are
created.
So pick something that you find interesting.
Find the arm template for that.
There's some bicep in here as well, which is pretty cool.
And look at the way that the ARM template is configured.
The various properties of this JSON file, how parameters are passed, how resources are specified.
Because there is a good chance there's going to be a couple of questions on the exam relating to ARM
templates.
Now that you have to write them more, that you would have to understand what would go in a particular
value or what would be the parameter name.
So if this parameter name was missing, you should be able to determine what is the likely parameter
name from a list of predefined options.
So yeah ARM templates quickstart.
The link is attached to this video.
Definitely check it out.


### 📺 Lesson: Troubleshoot a Load Balancer


So we have successfully deployed the load balancer, three virtual machines, three network interface
cards, public IP network security group virtual network using that template.
And we can actually go into deployments of the resource group.
And we can see that the template deployment succeeded.
And it took around seven minutes to deploy all those things.
A lot simpler to do than to set them up from scratch yourself.
Now let's go into the load balancer.
So the purpose of this video is to look at all of the things that can go wrong with a load balancer
setup, and how what I would do to diagnose those.
Now I want to start off by saying that there's really only 4 or 5 setting blades within a load balancer.
We can see them listed as front end, back end health probes, the load balancing rules, and the network
address translation rules.
There's also the outbound rules, but that's not a very rare thing that people are going to set up outbound
rules for traffic.
Okay, so what can go wrong with your front end configuration?
Well, of course, this is the IP address that's available to the world, right?
So if you're going to enter that IP address into a browser, you're going to get some type of result.
It's pretty cool that this template has a running web browser that says hello World and the name of
the server as part of the configuration.
So thumbs up to the template that that does that.
That could be an nginx or something type thing.
So the IP address is what is connected to the world of course.
And so if you're using a domain name, you have to make sure that that domain name resolves to the correct
IP address.
That that's all set up uh, for domain resolution.
Now the IP address is associated with rules.
So this is this will be under load balancing rules.
But if I go under this I can see that it's my HTTP rule.
Okay.
That's what the rule that it's associated with.
I'm going to do that later on here.
Go into the next one is back end pool.
So what can go wrong with your back end pools?
Well first of all are you pointing these load balancer to the correct servers.
And so you may have 123.
You might have several back end pools that are all resolved to answer for this traffic.
You can see here that one of my virtual machines is in a stop state.
I just stopped it myself.
And so one of the things that could be happening, of course, is that only two of your servers are
doing the work, and the third server is never called upon.
Right.
An unequal distribution of traffic.
Now you're not going to see VM two coming up on the web browser because it's stopped and because of
the health probe, health probe is removed VM two from the rotation.
So the health probe is what decides whether the back end pool is returning a normal response.
So this is the health probe.
If we go into it, we see it's a TCP health probe that's checking port 80.
We also have the option for HTTP health probes and HTTP s health probes.
An HTTP health probe checks the document can be retrieved from the web server, whereas the TCP health
probe checks to see if it can connect to the port.
So this is trying to connect to port 80.
Now it's going to try it every five seconds forever.
And if at any time the health probe fails, it's going to remove it from the rotation until the health
probe succeeds.
So if the problem resolves itself, then that's fine.
Go to back end pools.
This server that is deallocated has been kicked out of the pool based on the health rule.
I can actually click on this and say start.
But we're going to start that up.
And then then hopefully we'll see VM start to get responses from our calls.
Now the fourth A critical part of a load balancer course is the load balancing rules.
And we saw the front end IP addresses connected to this rule.
And this rule basically takes the front end address and will send all traffic from port 80 in inbound
to port 80 on the server.
So you're going to have to have make sure that your server is listening on that port.
This is the pool that contains the virtual machines.
So make sure that your load balancer rule goes to the right pool.
Again the health probe has been chosen here.
Now session persistence is whether the same user gets sent to the same server every time, or whether
you can have any server responding to that user.
This concept of Idle is basically the client and the server have this open connection, as opposed to
it being closed and then having to be reopened.
All right.
So we're going to leave the load balancing rules as they are.
The final section is Nat rules.
Now we don't have any setup, but network address translation is more specifically when you're taking
in traffic over one port and sending it to a port mapping to the target port.
It is, you know, incoming traffic sent to a selected IP address and port combination to a specific
virtual machine as opposed to the whole group of them.
So if you if you're looking for that kind of setup, then this is where you're going to debug any kind
of problems with that.
We don't have any of those.
Now if you do need to configure rules for traffic leaving the virtual machines traveling through the
load balancer, then you can set them up in the outbound rules here.
So in terms of debugging your your front end being set up correctly with the correct load balancing
rule, your back end being set up correctly.
Your server's all in a running and proper state.
Your health probes pointing to a proper location that would successfully tell your load balancer whether
or not it is healthy properly.
And finally, the rules themselves that you know, tell you which traffic can get through and which
traffic cannot.
So for instance, right now we don't have an Https rule.
And so that would be basically blocked by the load balancer.
Now I should also mention that you can set up an alerts process so that if there's ever any health probe
issues, uh, back end servers that are not responding, that a particular alert group is going to be
notified or an action group here.
So we can say the resource is the load balancer under the condition we can choose the um, we can see
here some of the signals available health probe status being one the number of bytes uh, being, uh,
sent through the number of packets, whether or not the load balancer, these are more administrative.
You wouldn't necessarily set these up, but health probe status is a good one.
And so we can see, um, the health probe was having problems.
I restarted the server.
And number of problems are going to, uh, go up and go down.
Right.
So we can choose the, um, we don't need to basically, we can say more than five failures in five
minute period means that you're going to get a notification, um, in your alert your action group here.
And that could be an SMS message.
It could be an email that could be some type of job that kicks off, etc..
So setting up alerts is another way of figuring out health probes are failing and your load balancer
is having difficulties.


### 📺 Lesson: Create Application Gateway


Instructor: Now, the load balancer
that we created a couple of videos ago
is actually what's called a layer four load balancer,
and it operates on the layer four
of the OSI transport model.
That means that it understands the difference
between TCP and UDP.
It understands IP addresses, NIC cards,
but it doesn't understand applications.
It doesn't have a grasp or a concept
of the packets that are being sent to the server.
It doesn't have the ability to inspect those packets
and make decisions based on the contents of those packets.
It's purely just IP addresses and ports.
Let's say you need the load balancer
to be able to look at the path of the URL
and send traffic to one server
if the URL contains a certain path
and a different server, if the URL is slightly different.
Okay, you could have different domain names
with the same IP address
or just paths underneath that domain name.
Well, then you need what's called a level seven
or a layer seven load balancer.
And in Azure, that's called an application gateway.
So if we go up and we search for application gateway,
we're going to see application gateways.
It is a load balancer,
but again, it operates at a higher level.
It understands that you're dealing with a web app
and it understands, you can look at the contents
of that packet and make decisions based on that.
So I'm going to say create application gateway.
I'm going to put this into the same resource group
that I previously did,
and we're going to call this demoappgateway.
I'll leave this in Northern Europe
with the other load balancer and the VMs.
Now, just like with load balancer, there are tiers to this.
Okay, we see that you have V2 standard,
the web application firewall V2.
Now the application gateway, there used to be a V1
that was deprecated in 2023, announced in 2023
by April, 2026, you should not be using the V1.
Again, you cannot even pick it from the list at this point.
And we must be moving to the V2 SKU.
All right, so I'm going to choose the standard V2.
Now, this web application firewall
includes a basic firewall which can understand
when somebody is trying to do basic SQL injection attacks,
cross site scripting attacks,
there's a list of industry standard attacks to websites
that a web allocation firewall can protect you against.
Now this application gateway can scale.
So if you have, if you are expecting a lot of traffic
and you may need more than one application gateway,
then you can certainly turn on autoscaling
at the application gateway level.
I'm not going to, I'm just going to leave one instance
and we're going to deploy it across zones here.
Again, we can choose IPv4 or both,
and we can choose HTTP2 standard
HTTP protocol, instead of 1.1,
it comes in as two,
and then it gets translated to 1.1 for the backend.
Let's leave that turned on.
We have to deploy this into a virtual network.
I'm going to deploy it into my virtual network that exists.
Now we need to have, it has to have its own subnet.
So having a VM on this is not going to work.
So we need to say Manage subnet.
So we're going to create a new subnet
just for our application gateway.
We give it a name called MyApplicationGateway.
It's something you can give it a name,
anything that you want
we're going to,
that's quite a big range.
So you see it includes 256 addresses by default.
From 10.0.1.0 to 10.0.1.255.
So we're going to leave everything with the defaults here
and say Add.
Now that that's created, we can go back
to the previous screen and we can choose
the new application gateway subnet.
Now we have a couple of IP addresses,
the VM and the load balancer.
We have to create a third one, I guess,
appgatewayip.
So we're going to create a pool here,
but we're going to leave it empty for now.
We'll add targets in a second.
Now, just like with a load balancer, standard load balancer,
we do need to have rules to travel traffic
from the frontend IP to our backend pool.
And like I said, this is a level seven load balancer.
And so this is going to understand,
it's going to understand that there are HTTP or HTTPS,
and there's going to be maybe basic rules
that we can add to it.
So I'm going to say priority 100,
we have to create a listener.
This is going to be listening on the frontend over IPv4
for port 80.
Remember, this is for applications.
And if we choose the backend target, we can choose pool2
and we can set up some settings.
So all traffic coming in port 80,
we're not going to have path specific traffic,
like I said, application gateway can support that,
and say Add.
Now, if we had multiple pools,
we could have this path based rules,
which we won't do.
Now we say Review and create.
So you'll see it's very similar to a load balancer,
but again, this operates at a different layer
of the OSI model.
And you're dealing with containers,
you're dealing with web apps, you're dealing with things
that can understand HTML, HTTP,
and not just IP address based traffic.
So I think we're going to leave that there.
If you want to add virtual machines
and add them to the backend pool,
you're certainly free to do that.
But this is the example of creating application gateway,
how similar it's to load balancer
and indeed the differences.


### 📺 Lesson: Network Watcher


Instructor: So in this video
we're gonna talk about a service in Azure
called Network Watcher
and the number of tools that we have available
to us under the Network Watcher service,
one including Connection Monitor.
Now to get here,
I'm searching in the Azure portal for Network Watcher,
and you'll see
that there's a service called Network Watcher.
When I go into it,
I will see usually one Network Watcher already set up for us
for each of our regions
and subscriptions that we've used in the past.
So you can see that I didn't use every region in the world.
I've used East US and East US-2, Central,
North Europe, West Europe, West US,
and Azure has along the way
created these Network Watchers for me.
So I can see that
for this particular subscription for East US region,
there's a Network Watcher available to me.
Now the tools for using Network Watcher are
actually at this level.
You don't go into the Network Watcher itself
because there's really nothing there.
What we want is at the Network Watcher service level,
and on the left you can see
there are a set of monitoring tools
and network diagnostic tools.
We saw the Connection Troubleshooter
in the section talking about network security groups
where we can test the connection
between virtual machines and other things.
Source being VM, VM scale set, Gateway or Bastion.
And we can try to figure out
why these Azure services can't connect
to something either on the internet
or within our Azure subscription.
But I'm more interested today
in something called Connection Monitor.
Now, Connection Monitor is part of the Azure Network Watcher
and it allows you to track network connectivity over time.
So unlike the Connection Troubleshooter,
which is a one-time test,
Connection Monitor gives you ongoing insights
into whether a VM or resource is reachable.
It can track latency, packet loss, and even alerts you
if a connection becomes unstable or unreachable.
So again, we've reached Connection Monitor
by finding Network Watcher and going under monitoring here.
And now we want to create a new monitor.
So I'm gonna click the Create button.
We're going to give it a name.
It's going to be again this subscription
and the East US region
because I have a VM and a network already there.
Now I go to the next tab called Test Groups.
Now in this case, maybe I want to test my virtual machine
and to see that it can connect
to the internet over port 443.
So I give it a name, and I say Add sources,
and I'm gonna choose the virtual machine that I had created.
If you don't have one, you can go ahead and create one.
And for the destination,
I'm going to go to an external address,
and we were testing bing.com.
And so we can test that.
And we can see what we've selected under external addresses
and say Add endpoints.
And under test configuration,
we can define what we want to test.
And so this is, let's call it test one,
and it's chosen as a default HTTP protocol.
Now we could choose the TCP protocol to port 80,
which is the same thing.
And how often do we want to test this?
Now 30 seconds seems a bit excessive,
especially to a site we don't own like Bing,
but maybe every five minutes,
we can run a ping to Bing using port 80.
And success threshold,
so do we have a a point at which we are okay,
90% worked, 50% worked,
what percentage would have to have failed
in order for us to alert?
So let's say that if 10% of these tests fail,
I want to be alerted,
and we saw that the round trip is under two milliseconds
in the connection test that we were doing before.
But let's say we're fine with up to 25.
We don't need to be so fast with bing.com.
Alright, now we are gonna get charged for this.
Obviously this is a resource,
and it it's gonna continually run.
If we didn't want to, we can disable this on creation,
but let's say Add Test Group.
Now it needs to use a log analytics workspace
and I'm just gonna pick the default log analytics workspace.
Do we wanna be notified
if this Connection Monitor discovers any failures?
We could set up an action group
to either email us or SMS us,
notify us in some way that this test didn't work.
So I'm not gonna create an alert.
I'm gonna say Review and Create,
and you'll see that it's about 30 cents per month
to set this test up.
I'm gonna say Create.
So that succeeded.
If we go back to Network Watcher under Connection Monitor,
we can see the monitor that we created.
Now so far this monitor is failing.
If you'll remember,
the test that we made is testing port 80,
which we know is going to fail.
If we update this to 443, and we update that,
update the test group and update the deployment,
then when we go back to Network Watcher,
we can refresh this.
What we'd expect to happen is that
even though the first one failed,
that the next one should succeed.
So we'll wait, I believe we set it two every five minutes.
So we'll wait for five minutes
and then the Connection Monitor will start to succeed.
So in this way,
we can have an ongoing check of the connectivity
between two sources in Microsoft Azure.


### 📺 Lesson: Network Diagnostic Logs


Instructor: Now moving on to diagnostic logs.
We already know that most resources
within Microsoft Azure have a diagnostic system
that collects metrics and data,
and feeds it into a log analytics workspace.
And you can use something like Azure Monitor to see reports
and to collect that stuff centrally.
So right now I can see diagnostic logs that lists me
all of my network interfaces
and network security groups on my entire account.
And I can see that diagnostics is not currently turned on.
So let's see.
We're gonna look at these one each.
Let's look at a network interface card.
If I click on diagnostics,
then you can see there's only one thing that it collects,
which are metrics.
And metrics I guess are bits and bytes
that are coming in over the network card.
So if I wanted to collect that,
I can say, give it a name, diag1
and send it to a, log in, Linux workspace,
and I'm gonna put it in the Northern Europe workspace.
I have a number of them, and hit save.
So now this network network interface card
is going to be collecting metrics.
This is obviously not a lot of information.
We're gonna see that when we
go into Azure monitor, what it collects.
We could also additionally store this in a storage account
stream it to an event hub,
or have some other third party solution
that will take this data and do something with it, right?
These are check boxes and it's an either or and situation.
If I go back to network watcher, diagnostic logs,
close that I guess, oops,
go back to network watcher,
go down to diagnostic logs, and now we can see
the network interface card has logs enabled.
Now let's look at the network security group.
Now, network security group gives off two things.
One is called an event and the other is the rule counter.
So let's add that.
So I'm going to collect everything, all logs,
send it to a log analytics workspace.
I'm gonna put this in Northern Europe,
and this is gonna be called diag2.
And again, I can collect that.
Now these are different bits of data.
This is relating to the the network security group.
The other one was relating to the network interface card.
And so the data is gonna be different,
the format's gonna be different, et cetera.
All right, so we can see here, now we have
enabled network interface card and network security group.
Now this information, again, if it's stored
in a security account, you could pull that into Power BI,
and you could actually run your own reports, right?
It's data like any other data.
This does not retroactive,
and so you do have to then start running traffic
into these things, whether there's a network interface card
or a net security group,
in order to see that.
And then there is a delay.
So let's go into Azure Monitor real quick,
this gauge on my menu,
or I can go into all services, analytics, is it?
Oh, monitor.
Monitor's its own service, and I can go into Azure Monitor.
Now Azure monitors a central dashboard
for all Azure services, or almost all Azure services.
And we can see that we're dealing with virtual machines,
storage accounts, containers,
SQL in preview, cosmos DB vaults.
We're concerned obviously with networks.
Now the problem of course is, there is a lag, okay?
So going into monitor, even if I was to
ping the public IP address, again,
attempt to load the web server up over the public internet,
which we know is denied 'cause we didn't yet add
a rule to allow that traffic through.
But we would expect that the NSG for this frontend server
would deny the traffic, and we'd be able to see that
in our Azure monitor here.
But there is a lag.
And so having done this in real time, I am not expecting
there to be a report that shows me that it was denied.
In the networks insights
we can see our network interface cards,
network security groups, the IPs are on in here,
and as well as the virtual networks.
So I'm gonna click on network security groups,
and I can see that there are two of them.
And right now, it's not able to tell me
about the resource health, so I can click into it.
That's not useful right now.
So again, this is not going to be useful
to me just right now, but I could set up
an alert when events happen within this group.
Another way to do this, is to go directly to the logs.
So we have the logs tab here.
We do have to choose a scope.
I'm gonna choose the resource group as the scope.
Unfortunately it doesn't like it when you choose things
with different resource types.
So I'm actually going to choose
both of the network security groups,
one and two as the scopes, okay?
I'm gonna close this and open the left menu here.
And so we can see that we are dealing with
network security groups, and there's going
to be some example queries that we're going to show you
like this is NSG Flow Log Search.
And I can double click that.
And this is gonna show me a query
that I could run against the data if there was yet data.
This language is called KQL or Kusto Query Language.
It's its own unique thing.
So it may not look exactly like anything you've seen before
but if you're gonna be spending a lot of time in diagnostics
and Azure Monitor, you're gonna want to learn KQL.
And so this is even telling me,
that as far as it knows the table
doesn't exist for this search,
but you can see the query and it has various complexities
in terms of being able to search for data.
So hopefully that gives you a little overview
of how resources in Azure can collect data
and log analytics, and you can either use the existing tools
within the monitor space to view that output,
or write your own queries or use
some of those pre-built queries to do that as well.

