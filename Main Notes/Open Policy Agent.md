---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
domains:
  - "kubernetes"
  - "security"
related_concepts:
  - "[[admission-controllers]]"
  - "[[pod-security-standards]]"
against:
  - "[[pod-security-policies]]"
reference_guides:
  - "[[Reference Notes/0-7-2_pod_security_standards_and_admission.md]]"
tags:
  - kubernetes/security
  - kubernetes/cks
  - security/policy
  - status/completed
---

# Open Policy Agent

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Governance > **Open Policy Agent**

---

## 🎯 Purpose (Why it is used)
Open Policy Agent (OPA) is an open-source, general-purpose policy engine that enables unified, context-aware policy enforcement across microservices, Kubernetes clusters, and CI/CD pipelines. Through its Kubernetes implementation (**Gatekeeper**), OPA decouples policy definition from application code.

---

## ⚙️ Functionality (What it is doing)
* **Declarative Policy Logic:** Uses **Rego**, a high-level declarative query language designed to express complex constraints over structured JSON/YAML data.
* **Admission Interception:** Intercepts Kubernetes API creation, modification, and deletion requests via validating and mutating admission webhooks.
* **Audit & Drift Detection:** Continuously evaluates live cluster resources against constraints to identify existing non-compliant objects.
* **Custom Resource Management:** Provides `ConstraintTemplate` (the policy logic) and `Constraint` (the policy parameters and enforcement scope) CRDs.

---

## 🏛️ Architectural Context (How it fits in the architecture)
In Kubernetes, OPA runs as the Gatekeeper controller. When a client issues a request to `kube-apiserver`, the API server sends an `AdmissionReview` payload to Gatekeeper. Gatekeeper evaluates the object against active Rego policies and returns an admission decision.

---

## 🧩 Problem Solver (What problem it solves)
Standard Kubernetes RBAC and Pod Security Admission only enforce fixed, built-in rules. OPA solves complex organizational governance needs, such as mandating specific cost-allocation labels, blocking public ingress hostnames, or restricting external image registries.

---

## 🟢 Operational Impact (What will happen with it operating)
Cluster administrators can declaratively codify compliance rules across all teams. Developers receive immediate, detailed violation feedback upon running `kubectl apply`.

---

## 🔴 Failure Impact (What will happen without it)
Policy enforcement relies on manual peer reviews or post-deployment audits, resulting in security drift, unlabelled resources, and unauthorized external ingress routes.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Open Policy Agent**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[Open Policy Agent]]
SORT file.name ASC
```
