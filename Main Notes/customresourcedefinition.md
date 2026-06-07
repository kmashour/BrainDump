---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[operator-pattern]]"
  - "[[api-aggregation]]"
against:
  - "[[configmap]]"
reference_guides:
  - "[[Reference Notes/16_kubernetes_api_extension_and_operators.md]]"
tags:
  - kubernetes/extending
  - status/completed
---

# CustomResourceDefinition

**Breadcrumbs:** [[0-Index|🏠 Index]] > infra > **CustomResourceDefinition**

---

## 🎯 Purpose (Why it is used)
A **CustomResourceDefinition (CRD)** allows cluster administrators to extend the Kubernetes API by registering new, custom object types. Once defined, users can interact with these custom objects using `kubectl` and API client libraries.

---

## ⚙️ Functionality (What it is doing)
*   **API Registration:** Registers new resource groups, kinds, and versions in the API discovery tree.
*   **Validation enforcement:** Uses OpenAPI v3 schemas to validate input payloads prior to storage.
*   **Subresource Activation:** Supports `/status` (decoupling spec/status writes) and `/scale` (enabling autoscaling bindings).

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **API Server Integration:** Requests targeting the custom path are processed directly by the primary `kube-apiserver` and persisted in the default `etcd` backend.
*   **Discovery Pathing:** Populates paths under `/apis/{group}/{version}/namespaces/{namespace}/{plural}`.

---

## 🧩 Problem Solver (What problem it solves)
Standard Kubernetes resources (Pods, Services, etc.) cannot package domain-specific operations (like running a custom database backup or provisioning a external message broker). CRDs solve this by providing custom data models that can be registered natively with the Kubernetes control plane.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Declarative Extensions:** Developers model complex custom systems as native declarative specs.
*   **Tooling Compatibility:** Works out-of-the-box with standard CLI wrappers (`kubectl get`, `kubectl describe`).

---

## 🔴 Failure Impact (What will happen without it)
*   **Extensibility Blocked:** Teams must rely on ConfigMaps or databases outside the cluster to store custom metadata, losing native API validation.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **CustomResourceDefinition**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[customresourcedefinition]]
SORT file.name ASC
```
