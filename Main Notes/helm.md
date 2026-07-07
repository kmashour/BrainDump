---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: packager
domains:
  - "kubernetes"
  - "devops"
related_concepts:
  - "[[kubernetes]]"
  - "[[kubectl]]"
against:
  - "[[kustomize]]"
reference_guides:
  - "[[Reference Notes/12-3_helm_package_management.md]]"
tags:
  - kubernetes/package-manager
  - status/completed
---

# helm

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Kubernetes > **helm**

---

## 🎯 Purpose (Why it is used)
Helm is the package manager for Kubernetes. It simplifies the definition, installation, upgrading, and lifecycle management of complex cloud-native applications on a cluster by bundling individual Kubernetes manifest resources (Deployments, Services, ConfigMaps, Secrets, etc.) into unified, version-controlled packages called **Charts**.

---

## ⚙️ Functionality (What it is doing)
*   **Manifest Templating:** Parametrizes static Kubernetes YAML manifests, allowing variables to be injected dynamically from a central `values.yaml` file.
*   **Release Management:** Deploys charts as discrete named instances called **Releases** and tracks their lifecycle across multiple version revisions.
*   **Dependency Management:** Resolves and installs sub-charts and database layers required by an application natively using the `dependencies` spec.
*   **State Reconciliation:** Stores release metadata securely inside the cluster as Kubernetes Secrets to track historical state snapshots.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Client-Only Model (Helm 3):** Exists as a CLI tool on the administrator's workstation. It directly connects to the Kubernetes API server, using the active `kubeconfig` context and respecting standard **RBAC** security policies.
*   **Registry Ecosystem:** Pulls versioned packages from local or remote chart registries (e.g., Artifact Hub) and packages them as local directories or compressed tarballs.

---

## 🧩 Problem Solver (What problem it solves)
*   **Microservice Sprawl:** Solves the operational bottleneck of manually applying (`kubectl apply -f`) and tracking dozens of disconnected YAML resource manifests for a single application stack.
*   **Parameter Redundancy:** Prevents configuration drift and errors by exposing a single configuration interface (`values.yaml`) instead of forcing developers to search and replace values across multiple raw YAML files.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Single-Command Orchestration:** Entire application tiers can be installed, updated, or uninstalled with single commands (`helm install`, `helm upgrade`, `helm uninstall`).
*   **Safe Rollbacks:** Allows operators to return a broken deployment back to a known-healthy state revision (`helm rollback`) using a three-way strategic merge patch.

---

## 🔴 Failure Impact (What will happen without it)
*   Without Helm, administrators must manage Kubernetes configurations using raw YAML, manual shell scripting, or alternative templating tools (like Kustomize), which increases configuration drift risk and complicates version rollbacks.
*   If the local Helm client is misconfigured, releases can conflict with existing namespace resources or fail to install due to RBAC privilege mismatches on the API Server.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and configurations associated with **helm**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
