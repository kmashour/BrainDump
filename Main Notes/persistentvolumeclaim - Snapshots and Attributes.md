---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[persistentvolumeclaim]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/storage/volume-snapshots/"
author: "Kubernetes Authors"
course_title: "Kubernetes Storage Concepts"
against: []
tags:
  - kubernetes/storage
  - kubernetes/deep-dive
---

# persistentvolumeclaim - Snapshots and Attributes

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[persistentvolumeclaim]] > **Snapshots and Attributes**

---

## 📑 Volume Snapshots & Dynamic Performance Scaling

Kubernetes storage provides APIs to take point-in-time snapshots of PVCs and dynamically modify volume parameters (like IOPS or throughput) without application downtime.

### 1. Volume Snapshots
Volume snapshots allow you to back up and clone the state of a `PersistentVolumeClaim` at a specific moment. The process is fully integrated with CSI storage drivers via custom resources:
*   **`VolumeSnapshot` (Namespace-scoped):** The user's request for a snapshot. It specifies the source PVC and the class.
*   **`VolumeSnapshotClass` (Cluster-scoped):** Defines the storage driver, parameters, and the `deletionPolicy` (whether deleting the `VolumeSnapshot` CR deletes the backup on the backend storage).
*   **`VolumeSnapshotContent` (Cluster-scoped):** The actual snapshot resource allocated on the physical storage array.

#### Snapshot Recovery (Restore):
To provision a new volume from a backup, define a new PVC and specify the snapshot as its `dataSource`:
```yaml
spec:
  dataSource:
    name: db-backup-snapshot
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  resources:
    requests:
      storage: 10Gi
```

### 2. Volume Attributes Classes (Dynamic IOPS Tuning)
Introduced to allow the modification of volume properties (e.g., IOPS, latency tiers, throughput) without requiring volume expansion or database restarts.
*   **`VolumeAttributesClass` (v1.34+ GA):** Defines a profile of performance metrics (like target IOPS).
*   **Usage:** PVCs reference this class via `spec.volumeAttributesClassName`. Modifying this reference dynamically triggers the CSI driver to scale performance parameters on the live backend volume.

### 3. Volume Health Monitoring
CSI drivers monitor physical storage arrays and disks for failure events (e.g., partition corruption, storage controller timeout).
*   If a storage failure occurs, the driver logs a warning event (e.g., `VolumeUnhealthy`) on the PVC.
*   Cluster operators can capture this event via a controller to automate database replica failover or Pod rescheduling.

*Read more in [0-8_storage_mechanics_and_csi.md](../Reference%20Notes/0-8_storage_mechanics_and_csi.md#63-volume-snapshots--volumesnapshotclasses)*
