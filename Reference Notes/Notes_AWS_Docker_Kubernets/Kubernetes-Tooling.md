---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: 
Date: 2025-04-17T22:30:00
deadline: 
status: true
---
We will address two ways to install kubernetes cluster on our machine , data centers , rassberypi. There are more ways more ways but we will only focus on two them 

**But we need to install kubectl** , 
The Kubernetes command-line tool,allows you to run commands against Kubernetes clusters. You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs.

API-server understands http and Restful api kubectl abstract all that shit and communicate with the api-servers through http and Restful api!!! developers are exposed to Restful api so its supposed to be easier, so using kubectl could make it more understandable 

kubectl is like any package from kubernetes eco-system developed with GO lang 

we can install it by 
- **package manager** 
- Binary file (no dependencies) its written in GO

**we will use curl**

#kubernetes_Tooling_Note 
make sure to move kubectl to /usr/local/bin in order to be able to use its commands without having to write down the full path 
**mv kubectl /usr/local/bin**

Give execute permission to the kubectl 
chmod +x /usr/local/bin/kubectl

**Kubernetes cluster exactly means the API-server** which is End point of kubernetes cluster, through it we can configure it and gain access to the cluster......

```
kubectl version --client
```

--client --> kubectl version will automatically try to connect to kubernetes cluster to display its version but to this point we still don't have it 
kubectl can't out-date the API-server maximum of 3 versions it will work but use at your own risk 

https://kubernetes.io/docs/reference/kubectl/

#kubernetes_Iam_your_mystery
because the API-servers has certain shit that Iam yet to understand something related to the url it uses or whatever 

-----
KinD --- Kubernetes in Docker 
kind lets you run Kubernetes on your local computer. This tool requires that you have either **Docker** or **Podman** installed. kind lets you run Kubernetes on your local computer.