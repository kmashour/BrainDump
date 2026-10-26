---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Workload Security and Container Hardening]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Workload Hardening"
tags:
  - kubernetes/security
  - kubernetes/seccomp
  - linux/seccomp
  - linux/bpf
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Workload Security - Seccomp BPF Syscall Filtering and RuntimeDefault Profiles

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Workload Security and Container Hardening]] > **Seccomp BPF Syscall Filtering and RuntimeDefault Profiles**

---

## 🎯 1. Architectural Foundations: The System Call (Syscall) Boundary

Every containerized process executes in Userspace (CPU Ring 3) and must interact with physical hardware and operating system resources through the Linux Kernel (CPU Ring 0). Applications request kernel services through **System Calls (syscalls)**:

* **File I/O:** `read()`, `write()`, `openat()`
* **Networking:** `socket()`, `connect()`, `bind()`
* **Memory Management:** `mmap()`, `brk()`
* **Process Spawning:** `clone()`, `execve()`

```
[ USERSPACE (Ring 3) - Containers & Apps ]
   nginx / python / database
       │
       ▼ Invokes System Call (syscall)
┌─────────────────────────────────────────────────────────────┐
│ LINUX KERNEL (Ring 0)                                       │
│ Provides ~350+ System Calls (read, write, socket, reboot...)│
└─────────────────────────────────────────────────────────────┘
```

---

## ⚠️ 2. The Threat Vector: The 300 Unused Kernel System Calls

The Linux kernel exposes over **350+ system calls**:
* Typical production microservices (e.g., Nginx, Go binaries, Node.js) require only **~40 to 60 system calls** to perform all required business logic.
* The remaining **~300 system calls** include dangerous, obsolete, or administrative interfaces:
  - `reboot()`: Reboots the physical host server.
  - `ptrace()`: Attaches to another process's virtual memory to inspect registers and inject shellcode.
  - `kexec_load()`: Overwrites and boots a new Linux kernel into memory.
  - `bpf()`: Loads arbitrary eBPF bytecode into kernel memory.

### The Attack Surface:
Even if a container runs as an unprivileged user (`runAsUser: 30000`) with a read-only rootfs, **it still communicates directly with the shared host kernel**. If an obscure or legacy system call contains a memory corruption or race condition bug, an attacker inside a container invokes that system call, triggers kernel privilege escalation, and compromises the physical host.

---

## 🔒 3. Seccomp (Secure Computing Mode) BPF Architecture

**Seccomp** is an in-kernel security facility that utilizes **Berkeley Packet Filter (BPF)** bytecode to intercept every system call before it reaches the kernel dispatch table.

### Seccomp Evaluation Actions:
When a system call is made, the Seccomp filter checks its rule table:
* **`SCMP_ACT_ALLOW`:** The system call is approved and forwarded to the kernel handler.
* **`SCMP_ACT_ERRNO`:** The system call is blocked; the kernel immediately returns an error code (typically `EPERM` - Operation not permitted) without executing the code.
* **`SCMP_ACT_KILL`:** The kernel immediately terminates the process thread with `SIGSYS`.
* **`SCMP_ACT_LOG`:** The system call is permitted, but an audit log entry is recorded (utilized for application profiling).

```
[ Container Process ] ───(Tries to call: ptrace or reboot)───► [ Linux Kernel ]
                                                                      │
                                                           [ Seccomp BPF Filter ]
                                                                      │
                                                           Rule: ptrace -> ERRNO
                                                                      │
                                                                      ▼
                                                           [ BLOCKED: EPERM! ❌ ]
```

---

## ⚙️ 4. The Two Seccomp Profiles in Kubernetes

Kubernetes provides two mechanisms for configuring Seccomp within `securityContext`:

### Profile 1: `RuntimeDefault` (The Production Standard)
`RuntimeDefault` is the built-in profile defined by the underlying container runtime (`containerd` / CRI-O):
* Automatically **blocks approximately 50 to 60 of the most dangerous system calls** (including `reboot`, `ptrace`, `kexec_load`, `mount`, `swapon`, `syslog`, `acct`).
* Permits standard microservice operations (networking, file I/O, threading).
* **PSA Compliance:** Under the Pod Security Standards **`restricted`** tier, declaring `type: RuntimeDefault` is **mandatory**.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secured-pod
spec:
  securityContext:
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: web
    image: nginx:1.25
```

---

### Profile 2: Custom Localhost Profiles (`type: Localhost`)
When an application requires a custom, fine-grained whitelist, a JSON profile is deployed directly onto the worker nodes:

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": ["SCMP_ARCH_X86_64"],
  "syscalls": [
    {
      "names": ["read", "write", "exit", "exit_group", "futex", "nanosleep", "epoll_wait"],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

#### Node Filesystem Root Directory:
Kubelet requires custom Seccomp profiles to reside strictly within:
`/var/lib/kubelet/seccomp/`

If a profile is stored at:
`/var/lib/kubelet/seccomp/profiles/audit.json`

The manifest must declare a **relative path**:
```yaml
spec:
  securityContext:
    seccompProfile:
      type: Localhost
      localhostProfile: profiles/audit.json    # Relative to /var/lib/kubelet/seccomp/!
```

> [!WARNING]
> Specifying an absolute path (`/var/lib/kubelet/seccomp/profiles/audit.json`) causes Kubelet to search for `/var/lib/kubelet/seccomp/var/lib/kubelet/...`, crashing the pod with `CreateContainerError`.

---

## 🛠️ 5. Terminal Verification Commands

Inspect `/proc/1/status` inside the container:

```bash
kubectl exec -it secured-pod -- grep -E "Seccomp|Seccomp_filters" /proc/1/status
```

**Terminal Output:**
```text
Seccomp:         2
Seccomp_filters: 1
```

* `Seccomp: 0` ──► Disabled (Unconfined).
* `Seccomp: 1` ──► Strict mode (only permits read, write, exit, sigreturn).
* `Seccomp: 2` ──► **Filter Mode Active!** The process is actively sandboxed by Seccomp BPF rules.
