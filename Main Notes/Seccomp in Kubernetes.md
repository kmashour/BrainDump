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
  - "[[AppArmor in Kubernetes]]"
  - "[[Falco]]"
against:
  - "[[gVisor and Sandboxed Containers]]"
reference_guides:
  - "[[Reference Notes/0-7-7_system_hardening_seccomp_apparmor_and_syscalls.md]]"
tags:
  - kubernetes/security
  - linux/seccomp
  - status/completed
---

# Seccomp in Kubernetes

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Linux Security > **Seccomp in Kubernetes**

---

## 🎯 Purpose (Why it is used)
**Seccomp (Secure Computing Mode)** is a Linux kernel security feature that restricts the system calls a process can issue. In Kubernetes, Seccomp profiles reduce the kernel attack surface by preventing containers from invoking dangerous, obscure, or non-essential system calls (such as `reboot`, `sys_chroot`, or `bpf`).

---

## ⚙️ Functionality (What it is doing)
* **Syscall Whitelisting/Blacklisting:** Evaluates system calls against defined actions (`SCMP_ACT_ALLOW`, `SCMP_ACT_ERRNO`, `SCMP_ACT_LOG`, `SCMP_ACT_KILL`).
* **RuntimeDefault Integration:** Provides a battle-tested default profile built directly into container runtimes that disables roughly 50 high-risk syscalls out of ~350 available Linux system calls.
* **Custom JSON Profiles:** Supports deploying custom JSON profiles to worker nodes under `/var/lib/kubelet/seccomp/profiles/` and referencing them via `securityContext.seccompProfile.type: Localhost`.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Seccomp is enforced at the host Linux kernel level when the container runtime (containerd/CRI-O) creates the container process. The Kubelet passes the profile path or type from the Pod's `securityContext` to the runtime during pod initialization.

---

## 🧩 Problem Solver (What problem it solves)
Most containerized microservices require fewer than 50 system calls to perform their intended function (e.g. read, write, epoll, socket). However, the underlying Linux kernel exposes hundreds of legacy system calls that may contain zero-day vulnerabilities. Seccomp eliminates exposure to these vulnerable code paths.

---

## 🟢 Operational Impact (What will happen with it operating)
Workloads execute with an enforced syscall boundary. Any invocation of a forbidden syscall returns an immediate error (typically `EPERM` or `ENOSYS`), preventing attackers from exploiting dormant kernel vulnerabilities.

---

## 🔴 Failure Impact (What will happen without it)
Containers run with `Unconfined` seccomp profiles, giving malicious actors full freedom to invoke arbitrary kernel system calls, significantly increasing the probability of host kernel privilege escalation.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **Seccomp in Kubernetes**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
