---
obsidianUIMode: preview
class: inflow-note
tier: inflow
domains:
  - terraform
  - azure
source: https://www.youtube.com/watch?v=IEqxhA4rnsg
duration: "16:35"
tags:
  - terraform/azure
  - status/raw
---

# Day 13/28 - Terraform Data Sources Tutorial (with azure provider)

**Source URL:** [YouTube: Day 13/28 - Terraform Data Sources Tutorial (with azure provider)](https://www.youtube.com/watch?v=IEqxhA4rnsg)  
**Duration:** `16:35` minutes

---

## 📋 Video Overview & Description

Welcome to 13/28 day of Terraform Full Course For Beginners
In this video, we will look at how to fetch existing resources and use the values in your terraform configuration with the help of data sources.

⭐️ Below topics will be covered in this video:

- What are Data Sources and why they're crucial
- How to query existing Azure resources
- Real-world examples using azurerm provider
- Assignment to get your hands dirty

💡 Key Takeaway: Data Sources are your gateway to incorporating existing infrastructure into your Terraform code. They're like READ-ONLY references that help you build upon what's already there!

👨‍💻 GitHub repo :
https://github.com/piyushsachdeva/Terraform-Full-Course-Azure/

𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘 COURSES  👌 It’s   🅵🆁🅴🅴 ⛳
✅ Terraform Full Course For Beginners - #28daysofAZTerraform
https://www.youtube.com/playlist?list=PLl4APkPHzsUUHlbhuq9V02n9AMLPySoEQ

✅ Certified Kubernetes Administrator (CKA) 2024
https://www.youtube.com/playlist?list=PLl4APkPHzsUUOkOv3i62UidrLmSB8DcGC

✅ 𝗔𝘇𝘂𝗿𝗲 𝗗𝗲𝘃𝗢𝗽𝘀 𝗭𝗲𝗿𝗼 𝘁𝗼 𝗛𝗲𝗿𝗼:
https://www.youtube.com/playlist?list=PLl4APkPHzsUXseJO1a03CtfRDzr2hivbD

✅ 𝗔𝗭𝟵𝟬𝟬 𝗔𝘇𝘂𝗿𝗲 𝗙𝘂𝗻𝗱𝗮𝗺𝗲𝗻𝘁𝗮𝗹𝘀 𝗙𝘂𝗹𝗹 𝗖𝗼𝘂𝗿𝘀𝗲
https://www.youtube.com/playlist?list=PLl4APkPHzsUUOCWcjaXcH-WBVxCccZ4uO

✅ 𝗡𝗮𝗺𝗮𝘀𝘁𝗲 𝗚𝗼𝗼𝗴𝗹𝗲 𝗖𝗹𝗼𝘂𝗱 | 𝗚𝗖𝗣 𝗧𝘂𝘁𝗼𝗿𝗶𝗮𝗹 𝗳𝗼𝗿 𝗯𝗲𝗴𝗶𝗻𝗻𝗲𝗿𝘀, 𝗮 𝗰𝗼𝗺𝗽𝗹𝗲𝘁𝗲 𝗽𝗹𝗮𝘆𝗹𝗶𝘀𝘁 𝗳𝗼𝗿 𝘁𝗵𝗲 𝗔𝘀𝘀𝗼𝗰𝗶𝗮𝘁𝗲 𝗖𝗹𝗼𝘂𝗱 𝗘𝗻𝗴𝗶𝗻𝗲𝗲𝗿 (𝗔𝗖𝗘) 𝗖𝗲𝗿𝘁𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗘𝘅𝗮𝗺:
https://www.youtube.com/playlist?list=PLl4APkPHzsUXvkDFARdrH2LMESVqeuH8W

✅ 𝗔𝘇𝘂𝗿𝗲 𝗗𝗮𝘁𝗮 𝗳𝘂𝗻𝗱𝗮𝗺𝗲𝗻𝘁𝗮𝗹𝘀 𝗗𝗣 𝟵𝟬𝟬 𝗳𝘂𝗹𝗹 𝗰𝗼𝘂𝗿𝘀𝗲
https://www.youtube.com/playlist?list=PLl4APkPHzsUUd4rzzHEpHMsyD5PbVWz1I

✅ 𝗝𝗲𝗻𝗸𝗶𝗻𝘀 𝗧𝘂𝘁𝗼𝗿𝗶𝗮𝗹 𝗳𝗼𝗿 𝗕𝗲𝗴𝗶𝗻𝗻𝗲𝗿𝘀
https://www.youtube.com/playlist?list=PLl4APkPHzsUV3pz6zRpFJe3A4wTM2Pjvv

✅ 𝟭𝟬𝘄𝗲𝗲𝗸𝘀𝗼𝗳𝗰𝗹𝗼𝘂𝗱𝗼𝗽𝘀 - 𝗥𝗲𝗮𝗹-𝘁𝗶𝗺𝗲 𝗰𝗼𝗺𝗽𝗹𝗲𝘅 𝗵𝗮𝗻𝗱𝘀-𝗼𝗻 𝗽𝗿𝗼𝗷𝗲𝗰𝘁𝘀 𝗼𝗻 𝗖𝗹𝗼𝘂𝗱 𝗮𝗻𝗱 𝗗𝗲𝘃𝗢𝗽𝘀
https://www.youtube.com/playlist?list=PLl4APkPHzsUUc8HOEIwfB3Z2uxRv2SKOG

✅ 𝗗𝗲𝘃𝗢𝗽𝘀 𝗮𝗻𝗱 𝗖𝗹𝗼𝘂𝗱 𝗣𝗼𝗱𝗰𝗮𝘀𝘁𝘀:
https://www.youtube.com/playlist?list=PLl4APkPHzsUWr7SI4Kym5dr80DovuSbL2

✅ 𝗚𝗶𝘁𝗹𝗮𝗯 𝗖𝗜 𝗖𝗗 𝗧𝘂𝘁𝗼𝗿𝗶𝗮𝗹 | 𝗘𝗻𝗱 𝗧𝗼 𝗘𝗻𝗱 𝗥𝗲𝗮𝗹-𝘁𝗶𝗺𝗲 𝗣𝗿𝗼𝗷𝗲𝗰𝘁 [𝗙𝘂𝗹𝗹 𝗖𝗼𝘂𝗿𝘀𝗲]
https://youtu.be/uYaMRn2meJQ

Subscribe to our channel to get notified about the latest videos. 
🔥 https://www.youtube.com/TechTutorialswithPiyush

-----------------------------------------------------------------------------------------------------------------------
𝗖𝗼𝗻𝗻𝗲𝗰𝘁 𝗺𝗲 𝗛𝗲𝗿𝗲:👇👇

🔥𝗬𝗼𝘂𝗧𝘂𝗯𝗲 ▶  https://www.youtube.com/TechTutorialswithPiyush
⛳𝗟𝗶𝗻𝗸𝗲𝗱𝗜𝗻 ▶  https://www.linkedin.com/in/piyush-sachdeva/
🚀𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 ▶ https://www.instagram.com/techtutorialswithpiyush/
🌍𝗧𝘄𝗶𝘁𝘁𝗲𝗿 ▶  https://twitter.com/techie_piyush
👨‍💻 𝗚𝗶𝘁𝗵𝘂𝗯  ▶  https://github.com/piyushsachdeva
✍ 𝗠𝗲𝗱𝗶𝘂𝗺.𝗰𝗼𝗺 ▶ https://medium.com/@piyush.sachdeva055
📚 𝗱𝗲𝘃.𝘁𝗼  ▶  https://dev.to/piyushsachdeva
✨𝗗𝗶𝘀𝗰𝗼𝗿𝗱 ▶  https://discord.gg/TNCs4BRzq8
-----------------------------------------------------------------------------------------------------------------------

References 📚:

#devops #techtutorialswithpiyush

---

### Video Chapters & Timeline Breakdown

- **`00:00`** — Introduction
- **`00:41`** — Why use Terraform
- **`05:07`** — Creating the data source
- **`08:18`** — Naming the resource group
- **`15:51`** — Outro


---

## 📝 Full Video Transcript

Hello everyone, welcome back to my channel. My name is Piyush and this is day 13 in the series 28 days of easy Terraform. In this video, we'll be looking into data sources. What are those? Why do we use it? How do we use it? And of course, with the help of of an example, how do we use it? We'll see the real-time implementation of it. And the comments and like target of this video is going to be 150 like, 150 comments in the next 24 hours. All I need is 100 dedicated learners. That's all I need. That's all I wish for. And it will make all the efforts worthwhile. Right. So, without any further ado, let's start with the video. All right. So, let's see why do we use it and what it is. So, with the help of an example, of course. Okay. Let's say we have a shared virtual network over here in your Azure environment. Why I'm calling it a shared virtual network? Because it's been shared with multiple teams. And a different set of team members manages this infrastructure for you. Okay. So, let's say there is a network infra team who manages this for you. Okay. Now, it happens in many organization because as you grow in size, grow in number in the organization. Um like there is a dedicated team to manage your security aspects of infrastructure. There is a dedicated team to manage your networking side of it and there are different other teams. So, let's say you have a network infrastructure team who manages this virtual network for you. Now, it'll have multiple subnets created for each of the teams. Or each of the line of businesses or however they have configured it. For now, let's assume they have created for each of the teams and each of the live environments. Okay. So, I'm just going to create, let's say, seven six subnets over here. Subnet one, subnet two, subnet three, subnet four, subnet five, and subnet six. Now, this will be for your dev environment, this will be for your test environment, for your staging environment, for your prod environment, and then this will be for your development team, and this would be, let's say, for your devops teams. Okay? So, we have created separate subnet within the same virtual network, and dedicated each of the subnet to different teams and different environments. Now, you are part of a devops team, okay? So, you need to create a virtual machine for your own POC or for your own testing purpose. So, let's say, you have your resource group over here, okay? So, let's call it RG Piyush, or you can call it RG whatever your name is. And then, you have to provision your virtual machine in this particular resource group. But, the issue over here is you cannot create your own virtual network, you cannot create your own subnet because it's already been managed by some other team, and you have to make use of it like the way they have instructed, okay? So, this is the subnet in which we'll be provisioning our instance. Now, how do you do that? So, you do that with the help of something called as a data source. Okay? Data source make it possible, data source help you with taking the reference of resources that has already been provisioned for you. Okay? So, that you don't have to create it again, so that let's say, in in your team there are 10 devops engineers, each of them would not create their own subnet or their own virtual network, okay? And like for the security and compliance purpose for uh the process setup purpose, there are many other purposes as well. Now, uh how do we create it? So, in our let's say over here, let's say you have your Terraform code, okay? In that, you create something called as a data source. So, you create data source for your subnet, for your VNet. Okay? And then you give the reference of this particular subnet over here, and you give the reference of this particular VNet over here. Okay? Now, when you instruct your Terraform to provision the virtual machine with the help of these data sources, then that virtual machine, it will exist in your resource group, but it will be part of this shared virtual network and subnet six, okay? So, here it will be created. Okay? So, it will be more clear when we have a look at that with the help of an example, when we'll do the demo, which what we are going to do next. So, let's have a look at that. I'm going to keep this away for now. Okay? And let's go back to our screen. Okay. So, I have taken uh provider.sh and backend.sh from the previous videos. Now, what we need to do is we need to take the reference of as I have told you from the existing resource. So, I already have the resource created. So, uh where it is? Here. So, I have created one shared virtual network and called it shared network RG. Okay? Inside that, I have created uh subnet and called it No, that's actually that's the resource group name, shared network RG, and then we have a shared virtual network, shared network VNet. Inside that, I have created a subnet, shared primary SN. Right? So, we have these three resources created. Now, we'll be creating data source for these three resources so that we can use in our existing configuration. And what we're going to do, we're going to um implement or we're going to provision a virtual machine using these, okay? So, I'm just going to copy the virtual machine Let's go over here and I'm going to copy Azure RM virtual um sample code from uh from the documentation. Where it is? Let's see. Um close. Okay, here. Right? So, let's create a sample and we'll make the changes over there. So, I have copied it. Now, I'll create a new file and I'm going to call it main.tf. Let's paste it over here. Okay. Now, it has a variable which says it's prefix. So, let's keep it the way it is. I'll just change the name to something more uh meaningful to us. So, let's call it day 13. So, now our resource group will be created with the name var prefix, which is day 13. And RG. Let's change the location to Canada Central. Feel free to use variables. Um so, we have seen that multiple times. Okay? And now, it it's going to create one virtual network and one subnet. But, we don't need to create those. We already have those created. We just need to give the reference for those, okay? So, I'm just going to delete these two resources from here. Okay? And now, how we take the reference? We'll create something called as a data source. So, you can create the in the same file or you can create a separate file. Let's create in the same file and then we'll move it to the separate file. So, it starts with data, okay? And then the name of the uh data source type and then the name of the data source. Now, if you want to see the syntax of it, you can go back to Azure documentation. Like where do you see the resource? Just down there you will have the data sources as well, you know? So, these are the data sources specific to Azure virtual machine. Similarly, if uh we're going to check for, let's say, virtual network. So, here is data source for AzureRM virtual network. What it needs, it needs a name and a resource group name. Okay. Yeah, let's start with the um AzureRM resource group. Do we need the resource group name for that? Okay. Let's start the AzureRM resource group name. AzureRM resource group and then let's call it RG shared. Now, if you hover the mouse, it will show you what it's missing. Uh currently, it we have not provided anything, so it says a data block. So, name. Let's start with the name. Let's give it a name. Um name should be like whatever we have created, okay? Whatever we have in uh existed. So, it was Let me just double-check what was it. Uh resource group name was shared network RG. Okay, so let's just give it over here. Shared network RG. So, that's the data source for shared network resource group. Now, we have data for AzureRM virtual network. It's over here, and then give it a name. Um VNet shared. And again, let's give this a name. Name is shared network RG. So, you can just copy it from here or just type it from there. That's not a problem. Shared RG. Now, it is missing something else. So, let's over the mouse. It says resource group name is also required. Like this resource belong to which resource group. Okay, so let's give resource group name. Resource group name Now, we don't have to enter it again. We can take it from this data source, right? So, how do we take it? Data .resource group azurerm_resource_group.rg_shared and then .name. Okay, we are just taking the value from its attribute. Now, this is also done. The next is data azurerm_subnet. Okay, so let's call it subnet_shared. Okay, again, let's give this a name. Name is over here shared primary SN. Okay, and I guess it'll also expect resource group name. So, take it from data.resource_group.rg_shared .name. And it is accepting one more field, so which is your virtual network name because subnet is part of a virtual network. So, let's give it virtual network name, which we can again take from the previous data source. Uh which is data.azurerm.virtual_network.vnet_shared.name. Okay, so now we have just initialized the data source. Now, we can use that in our configuration. Now, go back and let's say we don't want to hardcode the location over here. We want to use the same location in which our um VNet has been provisioned, okay? So, for this, let's take it from data. dot uh resource group RG.shared.location. Okay, now it will take the same location. And then we have uh AzureRM virtual network. So, let's see. It has a location. Now, location it is taking from the AzureRM resource group, which is over here. But, resource group location is also dependent on the location of the resource group that was created by us by the network admin team, right? So, there is uh this dependency. So, it will take the source location. So, whatever resource group location is there, let's say it's resource group uh shared network East US. So, all the resources will be created in East US because we have used data source over here. And then we have used the same data source over here in the location for AzureRM resource group. And inside network interface as well, we are taking reference from that resource group. Okay? Now, it has resource group name, that is fine. Uh IP configuration subnet IP subnet ID. This is where we need to provide the data source for subnet. So, data. AzureRM subnet ID subnet shared.id. Okay, now virtual machine virtual machine is name, which is fine. Location resource group name, network interface, that's all good. Now, let's just uncomment this. Otherwise, it will throw you error for deleting the Terraform resources. And let's keep the same. So, for the storage image reference as well, you can use the data source. Like, it is one of the use cases of data source. And then uh storage OS disk is fine. Uh OS profile this Oh, yeah. That's everything is fine. So, now if we go and run TF plan, oh, we have to do TF in it first. Let's initialize the infrastructure. And then run TF plan. Let's say grep grep will be created. Oh, it has thrown an error. Let's see what it is. So, it says shared network RG was not found. Oh, actually, I have given the wrong virtual network name somewhere. Let's see. Shared network RG No, it's not shared network RG. It's shared network VNet. Okay. This is what I told you like you can type it or you can copy and paste. So, yeah, overconfidence. Okay. So, it says three resources will be created, network interface, resource group, and virtual machine. It's not creating subnet. It's not creating VNet. Still, it is able to create these resources inside the already existing VNets. So, let's apply these changes and let's verify from the console. I'm going to do auto auto approve. Okay, it says the resources have been created. Now, let's check on the Azure portal. So, I'm going to go to my resource group, and I've created a new resource group for this day 13 RG. In that, there are three resources, VM, disk, and NIC. So, let's see where it was created. Okay, let's go to networking. See network settings. Okay, so it's part of the virtual network shared network VNet and part of the subnet shared primary SN which is what we have configured for this VM. And this is how we have used data source. So, I'm just going to hit TF destroy. Um so, yeah, this is what I wanted you to see about um data sources in Terraform. I hope this was clear now. I hope you were able to do the demo along with me or you can do it now if you were not following along. So, thank you so much for watching. I will see you soon with the next video. In the next video, we'll be doing we'll be starting with the mini projects. So, we'll be starting with the provisioning a lot of infrastructure resources, virtual machine scale sets, virtual machines, um VNet, subnet, and a lot of cool stuff. So, uh stay tuned for that and thank you so much for watching. Make sure you complete the comments and like target. I will see you soon. Thank you so much. Bye-bye.
