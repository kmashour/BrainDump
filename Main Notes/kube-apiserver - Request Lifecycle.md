---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-apiserver]]"
sub_type: core-concept
sources:
  - "Mumshad CKA Course"
  - "Kubernetes Official Docs"
tags:
  - kubernetes/kube-apiserver
  - kubernetes/deep-dive
---

# kube-apiserver - Request Lifecycle

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[kube-apiserver]] > **Request Lifecycle**

---

## 🔒 Request Lifecycle Flow
When a request hits the API server, it follows a strict sequence:
1. **Authentication:** Validates identity (Token, Certificate, OIDC).
2. **Authorization:** Validates RBAC permissions (`Role`, `ClusterRole`, `NodeRestriction`).
3. **Mutating Admission Controllers:** Modifies the request if needed (e.g., injecting sidecars or default limits).
4. **Schema Validation:** Verifies structural compliance against OpenAPI specifications.
5. **Validating Admission Controllers:** Checks final object rules before persistence (e.g., checking if namespace exists or quota limits are exceeded).
6. **etcd Storage Commit:** Saves the object definition to the key-value database as a transaction.

*Read more in [01_kube_api_and_kubectl.md](../Reference%20Notes/01_kube_api_and_kubectl.md#a-api-server-request-lifecycle-creation-flow)*.
