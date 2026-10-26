---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Workload Security and Container Hardening]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "Kubernetes Storage Internals & Permission Architecture"
tags:
  - kubernetes/security
  - kubernetes/storage
  - kubernetes/fsgroup
  - kubernetes/user-namespaces
  - kubernetes/performance
  - kubernetes/deep-dive
---

# Kubernetes Volume Permissions - fsGroup Mechanics, Supplemental Groups, and RootMismatch Optimization

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Workload Security and Container Hardening]] > **Volume Permissions - fsGroup Mechanics, Supplemental Groups, and RootMismatch Optimization**

---

## 🎯 1. The Core Problem: The Non-Root Volume Permission Denied Deadlock

When adhering to security best practices, containers are configured to run as unprivileged users (e.g. `runAsUser: 1000`).

However, when Kubernetes attaches an external storage volume (such as an AWS EBS, GCP Persistent Disk, or local volume) to a node:
* The host filesystem initializes the directory owned by: **`root:root` (UID `0`, GID `0`)** with permissions `0755` (`rwxr-xr-x`).
* When the container process running as user **`1000`** attempts to write data:
  ```bash
  echo "data" > /data/file.txt
  # Result: bash: /data/file.txt: Permission denied!
  ```
The non-root container cannot write to the storage volume, forcing developers into the dangerous anti-pattern of running workloads as `root`.

---

## ⚙️ 2. The Solution: `fsGroup` & Supplemental Groups

To grant unprivileged containers write access without elevating them to root, Kubernetes provides **`fsGroup`** under `pod.spec.securityContext`.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: storage-app
spec:
  securityContext:
    runAsUser: 1000
    fsGroup: 2000          # The Pod filesystem group ID
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
    volumeMounts:
    - name: data-vol
      mountPath: /data
  volumes:
  - name: data-vol
    persistentVolumeClaim:
      claimName: my-pvc
```

### What Kubelet Does Under the Hood (The 3 Automatic Actions):
When Kubelet mounts the volume on the worker node, it executes three operations:
1. **Supplemental Group Assignment:** Kubelet injects GID `2000` into the container process's list of supplementary groups.
2. **Ownership Change:** Kubelet recursively updates the volume so that its group ownership becomes GID `2000`.
3. **The `setgid` Bit (`chmod g+s`):** Kubelet sets the setgid permission bit on all directories within the volume. **Any new file or directory created inside the volume automatically inherits group ownership of GID `2000`.**

Now, user `1000` presents its supplementary group `2000` badge and writes to `/data` seamlessly.

---

### Why is `fsGroup` Pod-Level and NOT Container-Level?
In the Kubernetes schema, **volumes belong to the Pod (`spec.volumes`), not to individual containers**. 
* If two containers in the same Pod mount the same volume, the volume's underlying permissions on the host filesystem cannot differ between containers.
* Therefore, `fsGroup` is declared once at the Pod level to enforce uniform volume access across all containers in that Pod.

---

## 🔬 3. The 6 Linux Namespaces & The User Namespace Reality

Why must we rely on `fsGroup` and non-root UIDs instead of relying on container isolation?

```
+---------------------------------------------------------------------------------+
|                       THE 6 LINUX KERNEL NAMESPACES                             |
+-------------------+---------------------------------------------+---------------+
| Namespace Type    | What it Isolates                            | Enabled in K8s|
+-------------------+---------------------------------------------+---------------+
| 1. PID Namespace  | Process IDs (Container thinks it is PID 1)   |  YES (Default)|
| 2. NET Namespace  | IP addresses, ports, routing tables         |  YES (Default)|
| 3. MNT Namespace  | Filesystem mount tree (chroot / pivot_root) |  YES (Default)|
| 4. IPC Namespace  | Shared memory, semaphores, message queues   |  YES (Default)|
| 5. UTS Namespace  | Hostname and domain name                    |  YES (Default)|
| 6. USER Namespace | User IDs and Group IDs (UID / GID mapping)  | ❌ NO! DEFAULT|
|                   |                                             |    DISABLED!  |
+-------------------+---------------------------------------------+---------------+
```

### The Critical Takeaway:
* The container has its own PID namespace (PID 1) and Mount namespace (its own rootfs).
* **However, User Namespaces are DISABLED by default in Docker and standard Kubernetes.**
* A process executing as `root` (UID 0) inside a container shares the **exact same user table with the host kernel**.
* If a container process running as `UID 0` breaks out of its Mount namespace, it lands on the host as **genuine root (UID 0)**!

---

## ⚡ 4. The Recursive `chown` Performance Problem & The Fix

### The Disaster on Large Volumes:
Suppose a pod mounts a storage volume containing **5 million files** (e.g. a database or image cache):
* Every time the pod starts or restarts, Kubelet executes a recursive `chown -R` across all 5 million files on disk.
* That results in 5 million disk read-and-write operations **on every pod boot**.
* The pod remains stuck in **`ContainerCreating` for 15 to 30 minutes**, causing severe application downtime and timeout crashes.

---

### Why "Projected Volumes" Do NOT Fix This:
* **Projected Volumes** are strictly designed to merge small control-plane metadata and credentials (Secrets, ConfigMaps, DownwardAPI, ServiceAccount tokens) into a single directory.
* They hold small text files; they cannot be used to mount large persistent disks or application databases.

---

### The Real Kubernetes Fix: `fsGroupChangePolicy: "OnRootMismatch"`

Kubernetes introduced **`fsGroupChangePolicy`** inside `securityContext` to eliminate startup lag:

```yaml
spec:
  securityContext:
    runAsUser: 1000
    fsGroup: 2000
    fsGroupChangePolicy: "OnRootMismatch"    # Skips recursive walk if root matches!
```

#### Comparison of Policies:

| Policy | Behavior | Startup Time on 5M Files |
| :--- | :--- | :--- |
| **`Always`** (Default) | Kubelet recursively walks and updates every file on every pod start. | **15 - 30 Minutes!** |
| **`OnRootMismatch`** | Kubelet checks **only the top-level root directory** of the volume. If the root already matches GID `2000`, it **skips the remaining 5 million files entirely**. | **0.1 Seconds!** |

With `OnRootMismatch`, the recursive walk executes only the very first time a volume is attached. All subsequent restarts are instantaneous.

---

## 🛠️ 5. Terminal Verification Commands

```bash
# 1. Exec into the pod and verify user and supplementary groups:
kubectl exec -it storage-app -- id
# Output:
# uid=1000 gid=0(root) groups=2000

# 2. Verify file creation inside the volume inherits the fsGroup:
kubectl exec -it storage-app -- touch /data/testfile
kubectl exec -it storage-app -- ls -l /data/testfile
# Output:
# -rw-r--r-- 1 1000 2000 0 ... /data/testfile (Group is 2000!)
```
