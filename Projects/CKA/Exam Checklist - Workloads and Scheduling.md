---
class: exam-checklist
tier: project-note
project: "CKA Exam"
topics:
  - "Pod Spec & Shell overrides"
  - "Liveness/Readiness Probes"
  - "Deployment Upgrades/Rollbacks"
  - "DaemonSets"
  - "Static Pods"
  - "Jobs and CronJobs"
status: "Ready for Review"
---

# CKA Exam Checklist - Workloads and Scheduling

This guide is optimized for speed, precision, and accuracy on the CKA (Certified Kubernetes Administrator) exam. It covers core workload configurations, troubleshooting commands, and dry-run YAML tricks.

---

## 1. Pod YAML Generation & Modifications

Speed is critical during the exam. Never write a Pod manifest from scratch. Use imperative CLI generation and modify the output.

### 1.1 Rapid YAML Generation
Generate a baseline Pod template using `--dry-run=client -o yaml`:
```bash
# Generate basic nginx Pod manifest
kubectl run nginx-pod --image=nginx:alpine --dry-run=client -o yaml > pod.yaml
```

### 1.2 Overriding Commands and Arguments
Kubernetes `command` maps to Docker's `ENTRYPOINT`, and `args` maps to `CMD`.
*   **Command Override:** To set a custom entrypoint via the CLI, use the `--command` flag:
    ```bash
    # Generates a Pod that runs 'sleep 3600' as the primary process
    kubectl run sleep-pod --image=busybox --dry-run=client -o yaml --command -- sleep 3600
    ```
*   **Arguments Override:** Arguments are passed after the `--` separator:
    ```bash
    # Generates a Pod with custom arguments passed to the default entrypoint
    kubectl run echo-pod --image=busybox --dry-run=client -o yaml -- sh -c "echo Hello CKA"
    ```
*   **Resulting YAML structure:**
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: echo-pod
    spec:
      containers:
      - name: echo-pod
        image: busybox
        command: ["sh"]
        args: ["-c", "echo Hello CKA"]
    ```

### 1.3 Manual Scheduling Bypass via `spec.nodeName`
If you need to place a Pod on a specific node without using node selectors or scheduling rules (or if the Scheduler is down/broken), bypass the scheduler entirely by hardcoding `spec.nodeName`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: scheduler-bypass-pod
spec:
  nodeName: worker-node-01  # Bypasses scheduling entirely, ignoring taints!
  containers:
  - name: nginx
    image: nginx:alpine
```
> [!IMPORTANT]
> Pods scheduled via `nodeName` skip the scheduler filter phase. They will bind to the target node regardless of taints, resource limits, or other scheduling constraints.

---

## 2. Health Probes

Health probes are executed by the Kubelet to verify container status. The three probe types are:
1.  **Startup Probe:** Runs first. Blocks all other probes. If it fails, Kubelet restarts the container.
2.  **Liveness Probe:** Checks for deadlocks or frozen states. If it fails, Kubelet restarts the container.
3.  **Readiness Probe:** Checks if the container is ready for network traffic. If it fails, the Endpoints controller removes the Pod's IP from any matching Service.

### 2.1 HTTP Probe Snippet
```yaml
readinessProbe:
  httpGet:
    path: /healthz
    port: 8080
    httpHeaders:
    - name: Custom-Header
      value: Awesome
  initialDelaySeconds: 5
  periodSeconds: 10
  timeoutSeconds: 2
  successThreshold: 1
  failureThreshold: 3
```

### 2.2 TCP Probe Snippet
```yaml
livenessProbe:
  tcpSocket:
    port: 3306
  initialDelaySeconds: 15
  periodSeconds: 10
```

### 2.3 Exec Probe Snippet
```yaml
livenessProbe:
  exec:
    command:
    - cat
    - /tmp/healthy
  initialDelaySeconds: 5
  periodSeconds: 5
```

### 2.4 Native gRPC Probe Snippet (Kubernetes 1.24+)
Checks the community-standard `grpc.health.v1.Health` service.
```yaml
livenessProbe:
  grpc:
    port: 9000
    service: "search-service"  # Leave as empty string "" for general server health
  periodSeconds: 10
  timeoutSeconds: 2
```

### 2.5 Verifying and Troubleshooting Failing Probes
When a probe fails, the Kubelet emits events. Diagnose them using:
```bash
# 1. Inspect Pod details and look at the 'Events' section at the bottom
kubectl describe pod <pod-name>

# 2. Look for warning events with reason 'Unhealthy'
# Example Event: Warning  Unhealthy  4s  kubelet  Liveness probe failed: HTTP probe failed with statuscode: 500

# 3. Retrieve failure logs from the container
kubectl logs <pod-name> -c <container-name> --previous  # Check logs of the crashed container instance
```

---

## 3. Deployment Rollouts & Rollbacks

Deployments manage ReplicaSets to enable declarative, zero-downtime rolling updates.

### 3.1 Fast Image Update
Update the container image of a deployment directly from the CLI:
```bash
kubectl set image deployment/web-deploy web-container=nginx:1.25.4-alpine
```

### 3.2 Audit Rollout Status
Track the progress of the rolling update:
```bash
# Check status in real-time
kubectl rollout status deployment/web-deploy

# View history of deployment revisions
kubectl rollout history deployment/web-deploy

# View details of a specific revision
kubectl rollout history deployment/web-deploy --revision=3
```

### 3.3 Rollback Deployment
If an update causes failures, roll back immediately:
```bash
# Roll back to the immediate previous revision
kubectl rollout undo deployment/web-deploy

# Roll back to a specific revision
kubectl rollout undo deployment/web-deploy --to-revision=2
```

---

## 4. DaemonSet Migration

If the exam requires converting a Deployment to a DaemonSet, follow this fast conversion strategy:

### 4.1 Step-by-Step CLI Migration
1.  **Extract the Deployment YAML:**
    ```bash
    kubectl get deployment my-deploy -o yaml > ds-migration.yaml
    ```
    *(Or generate a fresh template: `kubectl create deployment my-deploy --image=nginx:alpine --dry-run=client -o yaml > ds-migration.yaml`)*

2.  **Open `ds-migration.yaml` in Vim and modify:**
    *   Change `kind: Deployment` to `kind: DaemonSet`.
    *   Remove `spec.replicas` (DaemonSets run one pod per node by default).
    *   Remove `spec.strategy` (DaemonSets use `updateStrategy`, not `strategy`).
    *   Remove status fields at the bottom (like `status: {}`).

3.  **Manage Tolerations / Affinities:**
    If the DaemonSet must run on control-plane/master nodes (which usually have taints), ensure you add the following tolerations under `spec.template.spec`:
    ```yaml
    spec:
      template:
        spec:
          tolerations:
          - key: node-role.kubernetes.io/control-plane
            operator: Exists
            effect: NoSchedule
          - key: node-role.kubernetes.io/master
            operator: Exists
            effect: NoSchedule
    ```

4.  **Apply the DaemonSet:**
    ```bash
    kubectl apply -f ds-migration.yaml
    ```

---

## 5. Static Pods Management

Static Pods are managed directly by the Kubelet on a specific node, bypassing the API Server control plane.

### 5.1 Locate Kubelet's Static Pod Manifest Path
1.  SSH into the target node:
    ```bash
    ssh worker-node-01
    ```
2.  Find the active Kubelet configuration file path:
    ```bash
    ps -ef | grep kubelet | grep config
    ```
    *(Look for `--config=/var/lib/kubelet/config.yaml` or similar).*
3.  Inspect the configuration file:
    ```bash
    sudo grep staticPodPath /var/lib/kubelet/config.yaml
    # Output: staticPodPath: /etc/kubernetes/manifests
    ```

### 5.2 Creating/Deleting Static Pods
*   **Create:** Copy your Pod manifest (e.g., `static-web.yaml`) to the static pod directory:
    ```bash
    sudo cp static-web.yaml /etc/kubernetes/manifests/
    ```
    *(The Kubelet will automatically detect the file and start the containers).*
*   **Delete:** Remove the manifest from the static pod directory:
    ```bash
    sudo rm /etc/kubernetes/manifests/static-web.yaml
    ```

### 5.3 Debugging Mirror Pod Sync Issues
Kubelet registers a read-only **Mirror Pod** (`<pod-name>-<node-name>`) with the API server so administrators can see it. If the Mirror Pod is missing or stuck:
1.  **Check Kubelet Status on the Host:**
    ```bash
    sudo systemctl status kubelet
    sudo journalctl -u kubelet -e
    ```
2.  **Inspect Runtime Containers Directly:**
    Bypass Kubelet using `crictl` to check if container runtime is executing the pod:
    ```bash
    sudo crictl pods
    sudo crictl ps
    ```
3.  **Check API Connectivity:**
    If Kubelet cannot reach the API Server, it cannot create the Mirror Pod, although the container continues running locally.

---

## 6. Jobs & CronJobs

### 6.1 Jobs (`batch/v1`)
Jobs run a container to completion. The `restartPolicy` under `spec.template.spec` must be set to `Never` or `OnFailure`.
*   `completions`: Desired number of successful pod completions.
*   `parallelism`: Max number of pods running concurrently.
*   `backoffLimit`: Max number of retries before marking the Job failed (Default: 6).
*   `activeDeadlineSeconds`: Hard execution timeout.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: backup-job
spec:
  completions: 3
  parallelism: 2
  backoffLimit: 4
  activeDeadlineSeconds: 300
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: backup
        image: busybox
        command: ["sh", "-c", "echo 'Backup complete'; sleep 5"]
```

### 6.2 CronJobs (`batch/v1`)
CronJobs schedule Jobs to run periodically using cron syntax (`* * * * *`).
*   `concurrencyPolicy`:
    *   `Allow` (Default): Multiple jobs can run concurrently.
    *   `Forbid`: Prevents concurrent runs; skips the next scheduled job if the current one is still running.
    *   `Replace`: Terminates the current job and starts a new one.
*   `startingDeadlineSeconds`: Time window to start the job if it misses its schedule.
*   `successfulJobsHistoryLimit`: Successful jobs to retain (Default: 3).

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: nightly-cleanup
spec:
  schedule: "0 1 * * *"  # Daily at 1:00 AM
  concurrencyPolicy: Forbid
  startingDeadlineSeconds: 120
  successfulJobsHistoryLimit: 5
  failedJobsHistoryLimit: 2
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: Never
          containers:
          - name: clean-tool
            image: alpine:latest
            command: ["sh", "-c", "echo 'Cleaning old files...'; sleep 10"]
```

---

## 7. StatefulSets & Stable Database Clustering

For clustered databases (e.g., MySQL, Postgres), workloads require stable network identities, ordering, and dedicated storage.

### 7.1 Key Characteristics
1.  **Companion Headless Service:** Requires `clusterIP: None` so CoreDNS resolves individual pod IP addresses instead of load-balancing them.
2.  **Stable DNS Format:** Ordinal index determines stable FQDN:
    $$\langle\text{pod-name}\rangle.\langle\text{service-name}\rangle.\langle\text{namespace}\rangle.\text{svc.cluster.local}$$
    *Example:* `db-node-0.db-service.default.svc.cluster.local`
3.  **Volume Claim Templates:** Provision a unique PVC for each pod ordinal (e.g., `data-db-node-0`). Storage re-binds to the exact same ordinal even if rescheduled to a different host node.

### 7.2 CoreDNS Verification Commands
If database replication fail, execute these lookups from a network utility pod (like `nicolaka/netshoot`):
```bash
# 1. Query Headless Service for all member IPs
nslookup db-service.default.svc.cluster.local

# 2. Query individual Pod Ordinal directly
dig +short db-node-0.db-service.default.svc.cluster.local

# 3. Query SRV records for port and ordinal member membership discovery
dig SRV _mysql._tcp.db-service.default.svc.cluster.local
```
