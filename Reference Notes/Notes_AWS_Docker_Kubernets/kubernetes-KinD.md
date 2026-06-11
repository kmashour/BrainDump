---
tags:
  - kubernetes
Type: Reference Note
source: 
page: "-"
Date: 2025-04-19T13:09:00
deadline: 
status:
---
KinD --> kubernetes in Docker 

Docker for Desktop (install a a lite weight vm to run linux so we can run Docker) as we know it can be installed on linux 
we will use it to install kubernetes and it automatically sets up my cluster but this approach is mostly used with windows/MacOS 

In MacOS / linux we can use **KinD although some people like minikube but KinD installs kubernetes cluster in a docker container its very lite weight** 

through KinD I can make complex scenario multi node cluster unlike minikube and docker for desktop which just one node and it combines master and work nodes in one virtual machine (node) and as we said thats fine **but in complex or scenarios with special requirements like affinity and anti-affinity we might need to have more control over our cluster nodes**......

KinD is use by the developers of kubernetes to test new features 

KinD can create multi-node cluster through yml file to config what we need 

we can install it either using a package manager
=> **homebrew**
or just install the Binaries build and move it to /bin

```
kind create cluster 
```
You are set here to run 

```
kubectl get nodes 
```

(by default, or without any config), **Kind creates a single-node Kubernetes cluster**, and that node is both:
- the **control plane** (runs kube-apiserver, etcd, scheduler, controller-manager), and    
- the **worker node** (can run pods, though it's technically a control-plane-only node).

- Whether you have **worker nodes** or just a **control plane node** in kind, the **kubelet**, **kube-proxy**, and **containerd** will all run on the node, because kind simulates the entire Kubernetes node setup within Docker containers.
- The **control plane components** (`kube-apiserver`, etc.) will also run as containers in kind.

So you can think of `kind-control-plane` as:
> 🧠 **The brain of the cluster** (control-plane)  
> 💪 **And also one of the muscles** (a node that can run pods)


For more Cluster related info 
```
kubectl cluster-info --context kind-kind 
```



**To create more nodes within the cluster :** 
```
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
  - role: worker
```

```
kind create cluster --config cluster-config.yaml
```

when you return look up for a command for faster implementation 



For multi-node configurations 
https://kind.sigs.k8s.io/docs/user/quick-start 


