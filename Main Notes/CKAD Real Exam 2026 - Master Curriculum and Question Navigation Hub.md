---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: master-curriculum-hub
domains:
  - kubernetes
  - application-developer
  - ckad
related_concepts:
  - "[[CKA Certification Real Exam 2026 - Master Curriculum and Question Navigation Hub]]"
  - "[[CKS Real Exam 2026 - Master Curriculum and Question Navigation Hub]]"
against: []
reference_guides:
  - "[[Reference Notes/8-1_application_design_and_build.md]]"
  - "[[Reference Notes/8-2_application_deployment.md]]"
tags:
  - kubernetes/ckad
  - kubernetes/exam-prep
  - kubernetes/curriculum-map
  - status/completed
---

# 🚀 CKAD Master Curriculum & Knowledge Directory: What's Inside Every Note
**Comprehensive Exam Blueprint, Domain Mappings, and Paired Question Alignments**

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Master Index]] > **CKAD Master Curriculum & Knowledge Directory**

---

## 🎯 Purpose of This Knowledge Directory

The **Certified Kubernetes Application Developer (CKAD)** exam tests your ability to design, build, configure, deploy, and troubleshoot cloud-native applications on Kubernetes under extreme time pressure (120 minutes for 15–17 performance scenarios).

This directory maps every foundational concept, architectural pattern, YAML schema, and speed shortcut into the **5 Official CKAD Exam Curriculum Domains**.

For each section, you will find:
1. **Core Architectural Insights:** The fundamental mechanics behind the Kubernetes primitive.
2. **Speed Run CLI Formulas:** Imperative one-liners and dry-run tricks to generate YAML in seconds.
3. **Paired Approach Matrix:** Contrasting similar questions that require different approaches (e.g. Canary vs. Blue/Green, Secret keyRef vs. bulk envFrom, Liveness exec vs. Readiness HTTP).
4. **Exam Scenario Alignment:** Direct mapping to the 20 simulation lab scenarios in [[Projects/CKAD/Real Exam 2026 - 20 Question Simulation Lab Guide|Real Exam 2026 - 20 Question Simulation Lab Guide]].

---

```
===================================================================================================
                                CKAD CURRICULUM ARCHITECTURE AT A GLANCE
===================================================================================================

  [ Domain 1: Application Design & Build (20%) ] ──────► OCI Images, Multi-Container, Jobs & CronJobs
            │
            ├──► [ Domain 2: Application Deployment (20%) ] ──► Rollouts, Canary, Blue/Green, Helm
            │
            ├──► [ Domain 3: Observability & Maintenance (15%) ] ──► Liveness/Readiness, Top, Logs
            │
            ├──► [ Domain 4: Environment, Config & Security (25%) ] ──► Secrets, CMs, RBAC, SecurityContext, Quotas
            │
            └──► [ Domain 5: Services & Networking (20%) ] ──► Services, Endpoints, NetworkPolicies, Ingress v1
===================================================================================================
```

---

## 📦 DOMAIN 1: Application Design and Build (20%)

This domain focuses on designing, building, and running application workloads, container packaging, multi-container pod communication, and batch controllers.

### 1. Container Image Building & Registry Exports (Podman / Docker)
* **What's Inside:**
  - OCI build mechanics: layers, context directories, Dockerfile directives (`FROM`, `RUN`, `COPY`, `CMD`, `ENTRYPOINT`).
  - Building container images locally without a remote registry:
    ```bash
    podman build -t my-app:1.0 /root/app-source
    ```
  - Exporting container images as flat `.tar` archives for offline deployment:
    ```bash
    podman save -o /root/my-app.tar my-app:1.0
    ```
* **Exam Scenario Alignment:** **Question 05 (`q05-podman-build`)** — Building and archiving images with Podman.

---

### 2. Multi-Container Pod Patterns (Sidecar, Adapter, Ambassador)
* **What's Inside:**
  - Container co-location within a shared network and storage namespace.
  - **The Logging Sidecar Pattern:** Main application container appends raw logs to an `emptyDir` in-memory volume; sidecar streaming agent tails and formats the log stream for external log collectors.
  - **InitContainers:** Synchronous sequential gates that run to completion before app containers start (e.g. waiting for database socket availability via `nc -z`).
* **Exam Scenario Alignment:** **Question 17 (`q17-sidecar-logging`)** — Multi-container logging sidecar.

---

### 3. Jobs and CronJobs (Batch Execution & Scheduling)
* **What's Inside:**
  - CronJob schedule expressions (`minute hour day-of-month month day-of-week`).
  - Essential operational controls:
    - `activeDeadlineSeconds`: Hard execution ceiling preventing orphaned hanging jobs.
    - `successfulJobsHistoryLimit` & `failedJobsHistoryLimit`: Housekeeping limits preventing etcd object bloat.
    - `restartPolicy: Never` vs `OnFailure`.
  - **The Paired Approach:**
    - **Variant A (Recurring Schedule):** Configuring full CronJob specs with retention limits (**Question 02A**).
    - **Variant B (On-Demand Execution):** Instant testing by creating a Job directly from a CronJob (`kubectl create job --from=cronjob/<name>`) and multi-pod parallel processing (`completions`, `parallelism`) (**Question 02B**).
* **Exam Scenario Alignment:** **Question 02A (`q02a-cronjob-limits`)** & **Question 02B (`q02b-job-ondemand`)**.

---

## 🚢 DOMAIN 2: Application Deployment (20%)

This domain covers managing stateless application lifecycles, rollout strategies, rolling updates, and zero-downtime release models.

### 1. Rolling Updates, Revisions & Automated Rollbacks
* **What's Inside:**
  - Rolling update parameters: `maxSurge` (temporary capacity headroom) and `maxUnavailable` (allowable capacity drop).
  - Updating container images imperatively:
    ```bash
    kubectl set image deploy/<name> <container>=<image>
    ```
  - Inspecting rollout progression and history:
    ```bash
    kubectl rollout status deploy/<name>
    kubectl rollout history deploy/<name>
    ```
  - Performing targeted instant rollbacks:
    ```bash
    kubectl rollout undo deploy/<name> --to-revision=1
    ```
* **Exam Scenario Alignment:** **Question 09 (`q09-rolling-update`)** — Live rolling update, inspection, and rollback.

---

### 2. Advanced Release Strategies: Canary vs. Blue/Green Deployments
* **What's Inside:**
  - **The Paired Approach:**
    - **Canary Strategy (Proportional Routing):** Two concurrent Deployments share the exact same `app` label targeted by a Service, but have distinct `version` labels. Traffic is distributed purely based on the ratio of replicas (e.g., 8 baseline pods vs. 2 canary pods = 80/20 split) (**Question 06A**).
    - **Blue/Green Strategy (Instant Cutover):** Both `app-blue` and `app-green` run full replica sets simultaneously in production. The Service selector is updated atomically to switch all live traffic instantly to the green version (`kubectl set selector svc ...`), enabling instant rollback if errors occur (**Question 06B**).
* **Exam Scenario Alignment:** **Question 06A (`q06a-canary-deployment`)** & **Question 06B (`q06b-bluegreen-cutover`)**.

---

### 3. API Version Deprecation & Schema Migration
* **What's Inside:**
  - Upgrading legacy API versions to stable GA groups:
    - Deployments: `extensions/v1beta1` -> `apps/v1` (requiring mandatory `spec.selector.matchLabels`).
    - Ingress: `extensions/v1beta1` -> `networking.k8s.io/v1` (syntax changes to `service.name`, `service.port.number`, and `pathType`).
    - CronJobs: `batch/v1beta1` -> `batch/v1`.
* **Exam Scenario Alignment:** **Question 08A (`q08a-api-deployment`)** — Resolving broken deprecated schemas.

---

## 🔍 DOMAIN 3: Application Observability and Maintenance (15%)

This domain covers container health checks, diagnostic metrics, log extraction, and troubleshooting unhealthy pods.

### 1. Health Probes: Liveness vs. Readiness vs. Startup
* **What's Inside:**
  - **The Paired Approach:**
    - **Readiness Probes (Traffic Gate):** If a readiness probe fails, Kubernetes leaves the container running but removes its Pod IP from all Service endpoints, shielding clients from uninitialized backends (**Question 10A**).
    - **Liveness Probes (Process Lifecyle):** If a liveness probe fails, Kubelet actively terminates and restarts the container, recovering from unhandled deadlocks (**Question 10B**).
  - Probe handler mechanisms:
    - `httpGet`: HTTP GET requests expecting status code 200–399.
    - `exec`: Running commands inside the container expecting return code 0.
    - `tcpSocket`: Attempting TCP handshakes on specified ports.
* **Exam Scenario Alignment:** **Question 10A (`q10a-readiness-probe`)** & **Question 10B (`q10b-liveness-exec`)**.

---

### 2. Metrics & Log Forensics (Metrics Server & kubectl Logs)
* **What's Inside:**
  - Querying live resource utilization with Metrics Server:
    ```bash
    kubectl top pods -n <ns> --sort-by=cpu --no-headers
    ```
  - Filtering multi-container and streaming logs:
    ```bash
    kubectl logs <pod> -c <container> | grep "ERROR" > /opt/errors.log
    kubectl logs <pod> --previous   # Crucial for crashed containers!
    ```
* **Exam Scenario Alignment:** **Question 18 (`q18-observability-logs`)** — Top pods extraction and log filtering.

---

### 3. Resource Sizing & Bottleneck Troubleshooting
* **What's Inside:**
  - **The Paired Approach:**
    - **Forward Calculation (ResourceQuota):** Reading namespace quotas and provisioning pods with mathematically derived fractions of limits (**Question 16A**).
    - **Reverse Troubleshooting (Pending Pods):** Diagnosing pods stuck in `Pending` due to `0/2 nodes available: Insufficient memory`, inspecting node allocatable memory, and right-sizing specifications (**Question 16B**).
* **Exam Scenario Alignment:** **Question 16A (`q16a-resource-quota`)** & **Question 16B (`q16b-troubleshoot-pending`)**.

---

## 🔒 DOMAIN 4: Application Environment, Configuration and Security (25%)

This domain represents the highest weight in CKAD. It covers configuration injection, RBAC identity, and Linux security contexts.

### 1. Configuration & Secret Injection (Selective vs. Bulk)
* **What's Inside:**
  - **The Paired Approach:**
    - **Selective Binding (`valueFrom`):** Mapping specific keys from Secrets/ConfigMaps to explicit environment variable names (**Question 01A**).
    - **Bulk Injection (`envFrom`):** Injecting all key-value pairs from a ConfigMap or Secret into a container environment in a single directive (**Question 01B**).
    - **Volume Projections:** Projecting ConfigMaps or Secrets as read-only files mounted into container directory paths.
* **Exam Scenario Alignment:** **Question 01A (`q01a-secret-keyref`)** & **Question 01B (`q01b-configmap-envfrom`)**.

---

### 2. RBAC Diagnostics & Authorization Gating
* **What's Inside:**
  - Reading pod authorization failures from logs (`User cannot list pods in namespace`).
  - Generating RBAC primitives imperatively:
    ```bash
    kubectl create sa log-sa -n audit
    kubectl create role log-role --verb=get,list,watch --resource=pods -n audit
    kubectl create rolebinding log-rb --role=log-role --serviceaccount=audit:log-sa -n audit
    ```
  - **Pod Immutability Trap:** `serviceAccountName` cannot be patched on existing Pods. You must export (`-o yaml > p.yaml`), delete (`--force --grace-period=0`), and recreate.
  - **Namespace vs. Cluster Delegation:** Binding a `ClusterRole` using a namespace-scoped `RoleBinding` to grant permissions exclusively inside that namespace.
* **Exam Scenario Alignment:** **Question 03A (`q03a-rbac-logs`)**, **Question 03B (`q03b-rbac-cluster`)**, & **Question 04 (`q04-rbac-pod-fix`)**.

---

### 3. SecurityContexts: User IDs, Capabilities & Immutability
* **What's Inside:**
  - **The Paired Approach:**
    - **User ID & Capabilities:** Setting Pod-level `runAsUser: 1000` combined with Container-level `capabilities: add: [NET_ADMIN]` (**Question 11A**).
    - **Immutability & Scratch Mounts:** Setting `readOnlyRootFilesystem: true` combined with an `emptyDir` scratch mount for writable cache directories (`/tmp`) (**Question 11B**).
* **Exam Scenario Alignment:** **Question 11A (`q11a-security-context`)** & **Question 11B (`q11b-readonly-rootfs`)**.

---

## 🌐 DOMAIN 5: Services and Networking (20%)

This domain covers East-West cluster communication, North-South ingress routing, and network microsegmentation.

### 1. Services, Selectors & Endpoint Resolution
* **What's Inside:**
  - Service resolution mechanics: How `spec.selector` maps to dynamically managed `Endpoints` (`Endpoints` and `EndpointSlices`).
  - Diagnosing broken connections: When `kubectl get endpoints <svc>` returns `<none>`, the issue is always a label mismatch between the Service selector and the Pod template labels.
  - Exposing NodePorts imperatively:
    ```bash
    kubectl expose deploy <name> --name=<svc-name> --type=NodePort --port=80 --target-port=8080
    ```
* **Exam Scenario Alignment:** **Question 12 (`q12-service-selector`)** & **Question 13 (`q13-nodeport-service`)**.

---

### 2. NetworkPolicies: Remediation vs. Greenfield Authoring
* **What's Inside:**
  - **The Paired Approach:**
    - **Label Remediation:** When policies are immutable, modifying Pod labels via `kubectl label pod <name> key=val --overwrite` to satisfy the active firewall rules (**Question 07A**).
    - **Greenfield Policy Authoring:** Writing complete YAML specifications from scratch with default-deny, `namespaceSelector` + `podSelector` combinations, and mandatory egress holes for CoreDNS (UDP/TCP port 53) (**Question 07B**).
* **Exam Scenario Alignment:** **Question 07A (`q07a-netpol-labels`)** & **Question 07B (`q07b-netpol-authoring`)**.

---

### 3. Ingress Routing & PathType v1 Standards
* **What's Inside:**
  - **The Paired Approach:**
    - **Host and Multi-Path Routing:** Routing traffic for domain names across multiple backend microservices based on URL prefixes (**Question 14A**).
    - **TLS Secret Termination:** Binding an SSL/TLS certificate Secret to an Ingress `spec.tls` array (**Question 14B**).
    - **PathType Syntax Correction:** Fixing invalid values (`InvalidType` -> `Prefix`, `Exact`, `ImplementationSpecific`) (**Question 15**).
* **Exam Scenario Alignment:** **Question 14A (`q14a-ingress-host`)**, **Question 14B (`q14b-ingress-tls`)**, & **Question 15 (`q15-ingress-pathtype`)**.

---

## 💾 DOMAIN 6: Storage (Persistent Volumes & Volume Claims) (10%)

### 1. PV, PVC & Pod Mount Integration
* **What's Inside:**
  - The Storage binding triangle: PersistentVolume (`capacity`, `accessModes`, `storageClassName`, `hostPath`) -> PersistentVolumeClaim (`requests.storage`, matching `accessModes`, matching `storageClassName`) -> Pod (`volumes.persistentVolumeClaim.claimName`).
  - Dynamic Volume Expansion: Editing PVCs in-place (`spec.resources.requests.storage: 2Gi`) on StorageClasses with `allowVolumeExpansion: true`.
* **Exam Scenario Alignment:** **Question 19 (`q19-pv-pvc-pod`)** & **Question 20 (`q20-pvc-expansion`)**.

---

## 🔗 Related Master Notes & Navigation
- Full 20-Question Lab Guide: [[Projects/CKAD/Real Exam 2026 - 20 Question Simulation Lab Guide|Real Exam 2026 - 20 Question Simulation Lab Guide]]
- Master Hub: [[Main Notes/0-Index|🏠 Master Second Brain Index]]
- CKS Curriculum Hub: [[Main Notes/CKS Real Exam 2026 - Master Curriculum and Question Navigation Hub|CKS Master Curriculum & Knowledge Directory]]
