---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Cluster Component Hardening and Communication Security]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Cluster Hardening"
tags:
  - kubernetes/security
  - kubernetes/cks
  - kubernetes/kubelet
  - kubernetes/etcd
  - kubernetes/mtls
  - kubernetes/pki
  - kubernetes/deep-dive
---

# Kubernetes Component Security - Kubelet Port 10250, etcd Client Auth, and mTLS Handshake Mechanics

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Cluster Component Hardening and Communication Security]] > **Kubelet Port 10250, etcd Client Auth, and mTLS Handshake Mechanics**

---

## 🎯 1. Architectural Roles & Threat Surfaces

Kubernetes control plane and worker components operate across distributed network endpoints. Two of the most critical endpoints in the entire cluster are **Kubelet (Port 10250)** and **etcd (Port 2379)**.

```
[ Attacker on Host / Internal Subnet ]
         │
         ├───► Probe Port 10250 (Kubelet Daemon)
         │     Default: anonymous: enabled: true, authorization: AlwaysAllow
         │     Impact: Direct RCE in containers via /run/<ns>/<pod>/<ctr>
         │
         └───► Probe Port 2379 (etcd Key-Value Store)
               Default: --client-cert-auth=false (or missing)
               Impact: Full plaintext dump of all Secrets, Tokens, and PKI
```

---

## ⚙️ 2. Kubelet Hardening: Port 10250 & SubjectAccessReview

### The Default Insecurity
When a worker node is bootstrapped without explicit security overrides:
* **Authentication:** Requests without TLS client certificates or bearer tokens are accepted under the anonymous identity `system:unauthenticated` (group `system:unauthenticated`).
* **Authorization:** Configured to `AlwaysAllow`. Any request reaching the port—even anonymous ones—is permitted to execute actions.

### The Remediation Anatomy (`/var/lib/kubelet/config.yaml`)
Kubelet is a host `systemd` service (not a static pod). Its configuration file is located at `/var/lib/kubelet/config.yaml`.

```yaml
authentication:
  anonymous:
    enabled: false    # 1. Rejects any request lacking valid credentials
  webhook:
    enabled: true     # 2. Delegates Bearer Token validation to kube-apiserver
  x509:
    clientCAFile: /etc/kubernetes/pki/ca.crt

authorization:
  mode: Webhook       # 3. Forwards requests to kube-apiserver for RBAC check
```

### How `authorization.mode: Webhook` Works Under the Hood
When a request arrives at Kubelet port `10250`:
1. Kubelet pauses execution and constructs a `SubjectAccessReview` API object.
2. Kubelet posts this request to `kube-apiserver`.
3. The API Server evaluates cluster RBAC policies: *"Does caller X have permission on resource `nodes/proxy` or subresource `pods/exec`?"*
4. If RBAC allows it, Kubelet executes the command. Otherwise, it returns `403 Forbidden`.

```
[ Caller ] ──(Request: /run/prod/web/app)──► [ Kubelet :10250 ]
                                                    │
                                                    │ 1. SubjectAccessReview
                                                    ▼
                                            [ kube-apiserver ]
                                                    │
                                                    │ 2. Evaluate RBAC
                                                    ▼
                                            [ Allowed / Denied ]
```

---

## 🔐 3. etcd Hardening: Port 2379 & Mutual TLS (mTLS)

### The etcd Threat Model
`etcd` stores the entire state of the cluster. If client certificate authentication is disabled, any client that can route packets to port `2379` can extract or overwrite cluster data.

In `/etc/kubernetes/manifests/etcd.yaml`, strict client TLS validation is enforced via:
```yaml
spec:
  containers:
  - command:
    - etcd
    - --client-cert-auth=true
    - --trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt
    - --cert-file=/etc/kubernetes/pki/etcd/server.crt
    - --key-file=/etc/kubernetes/pki/etcd/server.key
```

When `--client-cert-auth=true` is set, etcd requires **Mutual TLS (mTLS)**.

---

## 🔬 4. Deep Cryptographic Mechanics: The Two-Signature mTLS Handshake

A common misconception in PKI is that presenting a certificate signed by the CA is sufficient to prove identity. In reality, mTLS involves **two distinct cryptographic signatures** performed at different times with different keys.

### Signature 1: The CA's Signature on the Certificate (Identity Validation)
During cluster provisioning:
1. A client key pair is generated (Client Public Key + Client Private Key).
2. The CA takes the client identity and Public Key, hashes them, and signs the hash using the **CA's Private Key**.
3. This creates the Certificate (`.crt`).

```
+-------------------------------------------------------------+
|                  Client Certificate (.crt)                  |
|                                                             |
|  Subject: CN=kube-apiserver-etcd-client                     |
|  Client Public Key: 04a7b2...                               |
|                                                             |
|  CA Signature: [Hash encrypted with CA PRIVATE KEY]         |
+-------------------------------------------------------------+
```

When etcd receives this certificate, it uses `--trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt` (the **CA's Public Key**) to verify the CA signature. This proves:
> *"This certificate is authentic and was officially signed by our CA."*

---

### The Stolen Certificate Problem
**Certificates are public artifacts.** They traverse networks in cleartext (or within TLS handshake envelopes) and sit on node filesystems. If Alice copies Bob's certificate file (`bob.crt`), Alice can present `bob.crt` to etcd. 

The CA signature check will pass! To prevent this, etcd requires **Proof of Possession**.

---

### Signature 2: The Client's Live Handshake Signature (Proof of Possession)
To prove that the client presenting the certificate actually owns the underlying private key, etcd challenges the client during the live TLS handshake:

```
[ Client (etcdctl / API Server) ]               [ Server (etcd :2379) ]
           │                                                │
           │───────────── 1. ClientHello ──────────────────>│
           │<──────────── 2. ServerHello + Server Cert ─────│ (etcd proves its identity)
           │<──────────── 3. CertificateRequest ────────────│ (etcd demands client cert)
           │                                                │
           │  [Client takes the handshake exchange data     │
           │   and signs it using its PRIVATE KEY (.key)]   │
           │                                                │
           │── 4. Certificate (.crt) + Digital Signature ──>│
           │                                                │
           │                                      [etcd verifies two things:]
           │                                      1. Cert Authenticity: Uses
           │                                         CA Public Key (ca.crt)
           │                                         to verify CA signature.
           │                                      2. Proof of Possession: Uses
           │                                         Client Public Key (inside .crt)
           │                                         to verify the Signature!
           │                                                │
           │<──────────── 5. Handshake Complete ────────────│
```

### The Verification Matrix

| Check | Question Answered | Key Used to Verify | What It Proves |
| :--- | :--- | :--- | :--- |
| **1. Certificate Check** | *"Was this cert created by our CA?"* | **CA Public Key** (from `ca.crt`) | The identity card is genuine. |
| **2. Possession Check** | *"Does the client hold the private key?"* | **Client Public Key** (extracted from `.crt`) | The caller is the true owner, not an imposter. |

This is why `etcdctl` **cannot function** without `--key`. The private key is required to sign the live challenge.

---

## 🛠️ 5. Practical Terminal Execution & Recipes

### A. Kubelet Configuration & Systemd Reload
```bash
# 1. Edit config
sudo vi /var/lib/kubelet/config.yaml

# 2. Required configuration values:
# authentication.anonymous.enabled: false
# authentication.webhook.enabled: true
# authorization.mode: Webhook

# 3. Reload systemd and restart service
sudo systemctl daemon-reload
sudo systemctl restart kubelet

# 4. Verify service status
sudo systemctl status kubelet --no-pager
```

### B. Testing Kubelet Anonymous Access
```bash
# Probe port 10250 without credentials
curl -k -s -o /dev/null -w "%{http_code}\n" https://127.0.0.1:10250/runningpods/

# Expected output after hardening:
# 401 (Unauthorized) or 403 (Forbidden)
```

### C. Querying etcd with Full mTLS Credentials (Positive Test)
```bash
ETCDCTL_API=3 etcdctl \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  endpoint health
# Expected output:
# 127.0.0.1:2379 is healthy: successfully committed proposal: took = ...
```

### D. Testing etcd Client Certificate Authentication (Negative Test)
To prove that unauthenticated client connections are strictly rejected by etcd's TLS handshake:
```bash
# Attempt to query etcd without client certificate:
curl -k https://127.0.0.1:2379/healthz

# Expected output when --client-cert-auth=true is ENFORCED:
# curl: (35) error:0A000412:SSL routines::ssl/tls alert bad certificate
# (Or connection reset / handshake abort)

# Or test via etcdctl without --cert and --key:
ETCDCTL_API=3 etcdctl --cacert=/etc/kubernetes/pki/etcd/ca.crt endpoint health
# Expected output:
# {"level":"warn","msg":"failed to connect", ... "remote error: tls: bad certificate"}
```

### E. 1-Second Process Inspection Check
```bash
ps aux | grep etcd | grep client-cert-auth
# Confirms --client-cert-auth=true is actively running in the etcd daemon process arguments
```

### F. Static Pod Troubleshooting (`crictl`)
If `etcd` fails to restart after editing `/etc/kubernetes/manifests/etcd.yaml`, do not rely on `kubectl` (as the API server will be offline):
```bash
# 1. List recent etcd containers
sudo crictl ps -a --name etcd

# 2. Extract crash logs from the latest failed container
sudo crictl logs $(sudo crictl ps -a --name etcd -q | head -n1)
```
