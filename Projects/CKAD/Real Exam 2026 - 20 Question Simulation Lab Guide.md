# CKAD Real Exam 2026 - Authentic 20-Question Simulation Lab Guide
**Master Blueprint, Paired Approach Variants & Speed Run Protocols**

---

## 📌 Executive Overview & Strategy

The **Certified Kubernetes Application Developer (CKAD)** exam is a 120-minute, 100% hands-on performance test comprising 15 to 17 real-world tasks. Unlike CKS (which emphasizes deep Linux security layers, eBPF, and container breakouts) and CKA (which emphasizes control-plane infrastructure and node maintenance), **CKAD is 100% focused on speed, declarative workload management, containerized architecture patterns, and rapid troubleshooting**.

> [!IMPORTANT]
> **The Paired-Approach Rule:**
> In the real exam, similar questions appear with subtly different approaches (e.g. Canary vs. Blue/Green, Ingress PathType fix vs. TLS termination, Secret single-key injection vs. bulk `envFrom`, Liveness exec vs. Readiness HTTP). This guide structures every core topic into **paired scenarios** so you are never caught off-guard.

---

## ⚡ Master Exam Speed Table (2-Minute Execution Formats)

| # | Topic | Core Exam Pattern | Speed CLI / Shortcut Formula | Target Time |
| :---: | :--- | :--- | :--- | :---: |
| **01A** | Secrets (Selective) | `valueFrom.secretKeyRef` | `kubectl create secret generic <name> --from-literal=K=V` | 2 min |
| **01B** | ConfigMap (Bulk) | `envFrom.configMapRef` + Volume | `envFrom: [configMapRef: {name: ...}]` | 2 min |
| **02A** | CronJobs | History limits, deadline, Never | `kubectl create cronjob <name> --image=... --schedule="..."` | 2 min |
| **02B** | Jobs | Completions & `--from=cronjob` | `kubectl create job <name> --from=cronjob/<cron-name>` | 1 min |
| **03A** | RBAC (Namespace) | Logs error -> SA -> Role -> Binding | `kubectl create sa/role/rolebinding` | 2.5 min |
| **03B** | RBAC (Cluster) | ClusterRole + RoleBinding delegation | `kubectl create clusterrole` + `rolebinding` | 2 min |
| **04** | RBAC Pod Binding | Replace wrong SA on immutable Pod | `k get po <name> -o yaml > p.yaml` -> replace | 1.5 min |
| **05** | Image Build | Podman build + save tarball | `podman build -t <tag> . && podman save -o <f> <tag>` | 2 min |
| **06A** | Canary Release | Proportional replicas + label match | `kubectl scale deploy ...` (80/20 ratio) | 2 min |
| **06B** | Blue/Green Cutover | Instant Service selector switch | `kubectl set selector svc ...` or `k edit svc` | 1.5 min |
| **07A** | NetworkPolicy (Labels)| Fix Pod labels to satisfy policy | `kubectl label pod <name> role=<val> --overwrite` | 1.5 min |
| **07B** | NetworkPolicy (Write) | Multi-tenant Ingress & Egress hole | NamespaceSelector + PodSelector + DNS hole (port 53) | 3 min |
| **08A** | API Deprecation | `extensions/v1beta1` -> `apps/v1` | Add `spec.selector.matchLabels` | 2 min |
| **08B** | Ingress API Fix | `networking.k8s.io/v1` syntax | `service.name` + `service.port.number` + `pathType` | 2 min |
| **09** | Rollouts & Undo | `set image` -> status -> undo | `kubectl rollout undo deploy/<name> --to-revision=1` | 2 min |
| **10A** | Readiness Probe | HTTP GET traffic gate | `readinessProbe: httpGet: {path: /ready, port: 8080}` | 2 min |
| **10B** | Liveness Probe | Exec command restart lifecycle | `livenessProbe: exec: {command: [test, -f, /tmp/h]}` | 2 min |
| **11A** | SecurityContext | Pod `runAsUser` + Container `cap` | `runAsUser: 1000` + `capabilities: add: [NET_ADMIN]` | 2 min |
| **11B** | ReadOnly Filesystem | Non-root + read-only + emptyDir | `readOnlyRootFilesystem: true` + mount `/tmp` | 2.5 min |
| **12** | Service Endpoints | Fix broken service selector | Compare `kubectl get po --show-labels` vs `svc.spec` | 1.5 min |
| **13** | NodePort Service | Expose Deployment on NodePort | `kubectl expose deploy <name> --type=NodePort --port=80` | 1.5 min |
| **14A** | Ingress (Host/Path) | Path-based routing with host header | `kubectl create ingress <name> --rule="host/path=svc:port"`| 2 min |
| **14B** | Ingress (TLS) | HTTPS termination with Secret | `spec.tls: [hosts: [...], secretName: ...]` | 2.5 min |
| **15** | Ingress PathType | Fix invalid `pathType` value | Change `InvalidType` to `Prefix` or `Exact` | 1 min |
| **16A** | Resource Limits | Half ResourceQuota calculation | Compute `limits.cpu / 2` and `limits.memory / 2` | 2 min |
| **16B** | Resource Bottleneck | Pending Pod memory troubleshooting | `describe pod` -> find `Insufficient memory` -> lower req | 2 min |
| **17** | Multi-Container Pod | Logging sidecar with emptyDir | Main writes to `/var/log`, sidecar tails `/var/log` | 2.5 min |
| **18** | Observability | Top pods & log grep filtering | `k top pods --sort-by=cpu` & `k logs ... \| grep` | 1.5 min |
| **19** | Storage (PV/PVC) | hostPath PV + PVC + Pod mount | Match `storageClassName`, `accessModes`, `capacity` | 3 min |
| **20** | Storage (Expansion) | Online PVC expansion | `k edit pvc <name>` -> bump `spec.resources.requests` | 1.5 min |

---

## 🛠️ Full Question Scenarios, Problem Statements & Speed Formulas

```
+---------------------------------------------------------------------------------------+
| DOMAIN 1: APPLICATION ENVIRONMENT, CONFIGURATION & SECURITY (25%)                    |
+---------------------------------------------------------------------------------------+
```

### 🔹 Question 01A: Secret Creation & Single-Key Injection (`valueFrom`)
* **Directory:** `/home/karim/ckad-exam-lab/q01a-secret-keyref/`
* **Approach:** Selective key injection from Generic Secret.
* **Problem Statement:**
  In namespace `default`, Deployment `api-server` currently contains hardcoded environment variables `DB_USER=admin` and `DB_PASS=Secret123!`.
  1. Create a generic Secret named `db-credentials` in namespace `default` containing these credentials.
  2. Modify Deployment `api-server` to inject these credentials securely using `valueFrom.secretKeyRef`.
  3. Ensure the Deployment successfully rolls out without changing the Deployment name.
* **Speed Formula:**
  ```bash
  # 1. Create secret imperatively:
  kubectl create secret generic db-credentials \
    --from-literal=DB_USER=admin \
    --from-literal=DB_PASS='Secret123!' \
    -n default

  # 2. Edit deployment:
  kubectl edit deploy api-server -n default
  ```
  ```yaml
  # Inside spec.template.spec.containers[0].env:
  env:
  - name: DB_USER
    valueFrom:
      secretKeyRef:
        name: db-credentials
        key: DB_USER
  - name: DB_PASS
    valueFrom:
      secretKeyRef:
        name: db-credentials
        key: DB_PASS
  ```
  ```bash
  # 3. Verify rollout:
  kubectl rollout status deploy api-server -n default
  ```

---

### 🔹 Question 01B: ConfigMap Bulk Injection (`envFrom`) & Volume Projection
* **Directory:** `/home/karim/ckad-exam-lab/q01b-configmap-envfrom/`
* **Approach:** Bulk injection vs. Volume file projection (Contrasts with Q01A).
* **Problem Statement:**
  In namespace `staging`, an existing ConfigMap `app-config` contains 10 application flags.
  1. Update Deployment `order-service` to load **all** keys from `app-config` as environment variables at once without declaring individual key references.
  2. In the same namespace, create a ConfigMap `special-config` containing key `ui.properties` with value `theme=dark\nmode=compact`.
  3. Mount `special-config` as a read-only volume into container `app` at path `/etc/config`.
* **Speed Formula:**
  ```bash
  # 1. Create special configmap:
  kubectl create configmap special-config \
    --from-literal=ui.properties="theme=dark
  mode=compact" -n staging

  # 2. Update deployment with envFrom and volumeMount:
  kubectl edit deploy order-service -n staging
  ```
  ```yaml
  spec:
    template:
      spec:
        containers:
        - name: app
          envFrom:
          - configMapRef:
              name: app-config
          volumeMounts:
          - name: config-vol
            mountPath: /etc/config
            readOnly: true
        volumes:
        - name: config-vol
          configMap:
            name: special-config
  ```

---

### 🔹 Question 11A: SecurityContext — Pod-Level User vs Container-Level Capabilities
* **Directory:** `/home/karim/ckad-exam-lab/q11a-security-context/`
* **Approach:** Splitting privileges between Pod and Container layers.
* **Problem Statement:**
  In namespace `default`, Deployment `secure-app` runs without security parameters.
  1. Configure the Pod specification to run processes with user ID `1000` (`runAsUser: 1000`).
  2. Add the Linux capability `NET_ADMIN` to the container named `app`.
  3. Verify the updated deployment pods reach `Running` state.
* **Speed Formula:**
  ```yaml
  spec:
    template:
      spec:
        securityContext:       # <-- POD LEVEL (Applies to all containers)
          runAsUser: 1000
        containers:
        - name: app
          image: nginx
          securityContext:     # <-- CONTAINER LEVEL (Capabilities are container-only!)
            capabilities:
              add:
                - NET_ADMIN
  ```

---

### 🔹 Question 11B: Hardened SecurityContext — ReadOnly Root Filesystem with Scratch Mount
* **Directory:** `/home/karim/ckad-exam-lab/q11b-readonly-rootfs/`
* **Approach:** Container immutability with temporary writable storage (Contrasts with Q11A).
* **Problem Statement:**
  Deployment `payment-worker` in namespace `banking` must be hardened:
  1. Enforce `runAsNonRoot: true` and `allowPrivilegeEscalation: false`.
  2. Make the container root filesystem immutable (`readOnlyRootFilesystem: true`).
  3. Because the container must write transient cache files to `/tmp`, mount an in-memory `emptyDir` volume to `/tmp`.
* **Speed Formula:**
  ```yaml
  spec:
    template:
      spec:
        containers:
        - name: worker
          image: nginx
          securityContext:
            runAsNonRoot: true
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
          volumeMounts:
          - name: scratch-space
            mountPath: /tmp
        volumes:
        - name: scratch-space
          emptyDir: {}
  ```

---

```
+---------------------------------------------------------------------------------------+
| DOMAIN 2: APPLICATION DESIGN AND BUILD (20%)                                         |
+---------------------------------------------------------------------------------------+
```

### 🔹 Question 02A: CronJob Configuration (Schedule, History, Deadline)
* **Directory:** `/home/karim/ckad-exam-lab/q02a-cronjob-limits/`
* **Approach:** Recurring cron schedule with strict operational retention constraints.
* **Problem Statement:**
  Create a CronJob named `backup-job` in namespace `default`:
  - Schedule: Every 30 minutes (`*/30 * * * *`).
  - Container Image: `busybox:latest`.
  - Command: `echo "Backup completed"`.
  - Set `successfulJobsHistoryLimit: 3`.
  - Set `failedJobsHistoryLimit: 2`.
  - Set `activeDeadlineSeconds: 300`.
  - Set `restartPolicy: Never`.
* **Speed Formula:**
  ```bash
  kubectl create cronjob backup-job \
    --image=busybox:latest \
    --schedule="*/30 * * * *" \
    --dry-run=client -o yaml -- /bin/sh -c 'echo "Backup completed"' > cron.yaml
  ```
  Add the 3 limits into `spec` and apply:
  ```yaml
  apiVersion: batch/v1
  kind: CronJob
  metadata:
    name: backup-job
    namespace: default
  spec:
    schedule: "*/30 * * * *"
    successfulJobsHistoryLimit: 3
    failedJobsHistoryLimit: 2
    jobTemplate:
      spec:
        activeDeadlineSeconds: 300
        template:
          spec:
            restartPolicy: Never
            containers:
            - name: backup-job
              image: busybox:latest
              command: ["/bin/sh", "-c", "echo \"Backup completed\""]
  ```

---

### 🔹 Question 02B: Batch Jobs & Instant On-Demand CronJob Triggering
* **Directory:** `/home/karim/ckad-exam-lab/q02b-job-ondemand/`
* **Approach:** Parallel batch execution & manual trigger from CronJob (Contrasts with Q02A).
* **Problem Statement:**
  1. An existing CronJob `nightly-cleanup` is in namespace `maintenance`. An administrator needs to test its execution immediately without waiting for the next scheduled interval or modifying the CronJob. Create a Job named `manual-test-run` spawned directly from `nightly-cleanup`.
  2. Create a standalone Job `parallel-processor` in namespace `batch-ops` that runs image `busybox` with command `sleep 5`. Configure it to complete 6 times (`completions: 6`) with 2 parallel pods (`parallelism: 2`).
* **Speed Formula:**
  ```bash
  # 1. Spawn Job instantly from existing CronJob:
  kubectl create job manual-test-run --from=cronjob/nightly-cleanup -n maintenance

  # 2. Create parallel Job:
  kubectl create job parallel-processor --image=busybox -n batch-ops --dry-run=client -o yaml -- sleep 5 > job.yaml
  ```
  Add completions and parallelism:
  ```yaml
  spec:
    completions: 6
    parallelism: 2
    template:
      spec:
        restartPolicy: Never
        containers:
        - name: parallel-processor
          image: busybox
          command: ["sleep", "5"]
  ```

---

### 🔹 Question 05: Build Container Image with Podman & Save Tarball
* **Directory:** `/home/karim/ckad-exam-lab/q05-podman-build/`
* **Domain:** Container Runtimes & OCI Artifacts
* **Problem Statement:**
  Directory `/root/app-source` contains an application source tree and a valid `Dockerfile`.
  1. Using `podman`, build a container image tagged `my-app:1.0` using `/root/app-source` as build context.
  2. Save the built image as an uncompressed tarball to `/root/my-app.tar`.
  3. Verify the image exists locally and the tar file is created.
* **Speed Formula:**
  ```bash
  # 1. Build image:
  cd /root/app-source
  podman build -t my-app:1.0 .

  # 2. Save tarball:
  podman save -o /root/my-app.tar my-app:1.0

  # 3. Verification:
  ls -lh /root/my-app.tar
  podman images | grep my-app
  ```

---

### 🔹 Question 17: Multi-Container Pod (Sidecar Logging Pattern)
* **Directory:** `/home/karim/ckad-exam-lab/q17-sidecar-logging/`
* **Domain:** Multi-Container Pod Design Patterns
* **Problem Statement:**
  In namespace `logging`, deploy a Pod named `multi-app`:
  1. Container 1 named `app` (image: `busybox:latest`) appends the current timestamp to `/var/log/access.log` every 1 second: `while true; do date >> /var/log/access.log; sleep 1; done`.
  2. Container 2 named `sidecar` (image: `busybox:latest`) reads the log stream: `tail -n+1 -F /var/log/access.log`.
  3. Both containers must share an `emptyDir` volume mounted at `/var/log`.
  4. Verify that running `kubectl logs multi-app -c sidecar -n logging` streams the timestamp output.
* **Speed Formula:**
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: multi-app
    namespace: logging
  spec:
    containers:
    - name: app
      image: busybox:latest
      command: ["/bin/sh", "-c", "while true; do date >> /var/log/access.log; sleep 1; done"]
      volumeMounts:
      - name: shared-logs
        mountPath: /var/log
    - name: sidecar
      image: busybox:latest
      command: ["/bin/sh", "-c", "tail -n+1 -F /var/log/access.log"]
      volumeMounts:
      - name: shared-logs
        mountPath: /var/log
    volumes:
    - name: shared-logs
      emptyDir: {}
  ```

---

```
+---------------------------------------------------------------------------------------+
| DOMAIN 3: APPLICATION DEPLOYMENT (20%)                                                |
+---------------------------------------------------------------------------------------+
```

### 🔹 Question 06A: Canary Deployment via Replica Ratio (Label Sharing)
* **Directory:** `/home/karim/ckad-exam-lab/q06a-canary-deployment/`
* **Approach:** Proportional multi-deployment traffic splitting via shared Service selectors.
* **Problem Statement:**
  In namespace `default`, Deployment `web-app` runs with 5 replicas (labels: `app=webapp, version=v1`). Service `web-service` targets `selector: app=webapp`.
  1. Scale Deployment `web-app` to 8 replicas (representing 80% baseline traffic).
  2. Create a new Canary Deployment `web-app-canary` running 2 replicas (20% traffic) with image `nginx:1.25`, labels `app=webapp, version=v2`, and selector `matchLabels: { app: webapp, version: v2 }`.
  3. Verify Service `web-service` endpoints select all 10 pods across both versions.
* **Speed Formula:**
  ```bash
  # 1. Scale baseline:
  kubectl scale deploy web-app --replicas=8 -n default

  # 2. Create canary:
  kubectl get deploy web-app -n default -o yaml > canary.yaml
  ```
  Edit `canary.yaml`:
  - `metadata.name: web-app-canary`
  - `spec.replicas: 2`
  - `spec.selector.matchLabels.version: v2`
  - `spec.template.metadata.labels.version: v2`
  - `spec.template.spec.containers[0].image: nginx:1.25`
  ```bash
  kubectl apply -f canary.yaml

  # 3. Verify endpoints count = 10:
  kubectl get ep web-service -n default
  ```

---

### 🔹 Question 06B: Blue/Green Deployment via Instant Service Cutover
* **Directory:** `/home/karim/ckad-exam-lab/q06b-bluegreen-cutover/`
* **Approach:** Zero-downtime atomic switch via Service selector mutation (Contrasts with Q06A).
* **Problem Statement:**
  1. Deployment `app-blue` runs 3 replicas in namespace `production` with image `nginx:1.20` and labels `app=shop, color=blue`.
  2. Service `shop-service` currently routes traffic to `selector: app=shop, color=blue`.
  3. Create Deployment `app-green` with 3 replicas running image `nginx:1.25` and labels `app=shop, color=green`.
  4. Perform an atomic zero-downtime cutover by repointing `shop-service` to `color=green`.
* **Speed Formula:**
  ```bash
  # 1. Create green deployment:
  kubectl create deploy app-green --image=nginx:1.25 --replicas=3 -n production
  kubectl label deploy app-green color=green app=shop --overwrite -n production

  # 2. Atomic cutover:
  kubectl set selector service shop-service "app=shop,color=green" -n production

  # 3. Verify endpoints immediately switched to green pods:
  kubectl describe svc shop-service -n production | grep Endpoints
  ```

---

### 🔹 Question 09: Rolling Updates, Revision History & Rollbacks
* **Directory:** `/home/karim/ckad-exam-lab/q09-rolling-update/`
* **Domain:** Workload Lifecycle & Rollout Controllers
* **Problem Statement:**
  Deployment `app-v1` in namespace `default` runs image `nginx:1.20`.
  1. Perform a rolling update updating container `web` to image `nginx:1.25`.
  2. Monitor and wait for the rollout to complete.
  3. Check the rollout history and identify the revision numbers.
  4. Perform an undo rollback to revision 1.
  5. Verify that the image reverts to `nginx:1.20`.
* **Speed Formula:**
  ```bash
  # 1. Set image:
  kubectl set image deploy/app-v1 web=nginx:1.25 -n default

  # 2. Wait for completion:
  kubectl rollout status deploy/app-v1 -n default

  # 3. View history:
  kubectl rollout history deploy/app-v1 -n default

  # 4. Rollback:
  kubectl rollout undo deploy/app-v1 --to-revision=1 -n default
  kubectl rollout status deploy/app-v1 -n default

  # 5. Verify image:
  kubectl get deploy app-v1 -n default -o jsonpath='{.spec.template.spec.containers[0].image}'
  ```

---

### 🔹 Question 08A: Deprecated API Version Migration (`extensions/v1beta1`)
* **Directory:** `/home/karim/ckad-exam-lab/q08a-api-deployment/`
* **Domain:** API Schema Evolution & Resource Validation
* **Problem Statement:**
  File `/root/broken-deploy.yaml` fails to apply with schema errors.
  1. Fix the deprecated API version `extensions/v1beta1` to `apps/v1`.
  2. Add the required `spec.selector.matchLabels` matching `app: myapp`.
  3. Apply the fixed manifest and verify all pods are running.
* **Speed Formula:**
  ```yaml
  apiVersion: apps/v1          # <-- Changed from extensions/v1beta1
  kind: Deployment
  metadata:
    name: broken-app
    namespace: default
  spec:
    replicas: 2
    selector:                  # <-- Added missing mandatory selector
      matchLabels:
        app: myapp
    template:
      metadata:
        labels:
          app: myapp
      spec:
        containers:
        - name: web
          image: nginx:latest
  ```

---

```
+---------------------------------------------------------------------------------------+
| DOMAIN 4: APPLICATION OBSERVABILITY AND MAINTENANCE (15%)                            |
+---------------------------------------------------------------------------------------+
```

### 🔹 Question 10A: Readiness Probe (HTTP GET Traffic Gate)
* **Directory:** `/home/karim/ckad-exam-lab/q10a-readiness-probe/`
* **Approach:** Network traffic gating based on application readiness.
* **Problem Statement:**
  Deployment `api-deploy` in namespace `default` serves traffic on port `8080`.
  1. Add a readiness probe to container `api`:
     - Protocol: HTTP GET on path `/ready`
     - Port: `8080`
     - `initialDelaySeconds: 5`
     - `periodSeconds: 10`
     - `failureThreshold: 3`
  2. Ensure the Deployment rolls out successfully.
* **Speed Formula:**
  ```bash
  kubectl edit deploy api-deploy -n default
  ```
  ```yaml
  # Under spec.template.spec.containers[0]:
  readinessProbe:
    httpGet:
      path: /ready
      port: 8080
    initialDelaySeconds: 5
    periodSeconds: 10
    failureThreshold: 3
  ```

---

### 🔹 Question 10B: Liveness Probe (Exec Command Process Restart Gate)
* **Directory:** `/home/karim/ckad-exam-lab/q10b-liveness-exec/`
* **Approach:** Process health & container restart lifecycle (Contrasts with Q10A).
* **Problem Statement:**
  In namespace `default`, a legacy pod `worker-pod` experiences unhandled memory deadlocks.
  1. Add a Liveness Probe that executes: `cat /tmp/healthy`.
  2. Set `initialDelaySeconds: 10` and `periodSeconds: 5`.
  3. Ensure that if `/tmp/healthy` is missing or deleted, the container is automatically restarted by Kubelet.
* **Speed Formula:**
  ```yaml
  # Inside container spec:
  livenessProbe:
    exec:
      command:
      - cat
      - /tmp/healthy
    initialDelaySeconds: 10
    periodSeconds: 5
  ```

---

### 🔹 Question 16A: Pod Resource Requests & Limits Calculation from ResourceQuota
* **Directory:** `/home/karim/ckad-exam-lab/q16a-resource-quota/`
* **Approach:** Proportional capacity calculation from namespace policy.
* **Problem Statement:**
  Namespace `prod` has a ResourceQuota configured.
  1. Inspect the ResourceQuota in namespace `prod` to find the CPU and Memory limits.
  2. Create a Pod named `resource-pod` in namespace `prod` with image `nginx:latest`.
  3. Set CPU and memory limits to **exactly half** of the ResourceQuota limits.
  4. Set requests to `100m` CPU and `128Mi` memory.
* **Speed Formula:**
  ```bash
  # 1. Query Quota:
  kubectl describe quota -n prod
  # Example output: limits.cpu = 2, limits.memory = 4Gi
  # Half values: cpu = 1 (or 1000m), memory = 2Gi

  # 2. Create Pod:
  kubectl run resource-pod --image=nginx:latest -n prod --dry-run=client -o yaml > pod.yaml
  ```
  ```yaml
  spec:
    containers:
    - name: resource-pod
      image: nginx:latest
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          cpu: "1"
          memory: 2Gi
  ```

---

### 🔹 Question 16B: Troubleshooting Pending Pod Due to Node Resource Exhaustion
* **Directory:** `/home/karim/ckad-exam-lab/q16b-troubleshoot-pending/`
* **Approach:** Bottleneck diagnosis & allocatable capacity tuning (Contrasts with Q16A).
* **Problem Statement:**
  Pod `heavy-worker` in namespace `compute` is stuck in `Pending` state.
  1. Diagnose why the Pod fails to schedule.
  2. Determine the available allocatable memory across cluster worker nodes.
  3. Adjust the Pod specification so that it schedules and transitions to `Running` state without deleting the namespace.
* **Speed Formula:**
  ```bash
  # 1. Inspect events:
  kubectl describe pod heavy-worker -n compute | grep -A 5 Events
  # Output: 0/2 nodes available: 2 Insufficient memory.

  # 2. Check node allocatable:
  kubectl describe nodes | grep -A 5 "Allocatable:"

  # 3. Export, reduce requested memory (e.g. 8Gi -> 256Mi), recreate:
  kubectl get pod heavy-worker -n compute -o yaml > p.yaml
  sed -i 's/8Gi/256Mi/g' p.yaml
  kubectl delete pod heavy-worker -n compute --force --grace-period=0
  kubectl apply -f p.yaml
  ```

---

### 🔹 Question 18: Observability — Top Pods Sorting & Log Grep Extraction
* **Directory:** `/home/karim/ckad-exam-lab/q18-observability-logs/`
* **Domain:** Cluster Metrics & Log Analysis
* **Problem Statement:**
  1. Using Metrics Server CLI, identify the pod consuming the highest CPU in namespace `monitoring`. Save the Pod name to file `/opt/high_cpu_pod.txt`.
  2. Microservice `faulty-backend` in namespace `default` is failing. Extract all log lines containing the string `[ERROR]` and save them to `/opt/errors.log`.
* **Speed Formula:**
  ```bash
  # 1. Top pod by CPU:
  kubectl top pods -n monitoring --sort-by=cpu --no-headers | head -n 1 | awk '{print $1}' > /opt/high_cpu_pod.txt

  # 2. Extract error logs:
  kubectl logs faulty-backend -n default | grep "\[ERROR\]" > /opt/errors.log
  ```

---

```
+---------------------------------------------------------------------------------------+
| DOMAIN 5: SERVICES AND NETWORKING (20%)                                              |
+---------------------------------------------------------------------------------------+
```

### 🔹 Question 07A: NetworkPolicy Remediation via Pod Label Correction
* **Directory:** `/home/karim/ckad-exam-lab/q07a-netpol-labels/`
* **Approach:** Label patching to satisfy immutable network firewall rules.
* **Problem Statement:**
  In namespace `network-demo`, three Pods exist with broken labels: `frontend` (`role=wrong-frontend`), `backend` (`role=wrong-backend`), and `database` (`role=wrong-db`).
  Existing policies enforce:
  - `allow-frontend-to-backend`: Allows ingress from `role=frontend` to `role=backend`.
  - `allow-backend-to-db`: Allows ingress from `role=backend` to `role=db`.
  - Default Deny ingress across all pods.
  **Do NOT edit or delete the NetworkPolicies.** Update Pod labels so that communication flows from `frontend` -> `backend` -> `database`.
* **Speed Formula:**
  ```bash
  # Rapid label overwrite without recreating pods:
  kubectl label pod frontend -n network-demo role=frontend --overwrite
  kubectl label pod backend -n network-demo role=backend --overwrite
  kubectl label pod database -n network-demo role=db --overwrite
  ```

---

### 🔹 Question 07B: Authoring Multi-Rule Ingress & Egress Policy from Scratch
* **Directory:** `/home/karim/ckad-exam-lab/q07b-netpol-authoring/`
* **Approach:** Writing complex ingress/egress policies with namespace selectors & DNS holes.
* **Problem Statement:**
  In namespace `finance`, create a NetworkPolicy named `protect-ledger`:
  1. Applies to Pods labeled `app=ledger`.
  2. Allows Ingress ONLY from pods labeled `role=api-gateway` located inside namespace `public-mesh` on TCP port `8443`.
  3. Allows Egress ONLY to:
     - CoreDNS on port `53` (both UDP and TCP).
     - Database pods in the same namespace labeled `app=db` on TCP port `5432`.
* **Speed Formula:**
  ```yaml
  apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    name: protect-ledger
    namespace: finance
  spec:
    podSelector:
      matchLabels:
        app: ledger
    policyTypes:
    - Ingress
    - Egress
    - Ingress:
      - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: public-mesh
          podSelector:
            matchLabels:
              role: api-gateway
        ports:
        - protocol: TCP
          port: 8443
    egress:
    # 1. DNS Hole:
    - to: []
      ports:
      - protocol: UDP
        port: 53
      - protocol: TCP
        port: 53
    # 2. Database egress:
    - to:
      - podSelector:
          matchLabels:
            app: db
      ports:
      - protocol: TCP
        port: 5432
  ```

---

### 🔹 Question 12: Service Selector Debugging & Endpoints Verification
* **Directory:** `/home/karim/ckad-exam-lab/q12-service-selector/`
* **Domain:** Core Service Resolution & Endpoints
* **Problem Statement:**
  Deployment `web-app` runs pods with labels `app=webapp, tier=frontend`. Service `web-svc` exists, but client requests fail with `connection refused`.
  1. Inspect Service endpoints to identify the issue.
  2. Update Service `web-svc` selector so it correctly selects pods from `web-app`.
  3. Verify that the endpoints list updates with the active Pod IPs.
* **Speed Formula:**
  ```bash
  # 1. Check endpoints:
  kubectl get endpoints web-svc -n default   # Shows <none>

  # 2. Match selector:
  kubectl set selector service web-svc "app=webapp,tier=frontend" -n default

  # 3. Verify endpoints populated:
  kubectl get endpoints web-svc -n default
  ```

---

### 🔹 Question 13: NodePort Service Creation & Port Mapping
* **Directory:** `/home/karim/ckad-exam-lab/q13-nodeport-service/`
* **Domain:** Inbound Node Traffic Routing
* **Problem Statement:**
  In namespace `default`, Deployment `api-server` runs with label `app=api` and containerPort `9090`.
  1. Create a Service named `api-nodeport` of type `NodePort`.
  2. Select pods with `app=api`.
  3. Map Service port `80` to target port `9090`.
  4. Note the dynamically assigned NodePort (30000–32767).
* **Speed Formula:**
  ```bash
  kubectl expose deploy api-server \
    --name=api-nodeport \
    --type=NodePort \
    --port=80 \
    --target-port=9090 \
    -n default
  ```

---

### 🔹 Question 14A: Ingress Resource Path-Based Routing with Host Header
* **Directory:** `/home/karim/ckad-exam-lab/q14a-ingress-host/`
* **Approach:** Multi-path HTTP routing under a specific domain name.
* **Problem Statement:**
  In namespace `default`:
  - Service `web-svc` listens on port `8080`.
  - Service `api-svc` listens on port `9090`.
  Create an Ingress named `web-ingress` using `networking.k8s.io/v1`:
  - Host: `app.example.com`.
  - Path `/` routes to `web-svc:8080` with `pathType: Prefix`.
  - Path `/api` routes to `api-svc:9090` with `pathType: Prefix`.
* **Speed Formula:**
  ```bash
  kubectl create ingress web-ingress \
    --rule="app.example.com/=web-svc:8080" \
    --rule="app.example.com/api=api-svc:9090" \
    -n default
  ```

---

### 🔹 Question 14B: Ingress with TLS Certificate Termination
* **Directory:** `/home/karim/ckad-exam-lab/q14b-ingress-tls/`
* **Approach:** HTTPS encryption & certificate secret association (Contrasts with Q14A).
* **Problem Statement:**
  1. Create a TLS Secret named `secure-cert` in namespace `default` using certificate file `/root/tls.crt` and private key `/root/tls.key`.
  2. Create an Ingress named `secure-ingress` routing host `secure.example.com` to Service `auth-svc:443` with `pathType: Prefix`.
  3. Configure the `tls:` block to terminate HTTPS traffic for `secure.example.com` using Secret `secure-cert`.
* **Speed Formula:**
  ```bash
  # 1. Create TLS Secret:
  kubectl create secret tls secure-cert --cert=/root/tls.crt --key=/root/tls.key -n default

  # 2. Create Ingress:
  kubectl create ingress secure-ingress \
    --rule="secure.example.com/*=auth-svc:443,tls=secure-cert" \
    -n default
  ```

---

### 🔹 Question 15: Ingress PathType Syntax Correction
* **Directory:** `/home/karim/ckad-exam-lab/q15-ingress-pathtype/`
* **Domain:** Ingress Spec v1 Validation
* **Problem Statement:**
  File `/root/fix-ingress.yaml` fails to apply with error: `spec.rules[0].http.paths[0].pathType: Unsupported value: "InvalidType"`.
  1. Fix the `pathType` field to a valid Kubernetes v1 value (`Prefix`).
  2. Ensure the backend points to Service `api-svc` on port `8080`.
  3. Apply the fixed file and verify the Ingress is accepted by the API server.
* **Speed Formula:**
  ```yaml
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: api-ingress
    namespace: default
  spec:
    rules:
    - http:
        paths:
        - path: /api
          pathType: Prefix        # <-- Corrected from InvalidType
          backend:
            service:
              name: api-svc
              port:
                number: 8080
  ```

---

```
+---------------------------------------------------------------------------------------+
| DOMAIN 6: STORAGE & PERSISTENT VOLUMES (10%)                                         |
+---------------------------------------------------------------------------------------+
```

### 🔹 Question 19: PersistentVolume, PersistentVolumeClaim & Pod Mounting
* **Directory:** `/home/karim/ckad-exam-lab/q19-pv-pvc-pod/`
* **Domain:** Core State & Persistent Storage
* **Problem Statement:**
  1. Create a PersistentVolume `app-pv` with capacity `1Gi`, `accessModes: [ReadWriteOnce]`, `storageClassName: manual`, and `hostPath: /mnt/data`.
  2. Create a PersistentVolumeClaim `app-pvc` in namespace `default` requesting `1Gi`, `accessModes: [ReadWriteOnce]`, `storageClassName: manual`. Confirm status is `Bound`.
  3. Create a Pod `app-storage` running `nginx:latest`, mounting `app-pvc` at `/usr/share/nginx/html`.
* **Speed Formula:**
  ```yaml
  apiVersion: v1
  kind: PersistentVolume
  metadata:
    name: app-pv
  spec:
    capacity:
      storage: 1Gi
    accessModes:
      - ReadWriteOnce
    storageClassName: manual
    hostPath:
      path: /mnt/data
  ---
  apiVersion: v1
  kind: PersistentVolumeClaim
  metadata:
    name: app-pvc
    namespace: default
  spec:
    accessModes:
      - ReadWriteOnce
    storageClassName: manual
    resources:
      requests:
        storage: 1Gi
  ---
  apiVersion: v1
  kind: Pod
  metadata:
    name: app-storage
    namespace: default
  spec:
    containers:
    - name: web
      image: nginx:latest
      volumeMounts:
      - name: storage
        mountPath: /usr/share/nginx/html
    volumes:
    - name: storage
      persistentVolumeClaim:
        claimName: app-pvc
  ```

---

### 🔹 Question 20: PersistentVolumeClaim Online Volume Expansion
* **Directory:** `/home/karim/ckad-exam-lab/q20-pvc-expansion/`
* **Domain:** StorageClass Capabilities & Dynamic Resizing
* **Problem Statement:**
  In namespace `data-tier`, an active database uses PersistentVolumeClaim `db-data` currently sized at `1Gi`. The underlying StorageClass supports `allowVolumeExpansion: true`.
  1. Expand the PVC capacity from `1Gi` to `2Gi` without restarting or deleting the running Pod.
  2. Verify that `kubectl get pvc -n data-tier` reflects `2Gi`.
* **Speed Formula:**
  ```bash
  # 1. Edit PVC:
  kubectl edit pvc db-data -n data-tier
  # Change: spec.resources.requests.storage: 2Gi

  # 2. Verify:
  kubectl get pvc db-data -n data-tier
  ```

---

## 🚀 Hands-On Practice Protocol on Your Ubuntu VM

Run these commands on your VM to practice with the `ckad` CLI helper:

```bash
# 1. List all 20 scenarios:
ckad list

# 2. Start a scenario (injects broken state & prints exam instructions):
ckad start 1

# 3. Solve the task using speed formulas, then check your score:
ckad check 1

# 4. View official solution if stuck:
ckad solve 1

# 5. Clean up for repetition drills:
ckad undo 1
```
