---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "05"
title: "Module 05: Administer Azure Virtual Machines and VMSS"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 05: Administer Azure Virtual Machines and VMSS

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** VM Provisioning, OS & Data Disks, Networking, Resizing, Availability Sets & Zones, Azure Bastion, VMSS Manual & Autoscale, PowerShell VM Creation, Linux VM Web Server Lab  
**Line Range:** Lines 7612 – 10139 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


### 📺 Lesson: Create a Virtual Machine


Instructor: So in this section of the course,
we're actually gonna cover something
that I consider to be pretty exciting,
which are virtual machines.
As you can see from the requirements of the AZ-104 exam,
there's a big section on creating
and configuring virtual machines.
And so we're going to talk about that.
Virtual machines sizes, VM disks,
availability zones and sets, and things like that.
So in this video and in the videos that follow,
we're going to create our virtual machine.
I'm gonna go into the create a resource button,
and if we scroll down a little bit,
we can see virtual machine
near the bottom of the list of the popular resources.
You can also go under the compute category.
So I'm gonna say Create.
Now, we have a wizard type-interface with multiple tabs.
So in this video, we're gonna talk about the Basic tab,
and we'll just go to each subsequent video
to talk about each subsequent tab.
Like every resource, it has to belong to a subscription,
which is the base model
for who's gonna pay for this resource.
We're gonna create a new resource group for this.
Now, every virtual machine has to have a name.
It does not need to be globally unique
because we're going to have to come up
with DNS settings in another area.
So I can call this azsjdmyvm.
I do recommend like a naming convention
so that when you have multiple virtual machines
in your account, you roughly know what each one does.
So do think some in advance
in terms of your production environment at least
how you're gonna name things.
In terms of region, very similar to other resources.
You wanna put this resource
as close to the users of the resource as possible.
So if this VM serves a purpose
and has to be responsive to users,
then where those users are geographically located,
it makes sense to put the VM close to them,
as well as other related resources.
There is pricing implications.
So each region will have slightly different prices
for a virtual machine.
There's also VM families and sizes.
So Microsoft might have certain VMs
that are in one region that don't exist in the other.
So if you have a very specific need
for a very powerful machine,
you may wanna look up which regions it's available.
One of our first big decisions here
is this availability options.
Now, you'll see that availability zone
is selected by default.
Let's talk about the different options here.
So if this is a standalone VM,
then oftentimes no redundancy is required
because it's standalone.
There's not a second VM that it needs to work with.
What you are talking about in terms of availability
is how you place the other VMs.
So if you have, let's say you have five virtual machines
that all do the same job,
and any one of them can receive the request
and answer the request,
well then you wanna be conscious about physically
where those machines are being placed within Azure.
So the easiest to explain is an availability set.
An availability set basically focuses
on the points of failure.
So if there is a power supply that fails,
or there is a particular rack that fails,
you don't want all of your VMs to be placed
so close together that a single failure
is going to affect them all.
So this is in terms of unplanned failures, for instance.
The other types of failure are planned failures.
When Microsoft is doing updates to their Azure services,
they're gonna do them on a rolling basis,
and you don't want all of your VMs
to be placed in the same update
so that they're all taken down
for new Azure software to be rolled out at the same time.
So marking multiple VMs as part of the same availability set
allows Microsoft to know,
oh, we have to keep some of these running at the same time
through planned or unplanned outages.
Availability zone is sort of a step above
in terms of availability.
It allows you to choose data centers.
So let's say in the East US region,
you get up to three buildings
that you can deploy your VMs into
and that protects you against a single
entire building getting offline
if the power goes out or the internet goes out.
Hopefully the other buildings in the zone are not affected.
So that's a higher level of availability.
VM scale sets we're gonna talk about elsewhere
in this course.
So since this is a standalone VM, I'm just gonna leave this
as no infrastructure redundancy required.
Now, under security type,
we have this trusted launch virtual machine set
to be the default.
Now, a trusted launch virtual machine
is an enhanced VM configuration designed around security,
which will protect against certain threats like rootkits,
bootkits, and other firmware-level malware.
So this is pretty advanced stuff
in terms of protecting a machine from being booted
in something that's been physically compromised.
We're just gonna choose the standard set,
but the default is trusted.
And if you can deal with gen two virtual machines,
that's fine as well.
Confidential virtual machines
is actually a specialty product,
which is basically confidentially and integrity guaranteed,
it's a hardware solution to make sure
that whatever workloads you're running in them
cannot be spied upon.
We don't need that level of security.
I'm just gonna choose the standard.
Our next big decision is around the image.
So one of the good things about the cloud
is you can choose from hundreds and hundreds
of available images that you can launch
into a virtual machine.
So if we're just looking at the services
that Microsoft provides,
then we can say publisher type Microsoft.
And you can see there's 653 operating system options.
Some of these options include software.
So you can have SQL Server virtual machine
on running on top of Windows Server,
and Visual Studio Dev Box and things like that.
They have desktop operating systems like Windows 11.
So you have lots of different options.
And if you don't restrict yourself
to only the Microsoft options
and you go to the third parties,
you can get, again, 20,000 different options
in terms of other publishers,
like directly from Canonical, Oracle, Red Hat,
these are publishing their own virtual machines
that you can choose from.
So I'm just gonna choose Windows Server 2019
just to keep with it.
Now, depending on the image you choose,
you can choose from different hardware.
Intel is the default here, and I'm just gonna keep with it.
Spot instances are a way of saving money.
They are instances that are available
because no one else is using them,
but as soon as someone comes along
and wants to pay full price, you're gonna get booted.
So this is really low priority workloads,
it's a discounted rate,
but you're gonna be at some point booted off
when someone else is coming along that needs it.
Next big decision is this size,
and with virtual machines,
there's a number of prepackaged sizes,
literally 1,000 of them that you can choose from.
And they all have names that are,
you know, letters and numbers, version numbers together.
But you start off by saying,
what is the purpose of my workload?
Is it just a general purpose? Do I need high memory?
This one is for vector processing for AI.
Do I need, you know, high CPU and low memory?
There's various combinations,
but general purpose is sort of where it's at.
And you'll see over time, Microsoft improves the hardware
and it goes V2, V3, V4, V5, et cetera.
The B Series is great for testing.
So we'll start off with the B Series
just for testing purposes.
We can see, you can choose by number of CPUs,
two or four in this case,
the amount of RAM, eight or 16,
external disks, we'll talk about in this course.
And if you scroll over it, you'll see pricing,
and pricing is subject to change
and it's in your local currency.
So I'm just gonna choose this B2as option,
and I'm gonna say Select.
Now, hibernation is a relatively new feature.
It allows you to pause a virtual machine
by saving its memory and your system state to disk,
and then you can resume it exactly where you left off.
So you shut down the VM in a state
that you can restart it with memory intact,
and it allows you to save money
because you're paying for the virtual machine by the second.
And if it's not running, you're not paying by the second,
you're just paying for storage.
So hibernation is an option.
As a Windows machine,
you have to give it a user ID and password
as a Windows login.
And on this Basics tab,
we'll get the first inclination about networking.
We're gonna get this question again later in this thing,
but do you want any inbound public ports?
This is a security risk, of course,
if you have allowing traffic from the public internet.
If you wanna turn that off, you can see none.
But if you do want this to be a web server,
you may have to turn on the HTTP ports.
If you wanna be able to remote desktop into it,
turn on the RDP port.
And for Linux machines, SSH.
So those are sort of the options.
The last option on the screen is licensing.
And this is an interesting benefit.
If you are a Microsoft Enterprise customer
and you have a plan with Microsoft that you pay for,
it might include some Azure virtual machines
with your license.
And so if you're paying for it,
you might as well use those virtual machines,
and that's called Azure Hybrid Benefit.
We can see, I've decided to go with the B2ms VM here,
and that's marked as $90 a month.
And if I choose to reuse my existing license,
then that drops to $82 a month.
So I'm saving $8 a month,
around 10% off of this VM
just by reusing a license I'm already paying for.
So I don't have that,
I'm not going to use that benefit.
But if you have it, it's worth checking out
that if you've used up all your licenses
to save a little bit of money.
Now, they say up to 49%.
That's obviously gonna be off of the bigger VMs.
The more CPUs you have and things like that,
you're going to be able to save more
as it makes up your cost
in terms of your Windows licensing.
Anyways, and that's enough for this video.
In the next video, we're gonna talk about external disks.


### 📺 Lesson: Azure VM Disk Options


Lecturer: All right, in this video,
we're gonna talk about virtual machine disks.
We're in the Creative virtual machine interface
on the Disks tab.
And we have a number of options
relating to the virtual hard drive
that is attached to this VM.
Not only the operating system disk and the temporary disk,
but any additional data disk that we can optionally add.
So right at the top of the screen,
it's warning us that the virtual machine that we've chosen,
which is a B2ms, is not as fast
as the temporary disk that we're gonna be using.
So, the current virtual machine
supports 23 megabits per second,
and the disk is a hundred megabits per second.
So we've chosen a smaller, less powerful VM,
but this is only for testing purposes.
So as you can see on the screen,
it says VMs have one OS disk and one temporary disks.
So, every VM is gonna come with two disks, C and D.
You can also attach other disks for your usage,
and that will be down here.
So, the first decision we're making
has to do with encryption.
So, all VM disks are encrypted automatically.
So, it's just gonna be done
by automatically at rest.
So, it's transparent data encryption.
So as the VM writes its data to disk,
it's encrypted and stored encrypted.
Now, we also have this option for encryption at host.
Now, encryption at host is basically using,
the operating system has the feature of encrypting it
before it attempts to write to the virtual disk.
And then, so you're basically getting double encryption.
So, do we want the Windows to also try to encrypt
the data before it writes it?
We're gonna not enable this for this testing purpose,
but if you really are concerned about encryption,
you can certainly do that.
So, we'll start off with the operating system disk.
This is obviously the C drive, right?
So, this is the, comes with the image is 127 gigabytes.
Now, we can choose a larger one,
128, 256, 512, if we think we're going to need it.
Now, I will say that it's not good practice
to have a virtual machine writing anything
to its local disk.
Virtual machines almost by their nature
can be destroyed and recreated.
And so, writing stuff to the local disk
is just asking for a little bit of trouble.
You should better to be used external data disk
or even Azure file shares or databases
if you need to store stuff.
Premium SSD is the default in terms of storage.
It is a high performance, low latency,
good for production workloads.
You can downgrade to the Standard SSD,
which is good for web servers.
Anything that doesn't really use the disk a lot
and dev test.
You can even downgrade further
to the traditional magnetic hard disk drive.
And so, those are your sort of options.
Let's stick with the Premium. That's the recommended.
What do you want to happen to this VM once you delete?
What do you want to happen to the virtual hard disk
once you delete the virtual machine?
Deleting it is by default.
We're getting similar questions
in terms of the way the security is managed.
Microsoft managed key is the default.
If we wanted to have customer-managed key,
we would have to use a disk.
We'd have to create a disk encryption set,
and then we can choose it to work with this VM
in terms of encrypting using that key.
But we don't have one, so we can't choose it.
Now, only certain virtual machines
support what is called ultra disks, okay?
So it is, in this fact,
it is supported based on availability zoned,
which we have not selected for B2ms.
Ultra disks are for high throughput,
mission critical workloads, like large databases.
So if your machine is gonna be pounding,
the disk reads and writes repeatedly,
you may want to go beyond Premium SSD into Ultra.
Of course, that costs more money as well
and subject to the limitations of your image type,
as well as the location.
So finally at the bottom, we get to the external data disk.
So, you can add or configure additional data disk
for your virtual machine
or if you have them already, you can attach them.
So, what this allows you to do is have a DEF drive.
You can attach a additional disk.
When we chose this B2ms image,
it came with a number of disks that it supported.
So if I go back to this selection
and we look at B2ms,
it supports up to four additional disks.
So the limitation on the number
of, you know, EFG type of drives
is going to be based on the image selection.
If that's not enough for me,
I would have to choose a bigger selection.
All right.
So, I'm not going to attach
a disk right now.
We can do that additionally in the the future.
One of the advantages of attaching a disk
or creating and attaching a disk
is that it's independent of the VM.
It's not gonna get deleted when the VM is deleted.
And you can detach a disk to from a VM
and attach it to a different VM.
So, let's say you need to migrate a bunch of data.
You can create a disk, attach it to a VM.
Have the VM collect the data,
put it onto the external disk,
and then detach that disk.
Attach it to a different VM,
and you can then process the data from there.
So, disk are basically separate entities
that are attached and detached from virtual machines.
Well, that's what we'll talk about in terms of disks.
In the next video, we'll talk about something important,
which is networking.


### 📺 Lesson: Azure VM Networking Options


So in this video, we're going to talk about one of the more important aspects of virtual machines,
which is virtual networks.
We are on the networking tab of the virtual machine interface in the portal.
Now every virtual machine must be attached to a virtual network.
There is no concept of a virtual machine that does not have at least one virtual network.
So as we're creating it, we must create one.
Now the two options you have are to create a brand new one or to attach it to an existing virtual network.
So as I look at this drop down under virtual Network, I can choose one of the ones that I've created
in the past and I won't have to create a new one.
But by this bracket, new it signifying to me that it's going to try to create a new VNet for me.
I'm going to hit the Create New button just to see what it's doing by creating this virtual network.
So all virtual networks have a name, and the automatically given name is the VM name with a hyphen
and VNet.
The virtual network itself has a size, and that size is expressed in what is called Cidr notation.
The default given here is slash 16, so it's tried to find a free open unused address range.
In my case, I must have A10 .0.0.0 that is being used by another network.
So 10.1.0.0 is the logical next range.
The slash 16 is quite a large network.
Uh, as you can see, it's reserving 10.10 0 to 1 .1255.255, which is a total of 65,000 plus IP addresses.
That's an absolutely massive, almost unnecessarily large VNet.
But because it's in the ten dot range, these are this is a private IP address range and there's no
chance of overlapping with another customer, another user.
I can create as many of these as I want because they do not exist on the open internet at all.
It's a it's a reserved range.
The slash 16.
Since it's covering these two blocks of your IP address, it's called a C block in old notation.
So this is quite a large range.
Uh IP virtual networks can have multiple ranges.
So if I wanted to reserve the um 10.2 range as well I can reserve both ranges for this one virtual network.
And you can see that's being reserved for me.
Now another part of a virtual network is called a subnet.
Now a subnet is basically segmentation of the VNet.
By default, all Vnets are given the subnet called default.
By default and you can see it's created a smaller range slash 24.
The bigger the number, the smaller the range.
So this is only a D block which is 10.1.0. 0 to 1 2.1.0.255.
In this case or 256 addresses.
So this subnet has room for multiple other subnets.
If I wanted to create the front end I can do that.
If I wanted to create the back end or the middle tier.
But I'll put back end.
I can also do that.
Okay.
So we can create as many subnets as we need within the range of the whole virtual network.
If in the future you run out of space, you can always resize these.
It's pretty easy to do.
So I'm going to click okay.
So we can see the virtual network and the subnet being given to us.
I'm going to put this first VM into the default.
Now another option being offered to us is a public IP address.
So hopefully majority of your VMs will not have a public IP address.
Not only is it largely unnecessary, it's not recommended.
And it costs money as well to have many multiple IP addresses.
But in the first time we're creating this VM, it's offering it to us.
We're going to need a public IP address for a remote desktop protocol or for SSH.
So there's a purpose for it in this example.
So the network security group is an access control list.
That can is a list of rules of how traffic has to behave coming inbound to the network and leaving the
network.
You can certainly not have one, in which case all traffic will be allowed into the network, but definitely
recommend having one, because that's sort of the most basic level of security blocking ports and such.
Now, I said before on the basics tab that I'm going to allow certain ports in.
So this is just a second chance at setting those settings.
Now, similar to your OS disk, you have the option of deleting the public IP and the network interface
card when the VM is deleted.
Okay.
There's this option called Accelerated Networking.
It says the selected VM size does not support accelerated networking.
Accelerated networking improves throughput and lowers latency.
This is great when you have a lot of powerful computers that need to talk to each other often.
So if you have like a cluster of 64 CPU machines, and they're doing some intense batch processing of
data, and they need to talk to each other frequently.
Then accelerate.
Networking is great for having VMs communicating as quickly as possible, otherwise it's not worth it
and you should just use regular networking.
The other option here given is load balancing.
And Microsoft does have two different load balancers.
We're going to talk about that in a separate video.
The Azure Load balancer and Application Gateway.
They have different purposes.
They run at different network levels.
So application gateway is a level seven application level load balancer.
And the Azure load balancer is a level four load balancer.
We'll talk what that means in a future video.
So I'm not going to because it's a standalone virtual machine.
We don't need a load balancer.
All right.
Well that's the networking page coming up.
We're going to talk about the next set of options for creating a virtual machine.


### 📺 Lesson: Azure VM Management and Advanced Options


Instructor: All right, so onto the Management tab.
We are looking at various options
for setting up this virtual machine.
First at the top is Defender for Cloud,
but there's not really any option here.
There is a free version of Defender for Cloud,
and so your virtual machine is gonna be covered
by this security management service,
and you can optionally pay extra
to have this more actively managed
and you'll deal with that
when you're talking about Defender.
If your virtual machine needs to access other resources
and you wanna use role-based access control
and Entra ID to manage those permissions,
we could create a system assigned managed identity.
This allows you to assign permissions.
So for instance, with the storage account,
if you're using Entra ID
as your permissioning system for storage,
well, then you can get an identity
for your virtual machine
and assign the virtual machine permissions
to the storage account.
Relative new option here
is to actually log in using Entra ID.
We've had to provide a Windows user
and password in the earlier screens,
but if we want to use Entra ID as the login,
we would have to enable that,
and then have a particular role
in order to be able to log in using Entra ID.
When you're playing around with virtual machines,
auto-shutdown is pretty helpful.
You could have it running,
it's gonna cost you by time while it's running
and then when you're no longer using it at night,
it shuts down automatically in this particular case.
And then the next morning when you're ready to use it again,
you just manually start a backup
and this is gonna save you money.
Obviously if you're using a free account
or you're using an extremely cheap server,
it's not gonna matter much.
But if you're trying to save money,
having auto-shutdown enabled is a smart option.
We haven't talked about backing up VMs yet.
We will in the future,
but if we want to start to set that process up here,
we could enable a virtual machine backup.
Another type of emergency service
is called Azure Site Recovery.
And what this does is it makes your virtual machine
able to be recovered in a different region.
So let's say you deployed this to East US
and for whatever reason East US is suffering an outage.
Well, if you had Site Recovery set up,
within seconds you could have a virtual machine
running in West US, for instance,
and get your workloads back running again.
So Disaster Recovery or Azure Site Recovery
is sort of the ability to failover
from one region to another.
It's not automatic right away,
but it's very easy to do as opposed to restoring a backup
and all of the hassle around that.
Now, getting operating system updates like Windows Updates,
you can enable various options around that.
One has to do with automatic updates.
So in turning on the Windows Update
on the operating system itself,
or you could enable manual updates
so that you are more directly responsible
for updating a server.
Maybe you want something like that for production workloads.
Let's talk about monitoring.
Now, Microsoft in recent years
has created a set of recommended alerts.
And so if there is some events happening,
you can have it basically email you
or send you a mobile app notification.
You can see there are, in this case,
seven alert rules that are going to be created
automatically with this checkbox:
percentage of CPU, available memory,
data disk and OS disk consumed percentage of operations,
networking, these are the basic
communication features and availability.
And remember, there is a cost for these.
And so you're looking at 95 cents a month roughly
for these seven alerts if you were to turn them on.
Now I oftentimes when Windows for instance starts up,
it's gonna work 99.999% of the time.
The one time it fails to boot obviously will be the time
when you should have had some type of logging.
So boot diagnostics is basically going to track
boot failures for custom or platform images.
I always turn this off
because it's taking up storage, costing me money,
and I'm never ever going to read the boot logs
to try to figure out
why a particular boot image won't start.
The other option is diagnostics.
Now we're gonna get into diagnostics in this course,
which is Azure Monitor and tracking performance of VMs,
but we can turn that on right from here.
Finally, application health monitoring,
this actually is for the scale set specifically,
we are gonna talk about virtual machine skill sets
in a later video.
This is just a standalone virtual machine for now.
On the Advanced tab,
we have the ability to set up extensions.
So let's say you want to have some type
of agent installed and running.
So the AMD GPU driver,
we don't have a GPU on this machine,
but if we did, we might want that.
Application Insights Agent,
Azure AD Windows login, that's an extension.
So if we wanted to have these third-party
and Microsoft extensions installed
as we're creating the virtual machine,
we can do that.
We can also do that after it's been created.
We also, now VM is gonna start,
it's just gonna be the operating system and the disk.
There's not gonna be any code there.
So VM applications allow us to create packages
of application files
and that we can install and uninstall
using this particular extension.
So if we wanted to bundle our apps together,
now we don't have any to demonstrate
'cause we haven't done that yet.
But if we wanted to bundle our apps as VM applications,
that could be installed on provisioning.
We also have the ability to pass
some type of custom data.
So if we had a VM name or some kind of region
or something we needed to pass in into the startup,
then during provisioning we could do that.
Another option is with this user data.
So it says pass a script,
configuration file or other data
that will be accessible to your applications
through the lifetime of the VM.
This is for the provisioning
and this is for the lifetime in terms of passing in things.
Now we're not using NVMe,
so in this particular B2ms,
and so this is not gonna be really relevant,
but if we wanted to have remote disk storage performance,
we could install that here.
VMs, we do have the option
of having dedicated hosts within Azure.
So if we're willing to pay for a physical machine
that's entirely ours
and no other Azure customers get to share it,
we could deploy this VM to a host group.
If you know you're gonna need a VM in the future
and you are afraid that a particular region
is gonna not have a VM available to you,
you can get the reservation
and Microsoft will reserve it for you
and they'll charge you for it.
And then when you're ready to deploy the VM,
it goes into your capacity reservation.
Proximity placement groups,
it's sort of like the opposite of an availability set.
This is forcing Azure resources
to be physically closer together.
It should reduce latency
by millionths of a second or what have you.
But the closer your servers are,
and if they do need to talk to each other,
the faster that's going to be.
We've talked about resource tags previously
in terms of tracking
for cost management and things like that.
We're gonna move on to the last step,
which is Review + create.
So at the end of this process,
it's running final validation.
And when it does complete
and I hit the Create button,
I'm going to have a standard B2ms server,
I'm gonna start paying for it immediately.
And then I can start setting that up
and doing what I need with it.
So I know this has been a long process
going through this line by line and step by step,
thank you for sticking that out.
I'm gonna hit the Create button
and then in the next video
we can take a look at what we've created,
how we're going to see that it's working,
remote desktop, Intuit, et cetera,
so come back for that.


### 📺 Lesson: Connect to a Virtual Machine


Instructor: So the VM was created.
Now we can go into the deployment details
and we can just see how long it actually took to create.
So we've got the network security group, IP address,
virtual network.
This VM 300 is the network interface card,
and this is the VM.
So if we go into operation details,
we can see that it took only 27 seconds
to create this virtual machine.
Now the reason why it's so quick actually
is that Microsoft has hundreds of virtual machines
of all the different sizes standing by
and they simply just have to rename it
and restart the machine in order to provide it to you.
Pretty clever way to get deployments
down to just seconds.
So if I say go to resource,
first thing I notice is the machine is stopped.
So my bet is that the auto shutdown,
this is past seven in the evening.
We created this at 6:30.
And so the auto shutdown actually kicked in.
So I'm going to hit start, but the machine did get created.
It is a standard B2ms as we wanted.
You'll see that a IP address has been assigned
and it's on a network, etcetera.
Now I can't really do anything with this IP address
until I install some software such as IIS
or web application.
We can connect to RDP and we'll do that in this video.
Now let's check something real quick.
We go into network settings
and we're gonna talk about the network security groups.
But the first thing I just wanna make sure
is that the traffic for Port 84, 443
and RDP Port 3389 is being allowed
through from any source to this VM.
So go back to overview.
And the way I'm gonna connect to this
through RDP is there's a connect button at the top
and I'm gonna click connect.
What this is gonna do is it's gonna validate
that I can connect.
There's the public IP address for this machine.
If I wanted to, I can click this check access to make sure
that my computer can access this IP over this port.
That there's nothing blocking it.
And it says accessible.
All right, so the way I'm gonna connect,
the most common way to connect here is through RDP.
That means downloading RDP file
and then being able to connect to it through RDP.
So I'm gonna download this.
If I click it, obviously I have to authorize it.
Now you'll remember I created a user, this user,
and I do have to provide
the password.
I have to accept that there's a certificate
and it's a self-signed certificate.
So it's, I do have to say that I created it
and now we're using RDP protocol to connect to this machine.
Now this is the first time I'm connecting,
so it is creating a Windows desktop profile for me
going through those steps for the first time.
So this is the first boot up.
I can turn off network discovery.
And right now this machine doesn't have any role.
So it's just a fresh install of,
I believe we chose
Windows Server
2019 if I recall.
And so it's just a fresh install
and it's up to us to add software,
add things,
to it to make it do something.
Now I'm just going to, real quick,
turn this into a web server.
So I choose web server from Windows Features.
And it doesn't really matter if I, what features I install.
'Cause I just want the default features
and I can say install.
So now I'm turning this server into a web server.
We'll let that go.
So it's installing the web server,
but I just went to local host in the web browser
and the basics
of the server itself is already installed and running.
It's now adding some additional features here
that feature installation succeeded.
So we do have a web server running on this machine
through local host here.
Now if I go back to the Azure portal, grab the IP address,
paste the IP address into a web browser on my local machine,
I can also access the IAS homepage.
So we have created a VM
and as we saw, it's gonna cost us not too much,
about $80 a month,
and we are able to RDP into it,
install whatever software we wish,
and I installed a web server
and we are now successfully connected to the web server.
So we have successfully created a VM
and we can use it for whatever it is that we wish in terms
of using it for a productive workload.


### 📺 Lesson: VM Availability


Scott: Now, when we were creating the virtual machine,
we came across this availability options option
on the basics tab of the virtual machine creation process,
and we ended up choosing no redundancy required
because it was gonna be a standalone virtual machine.
There was never going to be a second or third
or additional virtual machine to stand beside it
that is identical, so there's just no availability options.
It's going to be no redundancy required,
but let's talk about the other three options
in this dropdown.
The first one I wanna talk about is availability set.
Now, availability set, the purpose of it is to protect
against hardware failures within a single data center.
There are two primarily types of failures
that we're trying to protect against.
One is the unintended failures,
and these are called fault domains.
I'm gonna click create new under the availability set here.
So fault domains, the easy way to remember this
is the word fault, which means that something failed,
so it's either the rack or the power supply
or the network switch.
Something relating to this computer failed,
and when you have, I'm gonna call this avail one,
when you have two or more VMs in availability set,
then Microsoft Azure is able to distribute those
across different racks in the same data center.
This way, the most common types of failures
are protected against, and let's say you have two VMs.
Well, in the normal situation, neither of them will go down,
but in the abnormal situation,
only one of them will go down,
and the other one will still be running.
So we have fault domains.
We only have three options,
so we have one fault domain, two, or three.
This is really how many different physical racks
it's gonna be distributed against,
and so in this particular case, with two,
that means two different racks.
Even if you have four or eight or 12 VMs,
they're all gonna be distributed like six and six
on the two different racks.
Update domains is the other thing it protects against,
which are planned maintenance,
so when Microsoft is rolling out updates to its software,
it does it by update domain.
Now, there are, I believe, 20 total update domains,
and so you can imagine Microsoft is just rolling them out,
first to the first one, second to the second one,
third to the third one, et cetera.
So let's say you have five VMs and five update domains.
That means, at any one time, only one of your VMs
will be disturbed by this update.
If you have 10 VMs and five update domains,
that means that two of your VMs will be disturbed
by these updates at a time.
So that's availability set.
Again, protects against hardware failures
within a single data center,
and it's within a single availability zone or single region.
There's no scaling involved.
It's not gonna add more VMs when the demand is required.
It's not gonna remove VMs when you don't need them anymore.
Those are a scale set.
This is just distributing the VMs
across different devices to protect against planned
and unplanned maintenance and failures.
The second option for availability
is called an availability zone,
and this is where you are physically separating your VMs
into different buildings or data centers.
The purpose of this is to protect
against the entire data center failing,
so if I say self-selected zone, you can see I can deploy VMs
into one, two, and/or three.
If I choose all three,
then I'm gonna get three virtual machines to be created.
If I choose just one,
we know exactly which building it's going into,
which is called zone one.
Each of these zones has independent power,
cooling, networking, so even a connection to the ISP
is independent for each of these.
There's nothing shared between them.
It is stronger isolation than availability sets,
so this is even less likely
that your VMs will all go down together.
Now, the third option is the virtual machine scale set.
So this is like an availability zone,
but you also get scaling in addition,
so when you need more servers, more servers get added.
When you don't need as many servers,
you can have servers removed.
So this works either single zone,
or you can deploy this across zones.
It automatically handles the creation of the additional VMs,
it automatically handles load balancing,
there's built-in health monitoring,
and if something was to happen to one of your VMs,
it will replace it.
So this is used when you need auto-scaling and redundancy,
and again, these are for stateless workloads,
so when you're adding VMs and you're removing VMs,
you don't want a customer to be impacted.
You don't want somebody to be in the middle of something,
and then the server they were working on disappears,
so it has to be stateless.
So availability sets, availability zones,
and scale sets protects your application
against both planned and unplanned outages
through different methods.


### 📺 Lesson: Resizing an Azure VM


Instructor: Now, going back to the VM that we created,
one of the great advantages of using cloud computing
virtual machines is the ability to resize them.
So unlike buying a physical computer,
you're sort of stuck with how many VMs
and how much memory you have without a lot of effort
to change it.
But with a cloud-based virtual machine,
you simply go into the machine,
go down to Availability and scale sub menu,
and click Size.
You'll see that we did choose the B2MS machine
with two CPUs, eight gigabytes of RAM, up to four data disks
and 16 gigs of local storage for $90 a month.
If we realize later that this is a bit slow,
we need maybe four CPUs and not just two,
we simply go into the Size, we choose the B4,
and you'll see the price is actually almost exactly double,
within a few cents of being double,
which is typically how VMs are.
If you go up to 32 gigabytes of RAM,
it's roughly quadruple the original price.
So if I go B4MS, and I say Resize,
this is a disruptive event.
So if the virtual machine is currently running,
changing its size will cause it to be restarted.
But the everything that I've installed remains installed.
The virtual hard disc C and D drives don't get wiped.
All I'm doing is I'm getting a larger instance here.
So I've now hit Resize and it's now going off,
and it says it's resizing the virtual machine.
And not very long at all, it actually gets done.
So if I go to, back to the Overview here,
we can see that it is now a B4MS machine.
So resizing a VM in Azure, not very difficult at all.
Now, of course, we can go back down,
from B4 back down to B2.
You may notice that there are only 269 VMs being offered
when we had more than 1,000 on creation.
So there are some limitations
that are going to be imposed once a VM has been created
and one of them is going to be that the VM
that we've created is a gen two VM
and we will not be able to go back down to a gen one image.
So it's really a limitation on the fact that we've created
a VM that is more advanced
than the previous hardware supports.
There is quota issues.
So for instance, I'm gonna need to get for a 96 CPU,
I need to request quota for that
and I've chosen a premium disc
and these non-premium disc options
are not gonna be available to me.
So there are some limitations,
but generally I still have hundreds of options
in terms of switching from the,
even from the B-series up to the D-series
for a production level workload.


### 📺 Lesson: Azure VM Additional Disks


Instructor: Now, hopefully you recall,
when we chose the size to create the virtual machine,
originally B2ms, now upgraded to B4ms.
That not only are we choosing for CPUs and RAM,
we have a column here called Data Disks.
And originally had up to four data disks,
and now we can have up to eight.
I will also point out
that the operations per second has been upgraded
as well as the size of the temporary storage.
Here is the remote desktop
that I've logged into my server here,
and we can see that the C drive is 126 gigabytes
and the temporary storage 32 gigabytes.
So that lines up with the temporary storage indicated here.
But what if we actually really wanted to store some data?
We shouldn't store it on the Windows C drive
or in the temporary drive.
There should be a E, F, G type drive
that we can store things to.
Those are gonna be called data disks.
So what I'm gonna do is I'm going to disconnect from this.
And I'm going to add a data disk.
We have, again, up to eight
that we can add to this particular size.
That is under the Settings option.
You'll see the very first item is Disks.
And here's our OS disc, 127 gigabytes.
We saw that.
Now we're gonna want to create a data disk.
So I'm gonna click this Create button.
Now, what it's done is it's given me,
it's not the traditional wizard style,
it's given me a bunch of text boxes
and dropdown boxes that I can fill out
in terms of creating this data disk.
So I can give the disk a name.
We saw the C drive is named Windows,
so I'm gonna call this my Data Drive.
Oh, there's no spacing allowed.
We're gonna continue on with the Premium SSD.
We could downgrade to Standard SSD or HDD
if that's what we wanted,
but we'll just keep the premium one.
Now, how much do we want in terms of a data disk?
It starts off with a relatively puny four gigabytes.
Let's say we wanted 128 gigabytes for our data disk.
Actually, the more gigabytes that we request,
the faster we have transactions.
So our operations per second and our max throughput
in terms of megabytes per second goes up
the more data that we request.
So 96 or 128 gets us a certain criteria, okay?
These things are encrypted.
We're gonna keep with the Microsoft-managed key.
And we could have read caching or read/write caching.
Let's leave it as the default.
And we will say Apply.
So now it's creating this data disk for me.
Of course there's a charge for this.
And it's going to attach this drive to this machine.
Just to show you, we go to the Pricing page,
and Premium SSD disks with LRS redundancy
is actually the same price as Azure Storage account,
which is 1.8 cents per gigabyte per month.
And we can see this is SSD LRS,
so we're gonna be paying about two cents per gigabyte,
which is about $2.50 per month.
Not bad, huh?
So this data disk has been added to the machine.
Let's log back into the machine and see it.
Ah, we can't see it.
So what we need to do
is actually mount this drive to this machine.
If we open up Disk Management,
which is the traditional application
within Windows Servers to manage it,
immediately, it wants us to initialize the disk.
So we have to select Disk 2.
We have to decide, it's not gonna be a boot disk,
so it's just gonna be a regular partition table.
I can say OK.
And if we scroll down,
we can see that it hasn't been allocated yet.
We haven't put this into a drive.
So if we say New Simple Volume,
there's a wizard for that.
We're gonna take all of the space.
And which drive letter do we want?
I'm gonna put Drive E.
Format it.
And say Finish.
And almost immediately a Drive E shows up
at 127 gigabytes of free space.
So we can add, again,
up to eight data disks to this particular size of VM.
And this is where we could store our data.
And as I said previously,
when you are done with it, you can detach this,
so there's a Detach button,
and you can attach this to another VM.
So this is a way of transferring data between VMs,
if that's what you wish to do.
So Azure data disks,
the recommended way to store data in virtual machines
as opposed to storing it in the temporary storage
or the C drive of the machine,
which is not recommended because it can be lost.


### 📺 Lesson: Azure Bastion Service


-: So far we've been using what is called the RDP service,
Remote Desktop Protocol to connect to RVM.
We've seen here on the network settings
there's this orange alert symbol next to RDP
and that signifies that
this is usually an unsafe practice long term.
You do not necessarily want to have
your administrative ports open to anyone
from any IP address on the internet,
at least even having access to try to log into your device.
So long term should be eliminated completely.
It's for short-term administration purposes only.
At a very minimum, you should probably put
some kind of filter on here
so that only specific devices from specific sources
could use it.
But Microsoft actually provides a safer alternative
to RDP and SSH called Bastion.
So the Azure Bastion service
is fully managed platform as a service
that allows you secure RDP and SSH access
to your virtual machines through the Azure portal.
This means there's no public IP address required,
so you're gonna shut down this locked door
that faces the street
and you don't have to have port 3389,
or port 22 open either.
So more protection for public-facing virtual machines.
So we're gonna go into the creative resource
and we're gonna look for Bastion.
So the Bastion service is going to be deployed
to our virtual network
and it will cover in the simplest form
all of those machines on that network.
So I'm gonna create a Bastion service,
pick the subscription and the group as usual,
give it a name, I'm gonna call it a Bastion test.
Pick a region.
We still have the same region
and availability zone choices as before.
Now Bastion has several tiers
and when if I pull in the pricing for Bastion
we can see that there's a free developer tier.
So Microsoft obviously wants to encourage the use of Bastion
for these developer workloads
at least so that you're reducing public IP address usage
and reducing this exposure.
There's a basic and a standard levels
at 19 and 29 cents per hour.
And then there's obviously going up to the premium tier.
You're also like a lot of services gonna pay for traffic
that travels across that device.
So if we switch over to the documentation,
we can see that RDP and SSH is supported.
That is an HTML5 web-based client.
So you don't even need that software anymore.
And it's a private IP address,
so there's no longer for the public IP address.
You don't have to open the parts in NSG, which we just saw.
You don't have to have your own VM.
A lot of people would have their own,
what they used to call a jump box
for hosting these types of devices.
We don't have to do that anymore.
And you get close the ports of your VM as well.
So we've got our developer basic standard premium SKUs
and we can see that you're getting a lot of these benefits
no matter which SKU you choose.
Using RDP on Linux requires standard or above,
using SSH on Windows standard or above.
Being able to customize which port it's coming in on
is a standard or above.
We can see scaling doing file transfers over Bastion,
standard or above.
And finally, a session recording and private-only deployment
is a premium tier service.
All right, I'll create a basic tier service.
We don't need multiple instances above the two.
I'm gonna deploy this to my VM
that I've been playing with this time.
Now Bastion requires its own subnet
called Azure Bastion subnet,
actually has to have a specific name,
so we haven't created it yet.
Remember we have default frontend and backend.
So we need to create a new subnet specifically for Bastion.
So we create a new subnet
and we're gonna call it a,
we're gonna call it a Bastion, it gives it a name.
Now, since Bastion requires its own subnet,
we're going to have to choose a size for it.
We don't need that many IP addresses.
We just really need the one.
So we'll choose the smallest one,
which in this case is a /26.
Provides 64 IP addresses,
and we're just gonna say add.
So now we have a Bastion subnet.
We can now go back to the creation
and it's chosen automatically.
Now the Bastion itself needs to use a public IP address.
Obviously, if you're going to use Bastion
over the public internet.
So, we create a new address for that.
We could reuse the existing one
that is currently pointing to the VM,
but then we'd have to detach it and stuff like that.
So we'll just leave that.
We are going to, all of these things are grayed out.
I guess we're in the basic plan
so we don't have session recording
and all of these features.
So we'll skip that,
and we'll say "Create."
Now this takes a bit of time.
I'm gonna pause the video and when we come back
we will be able to connect to our VM
using the web browser over the private IP address.
All right, so that did take a few minutes to deploy.
If we go into the deployment details,
look at operation details,
we can see that it just took around 10 minutes to complete,
which is normal.
I'm gonna click on Go to Resource.
And so the easiest thing we can do to test from here
is to connect to our virtual machine through this bastion.
So I'm actually gonna switch over
to the virtual machine itself.
That we were previously connecting with RDP
and under the Connect option,
I'm gonna say Connect via Bastion.
And we can see that we've got our
admin ID and password in here
that we've created when we created the VM.
I'm gonna enter them here.
And now there's this blue Connect button, all right.
So now we're in the browser,
but we are doing an RDP-type experience
getting access to this machine as we were with RDP.
So we've seen that Bastion is a more secure way
of connecting to your machines for administrative purposes.
It is not free.
However, it does have some requirements
such as a private IP address
and allowing NSG access to Bastion.
But it is pretty good for this purpose,
even though you can allow file transfers,
it is not necessarily recommended
as a way for getting files onto a machine
because there is a cost for that data transmission.
So Azure Bastion is definitely when you see on the exam
talking about secure ways of connecting to your machines,
you should be thinking about using Bastion
instead of RDP and SSH.


### 📺 Lesson: Virtual Machine Scale Sets (VMSS)


Instructor: So when we were dealing
with a single virtual machine,
we saw how easy it was to resize the machine.
If for whatever reason we needed a bigger,
more powerful machine, we could simply make a bigger one.
But that doesn't necessarily increase availability.
It certainly would increase its ability
to handle larger workloads, but it still suffers
from the same challenges in terms of there being,
first of all, a maximum limit
to which you could size a machine.
So we saw that there is a 96 CPU machine.
But if we just wanted to stick with the B series,
for instance, the maximum size is,
looks to be 20 CPUs.
So we could increase the size of this machine
a few more times, but then there'll be a maximum limit.
So another option of this, of course,
is called scaling out.
And that has to do with increasing the number
of identical load-balanced instances there are.
So if we created two B4ms machines,
we would still have all of this power.
We would still be able to handle
usually about twice the workloads,
but you actually reduce the risk
because if one of the machines goes down,
the other machine's still up and can handle the load.
If you go to four or eight
or 16 of these identical machines, you're reducing the risk
of the entire application going down significantly.
In Azure, there is a convenient tool
for you to be able to do this,
and that is called a scale set,
or VMSS virtual machine scale set for short.
So a scale set is a group of identical load balance VMs
that can automatically scale in or scale out.
And scaling in means to reduce the number
of virtual machines, and to scale out
means to increase the number of virtual machines
in that group.
So this is a group of virtual machines acting together,
and they're identical.
Designed for stateless workloads.
So perfect for web servers, perfect for API servers.
Anything where it doesn't need to remember
anything about previous interactions
every time it gets a request.
And because it's a VMSS, it's a scale set,
you're handling everything as a group.
This is a group modifications and group maintenance.
So VMSS is autoscaling, redundancy,
and load balancing for virtual machines.
So I'm in the VMSS section.
I'm just gonna click the Create button here and we'll see.
Now you'll notice it's got a very similar outlook
to creating a virtual machine.
We have additional elements such as health tab,
as well as we can do spot VMs as part of our thing.
We're gonna see all the differences now.
I'm gonna place this in the same virtual machine test group
that we've been working with,
and I'm gonna call this AZ VMSS demo.
Put that in the same region, same availability zone,
the same information about these things
applies as in virtual machines.
Now when it comes to orchestration,
that's where we get to be a little bit different.
So orchestration mode has the choices
between flexible and uniform.
With uniform orchestration, all the instances are identical.
And it's basically the same image, the same configuration.
It's all managed by the same scale set.
It supports autoscaling, rolling upgrades,
automatic healing, and again,
ideal for the stateless workloads like a web server.
So with uniform orchestration,
VMSS handles the entire lifecycle of starting,
maintaining and ending those instances.
You cannot log into an individual instance
and make changes to it.
And if you do make a change, then it could be,
could be overwritten because the VMSS assumes it's the one
that's managing the instance.
Flexible, by the name implying,
is more complicated and can handle stateful workloads.
So the VMs can be individually managed.
You can mix VMs of different sizes.
You could have spot VMs and regular VMs working together.
It still supports autoscaling to a degree,
but there is more manual control in the flexible option.
You can SSH or RDP into individual VMs.
You can make changes that will persist.
And it's great when you have multiple apps or custom apps,
and certain servers have certain functions,
and other servers have more than that function.
And this also works with availability zones.
So if we need to deploy individual VMs
to an individual availability zones,
you're in the flexible state.
All right, I'm gonna choose for the simplicity of it
the uniform model.
We'll have two instances as our default here.
Now, we haven't talked about scaling.
I have a video talking
about manually scaling and autoscaling.
So we'll talk about that in that video.
And just like choosing a VM, we'll choose the image,
we'll choose the architecture, we'll choose the size,
and then we have to give it administrator,
user ID and password.
We have hybrid benefit as an option.
Now, spot instances, we haven't talked about it yet,
but spot instances allow you to bring on capacity
at a discounted rate for workloads
that can tolerate interruptions.
So at any time, Azure can pull back your access
to a spot instance.
It really is like taking a standby seat on an airplane.
You are there because they have the capacity,
but as soon as they don't have the capacity,
you're gonna have to give up your seat.
And then these are the types of evictions.
If you do choose spot instances,
then you have to figure out what to do when you get evicted.
Now, just like with VMs,
you're gonna choose the operating system image,
the premium SSD as the disc type,
what kind of security keys get managed,
same as everything.
There is a virtual network.
Of course, every VM needs one.
And this is choosing to create a new virtual network.
I could add it to one of my existing virtual networks
if I wanted to.
Actually, I'll do that.
I'm gonna put this
in the backend of my existing virtual network.
You'll see that a network interface card is created.
Now, this load balancing,
if you have an existing load balancer,
then this is where you would select that.
Of course, a VMSS requires a load balancer
because you have multiple identical VMs
and they need somewhere to direct the traffic to them.
We'll skip choosing a load balancer for now.
We'll deploy these as standalone VMs.
Same management type options, Defender for Cloud.
How instances get upgraded
in terms of operating system updates,
I'll choose automatic.
I'll turn off boot diagnostics.
These are all.
Now, VMSS has the higher chance of getting terminated
because you get an instance created
and in an instance is destroyed.
So do you need those type of notifications
to some application running on the VM
so it can do something before it gets terminated?
All right.
Overprovisioning is a cool feature for VMSS.
Right now, when we're gonna select the scaling options,
it's waiting until the instance gets to a certain threshold.
Let's say you're waiting on 70% CPU utilization,
and then it creates a VM,
there might be some startup that is required.
You know, scripts need to be installed.
Software needs to be downloaded.
It might take several minutes
for a virtual machine to be instantiated.
And so overprovisioning has a VM on standby
that if you know you're gonna need to add a VM,
pretty surely eventually,
it's got them already spun up and waiting to go.
So this is sort of early provisioning.
You are not billed for the extra VMs,
and they do not count towards your quota.
That's pretty clever.
Now, I mentioned that VMSS has a health feature.
This means that you can have the VMSS
monitor the health of those machines
and do something when the machine is not responding.
So let's say you've got five virtual machines
and one of them is just, you send a request over a port,
and you get zero response back.
Well, then it might be smart
to shut that machine down and restart it.
Or, at the very minimum,
kick that machine out of the rotation.
So you go down from five to four
because you've got one unhealthy instance.
So health monitoring is actually pretty important
for virtual machine scale sets.
Now, typically, what you're doing
for something like an HTTP monitor
is you're looking for a webpage.
So there might be a /status.html page that it would pull up.
And if that returned successfully,
then we know that the machine is healthy.
You can also do a TCP health monitor
where it just checks the port 80.
When you open the port, it opens successfully
and then you can close the port.
So simply checking the port is one other way to do that.
So I'm gonna leave that turned off for now.
Once you've got your health monitoring set up,
you can set it up for automatic repairs.
So again, once we find a bad instance,
what do we do?
We restart the machine.
Do we just instantiate it and instantiate a whole new one?
Do we reinstall the whole image?
There's lots of options for automatic repairs.
Going to Advanced, it used to be very sensitive
that you would have a maximum of a hundred instances,
and you needed to do something special
in terms of a placement group to get more than a hundred.
And as you can see, you don't even have the option.
You can scale beyond a hundred now.
Similar to VMs, you can add extensions,
add applications, have custom data
and user data pass along with it.
These are all the same settings for VMs.
And now I'm gonna say review and create.
So when I hit the Create button,
two additional standard B2ms machines
are going to be created that,
like I said, I can operate on them together.
I can make it three, I can make it one.
We'll see that when we're talking about manually scaling.
And I'm gonna hit the Create button,
and we'll let that run, and we'll see that in a second.
All right, so just like with virtual machines,
that didn't take very long at all.
So we can see the virtual machine scale set
took just over a minute.
I'm gonna say go to resource.
And the view here is a little bit different.
We're gonna be able to see the individual instances view,
but we do have a view of our virtual machine scale set
as being succeeded.
We've got two B2ms instances running.
They all have to be identical, remember,
because we're using uniform.
If we go on the Instances tab on the left,
we can see the individual VMs.
And if we click it, then we can see it
just as if we were using a VM tab.
We can even connect to it.
But remember, because it's uniform,
we can't make any changes to this
to make it any different than the other one.
So this is a slim down view of a virtual machine.
All right, so let's talk about scaling,
coming up.


### 📺 Lesson: VMSS Manual Scaling


Instructor: All right, so let's talk
about manually scaling this virtual machine scale set.
So if we go under availability and scale, under scaling,
we can see that we have a slider here.
It's on the manual scale setting.
And we can just pull this slider.
If we had capacity for hundreds,
we could pull the slider all the way to 1,000 instances.
But even going from, well,
let's just overwrite the number and say two to three.
If I was to click save at this point,
then we would have the VMSS
automatically deploy a third VM.
And so we'll see that on the instances tab.
Now, this is not generally the recommended way
to do scaling.
You'd wanna set up auto scale,
which we'll talk about in a second,
to do it based on some schedule
or based on some other metrics
or some prediction in advance.
But simply having multiple virtual machines
that are always running,
it's quite normal as well.
So if you know that your web server
always requires five VMs
and you're never going up or down,
you would be on the manual scale.
And if you did need to save a bit of money, you go down.
If you did need to increase the capacity, you go up.
That's perfectly fine as well.
So this is for predictable workloads.
If I click over to the instances tab and I refresh this,
I'm now running three instances, zero, one and two.
Now, it's worth pointing out as well
that you may not even want to use the portal
for doing the scaling.
You may wanna do things by script.
And so opening up,
I'm gonna open up the cloud shell here to demonstrate.
But we have the ability
to run either PowerShell or CLI commands
to do the scaling for us.
I'm gonna switch over to a Bash shell.
And if I paste in this command,
az vmss scale,
give it the name,
give it the resource group capacity down to two,
and hit enter,
it's now doing the scaling.
Let's minimize this window a little bit.
You'll see that the instance is being deleted.
It says deleting.
And now the instance has been removed from our list.
And so we can see
that there's scriptable ways of changing it, of course.
Now, for the exam,
it's important to remember
the difference between manual scaling and automatic scaling,
and as well as understanding that for manual scaling
is for predictable workloads.
You are gonna pay for the instances that you create,
and you're going to save money
on the instances that you remove.
And so this is an important method
for controlling costs in the cloud,
as well as keeping performance for your users
to the expected standard.


### 📺 Lesson: VMSS Auto Scaling


Tutor: So we've seen that with manual scaling,
that we're able to either increase the performance
that our users experience or reduce the cost
using manual scaling,
but Autoscaling takes that
and makes it automated, of course.
So this is automatically adjusting
the number of VM instances,
it's based on either a schedule or performance metrics,
and whatever you do is based on a predictive event.
So for this AZ 104 video,
we're going to talk about Autoscaling.
Now, you'll see that it's given in a name
and it's gonna place this Autoscaling
as its own resource in the Resource group.
Now, Predictive autoscaling is a relatively new feature
that uses machine learning
to forecast when your app is likely to need more capacity,
and so it knows that every Monday at 10:00 AM
there's a spike in traffic,
and so by 9:45, it's got the server,
additional servers ready to go.
And so you can have the Enable the learning mode
where it's just basically forecasting
when the scaling is gonna be required,
or you can just turn it on
and trust that its predictions can be accurate.
So we're not gonna get into that,
but Predictive autoscaling is possible.
Now what we're gonna do is we're gonna define a set of rules
that when to add a particular instance
or remove an instance.
So, the rule that we're gonna create
is gonna be scaling based on a metric.
And so we're going to say we want a Minimum 2 instances,
a Maximum of 5 instances,
and 2 is the Default, okay?
So we've got this Minimum/Maximum concept,
and when the VMS' first starts up, how many it's created.
So we do need to create these things called rules,
and that's going to indicate when do you add an instance
and when do you remove an instance?
And you should have a rule for both, right?
So, a rule for adding, and at least one rule for removing.
So we can see, for instance,
we want to look at the Percentage of CPU in this instance,
so I'm going to, we're seeing here
that this server is not really pushing the CPU very high,
but let's create the rule based on a 70% CPU,
over a period of 10 minutes,
so that's quite a long period to wait to act,
but we're gonna leave it with the default,
and we're going to increase the count by 1,
so it'll go from 2 to 3,
if the CPU utilization on the 2
will exceed 70% for more than 10 minutes,
and then it's gonna wait 5 minutes
before evaluating this again,
so that's the rule.
Now remember, we've added a scaling out rule,
we should probably add a scaling in rule.
So I'm gonna say if it's less than 25%
for more than 10 minutes, oh, let's make it 15%,
then it's going to decrease the count by 1.
So we've, if it's over 70, we increase,
if it's less than 15, we decrease.
Actually, if we Default to, well, 4,
then the Autoscaling in rule will kick in eventually
and get us back down to 2.
So, I'm gonna say Save.


### 📺 Lesson: Create a VM in PowerShell


Instructor: So, in this video,
I just wanted to demonstrate
that we could use PowerShell to create virtual machines.
And there's many different ways to do that.
There's a lot of flexibility with PowerShell.
We'll start off with the simplest way.
So, the commandlet for creating a VM is New- AzVM
and you give it a name.
So, it could be azsjdnewvm,
and you need to give it a credential,
but in this case, I'm going to ask the system
to get the credential from me.
So I'm gonna say Get-Credential.
So this is the simplest command
for creating a virtual machine.
It just assumes defaults for everything.
It gets a default vnet name,
it gets default network interface, all of these things.
So I have to enter the credentials.
Luckily it hides the password
and it's just going to get defaults for everything.
Standard_D2s_v3 is this default size,
and we can sort of see there's even a progress bar
that's being created here within the text.
If I was to minimize this window,
I could go into the virtual machines
I have running, I called this azsjdnewvm.
put that in the Resource Group New VM
and it is running Standard_D2s_v3.
So, that's exactly what I had requested to be created.
So, like I said, did a lot of this
with just the default settings.
Now, it's very easy as well to get way more complicated
where you have a 26-line script that sets up
all of the variables
and sets up the configuration variables,
creates the vnet exactly how you wanted,
creates a network interface card
and then sets up the virtual machine.
So, you can get complicated
or you can just accept the defaults.
There's lots of different options
in terms of creating VMs by PowerShell.
So if I was to upload this script
and then executed it, let's see it create the VM.
Way less verbose than I was expecting.
So, that completed.
And if we bring in our portal here
and we hit refresh, we can see that my VM now exists,
which was the VM that was created by the script.
So, creating VMs by script, it's certainly possible.
It's not as easy as the portal, but probably more reliable.
You're gonna do this long term,
you're gonna have your scripts created
that can create you a VM to your standards,
and you just do it repetitively like this.
It's probably a more common way to create a VM
even though the portal is more foolproof, I suppose.


### 📺 Lesson: Practice Lab: Create a Linux VM and Host a Web Page


Well, hi there, in this video,
we're going to build a virtual machine in Azure.
And so this is called a practice lab.
And if you haven't tried it before, dive right in.
So this video and this lab is completely optional.
If you don't wanna do it, you can just watch
or you can mark the lessons complete and continue.
But if you do wanna give it a try,
and I do encourage you to try this, it's not that difficult,
and it's a way of reinforcing learning, then continue along.
I'm going to give you a series of steps in this video
and you're going to practice it within the Azure portal.
Udemy gives you an Azure portal that you can work with,
and so you're gonna be doing that.
Or if you have your own account provided by your company,
you can do this yourself as well.
Do keep in mind that creating virtual machines
does have a charge sometimes associated with it.
If you choose the free tier, et cetera,
maybe that can be done for free,
but there is a possibility
of this costing you money if you're doing this
in your own account.
All right, so in this lab,
we're gonna build a real web server in Azure,
starting from nothing to a webpage
where you can open it in your browser.
So let's give you a scenario.
Let's imagine your company needs a simple website
and the team has decided to run it
on a virtual machine in Azure.
That's called Infrastructure as a Service or IaaS.
So Azure gives us the hardware, the network
and the data center, and we are responsible
for the operating system and everything we install on it.
Remember, that's the shared responsibility model.
So in this lab, we're gonna do six things.
We're going to create a Linux virtual machine.
We're gonna give it a name.
We're going to connect to it using the Cloud Shell.
We're gonna install the web server.
We're gonna open the firewall
so people can actually read it.
And number six is we're gonna stop the VM
so that it stops costing us money.
So I encourage you, like I said,
to follow along in your lab workspace.
And each task of these six tasks is marked
in the video timeline.
So if you get stuck, you can always go back
and watch that part of the video.
All right, so I'm inside the resource group
that I created for this.
And in the search bar,
I'm gonna search for virtual machine.
And you're gonna see
that there is a service called virtual machines.
It's also available with this computer monitor in the menu,
but I'm just gonna go from here.
Now, I already have a virtual machine,
but maybe you don't have any,
and in the Udemy platform, you wouldn't have any.
So this should be relatively empty.
I'm gonna go up to the create
and I'm gonna say create virtual machine.
Now, I am gonna have to choose the resource group
if we're creating it this way.
And so I'm gonna go into this list of resource groups
and choose the one that I created,
or in the case of the Udemy environment,
you'll choose the Udemy resource group.
Scrolling down...
I'll make sure that the subscription is correct.
Scrolling down, we have a number of options here
from virtual machine name, region, availability,
image and the machine size.
All right, so I give the virtual machine a name
and I keep it in the same region
as the resource group in my case.
Now, the availability option
is chosen as availability zone as default,
but I'm gonna change this
to no infrastructure redundancy required.
It's gonna place this VM in whatever data center
in this region that it wishes.
Now, the image choice is important.
Here we're doing a Linux deployment.
So I chose Ubuntu Server as the option.
Going down to the size,
I've chosen a B2s virtual machine, relatively cheap.
If you say see all sizes, you can choose.
You're gonna have in the Udemy environment
only a limited number of options.
You could say, I think there's the B1s option
if you really want to save money.
It says end of life.
So obviously Microsoft doesn't want you to choose this,
but the B2s option also, I think it's end of life,
still a decent option
and relatively cheap on a monthly basis.
So we're gonna select B2s in this case.
And we're gonna leave all this to default.
Now, in reality, you might wanna choose an SSH public key,
but in this particular case,
we're going to use a password setup
so we can connect to this using a username and password
instead of the more secure method.
We're only doing this for demonstration purposes.
All right, for the administrator account,
I'm using a password, makes it easier in this demonstration.
The default user's called azureuser
and I've created a password for it that only I know.
If we scroll a little bit, we can see
that we are authorizing inbound access,
SSH only at this time.
Even though I intend to make this a web server,
we'll show you how to open those ports later in this lab.
But for now we're having SSH open.
I'm gonna say Next.
All right, so in terms of the disks,
this is offering me a solid state disk.
I could certainly downgrade
to the standard spinning magnetic disk,
but the standard SSD does fine for our purposes.
It's a good balance between cost and speed.
We're gonna leave everything else pretty much the default.
So I'm gonna say to disk, Next.
I'm gonna say networking.
It's gonna create a virtual network for us.
We'll leave that as the default.
Management, we're gonna leave that as the default.
Monitoring, I usually turn off boot diagnostics
and so we can turn that off.
And we're just advancing through the tabs here all the way
to review and create.
All right, so it's telling us the server's gonna cost us
around four cents per hour.
And we're gonna click the Create button.
And it is gonna take a couple of minutes.
And so we're gonna let that deploy,
but this is the end of the first task,
which is to create a virtual machine.
All right, it says the deployment is complete.
We can say go to resource.
And under the Essentials tab on the overview screen,
we can see that the VM is running.
It is a Linux operating system with a standard B2s size.
And you'll see here it has a public IP address.
So our second task is to give our VM a DNS name.
So right now we can address this virtual machine
using this IP address,
but IP addresses are hard to remember
and not too pretty when you're trying to give this
to someone else to access your website.
So we're gonna scroll down a little bit
into the properties.
Under networking, we can see again the IP address repeated,
but under DNS name it says configure.
And so we're going to click that.
It's gonna take us to the IP address itself
and you'll see that the IP address
can have an optional DNS name
and it's got a fairly lengthy domain
and sub-domain names.
So it's .westus2.cloudapp.azure.com
and we have to give it a name.
So whatever name we give it has to be unique
for this sub-domain.
So I've called it newlinuxvm996
to give it this more defined name
to the IP address.
Now, using the domain name system,
you can actually create what's called a CNAME record
and get your own friendlier domain,
if you've got a company one, and map it to this.
So there's a way of redirecting traffic from a good domain
that you've registered to this less good domain.
But anyways, this is an improvement over the IP address.
So I've typed in this DNS name and I'm gonna say Apply.
And so if we go back to the overview screen
for the virtual machine
and we hit refresh,
we can see the DNS name is now there.
So that was task number two, give the IP address a DNS name.
All right, task number three is to connect
to this VM in the Cloud Shell.
So what we're gonna do in this task
is we're going to use what's called the Cloud Shell.
So in the top menu bar at the very top,
there is this square
with a greater than sign and underscore,
and that is called the Cloud Shell.
So before I connect to it,
I'm going to copy the full DNS name,
including the cloudapp.azure.com
with Control + C,
and I'm going to say click on the Cloud Shell.
Now, this is opening up a browser frame that is a terminal
and that is going to allow me to connect
to my Linux VM.
Now, it's possible that you're gonna have
to set this up for the first time.
There should be an option
to use the Cloud Shell without storage.
Actually, it actually says it's ephemeral.
So this is a no storage option here,
but you might get a popup when you click Cloud Shell
for the first time.
Now, what I'm gonna say
is I'm going to use the ssh command
and the user is called azureuser.
That was the default that was offered to us
when we created the virtual machine.
So hopefully you didn't change that.
And we're gonna paste, which is Shift + Insert,
the full DNS name that we created.
And so you'll see the command ssh azureuser@
and then my newlinuxvm996 and the rest.
And if I click Enter,
it's going to ask me, "Am I sure?"
Because I'm accepting a security certificate.
So I'm gonna say yes.
And now it's trusting this machine.
So now it's asking for the password
that I set when I created this machine.
So I typed it and now I have connected
to Ubuntu 24.04 in my case.
And you can see that it has been running.
It's giving me some legal warnings.
And I have a command line here at the bottom
that is azureuser@,
and that's the name of the VM I gave it, newlinuxvm.
So I'm no longer using the Cloud Shell,
I'm using the shell of the virtual machine that we created.
So that was task number three,
which is to connect to the VM using Cloud Shell.
Now, task number four is to install a web server.
So what we're gonna be doing here
is we're going to turn this Linux machine,
which has nothing really installed on it, into a web server.
What we're gonna do is make sure, first of all,
that all of the software is updated
and in a single command,
we're also going to install an app called Nginx, N-G-I-N-X.
And that is the very light web server.
Now, there's other web servers,
like Apache and things like that,
but Nginx is a very popular light web server.
So I entered this command. I'll show it to you.
Go back up.
I said sudo apt update,
which is gonna update the lib virtual machine
and then two &amp; signs, which means it's a second command.
And I'm gonna say sudo.
Again, sudo is giving me superuser permissions.
And I'm gonna say apt install
and I'm gonna automatically accept.
y is to override and say yes, nginx.
So it's gonna do a bunch of updates
and then it's gonna install nginx brand new.
And that's it. It's done.
All right, so the next thing we're gonna do
is we're going to replace the default homepage of Nginx
with our own custom version.
I'm gonna paste it here.
What I'm doing, you don't have to do this,
but this just makes a good demo,
is I'm gonna say, "Hello from my Azure VM" in heading
and also built in the lab as a paragraph.
And that's gonna get piped into this index.html.
And this is the default homepage.
Now let's test it.
Now, right now we don't have port 80 open,
so we can't test it from our browser.
And this is just a command line.
So I'm gonna use what's called the curl command.
Curl allows you to call
to a URL and retrieve the results.
And so localhost is the server that we're running on
and curl is just grab some HTML
for me from the server that I'm running on.
So I'm expecting to see my brand new homepage.
And as you can see, hello from Azure VM, built in the lab.
When I turn this into a web server
while opening port 80,
this is going to display inside your browser.
So that is a successful test.
And in fact, we can test this for real.
We're gonna copy again this domain name.
Opening a browser tab
and I'm gonna paste the domain name, and it shouldn't work.
So we're expecting this because port 80's not open.
This is not a valid path right now
and that's successful test.
So we have successfully installed a web server.
It works internally,
but it doesn't work externally as expected.
All right, so task number five is to allow web traffic
by changing the network security group rules.
I'm gonna move this browser to the side here.
Now we're back on the Linux VM homepage in the portal.
And on the left, I'm gonna go under Networking
and we're gonna look at network settings.
Now, if we scroll a little bit, we can see
that there's inbound rules and outbound rules.
Right now, the only thing that's allowed inbound is SSH.
There are some default rules that allow other VNets
to talk to it, load balancers and stuff,
but by default, everything is denied, except for SSH.
We also have outbound rules.
So we're gonna create an inbound rule.
I'm gonna say create port rule, inbound rule.
And we're going to say that we want any traffic
to any destination.
And I'm gonna choose
from the service dropdown the HTTP service.
We could have manually typed in port 80,
but this is a convenient shortcut,
port 80 for TCP service.
It's gonna allow.
And this priority 310 is slightly
behind the SSH priority.
In this case, it doesn't matter.
And we're gonna call this Allow-HTTP.
You have to give it a name, and say Add.
So once this is accepted,
then traffic along port 80 will be allowed inbound
to this virtual machine through this network security group.
As you can see, HTTP traffic has now been allowed.
I'm gonna give that about 30 seconds
and then we're gonna refresh the browser window.
All right, so I'm back to the browser window.
I'm gonna hit F5, refresh.
And now it's spinning.
Be sure that we're using HTTP connection, not HTTPS.
And it says, "Hello from my Azure VM,"
exactly as I expected.
So in this task number five, we opened port 80
within the network security group,
allowing traffic inbound over port 80,
and successfully we're able to connect
to our virtual machine that's running a web server.
All right, so task number six
is to stop the virtual machine.
If you have the Cloud Shell still open
and you're connected to the VM, exit from that.
So type exit.
Otherwise, we can go to the VM overview,
go up to the menu here, say Stop,
and it will ask us, "Are we sure?"
We can say yes.
And that's going stop the VM.
Now, what matters for your bill,
if you're talking in reality,
stopping does release the instance.
So now this B2s will go back to being available
for use by other people,
but it does keep a little bit for the disk.
So if we look at the disk settings,
we reserved a relatively small operating system disk
of 30 gigabytes.
That will still not be deleted so that we can start it again
and not lose anything that we've done with that machine.
The web server will still be there.
The default homepage I created will still be there
because this disk exists
and stopping the machine doesn't delete the disk.
Other thing to note is in Linux, you can say shut down
and that does not release the instance back to the pool
and you're gonna continue paying for it.
So you could shut down the operating system,
but still have the instance running
and that is a bad situation.
So always stop your VMs from the portal
and not from inside the operating system.
So task number six, we stop the VM.
We're saving money on the price of this B2s.
All right, so let's recap what we did in this lab.
We created a Linux virtual machine
that's Infrastructure as a Service.
Azure manages the hardware
and we manage the operating system
and all the software, including patches.
We gave it a DNS name.
We connected to it using SSH from the Cloud Shell.
We installed a web server.
And until we opened up port 80,
the browser from my machine couldn't reach it.
So the security was enabled
until we allowed traffic over that port.
Of course, if we want secure traffic, that's port 443.
It's a different port.
By stopping the VM, we have de-allocated it,
allowed other people to use this B2s instance,
but we haven't stopped all the charges
'cause we still have a disk.
Now, in order to be absolutely complete,
I can delete this virtual machine
or even go up to the resource group.
You'll see a bunch of resources were created relating
to the virtual machine, including the IP,
the network security group, the network's interface card,
the disk, et cetera.
If you have this on your own instance,
your own subscription, you can say delete resource group
and that will remove all of these resources.
That's one of the benefits of resource groups
is deleting all resources at once safely.
If you're doing this within Udemy,
you can simply just delete the virtual machine
or stop it from running.
So that's it. Thanks a lot.
We'll see you in the next video.


### 📺 Lesson: HANDS-ON LAB: Create a VM Scale Set using a VM Image


[No transcript available for this lecture]

