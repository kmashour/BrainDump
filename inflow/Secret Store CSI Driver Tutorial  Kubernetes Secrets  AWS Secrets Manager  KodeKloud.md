---
title: "Secret Store CSI Driver Tutorial | Kubernetes Secrets | AWS Secrets Manager | KodeKloud"
source: "https://www.youtube.com/watch?v=MTnQW9MxnRI"
author:
  - "[[KodeKloud]]"
published: 2024-03-20
created: 2026-06-18
description: "Dive deep into the world of Kubernetes security with our comprehensive guide to Secret Store CSI Driver. Discover why this tool is essential for safeguarding sensitive information, learn how it compar"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=MTnQW9MxnRI)

Dive deep into the world of Kubernetes security with our comprehensive guide to Secret Store CSI Driver. Discover why this tool is essential for safeguarding sensitive information, learn how it compares to alternatives like ESO and Sealed Secrets, and master the process of setting it up for your Kubernetes cluster. With insightful demos showcasing the creation of secrets in AWS Secret Manager and the seamless integration of Secret Store CSI Driver, this video is your ultimate resource for enhancing security in your DevOps environment. Join us on this journey to strengthen your Kubernetes security posture and protect your valuable data.  
  
  
  
⬇️Below are the topics we are going to discuss in this video:  
00:00 - Introduction  
00:48 - Why do we need Secret Store CSI Driver?  
03:03 - What is Secret Store CSI Driver?  
04:01- Secret Store CSI Driver vs ESO vs Sealed Secrets  
05:25 - How does Secret Store CSI Driver works?  
08:14 - Demo - Creating Secret in AWS Secret Manager  
09:30 - Demo - Setting up Secret Store CSI Driver for Kubernetes Cluster  
30:56 - Conclusion  
  
✅Start your Kubernetes Career Now - https://bit.ly/KubernetesLearningPath  
  
Check out our learning paths at KodeKloud to get started:  
▶️ Cloud Computing: https://kode.wiki/CloudLearningPath\_YT  
▶️ Kubernetes: https://bit.ly/KubernetesLearningPath  
▶️AWS: https://kode.wiki/awslearningpath\_yt  
▶️Azure: https://kode.wiki/azurelearningpath\_yt  
▶️Google Cloud Platform: https://kode.wiki/GCPlearningpath\_YT  
▶️ Linux: https://bit.ly/LinuxLearningPath  
▶️ DevOps Learning Path: https://bit.ly/DevOpsLearningPath-YT  
  
#Kubernetes #DevOps #SecretStoreCSIDriver #K8sSecurity #AWS #sealedsecrets #awssecrets #DevOpsTools #CyberSecurity #CloudComputing #kodekloud  
  
For more updates on courses and tips, follow us on:  
🌐 Website: https://kodekloud.com/  
🌐 LinkedIn: https://www.linkedin.com/company/kodekloud/  
🌐 Twitter: https://twitter.com/KodeKloudHQ  
🌐 Facebook: https://www.facebook.com/KodeKloudHQ  
🌐 Instagram: https://www.instagram.com/kodekloud/  
🌐 Blog: https://kodekloud.com/blog/

## Transcript

### Introduction

**0:00** · hey everyone it's Sanji from code cloud and today we are going to take a look at a tool that was created to address some of the challenges that we face when it comes to working with secrets in our kubernetes cluster now there's a variety of different tools that have been created around this one problem which is managing Secrets there's tools like external Secrets operator sealed secrets

**0:18** · and today we're going to take a look at a tool called Secret store CSI driver and so what we're going to do is we're going to go over you know why was this tool ultimately created we're going to go over how this tool differentiates itself from some of the other tools like external Secrets operator and sealed secrets and then we're going to do a demo going over how to actually use this within our kubernetes cluster and you're going to see that this is a fantastic tool that we can utilize to manage Secrets within kubernetes so let's go ahead and Dive Right In and take a look at how to work with the Secret store CSI driver now before we get started going over what is the secret store CSI driver

### Why do we need Secret Store CSI Driver?

**0:50** · and how to use it I want to go over why exactly The Secret store CSI driver was created what problems does it help us address now Within kubernetes anytime we have any kind of sensitive information that our application may need to use whether that's you know credentials to authenticate with like a cloud provider or talk to a database we're going to store them in a kubernetes secret now the problem with this is if we take a look at DB password it looks like that value is secure but it's important to understand that this is actually not secure this is base 64 encoded which

**1:20** · means that it can easily be decoded so don't mistake encryption is secure if you encrypt data it's going to be secure but if you just encode data it can be easily so this data at this point the DB password anybody that has access to the secret will be able to know the value of the DB password because they can easily decode it and so if we ever upload our

**1:38** · yaml manifest or kubernetes manifest to gith which most likely we do or we want to do then anybody that has access to that GitHub repo will automatically know our database password because they're able to decode that value so that's one of the issues that we need to address because right now there's no way for us to Define secrets and safely stored in GitHub because all of our secrets can be easily decoded in addition to that a lot of organizations have started making use of external Secrets stores so things like hashy cour Vault aw Secrets manager

**2:06** · Google Secrets manager and Azure key Vault and so what these different Services allow organizations to do is it allows them to manage all of their secrets in one central location so all their secrets will be stored inside one of those platforms and then any applications that they need to have access to those Secrets they will just pull those Secrets using an API so that

**2:24** · way they don't have to manage Secrets across multiple different locations they'll all store it in one central location and so with all of these secrets being stored within one of these external secret stores we need a way for kubernetes to be able to pull those secrets and store them and sync them within native kubernetes secrets so that any application running within a kubernetes cluster can actually make use of those secrets and so natively there isn't way to do that but that's why ultimately tools like The Secret store CSI driver the external Secret store

**2:53** · operator have been created so that we can actually syn secrets from a Secret store into our kubernetes cluster all right so we went over why we would need a tool like The Secret store CSI driver let's talk about what exactly is it well the Secret store CSI driver synchronizes secrets from external apis and mounts

### What is Secret Store CSI Driver?

**3:10** · them into containers as volumes so if you're using something like aw Secrets manager it's going to pull those secrets from the aw Secrets manager or any other Secret store that you're using and it's going to mount them as volumes into your pod so that your application has access to those secrets and so once again you know one of the main benefits of this is that we get to use one of those Secret

**3:30** · store so we get to manage all of our secrets in a central place like Hashi cor Vault or AWS Secrets manager so that we don't have secrets kind of scattered all over the place we have one place to manage all of our secrets and then our kubernetes clusters or any other platform or tool that we use can just pull those Secrets dynamically and most importantly because it pulls these secrets at runtime essentially the great

**3:51** · part is that we don't need to worry about checking secrets into git because the secrets aren't going to be stored in git because it's all pulled from the aw Secrets manager or whatever entral Secret store that you're using now for those of you that know there's several other tools that help us manage Secrets within kubernetes things like external Secrets operator and sealed secrets and so I want to go over you know what is the difference between the Secret store CSI driver and the external Secrets

### Secret Store CSI Driver vs ESO vs Sealed Secrets

**4:15** · operator and sealed secrets and what makes this solution a little bit different it's not a major difference but I do want to make sure that you guys understand you know what it can bring to the table versus some of the other Solutions and there's really one main thing the main advantage of using the Secret store CSI driver over or some of these other Solutions is that you no longer store credentials in kubernetes secrets and so usually if you use like external Secrets operator or sealed Secrets what's going to happen is you're going to grab your secret from a central Secret store and you're going to sync it with a kubernetes secret well with the

**4:44** · Secret store CSI driver you don't actually create a kubernetes secret so there's no secret within kubernetes it's just going to pull it dynamically from your central Secret store like aw Secrets manager so what is the benefit of this like what do we gain by not actually creating a native kubernetes secret to manage our secret well it minimizes the attack surface as much as possible because that's one less place we're storing our secret in we're no longer storing our secret within kubernetes it's only in our secrets manager and so because of that this is

**5:10** · great from a compliance and Regulatory perspective because that's one less platform that has to adhere to various you know regulator bodies and that's one less platform that we have to audit because now our secrets are only within Secrets manager we don't have to worry about storing them within kubernetes so how does The Secret store CSI driver work well we're going to have our kubernetes cluster and we have to install The Secret store CSI driver and normally what we do is we're going to use something like Helm a package manager to deploy our secret store CSI

### How does Secret Store CSI Driver works?

**5:38** · driver so we can just do a Helm install and that's going to install everything that we need now what it's going to install well first of all there's going to be a couple of custom resource definitions and we'll go over what those are in a second but let's say that we have our secrets stored in a central Secret store and in this example let's say that we're using the aw Secrets manager and let's say that we have our database credential stored in there so we created a secret within Secrets manager called the db- creds and we've got dbor password as one key value pair

**6:03** · and dbor username as the other one so what we need to do now is we have to basically tell the Secret store CSI driver What secrets do we want synced and how do we actually access those Secrets where are they stored and so this is where we make use of one of the custom resource definitions that was created when we deployed that Helm chart and that's going to be called secret provider class so this is an example configuration of a secret provider class you can see we're using the AWS provider

**6:28** · and then we have to specify you know like where where is our secret stored with an AWS so it's going to be stored in Secrets manager and here we're just giving it the name of the secret which is going to be the name of the secret that we specified within aw Secrets manager the next thing that we have to do is we have to create our podspec and basically tell the Pod that hey we want

**6:46** · this specific secret mounted within the container within that podspec so here we'll create our podspec and we're going to create a volume like we normally do the only difference is we have to provide some properties for CSI and you're going to see that we referenced the name of the secret Prov class DB secrets so those are going to match up and that's basically just saying like okay whatever secrets that we pull from AWS I want it mounted into this specific

**7:09** · container and you can see here we mounted them in sltm within that specific container so after we create our pod spec and then we actually deploy it to kubernetes what's going to happen is the cuet is going to you know ultimately be responsible for creating that pod and it's going to see that we want a volume created and so it's going to talk to that the Secret store CSI

**7:28** · driver because it sees the configuration for that the CSI driver will then see the configuration of that and see that it points to the secret provider so if you remember this is going to be the configuration for the secret provider and so this is just basically telling you know the CSI Secret store you know what credentials do I want and how do I access them and so the secret provider is going to talk to AWS it's going to get the value of the secrets that we specified it's going to return it to the CSI driver and at that point we can then go ahead and create our pod and the CSI driver is going to then Mount the volume

**7:57** · onto that pod and that volume is going to contain the secrets that we pulled from AWS and it's going to mount it specifically in the location that we specified so in this case we said we want to mount it in the sltm directory and so it's going to mount all those credentials as a file into that sltm

**8:13** · directory so let's go ahead and get started with a demo now for this demo we're going to be utilizing aws's Secrets manager and that's going to act as our secret store so we're going to be focusing more specifically on that keep in mind that the steps are going to be a little bit different if you're using one of the other services like on Azure or gcp but we're going to cover AWS so the

### Demo - Creating Secret in AWS Secret Manager

**8:29** · first thing that we're going to do is we're going to create our secret so let's go ahead and search for the secrets manager service and what I'm going to do is I'm going to create a new secret and this is ultimately what we're going to mount into our pod and here I'm going to just select other type of secrets so we can provide key value Pairs and I'll just say maybe we're going to have a username property and this is going to represent I mean this could ultimately represent anything but I'm going to you know in this example use it as a you know like database credentials so I'll say username equals user 1 2 3 and then password I'll say this is password 1 2

**9:03** · 3 and I'll give this a name of MySQL D creds so this going to have all the credentials for connecting to a mySQL database I'll hit next and then we'll leave all the others as defaults and then hit next and finally we will store that and if I hit refresh we should see MySQL creds and if we go here we should

**9:21** · be able to see all the key value pairs we've got username user one password password 1 23 so now that we have our secret configured in secrets manager let's go ahead and set up the Secret store CSI driver for our kubernetes cluster and so if we take a look at the documentation page and you can use this URL right here and I'll make sure to include that URL in the description for

### Demo - Setting up Secret Store CSI Driver for Kubernetes Cluster

**9:41** · this YouTube video but we can go ahead and select installation and this is going to walk us through the steps for setting this up and it's going to be utilizing Helm to actually just deploy a Helm chart so that it can configure everything for us with just a simple command and so there's two things that we have to do and so first we have to install The Secret store CSI driver repo and then from there we can in install the CSI Secrets Secret store CSI driver chart that's listed right here so I'm going to copy this first line and I'm going to go to my terminal now and we can just copy and paste

**10:15** · that and then we can go to the second line and once again if we just take a look at the command we're going to create this chart right here and what we're going to do is we're going to deploy it in a namespace of cube system you don't have to use the cube system namespace just make make sure you don't use the default namespace make sure you have a separate namespace for the CSI driver we'll just go ahead and deploy it into the cube system namespace like the example

**10:42** · does all right so now that our charts installed if you want to take a look at some of the things that it's deployed we can go ahead and just do a cube CTL get crd and we'll do the namespace of cube system because that's where we deployed it and you'll see the custom resource definitions that were created by that Helm chart and so you can see here we've got two of them that look interesting to us which is the secret provider class from the secret store.

**11:05** · CSI and then we got secret provider class pod status so it's just two crds but that's what comes with the helm charts that were installed now if we go back to the documentation you'll see that there's two kind of notable optional values we've got sync as kubernetes secret um that's one of them and what that does is that it'll actually create a kubernetes secret and keep it synced up with the secret that's in AWS by default that's set to to be

**11:29** · turned off and then we have secret auto rotation if you enable this feature what it's going to do is anytime you make changes in The Secret store it's going to continuously pull the Secret store to see if there's any changes and then update the secret within your pod accordingly so by default both of them are turned off and we'll see later on in this video what it looks like when we turn on the secret auto rotation we're not going to really worry too much about syn as kubernetes secret one of the benefits of utilizing the CSI Secret

**11:52** · store driver is that we don't need to have kubernetes secrets but if you did want to for some reason or another you can always turn that on now now the next thing that we have to do is set up the AWS integration with the Secret store CSI driver so there's Specific Instructions for AWS and keep in mind that this is just because I'm using AWS if you're using Azure or gcp or vault

**12:13** · you're going to have your own specific steps for setting this up this is just for AWS just keep that in mind so let's take a look and if you go to this GitHub page once again I'll have this link in the description as well this is going to have all of the instructions for us and so there's a couple things that we got to do so this is just the requirements which is we have to have in this case since we're using AWS we have to have an eks cluster and then we have to have the Secret store CSI driver installed which we already do and then we have to the first step would be to install the AWS provider so I can just copy this command it's going to give us a manifest for deploying that so I'll copy

**12:57** · that now the way that the AWS provider Works in The Secret store CSI driver is that what it allows us to do is actually bind in a uh policy to a kubernetes service account and that's specifically with eks clusters and so this is once again how the AWS provider works the

**13:16** · other providers for Azure and gcp they're going to be completely different they handle the whole authentication with their platform completely differently so keep in mind some of the steps that I'm going over right now are just specific to AWS because that's what I'm going to do in this example so so we're going to first create our policy so I'm going to go back to AWS and I'm going to search for I

**13:46** · am so here we'll then go and select policies and we're going to create a policy so I'll create a policy here and I'm going to we can use either Json or the visual editor so first we'll choose services so remember this policy has to give kubernetes permission to retrieve the secrets within the secrets manager so I'm going to search for Secrets manager and then we have to specify the

**14:09** · different policies or the things that it can do within Secrets manager so let's open this up and we don't really need either of these but if I go to read this is going to be where we need it so we need to be able to describe secret and we need to be able to get secret value so those are the only two permissions and then here we have to specify the specific resources so I'm can I can say add RN and then you could specify the exact resource if I want to I could say us east-1 that's where I created that secret and then the secret name which I think it was like MySQL D creds maybe

**14:38** · and so you would just hone in on the specific Arn of the secret that you created or if you want to you could just do any region any secret once once again that's not the safe way to do things you always want to make sure you give only the permissions it needs so if you only wanted to give it access to those Secrets then you would want to specify that or if you wanted to give access to all of the secrets then you can just do what I'm doing here and so I'm just going to keep keep this example simple so I'm just going to give it full access to all the secrets but like I said you

**15:02** · want to make sure that you drill down and only give it permissions to access the secrets that it needs to know about and then we can go ahead and select next we'll give this policy name I'll we'll call it how about CSI eks access Secrets

**15:23** · manager and then I'll create that policy and we shall have successfully created our policy now now if we go back to the AWS instructions you'll see that there's a couple things that we have to do which is now we have to create the I am service account so this is going to basically bind that am policy and to a

**15:43** · service account that exists on our kubernetes cluster so it'll create the service account and then assign the necessary permissions that way our pods can then retrieve the secrets from AWS so there's this command that we can use using the eksctl utility so if you aren't familiar with AWS or eks it's just a CLI utility that makes it easy to work with eks clusters once again this is only specifically for anyone that's using the AWS provider in The Secret

**16:08** · store CSI driver if you're using Azure or gcp it's going to be a little bit different so I'm going to open up the terminal again and we're going to enter in a pretty long command so the command is going to look like this we'll say eksctl create I am service

**16:26** · account then we have to give the service account a name so what this is going to do is it's going to create a service account in our kubernetes cluster and we have to give it the name that we want so I'll call this since in this demo I'm going to you know assign these to secrets to a API container I'll call this API dsay for service account then we have to specify the region that my eks cluster is in so I'll say us- east-1 and then we have to provide the eks cluster name which happens to be eks demo 1 and then we say D- attach D

**16:57** · policy D Arn and then we have to get the Arn of the I am policy that we created in the previous step so I'll go back to AWS and I'll search for I forget what I called it I believe it was this one right here cesi Secrets volume Secrets manager I'll click on that we can get the irn right here and then I can just paste that

**17:26** · in then just a couple of other flags which is D- approve and a flag of-- override Das existing service accounts and that should be all that we need so I'll hit enter and we'll let that run and so this is going to actually create a couple things uh you know it's going to create a few things within AWS as well as the service account in our kubernetes

**17:57** · cluster all right so now that's complete if I do a cube CTL get surface account we should see that it created a service account based off of the name that I gave it which is if we take a look at the D- name flag API DSA and if you want to just poke around and we can take a look at what that's going to look like if I do this we can do a

**18:27** · describe and you could see several details like image pull Secrets mountable Secrets annotations and a few other things now the next step is to tell the

**18:42** · Secret store the CSI Secret store driver how to actually you know talk to AWS and the way that we do that is if I type in cctl get crd there's going to be a custom resource definition for this and so that's going to be the secret provider class so let's go ahead and create that so I'm going to create a new file and I'm just going to call this secret provider.

**19:02** · yo and I'm going to provide some base configuration which is here we use the API version this which is just in the documentation and then the kind is going to be that custom resource definition then we'll give it metadata so what is the name this is going to be any name that you want I'm going to call this database D AWS secets and then we'll go under spec here we'll say that this is a provider for AWS and then we have to pass in some

**19:36** · parameters we'll say objects and then here we have to provide two values which is going to be object name which is going to be the name of the secret that we stored within AWS and so that's just going to be MySQL D

**19:57** · creds and then we have to provide object type which is just going to be Secrets manager and so this MySQL creds that's going to come from AWS so if I go back to here we can see MySQL D creds and so now we can do a cctl apply and we can apply that secret

**20:22** · provider and I realized I forgot to save that file so let's run that again now if I do Cube CTL get secret provider class we should see it show up

**20:40** · here all right so I think we've got everything set up now the last thing that we have to do is let's just deploy a pod and make sure it gets access to the secrets so I'm going to create a new file and I'll just say this represents my API deployment and I'm going to paste in

**20:57** · just some basic configuration for deploying a pod so if we take a look at this I've got a deployment here we just called it my app and it's going to deploy an engine X container I understand that's not technically an API but this is just meant to be a simple demo and so we want to give this container this pod access to the secrets within AWS how do we do that well there's going to be a couple things that we have to configure the first thing is we have to configure a volume so this is going to be just like any other volume that we configure within a pod so we'll go under spec we'll say volumes and and here I'll give it a name

**21:30** · we'll call this how about db- creds and then we'll say CSI then we'll say the driver that we're going to use which is going to be following right here and once again this is just going to come from the documentation we're going to set read only to be

**21:47** · true and then a few other things which is volume attributes and then we'll say secret provider class and this is going to reference the provider class that we created here so we can just copy this name and pass it

**22:11** · here all right so we've got our volume and obviously once we Define our volume we have to then Mount our volume in our container so we'll go under Eng X container I'll say volume Mount what's the name of the volume that's the db- creds and then we'll say Mount path and then specify wherever you want to mount it I'm just going to mount it in sltm because it's just a demo all right and so that's going to be pretty much it but there's one last thing that we have to do if you recall let me see if I can

**22:43** · find the output of that remember when we created the service account so this surface account is what it's going to be used to authenticate with AWS to actually retrieve those secrets so we're going to actually have to specify the service account we want to make sure our pod uses that service account so that service account is called API DSA and so here we'll just go and just like we would any other time whenever we want to use a specific service account we'll say service account name and this is going to be what we just copied API dsay so

**23:14** · now that we got that let's go ahead and apply this all right so it's created now let's go ahead and do a qctl get pods and let's see if it was successfully deployed all right we can see it's in a container creating

**23:37** · State all right so if I do a cctl get pod let's take a look at the status of the Pod we can see it's still in container creating something's probably wrong it's been up for 78 seconds so if I do a cctl describe

**23:53** · pod it's going to usually give us some pretty good detailed error messages and here we you can see amount volume failed for DB creds and then it says you know failed to mount and then here it says must use object type when a full Arn is not specified so there's something with the object type configuration in our secret provider so if we go here you I will I know because based off the documentation I made a typo so this

**24:18** · should not be a separate entry this should just fall under there so that's probably what's causing that issue let's go ahead and apply that and then I'm going to do a cctl get pod we'll go ahead and just delete that just in case start from

**24:57** · scratch now if I do a CCT I'll get pod all right now we can see we redeployed the Pod and after that correction we can now see it's in a running state but even though it's running let's make sure that it actually was able to achieve our secrets so I'll do Cube C exac we're going to exec into it and uh we'll just drop into

**25:26** · bash and I'm going going to cat Etsy and under Etsy oops not Etsy we want to go into sltm and I'll just CD into there for you guys we take a look there should be a file called MySQL creds which is the name of the secret and if I C that we should see we've got a Json object with a username and password stored in there

**25:53** · so this shows that we were successfully able to retrieve our secrets from AWS and mounted at a volume into our pod that's running in our kubernetes cluster all right so now let's say that we had to change our database password so we go to our secrets stored in our secrets manager and under my SQL creds let's say that I want to edit one of these properties so let's say the password is now going to be new secret

**26:22** · password I'll save that and what we'll do is we'll go and I'm going to run that same command what do you guys think is going to happen if I run this command we can see our password is still password 23 so

**26:39** · it doesn't automatically update for us obviously we can delete the container if we wanted to or delete the Pod and then once a new pod gets deployed it's going to retrieve the new value but instead of that if you wanted to dynamically update on your behalf if you recall at the beginning of this uh demo I went over

**26:59** · the documentation and it pointed out some optional values which is the secret auto rotation what this is going to do is basically continuously paying AWS and if it sees that there's a change in your one of your secrets it's going to update that and make sure that the updated values are mounted in your kubernetes cluster or in the pods running in your kubernetes cluster so let's go ahead and do that what I'm going to do is I'm going to run a few commands so that we can actually get the values file for that Helm chart so I'll say Helm search believe

**27:29** · repo and I'll just search for CSI I forget the name of the chart okay so this is the name of the chart that we used and what I'm going to do is I'm going to do Helm show values we'll paste that in and this is going to print out all of the different values that we could set and what I'm going to do is I'm going to save that to a file we'll call it values.

**27:51** · yl and here you could see all of the different values that we can set now we don't care about most of these we just care about that one specific property and so let me see if I can find

**28:16** · that and this is the one that we want enable secret rotation so I'll set this to be true and then you can also set a rotation pole interval so this is basically just how how often should it pull AWS to see if there was a change in your credentials the default I believe is 120 seconds so every 2 minutes we're going to leave it as default but if you did want to customize it just go ahead and set that property to be how many seconds you want that interval to be so let's go ahead and upgrade our Helm release with the new configuration changes that we made to that uh values.

**28:50** · yo file so if I do Helm list- nc- system the name we called it CSI Secret store so I'll say Helm upgrade then we grab the name of that release then we grab the name of the chart which is going to be that long name that I copied previously and then here we can pass in the dh- values flag so that way we can pass in our values.

**29:17** · AML and then remember this is going to be in the namespace cube system

**29:34** · all right so we've successfully deployed those changes and so now if I go back to that container and I just hit the up command and we cat that file we can see that it now has the new secret password so every 2 minutes or whatever the default value is it's going to pull and ask AWS you

**29:52** · know has the secrets changed if it has it's going to update those values kind of dynamically on the Fly to Your container and you know obviously with that in mind if you're going to do it like this then you're going to have to make sure your application has the logic built in to actually you know make sure and check that the values in this file haven't changed because if it has changed then it has to actually you know go ahead and pull those new values in and update the application accordingly

**30:14** · video on kubernetes Secret store CSI driver so we got a chance to take a look at how we can actually utilize the tool to manage Secrets within kubernetes and manage Secrets within our application we got a chance to dive into how it kind of differentiates itself from some of the other tools that are a ailable within the kubernetes ecosystem you know I'm curious to find out what is your favorite Secrets management tool especially when it comes to kubernetes whether it's external Secrets operator sealed Secrets or CSI driver please let me know post a comment in the video and let me know which one is your favorite and I'll see you guys in the next

### Conclusion

**30:56** · one