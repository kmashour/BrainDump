---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[namespace]]"
sub_type: core-concept
source_type: udemy
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
tags:
  - kubernetes/namespace
  - kubernetes/deep-dive
---

# namespace - Logical Isolation

**Breadcrumbs:** [[Index|🏠 Index]] > [[namespace]] > **Logical Isolation**

---

## 📑 Logical Isolation Boundaries

Namespaces divide cluster resources logically, but they do **not** provide physical network isolation or secure container isolation out-of-the-box.

### 1. Resource Types: Namespaced vs. Cluster-Scoped
Not all Kubernetes resources live inside a Namespace.
*   **Namespaced Resources:**
    *   Pods, Deployments, ReplicaSets, StatefulSets, DaemonSets
    *   Services, Ingresses
    *   ConfigMaps, Secrets, PersistentVolumeClaims
    *   ServiceAccounts, Roles, RoleBindings
*   **Cluster-Scoped Resources (Global):**
    *   Nodes
    *   Namespaces
    *   PersistentVolumes, StorageClasses
    *   ClusterRoles, ClusterRoleBindings
    *   CustomResourceDefinitions (CRDs)

To check which resources are namespaced or cluster-scoped:
```bash
# List namespaced resources
kubectl api-resources --namespaced=true

# List cluster-scoped resources
kubectl api-resources --namespaced=false
```

---

## ⚠️ Isolation Fallacies & Security Boundaries

### 1. Network Pathing (No Network Isolation by Default)
A common fallacy is that Pods in the `dev` namespace cannot talk to Pods in the `prod` namespace. By default, **all Pods in a Kubernetes cluster can communicate with each other, regardless of their namespace**.
*   **Mechanism:** The pod overlay network (CNI) routes packets cluster-wide.
*   **Enforcement:** To secure namespaces, you must explicitly apply **NetworkPolicies** to block inter-namespace traffic.

### 2. DNS Resolution across Namespaces
Pods can resolve Services in other namespaces by appending the target namespace name to the service hostname (FQDN format).
*   **Intra-Namespace Query:** `http://database-service`
*   **Cross-Namespace Query:** `http://database-service.prod-namespace.svc.cluster.local`

---

## ⚙️ Operations & Active Context

*   **Temporary Context Switch (using kubectl):**
    ```bash
    kubectl get pods -n dev-ns
    ```
*   **Permanent Context Switch (default namespace change):**
    ```bash
    kubectl config set-context --current --namespace=dev-ns
    ```
*   **Cascading Deletion Danger:**
    Executing `kubectl delete ns dev-ns` triggers a cascading deletion. The API server updates the namespace status to `Terminating`, finalizes nested API components, and permanently purges all Pods, Services, Deployments, and Secrets inside that namespace.

*Read more in [14_scheduling_logging_and_lifecycle.md](../Reference%20Notes/14_scheduling_logging_and_lifecycle.md#1-advanced-scheduling-node-placement)*
