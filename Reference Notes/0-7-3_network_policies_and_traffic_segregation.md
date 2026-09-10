---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - kubernetes/security
  - kubernetes/networkpolicy
---

# Module 0-7-3: NetworkPolicies & Traffic Segregation

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Reference MOC]] > **Module 0-7-3**

---

## 10. NetworkPolicies

By default, Kubernetes network traffic is **non-isolated (default-allow)**: any Pod can communicate with any other Pod in the cluster, across all namespaces. NetworkPolicies restrict traffic flow (ingress and egress).

> [!IMPORTANT]
> NetworkPolicies are enforced by the cluster's CNI network plugin (e.g., Calico, Cilium, Weave, Kube-router). If you are using a CNI plugin that does not support network policies (like Flannel), NetworkPolicy manifests will be accepted by the API server but will not be enforced.

### 10.1 Selector Combinations: AND vs. OR
Understanding the syntax for combining namespace and pod selectors inside `from` and `to` blocks is critical:

#### OR Logic (Separate Array Elements)
Traffic is allowed if it matches the namespace selector **OR** the pod selector.
```yaml
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          environment: production
    - podSelector:
        matchLabels:
          app: frontend
```
*Matches:* Any pod in a namespace labeled `environment: production` (regardless of pod labels), and any pod in the same namespace labeled `app: frontend`.

#### AND Logic (Single Array Element with Multiple Keys)
Traffic is allowed only if it matches both selectors.
```yaml
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          environment: production
      podSelector:
        matchLabels:
          app: frontend
```
*Matches:* Only pods labeled `app: frontend` that reside inside namespaces labeled `environment: production`.

---

### 10.2 Production Network Policy Templates

#### Template 1: Default Deny All Ingress & Egress (Namespace Lockdown)
Run this policy in a namespace to block all traffic by default. Services must then be explicitly allowed.
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: secure-app
spec:
  podSelector: {} # Empty selector matches all pods in the namespace
  policyTypes:
  - Ingress
  - Egress
```

#### Template 2: Database Policy (Ingress Only)
Allows inbound database connections on port `5432` only from the API application pods, blocking all other ingress.
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-policy
  namespace: secure-app
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: api
    ports:
    - protocol: TCP
      port: 5432
```

#### Template 3: Strict Egress Isolation (Allow DNS and specific backend only)
Restricts app pods to only call DNS (UDP/TCP 53) in the `kube-system` namespace and a specific database in the same namespace.
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-egress-policy
  namespace: secure-app
spec:
  podSelector:
    matchLabels:
      role: api
  policyTypes:
  - Egress
  egress:
  # Rule 1: Allow DNS resolution
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: kube-system
      podSelector:
        matchLabels:
          k8s-app: kube-dns
    ports:
    - protocol: UDP
      port: 53
    - protocol: TCP
      port: 53
  # Rule 2: Allow database access
  - to:
    - podSelector:
        matchLabels:
          role: db
    ports:
    - protocol: TCP
      port: 5432
```

#### Template 4: Access to External IP Ranges (Egress with CIDR)
Allows pods to communicate with an external API server outside the cluster (e.g., IP `203.0.113.50`).
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: external-egress-policy
  namespace: secure-app
spec:
  podSelector:
    matchLabels:
      role: api
  policyTypes:
  - Egress
  egress:
  - to:
    - ipBlock:
        cidr: 203.0.113.0/24
        except:
        - 203.0.113.10/32 # Block this specific host
    ports:
    - protocol: TCP
      port: 443

---

### 10.3 Step-by-Step Walkthrough: Locking Down a Namespace and Allowing Labeled Traffic
By default, all pods in a cluster can communicate freely. In this walkthrough, we will establish a **Default Deny-All** posture in a test namespace, verify that it blocks untrusted communication, and then explicitly allow traffic from a trusted, labeled client pod.

#### Step 1: Create Namespace and Apply Default Deny-All
Create a test namespace:
```bash
kubectl create namespace netpol-test
```
Create and apply a default deny-all policy (`deny-all.yaml`) that targets all pods (`podSelector: {}`) and blocks all incoming (Ingress) traffic:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: netpol-test
spec:
  podSelector: {} # Empty selector matches all pods in this namespace
  policyTypes:
  - Ingress
```
Apply the policy:
```bash
kubectl apply -f deny-all.yaml
```

#### Step 2: Deploy the Target Web Server
Deploy an Nginx web server and expose it as an internal ClusterIP service:
```bash
kubectl run web-server --image=nginx --labels="app=web-server" -n netpol-test
kubectl expose pod web-server --port=80 --target-port=80 -n netpol-test
```

#### Step 3: Verify Blocked Traffic (Negative Case)
Spin up a temporary, untrusted pod to query the web server. This request should fail (timeout) because of our deny-all policy:
```bash
kubectl run untrusted-client --image=busybox -n netpol-test --rm -it -- wget -qO- --timeout=2 http://web-server
```
*Expected Output:* `wget: download timed out`

#### Step 4: Create a Label-Based Allow Policy
Create an allow policy (`allow-labeled.yaml`) that permits inbound TCP traffic on port `80` to any pod labeled `app: web-server`, but **only if** the sender pod is labeled `access: "true"`:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-web-access
  namespace: netpol-test
spec:
  podSelector:
    matchLabels:
      app: web-server # Target pod to secure
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          access: "true" # Allow traffic only from pods with this label
    ports:
    - protocol: TCP
      port: 80
```
Apply the allow policy:
```bash
kubectl apply -f allow-labeled.yaml
```

#### Step 5: Verify Allowed Traffic (Positive Case)
Launch a client pod that contains the matching `access=true` label, and query the web server:
```bash
kubectl run trusted-client --image=busybox --labels="access=true" -n netpol-test --rm -it -- wget -qO- --timeout=2 http://web-server
```
*Expected Output:* The standard HTML source code of the Nginx welcome page, proving the label-based policy successfully permitted the connection.

---

## 5. Advanced CKS Network Security Patterns

### 5.1 Blocking Cloud Metadata Endpoints (SSRF Mitigation)
In cloud environments (AWS, GCP, Azure), workloads can query the link-local metadata address (`169.254.169.254`) to extract IAM instance credentials, bootstrap tokens, and cloud account roles. If an application suffers from Server-Side Request Forgery (SSRF), an attacker can steal node IAM privileges.

To prevent this, enforce an egress policy that allows all internet egress *except* the metadata endpoint:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: block-cloud-metadata
  namespace: production
spec:
  podSelector: {} # Applies to all pods in the namespace
  policyTypes:
  - Egress
  egress:
  # 1. Allow DNS resolution to kube-system
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: kube-system
    ports:
    - protocol: UDP
      port: 53
    - protocol: TCP
      port: 53
  # 2. Allow outbound access to internet/VPC, excluding 169.254.169.254
  - to:
    - ipBlock:
        cidr: 0.0.0.0/0
        except:
        - 169.254.169.254/32
```

### 5.2 Strict Multi-Tenant Pod Isolation (Zero-Trust Model)
In multi-tenant environments, every namespace should have:
1. **Default-Deny Ingress and Egress:** Completely sever untracked network activity.
2. **Explicit Internal Egress:** Permit egress only to designated databases and DNS resolvers.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: tenant-a
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

### 5.3 Cilium CNI Architecture & eBPF Security
Traditional Kubernetes networking with `kube-proxy` relies on `iptables` or `IPVS`. As cluster scale expands to thousands of pods and services, sequential traversal of tens of thousands of `iptables` packet filtering rules introduces substantial CPU overhead and connection latency.

**Cilium** replaces `kube-proxy` and standard packet filtering by attaching **eBPF (extended Berkeley Packet Filter)** programs directly into Linux network sockets and traffic control (`tc`) hooks:
* **Identity-Aware Security:** Packets are tagged with cryptographic numeric security identities rather than raw IP addresses, eliminating rule explosion.
* **L7 Protocol Awareness:** Enforces HTTP verbs (`GET /api/public` vs `POST /api/admin`), gRPC methods, and Kafka topics natively at the socket layer.
* **Transparent Pod-to-Pod Encryption:** Provides automatic wire encryption between nodes using WireGuard or IPsec without modifying application pods or installing service mesh sidecars.

### 5.4 Pod-to-Pod Mutual TLS (mTLS) vs. One-Way TLS
Securing east-west traffic inside the Kubernetes cluster is essential for zero-trust microservice communications:

| Dimension | One-Way SSL/TLS | Mutual TLS (mTLS) |
| :--- | :--- | :--- |
| **Authentication Target** | Client verifies Server identity only | Server AND Client cryptographically verify each other |
| **Threat Mitigated** | Eavesdropping, passive packet sniffing | Man-in-the-Middle (MITM), pod impersonation, unauthorized callers |
| **Implementation Modes** | Application-level HTTPS certificate | Sidecar Proxy (Istio Envoy) or CNI Kernel-level (Cilium WireGuard) |
| **Identity Verification** | Server domain name (SAN) | SPIFFE ID / X.509 Subject Alternative Name (e.g. `spiffe://cluster.local/ns/prod/sa/payment-service`) |

---

<!-- Documentation References -->
[Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
[Kubernetes Security Overview](https://kubernetes.io/docs/concepts/security/overview/)
[KodeKloud CKS: Pod to Pod Encryption](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Pod-to-Pod-Encryption/page)
[KodeKloud CKS: One way SSL vs Mutual SSL](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/One-way-SSL-vs-Mutual-SSL/page)
[KodeKloud CKS: Introduction to Cilium](https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Minimize-Microservice-Vulnerabilities/Introduction-to-Cilium/page)

