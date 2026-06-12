---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: storage
domains:
  - "kubernetes"
related_concepts:
  - "[[persistentvolumeclaim]]"
  - "[[storageclass]]"
against:
  - "[[hostpath]]"
  - "[[emptydir]]"
reference_guides:
  - "[[Reference Notes/0-8_storage_mechanics_and_csi.md]]"
tags:
  - kubernetes/storage
  - status/completed
---

# persistentvolume

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Workloads & Infrastructure > **persistentvolume**

---

## 🎯 Purpose (Why it is used)
A `PersistentVolume` (PV) represents a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using a StorageClass. It has a lifecycle independent of any individual Pod that uses the PV.

---

## ⚙️ Functionality (What it is doing)
* **Storage Abstraction:** Wraps physical disks (AWS EBS, NFS, Local LVM, hostPath) into a standard Kubernetes API resource.
* **Access Control:** Enforces access modes (`ReadWriteOnce`, `ReadOnlyMany`, `ReadWriteMany`, `ReadWriteOncePod`).
* **Lifecycle Reclaim Governance:** Defines what happens to the underlying disk after the claim is deleted:
  - `Retain`: Keeps data on disk; administrator must recover it manually.
  - `Delete`: Automatically wipes and deletes the physical storage volume.
  - `Recycle`: Performs basic scrub (`rm -rf`) (Deprecated).

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **Cluster Resource:** PVs are cluster-level resources, meaning they do not belong to namespaces. They are bound to namespaced `PersistentVolumeClaims` (PVCs).
* **CSI Integration:** Communicates with host storage arrays and cloud APIs via the local container storage driver (CSI).

---

## 🧩 Problem Solver (What problem it solves)
* **Data Persistence:** Solves the ephemeral container storage problem. If a database container crashes or is rescheduled, its data remains safe on the PersistentVolume and can be re-attached.
* **Storage Detach/Attach Automation:** Decouples storage management from pod scheduling.

---

## 🟢 Operational Impact (What will happen with it operating)
* Stateful applications store transactions, databases, and logs safely on persistent disks.
* PV allocations are visible to administrators for capacity planning.

---

## 🔴 Failure Impact (What will happen without it)
* All container data is ephemeral; restarting a container or rescheduling a pod obliterates all local changes, database files, and configuration updates.
* Stateful applications cannot run in the cluster.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **persistentvolume**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND (contains(parent_concept, this.file.link) OR icontains(string(parent_concept), this.file.name))
SORT file.name ASC
```
