---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - azure
  - az-104
course: "AZ-104: Microsoft Azure Administrator"
instructor: "Scott Duffy"
module_id: "01"
title: "Module 01: Course Introduction, Budgeting, and Admin Tooling"
source: "Udemy - AZ-104 Microsoft Azure Administrator (Scott Duffy)"
tags:
  - azure/az-104
  - status/raw
---

# Module 01: Course Introduction, Budgeting, and Admin Tooling

**Instructor:** Scott Duffy  
**Course:** AZ-104 Microsoft Azure Administrator  
**Key Topics:** AZ-104 Certification Guide, Azure Free Account, Cost Budgeting, PowerShell Core, Az Module, Azure CLI  
**Line Range:** Lines 1 – 649 of master transcript  

---

## 📋 Module Overview & Cleaned Transcripts



## 🏛️ Section: Microsoft Azure Administrator Certification Course



### 📺 Lesson: Welcome to Azure Administrator Certification Course


Thank you so much for signing up for this course on the AZ 104 Microsoft Azure Administrator exam.
My name is Scott Duffy.
This course covers all of the requirements of the AZ 104 exam.
If you take and pass this exam, you'll qualify for Microsoft certification as an Azure Administrator
at the associate level.
So as you can see, this course does cover all of the requirements and you're signed up for it.
So that's great.
This is not a short course.
So I want to set the expectation that you're not going to be able to sit down and watch this course
in a day or in a weekend, and then go and take the test the following Monday.
This is going to require some study.
I'm expecting you to go off into the Azure portal, do some of the work yourself, do some of the assignments,
and it's going to take some time to prepare for this test.
There's also a practice exam at the end of this course that you can go and test your knowledge against
some practice questions.
So you're going to go through this course.
I do generally go through the requirements of the exam on a section by section basis.
Let's switch over to the Microsoft landing page.
If you enter the key word AZ hyphen 104 into your favorite search engine, the first result should be
the Microsoft Learn website that takes you to the landing page for this certification.
On this page, you're going to see the time that the exam was last updated.
And so just go and check to make sure that it hasn't been recently updated, or it won't be updated
before you take the test.
I do try to keep this course up to date with the latest.
And luckily Microsoft does not update this exam A super frequently anymore.
So check the date on the landing page for Microsoft.
Learn to make sure that there's no changes on the horizon.
Now this course is based on Azure administration.
And so we're talking about some of the technical aspects of Azure.
It is expected that you do have a bit of a technical background.
I'm not going to go over the fundamental basics of what a network is or how the IP addressing system
works and things like that.
We will talk about the cloud and how virtual networks work, how the Cidr notation is within Microsoft
Azure for specifying ranges of IP addresses, etc., but not the basic fundamentals.
We're going to talk about virtual networks, storage.
Compute identity is a big feature of Azure security and governance.
And they're expecting that you are either an administrator or looking to be an administrator.
And so you're you're looking to work in those roles of delivering solutions to clients.
Microsoft does not just contain the portal.
There's also some scripting elements PowerShell and CLI.
We're going to cover in this course the way you can predefine and configure resources using templates
and the entry ID tool for identity.
So I'm on this page I'm going to scroll down a little bit.
They've changed this page last couple of years.
So some of the stuff has changed.
This is where you can book the exam.
So you'll see it saying schedule through Pearson Vue and you can schedule the exam.
It's offered not only in English but in a number of languages.
So if that's more comfortable for you, you may want to try that.
The price of the exam does vary based on your location, so it's 165 USD.
Price hasn't changed in a few years, but if you're based in different location, for instance, in
Europe you are going to see a different price.
A lot of this is based on the exchange rate, which is fluctuating.
Of course, this exam does last for 12 months and you do have to renew it after 12 months.
But it's very easy to renew.
You do it online, it doesn't cost anything and it's can be done in 15 or 20 minutes.
So don't be afraid of that.
Now this certification resources, the exam study guide is where we're going to find out all of the
details of the exam.
What is covered.
We go down under the skills measures section.
We're going to see who again who this exam is for.
That's a bit of a repeat but how the exam is divided.
Okay.
Under skills at a glance you get the percentage breakdowns between identities storage, compute, virtual
networking, and the monitoring and maintenance of Azure resources.
So there is between ten, 20, 25% to these different sections.
Like I said, this course is broken down section by section and topic by topic.
So you will find videos in this course for each of these in terms of users, external users, roles,
uh, locks, groups, things like that.
So my recommendation is just to follow the course, uh, section by section stop at various points.
Go and test it yourself.
If you're interested in creating some users and groups in entra, go into Azure and do that and see
it with your own eyes.
Make the mistakes, troubleshoot it, fix it, make it work, and continue on.
But Scott, what if I don't have an Azure account?
I can help you with that.
We'll talk about how to get a free account in the next video.


### 📺 Lesson: How to Get an Azure Free Account or Student Account


I don't believe that you can pass
without any hands-on experience.
And for that, you're gonna need an Azure account.
Now Azure does provide a free account
with some limited privileges if you need one to pass,
or if you already have access to an Azure account
through your work or some other means,
then you can use that account.
If you do already have an account set up and ready to go,
you can skip the rest of this video
and move on to the next section.
The rest of this video,
we're gonna be talking about the Azure free account,
the limitations on that and how to get one.
Now go to your favorite search engine,
in this case, it's Google.
I entered the word Azure free and hit Enter.
Now the first link that comes up is the Microsoft website,
azure.microsoft.com.
If I click on it, you can see the advertisement
for the Microsoft Azure free account.
Now scrolling down a little bit,
we can look at what the limitations are
'cause it's very important to keep in mind
while you're studying when those expiry dates are.
Now Microsoft does things a little differently than AWS.
You get 30 days of free usage of Azure with a $200 credit.
Now if you use up that $200 within the 30 days,
then you're gonna have your services shut off.
Or when the 30 days runs out
and you haven't used your credit,
you're gonna basically lose that credit.
And on top of that, there are 12 months of free services
included in the free account.
And these services switch over
to paid services after 12 months.
And there are also always free services.
Scrolling down a little bit more,
we can look at the different services that are available.
So outside of the $200 credit in the first 30 days,
you can also get up to two virtual machines of a small size
for up to 12 months.
So you can still continue to practice
even after the 30 days is over.
You get some disk space, some blob storage,
file storage, et cetera.
Scroll back to the top and we're gonna say start free.
Now in order to access Azure,
you do need a Microsoft account.
I can use, this is the account I already have for Azure,
but I can't get a second free account.
Once you've used it, you can't have it again.
So I'm gonna say Use another account.
Now if you have another Microsoft valid email address
like Hotmail, Outlook or something else,
you can certainly use that one.
Or if you don't have one
and you want to use a different email address, you can.
It says create one and you can say create an account.
You can provide your current email address,
whether it's your personal or work address,
or you can even create a new address.
So let's say we got past this creating an account aspect.
Now to create an Azure account,
you do need to provide some information,
you need to provide your name and phone number,
you need to prove your identification by phone,
you are also gonna have to provide a credit card
as validation and sign the agreement.
Now Microsoft does promise
that there is no automatic charges
at the end of the 30 days.
So your services will shut off
if you use up your credit or if your 30 days has expired,
and they're not gonna start magically billing
your credit card.
But you do need a credit card in order to create an account.
Part of the reason of this is so that they can restrict you
to a single account per person.
So you can't create an unlimited number of free accounts.
Now I should mention that if you are a student
studying at an accredited school,
you can get a free Azure account
that does not require a credit card.
Now the number of credits you get $100
is less than for a regular free account.
And some of the free things that are included
are a little bit less.
So go to azure.microsoft.com/free/students
and you can get yourself a student account
with no credit card required if you qualify.
Once you've signed up for Azure,
you're gonna wanna log into the portal.
Now the central URL for the Azure portal
is portal.azure.com.
That is where you're gonna go every time you wanna log
into Azure and do something with it.
Once you're logged in,
you're gonna see a homepage similar to this.
You're gonna have some very frequent services across the top
and some other options,
including documentation and other learning resources
along the bottom.
We're gonna get into all of these later in this course.
But for now, if you're able to get this far,
then congratulations, you've successfully created
an Azure account.


## 🏛️ Section: Azure Concepts



### 📺 Lesson: Assignment: Log in to Azure


[No transcript available for this lecture]


## 🏛️ Section: PowerShell and CLI



### 📺 Lesson: Setting a Budget


Now, one thing
that people worry about, justifiably,
is cost overruns while learning
or playing around in the cloud.
It is quite possible to go into the cloud,
create a resource, such as a virtual machine,
and then start racking up $1 per hour of charges,
and then you've totally forgotten about it,
you went off to go for dinner, you go to sleep,
you wake up the next day,
and somehow you've racked up $25 of charges,
and it can be even worse.
There are some resources,
such as Cosmos DB,
which can be quite expensive at the higher end.
So in this video, we're gonna talk about
the concept of budgets.
And if you are playing around
with a pay-as-you-go subscription
and it's your own money that's on the line,
I definitely recommend that you pay attention to budgets.
It's also going to be on the test,
and if you have an Azure free account,
this might be less useful
because obviously it is coming out of credits
that Microsoft is giving to you.
But again, it's useful to know
what a concept of a budget is in Azure.
So to get there, we're gonna go into the Subscriptions tab.
You can see on my left here,
I have subscriptions permanently tabbed to my menu.
You can also go under All services
and search for subscriptions.
I'm gonna choose my pay-as-you-go subscription.
Now, again, if you have a free plan,
then this is gonna be kind of different
and kind of irrelevant
because you can't create a budget
for the free plan I don't think.
So we're under the subscription,
and we can see my spending rate's very low right now,
20 cents currently.
And Microsoft is estimating
that by the end of the month
I'll have racked up 23 cents.
So I've definitely closed this account down
to the minimum that I can get away with spending
while being able to keep my files here.
Now, this hasn't always been true,
but right now my account is at a very low level.
But let's say for the sake of argument,
I do wanna be notified if my spending reaches $50.
So I go under Subscription and I go under Budgets.
I don't have a budget currently.
I'm going to add a budget.
Now, the first thing to keep in mind
is that you can create a budget,
it can be at a scope.
So let's say you want to create a budget
at a resource group level,
then you can add a filter
to filter down beyond this scope
into specific resource groups.
So let's say I want to say filter
based on ResourceGroupName,
and I want to know that for this particular resource group.
So now I can have a budget down to the resource group level.
You saw also there were filters based on product, right?
Based on publisher of the resource.
If I had reservations, VM reservations,
things like that.
Tags even.
So you can create budgets
based on any number of things.
Give our budget a name.
So I'm gonna say SpendingTooMuch.
And at what frequency we want to measure this budget?
So you can see by default there's a monthly frequency.
We can choose to do it a quarterly or annual frequency.
I think monthly is fine for now.
Now, budgets have both a creation date
and an expiration date.
So this budget is going to last me
for two years by default.
I can change that to say this budget's good for four years.
Now I said I wanted to let be alerted
when the budget hit $50,
so I can enter the amount
in the currency that I work with.
I can also see historically over the months
what my spending has been against this account.
Like I said, I keep this pretty low.
I'm gonna say Next.
Now, the question is, then,
what happens when the budget hits $50?
Now, you might think that the budget
will then stop spending
once it hits $50,
that the charges will stop accumulating.
And that is actually not the way it works.
The way that it works is it lets you know.
So there is no automated actions that happen
other than sending out alerts.
Now, you can have multiple alerts
for this one budget.
So for instance, when the actual budget
hits 100% of the budget, $50,
then I can want something to happen.
There's these things called action groups,
and this action group will send me an SMS message,
in this case,
in terms of notifying me.
I can also let me know
when it's forecasted to reach $50 for the month.
So let's say we are two days into the month,
and I've just kicked off a virtual machine
that costs $1 an hour,
the next time the forecast run,
and it's not real time,
but in a few hours, the forecast will be recalculated
and it will notify me even if it hasn't currently hit $50.
I can say I want to be texted
even if the forecast hits $50.
You might also want to be notified
when half of your budget has been reached.
So that could be an unusual situation.
And so you can have different alerts
at different percentages
based on either the actual or the forecast.
Now, there is a mandatory email
that you have to add here.
And then you can set which language
you want to be notified in.
It doesn't take into effect right away,
it takes a few hours for the evaluation to happen.
All right, so then I can say Create.
So now I have a budget in place
that will notify me when my budget hits the $50.
It'll also notify me when it's forecasted to hit $50
or when 50% of the budget has been reached.
And like I said, it's not a real-time evaluation,
so it's not gonna notify me within minutes
or seconds of reaching $50,
and it's not going to stop any of the jobs
or stop any of the VMs.
I can mention that it is possible
to have your action groups
to actually do things.
So let's go under Next.
And if I go under Manage action group,
right now I have this email and SMS message set up,
but there are also ways of doing action groups.
Let's call this newactiongroup.
I can call this Stop all VMs, right?
And there's no, necessarily, no notifications
that need to go out.
You can not have them.
But you can have Azure functions that run automations,
some type of web hook that calls,
that could be a logic app
or some external thing that happens.
So you can have automations that run
once your budget is reached,
or you can just have it send you a text, or an SMS,
or an email, or something like that.

