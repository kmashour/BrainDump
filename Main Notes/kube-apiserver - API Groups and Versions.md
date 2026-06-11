---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-apiserver]]"
sub_type: architecture
sources:
  - "Mumshad CKA Course"
  - "Kubernetes Official Docs"
source_type: udemy
tags:
  - kubernetes/kube-apiserver
  - kubernetes/deep-dive
---
# kube-apiserver - API Groups and Versions

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kube-apiserver]] > **API Groups and Versions**

---

## 📁 API Groups and Versioning
The Kubernetes API is divided into logical groups to partition the workspace and scale development:
* **Core Group (`/api/v1`):** Basic resources (Pods, Services, Namespaces, ConfigMaps).
* **Named Groups (`/apis/<group>/<version>`):** Extended features (e.g., `apps/v1` for Deployments, `networking.k8s.io/v1` for Ingresses).
* **Version Stages:**
  - `v1alpha1`: Disabled by default, unstable specs.
  - `v1beta1`: Enabled by default, stable but subject to schema migration.
  - `v1`: Production-ready, backward-compatible.

*Read more in [0-1_kube_api_and_kubectl.md](../Reference%20Notes/0-1_kube_api_and_kubectl.md#2-api-groups-and-versioning)*.
