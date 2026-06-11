#kubernetes_follow_up 

https://kubernetes.io/docs/concepts/services-networking/ingress/



So what is ingress its a single point of connection to all the services 

in the previous notes I discussed services and it had a clusterIp type and a nodePort

clusterIp allowed the communication on a cluster level with an exception of port forwarding 

NodePort allowed external communication where the service gave a random port to each node of the cluster as an end point of communication with the external user but it had some downfalls 

- if a node fails it becomes a hassle for the end user to reach the application..
- The node end-point is not convenient for end-users 

The last two types of services which was the load balancer and cloud load balancer solved them by grouping all the nodes ip:port into a pool and acted as a single point of access to the cluster the load balancer can route external traffic or internal according to design


 
 In micro-service architecture if I have multiple end points for different micro-applications so i will have a service for each micro application and according to design i will expose the service to the end user through
 - **NodePort where each service resource will have a port on the cluster nodes**.... 
 - I can use load balancer service and through it i will be able to access the application and on cloud i will use 3 load balancer instances for each (application) replication will cost 3x more,To expose every node (whole application) we will use a loadbalancer 

![[Screenshot from 2025-04-21 23-50-42.png]]

That's why we use the ingress object its used as load balancer and single point of access to multiple services but kubernetes doesn't have by default a controller for load-balancing so we use external one as nginx ... in the manifest file we declare how we want the load balancer to do as it begins executing according to its design and implementation or just leave for its default behavior 

**bare in mind that the picture assumes all on the same node so clusterIp did the magic**  

Tldr 
assuming here that I have three nodes each with a replica of the application: 

If i have load balancer service and an ingress the load balancer service will be mostly by a cloud provider an external service it will only act as an end-point for end-user to communicate with the app through provided DNS name and the load balancing will be handled by the ingress object which will act as an end-point for all service and the service type will also be a NodePort as long as our application is replicated over 3 nodes 