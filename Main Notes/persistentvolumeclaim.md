---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: storage
domains:
  - "kubernetes"
related_concepts:
  - "[[persistentvolume]]"
  - "[[storageclass]]"
against: []
reference_guides:
  - "[[Reference Notes/09_storage_mechanics_and_csi.md]]"
tags:
  - kubernetes/storage
  - status/completed
---

# persistentvolumeclaim

**Breadcrumbs:** [[Index|🏠 Index]] > Workloads & Infrastructure > **persistentvolumeclaim**

---

## 🎯 Purpose (Why it is used)
A `PersistentVolumeClaim` (PVC) is a request for storage by a user. It allows developers to request storage size and access modes without knowing the details of the underlying cloud storage infrastructure.

---

## ⚙️ Functionality (What it is doing)
* **Storage Request Specification:** Requests specific storage sizes (e.g. `10Gi`) and access modes.
* **Volume Binding Selector:** Automatically searches for and binds to an available `PersistentVolume` that matches the request criteria.
* **Dynamic Provisioning Trigger:** If no manual PV is available, it requests a `StorageClass` to provision one dynamically.
* **Deletion Protection:** Uses the `kubernetes.io/pvc-protection` finalizer to prevent deleting the PVC if a running Pod is currently using it.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **Namespaced Claim:** Unlike PVs, PVCs are namespaced resources, allowing developers to allocate storage inside their own environments.
* **Pod Mount:** Pods reference the PVC in their `spec.volumes` block to mount the volume.

---

## 🧩 Problem Solver (What problem it solves)
* **Separation of Concerns:** Solves the division of labor. System administrators manage PV storage pools and StorageClasses, while developers simply claim storage space using PVCs without needing cloud credentials.
* **Automated Provisioning:** Solves manual storage setup delays.

---

## 🟢 Operational Impact (What will happen with it operating)
* Developers request storage on-demand.
* Volumes are automatically created, formatted, and mounted to pods at launch.

---

## 🔴 Failure Impact (What will happen without it)
* Developers must contact cluster administrators to manually provision host paths or cloud disks for every single pod deployment, causing significant rollout delays.
* Self-service storage allocations are blocked.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **persistentvolumeclaim**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[persistentvolumeclaim]]
SORT file.name ASC
```
