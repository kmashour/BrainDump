---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: workload
domains:
  - "kubernetes"
related_concepts:
  - "[[secret]]"
  - "[[pod]]"
against:
  - "[[secret]]" # Secrets are used for sensitive configurations, ConfigMaps for non-sensitive ones
reference_guides:
  - "[[Reference Notes/14_scheduling_logging_and_lifecycle.md]]"
tags:
  - domain/kubernetes
  - status/completed
---

# ConfigMap

**Breadcrumbs:** [[0-Index|🏠 Index]] > workloads > **ConfigMap**

---

## 🎯 Purpose (Why it is used)
A **ConfigMap** is an API object used to store non-confidential data in key-value pairs. It allows you to decouple environment-specific configurations from container images, making applications easily portable and reusable across different environments (dev, test, prod).

---

## ⚙️ Functionality (What it is doing)
*   **Decoupled Configuration:** Stores configuration data such as application properties, parameters, and environment settings separately from container binaries.
*   **Multiple Ingestion Pathways:** Can be created from literal values, files, directories, or env files.
*   **Dynamic Injection:** Provides data to containers as environment variables, command-line arguments, or mounted files within a directory volume.
*   **Live Updates:** Mounted ConfigMaps are dynamically updated by the Kubelet without requiring a Pod restart (except when using `subPath` mounts).

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Controller Manager:** Watches for ConfigMap changes and reconciles their states in the cluster.
*   **Kubelet:** Reads ConfigMaps from the API server and injects them into Pod containers during initialization, or mounts them as read-only directories in the container file system.
*   **etcd:** Stores ConfigMap key-value payloads securely on the cluster's main key-value database.

---

## 🧩 Problem Solver (What problem it solves)
Without ConfigMaps, application configurations would have to be hardcoded into container images. Changing a simple property (like a database host URL) would require rebuilding, tagging, and redeploying the entire image. ConfigMaps separate configuration from application code, allowing the same container image to be run in different environments with zero rebuilds.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Portability:** Container images remain environment-agnostic and reusable.
*   **Centralized Config Management:** Configurations are version-controlled, managed, and audited natively via Kubernetes manifests.
*   **Dynamic Tuning:** Applications that watch mounted configuration files can dynamically reload their configurations on the fly when the ConfigMap updates.

---

## 🔴 Failure Impact (What will happen without it)
*   **Workload Failures:** Pods referencing missing ConfigMaps will fail to start, stuck in a `CreateContainerConfigError` or `RunContainerError` state.
*   **Maintenance Overhead:** Changing any application property requires code rebuilds and image redeployments.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **ConfigMap**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[configmap]]
SORT file.name ASC
```
