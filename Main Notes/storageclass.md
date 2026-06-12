---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: storage
domains:
  - "kubernetes"
related_concepts:
  - "[[persistentvolume]]"
  - "[[persistentvolumeclaim]]"
against: []
reference_guides:
  - "[[Reference Notes/0-8_storage_mechanics_and_csi.md]]"
tags:
  - kubernetes/storage
  - status/completed
---

# storageclass

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Workloads & Infrastructure > **storageclass**

---

## 🎯 Purpose (Why it is used)
A `StorageClass` defines a "profile" or "tier" of storage (e.g. SSD, HDD, high-IOPS). It automates dynamic volume provisioning, mapping developer claims (PVCs) to cloud or local storage providers on demand.

---

## ⚙️ Functionality (What it is doing)
* **Dynamic Provisioner Router:** Points to a CSI driver (e.g. `ebs.csi.aws.com` or local provisioners) to call API endpoints for creating storage disks.
* **Volume Binding Modes:**
  - `Immediate`: Creates the disk immediately when the PVC is created. Can lead to scheduling failures if the volume is placed in a availability zone different from the node where the pod is scheduled.
  - `WaitForFirstConsumer`: Delays disk creation until the Pod using the PVC is scheduled. Enables **Topology-Aware Scheduling**, ensuring the storage volume is created in the same zone as the assigned node.
* **Expansion Rule Enforcer:** Sets `allowVolumeExpansion` to `true` to permit online resizing.

---

## 🏛️ Architectural Context (How it fits in the architecture)
* **Storage Template Engine:** Sits at the cluster level. Developers reference the class by name in their PVC `spec.storageClassName`.
* **CSI Controller:** Coordinates with out-of-tree CSI plugin sidecars (like `external-provisioner` and `external-resizer`) to provision or resize volumes.

---

## 🧩 Problem Solver (What problem it solves)
* **Manual Volume Setup Bottleneck:** Solves administrative scaling limits. Administrators do not need to create physical block devices and PV manifests in advance; they define a StorageClass template once, and K8s provisions disks automatically.
* **Mismatched Availability Zone Failures:** Solves AZ mismatch crashes using `WaitForFirstConsumer` scheduling.

---

## 🟢 Operational Impact (What will happen with it operating)
* Persistent Volumes are provisioned dynamically when PVCs are requested.
* Developers can request fast or cheap storage classes depending on application tiers.

---

## 🔴 Failure Impact (What will happen without it)
* Dynamic provisioning is disabled; administrators must manually provision every PV in advance.
* Auto-scaling stateful applications (like replica database pods in StatefulSets) cannot scale dynamically since new ordinal claims will hang indefinitely in `Pending` state.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **storageclass**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND (contains(parent_concept, this.file.link) OR icontains(string(parent_concept), this.file.name))
SORT file.name ASC
```
