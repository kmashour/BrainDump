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

![[pod.ref_volume.yml]]

Container as we know has an ephemeral storage it doesn't persist if a container crashes or subjected to deletion  

and if we needed storage to persist we used container volumes the same happens with kubernetes 

Volumes 

- EmptyDir : (creating persistent volume on pod level)
	- if the pod is deleted or moved from the node the data on that volume is lost
	- if the container crashed and the **pod is still available** and restarted on the pod the data will be persistent 
	- Stores the data for the duration of the Pod 


When creating a path for a volume of type EmptyDir you are creating a mount point to a volume on node level that can be shared among container of a Pod the mount point path will be created in a container if it didn't exist by default 

In summary, while emptyDir is the standard and explicitly mentioned mechanism for sharing storage within a single Pod
Data within an emptyDir volume is stored on the node where the Pod is running. This can be either in memory or on the node’s disk

But its explicitly stated that emptyDir for sharing data within a pod...

Example
1- Cache memory (avoiding expensive calls) -->
	In web-application it normally takes data from a database or api to process the requests from end user by using cache memory we only need to extract the data once from the db or the api and store for sometime until its cleared and process repeats for other request, cache is used to increase performance 
**caching is used in web-application and i don't need the cache to be persistent across nodes we are here talking about the front-end of the web app** 
2- Process checkpoint 
   some process may take hours so if a container crashed midway when it restart thanks to empty-dir volume it will save us hours because it will start from where it stopped 
3- Scratch space 
   some operation may need a temporary files to perform an operation when the operation finished to just discard the files or data it was using like merging sorting its something in the same logic of swapping two variables

- hostPath  :	
  Advanced usage where I want the container to have access to the disk as a device on the hardware level not just the file system  
 - ![[Pasted image 20250424152235.png]]

 - ![[Pasted image 20250424152501.png]]

 - ![[Pasted image 20250424152506.png]]

- nfs :
	Most used ,A shared volume can be shared among different nodes and different cluster
	Here data is persistent when pods transfer among the nodes 
	nfs is something I must create it doesn't matter where i create it on the cluster on different cluster 
	or even on different server **the most important thing is for kubernetes to be able to access it over the network** 
	So any pod on any node on any cluster can have access to the nfs volume and can even do write operations on the same time 

**This type of volume has a very unique feature unlike the emptyDir and host path volume is that container (pod) data wasn't persistent across nodes**

- `192.168.1.8` is a private IP, usually belonging to your **host machine on the LAN**.
- Your Pod runs in a virtual network or container network namespace that likely has access to this IP directly.


 nfs: 
  server: 192.168.1.8  
  path: /mnt/shared