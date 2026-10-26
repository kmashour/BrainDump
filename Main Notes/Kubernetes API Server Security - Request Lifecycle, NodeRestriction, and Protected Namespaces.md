---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Cluster Component Hardening and Communication Security]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & API Server Hardening"
tags:
  - kubernetes/security
  - kubernetes/apiserver
  - kubernetes/rbac
  - kubernetes/admission-control
  - kubernetes/noderestriction
  - kubernetes/protected-namespaces
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes API Server Security - Request Lifecycle, NodeRestriction, and Protected Namespaces

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Cluster Component Hardening and Communication Security]] > **API Server Security - Request Lifecycle, NodeRestriction, and Protected Namespaces**

---

## 🎯 1. Architectural Foundations: The 3-Stage API Request Lifecycle

Every HTTP request reaching the Kubernetes API Server (`https://<controlplane>:6443`) passes through **three sequential security gates** before it is permitted to interact with the `etcd` datastore:

```
[ Incoming Request (curl / kubectl / Kubelet) ]
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│ 1. AUTHENTICATION GATE (Who are you?)                       │
│    - X.509 Client Certs, Bearer Tokens, Webhook Tokens     │
│    - Controlled by: --anonymous-auth=false                  │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Valid identity established)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. AUTHORIZATION GATE (Are you allowed to do this?)         │
│    - Evaluates permissions in order: Node, then RBAC        │
│    - Controlled by: --authorization-mode=Node,RBAC          │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Approved)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. ADMISSION CONTROL GATE (Is this payload valid & safe?)   │
│    - Mutating & Validating Webhooks, Security Plugins       │
│    - Controlled by: --enable-admission-plugins=...          │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Passed all gates)
                               ▼
                        [ Write to etcd ]
```

---

## 🛡️ 2. The Three Control Plane Hardening Flags

---

### Gate 1: Disable Anonymous Access (`--anonymous-auth=false`)
* **Default Behavior:** By default, `--anonymous-auth=true`. If an incoming request lacks bearer tokens or client certificates, the API Server assigns the caller to username `system:anonymous` in group `system:unauthenticated`.
* **The Security Threat:** If a misconfigured RoleBinding or third-party Helm chart grants permissions to `system:unauthenticated`, external callers on the network can query API endpoints anonymously.
* **The Hardening:** Enforce `--anonymous-auth=false`. Any unauthenticated request is immediately rejected with `401 Unauthorized`.

---

### Gate 2: Authorization Modes (`--authorization-mode=Node,RBAC`)
Authorization plugins are evaluated **sequentially** (the first authorizer to return `Allow` grants access):

1. **`Node` Authorizer (Evaluated First):**
   - Specifically authorizes requests issued by Kubelets (identified by user `system:node:<nodeName>` and group `system:nodes`).
   - Restricts Kubelets to only read secrets, configmaps, and pods scheduled on **their own node**.
   - **Defense:** If an attacker compromises worker node `node01`, the `Node` authorizer prevents that node's Kubelet from reading secrets or pods allocated to `node02`.
2. **`RBAC` Authorizer (Evaluated Second):**
   - Evaluates standard Kubernetes `Roles`, `ClusterRoles`, and `RoleBindings` for human users, ServiceAccounts, and controllers.
3. **Syntax Rule:** The flag takes a strict comma-separated list without spaces: `--authorization-mode=Node,RBAC`. (Never include `AlwaysAllow`).

---

### Gate 3: The `NodeRestriction` Admission Controller (`--enable-admission-plugins=NodeRestriction`)
While the `Node` authorizer controls what a Kubelet is allowed to **read**, the `NodeRestriction` admission controller controls what a Kubelet is allowed to **write or modify**:
* Prevents Kubelets from modifying or adding labels beginning with `node-restriction.kubernetes.io/`.
* Prevents Kubelets from modifying labels in protected namespaces.
* Prevents Kubelets from modifying pods, status, or leases belonging to other nodes.

---

## 🏛️ 3. What is a "Protected Namespace"?

A **protected namespace** refers to system-critical namespaces that host core cluster networking, DNS, and node health infrastructure. Tampering with these namespaces causes immediate cluster-wide failure.

### The Core Protected Namespaces

| Namespace | Critical Components | Why It Is Protected |
| :--- | :--- | :--- |
| **`kube-system`** | CoreDNS, `kube-proxy`, CNI daemon (Calico/Cilium), metrics-server, CSI storage | If deleted or corrupted, all cluster DNS, overlay networking, and pod routing collapses. |
| **`kube-node-lease`** | Node `Lease` heartbeat objects (1 per node) | Kubelets renew their Lease every 10 seconds. If blocked, the control plane presumes nodes are dead and evicts all pods. |
| **`kube-public`** | `cluster-info` ConfigMap | Read-only bootstrap information for `kubeadm join`. Contains no secrets. |

---

### How `NodeRestriction` Protects `kube-system`
If an attacker compromises worker node `node01` and steals its Kubelet client certificate:

```
[ Compromised Worker Node (node01) ]
                 │
                 ▼ (Attacker uses Kubelet credentials)
[ Attacker crafts malicious API request pretending to be Kubelet ]
                 │
                 ├── Attempt A: Delete CoreDNS pod in 'kube-system' ──► [ NodeRestriction: REJECTED! ❌ ]
                 │                                                     ("Kubelet cannot modify kube-system pods!")
                 │
                 └── Attempt B: Tamper with node02 Lease ─────────────► [ NodeRestriction: REJECTED! ❌ ]
                                                                       ("Kubelet can only update its own Lease!")
```

---

### The Admission Webhook Deadlock Rule
Because `kube-system` houses infrastructure pods (such as CNI and `kube-proxy`) that **must run as root and need `hostNetwork: true`**, strict security admission webhooks (like OPA Gatekeeper or Kyverno) must **always exempt protected namespaces**:

```yaml
namespaceSelector:
  matchExpressions:
  - key: kubernetes.io/metadata.name
    operator: NotIn
    values:
    - kube-system
    - kube-node-lease
```
*(See [[Main Notes/Kubernetes Admission Control - Webhook Deadlocks, CNI Collapse, and Namespace Blacklisting|Admission Webhook Deadlocks & CNI Collapse]] for details on circular dependency recovery).*

---

## 🛠️ 4. Static Pod Editing & Troubleshooting (`kube-apiserver.yaml`)

### Step 1: Backup Before Editing
Always copy the manifest outside `/etc/kubernetes/manifests/`:
```bash
cp /etc/kubernetes/manifests/kube-apiserver.yaml /root/kube-apiserver.yaml.bak
```

### Step 2: Apply Hardening Flags
Edit `/etc/kubernetes/manifests/kube-apiserver.yaml` under `spec.containers[0].command`:
```yaml
spec:
  containers:
  - command:
    - kube-apiserver
    - --anonymous-auth=false
    - --authorization-mode=Node,RBAC
    - --enable-admission-plugins=NodeRestriction
```

### Step 3: Crash Recovery with `crictl`
If the API Server enters a crash loop (`kubectl` returns `connection refused`):
```bash
# 1. Identify the crashed container ID:
sudo crictl ps -a --name kube-apiserver

# 2. View fatal error logs:
sudo crictl logs $(sudo crictl ps -a --name kube-apiserver -q | head -n1)
```
Fix typos or restore from `/root/kube-apiserver.yaml.bak`.

---

## 🎯 5. Real Exam 2026: Question 16 Blueprint & Pitfalls

### Key Checks:
1. **No Spaces in Flag Values:** `--authorization-mode=Node,RBAC` (spaces around commas break the command parser).
2. **Singular vs Plural:**
   - `--anonymous-auth=false` (singular)
   - `--authorization-mode=Node,RBAC` (singular `mode`)
   - `--enable-admission-plugins=NodeRestriction` (plural `plugins`)
3. **Sequential Verification:** Test with `kubectl get nodes` to confirm the static pod restarted and authenticated requests succeed.
