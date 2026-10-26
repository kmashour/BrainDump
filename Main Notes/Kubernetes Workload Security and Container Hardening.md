---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: security
domains:
  - kubernetes
  - containers
  - security
related_concepts:
  - "[[Kubernetes Attack Surface and the 4Cs of Cloud Native Security]]"
  - "[[Kubernetes Cluster Component Hardening and Communication Security]]"
  - "[[Kubernetes Pod Security and Policy Engines]]"
  - "[[Linux Operating System Architecture and Kernel Mechanics]]"
against: []
reference_guides:
  - "[[Reference Notes/0-7-9_workload_kernel_isolation_seccomp_apparmor_and_capabilities.md]]"
  - "[[Reference Notes/0-7-2_pod_security_standards_and_admission.md]]"
tags:
  - kubernetes/security
  - kubernetes/workload-hardening
  - kubernetes/security-context
  - kubernetes/cks
  - status/completed
---

# Kubernetes Workload Security and Container Hardening

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Security > **Kubernetes Workload Security and Container Hardening**

---

## 🎯 Purpose (Why it is used)
In the 4Cs of Cloud Native Security, the **Container** layer sits directly between application code and the host operating system. Even when control plane components and networks are hardened, an application-level Remote Code Execution (RCE) bug can compromise the underlying host if the container executes with excessive privileges, writable root filesystems, or shared root identities. **Workload Hardening & SecurityContext Configuration** establishes in-container sandboxing, strips kernel privileges, and enforces storage permission boundaries so that an application compromise remains strictly contained.

---

## ⚙️ Functionality (What it is doing)
Workload security operates at the container process and volume boundary:
filesystems can be mounted with the noexec option:
  • A user can write files to /tmp.
  • A user can read files from /tmp.
  • BUT THE LINUX KERNEL WILL REFUSE TO EXECUTE ANY BINARY OR SCRIPT FROM THAT DIRECTORY!
  If the attacker runs /tmp/malware.sh, the kernel immediately blocks it:
    bash: /tmp/malware.sh: Permission denied (EACCES)

1. **Filesystem Immutability:** Enforces read-only root filesystems (`readOnlyRootFilesystem: true`), preventing attackers from downloading webshells, compiling malware, or altering system libraries.
2. **Privilege Escalation Suppression:** Sets the Linux kernel's `no_new_privs` bit (`allowPrivilegeEscalation: false`), neutralizing Set-User-ID (SUID) binaries from escalating permissions.
3. **Identity & User Isolation:** Enforces non-root execution (`runAsUser: <UID>`), defending against the reality that Linux User Namespaces are disabled by default in standard Kubernetes.
4. **Storage Permissions & Group Federation:** Utilizes `fsGroup` and optimized change policies (`fsGroupChangePolicy: "OnRootMismatch"`) to grant non-root workloads read/write access to attached volumes without introducing startup latency.

```
+---------------------------------------------------------------------------------+
|                       HARDENED CONTAINER RUNTIME SANDBOX                        |
|                                                                                 |
|   +─────────────────────────────────────────────────────────────────────────+   |
|   | Container Process: non-root (UID 30000, supplemental GID 2000)          |   |
|   | Kernel Bit: no_new_privs = 1 (No SUID escalation possible)              |   |
|   +─────────────────────────────────────────────────────────────────────────+   |
|         │                                                 │                     |
|         ├──► Attempts write to /bin or /etc               ├──► Writes to /tmp   |
|         │    [ REJECTED: EROFS Read-only file system ]    │    (emptyDir mount) |
|         │                                                 │    [ Permitted ]    |
|         ▼                                                 ▼                     |
|   [ Read-Only Root Filesystem ]                 [ Ephemeral Scratch Space ]     |
+---------------------------------------------------------------------------------+
```

---

## 🏛️ Architectural Context (How it fits in the architecture)
This domain operates at **Layer 3 (Container)** of the 4Cs Security Model:
* It protects the physical worker node by ensuring container processes cannot execute as root on the host kernel.
* It works beneath Pod Security Admission (PSA), translating high-level namespace policies (`restricted`) into concrete container runtime configuration fields.
* It interfaces with host storage systems via Kubelet volume managers, coordinating user and group ownership across persistent and ephemeral storage volumes.

---

## 🧩 Problem Solver (What problem it solves)
* **Webshell & Malware Persistence:** Blocks attackers from downloading or installing arbitrary binaries inside compromised containers.
* **SUID Privilege Escalation:** Neutralizes host and container binaries configured with the SUID bit from escalating unprivileged users to root.
* **Volume Permission Deadlocks:** Solves the classic "Permission Denied" bug encountered when non-root containers attempt to write to root-owned persistent volumes.
* **Storage Initialization Timeouts:** Eliminates the catastrophic multi-minute pod startup lag caused by recursive `chown` operations across massive volume directory trees.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Defense-in-Depth:** An RCE vulnerability in application code is immediately stopped from writing payloads or escalating privileges.
* **Deterministic Volume Access:** Workloads access persistent storage seamlessly under dedicated group IDs without granting root access.
* **High-Speed Restarts:** Pods mounting millions of files initialize in milliseconds rather than timing out in `ContainerCreating`.

---

## 🔴 Failure Impact (What will happen without it)
* **Host Takeover via Container Escape:** Workloads running as default `root` (UID 0) that breach container boundaries arrive on the worker node with genuine root authority over the host kernel.
* **Persistent Cryptomining:** Attackers exploit web vulnerabilities to download and run background mining scripts inside writable container directories.

---

## 🔍 Deeper Dive Notes
* [[Main Notes/Kubernetes Container Hardening - Immutability, SecurityContext Trinity, and Multi-Container Configurations|Container Hardening: Immutability, SecurityContext Trinity & Multi-Container Configs]]
* [[Main Notes/Kubernetes Volume Permissions - fsGroup Mechanics, Supplemental Groups, and RootMismatch Optimization|Volume Permissions: fsGroup Mechanics, Supplemental Groups & RootMismatch Optimization]]
* [[Main Notes/Kubernetes Workload Security - Linux Capabilities Stripping, CAP_NET_RAW, and eBPF Profiling|Workload Security: Linux Capabilities Stripping, CAP_NET_RAW & eBPF Profiling]]
* [[Main Notes/Kubernetes Workload Security - AppArmor Mandatory Access Control, Profile Lifecycle, and Modern v1.30 Syntax|AppArmor Mandatory Access Control, Profile Lifecycle & Modern v1.30 Syntax]]
* [[Main Notes/Kubernetes Workload Security - Seccomp BPF Syscall Filtering and RuntimeDefault Profiles|Seccomp BPF Syscall Filtering & RuntimeDefault Profiles]]
* [[Main Notes/Kubernetes Sandboxed Runtimes - gVisor, Kata Containers, and the 3-Layer RuntimeClass Chain|Sandboxed Runtimes: gVisor, Kata Containers & 3-Layer RuntimeClass Chain]]

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
