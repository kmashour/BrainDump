![[replicasets.html]]

**We describe** to know information about the replica set specially the events section we use describe if the replica set wasn't even selected the replica set selector is also stated in the describe 

**We use log** to debug weird behavior of the replica set after it is up and running  بس لاوم تقوم عشان logs اشوفلها... Remember that the logs are generated from the applications inside the containers  

**Identifying the pod's ReplicaSet :**
 json file with creation details of the pod here we can fine the owner reference name which is the replica set
```
kubectl get pods {pod-name} -o yaml
```

![[Pasted image 20250424235359.png]]

```
kubectl get pods {pod-name} -o=jsonpath='{.metadata.ownerReferences[0].name}
```
More clear way 
```
kubectl get pods {pod-name} -o=jsonpath='{.metadata.ownerReferences[0].kind}
```
jsonpath --> extract certain information from the json file, its like running a query and returning only what you asked for 




**To identify the Replica set pods just search for the label** 
```
kubectl describe replicaset myapp
```

```
kubectl get pods -l app=myapp 
```




scaling replica sets 
The Html file is perfecto ..... 
Remember when using imperative commands in scaling is to always return back and implement the changes to the manifest if i want the changes to be constant to avoid returning back to undesired replica set state 



vertical Autoscaling 
 increases POD resources through resources and limits and eventually i will need to upgrade the hardware itself 

horizontal AutoScaling
 increase number of pods automatically autoscaling action occurs according to the resources usage threshold, autoscaling is done through kubernetes HPA (horizontal pod autoscaling) that deal with another component called metric server downloaded on the system if its not provided from the cloud provider   

Cluster AutoScaling 

 Increase Number of Nodes according to a Threshold either its CPU , Memory or custom metric most likely found in cloud environment infrastructure 

 The autoscaling feature depends heavily on the infrastructure you are currently.. but the scaling concept is the same in sense of vertical and horizontal and cluster scaling  


House Keeping My machine 

 Deleting the replica set will delete the replica set with all its related pods 

 adding --cascade=orphan will leave the pods will only delete the replica set 

 Now the pods has no manager if we created a new replica set with a matching selector to the pod labels they will fall under the new created replica-set and the replica set will take action creating or deleting according to the existed number of pods and the desired replica count 

 ![[Pasted image 20250425010806.png]]