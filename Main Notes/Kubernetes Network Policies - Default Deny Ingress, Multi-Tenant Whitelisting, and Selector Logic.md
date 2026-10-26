---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Network Security and Traffic Segregation]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Network Hardening"
tags:
  - kubernetes/security
  - kubernetes/networking
  - kubernetes/network-policy
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Network Policies - Default Deny Ingress, Multi-Tenant Whitelisting, and Selector Logic

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Network Security and Traffic Segregation]] > **Default Deny Ingress, Multi-Tenant Whitelisting, and Selector Logic**

---

## 🎯 1. Architectural Foundations: The CNI Packet Filtering Model

Unlike Kubernetes controllers that reconcile API resources directly in userspace, **NetworkPolicies are enforced at the Linux kernel level by the Container Network Interface (CNI)** plugin.

```
[ Developer / Admin ]
        │
        ▼ (kubectl apply -f netpol.yaml)
[ kube-apiserver ] ───(Stores NetworkPolicy in etcd)
        │
        ▼ (Watches API via informers)
[ CNI DaemonSet Agent on Node ] (e.g. Calico calico-node / Cilium cilium-agent)
        │
        ▼ Compiles rules into:
+----------------------------------------------------------------+
| Linux Kernel Packet Filters                                    |
| - iptables / ipset (Calico / Kube-router)                     |
| - eBPF Programs attached to TC / XDP hooks (Cilium / Calico)   |
+----------------------------------------------------------------+
```

### Pod Isolation Lifecycle (Additive Whitelisting)
Pods inside a namespace exist in one of two states:
1. **Non-Isolated (Default State):** If zero NetworkPolicies select a Pod for ingress, all incoming traffic is accepted from any source within or outside the cluster.
2. **Isolated State:** The moment a single NetworkPolicy selects a Pod via `spec.podSelector`, that Pod becomes isolated. All incoming traffic is immediately dropped **except** what is explicitly whitelisted.
3. **Additive Logic (Logical OR):** When multiple NetworkPolicies select the same Pod, their allow rules are combined additively.

---

## ⚠️ 2. The Critical Exam Pitfall: The Dash (`-`) Trap (AND vs. OR Logic)

The single most common failure point in Kubernetes NetworkPolicy configuration lies in YAML array indentation under `ingress.from`.

```
===================================================================
Case A: Separate List Items (Logical OR)
===================================================================
ingress:
- from:
  - namespaceSelector:
      matchLabels:
        env: prod
  - podSelector:            <-- Note the dash '-': Separate list element!
      matchLabels:
        role: frontend

SEMANTICS: Allow traffic from ANY pod in namespace 'prod'
           OR from ANY pod in the current namespace labeled 'role: frontend'.
```

```
===================================================================
Case B: Single List Item with Two Selectors (Logical AND)
===================================================================
ingress:
- from:
  - namespaceSelector:
      matchLabels:
        env: prod
    podSelector:            <-- NO dash! Indented under the same list element!
      matchLabels:
        role: frontend

SEMANTICS: Allow traffic ONLY from pods that have label 'role: frontend'
           AND simultaneously reside inside a namespace labeled 'env: prod'.
```

---

## ⚙️ 3. Concrete Implementations: Default Deny & Multi-Tenant Whitelisting

### Pattern 1: Baseline Default Deny Ingress
To eliminate the open-by-default behavior across a target namespace, deploy a baseline deny policy:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: isolated-apps
spec:
  podSelector: {}          # Empty braces select ALL pods in the namespace
  policyTypes:
  - Ingress                # Isolate Ingress. Because the 'ingress:' section is omitted,
                           # ALL incoming traffic to all pods in this namespace is blocked.
```

> [!IMPORTANT]
> If `policyTypes: [Ingress]` is omitted when no `ingress:` block exists, Kubernetes may not activate ingress isolation. Always declare `policyTypes: [Ingress]` explicitly.

---

### Pattern 2: Multi-Tenant Namespace Whitelisting with Port Restriction
To allow ingress only from approved tenant namespaces on a dedicated TCP service port:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-ns-ingress
  namespace: isolated-apps
spec:
  podSelector: {}          # Protects all pods in isolated-apps
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:   # Allow traffic originating from namespaces
        matchLabels:
          access: allowed  # labeled 'access: allowed'
    ports:
    - protocol: TCP
      port: 8080           # Restrict allowed traffic strictly to TCP port 8080
```

> [!NOTE]
> **Traffic Scope & Port Locking:**
> * **Who can connect?** Because `namespaceSelector` has **no sibling `podSelector`** in this `from:` element, **ANY pod** residing in any namespace labeled `access: allowed` is permitted to connect.
> * **Port Constraint:** Traffic is strictly restricted to TCP port `8080`. Any traffic to other ports (22, 80, 443) from those same pods is completely dropped by the `default-deny-ingress` baseline.

---

## 🛠️ 4. Practical Terminal Verification Workflows

Never assume a NetworkPolicy works solely because `kubectl apply` succeeded. Always perform active verification using transient pods.

### Step 1: Identify Target Pod IP
```bash
TARGET_IP=$(kubectl get pod -n isolated-apps -o jsonpath='{.items[0].status.podIP}')
```

### Step 2: Negative Test (Verify Traffic is Blocked from Unapproved Namespace)
Run a curl or wget probe from the `default` namespace (which lacks the `access: allowed` label):
```bash
kubectl run test-fail --rm -it --image=busybox:1.36 --restart=Never -n default -- \
  wget --spider --timeout=2 http://${TARGET_IP}:8080
```
* **Expected Output:** `wget: download timed out` (Traffic successfully dropped by the CNI filter).

---

### Step 3: Positive Test (Verify Traffic is Allowed from Approved Namespace)
Ensure the source namespace is labeled and repeat the probe:
```bash
# 1. Create and label source namespace
kubectl create namespace tenant-a
kubectl label namespace tenant-a access=allowed --overwrite

# 2. Probe from the labeled namespace
kubectl run test-pass --rm -it --image=busybox:1.36 --restart=Never -n tenant-a -- \
  wget --spider --timeout=2 http://${TARGET_IP}:8080
```
* **Expected Output:** `Connecting to ... (200 OK)` (Traffic successfully permitted).
