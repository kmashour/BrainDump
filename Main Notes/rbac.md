---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "kubernetes"
related_concepts:
  - "[[serviceaccount]]"
  - "[[kube-apiserver]]"
against:
  - "[[abac]]"
reference_guides:
  - "[[Reference Notes/08_security_and_network_policies.md]]"
tags:
  - kubernetes/security
  - status/completed
---

# rbac

**Breadcrumbs:** [[Index|🏠 Index]] > Workloads & Infrastructure > **rbac**

---

## 🎯 Purpose (Why it is used)
Role-Based Access Control (`RBAC`) is the primary authorization engine in Kubernetes. It regulates access to cluster resources (such as pods, secrets, and nodes) based on the roles assigned to individual users or service accounts.

---

## ⚙️ Functionality (What it is doing)
* **Resource Auditing:** Matches incoming API requests (User + Verb + Resource) against authorization rules.
* **Scope Isolation:**
  - **Namespaced Roles (`Role`/`RoleBinding`):** Grants access to resources within a single namespace.
  - **Cluster-Wide Roles (`ClusterRole`/`ClusterRoleBinding`):** Grants access across all namespaces, non-namespaced resources (like nodes or PVs), and API endpoints (like `/healthz`).
* **Cross-Scope Binding:** Allows binding a `ClusterRole` using a namespaced `RoleBinding` to grant access to namespaced resources without duplicating roles.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **API Server Filter:** Runs as an authorization module inside the `kube-apiserver` (configured via `--authorization-mode=RBAC`).
* **Evaluation Logic:** If multiple authorization modes are active (e.g. `Node,RBAC`), Kubernetes evaluates them in order; a request is permitted as soon as any module grants access.

---

## 🧩 Problem Solver (What problem it solves)
* **Privilege Escalation Prevention:** Solves the risk of accidental or malicious system modifications by ensuring developers and automated agents only hold the minimum permissions required for their tasks (Least Privilege).
* **Automated Permission Audits:** Allows administrators to test query permissions using `kubectl auth can-i`.

---

## 🟢 Operational Impact (What will happen with it operating)
* Developers are isolated into namespaces and restricted from editing cluster configurations.
* Automated CI/CD agents deploy workloads without holding root administrative access.

---

## 🔴 Failure Impact (What will happen without it)
* If disabled (e.g., using `AlwaysAllow`), any user or container with network access to the API server can read secrets, deploy malicious pods, or delete the entire cluster database.
* The cluster violates basic compliance and security isolation rules.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **rbac**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[rbac]]
SORT file.name ASC
```
