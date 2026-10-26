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
  - kubernetes/gvisor
  - kubernetes/kata-containers
  - kubernetes/runtimeclass
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Sandboxed Runtimes: gVisor, Kata Containers, and the 3-Layer RuntimeClass Chain

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Main Notes/Kubernetes Workload Security and Container Hardening|Kubernetes Workload Security and Container Hardening]] > **Kubernetes Sandboxed Runtimes: gVisor, Kata Containers, and the 3-Layer RuntimeClass Chain**

---

## 💀 1. The Shared Kernel Vulnerability in Standard Containers (`runc`)

A container running under standard `runc` (the default OCI runtime in containerd and CRI-O) is **not a virtual machine**. It is simply a Linux process wrapped inside namespaces (`pid`, `net`, `mnt`, `ipc`, `uts`, `cgroup`) and constrained by cgroups.

```
+-----------------------------------------------------------------------------------+
|                        STANDARD CONTAINER EXECUTION (runc)                        |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ Pod A (Untrusted App / Multi-Tenant Code) ]   [ Pod B (Critical Internal App) ]|
|             │                                                  │                  |
|             │ Direct Syscalls (open, clone, bpf, io_uring)     │ Syscalls         |
|             ▼                                                  ▼                  |
|  ===============================================================================  |
|                         SHARED HOST LINUX KERNEL (UID 0)                          |
|  ===============================================================================  |
|                                         │                                         |
|                                         ▼                                         |
|                                 PHYSICAL HARDWARE                                 |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### The Inherent Threat Model
The Linux kernel exposes **350+ system calls**. Complex kernel subsystems like `io_uring`, eBPF, netfilter, and memory managers regularly suffer zero-day privilege escalation vulnerabilities (e.g., Dirty COW, Dirty Pipe, CVE-2024-1086).
- If an attacker compromises Pod A and executes a kernel exploit, **they compromise the host kernel directly**.
- Once the host kernel is owned, all other pods residing on that physical node (including Pod B) are immediately compromised.
- While Seccomp, AppArmor, and Capabilities drop unnecessary privileges, untrusted code execution (such as user-submitted scripts in CI/CD or multi-tenant SaaS) demands **complete kernel isolation**.

---

## 🏛️ 2. Sandboxing Paradigms: gVisor vs. Kata Containers

To eliminate host kernel sharing, the cloud-native ecosystem developed two distinct architectural paradigms:

```
+-------------------------------------------------------------------------------------------------------+
|                                    SANDBOXED RUNTIME ARCHITECTURES                                    |
+-------------------------------------------------------------------------------------------------------+
| FEATURE                   | gVisor (runsc)                     | Kata Containers                      |
+---------------------------+------------------------------------+--------------------------------------+
| Philosophy                | User-space Kernel (Emulation)      | MicroVM (Hardware Virtualization)    |
| Developer                 | Google                             | OpenInfra Foundation / Intel / AWS   |
| Virtualization Layer      | None (Runs as user-space process)  | KVM / QEMU / Cloud-Hypervisor        |
| Kernel Isolation          | Emulates Linux kernel in Go        | Dedicated guest Linux kernel per Pod |
| Memory Footprint          | ~15 MB per sandbox                 | ~30 - 50 MB per MicroVM              |
| Startup Latency           | Milliseconds                       | Hundreds of milliseconds             |
| Hardware Requirement      | Standard CPU (no nested virt)      | Hardware virtualization (VT-x/AMD-V) |
| Syscall Coverage          | ~300 common syscalls implemented   | 100% Linux kernel compatibility      |
+-------------------------------------------------------------------------------------------------------+
```

---

## 🔬 3. Deep Dive: gVisor (`runsc`) Architecture

gVisor intercepts application system calls before they ever reach the host operating system. It consists of two core components: **Sentry** and **Gofer**.

```
+-----------------------------------------------------------------------------------+
|                                 gVisor ARCHITECTURE                               |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ Container Application ] (e.g., untrusted python/node script)                   |
|             │                                                                     |
|             │ Syscall (e.g., sys_read, sys_socket)                                |
|             ▼                                                                     |
|  +-----------------------------------------------------------------------------+  |
|  |  SENTRY (User-Space Kernel written in Go)                                   |  |
|  |  - Intercepts all syscalls via ptrace or KVM                                |  |
|  |  - Implements network stack (Netstack), memory management, and VFS in Go    |  |
|  +-----------------------------------------------------------------------------+  |
|             │                                                 │                   |
|             │ Safe, filtered host calls                       │ File System I/O   |
|             ▼                                                 ▼                   |
|  +----------------------+                           +--------------------------+  |
|  | HOST LINUX KERNEL    |                           | GOFER (Isolated Process) |  |
|  | (Sees only ~20 safe  |                           | Mediates host file I/O   |  |
|  |  syscalls from Go)   |                           | via 9P/virtio-fs         |  |
|  +----------------------+                           +--------------------------+  |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

1. **Sentry (The Emulated Kernel):**
   - Written in Go, Sentry acts as an independent guest kernel running in user space.
   - When the container makes a system call, Sentry intercepts it (using `ptrace` or the KVM virtualization extension) and handles it entirely inside Go memory.
   - Sentry implements its own virtual filesystem, memory management, and complete network stack (`Netstack`).
   - The host Linux kernel never sees the untrusted syscalls.

2. **Gofer (File System Isolation):**
   - File system access is isolated into an external process called Gofer.
   - Sentry never opens host files directly; it communicates with Gofer across an IPC socket using the 9P or virtio-fs protocols.
   - Even if Sentry's memory were breached, Gofer prevents arbitrary directory traversal on the host node.

---

## ⚙️ 4. The 3-Layer Integration Chain: Why It Exists

To integrate sandboxed runtimes into Kubernetes, the platform implements a **3-Layer Chain**:

```
[ Layer 1: containerd ]       ──►  [ Layer 2: RuntimeClass ]       ──►  [ Layer 3: Pod Spec ]
  /etc/containerd/config.toml        apiVersion: node.k8s.io/v1           spec:
  handler = "runsc"                  name: gvisor                          runtimeClassName: gvisor
                                     handler: runsc
```

### Why not let the Pod directly specify `runtime: /usr/bin/runsc`?

Allowing workloads to specify host runtime paths directly breaks security, portability, and scheduling. The 3 layers enforce strict separation between three distinct personas:

```
+-------------------------------------------------------------------------------------------------------+
|                                  THE 3-LAYER SEPARATION OF CONCERNS                                   |
+-------------------------------------------------------------------------------------------------------+
| LAYER                     | WHO OWNS IT?             | ARCHITECTURAL RATIONALE                                |
+---------------------------+--------------------------+------------------------------------------------+
| 1. containerd             | Node / OS Admin          | Host Security Boundary: Only the root node     |
|    (/etc/containerd)      | (Infrastructure Layer)   | admin decides what binaries physically execute.|
+---------------------------+--------------------------+------------------------------------------------+
| 2. RuntimeClass           | Cluster Admin            | Scheduling & Governance Bridge: Tells the      |
|    (API Object)           | (Governance Layer)       | Kube-Scheduler which nodes have the runtime.   |
+---------------------------+--------------------------+------------------------------------------------+
| 3. Pod Manifest           | Application Developer    | Portability & Declarative Intent: Developer    |
|    (runtimeClassName)     | (Workload Layer)         | requests isolation without hardcoding paths.   |
+---------------------------+--------------------------+------------------------------------------------+
```

### The Four First-Principles Reasons

#### 1. Host Security Boundary (Arbitrary Binary Execution Prevention)
If developers could set `spec.runtimeBinary: /bin/bash` or specify arbitrary file paths in YAML, any user with `create pods` RBAC could execute host-level binaries or malicious scripts dropped onto the node. Layer 1 guarantees that only pre-approved, root-configured runtime handlers in containerd can ever be invoked.

#### 2. Cloud & Vendor Portability
Workload manifests must remain vendor-neutral. A team should deploy the exact same YAML to an on-prem cluster running gVisor (`runsc`), an AWS EKS bare-metal cluster running Kata Containers with Firecracker, or an AKS cluster with Cloud-Hypervisor. `RuntimeClass` abstracts the underlying engine into a logical name (`runtimeClassName: sandboxed`).

#### 3. Heterogeneous Clusters & The Kube-Scheduler Bridge
Sandboxed runtimes incur CPU/memory overhead, and Kata requires hardware virtualization CPU flags (Intel VT-x / AMD-V) that rarely exist across all nodes in a cluster.
The `RuntimeClass` solves this by embedding **automated scheduling rules**:
```yaml
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: gvisor
handler: runsc
scheduling:
  nodeSelector:
    sandbox.runtime: gvisor
  tolerations:
  - key: sandbox.runtime
    operator: Equal
    value: gvisor
    effect: NoSchedule
```
When a developer sets `runtimeClassName: gvisor`, the **Kube-Scheduler** automatically evaluates these selectors and routes the pod *only* to nodes equipped with the sandbox runtime.

#### 4. The Container Runtime Interface (CRI) Contract
Kubelet does not understand specific runtime vendor binaries. Kubelet only communicates with containerd via gRPC over `/run/containerd/containerd.sock`.
- Kubelet issues: `RunPodSandboxRequest(runtime_handler="runsc")`.
- containerd maps the handler string `"runsc"` to low-level OCI shim binaries (`containerd-shim-runsc-v1`).
- This decouples the Kubernetes codebase entirely from container runtime implementations.

---

## 🛠️ 5. Practical Configuration & Manifests

### Step 1: Configure Containerd (`/etc/containerd/config.toml`)
On worker nodes equipped with `runsc`:
```toml
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runsc]
  runtime_type = "io.containerd.runsc.v1"
```
Restart containerd:
```bash
sudo systemctl restart containerd
```

### Step 2: Create the `RuntimeClass` Resource
```yaml
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: gvisor
handler: runsc
```

### Step 3: Deploy Workload Using `runtimeClassName`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-sandbox-app
spec:
  runtimeClassName: gvisor
  containers:
  - name: app
    image: python:3.11-alpine
    command: ["sleep", "3600"]
```

---

## 🔍 6. Terminal Forensics: Detecting gVisor from the CLI

In the CKS exam, scenarios frequently ask you to identify whether a pod is running under gVisor:

### Forensic Check 1: Kernel Ring Buffer (`dmesg`)
Execute `dmesg` inside the container:
```bash
kubectl exec -it secure-sandbox-app -- dmesg
```
- **Standard `runc`:** Displays extensive host hardware boot logs, ACPI entries, and device drivers.
- **gVisor (`runsc`):** Displays the simulated gVisor initialization banner:
  ```text
  [ 0.000000] Starting gVisor...
  [ 0.231201] Setting up playground...
  [ 0.450123] Ready!
  ```

### Forensic Check 2: Kernel Name & Version (`uname -a`)
Execute `uname -a` inside the container:
```bash
kubectl exec -it secure-sandbox-app -- uname -a
```
- **Standard `runc`:** Returns the actual host Linux kernel release (e.g., `Linux worker-01 6.8.0-40-generic ...`).
- **gVisor (`runsc`):** Returns a fixed synthetic Linux kernel string (typically `Linux ... 4.4.0 ... gVisor`).

---

## ⚡ 7. Exam Diagnostic Pitfalls

1. **Pod Stuck in `ContainerCreating`:**
   Inspect `kubectl describe pod <name>`:
   ```text
   Failed to create pod sandbox: no runtime for "runsc" is configured
   ```
   *Diagnosis:* The `RuntimeClass` exists, but the worker node's `/etc/containerd/config.toml` lacks the `runsc` handler definition, or containerd was not restarted.
2. **Missing `RuntimeClass`:**
   If a deployment specifies `runtimeClassName: gvisor` but the `RuntimeClass` resource is missing from the cluster, admission rejects the pod immediately.

---

## 🔗 Related Master Notes & References
- Parent Landing Note: [[Main Notes/Kubernetes Workload Security and Container Hardening|Kubernetes Workload Security and Container Hardening]]
- Container Hardening: [[Main Notes/Kubernetes Container Hardening - Immutability, SecurityContext Trinity, and Multi-Container Configurations|Container Hardening Trinity & Immutability]]
- Seccomp Filtering: [[Main Notes/Kubernetes Workload Security - Seccomp BPF Syscall Filtering and RuntimeDefault Profiles|Seccomp BPF Syscall Filtering]]
- Capabilities Stripping: [[Main Notes/Kubernetes Workload Security - Linux Capabilities Stripping, CAP_NET_RAW, and eBPF Profiling|Linux Capabilities Stripping & CAP_NET_RAW]]
- Reference Guide: [[Reference Notes/0-7-9_workload_kernel_isolation_seccomp_apparmor_and_capabilities.md|Module 0-7-9: Workload Kernel Isolation]]
