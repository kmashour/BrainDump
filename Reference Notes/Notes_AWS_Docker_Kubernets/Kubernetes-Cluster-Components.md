---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
canvas: "[[KubernetesCluster-components-v1.canvas|Cluster-components-v1]]"
flogetzzel: 
page: 
links: 
Date: 2025-04-17T14:33:00
---


Control Plane (العقل المدبر)
- One or more nodes running on linux called master node(s)
- Those nodes manages and orchestrate resources of the Data plane the nodes in data plane are referred to as worker nodes

Data Plane - Worker node(s) 
(cluster may contain multiple nodes)
- One or more nodes running on linux or windows, Microsoft did some work in order to make windows suitable for container but still linux is more dominant 
- where the application is hosted


Kubernetes interpretation to cluster is a bit tweaked because it **completely decoupled the cluster into the master cluster and worker cluster thats to avoid overloading** the cluster if the control plane is consuming high resources load which may hinder the cluster performance... In production , in lab environments both will be hosted on **master node** (on one cluster) (بيئه منتهيه الصغر)

**In production Master nodes should be an odd number !!**

Control plane components 
- API-server (API Its a type of web-server ) 
	- **receives requests in http protocol like any web-server but it always responds in json which data needed by applications to communicate so API is always used by tools and application...**  (control planeقلب ال) without it the master node won't be able to receive commands  <-- 1
	
	- Communicating as End user with Kubernetes my requests sent through yml file (manifest) **it also checks my authentication authorization after executing the request** e.g if Iam allowed to create a node for example .. The API server returns the status..... 


If a container was deployed we must store that data to keep track of my cluster so kubernetes mind (control plane) **uses ETCD database lite weight very fast database**   <-- 2 

-  ETCD (Outside the API server its an independent entity)
	- Its as a cluster itself in terms of being completely independent from the API-server 
	  but its within the control plane as a component
	- For ETCD cluster to work efficiently and provide high availability The ETCD component must be an odd number to achieve Quorum النصاب which one will write, one will write two read-only at a time very advanced concept just use the odd number as best practice #kubernetes_best_practice 
	  Quorum النصاب(Who will be the leader)
  
- Controller Manager ( مدير المتحكمين)
	- In kubernetes realm everything happens through a controller so every entity that can execute a certain task is controlled by a controller under the controller manager center , Every controller has an object (resource) that is manged by it example 
	  Deployment controller --> Replica-set Controller ->POD Controller


> [!NOTE] Terminologies
>  
> A **Kubernetes object** is a _record of intent_ a specific instance of something you want to exist in the cluster. When you create an object, you're telling Kubernetes what you want (e.g., “I want this container running with 3 replicas”). any thing that made out of a manifest so it has a spec , status , metadata 
> 
> Maintains desired state (if you said "3 replicas", it ensures 3 are running at all times) hence its record of intent  _"This is the state I want — make it so and keep it that way."_
> 
> A **resource** is a type or kind of object in the Kubernetes API. Think of a resource as a category or class, while an object is an instance of that class.
> So:
> - **Pod** is a resource type.
> - **my-app-pod** is an object of type Pod.
   You define and manage **resources** through the Kubernetes API, and the actual **objects** are instances of those resource


Now through API there is a request to create a POD 
(POD may contain a container or more) SO THE API-SERVER 
1- receives the request 
2- request saved on ETCD 
3- Publish an event through the master node with the need to create a POD 
4- The controllers are subscribed to the API server (publisher) so they receive the published event
5- Now the controller responsible will respond to the published event  
6- Begin execution according to its design 

In kubernetes Everything happens inside the master cluster through API-server like Event publishing that are shared within the master node ... The API server gets confirmation from any component with each operation .. if a pod crashes it (API-server) publish an event so the related controller could start to take actions according to its design,

**Worker nodes** through **kubelet** updates the status every **5** sec when no status is received it gives a window of **40** sec after that is informs API server not to forward any requests to that worker node **up till here** what **appears** to me as an end user **every thing seems fine** and ready until **5 mins passes it will show a status that this node is not ready !!** the number 5 min is very **dangerous** and it can be configured to 1 - 2 mins 

- scheduler (sees which node could host which POD)
	- In kubernetes it means to put a pod on a worker node according to some metrics (algorithms) like  
		- The node health (resources utilization)
		- POD if predesignated to be added to a certain node which is called affinity (بتتأكد من امكانيه حدوث ده)

resource utilization here refers to the percentage node utilization how much free resources in the node to put a pod 
so how much is utilized from the node how much is available so i could add my pod !!!

Cloud controller manager 
- Deals with cloud provider that host my cluster 
- if the cluster is on my PC or data center its useless 
 

 

Data plane components 
- kubelet 
	- Each host (node) on the cluster has a kubelet and through this component the containers(pods) will run 
	- This component is the real worker (هيا اللي بشغل بأديها), Running the container is its responsibility 
	- Direct connection between it and the API server and updates the status of the node periodically to the API server with its current status (ready - Not ready )
- Container Runtime --> (contianerd) in openshift --> crio
	- Lower level of execution this component addresses the container directly and as a user Iam abstracted from its execution... (run - pull - stop) container, some cloud provider offers the option to configure the container Runtime but as a user its a very rare case where i have a unique app with unique requirements very specialized cases ,,,, **MOST OF THE CASES WE USE THE DEFAULT** 
- kube proxy 
	- responsible for connections within the node and from the node to the outside an vice versa ,,, if i want to address a container inside (x) node inside (x) pod that will happens through the kube proxy (المتحدث الرسمي)
	- Ensures that Pod-to-Pod and Pod-to-Service communications work correctly within the cluster.
	- **kube-proxy** is for **Service networking**, not API server ↔ node communication.

 **kubelet** is the component that directly talks to the API server on worker nodes. **KUBELET HAS DIRECT OPEN COMMS WITH THE API SERVER**