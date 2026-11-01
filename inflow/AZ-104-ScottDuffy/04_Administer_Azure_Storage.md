---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "04"
title: "Module 04: Administer Azure Storage"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 04: Administer Azure Storage

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** Storage Accounts, Redundancy (LRS/ZRS/GRS), Access Tiers, Networking & Firewalls, Data Protection, Encryption, Blobs, Files, Queues, Tables, Access Keys, SAS, Stored Access Policies, Entra ID RBAC, Lifecycle Management, Object Replication, AzCopy, Azure Files & Snapshots  
**Line Range:** Lines 5837 – 7611 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


### 📺 Lesson: Create Storage Account


Instructor: So as you can see,
about 1/5 of this exam
says "Implement and manage storage."
There are three sub-objectives underneath that,
including configuring access to storage,
configuring storage accounts,
and Azure files and Azure blobs.
So in this section of the course,
we're gonna talk about storage.
Now, despite only being worth
around 1/5 of the exam score,
it's actually a pretty big topic.
We do really need to get into a lot of the nitty-gritty
when it comes to Azure storage accounts.
In my view, a storage account
is one of the three fundamental services
in infrastructure as a service.
The other two being virtual machines and networking.
So let's go to the Azure portal,
and let's look at the process
of creating a storage account.
So I'm going to say Create a resource.
And right off the Get Started tab,
storage account is one of the more popular resources,
or I could always go to the Storage category
and say Create.
Now, over the years,
this interface has changed slightly from time to time.
We have at the current time
six tabs of the wizard
plus the Review and Create tab.
Like any resource in Azure,
you must select a subscription,
and you must select a resource group
for this resource to live.
You also must give the storage account a name.
As it says in the tool tip,
the name must be unique
across all existing storage account names in Azure.
And so as a result,
you might have to get fairly detailed
when it comes to naming it
given that there are millions of storage accounts
across all of Azure.
Now, as most resources,
we have to pick a region of the world
to deploy it to,
and I've got the default here,
which for me is East US.
It could be different for you,
I'm just gonna leave it in the East US region.
Now, the region that you choose
could be important for a couple of important reasons.
One is going to be pricing.
The region that you choose
is directly related to how much you're going to pay.
As you can see, there is a price of 2.1 cents per gigabyte
for the first 50 terabytes in this East US region.
If I was to choose a different region, such as UK,
it's actually cheaper,
1.9 cents per gigabyte.
So the region of the world actually does affect pricing.
Second thing is you want your data
to live close as possible to the places
where you use the data.
So if you have your apps
and your virtual machines in one region,
and they access that data in a storage account,
you may want your storage accounts
to be in the same region.
Third, you may have various data residency requirements
that you have to live by.
So again, different countries
and different regions are gonna have laws
where data must be stored for their citizens.
And so if you are, for instance, a European citizen
and you're storing the private data of European citizens,
then perhaps you may have to store that data
in the region of Europe.
So you're gonna choose region
based on a number of different factors.
Oh, finally, there might be various features
that are only available to certain regions.
Microsoft does have the tendency
to roll out new types of things
to one region before another
so that they can be tested out.
So if you are dependent on a new feature
that is just being released,
you may have to choose a region for that.
One of the new changes to the UI
is to select your primary service.
Now, the most normal one is called blob storage.
Data lake storage is a special type of storage
that's for extremely large amounts of data
using big data-type workloads,
but blob storage is gonna be the most normal selection.
If you need files or you need something else,
tables or queues,
you would choose a different option for this.
Continuing on this page,
this is gonna be one of the first options that we have
having to do with speed and latency
in terms of access.
So if we were to choose a premium account,
as you can see, it's got recommended
for low-latency scenarios.
Now, the premium account has a much higher
per gigabyte charge per month,
as well as a lower access charge.
So it's gonna be, let's say, 2/10 of a cent
for 10,000 read operations
versus 6/10 of a cent under normal hot access.
So premium access is more expensive per month per gigabyte,
but cheaper to read from.
So that's just one of these decisions
that we're gonna make right off the top here.
So we're just gonna stick with a standard storage account.
Now, we do need to talk about the concept of redundancy.
So I'll pause the video here,
and in the next video, we'll talk about these options
for how your data is stored and protected
in case of failures.


### 📺 Lesson: Storage Account: Redundant Storage


Instructor: So while we're on the subject,
let's talk about redundancy in Azure storage accounts.
So I'm in the process
of creating a storage account in east US.
When I get to the redundancy part of that basic screen,
I'm given four options locally-redundant storage,
geo-redundant storage, zone-redundant storage,
and geo-zone redundant storage.
What does this all mean?
So the concept of redundancy is that by default for free,
Microsoft is going to keep multiple copies of my files
in case of failure in case of emergency.
So even at locally redundant storage, which is the cheapest
and most basic option, Microsoft is gonna keep a total
of three copies of any file I upload
into the storage account.
So the reason it does that is
because hard drives from time to time fail,
they are spinning magnetic discs.
And despite our best efforts in engineering,
after so many thousands of hours of active use,
the hard drive could experience some type of failure.
So Microsoft keeps two additional copies of that file
such that if the hard disk was to fail,
then they're able to reconstruct the hard disc
based on the files they already have stored elsewhere.
The reason they do three
and not two is in the very, very unlikely case
that two hard drives fail, that contain the same files.
So this is giving you a lot of redundancy
and resistance to failures, server rack
and drive failures.
So for locally redundant storage,
you're going to get three copies of your files.
This is stored in a data center.
So I've chosen east US as my region.
This is gonna be stored in one region
of the east US region in one data center.
Now zone-redundant storage would be the next more redundant,
the safer option.
What this does, it still keeps three copies of my files,
but instead of keeping them in the same building,
it spreads them across three different buildings
in the region.
So these are called data centers.
And so zone-redundant storage would protect you in case
that the entire building was to lose power
or to have a flood or some kind of a disaster was to strike.
Your files are safely stored
in a physical separate location.
I should point out that not every
option is available in every region.
So in east US it has these options.
If I go down to north central US,
it's one of the older regions
and we can see that there's only locally-redundant
and geo-redundant.
It doesn't have the concept of zones in north central US.
So as you might expect,
then going to geo-redundant storage is even safer still.
This takes your data out to another region.
So in the case of east US, this could store three copies
of your data in a single data center in east US,
as well as three copies
of your data in a single data center in west US.
So these regions are paired
and so they're basically storing six copies
of your files in two different regions.
Now, geo-redundant storage is also not available
in every region.
So for instance, if you go to Qatar,
then you'll see that you only have the option for locally
and zone-redundant storage.
And then for the last one, geo-zone redundant storage.
That is the safest option of all.
It's going to combine the two.
It's gonna keep three copies
of your files in three different data centers in a region
and three additional copies
of your files in three data centers in the other region.
There are costs associated with this.
So when we go to the costing screen, we can see,
I'll go back to east US.
That LRS is costing in that range
of 2.10 cents per gigabyte.
But if I go to a zone-redundant storage,
that is now 2.60 cents per gigabyte.
And I want to go to geo-redundant storage
prices could change of course, but 4.6 gigabytes.
You see we've now doubled the cost
and geo-zone redundant storage.
The last thing I would say about storage is when you get
into the geo-redundant storage area,
when you've got two regions,
you have the additional checkbox that allows you
to have a read-only access to the second region.
So if I was to check this checkbox,
I would have a second URL
that I could read data from the storage account.
So in the case of east US,
I know that the data's also stored in west US
and I would have a read-only URL
for the west US data in case of emergency.
And of course that does have an impact on pricing too.
So when I go to read access geo-redundant storage,
then I'm going up to 5.90 cents per gigabyte.
I believe it was 4.6 without that second option.
So an extra one
and a half cents almost for this option.
So redundancy really just makes it much more difficult
for Microsoft to lose your files.
The higher you up you go, the more you pay.
But then the more you would expect your files
to be perfectly fine
and survive for millions of years in Microsoft Azure,
as long as you pay for it.


### 📺 Lesson: Storage Account: Advanced Options


Scott: We've been creating a storage account here
in the Azure portal.
I'm gonna leave the one that we've created in the East US,
and I'm gonna choose locally redundant storage,
and I'm gonna hit next, which will take us
to the advanced tab.
As the name implies,
the advanced tab contains a lot of security, access,
and other settings.
Under security, the first setting says,
"Require secure transfer for REST API operations."
This basically means that you cannot interact
with a storage account using unsecured,
unencrypted, so HTTPS is the only method
for interacting with this over the API.
This here is enabled by default,
and you probably should keep it
unless you have a good reason
for not needing secure transfer.
Second option is enabling anonymous access.
Now, this is a big security risk.
It's happened dozens of times in the past,
where someone is looking around,
and they find an open anonymous storage account
or storage bucket for AWS, so it is off by default,
and unless you're gonna use the storage account
for web files, like images and MP4 files and JavaScripts,
unless you're intending anonymous users
to be able to access them, I would leave it off.
There are two methods of authorization and authentication
to get access to the storage account.
One is what's called storage account key,
and that is on by default.
We're gonna see in a coming up video
about managing your keys.
Basically, the key means if you have the key,
which is a series of letters and numbers that is very long
and impossible to guess,
then you can get access to the storage account,
the contents of it.
So it's what's called claims-based authentication.
Or do you want to use Microsoft Entra,
which is role-based access control that is handled by Entra?
Storage account key is on by default,
because if you're going to be using applications
and legacy applications,
this is what's traditionally been supported.
In order to use Entra, you have your applications register
with Entra, and there's special methods
that they're gonna need to get authorization.
Obviously, TLS 1.2 is the minimum.
I believe it's been shown that 1.0 and 1.1 are,
at this point, insecure,
so leaving it at 1.2 is perfectly fine.
We'll skip over the preview feature.
Now, I mentioned in the last video
that Data Lake Storage Gen2
is a different type of namespace.
It's an actual hierarchical namespace
where you can have files and folders.
In a default storage account with blobs and containers,
it's a container model, and basically,
everything goes into the container.
Data Lake Storage Gen2 is more of a files and folders model
specifically for big data analytics,
and it has different limits
in terms of the amount of data you can store,
and it has different access control policies,
so we're not going to talk about that much in this course.
This is where you would set it up if you want.
You would have to be using Data Lake Storage Gen2
in order to set up SFTP or NFS.
For blob storage,
we have, the most important thing here is the access tier.
Now, access tier is an important concept
and is a requirement for the exam, and so what we'll do,
we'll come back in the next video,
and we'll talk specifically about hot, cool, cold,
and archive.


### 📺 Lesson: Storage Account: Access Tiers


Instructor: So while you're in the process
of creating your storage account,
you can choose what the default
access tier is between hot, cool, and cold.
So first of all, what is the access tier?
Well, I'm gonna pull in the pricing page here,
and we can sort of see in this matrix
the difference between them in terms of pricing.
A couple of videos ago, we talked about premium storage
being the most expensive to store per gigabyte
and the cheapest to access per read or write operation.
And this is pricing in terms of 10,000
operations in one unit.
So premium really is for when you need
the quickest access to a file
and you're willing to pay a little bit more to store it.
Now, there is actually a way of saving money
using the premium plan over the hot plan,
but that would involve reading the same file
dozens of times per second, seven days a week,
24 hours a day all month.
So it's a pretty, in unlikely circumstance,
you may be better off using a Redis cache
than premium storage in that circumstance.
So if you do really need to access
a file quickly and frequently,
premium storage may be the way to go.
Now, hot storage is what you would normally
consider the default, right?
When you go into the screen, hot is chosen for you.
And the text says, "Optimized for frequently accessed data
and everyday usage scenarios."
So this is sort of a balance between the price of storing
and the price of access.
So we can see it's, in this case,
1.80 cents per gigabyte per month for hot storage.
And additionally, half a cent per 10,000 reads operations,
and 6 cents per 10,000 write operations.
So that is the balance between the price of storage
and the price of access.
Now, if you do not need to have access
to the file as frequently,
what is considered infrequent access,
you may wanna consider cool storage.
It gives the example of infrequently accessed data
and backup scenarios.
Now, cool storage is almost half price
per gigabyte per month.
So you'll see that it's 1.80 cents for hot
and 1 cent for cool.
But in order to pay half the price for storage,
you are going to pay exactly double for access.
So instead of 6.50 cents for 10,000 writes, it's 13 cents.
Instead of half a cent for 10,000 reads, it's 1.30 cents.
So you pay more for access, but it's cheaper to store.
That's why this is good for files
where you don't think you're gonna need
to access it even once per day, right?
The breakeven between the number of accesses
and the pricing per month is probably on the order
of less than one time per hour.
And you're gonna save money in the cool tier.
So maybe you want to consider choosing cool as the default.
Cold is relatively new.
And as you can see, you're actually paying
a way less for storage.
So instead of one cent per gigabyte in the cool tier,
it's one third of a cent per gigabyte in the cold tier.
And as we scroll down to see the data transfer,
once again, it's almost double.
So it goes from 13 cents to 23.40 cents for 10,000 writes,
and from 1.30 cents to 13 cents 10 times for reads.
And for this reason, cold may only be good for things
you really don't offer access at all.
So cold storage is rarely accessed data and backups.
So let's say the scenario
is you did a backup of your server yesterday.
Well, that might be good to be stored in closed storage
because the chances of you needing to restore
from a backup from yesterday are very low.
But you still may wanna keep backups from a month ago,
from three months ago.
You may have a need to keep older backups,
in which case, the chances of being accessed
are extremely low, and you're gonna save lots of money
storing this in cold storage,
around 5% of the cost of hot storage, or 20 times less.
But then you pay more if, in that case of emergency,
you need to access the file.
So that is hot, cool, and cold.
Now, one thing that's not offered
by default is archive storage.
Now, archive storage is very special in which basically,
you cannot access archive storage quickly.
The analogy will be an offline tape.
Back in the '80s, when you used to back up your mainframe,
you would back it up to tape,
and then you would just dismount the tape
from the tape drive, and that was your archive.
So this archive storage, you can move stuff to archive.
You'll see that it's another order of magnitude cheaper,
two tenths of a cent per gigabyte for storage,
but another order of magnitude more expensive,
not for writes, but for reads, you're looking at $6.50
for 10,000 operations as opposed
to only 13 cents or 1.30 cents,
or even half a cent for hot storage.
So this is more than an order of magnitude
more expensive for reads.
And if you are in a hurry,
let's say you use the archive tier, your server crashes,
you need to get access to that file,
then you're gonna pay $65 for high priority read.
So this really is for things that, let's say,
things you need to store for government purposes.
And if you ever do receive a request from the government
to retrieve it, you are going to wait several hours.
So it could be a four hour plus wait to get this back.
So archive storage is for that type of scenario.
You are not locked into hot, cool, cold, or archive
once you've made a selection.
This is just the default.
So you could have mixture of files.
Some of them are hot, some of them are cool or cold,
and even some of them are archived
in the same storage account.
There's no restriction on that.
So if you are sensitive to the cost of storage,
you're looking to save money,
let's say you have a lot of storage
and it's all in the hot tier, and you might think about,
what can I move to cool tier
in order to save almost half the price,
or even to cold tier to save
down to 5% of the original price?
Then consider changing your default
or consider moving your files between these.
It's possible to move them from one to the other.
Part of this course, we'll have a video on lifecycle access,
and we'll talk about automating the movement
from hot to cool, from cool to cold, et cetera.
So that is the decision for access tiers.
I'm just gonna keep this.
I'm gonna set this to cool access,
because the data that I'm using for testing purposes,
I don't mind paying a little bit more for access
because I'm gonna save so much on the storage cost.
Let's move on to talk about networking in the next video.


### 📺 Lesson: Storage Account: Public vs Private Networking


Instructor: All right, let's click next.
So on this tab we're talking about networking.
Now it might alarm you to say that by default,
storage accounts have public internet access.
That is that anyone anywhere in the world
can access the storage account if they know the public URL
and they have the access key
if you're using access key authentication.
So, the analogy that I use is that it's like having
a locked door on a busy street.
So, let's imagine you are a business,
you have a door that has a lock,
nobody is going to be able to get in unless they have a key.
Also, we can say that you can't break in,
there's no way to hack into Azure,
at least as far as we know.
So if you don't have the key,
you're not getting access to the files.
That is public access from all networks.
Now, let's say that still gives you uneasiness,
and so you want to restrict access from the public internet
and you only want access from selected networks.
So if you select the second option,
then you're going to be able to choose a virtual network.
So in this case, I'm choosing vm1-vnet
and choosing a specific subnet
and only computers that are connected to that vnet,
to that subnet can access the storage account.
So it is more private,
so any computer attached to this subnet
can access your storage account with the access key,
but not the public internet.
Now, maybe you do have certain public internet addresses
that you do want to have access
so I can add a public internet access address
to have access.
So this is, again, selected networks, very specific
either address or a range of addresses.
Finally, you have the option to disable public
and private access.
So there's a thing within Azure called private endpoint,
and you can set up, basically a proxy connection
from this storage account to another resource
inside of Azure and those are called private links.
So this is the most secure way
where you are specifically allowing
one resource to talk to this storage account.
This is for, again, virtual networks
and public IP addresses that you've manually added
or the public internet.
So that is your role of adding security
in terms of networking.
Also on the screen is a concept of network routing.
Now, typically you would not have to touch this.
Microsoft network routing is the default.
What does this mean?
So let's imagine that you have a resource
inside the United States
and you have a server in your office in Japan,
and that server in your office in Japan
needs to access a file from within the storage account
inside the United States.
With Microsoft network routing,
the Japanese computer is going to connect
to the Microsoft network in Japan,
and then it's gonna travel over a private network,
the Microsoft Global network from Japan to United States
to talk to your storage account.
With internet routing, this means that
from Japan, it's gonna travel over the public internet
encrypted of course,
and then enter the Azure network inside the United States.
So, that's why Microsoft networking is the default.
There's not really a great reason to choose internet routing
unless, well, unless you want to, obviously.
So, that is the networking screen.
I'm gonna leave the selected virtual networks option open
with my own IP address,
and that way I can test this from my home
but it's not open to the public internet
even if you have the key.


### 📺 Lesson: Storage Account: Data Protection


Instructor: All right, we're moving on
to click the Next button,
and we're coming up to the Data protection tab
of the storage account creation process.
Now, this is important because it's gonna allow you
to be protected from accidental or malicious deletion
or modification of files.
So we can see on this screen a number of check boxes
going down under recovery, tracking, and access control.
You have the option of enabling,
a option called point-in time restore.
Now, point in time restore is going to keep versions
of your files and allow you to go back to any date and time
that you specify within the maximum restore point.
And so you can go up to 30 days back
in terms of point-in time restore.
So let's say I wanna be able to go back
to any point within the last 21 days
in order to restore the container to that earlier state.
Now, like it says in the note, that in order to have this,
it needs other features,
such as versioning, change feed, and soft delete.
So speaking of which, soft delete is a feature
that means when you go to delete a file,
it doesn't actually get deleted.
It's called marked for deletion.
So when you have soft delete enabled,
it basically enforces a time period
in which you can still restore that file.
So even if you don't have point-in time restore enabled,
you can have this soft delete.
So with this setting, and it's on by default,
I can delete a file
and I still have seven days in the future where I can say,
"Oh, I actually made a mistake
and I want to recover that file."
The reason this is good
is because in case of malicious deletion,
any person that goes into your account
and deletes a bunch of things,
if you can catch it within this time period,
then you can easily restore it
without having to go to backups and others.
So there are three options for soft delete.
One is for blobs, one is for the entire container.
So if someone deletes the container,
you can restore it within those many days.
And also for file shares. This is on by default.
The only thing that this really impacts when you are testing
is it's an extra bit of work in order to delete files
when they're just test files.
So in a non-production capacity,
then this is actually more work.
Going down to the tracking section.
We do have the option of keeping previous versions of blobs.
So let's say you have files
that change every once in a while.
So every 30 days a particular file gets updated
in an update method.
Well, having versioning
means you're automatically gonna have version six,
version seven, and version eight.
And so Azure's gonna store those versions,
and you're going to basically pay for it.
So the more versions of something you have,
then the more gigabytes that you're storing.
You can control your versioning through data lifecycle,
which we'll talk about.
The change feed allows you to see
when somebody makes changes, create modification,
or delete changes to blobs.
So it's basically in a feed
that you can then listen to or you can query
and you can perhaps perform certain actions
when changes occur.
And finally, under access control
you have this concept of immutability.
Now, immutability means that a file
can never be altered or even deleted.
So this is for important files that once it's written,
you never ever want somebody to go
and change the contents of that file.
This would be like a security log,
would be a good example of this.
So if you're tracking everyone who's logged in or logged out
or login failures into your application,
you may consider some type of immutable log,
such that a hacker could not then go
and delete the log files and cover their trails.
So this is time-based retention policy
that applies to all blob versions.
So if you have versioning enabled,
it applies to all the versions of a file.
So you can have this at a container level,
or you can have this at an account level
or even at a specific blob level.
And in order to do this,
then you're gonna need to have versioning enabled for this.
All right, so that's the different data protection,
recovery tracking, and access control features
that you can enable for a storage account.
In the next video, we'll finish it up.
We'll talk about encryption and we'll create this account.


### 📺 Lesson: Storage Account: Encryption


Instructor: Okay, we're almost done here.
We're onto the second to last tab,
which is encryption.
Now the big decision here is who are you going to trust
to manage the encryption of your data
inside your storage account?
So all data is encrypted by default,
and if you don't change the setting,
Microsoft will encrypt your data.
This is called Microsoft-managed keys.
It's also Transparent Data Encryption, TDE.
What that means is that you don't get to interact
with the keys at all.
You don't have access to them.
You upload your files unencrypted
and Microsoft will store it on the physical hard disk
encrypted, and then when you go to retrieve the file,
it will automatically decrypt it for you
and you'll receive it unencrypted.
So that is a Microsoft managed key,
and it's the easiest thing to handle.
Now, slightly more complicated
is the concept of customer-managed keys.
Some companies insist on having the security keys
access to them.
Maybe they have a policy for changing them
every so many months.
And so customer-managed keys means that you create
and manage the keys.
Microsoft still uses them transparently.
So you provide the file unencrypted,
it encrypts it using your keys.
The way it does this is it stores the key
in what is called a key vault.
Key vault is a special Azure service for handling secrets,
keys, and certificates.
And so you can create a key
using the key vault and reference that key
when it comes time to creating your storage account.
So it's not too difficult to create a key in the key vault.
And then from that point forward,
Microsoft will use that key.
The default is Microsoft-managed keys,
and unless you really do wanna manage your keys
and take responsibility for that,
then I would suggest you select that.
Now, if you do go the way of customer managed keys,
additional challenge for you
is going to be what services are going to use
your customer-managed keys.
So is it only for blobs and files,
but you're gonna leave tables and queues
using Microsoft Method,
or is it for all service types?
Again, we're gonna leave this as Microsoft-managed keys.
Note that this option cannot be changed
after the storage account is created.
Do you know what's even better
than doing either Microsoft-managed keys encryption or CMK?
Well, that is doing another layer of encryption.
That is the infrastructure encryption option.
It's disabled by default.
You can enable it,
and what that does is it takes your file,
passes it through this first layer of encryption,
and then it takes the resulting encrypted file
and encrypts that before storing it to the hard disk.
So this is obviously a very secure,
because once they've, let's say someone was to get hold of
that hard disk and they were able to reverse
the encryption on it,
well then they would still only be getting encrypted files
out of that and they would have to reverse it again.
So this is going to make somebody's job
a lot more difficult.
So turning on infrastructure encryption,
if that's what you want, is an option,
doesn't cost anything extra.
It may add a little bit more latency
when it comes to the data that you send to Azure,
finally making it to a disk.
But if you're really mostly concerned
with the data that you're sending to Azure being encrypted,
then this is one pretty good option.
Now I have a separate video talking about tags,
so we're not gonna be talking about that.
In the next video, we are going to finally
hit the create button
and get this storage account created.
So come back for that.


### 📺 Lesson: Storage Account: Final Creation


Instructor: So this is the moment
that we've been waiting for.
We are on the final tab called Review and create.
As you can see, there are some validation that goes back to
check out all of our settings
to make sure we haven't made any mistakes.
We can review the settings here.
If we want to save this and you run it
as an automation template,
and we do have videos in this course talking about
arm templates, this is where we would do that.
And we'll talk about that in the appropriate video.
So now that it's all past the validation,
I'm just gonna hit the Create button,
And all that we've done has now being turned
into a deployment and is going to be passed
through Azure Resource Manager
and the storage account will be created.
So we're gonna let that run for about a minute.
That didn't take too long,
and our deployment is now complete.
If I open this deployment details,
I can see what goes into creating the storage account.
Remember, I attach the storage account
to a specific virtual network,
and so that's part of the deployment.
And if we look at the storage account itself,
it took about a minute and 20 seconds to create one for me.
Okay, so I'm gonna click this blue
Go to resource button
and that'll load.
We can see that provisioning says Succeeded.
It is a general purpose v2
as we selected locally redundant storage.
Standard, not premium performance in the East US region.
So all of the things that we asked for it,
it's been created.
Now in the videos that follow,
I'm gonna talk about various features.
Now that we have a storage account,
we can look at things like storage explorer.
We can create containers,
we can create blobs inside those containers,
we can access those.
I can talk about how keys work
in terms of getting the access to the contents
and all that fun stuff.
But as of now,
we have a storage account created in Azure.
So let's keep going.


### 📺 Lesson: Storage Accounts: Blobs, Files, Queues and Tables


Instructor: So in our storage account,
we can store four different types of data.
So this, if you recall,
was a general purpose v2 storage account.
And in a GP v2's account,
we can store blob files,
which is stored inside of containers,
file shares, which is more of a traditional mounted storage
that can be shared among multiple servers or computers.
Storage queues and storage tables.
Queues and tables are not on this AZ-104 exam,
so we're not really gonna get into it in any detail.
We're gonna focus, in this video, on containers.
We're also gonna talk about Azure files
in this course as well.
So let's talk about containers.
If I click on the Containers option,
I'm gonna be taken to this containers section.
As you can see, I don't have any containers yet.
So a container is just as the word sounds, it's like a box.
You're going to put all of your files inside this container.
You can have multiple containers.
And so in that way, you can organize your files according
to the type or whatever way you want to organize them.
So let's create a container.
I'm gonna call it first container.
That makes sense, right?
Now, this container is marked as private
and I have no option to mark it as public.
Remember, when we created this account,
we did not enable the option to have public containers.
And this is a security risk
if you leave your containers open,
but there are some reasons to do that.
So I'm gonna click Create.
So it says, successfully created storage container.
Now, container by itself isn't gonna give me anything.
I'm gonna want to put some files in here.
Now, normally you are not going to use the Azure portal
to upload or download files from a storage account.
This is just for demonstration purposes
Usually you're gonna do it programmatically
to put your files in here, typically.
So I'm gonna click this Upload button
and I'm gonna put a file into my container.
So I'm gonna use the drag and drop to put the file there,
and I'm gonna say Upload.
Now, this is a 70-megabyte file,
one of the videos for this course in fact.
Now, remember we set the default access tier to cool.
So it's showing us as the cool tier.
If we wanted to, we could change this to hot or cold tier
simply by changing tier.
We could even change to archive even though
we didn't have the option of setting to default.
Now, if you recall, we did turn on versioning
when we created this account.
So if I was to upload the same file again
and overwrite the file,
then it's going to create a second version of this file.
So if I go into three dots here
and I say View versions,
then we have the current file
and we also have an older version that we can access here.
We can also delete the version
or make it the current version.
Now this file, even though we don't have access to it
from the public internet, I did add my IP address
as an acceptable access point,
so I should be able to access the file.
So what do you think will happen if I just copy the URL
to the file and try to access it?
It is a video, it should download and play.
So I copied the URLI pasted into my browser.
I hit Enter
and I get an error message,
public access not permitted on this storage account.
So this file is not available for access.
Ah, so like I said, it's the locked door on the street.
Even though we have a URL, we don't have access,
but we haven't talked about access keys yet.
And I'll create a lecture about that,
and of course, secure access signature.
But there is a way to access this file with the access keys,
and we'll talk about that in a future video.
All right, so what we have is we have a storage account
with a first container.
We've uploaded a file that's now versioned.
And everything seems to be configured exactly
as we expected.
So in the next video we're gonna talk about access keys
and shared access signature.
So stay tuned for that.


### 📺 Lesson: Storage Accounts: Access Keys and SAS


Narrator: Now we just saw how easy it was
to create a container and upload files into that container.
But when it comes to accessing those files,
we were getting this message, PublicAccessNotPermitted.
We were accessing the storage account by its endpoint,
and my computer has access to this endpoint.
So, how do we go about getting access to this file?
Well, first we have to understand this concept
of access keys.
So if we go back to the storage account,
out of Data storage and into Security,
we can look at Access keys.
When we set up this account,
we said we would use access key authentication
and not Entra ID.
You do have the option of having Entra ID and keys
or having only Entra ID.
So, this keys is a very interesting process.
It is, in fact, a secret that anyone who has the secret
and access to the endpoint using networking
can have full administrative access
to the contents of your storage account.
So, they can add files, they can delete files,
they can read files.
If they have the key, they are in.
I'm gonna show you the key.
This right now, it's obscured,
but if I show it to you, this is our sequence of letters,
numbers, uppercase, lowercase, symbols;
that is impossible to guess or hack.
So, if I had public networking on,
and you had this key, you could access this storage account,
but I don't have public network access on.
Now, this is why it's extremely important
to keep your key a secret.
So, this is very much on a need-to-know basis.
The fewer the people that have access to this, the better.
Now, what happens if this somehow leaks?
Let's imagine you've hard-coded this into some code,
and then you publish the code to GitHub public repository.
That's happened.
And believe me, there are programs
scanning GitHub constantly, looking for the security keys.
So within minutes, if you were to publish code
with this key in it and the endpoint, within minutes,
this account would be hacked.
So, what happens?
Well, first thing you're gonna wanna do
is void the key.
So, that's called rotation, or regeneration.
So, as soon as I click this button saying Rotate key,
this key becomes invalid
and no one would be able to access this account using it.
Say Yes.
Now, do keep in mind
that if you are using this key for other purposes,
like an application, a script, some programmatic purpose,
then everything's invalid.
So, not only the hackers would have been invalid,
but legitimate access would also be invalid.
So how do we avoid that?
Well, Microsoft gives us two keys.
The purpose of the key is to allow you to switch
to the second key before you regenerate the first.
So, the sequence of events would be,
once you realize this key has been hacked,
or you wanna re regenerate it,
you switch all your legitimate programs to the second key,
republish them, ensure it's all working,
and only then you regenerate the first key.
And that way your programs are using the second key.
So this is why there's two keys,
and this is how you rotate them.
There is this ability to have a reminder.
So, let's say you want, every six months, to change the key,
or whatever the policy is that you want,
then that can be done right from here.
So, knowing this key is going to allow me,
programmatically using C# or any of the SDKs,
Python, to access the storage account.
But how are we gonna get access
to that video that I uploaded?
All right, what we're gonna do,
is we're gonna go back to Data storage.
Under Containers,
go into the container.
Now, instead of going, I'll say View first,
and so instead of taking the URL off of the Overview screen,
I'm going to choose Generate SAS.
Now, SAS stands for shared access signature,
and it's a more secure way of granting limited access
to your blob or your container.
Now you'll notice that it's using the key, Key number 1,
as a signing key.
You assign a permission.
So in this case, it's read-only permission
and it has a start date and time, and an end date and time.
Optionally, you could provide an IP address, even here.
And as well, you're gonna choose HTTPS only,
or to allow HTTS access.
So I'm gonna leave all the defaults,
and I'm gonna say Generate SAS token.
Now, there's two components to this. One is just the token.
So this token, you don't need to know this for the exam,
but it's a series of names and values
and you can see that sp=r,
clearly relates to the permissions.
And the st is the start time
And the se is the end time.
So, it's sort of embedded
what you've selected into this thing.
The key part, of course, is it's signed.
So, there's a signature at the end
that the Key 1 has been used
to create this signature hashing, I guess,
of the entire text.
What I'm interested in is this URL, Blob SAS URL.
So, I'm gonna copy that.
Now we go back to the browser,
and we paste the URL that includes the SAS token,
and I hit Enter.
And now a video loads.
So, we have the read access during this period of time,
based on this URL.
There is a downside to this though.
So, I've created this SAS token.
There is no ability to revoke it.
So, there's no name for this. It's not saved anywhere.
As soon as I leave the screen,
this is all gone and forgotten.
The key is signed, the token is valid,
you're going to be given access.
So, let's say you've generated an SAS token,
it accidentally got leaked somewhere it shouldn't have.
How do you revoke it?
Well, you have to regenerate the key.
So, if the key is invalid,
then the token signature is invalid.
So, you go back to the Storage account,
under Security, under keys,
and regenerate the key.
With a regenerated key, this URL should no longer be valid.
If I open up a new browser,
place the SAS token, including the signature,
it says AuthenticationFailed.
It's a different error,
but the signature is being called out.
"Signature did not match."
So, that's the only way you can invalidate an SAS token,
is by invalidating the key.
In the next video,
we're gonna talk about stored access policies,
which will solve this particular problem.


### 📺 Lesson: Storage Accounts: Stored Access Policies


Instructor: We saw in the video
on shared access signature that we assign permissions,
start date, end date,
perhaps IP address and the allowed protocols.
But once we've created this SAS token, we cannot modify it.
We cannot revoke it.
So you create it, you give it to someone,
and you're pretty much stuck
with having this token out there
unless you invalidate the key.
One way around that is using
what's called a stored access policy.
So a stored access policy is a way
to centrally manage SAS token settings.
It is defined at the container level.
So we go up to...
Under containers, we're looking at first container,
and we right-click on the three three dots,
and we look at Access policy.
So this policy does contain permissions,
a start time, and expiry time,
similar to the way that we would
with a shared access signature.
So I'm gonna call this first policy,
and we're gonna give it Read permissions.
And we're going to choose a one week policy
and say, "OK."
So this, I haven't actually granted anybody any permissions.
I've just created the policy called first policy,
and I'll say, "Save."
Now when I go to the file,
I can go to the one that I uploaded
and I can say, "Generate SAS."
And if I choose the first policy from stored access policy,
it's now prevented me from editing the start
and expiry date and time as well as the permissions.
I can then generate the SAS token with this.
Let's say that I've copied it.
Now if I've given this to somebody
and I want to revoke the permissions,
I'm not only able to do so by invalidating the key,
I can also modify the policy.
So if I go back up to the container
and I go look at access policy,
I can either delete the policy or edit it.
And let's say I want to extend the life of this
for a few more weeks.
So now the permissions,
again, have been embedded in the policy.
So whoever has the SAS token can continue to use it
until the new expiry time.
If I wanted to expire it early,
let's say, I wanna expire it 30 minutes ago,
then I can change the expiry time to a much shorter period.
So now I have editable permissions
on the permissions and the time
without having to regenerate the token
or even contact people.
Now this is best used when you have long lived policies.
You wouldn't do this for just a few hours,
but if you had something that is a six month policy,
that's a long time for something to change.
You need to grant additional permissions
or to change the expired time.
The other benefit, of course, is you can reuse this policy.
So you can grant multiple SAS tokens
pointing to the same policy,
and then modify the start date and end date
and the permissions all at once.
So this is a much more flexible
and useful way of managing SAS tokens if you're gonna use it
to give access to your containers and or your files.


### 📺 Lesson: Storage Accounts: Entra ID (Azure AD) Access Control


Instructor: So let's go back to talking about security.
Up till now, we've been working with access keys,
which means that if you have the key,
then you pretty much have full access to the contents
of a storage account,
depending on the network settings, of course.
The other type of access is called Entra ID,
which is identity-based access control.
This shifts the authentication from what you have in terms
of the secret key into who you are.
And once you've authenticated with Azure,
then you would be given the appropriate permissions,
which may or may not include access to the storage account
or to the container or to a file share.
So this is also called role-based access control
within Azure.
So for general-purpose v2 storage accounts,
this is available by default.
You don't have to do anything in order
to enable access control.
What you may wanna do is disable the account key.
So if we go down into this overview screen,
we can see under security,
it has storage account key access enabled.
If I click this, it takes me into the configuration
and I can go down to allow storage account key access.
If I set this to disabled,
well, suddenly all of the keys no longer work.
All of the SAS tokens
and the shared access policies no longer work.
So I'm gonna do that.
And Entra ID has, again, for general-purpose v2,
I don't have to do anything to enable it.
Now, there is the concept of defaulting to this.
So there are ways of accessing your storage account
in the portal, including a storage browser
and when you use the portal to navigate into a container
and into the files, do we switch over to Entra authorization
for the portal?
Actually, I have to enable this
'cause I've disabled the storage account key,
so I'm going to save that.
Okay, I'm gonna go back to the overview screen here.
So there's a couple of different levels
in which you can assign authentication using Entra ID.
First is at the account level,
and right from this overview screen,
we see the menu says access control.
We can click onto that,
and let's look at the roles.
So if we go under access control in roles,
we can scroll down and we can see
that there's a number of roles and what we're looking for,
I'm gonna actually search instead of scrolling,
we're looking for the word storage, let's say to start with.
And we're looking for, for instance,
Storage Blob Data Contributor.
Allows for read, write, delete access
to Azure Storage Blob containers and data.
So if you assign this access to someone,
then they're going to be able to add files and read files
and delete files inside
of a blob container in this storage account.
So azsjdnewstoragedemo.
Assign someone this permission,
they will have access to that container,
all the containers in the storage account.
You can also go down to this individual container.
And under properties,
there is this access control on the left.
And again, we can go to the storage account,
Storage Account Contributor role
as an example,
and then they would only have access to this container.
So those are, in terms of blob storage,
the two levels of access that you have the ability
to assign people.
Of course, that's not the only role
that may have access to this.
There are other roles,
like Reader and Data Access lets you view everything,
but not lets you delete
or create a storage account or any of the resources.
It gives you access to all data.
So this isn't the only role that you can assign,
but some of these roles
are gonna have storage account access built into it.
So even though I created this account
and I created this container, if I go to the overview,
it's gonna tell me I do not have permissions to this
because I've turned off key permission.
I've turned on the default for Entra ID permissions,
and I have not assigned myself permissions to this.
So if I go under access control for the container,
and then I can add a role assignment,
I can choose the Storage Blob Data Contributor role
as an example.
I can choose myself
and I say review and assign,
and say review and assign.
Now when I go under view my access,
I can see that I'm not only administrator
in this management group,
but I'm a Blob Data Contributor for this resource.
Now, this could take a few seconds to propagate,
but eventually when you go back to the overview screen,
you'll see that you do have access to list the contents
and even to view the contents of this.0
you'll see the authentication method
has been set to Microsoft Entra.
So as we've seen,
using the access key is definitely the easier way
of getting access to a storage account.
It used to be historically the way that it was done,
but there is some pitfalls.
If you lose this access key that allows other people
to have full control over your storage account,
you do not have really good ways
of controlling the access key.
You can use the shared access signature
or stored access policies, but that is not perfect.
Changing the key can be a little bit of a hassle sometimes.
So moving to a Microsoft Entra for authentication
and control of your storage account, while more difficult
to implement initially, does give you finer grain control
and maybe better long-term control over the contents
of your storage accounts and your containers.
So this is the lesson on Microsoft Entra.


### 📺 Lesson: HANDS-ON LABS: Storage


[No transcript available for this lecture]


### 📺 Lesson: Udemy Lab: Azure Storage, Create a Container and Upload a File


[No transcript available for this lecture]


### 📺 Lesson: Storage Account: Lifecycle Management


Instructor: So let's talk about
a few of the cool other features
that storage accounts support
for blobs and other file types.
Let's talk about lifecycle management.
If we go on the Azure portal
on the storage account under Data management,
we'll see an option called Lifecycle management.
Now, lifecycle management,
and I think I've mentioned this before in this course,
is the ability to move data
from a more expensive pricing tier
down to cheaper tiers as the files get older effectively.
So for log files and backup files,
things that have less value to you as they get older,
but you might still want to keep, you can move them
to cooler or colder levels of storage
and save significant amounts of money.
So this, let's look at this.
I'm going to click on Add a rule.
Give the rule a name.
I'm going to call this the Saving Money Rule.
And I have the option of applying the rule
to all blobs in the entire storage account,
or to set some type of filter so that only blobs
in a certain container get applied.
I also get to choose which type of blobs get picked up.
Now, one of the interesting parts
is whether I want this to operate on
the blobs themselves, snapshots,
which we'll talk about in the section coming
in terms of Azure files and points in time recovery
for Azure files or versions of files.
So imagine you've turned on versioning
and over six months, nine months, some of the older versions
become less and less important to you.
You can actually just save money
by storing the older versions in cooler
or colder storage that you need in case of emergency,
but you're not likely to access frequently.
So I'm going to do this based on base blobs
just for this example.
Now what we're setting up here is a rule
that says if the blob was last modified
more than so many days ago, let's say more than 30 days ago,
then what do we want to happen to it?
Now we can just delete it.
So if it's a daily log file,
then maybe you don't need to keep more than 30 days
of daily log files.
And so on the 31st day,
this lifecycle management rule will delete the file,
and that's perfectly fine too.
Or maybe you just want to move it from hot storage
to cool storage,
or even as far as going to cold storage,
if you really don't think you're going to need this file
after 30 days.
Now notice some of the comments here.
I haven't mentioned it before in this course,
but as you get into cool, cold and archive,
there is some minimum charges
that come into play.
So when you move a file into cool storage,
you're going to be charged a minimum of 30 days
at that rate.
So you can't just move a file into cool storage for 24 hours
and then delete the file
and expect to save money just for that one day.
You've got a minimum terms of the charge.
You can still delete the file,
but you'll be charged for the full 30 days.
Cold storage is for 90 days,
and archive storage is going to minimum charge you 180 days
at that lowest rate.
But remember, archive storage can be 5%
of the cost of hot storage.
So you're saving a significant amount of money,
and even if you store it just for a month,
you're still saving money at that level.
So as we can see, lifecycle management is where you go.
If you see this on the exam
and it's asking about setting up a job
to automatically move blobs to save money,
then you should be thinking about lifecycle management
as being the easiest way to do that.


### 📺 Lesson: Storage Account: Object Replication


Instructor: Now the AZ-104 exam requirements
mentions the topic of object replication.
If we go into the storage account, under Data Management,
you'll find an Object Replication menu item,
and we go into there.
So object replication allows you to have asynchronous copies
of a source storage account to a destination account.
So you can imagine a scenario
where you have storage accounts
that are specific to a region
or specific to a particular location of your business,
and you wanna have a roll up
where all the data from all of these storage accounts
get stored into one central account.
And so you can do this using object replication.
As it says, you can use,
if the storage account has been created
with cross-tenant enabled,
which is an action that you have to take to allow it,
then you can use the storage accounts across subscriptions,
or even the storage accounts may be in different regions.
So if you have storage accounts from all over the world
coming to a particular region for the roll up action.
So we have two tabs here, Your Accounts and Other Accounts.
Let's just take a look at this concept of replication rules.
It should be pretty straightforward.
So we have a source, a storage account,
and a destination storage account.
So it's asking for a destination.
I'm gonna choose one of these other storage accounts
as the destination.
Then we can choose the source,
which could be the first container that we've created,
and we can choose the destination,
which could be one of these containers.
And as it says, copy over only new objects.
We can obviously modify this such that it copies everything
or that we put some custom rules on what gets copied,
date, time, et cetera.
So if we were to create this rule,
then any new files created on this storage account,
azsjdnewstoragedemo, in this container
will get copied to that other storage account
in that other container.
So that's a pretty straightforward way
to do object replication
using tools provided by Microsoft Azure.


### 📺 Lesson: Copy Files with AzCopy


Scott: Now, we already know that if you want
to upload a file into a storage account,
you can use the portal through the browser.
You could upload a file into the storage account manually
at this user interface,
but this is definitely not the most efficient way
to do this.
Now, what if you have two storage accounts,
and you wanna move a file or copy a file
from one storage account to the other?
It doesn't seem very efficient as well
to then download the file to your local machine,
go over to this other storage account,
and upload the file there.
We need some kind of tool that allows us to copy files
into and out of a storage account
or between storage accounts
in the most efficient manner possible.
That tool is called AzCopy,
so you can go into your favorite search engine
and search for AzCopy.
Now, this tool hasn't changed in many years.
AzCopy V10 is still the latest version.
If you want to download it,
it comes across many different operating system.
so we got Windows and Linux and Mac.
It also has RPM and other types of Linux installers
that it supports, APT.
So I'm gonna start PowerShell here,
and we're going to CD into the directory.
I downloaded Windows 64-bit version
and extracted the zip file,
and I have AzCopy running here as a standalone program.
Now, there's a couple of ways that we can use it.
We can obviously log into Entra using AzCopy
and have permissions that are granted by RBAC,
or one way that I like to use it is through an SAS token.
So let's say I want to go back to my containers,
I want to go to this destination folder,
but I want to generate the SAS for this destination folder.
I'm gonna use the storage account key.
I want to be able to write files using this,
let's give it full permissions.
For a limited time, it looks like it's about six hours,
and HTTPS, and I wanna say generate SAS token,
and I'm gonna copy the whole URL,
including the storage account and the folder name.
So I can say AzCopy, the command is copy.
I have to choose the source file for this,
and then the destination,
which I just created the SAS token.
All right, so I picked a random MP4 file off of my computer,
and I'm gonna be uploading it into the destination container
of this storage account.
Again, we're using the SAS token that I generated
so I would have permissions to write.
Now it is running, and I can see transfers completed,
the number of bytes transferred, et cetera.
If I go back into the destination,
I can see the file I just uploaded is there already.
So AzCopy allows us to manipulate files, again,
between storage accounts
or from your local to storage account, copy blobs,
synchronize blobs, et cetera, using a command line,
which is a lot more efficient
than doing everything through the browser.


### 📺 Lesson: Storage Browser


Instructor: So you may have seen this Storage browser
on the left side of the storage account.
Now, it does bear some similarity
to the way that we look at containers or file shares
from the container or file share section of this.
We can see that we go into Storage browser,
we can go into Blob containers,
and here we have our first container that we created.
We can create a new container.
So it's very similar to the other interface.
One of the differences here
is that we can actually perform some file operations,
like copy and paste.
So if I wanted to copy this file into a new container,
then I could copy it here,
move to the other container, and paste it in there.
So there are some additional functions
in the storage browser.
We still have the three dots,
and we can still do things such as SAS.
And here's another clone.
So if we wanted to make a duplicate of this file,
there's a clone option within the three dots.
If I go down to the File shares, very similar,
we'll see the file share that we created.
We'll see the directory, and we'll see the files.
I can, again, copy and paste files
from within storage browser.
One of the new features in the storage browser
that doesn't exist in the file share section
of the storage account is the SAS option.
So there's three dots next to the file.
I'm gonna choose this one with the txt, say Generate SAS,
and then I can, in this case, use the key.
So one of the things, of course,
is the key has been disabled for this account.
We no longer use key, so we can't do SAS for the file share
because I've disabled it for this account.
But if we did have it, that would be where you could do it.
Now, Microsoft does have a downloadable app
called Azure Storage Explorer,
which you could do something very similar from your desktop.
It's a free download for Windows, Mac, and Linux,
and you can do these file-based manipulations
in a software application on your desktop.
So now, of course, if we're doing file shares,
you can just use the normal Windows or Linux connection
to that share just as you would a local drive.
But if you need an app to do it, you can download an app.
So anyways, that is a storage browser.
It does allow you a different view of your storage account,
including containers, file shares, queues, and tables,
and a couple of additional features
not available in the other view.


### 📺 Lesson: Create Azure file share


Instructor: So we've been talking about blob storage
up until now,
but storage accounts can contain other types of data.
The one that is relevant to this exam is called file shares.
So I'm gonna click on file shares under data storage.
Now, file shares is more similar
to what could be called a file server
within your internal network.
This could be a common server
that many other computers connect to
to store files that each other can access.
You may have an S drive or a T drive
or some other letter at your computer at work
that is common to everyone.
You may even have your own private directory
on that common server.
So this is great for what is called
a lift and shift scenario,
where you have a file server
internal to your company network
and you wanna migrate that into a storage account
in the cloud.
Now, file shares use two different types of protocols.
One is called SMB, which is the server message block,
and the other is called NFS.
So you can mount your file share
to your Windows servers, Mac servers,
or Linux clients.
NFS is for Linux-based workloads.
This also has capability of synchronizing.
So if you have an existing file server
and you want to have a copy of those files in the cloud,
there's a tool called Azure File Sync
that can keep the files synchronized
between your on-premises server and Azure files.
So I'm into the file share section of the storage account.
Let's create the first file share.
So I'm gonna click the plus sign
and I have to give it a name.
So first share.
Now we'll see very similar to the blob storage
we do have access tiers.
There is a premium tier,
but it's only available to be chosen
for a premium file storage account.
So if we had chosen premium for the the storage account,
we could choose premium access tier.
We have three other options that is transaction optimized,
hot and cool.
Transaction optimized is your general purpose
low transaction cost pricing
for transaction heavy workloads.
So it's not low latency,
but this is sort of a good starting level.
The hot tier, just like with blobs,
has a balance between storage and transaction pricing.
So it's relatively cheap for storage
and also relatively cheap for transaction.
Not trying to optimize for either.
We also have the cool level,
which is the cheapest for storage,
but will obviously cost you a bit more for access.
The same as the blob storage.
So I'm just gonna choose the default,
which is transaction optimized.
Now we can see that we're being told
the performance of this selection.
So we've got 20,000 operations per second,
and in this particular file share,
100 terabytes is the maximum capacity.
Now, there is a backup tab here,
and we can use a backup vault
for storing the content.
So just like you would back up a server,
like a virtual machine
or non premises server, you can store these files
that are stored in your Azure file share
into a backup vault.
You'll see that there are a backup policy.
So every day at 7:30 UTC
it's going to keep that for 30 days.
And that's enabled by default,
but you can obviously disable that
if you don't want these files backed up.
So I'm going to create this.
Create.
Alright, so we successfully created our first file share.
As you can see, there's a URL for it,
the storage account name .file.core.windows.net,
and the name of the file share.
We can even create some type of directory structure in here.
Now, conveniently, there's this connect button
that will help us to build that connection.
So we've got Windows, Linux, and macOS options
In terms of connecting to this
using the SMB protocol.
You'll see various notes on here on the connect screen.
First of all, we have the choice of drive letter.
So if we want this to be our S, T, U drive letter,
we can choose one of those options.
By default, it's gonna use the storage account key
as the authentication method.
This is only recommended for admin access.
You do not want to be sharing your storage account key
across your company to dozens of people.
And so you probably would be better off
to use a active directory type authentication.
There's not a script unfortunately for this,
so we'll leave as storage account key.
So if I click show script,
it'll actually give me a PowerShell script that I could use
to connect to this drive from my local machine.
Now there are some other caveats here
that this connects over port 445
which is often blocked from private home ISPs
generally over the internet
or maybe even your own organization,
doesn't allow file shares to pass through
your own corporate firewall.
So you may require a VPN, a point-to-site VPN
a site-to-site VPN or express route
in order to get into Azure
in order to use this type of connectivity.
Now, if you're VMs are already running an Azure,
this would not be an issue.
You could take this script
and you can use your virtual machines
to connect to this file share in this way.
So we can see how an Azure file share is different
than a container or blob storage.
It has different capacities.
It has the concept of directories.
It can be mounted as a drive letter on a Windows machine
or mounted to Linux or macOS in the way
that external disks are,
and definitely is something that's worth looking into
if you want your files to live in the cloud,
be backed up regularly,
but treated as if it was a file server
running in your local machine.
In the following videos, we're gonna be talking about
some of the other features of file shares in Azure.


### 📺 Lesson: Azure File Shares Snapshots


Instructor: So I just want to create some files
on this account, and I've given myself
Storage File Data Privileged Contributor
as well as SMB Share Contributor access.
And you go to the overview screen, say add directory,
and you can add a directory from here.
When I go to the browse section, I can see
that I've been able to create directories,
and obviously, I can upload files from here.
So I have chosen 16 sample files
from my local machine to upload.
Now, the purpose of this video
is really to show you about the concept of snapshots.
Now, snapshots are point-in-time, read-only versions
of your Azure file share.
This allows you to recover deleted or modified files.
And it's not a separate storage account,
it's actually gonna be your same storage account
that's going to store the snapshots as well.
So the snapshot is created manually,
or you can script it
so that you can run it at your own schedule.
These are stored as incremental backups,
so only when there's changes to those files,
then the snapshot gets updated.
The data can be retained for as long as you need.
And again, this is not a separate storage account;
it's all contained within the same snapshot here.
And once you have a snapshot,
then what you can do is restore
from a specific point in time.
So you can browse the snapshot contents,
copy files back to the active file share.
And there is such a thing
as a previous versions tab supported in operating systems
such as Windows.
So again, this is only for general-purpose v2 accounts
or for premium file shares.
So let's create a snapshot.
I'm in the snapshots operation under the file share,
and I'm gonna say add snapshot.
And I'm gonna say this is going to be previousversions.
And so now that we've created a snapshot,
we can actually go into the snapshot.
We can see the storage account file share
as it existed at the time the snapshot was created.
And if I wanted to restore this version of this file,
I can click this restore and it becomes the recent version.
So if this file has changed, has been deleted,
it's been updated since then,
I just navigate into the snapshot and I can then restore it
or download the specific version.
Now, I should point out that another way to get snapshots
is through backups.
So we'll see under operations it says backup.
Now, Azure Backup backs up its data
to a Recovery Services vault,
and I can even navigate into the Recovery Services vault.
Go under backup.
I can see backup items, Azure Storage,
Azure Files, one item.
But it's not a regular backup.
It's actually backing up as a snapshot.
So you'll see it even says Snapshot
within the Recovery Services vault.
If I go into the file share under Snapshots,
I can see the snapshot that I created manually,
as well as one that automatically kicked off
to do AzureBackup.
Now, the advantage of the automated backup
is that there's a policy,
and so the policy can say
that every day at 7:30 UTC in this example,
it's going to make a backup of anything
that's changed in the file share,
and it's gonna retain those backups for 30 days.
So I have a backup policy to automatically create snapshots
so that I can do the point-in-time recovery,
not only the ones when I can manually create a snapshot,
but I can also have it scheduled through backup.
So definitely a convenient way to keep copies
of your file share over time.

