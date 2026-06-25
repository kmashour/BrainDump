-: Hello and welcome to this section

on storage in Kubernetes.

This is Mumshad Mannambeth, and we are going through

the Certified Kubernetes Administrators course.

In this section, we look at

the various storage related concepts,

such as persistent volumes, persistent volume claims,

access modes, and how to configure applications

with persistent storage.

There are so many different storage options out there.

And depending on your environment, the options may vary.

However, looking at all of those options

is out of scope for this course.

In this course, our focus

is on the Kubernetes side of storage.

Once you get that,

you should be able to relate that knowledge

to implement any third party storage solutions out there.

So let's get started.



Let us now look at storage in Kubernetes to understand storage in container orchestration tools like

Kubernetes.

It is important to first understand how storage works with containers.

Understanding how storage works with Docker first and getting all the basics right will later make it

so much easier to understand how it works in Kubernetes.

When it comes to storage in Docker, there are two concepts you must know about storage drivers and

volume driver plugins.

In the upcoming video, we will discuss about storage drivers.

It's something that we've discussed in the Docker course, so if you have gone through that already,

feel free to skip this video or you may choose to stay and refresh your memory.

Once done, we will talk about volume drivers.

In this lecture we are going to talk about Docker storage drivers and file systems.

We're going to see where and how Docker stores data and how it manages file systems of the containers.

Let us start with how Docker stores data on the local file system.

When you install Docker on a system, it creates this folder structure.

At var lib docker you have multiple folders under it called aufs, containers, image volumes, etc.

this is where Docker stores all its data by default.

When I say data, I mean files related to images and containers running on the Docker host.

For example, all files related to containers are stored under the containers folder, and the files

related to images are stored under the image folder.

Any volumes created by the Docker containers are created under the volumes folder.

Well, don't worry about that for now.

We will come back to that in a bit.

For now, let's just understand where Docker stores its files and in what format.

So how exactly does Docker store the files of an image and a container?

To understand that, we need to understand Dockers layered architecture.

Let's quickly recap something we learned when Docker builds images, it builds these in a layered architecture.

Each line of instruction in the Docker file creates a new layer in the Docker image, with just the

changes from the previous layer.

For example, the first layer is a base ubuntu distribution, followed by the second instruction that

creates a second layer which installs all the apt packages, and then the third instruction creates

a third layer, which with the Python packages, followed by the fourth layer that copies the source

code over, and then finally the fifth layer that updates the entry point of the image.

Since each layer only stores the changes from the previous layer, it is reflected in the size as well.

If you look at the base ubuntu image, it is around 120MB in size.

The APT packages that are installed is around 300 MB and then the remaining layers are small.

To understand the advantages of this layered architecture, let's consider a second application.

This application has a different Docker file, but is very similar to our first application.

As in, it uses the same base image as ubuntu.

Uses the same Python and Flask dependencies, but uses a different source code to create a different

application.

And so a different entry point as well.

When I run the docker build command to build a new image for this application, since the first three

layers of both the applications are the same, Docker is not going to build the first three layers.

Instead, it reuses the same three layers it built for the first application from the cache, and only

creates the last two layers with the new sources and the new entry point.

This way Docker builds images faster and efficiently saves disk space.

This is also applicable if you were to update your application code whenever you update your application

code, such as the app dot Pi.

In this case, Docker simply reuses all the previous layers from cache and rebuilds the application

image by updating the latest source code, thus saving us a lot of time during rebuilds and updates.

Let's rearrange the layers bottom up so we can understand it better.

At the bottom we have the base ubuntu layer, then the packages, then the dependencies, and then the

source code of the application and then the entry point.

All of these layers are created when we run the docker build command to form the final Docker image.

So all of these are the Docker image layers.

Once the build is complete, you cannot modify the contents of these layers.

And so they are read only.

And you can only modify them by initiating a new build.

When you run a container based off of this image using the docker run command, Docker creates a container

based off of these layers and creates a new writable layer on top of the image layer.

The writable layer is used to store data created by the container, such as log files written by the

applications.

Any temporary files generated by the container, or just any file modified by the user on that container.

The life of this layer, though, is only as long as the container is alive.

When the container is destroyed, this layer and all of the changes stored in it are also destroyed.

Remember that the same image layer is shared by all containers created using this image.

If I were to log in to the newly created container and say create a new file called temp dot txt, it

will create that file in the container layer which is read and write.

We just said that the files in the image layer are read only, meaning you cannot edit anything in those

layers.

Let's take an example of our application code.

Since we bake our code into the image, the code is part of the image layer and as such is read only

after running a container.

What if I wish to modify the source code to say, test a change?

Remember, the same image layer may be shared between multiple containers created from this image.

So does it mean that I cannot modify this file inside the container.

No, I can still modify this file, but before I save the modified file, Docker automatically creates

a copy of the file in the read write layer, and I will then be modifying a different version of the

file in the read write layer.

All future modifications will be done on this copy of the file in the read write layer.

This is called copy on write mechanism.

The image layer being read only just means that the files in these layers will not be modified in the

image itself.

So the image will remain the same all the time until you rebuild the image using the docker build command.

What happens when we get rid of the container?

All of the data that was stored in the container layer also gets deleted.

The change we made to the App.py and the new temp file we created will also get removed.

So what if we wish to persist this data.

For example, if we were working with a database and we would like to preserve the data created by the

container, we could add a persistent volume to the container.

To do this, first create a volume using the Docker volume create command.

So when I run the Docker volume create data underscore volume command, it creates a folder called data

underscore volume under the var lib docker volumes directory.

Then when I run the docker container using the docker run command, I could mount this volume inside

the Docker containers rewrite layer using the dash v option like this.

So I would do a docker run dash v, then specify my newly created volume name, followed by a colon

and the location inside my container, which is the default location where MySQL stores data.

And that is var lib MySQL.

And then the image name MySQL.

This will create a new container and mount the data volume we created into var lib MySQL folder inside

the container.

So all data written by the database is in fact stored on the volume created on the docker host.

Even if the container is destroyed, the data is still active.

Now what if you didn't run the Docker volume?

Create command to create the volume before the docker run command.

For example, if I run the docker run command to create a new instance of MySQL container with the volume

data underscore volume two, which I have not created yet, Docker will automatically create a volume

named data, underscore volume two and mount it to the container.

You should be able to see all these volumes if you list the contents of the var lib docker volumes folder.

This is called volume mounting as we are mounting a volume created by Docker under the var lib docker

volumes folder.

But what if we had our data already at another location?

For example, let's say we have some external storage on the docker host at forward slash data, and

we would like to store database data on that volume and not in the default var lib docker volumes folder.

In that case we would run a container using the command docker run dash v, but in this case we will

provide the complete path to the folder we would like to mount that is forward slash data or slash MySQL.

And so it will create a container and mount the folder to the container.

This is called bind mounting.

So there are two types of mounts a volume mounting and a bind mount.

Volume mount mounts a volume from the volumes directory and bind mount mounts a directory from any location

on the docker host.

One final point to note before I let you go using the dash V is an old style.

The new way is to use dash mount option.

The dash dash mount is the preferred way, as it is more verbose, so you have to specify each parameter

in a key equals value format.

For example, the previous command can be written with the dash mount option as this using the type,

source and target options.

The type in this case is bind.

The source is the location on my host, and target is the location on my container.

So who is responsible for doing all of these operations?

Maintaining the layered architecture, creating a writable layer, moving files across layers to enable

copy and write, etc..

It's the storage drivers.

So Docker uses storage drivers to enable layered architecture.

Some of the common storage drivers are UFS btrfs, DFS Device Mapper, Overlay and Overlay.

Two.

The selection of the storage driver depends on the underlying OS being used.

For example, with ubuntu, the default storage driver is UFS, whereas the storage driver is not available

on other operating systems like fedora or CentOS.

In that case, Device Mapper may be a better option.

Docker will choose the best storage driver available automatically based on the operating system.

The different storage drivers also provide different performance and stability characteristics, so

you may want to choose one that fits the needs of your application and your organization.

If you would like to read more on any of these storage drivers, please refer to the links in the attached

documentation.

For now, that is all from the Docker architecture concepts.

Okay, so in the previous lecture we discussed about storage drivers.

Storage drivers help manage storage on images and containers.

We also briefly touched upon volumes in the previous lecture.

We learned that if you want to persist storage, you must create volumes.

Remember that volumes are not handled by storage drivers.

Volumes are handled by volume driver plugins.

The default volume driver plugin is local.

The local volume plugin helps create a volume on the Docker host and store its data under the var lib

docker volumes directory.

There are many other volume driver plugins that allow you to create a volume on third party solutions

like Azure File Storage, convoy, DigitalOcean, Block Storage Locker, Google Compute Persistent Disks,

Glusterfs, NetApp X-ray Portworx, and VMware vSphere storage.

These are just a few of the many.

Some of these volume drivers support different storage providers.

For instance, X-ray storage driver can be used to provision storage on AWS, EBS, S3, EMC storage

arrays like Isilon and Scaleio, or Google Persistent Disk or OpenStack cinder.

When you run a Docker container, you can choose to use a specific volume driver, such as the X-ray

EBS, to provision a volume from Amazon EBS.

This will create a container and attach a volume from the AWS cloud.

When the container exits, your data is saved in the cloud.

In the upcoming lectures, we will see more about volumes in Kubernetes.

Let us now look at the container storage interface.

In the past, Kubernetes used container D alone as the container runtime engine, and all the code to

work with container D was embedded within the Kubernetes source code, with other container runtimes

coming in, such as rocket and Cri-o.

It was important to open up and extend support to work with different container runtimes, and not be

dependent on the Kubernetes source code.

And that's how Container Runtime Interface came to be.

The container runtime interface is a standard that defines how an orchestration solution like Kubernetes

would communicate with container runtimes like Docker.

So in the future, if any new container runtime interface is developed, they can simply follow the

CRI standards, and that new container runtime would work with Kubernetes without really having to work

with Kubernetes team of developers, or touch the Kubernetes source code.

Similarly, as we saw in the networking lectures to extend support for different networking solutions,

the container networking interface was introduced now.

Any new networking vendors could simply develop their plugin based on the CNI standards and make their

solution work with Kubernetes.

And as you can guess, the container storage interface was developed to support multiple storage solutions

with CSI.

You can now write your own drivers for your own storage to work with.

Kubernetes.

Portworx.

Amazon EBS.

Azure disk.

Dell EMC Isilon Powermax.

Unity.

Xtremio NetApp.

Nutanix HPE Hitachi.

Pure Storage.

Everyone's got their own CSI drivers.

Note that CSI is not a Kubernetes specific standard.

It is meant to be a universal standard and if implemented, allows any container orchestration tool

to work with any storage vendor with a supported plugin.

Currently, Kubernetes, Cloud Foundry, and Mesos are on board with CSI.

So here's what the CSI kind of looks like.

It defines a set of rpcs, or remote procedure calls that will be called by the container orchestrator,

and these must be implemented by the storage drivers.

For example, CSI says that when a pod is created and requires a volume, the container orchestrator

in this case Kubernetes should call the create volume RPC and pass a set of details such as the volume

name.

The storage driver should implement this RPC and handle that request, and provision a new volume on

the storage array and return the results of the operation.

Similarly, container orchestrator should call the delete volume RPC when a volume is to be deleted,

and the storage driver should implement the code to decommission the volume from the array when that

call is made.

And the specification details exactly what parameters should be sent by the caller, what should be

received by the solution, and what error codes should be exchanged.

If you're interested, you can view all these details in the CSI specification on GitHub at this URL.

So that's about it for now.

About container storage interface.

I'll see you in the next lecture.



Before we head into persistent volumes, let us start with volumes in Kubernetes.

Let us look at volumes in Docker first.

Docker containers are meant to be transient in nature, which means they are meant to last only for

a short period of time.

They are called upon when required to process data and destroyed once finished.

The same is true for the data within the container.

The data is destroyed along with the container.

To persist data processed by the containers, we attach a volume to the containers.

When they are created.

The data processed by the container is now placed in this volume, thereby retaining it permanently.

Even if the container is deleted, the data generated or processed by it remains.

So how does that work in the Kubernetes world?

Just as in Docker, the pods created in Kubernetes are transient in nature.

When a pod is created to process data and then deleted the data processed by it gets deleted as well.

For this, we attach a volume to the pod.

The data generated by the pod is now stored in the volume, and even after the pod is deleted, the

data remains.

Let's look at a simple implementation of volumes.

We have a single node Kubernetes cluster.

We create a simple pod that generates a random number between 1 and 100, and writes that to a file

at slash opt out.

It then gets deleted along with the random number.

To retain the number generated by the pod, we create a volume, and a volume needs a storage.

When you create a volume, you can choose to configure its storage in different ways.

We will look at the various options in a bit, but for now we will simply configure it to use a directory

on the host.

In this case, I specify a path forward slash data on the host.

This way any files created in the volume would be stored in the directory data on my node.

Once the volume is created to access it from a container, we mount the volume to a directory inside

the container.

We use the volume mounts field in each container to mount the data volume to the directory.

Slash opt within the container.

The random number will now be written to opt mount inside the container, which happens to be on the

data volume, which is in fact the data directory on the host.

When the pod gets deleted, the file with the random number still lives on the host.

Let's take a step back and look at the volume storage options.

We just used the host path option to configure a directory on the host as storage space for the volume.

Now that works fine on a single node.

However, it is not recommended for use in a multi node cluster.

This is because the pods would use the slash data directory on all the nodes and expect all of them

to be the same and have the same data.

Since they are on different servers, they are in fact not the same.

Unless you configure some kind of external replicated cluster storage solution.

Kubernetes supports several types of different storage solutions such as NFS cluster, NFS, Flocker,

Fibre Channel, Cephfs, Scaleio, or public cloud solutions like AWS, EBS, Azure Disk or File or

Google's Persistent Disk.

For example, to configure an AWS Elastic Block Store volume as the storage option for the volume,

we replace Hostpath field of the volume with the AWS Elastic Block Store field, along with the volume,

ID and filesystem type.

The volume storage will now be on AWS EBS.

Well, that's it about volumes in Kubernetes.

We will now head over to discuss persistent volumes.

Next.In the last lecture, we learned about volumes.

Now we will discuss persistent volumes in Kubernetes.

When we created volumes in the previous section, we configured volumes within the pod definition file.

So every configuration information required to configure storage for the volume goes within the pod

definition file.

Now when you have a large environment with a lot of users deploying a lot of pods, the users would

have to configure storage every time.

For each pod, whatever storage solution is used, the users who deploys the pods would have to configure

that on all pod definition files in his environment.

Every time a change is to be made, the user would have to make them on all of his pods.

Instead, you would like to manage storage more centrally.

You would like it to be configured in a way that an administrator can create a large pool of storage,

and then have users carve out pieces from it as required.

That is where persistent volumes can help us.

A persistent volume is a cluster wide pool of storage volumes configured by an administrator, to be

used by users deploying applications on the cluster.

The users can now select storage from this pool using persistent volume claims.

Let us now create a persistent volume.

We start with the base template and update the API version.

Set the kind to persistent volume and name it PV Vol one.

Under the specs section, specify the access modes.

Access mode defines how a volume should be mounted on the hosts, whether in a read only mode or read

write mode, etc. the supported values are read only.

Many read write once or read write.

Mini mode.

Next is the capacity.

Specify the amount of storage to be reserved for this persistent volume, which is set to one GB here.

Next comes the volume type.

We will start with the host path option that uses storage from the node's local directory.

Remember, this option is not to be used in a production environment.

To create the volume, run kube control, create command and to list the created volume from the kube

control.

Get persistent volume command.

Replace the host path option with one of the supported storage solutions.

As we saw in the previous lecture, like AWS Elastic Block Store, etc..

Well, that's it on persistent volumes in this lecture.

In the next lecture, we will look at how we use persistent volume claims to claim the volume configured

with persistent volumes.

In the previous lecture, we created a persistent volume.

Now we will try to create a persistent volume claim to make storage available to a pod.

Persistent volumes and persistent volume claims are two separate objects in the Kubernetes namespace.

An administrator creates a set of persistent volumes, and a user creates persistent volume claims to

use the storage.

Once the persistent volume claims are created, Kubernetes binds the persistent volumes to claims based

on the request and properties set on the volume.

Every persistent volume claim is bound to a single persistent volume.

During the binding process, Kubernetes tries to find a persistent volume that has sufficient capacity

as requested by the claim and any other request.

Properties such as access modes, volume modes, storage class, etc. However, if there are multiple

possible matches for a single claim and you would like to specifically use a particular volume, you

could still use labels and selectors to bind to the right volumes.

Finally, note that a smaller claim may get bound to a larger volume if all the other criteria matches

and there are no better options.

There is a 1 to 1 relationship between claims and volumes, so no other claims can utilize the remaining

capacity in the volume.

If there are no volumes available, the persistent volume claim will remain in a pending state until

newer volumes are made available to the cluster.

Once newer volumes are available.

The claim would automatically be bound to the newly available volume.

Let us now create a persistent volume claim.

We start with a blank template.

Set the API version to v1 and kind to persistent volume claim.

We will name it my claim.

Under specification, set the access modes to read.

Write once and set resources to request the storage of 500MB.

Create the claim using cube control.

Create command to view the created claim.

Run the cube control.

Get persistent volume claim command.

We see the claim in a pending state.

When the claim is created, Kubernetes looks at the volume created.

Previously.

The access modes match.

The capacity requested is 500MB, but the volume is configured with one GB of storage.

Since there are no other volumes available, the persistent volume claim is bound to the persistent

volume.

When we run the Get volumes command again, we see the claim is bound to the persistent volume we created.

Perfect.

To delete a PVC we run the kubectl delete persistent volume claim command.

But what happens to the underlying persistent volume when the claim is deleted?

You can choose what is to happen to the volume.

By default, it is set to retain meaning the persistent volume will remain until it is manually deleted

by the administrator.

It is not available for reuse by any other claims.

Or it can be deleted automatically this way, as soon as the claim is deleted, the volume will be deleted

as well, or a third option is to recycle.

In this case, the data in the volume will be scrubbed before making it available to other claims.

However, note that this is an older option and is deprecated now because the Recycle controller originally

did a best effort wipe by launching a tiny recycler pod that mounted the volume and ran a shell command

like rm rf Scrub star to clear files.

It basically tried to do the admins manual cleanup for you with a simple file level delete.

But this isn't sufficient in practice.

It didn't guarantee secure erasure, didn't handle snapshots, or provide provider metadata, and only

worked for certain entry volume plugins on cloud or block backends like EBS, Google Cloud, Azure Disk,

or network storage like NFS or Sis drivers.

Proper cleanup can involve unmount, detach, file system, reformat, snapshot, retain policy handling,

encryption, key rotation, or provider level delete calls.

A plain rm rf leaves a inode metadata and may fail under permissions.

Because of these portability and security gaps, Kubernetes moved to a newer model.

The modern approach is dynamic provisioning with a storage class and CSI drivers, which we will discuss

next.

Well, that's it for this lecture.

Head over to the labs and practice configuring and troubleshooting persistent volumes and volume claims


Using PVCs in Pods

Once you create a PVC use it in a POD definition file by specifying the PVC Claim name under persistentVolumeClaim section in the volumes section like this:

  

1. apiVersion: v1
2. kind: Pod
3. metadata:
4.   name: mypod
5. spec:
6.   containers:
7.     - name: myfrontend
8.       image: nginx
9.       volumeMounts:
10.       - mountPath: "/var/www/html"
11.         name: mypd
12.   volumes:
13.     - name: mypd
14.       persistentVolumeClaim:
15.         claimName: myclaim

  

The same is true for ReplicaSets or Deployments. Add this to the pod template section of a Deployment on ReplicaSet.

Application Configuration

We discussed how to configure an application to use a volume in the "Volumes" lecture using volumeMounts. This along with the practice test should be sufficient for the exam.