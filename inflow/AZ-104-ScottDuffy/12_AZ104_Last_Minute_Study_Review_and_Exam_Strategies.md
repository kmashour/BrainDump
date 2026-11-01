---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "12"
title: "Module 12: AZ-104 Domain Review, Exam Strategies and Certification"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 12: AZ-104 Domain Review, Exam Strategies and Certification

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** Comprehensive Domain Reviews: Identity, Governance, Storage, Compute, Networking, Monitoring; Certification Renewal, AI-Assisted Study, Practice Questions  
**Line Range:** Lines 19662 – 24731 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


### 📺 Lesson: AZ-104 Last Minute Study Review - Identity and Governance


All right, so in this video
and the next few videos that follow,
I'm gonna be going through the requirements
of the AZ-104 exam in quicker detail.
So you've just watched a course, hopefully,
on the AZ-104 exam.
It's gonna be 16 plus hours up to this point,
but I wanna try to condense that information down into two
to three hours in the next five videos, including this one.
So this video will talk about Azure identity and governance,
and the next video will talk about storage
and the next video compute.
Each video should be around half an hour.
I'm gonna try to keep it in under half an hour,
and I'm not gonna get into so much detail.
We're just gonna basically cover each
of the requirements of this domain as quickly as possible.
Now, I am gonna be using the Azure portal
as my method of demonstrating.
There's no slides to this section.
And so when I'm talking about creating
a VM, we are going to be going through the wizard
to create a VM, and I'll just do that as quickly
as possible for each of the areas of this exam.
Hopefully that makes sense.
So I'm gonna assume that you have an account
on Azure that you can go to portal.azure.com,
sign in, make sure you are working
in either a free subscription
or a Pay-As-You-Go subscription and let's go.
So the first domain of this exam is Entra.
And so we're gonna navigate to Entra.
We either, I have it across my hot bar here
at the top, it's also in my menu,
but you can just type Entra ID in the search box
and you will see it come up under list of services.
So we're gonna start off on the left here
under Manage, and you can see the types of objects
that the Entra ID service manages.
First off is users. So there are two types of users.
There are members and there are guests.
And we can see along the column here
under user type, members and guests, what is the difference?
So members live in your tenant,
and a tenant is the organization
that this Entra ID represents.
So users live in the tenant. Guest users are external.
So we can invite a guest to get access to our resources,
but they're not principally living in our tenant.
They're just linked from an external source.
Users have their user ID password
and other profile details that live here.
Now, when it comes to members or users, remember
that there is an on-premises active directory or AD.
And so you can actually synchronize your on-premises users
to the cloud in Entra using Entra ID synchronization,
or we can create a user that only lives in the cloud.
Now, if you have users that come from your on-premises AD,
you're not gonna be able to really manage them in the cloud.
They have to be managed in the active directory.
So there is a difference between synced users
and users whose home is in the cloud here.
Now the other thing we'll talk about
in this section is groups.
So groups are security groups.
They control access to resources.
You can have a Microsoft 365 groups
that add Teams and SharePoint collaboration features.
When you create a group, you can assign users
to become members of that group manually,
or you can have dynamic group membership
that is, there's a rule that anyone added
to this department is always going
to be added to this group.
Alright, for this next part I'm going
to switch to a different tenant.
This tenant that I'm in has a free license,
as I said, and so I can't show you the licensed stuff,
but I do have a tenant that has a paid license.
So if I go to the top right and say Switch Directory,
I can go to another one of my active directory
or Entra ID instances
and give that a second to load up.
Now I don't have any subscriptions
or resources, but I do have a license.
So this is a premium P2 licensed tenant.
So if I go under Users and I choose a user.
This is a guest user, but I actually have a license.
So if I go under Licenses for this user,
he's actually assigned one of my Entra ID P2 licenses.
If I click on that, I can see that
for this user, I've got Defender for Cloud Apps,
I've got the multi-factor authentication
and P1, P2 licenses all enabled for this user.
Now there is a price, obviously you pay, per user
and the good news is
of all your users, you may have hundreds of users,
but maybe out of your 100s of users,
only 50 of them require licenses.
So you can actually pay for licenses
and assign them manually
to whoever you think needs it for those features.
Now, one feature that requires licenses
is the self-service password reset.
So if you have an organization,
then you allow users to modify their password
or you don't allow users to modify their password,
or only selected groups can modify their password.
So I'm going to say in this organization,
I'm gonna allow all users,
if they wish, to modify their password.
You can see we go on authentication methods.
The question is how many authentication methods are required
in order for someone to change their password?
And in this organization only require one method
and they have availability of email and phone.
You can see Microsoft is retiring the concept
of security questions next year.
So that's gonna have to be some kind of mobile app
or again, email and phone still apply.
Alright, so in terms of review, this is far
to going for users and groups.
Let's move on to talk about role-based access control.
Alright, so now that we've seen how users
and groups are managed within Entra.
Let's talk about the actual security,
which in Microsoft Azure is generally called
role-based access control.
So RBAC, role-based access control,
is basically a security model where you've got an individual
or an application called a security principle.
You have a role definition and you have a scope.
And so for every person
or application, they are assigned one or more roles
and those roles have permissions to do certain things.
Could access a virtual machine
or an app or access a resource group.
There's also administrative roles
within Azure and things like that.
And you can have multiple role assignments
on an individual.
So I'm gonna demonstrate this
to you by going into one of these resource groups.
So the role-based access control is managed
at the resource level.
And so if I go into a resource group
as an example, there is this menu called access control.
And you can see that there's a overall list of roles.
And so across all of Azure, actually
there is hundreds and hundreds
of these roles predefined like still in the As.
There's 915 predefined roles at this time.
And then there's some generic roles
like owner, contributor, reader.
Whenever you see owner, this is the top level of access.
It grants full access to manage all resources, read
and write, create and delete,
as well as assign permissions to others with that.
So the owner can actually create other owners
or even other users.
Contributor is a read and write permission to all resources,
but you can't then create another user that has permissions.
You can't grant permissions to anyone.
And readers, just as it sounds,
it is a read-only permission.
You can view all resources with read-only access,
but you can't modify them, delete them,
create them, et cetera.
But then on individual resources
like Azure Container Registry,
like API management services, app configuration service,
there are individual permissions per service.
So if you assign more than one role
to an individual, then those things add up, right?
They're a cumulative model.
So if I look at myself, I'm gonna say check access,
and I'm gonna search for my account here.
And I can see that at this level,
at this resource group level,
I have four roles and these roles have been all inherited
from the subscription level,
from a management group level or even root level.
These are my roles.
So I don't have any specific role for this group.
All the permissions that I have come
from higher level things.
But still, even though I probably
have full permissions on everything
in here, I can still assign myself additional permissions.
So if I go under, let's say I go under Roles
and I say Add Role Assignment.
I can pick a role.
So I search for virtual machine roles
and there is a virtual machine contributor.
Lets you manage virtual machines but not get access to them,
or not the storage account or virtual network.
So let's say I choose this virtual machine contributor role.
I can select who gets access to that role.
So I have a number of fake accounts
in this active directory.
And so I've chosen the user Tom Smith.
So Tom Smith is gonna be granted the permissions
of a virtual machine contributor.
For any virtual machines in this resource group.
So I'm scoping this to the scope of the resource group.
We can see that under Scope, it's the resource group,
AZ900Course scope, and Tom Smith
is getting virtual machine contributor permissions.
So I can then assign him that permission.
So this is how you use role-based access control
to manage and assign permissions to specific users
for a specific task within your Azure subscription.
And not only at the subscription level,
but this can be inherited by individual resources of course.
Now, I should point out that there is a propagation
that takes place.
So if Mr. Tom Smith was to go
and check that he can have contributor permissions
to virtual machines, it might take a few minutes
to take effect, so he would have to wait 10
or 15 minutes before it goes into effect,
but that's just the way it works.
So let's move on to talk about subscriptions and governance.
This little key icon in my menu is for subscriptions.
Now I actually have three subscriptions
and I've only filtered so that two of them are active.
So I select a subscription that I want to look at.
When I go into the subscription overview,
I can immediately see things
like my spending, cost by resource,
number of resources I have
against my subscription, et cetera.
So the subscription is the basis
for which things get charged.
So all resources must belong
to one and only one subscription.
And a subscription has a billing element where a credit card
or a corporate account where the bill gets sent to.
So right now I've spent $69
and at the end of the month, if nothing changes,
I will be charged $69 for this subscription.
So this is the unit of measure for how things get built.
Now there's actually a hierarchy
above subscriptions called management groups.
And by default, you're not gonna put your subscriptions
into a hierarchy.
But you can actually create groups that contain other groups
and you can distribute, if you have access to a lot
of subscriptions, you can logically organize them
into various folder, sub-folders, things like that.
Purpose of that is so
that you can manage your subscriptions as a group.
So in the root group,
for instance, I have three subscriptions.
And I can create certain resource groups
that are going to be common among all three.
I can create permissions policies.
So I can create an Azure policy at the root group level
or any group level that will get distributed
to subscriptions that are under that group.
So it's basically a way of doing management
across multiple subscriptions.
Apparently there's a limit you can have up
to six levels deep.
And so any RBAC or policies
as applied here are inherited to the child subscriptions
and can't be overridden by those child subscriptions.
Speaking of policies,
if we go to the Azure Policy Service, we're gonna see
that Azure policy enforces organizational standards.
So the basis for this is called a definition.
And once again, Microsoft gives you a thousands
of definitions, 3,400 at the current time
built-in definitions that allow you
to enforce whatever organizational standards you have
against your resources.
So think of it like this, let's imagine
that you require SSL, or in this case TLS,
but you can say SSL connections to all your databases.
That could be one of your organizational standards.
And so you can say in like this is a preview one,
but in enforce encryption in transit
across all Azure services.
And this is a group, there's 17 policies buried in this.
You can see functions, you can see app services,
you can see storage accounts.
If we choose any particular one of these, we can see
that an Azure policy comes down
to a JSON document, which is called a definition.
Now these are actually pretty readable.
And we can see that
this particular standard, it doesn't deny it
or block it, it's just forces this to show up on a report.
So the effect of this is there's gonna be a report
that says which storage accounts don't have secure transfer?
And you'll see the resources it applies
to is Microsoft.Storage/storageAccounts.
It's checking a particular parameter called
HTTPS TrafficOnly.
If it says false, then we know
that this needs to go on a report.
So what you want is HTTPS traffic only to be true.
All right? Like I said, the parameter of this is an audit.
So an Azure policy is a very good way
to enforce your organizational's rules
against your resources.
So instead of just telling developers
that all resources must be HTTPS only then you can actually
have Microsoft Azure enforce those rules.
If you don't like any of these policies
or you need to customize it, you can create custom policies
or such a thing as a custom policy.
So if I cleaned this out
and I just said I wanna see the custom policies.
I don't have any.
Alright, the next governance thing
that we can possibly talk about are resource locks.
I'm gonna go back into a Resource Group
and I'm gonna go under Settings, Locks.
So resource locks are a way
that you can apply at the subscription resource group
or individual resource level.
There are two types of locks.
One is called delete, cannot delete.
So users can read and modify the resource,
but not delete it.
Read-only means that the users can only read the resource
but not modify or delete it.
So locks apply regardless of your permissions.
So if you have the permission
to delete the resource, but there is a lock on it,
you still will be denied the ability
to delete it until you delete the lock.
So you have to then remove the lock.
It's also possible not to have permissions to modify locks.
And so you can have a situation where you can create
or delete resources, but some resources are locked
and you don't have permission to modify the lock.
And so that's a good security method
for locking down some resources that nobody can touch.
Alright, so the next type of governance thing
that we'll talk about is the concept of tags.
Now, when you create a resource,
you are always given the choice to add tags.
Tags are key value pairs
and they are applied to resources
or resource groups in this case.
They're not inherited, so you're gonna need
to apply them one by one resources if that's what you want.
You can use an Azure policy to deal with inheritance.
So there is a policy for inheriting tags.
And this is generally used for cost tracking, automation
and reporting and other types of governance.
You can have a maximum of 50 tags per resource.
Now we're looking at resource groups,
and these are containers for resources.
So you can see I have two resources in this resource group.
You don't have to, even though your resource group lives
in a location, the resources inside do not have
to live in that same location.
This one is one that does, but it's not mandatory.
Deleting the resource group deletes all
of the resources in it.
And you can actually move resources.
So if you go into the resource, there is
often a move option such that you can change it
from one group to another.
Just so for organizational purposes.
Alright, the last type of governance
thing we'll talk about is cost management.
So if you go into Cost Management
as a service, it's chosen my subscription by default,
but I can obviously change to a different subscription.
And there's gonna be a number
of reports monitoring budgets that is available.
So for instance,
I know the subscription has some cost to it.
When I go under Reporting, I can see some reports
that I often go to versus other reports that are available.
So let's look at accumulated costs
on this resource for the month of May.
And we can see that as the month has gone on,
how my costs have changed.
I had a VM that was costing me about $2 a day
and that was just running.
And then at some point I started creating other resources
like Cosmos DB and PostgreSQL,
and the cost was to go up.
But I can see based on my costs,
what resources are have accumulated most of that.
So virtual machines, my PostgreSQL database,
a storage account, there's some VNet costs, Redis,
I've been running some Redis.
I can see which regions these are and which resources.
This is an open cost server that's costing me the most,
but I've got other demos
that have cost associated with them.
I can drill down into these if I want. I can add filters.
So let's say I only want to know things
that were for virtual machines.
If I scroll down a bit,
I can see the B series virtual machines,
and this will change the information
on this screen based on filters.
I can have it grouped by location
and things like that.
Now, one of the more useful
things you can do is set up alerts and budgets.
So for instance, I have a budget on this that I set
to $50 and the budget has gone off
a few times since this month has been going on.
I call it spending too much.
So I can consider $50 to be higher than average month.
It resets monthly and it's just, budgets have a start
and end date, but this one is gonna last for a few years.
Now, budgets don't actually stop the spending,
they just set up an alert, so I have budget alerts.
When I hit 50% of my budget, I get a text.
When I hit 100% of my budget, I get a text.
The actual cost and then when my forecast is forecasted
to hit my budget, I get a text.
So I have three texts a month
that can go off relating to my $50 budget.
So you can set this to emails, you can set a program to run.
So if you have something that needs
to happen that's in action, you can have a program
that runs and things like that.
Now there is a service called Azure Advisor
that runs on your account occasionally
and will make recommendations for reducing cost.
So I have two active cost recommendations.
Be curious to see what they are.
So this virtual machine that I run,
I Pay-As-You-Go pay by the hour.
It is suggesting that I actually move this
to a reserved instance and I can save $1,700 a year
if I change the the way that that subscription happens
or choose another type of savings plan for this.
So I can, depending on how I sign up for this,
I can save some money.
That's a good recommendation, right?
There's also security, reliability,
and other performance, other recommendations
that Azure advisor can make depending on your resources.
For instance, my Cosmos DB doesn't index every column.
I had some exclusions and so now it's recommending
that I add missing indexes.


### 📺 Lesson: AZ-104 Last Minute Study Review - Storage


All right, so in the last video
we reviewed identities and governance section.
So all the Entra stuff, built-in roles, RBAC,
and subscriptions and governance.
In this video we're gonna talk about storage,
so configuring access to storage
and managing storage accounts, files, and blobs.
All right, we're back in the portal
and we went into the create a resource option,
chose Storage Account from the list.
And we're going to go through creating a storage account
to talk about the various features.
Now, every storage account,
as every other resource in Azure, has to have a subscription
and be part of a resource group, either existing or new.
And the storage account has to have a name.
In this case, it has to be unique
and I put some numbers at the end
to make it unique, and a region.
And one of the first things we have to decide
is what type of storage account it is.
So it's either gonna be primarily
a general purpose account, which is blob storage,
Data Lake storage, which we'll talk about in a second.
It can be Azure files
or it can be other things like tables and queues.
Again, this is just a guidance
that sets up your wizard accordingly.
So let's call it a blob storage account,
which is general purpose.
Now we get the choice between standard account
or premium account.
And this is a significant choice
because if I was to choose a premium account that is SSD,
which is solid state disk, low latency.
And when you choose premium, you are going to get the choice
of other options like block blobs, page blobs,
and things like that.
From standard, this is the typical HDD,
spinning metallic hard disk.
It's a general purpose account.
Either option, you get to choose what's called redundancy.
Now redundancy is how Microsoft Azure stores your files
within their data centers.
The lowest level of redundancy
is called locally redundant storage or LRS.
So this keeps three copies
of your data in a single data center.
So let's say you upload a file, a picture of your vacation,
well this is gonna get stored three times
within a single building.
That way if you have a physical problem where the hard disk,
remember this is a metallic spinning disk,
it can get dusty, it can break.
If something happens to the disk,
there's still two other copies of your files.
And so it is an almost infinitesimally small chance
of losing your data for having two copies,
three copies in a data center.
Now we still have what are called regional issues.
So let's say there's a flood or a lightning storm
or a power outage, this could affect the whole building.
And so locally redundant storage protects you
against those individual failures,
but not against an entire regional issue.
Now the next level up is called zone redundant storage.
Zone redundant storage still keeps three copies
of your data, but it stores it in separate buildings.
These are other zones in the same region.
Okay?
So this way if a single problem happens to
that single building, it is less likely
to affect the other building.
So a sprinkler problem or, you know,
even a power outage may not affect both buildings
because Microsoft sources its power independently,
its internet independently and things like that.
Or the buildings could be a few miles away
from each other as well.
So there could be regional issues that don't affect
all of the data centers in the region.
So zonal is a little bit more safe
in terms of your data, but only still only three copies.
Now we get up to GRS,
which is basically locally redundant storage
in two different regions.
So you get three copies of your data in one data center
and three copies of your data in another data center.
And these are asynchronously copied.
Okay?
So this is more globally safe.
You're gonna store your data in let's say Northern Europe
and in Eastern Europe.
So you've got two different regions.
Going up even further,
we get this geo zone redundant storage.
So this keeps six copies of your data as well,
but it keeps it spread across different buildings
in two different regions.
If you choose one of these geo redundant options,
either one, you do get this option to have a read access.
So by default,
even though they're keeping your data in other regions,
you don't have access to it.
But if you're willing to pay for it,
you can get a read access URL
and endpoint in case the entire region goes down.
Then you can switch over
to reading your data from the other region.
It's not writing access, it's still only reading access,
but at least the data's there.
All right, so I'm just gonna choose
locally redundant storage.
So next up we're gonna talk about access tiers.
It's an important concept.
We have a hot access, which is the most balanced one.
It's for frequently accessed data.
And what that means is you're gonna pay
around two cents per gigabyte per month for storage
and you're gonna have very low reasonable fees
for accessing that data.
So you're gonna pay for reading
and pay for writing, pay for doing a directory listing.
Those are relatively cheap anyways,
but this is reasonable price for monthly storage
and a really cheap price for access.
When you get down into cool and cold,
you're actually saving money on the monthly storage.
So it's going to be, instead of two cents per month,
it's gonna be one cent per month for cool access.
And I don't remember, but it's much cheaper for cold access.
Okay, so the monthly charge goes way down
when you go into these lower colder tiers,
but it costs more to access it.
So this is good for backup files,
old log files, anything that you still want to keep a copy
of, but you don't really need to get frequent access to.
And in this section you can set the default.
There is also another feature called a lifetime access,
where you can move files from hot to cool to cold,
or even to an archive tier, which is not a default.
So archive tier is more like an offline tier,
not shown here, but you have,
oh, for each of these you have minimums.
So 30-day minimum, 90-day minimum,
archive tier has 180-day minimum,
but it's the cheapest when it comes
to the monthly charge for storage.
And the most expensive when it comes to reading that data,
it's stored offline
and so it does take some hours to even get access to it.
So if you want to thaw your archive
data back into a hot tier, then that could take hours.
So this is really for things that
you don't need immediate access to, might be legal stuff
that if you get a government subpoena,
you need to be able to come up with it.
But there's no reasonable expectation
that you're gonna be able to get access to it right away.
Now these things can be set either at the account level
or at the individual blob level.
So you can have some blobs that are hot
and then some blobs that are cool on the same account.
Now if we switch ahead to the Encryption tab, we can see
that there is what's called Microsoft managed keys.
So all data is encrypted.
So when you store a file into an Azure storage account,
it's actually encrypted by Microsoft
before it's written to disk.
And Microsoft controls the keys.
If you as the customer want to control the keys,
that is you generate them, you have access to them,
and you can regenerate them whenever you want,
that's a customer managed key
that gets stored in a key vault.
Okay?
But all data is encrypted.
And the next thing, of course,
is if you want customer managed keys,
what types of files get managed by those keys?
Now there is a second layer of encryption that is optional.
So by default you're getting one turn of encryption.
So you store a file, it gets encrypted and stored.
There is this infrastructure encryption option,
which means that at the software layer
this is being encrypted.
And then before it's actually written to disk,
there's another encryption that gets added
to it at the infrastructure level.
This is more of a hardware encryption,
think of it like BitLocker for Windows computers.
So I'm gonna cancel out of here
and we're gonna talk about,
we're gonna go into a storage account.
I'm gonna choose one of my storage accounts
and we're gonna talk about this concept
called object replication.
So object replication allows you
to basically automatically asynchronously copy blobs
between a source and a destination.
And that could even be across regions.
So let's say you have your storage account
in East US region, but you want to have a copy
of all those files elsewhere, kind of like a backup,
but you can get access to it.
So there is this object replication option.
You can set up replication rules
and the objects will be copied the background
between the two accounts.
In order to handle this,
it requires a feature called blob versioning.
So that means that as you update a blob
it doesn't overwrite the previous one,
it just creates a new version, version two, version three,
version four, and so that it needs to be enabled
in order for object replication to be enabled.
Now another way to manage your files in a storage account
is what's called a Storage Explorer,
or in this case a Storage Browser.
So Storage Explorer is a piece
of software you can install on your local machine
and if you Google it, you will find it
and you can download this, I believe it's cross-platform.
You see Windows, Mac, Linux,
and this allows you to connect
to an Azure storage account from a remote location
like your workstation and be able to interact
with the files in that storage account.
Then another option you need
to know about is called AzCopy.
Now, AzCopy is a command line tool that allows you
to copy files between your on-premises
and your storage account, or vice versa,
storage account to on-premises or between storage accounts.
One of the big benefits of doing
between storage accounts in this way is that you don't have
to download the file to your local
and then upload the file to the other storage account.
This does it completely remotely.
So for instance, you have a one terabyte file in an Azure
storage account and you want to copy that file
to a different Azure storage account, AzCopy can do that.
Or like I said, you want to get data from your local
into such a storage account.
You can have a command line tool that runs called AzCopy.
Now there's actually a couple of different ways
to manage access to your storage account.
If I go under Security,
I can see there's an option called Access Keys.
And so by default you have a storage account
and you are given two keys with it.
So an access key is a 512 bit key
and having this key will give you full
access to the account.
So if I was to show this to you, actually I'll do that.
Anyone who has this string can get full access
to this account as long
as I have my networking open for them.
But the key here is that I can change it at any time.
So I can say rotate or regenerate access,
and this key is going to be regenerated.
And the old key will be invalid.
I'll do it again just 'cause I was showing it.
So anyone with this key has owner level access.
This is not actually the preferred way of sharing access
to your storage account.
Another way is called shared access signatures.
So a shared access signature is a time limited
and permission limited way
of giving access to your account.
So let's say I want to give read access
and list access to my blob account, my containers,
but not to Azure files, to queues, anything like that.
I don't need to access indexes or anything like that.
So I can use the key, instead of giving them the key,
I can give them a connection that contains these permissions
for this limited period of time.
And so anyone with this SAS token
can get the access that I've outlined above
to this container.
And there's even the full on URL
that I can share with somebody.
Now the problem with this is once you generate it,
you can't revoke access.
You can't say to the person, oh,
I'm gonna delete their SAS token.
That's once it's generated
and you've shared it with somebody, that's it.
What you can do is you can invalidate the key.
So once the key is invalid, all of the SAS tokens that
that key was used to sign will also be invalidated.
Now we're gonna switch to a different
storage account for this demo.
We're gonna talk about what's called a stored access policy.
So a stored access policy is defined at the container level
or in the case of queues,
it can be a queue level or table level.
And at the container level there's a setting
called Access Policy.
And really what it is, is it allows you to create
a policy that then can be revoked.
So remember I said the shared access signatures,
once you create them, the only way to revoke them
is by revoking or regenerating the key.
Well having a stored access policy allows you to create,
we can call this, you know, policy1.
We can say we want this to have read permissions.
Give it some.
Date and time for expiry.
And then when I create the shared access signature,
I can refer to this policy
and I can then modify the policy so that it expires
or to modify the permissions on that policy.
So let's go back to the thing.
I'm gonna say create shared access signature,
and I'm signing with Key 1, but I'm referencing the policy.
And notice I can't then
modify the permissions and the dates.
So the policy separates out the permissions and the dates
from the SAS token.
And in this way I can modify
or invalidate the policy without having to modify
or invalidate the key.
This makes SAS tokens a little bit more useful
by having stored access policies.
Now another thing you'll notice we've been using,
or I mentioned we had access keys access to this account.
We can switch such that we're using the role-based access
control with Entra to get access to this.
So then we have identity-based access
and now you are granting people permissions in RBAC
to read storage accounts
and get access to containers and things like that.
It replaces access key control.
Once you do this, then you are not going to be able
to use access key control.
So you have to make this determination whether you want
to have this secret key that is used for tokens
and signing, that can be used by applications directly
to get full owner access to your account
or a more fine grained access control using Entra.
All right, next up we're gonna talk
what is called a firewall.
Now when we set this up, this storage account,
we enabled public access,
effectively access from any network.
So you'll see under Networking,
public network access is enabled from the internet
and from any other network.
So if I was to go and to try to modify this,
I can say I do not wanna enable this from every network.
I wanna be able to select which networks.
Okay, so let's just say I just do that.
I say I only want selected networks.
So this is going to block access
to the storage account from everywhere.
The internet can't access it,
no other network within the Azure portal
will be able to access it.
I have basically, I might as well just say,
disable network access,
and then that way there's just no, no one can access it.
Now why would I want to do this?
Well, obviously having this thing open,
even if we have security keys
or RBAC, there is a risk, right?
So if the security key gets leaked,
then someone will be able to find this account,
and because the internet is enabled.
So by disabling it, it is the maximum security.
Then what you could do is have
what's called private endpoints.
So even though network access is disabled,
you can set up a private connection
between this storage account and a virtual network,
avoiding the need to expose it to the public.
So effectively you can set up a, almost like a VPN,
but it's a private connection between the storage account
and a virtual network.
So this is the best security
is to turn off full open access and say private endpoints.
Another way to do that is by saying,
enable from selected networks and then choosing
one of the virtual networks that you have.
And then only virtual machines
and applications that are connected to this virtual network
and this subnet will have access to this storage account.
So effectively it's like the private connection,
but this is what is called a storage firewall.
So you are restricting effectively the IP.
I saved this, right or not?
Okay, yeah.
Restricting the IP addresses who can access this
to the network that you've en enabled.
Of course you can add your own very specific
or another IP address so that you can access it
from your desktop, from your home,
as well as giving only private access.
So that is an option as well.
Be sure to select trusted Microsoft services as well
because if you have a backup service
or recovery vault, things like that,
they're gonna need access to this.
If you turn off all access,
you're gonna be blocking some critical stuff.
So this is generally a good exception to have.
Now you'll see in this storage account center,
it's showing me two types of storage,
a StorageV2 and BlobStorage.
So that indicates
that there is a general purpose storage account
that can handle blobs, files, tables, and queues.
And then there is just a blob specific storage account
that only handles blobs.
So when you go to create a storage account,
there is a tab called Data Protection
and this is where we're going to enable
or disable point in time restores,
soft deletes and versioning and other features
and we'll talk about that.
So versioning, I think I mentioned this,
but this is the idea
of maintaining previous versions of your blobs.
So every time you update a file,
it maintains the previous version
and it just increments the version number
and stores that new version as a separate file.
So obviously if you go to retrieve that file,
you get the latest version,
but you can also specifically request the last,
another version if you want to go back in time.
Now there are cost implications
because if you are keeping multiple copies of files,
you are paying more for storage
and there is a lifecycle management option
to retire effectively older versions.
We've talked about cool and cold and archive,
you can even move versions
to the cheaper options or delete them.
So that's versioning.
Now, soft delete, you'll see this in a lot of things,
but soft delete means that when you go
and delete a file, it doesn't immediately delete it.
So it marks it for deletion
and it basically in this particular case
will retain deleted blobs for seven days.
So it marks it for deletion
and then not until seven days later
is it available to be deleted.
This is a security protection not only
for malicious intentions but for accidents.
So if you have a storage account and you have some files
and you delete a few, but you realize afterwards,
oh, I accidentally deleted one that I need.
Then with this feature enabled
and it is enabled by default, you will have to be able
to go back up to this many days in it.
We have the blob level soft delete.
There is also a container level delete.
So if you delete the entire container,
then that will be retained for several days.
And then there's also file share soft delete.
So if you are using Azure file services,
then no files are actually deleted
immediately when you delete them.
So that's very useful and it's a good,
I would say security and peace of mind option.
All right.
Moving on, we're gonna talk about the concept
called lifecycle management.
Now I've alluded to it already,
but if you are in a storage account
and you go under Data Management,
there's an option called Lifecycle Management.
Lifecycle management allows you to set up certain rules
that will allow you to transition your data
from hot to cool, from cool to cold or to archive
and from any to any.
So I'm gonna say Add Rule,
I give it a name, I'll just call it rule1,
apply to all blobs in your storage account.
And I'm gonna apply to block blobs
and in just the blobs,
not their snapshots and things like that.
So this is where you set up a rule.
So you're either operating off of the last modified date
or the date it was created.
So let's say 30 days,
it was modified more than 30 days ago.
Then what do you want to happen?
Do you want it to move to cool storage,
move to cold storage, move to archive storage?
Remember I said it was offline,
or we can just delete the blob after 30 days.
So let's say if something has been modified
only 30 days ago, then it makes sense
that it actually gets moved to cool storage.
So this could be a particular rule.
You can then further say once it's been
last updated more than 60 days ago, then we're going
to the next one, which is cold storage.
Actually, maybe I'll make that 90 days.
So once it's been modified more than 90 days ago,
we're gonna save even more money in cold storage.
I can then add this as a rule
and it does take up to 24 hours to go into effect.
But basically this is a way of saving money
by moving your files to those access tiers
when you need them less and less.
Now on general purpose storage accounts,
you can support up to four different types of data.
So we've got a blob data, we've got file data,
we've got queue data, and we've got table data.
This is a rows and columns type of data service.
The same storage account can handle all four types.
Now the one that's interesting right now
is the file share service.
So file share is basically very similar
to what we used to use for company-wide file servers
where everyone had access to the same S drive.
It's mounted to your workstation as S,
and there's some company files there
that everyone could get access to templates
and budgets and things like that.
In some cases you get your own server-side storage
in that S drive, but not in every case.
So that's a file share.
So I can create a file share, give it a name,
call it, you know, companyfiles.
Only lowercase.
And once again we get this hot, cool type of option
for pricing or a transaction optimized,
lowest transaction cost for transaction heavy workloads.
So let's just leave it as a hot file share.
We can see there's a performance,
operations per second at 20,000
and 100 terabytes maximum capacity.
Do we wanna set this up for a backup?
I'm gonna turn that off for this demo.
So I have this companyfiles file share that can handle
up to 100 terabytes.
And as you can see it gets a URL
and this can be used to set up that file share.
So if I go under Connect here, I have Windows, Linux,
or Mac, I can choose the drive letter.
Let's say it's the S drive.
How do I want to get access to this?
Well for this purpose,
we're gonna use the storage account key,
but in reality, maybe we wanna use Microsoft Entra.
And it'll give us a little PowerShell script
that we can copy and run on our local
that will mount this drive as the S drive for us.
So we can store files in Azure from our local using,
once this is set up, it's going to basically
add this drive, New-PSDrive will mount the drive as S drive.
Now of course this does not necessarily work
over the open internet, so most ISPs
and security will block this type of thing.
But if you have a corporate network
and you're connecting to Azure in a corporate fashion,
like with ExpressRoute, then you could probably do
what's called, you can mount it.
And so there's Linux support, SMB 3.0,
or Mac support and things like that.
Now of course we could create a storage account
that is a file share specific account.
We have to set this up.
Let's just do this real quick as a premium account.
So Azure Files is the service that I'm interested in.
And again, you can host it in HDD or SDD.
Now file share is billed based on provisioned capacity.
So unlike a storage account
which you pay for what you use, like I said,
two cents per gigabyte per month,
file shares are paid for on the provisioned capacity.
So you provision 100 terabytes,
you're gonna pay for 100 terabytes.
Anyways, that's what I wanted to say about storage accounts
for this AZ-104 exam.


### 📺 Lesson: AZ-104 Last Minute Study Review - Compute


[No transcript available for this lecture]


### 📺 Lesson: AZ-104 Last Minute Study Review - Networking


All right, so welcome back.
And in this video, we're gonna deal with the implement
and manage virtual networking objective of the exam.
And so in, we're gonna talk
in a sort of high level details
about virtual networks, subnets, peering,
IP addresses, routes, troubleshooting,
security, it's a big topic of course,
securing virtual networks,
load balancing, and DNS.
So those are the major topics of this exam for networking.
And we're gonna sort of go through this in the same way
that we went through compute
and other topics in the previous videos.
All right, so the most fundamental aspect here
is the virtual network itself.
So a virtual network is basically
a private network in the cloud.
You're gonna use it to connect your network resources,
such as virtual machines.
So virtual machines must be connected to a virtual network.
If you remember from the compute video,
when we created a virtual machine,
it actually asked us whether we wanted to add it
to an existing virtual network or created a new one
and we created a new one.
So I'm gonna create a virtual network
as a standalone entity.
We're not going to create it
as part of a VM like we did last time.
So I found virtual network in the Azure Marketplace
and I hit Create.
Now, virtual networks themselves are free.
Now, there are costs involved
when you're talking about traffic leaving Azure,
or when you're talking about traffic between regions,
or you're talking about IP addresses,
but those are separate things.
The VNet itself is fundamentally free.
There are some limits to VNet, so you can't create
an infinite number of them, for instance.
So it's basically a private network in Azure.
It has a boundary.
When we create this, and we're about to do this,
we're gonna assign it an IP address range
and that has to live within your other resources
and we'll get into subnets and stuff in a second.
So I'll choose a subscription as always,
even though they're free,
it has to still be part of a subscription.
I created a new resource group for this demo
and gave it a name.
Name does not have to be universally unique
because the network itself
does not have an accessible address.
Now, placing it in a region is important
because only resources in that region
can connect to that network.
So you cannot create a region, a network in Canada
and then add a VM from Europe to it.
The region is essential for the network
and the resources that are part of it.
So keep that in mind.
Now, the first major question we have here
is the concept of encryption.
So encryption is a feature that encrypts traffic
between Azure virtual machines
when it's traveling across Microsoft's internal network.
So as soon as we cross
into the external public internet,
then that goes over normal encryption,
which could be SSL or maybe it's unencrypted,
but there is a special encryption
that simply runs on Microsoft's internal network.
It can only be used for virtual machines
that support accelerated networking and have that enabled.
So it is a special type of VM network interface card.
But let's say we do wanna create a Vnet
that has traffic that travels across it
using Microsoft's own internal encryption.
Again, this encryption happens at the network layer,
protects data in transit, managed entirely by Azure,
and it does not replace HTTPS.
It does not encrypt data at rest.
It does not encrypt data that's hitting the internet.
So it's not encrypting other things,
just traffic traveling across this network.
Now, Azure bastion is a secure way to remotely connect
to a Windows or Linux machine through RDP or SSH
without having to open a port
on that virtual machine specifically for it.
So as you may know, I think RDP is 1433.
If you wanted to remote into a Windows machine,
you have to open port 1433 in order to do that.
Well, with an Azure bastion server,
again, it's a separate service,
then that's going to allow you to connect to the server
in a more secure fashion.
We can always enable this later, so we won't.
A firewall clearly is a device
that allows you to pass traffic over it
and does certain security checks of that traffic.
So for instance, if you force all traffic
that's leaving your VM to pass through a firewall,
then you can filter that traffic, block it,
restrict it to travel over certain routes, et cetera.
Distributed denial of service,
all networks have a basic level of distributed
denial of service attack protection generally.
So there's a generic protection that comes for free.
But if you want this enhanced DDoS protection,
whether it's at the IP level or at the network level,
this is for network level,
then you need to sign up for that
and there's a fee relating to that.
All right, so moving on to the Address Space tab.
This is where we set the size of the virtual networks.
Yes, virtual networks have sizes.
And the good news is that you can change the size.
So if you set it to be one size now,
in the future, you can either grow it or shrink it
depending on your needs.
Now when I say size,
I'm talking about the number of devices in total
that can connect to the virtual network.
You can set it based on an IPv4 and/or an IPv6 range.
So when it comes to IPv4 ranges,
there are a few ranges that are considered private ranges
and anything that starts with 10
is considered a private IP address range.
So all of the IP addresses that follow this
are considered private.
Now in this dropdown,
we're gonna set the starting point of the range.
So by default, I'm given 10.0.0.0,
which is the starting point
of the private network space for 10.
And as you can see, we have this dropdown,
which got a number in it /24.
And that is a CIDR notation, C-I-D-R.
And each number that you choose
is going to set the size
in terms of the number of addresses.
So /16 is two full octets,
so 10.0.0.0 to 10.0.255.255.
So you can see it's a good chunk of that
and it's 65,000 addresses.
In fact, every eight represents one of those octets.
So /8 is everything to the end of the 10 address space
of 16 million addresses.
Now, this is overkill.
You're never gonna have 16 million devices
and you're actually blocking yourself
from creating other virtual networks
and linking them together.
So you should probably create a good sized VNet
that's not too big, not too small, right?
Something Goldilocks.
So if you look at the /24,
that gives you up to 256 devices into that range.
And if you ever need to grow it, you can grow it.
You can make it /23 and that gives you double, right?
Every number that decreases doubles the size.
I should also point out
that there are some reserved numbers in this range.
So for instance, if I had a slash,
a small one, /29, that says eight addresses,
but the first IP address is reserved as the network address
and the last one is reserved as the broadcast address.
So two of these eight are reserved for internal uses.
So you really only have six devices you can connect.
So keep that in mind.
So let's create this as being a /24.
Now, the other concept between virtual networks
is the concept of subnets.
Now, subnets allow you to subdivide the virtual network
into smaller networks that you can control
the security of independently.
And devices don't connect to the actual virtual network,
they connect to a subnet.
So for instance, I have this /24 virtual network,
but I have a subnet that's called default,
that's the default name,
right now it's taking up the entire
100% of the addressable space of the virtual network.
I could edit this
and instead of it being a /24,
I can make it a /25
and it would only take up half the space.
So you'll see it ends around the halfway mark
and I can hit,
I can hit Save,
and then I can add another subnet,
call it,
you know, backend,
and it starts at the end of the other subnet.
And so it's as well 128 addresses
and it's starts at 128.
So these are two subnets now
as part of the one VNet
and they each take up half,
front half and back half.
Now sometimes, some resources require their own subnet.
And so you're going to let's say add a subnet
and you need it for that bastion server
that we were just talking about.
Well, the bastion server has its own name
and it's going to take up its own set of addresses.
You see its 64 addresses on the VNet.
It's its own subnet.
And the firewall is the same thing.
And so you have sometimes virtual network gateways,
they need their own subnet.
So keep that in mind as well when you're planning it.
All right, so I'm going to hit Review and Create.
Let's create this subnet.
Actually, I'll remove the bastion.
We'll move this back down /24
and I'll say Review and Create
and then Create.
Let that create.
Now, what I'm gonna do just to demonstrate this,
is I'm gonna create a virtual machine
and I'm gonna place one virtual machine
in the default subnet
and one virtual machine in the backend.
And you can see when I'm creating the virtual machine,
I can select the existing virtual network
that we just created
and which subnet it's gonna be placed in.
I also want a public IP address,
so that I can demonstrate this.
Now in addition to two VMs on those two subnets,
I'm gonna create a third VM on its own subnet.
So we're gonna create a new subnet
in line with creating the virtual machine.
As you can see, it has an IP address range
outside of the one that we assigned.
And I'll just leave the default to say default.
Now, we're gonna talk about security in a second,
but I just wanna point out
that by default, the security rules allow traffic
between the two subnets on the same VNet.
So if I was to go into the virtual machine
demo one that I created,
I could talk to the virtual machine on demo two.
All right, so in order to demonstrate this,
I do need to run a command,
purpose is to allow me to ping between the two machines.
That is the ICMP port.
So let's enable ICMP service between the two machines here.
All right, so both vnetdemo1 and vnetdemo2
will have this ICMP port open.
Now, in order to demonstrate this,
I'm gonna be in vnetdemo1
and I'm going to have to ping vnetdemo2.
And this is gonna show
that two machines running on two different subnets
in the same VNet by default can communicate to each other.
So this is the private internal IP address
for the second machine.
And I'm gonna use this to ping from the first machine,
so I can say ping
and it's 10.0.0.132.
And so we have successful communication
between vnetdemo1 and vnetdemo2
showing that by default,
two machines on the same VNet
on different subnets can communicate.
All right, so what I'm gonna demonstrate now
is that this machine on the left, which is vnetdemo3,
which is running on its own VNet,
not on the same VNet as the other two,
it's got a 10.1 IP address,
will not be able to communicate with a machine
that's running in the other VNet.
So I'm gonna do the same ping
as we just did, 132, which is the backend vnetdemo2.
And I'm expecting this to fail
and it did fail.
So by default, two virtual networks,
even if it's in the same region,
even if's in the same subscription,
two virtual networks cannot communicate
with each other by default,
although two machines on the same virtual network,
even if they're in different subnets, can.
And so now we're gonna show you
how to connect these two networks.
That's called peering.
All right, so like I said, we have two virtual networks.
In fact, I'm gonna go into the resource group
and I'm gonna search by virtual network.
We're now onto a two-page resource group
and you can see there are two virtual networks,
vnetdemo and vnetdemo2.
I can go into either of these
and I can set up a connection with the other.
Now I mentioned before, but I'll say it again,
the key here is that the address space cannot overlap.
So vnetdemo has 10.0.0.0,
whereas vnetdemo2 is 10.1.0.0.
And so in this example, they do not overlap
and so they can be connected through what's called peering.
All right, so to set up peering,
I'm gonna go into one of the virtual networks,
and under settings,
and I'm gonna go into what's called peerings.
So virtual network peering enables you
to seamlessly connect two or more virtual networks in Azure.
What that means is that the two networks
can communicate with each other seamlessly,
so that there's nothing more that needs to be done
other than to connect this peering.
So we're gonna set this up both ways.
So we're gonna set up a peer to that other network
and we're gonna set up another network
being able to communicate it back
and you can obviously not do that.
This also works if it's two different subscriptions.
So if you have two networks
that are under different subscriptions,
you can use what's called a resource ID.
So I can set up also a network-to-network
or subnet-to-subnet.
So I'm gonna do network-to-network
and we're gonna give it a name.
And since I'm doing this on vnetdemo,
I'm gonna choose a vnetdemo2
as being the remote virtual network.
And then I'm gonna say allow vnetdemo2 to access vnetdemo.
Now, there are other settings having to do
with allowing traffic to pass through
from vnetdemo2 to vnetdemo and then onto another,
that is more of a hub and spoke setup,
but I'm gonna leave all of these as the default.
We're not going to allow traffic to be forwarded.
We're not going to, if we had a gateway,
use another network to use our gateway.
Now, we are going to do the same connection back.
So we're gonna say VNet can access a vnetdemo2 as well.
That is the local virtual network.
And I'm gonna enable this checkbox
and I'm gonna say add.
So what this should do
is it should set up a two-way connection
between vnetdemo and vnetdemo2
such that those pings would work.
Now right away, we can see that the peering does appear.
And if I was to go to the other network,
I would see peer1.
And there's green check marks
to say that everything is connected.
So if I was to return to the vnetdemo3,
which appears on the vnetdemo2 network,
confusing, sorry,
I should be able to ping to the other network now
and you can see that it now works.
So we set up peering between two virtual networks
that are in the same region.
Now, we can also set this up for other regions.
So let's say we had traffic in Japan
and traffic United States,
you can set up what's called global peering.
It's the same technique.
You're just connecting to another network in another region.
And I should point out
that there is a cost for cross-region connections.
So to go from US to Japan and Japan to US,
you're gonna pay per gigabyte charges
for traffic flowing on the Microsoft network
between those two remote regions.
And that's just the way it is.
Moving on, we're gonna talk about the public IP address.
There used to be Basic and Standard SKUs.
Microsoft is deprecating the Basic
and so Standard is the selection going forward.
It is a static SKU
and that means that when you stop using the VM
and start again, you're gonna keep your IP address.
It's not dynamically generated,
it's statically assigned.
As well,
this is costing money.
So there is a charge for having an IP address
and there's no free IPs.
Now, the next subject we wanna tackle
is called user-defined routes or UDR.
Now, a route table is effectively overriding
the Azure default routing.
So what that means is that you have traffic on your VM
and you wanna to connect to the internet
and it will go by the default method from that VM
out to the public internet.
Well, you may want to route that traffic through a firewall
to force it to go through the firewall's rules
before being allowed out.
And then you would need a route table
in order to force the traffic to follow a different path.
So connecting from a virtual machine
to a firewall is a good example of a route.
Another one would be if you have let's say ExpressRoute
and you have a connection of your office into Azure,
maybe you want that VM not to go from Azure
right to the internet.
Maybe you wanna force that
to travel over ExpressRoute into your corporate network
and then follow whatever security
and other setups you have on your corporate network.
So you could force your VM traffic
to travel across ExpressRoute.
That would be another example of using a route table.
Now, when we created a virtual machine
and attached it to a virtual network,
we were given what's called a network security group
or NSG by default.
The NSG is like a static set of rules
that secure the traffic going and coming from the network.
And so basically, it's what's called a list,
access control list.
So if I go into a network security group as an example,
I can see inbound rules and outbound rules.
We had to add a new rule to inbound
to allow us to RDP.
So this RDP rule for port 3389
allows TCP traffic from anywhere,
which could be the public internet, to any destination.
So that's why there's a yellow triangle.
Orange triangle is telling me
that this is a security concern, but I'm just demoing this.
So it's good to know what the default rules are
in terms of NSG.
So in terms of inbound, there's only two types of traffic
that is allowed into a network by default.
And first of all is traffic from within the virtual network.
So that's why we saw in the demo
that vnet2 can connect to vnet1 and vice versa
because of this rule.
The other is load balancer traffic.
So if we have a load balancer, which we don't,
then that traffic would be allowed to travel into the VNet.
All other traffic would be denied,
including public internet,
including other peers, et cetera.
So we have these security rules.
And on outbound,
we allow traffic to go
between the virtual networks outbound.
In this particular case, we're allowing internet,
so any VM can connect to the internet.
This is a rule
and every other type of traffic is blocked.
Which, what kind of traffic would that be?
So if you have a virtual network,
and you have, let's say you have a frontend subnet
and a backend subnet,
maybe you wanna be more restrictive
on allowing traffic into that backend network.
And vice versa,
you would want to maybe turn off traffic leaving
to go to the internet.
Maybe you don't want your backend servers
having any public internet access
and that would be a rule that you could add.
Rules are evaluated in order of priority.
The lower number is better, is higher.
So 100 is the highest priority
and 65,500 being the lowest.
These are the default rules actually.
Maybe an important thing to know
about network security groups
is there are two places that can have them.
Back to the resource group.
One of them is on the subnet.
So if I go into the virtual network
and I go into subnets
and I choose one of them,
let's say I choose this backend subnet,
I can see that I have an option
of adding a network security group to the subnet itself.
And that means all traffic traveling to the subnet
would have to follow these rules, to and from.
The other option that we have
is the virtual network interface card.
So if I choose the virtual network interface card
for one of the Vms
and I go into settings,
you can see network security group is an option.
And we have the network security group set.
So that means that if I have multiple VMs
on the same subnet,
I can set different security rules for them if I wish
or I can set it for the whole network or both.
Now, I also want to differentiate
the concept of a network security group
with an application security group.
And this could appear on the exam.
Application security group
is almost an entirely different concept.
It's really just a way of grouping related resources
under a convenient tag or name.
So this is a logical grouping.
So for instance, let's say you have
a bunch of frontend web servers
and a bunch of database VMs
and all in your virtual network,
you have associated list of frontend web servers
and backend servers.
You could create an application security group
just with the frontend servers.
And so by doing this,
you are effectively allowing you
to create a network security group rule
just to apply to those.
So let's say I call this my web servers,
that's my application security group.
There's really not much to it.
It's more of like a tagging mechanism.
So I'll create a web server as ASG.
And now when I go into the network security group,
and let's say I wanna add a rule,
so I go under settings, inbound rules, add a rule,
and I want to say only apply this to the web servers.
So I can add a rule that only applies
to servers that are tagged.
Now I created it,
I haven't added any resources to it by the way,
so I'll close that out.
I'll go back to the VNet
and I'm gonna go into the virtual machine,
application security groups.
I'm gonna say add.
And so I'm adding my vnetdemo1 VM
to this application security group.
As you can see,
you can have multiple ASGs for that resource.
And so now when I go into my network security group,
I can add a rule that only applies to this machine
because it's the only application security group.
It's the only machine in the web server's ASG.
And therefore, whatever rule I create
will only apply to that machine.
So that's an application security group.
It's really just a way of filtering
your resources to only web servers, databases.
You can assign related resources into the same tag.
All right, there's a lot of networking concepts obviously,
and I wanna cover them too with sufficient detail.
We're still going pretty fast.
So let's talk about the bastion service.
I mentioned it earlier in this video.
It is a way of connecting remotely to virtual machines,
particularly on your network,
without exposing that RDP port.
So we saw that having port 3389 exposed
is potentially a security risk.
And so what you can do instead is create a bastion server
and then you can basically connect to the bastion server
to connect to those machines.
And this can be done through your Entra ID and password.
There's much safer ways you can do it over HTTP I believe.
You don't have to open 3389 in order allow that.
Now, we used to call this back in the day,
many, many, many years ago, a jump box.
It's not exactly a jump box
'cause you're not VMing into a machine
in order to VM into other machines,
but it's the same kind of concept.
This is a device that allows you to get RDP access
to your VM
without having to open the insecure ports for that.
I mentioned before that the Azure bastions
need to be on its own subnet.
So you can either put it on the vnetdemo,
but then you would need to expand it
because vnetdemo is quite full.
But if we put it on the second one,
there is apparently some space for it.
So I can have the bastion subnet
in a new subnet on vnetdemo2.
Now, it's gonna have a public IP address
'cause that's how we're gonna connect to it.
We don't need public IP addresses for the VMs anymore.
We can just use the public IP address of the bastion.
All right, our next topic is gonna be
what's called service endpoints.
Now we saw earlier in this,
maybe in the last video or the video before,
that we can create what's called a platform as a service,
could be a web app or it could be a storage account.
And we could,
as we are creating it or later,
we can attach it to a network.
So I'm just gonna go to the Networking tab.
Right now, it's got public access enabled,
but I can say enable from selected virtual networks
and I can pick, let's say vnetdemo as it.
And then I can choose the subnet, either one or both.
Now, you'll see this note that says
Microsoft Storage endpoint will be added.
So Microsoft Storage still continues to exist
as a platform as a service,
but it's going to modify my virtual network
such that resources on that network have a path
in order to connect to the storage account
but other networks and the public do not.
So this is basically enabling a path
that extends the VNet's private address to the PaaS service,
traffic stays on the Microsoft backbone
and this has to be enabled per subnet.
So when I set this up,
the VMs are gonna be able to access the storage account,
but no other resource will
unless I add it.
So you have to give the endpoint a name,
I'll call it private1.
And you'll see it supports many different types of traffic,
such as files and blobs and tables.
So we're connecting this storage account
to this virtual network and to that subnet.
All right, so I see this tag about private DNS
and we're gonna discard these changes
and we're gonna switch over completely
and talk about the DNS services within Azure.
So there are essentially two types of DNS within Azure.
One is the public DNS, which is the domain name service.
When you have a domain name like example.com,
there needs to be a server to resolve that to an IP address,
and this is what is a DNS zone.
So in this case, we're gonna give it a domain
such as example.com
and we're going to then be able to create records
that the public internet will be able to look up
and get resolved for.
Now, you are going to have to change your registration
in the registrar to point to this name servers
in order for this to be the name server, the definitive one,
but that's possible.
The other option is what's called a private DNS zone.
Now, a private DNS zone only operates within Azure.
Now, why would you need a DNS server
that only operates inside of Azure?
Well, the answer is that we saw earlier,
we can create,
you know, two servers that have private IP addresses.
So we saw 10.0.0.132.
All right, I think I missed out on recording that.
But I finished creating a domain,
I gave it a name, I called it server.local.
Now, this is equivalent to the domain name.
So if I had example.com in the public,
this is server.local for the private.
You can call it whatever you want
because no one will ever see it, but your servers.
The other thing that I did
was I attached this to a virtual network.
So there's a thing called a virtual network link
and I attached it to virtual network demo,
which has that frontend and backend server example.
So we've got the private DNS called server.local
and it's attached to our VMs,
or at least it's attached to the VNet.
Now, if we head over to record sets,
we're gonna see that there are two relevant ones.
They're both referring to the virtual machines
that already exist.
And you can see,
so it's been auto-assigned, auto-registered,
those two VMs.
So if I go over to vnetdemo1
and I say ping vnetdemo2,
this works
because their private DNS
has a record for this IP address being this name.
Now, it may be that you don't want it to be called that,
that still may be not clear to you,
so you could obviously edit this
or you can add another record with a name that you prefer.
So I can call this db
and I can put the IP address and say add.
Also keep in mind this can be fully qualified
if you have multiple servers.
Remember, we called it server.local.
So vnetdemo2.server.local
and that is the fully qualified name.
I cannot ping db.server.local 'cause we just added
and it resolves to the same server
'cause that's the nickname we gave it.
So this is the use of private DNS.
Now we'll switch gears again
'cause we're still talking about networking
and I do wanna wrap this up,
we're gonna talk about load balancers.
So there are a couple of types
of load balancers within Azure,
three of them I would say that we'll talk about.
One of them is just called the load balancer.
It's self-named, load balancer.
There used to be a Basic load balancer
and that has been deprecated.
From this point forward,
Standard load balancer is the only option.
So this load balancer is what's called
layer four load balancing.
This means it has no knowledge of HTTP, HTTPS,
paths, query strings, nothing like that.
It's just network level.
It's for basically taking network traffic
and taking network traffic in
and sending it to a backend,
one or more backends in a distributed fashion
so that it sits in front of your virtual machines
and distributes traffic.
Okay, so this is the most basic,
again, network level load balancing.
There is another load balancer called application gateway
and that's called a layer seven load balancer.
Now, this is application-aware.
That means that if it is an HTTP server
or a web server, you can check the domain name
and you can say, oh, this domain goes here.
That domain goes there.
The application gateway is aware of the domain name,
it's also aware of the path.
So images can go this way
and videos can go that way.
It can just check the string inside the path
and redirect traffic accordingly.
Okay.
Now, there's a third type of load balancer
called traffic manager.
I don't think this is on the exam,
but this does traffic load balancing
at the DNS level.
So that means when you enter example.com in your browser,
it makes the determination then where to send your traffic.
If you are in Asia,
you can have the traffic being sent to a server in Asia.
If you're in America,
it can send the traffic to America and Europe.
And that's all done at the DNS level
and that's called traffic manager.
Now, when you're setting up load balancers,
one of the things that you need to think about
is what happens when a server fails.
So let's say you have three web servers
serving web traffic identically.
Load balancer in front of it.
And then at some point,
one of those web servers stops working.
It just doesn't reply, it's stuck in a loop,
it's crashed, blue screen of death.
The load balancer is smart enough to know this
and this is called a health probe.
So what you're gonna want to do
is have the load balancer check with the server
every 30 seconds, something like this.
And if the server returns a good result, it keeps going.
And if the server does not return a good result,
it should stop sending traffic to that server.
Now, there's ways of doing more sophisticated like checks
where the server itself can then restart
or get redeployed and stuff like that.
The most basic thing to do is
to remove traffic from load balancing
if that server is not responding well.
And that's called health probe.
Anyways, that is the most basic layer
of what load balancing is,
application gateway versus load balancer
versus traffic manager.
And we basically come to the end
of the networking stuff within this exam.
Again, this was intended to be a really quick overview,
go back and watch the course
for any of these things in more detail.
But yeah, that's the requirements of AZ-104 for networking
and if you understand all that,
then you should be fine on the exam.


### 📺 Lesson: AZ-104 Last Minute Study Review - Monitor and Maintain


Alright, so the fifth and last domain
of the AZ-104 exam says:
monitor and maintain Azure resources.
It's worth just 10% to 15% of the exam.
So there are two sub-domains.
One is monitoring.
Now, monitoring is things like metrics, logs,
queries, alerts, Azure Monitor Insights,
and the various networking tools that are available.
The second part of this video is gonna talk
about backup and recovery, particularly the difference
between a Recovery Services vault and an Azure Backup vault.
And we'll talk about the tool, Azure Site Recovery, as well.
So thanks for being here.
We'll keep going.
So we do have a lot to cover, and I'm gonna try to go quick.
Again, this is a review,
not necessarily an in-depth teaching.
I'm gonna go into the Azure Monitor tool,
which is this speedometer-looking icon.
And this is the current homepage.
Has a bunch of tiles on it and gives you an idea
of what Azure Monitor covers.
Azure Monitor is a unified monitoring platform
for all Azure resources.
Now, particularly, we're gonna talk
about things such as metrics.
Now, metrics are generally numbers,
and it's basically the things like CPU utilization,
memory utilization, any kind of-
we'll go into VM here-disk I/O, right?
Basically, it's the performance metrics of your resource.
It doesn't have to be a virtual machine;
that these things could be storage accounts
and other things as well, okay?
So metrics are numbers.
The other option is logs.
Now, logs are basically going to be textual.
If we go into here-we've got a scope,
which happens to be right now set
to a virtual machine scope.
You can have multiple virtual machines
in the same log report, but you can't mix
and match VMs with other resources.
Now, each resource type is gonna make available
to you a bunch of things called tables.
And so this is the virtual machine set,
and we're gonna have the metrics, heartbeat,
insights, and some VM-specific metrics,
as well as a generic AzureActivity.
Now, actuality, the activity log we see
on the left is also the same as this AzureActivity report.
Now, this window here-I'm gonna minimize this
so we get a little bit more space-this is a query window,
and the most simplest query is just
to have a table name and say run.
And that's like saying select star from in the SQL language.
This is called Kusto, or KQL-Kusto Query Language.
Now, by entering the table name and saying run,
I get a bunch of results,
and these are basically going to be the starts and stops.
And anytime I've updated the settings
of this virtual machine, it gets put into this table,
success or not.
Now, the real power here is that you can build a query;
you can filter out-let's say-you don't care
about the successes; you care about the failures.
Or let's say you don't care about when the VM started;
you care about when the VM was stopped.
Let's say you want to receive an alert every time
the VM is stopped.
And so you can go under queries-
this purple icon-and you can get an alert for updates,
automatic updates, CPU usage,
the computer is missing updates, malware,
and other types of things.
But...
Windows failed logins-that's a good one.
So if we ever have a Windows VM where somebody tried
to log in and it failed,
maybe we want to receive a text message about that.
I do have to remove the previous record here.
Now, the thing to note is this table might-
it clearly exists 'cause it's not giving me an error-
but it may not contain any data.
Well, first of all, I haven't not logged in.
So this login failure may not even exist.
I'm gonna run it and say, "Zero results.
Probably no results found in the last 24 hours."
But this language, you'll notice, has the table name;
there's a where clause, and there's a summarize.
So this is like the group by of the KQL statement.
Luckily, Microsoft does provide dozens and dozens
of examples of this KQL.
And if you wanna modify this-so let's say 24 hours
is not a good enough thing,
you want to run this across a week-
you just change the time range.
Let's say you wanna only receive the top 10 results;
there are various filters you can run against this.
Now, oftentimes, in order to get data into these tables,
you have to turn on diagnostics or Log Analytics.
So I'm gonna exit here and go
into one of the virtual machines.
I'm gonna go into VM demo two,
which was a VM that we created
for the last video in this series.
And if I go down to diagnostic settings,
right now it's not collecting;
it's asking me to create a storage account in order
to store CPU, disk, and network.
In fact, this is being marked as deprecated.
If we go into the logs option,
there is a more modern way to collect this information.
So I'm gonna say enable logs,
and it's offering me this OpenTelemetry option.
So OpenTelemetry is the modern way
to collect this, and we can set the settings.
There's also the classic log-based metrics
that we would've seen there just a few months ago,
but I'm gonna leave OpenTelemetry for now.
It comes with some graphing;
we're not gonna worry about that,
and I don't wanna enable the alert just yet.
So I'm going to just turn on OpenTelemetry
for this particular VM.
We can see on the screen the types
of data that's being collected:
performance counters and per-process metrics.
It's being stored in an Azure Monitor workspace
for the region, since this already exists.
So I'm gonna enable that, and it does take five
to 10 minutes for this to be enabled.
So it will take a little bit for us to get data out of this.
Now, I have this already enabled on another VM,
so I'm gonna switch over to the VM one,
and there is a monitor tab.
So right off of the VM, there's this monitor tab.
We can see green check boxes saying it's been up,
it's available, there's been no outages.
I can scroll down to the graphing,
and I can see that availability has been pegged
at 100 for a while, and CPU utilization is less than 1%.
There are some graphs that are not collecting data,
and we would have to then change the way
that data is being collected
in this what's called data collection rule.
So when I click on it, and I click on data collection rule,
there are two concepts here.
One is called sources and resources.
So for this data collection rule,
it's only connected to this one VM.
The data sources are going to be the performance counters
that we care about.
So I'm gonna click on this,
and we can see that there's only one CPU-related performance
counter being collected every 60 seconds,
and some of these other ones are not being collected.
Same with disk; there's I/O and operations,
but not other metrics related to that.
So it's trying to conserve the storage space
for what's being collected.
Now, for this one, what I've done is
I want to collect the memory ones,
and so I've selected all of the memory-related ones,
even though this is not a Linux VM.
I collected all of the memory ones.
It gets stored in what's called an Azure Monitor workspace,
and I can say Save.
And so this is going to start collecting
the memory-related counters for VM one.
Now, when we enabled the monitoring for this resource,
we were offered the ability to set up an alert,
and I declined it.
But we can get notified when things happen
relating to this resource.
So even within the monitor tab of the VM,
I can enable an alert; at the bottom here,
it says "enable recommended alerts."
And so Microsoft has a set of alerts
that it recommends for virtual machines.
One of them is a VM availability
ever falls less than perfect.
So if a VM is only 90% available, that's not good;
I want to be alerted.
Or there's these guest OS metric rules,
and there's a bunch of them;
we can dig into that in a second.
Right now, it's set an alert just as an email,
but I can obviously change this to text me,
or to run a program, or to call a webhook,
or something like that.
Now, in order to set up this alert,
I'm gonna need to set up a managed identity.
Now, I do have one called Alert Identity.
Now, it should be able to get an alert
if this VM has these triggers.
Now, I don't have to go with the predefined alerts.
I can always go into alerts and say create an alert rule,
and then set the conditions at which an alert gets notified.
So, for instance, if I just want
when the memory gets below a certain figure-
so in this case, I'm gonna change this to gigabytes for my-
so if I get less than two gigabytes of free memory,
then I want an alert on that.
It's gonna check every five minutes to every minute,
sorry, that there is at least two gigabytes of free memory.
Now, I can see here that the free memory dipped to 2.1,
but it's always stayed around 2.3.
Actually, maybe that's a bit.
So I'm gonna change this to 1.5 gigabytes,
'cause if it gets down here, then I can really worry.
Now, the actions, again, are- it's not just email.
So let's look at what's called an action group.
So an action group- I'm gonna skip over this into actions.
You can see that the actions can be to run an automation,
call an Azure Function, pass an event into Event Hub,
link in with an IT ticketing system-
might be a third-party tool-Logic App,
or calling a webhook,
which, again, could be a function
or some other type of end thing.
The other thing, of course, is you can get it
to email to people who have an Azure manager role.
So let's say you have the VM manager role;
well, then send an email to all the VM managers
with this, or send an email SMS message,
or a some other type of notification to a phone,
or to an email address, or a phone, or a voice call.
So there are lots of options for notifications of alerts
and lots of triggers that can cause an alert.
So in my case, I couldn't find
that the Azure Monitor Agent was running there.
Didn't seem also to be an option
within the virtual machine to add it.
It's supposed to be automatic when you set up the telemetry,
but it didn't seem to be for me.
It says not onboarded.
So I just ran this little command line saying
az vm extension AzureMonitorWindowsAgent,
and that will install the Windows agent
on these Windows machines, both of them,
so that I can collect the data for these charts.
Alright, with that enabled, if we go back to the VM,
now we're seeing numbers on these memory utilization
and top processes, et cetera.
If I go back to the monitor
under insights, virtual machines,
the VM is still not going to be listed as enabled
because we're not using classic logs;
we're using OpenTelemetry, but on the performance tab.
Now I wanna share with you a couple of tools that we can use
to verify connectivity.
Now, one- it's called Network Watcher-
and there's a service, so we'll go into it.
And the first tool we'll talk about
is called IP Flow Verify.
So IP Flow Verify is going
to check your network security group rules.
So let's say you've got a virtual machine called VNetdemo1.
It only has one network interface card,
and you wanna see if that virtual machine can go
to another place.
So I'm going to put port 80 here,
and we can check if it's able to connect to the second VM.
So this is an outbound test over the TCP network,
port 80 from VNet1 to VNet2,
which is the VM name-sorry for the confusion.
And this is literally just gonna check the network
security group rules.
So can the front end VM talk to the backend VM over port 80?
It should be green because all traffic is allowed.
There's a allow VNet outbound rule on the NSG
that allows traffic.
Now, if we were to do another one where we
were checking in-let's see-do an inbound test,
and instead of testing the remote IP,
I'll test my own IP, right?
So I'll paste my own IP in there,
and I'm gonna see if I can't connect
to port 80 inbound to the first VM.
Now, I'm expecting this to fail
because we do not have port 80 open inbound.
And, of course, this was denied
because all traffic inbound is denied by default,
except if it's allowed, and we don't allow traffic.
The other thing we can test-
I think 3389 is the RDP port-and so we can see
if I can connect to that machine by RDP,
and I happen to know that I can because I do it,
and we have a rule-there should be a rule-
that allows RDP traffic through the network security group,
and that is allowed
because we have a specific rule for that.
Alright, the other tool that I'll talk
about is called Connection Monitor.
And you can set up a monitor between two points,
and it will run it every 30 seconds.
So let's say create, give it a name,
connect one subscription.
I'm gonna choose Canada Central is my location,
'cause I happen to know that's where the thing is.
Now, the way that this works is there's a test
between a source and a destination.
So the source: we have the choice
of the entire subscription, a resource group,
VNet, or subnet.
So I'm gonna choose this subnet.
This is the front end subnet.
We just tested it as a source,
and we can see that the VM is selected as the endpoint,
and we can choose either the private IP or the public IP.
Let's just choose both.
And what is it gonna try to connect to?
So I am gonna choose also in VNet demo.
I won't choose them all.
I'll choose the backend.
And this is the demo backend.
Again, we can choose private or public
IP addresses for that.
It's on the backend subnet.
So now we have two endpoints:
the front end subnet and the backend subnet.
And it's a matter of setting up
what do you want the test to be.
Now, you can-if we had a web server running-
we could use the HTTP protocol to test
that the web server's responding on port 80,
or, without the web server, we can just ping-not ping-
but use the TCP protocol, open up a port,
and see if it would respond.
So if I created this, it would be test one.
I know that the front end and the back end
can talk to each other.
So it's gonna try to open port 80.
Now, there's nothing listening on that port.
So we don't have a web server.
It'll check every 30 seconds,
and if 5% of the checks failed
or the time takes more than 150 milliseconds,
it's gonna fail, and that will be the test.
So Network Watcher is a way of or Connection Monitor
is a way of setting up, essentially,
an alert that checks the connectivity
between two points and will let you know
if something is amiss.
Alright, so that's the exam-cram view
of the relevant monitoring.
Now let's talk about backup and recovery.
If I go into one of my VMs, this is the second VM,
the so-called backend.
Under overview, you'll see that there is backup
as one of the options.
So when we set up this VM, I did not set up a backup,
but we can go ahead and do that.
Now, there is a concept within backups called
the Recovery Services vault.
And this is specifically for backing up
and restoring virtual machines.
We can either create a new one or select an existing
backup Recovery Services vault.
Now, the backup revolves around what's called
a backup policy.
If I go to create a new policy,
you can see that I can choose hourly, daily, weekly backups.
You can choose the time, how frequent,
and how long to give the backup to complete,
and specifically what time zone it runs in.
So there's a couple of concepts here.
One's called Instant Restore.
So it's gonna be able to restore the backup faster
because it uses something called snapshots.
So it can get you back to a recovered state quicker
within a seven-day or less old backup.
By default, you'll see this policy forces me
to retain daily backups, and the default here is 30 days.
So if I ran this job, over the next month,
it would take a backup every day.
In fact, it's gonna take a backup every hour,
but it's gonna retain one day's backup per day
up to 30 days.
So a daily backup for 30 days is retained.
Now, you could also aim for some weekly backups.
So you only get one month of daily backups,
but beyond that, you could keep another couple
of months of weekly backups, just in case.
If you really want to go crazy,
you can keep monthly backups.
So the first Sunday of every month for the five years,
it keeps monthly backups.
That's 60 monthly backups, 12 weekly backups,
plus 30 daily backups.
That's a lot of files.
You're obviously paying for the data storage.
So, but if that's important to you,
you can set this all up, right?
So that's that backup policy.
Now it's going to back up the operating system disk,
of course, but I could also make it
that it backs up any future disk that I added.
So additional disks get included or not.
If I say enable backup, then this is going to link
to this-a Recovery Services vault-
and it's gonna schedule the first backup.
Now, I should be careful because you can stop a VM,
and you can delete a VM, but it is not so easy
to delete a Recovery Services vault.
There is a soft-delete concept
where it's going to retain those backups.
I believe we-it was for seven days, the snapshot.
And you cannot delete the backups of a VM quicker
than seven days.
This is gonna protect you against malicious deletions
or accidental deletions.
So we saw that Recovery Services vaults
are for specific resources like virtual machines,
Azure Files, and even the databases inside of a VM.
But what if you want back up your storage account?
Well, that's possible,
but that is a different service called a Backup vault.
And so a Backup vault is a newer type of backup.
It's kind of got of a different architecture,
but it is specifically for storage accounts
and other types of databases.
So I'm gonna create this in my VNet.
I'm gonna call this my backup.
And it matters what region it is.
You wanna put this in the same region as your resource.
So in this case, I'm gonna put this in East US 2,
and you get to choose whether you want your backup
to be locally redundant, zone redundant,
geo redundant, just like storage accounts.
You can choose to have your backups
located in other places.
So I'm gonna sort of not set all these settings.
You can make it harder to delete, so immutable.
You can have a soft-delete retention period
differently than 14 days, et cetera.
So we'll skip this, and we'll just say review and create.
Alright, so let's go to our Backup vault.
Now, if I click backup, we can see the data
sources are managed disks, blobs, which are unmanaged,
the various Azure database options, MySQL,
PostgreSQL, Azure Data Lake Storage, Cosmos DB, Kubernetes.
So I'm gonna choose Azure Blobs, and I'm gonna say next.
And now we get to define the backup policy,
just like we did for the VM.
So this policy-I'll call it policy-and the schedule:
we have a couple different options.
One of them is operational backup,
which just means it's always backup.
It's called a continuous backup.
There's no schedule.
It's just, whenever there's a new file added
to the storage account,
it will eventually get back into the backups as well.
And this will keep for 30 days.
Okay?
So that is an operational backup.
The other one is a traditional-
what they're calling vaulted backup.
That can't be unselected,
and you can have either daily or weekly.
You can schedule the time when this backup runs.
So every day at 11:30 at night,
and that'll keep 90 days worth in this default.
I can obviously edit that.
So this is my policy.
I can say Create.
All right, so next step: I gotta choose what to back up.
So these are the data sources.
So I'll add a storage account.
I have one.
It has very little in it, but that doesn't matter.
So it's now checking the storage account to see
if it is okay.
All right, so there is a security.
We do need to assign a role in order
to get the backup access to the right account.
So I select it, and I say assign missing roles.
Tell me to wait 10 seconds.
Alright, ready to go.
So when I set this button, configure backup,
then I'm gonna get daily backups,
scheduled backups to the storage account,
as well as continuous ongoing backups
to the Backup vault, which is, again,
different than the Recovery Services vault.
So the real trick then is
what to do when you want to restore.
So let's say you have your virtual machine,
and something happened to it.
It's been corrupted.
You can't log in.
You can't-rebooting doesn't save it.
And you want to restore back to the way that it was.
So we can navigate in the Recovery Services vault
to the virtual machine.
The one that we added is still pending,
but I do have a previous one,
and we can see that there's-I can force it to back up now.
There's also a restore option,
and there's also the option to just grab some files from it.
Now, restoring this virtual machine will not kill
the one that's currently running.
It's actually gonna create a new machine.
So I'll have- this is a VM one.
I am going to have a another virtual machine
that is a copy from the backup of VM one.
Of course, I can also replace the existing VM
if I so choose.
I won't consider continue with that.
But also, as you saw,
we can get access to just some files from this last backup.
So there's a way to download it:
a program that will mount my recovery point
as a local drive to the machine.
And then, when I'm done with it, I can unmount,
so it becomes an SMB-mountable disk.
If we go to the Backup vault-
I called it my backup, right?
I can go down to the backups and see
that we have one protection is configured.
Again, I can force a backup,
although there is continuous backups.
So I can force it in the scheduled sense.
Also, I can restore this.
Now, this restoring-this backup will create-
I can choose from the continuous backup,
the operational backup, or the specifically vaulted backup.
I can, of course, restore all the blobs,
choose up to 10 containers to restore,
or have some type of prefixes that I want to restore.
So as you can see, we have the ability to do backups
in files, blobs, VMs, and restores is pretty,
pretty straightforward: point-and-click.
Now, the last thing I'll probably talk about,
going back to Recovery Services vault,
is this concept of the Azure Site Recovery.
So Azure Site Recovery is basically a way
of replicating a virtual machine to a secondary region.
You can go into-
let's go back into the VNet-
and we're gonna click on disaster recovery.
And so what this is gonna do is:
I have this VM in Canada Central;
I can choose another region
where this VM could be copied to.
So you can replicate your VM to another region
for business continuity and disaster recovery needs.
So let's say I want to have this VM in Canada
and also same setup in the U.S.
As you can see, it's not just the VM,
but it is going to create a resource group,
a virtual network.
It's going to honor the availability settings,
or PPGs, proximity placement groups.
If I have reservations, there's that.
It will also eventually load up
the storage account that's required and things like that.
So this is gonna allow me to either instantly copy the VM
in the case of I want it to be running
in a new region quickly,
or set it up such that I can do it
in a sort of moment's notice.
So a prepared restoration, as opposed to ready to go,
maybe like- I guess better to say synchronized.
And when the two regions are synchronized,
then you set up when it fails over.
So let's say the VM is down.
There's no hope of recovering it.
You log into Azure, and you say fail over.
And then the secondary region,
which in this case is East US, becomes your primary region.
And if the original region gets recovered,
there's a thing called a fail back.
So you fail over when it's not working,
and then, when it is working, you can fail back.
All right, sort of tying this section of the video
with the previous section,
you can actually monitor your backups.
That makes total sense.
You go under your Recovery Services vault monitoring,
go into diagnostic settings,
and you could set up a way to monitor the backup jobs.
We could set up some sort of reporting
so that you can see when backups are happening
and also your Azure Site Recovery jobs and events
and all of the metrics related to that.
So it's pretty straightforward.
Now, this is using the old Log Analytics method,
and you can choose which data, the jobs data,
any kind of events,
and that'll go into your Log Analytics.
And then you can go into Azure Monitor,
and you can see the performance of your backups
and trigger alert when it fails, for instance.
Anyways, that's been a too-short review
of all of the requirements of the AZ-104 exam.
In these videos, we've covered all of the topics
in the requirements document.
And so, again, if you have any questions
or you want to review, there is a full set of videos
and a full course on it from me.
I hope you seek that out.
And otherwise, I wish you the best of luck in your exam.
Hopefully, this is all retained in your short-term memory,
and you go this afternoon or tomorrow and take the exam.
Good luck to you.
I really do wish you all the best.


### 📺 Lesson: Congratulations!


[No transcript available for this lecture]


### 📺 Lesson: Renewing Your Administrator Certification


-: So in this video we're gonna talk about renewing
your Microsoft Azure Administrator Associate Certification.
Now up to six months in advance
from when your certification expires,
you're going to receive an email from Microsoft
with a subject Action Required,
and it will tell you that you have a certification
that's going to expire on a certain date.
And so again, you have six months to prepare for this.
Now, the renewal of the exam is completely different
than the initial taking of the exam.
The renewal is free
and it's done completely online from home.
There's no proctor, you're not registering
with your license, there's no webcam involved.
You're just taking an online multiple choice
question assessment, and if you pass,
you will renew your certification for another year.
So the initial expiration is one year
from the time that you took it,
and you need to do the online assessment
every year after that.
Another thing that is important to know
is that the renewal is not as comprehensive
as your initial test.
See if we go down here and we click
on Renew Your Certification,
it's gonna take us to this page here.
Now, I haven't signed into the Microsoft Learn site
so this is not personalized to me at all right now,
but this is the portal for the renewal
of the administrator certification.
Now you can see here that these are the topics
of the renewal.
At the time of recording,
it's talking about these eight topics.
Now in the original AZ104 exam
with the Azure Associate Certification,
there are dozens and dozens of topics.
So this assessment is only limited to these eight topics.
Now these topics are gonna be
things that are relatively new in the last 12 months
that are important for the exam.
For instance, it's talking about Dockers,
talking about Azure D and Nest,
in this case of administrator service endpoints,
Azure Backup, Kubernetes, and Azure AD.
These topics are what is focused for the renewal.
Now, the renewal is free,
and what you can do is if you don't pass the first time,
you can take the assessment again immediately.
So you can take it twice in the first day
and after your second attempt,
you need to wait 24 hours between retakes.
So if you have 180 days of notice
to renew this certification,
then technically you have 181 chances to pass this test.
And so technically
you could just take the certification assessment repeatedly
and you'll eventually pass.
The material will start to sink in.
Now, Microsoft does also have a collection
of Microsoft Learn modules,
and so all of the topics of the exam,
you can see that there are free training
on the Microsoft Learn website relating to these topics.
So if you just wanted to sit down,
now this is according to their timing
it looks like about six or seven hours of effort.
I don't find these timings particularly accurate.
It's not gonna take you one hour to get through this.
I guess it could,
but generally you'll get through this in 15 or 20 minutes,
or you can just review the things that you're not sure of.
So if you're good on a lot of these things,
but if the DNS that you really haven't played within a while
maybe you wanna review this.
My personal recommendation is to take the assessment you get
to takes in one day for free.
I would just take the assessment,
because there's a good chance that you'll pass.
And it's gonna take you about 15 minutes
to go through the assessment.
And maybe that's it.
You take the assessment, you passed, no preparation required
and you're good for another year.
So I would start by taking the assessment.
That gives you an overview of your strengths or weaknesses,
when you take the assessment and fail,
Microsoft will actually recommend specific learning modules
for you based on your weaknesses.
And so you'll get your own personal collection
to take the renewal a second time.
So maybe you take it if you fail
then you do the preparation based on Microsoft suggestions
and you take it again.
As you can see, taking the renewal is a lot less onerous
than taking the original exam.
The amount of content covered is very specific.
It's multiple choice questions done on the web.
It's not the same level of scrutiny.
You don't have to have a room with a locked door
with no papers, none of the same requirements
as of taking a real test, just take it.
There's no time limit.
I believe you can take your time with each of the questions.
So that is how you do the Azure administrator renewal.
Again, to look out for an email that says 'Action required'
from Microsoft,
and that will tell you
what you need to do to renew your certification.


### 📺 Lesson: Pass AZ-104 Azure Administrator with the Help of AI


So I don't know about you, but I find myself using AI for a lot these days.
Almost every day I'm in ChatGPT or some other AI to help me to do something.
So in this video, I want to talk about how you can use AI to help you study for the AZ 104 exam, including
create this cool little graphic for it.
Now the first thing that you can do is you can create your own study plan.
So in the previous lesson, I show you a 30 day study plan that if you wanted to start from scratch
and learn the content of AZ 104, that's a complete study plan over 30 days.
But let's say you've got more time available to you, and you want to shorten the amount of studying
required.
You want to do it in 21 days, or you want to do it in 14 days, but you can do a couple of hours a
day of studying.
You can go into your favorite large language model and ask it to create a study plan, giving the restrictions,
how many days you want and how many minutes per day you have to study.
What I like to do is I include a link to the exam objectives, because a lot of times these, uh, and
large language models would pull in requirements from an older objective.
You know, there's a lot of content on the web.
And so it's not sure what's the latest.
So we know that this AC 104 exam was updated as of this date.
And we want to ensure that the answer reflects that.
And then you can actually go through, you know, always double check what the eye tells you.
Go through and make sure that all of the resources listed are, uh, what's on the exam, the topics.
Now notice there's also links under each of these in this example where you can go to the Microsoft
Learn page.
And there might be a little short course or some other content that you can use to learn this.
Of course you have this course, and so I would hope that you would be watching my videos on this and
following along with this study plan.
So you can obviously customize the study plan to your own search situation.
Maybe you've already spent a year working with it, and you want to focus on virtual machines and infrastructure
as a service or something.
You can tell it.
I want my study plan to reflect something else.
All right.
The other thing you can do is you can have it quiz you.
So I can say, I want to pass the AZ 104 exam.
I want you to quiz me, come up with a multiple choice practice test exam.
But don't tell me the answer.
I will guess the answer and you will tell me if I'm correct and then you will create another one.
So it sort of loops and makes sure again listed based on the latest exam requirements.
And so here it comes up with a practice test Test question.
Now once again, these things do not necessarily are right.
So if you see something that seems a bit off then you should question it.
You should not rely on this as being 100% correct, but it can be helpful.
The third thing is if you have specific concepts that you are having trouble grasping.
So if you go through the exam requirements and you understand almost everything, but there's a couple
of things that you think are a bit weaker besides watching my videos, of course you can just say I
want to explain the concept of private endpoints.
That's perhaps that's what you're sticking on, and you tell it the exam code and it will give you the
answer.
And in this case a deeper understanding way.
If you're studying a fundamentals exam, it might have a lighter understanding weight.
You can even ask it to guide you through a demo.
Give you some quick steps that you can get started now.
ChatGPT is great, I, I particularly like it, but it's not the only one out there.
If you want to try Google Gemini.
I think Gemini is also come a long way.
Uh, this is 2.5, 3.5 is out.
And I think that's been um, generally they've caught up to ChatGPT and a lot of ways.
So you can certainly ask those questions to Gemini.
One thing that I do also like is there's a Google tool called notebook LM that's notebook LM google.com.
And what you can do is you can upload your own sources.
Okay.
So these this could be I'm going to zoom a little bit.
This could be the PDF um for the exam objectives or links.
So here's the Microsoft Learn website.
It's a link a video.
Maybe there's some interesting long YouTube videos.
You get your own sources and then you can chat with it based off of those sources.
So you're not querying a generic model that is not is trained on the entire web and not trained on specific
documents.
Notebook LM only answers the question to the extent that the answer lives within the sources, and you
can have up to 50 sources.
So you can build yourself up a little.
AZ 104 notebook.
And then you can query specifically the official Microsoft documentation and nothing else.
Another cool feature of notebook LM is this concept of the deep dive.
So these are two AI generated hosts who are talking in a podcast format.
And so they've they've got the they've read the sources and they understand it.
And so they're going to create a ten minute or so conversation based on the content.
That to me is actually quite approachable.
You can sit down for ten minutes, listen to them talk.
It's I, of course, but it actually has read and digested some fairly deep stuff and can create some
audio that provides you some insights if you like to listen to it.
So those are a few ways you can use AI to help you learn.
Now I am fascinated by this stuff.
AI has been revolutionary and I think it will continue to be.
If you are using AI to help you study for the AZ 104 exam in a way that I haven't mentioned, please
let me know.
Make a comment in the Q&amp;A section of this course and just say Hey Scott, I am using AI for this.
You don't have to, uh, you know, get long and detailed, but just give me a heads up in terms of
how you're using AI to help you pass, and that could help other students as well.
So attached to this video is a text file that contains the prompts that I've been using.
So I copied my prompts.
And you can take them right from the text file attached as a resource to this video.
Anyways, let's continue on with the AZ 104 exam.


### 📺 Lesson: Study Guide


[No transcript available for this lecture]


### 📺 Lesson: Bonus: Your Next Step – Practice Tests


[No transcript available for this lecture]
