---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
links: 
flogetzzel:
---
ReplicaSet ==> makes sure that a certain number pods are always live, so replica set helped us to manage large number of pods to ensure high availability of our in addition to agility in increase and decreasing number of pods that run a certain application 


- The Issue with ReplicaSet is the downtime 
	downtime will be caused when trying to update the pod template it can't handle that any change or update in container template in order to take place we will need to delete the old ReplicaSet and create a new one with the new template configuration .. (That is because pods are immutable the containers can't be changed in runtime)

Downtime nowadays are not something tolerable except for outage scenarios.

**The Deployment Will give zero downtime**
 its a kubernetes component specifically for zero downtime in case of any changes happens on the application either its update or changing something the design .. 

 **The deployment** 

 ![[Pasted image 20250425170730.png]]


 Think of deployment as the parent of replica-set the deployment is built over the replica-set in the same sense that the replica-set is built over the pods 

 Deployment is able to manage the pods through the replica-set 


Deployment give us a great package of features 
- self healing 
  The deployment automatically creates a replica-set and manage the pods through them the self healing is a replica-set feature because it automatically creates new pods instead of crashed on The deployment just makes sure that the replica set is doing its job another layer of confirmation 
- Scaling 
  Deployment can handle scaling, the thing is that the component who really do the scaling is the replica set so this feature its also done through the replica set and the deployment is nothing but a layer of confirmation ,Deployment manages this feature through the replica-set 
   ![[Pasted image 20250425184622.png]]

Deployment manages replica-sets:
الجزئين دول اللي بيعملهم ال replica-set ولاكن انا بكلم الdeployment و هو بيكلم ال replica-set بالنيابه عني

- Rolling update / Rollback 




Rolling update strategies
 
 Rolling update is the default deployment strategy 
  ![[Pasted image 20250425182330.png]]

   The new Replica set created is based on the new deployment manifest, Deployment will begin creating the other replica-set and after it brings a new pod up and it make sure its running it deletes one from the old replica-set until 
   The new ReplicaSet is fully scaled up to match the desired number of replicas 
   ![[Pasted image 20250425182612.png]]
   ![[Pasted image 20250425182636.png]]
   The **old ReplicaSet** is **scaled down to zero** (but not deleted unless you manually clean it up or hit the `revisionHistoryLimit`).
   - **New ReplicaSet = main one after update.**
   - **Old ReplicaSet = kept around (with 0 pods) for rollback purposes.**



  
   ![[Pasted image 20250425182651.png]]
  For the service its no big deal since all it cares about is the labels so during the shift that the deployment undergoes in rolling update the application faces zero downtime and runs perfectly fine


-----------------------------------------------------------------

The application at some instances in time will have even more pods than the replica set is accounted for due to the process of rolling update so the service may route users to the old version and others to the new version, Most of us has faced such scenarios while using an app you found out that a new feature appeared without even experiencing a slight downtime or latency or lag in app 
 
  ![[Pasted image 20250425182818.png]]
  ![[Pasted image 20250425182832.png]]

   It allows for the application to run different versions briefly during the deployment process. This approach minimizes downtime and reduces the impact on end users, as there’s always a version of the application available to serve user requests. **However, managing different versions during the roll-out can be complex, especially with database changes.**


  ![[Pasted image 20250425182857.png]]






   ![[Pasted image 20250425182908.png]]


  ------------------------------------------------------------------
   From what is appears we only need to use the big boss which is him because it has all replica set features done through in addition to the zero time rolling update

   **replica setيغنيني عن ال** Deployment 

   Deployment manages replica set instead of me 

  ------------------------------------------------------------------

---------------
 
 Rolling Update strategy, we can have control over how the deployment manages it 


 Best practice is to increase one parameter and decrease one parameter according your application business 
  ![[Pasted image 20250425190536.png]]


 By default, Kubernetes ensures that a **new pod is created and becomes "Ready"** in the new ReplicaSet **When deleting one** from the old ReplicaSet. This helps maintain availability. Termination happens first then creation of new one when its ready (according to Readiness probe) it will continue the same process until the roll out is finished 
 This behavior is controlled by:
  - `maxUnavailable: 1` (default) – at most **1 pod can be unavailable** during the update.
  - `maxSurge: 1` (default) – Kubernetes can temporarily **go 1 pod above** the desired replica count to spin up the new one.
   So its **a new pod comes up before an old one goes down**, unless you've customized these values to be more aggressive.

-------------------


Recreate strategy 
 - **All old pods are killed first.**
 - Then **new pods are created** using the updated ReplicaSet.

This means:  
 Simple  
 Causes downtime (no pods running during the transition)

When to use it 
 - Use `Recreate` when your application **can’t handle multiple versions** running at the same time — like when there's **shared storage** or strict **state dependency**.
 - Use when there is security issue like zero day vulnerability 

 ![[Pasted image 20250426001018.png]]

-----------------------------


![[Pasted image 20250426001052.png]]
Deployment main purpose is to ensure that the don't crash in update 
 It will either pause the update if the deployment replica-set doesn't start and its a time threshold that is set... 

 Another option for me is to rollback to older version

-----------

In deployment no need at all to implement the replica-set in the manifest we just state how many pod replica we need and implicitly the deployment create the replica-set because through it most of the deployment features is done so its basically the same as the replica set manifest
