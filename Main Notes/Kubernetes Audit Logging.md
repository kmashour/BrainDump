---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "kubernetes"
  - "security"
related_concepts:
  - "[[Falco]]"
  - "[[kube-apiserver]]"
against:
  - "[[kube-bench]]"
reference_guides:
  - "[[Reference Notes/0-7-6_runtime_security_falco_and_audit_logging.md]]"
tags:
  - kubernetes/security
  - kubernetes/auditing
  - status/completed
---

# Kubernetes Audit Logging

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security > **Kubernetes Audit Logging**

---

## 🎯 Purpose (Why it is used)
**Kubernetes Audit Logging** provides a chronological, security-relevant record of actions submitted to the Kubernetes API server. It documents the provenance of every administrative operation, identity authentication, resource mutation, and controller request across the cluster for compliance and forensic analysis.

---

## ⚙️ Functionality (What it is doing)
* **Stage Tracking:** Tracks requests through up to four execution stages: `RequestReceived`, `ResponseStarted`, `ResponseComplete`, and `Panic`.
* **Granular Policy Filtering:** Enforces audit levels (`None`, `Metadata`, `Request`, `RequestResponse`) based on user identity, HTTP verbs, and target API resources.
* **Dual-Sink Delivery:** Streams structured JSON audit events to a local file sink (with log rotation parameters like maxage, maxsize, and maxbackup) or an external HTTP webhook sink.
* **Credential Protection:** Prevents credential leakage by permitting sensitive resources (`Secrets`, `ConfigMaps`) to be audited at `Metadata` level only.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Audit logging is an integral sub-system of the `kube-apiserver`. Configured via `--audit-policy-file` and `--audit-log-path`, it intercepts incoming HTTP requests immediately after the handler receives them, logging outcomes before and after they interact with the storage engine (`etcd`).

---

## 🧩 Problem Solver (What problem it solves)
Without auditing, cluster administrators cannot determine *who* deleted a production namespace, *what* service account elevated its privileges, or *when* an unauthorized user queried sensitive secrets. Audit logging establishes accountability and forensic traceability.

---

## 🟢 Operational Impact (What will happen with it operating)
Every API call is recorded with user identity, client IP, impersonated groups, requested URL, response code, and timestamp, allowing SIEM systems to correlate cluster activity and detect lateral movement.

---

## 🔴 Failure Impact (What will happen without it)
Post-incident forensic investigations are severely compromised. Security teams have no mechanism to prove whether data was modified or exfiltrated, leading to failed compliance audits (SOC2, HIPAA, PCI-DSS).

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Kubernetes Audit Logging**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
