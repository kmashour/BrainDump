---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "11"
title: "Module 11: Administer Data Protection, Backup and Site Recovery"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 11: Administer Data Protection, Backup and Site Recovery

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** Azure Backup, Recovery Services Vault, Manual & Scheduled VM Backups, File-Level Recovery, Full VM Restore, On-Premises Backup, Soft Delete, Azure Site Recovery (ASR) Replication & Test Failovers  
**Line Range:** Lines 18184 – 19661 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


### 📺 Lesson: Azure Backup


So in this section of the course,
we're gonna be talking about backup and recovery.
Now, I have an Azure VM that I created recently.
As you can see on screen,
it's just a standard Windows VM running in West US 2.
Now, when I created the machine,
I did have the option of enabling a backup.
It's in the underlying settings of the creation screen,
but I chose not to do that at the time.
So right now, I have this machine running
with no backup protection.
Now, if I was intending to use a machine for production
or any critical purpose,
operating without regular backups is obviously a bad idea.
Fortunately, it's pretty easy to set up.
I'm here in the virtual machine blade of the Azure portal.
And on the left side, I'm gonna scroll down
to the Backup and disaster recovery,
and you'll see that there's a number of options.
We're going to select Backup.
Well, I am gonna talk about disaster recovery
a couple of videos from now.
But first, we're gonna talk about backup.
All right, so if I click on this Backup,
you'll see that I do have the option
of enabling and creating a backup right within the portal.
Now it's telling me about something called
a Recovery Services Vault,
and it's offering me to create a new one.
And you'll notice that it's selected
the Enhanced backup as the default,
which allows multiple backups per day
up to 30 days of retention.
It supports this Trusted VM; this is what this is.
It also supports Ultra and Premium SSD disks.
Okay?
So Standard does not have those types of support
and talks about a policy.
So this policy that it's offering me to create
is what's gonna dictate how often this gets backed up.
So you'll see that it's offering me a backup policy
where for every four hours it's going to run,
starting at 8:00 AM, noon, 4:00 PM, 8:00 PM, et cetera.
Okay?
And it's going to retain seven days of instant recovery.
So I'm gonna be able to pull out
to a specific point in time for up to seven days,
and it's hard-coded here
for 30 days of retention for the daily backup.
Now, if I had chosen a weekly backup or a monthly backup,
I could set those as separate retentions.
Now, if I just said, "Okay," and set "Enable backup,"
then we would set up this backup in an automated fashion.
But in this video, I want to talk about manual backups.
So I'm gonna X out of here and go to the dashboard,
into my resource.
I'll go to the dashboard,
and the first thing I'm gonna do
is I'm gonna create the Recovery Services Vault myself.
So I'm gonna search for "recovery."
And Backup and Site Recovery is the offer.
And so we're gonna create a Recovery Services Vault.
Now, Recovery Services Vault is just a storage account
that has certain rules applied to it
because it's specifically for backups.
I'm gonna put this into my VM Resource Group,
and I'm gonna call this "my new Recovery Services Vault."
And for convenience, I'm gonna keep it
in the same region as the VM.
Although if we're gonna do this in the recovery aspect,
you'd want this to be in a separate region,
but for backups, let's keep it in the same region.
How often... we want this to be redundant?
Well, it's going to be in this demo Locally Redundant.
So as you know, under storage, it keeps copies locally
versus Zone Redundant or Geo Redundant,
and you're gonna pay more for that.
Next up, encryption.
I'll just leave it as a Microsoft-managed key.
Now, if I wanted this backup
to never be changed or deleted,
then that would be immutability.
I'm not going to touch that.
I'm not going to change the networking.
And we're just gonna say "Review and create."
So this will go off and create a storage account
for my backups, and we'll let that run.
All right.
The Recovery Services Vault seems to have created,
so right now this is an empty Recovery Services Vault,
and it's not tied to any specific virtual machine
or any specific data job.
So what I want to do at this point
is I can set up the backup job
from within the Recovery Services Vault.
So I go under Backup.
What is your workload?
Well, my workload is running in Azure.
We're gonna talk about on-premises backups in a second,
but we're talking about Azure backups.
And I want to back up a virtual machine.
You can see that I can back up a file share,
SQL database, and the SAP workloads.
But in this case, we're backing up a virtual machine,
and I'll say "Backup."
And now I'm being given a very similar setup
to what we could have been creating
either at the time we created the virtual machine
or in the backup blade of the VM.
I have the choice between Enhanced and Standard.
I'm gonna choose Enhanced
because this is a Trusted Launch VM,
and if I try to choose Standard, it might not work.
And as you can see, we have the backup policy,
and it's the one we saw earlier,
which is an hourly backup starting at 8:00 AM
every four hours,
and it keeps 30 days for retention for the backup,
as well as instant recovery for seven days.
And I'll say, "Okay."
It puts in text here exactly what we saw.
And now I can add
which virtual machine I want to add this policy to.
This is the machine that I was just looking at.
So as you can see, you can sort of manage,
if you have a single backup policy
or maybe production policy and a development policy,
you can come into your Recovery Services Vault
and pick which VMs are covered by which policy through this.
So now I can say "Enable backup," and I'm gonna click it.
So now it's setting up the policy,
and it's going to schedule this backup.
Now, it doesn't do the backup right away,
but we'll see that in a second when it's complete.
All right, so the backup policy has been deployed,
and if I go into the Recovery Services Vault
and I choose the Backup tab, we're gonna see none.
None of the backups have run yet,
but we do have one item under Backup Items,
and we can also see it here under Protected Items.
One virtual machine.
When I go into it, the backup pre-checks has passed,
but we have not yet run the initial backups.
So this is scheduled for, if you recall, every four hours.
So at 8:00 PM today will be the next time
that the backup is scheduled to run.
So in this video, we saw that there's at least
two or three different ways we can schedule a backup,
and we have a backup scheduled for our virtual machine
in a brand new Recovery Services Vault.


### 📺 Lesson: Running a Manual Backup


All right, so we've seen that
we've got our virtual machine scheduled to be backed up.
And again, it probably runs it at 8:00 PM
will be the next time that this runs.
I can go into the backed up items and see the details.
And this is just gonna give me
an overview that the pre-check has passed,
but it hasn't run the initial backup.
And I could see if there were restore points
when the last time it ran, if I wanna recover to that.
So what we can do is called a on-demand
or ad hoc or manual backup.
We can say backup now,
right from within this details of the backup item.
And I can define how long I want this backup to be retained.
So that's a manual.
Let's say I want to do it for just a week.
And now it's gonna go
and trigger the backup instead of waiting for it.
So anytime you know,
let's say you are about to make a change to the server,
and you're like, well, let's make a backup
just before we make this major change.
That'll make it easier to recover,
then you can go and manually trigger a backup
with this method.
Now, once you've kicked off the backup,
this can take some time.
So it's not gonna take five minutes, 10 minutes, 15 minutes,
it's gonna take some time to get the backup going.
Even a small VM could take 20 minutes to an hour,
depending on the size.
So I actually don't have to sit here
and just stare at the screen waiting for it to complete.
There is such a thing as a job and a monitor.
So if I go back to the recovery services of vault itself
and I can go under Monitoring,
I can see there's a item called Backup Jobs.
And so I can see my initial configuration
took place at this date and time,
and now the triggering of the backup,
which we did manually, has kicked off here.
So this is a way of checking out on jobs
that are in progress.
Of course, I can say View Details
and we can see, you know, the tasks that it's doing,
how long it's taking, et cetera.
Now the taking of the snapshot is usually pretty quick.
Transferring that data to the vault
is what usually takes some time.
So we can wait for that.
Now, another thing we can do while we're waiting,
the virtual machine is still running
and hopefully this backup is not
so disruptive to the virtual machine.
I mean, obviously it can be,
but we can take a look at the VM
and to see how it's going, right?
So we're seeing CPU utilization, VM availability.
Well, availability is positive.
CPU utilization is running around 47%.
We got some, obviously some bytes that are happening.
So there is some activity on the server itself,
as you would expect during a backup.
We see it took around eight minutes for the backup
to be done, but another eight minutes at least
for the data to be transferred to the vault.
And as expected, it took about half an hour, 27 minutes,
to do the backup and transfer the data to the vault.
And so that's how you do a manual on-demand backup.


### 📺 Lesson: File Recovery from a VM Backup


So let's assume that you've got
a virtual machine and you've got a backup running
and it's doing its every-four-hours backup,
but at some point you want to recover a file.
You don't need to restore the entire VM.
You just want one important file.
How do we handle file recovery?
If we were having to restore the entire server
just to get back to that one file,
that's a bit of overkill, excessive, and time-consuming,
so what we're gonna do is do something called file recovery.
I'm in the virtual machine here
and I'm gonna go under Backup, which is where
the backup exists, and you'll see
that my last backup status is successful
and I do have an applications
consistent backup in the recovery points.
Up at the top it says File Recovery and I'm gonna click it.
So before I do that, I have to pick from which backup
I want to recover that file.
So I only have the one because we just did a manual backup,
and so I'm gonna click this one initial backup.
Now, you'll notice something strange.
It is basically, it is not giving us a list of files
and asking us to pick which file.
It's giving us an executable at which we can download.
Now this executable mounts the discs
from the selected recovery point
as a local drive on a machine and then these drives
remain mounted for 12 hours.
So if I wanna get access to the backup,
I have to basically download executable and execute it,
and that will mount that backup
as a local drive that I can then access,
and it requires a password to get access to.
When I'm done with it, I can unmount the disk
and close the connection.
So I'm gonna click Download Executable.
It says, "Generating script and password,"
and, "You require the password to run the script."
All right, I've got the file and the password.
So I downloaded the executable, I copied the password,
I ran an administrator window on my local machine here,
executed the program, and it kicked off a PowerShell script,
and we can read here that it has connected
to an iSCSI over the internet and has restored my volumes
to the D drive on my local.
And so this is the operating system disc
for the virtual machine that we just backed up.
Now, I don't have any, I guess
I didn't use the computer, so I don't have anything
I can really dig into, but this is the computer
that we backed up, and if there was files here
that I needed to access, I could.
Of course, it's telling me when I'm done with it
that I can just click Unmount and then it will
no longer grant access to this as a backup.


### 📺 Lesson: Restore a Full VM


So let's imagine the worst happens
and our something's gone wrong with our VM,
we've been infected with a virus,
or we did some changes to it,
and we want to roll back,
or some kind of critical error.
This is when we might want to use the Restore VM option.
Now, this function isn't just about disasters.
It's also a great way to do a copy of a VM.
So you can do a backup and a restore,
and that'll get you a second VM identical to the first.
So if you want to test something
and you take a backup of the production server
and you restore it to development,
and then you can certainly do your tests,
and then you've got a brand new virtual machine
to do your tests against.
So I'm gonna go to my recovery services vault
into my backed up items,
and we're gonna drill down into the backed up item
and say View details.
And just like we saw with the File Recovery here,
we have the Restore VM option.
So I'm gonna click Restore VM.
Now, just like with recovering the file,
we have to choose a restore point.
And I'm gonna pick this successful restore point.
And you'll notice that we have two main options
for the restoration.
One is to create a new VM,
and the other is to replace the existing VM.
So for this demo, I'm just gonna create a new VM.
This is going to be like having a second VM,
which is a copy of the first.
So I put Create new.
So I have to give it a name.
So I'm gonna call this a "vmcopy",
call it whatever you want.
And I'm gonna keep it in the same resource group
and the same subscription as the existing one.
Now, you can change that,
you can change the different region and things like that,
but let's keep it the same.
And I'm even going to keep it
onto the same virtual network,
and we'll just have a second VM running on the same VNet.
Now, in terms of the staging location,
we need a storage account
where the backup is gonna be restored into a temporary spot.
Now, you'll notice I don't have a storage account,
I'm going to have to stop and create that.
So I opened a new tab on my browser
and I've gone over to create a storage account,
same region as the restore, the Recovery Services vault,
and I'm making it locally redundant,
and I'm gonna leave all of the defaults here.
Public network access is all fine.
Now, I don't think I need to have
all the soft delete stuff for the...
It's just a temporary storage account that I'll delete
Encryption, tags.
And I'm gonna create.
Obviously, if you have access to a storage account
that you can use for temporary purposes,
you don't need to do this step of course.
So I'm gonna go back and start over
because there's no refresh button.
I'm gonna pick my backup, the original one,
create new, vmcopy,
same resource group, same virtual network.
And this time, I'm gonna put it
into this storage account that I created.
So now I can click the Restore button,
and this is gonna kick off a job.
And this job is going to copy data from the vault
to that staging location.
It's gonna create new managed discs
and a new virtual machine resource,
and then it will attach the discs and boot up.
And so we're getting this restore going,
and in a few minutes,
we're going to have a virtual machine,
which is a backup restored copy
of that backup we did a few hours ago.
Now, I can monitor this just like I can with a backup job.
If I go into the recovery services vault
and I go under Backup Jobs,
you can see that I have a restore in progress,
and it's even given me a percentage complete,
so we can wait for that restore to run.
And if we scroll a little bit,
we can see that there's the two tasks transferring the data
and creating a restored virtual machine.
So we can see that it took about two minutes
for the restore to say completed
and the job progress to say 100%.
So if I go back to my dashboard into my resource group,
then I should have a VM copy, and do,
which is a running virtual machine,
which is a copy of the backup that we did.
Now, from there, I can log into this machine,
I can connect into it, I can test my test
if I needed to do some sort of test
that I didn't wanna affect production,
I can recover data.
And then when I'm done, I can delete the VM,
or I can change my domain name registration
to point to this instead of the other one,
or whatever I need to do once I have this VM running.
So performing a VM restore, a full VM restore,
is a powerful option for both disaster recovery
and also for testing.


### 📺 Lesson: On-Premises Backup


-: Now I briefly mentioned that the backup service
does not only deal in Azure workloads.
So if we go into the recovery services vault
under getting started backup
we saw the selection includes Azure Stack,
which is an On Premises cloud and Azure Stack Hub,
as well as On Premises itself.
And so choosing On Premises gives us these eight options.
Now files and folders, again, very selective backup.
It can run as an application
on the server that's being backed up.
A couple of different virtual machine options
the Windows Hyper-V, as well as the VMware product
which Azure integrates into very well.
It's a partner.
You can do a On Premises SQL Server backup.
You can do a SharePoint server, an exchange server.
You can back up the system state,
or you can do what is called Bare Metal,
which takes the entire server right
down to the operating system to back that up.
And so you have a number of options.
Each of these options has slightly different instructions.
So if I say files and folders,
and I say prepare infrastructure,
then I'm taken to their recommendation
which is the Recovery Services agent.
Now, the Recovery Services agent is a download
for Windows Server,
or Windows client where you can download this application
install it onto your machine.
You'll need to get credentials
so that your machine can register
to the Recovery Services vault.
The credentials expire after 10 days
in order to set this up.
And then you schedule the backup and you can basically, just
as we did with the VMs, monitor the backup on the jobs page.
We can even receive notifications when backups don't work
in terms of notifications, alerts.
So we can see here files and folders are dealt with one way.
If I don't do that
and I instead choose the Hyper V virtual machine
then we're not given the agent, we're given a backup server.
So this needs to be a machine that doesn't have to
be dedicated to it, but you have to have a machine other
than the the machine being backed up, of course.
And that's called MABS, or Microsoft Azure Backup Server.
This also requires the credentials.
And then you're going to use the MABS UI to
configure the backup to which virtual machines in HyperV
you're going to be backing up.
We can see a VMware also uses MABS.
You do need to...
I guess you have the option of using system center
for some of these backups.
Now, different again, different agents are
gonna require different sets of instructions.
You can see SQL Server.
If we go down
to the Bare Metal option this is also MABS.
Again, this is an external server that runs outside
of the machine that's being backed up.
And so this MABS has replaced a couple
of different backup products that previously existed.
And so you can then configure all of your backups in here.
We also notice how the option of having
more than one thing selected at a time.
And I guess MABS is the default option when
you've got to do lots of different types of backups.
So as you can see On Premises does work
keep in mind for the files and folders one
you could even run this on
a AWS EC2 instance or Google Cloud server.
Anywhere where you can install this agent
on a Windows server, you can actually get a backup
into the Azure Recovery Services vault.


### 📺 Lesson: Backup Reports


So over the years,
Microsoft has standardized diagnostics across Azure,
whether it's virtual machines,
storage accounts,
or in our case, recovery services vaults.
We can track operations and metrics
by sending them to a log analytics workspace.
Once the data is in log analytics,
we can analyze it using Azure Monitor,
or specialized workbooks,
often called backup reports.
But to get these reports,
we first have to turn on the data flow.
So I'm in my recovery services vault,
and I'm gonna scroll down
under the Manage section.
And there's a blade called Backup Reports.
Now, historically, this has been the job
of something like Power BI,
but again, this has all been centralized in log analytics.
Now, you'll see here that there is no data
because we haven't turned on diagnostics.
So we have to go under Monitoring,
under Diagnostic settings.
And I don't have any diagnostics configured,
but you can see all of the data
that we can pull out of this diagnostics.
So I'm gonna click Add diagnostic setting.
I have to give it a name.
And so I'm gonna call this backuplogs.
Now, if we look at the categories,
we have lots of them,
and we have Azure backup-related logs
and Azure site recovery-related logs.
Now, if I try to select everything,
all the logs,
and send it to the workspace,
Azure might complain
because that's just a lot of data
and there's some schema
that is overlapping and things like that.
So let's be very specific
in terms of what data we want to store.
So since we're focusing on backup right now,
let's choose the core Azure backup category,
as well as the backup job data
and backup alerts.
All right, so that's going to give us a core set.
And I'll make sure that none of the site recovery stuff
is in there right now.
So I'm gonna send this to a log analytics workspace.
And I already have a subscription
and a workspace.
As you can see in the warning,
it wants us to do separate workspaces
for our separate diagnostics for Azure backup
and Azure site recovery events
so that there's no overlap.
All right, so we're just going to store these things.
Now, if you want to,
you can store this in a storage account additionally,
or instead of,
that's totally up to you.
Now, I'm also going to collect metrics.
I'll go to the bottom and say AllMetrics.
And now I can click Save.
So now that we have set up some settings for diagnostics,
the next time we do a backup,
those diagnostics data is gonna be stored
in our log analytics workspace.
It's not gonna be able to go back, obviously,
to the one that we previously did,
but it's gonna be able to grab data from every backup
that happens every four hours,
as we currently have set up.
So in order to test this,
I could certainly go to the backup again,
to the virtual machine.
View details.
And say Backup now.
So we can do a second manual backup.
Again, that's gonna take another half an hour.
But that's gonna generate the data
that's gonna go into our reports.
So this usually takes a little while,
and then we can examine the reports from that.


### 📺 Lesson: Backup Logs


So we're in the Recovery Services Vault.
We're into the backup jobs,
and we can see that our second backup completed.
So let's compare the two.
It took about the same amount of time, 27-28 minutes.
The first backup, we can see,
was 11.8 gigabytes, roughly,
and the second backup was only 350 megabytes,
which is comparatively smaller.
That is because Azure backup is incremental.
So after the first full backup, it only transfers changes.
Now let's look at the reporting side.
If we go into Backup Reports,
we select the log analytics workspace
that we were working with,
we're gonna see that there's really nothing.
That's because there's often a latency.
So we just ran the backup
and the backup reports could be not run until tomorrow.
So we are not getting real time information
under Backup Reports here.
So if I go to the Summary tab,
again, it hasn't yet been run.
So in order to get more data,
we're gonna have to switch over to a logs view.
To do that, I'm gonna go into Azure Monitor
and I'm gonna go into logs.
And once I close the video, I can narrow the scope
of the logs into the Recovery Services Vault itself.
So I'm gonna go into the subscription, the resource group,
and I'm going to choose the Recovery Services Vault
as my scope.
And click Apply.
I am going to shrink the menu here
and I'm going to say Select a Table,
and we can see three tables on the left side, right?
So we have the Azure Diagnostics,
we have Azure Activity,
and we have the Backup Jobs table.
Now the language of this Azure logs
is called KQL, or Kusto Query Language.
And so I'm going
to click on the Azure Backup Jobs table,
and by default it runs
and shows me all of the entries.
I can also switch over to KQL mode if I want to write this
as a query, and I'm familiar with KQL
and can be more complicated with that.
So what we have here is two entries in the backup jobs,
and we can see the data transferred.
One of these entries is the backup
and one of these entries is the restore.
I can switch over to KQL mode,
and we can see, I'll zoom in a little bit,
we can see that it's just got the table name.
If I want to be more specific,
I can say summarize jobs by status,
and I'll run that.
And that shows me that there are two completed jobs in this,
or however many jobs that ran.
Now if you're not sure what else kind of information
you can get from this,
there's this link at the top that says Queries Hub.
And we are, again, very specific
to the Recovery Services Vault type that we're in.
And we can see failed jobs.
We can see the trend for cloud storage consumed
and things like that.
Get information on jobs, successful jobs,
failed jobs, et cetera.
And even look at the different types of items
that have been backed up by vault and by backup item.
So there are prebuilt queries that we can look through
to get inspiration for what kind of reports we want
to get from this data.


### 📺 Lesson: Soft Delete for VM Backups


NOTE
This file was generated by Descript
Now Azure has released a new
security feature called the Soft
Delete for Recovery Services Vaults.
If you're not familiar with the
term, a soft delete is when you go
and delete something but it doesn't
actually get deleted right away.
There is a delay between the time
that you initiate the delete process
and when it gets actually deleted.
This allows you to change your mind.
Now, the reason this is a security
feature is because if somebody was to,
hack into your account and to delete
your virtual machines, they would then
also maybe want to delete your backups.
And that would really get you in trouble.
So them not being able to affect your
backups because you can restore within
14 day period is a security feature.
Now this is enabled by default on
brand new recovery services vaults.
If you have an older recovery
services vault, you can turn this on.
Now in Azure, the soft delete
process takes 14 full days.
So if you initiated delete,
there is a 14 day period where
it's still available for you.
That means you can undelete it.
And once you undelete it,
that file is available to
recover from things like that.
It becomes back to a normal
state on the 15th day.
If you have not undeleted the
file, it gets auto deleted.
Now that's explained.
This graph is from Microsoft website.
Pretty much that's what's
being explained here is.
After 15 days and no user
action was required and the
data gets permanently deleted.
And if you stop that, undelete within
14 days, then you can actually resume
the backup jobs and get your virtual
machine going again, or you can
restore from that backup, et cetera.


### 📺 Lesson: Azure Site Recovery / ASR to Site-to-Site Replication


Instructor: Now when the worst case happens
and a whole entire region was to be unavailable,
let's say the internet was knocked off
to the US East region.
What do you do?
So one option is to have a disaster recovery plan in place
and to have a backup set of machines
and a backup environment ready to go.
In Azure, this is using the tool
called Azure Site Recovery or ASR.
So the idea here is that we're going
to take our environment that we have,
let's say in this case, in the East US.
We have a couple of virtual machines
in an availability set on a network
that run on a couple of discs.
Of course, virtual machines require discs,
and so you're gonna wanna have ready
to go in a different environment that same setup.
Now, that doesn't mean that it's a hot swap,
where you have these machines running
and they're, you know, they're on,
you're being charged for them,
but they're not being used.
This is a case of where you have it ready to go,
but as you can see in this diagram,
they're not running and they're not ready to go.
What ends up happening is when this environment
is not available, then Azure's going
to deploy these machines in a ready state
and with all of your data backed up
and in the exact same configuration,
and all you need to do is just direct the traffic
to that new environment.
So this is sort of a,
not a hot swap,
but a cold swap.
And it could take, I mean, realistically it could take
10 or 15 minutes for an environment to be ready,
not only creating the virtual machines,
but ensuring that they are in a ready to go state in terms
of the code that needs to be on there and things like that.
So the whole startup in instantiation process.
So it could be a good 10 minutes
before your environment is ready to go,
but that is obviously better than being down for hours.
So that's is the tool called Azure Site Recovery.
So I've got this virtual machine
that I've created and let's show
how to create this disaster recovery setup.
I'm in the portal under the virtual machine
and under the backup
and disaster recovery menu,
there is this disaster recovery setting.
Now, when I go into it, it says,
welcome to Azure Site Recovery.
And since I did not deploy this virtual machine
into an availability zone,
then I don't have the availability zone
recovery option available to me.
You'll see that it's chosen a region for me
to have my new environment.
Obviously, the farther away the region is,
you are going to have increased charges
when it comes to the data transfer
between continents here.
And this might be a slower connection,
so there might be some lag.
So it's generally a better idea to choose a region
that is not too far
from your current region.
Now, there is also this concept of region pairs
where for every region in Azure,
there is one region
that has the highest speed connection.
I believe that North Europe
and West Europe are region pairs.
And so this is going to be the cheapest
and quickest connectivity between these two regions.
And there shouldn't really be any event
that affects the Northern Europe data centers
that also affects West Europe data centers.
So let's choose that.
Now, again, it's up to you.
You could choose
US,
you could choose farther off into Europe,
into Poland, for instance.
That's totally up to you.
Just realize there are cost and leg implications.
So let's say next,
and what we're gonna see here is it's going
to set up under the same subscription,
a brand new resource group, a brand new virtual network.
It's understanding
that I'm doing replication on a single VM.
So you'll see that it's got the ability
to do this against availability zones,
availability sets, and VMSS.
If I had a proximity placement group for my VMSS,
I could choose one.
A lot of this stuff is going to get created,
just not the virtual machines being instantiated.
I could choose capacity reservation if I had any.
Now we can see here that it's also gonna create
the storage account,
and it's gonna do a replication
between the storage accounts.
So from the region in Northern Europe
where my machine currently exists,
it's gonna use a recovery services vault to do backups,
and it's gonna make sure
that the data is ready
to go into the new region.
So now I can say review,
and it's showing me what's gonna happen,
the target and the source,
basically storage, replication, etcetera.
And I can say start.
So as you can see, it's actually quite straightforward,
quite simple to set up this emergency
recovery that's going to now,
it's gonna take some time obviously
to set these things all in place,
but it's quite simple using the portal to get this going.
And if there was, like I said, this rare disaster,
it hasn't happened in at least a year,
I think, maybe more,
where a region is not available.
If that does happen, then I would have another,
another environment in a different region
that I could start up
and it would have all of the data backups
and everything ready to go.


### 📺 Lesson: ASR Test Failover


Instructor: So like many things when it comes to Azure,
we're gonna have to let this run for a little bit.
We can see that the notifications are still in progress,
that there's still this enabling replication job
that's been running.
If we go under disaster recovery,
after a few minutes it turns into this dashboard
and you can see the status says replication in progress.
I can even click it and I can see that it's done some things
and now it's starting the initial replication.
So we do have to wait for the virtual machine
to be duplicated into the recovery services vault
before we can test the failover.
So I'm gonna pause the video
and when we come back, hopefully that'll all be done.
So that actually took a little while to complete,
but now that it is complete, we can refresh this page.
We can see that the status is protected
and we've never tested the failover.
So in this video I do want
to click the test failover button.
Now incidentally, if we
no longer need the source environment,
let's say we are copying the environment
from one region to the other,
then we want to do the final failover,
which is to essentially
stop the replication
and to make the the destination target environment
its own environment.
But in this case we're going to test failover.
So now it's going to start this process.
So we have our original virtual machine in Northern Europe.
We have the ASR that was set up to point to West Europe.
We can see that the last processed recovery time is from
this time of the day
and we can choose
a virtual
network.
It says it's recommended the network selected for test
and final are different.
Well, in this case I'm not gonna do the final,
so we'll just say test.
So you can see it's starting the task.
So we've now moved into a
initializing
test failover.
We can see this as a job.
So we can see that it was able to
get the virtual machine running within around two minutes.
If we refresh.
So we now are supposed to go
and check it to make sure that it did run.
So we can see that the virtual machine
in the ASR sense in Western Europe is running.
And that did get created just a few minutes ago.
So we can obviously log into some machine, use it, make sure
that it's
successfully a complete copy
of what was running in Northern Europe.
So let's go back to the original.
So you'll see that the test failover has been completed
to delete the virtual machine created
during the test failover,
use the cleanup test failover option on the virtual machine.
And so back to where we have our failover test failover,
we have a cleanup
task
and we can kick that off
and we can see everything was fine and now it will go
and undo the test failover.
So we saw
that
setting up the
Azure site recovery was quite easy
and testing it,
we could do that quite straightforward as well,
and when we're done, we say clean up.
If we didn't, if we wanted to fail over permanently,
that is cut the connection
between the source and the target,
we would just do the failover option.


### 📺 Lesson: Hands-On Practice


[No transcript available for this lecture]

