---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-apiserver]]"
sub_concepts:
  - "[[API Request Lifecycle]]"
  - "[[API Groups and Versions]]"
  - "[[OpenAPI and explain]]"
  - "[[Watch Mechanism]]"
  - "[[Mixed Version Proxy]]"
  - "[[Admission Controllers]]"
use_cases:
  - "[[Debugging with Ephemeral Containers]]"
external_links:
  - "[Mumshad CKA Course](https://kodekloud.com)"
  - "[Kubernetes Official Docs](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)"
tags:
  - kubernetes/deep-dive
---

# kube-apiserver deeper

**Breadcrumbs:** [[Index|🏠 Index]] > [[kube-apiserver]] > **deeper dive**

---

This note covers the deep architectural mechanisms, configurations, and subresources specific to the **kube-apiserver**.

---

## 🔒 1. API Server Request Lifecycle
* **Authentication:** Validates identity (Token, Certificate, OIDC).
* **Authorization:** Validates RBAC permissions (`Role`, `ClusterRole`, `NodeRestriction`).
* **Mutating Admission Controllers:** Modifies the request if needed (e.g., injecting sidecars or default limits).
* **Schema Validation:** Verifies structural compliance against OpenAPI specifications.
* **Validating Admission Controllers:** Checks final object rules before persistence (e.g., checking if namespace exists or quota limits are exceeded).
* **etcd Storage Commit:** Saves the object definition to the key-value database as a transaction.

*Read more in [01_kube_api_and_kubectl.md](../Reference%20Notes/01_kube_api_and_kubectl.md#a-api-server-request-lifecycle-creation-flow)*.

---

## 📁 2. API Groups and Versioning
The Kubernetes API is divided into logical groups to partition the workspace and scale development:
* **Core Group (`/api/v1`):** Basic resources (Pods, Services, Namespaces, ConfigMaps).
* **Named Groups (`/apis/<group>/<version>`):** Extended features (e.g., `apps/v1` for Deployments, `networking.k8s.io/v1` for Ingresses).
* **Version Stages:**
  - `v1alpha1`: Disabled by default, unstable specs.
  - `v1beta1`: Enabled by default, stable but subject to schema migration.
  - `v1`: Production-ready, backward-compatible.

*Read more in [01_kube_api_and_kubectl.md](../Reference%20Notes/01_kube_api_and_kubectl.md#2-api-groups-and-versioning)*.

---

## 🔍 3. OpenAPI Schemas & kubectl explain
The API server contains the full OpenAPI schema loaded into memory. This schema dictates what fields are valid for every single API Object.
* **kubectl explain:** Directly queries the schema from the API server to get documentation and structures (e.g., `kubectl explain pod.spec.containers`).
* **OpenAPI Specs:** Exposed at `/openapi/v2` and `/openapi/v3` endpoints.

*Read more in [01_kube_api_and_kubectl.md](../Reference%20Notes/01_kube_api_and_kubectl.md#3-openapi-schema--kubectl-explain)*.

---

## 📡 4. The Watch Mechanism (`-w`)
Instead of polling the API server periodically (which scales poorly), clients use the HTTP Watch mechanism:
* The client opens a single persistent HTTPS connection.
* The API server streams state events (Added, Modified, Deleted) in chunked JSON messages as they occur in `etcd`.
* Essential for controllers and the scheduler to react instantly to cluster changes.

*Read more in [01_kube_api_and_kubectl.md](../Reference%20Notes/01_kube_api_and_kubectl.md#4-the-watch-mechanism--w)*.

---

## 🔀 5. Mixed Version Proxy
During cluster upgrades, different API servers inside the Control Plane can run different versions (version skew):
* If a request lands on a server that doesn't support the version of the requested resource, the API server proxies the request to another control plane node that does support it.
* Ensures zero-downtime upgrades of the Control Plane.

*Read more in [02_cluster_architecture_and_components.md](../Reference%20Notes/02_cluster_architecture_and_components.md#3-high-availability-ha-control-plane-mechanics)*.

---

## 🛠️ 6. Ephemeral Containers Subresource (`/ephemeralcontainers`)
Pods are immutable by design, meaning you cannot add or remove containers once a Pod is created. To debug running pods:
* The `/ephemeralcontainers` API subresource bypasses container creation validation.
* Allows `kubectl debug` to inject an administrative helper container directly into a running Pod's namespaces without restarting it.

*Read more in [05_containers_runtimes_and_lifecycle.md](../Reference%20Notes/05_containers_runtimes_and_lifecycle.md#8-ephemeral-containers-for-debugging)*.
