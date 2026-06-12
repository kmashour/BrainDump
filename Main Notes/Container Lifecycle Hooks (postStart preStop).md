---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/"
author: "Kubernetes Documentation"
tags:
  - kubernetes/pod
---

# pod - Container Lifecycle Hooks (postStart preStop)

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[pod]] > [[pod-deeper]] > **Lifecycle Hooks**

---

## 📑 1. Lifecycle Hook Entrypoints
Kubernetes allows you to register hooks to execute code at specific points in the container's lifecycle:

### A. postStart
Executes immediately after a container is created.
* **Non-blocking:** It executes asynchronously with the container's main `ENTRYPOINT`. However, the Pod's status remains `Pending` until the hook completes.

### B. preStop
Executes synchronously immediately before a container is terminated due to an API request or eviction.
* **Blocking:** The container is sent the `SIGTERM` signal only after the `preStop` hook completes. If the hook is still running when the termination grace period expires, the container is forcibly killed (`SIGKILL`).

---

## ⚙️ 2. Configuration Example
Run a graceful shutdown script before stopping Nginx:
```yaml
spec:
  containers:
  - name: web
    image: nginx:alpine
    lifecycle:
      preStop:
        exec:
          command: ["/usr/sbin/nginx", "-s", "quit"]
```

---

## 🔬 3. CKA Implementation Trick
Use `preStop` to ensure traffic drains cleanly from endpoint lists:
```yaml
    lifecycle:
      preStop:
        exec:
          command: ["sh", "-c", "sleep 10"] # <-- Gives kube-proxy time to update iptables
```

*Read more in [[Reference Notes/0-13_scheduling_logging_and_lifecycle.md#4-container-lifecycle-handlers-hooks]]*\n