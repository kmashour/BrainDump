---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Network Security and Traffic Segregation]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Service Mesh Security"
tags:
  - kubernetes/security
  - kubernetes/networking
  - kubernetes/service-mesh
  - kubernetes/istio
  - kubernetes/mtls
  - kubernetes/crd
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Service Mesh Security - Istio mTLS, PeerAuthentication CRDs, and Sidecar Injection

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Network Security and Traffic Segregation]] > **Istio mTLS, PeerAuthentication CRDs, and Sidecar Injection**

---

## 🎯 1. Architectural Foundations: Why NetworkPolicies Are Not Enough

While Kubernetes NetworkPolicies enforce Layer 3/4 packet filtering (controlling *who* can connect to *whom*), they **do not encrypt network payloads**.

```
[ Pod A (Frontend) ] ─────── Cleartext TCP Traffic ───────► [ Pod B (Backend) ]
                                   │
                                   ▼ (Node / Host Network Sniffer)
                      [ Attacker runs tcpdump on node interface! ]
                      [ Intercepts tokens, passwords, and PII!   ]
```

### The Service Mesh Solution: Transparent mTLS
A Service Mesh (such as Istio) implements zero-trust pod-to-pod **Mutual TLS (mTLS)** at Layer 7:
* A mutating admission webhook automatically injects an Envoy proxy container (`istio-proxy`) into every Pod.
* Local node `iptables` rules intercept all incoming and outgoing application traffic, redirecting it through the Envoy sidecar.
* Outgoing packets are transparently encrypted with mutual TLS using short-lived X.509 certificates issued by Istio's control plane (`istiod`).
* Incoming packets are decrypted by the receiver's Envoy sidecar and passed over `localhost` to the target application container.
* Neither application code nor application configurations need modification.

```
[ Pod A (Namespace: finance-mesh) ]             [ Pod B (Namespace: finance-mesh) ]
+---------------------------------+             +---------------------------------+
| Container: web-app              |             | Container: ledger-service       |
|              │ (Cleartext)      |             |              ▲ (Cleartext)      |
|              ▼                  |             |              │                  |
| Sidecar: istio-proxy (Envoy)    |             | Sidecar: istio-proxy (Envoy)    |
+--------------│------------------+             +--------------▲------------------+
               │                                               │
               └══════════════ Mutual TLS (mTLS) ══════════════┘
                         (Encrypted over the Wire!)
```

---

## 🧩 2. Istio Custom Resource Definitions (CRDs) & `PeerAuthentication`

`PeerAuthentication` is **not** a built-in Kubernetes native resource (like `Pod` or `NetworkPolicy`). It is an Istio **Custom Resource Definition (CRD)** registered in the cluster under the `security.istio.io` API group.

### Checking CRD Registration in the Terminal
```bash
kubectl get crd | grep -i peerauthentication
# Output:
# peerauthentications.security.istio.io    2026-10-02T10:00:00Z
```

### Supported mTLS Modes
The `PeerAuthentication` resource configures traffic tunneling behavior across workloads:
1. **`PERMISSIVE` (Default):** Workloads accept both unencrypted plaintext HTTP and encrypted mTLS. (Used for gradual onboarding so unmeshed pods do not break).
2. **`STRICT` (Security Hardened):** Workloads reject all cleartext traffic. Every incoming TCP connection **must** present a valid client certificate issued by the mesh CA.
3. **`DISABLE`:** mTLS is turned off completely.

---

## 🧭 3. Exam Strategy: How to Build the YAML Without Memorizing It

External documentation (`istio.io`) is **strictly blocked** by the secure browser proxy during the CKS exam. You do not need external internet access; use these three terminal discovery methods:

### Method 1: The "Cluster Scout" Trick (Fastest)
Before drafting YAML, check if an existing `PeerAuthentication` resource is already running in another namespace (e.g., `istio-system`) or if template files exist in the question workspace:
```bash
# 1. Check existing cluster resources:
kubectl get peerauthentication -A -o yaml

# 2. Check local directories for starter templates:
ls -la
grep -rn "PeerAuthentication" /opt/course/ 2>/dev/null
```
If an existing policy is found, export its skeleton, update `metadata.namespace` and `metadata.name`, and apply.

---

### Method 2: Offline Schema Discovery via `kubectl explain`
Because the CRD is registered with the API Server, **`kubectl explain` contains complete offline documentation for Istio resources**:

```bash
# 1. Discover resource kind and API version:
kubectl explain peerauthentication
# Output:
# KIND:     PeerAuthentication
# VERSION:  security.istio.io/v1beta1

# 2. Inspect the spec and available fields:
kubectl explain peerauthentication.spec.mtls
# Output:
# FIELDS:
#    mode <string>
#       Defines the mTLS mode.
#       Valid values: STRICT, PERMISSIVE, DISABLE
```
Right in the terminal, `kubectl explain` supplies the exact API version (`security.istio.io/v1beta1`), kind (`PeerAuthentication`), field path (`spec.mtls.mode`), and valid enum values (`STRICT`).

---

### Method 3: The 8-Line Canonical Skeleton
The complete policy requires only 8 lines of YAML:

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: finance-mesh
spec:
  mtls:
    mode: STRICT
```

> [!NOTE]
> Setting `metadata.name: default` configures the policy to apply to **all workloads** across the target namespace without requiring workload-specific selector labels.

---

## 🛠️ 4. The 3-Step Execution Sequence for CKS

To secure a namespace with Istio mTLS in the exam, execute the following sequence:

### Step 1: Label Namespace for Sidecar Injection
Enable automatic proxy injection on the namespace:
```bash
kubectl label namespace finance-mesh istio-injection=enabled --overwrite
```

### Step 2: Apply the STRICT `PeerAuthentication` Policy
Deploy the policy to enforce mutual TLS encryption:
```bash
cat <<EOF | kubectl apply -f -
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: finance-mesh
spec:
  mtls:
    mode: STRICT
EOF
```

### Step 3: Trigger a Rollout Restart (Mandatory)
> [!IMPORTANT]
> **Why `rollout restart` is mandatory:**
> Labeling a namespace **does not alter currently running pods**. If workloads in `finance-mesh` were deployed prior to labeling, their pods run with only one container (`1/1 Ready`), lacking the `istio-proxy` sidecar.
> Because `STRICT` mode rejects plaintext traffic, unmeshed pods will fail health checks or drop connections. Trigger a rollout restart to force the mutating admission webhook to inject sidecars into newly provisioned replicas:

```bash
kubectl rollout restart deployment -n finance-mesh ledger-service
```

---

## 🔍 5. Verification & Testing

### 1. Confirm Dual-Container Pod Readiness (`2/2 Ready`)
```bash
kubectl get pods -n finance-mesh
```
**Expected Output:**
```text
NAME                              READY   STATUS    RESTARTS   AGE
ledger-service-67995f5778-9px5l   2/2     Running   0          14s
ledger-service-67995f5778-v8x2b   2/2     Running   0          18s
```
The `2/2` status confirms both the application container and the `istio-proxy` sidecar are running.

### 2. Verify Container Names Inside the Pod
```bash
kubectl get pod -n finance-mesh -l app=ledger-service -o jsonpath='{.items[0].spec.containers[*].name}'
# Output:
# ledger-service istio-proxy
```
