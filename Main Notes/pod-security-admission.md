---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
related_concepts:
  - "[[pod]]"
  - "[[namespace]]"
against:
  - "[[rbac]]"
reference_guides:
  - "[[Reference Notes/0-7_security_and_network_policies.md]]"
tags:
  - kubernetes/security
  - status/completed
---

# Pod Security Admission

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > infra > **Pod Security Admission**

---

## 🎯 Purpose (Why it is used)
**Pod Security Admission (PSA)** is the built-in admission controller that implements the Pod Security Standards (PSS) at the namespace level. It replaces the deprecated PodSecurityPolicy (PSP) to enforce security boundaries on Pod specifications during creation.

---

## ⚙️ Functionality (What it is doing)
*   **Standards Enforcement:** Evaluates Pod configurations against three security levels: `privileged`, `baseline`, and `restricted`.
*   **Flexible Auditing:** Provides three validation modes: `enforce` (rejections), `warn` (header alerts), and `audit` (audit logging).
*   **Namespace Configuration:** Operates dynamically via labels assigned to individual namespaces.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Admission Control:** Executes in the admission phase of the `kube-apiserver` request pipeline.
*   **Namespace Boundaries:** Relies on namespace metadata labels to identify the target security policies.

---

## 🧩 Problem Solver (What problem it solves)
Without PSA, users could bypass namespace isolation by deploying privileged Pods that access host devices, read host files, or run as root. PSA solves this by providing native, out-of-the-box admission policies to enforce standard container isolation profiles.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Hardened Environments:** Enforces that default namespaces conform to least-privilege security contexts.
*   **Safe Migrations:** Warnings allow users to identify compliance violations before enforcing blockages.

---

## 🔴 Failure Impact (What will happen without it)
*   **Privilege Escalation:** Compromised containers can easily gain root host access or escape runtime namespaces.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Pod Security Admission**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), "pod-security-admission")
SORT file.name ASC
```
