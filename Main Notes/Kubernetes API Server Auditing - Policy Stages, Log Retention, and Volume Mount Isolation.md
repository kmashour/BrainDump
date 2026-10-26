---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Runtime Security and Threat Forensics]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Workload Hardening"
tags:
  - kubernetes/security
  - kubernetes/auditing
  - kubernetes/api-server
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes API Server Auditing: Policy Stages, Log Retention, and Volume Mount Isolation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Main Notes/Kubernetes Runtime Security and Threat Forensics|Kubernetes Runtime Security and Threat Forensics]] > **Kubernetes API Server Auditing: Policy Stages, Log Retention, and Volume Mount Isolation**

---

## 🏛️ 1. Architectural Foundations: The API Audit Pipeline

While kernel trace engines like Falco intercept low-level Linux syscalls, malicious actors and compromised accounts frequently perform attacks using legitimate Kubernetes REST APIs (e.g., extracting secrets, tampering with RBAC roles, deleting deployments).

The **Kubernetes API Server Auditing Engine** provides a chronological, tamper-evident record of all operations processed by `kube-apiserver`.

```
+-----------------------------------------------------------------------------------+
|                        KUBERNETES API AUDITING PIPELINE                           |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  Client (kubectl / ServiceAccount)                                                |
|         │                                                                         |
|         ▼ HTTPS REST Request                                                      |
|  [ kube-apiserver ]                                                               |
|         │                                                                         |
|         ├──► 1. Authentication (Identity resolution)                              |
|         ├──► 2. Authorization (RBAC evaluation)                                   |
|         │                                                                         |
|         ├──► 3. [ Audit Policy Filter: /etc/kubernetes/audit/policy.yaml ]        |
|         │       - Evaluates rules TOP-TO-BOTTOM.                                  |
|         │       - First matching rule determines Audit Level.                     |
|         │                                                                         |
|         ├──► 4. Admission Control (Validating / Mutating)                         |
|         │                                                                         |
|         └──► 5. [ Audit Sink: /var/log/kubernetes/audit/audit.log ]               |
|                 - Writes JSON structured event records                            |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

---

## 🎚️ 2. The Four Audit Levels & The "Plaintext Secret" Trap

Every request entering the pipeline is evaluated by the policy filter and assigned one of four distinct logging levels:

```
+---------------------------------------------------------------------------------------------------+
|                                     KUBERNETES AUDIT LEVELS                                       |
+---------------------------------------------------------------------------------------------------+
| LEVEL             | WHAT IT LOGS                                     | TYPICAL USE CASE           |
+-------------------+--------------------------------------------------+----------------------------+
| None              | Nothing. Zero log events written.                | High-frequency health      |
|                   |                                                  | probes (endpoints, leases).|
+-------------------+--------------------------------------------------+----------------------------+
| Metadata          | User, timestamp, verb, resource, namespace,      | High-volume resources,     |
|                   | response HTTP status code. (NO payloads).        | secrets, configmaps.       |
+-------------------+--------------------------------------------------+----------------------------+
| Request           | Metadata PLUS the full request JSON body.        | Auditing mutations on      |
|                   | (Omits the response body).                       | production deployments.    |
+-------------------+--------------------------------------------------+----------------------------+
| RequestResponse   | Metadata PLUS request body PLUS response body.   | Sensitive administrative   |
|                   | (Highest CPU and storage overhead).              | investigations.            |
+---------------------------------------------------------------------------------------------------+
```

> [!CAUTION]
> **The Plaintext Secret Disaster:**
> NEVER configure `Request` or `RequestResponse` on `secrets` or `configmaps`!
> If you log `RequestResponse` for `secrets`, base64-encoded passwords, tokens, and private keys will be dumped in cleartext into `/var/log/kubernetes/audit/audit.log` on the host control plane disk. Secrets must **always** be audited at `level: Metadata`.

### ⚡ The Architectural Paradox: Why etcd Encryption CANNOT Protect Audit Logs
A critical architectural question arises:  
*If a cluster has military-grade Secret Encryption at Rest (e.g. `aescbc` or AWS KMS) enabled for `etcd`, does setting `level: RequestResponse` on secrets still expose them in cleartext?*

**YES! 100% YES.** It will completely expose the secrets in cleartext (base64) on the host filesystem.

The reason lies in the **chronological execution pipeline** inside `kube-apiserver`:

```
+-----------------------------------------------------------------------------------+
|                        INSIDE THE kube-apiserver PIPELINE                         |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  Client executes: kubectl create secret generic db-pass --from-literal=p=Secret123|
|         │                                                                         |
|         ▼                                                                         |
|  1. Authentication & Authorization (RBAC passes)                                  |
|         │                                                                         |
|         ▼                                                                         |
|  2. [ API AUDIT LOGGING ENGINE RUNS HERE! (REST Layer) ]                          |
|         │                                                                         |
|         ├──► Captures raw API input: {"data": {"p": "U2VjcmV0MTIz"}}              |
|         │                                                                         |
|         └──► WRITES TO DISK: /var/log/kubernetes/audit/audit.log                  |
|              💥 THE BASE64 SECRET IS NOW SAVED ON DISK IN CLEAR TEXT!             |
|                                                                                   |
|  ===============================================================================  |
|                                                                                   |
|  3. Admission Controllers (Validating, Mutating, PSA)                             |
|         │                                                                         |
|         ▼                                                                         |
|  4. [ ENCRYPTION AT REST PROVIDER RUNS HERE! (Storage Layer) ]                    |
|         │                                                                         |
|         ├──► Encrypts bytes using AES-CBC / KMS: "k8s:enc:aescbc:v1:key1:..."     |
|         │                                                                         |
|         ▼                                                                         |
|  5. Saved to etcd Database: /var/lib/etcd (Ciphertext)                            |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

- **Encryption at Rest** operates at the **Storage Layer** (right before writing bytes to `etcd`).
- **Audit Logging** operates at the **REST API Layer** (when the request enters and exits `kube-apiserver`).
- Therefore, the audit engine writes the unencrypted API payload to disk **long before the storage encryption engine is ever invoked**! An attacker with node read access can bypass encrypted `etcd` entirely by scraping `/var/log/kubernetes/audit/audit.log`.

---


## 💾 3. Volume Permissions: Read-Only vs. Writable Isolation

When integrating the audit engine into the `kube-apiserver` static pod, candidates frequently cause catastrophic crash-loops by misunderstanding volume permissions:

```
+-----------------------------------------------------------------------------------+
|                        VOLUME MOUNT PERMISSIONS BREAKDOWN                         |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ kube-apiserver Container ]                                                     |
|         │                                                                         |
|         ├──► 1. Mount: /etc/kubernetes/audit (Holds policy.yaml)                  |
|         │       Permission: readOnly: true                                        |
|         │       Rationale: The API server only reads configuration rules.         |
|         │       It should never mutate policy files on disk.                      |
|         │                                                                         |
|         └──► 2. Mount: /var/log/kubernetes/audit (Holds audit.log)                |
|                 Permission: readOnly: false  <--- MUST BE WRITABLE!               |
|                 Rationale: The API server actively writes log event streams.      |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### The Read-Only Crash Loop Failure:
If an administrator copies the volumeMount block and accidentally leaves `readOnly: true` on the log directory:
```yaml
# ❌ FATAL CONFIGURATION:
- mountPath: /var/log/kubernetes/audit
  name: audit-log
  readOnly: true # <--- CRASHES KUBE-APISERVER
```
When `kube-apiserver` boots, it invokes `open("/var/log/kubernetes/audit/audit.log", O_WRONLY|O_CREAT|O_APPEND)`.
The Linux kernel denies the syscall with `EROFS: Read-only file system`. The API server panics, terminates, and `kubectl` returns `connection refused`.

---

## 🔄 4. Log Rotation & Retention: Preventing Disk Exhaustion

Because `kube-apiserver` processes thousands of API events per minute, unmanaged audit logs can rapidly consume all available disk space in `/var`. If the host disk fills to 100%, **`etcd` database writes fail and the entire cluster enters a permanent freeze**.

To mitigate disk exhaustion, Kubernetes provides two retention guardrails:

```
+---------------------------------------------------------------------------------------------------+
|                                    AUDIT LOG RETENTION FLAGS                                      |
+---------------------------------------------------------------------------------------------------+
| FLAG                    | VALUE      | MEANING & RETENTION LIFECYCLE                              |
+-------------------------+------------+------------------------------------------------------------+
| --audit-log-maxage=10   | 10 Days    | TIME-BASED PURGE:                                          |
|                         |            | The maximum number of DAYS to retain old audit files.      |
|                         |            | Files older than 10 days are deleted automatically.        |
+-------------------------+------------+------------------------------------------------------------+
| --audit-log-maxbackup=2 | 2 Files    | COUNT-BASED PURGE:                                         |
|                         |            | The maximum number of ROTATED ARCHIVES to retain.          |
|                         |            | Preserves the active log + up to 2 historical backups.    |
|                         |            | Creating a 3rd archive triggers deletion of the oldest.    |
+-------------------------+------------+------------------------------------------------------------+
```

### Physical Rotation Lifecycle:
When the active log file reaches its size limit (governed by `--audit-log-maxsize`, default 100 MB), log rotation triggers:
```
Day 1:
/var/log/kubernetes/audit/audit.log                      <-- Active file

Day 2 (Rotation):
/var/log/kubernetes/audit/audit.log                      <-- New active file
/var/log/kubernetes/audit/audit-2026-10-08T02-15-32.log  <-- Backup 1 (Preserved)

Day 3 (Rotation):
/var/log/kubernetes/audit/audit.log                      <-- New active file
/var/log/kubernetes/audit/audit-2026-10-09T02-15-32.log  <-- Backup 1 (Preserved)
/var/log/kubernetes/audit/audit-2026-10-08T02-15-32.log  <-- Backup 2 (Preserved)

Day 4 (Rotation):
/var/log/kubernetes/audit/audit.log                      <-- New active file
/var/log/kubernetes/audit/audit-2026-10-10T02-15-32.log  <-- Backup 1 (Preserved)
/var/log/kubernetes/audit/audit-2026-10-09T02-15-32.log  <-- Backup 2 (Preserved)
# Archive from Oct 08 is DELETED because --audit-log-maxbackup=2!

Day 12:
# Any archive older than 10 days is DELETED because --audit-log-maxage=10!
```

---

## 🎯 5. Real Exam Question 06: End-to-End Walkthrough

### Scenario
Configure the API Server audit logging engine:
1. Create `/etc/kubernetes/audit/policy.yaml`:
   - Stage 1: `namespaces` at `Metadata`.
   - Stage 2: `deployments` in namespace `prod` at `Request`.
   - Stage 3: `secrets` and `configmaps` at `Metadata`.
   - Stage 4: Catch-all at `Metadata`.
2. Configure `/etc/kubernetes/manifests/kube-apiserver.yaml` with:
   - `--audit-log-path=/var/log/kubernetes/audit/audit.log`
   - `--audit-policy-file=/etc/kubernetes/audit/policy.yaml`
   - `--audit-log-maxage=10`
   - `--audit-log-maxbackup=2`
3. Configure `hostPath` volumes and `volumeMounts` for `/etc/kubernetes/audit` and `/var/log/kubernetes/audit`.
4. Ensure the API server restarts cleanly.

---

### Step-by-Step Exam Execution

#### Step 1: Create Directories and Policy Manifest
```bash
sudo mkdir -p /etc/kubernetes/audit
sudo mkdir -p /var/log/kubernetes/audit
sudo vi /etc/kubernetes/audit/policy.yaml
```

```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  # Stage 1: namespaces at Metadata
  - level: Metadata
    resources:
      - group: ""
        resources: ["namespaces"]

  # Stage 2: deployments in namespace prod at Request
  - level: Request
    resources:
      - group: "apps"
        resources: ["deployments"]
    namespaces: ["prod"]

  # Stage 3: secrets and configmaps at Metadata (Never log body!)
  - level: Metadata
    resources:
      - group: ""
        resources: ["secrets", "configmaps"]

  # Stage 4: Catch-all at Metadata
  - level: Metadata
    omitStages:
      - RequestReceived
```

---

#### Step 2: Edit `kube-apiserver.yaml` Static Pod
Open `/etc/kubernetes/manifests/kube-apiserver.yaml`:
```bash
sudo vi /etc/kubernetes/manifests/kube-apiserver.yaml
```

**1. Add Audit CLI Arguments:**
```yaml
spec:
  containers:
  - command:
    - kube-apiserver
    - --audit-log-path=/var/log/kubernetes/audit/audit.log
    - --audit-policy-file=/etc/kubernetes/audit/policy.yaml
    - --audit-log-maxage=10
    - --audit-log-maxbackup=2
```

**2. Add Container `volumeMounts`:**
```yaml
    volumeMounts:
    - mountPath: /etc/kubernetes/audit
      name: audit-policy
      readOnly: true
    - mountPath: /var/log/kubernetes/audit
      name: audit-log
      readOnly: false # Writable for logging!
```

**3. Add Host `volumes`:**
```yaml
  volumes:
  - name: audit-policy
    hostPath:
      path: /etc/kubernetes/audit
      type: DirectoryOrCreate
  - name: audit-log
    hostPath:
      path: /var/log/kubernetes/audit
      type: DirectoryOrCreate
```

Save and exit (`:wq`).

---

#### Step 3: API Server Recovery & Crash Diagnosis
Wait for Kubelet to restart `kube-apiserver`. Verify cluster responsiveness:
```bash
kubectl get nodes
```

> [!WARNING]
> **Crash Recovery Protocol: The Two Failure Categories**
> 
> **Category 1: Container Crashes (API Server binary fails at runtime)**
> If the manifest is valid YAML but flags or mounts have issues (e.g. wrong flag name, wrong policy path):
> ```bash
> sudo crictl ps -a --name kube-apiserver
> sudo crictl logs <container-id>
> ```
> 
> **Category 2: The Manifest Parsing Trap (Zero Containers Created!)**
> If `sudo crictl ps -a --name kube-apiserver` returns **completely empty**, Kubelet failed to parse the YAML file before ever calling containerd!
> 
> **The #1 Culprit — Indentation of `volumes:`:**
> If `volumes:` is placed at column 0 (root level) instead of being indented under `spec:` (2 spaces):
> - Kubelet parses `spec.volumes` as completely empty.
> - Every `volumeMount` in `spec.containers[0].volumeMounts` (including default `ca-certs`, `k8s-certs`, etc.) throws a `"Not found"` error!
> - Inspect Kubelet journal logs immediately:
>   ```bash
>   sudo journalctl -u kubelet -n 30 --no-pager
>   ```
> - **Look for:** `err="invalid pod: [spec.containers[0].volumeMounts[0].name: Not found: \"ca-certs\" ...]"`
> - **The Fix:** Indent `volumes:` and all its volume entries by 2 spaces so they reside under `spec:`.

---

#### Step 4: Verification of Emitted Audit Stream
Tail the audit stream in real time and inspect JSON structured output:
```bash
sudo tail -f /var/log/kubernetes/audit/audit.log | jq .
```
*(Confirms that API interactions emit structured audit events containing user identity, URI, HTTP verb, and response code)*.

---

## 🔗 Related Master Notes & References
- Parent Landing Note: [[Main Notes/Kubernetes Runtime Security and Threat Forensics|Kubernetes Runtime Security and Threat Forensics]]
- Threat Detection: [[Main Notes/Kubernetes Runtime Threat Detection - Falco eBPF Mechanics, dev mem Memory Scraping, and Rogue Pod Remediation|Runtime Threat Detection: Falco eBPF Mechanics & /dev/mem]]
- Control Plane Security: [[Main Notes/Kubernetes API Server Security - Request Lifecycle, NodeRestriction, and Protected Namespaces|API Server Security, NodeRestriction & Protected Namespaces]]
- Reference Guide: [[Reference Notes/0-7-6_runtime_security_falco_and_audit_logging.md|Module 0-7-6: Runtime Security, Syscall Threat Detection & API Auditing Masterclass]]
