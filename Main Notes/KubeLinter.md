---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: client-tool
domains:
  - "kubernetes"
  - "security"
related_concepts:
  - "[[trivy]]"
  - "[[kube-bench]]"
against:
  - "[[yamllint]]"
reference_guides:
  - "[[Reference Notes/0-7-5_supply_chain_security_and_imagepolicywebhook.md]]"
tags:
  - kubernetes/security
  - kubernetes/cks
  - security/supply-chain
  - status/completed
---

# KubeLinter

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security Tools > **KubeLinter**

---

## 🎯 Purpose (Why it is used)
KubeLinter is an open-source static analysis CLI tool developed by StackRox (Red Hat) that analyzes Kubernetes YAML manifests and Helm charts to identify security misconfigurations and best-practice violations before deployment.

---

## ⚙️ Functionality (What it is doing)
* **Static Rule Verification:** Audits manifest files against 50+ built-in checks targeting security contexts, container privilege levels, resource quotas, and network bindings.
* **Misconfiguration Detection:** Flags containers running as root (`runAsNonRoot: false`), missing CPU/memory limits, writable root filesystems, and insecure capabilities.
* **CI/CD Security Gating:** Integrates directly into Git workflows and CI pipelines to reject non-compliant pull requests before they reach the cluster.

---

## 🏛️ Architectural Context (How it fits in the architecture)
KubeLinter operates entirely outside the cluster on static files (Shift-Left security). It evaluates code before it reaches the `kube-apiserver`, complementing runtime admission controllers like OPA Gatekeeper or Kyverno.

---

## 🧩 Problem Solver (What problem it solves)
Fixing misconfigured manifests in production causes rollbacks and security incidents. KubeLinter catches security vulnerabilities at the developer desktop or CI runner stage, preventing misconfigured manifests from ever being applied to a cluster.

---

## 🟢 Operational Impact (What will happen with it operating)
Workloads deployed to the cluster arrive pre-hardened, dramatically reducing violation alerts from runtime admission controllers and security monitors.

---

## 🔴 Failure Impact (What will happen without it)
Developers frequently commit manifests with `privileged: true`, missing resource limits, or root execution defaults, leaving workloads exposed to container escape and node resource starvation.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **KubeLinter**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[KubeLinter]]
SORT file.name ASC
```
