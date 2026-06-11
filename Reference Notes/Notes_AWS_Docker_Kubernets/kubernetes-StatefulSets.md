
till now we used stateless resources as deployment, So why was it stateless lets take for example an nginx deployment all it did was to host a web page it didn't really matter on which node the deployments pods was used.... 

But in case of using a message broker like kafka or a database that won't be our case because they save there states on the node storage and in order for a database to work it will need its mass storage 

When working with databases we may create a DB cluster within kubernetes and is a cluster within a cluster one will be a master(Leader)and the other two will be read replicas and that is a DB related stuff 

So now we want to work with stateful applications like mysql database 

The stateful service also known as a headless service because it doesn't have an IP it only has a FQDN.

When creating a stateful set object the pods are named in order and spun up in order because stateful application can't startup randomly or in the same time like in deployment and any pod created from that manifest will have a **fixed Ip** 

A stateful service returns the Ip of all the pods behind it and the load balancing is handled by the client to decide which pod he want to use 


![[Pasted image 20250525095314.png]]


![[Pasted image 20250525095718.png]]

We use a storage controller either on-premise like ceph to provision a persistent storage or we use a cloud provider storage controller like ebs anyways we make a pv claim from it a pv is created and attached to the stateful sets 

![[Pasted image 20250525095838.png]]

so the persistent storage is something outside the cluster completely decoupled from it so if anything happened to the cluster my data will not be harmed, KinD provide a storage controller but its a container created to mimick the behavior of what would happen with ceph or on the cloud 

![[Pasted image 20250525100034.png]]

The stateful set can be delegated to create the persistent volume from the same manifest instead of creating a dedicated manifest for the pv claim through the volume claim template 