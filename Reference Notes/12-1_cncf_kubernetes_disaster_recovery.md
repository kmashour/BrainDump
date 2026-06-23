---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - cncf/disaster-recovery
  - kubernetes/disaster-recovery
  - linux/backup
---

# Module 12-1: CNCF Kubernetes Disaster Recovery

**Breadcrumbs:** [[12-Index - CNCF References|🏠 CNCF References Index]] > **CNCF Kubernetes Disaster Recovery**

---

> [!NOTE]
> **Source Citation**
> This reference module summarizes and analyzes the CNCF presentation: *"Disaster Recovery for your Kubernetes Clusters [I]"* by engineers **Andy Goldstein & Steve Kriss** (Heptio). It covers operational disaster recovery design patterns, state boundaries definition, backup architectures, and file consistency.
> *   **Source Presentation:** [YouTube - CNCF KubeCon Talk](https://www.youtube.com/watch?v=qRPNuT080Hk)

---

## 🏛️ Traditional vs. Kubernetes Disaster Recovery

Disaster Recovery (DR) models diverge fundamentally when moving from monolithic host mappings to cloud-native orchestrations.

```
Monolithic (Server-State Coupled):
+-----------------------------+
| Application + Config + Data |
|           [ Server ]        |  <-- Backup/Restore entire Virtual Machine / Block Disk
+-----------------------------+

Kubernetes (Stateless Nodes / Segregated State):
+---------------------------------------------------------------+
| Masters & Worker Nodes (Stateless compute instances)          |
+---------------------------------------------------------------+
  State resides in:
  1. Control Plane State: [ etcd Cluster ] (Specs, Secrets, Configs)
  2. Application State:   [ Persistent Volumes ] (Database blocks)
```

### 1. Coupled Host Coupling (Traditional)
*   **Architecture:** A strong 1:1 correspondence exists between applications and servers.
*   **Backup Method:** Regular full disk-level partition block backups or filesystem snapshots (nightly).
*   **Restore Method:** Spin up a replica server matching the original hardware and write the block images back.

### 2. Segregated State Boundary (Kubernetes)
*   **Architecture:** Masters and worker nodes run compute processes but are essentially **stateless**. The state resides in two separate locations:
    1.  **etcd Database:** Tracks control plane specifications (Deployments, Services, ConfigMaps, Secrets).
    2.  **Persistent Volumes (PVs):** Houses database and file blocks for running workloads.
*   **Restore Method:** Spin up fresh nodes (e.g. via IaC tools like Terraform/Ansible) and inject the state (etcd configuration objects + volume snapshots). Rebuilding a master node or worker node does not require copying disk sectors.

---

## ⚙️ Control Plane & Node Recovery Patterns

When individual master or worker nodes fail, administrators use standard orchestrator APIs to reschedule containers.

### Node Maintenance Sequence
```bash
# 1. Mark node as unschedulable (Blocks new pods scheduling)
kubectl cordon worker-node-01

# 2. Evict active running pods gracefully to other host instances
kubectl drain worker-node-01 --ignore-daemonsets --delete-emptydir-data
```

### Automation & Bootstrapping Certs
*   **Automation Standard:** Cluster rebuilding must be automated (Ansible, Chef, Puppet) to minimize recovery time (RTO).
*   **Certificate Retention:** Administrators must back up and bring along internal cluster SSL/TLS credentials (e.g., `/etc/kubernetes/pki/`). Regenerating client/server certificates during recovery introduces complexity and extends outages.

---

## 🗄️ Control Plane State (etcd) Backup Strategies

CNCF defines four common methodologies for backing up cluster control plane states:

| Backup Method | Operational Action | Advantages | Disadvantages |
| :--- | :--- | :--- | :--- |
| **1. Block-Level Disk Backup** | Back up the block device partition hosting the etcd database. | Fast raw block capture. | Potential filesystem lock issues if writing occurs during backup. |
| **2. Filesystem Directory Backup** | Back up `/var/lib/etcd/` data directory. | Simple file-level copy. If a node fails, it catches up on delta transactions from other cluster members automatically. | Requires local file access permissions. |
| **3. etcdctl Snapshot DB** | Run `etcdctl snapshot save` command. | Clean database snapshot. | Restoring a snapshot creates a **new** etcd cluster, causing a cluster-wide service interruption. |
| **4. API Discovery Loop Query** | Query the API Discovery Endpoint to list resources and export them to YAML/JSON. | **Highly selective.** Allows namespace or individual resource restorations. Works on managed control planes (EKS, GKE). | Slow for large clusters. |

---

## 💾 Application State (Persistent Volumes) & File Consistency

Persistent Volumes (PVs) contain the stateful transactions of user workloads.

### 1. Volume Snapshots
*   **Mechanism:** Snapshot APIs hook into cloud provider storage controllers (e.g. AWS EBS, GCE PD) to checkpoint raw sectors.
*   **Evolution:** Modern setups standardize this via CSI (Container Storage Interface) Volume Snapshots.

### 2. Filesystem Coherency & fsfreeze
Taking raw block-level volume snapshots of a database writing live data can lead to corrupt tables.
*   **The Issue:** Operating system kernels cache writes in memory. If a block snapshot occurs while bytes remain in buffers, the snapshot database is in an inconsistent state.
*   **The Pattern:** Use the Linux `fsfreeze` tool:
    ```bash
    # Freeze the filesystem before executing disk snapshots (Flushes buffers and locks writes)
    fsfreeze --freeze /var/lib/mysql

    # Execute Cloud/Storage Controller Snapshot (API call)

    # Unfreeze the filesystem to resume database operations
    fsfreeze --unfreeze /var/lib/mysql
    ```

---

## 🛠️ CNCF Disaster Recovery Toolset: Heptio Ark (Velero)

Heptio Ark (now known as **Velero**) is an open-source backup utility specifically designed to orchestrate state restorations.

### Velero Architecture
```
                         +-----------------------------------+
                         |         Velero Operator           |
                         +-----------------------------------+
                               |                       |
                               v                       v
               (Discovery API Object Extraction)  (CSI Cloud Storage Plugin)
                               |                       |
                               v                       v
+------------------+     +------------------+     +------------------+
| API Object Specs |     | Object Storage   |     | Cloud Provider   |
| (Exported YAMLs) | --> | (S3, Minio)      |     | Volume Snapshots |
+------------------+     +------------------+     +------------------+
```

### Core Features
1.  **Fine-Grained Backups:** Filters backups by labels, resource types, or namespaces.
2.  **Namespace Remapping (Cloning):** Allows restoring resources into a namespace different from the origin (e.g. duplicating production environments to staging namespaces for debugging).
3.  **Extensible Actions & Hooks:**
    *   **Pre/Post Hooks:** Run arbitrary scripts inside container pods before or after volume snapshots (e.g., executing `fsfreeze` or database flush commands).
    *   **Plugins:** Pluggable architectures supporting customized object storage targets (S3, Azure Blob, GCS) and block storage providers without codebase recompilations.
    *   **Item Actions:** Mutates configuration metadata dynamically during backups or restores (e.g., changing node ports or ingress configurations).

---

## 🔗 Related Reference Notes
*   **Kubernetes Cluster Maintenance:** [[0-10_maintenance_upgrades_and_etcd|Module 0-10: CKA etcd Maintenance & Upgrades]]
*   **Linux Storage Filesystem Mounting:** [[8-2_filesystems_and_storage|Module 8-2: File Systems & Storage]]
*   **Linux Storage Volume Administration:** [[8-9_redhat_enterprise_linux_administration|Module 8-9: Red Hat Enterprise Linux (RHEL) Administration]]
