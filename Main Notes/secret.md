---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
related_concepts:
  - "[[configmap]]"
  - "[[pod]]"
against:
  - "[[configmap]]" # Secrets are used for sensitive configurations, ConfigMaps for non-sensitive ones
reference_guides:
  - "[[Reference Notes/0-7_security_and_network_policies.md]]"

tags:
  - domain/kubernetes
  - status/completed
---

# Secret

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > workloads > **Secret**

---

## 🎯 Purpose (Why it is used)
A **Secret** is an API object used to store and manage sensitive information, such as passwords, OAuth tokens, SSH keys, and TLS certificates. Using Secrets avoids exposing sensitive credentials in application manifests, shell histories, or container images.

---

## ⚙️ Functionality (What it is doing)
*   **Sensitive Data Isolation:** Stores sensitive payloads separately from code and configurations.
*   **Encoding:** Data is stored in base64 encoding to support binary files and arbitrary character sets.
*   **Multiple Secret Types:** Supports standard Opaque secrets, `kubernetes.io/dockerconfigjson` credentials, `kubernetes.io/tls` certificates, `kubernetes.io/basic-auth`, `kubernetes.io/ssh-auth`, and legacy `kubernetes.io/service-account-token`.
*   **Dynamic Injection:** Exposes data to containers as environment variables or mounted files inside `tmpfs` (RAM-backed) volumes.
*   **Immutable Secrets:** Supports marking secrets as immutable (`immutable: true`). Once set, contents cannot be changed (requires deletion/re-creation). This optimizes cluster performance by allowing Kubelet to skip setting up watches on those secrets.
*   **Size Constraint:** Limits individual Secret size to **1MiB** to protect the API server and Kubelet from memory exhaustion.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **API Server:** Validates and stores Secrets. It can encrypt secrets before writing them to etcd if encryption at rest is configured.
*   **Kubelet:** Retrieves secrets from the API server only if a Pod scheduled on its node requires it (least-privilege node distribution).
*   **tmpfs Storage:** Mounted secrets are stored in a volatile memory-backed filesystem (`tmpfs`) on the node, ensuring sensitive decrypted data never touches persistent physical disks.
*   **Garbage Collection:** Once the Pod depending on the Secret is deleted, Kubelet immediately purges its local copy of the secret data from memory.
*   **etcd:** Stores the final secret payloads. By default, etcd stores secrets in plaintext unless explicit encryption providers are configured.
*   **ServiceAccount Token Evolution (Evolutionary Bridge):**
    *   *Legacy Approach:* `kubernetes.io/service-account-token` Secrets are static, have infinite lifetimes, and remain stored in etcd indefinitely.
    *   *Modern Approach (v1.22+):* Uses **ServiceAccount Token Projection** via the `TokenRequest` API. Tokens are short-lived, automatically rotated, and bound directly to the lifecycle of the Pod (deleted automatically when the Pod terminates).

---

## 🧩 Problem Solver (What problem it solves)
If Secrets were not used, sensitive database passwords and API keys would be hardcoded in application code, baked into Docker images, or stored in git repositories. This exposes them to developers, CI/CD logs, and attackers. Secrets store this sensitive information out-of-band and mount them dynamically only to authorized containers.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Enhanced Security:** Credentials are kept secure and separate from source code.
*   **Access Control:** Access to Secrets can be restricted using RBAC (Role-Based Access Control) at the namespace level.
*   **Memory-only Storage:** Worker nodes store secrets in RAM-backed `tmpfs` volumes, ensuring they never touch persistent disk storage.
*   **API Server Resource Optimization:** Using immutable secrets drastically reduces API server watch connections in large clusters.

---

## 🔴 Failure Impact (What will happen without it)
*   **Workload Blockers:** If a Pod references a non-existent or misconfigured Secret, it will fail to start and stay in a `CreateContainerConfigError` or `RunContainerError` state.
*   **Security Breaches:** Credentials will be exposed in plain text within manifest repositories, logs, or image layers.

---

## ⚙️ Operational Workflow

### 1. Creating Secrets
*   **From Literal Values (Imperative):**
    ```bash
    kubectl create secret generic db-secret --from-literal=password="password123"
    ```
*   **From Files:**
    ```bash
    kubectl create secret generic ssh-key-secret --from-file=id_rsa=~/.ssh/id_rsa
    ```

### 2. Injecting into Pods
*   **Environment Variables (`valueFrom`):**
    ```yaml
    env:
      - name: DB_PASSWORD
        valueFrom:
          secretKeyRef:
            name: db-secret
            key: password
    ```
*   **Bulk Ingestion (`envFrom`):**
    ```yaml
    envFrom:
      - secretRef:
          name: db-secret
    ```
*   **Volume Mounts (RAM-backed `tmpfs`):**
    ```yaml
    spec:
      containers:
        - name: app
          image: nginx
          volumeMounts:
            - name: secret-vol
              mountPath: /etc/secrets
              readOnly: true
      volumes:
        - name: secret-vol
          secret:
            secretName: db-secret
    ```

---


## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Secret**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
