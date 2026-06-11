---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
Date: 2025-04-19T15:11:00
deadline: 
status: true
---
Most important **resource** in kubernetes the pods ? 
why kubernetes deals with pods not containers as in docker compose ?? 

In Kubernetes, a pod is the smallest unit that a developer can manage and deploy. It **can house one or more containers** that share **the** same **network** **space** and can communicate with each other using **localhost**. This **grouping** allows **containers** within a pod to share **resources and dependencies.**
Pods provide a **unified management layer**, which is beneficial for scenarios requiring multiple web servers or application components to work in tandem. By packaging containers that need to work together in a pod, Kubernetes simplifies deployment strategies


pod can have more than one container, it comes handy because they start up together and go down together(**unified management layer**), if two application are to be tightly coupled as an nginx container and a log shipper (consume logs), so those containers will be coupled together within a pod start/stop together.(OF COURSE THEY CAN BE DEPLOYED ON DIFFERENT PODS ON THE SAME NODE)


when two containers in the same pod **they share the file-system and storage** , two containers can communicate within the same pod directly through loopback <-- localhost:port1 localhost:port2 they are dealt with as two processes on the same machine, very helpful in pod design patterns (main container -  side car)..

Don't confuse that they (containers) share the file system in the sense they have the same filesystem e**ach container will have completely isolated file system but when using EmptyDir for example the two containers may mount on the same EmptyDir volume on that pod** 


Now what if we deployed the nginx container and the log shipper independently to default kubernetes behavior we might end up with a pod running and other container is not running we might end up having latency issue and a hassle in the connection between two pods on different networks (nodes) completely which may lead to latency issues

so kubernetes pod Object is the main and smallest resource kubernetes can offer 