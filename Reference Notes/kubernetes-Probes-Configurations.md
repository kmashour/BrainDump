---
tags:
  - kubernetes
Type: Reference Note
source: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
page: 
links: 
flogetzzel:
---

https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/


Pod life cycle:
 1- Pending: the pod is waiting to be scheduled on a node
 2- Running: the pod is running on a node
 3- Succeeded: the pod is terminated successfully
 4- Failed: the pod is terminated with an error
 5- Unknown: the pod is in an unknown state
 
==================================================================

Pod Conditions:
 1- PodScheduled: the pod is scheduled on a node
 2- Initialized: the pod is initialized
 3- ContainersReady: the containers in the pod are ready to serve the requests
 4- Ready: the pod is ready to serve the requests



==================================================================

Pod status:
 1- Running: the pod is running on a node
 2- Terminating: the pod is terminating
 3- Terminated: the pod is terminated


<======================= Readiness Probes =======================>
Readiness Probe: is a probe that is used to check if the pod is ready to serve the requests or not 
 1- exec: is a probe that is used to check if the pod is ready to serve the requests by executing a command in the pod
 2- httpGet: is a probe that is used to check if the pod is ready to serve the requests by sending an http request to the pod
 3- tcpSocket: is a probe that is used to check if the pod is ready to serve the requests by sending a tcp request to the pod


<======================= Liveness Probes =======================>
Liveness Probe: is a probe that is used to check if the pod is alive or not (if the pod is still running or not)

 1- exec: is a probe that is used to check if the pod is alive or not by executing a command in the pod
 2- httpGet: is a probe that is used to check if the pod is alive or not by sending an http request to the pod
 3- tcpSocket: is a probe that is used to check if the pod is alive or not by sending a tcp request to the pod
 
<===================== Common Probe Prameters ====================>


 1- initialDelaySeconds: the time that the pod will wait before starting the probe (default value is 0)
 2- periodSeconds: the time that the pod will wait before starting the next probe (default value is 10)
 3- timeoutSeconds: the time that the pod will wait before the probe is considered as failed (default value is 1)
 4- successThreshold: the number of times that the probe should be successful before the pod is considered as ready  
 (default value is 1)
 5- failureThreshold: the number of times that the probe should be failed before the pod is considered as not ready 
 (default value is 3)
 
 Kubernetes treats the container as unhealthy and triggers a restart for that specific container. The kubelet honors the setting of `terminationGracePeriodSeconds` for that container. For a failed readiness probe, the kubelet continues running the container that failed checks, and also continues to run more probes; because the check failed, the kubelet sets the `Ready` on the Pod to `false`.