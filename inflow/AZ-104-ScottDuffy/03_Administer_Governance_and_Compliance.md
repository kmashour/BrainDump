---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "03"
title: "Module 03: Administer Governance and Compliance"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 03: Administer Governance and Compliance

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** RBAC Built-in and Custom Roles, Scopes, Access Assignments, Storage RBAC, Subscriptions, Management Groups, Cost Management & Advisor, Resource Locks, Azure Policy, Custom Policies, Tags, Resource Move  
**Line Range:** Lines 3862 – 5836 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts


### 📺 Lesson: Overview of RBAC


Scott: So in this section of the course
we're gonna be talking about Role Based Access Control.
This term is abbreviated as RBAC or "R-back".
So RBAC is a security feature in Azure
that allows you to grant specific permissions
to users, groups, or applications
based on their roles in your organization.
So you get very granular control over permissions,
that allows you to have increased security
as well as increased compliance
with your various regulations and policies.
Now, at a very basic level,
in order for a user to be able to do something,
either within your application
or within Microsoft Azure itself,
it needs to have permission,
and what this means is that there's a table somewhere
within Azure of all of the users
and all of the permissions that those users have
to act within your environment.
At a very basic level,
we can look at something like this
and say we want to grant Student 1, which is a user,
read access to this storage account, Storage account 1,
and that is a single permission listed in a table.
But if you think about a larger organization
with tens of thousands of users
and perhaps thousands of resources
including storage accounts, and virtual machines,
and apps, and not only read access,
but write access and ownership access,
all of these types of permissions
become very difficult to manage.
You can take your 10,000 users
multiplied by 1,000 odd permissions that they can have,
and that gives you millions of permissions
that would be stored in this type of table.
So what is the drawback to this,
assigning individual permissions to individual users?
Well, Microsoft has something
called the Principle of Least Privilege.
It's more of a general policy within IT
and that is, in general, to have the best chance
of having a high security system,
you want your users to have the fewest amount
of permissions that they can have.
So don't just grant everybody
in your organization administrative permissions,
try to be more granular and grant read permissions
to people who only need to read stuff,
update permissions to people
who do need to interact with the data,
but don't need to own the data,
and be very selective
of who you give administrative permissions to.
So if you're doing this types
of one-on-one permissions-to-users mapping,
you may have some users in your organization
that end up with too many permissions.
You can imagine somebody who's been
with your company for years,
let's say 10 or more years,
have had a lot of roles in your organization,
moving from job to job,
they would then accumulate lots and lots
of IT permissions on their user account,
and their account is one of the more powerful accounts.
Maybe other employees come to that person
when they need assistance
because they have permissions to do things
that the employees don't.
Inversely, you have some employees that are trying
to do things that they should be allowed to do
that end up not having permissions.
You can have a brand new employee and it might take months
before you assign them all of the right permissions
that they need to do their job.
So, this increases the cost and the effort
in order to maintain your permission system.
You are gonna have a help desk
that's gonna receive inquiries every day
asking for permissions to do things,
then they have to wait for those tickets to be responded.
It slows everything down and you end up
with lower productivity across the organization,
and because you do have users
that have too many permissions,
you have a higher chance of some type of attack,
identity attack, where a malicious user gains access
to your system and can do things
that you don't expect them to be able to do.
So there is a system called Role Based Access Control.
In this case, there's this concept of a role,
which is like an abstraction.
When you create a role,
you're basically defining a job
that someone can potentially need to do,
may not map to your job titles,
but you can sort of generalize what the roles are
in your organization.
Who needs read only-access, who needs to be contributor,
and who needs ownership access to various resources.
You can loosely define those
into an abstraction called roles,
and then you assign those roles to individuals.
So, examples of roles could be a developer role,
a manager, development manager role,
or an IT operations role,
maybe just somebody who needs to view reports,
and doesn't want to be able to affect the data in any way,
and there's obviously gonna be
administrators of various sorts,
including global administrators.
These are roles that you can assign individuals to
in your organization.
Now, it doesn't mean that somebody can't be two roles,
so you can be operations and you can also be a developer,
and in this particular example,
you can assign two different roles to the same person,
there would not be any conflict in that.
And so you're just managing permissions at the role level.
You're not assigning permissions to individual users,
you only assign permissions to a role,
and you assign the role to the users,
and, believe it or not,
that actually simplifies the length of the table
in this example for how many permissions you have.
Instead of having millions of permissions
when you have tens of thousands of users
and thousands of resources,
you may only end up with several thousand permissions.
Makes it a lot easier and simpler for everybody.
What are the benefits of Role Based Access Control?
Well, it is a level of abstraction
that does simplify the management of permissions
across your organization.
A simpler management means fewer errors.
As long as you can confirm
that your users are assigned the right roles,
then they should be getting the right permissions.
If you ever get right into a situation
where a particular user needs a permission
that's something outside of their role,
then maybe you either need to define a new role
or they need to be also a member,
additionally a member of a second role.
That's the decision you're making,
not "Should I assign a new permission to a one-off user."
Basically, all users are treated the same for their role.
All developers have the same permissions.
Nobody has secret extra permissions.
When I say secret, it just means you do it once,
and then by tomorrow you've forgotten
that you've assigned this permission to somebody,
and then months and years later,
then that comes back and it bites you.
And it's also easier
for brand new employees who get started,
to just be assigned the developer role
and not have to go back
and find the 250 things that a developer can do.
Now, that's not the only approach to security.
There's also Claims Based Access Control or CBAC,
but in the Microsoft Azure world,
we tend to gravitate towards Role Based Access Control.
So it's one approach to simplifying permissions
and simplifying those assignments.
So in this video, and then in the videos that follow,
we're going to look at Microsoft Azure portal,
and how to create roles and assign roles to individuals.


### 📺 Lesson: Managing Azure Administrator Roles


Trainer: So we're back into Azure Active Directory
here in the overview screen.
We've already talked about users and groups
and external users.
Let's talk about roles and administrators.
Now, when I click on this screen,
it's gonna take a second to come up here,
but it's important to keep in mind
that we're only dealing with Azure Active Directory
related roles.
And these are typically called administrative roles.
So we're gonna see a list in a second here
of all of the roles that are available
to be assigned to users.
But none of them have to do with low level assignments.
It's not dealing with individual permissions
on a storage account or individual permissions in an app.
These are all administrative type permissions.
First thing I can see is it says "Your Role"
and it tells me that I'm currently logged in
as a global administrator.
If I was to log into Azure as a student or a teacher,
remember I have teacher accounts
that are help desk level users,
then this role would reflect that.
And in that particular case
I might not even be able to do anything on this screen.
A lot of these things would be grade out.
So because I'm global administrator
is what allows me to continue at this point.
Now there's a list here of built-in roles.
You see it says "Type, Built-in"
and there's over 90 built-in roles
that are all administrative related.
We can see that application,
the first one says "Application Administrator"
but what it relates to is managing app registrations
and enterprise apps.
So if we go back to the top screen here
we've got enterprise applications and app registrations.
So being an application administrator
simply gives me access to these features of Azure AD.
Similarly, other roles within this list
is gonna give me access to other features.
Now, in some cases you've got
administrator level permissions
and you have reader level permissions.
So you don't have the access in this case to
modify the security attribute keys and values,
but you can read the security attribute keys and values.
And this might be important if you have applications
that rely on reading these values
but you don't want those applications to ever modify them.
So you'll see a lot of times it's split
between administrator permissions and reader permissions.
We even have global administrator and global reader.
Global reader can read everything
that a global administrator can but not update anything.
That's really interesting too.
We already saw that you can have help desk permissions,
password permissions,
the knowledge management, license administration.
So all you can do is just manage licenses.
So this sort of goes into these very specific
administrative roles. Okay?
So, this might be, you know, you might be thinking
that this is not very useful for day-to-day users.
When you think about your employees
within your organization, maybe only a small percentage
a single digit percentage of them would ever have
administrative permissions, and that's true.
So this isn't the main way you're going to use RBAC
going forward in terms of Microsoft Azure.
But for administrative roles
this is obviously very important.


### 📺 Lesson: Switch Storage Account from Access Keys to RBAC


Instructor: All right, we've seen
how you can manage administrative permissions
inside Azure AD on the roles and administrator's menu.
And we saw about those 90 built in roles,
mostly having to do with admin stuff,
like printer management, password management,
and teams and SharePoint, and things like that,
but what about real resources,
like web apps, virtual machines, containers,
things like that?
How do you manage the permissions of users
to those resources?
I am back in my Azure portal.
Now, I just signed up for a free trial on this account.
It's eligible for it, I guess.
And what I need to do here is
I'm going to create a resource and then that resource,
we're gonna see how we manage permissions
to that resource using Azure AD.
So I'm gonna create a storage account
as my first resource here,
so I'm gonna go and say create storage account.
We have to create a resource group,
so this is my first resource group.
And we give the storage account a name,
so this is my very first storage account.
Let's see if that passes validation.
I'm gonna deploy it into Western Europe,
and I'm gonna choose the simplest options,
'cause we're not really demonstrating
how to create a storage account here,
we're demonstrating the permissions aspect.
So, I've created a fairly simple storage account.
I'm gonna basically go with the default versions
on the advanced tab here.
We're gonna go with the default versions
on the networking tab.
We have the data protection tab,
we're just going to keep the default as well,
encryption, tags,
and finally, we're going to create the storage account.
So remember, we do get a storage account free
as part of this free tier,
plus we're getting the credits as well,
so it's not really gonna be an issue.
Now, I did miss, I guess, on the advanced tab,
that we do have AD authorization as one of the options,
and we can enable this after the fact.
So we're gonna leave this disabled,
go back to the review screen, and say create here.
This should create in under 60 seconds,
and we can see that this storage account
was created in 30 seconds.
So, pretty good.
I'm gonna say go to resource.
Now by default,
because I didn't change the settings in the creation,
storage accounts are secured by access keys,
so this is an example of claims-based access control,
or CBAC.
If I have this security key,
then I have the ability to have administrative permissions
to this storage account,
so anyone, anywhere in the world,
who has access to this key,
has access to this storage account,
if I've got public networking enabled, which I do.
If you turn off public networking,
then it's just an internal to Azure,
and anyone internal to Azure would have access
to the account with that key.
So obviously, claims-based control is convenient,
but not always entirely safe,
so what we might wanna do
is have this storage account secured
by Azure Active Directory instead of the keys.
So we're gonna flip down
to the settings here under configuration,
and we're going to enable
Azure Active Directory authorization.
And this allows the role-based access control
to be the security for this particular account.
And at the same time, if we wanted to,
we can disable the storage account key type of access,
so disabling claims-based access control
and enabling Azure AD control.
That's one way to configure this.


### 📺 Lesson: Assigning Myself Permission to a Storage Account


Instructor: Now by disabling storage account key access
and enabling Azure AD access.
There are some immediate implications,
we saw when we clicked the disable
for storage account key access.
What we really did was we've basically
broken any access by keys, by shared keys,
secured, shared access signatures.
All of that is immediately denied.
So now any historical access
to this account using storage keys
is basically broken by doing this.
So don't do this on a production account that has
constant access by third party applications
and stuff like that.
Now if I go back to the overview screen here,
we should see here even on the overview screen
that a storage account key access is disabled and
therefore the active directory access is enabled.
We do this through the access control IAM tab.
Now I can click this view my access button
and I can see that I have an owner role
across the entire subscription.
And this is an inherited role.
You know, I was obviously able to create the storage account
and I could assign other people
permissions on the storage account.
So I do have ownership role,
but you might be surprised to say
and to learn that I do not have access to the contents
of the storage account.
So currently, even with owner permissions
on the storage account itself,
I cannot read, upload, delete any of the files
contained in the containers file shares any
of the data in the queues and tables.
So the data interaction permissions are separate
than their resource permissions.
So let's flip over to the roles tab here
and we can see that there are dozens of roles relating
to this storage account.
Very important point.
This is critical to role-based access control.
There are basically three types of permissions.
There is the reader permission,
there's the contributor permission,
and there is the owner permission.
These are built-in roles
and we can see, I'm gonna
expand the columns here a little bit,
but we can see that the reader permission
allows you to view all resources
but does not allow you to make changes.
The contributor permission gives you ability
to manage resources but not assign roles.
And the owner permission gives you full access
to everything, including the ability to assign roles.
So reader is read only, contributor is read and write,
and owner is granting permissions
and includes all of these things.
As we scroll through the dozens of permissions related
to storage accounts, we can see a common thread
where you've got reader, contributor type roles,
monitoring reader, monitoring contributor.
The one that's relevant to us here is data blob reader
and data blob owner and data blob contributor.
Okay, so data blob reader, as it sounds,
allows you to get read access to containers and data.
The contributor will give you read, write,
and delete access to containers and data.
And the owner gives you full access to containers and data.
So this is what I'm interested in to assign to myself.
I actually have to assign myself permissions
as a data owner in order to be able to work with containers.
So I'm gonna go into the add tab here.
I could have also done it, if I go back to check access,
there is this add role assignment button as well.
Two different ways to get there
and what I wanna grant myself is I want
to grant myself storage blob owner.
Okay, so I click on that and I say next
and I'm gonna select which members have
data owner permissions.
I'm gonna give it to my two administrative accounts, right?
So two administrative accounts.
I could put conditions on this if there is some type
of more fine grained access control,
but I don't need that right now.
And I'm gonna say review and assign.
And basically I've given blob data owner
permissions to those two users.
Now, I will not have access to tables, queues,
file shares at this point until I grant myself permissions.
If I go back to view my access,
I can now see storage data owner as being permission
for myself, which is exactly what I want.
I need this permission in order to start working
with containers and with blobs.


### 📺 Lesson: Managing Resources with Roles


Instructor: All right, so now that we've got
ownership permissions
over the data, right, so the data permissions are separate
from the resource permissions, we can go
into the blob storage containers, create a new container
call it my first private container, and that was successful.
We go into the container
and we should be able to see that authentication method says
that the authentication method is AD user.
Now, if we had both AD user and access key permissions
we could switch back and forth between them.
But remember, we disabled access key permissions
so this isn't gonna be able to help us.
If you are seeing a red box here
with some permissions error, it may be
that you didn't assign the data owner permissions
to the user that you're using.
So that's probably the most likely reason for an error.
But in this case, I have the right permissions.
I can say upload.
I'm gonna upload an image here
a jpeg file, png file to the account.
And so we've successfully been able to interact
with this storage account.
Now don't forget that the traditional methods of interacting
with this are no longer working, this SAS option.
We don't have storage account keys.
Anyone who wants to access this image requires
Azure AD level permissions.
Now, this may be a good time to talk about permission scope.
I can actually assign permissions only to this container.
Let's say I create a second container called second.
So I have my first and I have second.
I can assign permissions at the container level
and not at the storage account level if I was wanting to.
So if I go into access control
obviously I can view my own access and I can assign access.
So let's say I want to assign data reader permissions.
So not the ability to modify files or upload files
but just the ability to read the contents of a file.
And I wanted to do that to my teachers.
Okay, so I go teacher one, teacher two, teacher three.
So I can assign storage, blob data reader
to the teachers only on the, my first container
I'm gonna say review and assign
and we can see under scope before I click it.
This is a bit of Azure speak
but we've got the subscription ID
we've got the resource group
and then we have the storage account.
And then we have a very first storage account
and we have containers, and we have my first
so this scope right down to the container level, right?
So we can give scope to the subscription
scope to the resource group, which we haven't talked about.
Scope to the storage account or scope to the container.
Now there's a trick here as we're working with
storage accounts.
If I go into view, access to this resource
or I'll go into role assignments here
I can see that there are, for the scope only
the my first container, these people have access to it
but these other scopes are inherited.
If I go to the second container into access
control and role assignments, then the teachers
do not have access to the second container, right?
So you can see that permissions can be assigned
within Azure at various levels from the
specific container, storage account, resource group
and to the subscription level.


### 📺 Lesson: Creating Custom RBAC Roles


Instructor: Now it's entirely possible
that the roles listed here
are not granular enough for you,
or maybe there's certain permissions that aren't included
that you would like to be included
or permissions that are included
that you don't want to be included.
So Microsoft has obviously created these 50
or 60 roles for you to choose from
but maybe it's not great for your circumstance.
So there is this thing called custom roles.
You have to be a Azure Premium
P1 or P2 level in order to get access to custom roles.
But basically what you can do is get right down
into these super granular permissions
and then be able to pick and choose.
Actually, what I didn't ever show you
was that if you look at these roles that,
let me just expand the direct the names a little bit.
We go back to Storage Blob Data Contributor as an example.
And I say View,
this gives you an example
of there are actually six permissions
that are low-level permissions that are part of this role.
Okay, and if I switch over to the JSON view
we can see here
that there are these types of permissions, delete, read,
write on containers, and move and add and things like that.
Take data actions.
So maybe, like I said, maybe some of these
you don't want them to be able to delete.
They can read and they can write,
but deleting is, should be not allowed.
That would be an example, a contributor that cannot delete.
So, you can do a couple of different things, right?
You could assign them the contributor permission
and then you could actually assign them
a deny assignment for deleting.
That would be a bit complicated.
This is the type of thing that if you forget to do it
they can delete.
What you probably wanna do is create a custom role.
So we're gonna go back to the homepage.
We're gonna go into subscriptions
and we're gonna go into
the subscription that I'm dealing with here.
And we're gonna go down looking at access control.
And this is the subscription level.
So we can look again at the access
and who's got access to the subscription.
But what we're curious about and interested in
is this create a custom role section.
So I'm going to create a custom role.
And I like that idea.
I think what I'm gonna do is I'm going to create
a Data Contributor without the delete.
Okay, and you name it something that is relevant.
Storage Blob Data Contributor Without Delete.
Now you can see there are ways of getting about this.
You can start from scratch
which means you're gonna have to remember or look it up
what are the permissions that Blob Data Contributor can do
or probably more helpful would be able
to clone this existing role.
So I wanna clone the Storage Blob Data Contributor role.
I'm gonna select it.
So I'm gonna start off
by basically editing an existing role.
That's probably the, maybe the easiest way to start.
But what you're gonna find when you get
to some of the higher level permissions,
like the owner permission.
The owner permission is very simple.
It's only got three assignments.
And if you want to, you know,
come back on the owner permission,
it'll be a little bit more difficult.
But at the contributor level, and we can see here
these are the permissions that are contained
within the, we saw this in the JSON just a second ago
there are four action permissions
and five data action permissions.
So what I said I wanted to do is I wanted to
remove delete permissions.
And we can see here that there are permissions
that allow me to delete containers
and I don't want my, this role to delete a container.
And there's also deleting of the individual blobs.
And so I don't want to delete the individual blobs
and I'm gonna assume read, write,
and all of these other things are what I do want
but I don't want deleting of those things.
Now, by default, I'm assigning this
to the subscription level, which means that this role
is available for every storage account,
every resource group, across every container,
across my thing.
If I wanted to assign a user to this role,
then they would apply to everything.
An interesting thing here is I could say,
really, I'm only interested in the resource group
that's first RG.
And so this role would be very contained
to a specific resource group.
But do keep in mind that there are limits.
You can't, you can only create 5,000 custom roles.
And so creating too many roles and too granular scope
you might bump into that 5,000 limit.
We can actually look at the JSON
and we can see here now
we don't have the delete permissions,
so it's identical to the Storage Blob Data Contributor role.
But I don't have delete permissions.
And I can say, great and I can say create.
So I've created a custom role that does not have
it's a contributor without delete permissions.
And so if I wanted to, let's say I say role assignment
and I'm interested in my custom role,
which is this one
and I'm going to assign this custom role,
the Contributor Without Delete.
I'm gonna pick one of my students.
So student one, let's say student one, two, and three.
So these students can access Blobs and blob containers,
but they don't
they can't delete them, they can update them,
they can read and write and add, but they can't delete.
So in this way, we've used a custom role
to give ourselves more granular control
over our permissions that the built-in roles
aren't giving us.


### 📺 Lesson: Resource Group Scope


Instructor: Now we've previously discussed
this concept of scope when it comes to access control.
When you are making a role assignment, you are choosing
the individual, the role, and the scope, okay?
And you can see here a couple of examples
where there's subscription scopes permissions
and there are resource scoped permissions
for this storage account.
But some students ask this, and it's actually
quite a common thing to do in a production environment,
in a real environment, is the resource group scope.
So, it's not uncommon to restrict access to individuals
to certain resource groups.
So you might have a resource group for development resources
and that might have a wide range of people
who have permissions to access those development resources.
And likewise, you might have production resources
in a different resource group
and then you are able to restrict access
to those resources to only specific individuals.
So obviously you want the production individuals
to be only a handful, or as the development individuals
could be dozens or hundreds.
So, that's a resource group scope.
If we go into the resource group, I've created two,
one for development, one for production,
go into access control.
And I can see under role assignments,
we can see that the number of people inherit access to this
for storage blob contributors, for this resource.
And that's probably fine
but actually maybe I want to have these students
to have full contributor access to this resource group.
So, I can actually add a role assignment
and I can say contributor access.
So I'll just, instead of doing specifically for blobs
and for queues and things like that,
I'll just say for the development resource group,
I have full contributor scope.
So I'm gonna say select members
and I'm gonna focus on students one, two, and three.
Okay, so I want, in the development group,
for the development VMs resource group
these three students have full contributor access.
Now this actually gives them full contributor access
and it actually, whereas the student blob contributor
without delete role actually restricts their ability
to delete, these permissions actually enables their ability
to delete so you'll see here that there's,
we can call it a conflict where you've got one set
of permissions assigned here
and one set of permissions assigned here.
But really what's done is merged them.
So I would expect the students one, two, and three
to be able to delete files in the development resource group
because I've just given them contributor access.
Whereas in the production VMs,
we can see that they are going to inherit
this type of permissions.
So unfortunately, once you've granted them permissions,
there is this thing called deny assignments.
But deny assignments can only be done
through blueprints that map onto subscriptions
and so we cannot, in the portal, add a deny assignment.
But maybe what I'll do for this
is I'll only give them reader permissions.
So, if I say add, role assignment,
I'm gonna choose the reader level.
I'm gonna choose the same members
and we can see that this reader access
is on the production VMs so they can see them,
they know they exist, but they cannot modify them.
They cannot stop them, they cannot reboot them,
anything like that.
So again, when you've got two sets of permissions
for the same account, the permissions are merged.
So, you're not ever taking away permissions,
you're just adding permissions.
And so in this case, they've got a reader access
to the whole resource group, and they've got
specifically, blob data contributor access without delete.
So, and this way you can work with resource groups levels
to assign access and it's quite common
and this is done in a production environment all the time.


### 📺 Lesson: Interpret Access Assignments


Instructor: So the next requirement
of the exam says to, "Interpret access assignments."
Now, there's a couple of ways that we can look at the way
that others have access to our resources.
One way you could do it is to go into the resource,
in this case, the production resource group.
Go into Access control and under Role assignments.
And we can see a list of all the people and applications
that have access to this resource group, okay?
So you can see that, as the owner, I got...
the owner of the subscription I've inherited access
to this resource group.
Remember we assigned reader access
to three of the students and we've assigned
this blob data contributor without delete custom role
to those same three students
and we can sort of see that here.
Another way to see what an individual has access to
is to go into Azure AD, go into Users, pick the user.
And there are two types of roles.
Remember, we've been talking about this in this course.
There's Azure AD roles and so,
these are the administrative roles
for your Azure AD, and there's none.
And then there's the Azure roles
and there's two different menus
to view the assignments on that.
And so, we can see that this user,
Student 1, has reader access
to the production VMs resource group,
contributor access to the development VMs resource group
and, again, the storage blob data contributor
without delete access at the subscription level.
So these are the scopes and these are the roles
that have been assigned to this individual.
We can go back here, we can pick one of the teachers.
We can see that the teacher has been given both help desk
and password roles in terms of this,
actually the password resource has been deleted.
I'm not sure why the assignment is still there.
We can easily remove that particular assignment.
So he has help desk role to Azure AD.
And if we go into the Azure roles
we can see that they've got data reader access
to this entire storage account.
So that is how we interpret access assignments
within Microsoft Azure Portal.


### 📺 Lesson: Accounts, Subscriptions, and Resource Groups


-: So in this section of the course, we're gonna be talking
about subscriptions and resource groups.
And I wanna define some terms
before we get started, this way,
when I'm talking about Azure accounts or Azure subscriptions
you know that they're slightly different concepts.
So the four terms we're gonna talk
about in this video are the Azure account
a tenant, Azure subscription, and a resource group.
So let's start off talking about one
of the more basic concept, which is an Azure account.
Now, in the context of this, it's basically a user id
it's a person, or it also can represent a program.
So you can basically assign an account to an application
so that the application can run its own security context.
It is considered bad programming practice
to take a real person's user ID
and password and program that into an application.
So when we're talking about people
who have access to resources within Azure,
or assigned resources elsewhere in your solution,
you're talking about an account and
that can either be a person who's yourself or someone who
works in your organization, or it could be an application.
And so this is the basis of authentication.
Now we have a section of this course talking
about Azure Active Directory and authentication separately.
But basically this is
this is the top level definition of an account.
Now a related topic is a tenant.
So whereas the account represents the person
the tenant represents the organization or the company
and usually you have a domain name associated with that.
So we live in this modern era where every big company has
its own domain name
and you may want to start using that domain name
for your user IDs in terms of Microsoft Azure.
And so it's gonna be your company .com
as the tenant's domain name.
Now, if you don't have one, Microsoft will sign you one.
So they have this dot on microsoft.com extension.
And so when you create your tenant
it's gonna create the tenant name dot on microsoft.com
and that will be the domain you're given
if you don't provide one.
Now this basically represents what is called a
dedicated instance of Azure Active Directory.
And as I said, we do have a whole section
of this course talking about Azure Active Directory.
So I won't go too far into it here.
It's important to know though, you have this organization
which is a tenant, and every account
belongs to at least one organization.
There's no concept of having an Azure account
and you're not part of any tenant, that's just
you're not an Azure user if that's you.
So when you log in, you're gonna have a default tenant
and that's the tenant that you have.
You can also switch tenants and it's also fairly
easy to create tenants.
And we'll get into that in this course.
Next step, we'll talk about the concept of subscription.
So now we know that the account is the user
and the tenant is the organization.
The subscription is this billing agreement with Microsoft.
And so there's many different types of subscriptions.
You can have a free subscription or pay as you go.
There's enterprise agreements.
There are different programs.
I think there's probably, you know
a dozen different programs that Microsoft has
that are payment plans for subscriptions.
And so the subscription is the level
at which payment gets made.
So you're gonna have a credit card or an enterprise
agreement that the bill is gonna get sent out to.
And so any usage of resources
within Azure gets billed to the subscription.
So we should say that not every tenant has a subscription.
So if you go and create a brand new tenant today
by default, you have no subscription.
Now what this means is the tenant can't create
Azure resources, so there's no billing unit
and therefore there's no way
for you to even create a resource, even a free one.
So you can have tenants without subscriptions
and it's also possible to have multiple subscriptions.
So you might have an organization that has production
and development as two separate billing entities
and you can create two subscriptions for that.
So there is a multi subscription option.
Now accounts are basically assigned roles within the tenant
and so they can be an owner or a contributor or a reader
or you can give very granular role assignments to users.
So when you create a user, you assign them a role
you can actually create owners
and these people have full control of your tenant.
And so you're gonna be careful with that obviously
but it is possible to have more than one owner on a tenant.
And again, you if any account
that you wish you can invite other accounts
to your tenant and then grant them roles as well.
Now I'm gonna talk about resource groups, but
before we do, let's talk about the resources themselves.
So when I see resources in this course
I'm referring to any entity managed by Azure.
And so these are the typical ones, the virtual machines
web apps, the storage accounts, you know, SQL databases
anything that's sort of, you go in there, you create it
it's a resource, but sometimes
these resources themselves create sub resources.
So public IP addresses created when you create a virtual
machine, network interface card, network security group,
there's all sorts of resources
that get created when you create a virtual machine.
And any other of these big resources sometimes
have their own sub resources.
So those are also included as resources.
And just like you can assign accounts,
permissions, and roles within the tenant level
you can also assign people's individual resources.
Finally the resource group is that collection.
It's a way of organizing resources in a subscription.
So I look at it like a folder structure.
You go into your account, you have your subscription.
Under the subscription, you have resource groups.
And so all resources must belong
to one and only one resource group.
Now it makes it fairly easy to do some particular tasks.
You can grant permissions at the resource group level
and so all of the, you know
sort of account can only access the one resource group,
it sandboxes them in.
You can also delete a resource group
and that will delete all the resources inside.
It's one of the quickest ways to clean up what you did.
So it's a way of separating up projects,
keeping unrelated things separate.
You don't want to have a single resource group
with hundreds of resources inside.
And so keeping them separate allows you
to clean up pretty easily.
So those are the four basic concepts
as we get into this section.


### 📺 Lesson: The Subscription Dashboard


Instructor: So one of the requirements of this exam
is to be able to manage subscriptions.
And so in this video,
we're gonna be talking about the Azure subscription.
Now, the subscription is basically a billing unit
for how resources that are assigned to that subscription,
where they get billed to.
And there's basically a hierarchical structure.
Resources belong to resource groups.
Resource groups belong to subscriptions.
And subscriptions belong to management groups.
We're gonna be talking about management groups
in a future video.
So let's talk about subscriptions.
To do that, I'm gonna go into the subscription section.
Now you may have subscriptions
as part of your menu on the left, which I do,
but not necessarily for you.
You can obviously enter subscription into the search box
and get taken to that page as well.
And there's other ways to get there.
Now, I happen to have multiple subscriptions,
and maybe you have one, or maybe you have multiple as well.
Now we can almost see from the naming
that there are types of subscriptions.
There are free subscriptions.
There are enterprise subscriptions.
There are, in this case, it's a sponsorship.
This one is pay-as-you-go.
These are different people who are going to pay
for resources that are built against this subscription.
Now, every subscription can only be assigned to one tenant.
But each tenant can have multiple subscriptions.
So let's go into a one of these.
I'm gonna pick the Pay-as-you-go one to start.
I'm gonna minimize the menu on the left
to give us more screen.
Now we can see right off the overview screen
of the Pay-as-you go subscription,
I can see a spending rate and a forecast for the month,
which resources are billing me the most,
Azure Defender coverage,
security is always important,
which products I'm using,
that's just right off of the top here.
As I said, each subscription can only belong
to a single tenant,
and I can do that under Change directory.
So if for whatever reason
I want this Pay-as-you go subscription
to be associated with a different Azure tenant,
which is relating to intra, of course,
then I'll do that within this Change directory.
I'm gonna leave that for now.
Now, from this subscription page,
you can use role-based access control,
and you should use role-based access control
to control who has access to your subscription.
So, just like almost any resource in Azure,
you can assign a role to either an individual or a group
that will give them permissions to access a subscription.
So if you want to give someone else
the ability to create resources under your subscription,
this is where you're gonna do that.
If you don't want certain users
to be able to see the billing for the month,
you'll make sure they don't have the right permissions.
If you want someone to be able to see invoices
but not change anything,
there's rules for that as well.
Now, the portal is not the only place that you can go
to manage your subscription.
Of course, CLI and PowerShell
also have interfaces into the subscription.
Now, if you're ever concerned
about how your account is spending,
this is where you're gonna go.
We'll go into the subscription, under Cost Management,
and you can see a Cost analysis
as being the first place to go.
We're gonna talk about alerts, and budgets, and advisor
in future videos in this section,
so stay open for that.
But let's go into cost analysis.
So this is going to tell us in more great detail
how we're accumulating costs,
which resources are using them,
what the forecast is for the end of the period, et cetera.
Now, besides cost,
another of the things you can access here
is of course your historical invoices.
As well as under Settings,
we can see things such as quotas.
So as you may know,
you might have certain limitations
in terms of how much compute you can use
within a particular region.
So, for instance, let's say I want to look at the East US,
and so I can see all the various limitations
that I have in terms of this,
how many availability sets I can have,
how many vCPUs, dedicated CPUs,
individual instance families,
so my DS CPUs.
You can see that I'm limited to only 10
standard DS family CPUs.
If I wanted to increase that,
this is where I could do that.
I can request 20 if I know I need them.
So there are ways of limiting quotas for a subscription
within the quotas section.
All of these features,
we're gonna talk about resource groups,
policies, things like that,
in other areas of this course, locks and things like that.
But usage restrictions, they're here.
So as you can see,
understanding how to manage Azure subscriptions
is essential for organizing your resources,
applying governance, controlling access, controlling costs.
In the next video,
we're gonna talk about things such as budgets and alerts.


### 📺 Lesson: Cost Management - Analysis, Alerts, Budget, Advisor


Instructor: All right, so once again,
we're looking at my 30 day free subscription,
and just as if we had no forecast
or spending on the homepage, the cost analysis section
under cost management is equally boring
and in fact it returns an error.
I would not expect a free account to do very well
in terms of understanding what cost analysis helps you with.
So I'm gonna switch back over
to my pay as you go subscription if you'll bear with me.
So I'm back to my pay as you go
and I'm gonna go to the cost analysis page.
So this is where you're gonna find details
about your spending within Microsoft Azure
if you have a spending account.
Now again, right now it's very low spending
so it's gonna be not as interesting
as a very complicated account,
but even for my 31 cents a month, 39 cents actually,
I can see that storage is taking up 31 cents
and my SQL database is eight cents.
So I can actually see where those costs
are being split between.
I can look at the geographical split
between where my costs are.
Most of them are in US East.
I should point out
that your geography does actually impact your cost
because there are certain regions like Brazil, like Japan,
things like that
which are more expensive than other regions.
And even within the United States,
you'd be surprised to know
that there are differences in prices between things
like US East, US West, US West two, places like that.
They have subtle differences in pricing.
I can also see which resource group is taking up.
So it's my cloud shell,
if I was just to delete the cloud shell storage account,
I would save myself a whopping 30 cents per month.
We started the course talking about budgets
and so I set a budget on this account quite high actually
in terms of $150 a month.
So we can see right here
that it's got the budget as a dotted line
and so I'm not expected to come anywhere near my budget.
So if we go to the next section, it's called cost alerts.
And this is pretty straightforward.
It's going to allow you to set up alerts
based on certain thresholds
for what you are spending or what you're projected to spend.
When you go under ad, it'll actually allow you to add
a full on budget or just what's called an anomaly.
So if you don't necessarily want to have a budget,
but you just want to be alerted
when certain pricing situations happen,
then you can go into the anomalies.
Now, anomalies are actually defined by Azure.
So you can basically set yourself up an email
and it will detect when there is a cost anomaly
in your account.
So I'm actually just going to do this
and say save.
It doesn't like the subject.
Now an anomaly is defined as either new charges
that were not there the day before
or charges that were there
and have stopped or significant changes,
either increases or decreases to the cost.
So you would get an email, a daily email letting you know
that there was a change to your spending pattern,
either new resources or stopped resources
or changed of existing resource pricing.
So this is probably a good way
of tracking changes to your account.
Now, the other way we talked about earlier
in this course was budgets.
I do have a budget on this account, it's quite high.
I can actually go in here and lower the budget.
Now $150 is probably more higher than I would expect.
Now keep in mind budgets have a creation date
and expiry date
so I'm gonna go down to $20
and then I can basically have my budget text me
in this particular case when I've reached
either forecasted budget or actual budget
and what percentage of the budget was reached.
And we covered budgets before obviously.
The final thing under cost management is the advisor.
So the advisor is basically something
that runs constantly on your account
and makes recommendations across a number of categories.
And cost is one of those categories.
Now, I currently don't have
any cost related recommendations.
Obviously my account is not even running
up a dollar a month.
There's gonna be very little savings that I can look at,
but as your advisor does have cost recommendations
and if you've got a big spend,
then this can actually save you money.
The cost recommendations could be reservations
that you're paying for but are not using.
It could be virtual machines
who have very low CPU utilization constantly.
So it's almost an unused VM,
things like that where you have opportunities
to make savings.
So that is the advantage of using cost analysis
as well as budgets and alerts and advisor recommendations
within your subscriptions tab of your Azure account.


### 📺 Lesson: Resource Locks - ReadOnly and Delete


Instructor: So when you have an Azure subscription,
you have the ability to create a number of resources.
One of the risks of this then is you go into a resource,
and then you accidentally delete the wrong resource.
So let's say you're looking at this function,
and you say delete, and then you just,
it says, type the function name, you confirm.
Once you've deleted it, you've deleted it.
And so, there is some requirement for you to have
a type of warning or restriction
on the deletion of resources.
These are called resource locks.
And there are different scopes for these locks.
We'll start with the biggest scope,
which is a subscription level lock.
So if I go into a subscription, let's choose one,
and I search for lock and it says resource locks,
I can create a lock that will prevent any resource
that is part of this subscription
from being either deleted or modified.
So I'm gonna go into resource locks, I'm gonna say add,
give it a name, do not delete.
And I'm gonna choose the delete lock.
And I can even leave a little note saying,
talk to Scott before deleting please.
And if I add this lock,
then all resources that are inside of this scope,
which is the subscription,
will give you a warning message.
And saying you're not able to delete,
unless you then delete the lock.
So the lock needs to be removed
before you can delete a resource.
One advantage of this is you could
not give people permissions to delete locks.
So if you keep the person who can create and delete locks
to be a single person or a small group of people,
then your wide range of users are not gonna be able to go
and accidentally delete resources.
Another type of lock is the read-only lock.
So, read-only.
This prevents deletions and modifications.
So now, you cannot change the settings on a resource.
So for the delete lock, it only stops deletions.
But you can still go in and you go into your app service
and change some of the settings,
and manually scale the instance and things.
For the read-only lock, you are prevented
from making any changes to any resource.
I'm gonna keep these two locks.
So if I go back to the dashboard
and I go to, let's say, my function app.
And then I pick one of these resources
that's on the function app,
like the app itself, let's say.
And then I try to delete, this should fail
because I have a delete lock on the whole subscription.
And you can see, it says failed
because the following scopes are locked,
and it tells me the subscription.
So I do not even get the chance to override it at this time.
I have to go back to the lock and remove the lock
in order to be able to do it.
So I'm gonna go back to the subscription,
go back to the lock,
and I'm gonna remove both of these locks.
Now, like I said, there's multiple scopes here.
So I can also go to the resource group scope,
type lock,
and I can create another delete lock
on the entire resource group for function app.
This way, I can still not delete
any of the resources in this resource group.
So if I do try to delete the function app,
this failure is on the resource group scope.
So you'll see, it's the same message,
but it's a different scope for why it failed.
And you can even go into the individual resource.
So if we go into the function app and we type lock,
we can see that we could create a read-only lock
on this specific resource.
So other resources in the group
are prevented from being deleted.
This resource is prevented from being modified,
so they're cumulative.
This also means you can't allow us,
you can't overwrite
this lock in a subsequent resource
if you've got a lock on the higher level,
which is like the resource group in this case.
You'd have to go up to that resource in order to modify it.
And again, you may not even have permission for that.
Actually, we can see right off of this screen,
if I delete that lock,
I can go to the resource group scope right from here.
And I can go to the subscription scope right from here.
That's a clever addition. Way to go, Microsoft.
So resource locks operate at subscription,
resource group, and individual resource levels.
And allow you to prevent either just deletions,
or modifications and deletions on resources.
And you have the ability to control who has access
to delete or create locks.


### 📺 Lesson: Azure Policy


Instructor: So in this video
we're going to talk about the objective of the exam
that says implement and manage Azure policy.
Now policy is one of these core governance aspects
of your Azure subscription
where you can take a lot of different rules
that you might have in terms of the use of your account
or your subscription
and use policy to implement those rules.
Perhaps the best way to describe this is to show it.
So I'm going to go into Policy.
If you type policy into the search box,
you'll be taken to Azure policy.
On the left menu under Authoring it says Definitions,
Assignments, and Exemptions.
I'm going to choose Definitions.
Now there are hundreds and hundreds
of built-in options for policies.
So we can see everything from things about SQL database,
Kubernetes, PCI, which is the standard
for credit cards and banking.
There's country specific policies,
I'm going to put into a thing called allowed locations
into the search box.
'Cause we can't scroll through such a big list.
We're going to find the policy that we're interested in.
We can see there are three options that come up
when we search for allowed locations.
One just says allowed locations.
The other says allowed locations for resource groups.
And the third says Allowed Cosmos DB locations.
So I'm just going to choose allowed locations.
Now again, these are just definitions
and these are just options
that Microsoft is allowing us to choose from.
When we go into it, we can see that the policy
is a at its core, a JSON document and it's kind of readable.
If you can read a little bit of JSON, you'll be able to see
that it has a name, it has a description and a version.
And what it's going to be doing is it's going to be,
so asking as a parameter, for a list, an array of locations,
which are regions.
And the policy itself says only the field location
must match one of the list of allowed locations.
It also must match global.
Oh.
So when you're deploying any kind of resource,
the field location must be one of the allowed locations.
It's not going to count if it's going to the global,
and it's also not counting B2C
intra accounts.
But if the location is not one of the allowed locations,
it's going to deny that deployment.
Just the simple version is you can only deploy
resources to the defined locations.
So in order to show this, we're going to say Assign policy.
Now I get to decide which scope within our account
we want this to apply to.
We could be quite restrictive
and we can apply it to only a specific resource group.
So for instance, in this az104demo resource group,
I can restrict the locations of resources
that get deployed in that group.
It may be that certain users only have access to this group
and no other groups.
And then we want to restrict the locations
of resources deployed in that group.
So I'm going to select it,
but you could deploy it to the subscription level as well,
or to the management group level.
So I've chosen a resource group.
I can also exclude certain resources from this policy.
I'm going to skip over all of these predefined lists
called Allowed locations.
Now, one of the parameters of the policy
is to provide a list of regions.
So let's say I only want resources deployed
to East US, West US, one of those regions,
Central US, okay?
So I've chosen seven regions in the United States
that I want allow resources to deploy to.
So again, for that resource group,
resources will not be allowed to deploy
to any other location.
Now, I could have this running under
a specific managed identity if it needed to have access
to resources itself, but it doesn't.
But I can also create a custom compliance message.
I don't have to.
That says, you know, please speak to Scott
if you require these regions.
Something custom like that, say Review and create.
And I can say Create.
So we're going to let that run.
It says it takes five to 15 minutes to take effect.
It could be quicker than that.
Now like I said, there are literally hundreds of options.
So for some inspiration,
you can certainly read through the list,
find something that relates to what you need it to do.
You have options around which versions
of SQL Server that you deploy,
SSL connectivity, things like that.
You can have options around virtual machines,
virtual machine scale sets,
and many of the resources that you can,
that you want to restrict.
So enable Azure Monitor, enable change tracking,
things like that.
Now, if none of these actually suit your needs,
you can create your own policy.
So if you go under policy definition here,
then you can give it your own name
and deploy it to its own location
and then provide your own JSON
that does exactly what you need.
So it's totally, you can create your own custom policies.
Last thing I'll point out here is there are differences
between policies and initiatives.
Policy is obviously a single policy,
virtual machines and virtual machine scale sets
should have encryption at host enabled as an example.
But an initiative is a collection of policies.
So this initiative has five policies.
This initiative has 34 policies, and we can go into it
and we can see the various policies
that are included in this one initiative.
So you can batch assign a group of related policies
if they're collected together and in this initiative.
Alright, that's all for now.
We do have this assignment to restrict locations.
So in the next video, I am going to go and try
to create a resource not in East US
or West US, one of those seven defined regions.
And we'll see it fail.


### 📺 Lesson: Testing Azure Policy


Instructor: So we have a Azure policy,
which is currently assigned,
that restricts resources to only certain locations.
As you can see, it is east-us, west-us,
and a few other, south, central, et cetera
for a specific resource group.
So if we were to go and just create a,
let's call it a virtual network,
that should count as a resource.
And remember, it's the az104demo resource group
that I restricted this to.
It doesn't really matter as long as it's created in east-us.
I'm going to, for the sake of this demo,
try to create this in Japan.
If I go Next, skip over some of these defaults,
it's gonna say running validation, and it should fail.
Validation failed. Click here to view details.
And if I click to view the details,
it says disallowed by policy.
Please speak to Scott if you require these regions.
So this is exactly what we wanted to happen, right?
We wanted resources in that resource group
not to work because of this.
Now, obviously, then if we were to go back
and change the region to one of the allowed regions,
so east-us was one of the allowed regions,
say a review and create,
then it passed all the validation.
So that's how Azure policy can be used
to implement restrictions and limitations
on your Azure account, that may be policies that you have
within your company or business.


### 📺 Lesson: Create a Custom Policy


Instructor: So we've seen that Microsoft Azure
has Azure policies that contain hundreds and hundreds
of built-in examples of policies.
And even the policies themselves are quite flexible
in that they support parameters
and that you can assign them to specific scopes.
And you basically, a lot of these things
are gonna be able to do what you need to do.
But it is possible that there's policies
that are here are not exactly what you need
and you need something a little bit different.
And so what you can do is you can create your own policy.
And that would be like a custom policy.
Now it's not entirely easy or straightforward.
Like, if we look at these policies,
I'm just gonna pick one randomly here.
We can see that the definitions
are ultimately JSON documents.
So this is obviously a language,
and you can, if you see a policy that you like
that you wanna modify, you can obviously copy this.
There's this Duplicate Definition button
or Export Definition button.
So you can copy this and then just modify
this to your needs as well.
If you want to create your own policy from scratch
there is obviously a template,
a sort of a minimum policy
JSON document.
So you've got properties,
display name, description, parameters,
and the if statement, and then what happens.
So we can try to create our own custom policy here.
And what we're gonna do is create a policy
that will require HTTPS encryption on storage accounts
as an example for a policy that you can create
and then you can import.
So we have to give this a name
and we can call this something useful, obviously.
"Deny storage."
"Deny unencrypted..."
And the description doesn't have to be
more than that either.
And we want this to be available,
since we're not dealing with resource tags at the moment,
this is for all resources.
Now we saw with the production where we are
basically allowing storage accounts to be created,
but it'll be audited,
We have this ability to have an effect
that can be a parameter.
So I'm just gonna paste in here an effect
that basically has the denial by default,
but we can also disable the effect
just for auditing purposes.
So we have the ability to turn off and on the effect
in the parameters part, okay?
Now the policy rule is that we want storage accounts,
we're gonna look at a specific field
within the storage account.
Now this is the trickiest bit because we're looking
for a specific setting within the storage account.
I'm gonna go back to, I'm gonna take this off screen,
go back to home, Create a resource.
Go into, Storage Account should be
one of the common ones, right?
No. Why not?
Go into Storage Account.
Now I'm not actually gonna create the resource.
All right.
But I am gonna go to the Review tab
and I'm gonna look at the template, 'cause the template
is going to contain the tags that I need to check.
So this is an ARM template, obviously.
And so to create the storage account
what I want is "supportsHttpsTrafficOnly" to be enabled.
So instead of this being, whatever the parameter is,
this has to be enabled.
So you see I grabbed the property
that I need from the ARM template.
Now for convenience here, I'm just going to paste in this.
So what we're saying here is,
if, and all of the following things must be true,
on storage accounts, for type storage accounts,
the storage account supports HTTPS traffic only
cannot be false or has to be true, right?
So the not equals.
Then I'm going to have an effect.
Now I could just say deny, effect deny.
But we want to use our parameter called effectType
to whatever the effect is, so that when we're
when we are signing this we can determine
whether this is enabled or audit only, okay?
So this is our custom policy.
Now I'm copying that.
Now we're gonna go into, back to the policy section.
I'm gonna not create this storage account.
Go back to Policy.
Go into Definitions.
Then I can create my own new definition.
The definition must be associated, obviously,
with this subscription.
Now I called this "Deny unencrypted storage accounts."
Create new.
And instead of taking this thing,
we're gonna copy what we created.
Which doesn't like this properties.
This is a storage related policy.
And the policy isn't really doing anything.
Like we don't have to give the policy permissions
in order for it to update existing resources.
It's simply going to deny the creation
of storage account that doesn't have HTTPS only selected.
So we'll hit the Save button on that.
Now, with the policy created,
let's assign this to our production resource group.
Azure being a little slow today.
And instead of flipping through this,
let's go, we got advanced scope.
Parameters.
"Only show parameters that need input or review."
So unchecking this, we can now see
that we can either activate the policy
but don't act on it, or we can force the denial,
which is what we're doing.
Which is great.
And say Create.
So with this custom policy,
we should not be able to create storage accounts
that do not say HTTPS only.
And that's how you create a custom policy.


### 📺 Lesson: Apply and manage tags on resources


Instructor: So in this video,
we're gonna be talking about resource tags.
Now oftentimes, when we're creating resource
for testing purposes,
we just skip over the tags part of the creation.
But tags can play an important role in managing resources
and being able to define and decide who's responsible,
how you account for that internally, and things like that.
So when you go into a resource,
there is a tags menu,
and this allows us to have a name value pair
that we can define that basically is metadata
that's attached to the resource.
We can also sometimes see tags
right off of the overview screen,
there is a a tag section and we can add tags there.
Now oftentimes, you're gonna want to set tags
that are basically internal values to your company,
something that is relevant to you.
This is not generally going to
affect your resource in Azure.
This is basically information about the resource.
So for instance, you could choose a tag
to define what environment this resource is part of.
And so this is part of the dev environment in my case
and I just define the tag environment.
It's a name that I came up with
and the value dev that's relevant to me.
I can also do things like accounting and billing.
So I can say billing code as a tag
and then have some sort of 59762 being some relevant number
for a billing code within my accounting department.
You could have contact details.
So if you want to know who is responsible for this resource,
if I have any questions, who should I call to say,
"Hey, we're having trouble with this resource, please help?"
You can put your contact name, contact email,
things like that.
These are all values that you come up with.
So there's really no definition,
but you can basically create your own set of tags
and say, Apply.
Now what can it be used for?
Now, we've seen previously,
we're talking about Azure policy,
you can set policies that require resources to have tags.
So if I go into policies, into definitions here,
I can look for policies that mention the term tags.
And for instance, we can require a tag
or we can modify a resource to add tags,
add tags to resources, add or replace tags,
subscription level tags,
all sorts of inherent tag from the subscription.
So all sorts of policies we can put into place.
And finally, when we're talking about budget and costs,
we can go into the cost analysis section of our subscription
and then we can run reports based on certain tags.
So if we wanted to only see what the costs are
for resources tagged as dev
and we can see the cost for resources tagged as production,
we can see these separately.
I'm in a demo account here, 30-day free trial.
There's no costs obviously.
But we can basically add as a filter,
tag,
and we can see...
We can choose from our pre-list of tags.
Now I just credit these tags
and so cost management hasn't been updated yet,
but in a few hours,
we'll be able to filter based on environment,
based on contact name, contact email, billing code,
and then these cost management reports
will then reflect only that tag.
So in this way, tags can be a way of basically slicing
and dicing your cost management reports
that will help you with your accounting internally
as well as of course, understanding for individual resources
who is responsible and who needs to be contacted
and other relevant information that is specific
to your environment.


### 📺 Lesson: Move Resources


Instructor: You might find yourself
having set up a resource in a particular region
wishing that you had chosen a different region
at some point.
And so what are the choices?
Can you, let's say you've got this virtual machine
to a point where you like it,
it's all got your applications installed,
you are pretty happy with it.
Do you then back it up
and then try to restore it to a new region?
How do you move a resource?
Well, luckily there is a way to do that.
So I've got these,
this virtual machine in all its related elements,
IP address, network security group, virtual network,
network interface card, and the virtual hard disk.
I can select all of the resources, go up to the three dots,
and you'll see it says Move.
Now I have three options.
One is to move it to another region, another subscription,
or to just another resource group.
So if I choose move to another region,
I get a choice of another region, obviously.
So let's say instead of East US,
I would prefer this be in Central.
And I can say Next,
and you'll see here that it's got five of my six resources.
So not every resource is able to be moved.
For instance, moving of disks isn't currently supported.
And so what's what can happen while moving the VM
the disk data is copied and recreated in the destination.
So Microsoft is taking care of this.
We can see in the documentation a list of resources
that are supported by this resource mover.
VMs, it does say disks, but it's actually copying the disk
and not moving it.
NICs, all of these other things.
What you'll not see is app services and other,
lots of other types of services that cannot be moved.
Function apps and things like that.
Whereas this is mostly infrastructure, VMs,
virtual networks, IP addresses and stuff and such.
There's also,
if we go more details under
Move operation support for resources,
we can see a list of all of the services
and you can see that you,
it cannot be moved during to a resource group.
It cannot be moved to subscription.
But API apps can be moved to another region
and there is a documentation for that.
So you'll have to check the list of services
and whether it's supported.
Some of them are, like you said,
spring apps can be moved between resource groups
and subscriptions, but it cannot be moved between regions.
All right, so if I was to proceed with this and say Next,
then this, these resources would be moved
from East US to Central.
I'm going to close that out.
Now we saw here we had other options.
So if we just wanted to move these resources
from this move demo resource group
and choose the production resource group,
then it's going to make sure
all of these resources are able to be moved.
This might take a few minutes.
So you'll see that it is able to validate
that these resources were able to be moved,
and if I click Next,
then it would move from one resource group to the other.
So all in all, moving resources between subscriptions,
resource groups, or regions is possible.
It does depend on the resource,
and you'll see that again, Microsoft has documentation
around what resources are allowed and which aren't.


### 📺 Lesson: Managing Policy by PowerShell


Instructor: So we've been playing with resource groups
and tags and policies in the Azure portal.
It's actually not a great practice
to be relying on the portal
on your day-to-day job.
You're gonna want to develop sets of scripts.
You're gonna have your own either PowerShell
or bash scripts that are going to do things for you.
Automation definitely the way to go.
And so it's more common for working administrators
to be working in a terminal
than to be always just doing things in the portal.
Portal's great for learning, I love it, it's visual,
it tells you exactly what it needs,
but when you get up to an advanced level
you're gonna want to play around at the terminal level.
And so I wanted to create a little quick video
where we assign a policy to a resource group
but we do everything in the terminal instead of the portal.
Now you could download PowerShell on your local
in the AZ module for that or CLI,
I'm just going to use the Cloud Shell to demonstrate this.
Now, if you've never created a Cloud Shell account
this >_ symbol is the Cloud Shell.
And I've never, in this particular tenant,
and this particular account subscription,
I've not yet worked with Cloud Shell.
So I'm gonna have to create the storage account here
for it before I do anything.
So I'm gonna pick Power Shell.
I do have to say show advanced settings.
I don't know why this is a thing
but it's going to create this in West Europe.
I'm gonna create a new cloudshell resource group.
But you see it needs storage account names
and file share names.
So I'm gonna have to come up with
some random number for these unique names.
And I don't know why you have to say
show advanced settings for that to happen.
All right, so let's create some storage here
for my Cloud Shell.
Alright, so now we can see a terminal right in our browser.
We can flip between the portal and the terminal.
I'm just gonna maximize the terminal here.
I'm gonna say clear.
So we're starting with a new screen here.
Alright, so what I said I'm gonna do
is I'm going to assign a policy to a resource group.
What I can demonstrate first here
is creating a resource group.
And actually as soon as I start typing,
you'll see that it's got an auto complete.
Very useful actually because I actually wanna create
a resource group.
So it says New- and then it's auto filling
AzResourceGroup with the name and the location.
All I have to do is hit the right arrow key.
Sure I'm focused on the window, right arrow key,
and you can see now it's accepted that default.
I'm going to call this resource group Staging_VMs.
And I'm gonna keep this, yes, in Central US,
and I'm gonna hit enter.
So now it's created me a brand new resource group
in centralus.
Now I need to put this resource group is an object
into a variable.
So I'm gonna say $rg = Get-AzResourceGroup.
And I still have to provide it the name Staging_VMs
and the location.
Too bad there's no auto fill on that.
So now I have a variable rg that is an object representation
of that resource group.
And so I can say rg.ResourceGroupName I believe.
And you see it comes back as Staging_VMs.
So this resource group has object
and has a number of properties
and I can retrieve them individually.
I'm gonna clear that.
Now, the next thing I want to do
is figure out which policy that I want to assign.
And for that I'm gonna go back to the portal for a second,
I'm gonna drag the screen down, go into Definitions.
Now I'm gonna pick one of these at random.
Let's say Audit resource location
matches resource group location.
So this is strange, but you may want your resources
in a resource group to be in the same physical location
as the resource group itself.
So what I'm gonna do with this
is I'm gonna copy the resource Id.
So when you go into the policy,
you can see it says Definition ID
and there's this sort of unique string
that's globally unique identifier.
I'm gonna say copy the clipboard.
And this is gonna be able to,
we're gonna be able to pull the definition based on that ID.
So we're gonna go back up to here and say definition,
which we're gonna use this variable called definition
and it's going to be Get-AzPolicyDefinition.
And there is an ID parameter.
So we can say Id and then paste this unique Id
that we just copied.
Close the quote on that.
And that's going to get the AzPolicyDefinition
into this variable.
So I can see definition, we can see we have an object
that represents the policy.
So we have the ResourceGroup and we have the definition.
So I'm gonna clear this
and we're going to see New-AzPolicyAssignment.
We can see that there's an auto fill here.
And I'm going to, the only variables I'm going to pass in,
I'm not gonna put the identity type,
but we are going to use, oops sign, okay?
We are going to use the Scope and the policy.
So the Scope is going to be based on the resource group.
So it's rg.ResourceId.
And the policy definition we have
in the definition variable.
All right, I'm not gonna specify the geographic location,
we do have to give this a name.
So I'm gonna call this RGLocationMatch
and we have to give it a display name,
so I'll call it right,
ResourceGroupMatches resources location.
So this is our PowerShell command
in order to assign this policy
that's represented by definition, object to this scope.
Now you'll see there's upcoming breaking changes.
We can ignore this.
We do have our assignment.
So the PolicyAssignmentId has got an Id.
So it successfully worked.
So if we minimize this window a little bit,
we should be able to go back to definitions
and to assignments.
And now we can see, if I refresh here, four assignments.
And the Resource group matches resource location
is attached to the Staging_VMs resource group
that we just created.
So you can use PowerShell or CLI
to do all the things you can do in the portal.
And in a way, it's safer if you do it in predefined script.
If you save these scripts into your source control
and you have this as your method
of managing Azure resources compared to the portal.


### 📺 Lesson: Subscriptions and Management Groups


Instructor: So, let's take a moment
to talk about a really important concept
when it comes to Azure accounts,
and that is the concept of subscriptions.
So, I know that it can be confusing.
Obviously you have your user account
that you'll used to log into the portal.
You have the concept of a tenant,
so that user account is part of an organization
that is an Entra tenant,
and in order to have some type of resources
that require billing, you need a subscription.
So, if we're in the portal, we can go under Subscriptions,
we can see that I have
a couple of subscriptions available to me.
Now, I'm currently running a filter,
and so we can only see a couple of the subscriptions
of the three that I have.
Now, subscriptions can actually be nested
under what are called management groups.
Now, I have a root group,
and so there's not actually any nesting going on.
If I go into Management groups,
I can see that I have my root group
and I have three subscriptions that I can choose from
that are part of this group.
Now, at any time, I can create another management group,
and I can nest other management groups
inside of it and/or also subscriptions.
So, I can give it a name and say Submit.
I now have a New Management Group underneath my root.
I can go into it,
and this is where I can basically add subscriptions
that are children of this New Management Group,
so if I said Add subscription,
I can choose one of my existing subscriptions
to move from the root under here.
Now, I'm not gonna do that
because it can be kind of disruptive,
so let's not play with that.
Now, I could also create a new subscription
to place inside of this management group.
If I go back to Subscriptions
and I say Add, I give it a name,
choose who's paying,
and this is where I get to choose
what type of billing plan that I want to create.
So, this Microsoft Azure plan
is one of the options here,
and as you can see,
I can choose from the New Management Group
associated with this tenant, this management group,
and who the owner is.
I can even create a budget
for the subscription as I'm creating it.
So, management groups
and subscriptions are ways of organizing your billing.
Instead of having one subscription across all your resources
of all your accounts,
you can create multiple subscriptions
that separate out billing to different individuals,
different departments, different clients,
and even arrange those subscriptions
under groupings called management groups.


### 📺 Lesson: HANDS-ON LABS: Subscriptions


[No transcript available for this lecture]


### 📺 Lesson: HANDS-ON LABS: Policy


[No transcript available for this lecture]

