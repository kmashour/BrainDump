---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Pod Security and Policy Engines]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Workload Hardening"
tags:
  - kubernetes/security
  - kubernetes/psa
  - kubernetes/pod-security
  - kubernetes/admission-control
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Pod Security Admission: Restricted Standards, Pod Creation Control Flow, and ReplicaSet Debugging

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Main Notes/Kubernetes Pod Security and Policy Engines|Kubernetes Pod Security and Policy Engines]] > **Kubernetes Pod Security Admission: Restricted Standards, Pod Creation Control Flow, and ReplicaSet Debugging**

---

## 🎯 1. Architectural Evolution: From PSP to PSS/PSA

In Kubernetes versions prior to v1.25, workload admission security was governed by **PodSecurityPolicies (PSP)**. PSP suffered from severe architectural flaws:
1. **Implicit & Unpredictable RBAC Binding:** PSP applied to workloads based on the identity (`ServiceAccount` or user) that created the pod. If a controller created a pod under `system:serviceaccount:kube-system`, it could inherit a permissive PSP inadvertently.
2. **Mutating Race Conditions:** PSP could mutate pods on the fly (adding default capabilities, altering UIDs). When multiple PSPs matched, the selection order was non-deterministic, creating configuration drift.
3. **Cluster Lockout Risk:** A single misconfigured PSP could lock down the cluster control plane and prevent critical daemonsets or system pods from scheduling.

Kubernetes deprecated PSP in v1.21 and completely removed it in v1.25, replacing it with a decoupled, declarative architecture:
* **Pod Security Standards (PSS):** An opinionated, vendor-neutral security specification defining three static security levels (`Privileged`, `Baseline`, `Restricted`).
* **Pod Security Admission (PSA):** A built-in admission controller inside `kube-apiserver` that evaluates incoming pod manifests against namespace-level labels. PSA is **strictly non-mutating** (it validates and admits or rejects, but never silently rewrites manifests).

---

## 🏛️ 2. The Three Security Tiers and Three Admission Modes

### The Three PSS Tiers

```
+---------------------------------------------------------------------------------------------------+
|                               POD SECURITY STANDARDS (PSS) TIERS                                  |
+---------------------------------------------------------------------------------------------------+
| TIER         | SCOPE & INTENT                             | ALLOWED CAPABILITIES & PRIVILEGES     |
+--------------+--------------------------------------------+---------------------------------------+
| Privileged   | Completely open; zero restrictions.        | privileged: true, hostPID, hostPath,  |
|              | Intended for system daemons, CNI plugins.  | all capabilities, raw devices.        |
+--------------+--------------------------------------------+---------------------------------------+
| Baseline     | Prevents known privilege escalations;      | hostPath forbidden, host namespaces   |
|              | default out-of-the-box security posture.   | blocked; allows root UID and default  |
|              | Minimal configuration burden.              | Linux capabilities.                   |
+--------------+--------------------------------------------+---------------------------------------+
| Restricted   | Hardened security posture following        | Non-root UID required, drop ALL caps, |
|              | modern workload isolation best practices.  | allowPrivilegeEscalation=false,       |
|              | Heavy configuration requirements.          | RuntimeDefault seccomp profile.       |
+--------------+--------------------------------------------+---------------------------------------+
```

### The Three PSA Enforcement Modes

Each namespace can independently define up to three enforcement modes via Kubernetes labels:

```
+---------------------------------------------------------------------------------------------------+
|                                   PSA ADMISSION MODES (LABELS)                                    |
+---------------------------------------------------------------------------------------------------+
| MODE     | LABEL SYNTAX                             | ACTION ON VIOLATION                         |
+----------+------------------------------------------+---------------------------------------------+
| enforce  | pod-security.kubernetes.io/enforce       | HARD REJECT: Blocks pod creation HTTP 403.  |
+----------+------------------------------------------+---------------------------------------------+
| audit    | pod-security.kubernetes.io/audit         | SILENT LOG: Records audit event in API log. |
+----------+------------------------------------------+---------------------------------------------+
| warn     | pod-security.kubernetes.io/warn          | SOFT WARNING: Prints warning banner to CLI. |
+----------+------------------------------------------+---------------------------------------------+
```

Each mode also supports version pinning (`pod-security.kubernetes.io/<mode>-version: v1.30` or `latest`) to prevent newer Kubernetes release standards from breaking older stable workloads upon cluster upgrades.

---

## ⚡ 3. The Control Flow of Pod Creation & The "Silent ReplicaSet" Trap

Understanding why workloads fail when PSA is applied requires dissecting the asynchronous distributed control flow between `kubectl`, the `kube-apiserver`, controllers, and `etcd`.

### The Step-by-Step Control Flow

```
+---------------------------------------------------------------------------------------------------------------+
|                        POD CREATION & POD SECURITY ADMISSION CONTROL FLOW                                     |
+---------------------------------------------------------------------------------------------------------------+
|                                                                                                               |
|  [ Engineer / CI/CD ]                                                                                         |
|         │                                                                                                     |
|         │ 1. kubectl apply -f deployment.yaml (POST /apis/apps/v1/namespaces/prod/deployments)               |
|         ▼                                                                                                     |
|  [ kube-apiserver ]                                                                                           |
|         │                                                                                                     |
|         │ 2. Validates Deployment schema (Deployment spec is syntactically valid)                             |
|         │ 3. Writes Deployment object to etcd                                                                 |
|         ▼                                                                                                     |
|    [ etcd ] <─────────────────────────────────── [ Deployment Created: HTTP 201 Created ]                     |
|                                                                                                               |
|  ============================== ASYNCHRONOUS RECONCILIATION LOOP ===========================================  |
|                                                                                                               |
|  [ Deployment Controller ] (in kube-controller-manager)                                                       |
|         │                                                                                                     |
|         │ 4. Detects new Deployment; computes ReplicaSet spec                                                 |
|         │ 5. POST /apis/apps/v1/namespaces/prod/replicasets                                                   |
|         ▼                                                                                                     |
|  [ kube-apiserver ]                                                                                           |
|         │                                                                                                     |
|         │ 6. Writes ReplicaSet object to etcd                                                                 |
|         ▼                                                                                                     |
|    [ etcd ] <─────────────────────────────────── [ ReplicaSet Created: HTTP 201 Created ]                     |
|                                                                                                               |
|  ============================== POD SPAWN & ADMISSION INTERCEPTION =========================================  |
|                                                                                                               |
|  [ ReplicaSet Controller ] (in kube-controller-manager)                                                       |
|         │                                                                                                     |
|         │ 7. Detects replicas=1 desired, replicas=0 actual                                                   |
|         │ 8. POST /api/v1/namespaces/prod/pods (Attempts to create the child Pod)                             |
|         ▼                                                                                                     |
|  [ kube-apiserver ]                                                                                           |
|         │                                                                                                     |
|         ├──► 9. Authentication & Authorization (Passes: ServiceAccount has permissions)                      |
|         │                                                                                                     |
|         ├──► 10. Admission Plugins Executed:                                                                  |
|         │        [ Pod Security Admission Plugin (PSA) ]                                                      |
|         │        Evaluates namespace label: pod-security.kubernetes.io/enforce=restricted                     |
|         │        Evaluates incoming Pod spec: Missing runAsNonRoot, allowPrivilegeEscalation, etc.            |
|         │                                                                                                     |
|         │        X REJECTED (HTTP 403 Forbidden: violates PodSecurity "restricted:latest")                    |
|         │                                                                                                     |
|         ▼                                                                                                     |
|  [ HTTP 403 Forbidden Response sent back to ReplicaSet Controller ]                                           |
|                                                                                                               |
|  ============================== THE "SILENT REPLICASET" STATE ==============================================  |
|                                                                                                               |
|  * The Pod object is NEVER written to etcd.                                                                   |
|  * "kubectl get pods -n prod" returns "No resources found in prod namespace."                                 |
|  * "kubectl describe pod" fails because no pod exists.                                                        |
|  * Deployment shows: "0/1 READY".                                                                             |
|  * The failure error string is stored ONLY in:                                                                |
|         ReplicaSet Events -> "kubectl describe rs <rs-name> -n prod"                                         |
|                                                                                                               |
+---------------------------------------------------------------------------------------------------------------+
```

### Why the Error is Invisible to `kubectl apply` and `kubectl get pods`

When you run `kubectl apply -f deployment.yaml`:
1. You are submitting a **Deployment** object, not a **Pod** object.
2. The PSA admission plugin intercepts **Pod creation requests**, not Deployment or ReplicaSet creation requests (though PSA warn/audit will emit warnings to the terminal on Deployment submission if configured).
3. The API server returns `deployment.apps/web created` successfully because the Deployment resource itself was accepted.
4. Seconds later, the ReplicaSet controller tries to spawn the Pod. PSA catches the Pod creation request and throws a `403 Forbidden`.
5. Because the Pod never passed admission, it was **never written to etcd**. Therefore:
   ```bash
   kubectl get pods -n prod
   # Output: No resources found in prod namespace.
   ```
6. The only place the rejection reason lives is in the **ReplicaSet Events stream**:
   ```bash
   kubectl describe rs <replicaset-name> -n prod
   ```
   Under `Events:`, you will find:
   ```text
   FailedCreate: Error creating: pods "web-74d754b9d5-xk29j" is forbidden: violates PodSecurity 
   "restricted:latest": allowPrivilegeEscalation != false, unrestricted capabilities, runAsNonRoot != true...
   ```

---

## 🔒 4. The 5-Field Mandate for PSA Restricted Compliance

To pass PSA `enforce: restricted`, every container in the Pod must explicitly satisfy 5 core container-level and pod-level security constraints:

```
+-------------------------------------------------------------------------------------------------------+
|                               PSA RESTRICTED 5-FIELD MANDATE CHECKLIST                                |
+-------------------------------------------------------------------------------------------------------+
| FIELD                                      | LEVEL       | REQUIRED VALUE | EXPLANATION               |
+--------------------------------------------+-------------+----------------+---------------------------+
| 1. allowPrivilegeEscalation                | container   | false          | Sets PR_SET_NO_NEW_PRIVS. |
|                                            |             |                | Blocks SUID elevation.    |
+--------------------------------------------+-------------+----------------+---------------------------+
| 2. capabilities.drop                       | container   | ["ALL"]        | Strips all 14 default     |
|                                            |             |                | Linux capabilities.       |
+--------------------------------------------+-------------+----------------+---------------------------+
| 3. runAsNonRoot                            | pod/contain | true           | Enforces UID != 0 check   |
|                                            |             |                | at container launch.      |
+--------------------------------------------+-------------+----------------+---------------------------+
| 4. runAsUser (or runAsGroup)               | pod/contain | 1000 (non-0)   | Explicit non-root UID.    |
+--------------------------------------------+-------------+----------------+---------------------------+
| 5. seccompProfile.type                     | pod/contain | RuntimeDefault | Filters dangerous raw     |
|                                            |             |                | kernel syscalls via BPF.  |
+--------------------------------------------+-------------+----------------+---------------------------+
```

> [!IMPORTANT]
> **Level Scope Distinction:**
> - `runAsNonRoot`, `runAsUser`, and `seccompProfile` can be specified at the **Pod level** (`spec.securityContext`), applying automatically to all containers.
> - `allowPrivilegeEscalation` and `capabilities` **MUST** be declared at the **Container level** (`spec.containers[*].securityContext`). Declaring them at the pod level is a schema validation error.

---

## 🛠️ 5. Practical Manifest Implementation (Real Exam Question 12)

### Step 1: Label the Target Namespace for Restricted Enforcement

```bash
kubectl label namespace staging \
  pod-security.kubernetes.io/enforce=restricted \
  pod-security.kubernetes.io/enforce-version=latest \
  --overwrite
```

Verify the labels applied:
```bash
kubectl get ns staging --show-labels
```

### Step 2: Fully Compliant Deployment Manifest

Below is the golden template that satisfies all PSA Restricted rules without causing admission failures:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-app
  namespace: staging
  labels:
    app: secure-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: secure-app
  template:
    metadata:
      labels:
        app: secure-app
    spec:
      # Pod-Level Security Context
      securityContext:
        runAsNonRoot: true
        runAsUser: 10001
        runAsGroup: 10001
        fsGroup: 10001
        seccompProfile:
          type: RuntimeDefault

      containers:
      - name: app
        image: nginx:alpine
        # Container-Level Security Context
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          capabilities:
            drop:
              - ALL
        volumeMounts:
        - name: tmp-dir
          mountPath: /tmp
        - name: run-dir
          mountPath: /var/run
        - name: cache-dir
          mountPath: /var/cache/nginx

      volumes:
      - name: tmp-dir
        emptyDir: {}
      - name: run-dir
        emptyDir: {}
      - name: cache-dir
        emptyDir: {}
```

---

## ⚡ 6. Speed Troubleshooting & Exam Diagnostics

When an exam question states: *"A deployment was applied to namespace X, but no pods are running. Identify why and fix it."*

Follow this exact 3-step diagnostic ladder:

```
[ Step 1: Check Pod Existence ]
$ kubectl get pods -n <ns>
No resources found in <ns> namespace.

[ Step 2: Check ReplicaSet Status & Events ]
$ kubectl get rs -n <ns>
NAME                  DESIRED   CURRENT   READY   AGE
secure-app-6bf74b97   1         0         0       45s

$ kubectl describe rs secure-app-6bf74b97 -n <ns> | tail -n 10
Events:
  Type     Reason        Age                From                   Message
  ----     ------        ----               ----                   -------
  Warning  FailedCreate  12s (x4 over 45s)  replicaset-controller  Error creating: pods "secure-app-6bf74b97-xxxx" 
  is forbidden: violates PodSecurity "restricted:latest":
  - allowPrivilegeEscalation != false
  - unrestricted capabilities (must drop ALL)
  - runAsNonRoot != true

[ Step 3: Fast Dry-Run Pre-flight Test ]
$ kubectl apply -f deployment.yaml --dry-run=server
# "--dry-run=server" forces the API server and PSA admission plugin to evaluate the resource,
# surfacing admission rejections immediately in your terminal before updating etcd!
```

---

## 🔗 Related Master Notes & References
- Landing Concept: [[Main Notes/Kubernetes Pod Security and Policy Engines|Kubernetes Pod Security and Policy Engines]]
- Workload Hardening: [[Main Notes/Kubernetes Container Hardening - Immutability, SecurityContext Trinity, and Multi-Container Configurations|Container Hardening Trinity & Immutability]]
- Seccomp Filtering: [[Main Notes/Kubernetes Workload Security - Seccomp BPF Syscall Filtering and RuntimeDefault Profiles|Seccomp BPF Syscall Filtering]]
- Capabilities Dropping: [[Main Notes/Kubernetes Workload Security - Linux Capabilities Stripping, CAP_NET_RAW, and eBPF Profiling|Linux Capabilities Stripping & CAP_NET_RAW]]
- Reference Guide: [[Reference Notes/0-7-2_pod_security_standards_and_admission.md|Module 0-7-2: Pod Security Standards, PSP & PSA Masterclass]]
