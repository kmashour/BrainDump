---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[customresourcedefinition]]"
against:
  - "[[customresourcedefinition]]"
reference_guides:
  - "[[Reference Notes/0-15_kubernetes_api_extension_and_operators.md]]"
tags:
  - kubernetes/extending
  - status/completed
---

# API Aggregation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > infra > **API Aggregation**

---

## 🎯 Purpose (Why it is used)
**API Aggregation** (via `APIService` objects) allows developers to integrate custom API servers (Extension API Servers) directly behind the primary `kube-apiserver`. This enables exposing custom APIs that require unique storage, validation, or business logic.

---

## ⚙️ Functionality (What it is doing)
*   **Request Routing:** Registers API path blocks under `/apis/{group}/{version}`. When a client requests this path, the primary server proxies the HTTP traffic to the extension server.
*   **Custom Validation/Storage:** Bypasses `etcd` storage constraints, allowing the extension server to parse requests dynamically or write to alternate backends (e.g. database engines, custom datastores).

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Proxy Pattern:** The primary `kube-apiserver` acts as the single gateway router, verifying authentication and authorization before proxying requests to the extension server.
*   **Aggregator Registration:** Configured using the `apiregistration.k8s.io` group.

---

## 🧩 Problem Solver (What problem it solves)
While CRDs are simple, they are restricted to standard OpenAPI schemas and mandatory `etcd` persistence. If a team needs to implement dynamic version translation, complex multi-object validation hooks, or query an external system in real-time, CRDs are insufficient. API Aggregation solves this by giving developers complete control over the HTTP request handler.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Extended API Features:** Exposes advanced custom resources (e.g., Metrics Server exposing `/apis/metrics.k8s.io`).
*   **Client Transparency:** Clients use standard client tools (`kubectl`) to interact with custom services without knowing they are backed by a separate server.

---

## 🔴 Failure Impact (What will happen without it)
*   **No Extension APIServer routing:** Custom metrics collections and advanced API server additions cannot run.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **API Aggregation**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
---
*Read more in [0-15_kubernetes_api_extension_and_operators.md](../Reference%20Notes/0-15_kubernetes_api_extension_and_operators.md#5-api-server-aggregation)*
