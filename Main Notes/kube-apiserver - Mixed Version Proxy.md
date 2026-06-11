---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-apiserver]]"
sub_type: use-case
sources:
  - "Kubernetes Official Docs"
  - "CKA Upgrade Guide"
source_type: documentation
tags:
  - kubernetes/kube-apiserver
  - kubernetes/deep-dive
---
# kube-apiserver - Mixed Version Proxy

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kube-apiserver]] > **Mixed Version Proxy**

---

## 🔀 Mixed Version Proxy
During cluster upgrades, different API servers inside the Control Plane can run different versions (version skew):
* If a request lands on a server that doesn't support the version of the requested resource, the API server proxies the request to another control plane node that does support it.
* Ensures zero-downtime upgrades of the Control Plane.

*Read more in [0-2_cluster_architecture_and_components.md](../Reference%20Notes/0-2_cluster_architecture_and_components.md#3-high-availability-ha-control-plane-mechanics)*.
