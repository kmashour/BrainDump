---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Cluster Component Hardening and Communication Security]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Workload Hardening"
tags:
  - kubernetes/security
  - kubernetes/secrets
  - kubernetes/etcd
  - kubernetes/encryption-at-rest
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Secret Encryption at Rest: EncryptionConfiguration, Provider Chains, and etcd Verification

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Main Notes/Kubernetes Cluster Component Hardening and Communication Security|Kubernetes Cluster Component Hardening and Communication Security]] > **Kubernetes Secret Encryption at Rest: EncryptionConfiguration, Provider Chains, and etcd Verification**

---

## 💀 1. The Threat Model: Base64 is Not Encryption

In default Kubernetes deployments, `Secret` resources are merely Base64-encoded plain text stored in `etcd`. Base64 provides zero cryptographic confidentiality—it is strictly an encoding format designed to transport binary data over text-based protocols.

```
+-----------------------------------------------------------------------------------------------+
|                            UNENCRYPTED ETCD EXPLOITATION VECTORS                              |
+-----------------------------------------------------------------------------------------------+
|                                                                                               |
|  [ Attacker / Rogue Admin with Control Plane Access ]                                         |
|         │                                                                                     |
|         ├──► Vector 1: Direct File System Scraping (/var/lib/etcd)                            |
|         │    $ strings /var/lib/etcd/member/snap/db | grep -i password                        |
|         │    ---> Plaintext credentials and tokens dumped without API Server involvement      |
|         │                                                                                     |
|         ├──► Vector 2: Stolen etcd Snapshot Backups                                           |
|         │    $ etcdctl snapshot save backup.db                                                |
|         │    ---> Snapshot copied to unsecured S3 bucket; all cluster secrets exposed         |
|         │                                                                                     |
|         └──► Vector 3: Direct etcd Port 2379 Probing                                          |
|              $ etcdctl get /registry/secrets/default/app-db-pass                              |
|              ---> Returns Base64 string instantly decoded with "base64 -d"                    |
|                                                                                               |
+-----------------------------------------------------------------------------------------------+
```

To eliminate these vectors without breaking application workloads, Kubernetes implements **Envelope Encryption at Rest** within the `kube-apiserver` layer.

---

## 🏛️ 2. Architectural Mechanics: The Encryption Pipeline

Encryption at rest is executed transparently by `kube-apiserver` before writing data to `etcd` and during retrieval. Client applications and `kubectl` still see standard Base64-encoded secret manifests; the underlying storage is rendered into binary ciphertext.

```
+-----------------------------------------------------------------------------------------------+
|                               SECRET ENCRYPTION AT REST PIPELINE                              |
+-----------------------------------------------------------------------------------------------+
|                                                                                               |
|  kubectl apply -f secret.yaml                                                                 |
|         │                                                                                     |
|         ▼                                                                                     |
|  [ kube-apiserver ]                                                                           |
|         │                                                                                     |
|         ├──► 1. Authentication & Authorization (RBAC)                                         |
|         ├──► 2. Admission Controllers (Validating / Mutating)                                 |
|         │                                                                                     |
|         ├──► 3. [ Encryption Provider Engine ]                                                |
|         │       - Evaluates /etc/kubernetes/enc/enc.yaml                                      |
|         │       - Writes: Encrypts payload using the FIRST provider in list                   |
|         │       - Prepends envelope prefix: "k8s:enc:<provider>:v1:<key-name>:"               |
|         │                                                                                     |
|         ▼                                                                                     |
|  [ etcd Database ] ──► Stores Ciphertext (/registry/secrets/<ns>/<name>)                      |
|                                                                                               |
|  ===========================================================================================  |
|                                                                                               |
|  kubectl get secret <name> -o yaml                                                            |
|         │                                                                                     |
|         ▼                                                                                     |
|  [ kube-apiserver ]                                                                           |
|         │                                                                                     |
|         ├──► 1. Reads raw bytes from etcd                                                     |
|         ├──► 2. Inspects prefix ("k8s:enc:aescbc:v1:key1:")                                   |
|         ├──► 3. Tries providers TOP-TO-BOTTOM until matching key decrypts data                 |
|         └──► 4. Returns standard Base64 JSON/YAML to user                                     |
|                                                                                               |
+-----------------------------------------------------------------------------------------------+
```

---

## ⚙️ 3. The Top-to-Bottom Provider Chain Rule

The `EncryptionConfiguration` file evaluates providers using a strict hierarchical rule:

1. **Write Operations (Encryption):**
   - The API Server **always** uses the **first provider** in the `providers: []` array to encrypt newly created or updated secrets.
2. **Read Operations (Decryption):**
   - The API Server attempts to decrypt data by iterating through the provider list from **top to bottom**.
3. **The `identity` Provider:**
   - Represents unencrypted plain text.
   - If `identity: {}` is placed at the top, new secrets are written in plaintext.
   - If `identity: {}` is placed at the bottom, existing unencrypted secrets remain readable while all new secrets are encrypted.

### Supported Encryption Providers

```
+---------------------------------------------------------------------------------------------------+
|                                 KUBERNETES ENCRYPTION PROVIDERS                                   |
+---------------------------------------------------------------------------------------------------+
| PROVIDER   | ALGORITHM        | KEY SIZE   | PREFIX & CHARACTERISTICS                             |
+------------+------------------+------------+------------------------------------------------------+
| aescbc     | AES-CBC          | 32 bytes   | k8s:enc:aescbc:v1:<key>:                             |
|            | (PKCS#7 padding) | (256-bit)  | Standard CKS Exam provider. Simple, performant.      |
+------------+------------------+------------+------------------------------------------------------+
| secretbox  | XSalsa20 +       | 32 bytes   | k8s:enc:secretbox:v1:<key>:                          |
|            | Poly1305 MAC     | (256-bit)  | High-speed stream cipher; excellent on ARM/non-AESNI.|
+------------+------------------+------------+------------------------------------------------------+
| aesgcm     | AES-GCM          | 16/24/32 B | k8s:enc:aesgcm:v1:<key>:                             |
|            | (Authenticated)  |            | Requires key rotation every ~200,000 writes.         |
+------------+------------------+------------+------------------------------------------------------+
| kms        | Remote Envelope  | Variable   | k8s:enc:kms:v1:<key>:                                |
|            | (v1 or v2)       |            | Enterprise gold standard (AWS KMS, GCP KMS, Vault).  |
+------------+------------------+------------+------------------------------------------------------+
| identity   | None (Plaintext) | 0 bytes    | No prefix. Crucial fallback during migration.        |
+---------------------------------------------------------------------------------------------------+
```

---

## 🛠️ 4. End-to-End Implementation Recipe (CKS Real Exam Blueprint)

### Step 1: Generate a 32-Byte Base64 Key
Generate a cryptographically secure 32-byte (256-bit) string:
```bash
head -c 32 /dev/urandom | base64
# Example output: cU3Mh9K2vL6wP5zY1xT8oR7qE4sW0jA2bC5dE8fG1hI=
```

### Step 2: Create the `EncryptionConfiguration` File
On the control plane node, create `/etc/kubernetes/enc/enc.yaml`:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
    providers:
      - aescbc:
          keys:
            - name: key1
              secret: cU3Mh9K2vL6wP5zY1xT8oR7qE4sW0jA2bC5dE8fG1hI=
      - identity: {}
```

> [!WARNING]
> Do NOT omit `identity: {}` during initial rollout. If omitted, `kube-apiserver` will fail to read all existing unencrypted cluster secrets, causing control plane pod crashes and webhook auth failures.

### Step 3: Wire into `kube-apiserver.yaml`
Edit `/etc/kubernetes/manifests/kube-apiserver.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
  - command:
    - kube-apiserver
    # 1. Add CLI flag pointing to configuration
    - --encryption-provider-config=/etc/kubernetes/enc/enc.yaml
    volumeMounts:
    # 2. Add container volumeMount
    - name: enc-config
      mountPath: /etc/kubernetes/enc
      readOnly: true
  volumes:
  # 3. Add hostPath volume definition
  - name: enc-config
    hostPath:
      path: /etc/kubernetes/enc
      type: DirectoryOrCreate
```

Save and exit. Kubelet monitors `/etc/kubernetes/manifests` inotify events and automatically terminates and relaunches `kube-apiserver`.

### Step 4: Verify API Server Recovery
Monitor the static pod until it returns to ready state:
```bash
kubectl get pods -n kube-system -l component=kube-apiserver
```
*(If the API server does not start, inspect container logs: `sudo crictl ps -a | grep apiserver` followed by `sudo crictl logs <id>`)*.

### Step 5: The Critical Re-Encryption Phase
Enabling encryption does **not** retrospectively alter data already stored in etcd. Existing secrets remain in plaintext until overwritten.

To re-encrypt all secrets across all namespaces:
```bash
kubectl get secrets -A -o json | kubectl replace -f -
```

---

## 🔍 5. Verification: Direct etcd Data Inspection

To verify that encryption is physically active on disk, inspect etcd using `etcdctl`:

```bash
# 1. Create a test secret
kubectl create secret generic test-sec --from-literal=pass=Confidential123

# 2. Query etcd directly bypassing the API server
ETCDCTL_API=3 etcdctl \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  get /registry/secrets/default/test-sec | hexdump -C
```

### Encrypted Output Signature
```text
00000000  2f 72 65 67 69 73 74 72  79 2f 73 65 63 72 65 74  |/registry/secret|
00000010  73 2f 64 65 66 61 75 6c  74 2f 74 65 73 74 2d 73  |s/default/test-s|
00000020  65 63 0a 6b 38 73 3a 65  6e 63 3a 61 65 73 63 62  |ec.k8s:enc:aescb|
00000030  63 3a 76 31 3a 6b 65 79  31 3a a3 91 f8 b2 c0 41  |c:v1:key1:.....A|
```

The string **`k8s:enc:aescbc:v1:key1:`** confirms:
1. Provider `aescbc` was invoked.
2. Version schema `v1` was used.
3. Key named `key1` encrypted the payload.
4. The remaining bytes are ciphertext.

---

## 🔄 6. Zero-Downtime Key Rotation Lifecycle

When rotating keys, follow this three-phase sequence to prevent data loss:

```
+-----------------------------------------------------------------------------------------------+
|                            ZERO-DOWNTIME KEY ROTATION PHASES                                  |
+-----------------------------------------------------------------------------------------------+
|                                                                                               |
|  PHASE 1: Add New Key as Primary (Top of List)                                                |
|  ---------------------------------------------                                                |
|  providers:                                                                                   |
|    - aescbc:                                                                                  |
|        keys:                                                                                  |
|          - name: key2  # <--- NEW KEY: Encrypts all subsequent writes                         |
|            secret: <NEW_BASE64_KEY>                                                           |
|          - name: key1  # <--- OLD KEY: Retained for decrypting older secrets                  |
|            secret: <OLD_BASE64_KEY>                                                           |
|    - identity: {}                                                                             |
|                                                                                               |
|  PHASE 2: Force Re-encryption Across Cluster                                                  |
|  -------------------------------------------                                                  |
|  $ kubectl get secrets -A -o json | kubectl replace -f -                                      |
|  ---> All existing secrets are read using key1, re-encrypted using key2, and saved to etcd.   |
|                                                                                               |
|  PHASE 3: Retire Old Key                                                                      |
|  -----------------------                                                                      |
|  providers:                                                                                   |
|    - aescbc:                                                                                  |
|        keys:                                                                                  |
|          - name: key2  # Only key2 remains active                                             |
|            secret: <NEW_BASE64_KEY>                                                           |
|    - identity: {}                                                                             |
|  Restart kube-apiserver. Key rotation complete with zero downtime.                            |
|                                                                                               |
+-----------------------------------------------------------------------------------------------+
```

---

## 🔗 Related Master Notes & References
- Parent Landing Note: [[Main Notes/Kubernetes Cluster Component Hardening and Communication Security|Kubernetes Cluster Component Hardening and Communication Security]]
- Component Auth & PKI: [[Main Notes/Kubernetes Component Security - Kubelet Port 10250, etcd Client Auth, and mTLS Handshake Mechanics|Kubelet Port 10250, etcd Client Auth, and mTLS Handshake Mechanics]]
- API Server Hardening: [[Main Notes/Kubernetes API Server Security - Request Lifecycle, NodeRestriction, and Protected Namespaces|API Server Security, NodeRestriction & Protected Namespaces]]
- Workload Hardening: [[Main Notes/Kubernetes Workload Security and Container Hardening|Workload Security & Container Hardening]]
- Reference Guide: [[Reference Notes/0-7-8_cluster_hardening_cis_benchmarks_and_upgrades.md|Module 0-7-8: CIS Benchmarks & Cluster Hardening]]
