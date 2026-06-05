---
class: exam-checklist
tier: project-note
project: "CKA Exam"
topics:
  - "etcd Backup and Restore"
  - "Static Pods"
  - "Scheduler Bypass"
  - "Probes"
  - "crictl Debugging"
status: "Ready for Review"
---

# Exam Checklist: Core Architecture and API

This exam guide details the practical CLI formulas, configuration paths, manifest modifications, and troubleshooting workflows required for the core architecture and API mechanics of the CKA (Certified Kubernetes Administrator) exam.

---

## 1. etcd Backup & Restore

On the control plane node, `etcd` runs as a Static Pod. All Kubernetes state is stored here. If the control plane fails or state is corrupted, you must restore it from a snapshot.

### A. Environment Configuration & Target Certificates
The `etcdctl` CLI tool defaults to API version 2. You **must** force it to use API version 3 for modern Kubernetes:
```bash
export ETCDCTL_API=3
```

To authenticate with the secure etcd cluster, locate the following TLS certificates and keys in `/etc/kubernetes/pki/etcd/` (or via the arguments list of the running etcd pod):
*   **CA Certificate:** `--cacert=/etc/kubernetes/pki/etcd/ca.crt`
*   **Client Certificate:** `--cert=/etc/kubernetes/pki/etcd/server.crt`
*   **Client Private Key:** `--key=/etc/kubernetes/pki/etcd/server.key`

### B. Command Formulas

#### 1. Save Snapshot
Execute the `snapshot save` command. Always provide the certificates and point to the localhost endpoint:
```bash
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /var/lib/backup/etcd-snapshot.db
```

#### 2. Verify Snapshot
Verify that the snapshot file is valid and not corrupted before proceeding with a restore:
```bash
ETCDCTL_API=3 etcdctl --write-out=table snapshot status /var/lib/backup/etcd-snapshot.db
```

#### 3. Restore Snapshot to a New Data Directory
To restore, specify a **new host data directory** (e.g., `/var/lib/etcd-backup`). Do **not** overwrite the active directory (`/var/lib/etcd`) directly while etcd is running.
```bash
ETCDCTL_API=3 etcdctl \
  --data-dir=/var/lib/etcd-backup \
  snapshot restore /var/lib/backup/etcd-snapshot.db
```

### C. Updating the etcd Static Pod Manifest
Once the snapshot is restored to `/var/lib/etcd-backup`, you must point the etcd static pod to it:

1.  Open the etcd static pod manifest:
    ```bash
    sudo vi /etc/kubernetes/manifests/etcd.yaml
    ```
2.  Locate the `volumes` list at the bottom of the manifest. Update the `hostPath` for the volume named `etcd-data`:
    ```yaml
    volumes:
    - hostPath:
        path: /var/lib/etcd-backup  # <-- Change from /var/lib/etcd
        type: DirectoryOrCreate
      name: etcd-data
    ```
3.  *Note:* Do **not** change the `volumeMounts` path (`mountPath: /var/lib/etcd`) or the container arguments (`--data-dir=/var/lib/etcd`). The container will still write to `/var/lib/etcd` inside its own isolated filesystem, which is now mounted to the new host path `/var/lib/etcd-backup`.
4.  Save and exit. The local `kubelet` will automatically detect the manifest change, terminate the old etcd pod, and restart it with the restored database.

---

## 2. Static Pods

Static Pods are managed directly by the `kubelet` daemon on a specific node, bypassing the API Server control plane. They cannot be controlled by Deployments, DaemonSets, or the Scheduler.

### A. Finding the Kubelet Static Pod Directory
The `kubelet` configuration file defines where it monitors for static pod YAML files.

1.  Check the systemd unit file of the `kubelet` service:
    ```bash
    systemctl cat kubelet
    ```
    *Look for the `--config` flag value (typically `/var/lib/kubelet/config.yaml`).*
2.  Inspect the configuration file for the `staticPodPath` directive:
    ```bash
    grep -i "staticPodPath" /var/lib/kubelet/config.yaml
    ```
    *Output is usually:* `staticPodPath: /etc/kubernetes/manifests`

### B. Creating a Static Pod
To launch a static pod, generate a YAML manifest and save it directly to the designated static pod directory (e.g., `/etc/kubernetes/manifests`):

```bash
kubectl run static-nginx --image=nginx --port=80 --dry-run=client -o yaml > /etc/kubernetes/manifests/static-nginx.yaml
```

The Kubelet will detect the file and deploy the pod. The pod's name will automatically be suffixed with the node name: `static-nginx-<node-name>`.

### C. Resolving Mirror Pod Differences & Troubleshooting
*   **Mirror Pods:** Kubelet automatically creates a read-only "mirror pod" on the API server so that the static pod is visible via `kubectl get pods`.
*   **Immutable Mirror:** If you run `kubectl delete pod static-nginx-<node-name>`, the API server deletes the mirror reference, but the local Kubelet instantly regenerates it.
*   **Deletion Recovery:** To delete the static pod, you **must** log into the node and remove the YAML file from the static pod path:
    ```bash
    rm /etc/kubernetes/manifests/static-nginx.yaml
    ```
*   **Mismatch Triage:** If a static pod is modified on disk but the change isn't reflected, check the Kubelet service logs:
    ```bash
    journalctl -u kubelet -n 100 --no-pager
    ```

---

## 3. Scheduler Bypass

If the `kube-scheduler` is down or misconfigured, new pods will remain in the `Pending` state. You can bypass the scheduler to run workloads using two methods:

### A. Static Node Assignment (`spec.nodeName`)
Define the target node name explicitly in your PodSpec. The `kubelet` on that node will detect the pod, bypass the scheduler, and run it:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: scheduler-bypass-pod
spec:
  nodeName: worker-node-01  # <-- Directly bind to this node
  containers:
  - name: web
    image: nginx
```

### B. Manual Binding via the Binding API Resource
If a Pod is already created, is stuck in `Pending` state, and cannot be recreated with `nodeName`, you can manually bind it to a node using a `Binding` API subresource.

1.  Create a JSON payload named `binding.json`:
    ```json
    {
      "apiVersion": "v1",
      "kind": "Binding",
      "metadata": {
        "name": "pending-pod-name"
      },
      "target": {
        "apiVersion": "v1",
        "kind": "Node",
        "name": "worker-node-01"
      }
    }
    ```
2.  Start a local proxy in the background to access the API server securely:
    ```bash
    kubectl proxy &
    ```
3.  Send a POST request to the pod's `/binding` subresource endpoint:
    ```bash
    curl -X POST -H "Content-Type: application/json" \
      --data @binding.json \
      http://127.0.0.1:8001/api/v1/namespaces/default/pods/pending-pod-name/binding
    ```
4.  Kill the proxy once finished:
    ```bash
    kill %1
    ```

---

## 4. Health Probes

Probes are container health checks managed locally by the Kubelet. The CKA exam requires configuring them using different mechanisms (Exec, HTTPGet, TCP).

### A. Probe Types
1.  **`startupProbe`:** Runs first. Disables other probes until it succeeds. Prevents slow-starting containers from being killed prematurely.
2.  **`livenessProbe`:** Determines if a container needs to be restarted. If it fails, Kubelet restarts the container.
3.  **`readinessProbe`:** Determines if a container is ready to receive network traffic. If it fails, the container IP is removed from Service endpoints.

### B. Syntax Examples

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: probe-showcase
spec:
  containers:
  - name: app
    image: nginx
    ports:
    - containerPort: 80
    
    # 1. Startup Probe using TCP Socket Check
    startupProbe:
      tcpSocket:
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 10
      failureThreshold: 30  # Allows 30 attempts (300 seconds max startup)
      
    # 2. Liveness Probe using Exec Command Check
    livenessProbe:
      exec:
        command:
        - cat
        - /var/run/nginx.pid
      initialDelaySeconds: 10
      periodSeconds: 5
      timeoutSeconds: 2
      failureThreshold: 3
      
    # 3. Readiness Probe using HTTP GET Check
    readinessProbe:
      httpGet:
        path: /index.html
        port: 80
        httpHeaders:
        - name: Custom-Probe-Header
          value: Verification
      initialDelaySeconds: 5
      periodSeconds: 5
      successThreshold: 1
      failureThreshold: 2
```

---

## 5. Local CRICTL & Node Troubleshooting

When worker nodes fail, show `NotReady`, or lose api-server connection, you must use node-level diagnostic utilities.

### A. Setting the Socket Endpoint
`crictl` requires a connection to the container runtime socket. You can configure this three ways:

1.  **Persistently in `/etc/crictl.yaml`:**
    ```yaml
    runtime-endpoint: unix:///run/containerd/containerd.sock
    image-endpoint: unix:///run/containerd/containerd.sock
    timeout: 2
    debug: false
    ```
2.  **Via Environment Variable (Session-level):**
    ```bash
    export CONTAINER_RUNTIME_ENDPOINT=unix:///run/containerd/containerd.sock
    ```
3.  **Via Command Line Flag (One-off):**
    ```bash
    crictl --runtime-endpoint unix:///run/containerd/containerd.sock ps
    ```

#### Common Runtime Sockets:
*   **containerd:** `unix:///run/containerd/containerd.sock`
*   **CRI-O:** `unix:///run/crio/crio.sock`
*   **Docker (via cri-dockerd):** `unix:///var/run/cri-dockerd.sock`

### B. Core Node-Level Commands

Always use the local node runtime tools when debugging `NotReady` nodes:

| Diagnostic Action | crictl (Container Runtime level) | journalctl (Systemd level) |
| :--- | :--- | :--- |
| **Inspect Pod Sandboxes** | `crictl pods` | — |
| **List Containers** | `crictl ps` (use `-a` to show failed) | — |
| **Container Status** | `crictl inspect <container-id>` | — |
| **Fetch Container Logs** | `crictl logs <container-id>` | — |
| **Service Status** | — | `systemctl status kubelet` |
| **Stream Live Logs** | — | `journalctl -u kubelet -f` |
| **Filtered Log Search** | — | `journalctl -u kubelet -n 100 --no-pager` |

> [!WARNING]
> Containers created or managed via `crictl` are local runtime objects and are **not** synchronized with the Kubernetes control plane. Do not use `crictl run` to start application workloads. Use it strictly for read-only inspection and log analysis.

### C. Systemd Service & Kubelet Debugging

When a system-level component like the Kubelet fails to start or goes offline, debug using standard systemd tools:

1.  **Inspect Service Status:**
    ```bash
    systemctl status kubelet
    ```
    *Look for whether the service is `active (running)`, `inactive (dead)`, or `failed`.*

2.  **Extract Service Logs via Journalctl:**
    Always use `-e` (jump to end of logs) or `-n` (limit lines) and `--no-pager` to inspect without screen blocking:
    ```bash
    # Show the last 100 log lines for kubelet
    journalctl -u kubelet -n 100 --no-pager
    
    # Jump directly to the end of the logs
    journalctl -u kubelet -e
    
    # Follow the logs in real-time
    journalctl -u kubelet -f
    ```

3.  **Applying Configuration Updates:**
    If you edit the Kubelet unit file (typically `/etc/systemd/system/kubelet.service` or `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf`), you **must** reload the systemd configuration manager before restarting:
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl restart kubelet
    ```

4.  **Common Failures to Check:**
    *   **Swap Enabled:** By default, Kubelet fails if swap is on. Check using `free -m` or `swapon -s`. Temporarily disable with `sudo swapoff -a`.
    *   **Cgroup Driver Mismatch:** Ensure the cgroup driver matches between the container runtime (e.g. `systemd` in containerd) and kubelet config (`cgroupDriver: systemd` in `/var/lib/kubelet/config.yaml`).

### D. HostPath Volume & Directory Traversal Troubleshooting

When mounting files or directories from a Kubernetes worker node using `hostPath` volumes, permission and path structure mismatches are common causes of application crashes.

1.  **Directory Traversal (The Execute 'x' Bit):**
    For a containerized process running under a non-root UID (e.g., `securityContext.runAsUser: 1000`) to access a mounted host path `/data/db`, it must possess traversal rights.
    *   **The Trap:** If a parent directory on the host (e.g., `/data`) is owned by `root:root` with permissions `700` (`drwx------`), the kernel blocks any user other than root from traversing `/data` to reach `/data/db`, even if `/data/db` itself has `777` permissions.
    *   **The Solution:** Grant the execute (`x`) permission on *every* parent directory in the path on the host. You can do this by setting permissions (e.g., `chmod +x /data` or `chmod 755 /data`) or applying a File Access Control List (FACL):
        ```bash
        # Grant traversal (execute) permission specifically to the container UID
        sudo setfacl -m u:1000:x /data
        ```

2.  **Symbolic Links in HostPath Mounts:**
    If a `hostPath` volume points to a symbolic link on the host (e.g., `/var/lib/gitea` which symlinks to `/app/gitea`):
    *   **The Trap:** The container engine mounts the path on the host. If `/var/lib/gitea` is mounted, the runtime resolves the symlink and mounts the target `/app/gitea` into the container. However, if the symbolic link is broken, or points outside the host namespace (or container root), the mount will fail or show up as empty.
    *   **The Solution:** Always mount the **physical target directory** (e.g., `/app/gitea`) instead of the symbolic link in the `hostPath` volume manifest to bypass path resolution overhead and prevent broken-link failures.

3.  **SELinux Contexts:**
    If the worker nodes run in SELinux enforcing mode, host directories must have the correct container context (`container_file_t`) for the container runtime to mount and write to them:
    *   To automatically append the correct SELinux volume context flag, use the `:z` (shared write) or `:Z` (private write) volume mount options or set the host path SELinux context:
        ```bash
        sudo chcon -Rt container_file_t /app/gitea
        ```

---

## 6. Kubernetes API Management & Validation

### A. Bypassing Client-Side Validation (`--validate=false`)
When there is a significant version skew between the local `kubectl` client and the cluster's `kube-apiserver`, or when working with newly created Custom Resource Definitions (CRDs), the local OpenAPI schema cache (stored under `~/.kube/cache/schema/`) might be outdated or out of sync. This can result in:
* **False Rejections**: `kubectl` blocking a valid manifest locally because it does not recognize a new field.
* **Validation Hangs / Errors**: Version discrepancies causing local structural checks to fail before the request ever reaches the cluster.

To bypass local pre-flight checks and send the raw manifest directly to the API server:
```bash
kubectl apply -f manifest.yaml --validate=false
```
* **Under the Hood**: Bypassing client-side validation does *not* bypass security. The `kube-apiserver` still performs full server-side validation and admission control on the resource. It only bypasses the local, cached client-side schema checks.

### B. The 'last-applied-configuration' Warning and Mixed Management
If you mix imperative commands (like `kubectl create` or `kubectl run` without the `--save-config` flag) and declarative operations (like `kubectl apply`), you will see the following warning:
```plaintext
Warning: resource <kind>/<name> is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. The missing annotation will be patched automatically.
```

#### Why it Occurs
* **Imperative Commands**: `kubectl create` and `kubectl run` create resources directly in `etcd` without writing the `kubectl.kubernetes.io/last-applied-configuration` annotation.
* **Declarative Operations**: `kubectl apply` compares your local file against the `last-applied-configuration` annotation to determine updates and deletions. Without this annotation, it cannot compute precise differences.

#### Exam Action Plan
1. **Ignore it**: The warning is non-fatal. During the CKA exam, if you run `kubectl apply` on an imperatively created resource and get this warning, the API server will automatically patch the annotation on the fly. You can safely ignore the warning to save time.
2. **Use Server-Side Apply (SSA)**: Run `kubectl apply -f manifest.yaml --server-side` to use Server-Side Apply. SSA tracks field changes natively in `metadata.managedFields` rather than using the `last-applied-configuration` annotation. This bypasses the strict requirement for the annotation and solves the etcd metadata size constraint (approx. 256KB annotation limit in etcd) for extremely large manifests.

