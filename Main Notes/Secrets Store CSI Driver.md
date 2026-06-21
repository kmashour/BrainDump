---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
  - "storage"
related_concepts:
  - "[[secret]]"
  - "[[persistentvolume]]"
against:
  - "[[secret]]" # Mounts secrets via CSI volume rather than creating native API objects
reference_guides:
  - "[[Reference Notes/0-7_security_and_network_policies.md]]"
tags:
  - kubernetes/component
  - status/completed
---

# Secrets Store CSI Driver

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Storage > **Secrets Store CSI Driver**

---

## 🎯 Purpose (Why it is used)
The **Secrets Store CSI Driver** (Container Storage Interface) integrates external secret management platforms (such as AWS Secrets Manager, HashiCorp Vault, Google Secret Manager, Azure Key Vault) directly with Kubernetes workloads. It allows containerized applications to fetch credentials dynamically at runtime and mount them directly as file paths inside the container namespace, bypassing the creation and persistence of native Kubernetes `Secret` API objects in `etcd`.

---

## ⚙️ Functionality (What it is doing)
*   **Runtime Credential Ingestion:** Pulls secrets from the external store dynamically when a Pod is scheduled onto a worker node.
*   **Volatile Memory Mounting:** Mounts secrets as files inside a RAM-backed `tmpfs` volume, ensuring they never touch physical host disks.
*   **EKS OIDC Authorization (IRSA):** Uses projected service account credentials (via OpenID Connect) to authorize the CSI driver to fetch secrets from the cloud vault.
*   **Synchronized Native Secrets (Optional):** Can create and sync native Kubernetes Secret objects if required by certain workloads (e.g. for environment variable injection).
*   **Background Auto-rotation:** Periodically polls the external provider (e.g., every 2 minutes) to overwrite mounted files with rotated credentials.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Kubelet:** Manages volume setups. When a Pod with a CSI volume mounts, Kubelet passes the request to the CSI driver.
*   **SecretProviderClass CRD:** A Custom Resource describing the external vault provider and mapping specific secret path mappings.
*   **CSI Driver Plugin DaemonSet:** Runs on every worker node to handle mounting operations.
*   **External Store Providers:** Plugins that bridge the CSI driver to provider APIs (AWS Secrets Manager, HashiCorp Vault).

---

## 🧩 Problem Solver (What problem it solves)
Traditional Kubernetes secrets are stored in Base64 encoding in `etcd`. They require manual decryption setups, raise access control concerns, and are often pushed to Git repos accidentally. The Secrets Store CSI Driver solves this by managing credentials in a unified vault outside the cluster, mounting them at runtime, and removing the security risk of storing sensitive credentials in `etcd`.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Zero-Storage Footprint:** No persistent credentials reside in the Kubernetes API data store.
*   **Automated Rotation:** Secrets rotation in the vault automatically propagates down to Pod volumes without requiring Pod restarts.
*   **Compliance Compliance:** Eases security audits because the cluster data store has no plaintext passwords.

---

## 🔴 Failure Impact (What will happen without it)
*   **Failed Deployments:** Pods referencing missing CSI secrets will stay in `CreateContainerConfigError` or `ContainerCreating` states.
*   **WebIdentity token failures:** If OIDC annotations on ServiceAccounts are wrong, Pods fail to start with `FailedMount` warnings.
*   **Stale Credentials:** If auto-rotation is disabled, applications continue running with expired passwords even if updated in the vault.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Secrets Store CSI Driver**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
