---
class: exam-checklist
tier: project-note
project: "CKA Exam"
topics:
  - "Pod Spec & Shell overrides"
  - "Liveness/Readiness Probes"
  - "Deployment Upgrades/Rollbacks"
  - "ReplicaSets & Selectors"
  - "DaemonSets"
  - "Static Pods"
  - "Jobs and CronJobs"
  - "Node Selector & Node Affinity"
  - "Taints & Tolerations"
  - "ConfigMaps & Secrets Injection"
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

## 3.5 ReplicaSets, Selectors & Ownership Mechanics

ReplicaSets ensure that a declared number of Pod replicas run in a namespace. While Deployments manage them, you must understand their low-level mechanics and troubleshooting patterns for the CKA.

### 3.5.1 Set-Based Selectors (`matchExpressions`)
Unlike legacy replication controllers, ReplicaSets support set-based selectors. Use this format:
```yaml
spec:
  replicas: 3
  selector:
    matchExpressions:
      - {key: app, operator: In, values: [frontend, api]}
      - {key: env, operator: NotIn, values: [dev, qa]}
      - {key: tier, operator: Exists}
      - {key: legacy-app, operator: DoesNotExist}
```
*Operators Cheat Sheet:*
*   `In` / `NotIn`: Checks if the label value matches one in the list.
*   `Exists` / `DoesNotExist`: Checks if the key exists on the Pod. Do **not** specify a `values` block.

### 3.5.2 Adoption & Orphaning Mechanics
*   **Adoption:** If a ReplicaSet is created and there are orphaned Pods matching its selector, the controller manager injects `metadata.ownerReferences` into those Pods pointing to the ReplicaSet UID. This adopts them instead of spinning up new Pods.
*   **Orphaning:** To delete a ReplicaSet but leave its Pods running, run:
    ```bash
    kubectl delete replicaset <rs-name> --cascade=orphan
    ```

### 3.5.3 API Validation Webhook
The `apps/v1` API Server validates that the selector (`spec.selector.matchLabels` and/or `spec.selector.matchExpressions`) is a **subset** of the template labels (`spec.template.metadata.labels`).
If they mismatch, the request is rejected with a `Forbidden: selector does not match template labels` error and never persisted in `etcd`.

### 3.5.4 Advanced Troubleshooting: Thrashing Loops
 Runaway Pod creation/deletion loops (thrashing) are caused by:
1.  **Overlapping Selectors:** If two ReplicaSets have the same label selector but different template configurations, they will continuously delete and recreate each other's Pods since scale-down does not verify `ownerReferences`.
    *   *Fix:* Edit both workloads to specify unique, non-overlapping selectors (e.g. adding a `tier` or `env` label).
2.  **Mutating Webhook Interference:** A mutating admission webhook strips or alters the labels of created Pods. The ReplicaSet never sees its selector satisfied, leading to endless Pod creation requests.
    *   *Fix:* Check mutating webhook configurations or audit Pod label states.

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

---

## 8. Advanced Node Scheduling (Node Selectors & Node Affinity)

### 8.1 Node Selector (`nodeSelector`)
`nodeSelector` uses simple equality-based matching:
```yaml
spec:
  nodeSelector:
    disktype: ssd # Node must have label 'disktype=ssd'
```
*   **Label Node:** `kubectl label nodes <node-name> disktype=ssd`
*   **Remove Label:** `kubectl label nodes <node-name> disktype-`

### 8.2 Node Affinity (`nodeAffinity`)
Node Affinity uses set-based expression matching:
*   `requiredDuringSchedulingIgnoredDuringExecution`: Hard constraint. If not met, Pod stays `Pending`.
*   `preferredDuringSchedulingIgnoredDuringExecution`: Soft constraint. Scheduler assigns weights (1-100) to prioritize nodes.

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: topology.kubernetes.io/zone
            operator: In
            values:
            - us-east-1a
            - us-east-1b
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 50
        preference:
          matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
```

---

## 9. Node Taints and Pod Tolerations

Taints allow nodes to repel Pods. Tolerations allow Pods to run on tainted nodes.

### 9.1 Applying and Removing Taints
*   **Taint Node:** `kubectl taint nodes <node-name> dedicated=special-user:NoSchedule`
*   **Remove Taint:** `kubectl taint nodes <node-name> dedicated=special-user:NoSchedule-`
*   **Effects:**
    *   `NoSchedule`: Pod won't be scheduled unless it tolerates the taint.
    *   `PreferNoSchedule`: Scheduler will avoid placing the Pod on the node.
    *   `NoExecute`: Pod is evicted if it does not tolerate the taint.

### 9.2 Pod Toleration Syntax
```yaml
spec:
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "special-user"
    effect: "NoSchedule"
  - key: "infra-only"
    operator: "Exists"
    effect: "NoSchedule"
```

### 9.3 Remove Master/Control-Plane Taints (for single-node testing)
```bash
# Allow pods to run on the control-plane/master nodes
kubectl taint nodes --all node-role.kubernetes.io/control-plane- --ignore-not-found=true
kubectl taint nodes --all node-role.kubernetes.io/master- --ignore-not-found=true
```

---

## 10. ConfigMaps & Secrets Injection

### 10.1 Imperative Creation
```bash
# Create ConfigMap
kubectl create configmap app-config --from-literal=db_host=mysql-svc --from-literal=db_port=3306

# Create Secret
kubectl create secret generic db-secret --from-literal=db_password=supersecret
```

### 10.2 Bulk Environment Injection (`envFrom`)
Inject all key-value pairs from ConfigMap/Secret as environment variables:
```yaml
spec:
  containers:
  - name: app
    image: nginx:alpine
    envFrom:
    - configMapRef:
        name: app-config
    - secretRef:
        name: db-secret
```

### 10.3 Target Environment Injection (`valueFrom`)
```yaml
spec:
  containers:
  - name: app
    image: nginx:alpine
    env:
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: db_password
```

### 10.4 Volume Mount Injection
Mount keys as files inside a directory:
```yaml
spec:
  containers:
  - name: app
    image: nginx:alpine
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
    - name: secret-volume
      mountPath: /etc/secret
      readOnly: true
  volumes:
  - name: config-volume
    configMap:
      name: app-config
  - name: secret-volume
    secret:
      secretName: db-secret
      defaultMode: 0600 # strict permissions for security
```
> [!WARNING]
> **Exam Pitfall:** Mounting using `subPath` (e.g., to mount a single file inside an existing directory) disables Kubelet dynamic updates for that mounted volume.

---

## 11. Advanced Scheduling Constraints & Eviction Checklists

#### 1. Topology Spread Constraints Spec Checklist
If the exam asks you to spread Pods evenly across Availability Zones or Node Hostnames:
*   Add `topologySpreadConstraints` under `spec.template.spec`:
    ```yaml
    topologySpreadConstraints:
    - maxSkew: 1
      topologyKey: topology.kubernetes.io/zone
      whenUnsatisfiable: DoNotSchedule # or ScheduleAnyway
      labelSelector:
        matchLabels:
          app: my-app
    ```
*   Verify that `labelSelector.matchLabels` matches the Pod labels in the deployment template.
*   Verify that `maxSkew` is a positive integer (usually `1` is requested).

#### 2. Pod Priority and Preemption Debugging
If a high-priority Pod is stuck `Pending` and you need to verify if it will preempt lower-priority Pods:
1.  **Check the PriorityClass**:
    ```bash
    kubectl get priorityclasses
    ```
2.  **Define priorityClassName on the Pod**:
    Ensure the Pod spec contains `priorityClassName: <class-name>`.
3.  **Inspect Preemption Events**:
    ```bash
    kubectl get events -A --sort-by='.metadata.creationTimestamp'
    ```
    *Look for*: `Preempting` events showing that Kube-scheduler is terminating lower-priority pods to schedule the high-priority pod.

#### 3. Pod Scheduling Readiness Gates
If a Pod is created but remains `Pending` without any scheduling attempts (no events from the scheduler):
1.  **Check for Scheduling Gates**:
    Inspect the Pod YAML:
    ```bash
    kubectl get pod <pod-name> -o yaml
    ```
    *Look for*:
    ```yaml
    spec:
      schedulingGates:
      - name: example.com/external-check
    ```
2.  **Release the Gate**:
    Remove the gate using a patch command:
    ```bash
    kubectl patch pod <pod-name> --type='json' -p='[{"op": "remove", "path": "/spec/schedulingGates"}]'
    ```

#### 4. Kubelet Node-Pressure Eviction Diagnostics
If Pods in a namespace are suddenly terminated with status `Failed` and reason `Evicted`:
1.  **Describe the Evicted Pod**:
    ```bash
    kubectl describe pod <pod-name>
    ```
    *Look for*: `Status: Failed`, `Reason: Evicted`, and message indicating resource pressure (e.g. `The node was low on resource: [DiskPressure]`).
2.  **Inspect Node Conditions**:
    ```bash
    kubectl get nodes
    ```
    *Look for*: Node status showing `MemoryPressure`, `DiskPressure`, or `PIDPressure` as `True`.
3.  **Check Kubelet Logs**:
    SSH to the node and check Kubelet logs to verify the eviction thresholds configuration:
    ```bash
    journalctl -u kubelet -e | grep -i eviction
    ```
    *Common threshold configs in `/var/lib/kubelet/config.yaml`:*
    ```yaml
    evictionHard:
      memory.available: "100Mi"
      nodefs.available: "10%"
    ```

#### 5. Scheduler Bin-Packing Configuration Cheatsheet
If asked to configure or debug scheduler bin-packing (`MostAllocated` or `RequestedToCapacityRatio` in the `NodeResourcesFit` score plugin):
*   Verify the profile settings under `pluginConfig` in the `KubeSchedulerConfiguration` file:
    ```yaml
    apiVersion: kubescheduler.config.k8s.io/v1
    kind: KubeSchedulerConfiguration
    profiles:
    - pluginConfig:
      - name: NodeResourcesFit
        args:
          scoringStrategy:
            type: MostAllocated # or RequestedToCapacityRatio
            resources:
            - name: cpu
              weight: 1
            - name: memory
              weight: 1
    ```
*   Ensure that weight values are integers.

#### 6. PodGroup & TAS Scheduling Validation
If batch workloads are stuck pending due to deadlock or zone collocation needs:
1.  **Check PodGroup Status**:
    ```bash
    kubectl get podgroups.scheduling.k8s.io -A
    ```
2.  **Verify Feature Gates**:
    Ensure `--feature-gates=GenericWorkload=true,NodeDeclaredFeatures=true` is enabled on the control plane components if TAS or PodGroups are in use.

#### 7. Workload Autoscaling & User Namespace Troubleshooting
If asked to deploy or debug HPAs, VPAs, or User Namespaces:
1.  **HPA Imperative Generation**:
    ```bash
    kubectl autoscale deployment web-deploy --cpu-percent=80 --min=2 --max=10
    ```
2.  **Verify HPA Metrics**:
    ```bash
    kubectl get hpa
    ```
    *Look for*: `TARGETS` showing the current usage vs the target usage (e.g. `12%/80%`). If it shows `<unknown>/80%`, the **Metrics Server** is missing, not running, or Pods lack CPU resource requests under `spec.containers[].resources.requests`.
3.  **User Namespace Activation**:
    To enable User Namespace isolation:
    ```yaml
    spec:
      hostUsers: false
      containers:
      - name: secure-app
        image: nginx
    ```
    *Diagnostic Check*: Verify uid mapping inside the container:
    ```bash
    kubectl exec -it <pod-name> -- cat /proc/self/uid_map
    ```
    *Look for*: A mapping starting with non-zero IDs on the host side (e.g. `0 100000 65536`).

```
