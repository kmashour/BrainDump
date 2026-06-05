---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "kubernetes"
related_concepts:
  - "[[rbac]]"
  - "[[pod]]"
against: []
reference_guides:
  - "[[Reference Notes/08_security_and_network_policies.md]]"
tags:
  - kubernetes/security
  - status/completed
---

# serviceaccount

**Breadcrumbs:** [[Index|🏠 Index]] > Workloads & Infrastructure > **serviceaccount**

---

## 🎯 Purpose (Why it is used)
A `ServiceAccount` provides an identity for processes running inside a Pod. When a container needs to communicate with the local `kube-apiserver`, it authenticates using its ServiceAccount credentials rather than human credentials.

---

## ⚙️ Functionality (What it is doing)
* **Identity Provisioning:** Creates a machine identity resource within a namespace.
* **Token Distribution:** In modern Kubernetes (v1.22+), Kubelet dynamically mounts a short-lived, auto-rotating token via a projected volume at `/var/run/secrets/kubernetes.io/serviceaccount/token`.
* **RBAC Association:** Serves as a subject inside `RoleBindings` or `ClusterRoleBindings` to grant permissions to the pod process.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **Kubelet Ingestion:** The Kubelet reads the Pod specification, requests tokens from the token API on behalf of the Pod, and mounts them.
* **Token Controller:** A controller inside the `kube-controller-manager` monitors ServiceAccount creation and manages their token lifecycle.

---

## 🧩 Problem Solver (What problem it solves)
* **Secure Pod-to-API Communication:** Solves the challenge of secure machine access to the cluster control plane. Pods (like Prometheus, Ingress controllers, or Helm agents) can authenticate securely without hardcoding static keys.
* **Token Leak Mitigation:** Short-lived tokens (`TokenRequest` API) automatically expire and rotate, preventing attackers from using stolen tokens indefinitely.

---

## 🟢 Operational Impact (What will happen with it operating)
* Inbound API server requests from pods are authenticated and audited.
* Pods can query other cluster resources securely using local clients (like `client-go`).

---

## 🔴 Failure Impact (What will happen without it)
* Pods cannot interact with the cluster API, breaking dynamic components like autoscalers, controllers, and monitoring dashboards.
* Fallback to static secret-based tokens increases token leakage and compromise risks.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **serviceaccount**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[serviceaccount]]
SORT file.name ASC
```
