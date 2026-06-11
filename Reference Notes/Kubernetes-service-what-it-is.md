---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: 
links: 
flogetzzel: 
Date: 2025-04-20T22:58:00
---
Service Discovery is related to IT in general not only kubernetes 

any applications has micro-services or application communicating 

Issue (Why we use a service)

web-app working on a pod (all of the app on the same Pod) on Port 8080, so it listens on that port for example now i want the end user or another pod (mircoservice) to access the app that happens through the ip address or the DNS name after writing the url, the url is resolved in the DNS to its ip, **Pods doesn't have fully qualified domain name (a name that can be given to DNS and resolve it to ip )it may have a name buts its not DNS** --> remember when debugging the pods we never came across a DNS name so the only means of communication between pods is over there Ip 

assume the client has access to our cluster and has the ip address of the pod ?? 

A pod IP may vary because as we saw any change(image, volume, port)done on a POD can't be done when its running it must be terminated and deleted then start up again all of that because its ephemeral think of it like plastic spoons and plates they are not made to be washed and re-used for a different dish (different configs)

This leads to a problem: if some set of Pods (call them “backends”) provides functionality to other Pods (call them “frontends”) inside your cluster, how do the frontends find out and keep track of which IP address to connect to, so that the frontend can use the backend part of the workload.
**If that Pod dies and comes back, the name may not be valid anymore (especially in the case of ReplicaSets, Deployments, etc.).** 




**of-course with the exception to labels and annotations they can be reconfigured when the pod is running**


> [!NOTE] In short
> **SO WE CAN'T RELY ON IP** 



--------------
https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation/

Kubernetes service (kubernetes عباره عن جزئيه في )
- A **Service** groups a set of Pods (usually via labels).
- A **component** that has fixed IP address and DNS name 
   ==as long as the service is not recreated or deleted it will have a fixed IP and DNS== **stable DNS name and IP address**.
- Kubernetes service has internal DNS on the **CLUSTER level so pods behind the services could _communicate over the services_** 
	- (service is able to do that through kube-proxy)
- Internally, it **tracks the actual Pods** (and their changing IPs) using selectors in manifest file.
   - It also routes to healthy PODS (will be more clear when we use replica-sets)
   - **Service** uses the readiness probe **status** to decide **which Pods to send traffic to**.


In short
 A kubernetes service should remain stable, even if you change the Pods behind it (update Deployments, add more Pods with matching labels, `kubectl rollout restart` because it hung..
 **If you delete and recreate the Service there aren't any guarantees (in fact you will almost definitely get different IP addresses),**

so its better and good practice to use Service for pod communications 
-  **Kubernetes services solved this problems:**
	1- pods have ephemeral IP addresses 
	2- pods do not have DNS names 

Yet comes the service to solve another issue 
 - Since we work with cluster its normal to have multiple pods with the same application for high availability  
 - When the application service receives a request from client..
 - it begins to route it to one of the pods under it in Round Robbin fashion route to a pod after a pod i.e in turns.so it acts as a load balancer that only knows Round Robbins algorithm 

![[Pasted image 20250424213924.png]]




Think of the service as 
Front-end (DNS - IP)
Back-end (Load balancer)


so grouping all the related pods under a service is done through the label selectors , **service object uses the old way of label selectors**, the old labeling in services is based on ( AND ) when selecting the pods so if we use for example (app:myapp dev:app) on the pods with those two labels will be behind that service 

![[../../Attachments/Screenshot from 2025-04-20 23-40-02.png]]

**selector:** --> by using labels we select the pod that will be under a service object 

**targetPort:** --> can be used to refer to a specific container if we are dealing with a multi-container pod 

**type:ClusterIP** --> This service only listen on cluster level the pods behind the service will be exposed to the services of the same cluster so pods under different services will be able to communicate 

![[../../Attachments/Screenshot from 2025-04-20 23-40-32.png]]

Usually when exposing a port to end user we tend to use default http port 80 or port 443 https because they are default for any browser www.example.com:80 the (:80) is automatically added by the browser

Imperative approach:
```
kubectl expose pod nginx-pod --name=backend-service --port=80 --target-port=80 
```

**ports name:** 
==in containers ports can have a name and it can be used with targetPort , and its more convenient to use it like this because its constant while the port number now can be tampered with and it will not affect the service==  


DNS name : 
**Under the same name space we could use this**
myapp-service 

**Outside the name space we must use fully qualified Name**
myapp-service.default.svc.cluster.local
service-name.namespace.svc.cluster.local 

default --> because we didn't specify which namespace we will add the service to !! 
cluster.local --> as long as we didn't change cluster domain name 

> [!NOTE] Service DNS name
>  What makes services is crucial and pivotal kubernetes object is that its domain name is fixed even if the service was deleted and recreated with a new Ip because the DNS of the service is not based on the IP like our usual web Tcp connection so as long as the service is recreated all connection will be going through the service with no issues 





namespace is nothing but grouping of resources (objects)  under a common flag --> take it as that for now



--------------
**how the service works internally** 

EndPointSlice: A resource used by service to know which IP it should route the request to because it 
- **saves the latest IP addresses and ports of the pods behind the service** 
- **readiness state** 
- **EndPointSlice gets updated with any change in those previous two point thats how it manage and keeps track of the pods and thats how they can perform health checks on the pods**


---- its not likely to deal with stuff by yourself -----
Why use the EndPointSlice instead of the old EndPoint 
EndPointSlice: when there are very big number of ips it makes something called sharding it's a mechanism used in databases when its size increase, which is to divide data(ips) into shards (أجزاء) (slices )each shard will carry a number of ips that's was not the case in Endpoint (old version) that was used by kubernetes service when the number of pods increases it may cause bottlenecks  

**Constant over all service types** 
**kubeProxy (front-end of service)** 
--> reads the ip addresses from the EndPointSlice and routes traffic to them, 
**so routing rules in kubeProxy on a worker node is configured based on the Running kubernetes Service**

When a Pod fails its **readiness probe**, it is **marked as "not ready"**. The **Service removes the failed pod out of the available pods pool so kube-proxy won't find its ip in the EndPointSlice so traffic will be founded** to that Pod.

**EndPointSlice (back-end of service)** 
--> has load-balancing role based on the ip addresses it reads from EndPointSlice


------------

