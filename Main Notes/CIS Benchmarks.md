---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "kubernetes"
  - "security"
  - "linux"
related_concepts:
  - "[[kube-bench]]"
  - "[[Kubernetes Audit Logging]]"
against:
  - "[[Falco]]"
reference_guides:
  - "[[Reference Notes/0-7-7_system_hardening_seccomp_apparmor_and_syscalls.md]]"
tags:
  - kubernetes/security
  - kubernetes/cis-benchmarks
  - status/completed
---

# CIS Benchmarks

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security > **CIS Benchmarks**

---

## 🎯 Purpose (Why it is used)
**CIS Benchmarks (Center for Internet Security Benchmarks)** are globally recognized, consensus-driven cybersecurity standards and configuration baselines. In Kubernetes and Linux environments, CIS Benchmarks define prescriptive guidance to secure operating systems, container runtimes, and control plane daemons against unauthorized access and privilege escalation.

---

## ⚙️ Functionality (What it is doing)
* **Prescriptive Hardening Recommendations:** Details exact configuration flags, permissions, and security parameters across master nodes, worker nodes, etcd, and control plane daemons.
* **Scored vs. Unscored Controls:** Categorizes checks into scored guidelines (which must be met for automated compliance scoring) and unscored recommendations (requiring contextual organizational review).
* **Audit & Remediation Verification:** Provides step-by-step shell commands to audit running daemons and apply necessary configuration fixes.

---

## 🏛️ Architectural Context (How it fits in the architecture)
CIS Benchmarks serve as the baseline security policy across all four layers of the 4Cs model. Tools such as `kube-bench` automate the audit and verification of these benchmarks across the cluster.

---

## 🧩 Problem Solver (What problem it solves)
Default configurations for distributed open-source software prioritize simplicity and backward compatibility over defensive security. CIS Benchmarks eliminate guesswork by providing comprehensive, peer-reviewed hardening checklists.

---

## 🟢 Operational Impact (What will happen with it operating)
Systems operate under an established, defensive security baseline with minimized attack surfaces, passing compliance audits (SOC2, PCI-DSS, ISO27001, HIPAA).

---

## 🔴 Failure Impact (What will happen without it)
Infrastructure suffers from configuration drift and permissive default flags (e.g. anonymous API access, insecure TLS ciphers, world-readable keys), allowing attackers to achieve easy lateral movement.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **CIS Benchmarks**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
