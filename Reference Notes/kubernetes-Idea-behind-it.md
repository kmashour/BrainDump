---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
Date: 2025-04-17T13:56:00
deadline: 
status: true
---
The short answer you don't need Docker to learn kubernetes 
You need to understand Linux Container!! 

Now if we are hosting an app consists of 3 Applications
UI Backend Database each running in a container what if one them crashes, intuitive approach is to create another replicated container as Backup, so what if the host machine itself crashed !! 

So why don't we distribute containers on different machines now arises another problem how will we be able to manage the traffic between containers if they are on different machine (communication between containers) and how will we be able to manage external communication !!!! we are creating another issues while solving the main problems so we need an (orchestrator) منسق 

Docker swarm --> can't manage high number of containers 

Kubernetes --> More mature developed from google الابن المدلل ل
it came to market mature because google used it for so long internally until it was made open-source to the world 

Kubernetes cluster  
**kubernetes is both, its an orchestrator and a cluster but usually referred to as kubernetes cluster**

**Orchestrator :  manages containers on the machine it hands container running/stopped , the host machine health (Nodes) , network between containers so its a program that manages the life cycle of application** 

**Cluster : A group of machines that offer computational resources collectively, its a general term used when the collected power of all machine resources is utilized by applications as one cohesive resource....** 

**In cluster a machine(Host) is called node** 
- **If a node crashes the other nodes complement the deficiency** 
- **Scale out increase node**
- **Scale in decrease node**

Scale horizontally means extra nodes is added to the cluster 

scale vertically means the Resources are increases with respect to memory and cpu 

