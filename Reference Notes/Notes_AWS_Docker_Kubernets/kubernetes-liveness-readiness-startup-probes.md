---
tags:
  - kubernetes
Type: Reference Note
source: Elfakharny-Kubernetes-Udemy-Course
page: "-"
Date: 2025-04-19T12:32:00
deadline: 
status: 
links:
---
![[pod.Initial-ref.probes.yml]]

Attached Files contains some basic Configuration for Probes from Udemy-Elfakharny 





When we want to run a pod kubernetes as we learned do several process until the pod is up and running 

**but kubernetes is an orchestrator it monitors the container if its healthy** if its running as it should be if it replying to requests (serving the users)

**The thing is** **by default kubernetes** only cares about the container id as long as the id is up and running it deals with the containers as a healthy one and finds no issues with it **so all it monitors is if the process id is active or not**

Web application the process must be active but also the pod should be replying to the requests so from 
**POV kubernetes its up** 
**user its down** 

Kubernetes Health checks 
## Liveness check 

- Liveness probe : 
	- Action : Restart the container
	- life-cycle : As long as the container is running 
	The liveness probe is setup to determine when to restart the container may be experiencing an undefined behavior (ex. deadlocks) in a running container, if an application that was running for so long it may have been fine but at some point it began to crash liveness probe is configured so such behavior can be tackled with that probe and perform a restart action.... 
![[exec-liveness.yaml]]
NOTES ON LIVENESS PROBE !!
 - liveness probe doesn't wait or depend on readiness
 - we can use initial delay seconds if we want to wait before executing liveness probe or use the startup probe  

checks that pod is up **if its fails the action is restart the pod**  
HTTP response code 
2xx ---> ok  
3xx ---> redirect 
4xx and 5xx ---> error  
path: /     -> root of the 
path: /healthy -> end-point for health-checks 
 

Liveness httpGet-Check 
```
spec:
  containers:
    - image: nginx
      name: web 
      ports:
        - containerPort: 80
          name: http
          protocol: TCP
          livenessProbe: #####----> if liveness probe failed the pod will restart....runtime checks
            httpGet:
              path: /healthy  
              port: 8080
              initialDelaySeconds: 5   # default: 0 
              timeoutSeconds: 1        #default:  1
              periodSeconds: 10        #default:  10
              failureThreshold: 3      #default:  3
              successThreshold: 1      #default:  1
```

https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/ Docs
```
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-http
spec:
  containers:
  - name: liveness
    image: registry.k8s.io/e2e-test-images/agnhost:2.40
    args:
    - liveness
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
        httpHeaders:
        - name: Custom-Header
          value: Awesome
      initialDelaySeconds: 3
      periodSeconds: 3

```

The `command` field corresponds to `ENTRYPOINT`, and the `args` field corresponds to `CMD` in some container runtimes.

The /healthz is implemented within the server of aghnost image its an endpoint for health checks

Liveness Exec-Check 
![[exec-liveness.yaml]]



## readiness probe :
  - Action : The pod (container) that fails readiness will be removed from service will not receive traffic
  - life cycle : Readiness probes run on the container during its whole life-cycle.
 Makes sure that the container is ready to receive traffic..
 This is useful when waiting for all the application dependencies like Db connection , loading files the front-end may be live and up but not ready to receive or accept traffic 


Official documentation 
	says that "...the kubelet uses readiness probes to know when a container is ready to start accepting traffic. **A Pod is considered ready when all of its containers are ready**. One use of this signal is to control which Pods are used as backends for Services. When a Pod is not ready, it is removed from Service load balancers ..
	"...applications are temporarily unable to serve traffic... an application might depend on external services ... In such cases, you don't want to kill the application, but you don’t want to send it requests either. Kubernetes provides readiness probes to detect and mitigate these situations. A pod with containers reporting that they are not ready does not receive traffic through Kubernetes Services..."


**failing counts return to zero when the readiness probe exit successfully** 

An app might pass liveness probe but fail readiness probe because it replies to requests in longer time than expected so it up and running and replying (serving) requests but has high latency so its not ready 


Similar to liveness probe 

```yaml
readinessProbe:
  exec:
    command:
    - cat
    - /tmp/healthy
  initialDelaySeconds: 5
  periodSeconds: 5
```



```
 readinessProbe:  ######----> if it fails the pod is labeled out of service no traffic will routed to it...runtime checks
            httpGet:
              path: /healthz
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 10 
```


Sequence when failing Readiness probe 

The full sequence is :

1. pod deletion has been requested
2. `preStop` hook kicks in and `terminationGracePeriodSeconds` countdown starts :
    - if `preStop` hook completes, it sends a `SIGTERM` **which stops the pods**
    - if `preStop` hook isn't finished within `terminationGracePeriodSeconds` countdown, kubelet request 2 extra seconds before sending the `SIGKILL` **which will stops the pod**

![[Pasted image 20250520141729.png]]


## startup probe 
(اشتغل ولا لا containerبشوف ال)
A startup probe verifies whether the application within a container is started. This can be used to adopt liveness checks on slow starting containers, avoiding them getting killed by the kubelet before they are up and running.

If such a probe is configured, it disables liveness and readiness checks until it succeeds.

This type of probe is only executed at startup, unlike liveness and readiness probes, which are run periodically.


**Liveness and readiness probe works after the container starts up** 


```
   #####------> to check if the pod did startup as it should happen only once at startup of the Pod not periodic 
          #if the pod failed startup probe it will restart
          startupProbe:
            httpGet:
              path: / 
              port: 80
            initialDelaySeconds: 5 
            periodSeconds: 10

```




The solution is to set up a startup probe with the same command, HTTP or TCP check, with a `failureThreshold * periodSeconds` long enough to cover the worst case startup time.

```yaml
ports:
- name: liveness-port
  containerPort: 8080

livenessProbe:
  httpGet:
    path: /healthz
    port: liveness-port
  failureThreshold: 1
  periodSeconds: 10

startupProbe:
  httpGet:
    path: /healthz
    port: liveness-port
  failureThreshold: 30
  periodSeconds: 10
```

Thanks to the startup probe, the application will have a maximum of 5 minutes (30 * 10 = 300s) to finish its startup. Once the startup probe has succeeded once, the liveness probe takes over to provide a fast response to container deadlocks. If the startup probe never succeeds, the container is killed after 300s and subject to the pod's `restartPolicy`.

we use a 3rd party tools to check the logs in a GUI to check what pods are failing the logs are internal in kubernetes 
Prometheus
Grafana
DataDog


-----------




Example in the attached yml file in the top 

Combining Liveness and Readiness probes with tcpSocket test type  

tcpSocket:
check if the port is open and that gives initial indication that the service is up but it may have an issue


exec :
Runs a command in the container if its a db pod run a query , list a table , **kubernetes uses exit status** to know if command ran succesfully or not ,  **0-> success exit status > 0 failed** 
![[Screenshot from 2025-04-20 19-40-02.png]]





