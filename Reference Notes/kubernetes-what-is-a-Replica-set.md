---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: 
links: 
flogetzzel:
---



![[Pasted image 20250425121248.png]]


Till now all we did was to create pods manually because we just worked with 3-4 pods . In any application it will consist of at least 6 micro-services (micro-application) each service will have at least 4 pods for high availability 
so it will be very hard to manage **(Manual pod creation issues)**: ... 
 1- name must be unique 
 2- to scale out we will have a manual approach like            literally copy pasting the manifest of the pod and          running kubectl apply and we when scaling in we will delete each pod manually 
 3- to apply any change in the pod we must delete and run       kubectl apply on the manifest so changes could take effect 


The ReplicaSet will solve our issue: 
 - Can create and manage a number of identical pods based on a template (قالب)
 - will create any missing (or deleted) pods to match the replica count 
 - will also destroy any additional pods to maintain the correct count



- **When applying any change on the container template and apply it, the changes won't apply unless we delete the old replica set and create a new one
- **Through replica-set manifest we can change the number of replicas a replica-set should create and manage without bringing the whole replica set down can be re-configured in runtime**

This happens because of something called **Reconciliation Loop**

- the Reconciliation loop is something constant over all the kubernetes controllers  ( ReplicaSet ...etc). How does it work 
    - **The controller**s in the control plane checks the API server for updates, the updates are usually from the worker node kubelet to keep the api-server updated with the latest state of the worker node 

    - The controllers reacts to the event from the API-servers 
      (create/delete/modify/etc.)

    - Through reconciliation loop the controllers tries to make the cluster move from the **observed state** to the **desired state**and if the ReplicaSet for example satisfy the desired state according to the instructions in the manifest it will just observe without taking any actions 



**How are pods connected to the ReplicaSet ??**
  **ReplicaSet is like a service it uses label selector...**
  But it uses the new way which is **matchLabels** and we can use **matchExpressions** 



In the ReplicaSet manifest we will use a label selector and add to it the pod label that is used as a template for the ReplicaSet 

ReplicaSet adapts a loosely coupled approach to manage pods where it manage any pod that has the label defined in its label selector.. with keeping the desired number of replica's according to the manifest file 

in that sense if i created a pod manually with the ReplicaSet selector label it will be managed behind the ReplicaSet and in reaction the ReplicaSet will react by getting rid of a pod randomly to reach the desired number of Replicas (Desired state)





why kubernetes uses the loose coupling in ReplicaSet why wasn't it implemented in the ReplicaSet Design to manage the pods that created in its manifest ??? 

Lets say a Pod has misbehaved in our application we can manually change its label and labels can be updated while its running so if that happened it will be outside the ReplicaSet management pool and will be outside the service pool (The pod is quarantined) that pod now doesn't belong to anything... and thanks to the reconciliation loop another pod will be created instead of that ==quarantined== pod which can be subjected to debugging

So labels can defined which pod belongs to what ReplicaSet and what service... we can easily change a pod ReplicaSet just by giving it another ReplicaSet label 










ReplicaSet Manifest 
 Now ReplicaSet is a higher resource so we probably won't be dealing with Pods again and we will use pods through ReplicaSet


![[Pasted image 20250424232908.png]]