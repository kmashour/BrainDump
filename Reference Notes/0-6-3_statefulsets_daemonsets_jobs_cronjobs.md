---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - kubernetes/workloads
  - kubernetes/statefulset
---

# Module 0-6-3: StatefulSets, DaemonSets, Jobs & CronJobs

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Reference MOC]] > **Module 0-6-3**

---

## 10. StatefulSets: Stable Application Identities

StatefulSets (`apps/v1`) are used to manage stateful workloads that require stable network identifiers, dedicated persistent storage, and ordered deployment/scaling.

### 10.1 Key Characteristics
1.  **Stable Network Identity:** StatefulSet Pods have a sticky identity. This requires a **Headless Service** (a service with `clusterIP: None`). The DNS A-record resolved for each Pod follows the pattern:
    $$\text{Pod-DNS-Name} = \text{StatefulSet-Name}-\text{Ordinal}.\text{Service-Name}.\text{Namespace}.svc.cluster.local$$
2.  **Stable Storage Mapping:** StatefulSets use a `volumeClaimTemplates` array. Instead of sharing a single Volume, the controller creates a unique PersistentVolumeClaim (PVC) for *each* Pod ordinal. When Pod `db-0` restarts or is rescheduled to a different node, it automatically re-attaches to the PVC `data-db-0`.
3.  **Ordinal Indexing:** Pods are assigned integer ordinals from $0$ to $N-1$.

### 10.2 Deployment & Scaling Rules
*   **Ordered Startup:** Pods are started sequentially from $0$ to $N-1$. Pod $K$ will not start until Pod $K-1$ is fully `Running` and `Ready`.
*   **Ordered Teardown:** During scale-down, Pods are terminated in reverse order ($N-1$ down to $0$).
*   **`podManagementPolicy` Options:**
    *   `OrderedReady`: (Default) Strictly enforces ordered startup and teardown.
    *   `Parallel`: Starts and terminates all Pods concurrently, skipping the ordinal sequencing (useful for fast scaling).

### 10.3 E2E StatefulSet with Headless Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: database-headless-svc
  labels:
    app: db-cluster
spec:
  ports:
  - port: 3306
    name: mysql
  clusterIP: None  # Enforces Headless Service for DNS routing
  selector:
    app: db-cluster
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: db-node
spec:
  serviceName: "database-headless-svc"
  replicas: 3
  podManagementPolicy: OrderedReady
  selector:
    matchLabels:
      app: db-cluster
  template:
    metadata:
      labels:
        app: db-cluster
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: "SuperSecretPassword"
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: data-store
          mountPath: /var/lib/mysql
  # Unique volume claim per pod template
  volumeClaimTemplates:
  - metadata:
      name: data-store
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 10Gi

---

### 10.4 StatefulSet DNS Mapping & CoreDNS Resolution

CoreDNS resolves stable network identities for StatefulSet pods through a headless service (`clusterIP: None`). Instead of providing a single load-balanced virtual ClusterIP, the headless service acts as a grouping mechanism. The Kubernetes API Controller manages DNS entries pointing directly to individual Pod IPs.

#### 10.4.1 DNS Record Types Generated
*   **Stateful Pod A-Record (Individual IP Mapping):**
    Each ordinal pod in the StatefulSet is assigned a DNS A-record (or AAAA-record for IPv6) pointing directly to its Pod IP:
    $$\text{Format: } \langle\text{pod-name}\rangle.\langle\text{service-name}\rangle.\langle\text{namespace}\rangle.\text{svc.cluster.local}$$
    *Example:* `db-node-0.database-headless-svc.default.svc.cluster.local` resolves directly to the private IP of the first ordinal pod.
*   **Headless Service A-Record (Cluster-wide Discovery):**
    Querying the headless service itself returns the list of all active, ready Pod IPs matching the service's selector.
    $$\text{Format: } \langle\text{service-name}\rangle.\langle\text{namespace}\rangle.\text{svc.cluster.local}$$
*   **SRV Record (Port and Membership Discovery):**
    CoreDNS generates SRV (Service) records to allow discovering port configurations and matching hostnames:
    $$\text{Format: } \_\langle\text{port-name}\rangle.\_\langle\text{protocol}\rangle.\langle\text{service-name}\rangle.\langle\text{namespace}\rangle.\text{svc.cluster.local}$$
    *Example:* `_mysql._tcp.database-headless-svc.default.svc.cluster.local` returns the port `3306` and the hostname targets (`db-node-0...`, `db-node-1...`, etc.).

---

### 10.5 Step-by-Step DNS Troubleshooting Run Sheet

If application containers fail to resolve StatefulSet peer identities, use this run sheet to diagnose CoreDNS and headless service routing.

#### Step 1: Deploy a Temporary Diagnostic Pod
Launch a network diagnostics pod (like `nicolaka/netshoot` or `dnsutils`) running in the same namespace as your StatefulSet:
```bash
kubectl run dns-diagnostics --rm -it --image=nicolaka/netshoot --restart=Never -- /bin/bash
```

#### Step 2: Inspect Container DNS Search Paths
Verify that the container's DNS resolver matches the Kubernetes internal cluster settings:
```bash
cat /etc/resolv.conf
```
*Expected Output:*
```text
nameserver 10.96.0.10
search default.svc.cluster.local svc.cluster.local cluster.local
options ndots:5
```
*Troubleshooting:* Ensure the `nameserver` points to the ClusterIP of your `kube-dns` / `coredns` service.

#### Step 3: Audit A-Records for the Headless Service
Perform a lookup on the headless service to verify that CoreDNS returns the IP addresses of all ready Pods:
```bash
nslookup database-headless-svc
```
Or using `host`:
```bash
host database-headless-svc
```
*Expected Output:*
```text
database-headless-svc.default.svc.cluster.local has address 10.244.0.15
database-headless-svc.default.svc.cluster.local has address 10.244.0.16
database-headless-svc.default.svc.cluster.local has address 10.244.0.17
```
*Troubleshooting:* If no IPs are returned, verify that the StatefulSet pods have passed their readiness probes (`kubectl get pods -l app=db-cluster`). A pod in a non-ready state is automatically removed from the headless service endpoints.

#### Step 4: Resolve Individual Ordinal Pod A-Records
Verify that each individual pod ordinal resolves to its specific IP address:
```bash
nslookup db-node-0.database-headless-svc
```
Or using `dig`:
```bash
dig +short db-node-0.database-headless-svc.default.svc.cluster.local
```
*Expected Output:*
```text
10.244.0.15
```

#### Step 5: Query SRV Records for Port and Membership Discovery
Verify that CoreDNS is publishing the SRV record detailing the ports and ordinal member hostnames:
```bash
dig SRV _mysql._tcp.database-headless-svc.default.svc.cluster.local
```
*Expected Output:*
```text
;; ANSWER SECTION:
_mysql._tcp.database-headless-svc.default.svc.cluster.local. 30 IN SRV 10 33 3306 db-node-0.database-headless-svc.default.svc.cluster.local.
_mysql._tcp.database-headless-svc.default.svc.cluster.local. 30 IN SRV 10 33 3306 db-node-1.database-headless-svc.default.svc.cluster.local.
_mysql._tcp.database-headless-svc.default.svc.cluster.local. 30 IN SRV 10 33 3306 db-node-2.database-headless-svc.default.svc.cluster.local.
```
*Troubleshooting:* If the SRV records are missing, verify that the StatefulSet YAML `spec.serviceName` matches the headless `v1.Service` `metadata.name` exactly, and that the Service `spec.ports[*].name` matches the StatefulSet container `ports[*].name` exactly.

#### 10.5.1 StatefulSet Lab Walkthrough & Diagnostic logs
Analyze stateful workload deployment, ordinal scaling, and volume persistence testing using these resources:
* **Interactive StatefulSet Lab logs:** [statefulset-lab.html](file:///home/karim/Desktop/BrainDump/Attachments/statefulset-lab.html)

---

## 11. DaemonSets: Node-Level Services

DaemonSets (`apps/v1`) guarantee that a single copy of a specific Pod runs on all (or select) nodes in the cluster.

### 11.1 DaemonSet Use Cases & Scheduling Mechanics
*   **Common Use Cases:**
    *   **Log Aggregation:** Running log collectors (`fluentd`, `logstash`) on every node to stream host and container log files.
    *   **Node Monitoring:** Running performance agents (`prometheus-node-exporter`, `datadog-agent`) to collect node resource metrics.
    *   **Storage Daemons:** Running distributed storage controllers (`ceph`, `glusterfs`) on nodes to expose host storage to the cluster.
*   **Scheduling Mechanics:** DaemonSets are scheduled by the default Kubernetes Scheduler. By default, the DaemonSet controller automatically injects tolerations into the Pod spec for standard node taints:
    *   `node.kubernetes.io/not-ready`
    *   `node.kubernetes.io/unreachable`
    *   `node.kubernetes.io/disk-pressure`
    *   *Node Selector/Affinity:* You can target a subset of nodes using `spec.template.spec.nodeSelector` or `spec.template.spec.affinity`.

#### 11.1.1 Scheduler Bypass (Direct Node Placement)
In specialized scenarios, you can bypass the default scheduler entirely by assigning explicit `nodeName` fields or strict node selectors. This guarantees that DaemonSet Pods are scheduled directly to targeted nodes, even if the default scheduler is overloaded, failing, or completely unavailable.

### 11.2 E2E DaemonSet Specification
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-log-forwarder
  namespace: kube-system
  labels:
    app: log-collector
spec:
  selector:
    matchLabels:
      app: log-collector
  template:
    metadata:
      labels:
        app: log-collector
    spec:
      # Tolerates scheduling restrictions on Master/Control-Plane nodes
      tolerations:
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule
      containers:
      - name: fluentd-agent
        image: fluentd:1.16-debian
        resources:
          limits:
            memory: "200Mi"
            cpu: "100m"
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
```

#### 11.2.1 DaemonSet Lab Walkthrough & Diagnostic logs
Analyze DaemonSet scheduling across nodes and log outputs using this resource:
* **Interactive DaemonSet Lab logs:** [daemonsets.html](file:///home/karim/Desktop/BrainDump/Attachments/daemonsets.html)

---

## 12. Batch Processing: Jobs & CronJobs

### 12.1 Batch Workloads vs. Services
* **Services (Deployments, StatefulSets):** Run continuously and are designed to stay online indefinitely.
* **Jobs:** Run to completion. The Job controller spins up one or more Pods, tracks execution, and marks the task complete when the desired completions are reached.

### 12.2 Jobs (`batch/v1`)
A Job creates one or more Pods and ensures that a specified number of them successfully terminate.
*   **Required `restartPolicy`:** Must be set to `OnFailure` or `Never` (never `Always`, as the container is designed to exit).
*   **Key Controls:**
    *   `completions`: The total number of successful Pod executions required to mark the Job complete.
    *   `parallelism`: The maximum number of Pods that can run concurrently at any given point.
    *   `backoffLimit`: The maximum number of retries before marking the Job as failed (Default is 6).
    *   `activeDeadlineSeconds`: A strict real-time timeout cap for the Job. If exceeded, all active Pods are terminated and the Job is marked failed, regardless of the completion status.
    *   `ttlSecondsAfterFinished`: Automatically cleans up finished Jobs (Complete or Failed) and their child pods cascadingly after the specified duration (in seconds), avoiding resource garbage accumulation in etcd. Note that this is sensitive to time skew in the cluster.

#### 12.2.1 The Work Queue Design Pattern
Jobs are frequently used to process messages from a queue:
1. **Producer:** An application publishes tasks/messages to a queueing broker (e.g. RabbitMQ, Apache Kafka, or AWS SQS).
2. **Consumer:** The Job controller spins up consumer Pods (controlled by `parallelism`).
3. **Execution:** Each Pod pulls messages from the queue, processes them, and terminates once the queue is empty. Pod coordination and message retrieval logic are managed by the application code.

### 12.3 CronJobs (`batch/v1`)
A CronJob runs a Job on a repeating schedule using standard cron format:
$$\text{Schedule: } \text{Minute } \text{Hour } \text{Day-of-Month } \text{Month } \text{Day-of-Week}$$
*   **`concurrencyPolicy` Decisions:**
    *   `Allow` (Default): Permits multiple Job runs to execute simultaneously.
    *   `Forbid`: If a previous Job execution is still running, the CronJob controller skips the current scheduled run.
    *   `Replace`: If a prior Job is active, the CronJob controller terminates it immediately and starts a new Job.
*   **Job History Retention:**
    *   `successfulJobsHistoryLimit`: The number of successful completed jobs to retain in the API server (Default: 3).
    *   `failedJobsHistoryLimit`: The number of failed jobs to retain (Default: 1).
*   **`startingDeadlineSeconds`:** The deadline (in seconds) for starting the Job if it misses its scheduled run time (e.g., due to cluster resource depletion or API Server downtime).
*   **DNS & Naming Constraints (52-Character Limit):** CronJob names must not exceed **52 characters**. Because the CronJob controller appends an 11-character timestamp suffix to the Job name, and Job names have a strict maximum limit of **63 characters**, setting a CronJob name longer than 52 characters will violate validation constraints.

### 12.3 E2E CronJob Specification
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: database-backup-cronjob
  namespace: default
spec:
  schedule: "0 2 * * *"  # Runs daily at 2:00 AM
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 5
  failedJobsHistoryLimit: 2
  startingDeadlineSeconds: 200
  jobTemplate:
    spec:
      activeDeadlineSeconds: 1800  # Hard timeout of 30 minutes
      backoffLimit: 4
      template:
        metadata:
          labels:
            job: db-backup
        spec:
          restartPolicy: OnFailure
          containers:
          - name: backup-tool
            image: postgres:15-alpine
            command: ["/bin/sh", "-c", "pg_dump -h db-host -U admin prod_db > /backup/prod.sql"]
            volumeMounts:
            - name: backup-volume
              mountPath: /backup
          volumes:
          - name: backup-volume
            persistentVolumeClaim:
              claimName: backup-pvc

#### 12.3.2 Jobs & CronJobs Lab Walkthrough & Diagnostic logs
Verify execution tracking, completion parameters, and cron scheduling using this resource:
* **Interactive Job & CronJob Lab logs:** [jobs.html](file:///home/karim/Desktop/BrainDump/Attachments/jobs.html)
```
### 12.4 User Namespaces in Pods (v1.36+ Stable)
A Linux user namespace isolates the user running inside the container from the one on the host, preventing host-compromise security breaches.
*   **Opt-In Mechanism:** Set `spec.hostUsers: false` inside the Pod specification.
*   **Dynamic Mapping:** The kubelet dynamically maps the container's UIDs/GIDs (defaulting to the standard `0-65535` range) to unprivileged, unique UIDs/GIDs on the host, ensuring no two Pods share mapping ranges.
*   **Volume Compatibility:** The `runAsUser`, `runAsGroup`, and `fsGroup` fields still refer to IDs inside the container. Kubelet utilizes **idmap mounts** on the host filesystem (requires Linux kernel 6.3+ and support on the volume storage backends, e.g., tmpfs, ext4, xfs) to transparently map container UIDs/GIDs to host UIDs/GIDs during reads/writes.
*   **Requirements:** Runtime support is required at both the OCI level (crun 1.9+, runc 1.2+) and the CRI container runtime level (containerd 2.0+, CRI-O 1.25+).

### 12.5 Workload Autoscaling (HPA & VPA)
Kubernetes automates workload capacity tuning horizontally (scaling replica counts) or vertically (modifying resource allocations).

#### 1. Horizontal Pod Autoscaler (HPA)
HPA increases or decreases replica counts of a Deployment or StatefulSet dynamically based on resource utilization or custom metrics:
*   **Controller Loop:** Runs inside `kube-controller-manager` at intervals controlled by `--horizontal-pod-autoscaler-sync-period` (default: 15s).
*   **Metrics Source:** Queries the `metrics.k8s.io` API (usually supplied by the **Metrics Server** addon) or custom/external metrics APIs.
*   **Scaling Formula:**
    $$\text{desiredReplicas} = \left\lceil \text{currentReplicas} \times \frac{\text{currentMetricValue}}{\text{desiredMetricValue}} \right\rceil$$
*   **Tolerance:** Scaling actions are ignored if the metric ratio is within a configurable tolerance (default: `0.1`, which translates to ratios between `0.9` and `1.1`).
*   **YAML Spec:**
    ```yaml
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: web-hpa
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: web-deploy
      minReplicas: 2
      maxReplicas: 10
      metrics:
      - type: Resource
        resource:
          name: cpu
          target:
            type: Utilization
            averageUtilization: 80
    ```

#### 2. Vertical Pod Autoscaler (VPA)
VPA dynamically adjusts container CPU and memory requests and limits to rightsize resource consumption. It is installed as a Custom Resource Definition (CRD) from the `autoscaling.k8s.io/v1` API group.
*   **Three Cooperating Components:**
    1.  **Recommender:** Analyzes historical CPU/memory consumption and OOM events via the Metrics Server and writes recommendations (`Target`, `LowerBound`, `UpperBound`) to the VPA's `.status.recommendation`.
    2.  **Updater:** Monitors active Pods and evicts them (respecting PDBs) when their resource specs diverge significantly from recommendations.
    3.  **Admission Webhook:** Intercepts Pod creation requests and automatically injects the `Target` resource recommendation requests before the Pod is scheduled.
*   **Update Modes (`spec.updatePolicy.updateMode`):**
    *   `Off`: Only generates recommendations; does not alter Pods. Useful for monitoring resource requirements before enforcing limits.
    *   `Initial`: Recommends and applies resources only at Pod creation time.
    *   `Recreate`: Recommends resources and allows the Updater to evict active Pods to apply changes.
    *   `Auto`: Updates existing pods to recommended values. Currently, this performs exactly like `Recreate` (evicting and recreating). In the future, once in-place resizing is fully stable, `Auto` mode will resize containers dynamically without restarting.
*   **VPA YAML Spec Example:**
    ```yaml
    apiVersion: autoscaling.k8s.io/v1
    kind: VerticalPodAutoscaler
    metadata:
      name: web-vpa
      namespace: default
    spec:
      targetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: web-deploy
      updatePolicy:
        updateMode: Auto
      resourcePolicy:
        containerPolicies:
          - containerName: '*'
            minAllowed:
              cpu: 100m
              memory: 128Mi
            maxAllowed:
              cpu: 2
              memory: 2Gi
            controlledResources: ["cpu", "memory"]
    ```

#### 3. Horizontal vs. Vertical Autoscaling Comparison

| Feature / Metric | Horizontal Pod Autoscaler (HPA) | Vertical Pod Autoscaler (VPA) |
| :--- | :--- | :--- |
| **Scaling Method** | Scales replica count (adds or removes Pods horizontally). | Scales compute boundaries (CPU/Memory requests & limits vertically). |
| **Component Type** | Built-in controller in `kube-controller-manager`. | Custom CRD controllers (Recommender, Updater, Webhook). |
| **Pod Runtime Behavior**| Non-disruptive. Keeps existing Pods active; spins up new Pods. | Disruptive. Evicts and restarts Pods to apply values (until in-place is stable). |
| **Traffic Spike Suitability**| Excellent. Quickly scales out to handle sudden traffic peaks. | Poor. Delays caused by Pod evictions/recreation loops. |
| **Best Workloads** | Stateless services, web servers, API gateways, message queues. | Stateful/heavy workloads (Databases, JVM apps, JVM memory spikes). |
| **Cost Optimization** | Scales down replica count to save compute nodes during idle periods. | Prevents resource over-provisioning by rightsizing Pod requests. |

#### 4. In-Place Pod Vertical Scaling (Manual In-Place Resizing)
By default, altering resource requests or limits in a Pod's specification (e.g. inside a Deployment template) requires the API server to recreate the Pod. To allow dynamic resource scaling without Pod termination, Kubernetes provides the **In-Place Pod Vertical Scaling** mechanism.
*   **Feature Status & Levels:**
    *   **Container-level Resizing** (`spec.containers[*].resources`): **Stable (GA) in v1.35+** (enabled by default).
    *   **Pod-level Resizing** (`spec.resources`): **Beta in v1.36+** (enabled by default), allowing aggregate limits for the entire Pod sandbox in-place.
*   **Resize Policy Spec (`resizePolicy`):** For container-level resize, you can define how the container runtime reacts to CPU and memory scaling actions individually:
    *   `RestartNotRequired` (Default for CPU): The container runtime dynamically adjusts CPU cgroups shares on the fly without stopping the container.
    *   `Restart` (Often used for memory): The container runtime restarts the target container to apply the new memory parameters.
    *   **YAML Spec Example:**
        ```yaml
        apiVersion: v1
        kind: Pod
        metadata:
          name: in-place-pod
        spec:
          containers:
          - name: app
            image: nginx
            resources:
              limits:
                cpu: "1"
                memory: "512Mi"
              requests:
                cpu: "500m"
                memory: "256Mi"
            resizePolicy:
            - resourceName: cpu
              restartPolicy: RestartNotRequired
            - resourceName: memory
              restartPolicy: RestartNotRequired
        ```
*   **Manual Resize Patch Command:**
    Once enabled, modify container resource requests or limits imperatively:
    ```bash
    kubectl patch pod in-place-pod --patch '{"spec":{"containers":[{"name":"app","resources":{"requests":{"cpu":"1"}}}]}}'
    ```
*   **Critical Resizing Limitations:**
    *   **Resource Scope:** Resizing is restricted strictly to CPU and memory.
    *   **QoS Class Immutability:** Changing requests/limits cannot switch the Pod's QoS Class (e.g., from `Guaranteed` to `Burstable`).
    *   **Container Limitations:** Init containers and ephemeral containers are completely exempt and cannot be resized.
    *   **Initial Setup Constraints:** If requests or limits were not declared at Pod creation time, they cannot be added dynamically.
    *   **Memory Floor Constraints:** You cannot reduce a container's memory limit below its active physical usage. Doing so places the Pod in a `Proposed` state, and the resize status remains `InProgress` until memory usage drops or the limit is raised.
    *   **OS Support:** Windows pods are not supported; in-place scaling is restricted to Linux container environments.

*See complete playbooks and deployment manifests in [[Project - Vertical Pod Autoscaler|Project - Vertical Pod Autoscaler.md]].*

---
