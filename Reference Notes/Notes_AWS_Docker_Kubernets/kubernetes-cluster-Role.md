---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
links: 
flogetzzel:
---
Role is name-spaced only applied on object that are confined within a name space (Deployment, ReplicaSet , Service)

So what if I want to control the authorization over a Node, A Node can't be in a namespace is carries all the work loads in other words the the namespace that contain the object and resources are within a node 

so to control the authorization over a Node we use ClusterRole 
its exactly as a Role the only difference is that a cluster Role deals with the object that doesn't belong to a namespace 

![[Pasted image 20250524214824.png]]


![[Pasted image 20250524215317.png]]