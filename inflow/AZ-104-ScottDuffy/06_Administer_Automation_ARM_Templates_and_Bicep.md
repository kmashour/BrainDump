---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "06"
title: "Module 06: Automate Resource Deployment with ARM Templates and Bicep"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 06: Automate Resource Deployment with ARM Templates and Bicep

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** ARM Templates Syntax, Template Specs, PowerShell Deployment, Custom Script Extensions, Existing VHDs, Azure Bicep Authoring & Deployment in VS Code, ARM Decompilation to Bicep, VM SSE & ADE Encryption  
**Line Range:** Lines 10140 – 11786 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


### 📺 Lesson: What is an ARM Template?


So one of the requirements of this AZ 104 exam is a whole section on understanding Azure Resource Manager
templates and Bicep files.
And so we've got this whole area that we're going to talk about.
So we're going to start off talking about the Azure Resource Manager.
Now what what is it.
What is the Azure Resource Manager.
Well the Azure Resource Manager is the deployment and management layer for Microsoft Azure.
Even if you deploy resources using the portal or you're using the SDK or or Rest APIs, underlying everything
is the Azure Resource Manager.
To demonstrate this, I'm going to create one of the simplest resources that you can create, which
is a resource group.
So I'm going to just call this new RG.
And I'll go to the Review and Create tab.
This is literally one of the simplest resources that you can create at the top here it says automation
link.
When I click it, I'm taking over to the template.
So this is if I was to hit the create button.
This file would be saved into Azure in my account and deployed.
So I'm going to copy the content and let's discuss this content.
Now I'm going to use what's called a JSON viewer.
Lots of websites can do this.
To break down this JavaScript file and so that we can understand it clearer, I'm going to go back to
the viewer tab here so we can see that the JSON file, the ARM template has two top level properties.
And this one has four objects and or arrays of objects embedded in it.
So dollar sign schema, mandatory property content version, mandatory property parameters and variables
we'll talk about in a second.
These are optional but we do have to have resources.
This particular JSON has only one resource called zero.
And when I go into it I can see that it says type Microsoft resources slash resource groups.
So this JSON file, if I was to deploy it would deploy a resource group.
It gets the location and the name, any tags any properties.
It gets all from parameters.
So if I go back up to parameters I can see there are three parameters.
And this is what I would have passed in when I created this.
Now in the JSON file the template file it just defines the type.
If I go back here and I look at parameters.
I can see the values.
So this is new RG east US and no tags.
So this is what I, I set up when I was creating this resource group.
It's a separate file.
Parameters and template are two different files.
Okay.
So back to the resource here.
Now this particular resource has listed.
Let's go into the template.
It lists outputs empty.
This is an optional this is an optional element of the JSON.
So we just saw the one of the simplest uh ARM templates that you're ever going to see.
That's creating a resource group.
If I wanted to, I could save this.
There's a a way to in this particular case, download this and there's a way to deploy a resource group
using the command line.
Now resource groups are sort of special because they have to be deployed at the subscription level.
But um, if I was deploying a resource without the group, uh, I could I could do a deployment like
this so I could download this and I can run this repeatedly.
This could be become if I needed to create 100 resource groups, I can do it programmatically using
this ARM template.
Now, if we were to go to a more complicated resource, I was looking at virtual network a few minutes
ago, and you might think that virtual network would be pretty simple.
It's just got the network and it's got the subnet and you think, oh, it's just two elements, but
it's actually not.
It's got an encryption element.
It's got bastion element, firewall, DDoS protection.
These are all optional things that could be included in a deployment.
So this is the subnet some tags.
And if I look at the automation template and I copy the content.
And we go here and we paste the content.
You're going to see a much more complicated JSON.
So if I go under resources there are 13 resources deployed in this one file.
You've got of course the virtual network itself.
But you're also going to have um, if bastion was selected, there will be bastion.
If firewall was selected, there would be firewall elements.
DDoS has its own section.
The subnet is going to be in there as well.
Any kind of Nat if you're using a Nat gateway.
So there's just a lot more complexity.
It's a lot harder to read, but you can still make out, you know, there's still the readability in
terms of the type and then where the name comes from and things like that.
So yeah, there's there is an example of a, a virtual network.
Now I'll show you I'll show you something interesting.
So if I was to create this.
Now we can see that the resource got created very quick.
I'm going to go to the resource group and under settings is deployments.
And so I can see that this ARM template in eight seconds was deployed successfully and I can click on
it.
And I can absolutely see the ARM template that was used to create this.
So even after the fact, even weeks or months later, I can go back and look at exactly what was selected
in order to create this thing.
And if I modified it, there would be additional deployments.
So there would be, um, two and three and four different deployments listed under deployments.
So every change that you make would become an ARM template deployment.
And it gets listed in this deployment settings.
So what we saw here is that um we've got our infrastructure represented as code.
This is sometimes called infrastructure as code.
And this allows you to deploy things like VMs network storage in a repeatable and consistent way.


### 📺 Lesson: Read an ARM Template


Instructor: So let's have a look
in a little closer detail
the contents of this resources section.
This really is the powerhouse of the ARM template
and what is doing the work.
Now, maybe the network interface card
is not the first place to start,
but we can see that a network security group
is being created here.
We can see that it's got a name
and that name is being passed in through a parameter.
We can see that it has a type.
All resources have type, most of them have names,
in terms of Microsoft.Network/networkSecurityGroups.
Now, you don't need to know this wording for the test,
but it will help you to be able to look at this
and kind of understand what it's trying to do.
Like I said, it is supposed to be a human-readable format.
We don't need to worry about the apiVersion,
but we can see that the network security group
is gonna be deployed into the same location,
which is the default location
that was passed in as a parameter.
And finally,
in order to create the networkSecurityGroupName,
we need to create a networkSecurityGroupRule.
And the rules are a separate parameter.
And so, if we go over to the parameters file,
we can see that networkSecurityGroupsRules is an array.
So there's a value and it starts with the square bracket.
That's an array.
And really, the only rule that's being passed in
is the RDP port, where we want to allow TCP port 3389
inbound from all source addresses
to all destinations on the network.
Obviously, this could be quite restrictive
if you wanted it to be,
but it's an example of a netWorkSecurityGroupRule
that's just being passed in as a parameter.
So this single resource, if I was to copy that,
put this into our empty template here.
This would be enough to create a networkSecurityGroup.
And if that's all you needed to do,
I would have to hard code,
let's hard code the networkSecurityGroupName.
So there's the string for that
and the location, there's a string for that.
And the security group rules.
And as we saw, that's an array, not a string.
This alone would be enough
to deploy a new network security group into Azure,
if all I did was do this.
So you can see that these templates
do not have to be complicated if you don't need them to be.
So going back to the template,
we can see that the virtual network, which is vNet,
that's also can be quite simple.
It's got a type, a name, location,
and the properties are gonna be the IP address range
and the subnets.
And in this case, it's just the default subnet.
I suppose if we go down into here,
we can see the subnet name comes in as default.
The addressPrefixes is an array.
So it is worthwhile for you, from an exam perspective,
to at least be able to look at this and go, okay,
I understand where that's coming from.
Knowing the portal, this is the minimum required
to create a virtual network, right?
All of those other things are optional,
are not part of the creation process.
Public IP address, right?
Has a name, has a sku, there's the allocation method.
So just being able to scroll through this file,
read the types, understand things like dependsOn,
so this resource would not be deployed
until these other two resources
have been successfully deployed.
So that's how it knows
not to do the one thing before the other.


### 📺 Lesson: Modify an ARM Template


Instructor: So this video,
we're actually going to modify this ARM template
before deploying it.
Now, I thought about what I wanna do
in order to modify this
and I think what I'm gonna do is I'm going
to basically not deploy one of the resources.
So I've chosen the public IP address
as being the resource that will not be deployed.
We're not gonna have a public IP for this virtual machine.
It'll only be a private IP address.
So I can choose this whole section
that is a public IP address, and I can click delete.
And I'll even take away the blank line.
Now, what are the implications
of not deploying the public IP address?
Well, there actually is a dependency.
So if we go up to the network interface card, we can see
that publicIpAddress is one of the dependencies.
So we just have to remove that as a dependency
as it'll never be created
because it's not part of this file anymore.
So now we've removed it as a dependency.
The next thing we have to do is we have to remove it
as a parameter.
So under the network interface card properties,
we have this publicIpAddress that's under ipConfigurations.
So I'm going to actually remove the publicIpAddress attached
to the network interface.
Okay, so if I make sure my curly brackets,
there's two opens and two closes,
then this virtual machine network interface card
will not have a public IP address attached.
So that's pretty straightforward in terms of modifying this.
Now, you know, this can get quite complicated, obviously.
So if I wanted it to have two public network interface cards
and attach both interface cards
to the same VM, there, I can, you know,
copy the section and I can, you know, set that up
in the various sections of the resource management template.
But I'm just gonna keep it simple for now.
We've removed the public IP address.
So I think I've saved this.
It's on my local, and I think what we're gonna do
is we're gonna try
to get these resources deployed into Azure.
So why don't we do that next?


### 📺 Lesson: Deploy an ARM Template via Template Specs


Instructor: So we're back in the Portal.
We've downloaded the templates and the parameters file
to our local and made some changes to it.
Now what do we want to do?
Now we could save the template
that Azure downloaded to us to a,
what's called, a template library.
We could schedule this for deployment
right from this screen as well.
But we've modified this template.
And so really what we want to do
is we want to create a new template
in the template library.
Now, the other thing I should point out
is there's the PowerShell and CLI scripts
that can be used to deploy a template.
Now, it's pretty straightforward.
It's a single PowerShell command.
So if I said New hyphen AzResourceGroupDeployment,
that is the command that's going to set
the ARM template and the parameters file
out to be deployed.
But we're now gonna skip ahead.
What we're gonna do is we're gonna cancel out
of this creating of a virtual machine
and go to the Azure Portal home.
Now I'm gonna go into the search box,
and I'm gonna say template.
Now, Azure has recently introduced
a new thing called template specs.
Templates still exist if I go into Templates.
Now, I've never used this before on this subscription.
My other subscription has lots of templates to show.
But it says in headlines,
Templates will be retired after March, 2025.
And so we recommend converting your existing templates
to templates specs,
which makes it easier to share and link templates.
So we'll go into Template specs.
And we can see a couple of options.
We can create a blank template.
And then we can just copy and paste our template.
Or we can import a template.
So ARM Manager Template File.
And there's this little folder icon.
I can select my template file and say import.
So the template body has been populated
with imported content.
But some additional fields must be provided.
And we can see here
that the resource group is one field
that was not part of the original template,
but we should provide.
And so I'm gonna call this vmarmdemo.
Location was already part of the template.
And we can give this a description.
And we can version this.
And so there's basically-
This is version 1.0.
And this is sort of a brief demo.
We can be very detailed or not.
Next, we'll be able to see the template
that we're importing.
And we can actually see that the IP address,
so if we look at the NIC card virtual machine,
probably, it's up here.
Look at the NIC card
that the IP address is no longer dependency,
and the public IP address
is no longer part of the properties.
So this is the template that we modified.
We can make further modifications here. We won't.
Set some tags to it.
Say review and create.
What it think it's missing?
Oh, we have to give it a name, of course.
So this is az104 new demo.
Great. So basically, now we're gonna save this.
Now with this type,
it's basically turned a template into a resource.
And that resource can then be shared.
You can set permissions on this and things like that.
We can see the template specs.
If I go into the
ARM,
the resource group,
and I say show hidden types,
we can see the template spec is now stored as a resource.
That means we can share it with others
and give it access control and things like that.
So now we have a template that we can do things to.
And one of the things we may want to do
is, obviously, deploy this template.
So we're in the template spec resource.
And we can create a new version.
We can edit it, and we can deploy it.
So I'm gonna just go ahead and click Deploy.
Now, one of the challenges,
always been a challenge with ARM templates,
is we do end up with a lot of parameters.
You see all the parameters from the ARM template
are empty.
And there is no import parameter file option.
I don't know why Microsoft doesn't allow you
to import a parameter file.
It seems like an oversight to me.
It's always been like this.
But
what this forces us to do
is to go to our parameters JSON file
and copy and paste into it.
So I'm going to do that.
And I'll pause the video,
and I'll fill these values in.
All right, I've done my best here
to copy right from the parameters file
all of the values into the fields.
For things that are raised,
I maintain the square brackets.
For things that are strings,
I don't include the quotation marks.
And of course, I had to choose the VM size
using that picker.
Now I can say review and create.
Validation passed.
And now I got this extended terms and conditions.
But I can see all my settings.
And I can click Create.
Now by deploying ARM templates in this manner,
I've not really saved myself the,
in terms of automation,
like this is obviously a manual process
in terms of deploying templates so far.
But if I had settings that are always gonna be used,
what I've done is I've saved my default VM configuration,
and all I have to do is provide values
for things that might be different.
And this type of thing could all clearly be streamlined,
because the names of things could be set up as variables
and not as parameters.
So we could certainly reduce the amount of things
that need to be pasted in.
Or maybe there's a default network security group rule
and not have the user provide it.
But now you can see I'm deploying the virtual network,
the storage account, the network interface cards,
things like that.
So it's just like a regular deployment.
But at least this time,
the instructions have been provided by JSON file.
All right, so we can clearly see
that our resource group containing our virtual machine
and the network security group
and all that stuff has been successfully deployed.
So that is one way to deploy an ARM template.


### 📺 Lesson: Deploy an ARM Template Using PowerShell


Instructor: Now, I'm gonna stop
and ask you a question here.
What do you think would happen
if I was to deploy the same ARM template again?
That is, we have a resource group
that has all of the resources running inside of it,
the VM, the network security card, and all of these things.
But I was to run the same process
that we just went through a second time,
would it fail,
or would these resources be destroyed somehow,
or what would happen?
Well, in actual fact,
when you do an ARM template deployment again,
it skips over resources that are already existing
and have the same properties, right?
So the same disk created with the same name,
with the same settings,
would actually just get skipped over.
And so none of this would be, in fact, redeployed.
To show this,
I'm going to actually delete this virtual machine.
So I've got the VM
that we just created with this ARM template
and I'm going to hit Delete just on the VM.
Now, the network interface card, in this case,
will not get deleted.
The operating system disk will get deleted.
I'm okay with that.
That's two resources that are going to end up
being deleted out of the eight.
And I'm gonna say OK.
So I'll give that a few seconds to delete.
Now, what I'm gonna do then
is I'm gonna go into the Azure Cloud Shell
as a way of being in PowerShell.
We've been working within my local machine PowerShell
up until now,
but we will demonstrate this one from the Cloud Shell.
So we've clicked on the greater than sign, underscore icon
on the top,
and it's now starting up a PowerShell terminal for me.
All right.
So I'm gonna clear this.
Before we can continue,
I should point out that our ARM template file
has a null admin password.
So we are gonna have to provide a password
for the admin user
before we can upload the file into the Azure Cloud Shell.
And what we need to do to start
is we need to upload our template JSON
and our parameters JSON from the local machine.
So this file with the up arrow, down arrow,
and I'm gonna say Upload.
I've chosen the two files, parameters and template.
And then you can see the little toast
telling me that the file uploads are complete.
And then I can actually say dir,
and I can see the template JSON.
And if I do it again
for the parameters file,
I can see the parameters successfully.
And now we have the parameters
and the template on the Cloud Shell local disk.
Now, I'm gonna use
the New-AZResourceGroupDeployment command.
We're gonna have to deploy this into a resource group.
It's called vmarm...
It's called vmarmdemo.
And the template file is template.json.
The parameter file is parameters.json.
So this command, when posted into the Cloud Shell,
is going to deploy the template file
passing in the parameters file
into the resource group vmarmdemo.
So I'm gonna copy this.
Let's clear this.
So I'm gonna paste,
and you can see the...
Now, it's trying to autofill,
there's an IntelliSense here, predictive IntelliSense,
but I'm not going to use it.
So I can paste in the command on a single line here.
I will wait a little bit for this virtual machine
that we are trying to delete
for more than six minutes to actually be deleted.
So we'll pause this for a second.
All right, so we finally have the virtual machine deleted.
We can see here that the VM is gone.
The operating system disk is also gone.
And I believe the schedule for shutting down the VM
has also been taken away.
So those are three of the eight resources
that have been deleted.
So what we're gonna do
is we're going to go back to the Cloud Shell,
and we're gonna do
this New-AZResourceGroupDeployment command
into the same resource group with the template file,
the parameters file that has the password in it,
and I'm going to hit Enter.
And we're hopefully going to see our deleted resources
to be restored without any conflicts
to the resources that already exist.
So our deployment are completed
listed as an incremental deployment,
all of the properties and the outputs.
So let's close this up.
If we go back to the the resource group in the Portal
and we click Refresh,
we now have our virtual machine
and the virtual machine disk back with us, okay?
So that has been basically entirely recreated.
So deploying an ARM template twice or three times
really doesn't disturb resources that already exist
and can restore resources that have been modified
or accidentally deleted in some way.
And as you saw, you can do that
using the New-AZResourceGroupDeployment command.
You can also go into deployments,
I think I've said this before,
but we can see that
deployments are listed originally from a template,
and now doing this update that we did manually.
We could have also given that deployment a name
on the command line if we wished.


### 📺 Lesson: ARM Templates Capture a Point in Time


Instructor: So, we're wrapping up this section
on ARM templates and we've seen
that we can capture an ARM template
when we're creating the actual resource
in the Azure Portals.
Then, we can download a template.
We can modify that template.
We could even create templates from scratch if we wanted to.
Using template specs to deploy it.
And even the command line
with the new AzResourceGroupDeployment cmdlet.
And all that stuff is a way that you can create
ARM templates and use them for automation.
I showed you in the last video,
that the deployments get logged
and basically they'll end up here
in the deployment section of the resource group.
Now, I wanna point out a couple of limitations to this.
So, first of all, I believe there is a maximum number
of deployments that will be logged here.
So, if you are deploying
to the same resource group frequently,
let's say you are deploying it every six hours
and you have this for years,
then there's going to be basically a max limit
to the number of things that will be listed here.
And not every deployment
contains every resource in the resource group.
So, I could create a deployment
that only deploys a network interface card,
and that would be separate than the other two deployments
and there would be no unified ARM template
for everything that's in this resource group, right?
So, each deployment is incremental.
Another issue is that the deployments
capture a moment in time.
So, I deployed this at close to 5:00 p.m. today.
Now, if I go to, let's go to the virtual machine.
So, this is the VM here.
Now this VM is a standard B1s, right?
A very small VM.
Let's say I was going to the size setting
and I decided to upgrade to the B2s, right?
Twice the CPUs, twice the RAM,
twice the temp storage, twice the fun.
So, I'm gonna click Resize.
Now again, behind the scenes, this is using ARM
to make this change, but it's not actually deploying
an ARM template,
but it is using the Azure Resource Manager model
to communicate with the virtual machine.
All right, so, we have upsized the VM from B1s to B2s.
Now, if I go back into the resource group
and I go back into deployments.
First, you'll notice that the resize
did not get stored as a deployment,
so that any kind of settings change that you do
is not actually going to be captured as a deployment.
And the second thing is,
if we go into one of these deployment files,
we can see what happened,
we can see how long it took, and we can see the templates.
So, here is the template.
But what we don't get, so this is the parameters.
And what we don't get is we don't get the new options.
So, if you make a change to a virtual machine
or any other resource,
and you go back into the deployment
that you previously made,
the parameters still show the original settings.
So, this is not a way of capturing
the current state of Azure,
the current state of your resource group.
This captures a point in time.
So, the day and time that you deployed this template,
that's the template that you can make a copy of.
What you can't do within the Azure Portal
is create a brand new ARM template
based on the new settings of that virtual machine.


### 📺 Lesson: ARM Custom Script Extensions


Narrator: Now I've mentioned
that when you deploy a virtual machine,
by default, what you're getting is the Windows or Linux,
or virtual machine with the operating system
and no additional software.
And you're actually going to have to do some work
in order to get that virtual machine
to install your application.
Well, one thing that you can do
to get this additional work
is using something called a Custom Script Extension.
Now in this case, we're looking at ARM templates,
the traditional JSON ARM templates,
and we're looking at ways that we can pass parameters to it
for it can run a script
and do some extra work on creation.
So I am on the Sample Code website from Microsoft Learn,
and I am looking for the samples
that contain the words custom script using ARM.
And you'll see one of the results is Multiple Windows of VMs
with custom-script.
There's lots of others, Ubuntu,
Virtual Machine Scale Set, et cetera.
But this is just an example
of deploying multiple Windows virtual machines
in an ARM template with a script that gets run.
Now I can simply click the button for it to deploy,
Deploy to Azure,
but I want to go to GitHub and say Browse code.
And I'm going to choose the azuredeploy.json file
from GitHub.
And we can see here that it's a JSON file, of course.
If I scroll down past the parameters and the variables,
we can see a traditional virtual machine deployment.
You got storage accounts, public IP addresses,
network security groups, virtual networks and subnets,
network interface cards,
and, finally, the virtual machines.
And since this is a ARM template
that is deploying multiple virtual machines,
you have this copy parameter as part of it
that's going to create multiple versions of this resource.
Okay.
Going down, we can see the extensions,
Microsoft.Compute/virtualMachines/extensions.
This extension is the install script
for whatever you want it to do.
It's a PowerShell script that you have to write
that will do some kind of work when this VM gets deployed.
And so again, the copy statement is going to ensure
that multiple VMs get this.
And as we go down, we'll see that there's a command
and that it's a PowerShell command
passing in the script file name.
So you have this script posted somewhere
and this has a URL to it.
And you're going to run PowerShell
to point to that particular file.
And so this is how you're going to get custom software
installed on, in this case,
multiple Windows VMs using ARM template deployment.


### 📺 Lesson: ARM Use Existing VHD


Instructor: So, another example
that we can use ARM templates is,
if we have an existing virtual hard disk
and we want to create a new VM
based on that existing virtual hard disk.
So, I'm back at the sample code
for Microsoft Developers' website
and I filtered down to ARM templates,
and I'm looking, in this case, for VHD.
And we can see there are several examples.
So, we can create a new VM from a custom VHD,
or we can create a new VM from a generalized VHD,
or we could create one from an existing VHD,
and I'm gonna choose the existing VHD,
just as this example.
Now, we can read through what it's going to need
and what it actually does,
but I'm gonna go to the GitHub file
and we're gonna look at it directly.
All right, so, I'm going
to go into the deployment.json file.
And we can see here we've got the parameter settings,
all of the fields that it requires,
the existing URI for the disk, VM size, et cetera
where the VNet is.
I'm gonna scroll through storage accounts,
IP addresses, network interfaces.
Of course, these are things that are needed to create a VM.
In this particular case,
we're going to be creating a compute/disks resource,
but we're going to have a source URI,
which is going to basically import the VHD
from another location.
This is an import option as opposed to creating from new.
That is the operating system disk,
this is a data disk,
so we're importing a data disk in this particular one.
And now, we create the virtual machine.
The dependency is on the disk's existing,
and we're going to pass in the parameters for storage,
for the OS disk, and the data disk.
And so, as we can see, it's pretty straightforward,
that as long as we create the disk as import options,
then we can just attach those disk
to the VM that we create as normal.
So, in this way, we are using JSON and ARM templates
to create a virtual machine based on existing images
for maybe a VM that already existed or a copy of a VM.


### 📺 Lesson: ARM Templates for Almost Everything


[No transcript available for this lecture]


### 📺 Lesson: Overview of Bicep


So in this video,
we're gonna be introducing the concept of Bicep.
Now, if you've looked at the requirements
for the AZ-104 exam,
you'll see that Bicep is pretty much treated
on the same footing as ARM templates.
So you do need to understand
how to interpret an ARM template or a Bicep file,
you need to be able to modify an ARM template
or a Bicep file,
deploy resources using either,
and export your deployment to either.
So all the requirements that apply
to ARM templates also require to Bicep.
So what is Bicep?
Well, you can think of Bicep as a domain-specific language
for deploying Azure resources.
Think of it as an abstraction layer
on top of ARM templates.
So if you've used or written ARM templates before,
then you'll know that there is sometimes
a bit of a pain to it.
So we can look at an ARM template,
we can see all of this set up with the variables
and the parameters.
We get into the resources,
we have this JSON syntax.
Now, this here is not too bad,
we've got storage accounts and IP addresses
and things like that,
but you can get into things
that have got a fairly good nesting situation going on,
like this virtual network definition
and others like this network interface card,
has IP addresses and subnet IDs and things like that.
So this JSON is not necessarily easy to read.
Bicep solves this or attempts to solve this
by being a much simpler, cleaner syntax.
And what you do is once you've written this in Bicep,
it can compile into an ARM template,
so this is why it's called an abstraction.
They're not both,
you're not passing the Bicep file directly to Azure,
it's being converted into an ARM template
and we're still using the Azure Resource Manager model
to deploy the resources.
So let's look, this is an example of a template,
an ARM template for deploying a virtual machine.
And let's look at the equivalent Bicep file.
So this is all pretty much the same thing,
we've really simplified the variables
and the parameters section.
So we just basically define something as a parameter
and we can say, what's the length
and whether this password is a secure field,
things like that, give things descriptions.
Much easier to read and understand syntax
compared to the equivalent syntax in an ARM template.
Now you're gonna see a lot of stuff that is familiar
because really this is just in,
like I said, it's gonna become an ARM template.
So if we are defining a storage account,
there's no nesting here.
You'll see the resource command here.
And basically we're defining a storageAccount
and we're passing in name, location, sku,
and what kind of storage account.
That's going to be very similar
to when you define the storage account
in this ARM template we've got type, apiVersion.
Again, the the Bicep is a bit easier to read,
but the information is still there.
And we're gonna find the same situation,
we're looking at defining the IP address,
defining the NSG,
just the same information just easier to read, less nesting.
Bicep files support all of the features
that ARM template support,
so there's no downside,
you're not missing out on anything
if you write things as a Bicep file
instead of as an ARM template.
Now, to get started,
you've got a few different ways.
There is a command line tool
for compiling Bicep into ARM template
or for reverse,
compiling it to get a Bicep file out of an ARM template.
But you can also set up your VS Code IDE
with a plugin for Bicep as well as Visual Studio.
So if you wanna be using your authoring environment
as VS Code, that's totally supported right out of the box.
So from going forward,
what you're gonna find is when you're gonna try to find
quickstarts for some of these things,
it'll be available in both.
You'll have Bicep quickstarts as well
as ARM template quickstarts
because Microsoft is now at this point,
it's been several years,
Microsoft fully supports both formats.
One easier to read better for humans,
and they all compile into ARM templates.


### 📺 Lesson: Use Visual Studio Code to Author Bicep Files


So in this lesson
we're going to write our first Bicep file from scratch.
Our goal is to deploy an Azure storage account.
Step one is to set up our environment.
I have Visual Studio code here.
And I'm gonna go into File, Preferences, Extensions,
which is Ctrl+shift+x,
and I'm going to look for the Bicep extension.
I found it as being the first one when I search for Bicep,
and I'm going to click Install.
And so this is going to install
the official Microsoft Bicep extension.
If you already have it installed, make sure it's enabled.
This is gonna handle all the syntax highlighting
and the validation.
So step two is we're going to create a Bicep file.
And we can do it here, within the extension,
but we can also say file new.
So the file I'm gonna create is called storage.bicep.
Now in the bottom right here,
we can see that the language has been interpreted as Bicep.
Alright, so our goal is to create a storage account.
And we're gonna use parameters
'cause we want this to be reusable.
We don't want a hard code values.
Parameter keyword is param
and we're going to define three parameters,
one being a location.
Now as soon as I start typing,
you'll notice that the IntelliSense has kicked in
and it is suggesting some text;
location string = resourceGroup().location.
I do actually want to accept this.
So it is this tab
in order to accept the suggestion.
And the next thing we want to do
is param called accountName.
It is also a string.
And this case we are going to be accepting
the letters st followed by a...
We're gonna accept this uniqueString resourceGroup.id.
So this is going to be the name of the storage account.
And I can control, right arrow
or tab in order to accept portions of that.
The third parameter will be for the sku.
And you'll see it's already expecting me
to look for the sku.
And so I'm gonna say skuName string
and we'll accept the Standard LRS as the sku.
Now again, IntelliSense has kicked in
and is now giving me the storage account based on those.
Now this is pretty much exactly what I want.
The account name, the location, the sku,
the storage of E2, which is general purpose,
and we'll accept the default access tier as being hot tier.
So I didn't even have to really write much code,
but the storage account has been...
Is gonna be created in Bicep using this code
that's being suggested.
Now the last thing we need to do is output the results.
And so there is an output command,
and we can see this here,
where it's taken in the storageAccount
that's being created .name
and placing that into an output variable.
And that will be output after this Bicep
turned into an arm template is run.
So this ends the file.
We have a complete valid infrastructure as code document
in just 17 lines of code.
And now we can deploy this into the next video.


### 📺 Lesson: Use Visual Studio Code to Deploy Bicep Files


So now, we have our storage.bicep file ready,
and we're ready to deploy it.
Now,
you technically can deploy this file
using a command line tool like PowerShell or CLI.
There's a CLI command
such as az deployment group create to deploy this file,
but there is a faster way
to do this inside of Visual Studio Code.
So I'm gonna right-click within Visual Studio Code,
within the file.
And I can see there's a command that says Deploy Bicep File,
and I'm gonna select that.
Now, the output opens,
and I have to give the deployments a name.
I'm gonna accept the default by hitting Enter.
Now, I've already logged into Azure,
and so it shouldn't have an issue
with me not being logged in.
I am logged in.
Now, I have to pick the subscription.
I'm gonna put this into my pay-as-you-go subscription.
And it is asking me to create a resource group.
I'm going to put this into an existing resource group.
And we don't currently have a parameter file.
I wanna use the default values that are being defined,
so I'm gonna select None.
So now,
the output window will start to contain details
on the deployment.
The output window says, the deployment has started.
And we're waiting for it to complete.
And now, it says, deployment succeeded.
You see it took about 30 seconds.
So to validate this, I can go into the Azure portal,
I can go into the resource group where I deployed this.
And I can see that a storage account,
st with a random set of letters
and numbers has been created.
And that this was the one that we just deployed using Bicep.
We can even go back
to the resource group level under Deployments.
And we can see that it succeeded with the deployment
using the name that we provided during the deployment.
So this proves that Bicep is a transpiler.
It took my clean Bicep code,
turned it into a standard ARM template,
and submitted that
to the Azure Resource Manager for deployment.
We can see this as an ARM template,
the code that I wrote as a Bicep.
So this was a successful deployment
of our small example of our Bicep file.


### 📺 Lesson: Convert (Decompile) an ARM Template to a Bicep file


Narrator: So, the process from going from a Bicep file
to an ARM template is called compiling,
obviously part of the deployment process,
but if you wanted to go in reverse,
if you want to take an ARM template
and turn it into a Bicep file, that's called decompiling.
And believe it or not, it can be done,
because, like I said before,
all functions available within ARM templates
are generally available within Bicep,
even preview functions within Azure.
Now, there is a decompile command at the Azure CLI.
So, az, space, bicep, space, decompile,
pass in the JSON file,
and you'll end up with a Bicep file.
We also have the ability with in VS Code
to do the same thing in a much easier fashion.
So, VS Code as we know, we have the Bicep extension,
and we have a number of commands.
And if we go to the top bar, the command bar,
and start typing bicep, we're gonna see a list of commands.
Here's an ARM template that we used in a prior video
that is quite complex.
It's got three virtual machines on end virtual network,
three network interface cards, and an NSG.
So, this is the setup to some load balancers
we were gonna create, and application gateways.
So, this setup contains three VMs.
So, let's convert that into a Bicep file.
Now, like I said, there's a couple ways we can do this.
We can go up to the search with a greater than sign
and we can see Decompile into Bicep
as one of the options.
There's also a shortcut.
If you right-click on the JSON file name,
scroll to the bottom, Decompile into Bicep
is one of the options.
Now, it's quite fast.
It's done very quickly.
"Decompilation complete."
I have a Bicep file now in my local file directory,
and we can also see it here in VS Code.
So, we can look at the various parameters
that have been created and the naming of it.
We can look at the resources.
Remember we have one virtual network,
three network interface cards, three virtual machines.
Here's the network security group
that contains the security settings.
There's the virtual network.
And, pretty much, we're gonna have all
of the resources properly created in Bicep format.
So, going from ARM templates to Bicep,
I think Visual Studio Code is the simplest way.
You can certainly use the Azure CLI to do it as well.
It's pretty much gonna work,
because, as Microsoft has said,
almost all functions in ARM templates can be done in Bicep,
even preview and general availability features of Azure.
So, it's fairly mappable one-to-one
in terms of what ARM templates can do
and what Bicep can do at this point.
And that's how you decompile ARM template into a Bicep file.


### 📺 Lesson: VM Server-Side Encryption (SSE)


Instructor: So let's talk about the way
that virtual machines encrypt data in Azure.
Now, before we do that,
I want to create a key vault for this purpose.
I'm gonna put this into a resource group.
I'm gonna call this,
your name needs to be unique,
and I wanna make sure this is in the same region
as my virtual machines.
I don't need this, but I'll put that to the minimum.
Now, the key for our purposes here
is that we are gonna give access to deployments
to this key vault.
So for server side encryption,
we're gonna give Azure virtual machines access to this,
and for Azure disk encryption,
which we'll talk about in the next video,
we need to give that access to this.
So might as well put arm templates in there as well.
I'm gonna leave this as all networks, no tags,
and then say create.
Now we go into the key vault
and we're gonna want to create a key.
So you'll see this message saying
that we actually need to give ourselves permission.
Operation is not allowed.
Fairly easy to do.
We go under access control.
And you say under roles,
you're either gonna want to have owner or contributor
or key vault administrator roles.
So add role assignment.
Key vault administrator. Why not?
I add myself, and say review and assign.
Now when you go down to object keys,
there's no error message.
We say generate.
Say my first key. We leave it with an RSA 2048 key.
Leave all of these default,
leave it activated, and say create.
Now one thing that I forgot to do that we need to do
is have purge protection enabled for this key vault
because it's basically enforcing
a mandatory retention period.
So you can't delete objects and purge them immediately.
This is required for virtual machine dis-encryption,
and once enabled, it cannot be disabled.
So I am under settings properties
and I'm enabling purge protection.
All right, so believe it or not,
we've created the object keys
and now we want it to have a disk encryption set.
A disk encryption set is basically gonna use this key
and it's going to have a bunch of settings for that
so you can enable disk encryption.
So this is my first disk encryption set.
I'm gonna leave that in the same region,
the same resource group.
As you can see, we have the option for customer managed key,
which is what we want.
We have the double encryption option,
and there's also confidential compute.
Then we haven't talked about that yet,
but encryption at rest with the customer managed key
is what we're going for to start.
We have to pick the key from our Azure key vault,
which we just created.
So I'll pick that, and I'll create the key.
Choose the key that we created, just the current version,
and we're not gonna select any of this.
We do have the option of what's called key rotation.
And so if we want to have this key
be regenerated every so many months,
it gets automatically taken care of behind the scenes.
We're not gonna need that for the purposes of this demo.
Say review and create.
And now create.
So we have a bunch of settings relating to a specific key
that we can use when we are encrypting a VM.
All right,
so we do need to assign permissions to this thing.
So if we go back into our disk encryption set,
it says, to associate a disk image or snapshot,
you must grant permissions to that key vault.
So I'm gonna click it
and it then does the work to grant the permissions.
So now this disk encryption set
has the permissions to the key vault.
Now, if we go and start to create a virtual machine,
under Create VM,
I can choose my resource group, give it a name.
I'm gonna leave all the defaults.
I'm gonna choose a slightly bigger one, a D2SVM,
and I'm gonna leave all the defaults.
Enter a menu, user ID, and password.
And if we've done this correctly, we go into the disks tab.
We haven't registered encryption at Host
against our account.
Now, encryption at Host is basically a way
of doing end to end encryption.
So the virtual machine itself is writing encrypted,
it's aware of the encryption,
and it's writing encrypted to the virtual hard disk,
and that carries through all the way to storage.
And you're basically involving the guest operating system
with the encryption.
This is going to be similar.
We we're gonna talk about Azure disk encryption
in the next video, but this is similar to that
where the operating system is involved in the encryption.
If we don't want to do that,
if we want it to be invisible to the OS,
we could use what is called key management.
So by default, Microsoft Azure manages the keys for you.
So it's the virtual machine hard desk
is always stored encrypted against the storage account.
You have no control over this.
The question is, do you let Microsoft Azure manage the key,
or do we, as we just went through this process,
manage our own key
where we created the key in our Azure key vault,
we can invalidate that key and create a new one
and do key rotation and things like that.
So we can associate this disk encryption set
with the virtual machine, and therefore,
now we are in control of the security key
and we are giving Microsoft Azure, essentially,
permission to use that key.
So it doesn't improve your security only to the extent
that you think you can manage your keys
in a way that satisfies your own security requirements
and not doing it according
to the way Microsoft manages their keys.
So it's a control thing, effectively.
Now, you can actually modify an existing VM.
So if I go back to, let's find my existing VM.
The VM has to be stopped in order to change its encryption.
So if it's running, you have to stop it.
But you can go under settings, into disks.
You can look at either your operating system
or your data disk or both.
Okay, we see that the existing encryption
is server side encryption with platform managed key.
And if we click it and we go under the encryption setting
for the disk itself, we have the ability here
to switch over to customer managed key and say save,
and now our existing VM
changes the key that it uses for encryption.
I'm not gonna do that either.
Just the last thing I'll touch on
is this encryption at host feature.
Like we saw, you actually have to register
in order to be able to do that end-to-end encryption.
So I'm gonna copy my subscription ID, go into Cloud Shell.
All right, clear.
So I'm gonna set the context
to the subscription ID that I've copied,
and there is a command called a register feature.
So I will just paste it in here.
You can see that it says register AZ provider feature,
and the feature name is Encryption at Host.
And so I'm really just telling Microsoft Compute
within Azure that I am interested in using this feature.
Hopefully that's enough
such that I can get access to that feature now.
So you can actually see
under your subscription activity log,
the register provider feature
has been started and completed,
and it's been 12 minutes, as I record this,
since we did that.
But if I go to create a resource,
try to create a virtual machine,
I don't even have to pick the things at this first tab yet.
You can see that it's still not registering as registered.
So I do think it takes some time.
Let's say it takes half an hour, 45 minutes
for Azure Portal to understand that you register for it.
I think we just have to wait.
Anyways, that's how you do server side encryption
through either key management with a platform,
or customer managed key, or both, or encryption at Host,
which is end-to-end encryption,
starting from the operating system level.


### 📺 Lesson: Azure Disk Encryption (ADE)


In the last video,
we saw how to encrypt disks in Azure virtual machines
using customer-managed keys.
In this video, we're using a slightly different technology
called Azure Disk Encryption, or ADE.
Now, it's important to understand the difference
between ADE and server-side encryption, SSE.
So SSE, we saw in the last video,
encrypts your data at the Azure storage layer.
This is the physical disk
being stored within an Azure data center.
ADE encrypts your data inside the operating system,
using in the case of Windows, BitLocker,
or dm-crypt for Linux.
So it's like if you had Windows on your local system
and you turned on BitLocker.
It's using the operating system
to write in an encrypted manner to the disk.
So you'll see, I have a virtual machine here.
It's a different VM than the last video,
but it's still a Windows server 2019 VM.
I'm gonna go under Settings
to the Disks tab in the left-hand menu.
And we're looking at an operating system disk,
it is a Premium SSD.
And we're using a server-side encryption of course,
Microsoft platform-managed keys in this particular case,
we're not using the customer-managed keys.
So like I said, the Microsoft Azure is encrypting stuff
before writing to the disk using server-side encryption.
Now, if I want to enable the equivalent of BitLocker
or ADE, Azure Disk Encryption,
I go under Additional Settings.
Alright,
so if we scroll down a little bit under Encryption Settings,
we can see Azure Disk Encryption.
So this is the ability to run encryption
using the guest operating system
for either the OS and/or the data disk.
And so we get to choose which disk to encrypt.
Now, I don't have a data disk on this VM,
but I'm gonna choose the OS disk.
So this is going to encrypt the operating system disk
from using the operating system.
Now, I do need to create a key vault or have a key vault.
I don't have a key vault in the same region as this VM,
so I'm going to create a new one here.
So I'll say Create, I'll keep it in the same group,
I'll call it ade-keys.
And I'm gonna leave everything here at the default.
Now, you'll notice that there is a soft-delete,
so anything I store in this key vault
will be retained for, in this particular case, 90 days.
I'm gonna cut this down,
just for the convenience of this demo.
And I'm going to say Review and Create.
Oh, before I recreate this actually,
we have to go under Access Configuration.
So under Resource Access,
I have to enable Azure Disk Encryption for this key vault.
So there's a crucial step
for enabling access for this key vault.
So now, I'll say Review and Create.
And we'll let that validate.
And I'll say Create.
So the key vault has been deployed,
and I'm back into the VM overview
where I'm modifying the advanced settings for this VM.
If I go under this Disk Settings, OS disk.
Now the key vault has been selected,
and we're going to allow it to create a key.
You'll see, this is not mandatory.
We're gonna allow it to create a new key for this.
And so I'm gonna say Save.
So now that's gonna deploy this change
for OS Disk Encryption.
Now, this is a disruptive process, obviously
encrypting the virtual machine operating system disk
requires a VM reboot.
So I'm going to have to accept that deployment
is going to actually reboot the virtual machine.
While the VM is rebooting,
it does the encryption of the operating system disk,
and it can take 10 to 15 minutes.
So you don't wanna be doing this
in a production environment obviously,
you wanna get that all set up before you require it.
So we'll let that deploy,
and we'll wait for that to finish encryption,
and we'll come back.
So it says deployment is complete.
I'll go back to...
This is taking me to the Azure Disk Encryption resource,
I wanna go back to the virtual machine.
Under Disks.
And under the operating system disk,
we can see the Encryption now says server-side encryption
with platform-managed key and Azure Disk Encryption.
So the operating system disk has been now encrypted
both at the hardware level
and with the operating system itself.
And so, we have successfully enabled server-side encryption
and Azure Disk Encryption on the same disk
for maximum encryption and security.

