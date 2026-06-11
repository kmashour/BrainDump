

#kubernetes_follow_up 

Cluster configuration 
master plane 
worker plane 
Get your terminologies in check 

Running kubernetes on kind 
Running kubernetes on bare-metal 

-----------------------------------------------

![[service+discovery+-+lab01.html]]
The lab setup is kubernetes running on bare-metal 

![[Screenshot from 2025-04-21 12-30-09.png]]

consider the following scenario so we will run two web apps under a service 
we will edit the default html file in one of the pods
to see the load balancing option 

Implement the Pods manifest::::

![[../../Attachments/Screenshot from 2025-04-21 10-59-26.png]]

Would making two containers with same Ip cause a conflict or we avoided that by using the name ?? 
Absolutely no because they are on different pods hence different Ip 

![[Screenshot from 2025-04-21 11-27-40.png]]



Edit the html in the 1st pod to see the load balancing feature 
![[Screenshot from 2025-04-21 11-28-34.png]]


Edit the html in the 2nd pod to see the load balancing feature

![[Pasted image 20250421112922.png]]


Implement the service manifest::: 
![[Screenshot from 2025-04-21 11-31-59.png]]
**service type is by default clusterIp**


![[Pasted image 20250421113234.png]]

Shows the running services on kubernetes:::
![[Screenshot from 2025-04-21 11-33-48.png]]


I need to be a component within the cluster itself to access the service but the problem Iam an end-user Iam not an insider within the cluster,, So we make a pod especially that works as a client through it try to open connection with the service of the type clusterIP

Imperative way of creating a pod :::
![[Pasted image 20250421113627.png]]

This pod will be created once then we don't need again so imperative is better since it will only be used to run a command ( أخطف و اجري )

--rm-- --> when i finish with the command and exit the command which is the shell it will automatically remove the pod, وفرت عليا خطوة 

Now I want to test the service of the type clusterIP we can use any http client to test the service::: 
- apt update 
- apt install -y curl 
- curl my-clusterip-service.default.svc.cluster.local
- curl my-clusterip-service.default.svc.cluster.local
- curl my-clusterip-service.default.svc.cluster.local
   it will juggle between the two pods according to Round Robbin 
we can use the directly not the full DNS since we are under the same namespace    

what if i want my service to be of type clusterIp and I want to try it as a user, Iam a developer and I want to test ??? 

using a command called port forward this is part of kubectl 

connected to a raspberry pi by ssh which is the host machine-- on that host machine we had  a  master-plane node (vm) since this lab was conducted on a bare metal kubernetes cluster....

**the port forwarding is done through the host machine it self**

we can make port-forward on the pod directly but in our case we will apply port forwarding on the service :::
![[Pasted image 20250421115041.png]]


From local Browser :::
Local Host:8080 

![[Pasted image 20250421115341.png]]


but this is not the best approach its better to use a service of type Node-Cluster 

![[Pasted image 20250421122225.png]]

![[Pasted image 20250421122336.png]]


we will access through any node ip:port inside the cluster whether its the master node or a worker node 

![[Screenshot from 2025-04-21 12-26-54.png]]

192.168.2.76 or 192.168.2.77 or 192.168.2.78