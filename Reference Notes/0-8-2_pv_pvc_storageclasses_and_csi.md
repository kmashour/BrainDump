---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - kubernetes/storage
  - kubernetes/pv
---

# Module 0-8-2: PersistentVolumes, StorageClasses & Volume Control

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Reference MOC]] > **Module 0-8-2**

---

## 3. Persistent Volumes (PV) & Persistent Volume Claims (PVC)

Kubernetes separates storage infrastructure management from application workload requests.

```
 +------------------------+
 |   Physical Storage     | (NFS, AWS EBS, GCE-PD, Local NVMe)
 +-----------+------------+
             |
             v
 +------------------------+
 |   PersistentVolume     | (Cluster-Scoped, Created by Admin or CSI)
 +-----------+------------+
             ^
             | (Binding Match)
             v
 +------------------------+
 | PersistentVolumeClaim  | (Namespace-Scoped, Created by App Developer)
 +-----------+------------+
             ^
             | (Referenced by Name)
             v
 +------------------------+
 |       Pod Spec         | (Workspace Container)
 +------------------------+
```

- **PersistentVolume (PV):** A cluster-scoped storage resource provisioned by an administrator or dynamically via a StorageClass. It represents the physical backing storage.
- **PersistentVolumeClaim (PVC):** A namespace-scoped request for storage by a user. It specifies capacity, access modes, and storage classes.

---

### A. PV-to-PVC Binding Matching Criteria
Kubernetes automatically matches and binds a PVC to a compatible PV based on these rules:
1. **StorageClass Match:** If the PVC requests a specific `storageClassName`, it will only bind to a PV with the exact same `storageClassName`. If the PVC requests `storageClassName: ""`, it will only bind to PVs that have no storage class specified.
2. **Access Mode Support:** The PV must support *all* access modes requested by the PVC.
3. **Capacity Requirements:** The PV's capacity must be greater than or equal to the capacity requested by the PVC. The control plane selects the smallest available PV that satisfies the size.
4. **Selector Match:** If the PVC specifies a label `selector`, the PV must have matching labels.

#### 1. Conceptual Breakdown: Do PV and PVC Parameters Need to Mirror Each Other?
It is a common logical assumption that a PV and its corresponding PVC must be exact identical mirrors. However, in Kubernetes, they represent two different roles (PV is the physical hardware managed by the administrator; PVC is the request voucher created by the developer).

Here is why they do not require identical parameters:
*   **The Reclaim Policy belongs ONLY to the PV:** The PVC does not care what happens to the underlying disk after it is done using it. The Reclaim Policy (`persistentVolumeReclaimPolicy`) is a hardware lifecycle instruction, so it exists exclusively on the PV.
*   **Capacity is a "Minimum Requirement":** A PVC requesting `50Mi` can bind to a PV of `100Mi`. 
    *   *The 1:1 Binding Lock:* The relationship between a PVC and a PV is strictly **one-to-one**. A single PVC binds to exactly one PV, locking it.
    *   *Wasted Capacity:* If a `50Mi` claim binds to a `100Mi` PV, the remaining `50Mi` is completely inaccessible and wasted. You cannot bind a second `50Mi` claim to the leftover space on that same PV.
    *   *Pod Perspective (`df -h`):* When the PVC is mounted into a Pod, running `df -h` inside the container will reveal the full physical capacity (`100Mi`) of the bound PV. Kubernetes maps the underlying volume filesystem directly, so the container process has access to the full volume limit.
*   **Access Modes require strict matching:** If a PVC requests `ReadWriteOnce`, the PV must advertise support for `ReadWriteOnce`. If the PV only advertises `ReadWriteMany`, the binder will block the matching process, and the PVC will remain stuck in `Pending`.

#### 2. Quick Reference: PV/PVC Parameter Match Grid
| Parameter          | Must Match Exactly? | Binding Rule / Validation                                                              |
| :----------------- | :------------------ | :------------------------------------------------------------------------------------- |
| **Capacity**       | **NO**              | PV capacity must be greater than or equal to PVC request ($\text{PV} \ge \text{PVC}$). |
| **Access Mode**    | **YES**             | PV access modes list must contain all access modes requested by the PVC.               |
| **Storage Class**  | **YES**             | The `storageClassName` strings must match exactly (or both must be empty/unset).       |
| **Reclaim Policy** | **NO**              | Defined strictly on the PV; ignored/not present in PVC specifications.                 |

> [!TIP]
> **CKA Exam Tip - Access Mode Matching:**
> A PVC requesting `ReadWriteOnce` will NOT bind to a PV that *only* lists `ReadWriteMany` in its access modes (and vice versa). The binder requires that the PV supports *all* access modes requested by the PVC. If there is a mismatch, the PVC remains stuck in `Pending`.

---

### B. Binding States Lifecycle
The status of a PV transitions through these states:
- **`Available`:** The PV is healthy, idle, and ready to be bound by a PVC.
- **`Bound`:** The PV has been successfully claimed by a PVC.
- **`Released`:** The bound PVC was deleted, but the PV reclaim policy is `Retain`. The PV retains its data and cannot be claimed by other PVCs.
- **`Failed`:** The automatic cleanup or deletion process failed.

> [!NOTE]
> **Why is my PVC stuck in a `Pending` state?**
> A PVC stays `Pending` if:
> - No PV matches the capacity or access mode requested.
> - The requested `storageClassName` does not exist or has no matching PVs.
> - The StorageClass has its `volumeBindingMode` set to `WaitForFirstConsumer`, meaning the binding is intentionally delayed until a Pod using the PVC is scheduled.

---

### C. Access Modes Reference
Kubernetes supports the following access modes:
* **`ReadWriteOnce` (RWO):** The volume can be mounted as read-write by a single node. (Multiple Pods on the same node can mount the volume).
* **`ReadOnlyMany` (ROX):** The volume can be mounted as read-only by many nodes.
* **`ReadWriteMany` (RWX):** The volume can be mounted as read-write by many nodes (requires network storage like NFS or Ceph).
* **`ReadWriteOncePod` (RWOP):** The volume can be mounted as read-write by a single Pod in the entire cluster. This ensures absolute exclusivity.

---

### D. Reclaim Policies
The `persistentVolumeReclaimPolicy` field determines what happens to the PV and underlying storage when the PVC is deleted.

#### 1. Retain (Manual Cleanup Flow)
The PV remains in the cluster after PVC deletion, but its status changes to `Released`. The physical storage is NOT deleted.
To manually reclaim a `Released` PV:
1. **Delete the PV object:**
   ```bash
   kubectl delete pv <pv-name>
   ```
2. **Clean up the Physical Storage:** Log into the host or cloud provider console and format or erase the directory/disk contents.
3. **Re-create or Re-release:** Re-apply the PV manifest to make the resource `Available` again.

#### 2. Delete (Automatic Deletion)
The PV is automatically deleted, and the CSI driver invokes the backend storage API to destroy the physical volume (e.g. AWS EBS block storage or GCP persistent disk).

#### 3. Recycle (Deprecated)
Performs a basic file system scrub (`rm -rf /mount/*`) and returns the PV to `Available`. 
* **Evolutionary Context:** This policy is deprecated and unsupported by modern CSI plugins. Originally, the Recycle controller launched a tiny recycler pod on the node that mounted the volume and executed a shell file-level delete (`rm -rf /mount/*`). This approach introduced significant portability and security gaps: it did not guarantee secure erasure of underlying block devices, could not manage snapshots or cloud provider metadata, and often failed due to local permission issues or left orphaned inode metadata.
* **Modern Replacement:** Kubernetes has shifted entirely to out-of-tree CSI drivers that use `Delete` (invoking provider APIs to delete underlying storage resources) or `Retain` (manual secure scrubbing), integrated with dynamic StorageClass provisioning.

---

### E. PVC Protection and Finalizers
To prevent data loss and filesystem corruption, Kubernetes prevents active volumes from being deleted while in use.
- When you delete a PVC that is mounted by an active Pod, the PVC is marked for deletion and its status changes to `Terminating`.
- The PVC is protected by the finalizer: `kubernetes.io/pvc-protection`.
- The controller will block the physical removal of the PVC resource from the API server until the Pod using it is fully terminated.

---

### F. Troubleshooting Scenario: PVC Stuck in Terminating State
* **The Symptom:** `kubectl delete pvc <pvc-name>` hangs, and `kubectl get pvc` shows the PVC stuck in `Terminating` status.
* **The Investigation:** Running `kubectl describe pvc <pvc-name>` displays the finalizer `kubernetes.io/pvc-protection` in the metadata, indicating that the volume protection controller is active.
* **The Root Cause:** An active Pod is still running and referencing the PVC in its volume mounts. Kubernetes blocks deletion of volumes in active use to prevent filesystem corruption and host-level resource leakage.
* **The Fix:** Find and delete the Pod(s) that mount the volume. Once the Pod terminates and unmounts the volume, the volume protection finalizer is automatically removed, and the PVC completes its deletion immediately.

---

### G. Volume Node Affinity (Topology-Aware Scheduling)
Unlike network-attached storage (like AWS EBS or NFS), a **Local Persistent Volume** represents a physical SSD or directory attached directly to a single worker node. If a Pod mounts this volume, the Pod **must** be scheduled on that specific physical node.

#### 1. The Role of `nodeAffinity` on the PV
*   **Why PVs have affinity:** To enforce this scheduling constraint, the `PersistentVolume` manifest must specify `.spec.nodeAffinity`. This tells the Kubernetes Scheduler: *"This storage resource is physically locked to Node X. Any Pod that binds this volume's PVC must run on Node X."*
*   **Why PVCs do not have affinity:** PVCs are namespace-scoped, developer-facing abstractions (e.g. *"I want 50Gi of fast storage"*). They do not reference specific nodes or infrastructure topology. The topology constraints are managed entirely on the backing `PersistentVolume` (PV) and matched during scheduling.
*   **Volume Node Affinity Conflict:** If a Pod is scheduled to a different node (e.g. due to node selectors, taints, or resource shortages), or if the scheduler tries to place the Pod on a node that cannot physically reach the local disk, the Pod will remain stuck in a `Pending` state with the scheduling error: `1 node(s) had volume node affinity conflict`.

#### 2. Local PV YAML Syntax with Node Affinity
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-pv-demo
spec:
  capacity:
    storage: 50Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  local:
    path: /mnt/disks/ssd1       # Path to the physical disk mounted on the host node
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
                - worker-node-1 # The exact host name where this disk is located
```

#### 3. Core Mechanics: Local Storage Provisioning Q&A
*   **Question:** In the case of a local StorageClass, if I manually partition/format a local disk on `node01` and create a matching PV, must the PVC use a `selector` to bind to that PV, and how is it all influenced by `nodeAffinity`?
*   **Answer:** 
    *   **The PVC Selector is NOT mandatory:** You do **not** need a label selector on the PVC to bind it to a local PV. The standard way Kubernetes coordinates this is through the `storageClassName` and `volumeBindingMode: WaitForFirstConsumer`. When the Pod is created, the Scheduler evaluates which nodes can host the Pod (honoring the PV's `nodeAffinity`), schedules the Pod onto the correct host node, and automatically triggers the binder to bind the PVC to the matching local PV residing on that node. (A PVC label `selector` is only needed if you have multiple local PVs on the same node and want to target a specific physical drive class).
    *   **The Scheduling Influence:** The entire Pod scheduling process is heavily governed by the PV's `nodeAffinity`. Because the PV is bound to a specific host (e.g. `node01`), the Scheduler is forced to assign the Pod to `node01`, ensuring the volume mount is physically accessible to the running containers.

---

### H. Complete PV and PVC Manifest Templates
#### PV Manifest (`pv-definition.yaml`)
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: static-pv-demo
  labels:
    tier: fast
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  hostPath:
    path: /tmp/static-data-dir
    type: DirectoryOrCreate
```

#### PVC Manifest (`pvc-definition.yaml`)
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: static-pvc-demo
  namespace: default
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: local-storage
  resources:
    requests:
      storage: 2Gi
  selector:
    matchLabels:
      tier: fast
```

---

## 4. Using PVCs in Pods

Once a PVC is bound, a Pod can consume it by referencing it in its `spec.volumes` block.

---

### A. Complete Pod Configuration Template
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-database
  namespace: default
spec:
  containers:
  - name: mysql
    image: mysql:8.0
    env:
    - name: MYSQL_ALLOW_EMPTY_PASSWORD
      value: "yes"
    volumeMounts:
    - name: db-storage
      mountPath: /var/lib/mysql
      subPath: data
  volumes:
  - name: db-storage
    persistentVolumeClaim:
      claimName: static-pvc-demo
```

---

### B. Advanced Container Volume Features

#### 1. `subPath` Mounting
Allows mounting a specific subdirectory inside the volume rather than mounting the root directory. This is useful when running multiple containers in the same Pod that share the same underlying volume but require separated file trees.
- **Example configuration:** `subPath: data` will mount `/var/lib/mysql/data` instead of mapping the volume root to `/var/lib/mysql`.

#### 2. Mount Propagation
Controls whether mounts created by a container are visible to other containers in the same Pod or to other processes on the host node. Configured via `mountPropagation` in `volumeMounts`:
- `None` (Default): Inside the container, you see only the mounts present at container creation. Mount changes are not propagated.
- `HostToContainer`: The container receives new mounts made on the host or inside other containers, but does not propagate its own mounts.
- `Bidirectional`: Mounts created inside this container are propagated back to the host and all other containers sharing the volume. *Note: Requires privileged security contexts.*

---

## 5. StorageClasses & Dynamic Provisioning

StorageClasses allow clusters to dynamically provision physical disks and PVs when PVC requests are made, eliminating the need for cluster administrators to manually pre-provision disks.

---

### A. volumeBindingMode (Immediate vs. WaitForFirstConsumer)
The `volumeBindingMode` controls when volume provisioning and binding occurs:

#### 1. `Immediate` (Default)
- **Behavior:** The volume is provisioned and bound immediately when the PVC is created.
- **The Cross-AZ Failure Scenario:**
  1. A PVC is created in a multi-AZ cluster (e.g., AWS zones `us-east-1a`, `us-east-1b`).
  2. The CSI driver provisions a disk in `us-east-1a`.
  3. The Pod referencing the PVC is created. The scheduler determines that the Pod has node selectors or resource limits that force it to run in `us-east-1b`.
  4. The Pod stays stuck in a `Pending` state with a scheduling error: "1 node(s) had volume node affinity conflict".

#### 2. `WaitForFirstConsumer`
- **Behavior:** Delays volume provisioning and binding until a Pod using the PVC is created and scheduled.
- **The Solution:** The scheduler first evaluates the Pod's node selectors, resource limits, and affinity rules to choose a valid node. It then instructs the CSI provisioner to create the physical volume in the same Availability Zone (or local node) where that chosen node resides.
- **Usage:** Mandatory for local volumes and highly recommended for cloud persistent storage.

#### 3. Troubleshooting Scenario: PVC Stuck in Pending with WaitForFirstConsumer
* **The Symptom:** The PVC remains in a `Pending` state indefinitely after creation.
* **The Investigation:** Running `kubectl describe pvc <pvc-name>` shows an event with the message: `WaitForFirstConsumer: waiting for first consumer to be created before binding`.
* **The Root Cause:** The PVC's StorageClass uses `volumeBindingMode: WaitForFirstConsumer`. The Kubernetes control plane delays volume creation and binding until a Pod consuming this storage is scheduled, to ensure that the volume is provisioned on the correct host node or Availability Zone where the workload will run.
* **The Fix:** Create a Pod that references the PVC in its volume definitions. The scheduler will choose a node for the Pod first, which automatically triggers the binder to bind the PVC (or provision a new PV dynamically) on that specific node, shifting the PVC status to `Bound`.

---

### B. Volume Expansion Support
If a StorageClass has `allowVolumeExpansion: true`, you can resize a volume without recreations:
1. Edit the PVC manifest or live resource to request more storage (e.g., change `storage: 10Gi` to `20Gi`).
2. The `external-resizer` sidecar detects the change and expands the physical block device in the cloud.
3. Kubelet detects the change and performs an online filesystem expansion (`resize2fs`/`xfs_growfs`) inside the running Pod's filesystem.

---

### C. Complete StorageClass Manifest Templates
#### SC Template with WaitForFirstConsumer & Expansion (`sc-definition.yaml`)
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard-gp3
provisioner: ebs.csi.aws.com
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
parameters:
  type: gp3
  iops: "3000"
  throughput: "125"
```

#### SC Template for Local Volumes (No Dynamic Provisioner)
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage-sc
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
```

---

### D. Rancher Local Path Provisioner Setup (Dynamic hostPath Storage)
In local lab environments (e.g., bare-metal `kubeadm` setups or virtualized nodes), there is no cloud provider to dynamically supply backing block volumes. We can deploy the **Rancher Local Path Provisioner** to simulate dynamic provisioning on bare-metal by dynamically creating local `hostPath` directories on the node disks.

#### 1. Installation Command
Apply the Kubernetes manifests from Rancher's official repository:
```bash
kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml
```

#### 2. Verification
Check if the local-path driver controller is running:
```bash
kubectl get pods -n local-path-storage
```
Check that the `local-path` StorageClass is registered and set up:
```bash
kubectl get sc
```
*Expected Output:*
```plaintext
NAME          PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path    rancher.io/local-path   Delete          WaitForFirstConsumer   false                  1m
```

#### 3. Complete Dynamic PVC Manifest
Developers can request storage from this local pool by referencing `local-path` in their `storageClassName`:
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-path-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: local-path
  resources:
    requests:
      storage: 1Gi
```
*(Because the storage class uses `WaitForFirstConsumer`, the PVC will remain `Pending` until a Pod mounts it, at which point the provisioner creates a directory on the target worker node and binds the PV).*

---

## 6. CLI Command and Troubleshooting Cheat Sheet

### A. General Volume Operations
- **List storage classes, PVs, and PVCs:**
  ```bash
  kubectl get sc,pv,pvc
  ```
- **Inspect volume details and matching logs:**
  ```bash
  kubectl describe pvc <pvc-name>
  kubectl describe pv <pv-name>
  ```
- **Locate Pod mount paths:**
  ```bash
  kubectl get pod <pod-name> -o jsonpath='{.spec.volumes}'
  ```

### B. Patching Finalizers (Force Deletion)
If a PV or PVC is stuck in a `Terminating` state due to missing finalizers or orphaned state, you can clear the finalizers manually:
```bash
# Clear PVC Protection finalizer
kubectl patch pvc <pvc-name> -p '{"metadata":{"finalizers":null}}'

# Clear PV Protection finalizer
kubectl patch pv <pv-name> -p '{"metadata":{"finalizers":null}}'
```
> [!WARNING]
> Clearing finalizers manually bypasses Kubernetes protection checks and can lead to orphaned resources in your cloud/storage infrastructure. Use with caution.

---

## 🛠️ Practical Proof of Concept (PoC)

To validate the mechanics of `WaitForFirstConsumer` binding, dynamic matching, and file persistence, you can run the automated verification script located in the repository at:
`Reference Notes/scripts/verify_storage_poc.sh`

### Manual Run Sheet

#### Step 1: Create the StorageClass
Apply a StorageClass configured to delay binding:
```yaml
# storageclass.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: delayed-sc
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
```
```bash
kubectl apply -f storageclass.yaml
```

#### Step 2: Create the hostPath PV
Provide a backing PersistentVolume pointing to local host storage:
```yaml
# pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: delayed-pv
spec:
  capacity:
    storage: 100Mi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: delayed-sc
  hostPath:
    path: /tmp/delayed-data
    type: DirectoryOrCreate
```
```bash
kubectl apply -f pv.yaml
```

#### Step 3: Request Storage via PVC
Submit the claim:
```yaml
# pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: delayed-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: delayed-sc
  resources:
    requests:
      storage: 100Mi
```
```bash
kubectl apply -f pvc.yaml
```

#### Step 4: Verify Delayed Binding State
Run a query to inspect the status:
```bash
kubectl get pvc delayed-pvc
```
*Expected Output:*
```
NAME          STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
delayed-pvc   Pending                                      delayed-sc     5s
```
> The claim stays `Pending` because `volumeBindingMode` is `WaitForFirstConsumer` and no Pod has claimed it yet.

#### Step 5: Start a Pod to Trigger Binding
```yaml
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: consumer-pod
spec:
  containers:
  - name: writer
    image: alpine
    command: ["sh", "-c", "echo 'Storage Bound Successfully' > /data/status.txt && sleep 3600"]
    volumeMounts:
    - name: storage-mount
      mountPath: /data
  volumes:
  - name: storage-mount
    persistentVolumeClaim:
      claimName: delayed-pvc
```
```bash
kubectl apply -f pod.yaml
```

#### Step 6: Verify Bound Status
Wait for the Pod to schedule, then verify:
```bash
kubectl get pvc delayed-pvc
```
*Expected Output:*
```
NAME          STATUS   VOLUME       CAPACITY   ACCESS MODES   STORAGECLASS   AGE
delayed-pvc   Bound    delayed-pv   100Mi      RWO            delayed-sc     1m
```
The PVC is now `Bound` to the PV `delayed-pv`.

#### Step 7: Clean Up
```bash
kubectl delete pod consumer-pod
kubectl delete pvc delayed-pvc
kubectl delete pv delayed-pv
kubectl delete -f storageclass.yaml
```

---

## 6. Advanced Storage Concepts & Volume Control

Kubernetes modern storage APIs introduce granular controls for ephemeral files, volume backups, dynamic capacity scheduling, and on-the-fly performance tuning.

### 6.1 Projected Volumes
A **Projected Volume** maps multiple existing volume sources into the same directory within a Pod. 

*   **Supported Sources:**
    *   `secret`
    *   `configMap`
    *   `downwardAPI`
    *   `serviceAccountToken` (for projecting audience-bound, short-lived OIDC tokens)
*   **Key Behavior:** All sources are projected as read-only. Symbolic links are used under the hood to ensure files are updated atomically when the source changes in the control plane.

#### Example Projected Volume Manifest:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: projected-volume-pod
spec:
  containers:
  - name: app
    image: alpine
    command: ["sleep", "3600"]
    volumeMounts:
    - name: unified-config
      mountPath: /var/run/config
      readOnly: true
  volumes:
  - name: unified-config
    projected:
      sources:
      - secret:
          name: db-credentials
          items:
          - key: username
            path: db-user
      - configMap:
          name: app-settings
          items:
          - key: theme
            path: ui-theme
      - downwardAPI:
          items:
          - path: pod-info.txt
            fieldRef:
              fieldPath: metadata.name
```

---

### 6.2 Ephemeral Volumes (CSI & Generic)
While persistent volumes persist beyond the lifecycle of a Pod, **Ephemeral Volumes** are temporary directories tied strictly to the lifetime of the Pod. They are created when the Pod is scheduled and deleted when it terminates.

#### 1. CSI Inline Ephemeral Volumes:
These allow you to define CSI volumes inline inside the Pod specification. They are suitable for simple, local drivers that do not require full PersistentVolume lifecycle management (e.g., injecting secret keys or local certificates).
```yaml
spec:
  containers:
  - name: web
    image: nginx
    volumeMounts:
    - name: local-certs
      mountPath: /certs
  volumes:
  - name: local-certs
    csi:
      driver: inline.certs.csi.k8s.io
      volumeAttributes:
        secretName: site-cert
```

#### 2. Generic Ephemeral Volumes:
Generic ephemeral volumes allow any storage driver that supports dynamic provisioning to provide ephemeral storage for a Pod. It utilizes the PVC lifecycle internally:
*   When a Pod is created, the cluster automatically creates a matching PVC on behalf of the Pod.
*   The volume is dynamically provisioned and mounted.
*   When the Pod is deleted, the PVC is automatically deleted, triggering the deletion of the underlying PV.
*   *Advantages:* Supports volume limits, snapshots, and resizing via regular StorageClasses.
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: generic-ephemeral-pod
spec:
  containers:
  - name: cache-server
    image: redis
    volumeMounts:
    - name: scratch-space
      mountPath: /data
  volumes:
  - name: scratch-space
    ephemeral:
      volumeClaimTemplate:
        spec:
          accessModes: [ "ReadWriteOnce" ]
          storageClassName: "fast-local"
          resources:
            requests:
              storage: 2Gi
```

---

### 6.3 Volume Snapshots & VolumeSnapshotClasses
**Volume Snapshots** capture a point-in-time copy of a PersistentVolume's data. This feature relies on three Custom Resource Definitions (CRDs) managed by the CSI driver.

*   **`VolumeSnapshotClass`**: Defines the driver, the deletion policy (`Delete` vs `Retain`), and specific parameters for the snapshot backend (similar to a `StorageClass`).
*   **`VolumeSnapshot`**: The user's request to capture a snapshot. References a source PVC.
*   **`VolumeSnapshotContent`**: The actual physical copy on the storage backend. References a `VolumeSnapshot` and is cluster-scoped (similar to a `PersistentVolume`).

#### Default VolumeSnapshotClass Resolution:
An administrator can configure a default `VolumeSnapshotClass` by adding the annotation `snapshot.storage.kubernetes.io/is-default-class: "true"` to its metadata. 
*   **Automatic Matching:** When a `VolumeSnapshot` is created without specifying `volumeSnapshotClassName`, the controller automatically resolves the class by finding a default `VolumeSnapshotClass` whose `driver` matches the CSI driver defined in the source PVC's `StorageClass`.
*   **Coexistence and Constraints:** Multiple default `VolumeSnapshotClass` objects can coexist in a cluster, provided each is assigned to a unique CSI driver. If multiple default classes are defined for the *same* CSI driver, the snapshot creation will fail with a resolution conflict error.

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: prod-snapshot-class
  annotations:
    snapshot.storage.kubernetes.io/is-default-class: "true"
driver: hostpath.csi.k8s.io
deletionPolicy: Delete
---
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: db-backup-snapshot
  namespace: db-ns
spec:
  volumeSnapshotClassName: prod-snapshot-class
  source:
    persistentVolumeClaimName: postgres-pvc
```
*To restore a snapshot:* Create a new PVC and specify the `VolumeSnapshot` as the `dataSource`:
```yaml
spec:
  dataSource:
    name: db-backup-snapshot
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  resources:
    requests:
      storage: 10Gi # Must be >= size of snapshot
```

---

### 6.4 Storage Capacity Tracking & Scheduling
In large clusters, placing a Pod on a node before verifying available storage can result in the Pod being stuck in `ContainerCreating` or `VolumeBinding` states.
*   **`CSIStorageCapacity` API:** CSI drivers publish remaining capacity information to the API server.
*   **`kube-scheduler` Integration:** When scheduling a Pod that requests dynamic provisioning, the scheduler checks these capacity reports. It filters out nodes that lack sufficient local/regional storage, preventing volume provisioning bottlenecks.

---

### 6.5 Volume Attributes Classes (v1.34+ GA)
**Volume Attributes Classes** permit developers to dynamically modify volume configurations (e.g., IOPS, throughput, latency tiers) on the fly without deleting the PVC or causing database downtime.
*   **Usage:** A cluster-scoped `VolumeAttributesClass` defines storage profiles. A PVC references this class via `spec.volumeAttributesClassName`.
*   **Dynamic Update:** Modifying the reference in the PVC triggers the CSI driver to resize or alter storage performance parameters online.

```yaml
apiVersion: storage.k8s.io/v1alpha1
kind: VolumeAttributesClass
metadata:
  name: high-iops-class
driver: pd.csi.storage.gke.io
parameters:
  iops: "10000"
  throughput: "500"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-pvc
spec:
  accessModes: [ "ReadWriteOnce" ]
  resources:
    requests:
      storage: 100Gi
  volumeAttributesClassName: high-iops-class
```

---

### 6.6 Local Ephemeral Storage Limits & Volume Health Monitoring

#### 1. Local Ephemeral Storage resource control:
Local ephemeral storage (writable container layers, logs, and `emptyDir` volumes) is shared across the node's root filesystem. To prevent a rogue Pod from exhausting node disk space:
*   **Requests & Limits:** Define `resources.requests.ephemeral-storage` and `resources.limits.ephemeral-storage` in the container spec.
*   **Eviction:** The Kubelet monitors disk usage. If a Pod's local ephemeral storage usage exceeds its specified limit, the Kubelet evicts the Pod, terminating its processes to protect the node's disk integrity.
*   **ResourceQuotas:** Namespace-level storage quotas can limit the total ephemeral storage requests or limits allowed across all Pods in the namespace.

```yaml
spec:
  containers:
  - name: app
    image: busybox
    resources:
      requests:
        ephemeral-storage: "500Mi"
      limits:
        ephemeral-storage: "2Gi"
```

#### 2. Volume Health Monitoring:
Allows the CSI driver and Kubelet to detect disk health events (e.g., device errors, partition corruption, read-only mounts) from the underlying storage controller.
*   If a disk fails, the monitor logs an event on the PVC (e.g., `VolumeUnhealthy`) or Pod.
*   Cluster operators can capture these events to trigger auto-recreation of the Pod on a healthy node.
