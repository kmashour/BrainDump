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
*   **Multiple Secret Types:** Supports standard Opaque secrets, docker-registry credentials, TLS certificates, and ServiceAccount tokens.
*   **Dynamic Injection:** Exposes data to containers as environment variables or mounted files inside `tmpfs` (RAM-backed) volumes.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **API Server:** Validates and stores Secrets. It can encrypt secrets before writing them to etcd if encryption at rest is configured.
*   **Kubelet:** Retrieves secrets from the API server only if a Pod scheduled on its node requires it, minimizing node-level exposure. Mounted secrets are stored in memory (`tmpfs`) to prevent sensitive data from leaking to the worker node's physical disk.
*   **etcd:** Stores the final secret payloads. By default, etcd stores secrets in plaintext unless explicit encryption providers are configured.

---

## 🧩 Problem Solver (What problem it solves)
If Secrets were not used, sensitive database passwords and API keys would be hardcoded in application code, baked into Docker images, or stored in git repositories. This exposes them to developers, CI/CD logs, and attackers. Secrets store this sensitive information out-of-band and mount them dynamically only to authorized containers.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Enhanced Security:** Credentials are kept secure and separate from source code.
*   **Access Control:** Access to Secrets can be restricted using RBAC (Role-Based Access Control).
*   **Memory-only Storage:** Worker nodes store secrets in RAM-backed `tmpfs` volumes, ensuring they never touch persistent disk storage.

---

## 🔴 Failure Impact (What will happen without it)
*   **Workload Blockers:** If a Pod references a non-existent Secret, it will fail to start and stay in a `CreateContainerConfigError` or `RunContainerError` state.
*   **Security Breaches:** Credentials will be exposed in plain text within manifest repositories, logs, or image layers.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Secret**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
