---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "08"
title: "Module 08: Administer Virtual Networking and Intersite Connectivity"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 08: Administer Virtual Networking and Intersite Connectivity

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** Virtual Networks, Subnets, Public IPs, NICs, RDP Port Management, Global VNet Peering, Virtual Network Gateways, VNet-to-VNet VPN Connections, Azure DNS Public and Private Zones, Custom Domain Mapping  
**Line Range:** Lines 13979 – 15754 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


### 📺 Lesson: Virtual Networks


Instructor: All right, we're moving on to talk about
virtual networks.
Now virtual networks, I view
as the glue that tie various infrastructure
Azure services together.
And we've seen so far in this course
that virtual machines absolutely
require a virtual network in order to have connectivity
to the internet, to have connectivity to other,
to each other, and to other Azure services.
And you have the option
within things like app services
to connect to a virtual network to allow some control
over routing and security and things like that.
So in this video, we're going to create a virtual network,
and we're not going to give like,
when we create a virtual machine
it allows us to create a virtual network
at the same time.
We're actually going to intentionally
create a virtual network from scratch.
So you can go into the marketplace and search
for virtual networks or VNET, and you'll get to something
like this where you can say, create a virtual network.
Now, like anything, we have our wizard view
of creating this virtual network.
I'm going to create a new resource group to put this in,
and we're going to have to give it a name.
Now, the region of the virtual network does matter
because you are going to be restricted
to the virtual machines being from that region
to add it to the same virtual network.
There is a relationship
between the location of the network network
and the location of the computing resources.
So I'm going to choose West Europe to put this network.
That restricts me from only putting
VMs from West Europe onto this network.
Then I'm going to click next.
Now they've moved this around a little bit,
and the next tab is security.
So there are a number of services that you can add
to your network, and these are paid services.
So if you want to have Azure Bastian,
we saw that earlier in the course for RDP/SSH connectivity
to virtual machines
without having to open the ports.
We have an Azure firewall option.
We haven't talked about firewall yet.
DDoS protection.
And as if you were to check any of these services,
then you would have to,
you're basically provisioning that service.
So by checking Azure Bastian,
it's going to ask me for the host name
and it's going to create a new public IP address
for Bastian.
Similarly, for firewall, we then start
up the various firewall options.
We're not going to do that.
But there's an interesting side effect,
I'll show you in a second,
from me selecting these and then unselecting it.
When we go onto looking at IP addresses...
This is quite important, right?
So, the IP address range of a virtual network
can be changed after you start
with a number of private IP addresses
that are available for use.
And then you can again, add to it if you need more.
This space here, this 10.0.0.0/16,
that's called CIDR notation, C I D R.
And it's a bit map basically, a mask that will allow you to
determine how many IP addresses are in this range.
And we can see a clue
underneath where it says 10.0.0.0 to 10.0.255.255.
So this slash 16 basically is a mask
over the first two octets.
And then the other two octets of this are the full range.
If I said slash 24,
then you would only have 256 addresses available.
And if I said slash eight, I would have, you know,
the full three final octets available.
You don't need to make this too big.
Like 65,000
addresses means 65,000 virtual machines,
which is quite a lot.
By default, you get a subnet called default.
Notice the subnet is smaller
than the total addressable space for the VNET.
So by default, I'm giving it slash 24, which is
like I said, the 256 addresses.
That leaves
tens of thousands of other addresses that I could allocate
with other subnets.
Because I selected Bastian and firewall
on the previous screen and then unselected them,
Azure is helpfully allowing me to create two
additional subnets for those.
And as you can see,
it is 2.0.1 to 63
and 2.0.2 to 63.
So we're actually wasting
three quarters of this
part, this D block, I guess.
So,
we can see here it's done some helpful things for us.
Now, typically what you do with subnet is you
want to divide your network across security zones.
So you might have a subnet
for front end websites, a subnet for databases,
a subnet for middle tier applications, et cetera.
So each subnet can be secured differently
using a network security group.
If we wanted to change this,
we could add an address space.
If we wanted to add additional subnets,
like we had the middle tier and the back end,
we can add a subnet.
I'm not going to do that right now.
We'll add the subnet later in this course.
So I'm going to accept the defaults,
including the Bastian and firewall subnets,
not including those services.
We'll skip over the tags
and we'll get to the validation element.
Now, virtual networks are free.
There's no charge to create them at this moment,
but you are limited in the number
of virtual networks that can be associated
with your subscription.
I think it's 250 virtual networks per region.
So don't go absolutely crazy with creating them,
but you can create many, many of them and not worry
about racking up any charges until you create resources
like a virtual machine attached to it.
So I'm going to click the create button
We'll let that run.
Now, this took only a couple of seconds,
and I think the reason is because there's not
actually resources being instantiated
when you create a virtual network, you're really just,
it's really entries in a database table.
Microsoft has hardware, wires, hubs, and things,
and all they're doing is just learning how to
route traffic for you.
And those are just entries in a database,
behind the scenes.
I can say go to resource,
and now we have a virtual network.
As we saw, we have this one address space,
a rather large address space,
but the 10.0.0.0 address space,
this is not accessible from the the public internet.
It's a private address.
And in terms of subnets, we've got the three subnets,
one default, and one for Bastian, and one for firewall.
And we don't have any devices.
We haven't deployed any VMs
to the existing virtual network subnets.
Okay?
So that's how easy it is to create a virtual network.
In the rest of the section, we're going to talk
about the various requirements for the exam,
the various issues in terms of setting your virtual network.


### 📺 Lesson: Deploying Resources to a VNet


Teacher: So as you can see,
we don't have any devices on our vnet.
So maybe before we go any further, let's deploy
a little virtual machine to this.
So I'm going to create a Windows Server 2019 data
center, virtual machine.
Just for convenience,
I'm gonna put it into the same resource group.
I'm gonna call this a VM demo,
no infrastructure availability.
Let's just leave it as a standard VM.
This one is very small, B1s.
I'm gonna upgrade that to B2ms.
(keyboard clicking)
And put a user ID and password.
Just for demonstration purposes,
I'm not going to open any ports.
Okay, so let's assume
that there's no ports open at this moment.
We'll skip over the disk options
and we'll get into the networking options.
Now you can see it's chosen my vnet
by default because I have one in that region.
If I had chosen a different region
it wouldn't be available to me.
It's putting this virtual machine into the default subnet.
But in this particular case
it's coming up with a brand new public ip.
I'm going to say no to that, okay?
We let it create a network security group.
We're not gonna open any ports.
So right now, this machine will have a internal
private IP address that starts with a 10
and will not have a public IP address.
I'm gonna skip over most
of the next settings here, no diagnostics.
Skip the advanced, and get right into review
and create.
10 cents an hour for this B2ms.
Click create.
So what I'm expecting is
that it will deploy this B2ms machine onto this vnet
and we'll see that in a second.
All right, so that was pretty quick.
We can say go to resource.
Machine is still starting up obviously.
Going to the networking settings
for the virtual machine,
and we can see the network has a network interface card
and the network interface card is attached to our vnet.
Let's get out of here, go back
into our vnet,
vnet demo, and go into connected devices.
And now we can see the network interface card is connected
to our vnet using the following IP address.
So it's an internal IP address on the default subnet.
So this is exactly what we were expecting.
And so in this way, we can create devices
deploy them into the various subnets that we create.
These bastion firewalls are obviously reserved
for those Azure services.
And in this section we will talk about setting
up the security, opening up ports and restricting
let's say we have a front end and a backend subnet.
We'll talk about how to basically protect those
by closing off ports.


### 📺 Lesson: Creating and Modifying a Virtual Network Subnet


Instructor: Now just to further demonstrate this,
I'm going to create a couple of additional subnets
onto this virtual network.
Now we can see that 10.0.0.0 is already taken,
The full /24 range.
10.0.1.0 is only partly taken,
about a quarter of the range
and the same for 10.0.2.0.
So I'm gonna create a,
let's call it midtier subnet,
and you'll see it's automatically offering me up 10.0.3,
so these cannot overlap
and they must be subranges
of the total address space for the entire virtual network.
We have the option of getting IPv6.
All of Azure now supports IPv6 connectivity,
and we can select any sort of gateways,
any security groups routing.
We won't do that at this time,
but we have a lot of advanced options.
Now that's as easy as it is to create a subnet.
We can call it backtier,
and we get the 10.0.4 range and say Save.
So now I have three subnets that are from my creation.
Now one thing that's kind of bothering me
about the inefficiency here
is that we do have, as I said, a subnet
that is only using 59 or 64, effectively, IP addresses
out of a 256 address range and wasting the others.
So what I'm gonna do is I want to edit this firewall subnet
so that it is running beside this Bastion subnet
and we're not wasting potentially a space of range.
Now the reality is you don't have to be so thrifty
with IP addresses in the private space,
because there are millions of them
and you probably will never run out of private IP addresses.
But maybe there's a little bit
of wanting to be organized here.
And so I can change my subnet range for the firewall.
You'll see that this one,
each of them have 64 addresses that they're asking for.
So if I change this to 10.0.1.64/26,
I'm actually reserving the next block of 64
next to the Bastion subnet,
and I'm freeing up this 10.0.2 for another purpose.
So I can even edit the range of a subnet
as long as there's not other things running on it,
okay, to be clear.
So if there is devices running on this subnet,
then I can't just decide I want to change this
to a different,
oh, let's put this in,
a new subnet range,
because my network interface card and other things
have IP addresses in the old range.
So be careful when you're renaming subnets
that what's the downstream implications
for devices that are running on it.
So I won't touch the default,
but we can we can leave this as this.
And you can see you're not restricted to this .0 ending.
You can actually stack them quite nicely here.


### 📺 Lesson: Public IP Addresses


So right now we have a virtual network with some subnets.
We have a virtual machine that has a network interface card connected to that subnet.
Right now everything is set to private.
There is no public IP address for this network interface card.
What we're going to do in this video is we're going to create a public IP address and associate it with
this network interface card.
And and basically we can then start to open up some ports and get some traffic.
Now we could have done this all during the creation screen.
But I think there's value here in doing this step by step to see how it works.
So let's create a public IP address.
So I'm going to search for public IP address.
Now public IP addresses are not free.
So as of March 2025 Microsoft has deprecated the basic IP address tier that is no longer available.
That means they're also deprecating dynamic IP addresses which are not available as well.
Your only option is to create a standard IP address, which gives you a static IP address at half a
cent per hour.
So if you want that option, that's the price for that.
All right.
So let's go into the thing here.
We're going to create a public IP address and say create I'm going to put this into my VNet demo resource
group.
Now we can choose a region for that address I'll keep this in West Europe.
We give it a name.
So usually it's like pip something or other.
We can choose whether we want a V4 address or one of those new fancy V6 addresses.
Now a reminder that the basic tier no longer exists.
So standard is your only option because the standard load balancer is the only option.
They don't have a basic load balancer anymore either, so all of these options should match your load
balancer.
When you choose the standard option, which is the only option, you get the choice of availability.
Either it is not zone redundant at all, or it is zone redundant, or you can deploy to specific zones.
Again, this should match your load balancer.
Also with the tier uh, we saw on the pricing that there's global pricing versus regional pricing.
Again this must match the load balancer.
So we'll leave the regional pricing by default.
And you'll see we don't get the choice of dynamic versus static at the standard tier.
Now what we're going to want to do is we're going to want to give this DNS a label.
So I'm going to say Azure VM as my label.
And it's going to be fully qualified here based on the region you chose.
And this is a preview feature we won't talk about.
Now another new thing in this is DDoS protection.
Now you know that DDoS protection is now available in terms of either the network tier or versus specific
IP addresses.
So if we want DDoS protection for this IP address, we can sign up for that.
There's a cost to that.
Or if we want um, hundreds of IPS to be covered at the network level.
We can sign up for network level DDoS protection, or we can say we're not going to have any additional
DDoS protection, which I'm going to choose disable in this case.
So I'm going to skip over creating tags, and I'm going to to let it do its review here and say create.
Now does create fairly quickly in terms of the the resource itself, I can say go to resource.
And you can see I've been assigned a public IP address.
Again this is a standard skew.
It's a static address.
Even if I'm not using it it will be uh this address is reserved for me.
There's a cost to it we saw earlier.
It's half a cent per hour just to just to hold it.
When I'm ready to associate this with a network interface card, I can associate here, or I can go
into the network interface card itself and associate it as well.
So this is a public IP address now that I can use for various resources that need to be accessed from
the public.


### 📺 Lesson: Associate Public IP with Network Interface Card (NIC)


Instructor: So now we have this dynamic IP address
that is yet to be assigned.
And all we can do is associate it
with the network interface card
that will give the virtual machine a public IP address.
So, I click on the associate button
within the public IP address.
I choose network interface.
And I can choose the network interface card,
right here from the dropdown list.
Alternately, I can go into the network interface
and I can add an IP address from within there.
So there's two ways to go about this.
So I'm gonna click okay.
All right, so we successfully updated that.
Now what I'm expecting, if I refresh this,
I guess I could give it a moment to come up with it.
We're gonna go into the virtual machine
here under networking.
We can already see, actually,
we can already see that there's a public IP address
that's associated with this network interface card.
And it takes me back to this one that we just created.
It now has a public address.
Now if I go to the network interface card itself,
under IP configurations,
we can see that the same, basically,
network interface card has both a private address
and a public address.
So, virtual machines on the same network
can refer to this machine using its private address.
And of course,
publicly can be associated with this address.
Now keep in mind that the security is still enabled
and there should be, really, nothing that we can do
if we try to ping this address
or we try to remote desktop into it.
Certainly, we haven't installed a web server yet,
so there's nothing listening on port 80 or 443.
The network security group should have, really,
shut this down and not allowed any traffic to it.
So there's a public IP address,
hopefully there's, really, very little that can be exposed
to the machine.
Now we have a whole section
talking about securing access to networks,
network security groups,
effective security rules, and stuff like that.
But just briefly, I will show you,
we go into network security group
and it shows us here...
Actually we are gonna have to
go back up to the resource group,
and we'll see network security group
as something that exists.
And if we look at the inbound security rules,
basically deny, we have a deny rule on all inbound traffic.
The only traffic allowed is from the same virtual network
or from a load balancer.
So, there should be no traffic allowed
to this public IP address and to this server at this time.


### 📺 Lesson: Open Ports to Allow RDP Access


-: So we saw in the last video
that this network security group is attached
to the network interface card that's attached
to our virtual machine.
And right now it does not allow any traffic
in from the internet.
Since we've assigned a public IP address to it
let's start by attaching or allowing RDP traffic
to go to that virtual network.
So I'm in the network security group
under Inbound Security rules, and I'm gonna say, "Add."
We're gonna allow traffic from any store so we could
put our client IP address in here if we wanted to.
And we are going to choose, for a shortcut
we can choose the RDP service
and it tells you Port 3389 for TCP.
And we allow the rule.
Now priority, the lower number has the higher priority.
We have to give it a name.
We should give it a name that is, let's say,
relevant to this.
So allow RDP and say, "Add."
So now at this it's gonna take a couple minutes
to go into effect but now the network security group
is gonna allow traffic from outside over this port
onto the network.
Now, after a couple minutes of allowing this
to sort of filter through we can go
right to the virtual machine.
And like we did earlier in this course,
go to the Connect Menu item under RDP.
It will check to see if we have access,
which we should now that we have the rule created
for the network security group.
And here we go.
We have the RDP file at our disposal
and we should be able to establish a connection
which we have, right?
(computer keys clicking)
So that's how I would say, straightforward it is
to create a public IP address
associated with the network card, open up the rule
and then be able to connect to this virtual machine
using the remote desktop protocol.
Of course, this, you shouldn't have ports open
on your network security group if you don't need them.
And so this type of RDP port should be either very limited.
You should use a Bastion server, or you should remove
all of those types of open ports for security reasons.


### 📺 Lesson: Introduction to VNET Peering


Now when you're setting up
a complex production environment with multiple networks,
multiple servers, multiple applications,
sometimes you do need
to have them communicating with each other.
And by default, any server that's running
on a virtual network,
let's say in this case Newtest1
will not be able to communicate
with a server running in a different virtual network.
Call it Newtest2.
So there is a boundary, a network secure boundary
between these two different virtual networks.
And if you set up network security groups
and you have different subnets on your network,
you even have boundaries of security groups
between the different subnets.
So in this video, we're gonna talk about a concept
where we're going to be connecting two different
virtual networks called peering.
Now peering is the idea of setting up a relationship
between two virtual networks such that
they recognize each other.
And this allows virtual machines running on
one virtual network to communicate with virtual machines
running on another virtual network
because they recognize the IP addresses
in their network space.
Now an important prerequisite for this is that
each of the virtual networks that we're gonna be setting up
in a peering relationship have to have
different address spaces.
So we can see that Newtest1 has the 10.3.0.0 address space,
and Newtest2 in this example is 10.0.
And so they do not overlap in terms of addresses
and so we can connect them.
So we're gonna go into Newtest1 in this example
and scroll under settings
and there's a menu item called peerings.
And so we can see that right now there's no peerings,
Newtestone is a isolated virtual network.
There's no connectivity to any other virtual network.
And we can say add.
Now it's possible to have multiple peerings
between a virtual network and other virtual networks.
It says two or more.
And you can set this up.
There's even a model called the hub-and-spoke model
where you have one virtual network
as the center and other virtual networks as the spokes
and they can communicate with each other, things like that.
So you would do this using peering relationship
if you were trying to set up a hub-and-spoke model.
But in this case we just have the two
and we're going to just connect them A to B.
So we do have to give it a name.
And so I can say vnet2tovnet1
because this is under the remote virtual network.
And we're setting this up for vnet2.
We are authorizing traffic to travel
from the remote network, which is 2 to the local one.
And we have the other
link which is from the local to the remote.
So this is in fact vnet1tovnet2.
So you see what we're doing is we're setting up
two connections on one screen.
This is to go from the remote to the local,
and down here is from the local to the remote.
And we are authorizing the other traffic.
So we could obviously make this a one-way connection,
but we're gonna let this be a two-way connection.
Now there are other options here for forwarded traffic.
So let's say the traffic is not
originating from Newtest2.
Let's say there's a Newtest3
that is forwarding traffic through 2,
do we want to receive traffic that has been forwarded?
There is the gateway inside of Newtest1.
If we were to create a gateway, do we want to allow it
to forward the traffic on?
And do we allow Newtest2
to use the gateway on Newtest1,
we're gonna be talking about VPN gateways,
couple of videos from now.
But this is basically if we're gonna set up
that hub-and-spoke model,
or we're gonna use a single VPN gateway to do
site-to-site VPN from a corporate network to Azure.
But we want to allow other networks within Azure
to use that same site-to-site VPN.
We would have to enable some of these things.
So I'm just going to say add,
we've got a very simple two-way connection
between vnet1 and vnet2.
And I'm just gonna say add.
So right now we've got two deployments going on,
so they're deploying both of these as things.
So we'll see under peerings for Newtest2
that that peering did get connected.
We're in a connected state
and they're really up to date.
If we go over to Newtest2,
which is the what we were calling the remote network
and go under peerings,
then we'll see that the second connection,
2 to 1, has also been set up.
So, what we've done is we've created
two peering connections, one from vnet1 to 2
and one from vnet2 to 1.
And now any device on either of these virtual networks
can see and communicate with any other device
on the other network.
And so this is a peering relationship.
Now these connections still have to follow
network security group rules
if you have an NSG involved.
So if you have servers on a subnet
and it has NSG controlling that subnet,
the traffic still has to obey the rules for ports
and destinations and sources.
So peering doesn't override your security settings,
but it does allow it as a bridge
to those connected networks to talk to each other
as long as they follow NSG or firewall
or other settings that you have protecting traffic on
that network.


### 📺 Lesson: Configure Global Peering


So in the last video,
we set up virtual network peering
between two networks in the same region.
This is West US 2.
And I should point out,
I should have said it in the last video,
but I'll say it here, that there is a cost to that.
Okay?
So VNet peering within the same region
has a cost for the inbound data transfer
and for the outbound data transfer.
So what that means is
if you're sending a single gigabyte from VNet,
or New Test One to New Test Two,
you're paying a cent per gigabyte for it leaving,
and you're paying an additional cent per gigabyte
for it arriving.
Okay?
That's two cents per gigabyte to send one gigabyte
between two networks on a peer.
Now this could add up pretty quickly.
If you're talking about a hundred gigabytes per hour,
then that's a dollar per hour of data charges.
Okay?
So that obviously can add up pretty quickly.
But what about
if the virtual network is not in the same region?
So let's talk about connecting NewTest1,
which is in West US 2, to NewTest3, which is in Japan.
This is called global peering.
So I'm going to go into NewTest1, into peerings.
We still have our connection to NewTest2,
but I'm going to add vnet3tovnet1,
and we're going to choose this Japanese VNet
as the remote network.
And we're going to allow that data transfer.
And then we're going to do vnet1tovnet3
as being the local name,
and we're going to allow that access.
So what I've effectively done
is I've set up global peering.
There's a whole different set of charges for global peering.
So you're basically paying for the data
to travel halfway around the world.
So you'll see that Microsoft has broken the data into zones,
one, two, and three.
And the zones is basically
the different regions of the world
have been set up into these zones.
Let's look at the different zones here.
All right, so Zone 1, West US 2, is in Zone 1.
This is in the Australia, Canada, Europe, UK,
things like that.
Zone 2 has some specialized Australia East
and Southeast zones, India, Asia, Korea,
and Japan is in Zone 2.
And Zone 3, most expensive zone,
is Brazil, South Africa, and the UAE.
Okay?
So what we have is if we're sending a gigabyte
from West US 2 to Japan,
we have 3.5 cents per gigabyte leaving,
and we have 9 cents per gigabyte arriving.
So that is 12.5 cents per gigabyte
for data to go between the two global zones
in this particular example.
Okay?
So this vnet1tovnet3
has gone from 2 cents per gigabyte for local traffic
to 12.5 cents.
So effectively six times the cost to set up global peering.
But that is just the reality of paying for bandwidth
traveling over the Microsoft network between two regions.
So make sure you're sending only essential data
and that you're not being overly verbose for no reason.
And that is VNet global peering.


### 📺 Lesson: Azure-to-Azure Virtual Network Gateway


Now, virtual network peering
is only one way that we have
to allow traffic to travel
between two virtual networks.
Another way we can do that
is using virtual network gateways.
Now, you might know that a virtual network gateway
is also the device we use
when we wanna set up a VPN.
And so sometimes it's called a VPN gateway,
either a site-to-site VPN
or a point-to-site VPN.
Just to remind you,
a site-to-site VPN
allows you to connect say your corporate network
into the Azure network
so that you can communicate them together.
And so you have a virtual network gateway
on the Azure side
and an actual physical network gateway
on the corporate side.
You connect these two devices together,
and then you would have encrypted communication
between them.
But what we're talking about in this scenario,
it would be more in tune of VNet-to-VNet communication.
So you can do the same thing
that you do between your corporate site and Azure
between two virtual networks
using virtual network gateway devices on both sides.
So let's do this as an example.
So I'm looking at my virtual networks
in the Azure portal,
and I wanna pay attention to two of them.
One called NewTest2,
which is located in West US 2,
and one called NewTest3,
which is located in Japan.
Now, if I had a device on NewTest2,
it could not communicate with a device on NewTest3
unless I set up global peering.
The other way we can do this
is through virtual network gateways,
and this is what we're doing here.
So I'm gonna go into NewTest2,
and I'm gonna look under Settings
and under Subnets.
Now, I will point out that I have a default subnet
that is a /24 size,
but the whole network itself is /16.
So there's plenty of address space
for additional subnets.
Obviously if in your example the size of the subnet
is the same size as the address space,
then you're gonna have to create more address space.
But in my case, I do have room.
So the first thing we need to do is create a gateway subnet.
So I'm under Subnets,
and I'm gonna press the + Subnet.
And we're gonna create a subnet
for our virtual network gateway.
So under Subnet purpose,
I'm gonna choose Virtual Network Gateway.
These subnet gateways
have a name of GatewaySubnet.
So it's chosen the next available starting address
with the appropriate size.
And then I can say Add.
All right, so this is the location.
The gateway subnet is where we have to deploy
a virtual network gateway.
So I'm gonna go back to the home screen,
say Create a resource.
So we're looking for virtual network gateway,
and so we'll create a virtual network gateway.
So we're gonna call this vnet2
because it's gonna live in TestNet2.
We'll deploy this first one into the West US 2,
which is where the network is.
We're using a VPN-type gateway.
Now, we have a number of SKUs to choose from,
from Gw1 up to Gw5.
We can flip over to the Azure documentation
for VPN gateways.
And we can see for VNet-to-VNet tunnels,
it's ignoring Generation1
and going down to Generation2,
there are limits on the number of tunnels
that we can create.
So Gw2 and Gw3 are limited to 30,
and Gw4 can support up to 100.
So obviously we don't need a big tunnel
just for this demonstration purposes,
we can pick the Gw2 offer.
So I'm gonna put this on NewTest2,
which is the one that we were dealing with,
the gateway subnet automatically selected.
And because we're doing these virtual networks this way,
we do have to create an IP address for it.
So this is going to be, you know, vnetgw2.
We'll leave the default.
We also should create a secondary public IP address.
And I can call this second.
So we're gonna leave all of the defaults here
for this internal VNet-to-VNet communication.
Review and create.
Now, we're gonna leave that,
we're gonna go back to our virtual networks
and to our other network is in Japan East.
And one thing I didn't do
was create the gateway subnet for that.
So I'm gonna go and just create a virtual network gateway,
and say Add.
Then we go back to Virtual network gateways,
not ExpressRoute, but VPN gateways.
And we'll create VNet3,
which is gonna be in the Japan region
because it has to be in the same region.
Remember, we're doing VPN types,
we'll leave the Gw2 SKU.
Now we can choose our Japan network from there.
And we'll give it an IP address, a name.
We also call the secondary address a name.
Leave all the rest the defaults
and say Review and create.
And so that'll create the second gateway subnet
in the Japan region.
All right, so that took about 22 minutes.
The other one took about 25 minutes.
So now we have two VNet gateways
running on two different VNets.
So we go into Virtual network gateways.
Under VPN gateways,
we can see we have two of them
running in the two regions.
And when we come back,
we're going to connect these two virtual networks
through their VNet gateways.


### 📺 Lesson: Adding a Network Gateway Connection


All right, so in the last video,
we created two virtual network gateways,
one in West US 2 and one in Japan.
Now before I connect them, I'm gonna have
to make a little bit of a change.
Right now both VNet gateways have the same ASN
and so connecting them using BGP is going to fail
because they have the same ASN.
So I'm going to change the ASN
for the Japan VPN gateway.
So I will go into configuration,
change that number, and say Save.
So in this updates, we're gonna be able
to use BGP to connect them.
So I'm looking at the gateways I've created
and what we're gonna do is we're gonna create a connection
from vnet2 to vpn3 gateway,
and then we'll create a connection from vpn3 to vnet2.
So I go into the virtual network gateway
and I go under Connections.
Right now there are no connections and I'm gonna say Add.
Now, we have a bit of a challenge
in that the connection has to live
in the same region as the VNet.
So I'm going to create this
in my resource group.
I'm gonna create a VNet-to-VNet connection.
Now, we do have this option for bidirectional connectivity,
but again, the problem is if you're trying
to create two connections at the same time,
both of them are going to be created in the same region,
and our challenge here is that they have
to be created in two different regions.
So I'm gonna create the West US one first,
West US 2, and I'm gonna call this vnet2tovnet3.
That's the name of the connection.
And so this is a one-way connection
from West US 2 to Japan.
And so I'm gonna pick the West US as the first,
and I'm gonna pick the Japan as the connection.
Now, we have a couple of different authentication methods,
one of them is called the pre-shared key, PSK,
and that's just like a password.
And so I'm going to hard code a password in here.
I could create a certificate in a key vault,
and that's a more complicated way
of authentication, of course.
Now I'm gonna leave the defaults,
except we did change that ASN number
in order to be able to use border gateway protocol.
The big advantage of BGP is that it allows
for automated sharing of the resources
in each network to the other.
Instead of having to manually set up routes
to say that if somebody wants
to reach something in the Japan network,
then you have to create a routing table,
this is gonna be automatic.
Now, it is telling me that I need a standard SKU
but I believe I do have a standard SKU.
So that's not really an issue.
And I'll leave all everything else as the defaults.
And I'm going to say Review + create.
And then say Create.
Now I'm gonna let the deployment for this run.
And while it is running,
I'm gonna go to the Japan VPN
and go under connections.
And I'm going to say Add.
Again, this is the ability for devices running
in the Japanese network to find
and connect to devices in the West US 2.
Again, it's a VNet-to-VNet.
I have to give this a name.
I'll call this vnet3tovnet2,
and this is where I choose the Japanese network connecting
to the American network.
Give it a password, enable BGP,
and say, Review + create.
Let it validate, and say Create.
Now, if the two VNets were running in the same region,
we could do the bidirectional connection.
But again, the connections have to be made
in the same region as the source network.
We'll let that run too.
So if I go into vnet2,
which is the last one we were working with,
and under Connections,
and I say Refresh,
now I can see that the vnet2tovnet3 is starting up,
it's in an unknown state,
and vnet3tovnet2 is still being created.
So that's in an updating state.
We do need to wait until this is successfully connected.
And while that's running, let's talk about why.
Like, we have a couple of options here.
One of them is peering.
Now, peering is being charged per gigabyte.
And so as data is being passed from West US 2 to Japan,
it is being charged for that connectivity twice.
So the leaving of the US is being charged at one rate
and the entering into Japan is being charged
at a different rate.
So effectively, you're paying double the connectivity,
the traffic charges, one for leaving and one for entering.
With a VPN connection, you're paying a monthly charge
for the VPN, so you're renting this virtual device,
and you're only paying for the egress charge,
not for the ingress charge.
So it's effectively one half of the bandwidth rate
for this VPN connection.
But you are paying a fixed monthly rate for the device.
If you already own the devices,
let's say you have site-to-site VPNs
or express route VPNs set up,
then you're not paying anything extra
for this VNet-to-VNet connectivity
and you're saving half of the cost.
So it's depending on the volume
of traffic between these two regions,
it could be more cost effective
to set up a VNet-to-VNet tunnel using VPN gateways,
and especially if you already have
the devices running for other purposes.
So you'll see vnet3tovnet2 is now set to Connected,
and we're still waiting on the second connection
to be established.
And actually, the last thing I'll mention
about the advantages of this
is you can use Vnet-to-VNet tunnels connections
across different subscriptions.
Now, you can't use it using the portal,
like we saw it filled it in by a dropdown.
But you can set up this connection
if you know the fully qualified resource ID,
and you can do that using, you know,
deployment scripts or command line utilities.
So that's an option too.
You aren't restricted to your own subscription
for setting up these connections between VNets.
So this is the end of the section talking about VPNs
and VNet-to-VNet connections as well as peering.


### 📺 Lesson: Azure DNS Services


Tutor: So let's do a quick recap of what the DNS is.
DNS stands for Domain Name System,
and this is the way that domain names
that we may remember
are turned into IP addresses.
So if you enter microsoft.com into your browser,
that resolves to this IP address,
and you don't have to remember that address.
The other important thing is, of course,
the address can change.
Let's say you wanna move servers
and so you create a new server with a new IP address
and all you have to do is update the directory
to give the new address,
and then people will start going to that machine over time.
There is some complexities to the global DNS system
and how things are cached,
and things are not updated instantly around the world,
and things like that,
but we don't have to worry about that for now.
So the DNS resolves human-memorable domain names
to non-memorable IP addresses.
Within Azure, you have a number of options,
you can obviously provide your own DNS services
hosted elsewhere, maybe your registrar,
maybe on your own premises.
You can use the Private DNS Services within Azure,
we'll talk about that.
You can use a public DNS service that we'll talk about,
and there's even a domain, app domains,
which we'll talk about.
So the Bring Your Own DNS
or the externally hosted domain name server
is basically the custom domain,
so it could be mycompany.com,
gets resolved to an IP address
before that traffic reaches Azure.
So the user enters yourcompany.com into their browser
and some other service, which could be your registrar,
could be hosted at your own site, does that work,
and then the traffic that comes to Azure,
already has that resolved, pretty straightforward.
Now the total opposite of that is the Private DNS,
where you have a virtual network inside of Azure
and you wanna resolve things to various domain names,
but it's not publicly accessible.
And so you can basically,
that's the key to know about that
is you have servers within your own environment
that may have their own names for things,
and it's not available to anyone outside of Azure.
Now, I like to say there are no rules,
there are rules, but there are basically no rules,
you don't have to register this custom domain
with any registry.
That means, if you wanna be cheeky as the British say,
you can use microsoft.com
as your own private DNS,
you can name your servers,
database.microsoft.com,
website.microsoft.com,
something else .microsoft.,
inside your Azure Private Network.
Again, it doesn't affect anything outside of your network,
so what that does is it actually might break some things
because if your web server wants to go to microsoft.com
to do an update, for instance,
then you've overridden the DNS with your private DNS.
That is more commonly done for
dev.local, production.local, staging.local,
you can create labels for servers
that only have private IP addresses
and don't have public IP addresses.
The Public DNS, it's very similar to the Bring Your Own DNS,
it's just working like your register would,
but it's available within Azure.
We have a video coming up
talking about these things, demonstrating them.
And finally, there is something called
the Azure Domain Services,
where you can, if you need a domain,
you can pay money for a custom domain,
yourcompany.com if it's available,
and associate that with a an Azure App Service.
So those are the options
currently within Microsoft Azure relating to DNS,
in the next couple of videos,
I will demonstrate to you private, public,
and also the domain services.


### 📺 Lesson: Create a Private DNS Zone


Instructor: So we're gonna start with the private DNS.
Let's start for, we're looking for DNS zone.
We don't have any,
so we're going to create a private DNS zone.
Doesn't need a resource group.
I'm gonna put it into a new one.
Now, in order for the instance to be valid,
it has to have two or more names with a period in between.
And so remember I was saying in the last video,
you could have like dev. Local, production.local.
Here in this example I'm putting DNS demo.local
and it's only gonna be valid for me.
If my friend wanted to access this
and he didn't have access to this virtual network,
then he's not going to be able to see this domain.
So it can be anything.
If I wanted to configure my DNS already, I could,
but I'm not going to do that.
I'll do this one at a time here.
So let's create the zone.
Let that run.
All right, I can say go to resource.
Now, in order for this to be useful,
it's gonna have to be associated to a virtual network.
So I'm going to create a virtual network here,
put it into my existing thing.
I will call it Dina's demo Vnet.
I'm not going to be too concerned with the encryption
with whatever range of IP addresses it's chosen
'cause this is just a demo.
And say create.
All right, so we have an empty virtual network.
We can obviously go to our DNS zone
under DNS management
and we can associate our brand new DNS demo vnet
with this particular DNSO.
I also wanna enable auto registration
in this particular case,
which means that as you create virtual machines
and attach it to the network,
it automatically gets added to your DNS here.
So I'm gonna say create.
While that's going, I'm going to demonstrate this.
I'm going to create a virtual machine here,
put this into my resource group.
I'm going to leave this as simple as possible.
Now, the only thing I care about is it's gonna be attached
to the virtual network that's using the private DNS.
So I'm going to say
I was to disable boot diagnostics,
and I say review and create.
So we'll let this VM create, come back in a second.
I always find it interesting how fast this goes
in which we basically have a virtual machine
available to us in 21 seconds.
That's incredible.
But we're not concerned about the VM at this time.
We're gonna go back to the DNS zone
and we're gonna go into the records.
And we can see that the VM that we just created
is already registered to this DNS zone.
So what this means is internal to this network,
we can refer to this VM as DNS demo-vm
'cause that is the automatically given DNS,
or we've got this .dns.local as a name.
Now the fact that we're auto registering
doesn't really add us a lot of convenience
because if you know the full name of the vm,
then you don't need a private DNS in order to access it.
But what becomes interesting
is if this is the dev machine, okay,
then you can add a custom name, dev.dns,
name DS demo.local,
and you're going to then have it as the,
I think it's 10.04 was the number, if I remember it.
It is.
So now I have dev.dnsdemo.local
and that's much easier to remember.
And so no matter what this VM
and even if this VM gets destroyed and gets re-added
and the IP address ends up changing and all this stuff,
I've got a consistent private DNS name
that I can refer to it as.
So that's the essence of the private DNS zone.


### 📺 Lesson: Create a Public DNS Zone


Instructor: With the public DNS service within Azure,
also known as DNS zones,
you can take your public domain name,
mycompany.com, for instance,
and have Microsoft Azure
determine which server's responding to which names.
So these are called DNS zones.
We can create this as a new domain.
So let's say you,
again, you can't use Microsoft Azure
to register the domain,
but if you already have it and you have mycompany.com,
you can create this as a zone.
Let's not upload the contents of that yet
so it's gonna be created with zero records.
Now, in order for Microsoft Azure
to be recognized by anyone else
as the owner/manager of this domain name,
you're going to have to provide these name servers
to your registrar.
So you go to your registrar,
whatever company you use to register the domain,
and you're gonna provide all four of these,
.com, .net, .org, and .info,
as name servers, at least the first two,
but up to four for maximum redundancy.
Now, just like with the private DNS,
what we end up with are record sets.
And so just like with any public registrar
having a name server service,
you can add your A records, your CNAME records,
your Mail MX records,
TXTs if you need.
So Microsoft public DNS supports all of these record types.
And whether or not the servers are hosted by Azure
or not hosted by Azure,
it has to have a public IP address.
There's no point having a public DNS
pointing to a private address.
It's not gonna work.
So pretty much, this is how we're going to create records
within our public DNS.
Commonly, it will be for www,
it'll be for the @ symbol
which represents the root of the host.
You could have your mail server being mail dot
or FTP servers, FTP dot.
You'll see this is how subdomains are added
to your main domain,
and Microsoft Azure can handle this for you.


### 📺 Lesson: App Service Domain: map custom domain to an app service


Instructor: So one of the requirements of the exam
is to associate a custom domain name with an app service.
If I go into this app service, which I just created,
you can see that it has a name,
and Microsoft has appended some random letters to it,
in order to make it unique,
because finding a unique domain name
is very difficult these days.
So it's all of these letters,
.canadacentral.01.azurewebsites.net.
This is not something you wanna share with clients
or with important people,
maybe your coworkers, and that's about it.
So how do you associate this with a custom domain,
which could be mycompany.com?
Well, there's at least three ways to do this,
and I'll talk about that.
The first way, we just saw a glimpse of when we created a,
our own DNS Zone, Public DNS.
So if we went into the record
and we added
a CNAME record,
which is a link to the subdomain,
and I called this mywebsite.mycompany.com
or more commonly www, right, mycompany.com.
I can then paste that full website URL,
into the Alias section,
and that will effectively redirect
the domain www.mycompany.com to this Alias.
That's one way to do it.
You can do this also in your own hosted DNS.
If you're using your registrar's DNS,
you can do the same thing, just this do a CNAME.
The second way to do it
(mouse clicks)
is to go into the web app
and under Settings,
we have Custom Domains.
(mouse clicks)
Under Custom Domain,
we can, under, All Other Domain Services,
we can add our mycompany.com.
(keyboard clicks)
And it will suggest to us that we can go to our registrar
and we can add the A record,
and we have to do this TXT to prove that we own it.
And if we do that, it's going to respond to mycompany.com.
It needs to, because the IP addresses are shared,
it needs to know what addresses to respond to.
So to get this A record, which is without the www,
you need to do it this way, okay, for other registrars.
You can also do this using the Azure Public DNS
for the A record.
If you do want the www, it's just like I said,
a CNAME record is an option.
But you, again, we go in here,
we put this into a CNAME record, as well as this TXT,
to prove that you own it.
We also have an A record option for this www,
where the host contains that.
So that's the second way that you can associate
a custom domain with a web app.
The third way, I think it's the way that Microsoft
wants us to talk about,
which is this concept of the App Service Domain.
Now the App Service Domain is basically,
a Domain Registration Service within Azure.
I can even close that and just say,
Buy App Service Domain.
Now, this is where I enter some text,
and it has to see if this domain is available.
(mouse clicks)
Now, if I enter something that I know is available,
then it's gonna say the domain is available.
If I enter something that is likely not available,
then it's going to basically make some suggestions for me.
We can, you know, azzone, azfit,
things like that.
So we can use this method to register a domain.
It's 11.99
per year to register a domain,
and that'll get associated with our app service as well.
So you have three ways of associating a custom domain
with an app service.

