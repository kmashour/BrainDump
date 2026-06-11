---
tags:
  - kubernetes
Type: Reference Note
source: "[[Kubernetes-Tooling]]"
page: 
Date: 2025-04-17T10:10:00
deadline: 
status:
---
```
kind create cluster
```
Default --> kind
To specify another image use the 
--image flag –> kind create cluster --image=....

```
kubectl cluster-info --context kind-kind
```


--------------------
kubeconfig defines how kubectl communicate with kubernetes clusters 

cluster --> kubernetes can connect to 

Authentication means (users) --> credentials to authenticate users who can access my cluster 

contexts --> defines the authorizations a user can have 
combo of :: clusters + users + namespace(optional)



By default, the cluster access configuration is stored in ${HOME}/.kube/config if $KUBECONFIG environment variable is not set.

![[Screenshot from 2025-04-18 10-09-37.png]]

or

```
kubectl --kubeconfig=/path/to/your/config ...
```


![[Screenshot from 2025-04-17 23-19-30 1.png]]




For the KUBECONFIG: 
- Identify cluster name 
- Identify the endpoint url i want to connect to
- Set the certificate authentication for the first time only and it should be a certificate authentication after that we could Active Directory on Azure cloud or any other method
- choose context ====> user + cluster




![[Screenshot from 2025-04-17 23-50-19 1.png]]


**How CA verify the server for the first time  ???**
You can also use `insecure-skip-tls-verify: true` (not recommended for prod)--> optional

**Core of Kubernetes authentication and TLS trust**
Kind spins up a Kubernetes cluster inside Docker containers. It uses `kubeadm` internally to bootstrap the cluster, so the **certificate generation and authentication mechanism** is the same, just tucked away in containers instead of your host filesystem. ????




