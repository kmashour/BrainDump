---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/pod
  - kubernetes/deep-dive
---

# pod - Health Probes (liveness readiness startup)

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[pod]] > [[pod-deeper]] > **Health Probes**

---

## 📑 1. The Three Probe Types

* **`startupProbe`:** Checks if the application within the container has started. Disables all other probes until it succeeds. If it fails, the container is restarted.
* **`livenessProbe`:** Checks if the container is alive. If it fails, Kubelet kills the container and restarts it according to the restartPolicy.
* **`readinessProbe`:** Checks if the container is ready to accept traffic. If it fails, the Pod is removed from all matching Services' Endpoint lists, preventing traffic routing.

---

## ⚙️ 2. Action Mechanisms (Probing Actions)
Probes check containers using one of four handlers:
* **`exec`:** Runs a command inside the container. Succeeds if exit code is `0`.
* **`httpGet`:** Sends an HTTP GET request to the container. Succeeds if status code is $\ge 200$ and $< 400$.
* **`tcpSocket`:** Attempts to open a TCP socket port on the container. Succeeds if port is open.
* **`grpc`:** Performs a gRPC health check call.

---

## 🔬 3. Manifest Example
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: probed-pod
spec:
  containers:
  - name: web
    image: nginx:alpine
    livenessProbe:
      httpGet:
        path: /healthz
        port: 80
      initialDelaySeconds: 15
      periodSeconds: 10
      timeoutSeconds: 2
      failureThreshold: 3
    readinessProbe:
      exec:
        command:
        - cat
        - /tmp/ready
      periodSeconds: 5
```

*Read more in [[Reference Notes/0-4_workload_lifecycle_and_healing.md#2-liveness-readiness-and-startup-probes]]*\n