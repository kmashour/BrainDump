
# Setting Cron Builds
There are multiple approaches for triggering a build.

So far we have used the manual approach by clicking the Build Now button.

Well, this method has its place.

Relying solely on it can feel as outdated as using a rotary dial phone in the age of smartphones.

It is functional, but there are definitely more efficient ways to do it.

So what are the options?

If you click here on configure.

And scroll down to build triggers.

We're going to see here multiple options available.

Let's first talk about build periodically.

This option allows us to run the pipeline, for example, once per hour or once per day.

For some use cases this would be a good option actually.

We might have long running jobs.

So there can be jobs that take several hours to complete.

And scheduling them to run overnight can be very efficient.

This way the results are ready by the morning when work resumes.

Optimizing the use of time and resources.

But even projects that are not actively updated but still need maintenance can benefit from this.

Periodic builds ensure that a project's pipeline remains functional.

This is crucial for identifying issues that may arise from changes in dependencies or the environment,

even when the project code has not been modified.

Okay, so we have definitely established that they are use cases for building a pipeline periodically.

But how can we configure this?

Well let's go ahead and click here on the checkbox.

And what will open up is this schedule.

So we need to specify how often we want to run this.

And we cannot use here a simple plain text and write something or run this job every Monday at 2 a.m.

or something like this.

This will not work.

Jenkins uses its own syntax here.

So if we click here on this question mark, we're going to get here a built in documentation for how

we can specify this.

And this is essentially the syntax of the cron.

So the name cron comes from the Greek word chronos which means time.

So we are configuring here using the syntax how often we want to run this.

And the syntax is relatively simple to understand.

It can look very scary in the beginning.

But I'm going to walk you through this and show you an example so there's no reason to freak out.

So we have here the minute, the hour, the day of the month.

Then we have the month, and then we have the day of the week.

So let's take a look at a practical example.

How can we run this pipeline using this Jenkins syntax every morning at 3 a.m. from Monday to Friday?

How can we do this?

Well, actually, all we have to do is start writing.

So what would be the minute?

So we need for the minute to select a value between 0 and 59, because it's going to be 3 a.m. in the

morning.

The value for the minute is going to be zero.

Next we need to specify the hour.

The hour is going to be three because it's a value between 0 and 23.

Perfect.

Let's add another space.

What's next?

We have the day of the month.

What we want to do in this case is we want to run this every day of the month.

We don't really care about the day of the month, so we don't want to specify each day individually.

And definitely we don't want to stick to a value between 1 and 31.

And in that case, what we can do here is use a star which essentially matches any value.

So whatever day of the month is going to be.

This is not going to matter.

The job is going to be executed perfect.

The next step is the monthly step.

Again, we don't really care about the month, so we can use a star here to match any month of the year.

Finally we have the date of the week, and we said here that we want to run this from Monday to Sunday.

In this context, zero is Sunday.

So the first day of the week is Monday.

So we're going to write here one.

But then how can we specify that we want to run this until Friday?

In this case we're going to use here this minus sign as explained here in the documentation or this

dash.

It's going to write 1-5.

And this will mean from Monday to Friday this job will be executed.

So let's click outside of this box and see what is happening.

And what you'll see here is a warning.

And it's saying here something about spreading the load.

So what is this.

The suggestion here is to use instead of zero.

Each.

So let's kind of replace here zero with h.

And I'll explain in a second what this means.

But as you can see this warning is now out.

So using H instead of a specific minute like we had previously, zero in the Jenkins cron syntax helps

distribute the load more evenly on the Jenkins infrastructure.

This is especially useful in environments where many jobs are scheduled to run at the same time.

This can happen more often than you think, as different people within the organization using the same

Jenkins instance can schedule their jobs at midnight, for example.

So then at midnight you have all these jobs starting all of a sudden at the exact same time and causing

a spike in the resource use.

And this can even block Jenkins.

So when scheduling jobs, the age character can be used as a placeholder for an actual number in the

cron syntax.

This causes the actual time of the job execution to vary, reducing the likelihood that many jobs start

at the same time, which could overload the Jenkins infrastructure.

Jenkins computes the h value based on the job name, ensuring that jobs run at a consistent time, but

they may start at, in this case, at a different minute each hour.

So as you can see here in our example, based on the job name, it informs us that it should have run

today, Monday at 356.

So it's still around 3:00, but it's 356, and that the next run will be tomorrow at 356.

And depending on how you have named this job, the value here for the minute will change.

If we revert this back to using zero here, you're going to see here that it starts at exactly 3 a.m.

in the morning every time.

So this is the main difference.

And every job will have here.

Then a different value even if the exact same syntax is being used here.

So multiple pipelines using this exact schedule will be run differently.

So the Jenkins server will not be overloaded.

So once we have configured this all we have to do here is click on save and just wait essentially for

the next day.

And then the job will be automatically triggered by Jenkins without us doing anything.

Going back to the configuration and taking a look here at the build triggers, if we think about this.

This doesn't really help us, right?

Because, for example, today we may be doing 20 changes or 30 changes, and we want to execute a pipeline

every time.

And actually if we click here on this question mark, not under the schedule but under this build periodically

feature, Jenkins will even tell us that this is not ideal for continuously building software projects.

So while there are use cases for our use case with this pipeline, we are far from ideal if we only

build once per day.

It is not often enough as we don't get immediate feedback.

Now of course, we could configure this schedule to run every hour, every half an hour, every 15 minutes,

even every minute if we want.

But if we build too often, we are actually wasting resources if there are no changes made to the code.

So for that reason.

Building this project more often doesn't really help us.

But still, it is an important feature you should be aware of, and I'm going to leave it enabled for

now.


# Github Hook and Git Polling 
So we have established that building this pipeline periodically is not really what we need.

What we actually want is to trigger the pipeline once we have made some changes.

So we want to replace the manual action of us going and clicking on build now.

So we want to make the changes and then the pipeline should magically start.

In our setup, we have used Git hub to store our code.

So when we make a change, GitHub knows.

But the problem is that Jenkins doesn't know.

To synchronize Jenkins with these changes, GitHub needs to notify Jenkins about the change.

However, this setting involves some configuration, and the Jenkins server needs to be publicly accessible

so that GitHub can reach it.

This poses a security risk and is a bit more complicated to configure.

Therefore, I've decided to leave it out of this course.

However, if you wish to implement this, check the resources folder for a tutorial.

For our use case, we're going to implement the second best option, which is typically known as poll

SCM or commonly referred to as git polling.

You're going to see here this option here poll SCM.

So what is git pulling?

Since Jenkins does not automatically detect changes in a repository, it needs to periodically check

or poll GitHub to see if there are any new changes.

This process is known as polling.

This approach allows us to trigger the pipeline only when new commits are detected in the GitHub repository.

Moreover, the setup is straightforward.

Let me show you.

So let's go ahead and enable here Paul SCM.

And again we're going to see here this schedule.

So if we are not sure about schedule we'll have to do is expand this.

And we're going to see that this uses the exact same syntax as here with building periodically.

Now, we're not going to build this project periodically.

We're only going to check if they are changes.

And the question is, how often do we want to check for changes in our git repository.

And we have here also some examples.

If you don't want to start really from scratch, there are some good examples.

And one of the examples that are listed here is for example.

Is checking every 15 minutes.

You're going to see here we have this example syntax here where we're checking for changes every 15

minutes.

So it's going to copy this here.

Paste it.

So once we click outside of the box, Jenkins is going to tell us when this was supposed to run last

and when it's gonna run next.

You're going to see here 926 this is when it was supposed to run last.

And then if we wait until 941, then it's gonna run again.

It's gonna check the git repository for changes.

Now, 15 minutes can be really a long wait.

So if we make a change right now, we still need to wait quite a bit until Jenkins is gonna check for

that change and then decide to trigger the pipeline.

So we want to have this value a bit lower.

Now.

For example, let's say we want to check every minute because we are so impatient and we don't really

want to wait so much.

So we could change here the value 15 to simply one.

And this is when people really are confused about this, because this will now not run every minute,

but it will actually run every hour.

So if you look here, you're going to see here it was supposed to run at 856, and it's going to run

again at 956.

Sometimes this Jenkins syntax can be a bit tricky and inconsistent for this particular edge case.

So how can we get this to run every minute.

Well in that case all we need to do is replace h forward slash one with another star.

So this will match every minute.

Every hour, every day of the month and so on.

You get the point.

So this check will be done every minute.

Let's go ahead and click on save.

And now nothing will happen.

But what you should see here is this additional menu item here git pulling log.

So if we think we have some issues with this, all we have to do is click on this and we're going to

see what's going on.

Initially, you're going to see that polling has not run yet.

So we need to wait a few seconds for this to run.

So we need to wait at least one minute to see something here.

I'm going to go back, wait one minute and come back to this.

All right, so one minute is over.

Let's check it again.

And what we see here is Jenkins checking against our git repository to see if there are any changes.

And what you'll see here right at the end it says no changes.

So now with this configuration, every minute Jenkins will go to the git repository and check if there

are any changes there.

If there are no changes, nothing will happen.

The pipeline is not going to be triggered, but if there are changes, the pipeline will be triggered.

So let's go ahead and make one change and see how this works.

So now from our project, it really doesn't matter what we change, we can change some project files.

We can change this Jenkins file.

We can even simply add a new file and the pipeline should be triggered.

So let's make a small change to the Jenkins file.

But as I said, it doesn't really matter what we put here.

We're gonna use here the echo message and right here the message small change.

And I'm going to go ahead and commit this message and push this change to the repository.

Let's go back to our Jenkins pipeline.

And I'm not going to do anything.

I'm just going to wait for a few seconds.

And what we should notice right here in the build history, a build being triggered.

And what do we see here?

It says pending.

And now in a few seconds, the build should start.

So this is how this feature works.

It only starts the pipeline if there is a change, but it checks every single minute.

If there is a change.

And we can see here if we're looking at the logs, let's click on the logs and go right here on top.

We're going to see here.

Started by an SQM change.

What this means is that the reason why this pipeline is running is because there was an SQM change.

There was a change in our git repository.

That's the reason for triggering this build.

If you're looking here at one of our previous builds.

You're going to see here started by user and then the username.

That's the main difference.

You can also check here.

The git polling, but in the meantime this has executed once again.

So we would have checked this log immediately after the pipeline has been started.

We should have seen here that there are some changes, but now this gets overridden every time.

So if you want to actually see this in practice, maybe change it to a different value so that it doesn't

run every minute.

Perfect.

So in a nutshell, this is how we can ensure that the pipeline gets triggered almost automatically when

we're making changes to the git repository.
![[Pasted image 20250530155240.png]]
![[Pasted image 20250530155251.png]]