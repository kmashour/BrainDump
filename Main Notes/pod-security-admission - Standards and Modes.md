---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod-security-admission]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/security/pod-security-admission/"
author: "Kubernetes Authors"
course_title: "Kubernetes Security Hardening"
tags:
  - kubernetes/security
  - kubernetes/deep-dive
---

# pod-security-admission - Standards and Modes

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[pod-security-admission]] > **Standards and Modes**

---

## 📑 Pod Security Standards (PSS) Levels

Kubernetes classifies Pod safety into three distinct standard profiles:
1. **`privileged`:** Unrestricted profile. Provides the widest level of permissions, letting containers bypass normal kernel namespace isolation and run with root capabilities.
2. **`baseline`:** Default profile. Prevents known privilege escalations, restricting hostpath volume mounts and host network access while still allowing standard root UID operations.
3. **`restricted`:** Hardened profile. Requires strictly secure workloads (must run as non-root, drop all Linux capabilities, and use read-only root filesystems).

---

## ⚙️ Pod Security Admission Modes

PSA applies PSS configurations to namespaces using three evaluation modes:
* **`enforce`:** The API server immediately rejects any Pod resource creation requests that violate the target standard.
* **`warn`:** The API server accepts the creation request but returns a user-facing HTTP warning header to notify client tools (e.g. CLI warnings during `kubectl apply`).
* **`audit`:** The API server accepts the request and appends an audit event to the cluster audit logs for tracking.

---

## ⚠️ Namespace Configuration and Label Escalation Risk

PSA policies are applied dynamically by labeling namespaces:
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: secured-apps
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: v1.30
    pod-security.kubernetes.io/warn: baseline
    pod-security.kubernetes.io/warn-version: latest
```

> [!CAUTION]
> **Privilege Escalation Vector:** Users with `patch` or `update` access on Namespace resources (e.g. application developers with local namespace Roles) can modify these labels. A malicious actor could patch the namespace labels to downgrade enforcement to `privileged`, allowing them to deploy highly insecure containers to compromise the worker node. Access to Namespace modifications must be strictly audited and protected via RBAC.

*Read more in [08_security_and_network_policies.md](../Reference%20Notes/08_security_and_network_policies.md#12-pod-security-admission-psa-and-standards)*
