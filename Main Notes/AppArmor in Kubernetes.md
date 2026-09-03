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
  - "[[Seccomp in Kubernetes]]"
  - "[[pod-security-admission]]"
against:
  - "[[gVisor and Sandboxed Containers]]"
reference_guides:
  - "[[Reference Notes/0-7-7_system_hardening_seccomp_apparmor_and_syscalls.md]]"
tags:
  - kubernetes/security
  - linux/apparmor
  - status/completed
---

# AppArmor in Kubernetes

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Linux Security > **AppArmor in Kubernetes**

---

## 🎯 Purpose (Why it is used)
**AppArmor** is a Linux Security Module (LSM) that provides Mandatory Access Control (MAC) based on program path names. In Kubernetes, AppArmor profiles restrict container access to host filesystems, network protocols, and process execution, ensuring that even processes running as root (`UID 0`) cannot access unauthorized system resources.

---

## ⚙️ Functionality (What it is doing)
* **Path-Based Confinement:** Restricts read, write, and execute permissions for specific file directories and path patterns.
* **Kernel-Level Enforcement:** Evaluates operations directly within the Linux kernel before syscall execution.
* **Dual Operating Modes:** Can operate in `enforce` mode (actively blocking violations) or `complain` mode (logging violations without blocking).
* **Native SecurityContext Integration:** In Kubernetes v1.30+, configured via the container's native `securityContext.appArmorProfile` field (`type: Localhost` or `type: RuntimeDefault`).

---

## 🏛️ Architectural Context (How it fits in the architecture)
AppArmor profiles must be pre-loaded into the Linux kernel on each worker node (via `apparmor_parser -q /etc/apparmor.d/<profile>`). Kubernetes manifests then instruct the container runtime (via Kubelet) to apply the loaded profile to the target container at startup.

---

## 🧩 Problem Solver (What problem it solves)
Standard Linux Discretionary Access Control (DAC) grants all capabilities to the `root` user. If an attacker gains root privileges inside a container, DAC cannot prevent them from writing to mounted host volumes or modifying sensitive application binaries. AppArmor overrides root authority, strictly preventing forbidden actions.

---

## 🟢 Operational Impact (What will happen with it operating)
Containerized processes are confined to their declared operating requirements. Attempts to execute unauthorized binaries (such as `/bin/sh` or `/usr/bin/curl`) or tamper with configurations are blocked with `Permission denied`.

---

## 🔴 Failure Impact (What will happen without it)
A compromised container running as root has complete write and execution permissions over any accessible mount or directory, simplifying lateral compromise.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **AppArmor in Kubernetes**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
