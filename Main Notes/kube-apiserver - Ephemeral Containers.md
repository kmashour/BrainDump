---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-apiserver]]"
sub_type: use-case
sources:
  - "Kubernetes Official Docs"
  - "Newsletter Article: Debugging in K8s"
source_type: documentation
against: []
tags:
  - kubernetes/kube-apiserver
  - kubernetes/deep-dive
---
# kube-apiserver - Ephemeral Containers

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kube-apiserver]] > **Ephemeral Containers**

---

## 🛠️ Ephemeral Containers Subresource (`/ephemeralcontainers`)
Pods are immutable by design, meaning you cannot add or remove containers once a Pod is created. To debug running pods:
* The `/ephemeralcontainers` API subresource bypasses container creation validation.
* Allows `kubectl debug` to inject an administrative helper container directly into a running Pod's namespaces without restarting it.

*Read more in [0-5_containers_runtimes_and_lifecycle.md](../Reference%20Notes/0-5_containers_runtimes_and_lifecycle.md#8-ephemeral-containers-for-debugging)*.
