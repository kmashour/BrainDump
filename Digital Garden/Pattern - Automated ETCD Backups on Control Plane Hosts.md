---
obsidianUIMode: preview
class: pattern-note
tier: main-note
domains:
  - "kubernetes"
  - "linux"
  - "database"
  - "storage"
components:
  - "[[etcd]]"
  - "[[node]]"
sources:
  - "[[Reference Notes/0-10_maintenance_upgrades_and_etcd.md]]"
tags:
  - architecture/pattern
  - kubernetes/etcd
  - linux/systemd
  - database/backup
---

# Pattern: Automated ETCD Backups on Control Plane Hosts

**Breadcrumbs:** [[0-Index|🏠 Index]] > Patterns > **Automated ETCD Backups on Control Plane Hosts**

---

## 🏛️ Architectural Context

ETCD stores the absolute state of a Kubernetes cluster, including configuration secrets, namespace configurations, workloads, and cluster metadata. If ETCD fails or is corrupted, the cluster is lost. To guarantee recoverability, administrative operations require automating ETCD snapshots.

There are two primary paradigms for automating backups: running backups within a Kubernetes-native workload (e.g., a Kubernetes `CronJob`) or executing them directly on the Linux host operating system of the control plane nodes (using a `systemd` service and timer, or a host-level `cron` job).

### The Circular Dependency Vulnerability
Running ETCD backups inside a Kubernetes-native `CronJob` introduces a **circular dependency**:
1. The `CronJob` depends on the Kubernetes API server and scheduler to run.
2. The API server depends on ETCD to read/write state and authenticate requests.
3. If ETCD suffers a consensus failure or disk saturation, the API server crashes.
4. Because the API server is down, the Kubernetes scheduler cannot schedule the backup `CronJob` pod, leaving the cluster administrator without a recent, automated backup right when it is needed most.

### The Host-Level systemd Architecture
Executing backups via host-level services on the control plane nodes breaks this circular dependency. The backup process runs as a local Linux daemon, completely bypassing the Kubernetes control plane. It accesses ETCD directly via the localhost loopback interface (`https://127.0.0.1:2379`) using the node's local filesystem paths to reference the required ETCD client certificates.

```
+---------------------------------------------------------------------------------+
| CONTROL PLANE WORKER NODE (RHEL / Ubuntu)                                       |
|                                                                                 |
|  [ systemd-timer ] ---> [ systemd-service ] ---> [ etcd-backup.sh ]             |
|                                                          |                      |
|                                                          | Reads Local certs    |
|                                                          v                      |
|  [ ETCD Static Pod ] <--- Loopback (127.0.0.1) <--- [ Local Certificates ]     |
|         |                                        (ca.crt, server.crt, key)      |
|         | Writes                                                                |
|         v                                                                       |
|  [ Host Directory (/var/lib/etcd-backups) ]                                     |
|                                                                                 |
+---------------------------------------------------------------------------------+
```

---

## ⚖️ Trade-offs & Alternatives

Cluster administrators must choose where the backup agent sits:

### Approach A: Linux Host-Level systemd Service + Timer (Recommended)
* **Pros**:
  * **Zero Dependency**: Works even if the Kubernetes API server is completely broken or unresponsive.
  * **Security**: Certificates and private keys are read directly from local root-owned directories (`/etc/kubernetes/pki/etcd`) without exposing them to the pod network or service accounts.
  * **Simplicity**: No overhead from container networking, image pull secrets, or pod scheduling.
* **Cons**:
  * Requires access and automation (e.g., Ansible, Puppet) to configure the systemd unit files and scripts on every control plane node.
  * Backup logs are written to host journald/syslog rather than cluster-wide logging dashboards (unless syslog forwarders are configured).

### Approach B: Kubernetes-Native `CronJob`
* **Pros**:
  * Declared as standard Kubernetes YAML manifests, facilitating GitOps workflows.
  * Easy to monitor using standard tools (`kubectl get cronjobs`, Prometheus container metrics).
* **Cons**:
  * **Circular Dependency**: Fails to run if the control plane is unhealthy.
  * **Privilege Escalation Risk**: Requires mounting host filesystems (`hostPath` to `/etc/kubernetes/pki/etcd`) and using `hostNetwork: true` to bypass authentication and route traffic to the ETCD endpoint on localhost.

---

## 🛠️ Verification & Practical Implementation

To implement host-level automated ETCD backups:

### Step 1: Write the Backup Script
Create the backup script `/usr/local/bin/etcd-backup.sh`. This script takes a snapshot, verifies its integrity, logs outcomes to syslog, and implements a rotation policy to delete backups older than 7 days.

```bash
#!/usr/bin/env bash
set -euo pipefail

# Configurations
BACKUP_DIR="/var/lib/etcd-backups"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/etcd-snapshot-${TIMESTAMP}.db"
KEEP_DAYS=7

# Ensure backup directory exists
mkdir -p "${BACKUP_DIR}"

# Execute snapshot
echo "Starting ETCD snapshot to ${BACKUP_FILE}..."
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save "${BACKUP_FILE}"

# Verify snapshot integrity
echo "Verifying snapshot..."
ETCDCTL_API=3 etcdctl --write-out=table snapshot status "${BACKUP_FILE}"

# Rotate old backups
echo "Cleaning up backups older than ${KEEP_DAYS} days..."
find "${BACKUP_DIR}" -name "etcd-snapshot-*.db" -mtime +${KEEP_DAYS} -delete

echo "ETCD Backup completed successfully."
```

Make the script executable:
```bash
sudo chmod +x /usr/local/bin/etcd-backup.sh
```

### Step 2: Create the systemd Service
Define the service file `/etc/systemd/system/etcd-backup.service` to execute the script:

```ini
[Unit]
Description=Automated ETCD Backup Service
After=network.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/etcd-backup.sh
User=root
Group=root
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

### Step 3: Create the systemd Timer
Define the timer file `/etc/systemd/system/etcd-backup.timer` to run the service hourly (or daily):

```ini
[Unit]
Description=Run ETCD Backup Service Hourly

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
```

### Step 4: Enable and Start the Timer
```bash
# Reload systemd configuration
sudo systemctl daemon-reload

# Start and enable the timer
sudo systemctl enable --now etcd-backup.timer
```

### Step 5: Verification & Inspection
Verify the backup automation is operating correctly:

```bash
# List active systemd timers
systemctl list-timers --all | grep etcd-backup

# Trigger the backup service manually to verify
sudo systemctl start etcd-backup.service

# View the run history and stdout logs
journalctl -u etcd-backup.service -n 50

# Verify the backup file was created and is readable
ls -lh /var/lib/etcd-backups/
```
