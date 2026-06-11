---
tags:
  - kubernetes
Type: Reference Note
source: NTI-gerges
page: 
Date: 2025-04-16T18:35:00
deadline: 
status:
---
External sources citation Books articles Research papers blogs video-courses courses lectures Docker compose can handle a limited number of containers probably more than 50 containers the management will not be convenient like i cant secure connection between containers (database - application)
also i cant secure connection of the app as an all and the customer imagine talking about 1000 container so we need a tool to have more control over our containers...

Kubernetes is developed by google, it gave me more control over containers configuration but with more control it becomes more of hassle on the engineer to setup and configure it 

kubernetes = cluster 
cluster = Master node -- worker node 
Master node by default nothing is installed in it
Worker node is where my installation happen and configuration

cluster has at least one master node with any number of worker node (think of it as windows server and multiple machine where the windows server manages all of them)

The Master needs some component to orchestrate the worker nodes 
- API server 
	The gateway to the cluster for me as a kubernetes user and to the cluster workers, Its the only component that can do that in kubernetes 
	its a broker for me and Master node 
	and Master node with workers 
- ETCD cluster 
	**It stores all the metadata for all the cluster (master node - worker node)** , similar to docker inspect json file , low latency database and its a non-relational database  (key - value) and its encrypted secure database 
- scheduler 
	Deploy application on worker nodes it works by default depending on the utilization of resources I can add restriction to deploy on a specific worker but it has a default algorithm it schedules according to it... 
	based on:
		- utilization
			- 80% is max resource utilization for the worker node default can be bypassed 
		- traffic
			- it may have small storage size but has high CPU Memory since traffic utilize this resources 
			- storage is easy to expand unlike CPU , Memory 
- Control manager 
	Monitor all worker node , Makes sure the worker node is up and running .. Up means there is a network connection both ways, and proper utilization of resources


The Worker needs some component
- kubelet
	Main component that receives and sends requests with the master node (worker node gateway)   
- kubeproxy 
	The only component responsible for connection and distribute ips for application (containers)
- container run time engine 
	Responsible for start create stop for the containers of an application



Minikube or kubeadam to use kubernetes locally  
Setup the whole components automatically 
Minikube -> cluster ( master node - worker node) only
kubeadam -> cluster ( master node - 2 worker node) only

{Master,Worker}Node = Individual Machine for each

**In Depth Master node**
API Server
	Authenticate and Authorize User through checking a if the user has access to cluster and check permission the user have on the cluster through referring to to the ETCD cluster . 
	P.s Any the API server is the only way to complicate with cluster components 

ETCD cluster 
	it only contains the metadata for both master and worker nodes , not the logs !! 

Control manager 
	manage all the components in a cluster and monitor worker nodes by checking the status through kubelet that is updated every 5 sec from all worker nodes control manager receive the status through API servers.... 
	5 sec passed and no status was sent it gives a window of 40 sec after that is informs API server not to forward any requests to that worker node up till here what appears to me as an end user every thing seems fine and ready until 5 mins passes it will show a status that this node is not ready !! the number 5 min is very dangerous and it can be configured to 1 - 2 mins 
	probably it will be a kubelet issue because it is the component that is responsible for the connection highly likely but it may be another thing 

   (**the manage responsibilities is abstracted existential crisis like-knowledge its totally abstracted in cloud for example you are not authorized or authenticated to access the machine even you only API endpoints to handle some config more than that we need to send ticket to AWS to handle it**),But take care between every transaction within the components of the master node components passes by the control manager so when the request is made it passes by control manager when the request is done it confirms with the control manager..every confirmation between phases of a request passes by it...................
   
Kube-scheduler 
	every application created is distributed according to utilization of worker load by default....scheduler asks for utilization of worker nodes from ETCD and accordingly assign the request to a the perfect fit worker node takes its ID and forward the request to the kubelet through API-SERVER for the worker node to create the machine, Internally it deals with 80% as 100%


**In Depth Worker node**
kubelet 
	Is the main component for communication in a worker node and the execution of a request from outside the worker node it also validate the request !!, 
kubeproxy 
	Manage Network in the machine for running applications(machines), Decoupling Docker runtime engine from all its layers except for containerd which runs stops create the container, and discarded the layers of the docker container engine which was responsible for the network because it made conflicts, this approach made the it more lite because we only took the layer we need from the docker before that the performance was heavy because it is as a tool we heavy ...

Docker Runtime engine 
	the forwarded request to the Worker node through the kubelet is passed to that runtime engine to create the container  

when a container is created in a worker node a reverse process happens where the kubelet sends the status to API server

the API server gives end user status update 
updates the ETCD directly
both action are done simultaneously 
