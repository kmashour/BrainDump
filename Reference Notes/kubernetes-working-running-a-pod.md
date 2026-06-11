---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
Date: 2025-04-19T12:31:00
deadline: 
status:
---
In debugging its very handy to monitor and trace the logs of a pod, the logs rely on the implementation of the application that running in pod (container) 

```
kubectl logs -f web 
```

In production its recommended to have a log aggregation system to trace the logs as splunk , **elastic search but for now this will do** 

in multi-container Pods 

```
kubectl logs web -c container-name
```

to execute inside the container inside the running pod 

```
kubectl exec -it web -- date 
kubectl exec -it web -- bash 
```

#kubernetes_best_practice 
**some containers runs a GO program for example so they don't have shell so we use a side-car container to debug the GO container since as we stated that two containers in the same pod share the same file system** 

```
 kubectl get services ===> To check the services in the cluster
 kubectl get all ===> To check all the resources in the cluster              (deployments, pods, services, etc)
 kubectl api-resources ===> To check the api resources that we can use with  kubectl
 kubectl get nodes ===> To check the nodes in the cluster (minikube cluster  has only one node)
 kubectl watch get all ===> To watch the changes in the cluster
 kubectl watch get pod ===> To watch the changes in the pods in the cluster
```

