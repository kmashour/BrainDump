---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
links: 
flogetzzel:
---
nginx docs and ingress for advanced routing rules and best practices 
web-infrastructure shit !!!!
https://kubernetes.io/docs/concepts/services-networking/ingress/


![[Pasted image 20250421230933.png]]


mainly host based routing :::
![[Pasted image 20250421232429.png]]

-------------  

path based routing ::: 

![[Pasted image 20250421232952.png]]

/api only or /api/xxx/xxx also will be routed to the same service since its type is prefix 

exact path routing :::

if no routing rule is configured to catch a wrong path entered by the end user the load balancer controller will throw an error 

![[Pasted image 20250422002848.png]]

Implementation-Specific (controller default)
![[Pasted image 20250422003025.png]]



Through annotations we could define routing rules but take care that the rules are interpreted differently for every load balancer controller so a complex regex rule may be differently interpreted by different load balancer

nginx annotation 

rewrite the path to / regardless what the user want 
the user and service are abstracted from this its done by the reverse proxy through routing mechanism 

![[Pasted image 20250422003446.png]]