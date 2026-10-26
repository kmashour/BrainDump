---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - kubernetes/disaster-recovery
  - kubernetes/etcd
  - kubernetes/bbolt
  - kubernetes/control-plane
  - linux/storage-engines
---

# Module 0-17-1: etcd B+ Tree (bbolt) Corruption, Freepage Collisions & Control Plane Resuscitation

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Master Index]] > **Domain 8: Corner Cases, Post-Mortems & Doomsday Scenarios** > **Module 0-17-1: etcd bbolt Corruption & Resuscitation**

This module provides an exhaustive, low-level forensic and architectural breakdown of a fatal Kubernetes control plane failure: **underlying B+ Tree database corruption in `etcd` (`bbolt`) triggered by an abrupt host crash or ungraceful VM shutdown**. It documents the exact root-cause mechanics, why standard Kubernetes tooling fails completely, and provides a surgical, zero-data-loss resuscitation playbook.

---

## 🗺️ Cognitive Map: The Anatomy of a Control Plane Resuscitation

When a Kubernetes control plane experiences total collapse, troubleshooting proceeds through six discrete forensic tiers:

```
+----------------------------------------------------------------------------------------------------+
| Tier 1: Outer Symptoms & Triage                                                                    |
| "kubectl: Connection Refused (:6443)" ──► Kubelet alive, but Static Pods CrashLooping             |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| Tier 2: Runtime Container Forensics                                                                |
| Inspect CRI (crictl/docker logs) ──► Identify Go panic: freepages: failed to get all reachable...  |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| Tier 3: Storage Isolation & Immutable Backup                                                      |
| Halt Kubelet ──► Freeze write locks ──► Create timestamped raw snapshot of /var/lib/etcd           |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| Tier 4: Low-Level Database Surgery (bbolt)                                                         |
| Acquire bbolt CLI ──► bbolt check (detect page collision) ──► bbolt surgery revert-meta-page       |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| Tier 5: Multi-Layer State Resynchronization                                                        |
| Align .snap.db files ──► Bypass/Fix RBAC (kubeadm:cluster-admins) ──► Regenerate CNI Subnet.env     |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| Tier 6: Health Verification & Cluster Stabilization                                                |
| Verify etcd healthz ──► Verify API server (:6443) ──► Verify CoreDNS/Flannel ──► All Pods Ready   |
+----------------------------------------------------------------------------------------------------+
```

---

## 1. Incident Post-Mortem & The Doomsday Cascade

### 1.1 Incident Classification & Severity
*   **Severity:** Level 0 (Total Cluster Outage / Control Plane Deadlock).
*   **Initial Symptom:** All cluster administrative commands fail immediately:
    ```console
    $ kubectl get nodes
    The connection to the server 10.0.0.133:6443 was refused - did you specify the right host or port?
    ```
*   **Root Trigger:** Abrupt host power termination, hypervisor host reset, kernel panic, or forced virtualization reset without executing Linux storage flush commands (`sync` / unmounting filesystems).

### 1.2 The Crash Cascade
The collapse of the Kubernetes control plane follows a deterministic dependency chain:

```
+-----------------------------------------------------------------------------------+
|                        THE DOOMSDAY CRASH CASCADE                                 |
+-----------------------------------------------------------------------------------+
| 1. Abrupt Host Shutdown / Hypervisor Power Cut                                    |
|    │                                                                              |
| 2. Flushed Write Cache Collision in /var/lib/etcd/member/snap/db                  |
|    │                                                                              |
| 3. etcd Static Pod Boots ──► bbolt.Open() Consistency Verification Check          |
|    │                                                                              |
| 4. CRITICAL PANIC:                                                                |
|    "panic: freepages: failed to get all reachable pages (page 248: mult references)"|
|    │                                                                              |
| 5. etcd Crashes (Exit Code 2) ──► Kubelet Enters CrashLoopBackOff (Port 2379 Dead)|
|    │                                                                              |
| 6. Kube-APIServer Liveness/Startup Fails ──► Terminates Process (Port 6443 Dead)  |
|    │                                                                              |
| 7. USER IMPACT: kubectl commands fail with "Connection Refused"                   |
+-----------------------------------------------------------------------------------+
```

---

## 2. First-Principles Architecture: The `bbolt` Storage Engine

To understand how etcd database corruption occurs and how to surgically repair it, one must understand how `etcd` persists data to disk.

`etcd` does not implement its own low-level B-Tree storage engine from scratch. It embeds **`bbolt`** (formerly BoltDB), a single-file, transactional, pure-Go key-value store based on memory-mapped files (`mmap`).

### 2.1 Physical Disk Layout of `/var/lib/etcd/member/snap/db`
The database file on disk is an exact byte-for-byte representation of fixed-size pages (default: **4096 bytes**):

```
+-----------------------------------------------------------------------------------+
|                       bbolt DATABASE DISK FILE LAYOUT                             |
+-----------------------------------------------------------------------------------+
| Page 0: Meta Page 0 (txid = 100, root_page = 4, freelist = 2, crc = 0x8a...)     |
| Page 1: Meta Page 1 (txid = 101, root_page = 6, freelist = 3, crc = 0x4f...)     |
+-----------------------------------------------------------------------------------+
| Page 2: Freelist Page (Array of reusable unallocated disk page IDs)               |
| Page 3: Freelist Page (Overflow/continuation page)                                 |
+-----------------------------------------------------------------------------------+
| Page 4: B+ Tree Root / Branch Page (Internal routing keys & child page pointers)  |
| Page 5: B+ Tree Branch Page                                                       |
| Page 6: B+ Tree Leaf Page (Contains actual keys, e.g. /registry/pods/...)          |
| Page 7..N: Additional Leaf and Data Pages                                         |
+-----------------------------------------------------------------------------------+
```

### 2.2 Key Architectural Components

#### 1. Page Types & Flags
Every 4KB page starts with a 16-byte header:
```go
type page struct {
    id       pgid    // Unique 64-bit integer page number (0, 1, 2, ...)
    flags    uint16  // Bit flags identifying the page type
    count    uint16  // Number of items stored on this page
    overflow uint32  // Number of subsequent trailing pages if data exceeds 4KB
    ptr      uintptr // Memory offset to the start of page payload
}
```
*   `0x01` (**Branch Page**): Holds child page IDs and separation keys to navigate the B+ tree.
*   `0x02` (**Leaf Page**): Holds actual key-value pairs (Kubernetes manifests, secrets, endpoints).
*   `0x04` (**Meta Page**): Holds database metadata (transaction ID, root page ID, freelist page ID).
*   `0x10` (**Freelist Page**): Holds a flat array of page IDs that are free for future allocation.

#### 2. Copy-on-Write (CoW) Transactions
bbolt enforces full ACID compliance using Copy-on-Write:
*   When a transaction updates or deletes an existing key, it **never modifies the existing page in-place**.
*   Instead, bbolt allocates a new page, copies the modified data to the new page, and updates the parent branch page with the new page ID.
*   The old page is added to a transaction-pending free list. Once all concurrent reader transactions reading the old page terminate, that page ID is pushed to the global `freelist` for reuse.

#### 3. Double-Buffered Meta Pages (Page 0 and Page 1)
How does bbolt commit a transaction atomically without a separate Write-Ahead Log (WAL)?
It uses **Double-Buffered Meta Pages**:
*   `Page 0` is `meta0` and `Page 1` is `meta1`.
*   When Transaction $N$ begins, bbolt reads the meta page with the highest valid `txid`.
*   During commit, bbolt writes all modified data pages to disk.
*   Next, bbolt writes the updated `freelist` to disk.
*   Finally, bbolt writes transaction metadata ($txid = N+1$, new root page ID, new freelist page ID, CRC64 checksum) to the **inactive** meta page (alternating between Page 0 and Page 1).
*   bbolt calls the kernel system call `f.Sync()` (`fsync`).
*   **The atomic switch:** The instant the inactive meta page's checksum is verified on disk, the database has atomically transitioned to the new transaction state.

---

## 3. The Forensic Breakdown: Why Did the Crash Happen?

### 3.1 The Invariant Violation: Freepage Double-References
When an abrupt power loss or VM crash occurs while the Linux kernel disk scheduler is writing out dirty pages:
1.  Some newly allocated leaf pages might be written to the disk platter, while the freelist update or the meta page write is interrupted or flushed out-of-order.
2.  Upon reboot, `etcd` starts and executes `bbolt.Open()`:
    ```go
    // Conceptual flow of bbolt initialization
    func (db *DB) loadFreelist() {
        // 1. Read the active meta page (e.g. Meta 0 with txid 2500)
        // 2. Read the freelist page pointed to by Meta 0
        // 3. Traverse all reachable pages from the B+ Tree root page
        // 4. Cross-reference reachable pages against the freelist
    }
    ```
3.  **The Collision (Double Reference):**
    During the reachability scan, bbolt discovers that a page ID (e.g. `Page 248`) is:
    *   Referenced by an active branch node as a valid child page.
    *   **AND** simultaneously listed inside the `freelist` array as available for allocation.
    *(Or referenced by two distinct branch pointers simultaneously)*.

### 3.2 The Exact Runtime Panic
```console
panic: freepages: failed to get all reachable pages (page 248: multiple references)

goroutine 1 [running]:
go.etcd.io/bbolt.(*DB).loadFreelist(0xc000188000)
	/go/pkg/mod/go.etcd.io/bbolt@v1.3.8/db.go:412 +0x2e5
go.etcd.io/bbolt.Open(0x7ffd5e0a0b23, 0x1d, 0x1a0, 0xc0000a6e00, ...)
	/go/pkg/mod/go.etcd.io/bbolt@v1.3.8/db.go:278 +0x654
go.etcd.io/etcd/server/v3/mvcc/backend.newBackend(...)
	/go/pkg/mod/go.etcd.io/etcd/server/v3@v3.5.11/mvcc/backend/backend.go:189
```

### 3.3 Why bbolt Refuses to Boot (Safety Panic)
If bbolt ignored this error and allowed the database to open:
*   A subsequent `kubectl apply` or secret creation would request a free page from the freelist.
*   bbolt would allocate `Page 248`.
*   Writing new data to `Page 248` would instantly **overwrite and destroy** whatever Kubernetes branch or leaf data was already using `Page 248`.
*   This would cause **silent, undetectable, cascading corruption** across the cluster.
*   Therefore, bbolt triggers a Go runtime `panic()`, intentionally killing the process to protect data integrity.

---

## 4. Why Standard Tooling Fails Completely

| Utility | Status | Failure Mode |
| :--- | :--- | :--- |
| **`kubectl`** | ❌ **Completely Dead** | `Connection refused`: The API Server process cannot start because its datastore (etcd) is offline. |
| **`etcdctl`** | ❌ **Completely Dead** | `context deadline exceeded` / `connection refused`: `etcdctl` is a gRPC network client that requires an active etcd daemon listening on port `2379`. |
| **`etcdutl snapshot restore`** | ❌ **Ineffective** | Designed to initialize a new cluster from a valid, uncorrupted `.db` snapshot. It cannot repair a live corrupted database file in-place and will reject files with freelist errors. |

Because all standard tools fail, administrators must drop down to **low-level filesystem and binary forensics**.

---

## 5. The Step-by-Step Surgical Resuscitation Playbook

Follow this precise, zero-data-loss procedure to recover a broken control plane.

### Step 1: Diagnose the Outage via Container Runtime (CRI)
Since `kubectl` is unresponsive, SSH directly into the control plane host as root (`sudo -i`):

```bash
# Check Kubelet status
systemctl status kubelet

# Verify control plane containers via CRI utility (crictl or docker)
sudo crictl ps -a | grep -E 'etcd|kube-apiserver'
```
*Observation:* Both `etcd` and `kube-apiserver` will show `Exited` or rapid `CrashLoopBackOff`.

Retrieve the logs of the crashing etcd container:
```bash
sudo crictl logs $(sudo crictl ps -a --name etcd -q | head -n1) | tail -n 30
```
*Confirmation:* Look for the string `panic: freepages: failed to get all reachable pages (page <NUM>: multiple references)`.

---

### Step 2: Service Isolation & Immutable Snapshot Backup
Before performing any repair operations, freeze container restarts and create a physical backup:

```bash
# 1. Stop Kubelet to halt static pod container restart loops
sudo systemctl stop kubelet

# 2. Stop running etcd containers if any remain active
sudo crictl stop $(sudo crictl ps -a --name etcd -q) 2>/dev/null || true

# 3. CRITICAL: Create an offline timestamped backup of the entire etcd directory
sudo cp -r /var/lib/etcd /var/lib/etcd.bak.$(date +%F_%H%M%S)

# 4. Verify backup existence and size
ls -la /var/lib/etcd.bak.*
```

---

### Step 3: Acquire the Low-Level `bbolt` Binary
Standard Linux distributions and Kubernetes nodes do not have the `bbolt` CLI installed by default. You can acquire it in seconds using Docker or containerd:

```bash
# Build bbolt inside a temporary container and copy the binary to host
sudo docker run --rm -v /usr/local/bin:/out golang:1.22-alpine sh -c \
  "go install go.etcd.io/bbolt/cmd/bbolt@v1.4.0 && cp /go/bin/bbolt /out/bbolt"

# Verify binary execution
bbolt --help
```

---

### Step 4: Run Diagnostic Integrity Verification
Inspect the corrupted database file directly using `bbolt check`:

```bash
sudo bbolt check /var/lib/etcd/member/snap/db
```
*Expected Output on Corrupt DB:*
```
page 248: multiple references
failed to get all reachable pages: multiple references
```

Inspect database metadata:
```bash
sudo bbolt info /var/lib/etcd/member/snap/db
```
*Output reveals:* Active page count, page size (4096), and which meta page (`meta0` or `meta1`) is currently active.

---

### Step 5: Execute Surgical Repair (`bbolt surgery`)

The `bbolt surgery` tool (introduced in bbolt v1.3.8+ and enhanced in v1.4.0) provides direct disaster-recovery primitives to manipulate page headers on disk:

```
+-----------------------------------------------------------------------------------+
|                        bbolt SURGERY: REVERT-META-PAGE                            |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ Meta 0 (Active) ] ──► Points to Tx 2501 (Corrupted by abrupt shutdown crash)   |
|          │                                                                        |
|          ▼                                                                        |
|  [ Meta 1 (Standby)] ──► Points to Tx 2500 (Clean, fully committed, 100% valid!)  |
|                                                                                   |
|  Command: bbolt surgery revert-meta-page db --output repaired.db                  |
|  Result:  Forces header to read Meta 1 ──► Bypasses bad Tx with ZERO data loss!   |
+-----------------------------------------------------------------------------------+
```

#### Strategy A: Zero-Data-Loss Transaction Rollback (`revert-meta-page`)
Because bbolt alternates writes between `meta0` and `meta1`, the inactive meta page contains the *previous* fully committed transaction ($Tx_{N-1}$), which committed cleanly before the power failure:

```bash
# Revert active meta page to the preceding consistent transaction
sudo bbolt surgery revert-meta-page /var/lib/etcd.bak.*/member/snap/db \
  --output /var/lib/etcd/member/snap/db

# Re-run integrity check
sudo bbolt check /var/lib/etcd/member/snap/db
```
*Expected Output:*
```
OK
```

#### Strategy B: Abandon the Corrupted Freelist (`abandon-freelist`)
If both meta pages were affected by multi-page torn writes, abandon the corrupted freelist. bbolt will recalculate all free pages from scratch upon startup:

```bash
# Abandon freelist and write clean database
sudo bbolt surgery abandon-freelist /var/lib/etcd.bak.*/member/snap/db \
  --output /var/lib/etcd/member/snap/db

# Re-run integrity check
sudo bbolt check /var/lib/etcd/member/snap/db
# Expected Output: OK
```

---

### Step 6: Synchronize Snapshot Files & Set Ownership
etcd stores both the active `db` and periodic Raft snapshot files under `/var/lib/etcd/member/snap/`. If a numbered snapshot file (e.g. `000000000002e643.snap.db`) exists, synchronize it with the repaired database:

```bash
# Sync repaired db to any existing numbered snapshot files
LATEST_SNAP=$(ls -t /var/lib/etcd/member/snap/*.snap.db 2>/dev/null | head -n1 || true)
if [ -n "$LATEST_SNAP" ]; then
  sudo cp /var/lib/etcd/member/snap/db "$LATEST_SNAP"
fi

# Ensure correct root permissions on the data directory
sudo chown -R root:root /var/lib/etcd
```

---

### Step 7: Restart Kubelet and Verify Daemon Startup
Start the Kubelet service to launch the static pods:

```bash
sudo systemctl start kubelet

# Wait 10-15 seconds, then check static pod containers
sudo crictl ps | grep -E 'etcd|kube-apiserver'
```
*Verification:* Both containers should now show `Running` without restarting.

---

## 6. Post-Boot Recovery Traps & Secondary Outages

Once `etcd` boots cleanly, the cluster may encounter two common secondary outages caused by the database transaction rollback.

### Trap 1: API Server RBAC Lockout (`kubeadm:cluster-admins` vs `system:masters`)

#### The Problem
In Kubernetes v1.29+, `admin.conf` identifies as `O = kubeadm:cluster-admins` rather than the legacy `O = system:masters`. If the database rollback reverted an RBAC binding, `kubectl` commands fail with:
```console
Error from server (Forbidden): nodes is forbidden: User "kubernetes-admin" cannot list resource "nodes" in API group "" at the cluster scope
```

#### The Triage & Bypass
1. Temporarily add `--authorization-mode=AlwaysAllow` to `/etc/kubernetes/manifests/kube-apiserver.yaml`:
   ```yaml
   spec:
     containers:
     - command:
       - kube-apiserver
       - --authorization-mode=AlwaysAllow  # <-- Temporarily enable AlwaysAllow
   ```
2. Wait 10 seconds for Kubelet to reload `kube-apiserver`.
3. Create an explicit `ClusterRoleBinding` granting `cluster-admin` to the administrative identities:
   ```bash
   kubectl create clusterrolebinding kubeadm-admin-binding \
     --clusterrole=cluster-admin \
     --group=kubeadm:cluster-admins \
     --group=system:masters \
     --user=kubernetes-admin
   ```
4. Restore `--authorization-mode=Node,RBAC` in `/etc/kubernetes/manifests/kube-apiserver.yaml`.

---

### Trap 2: Missing CNI Subnet Environment (`/run/flannel/subnet.env`)

#### The Problem
On Linux systems, `/run` resides in a volatile memory filesystem (`tmpfs`). When a VM halts uncleanly, `/run/flannel/subnet.env` is erased.
Workload pods remain stuck in `ContainerCreating`:
```console
$ kubectl describe pod <pod-name>
Warning  FailedCreatePodSandBox  kubelet  Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox: plugin type="flannel" failed (add): failed to load flannel 'subnet.env' file: open /run/flannel/subnet.env: no such file or directory.
```

#### The Triage & Resolution
1. **Re-initialize Essential Kubeadm Addons:**
   ```bash
   sudo kubeadm init phase addon all
   ```
   *(This idempotently verifies and applies CoreDNS and `kube-proxy`)*.
2. **Re-apply the CNI Overlay Manifest:**
   ```bash
   kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
   ```
   *(The Flannel DaemonSet pod will generate `/run/flannel/subnet.env` and bring the node to `Ready`)*.
3. **Restart Stuck Workload Pods:**
   ```bash
   kubectl delete pod <stuck-pod-name> -n <namespace>
   ```

---

## 7. Diagnostic Cheat Sheet & 60-Second Disaster Recovery

### Rapid Diagnostic Matrix
| Diagnostic Step | Command | Healthy Indicator |
| :--- | :--- | :--- |
| **1. Kubelet Daemon** | `systemctl status kubelet` | `active (running)` |
| **2. Container Logs** | `crictl logs $(crictl ps -a --name etcd -q \| head -n1)` | Clean startup logs, no `panic:` |
| **3. Database Integrity** | `bbolt check /var/lib/etcd/member/snap/db` | `OK` |
| **4. etcd Endpoint Health** | `ETCDCTL_API=3 etcdctl --cacert=... --cert=... --key=... endpoint health` | `... is healthy: successfully committed proposal` |
| **5. API Server Readiness** | `curl -k https://127.0.0.1:6443/readyz` | `ok` |
| **6. Node Status** | `kubectl get nodes` | `Ready` |

### Production Automated Resuscitation Script (`/usr/local/bin/etcd-resuscitate.sh`)
```bash
#!/usr/bin/env bash
# etcd-resuscitate.sh: Automated zero-data-loss recovery for bbolt page collisions
set -euo pipefail

ETCD_DIR="/var/lib/etcd"
SNAP_DB="${ETCD_DIR}/member/snap/db"
BACKUP_DIR="/var/lib/etcd.bak.$(date +%s)"

echo "[*] Halting Kubelet..."
systemctl stop kubelet

echo "[*] Creating safety backup to ${BACKUP_DIR}..."
cp -r "${ETCD_DIR}" "${BACKUP_DIR}"

echo "[*] Running bbolt surgery: revert-meta-page..."
bbolt surgery revert-meta-page "${BACKUP_DIR}/member/snap/db" --output "${SNAP_DB}"

echo "[*] Checking repaired database integrity..."
if bbolt check "${SNAP_DB}"; then
    echo "[+] Database check passed: OK!"
else
    echo "[!] revert-meta-page failed. Attempting abandon-freelist..."
    bbolt surgery abandon-freelist "${BACKUP_DIR}/member/snap/db" --output "${SNAP_DB}"
    bbolt check "${SNAP_DB}"
fi

# Sync snapshot files
LATEST_SNAP=$(ls -t "${ETCD_DIR}/member/snap/"*.snap.db 2>/dev/null | head -n1 || true)
if [ -n "$LATEST_SNAP" ]; then
    cp "${SNAP_DB}" "$LATEST_SNAP"
fi

chown -R root:root "${ETCD_DIR}"
echo "[*] Restarting Kubelet..."
systemctl start kubelet

echo "[+] Resuscitation complete. Verify cluster with: kubectl get nodes"
```

---

## 8. Architectural Hardening & Prevention Runbook

To prevent bbolt transaction collisions in production and virtualized lab environments:

1.  **Sanitized Shutdown Procedure:**
    Never force-reset or ACPI-kill a Kubernetes host. Always flush dirty buffers before halting:
    ```bash
    sudo systemctl stop kubelet containerd docker
    sync
    sudo shutdown -h now
    ```
2.  **Automated Daily ETCD Snapshots with Offline Check:**
    Add a daily root cron job (`/etc/cron.daily/etcd-backup`):
    ```bash
    ETCDCTL_API=3 etcdctl snapshot save /opt/backups/etcd-$(date +%F).db \
      --cacert=/etc/kubernetes/pki/etcd/ca.crt \
      --cert=/etc/kubernetes/pki/etcd/server.crt \
      --key=/etc/kubernetes/pki/etcd/server.key
    
    # Offline verification
    bbolt check /opt/backups/etcd-$(date +%F).db
    ```
3.  **Dedicated NVMe Disk & Mount Flags:**
    Mount `/var/lib/etcd` on a dedicated high-speed SSD/NVMe volume with the `noatime` and `barrier=1` mount flags to ensure disk writes flush directly to non-volatile media without page cache stalls.
