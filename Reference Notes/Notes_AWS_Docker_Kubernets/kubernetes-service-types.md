---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
links: 
flogetzzel:
---
In service: clusterIP as we said all the communication is limited under the same cluster so when a pod want to communicate with another pod it will seek the service that the pod is found under it so the request could be routed to it 


NodePort: 
**Expose the service through a port on all the cluster nodes in range between 30000 to 32767**

![[Screenshot from 2025-04-21 08-50-52.png]]


The service will give all the cluster nodes an Ip and a port number to be able to communicate with outside world 

WHY NodePort SERVICE: 

now suppose the three pods that host my application under a service of type nodeport  ?? 

Service of type NodePort exposes the worker nodes inside the worker cluster from Range of Ports
Suppose we have 3 nodes and my pods which is the UI pods for example is on the 1st node and I accessed the 2nd node Ip it won't return service not found 
The service itself will handle routing the traffic to the pods through internal routing protocols and kube proxy 

That is the main reason behind the ClusterNode service


To choose the port manually 

![[Screenshot from 2025-04-21 08-55-34.png]]

port:80 --> in order for the service to communicate internally to addressable inside the cluster 

targetport:8080 --> a specific container within the the pod 

nodePort: The port on the node which make the node accessible to the world 


In production 
![[Screenshot from 2025-04-21 09-11-06.png]]

Issue WHY LOAD BALANCER SERVICE
what if the node the end-user is communicating with crashed previously the NodePort handled pod crashing scenario now we are facing node crashing scenario

the end-user will not be able to access the service, and he will need to know the ip:port of other nodes in order to be able to access the service, so its not convenient in the first place is to access an application with having to know the port number in addition to that I need to know the other Nodes Ips ??  



![[Screenshot from 2025-04-21 09-12-51.png]]

issue solved 
Load balancer single point of access (ip - DNS of load balancer) to all the nodes within my cluster the load balancer is not a kubernetes object its something completely outside my cluster it routes the traffic to the healthy node (perform health checks to know what node it can use), so if a node fails it doesn't route traffic to it and just route it to another healthy nodes 

**loadbalancer can receive traffic either from outside the cluster or from the internal network


**Any load balancer can apply route rules  to route the request to the desired path in my application**



clusters can be on cloud and on-premise data-center 

![[Screenshot from 2025-04-21 09-15-35.png]]

AWS --> classic load balancer 
azure --> azure load balancer 
GCP --> google load balancer 

Load balancer can be available to receive from two ports 
80 & 443 for example
But it cost extra + the cluster hosting cost (EKS)

In practice:
 suppose for each node There are 3 UI pods one on each node we will use one load balancer only for all the UI pods service (which group the front-end pods over the three nodes to single end point)... and the request will be forwarded and routed in all the application layers according to NodePort service load balancing which was able to handle the internal communication and load balancing when used in testing phase 

so instead of using 3 load balancer cloud service for each node we only used one on the UI front-end pods in all our nodes


 
**we only use one load balancer for all our app because in cloud every app (node)  will require a load balancer service and that is costly so we only expose one layer which is the Front-End pods and add them to a pool and expose them to the load balancer all the operation after the load balancer receive the request is handled by NodePort service , the ClusterIp will only handle communication between pods over a node since the node will not be exposed through a port in ClusterIp communication between pods over Nodes will not be applicable

ADD a picture to illustrate 


![[Screenshot from 2025-04-21 09-25-31.png]]

Metal LB is layer 2-3 load balancer,
layer 2: service exposed to internal networks only 
layer 3(BGP MODE): service exposed to the outside world 
advertising the routes to the outside world 

When a service with name load balancer is created the metal LB automatically expose an Ip  and its considered as a single point of access to my cluster and begins to either route the traffic internally (layer 2 mode) or from the outside if its (layer 3 mode )  



NodePort + load balancer (F5) / nginx 

manually add all the NodePorts ips to the load balancer so it can perform the health checks  

