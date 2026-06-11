---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Udemy-Course
page: "-"
Date: 2025-04-19T12:32:00
deadline: 
status:
---
![[../../Attachments/section3-lab-manifest.yml]]


The scheduler decides which node will run the pod we will use several parameters based on it the scheduler will schedule a pod on a node 


Resources = CPU - Memory 

The schedule decision is based on the free CPU - Memory in a node 

But how will the scheduler know how much resources the pod need ?? 

In reality no Component in kubernetes knows  much resources a Pod needs to run this is only known when the pod runs on a node ... 

**The developer should and must have a rough estimate what the pod needs to Run And under several test environments we can have more accurate number of how much resources needed to Run a pod after the analysis kubernetes gave us ways to allocate the estimated resources to run the pod** 


cpu: "500m"  m -> milli, 500 milli core which 0.5 core 
cpu: "1m" -> one milli core the smallest possible 

memory: "128Mi" -> base 2 more preferred because base 2 is used in memory calculation 
memory: "128M" -> base 10


![[Pasted image 20250424132343.png]]


Pod act as a unit: 
suppose we two containers each needs 100m cpu and 200Mi 
so the total needed resources for the two is 200m cpu and 400 Mi 
The schedule will have to find a node with these resources available to schedule the pod if there we no nodes with this requirements the pod will not be scheduled containers in a pod is dealt with as one unit they must work together tightly coupled  

![[Pasted image 20250424132439.png]]




---------
If a pod is scheduled on a Node and suppose its the only pod on the node 

with initial resources of 400Mi and 500m, and after some time the application in the pod it started to consume more resources the kernel on the node will provide the increase in usage of resources as long as there are resources available 

CPU:
Now we scheduled another pod the node will start to share the node resources over the two pods.... 
if the 1st pod started to consume 2 Cpu and we only had 2 CPU and 2nd pods need 500m cpu the kernel will start to divide Cpu cycles over the 2 pods.
Even if we added more and more PODS the cpu cycles will be divided among them as long as the pod is scheduled... 
because of the pod that surges in its consumption at random times some pods may get scheduled when its normal so if they get scheduled and a surge occur in any of pods the kernel will just Divide CPU cycles among them which may hinder performance 


Memory: 
If one of the pods that where added tried to use more memory resources than requested the kernel will perform OOM (out of memory) kill **that is because the node resources are consumed because all the pods are trying to use more than the requested if there where free resources the kernel will allow the pod to use it**......
the scheduler will try to **re-schedule the pod in another node that can at least provide the requested resources** 
if all the nodes are out of resources the **pod status will be PENDING**

OOM kill --> will result in killing pods (applications) randomly 



**we need to add nodes or cloud instances expand vertically** 
or 

**use limits** 
![[Pasted image 20250424142242.png]]


resources --> indicates the minimum requirements 
limits --> indicates maximum requirements the pod may need 

Limits --> Allow me to secure my application (pod) from kernel OOM but it should be added with caution because it may need more than the limit and that will hinder performance (web-application -- server busy -- some requests are not fulfilled) no enough memory   



