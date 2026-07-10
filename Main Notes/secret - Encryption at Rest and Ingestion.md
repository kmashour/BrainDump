---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[secret]]"
sub_type: core-concept
source_type: udemy
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
against: []
tags:
  - kubernetes/secret
  - kubernetes/deep-dive
---

# secret - Encryption at Rest and Ingestion

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[secret]] > **Encryption at Rest and Ingestion**

---

## 📑 Secret Creation and Ingestion

Kubernetes Secrets are stored in base64 encoding. Note that base64 is **not** encryption; it is simply a representation format.

### 1. Base64 Encoding vs. Encryption
*   **Encoding:** Converts plaintext credentials to base64.
    ```bash
    echo -n "my-password" | base64
    # Output: bXktcGFzc3dvcmQ=
    ```
*   **Decoding:** Reverts base64 back to plaintext.
    ```bash
    echo "bXktcGFzc3dvcmQ=" | base64 --decode
    # Output: my-password
    ```

### 2. Creation Commands
*   **Opaque Secret (Generic):**
    ```bash
    kubectl create secret generic db-credentials \
      --from-literal=username=admin \
      --from-literal=password=supersecure
    ```
*   **Docker Registry Secret (for private images):**
    ```bash
    kubectl create secret docker-registry private-repo-key \
      --docker-username=my-user \
      --docker-password=my-password \
      --docker-email=user@domain.com \
      --docker-server=https://index.docker.io/v1/
    ```

---

## 🔒 Encryption at Rest (etcd Protection)

By default, etcd stores cluster data in plain text, meaning anyone with raw access to etcd or control plane backups can read all Secrets. To secure secrets, configure **Encryption at Rest**.

### 1. EncryptionConfiguration
Create an `EncryptionConfiguration` file at `/etc/kubernetes/enc/enc-config.yaml` on the control plane node:
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
              secret: dXNlci1wYXNzd29yZC1zZWNyZXQta2V5LXNhbXBsZQ== # 32-byte base64 key
      - identity: {} # Fallback provider (plaintext)
```

### 2. API Server Configuration
Update the Kubeadm static pod manifest `/etc/kubernetes/manifests/kube-apiserver.yaml` to mount this configuration and enable the encryption provider:
*   **Flags:**
    ```yaml
    - --encryption-provider-config=/etc/kubernetes/enc/enc-config.yaml
    - --encryption-provider-config-automatic-reload=true # Syncs rotations without API Server restarts
    ```
*   **Volume Mounts:** Ensure the file path is mounted from the host into the API server container.

### 3. Verification of Encrypted State
To verify that a secret is encrypted inside etcd, run a raw query using `etcdctl` directly on the control plane node:
```bash
ETCDCTL_API=3 etcdctl \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  get /registry/secrets/default/db-credentials | hexdump -C
```
If encrypted, the output prefix will contain the encryption provider header (e.g., `k8s:enc:aescbc:v1:key1`) rather than the raw base64 string.

---

## ⚙️ Envelope Encryption (KMS)

For enterprise deployments, storing static keys in `/etc/kubernetes/` is a security risk. Kubernetes supports **Envelope Encryption** via a Key Management Service (KMS) plugin:
*   **DEK (Data Encryption Key):** Generated locally to encrypt the resource payload.
*   **KEK (Key Encryption Key):** Managed by an external KMS (e.g., AWS KMS, HashiCorp Vault). Kube-apiserver calls the KMS plugin over a local gRPC UNIX socket to encrypt/decrypt the DEK.
*   **Benefit:** The actual master key never resides on the control plane server disk.

*Read more in [0-7_security_and_network_policies.md](../Reference%20Notes/0-7_security_and_network_policies.md#119-etcd-encryption-at-rest--envelope-encryption)*

---

## 🔄 Ingestion & Update Propagation Mechanics

Once a Secret is created, its propagation behavior to running container environments is determined by how it is injected:

### 1. Environment Variables (Static)
*   **Behavior:** Environment variables are resolved at container startup and are **static**.
*   **Propagation:** If you modify the Secret value in the API server, the running container's environment variables **will not change**. The Pod must be deleted and recreated (e.g., via a rolling update) to pick up new values.

### 2. Volume Mounts (Dynamic via Symlink Swap)
*   **Behavior:** Mounted files are **dynamic** and periodically reconciled by Kubelet (defaults to 1-2 minutes).
*   **Propagation:** To avoid partial or dirty reads, Kubelet writes new files to a fresh timestamped directory and updates a `..data` symlink pointer atomically inside `/etc/secrets`.
*   **The `subPath` Inode Binding Gotcha:** If a Secret key is mounted to a specific file path using `volumeMounts.subPath`, **dynamic updates are disabled**. The container engine bind-mounts directly to the file's individual inode at start time, blocking the symlink swap updates.
*   *See the complete low-level systems rationale and inotify folder watch requirements in [[Reference Notes/0-13_scheduling_logging_and_lifecycle.md#Systems Rationale: Why Kubernetes Uses This Symlink-Swap Pattern|Module 13 Reference Note > Systems Rationale]].*

---

## 🛠️ Built-in Secret Types & Configurations

Kubernetes uses the `type` field to enforce validations and configurations:

| Secret Type | Required Keys in `data` | Description / Best Practices |
| :--- | :--- | :--- |
| **`Opaque`** (Default) | None | Arbitrary key-value pairs. Subcommand: `kubectl create secret generic`. |
| **`kubernetes.io/tls`** | `tls.crt`, `tls.key` | PEM-encoded certificate and private key pair for HTTPS/Ingress. |
| **`kubernetes.io/basic-auth`** | `username`, `password` | Client credentials for basic access authentication. |
| **`kubernetes.io/ssh-auth`** | `ssh-privatekey` | Private key file for automated SSH authentication. |
| **`kubernetes.io/dockerconfigjson`** | `.dockerconfigjson` | Serialized JSON file for private registry authentication. |
| **`bootstrap.kubernetes.io/token`** | `token-id`, `token-secret` | Used during `kubeadm join` for node bootstrapping trust validation. |

---

### 🌐 External Documentation Sources
*   [Kubernetes Pods Print View](https://kubernetes.io/docs/concepts/workloads/pods/_print)
*   [Kubernetes Config API Reference](https://kubernetes.io/docs/reference/config-api/_print)


