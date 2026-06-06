---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[dynamic-resource-allocation]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/security/hardening-guide/dynamic-resource-allocation/"
author: "Kubernetes Authors"
course_title: "Kubernetes Security Hardening"
tags:
  - kubernetes/resource
  - kubernetes/deep-dive
---

# dynamic-resource-allocation - Security Hardening

**Breadcrumbs:** [[Index|🏠 Index]] > [[dynamic-resource-allocation]] > **Security Hardening**

---

## 📑 Least-Privilege RBAC for DRA Status Updates

Dynamic Resource Allocation requires secure permission policies because host-level drivers and controllers must update the allocation state of `ResourceClaims`.
Starting in v1.36, DRA decouples status update permissions into synthetic subresources to restrict unauthorized writes:

*   **`resourceclaims/binding`:**
    *   **Scope:** Controls updates to `status.allocation` and `status.reservedFor`.
    *   **Usage:** Granted to cluster-level resource schedulers (e.g. `kube-scheduler`) and custom allocation controllers.
*   **`resourceclaims/driver`:**
    *   **Scope:** Controls updates to `status.devices`.
    *   **Usage:** Granted to node-level device drivers. Crucially, this check is isolated per-driver to prevent driver A from editing/tampering with devices claimed by driver B.

---

## ⚙️ Node-Aware Verbs for DRA Drivers

To prevent a compromised node-level driver from updating claims on other nodes, the API server enforces specialized node-aware verbs:

1.  **`associated-node:<verb>`:**
    *   **Usage:** Granted to node-local drivers.
    *   **Mechanics:** The API server validates that the requesting driver's node matches the node associated with the target `ResourceClaim`.
2.  **`arbitrary-node:<verb>`:**
    *   **Usage:** Reserved for control-plane or cluster-wide multi-node controllers that manage allocations across the entire cluster.

*Read more in [08_security_and_network_policies.md](../Reference%20Notes/08_security_and_network_policies.md#13-hardening-guide-dynamic-resource-allocation-dra-security)*
