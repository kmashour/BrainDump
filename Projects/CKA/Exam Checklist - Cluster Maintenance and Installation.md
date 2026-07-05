---
class: exam-checklist
tier: project-note
project: 'CKA Exam'
status: 'Ready for Review'
---

# CKA Exam Checklist - Cluster Maintenance and Installation

This guide covers node maintenance operations, sequential cluster upgrades, and ETCD backup/restore procedures.

---

## 1. Node Maintenance Mechanics (Cordon & Drain)

When performing node maintenance (OS updates, hardware scaling), you must safely evict workloads to prevent service downtime.

### 1.1 Key Concepts
*   **Cordoning (`kubectl cordon`)**: Marks a node as unschedulable by applying the `node.kubernetes.io/unschedulable:NoSchedule` taint. Existing pods continue running; new pods will not be scheduled.
*   **Draining (`kubectl drain`)**: Cordons the node first, then evicts all running workloads.
*   **Eviction API**: Respects `PodDisruptionBudgets` (PDBs), sending a `SIGTERM` followed by a `SIGKILL` (after the grace period). Recreated pods are scheduled elsewhere by controllers.

### 1.2 Step-by-Step Commands
```bash
# 1. Mark a node as unschedulable (without evicting workloads)
kubectl cordon <node-name>

# 2. Drain workloads from the node
kubectl drain <node-name> --ignore-daemonsets --force --delete-emptydir-data

# 3. Mark the node as schedulable again (post-maintenance)
kubectl uncordon <node-name>
```

> [!IMPORTANT]
> **Why these flags are mandatory on the CKA Exam:**
> *   `--ignore-daemonsets`: DaemonSet pods cannot be scheduled elsewhere. Draining will fail without this flag.
> *   `--force`: Forces eviction of "bare pods" (pods not managed by Deployments, ReplicaSets, StatefulSets, Jobs). **Warning:** These pods are permanently deleted.
> *   `--delete-emptydir-data`: Forces eviction of pods using local `emptyDir` volumes. **Warning:** Local volume data is permanently lost.

---

## 2. Kubeadm Cluster Upgrades

Kubernetes components follow Semantic Versioning (`vMajor.Minor.Patch`). Skip-upgrades (e.g. `v1.26` to `v1.28`) are unsupported. You must upgrade minor versions sequentially.

### 2.1 Version Skew Rules (Relative to kube-apiserver version X)
*   **kube-apiserver**: Reference version ($X$)
*   **kube-controller-manager / kube-scheduler**: Up to **1 minor version older** ($X$ to $X-1$)
*   **kubelet / kube-proxy**: Up to **2 minor versions older** ($X$ to $X-2$), extended to **3 minor versions** ($X$ to $X-3$) in `v1.28+`.
*   **kubectl**: Can be **1 minor version newer or older** ($X+1$ to $X-1$).

### 2.2 Chronological Upgrade Sequence
Upgrades must occur in this exact order:
1.  **Primary Control Plane Node** (kubeadm package $\rightarrow$ upgrade plan/apply $\rightarrow$ drain node $\rightarrow$ kubelet/kubectl package $\rightarrow$ uncordon).
2.  **Additional Control Plane Nodes** (kubeadm package $\rightarrow$ upgrade node $\rightarrow$ kubelet/kubectl package).
3.  **Worker Nodes** (drain node $\rightarrow$ kubeadm package $\rightarrow$ upgrade node $\rightarrow$ kubelet/kubectl package $\rightarrow$ uncordon).

### 2.3 Exact Command Playbook

#### A. Upgrading the Control Plane Node
```bash
# 1. Unhold and upgrade kubeadm package
sudo apt-mark unhold kubeadm
sudo apt-get update && sudo apt-get install -y --allow-change-held-packages kubeadm=1.28.2-00
sudo apt-mark hold kubeadm

# 2. Verify and apply the upgrade plan
sudo kubeadm upgrade plan
sudo kubeadm upgrade apply v1.28.2 -y

# 3. Drain the control plane node
kubectl drain controlplane --ignore-daemonsets

# 4. Upgrade kubelet and kubectl packages
sudo apt-mark unhold kubelet kubectl
sudo apt-get update && sudo apt-get install -y --allow-change-held-packages kubelet=1.28.2-00 kubectl=1.28.2-00
sudo apt-mark hold kubelet kubectl

# 5. Reload configuration and restart the kubelet service
sudo systemctl daemon-reload
sudo systemctl restart kubelet

# 6. Uncordon the control plane node
kubectl uncordon controlplane
```

#### B. Upgrading a Worker Node
```bash
# 1. Drain the worker node (Execute from Control Plane Node)
kubectl drain node-1 --ignore-daemonsets --force --delete-emptydir-data

# 2. SSH into the worker node and upgrade kubeadm
sudo apt-mark unhold kubeadm
sudo apt-get update && sudo apt-get install -y --allow-change-held-packages kubeadm=1.28.2-00
sudo apt-mark hold kubeadm

# 3. Apply the upgrade node configuration
sudo kubeadm upgrade node

# 4. Upgrade kubelet and kubectl on the worker node
sudo apt-mark unhold kubelet kubectl
sudo apt-get update && sudo apt-get install -y --allow-change-held-packages kubelet=1.28.2-00 kubectl=1.28.2-00
sudo apt-mark hold kubelet kubectl

# 5. Restart the kubelet
sudo systemctl daemon-reload
sudo systemctl restart kubelet

# 6. Uncordon the worker node (Execute from Control Plane Node)
kubectl uncordon node-1
```

---

## 3. ETCD Backup & Restore

ETCD stores the cluster's complete state. In a `kubeadm` cluster, ETCD runs as a static pod.

### 3.1 Extracting ETCD Credentials
Locate ETCD TLS parameters by inspecting `/etc/kubernetes/manifests/etcd.yaml` or running:
```bash
kubectl describe pod -n kube-system etcd-controlplane
```
Identify the values for:
*   `--listen-client-urls` (e.g. `https://127.0.0.1:2379`)
*   `--trusted-ca-file` (e.g. `/etc/kubernetes/pki/etcd/ca.crt`)
*   `--cert-file` (e.g. `/etc/kubernetes/pki/etcd/server.crt`)
*   `--key-file` (e.g. `/etc/kubernetes/pki/etcd/server.key`)

### 3.1.1 ETCD Network Ports & API Server Connections
During cluster diagnostics or network checks, you can inspect ETCD's listening ports on the control plane node:
- **Port `2379` (Client):** Front door for `kube-apiserver` queries (binds to `127.0.0.1` and host IP).
- **Port `2380` (Peer):** Internal Raft clustering replication channel (binds to routable host IP).
- **Port `2381` (Metrics):** Exposes Prometheus scraping values locally (binds to loopback `127.0.0.1`).

*Note:* Running `netstat -pant | grep etcd` will show dozens of active `ESTABLISHED` TCP connections to port `2379` from high-numbered host ports. These are concurrent channels maintained by the `kube-apiserver` to manage persistent resource **gRPC Watches** and **Connection Pooling** (for multiplexing API reads/writes).

### 3.2 Snapshot Backup Command
Always set `ETCDCTL_API=3` before calling `etcdctl`.
```bash
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /opt/backup/etcd-snapshot.db
```

Verify snapshot status:
```bash
ETCDCTL_API=3 etcdctl --write-out=table snapshot status /opt/backup/etcd-snapshot.db
```

---

### 3.3 Stacked ETCD Restore Playbook
Stacked ETCD runs as a static pod on the control plane.

1.  **Restore the snapshot database to a new directory:**
    ```bash
    ETCDCTL_API=3 etcdctl snapshot restore /opt/backup/etcd-snapshot.db \
      --data-dir /var/lib/etcd-from-backup
    ```
2.  **Verify or assign root ownership:**
    ```bash
    sudo chown -R root:root /var/lib/etcd-from-backup
    ```
3.  **Modify the Static Pod Manifest:**
    Edit `/etc/kubernetes/manifests/etcd.yaml`. Locate the volume named `etcd-data` and update its hostPath to the new restored directory.
    ```yaml
    # Inside /etc/kubernetes/manifests/etcd.yaml
    spec:
      volumes:
      - hostPath:
          path: /var/lib/etcd-from-backup # <-- Update this path from /var/lib/etcd
          type: DirectoryOrCreate
        name: etcd-data
    ```
4.  **Verification:**
    The kubelet will detect changes and restart the ETCD static pod.
    ```bash
    kubectl get nodes
    kubectl get pods -n kube-system
    ```

---

### 3.4 External ETCD Restore Playbook
External ETCD runs on separate dedicated hosts as a systemd service.

1.  **SSH into the external ETCD host and stop the service:**
    ```bash
    ssh etcd-server
    sudo systemctl stop etcd
    ```
2.  **Restore the snapshot to a new data directory:**
    ```bash
    ETCDCTL_API=3 etcdctl snapshot restore /tmp/etcd-snapshot.db \
      --data-dir /var/lib/etcd-data-new
    ```
3.  **Assign ownership to the etcd service user:**
    ```bash
    sudo chown -R etcd:etcd /var/lib/etcd-data-new
    ```
4.  **Edit the systemd service file:**
    Open `/etc/systemd/system/etcd.service` and update the `--data-dir` flag:
    ```ini
    ExecStart=/usr/local/bin/etcd \
      --data-dir=/var/lib/etcd-data-new \
      ...
    ```
5.  **Reload configuration and restart the service:**
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl restart etcd.service
    sudo systemctl status etcd.service
    ```

---

## 4. Certificates API & Manual Certificate Management

On the CKA exam, you may need to generate user credentials manually and authorize them via the Certificates API.

### 4.1 CLI Commands for User Creation & Approval
1. **Generate a Private Key and CSR:**
   ```bash
   openssl genrsa -out developer.key 2048
   openssl req -new -key developer.key -out developer.csr -subj "/CN=developer/O=devs"
   ```
2. **Apply the CertificateSigningRequest (CSR) resource:**
   ```yaml
   apiVersion: certificates.k8s.io/v1
   kind: CertificateSigningRequest
   metadata:
     name: developer-csr
   spec:
     request: <BASE64_ENCODED_CSR>
     signerName: kubernetes.io/kube-apiserver-client
     usages:
     - client auth
   ```
3. **Approve the CSR:**
   ```bash
   kubectl certificate approve developer-csr
   ```
4. **Extract the Issued Certificate:**
   ```bash
   kubectl get csr developer-csr -o jsonpath='{.status.certificate}' | base64 --decode > developer.crt
   ```

---

## 5. Swap Memory Configuration on Nodes

By default, Kubelet fails if swap is active. Follow these steps to configure swap:

### 5.1 Kubelet Swap Configuration Checklist
1. **Edit Kubelet Configuration** at `/var/lib/kubelet/config.yaml`:
   ```yaml
   failSwapOn: false
   memorySwap:
     swapBehavior: LimitedSwap
   ```
2. **Restart Kubelet:**
   ```bash
   sudo systemctl restart kubelet
   ```
3. **Validate Node & Pod Swap Usage:**
   ```bash
   kubectl top nodes --show-swap
   kubectl top pods -n default --show-swap
   ```

---

## 6. Admission Webhooks and Troubleshooting

You must debug failing API calls caused by webhook timeouts or availability issues.

### 6.1 Diagnostic Workflow
1. **Identify the Failing Webhook:**
   Read the API error returned by `kubectl` (e.g. `failed calling webhook "my-webhook.example.com"`).
2. **Review Webhook Configuration:**
   Identify the backend service name and namespace:
   ```bash
   kubectl get validatingwebhookconfigurations -o yaml
   # or MutatingWebhookConfigurations
   ```
3. **Verify Backend Pods & Endpoints:**
   Ensure the backing pods are running and endpoints exist:
   ```bash
   kubectl get pods -n <webhook-namespace>
   kubectl get ep <webhook-service-name> -n <webhook-namespace>
   ```
4. **Bypass/Temporary Fix (If Allowed/Necessary):**
   Change `failurePolicy` from `Fail` to `Ignore` in emergency troubleshooting:
   ```bash
   kubectl edit validatingwebhookconfiguration <webhook-name>
   ```

---

## 7. API Priority and Fairness (APF) Diagnostics

APF prevents API server exhaustion by isolating and queueing requests.

### 7.1 APF CLI Diagnostics Checklist
1. **List Active Configuration Rules:**
   ```bash
   kubectl get flowschemas
   kubectl get prioritylevelconfigurations
   ```
2. **Analyze Rejected Requests:**
   Query the raw metrics from the API server:
   ```bash
   kubectl get --raw /metrics | grep apiserver_flowcontrol_rejected_requests_total
   ```

---

## 8. Graceful Node Shutdown and systemd Locks

Ensure node drains execute correctly during reboots.

### 8.1 Verification and Settings Checklist
1. **Configure systemd logind delay limit:**
   Ensure `/etc/systemd/logind.conf` allows enough delay (e.g., `InhibitDelayMaxSec=45`).
2. **Verify active inhibitor locks on the host:**
   ```bash
   systemd-inhibit --list
   ```
3. **Handle crashed nodes with persistent volumes:**
   If a node shuts down non-gracefully, force volume migration using the out-of-service taint:
   ```bash
   kubectl taint nodes <failed-node> node.kubernetes.io/out-of-service=nodeshutdown:NoExecute
   ```

