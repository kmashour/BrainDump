---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
related_concepts:
  - "[[pod]]"
  - "[[rbac]]"
  - "[[networkpolicy]]"
against:
  - "[[node]]" # Namespaces offer logical isolation, whereas Nodes offer physical machine/compute boundaries
reference_guides:
  - "[[Reference Notes/0-13_scheduling_logging_and_lifecycle.md]]"
tags:
  - domain/kubernetes
  - status/completed
---

# Namespace

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > infra > **Namespace**

---

## 🎯 Purpose (Why it is used)
A **Namespace** is a logical partition inside a single Kubernetes cluster. It is used to isolate groups of resources (like Pods, Services, and Deployments) for different environments, teams, projects, or tenants, preventing naming collisions and enabling granular resource allocation.

---

## ⚙️ Functionality (What it is doing)
*   **Logical Isolation:** Groups and partitions cluster workloads.
*   **Scope Partitioning:** Defines scope boundaries for resource names (e.g., you can have a Pod named `frontend` in namespace `dev` and another `frontend` in `prod`).
*   **Access Control Boundary:** Serves as the primary scope for RBAC (Role and RoleBinding) policies.
*   **Resource Constraints:** Allows administrators to enforce CPU, Memory, and Storage quotas at the namespace level using `ResourceQuotas` and `LimitRanges`.
*   **System Partitioning (Initial Namespaces):** Out-of-the-box system namespaces:
    *   `default`: Target for workloads defined without an explicit namespace.
    *   `kube-system`: Home for components created by the Kubernetes control plane.
    *   `kube-public`: Auto-created namespace readable by all users (authenticated and unauthenticated), historically used for cluster bootstrap details.
    *   `kube-node-lease`: Contains `Lease` objects associated with node heartbeats for scalability.
*   **Prefix Restrictions:** Users should avoid naming custom namespaces with the `kube-` prefix as it is strictly reserved for Kubernetes system components.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **API Server:** Namespaces partition the API path structure. Namespaced API calls target `/api/v1/namespaces/{namespace}/pods` whereas non-namespaced cluster-scoped calls target `/api/v1/nodes`.
*   **etcd:** Key paths in the etcd database are logically separated by namespace names (e.g., `/registry/pods/dev/my-pod`).
*   **DNS:** Services within a namespace get DNS records scoped to that namespace (e.g., `my-service.my-namespace.svc.cluster.local`).

---

## 🧩 Problem Solver (What problem it solves)
Without Namespaces, multiple teams sharing the same cluster would experience name collisions, easily delete each other's resources, and exhaust cluster-wide resources (CPU, Memory). Namespaces solve this by offering virtual cluster slices with native access controls and resource boundaries.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Multi-Tenancy:** Multiple teams or environments run safely inside the same physical cluster.
*   **Name Autonomy:** Teams define resource names without coordinating with other teams.
*   **Resource Fairness:** Resource quotas ensure that one namespace does not exhaust all the cluster's compute capacity.

---

## 🔴 Failure Impact (What will happen without it)
*   **Cluster-wide Congestion:** Workload naming conflicts, security authorization leaks, and resource hogging.
*   **Cascading Deletion:** Deleting a Namespace recursively deletes all API resources nested inside it (Pods, Services, Deployments). If a namespace is deleted accidentally, its entire environment is immediately wiped out.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Namespace**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), "namespace")
SORT file.name ASC
```
