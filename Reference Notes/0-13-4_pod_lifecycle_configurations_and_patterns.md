---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - kubernetes/lifecycle
---

# Module 0-13-4: Application Lifecycle, Multi-Container Patterns & Configs

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Reference MOC]] > **Module 0-13-4**

---

## 3. Application Lifecycle Management

Managing the lifecycle of applications involves configuring how they boot, pass configurations, and handle secrets.

### A. Commands and Arguments
When defining a Pod, you can specify a container command and arguments. This configuration interacts directly with the `ENTRYPOINT` and `CMD` instructions defined in the Dockerfile of the container image.

#### 1. Docker vs. Kubernetes Direct Map

| Dockerfile Instruction | Kubernetes YAML Field | Purpose |
| :--- | :--- | :--- |
| **`ENTRYPOINT`** | **`command`** | The main executable process to run when the container starts. |
| **`CMD`** | **`args`** | Default arguments passed to the executable process. |

#### 2. Overriding Rules

| Manifest Configured | Resulting Behavior |
| :--- | :--- |
| **Neither `command` nor `args` defined** | The container runs the `ENTRYPOINT` and `CMD` defined in the Dockerfile. |
| **Only `command` defined** | The image's `ENTRYPOINT` and `CMD` are **completely overridden**. The container runs the new `command` without arguments (unless defined in the executable path). |
| **Only `args` defined** | The image's `CMD` is overridden. The new `args` are passed to the image's `ENTRYPOINT`. |
| **Both `command` and `args` defined** | Both the image's `ENTRYPOINT` and `CMD` are overridden. The container runs the new `command` with the new `args`. |

#### 3. Syntax Formats
* **Shell Format vs Exec Format in Dockerfile:**
  * Shell format: `ENTRYPOINT sleep 10` (runs as `/bin/sh -c "sleep 10"`, PID 1 is the shell itself, not the sleep process).
  * Exec format: `ENTRYPOINT ["sleep", "10"]` (runs directly, sleep is PID 1, allows proper signal propagation like SIGTERM).
* **Kubernetes Manifest formats:**
  * Standard YAML list:
    ```yaml
    command:
    - "/bin/sh"
    - "-c"
    - "sleep 10"
    ```
  * Inline JSON list:
    ```yaml
    command: ["/bin/sh", "-c", "sleep 10"]
    ```

---

### B. Environment Variables
Kubernetes allows injecting environment variables into containers.

#### 1. Direct Configuration
Define values inline:
```yaml
spec:
  containers:
  - name: my-app
    image: alpine
    env:
    - name: DB_PORT
      value: "3306"
```

#### 2. Bulk Injection (`envFrom`)
Inject all key-value pairs from a ConfigMap or Secret in bulk. The keys automatically become the environment variable names.
```yaml
envFrom:
- configMapRef:
    name: app-config
- secretRef:
    name: app-secret
```

#### 3. Targeted Reference (`valueFrom`)
Inject specific values from external resources or cluster metadata.
* **ConfigMap Key Reference:**
  ```yaml
  env:
  - name: APP_COLOR
    valueFrom:
      configMapKeyRef:
        name: app-config
        key: theme-color
  ```
* **Secret Key Reference:**
  ```yaml
  env:
  - name: DB_PASS
    valueFrom:
      secretKeyRef:
        name: db-credentials
        key: password
  ```
* **Downward API Field Reference (Metadata):**
  Inject Pod names, IPs, namespaces, or node names into the container.
  ```yaml
  env:
  - name: MY_POD_NAME
    valueFrom:
      fieldRef:
        fieldPath: metadata.name
  - name: MY_POD_IP
    valueFrom:
      fieldRef:
        fieldPath: status.podIP
  ```
* **Container Resource Reference:**
  Inject resource request/limit constraints.
  ```yaml
  env:
  - name: CPU_LIMIT
    valueFrom:
      resourceFieldRef:
        containerName: app-container
        resource: limits.cpu
  ```

---

### C. ConfigMaps
ConfigMaps store non-confidential configuration data in key-value pairs.

#### 1. Creation Methods
* **Imperative Creation:**
  * From Literals:
    ```bash
    kubectl create configmap app-config --from-literal=COLOR=blue --from-literal=MODE=prod
    ```
  * From a File (the filename becomes the key, the file content becomes the value):
    ```bash
    kubectl create configmap app-config --from-file=app.properties
    ```
  * From a Directory of Files:
    ```bash
    kubectl create configmap app-config --from-file=config-dir/
    ```
  * From an Environment File:
    ```bash
    kubectl create configmap app-config --from-env-file=.env
    ```
* **Declarative Creation:**
  ```yaml
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: app-config
  data:
    COLOR: blue
    MODE: prod
  ```

#### 2. Injection: Environment Variables vs. Volume Mounts
ConfigMaps can be injected into Pods as environment variables (via `envFrom` / `valueFrom`) or mounted as a volume.

##### Mounting ConfigMap as a Volume:
Every key in the ConfigMap data represents a file name, and the value is the file content.
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-volume-pod
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: config-vol
      mountPath: /etc/config
  volumes:
  - name: config-vol
    configMap:
      name: app-config
```
Inside the container, `/etc/config/COLOR` contains the text `blue`, and `/etc/config/MODE` contains the text `prod`.

#### 3. Update Behavior and Sync Mechanisms
What happens when a ConfigMap is modified in the cluster while a Pod is running?

* **Environment Variables Injection:**
  * Environment variables are **static**.
  * When the ConfigMap is updated, the environment variables inside the running container **do not change**.
  * The Pod must be deleted and recreated (e.g. via rolling update of its deployment) to pick up the changes.
* **ConfigMap Volume Mounts:**
  * Volume mounts are **dynamic**.
  * When the ConfigMap is updated, the Kubelet periodically syncs the volume files to reflect the new ConfigMap contents. The sync time depends on the Kubelet sync interval + the cache TTL (defaulting to 1-2 minutes).

##### The Kubelet Atomic Directory Update Mechanism
To ensure that containerized applications do not read half-written or corrupted configuration files during a sync, Kubelet updates the mounted files **atomically** using a symlink swap mechanism. 

When a ConfigMap is mounted into a Pod, Kubelet organizes the files inside the mount directory (`/etc/config` in our example) using multiple layers of symlinks:
1. **Timestamped Directories:** Kubelet creates a new subdirectory with a timestamp (e.g., `..2026_06_05_10_00_00_123456789/`) and writes the actual data files there.
2. **The `..data` Symlink:** Kubelet creates a symlink named `..data` that points to the active timestamped directory.
3. **User-Facing Symlinks:** Every key file in the mount directory (e.g., `COLOR`, `MODE`) is created as a symlink pointing to the key inside the `..data` symlink (e.g., `COLOR` -> `..data/COLOR`).

###### Directory Tree Layout:
```
/etc/config
├── ..2026_06_05_10_00_00_123456789/   <-- Original data directory
│   ├── COLOR ("red")
│   └── MODE ("dev")
├── ..data -> ..2026_06_05_10_00_00_123456789/   <-- Symlink to current data
├── COLOR -> ..data/COLOR
└── MODE -> ..data/MODE
```

###### The Sync Swap Event:
When the ConfigMap is updated (e.g., `COLOR` changes to `blue`):
1. Kubelet creates a new timestamped directory: `..2026_06_05_10_05_00_987654321/` and writes the new file contents there.
2. Kubelet atomically updates the `..data` symlink to point to the new directory:
   `..data -> ..2026_06_05_10_05_00_987654321/`
3. The old timestamped directory `..2026_06_05_10_00_00_123456789/` is garbage collected and deleted.
4. Because the user-facing files point to `..data/COLOR`, they resolve to the new file instantly and atomically.

##### Systems Rationale: Why Kubernetes Uses This Symlink-Swap Pattern
Rather than overwriting files directly in place (e.g., executing `write()` or redirecting stdout into the target config file), Kubernetes employs this complex symlink system to solve four core Linux systems engineering requirements:

1. **Atomicity (Preventing Partial Reads):**
   * *The Problem:* File writes are not instantaneous. If the Kubelet overwrote files directly, there would be a window of time where a file is empty or half-written. If the application configuration reloader triggered a read in this microsecond window, it would ingest corrupted data and crash.
   * *The Solution:* In Unix/Linux, updating a symlink (`ln -sfn`) is an **atomic operation at the kernel level**. The pointer swaps in a single CPU instruction, ensuring that applications either read the complete old config or the complete new config—with zero risk of dirty/corrupted reads.

2. **Multi-File Consistency:**
   * *The Problem:* Large applications often consume multiple dependent configuration files (e.g., `db.conf`, `credentials.json`, `ports.yaml`). If Kubelet updated them sequentially, an application might reload a partial configuration state (new host, but old ports), breaking connections.
   * *The Solution:* By preparing all updated configuration files inside the new timestamped folder, and then performing a single swap of the `..data` symlink, **all configurations are updated simultaneously** from the application's perspective.

3. **Bypassing Inode Locks and Active File Descriptors:**
   * *The Problem:* When an application opens and reads a configuration file, the Linux kernel assigns an **Open File Descriptor (FD)** and holds a lock on it in memory. If Kubelet tried to overwrite or delete that exact locked inode, the host write operation would block or fail.
   * *The Solution:* Kubelet writes the new configuration to a fresh location with a new inode (inside the new timestamped directory). The active application can safely maintain its existing open file descriptor to the old inode without blocking Kubelet. The old folder is only deleted (garbage collected) by the OS kernel once all open file descriptors to it are closed.

4. **Preserving Read-Only Mount Boundaries:**
   * *The Problem:* Kubernetes projects ConfigMap and Secret volumes as **Read-Only (`ro`)** mounts inside the container's mount namespace to prevent containers from modifying their configurations. This read-only flag blocks direct write operations to the files within the container.
   * *The Solution:* The directory `/etc/config` itself remains a read-only mount. By leaving the user-facing file entries as symlinks and having Kubelet modify the directory structures on the host layer (where Kubelet has full write permissions), the kernel handles the path resolution seamlessly without requiring write permissions inside the container's mount namespace.

##### inotify Sync Mechanics inside Containers
The Linux kernel's `inotify` subsystem provides APIs for monitoring file system events. 
* **Watching Individual Files:** If an application sets an `inotify` watch on the mounted key file itself (e.g., `/etc/config/COLOR`), it **will not receive any events** when the ConfigMap is updated. This is because `/etc/config/COLOR` is a static symlink whose inode and content never change; only its target resolves differently once `..data` changes.
* **Watching the Parent Directory:** To detect ConfigMap changes, application configuration reloaders must watch the **parent directory** (`/etc/config`) or the `..data` symlink itself. When the atomic swap occurs, the directory's directory-entry changes, triggering `IN_MODIFY` or `IN_DELETE`/`IN_CREATE` on `..data`. The reloader catches this directory event and triggers a config refresh.

> [!WARNING]
> **The `subPath` Inode Binding Gotcha:**
> If you mount a ConfigMap key using `volumeMounts.subPath` to mount a single file (e.g., mounting `COLOR` to `/app/settings.conf`), **dynamic updates are disabled**.
> 
> * **Why this happens:** When container engines (Docker/CRI-O) mount a file via `subPath`, they perform a bind-mount directly targeting the resolved file's inode at container start time (which is the inode of `..2026_06_05_10_00_00_123456789/COLOR`).
> * **The Result:** When Kubelet updates the ConfigMap, it swaps the `..data` symlink to point to the new directory. However, the container's mount table remains hard-bound to the old inode inside the deleted/old directory. The file inside the container will never receive updates. To pick up the new configuration, the Pod must be restarted.

---

### D. Secrets

Secrets are API objects used to store sensitive data (such as passwords, tokens, or keys) to decouple credentials from container images. From an application configuration perspective, they are consumed similarly to ConfigMaps (injected as environment variables or mounted as volumes), but they require values to be Base64-encoded.

> [!IMPORTANT]
> **Security Hardening & Cryptography Notice:**
> While this section covers how applications *consume* Secrets, all security aspects—including:
> * **Base64 vs. Cryptographic Encryption** (and why Base64 provides zero security)
> * **Linux `tmpfs` Volatile Memory Mechanics** (preventing writes to physical disk)
> * **Modern TokenRequest API & ServiceAccount Token Projection** (auto-rotating, short-lived tokens)
> * **Signer Container Partitioning** (privileged/non-privileged container isolation)
> * **ETCD Encryption at Rest configuration and KMS Envelope Encryption**
> 
> Are documented in detail in [[Reference Notes/0-7-1_rbac_service_accounts_and_certificates#11-configmap--secret-security-management|Module 0-7: Section 11 (ConfigMap & Secret Security Management)]].


#### 1. Consumption Methods (Env vs. Volume Mounts)
Like ConfigMaps, Secrets can be injected into container runtimes in two primary ways:

##### A. Environment Variables
Injecting Secret keys as environment variables exposes them directly to the containerized process.
* **Manifest Example:**
  ```yaml
  spec:
    containers:
    - name: app
      image: my-app
      env:
      - name: DB_PASSWORD
        valueFrom:
          secretKeyRef:
            name: db-credentials
            key: password
  ```
* **Caveat:** Environment variables are static. If the Secret value is updated in the API server, the environment variables inside the running container will **not** update until the container is restarted.

##### B. Volume Mounts
Mounting a Secret as a volume writes each key in the Secret as a file containing the decoded plaintext value.
* **Manifest Example:**
  ```yaml
  spec:
    containers:
    - name: app
      image: nginx
      volumeMounts:
      - name: secret-vol
        mountPath: /etc/secrets
        readOnly: true
    volumes:
    - name: secret-vol
      secret:
        secretName: db-credentials
  ```
* **Dynamic Updates:** Kubelet periodically syncs updates. Modifications to the Secret in the API server will automatically propagate as file updates inside the container (typically within 1-2 minutes).
* **Subpath Exception:** Containers using a Secret with `volumeMounts.subPath` will **not** receive dynamic updates.

#### 2. Declarative Definition (Base64 Encoding)
Secret manifests require values in the `data` section to be Base64-encoded:
* **Example Manifest:**
  ```yaml
  apiVersion: v1
  kind: Secret
  metadata:
    name: db-credentials
  type: Opaque
  data:
    username: dXNlcg==     # base64 for "user"
    password: YWRtaW4xMjM= # base64 for "admin123"
  ```
* **Plaintext Input (`stringData`):** You can write keys in plaintext using the write-only `stringData` field; the API server automatically encodes them when writing to storage:
  ```yaml
  apiVersion: v1
  kind: Secret
  metadata:
    name: db-credentials
  type: Opaque
  stringData:
    username: user
    password: admin123
  ```

#### 3. Immutable Secrets
To prevent accidental updates and reduce load on the API server in large-scale deployments, mark Secrets as immutable:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: static-secret
immutable: true
data:
  api-key: dGVzdC1rZXkK
```
* **Note:** Once marked immutable, the `data` cannot be updated. You must delete and recreate the Secret to change its contents.

---

### E. Multi-Container Pod Design Patterns
To decouple concerns, helper processes can run in separate containers within the same Pod, sharing the same lifecycle, network namespace (`localhost`), and storage volumes.

#### 1. Sidecar Pattern
Enhances or extends the main application container without altering its core logic.
* **Use Case:** A log shipper (e.g. Filebeat or Fluent Bit) that tails log files written by the main application to a shared `emptyDir` volume and streams them to a central indexing backend, or an Envoy proxy running as a service mesh helper.

#### 2. Adapter Pattern
Normalizes or modifies application output/telemetry before exporting it to external systems.
* **Use Case:** A container that polls the main application's custom metrics endpoint, formats them into standard Prometheus metrics, and exposes them on port `9100`.

#### 3. Ambassador Pattern
Acts as a local proxy for outgoing connections, hiding the complexity of external networking or service discovery from the main application.
* **Use Case:** The main application connects to database services on `localhost:3306`, while the ambassador container handles routing, SSL termination, and authentication to the remote database cluster.

```
┌───────────────────────────────── Pod ─────────────────────────────────┐
│                                                                       │
│  ┌───────────────────┐    localhost     ┌──────────────────────────┐  │
│  │  Main Container   │ ◄──────────────► │    Helper Container      │  │
│  │  (App Process)    │   (TCP/Ports)    │   (Sidecar/Ambassador)   │  │
│  └─────────┬─────────┘                  └────────────┬─────────────┘  │
│            │                                         │                │
│            ▼                                         ▼                │
│       ┌────────────────────────────────────────────────────────┐      │
│       │               Shared emptyDir Volume                   │      │
│       └────────────────────────────────────────────────────────┘      │
└───────────────────────────────────────────────────────────────────────┘
```

---

### F. Init Containers
Init containers run initialization tasks sequentially to completion before any application containers start.

#### 1. Lifecycle Mechanics
* **Sequential Execution:** Defined in `spec.initContainers` as a list. They are executed one-by-one. Each must exit with code `0` before the next starts.
* **Failure Behavior:** If an init container fails (non-zero exit code), the Kubelet restarts the Pod (according to `spec.restartPolicy`). If the policy is `Never`, the Pod status transitions to `Failed`.
* **Application Delay:** Application containers do not start until all init containers have run to completion successfully.

#### 2. Native Sidecars (restartPolicy: Always)
Introduced to support sidecars (like log shippers or service mesh proxies) that must start before the main app but continue running for the entire Pod lifecycle.
* **Definition:** Defined in `spec.initContainers` but set with `restartPolicy: Always`.
* **Execution:** Kubelet starts the native sidecar, waits for its startup/readiness probe to succeed, and then proceeds to execute the next init container or app container. Unlike standard init containers, native sidecars do not exit and are terminated only when the Pod is deleted.

#### 3. Resource Allocation Math
The scheduler computes resource demands for the Pod by comparing sequential app container requirements with init container requirements:
$$\text{Pod Request} = \max\left(\sum\text{App Requests} + \sum\text{Active Sidecar Requests},\,\max(\text{Sequential Init Requests})\right)$$
$$\text{Pod Limit} = \max\left(\sum\text{App Limits} + \sum\text{Active Sidecar Limits},\,\max(\text{Sequential Init Limits})\right)$$

---

### G. Workload Autoscaling (HPA, VPA, and In-Place Resizing)
Kubernetes automates resource capacity adjustments horizontally (by replicas) or vertically (by container size).

#### 1. Horizontal Pod Autoscaler (HPA)
HPA monitors resource utilization (CPU/Memory) and dynamically scales the number of Pod replicas.
* **Prerequisite:** Requires the **Metrics Server** to run in the cluster to expose node/container metrics via `metrics.k8s.io`.
* **Formula:**
  $$\text{desiredReplicas} = \left\lceil \text{currentReplicas} \times \frac{\text{currentMetricValue}}{\text{desiredMetricValue}} \right\rceil$$

#### 2. Vertical Pod Autoscaler (VPA)
VPA monitors actual CPU/Memory usage and recommends or applies optimal container requests and limits.
* **Components:**
  1. **Recommender:** Analyzes metrics and calculates optimal resource boundary recommendations.
  2. **Updater:** Evicts Pods whose current configurations deviate significantly from the recommendations.
  3. **Admission Webhook:** Mutating webhook that overrides resources at Pod startup.
* **Update Modes (`spec.updatePolicy.updateMode`):**
  * `Off`: Generates recommendations only (read-only).
  * `Initial`: Applies target recommendations only at Pod creation.
  * `Recreate`: Evicts active running Pods to apply updated sizes.
  * `Auto`: Automatically sizes containers. Currently behaves like `Recreate` but will support in-place resizing in the future.

#### 3. In-Place Container Resizing (Vertical Scaling)
Traditionally, changing resources requires terminating the Pod and spinning up a new one. In-Place Pod Resizing allows modifying resource limits/requests without restarts.
* **Feature Level:** Container-level resize is stable in **v1.35+** (enabled by default). Pod-level sandbox sizing is beta in **v1.36+**.
* **Configuration (`resizePolicy`):** Defines how the runtime handles dynamic resource updates:
  * `RestartNotRequired` (Default for CPU): Updates CPU weights on the fly via cgroups.
  * `Restart` (Default for Memory): Restarts the container (brief container downtime, no Pod replacement) to apply memory limits.

---


## 🛠️ Practical Proof of Concept (PoC)

In this PoC, we will create a dedicated scheduling scenario (Taint + Node Affinity), verify Metrics Server operations, and observe the lifecycle difference between ConfigMaps injected as Environment Variables versus Volume Mounts.

### Step-by-Step Guided Steps

#### Phase 1: Exclusively Dedicated Scheduling
1. **Label and Taint a Node:**
   Identify a worker node (e.g. `worker-1`) and configure it for exclusive ML workloads:
   ```bash
   kubectl label nodes worker-1 department=ml
   kubectl taint nodes worker-1 department=ml:NoSchedule
   ```
2. **Deploy a Standard Pod (Without Tolerations):**
   ```bash
   kubectl run test-general-pod --image=nginx --dry-run=client -o yaml | kubectl apply -f -
   ```
   *Observation:* Describe the node or check scheduling. The general pod will never land on `worker-1` because it is tainted.
3. **Deploy the Dedicated Pod (With Affinity and Tolerations):**
   Create a manifest `ml-app.yaml`:
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: ml-app
   spec:
     tolerations:
     - key: "department"
       operator: "Equal"
       value: "ml"
       effect: "NoSchedule"
     affinity:
       nodeAffinity:
         requiredDuringSchedulingIgnoredDuringExecution:
           nodeSelectorTerms:
           - matchExpressions:
             - key: department
               operator: In
               values:
               - ml
     containers:
     - name: application
       image: alpine
       command: ["sleep", "3600"]
   ```
   Apply it:
   ```bash
   kubectl apply -f ml-app.yaml
   ```
   Verify it was scheduled on `worker-1`:
   ```bash
   kubectl get pod ml-app -o wide
   ```

#### Phase 2: Metrics Server Auditing
1. **Confirm Metrics Server is Running:**
   ```bash
   kubectl get deploy metrics-server -n kube-system
   ```
2. **Audit CPU and Memory Performance:**
   ```bash
   kubectl top node
   kubectl top pod -A
   ```

#### Phase 3: ConfigMap Update Behavior (Env vs. Volume Mount)
1. **Create the ConfigMap:**
   ```bash
   kubectl create configmap lifecycle-config --from-literal=COLOR=red --from-literal=MODE=dev
   ```
2. **Deploy the Test Pod mounting it via environment AND volume:**
   Create `config-test-pod.yaml`:
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: config-test-pod
   spec:
     containers:
     - name: reader
       image: alpine
       command: ["sleep", "3600"]
       env:
       - name: ENV_COLOR
         valueFrom:
           configMapKeyRef:
             name: lifecycle-config
             key: COLOR
       volumeMounts:
       - name: config-volume
         mountPath: /etc/config
     volumes:
     - name: config-volume
       configMap:
         name: lifecycle-config
   ```
   Apply it:
   ```bash
   kubectl apply -f config-test-pod.yaml
   ```
3. **Inspect Initial Values:**
   * Check environment variable:
     ```bash
     kubectl exec config-test-pod -- env | grep ENV_COLOR
     # Output: ENV_COLOR=red
     ```
   * Check volume file:
     ```bash
     kubectl exec config-test-pod -- cat /etc/config/COLOR
     # Output: red
     ```
4. **Update the ConfigMap:**
   Edit the ConfigMap and change `COLOR` to `blue`:
   ```bash
   kubectl patch configmap lifecycle-config -p '{"data":{"COLOR":"blue"}}'
   ```
5. **Observe Update Behavior:**
   * Instantly verify the environment variable:
     ```bash
     kubectl exec config-test-pod -- env | grep ENV_COLOR
     # Output: ENV_COLOR=red (Did NOT update)
     ```
   * Wait 1-2 minutes for Kubelet sync, then check the volume:
     ```bash
     kubectl exec config-test-pod -- cat /etc/config/COLOR
     # Output: blue (Successfully updated!)
     ```
6. **Clean up Resources:**
   ```bash
   kubectl delete pod ml-app test-general-pod config-test-pod
   kubectl delete configmap lifecycle-config
   kubectl taint nodes worker-1 department-
   kubectl label nodes worker-1 department-
   ```


### Phase 4: Automated Scheduling & Lifecycle Verification Script
For a fully automated validation of Kubernetes scheduling logic (Labels, Selectors, Affinities, Taints, Tolerations) and lifecycle configuration synchronization (ConfigMap/Secret volume mounts and env var injection), use the verification script located at:
`Reference Notes/scripts/verify_scheduling_lifecycle_poc.sh`

#### Script Functionality Summary:
1. **Dynamic Node Identification:** Detects a control-plane or worker node to target for label/taint operations, extracting and preserving pre-existing node taints to ensure compatibility.
2. **Node Labeling & Affinity Validation:** Applies `zone=frontend-secure` to the node, then deploys and verifies Pods targeting that label via `nodeSelector` and `nodeAffinity` respectively.
3. **Taints & Tolerations Validation:** Taints the node with `tier=backend:NoSchedule`, verifies that a Pod without a toleration remains `Pending`, and confirms that a Pod with a matching toleration schedules successfully.
4. **ConfigMap & Secret Sync Validation:** Configures a ConfigMap and Secret, mounts both as volumes, and injects keys into environment variables, verifying that all resource references are fully resolved inside the running container.
5. **Diagnostics & Cleanup:** Automatically collects verification Pod logs, audits `metrics-server` statistics if present, and tears down all created resources (using an EXIT trap to ensure cleanup even on failures).

#### How to Run:
```bash
# Make the script executable
chmod +x "Reference Notes/scripts/verify_scheduling_lifecycle_poc.sh"

# Execute the script (specify namespace option if desired)
./"Reference Notes/scripts/verify_scheduling_lifecycle_poc.sh" -n default
```

---

---
