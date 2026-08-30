---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - kubernetes/workloads
  - kubernetes/deployments
---

# Module 0-6-2: Deployments, ReplicaSets & Rollout Strategies

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Reference MOC]] > **Module 0-6-2**

---

## 8. ReplicaSets & Replication Controllers

Controllers ensure the desired number of Pod replicas are running at any given time.

### 8.1 Limitations of Manual Pod Management
Creating and maintaining Pods manually (outside of a controller) presents significant operational issues:
1. **Name Uniqueness:** Each Pod must have a unique name inside its namespace.
2. **Manual Scaling:** Scaling out requires copy-pasting manifests; scaling in requires manual deletion of specific Pods.
3. **Template Immutability:** Updating a container image or configuration requires manual deletion and recreation of each individual Pod.

### 8.2 Replication Controller vs. ReplicaSet (Evolutionary Bridge)
*   **Legacy Concept (Replication Controller):** The Replication Controller (RC) is the legacy replication technology in Kubernetes (running in the `v1` core API group). It was originally designed to solve the problem of scaling and high availability of stateless pods. However, it had severe architectural limitations:
    1. **Equality-Based Selectors Only:** It only supports basic equality-based selectors (e.g., `app: nginx` or `env: production`). There is no support for matching multiple environments or checking key existence.
    2. **Client-Side Rolling Upgrades:** The RC has no built-in rolling update logic on the server side. Upgrades were performed client-side using `kubectl rolling-update`, which required constant communication between the client CLI and the API server, making the process slow, brittle to network drops, and difficult to automate.
*   **Modern Bridge (ReplicaSet):** The ReplicaSet (RS) replaced the Replication Controller as the modern workload replication standard (using the `apps/v1` API group). 
    1. **Set-Based Selectors:** It introduces `matchExpressions` syntax supporting advanced logic (`In`, `NotIn`, `Exists`, `DoesNotExist` operators). This allows a single ReplicaSet to manage pods across multiple tiers or environment variables.
    2. **Orchestrated by Deployments:** Rather than managing rolling upgrades directly, ReplicaSets serve as the replication controller engine managed by the higher-level **Deployment** controller, which orchestrates ReplicaSets server-side to execute zero-downtime upgrades and rollbacks.

### 8.3 The Reconciliation Loop & Ownership Mechanics
A ReplicaSet automates Pod management using a continuous **reconciliation loop** comparing the observed state (actual running Pod count matching the selector) with the desired state (configured replicas):
* If there is a deficit, it commands the API server to create new Pods from its template.
* If there is a surplus, it deletes the excess Pods.

#### Selector-Based Pod Monitoring
ReplicaSets monitor pods dynamically via label selectors:
* **`ownerReferences`:** When the ReplicaSet spawns a Pod, it injects the ReplicaSet's UID as an `ownerReference` in the Pod's metadata.
* **Adoption:** If a ReplicaSet is created in a namespace where matching pods already exist, it checks if they have a controller `ownerReference`. If they do not, it **adopts** them by writing its owner reference to the pod metadata and counting them toward the replica limit.
* **Dynamic Pod Quarantining (Loose Coupling):** Since ReplicaSets rely solely on label matching, an administrator can change a malfunctioning Pod's labels at runtime. This disconnects the Pod from the selector, prompting the ReplicaSet to immediately spawn a healthy replacement pod while the quarantined pod remains running for debugging.

### 8.4 Workload Scaling Commands
ReplicaSets can be scaled in three ways:
1. **Manifest File Modification (Preferred/Declarative):** Modify the `spec.replicas` field in the local YAML and run:
   ```bash
   kubectl apply -f replicaset.yaml
   ```
2. **Imperative Scaling Command:**
   ```bash
   kubectl scale replicaset <rs-name> --replicas=5
   ```
3. **In-Memory Editor:**
   ```bash
   kubectl edit replicaset <rs-name>
   ```

### 8.5 Template Updates: Update-In-Place vs. Recreate Behaviors
* **No Automatic Rolling Updates:** When you modify the Pod template (`spec.template`) of a ReplicaSet (e.g., updating the container image), the ReplicaSet **does not automatically update or roll over existing pods**. The controller only applies the template to *new* pods created after the update.
* **Recreating/Applying Template Changes:** To apply the updated configuration to running pods, you must either:
  1. **Recreate the Pods (Manual Rollout):** Delete the existing pods. The ReplicaSet's reconciliation loop will detect the drop in replica count and create new pods using the updated template.
  2. **Recreate the ReplicaSet:** Delete the ReplicaSet and recreate it.
  > [!TIP]
  > For zero-downtime, automated rolling updates, always use **Deployments** instead of standalone ReplicaSets.

### 8.5 Identifying Pod Ownership & Diagnostics
ReplicaSet status and events are inspected using:
```bash
kubectl describe replicaset <name>
```
*(Note: `kubectl logs` streams container-level outputs, requiring backing Pods to be active).*

To verify which controller owns a specific Pod, query its metadata owner reference:
```bash
# Query the owner name directly via JSONPath
kubectl get pod <pod-name> -o jsonpath='{.metadata.ownerReferences[0].name}'

# Query the controller kind
kubectl get pod <pod-name> -o jsonpath='{.metadata.ownerReferences[0].kind}'
```

### 8.6 Cleanup and Cascade Deletion
* **Default Cascade Deletion:** Deleting a ReplicaSet deletes both the controller and all associated Pods:
  ```bash
  kubectl delete replicaset myapp
  ```
* **Orphan Deletion:** Deleting the controller while leaving Pods running:
  ```bash
  kubectl delete replicaset myapp --cascade=orphan
  ```
  *(If a new ReplicaSet with a matching selector is created later, it will adopt these orphan Pods).*

### 8.7 E2E ReplicaSet YAML
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: application-replicaset
  labels:
    app: multi-tier-app
    tier: api
spec:
  replicas: 3
  # Selector defines how the ReplicaSet finds which Pods to manage
  selector:
    matchLabels:
      tier: api
    matchExpressions:
      - {key: app, operator: In, values: [multi-tier-app]}
      - {key: environment, operator: NotIn, values: [development]}
  # Template defines the Pod to create when scaling up
  template:
    metadata:
      labels:
        tier: api
        app: multi-tier-app
        environment: production
    spec:
      containers:
      - name: api-server
        image: redis:7.2-alpine
        ports:
        - containerPort: 6379
```

### 8.3 Set-Based Selectors & matchExpressions Syntax
While legacy Replication Controllers only supported equality-based selectors (e.g., `app: nginx`), ReplicaSets support set-based selectors using the `matchExpressions` block. This allows for complex filtering using operators:
*   **`In`**: The label value must match one of the specified values.
*   **`NotIn`**: The label value must not match any of the specified values.
*   **`Exists`**: The label key must exist on the Pod (no `values` field should be specified).
*   **`DoesNotExist`**: The label key must not exist on the Pod (no `values` field should be specified).

*Example `matchExpressions` block:*
```yaml
  selector:
    matchExpressions:
      - {key: tier, operator: In, values: [frontend, api]}
      - {key: environment, operator: NotIn, values: [development, staging]}
      - {key: partition, operator: Exists}
      - {key: legacy-client, operator: DoesNotExist}
```

### 8.4 Under the Hood: Adoption, Orphaning, and Ownership Mechanics
ReplicaSets do not maintain a static list of Pods. Instead, they dynamically query the API Server for Pods matching their selectors. 

#### The Lifecycle Steps:
1.  **Creation & `ownerReferences`:** When a ReplicaSet controller creates a Pod to satisfy its desired count, the API Server injects an `ownerReference` field into the Pod's metadata pointing directly to that specific ReplicaSet instance (e.g., using its UID).
2.  **Adoption:** If a ReplicaSet is created and there are already existing Pods in the namespace that match its label selector:
    *   The controller inspects the Pods' `ownerReferences`.
    *   If a matching Pod is orphaned (it has no active controller `ownerReference`), the ReplicaSet **adopts** it by updating the Pod's `ownerReferences` to point to itself. It counts this Pod toward its active replica count instead of spinning up a new one.
3.  **Orphaning:** If you delete a ReplicaSet with the cascade orphan policy (`kubectl delete rs <name> --cascade=orphan`), the controller removes the `ownerReferences` from all managed Pods. These Pods become **orphaned** and will remain running until they are manually cleaned up or adopted by another controller with a matching selector.

### 8.5 The API Server's Validation Guardrail (apps/v1)
To prevent infinite creation loops caused by configuration errors, the `apps/v1` API group uses a validation webhook inside the API Server's request pipeline:
*   **The Mismatch Safeguard:** Before persisting a ReplicaSet object in `etcd`, the API Server verifies that the selector (`spec.selector.matchLabels` and/or `spec.selector.matchExpressions`) **perfectly matches or is a subset of** the Pod template labels (`spec.template.metadata.labels`).
*   **The Rejection:** If you attempt to apply a manifest where the template labels do not satisfy the selector (e.g., selector expects `app: frontend` but the template stamps `app: backend`), the API Server outright rejects the request with an error:
    `invalid: spec.template.metadata.labels: Invalid value: ... : 'selector' does not match template 'labels'`
*   **Consequence:** The misconfigured object is never stored in `etcd`, and the ReplicaSet controller never sees it. This prevents a simple typo from triggering an endless Pod creation loop.

### 8.6 Advanced Troubleshooting: Thrashing Loops
Because of the validation guardrail, runaway Pod creation loops in modern Kubernetes are almost exclusively caused by one of two cluster-level anomalies:

#### Scenario A: Controller Collision (Overlapping Selectors)
This happens when multiple controllers have overlapping selectors but different templates.
1.  **The Setup:** ReplicaSet-A (desiring 3 replicas) and ReplicaSet-B (desiring 3 replicas) both use `matchLabels: app: nginx`.
2.  **Adoption Check:** ReplicaSet-B wakes up, queries for `app: nginx`, and finds the 3 Pods created by ReplicaSet-A. It checks their `ownerReferences` and sees they belong to ReplicaSet-A, so it cannot adopt them. Thus, ReplicaSet-B calculates it owns 0 Pods.
3.  **Creation:** ReplicaSet-B creates 3 new Pods (stamped with its own `ownerReferences`). The namespace now has 6 Pods matching `app: nginx`.
4.  **The Cull (Scaling Down):** ReplicaSet-A wakes up, queries for `app: nginx`, and sees 6 Pods. When scaling down to its desired state (3), **the controller does not check `ownerReferences`**. It ruthlessly deletes 3 excess Pods (which may include Pods owned by ReplicaSet-B).
5.  **The Loop:** ReplicaSet-B wakes up, finds its Pods are gone, and creates 3 new ones. ReplicaSet-A wakes up, sees 6 Pods, and deletes 3. This infinite loop of creation and deletion is called **thrashing**, causing high API Server CPU load and transient Pod availability.
6.  **Resolution:** Edit the manifests to ensure unique selectors (e.g., combining `app: nginx` with a tier label like `tier: frontend` vs `tier: backend`).

#### Scenario B: Mutating Admission Webhook Interference
1.  **The Setup:** A mutating admission webhook (e.g., from a service mesh or security policy) intercepts Pod creation requests.
2.  **The Interference:** When the ReplicaSet submits a Pod with labels matching its selector (e.g., `app: frontend`), the webhook modifies or strips that label before the Pod is persisted in `etcd`.
3.  **The Loop:** The Pod is created but lacks the expected label. The ReplicaSet queries the API server, sees a deficit because the newly created Pod does not match its selector, and submits another Pod creation request. The webhook strips the label again, leading to the creation of hundreds of orphaned Pods.
4.  **Resolution:** Inspect admission webhook logs, check if Pods are missing expected labels, and update either the webhook configuration or the workloads' labels.


---

## 9. Deployments: Declared State Management

### 9.1 Limitations of Standalone ReplicaSets
In a standalone ReplicaSet, Pod templates are immutable. Upgrading a container's image or configuration requires manually deleting the old ReplicaSet and deploying a new one, causing direct application downtime.

### 9.2 Deployment Wrapper Architecture
A **Deployment** is a parent wrapper (`apps/v1`) that manages one or more ReplicaSets, which in turn manage the Pods.
* **Delegated Execution:** Scaling and self-healing tasks are executed by the underlying ReplicaSet.
* **Direct Abstraction:** The developer declares the desired state in the Deployment. The deployment controller manages ReplicaSet progression (creating new ones and scaling down old ones) automatically, abstracting the process.

### 9.3 Update Strategies

#### `Recreate` Strategy
*   **Behavior:** Terminates all running Pods associated with the Deployment before creating any new Pods.
*   **Events Under the Hood:**
    1. The Deployment Controller scales down the active ReplicaSet (old version) to `0` replicas.
    2. The old Pods are sent SIGTERM (and SIGKILL if graceful termination window expires) and deleted.
    3. Once all old Pods are fully terminated, the controller scales up the new ReplicaSet (new version) to the desired count.
*   **Downtime:** Causes absolute service downtime during the update window while old pods are dead and new pods are starting.
*   **Use Case:** Recommended when the application cannot support running multiple versions concurrently (e.g. sharing read-write storage with exclusive file lock requirements, or database schemas that do not support backward compatibility).

#### `RollingUpdate` Strategy
*   **Behavior:** Gradually replaces Pods of the old ReplicaSet with Pods of the new ReplicaSet. This is the default update strategy.
*   **Events Under the Hood:**
    1. The Deployment Controller creates a new ReplicaSet.
    2. It scales up the new ReplicaSet and scales down the old ReplicaSet incrementally, taking down old pods and bringing up new pods one-by-one (or in batches depending on `maxSurge` and `maxUnavailable`).
    3. The processes overlap: new pods are provisioned and old pods are terminated simultaneously, maintaining service availability.
*   **Parameters & Defaults:**
    *   `maxSurge`: The maximum number of Pods that can be created above the desired replica count during the update. Can be expressed as an absolute integer (e.g., `2`) or a percentage (e.g., `25%`). **Default: `25%`**.
    *   `maxUnavailable`: The maximum number of Pods that can be offline during the update. Can be an integer or percentage. **Default: `25%`**.
    *   **Validation Rule:** Both `maxSurge` and `maxUnavailable` **cannot be `0` simultaneously**. If both are set to `0`, the Deployment creation will fail because the controller would have no way to progress the rollout.
    *   *Calculation Example:* With 4 desired replicas, `maxSurge: 25%` (1 pod) and `maxUnavailable: 25%` (1 pod):
        *   Max total Pods during rollout: $4 + 1 = 5$
        *   Min active/healthy Pods during rollout: $4 - 1 = 3$


### 9.2 E2E Deployment Spec with Strategy Parameters
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app-deployment
  labels:
    app: web-server
spec:
  replicas: 4
  revisionHistoryLimit: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
  selector:
    matchLabels:
      app: web-server
  template:
    metadata:
      labels:
        app: web-server
    spec:
      containers:
      - name: nginx-web
        image: nginx:1.25.3
        ports:
        - containerPort: 80
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
```

### 9.3 Rollout and Revision History Management
When a Deployment is updated (e.g., changing the container image), a new ReplicaSet is created.
*   **Rollout Auditing:** You can track the state of the update using:
    ```bash
    kubectl rollout status deployment/web-app-deployment
    ```
*   **History Retainment:** The Deployment maintains historical ReplicaSets up to the `revisionHistoryLimit`. To view the list of revisions:
    ```bash
    kubectl rollout history deployment/web-app-deployment
    ```
*   **Revision Inspection:** View details of a specific historical version:
    ```bash
    kubectl rollout history deployment/web-app-deployment --revision=2
    ```
*   **Rollback Mechanism (Undo Rollout):** If the rollout fails or contains a bug, undo it. The deployment controller downscales the new ReplicaSet and upscales the previous ReplicaSet, restoring the prior state:
    ```bash
    # Revert to the immediate previous revision
    kubectl rollout undo deployment/web-app-deployment
    
    # Revert to a specific historical revision
    kubectl rollout undo deployment/web-app-deployment --to-revision=1
    ```

#### 9.3.1 Deployment Lab Walkthrough & Diagnostic logs
Analyze deployment rollouts, state changes, and history logs using these resources:
* **Interactive Deployment Rollout logs:** [deployments.html](file:///home/karim/Desktop/BrainDump/Attachments/deployments.html)
* **Interactive Rollout and Rollback Logs:** [rolling+out+and+rolling+back.html](file:///home/karim/Desktop/BrainDump/Attachments/rolling+out+and+rolling+back.html)

---
