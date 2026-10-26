---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "kubernetes"
related_concepts:
  - "[[Reference Notes/0-7-2_pod_security_standards_and_admission.md]]"
  - "[[Reference Notes/0-16_admission_controllers.md]]"
against:
  - "[[Reference Notes/0-7-2_pod_security_standards_and_admission.md#2-historical-architecture-pod-security-policy-psp-v13--v125]]"
reference_guides:
  - "[[Reference Notes/0-7-2_pod_security_standards_and_admission.md]]"
tags:
  - kubernetes/security
  - kubernetes/admission-control
  - status/completed
---

# Kubernetes Pod Security and Policy Engines

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security > **Kubernetes Pod Security and Policy Engines**

---

## 🎯 Purpose (Why it is used)
Kubernetes Pod Security and Policy Engines provide declarative admission-time boundaries that prevent insecure, misconfigured, or over-privileged workloads from ever reaching execution on cluster worker nodes. They establish guardrails so that application developers cannot accidentally or maliciously compromise host nodes, access sensitive hardware, or breach corporate compliance standards.

---

## ⚙️ Functionality (What it is doing)
1. **Admission Interception:** Intercepts API requests after authentication and authorization but *before* objects are persisted to `etcd`.
2. **Standard Hardening Enforcement (PSA):** Evaluates Pod specifications against predefined, opinionated security profiles (`Privileged`, `Baseline`, `Restricted`) at the namespace boundary.
3. **Tri-Mode Operational Auditing:** Supports `enforce` (blocking requests), `warn` (terminal feedback), and `audit` (audit logging) modes for zero-downtime policy rollouts.
4. **Custom Enterprise Validation (OPA/Kyverno):** Validates and mutates arbitrary Kubernetes resources (Ingress, Services, Namespaces) to enforce business rules like trusted image registries, mandatory billing tags, and network isolation.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Policy enforcement sits inside the `kube-apiserver` pipeline. Built-in **Pod Security Admission (PSA)** runs as an internal admission plugin evaluating namespace labels. External engines (**OPA Gatekeeper** and **Kyverno**) operate as dynamic Validating and Mutating Admission Webhooks communicating with the API server over HTTPS/mTLS.

```
+-----------------------------------------------------------------------------------+
|                        ADMISSION POLICY PIPELINE ARCHITECTURE                     |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  kubectl / Client                                                                 |
|         │                                                                         |
|         ▼                                                                         |
|  [ kube-apiserver ]                                                               |
|         │                                                                         |
|         ├──► 1. Authentication & Authorization (RBAC)                             |
|         │                                                                         |
|         ├──► 2. Built-in Admission: Pod Security Admission (PSA)                  |
|         │       Evaluates: namespace labels (enforce/warn/audit)                  |
|         │       Tiers: Privileged, Baseline, Restricted                           |
|         │                                                                         |
|         ├──► 3. Dynamic Webhooks: OPA Gatekeeper / Kyverno                        |
|         │       Evaluates: Custom Rego / YAML policies across all resources       |
|         │                                                                         |
|         ▼                                                                         |
|    [ etcd ] ──► (Persisted to Cluster State)                                      |
+-----------------------------------------------------------------------------------+
```

---

## 🧩 Problem Solver (What problem it solves)
* **Eliminates the "Root Takeover" Vector:** Without policy enforcement, any user with `create pods` permissions can launch a container with `privileged: true` or mount host `/` via `hostPath`, completely owning the underlying host node.
* **Prevents Cluster-Wide Outages (Post-PSP Era):** Replaces the brittle, deprecated `PodSecurityPolicy` (PSP) model with standardized, namespace-scoped controls that do not require complex RBAC role bindings.
* **Solves Multi-Tenancy Governance:** Allows platform teams to isolate hostile or untrusted tenants safely without building proprietary API filters.

---

## 🟢 Operational Impact (What will happen with it operating)
* Applications meeting the designated standard deploy transparently without administrative intervention.
* Developers submitting non-compliant pods receive immediate, actionable validation errors at the CLI (`kubectl apply`), detailing exact violations (e.g. `allowPrivilegeEscalation must be false`).
* Security and audit logs capture non-compliant attempts without impacting production uptime.

---

## 🔴 Failure Impact (What will happen without it)
* **Host OS Compromise:** Malicious or compromised containers can break out to the host, steal node IAM credentials (IMDS), and access raw host storage.
* **Configuration Drift & Cost Spikes:** Without policy engines, developers can launch untracked cloud load balancers, pull unvetted images from public registries, and run containers with root privileges.

---

## 🔍 Deeper Dive Notes
This table automatically indexes all detailed breakdowns, architectural evolutions, and deep dives associated with **Kubernetes Pod Security and Policy Engines**:

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```

### Core Architecture & Mechanics
- [[Main Notes/Kubernetes Pod Security Admission - Restricted Standards, Pod Creation Control Flow, and ReplicaSet Debugging.md|Kubernetes Pod Security Admission: Restricted Standards, Pod Creation Control Flow, and ReplicaSet Debugging]]

*Related Reference Module:* [[Reference Notes/0-7-2_pod_security_standards_and_admission.md|Module 0-7-2: Pod Security Standards, PSP & PSA Masterclass]]

