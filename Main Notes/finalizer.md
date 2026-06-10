---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[pod]]"
  - "[[namespace]]"
against:
  - "[[node]]"
reference_guides:
  - "[[Reference Notes/0-2_cluster_architecture_and_components.md]]"
tags:
  - kubernetes/metadata
  - status/completed
---

# Finalizer

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > infra > **Finalizer**

---

## 🎯 Purpose (Why it is used)
Finalizers are keys in an object's metadata that notify the Kubernetes control plane to block the hard deletion of a resource until target cleanup actions are completed. They ensure that dependencies are cleaned up and prevent resource leaking.

---

## ⚙️ Functionality (What it is doing)
*   **Deletion Blocking:** When a delete command is issued, the API server updates the resource with a `metadata.deletionTimestamp` but keeps it in `etcd` as long as finalizers are present.
*   **Cleanup Execution:** Controllers monitor objects with deletion timestamps and finalizers, execute their required cleanup scripts (e.g. freeing storage or unlinking resources), and remove their finalizer keys.
*   **Garbage Collection Trigger:** Once the finalizers list is empty (`[]`), the API server permanently purges the object from the cluster state.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **API Server Lifecycle:** Blocks the `DELETE` API call sequence from finalizing.
*   **Controller Coordination:** Enables controllers (like Namespace Controller or Volume Controller) to gracefully reconcile dependent states before the parent record vanishes from `etcd`.

---

## 🧩 Problem Solver (What problem it solves)
Without finalizers, deleting a parent resource (like a PVC) would immediately remove it from `etcd`, leaving background storage allocations orphaned in the cloud provider or blocking pods that are still trying to read/write to the volume. Finalizers solve this by establishing safe deletion gates.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Safe Resource Reclamation:** Associated physical infrastructure (like cloud persistent volumes) is properly de-provisioned.
*   **Orderly Cluster Demolition:** Deleting namespaces clean up all underlying objects sequentially without dangling dependencies.

---

## 🔴 Failure Impact (What will happen without it)
*   **Resource Leaks:** Orphaned volumes, persistent routes, and cloud load balancers.
*   **Stuck Deletions:** If a controller responsible for processing a finalizer is down or misconfigured, the resource will remain stuck in a `Terminating` state indefinitely until the finalizers are manually patched out.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Finalizer**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[finalizer]]
SORT file.name ASC
```
