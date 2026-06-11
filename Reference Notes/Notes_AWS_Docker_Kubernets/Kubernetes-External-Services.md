---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
links: 
flogetzzel:
---




Creating End-point slice to connect with an external service:

![[../../Attachments/Screenshot from 2025-04-21 09-55-23.png]]

![[../../Attachments/Screenshot from 2025-04-21 09-59-10.png]]

In this type there are no health check like in normal services ClusterIp and NodePort, Because we are using a custom endpoint slice 

The custom endpoint have Ip addresses it will do round robin between them  


External Name Service :


![[../../Attachments/Screenshot from 2025-04-21 10-04-27.png]]

I just redirect to the external service through a fully qualified domain name and all the load balancing and health checks is from the other side.....
from inside the cluster all i need is to use is the service name external-db and it will redirect me to the external service it configured with which is the URL db.external.net

