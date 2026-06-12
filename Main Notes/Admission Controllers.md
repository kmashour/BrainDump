---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
  - "security"
related_concepts:
  - "[[kube-apiserver]]"
  - "[[pod-security-admission]]"
against:
  - "[[rbac]]"
reference_guides:
  - "[[Reference Notes/admission_controllers_reference.md]]"
  - "[[Reference Notes/a_guide_to_kubernetes_admission_controllers.md]]"
tags:
  - kubernetes/admission-controllers
  - status/completed
---

# Admission Controllers

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > infra > **Admission Controllers**

---

## 🎯 Purpose (Why it is used)
**Admission Controllers** are plugins that intercept requests to the Kubernetes API server *after* authentication and authorization but *before* the object state is persisted in `etcd`. They allow clusters to enforce security policies, validate configurations, and automatically inject default values.

---

## ⚙️ Functionality (What it is doing)
*   **Request Interception:** Every write/modify request (Create, Update, Delete) is checked by the enabled admission controller chain. Read requests (Get, List, Watch) bypass them.
*   **Dual Phases:** Operating in two phases:
    1.  **Mutating Phase:** Modifies or injects defaults into the incoming request (e.g. adding a default StorageClass or injecting sidecar containers).
    2.  **Validating Phase:** Audits the final request configuration and either allows or rejects it based on custom rules (e.g. block running as root).
*   **Dynamic Extension:** Can call out to external custom webhooks (`MutatingAdmissionWebhook`, `ValidatingAdmissionWebhook`).

---

## 🏛️ Architectural Context (How it fits in the architecture)
Admission controllers run inside the `kube-apiserver` process. The order of execution is critical: mutating controllers run first, followed by validating controllers, ensuring that any mutations are validated.

---

## 🧩 Problem Solver (What problem it solves)
While RBAC controls *who* can access *what* resource, it cannot enforce *how* the resource is configured. Admission Controllers solve this by validating or altering the payload contents (e.g. blocking the `latest` image tag, enforcing resource limits, or automatically provisioning namespaces).

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Enforced Governance:** Automatically blocks non-compliant resources from entering the cluster.
*   **Autonomic Defaults:** Simplifies client requests by filling in missing values (e.g., storage class defaults).

---

## 🔴 Failure Impact (What will happen without it)
*   **Security Gaps:** Users can deploy insecure containers (e.g., root execution, host volume mounts) even if they are authorized to create pods.
*   **Configuration Drift:** Inconsistent workloads lacking standard labels, limits, or security contexts.

---

## 🛠️ Configuration & Management
To check the default enabled plugins:
```bash
kube-apiserver -h | grep enable-admission-plugins
```
Or for a `kubeadm` setup, inspect the kube-apiserver pod or manifest.

To enable/disable plugins:
Edit the `kube-apiserver` flags in `/etc/kubernetes/manifests/kube-apiserver.yaml`:
*   `--enable-admission-plugins=NodeRestriction,NamespaceLifecycle,LimitRanger,...`
*   `--disable-admission-plugins=AlwaysPullImages`

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Admission Controllers**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
