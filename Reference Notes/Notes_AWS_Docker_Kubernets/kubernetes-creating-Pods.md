---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
Date: 2025-04-19T15:40:00
deadline: 
status:
---
![[pod.Initial-ref.probes 1.yml]]

A pod is a kubernetes Resource 


Imperative approach : 
```
kubectl run web --image=nginx (imperative)
```

Declarative approach :
- Through a document a yml documents

---> pod.yml (manifest)
``` yml
apiVersion: v1
kind: Pod
metadata:
  name: web 
spec:
  containers: <----- list
    - image: nginx <----- item in list 
      name: web 
      ports:
        - containerPort: 80
          name: http
          protocol: TCP
```

```
kubectl get pods [optional name of pod]
```

kubectl apply -f pod.yml 

kubectl will add all the file contents to a payload and convert it to an http request to the api-server 


WHAT WILL HAPPEN 
- API SERVER VALIDATES THE REQUEST
- THE SCHEDULER DECIDES WHICH NODE IT SHOULD "SCHEDULE" THE POD ON
- THE WORKER NODE KUBELET IS NOTIFIED THAT A POD NEEDS TO LIVE ON THIS NODE SO IT RUNS THE container engine THROUGH THE CONFIGURED RUNTIME (containerd , podman )
- **IF the scheduler failed to find a suitable node the pod status becomes pending**
status pending
- it's the selected node can't host more pods 
- all nodes are out of resources and can't add any .,pod 

#kubernetes_pod_debugging_commands   
``` yml
kubectl get pods -o wide
```

#kubernetes_pod_debugging_commands 
```yml
kubectl describe pods [pod name]
```

The event may give insights to error that may happen during the pod creation 
``` yml
kubectl delete pods web 
```