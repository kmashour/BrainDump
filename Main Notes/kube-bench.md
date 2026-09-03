---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - "kubernetes"
  - "security"
related_concepts:
  - "[[Kubernetes Audit Logging]]"
  - "[[Falco]]"
against:
  - "[[Trivy]]"
reference_guides:
  - "[[Reference Notes/0-7-7_system_hardening_seccomp_apparmor_and_syscalls.md]]"
tags:
  - kubernetes/security
  - kubernetes/cis-benchmarks
  - status/completed
---

# kube-bench

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security > **kube-bench**

---

## 🎯 Purpose (Why it is used)
**kube-bench** is an automated auditing tool developed by Aqua Security to inspect Kubernetes clusters against the security recommendations documented in the **Center for Internet Security (CIS) Kubernetes Benchmark**. It validates whether host configurations, file permissions, daemon flags, and admission controllers adhere to industry-standard hardening baselines.

---

## ⚙️ Functionality (What it is doing)
* **Automated CIS Rule Verification:** Runs automated checks across control plane master nodes, worker nodes, and etcd clusters based on declarative YAML test specifications.
* **Granular Status Reporting:** Outputs test outcomes categorized as `[PASS]`, `[FAIL]`, `[WARN]`, or `[INFO]`.
* **Actionable Remediation Guidance:** For each failed test, outputs exact CLI commands or configuration edits (e.g., `chmod 600`, `--anonymous-auth=false`) necessary to achieve compliance.

---

## 🏛️ Architectural Context (How it fits in the architecture)
kube-bench operates as an out-of-band administrative scanning utility. It can be run either as a stand-alone Go binary on the host Linux OS, or executed as a Kubernetes Job with mounted host directories (`/etc/kubernetes`, `/var/lib/etcd`, `/var/lib/kubelet`).

---

## 🧩 Problem Solver (What problem it solves)
Manual verification of the 100+ configuration parameters across Kubernetes control plane daemons (`kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, `etcd`, `kubelet`) is error-prone and time-consuming. kube-bench automates this entire audit in seconds, identifying insecure defaults like unauthenticated Kubelet ports or permissive file ownerships.

---

## 🟢 Operational Impact (What will happen with it operating)
Engineers receive immediate, objective compliance assessments. Clusters pass regulatory security audits (SOC2, PCI-DSS, ISO27001) by ensuring CIS recommendations are systematically enforced.

---

## 🔴 Failure Impact (What will happen without it)
Without kube-bench, clusters commonly run with default, insecure configuration flags—such as anonymous Kubelet access, plaintext etcd communication, or unhardened static pod manifests—leaving the control plane vulnerable to privilege escalation.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **kube-bench**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
