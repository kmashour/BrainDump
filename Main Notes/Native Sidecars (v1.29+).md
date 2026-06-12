---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#sidecar-containers"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/pod
  - kubernetes/deep-dive
---

# pod - Native Sidecars (v1.29+)

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[pod]] > [[pod-deeper]] > **Native Sidecars**

---

## 📑 1. What is a Native Sidecar?
Before v1.29, sidecar containers (like log shippers or proxy sidecars) were run as standard containers. This caused issues in Jobs because the job could never terminate if the sidecar container kept running indefinitely.

Kubernetes v1.29 introduced native sidecar support by extending `initContainers` with a restart policy of `Always`.

---

## ⚙️ 2. Execution Flow
* **Parallel Bootstrapping:** A native sidecar container starts and initializes, but instead of blocking, the Kubelet starts the next init container immediately after the sidecar enters a running state.
* **Job Graceful Completion:** When the main task containers finish execution, the Kubelet automatically terminates the native sidecar containers, allowing the Job to exit and transition to `Succeeded`.

---

## 🔬 3. YAML Configuration Spec
Specify `restartPolicy: Always` inside the `initContainers` block:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: proxy-job
spec:
  initContainers:
  - name: vault-agent-sidecar
    image: vault:1.15
    restartPolicy: Always # <-- Marks this container as a native sidecar
  containers:
  - name: batch-processor
    image: busybox
    command: ["sh", "-c", "echo task complete"]
```

*Read more in [[Reference Notes/0-5_containers_runtimes_and_lifecycle.md#5-sidecar-containers-and-native-sidecars-v129]]*\n