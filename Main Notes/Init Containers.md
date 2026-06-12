---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/pods/init-containers/"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/pod
---

# pod - Init Containers

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[pod]] > [[pod-deeper]] > **Init Containers**

---

## 📑 1. What is an Init Container?
Init containers run before app containers start in a Pod. They are typically used to perform setup tasks (e.g. running migrations, setting file permissions, or waiting for dependencies) and must run to completion successfully.

---

## ⚙️ 2. Execution Flow and Rules
* **Sequential Run:** Init containers run one at a time, in order. The next init container starts only after the previous one exits successfully (exit code 0).
* **Blocking Main Containers:** Main application containers start only after all init containers have completed.
* **Failure Handling:** If an init container fails, the Kubelet restarts the Pod (unless `spec.restartPolicy` is set to `Never`).

---

## 🔬 3. Manifest Example
Wait for a database service to be ready before launching the application:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  initContainers:
  - name: wait-db
    image: busybox:1.36
    command: ['sh', '-c', 'until nc -z -w 2 db-service 5432; do echo waiting for db; sleep 2; done']
  containers:
  - name: app
    image: my-app:latest
```

*Read more in [[Reference Notes/0-5_containers_runtimes_and_lifecycle.md#4-init-containers-lifecycle-flow]]*\n