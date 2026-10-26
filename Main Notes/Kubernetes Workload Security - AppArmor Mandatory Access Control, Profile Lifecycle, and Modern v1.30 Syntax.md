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
  - kubernetes/apparmor
  - linux/apparmor
  - linux/lsm
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Workload Security - AppArmor Mandatory Access Control, Profile Lifecycle, and Modern v1.30 Syntax

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Workload Security and Container Hardening]] > **AppArmor Mandatory Access Control, Profile Lifecycle, and Modern v1.30 Syntax**

---

## 🎯 1. Architectural Foundations: Discretionary (DAC) vs. Mandatory (MAC) Access Control

To understand Linux Security Modules (LSM) like AppArmor, engineers must differentiate between the two core access control paradigms:

* **Discretionary Access Control (DAC) — Standard Linux Permissions:**
  - Enforced via user/group ownership (`chown alice:alice`) and file permission bits (`chmod 755`).
  - "Discretionary" means the owner of a resource determines who can access it.
  - **The Superuser Flaw:** DAC permissions are completely bypassed by `root` (UID 0). A compromised process running as root can read, modify, or delete any file on the filesystem.
* **Mandatory Access Control (MAC) — Kernel Security Profiles:**
  - Implemented via Linux Security Modules (LSM) like **AppArmor** and **SELinux**.
  - "Mandatory" means the **system security policy overrides both users and root!**
  - Even if an attacker possesses an interactive shell as `root` (UID 0) inside a container, if the active kernel AppArmor profile specifies `deny /etc/** w`, the Linux kernel rejects write attempts with `Permission denied`.

```
[ Process Running as ROOT (UID 0) ]
                 │
                 ├── 1. DAC Check: "Are you root?" ──► PASSES!
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. MAC Check: Linux Kernel AppArmor Hook                    │
│    "Does the active profile permit writing to /etc/?"       │
│    Rule: deny /etc/** w                                     │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
                   [ REJECTED BY KERNEL: Permission Denied! ❌ ]
```

---

## ⚙️ 2. How AppArmor Works: Path-Based Confinement & Permission Flags

Unlike SELinux (which labels filesystem inodes with cryptographic attributes), **AppArmor is path-based**. It evaluates system calls against the literal filesystem paths a process attempts to access.

### AppArmor Permission Modes
* **`r`** = Read
* **`w`** = Write / Append
* **`x`** = Execute
* **`ix`** = Inherit Execute (The spawned child process executes but remains confined under this **exact same AppArmor profile**)
* **`px`** = Discrete Profile Transition upon execution

### Profile Modes: `enforce` vs. `complain`
1. **`enforce` Mode (Production Default):** Violations are actively blocked by the kernel (returns `EACCES / Permission denied`) and logged to the audit log.
2. **`complain` Mode (Profiling):** Violations are permitted to succeed, but the kernel logs an audit event. Used during staging to record application access patterns before locking down rules.

#### How Profile Mode is Determined:
* **Inside the Profile File (Line 1):**
  - `profile k8s-deny-write flags=(attach_disconnected) { ... }` ──► Defaults to **`enforce`**.
  - `profile k8s-deny-write flags=(attach_disconnected,complain) { ... }` ──► Explicit **`complain`**.
* **Via `apparmor_parser` CLI on the Host:**
  - `sudo apparmor_parser -q <file>` ──► Loads in the mode defined by the file.
  - `sudo apparmor_parser -C <file>` ──► Forces **`complain`** mode (`-C`).

---

## 🔬 3. Deep Dive: Why `cat /proc/1/attr/current` Executes When Writes are Denied

A common security question: *If a profile contains `deny /** w` and `deny /bin/sh x`, how does `cat /proc/1/attr/current` execute?*

### The Anatomy of the Profile:
```text
profile k8s-deny-write flags=(attach_disconnected) {
  #include <abstractions/base>

  /** r,              # 1. Allow reading all files
  /bin/** ix,          # 2. Allow executing standard binaries under this profile
  /usr/bin/** ix,

  deny /** w,          # 3. Block all writes everywhere
  deny /bin/sh x,      # 4. Block interactive shell execution
  deny /bin/bash x,
}
```

### The Execution Mechanics:
1. **Direct Syscall Execution (`execve`):**
   When `kubectl exec secured-pod -- cat /proc/1/attr/current` is run, the container runtime invokes `/bin/cat` directly via `execve()`. **It does not launch a shell (`/bin/sh`)**.
2. **The Read Permission Check:**
   `/proc/1/attr/current` is a read operation (`r`). Since `/** r` is permitted, reading succeeds.
3. **The `ix` Inheritance:**
   The rule `/bin/** ix` permits `/bin/cat` to execute while keeping it strictly bound by the same profile.
4. **The Shell Defense:**
   If an attacker attempts `kubectl exec -it secured-pod -- /bin/sh`, Rule 4 (`deny /bin/sh x`) immediately intercepts the call:
   `OCI runtime exec failed: exec: "/bin/sh": permission denied by AppArmor`.

---

## 🛠️ 4. The 3-Step Node-to-Pod Lifecycle

AppArmor profiles **must be loaded into the Linux kernel on the worker nodes** before any Kubernetes pod can reference them.

```
[ Step 1: Write profile on Node ] ──► /etc/apparmor.d/k8s-deny-write
                 │
                 ▼
[ Step 2: Load into Kernel ]     ──► sudo apparmor_parser -q /etc/apparmor.d/k8s-deny-write
                 │
                 ▼
[ Step 3: Enforce in Pod YAML ]  ──► securityContext.appArmorProfile (K8s schedules container)
```

### Step 1: Write Profile on Worker Node (`/etc/apparmor.d/k8s-deny-write`)
```text
#include <tunables/global>

profile k8s-deny-write flags=(attach_disconnected) {
  #include <abstractions/base>

  file,
  /** r,
  /bin/** ix,
  /usr/bin/** ix,

  deny /** w,
  deny /bin/sh x,
  deny /bin/bash x,
}
```

### Step 2: Load into Kernel on All Worker Nodes
```bash
sudo apparmor_parser -q /etc/apparmor.d/k8s-deny-write

# Verify on host:
sudo aa-status | grep k8s-deny-write
```

---

## 🏛️ 5. Modern Kubernetes Enforcement Syntax (v1.30+ GA)

> [!IMPORTANT]
> **The Critical Syntax Shift in Kubernetes (v1.30+ / Current CKS Exams):**
> * **Legacy Syntax (Pre-v1.30):** Deprecated beta annotations on metadata:
>   `container.apparmor.security.beta.kubernetes.io/<container>: localhost/<profile-name>`
> * **Modern Syntax (v1.30+ GA):** Promoted to a first-class field inside **`securityContext.appArmorProfile`**!

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secured-pod
spec:
  securityContext:
    appArmorProfile:
      type: Localhost                      # Options: Localhost, RuntimeDefault, Unconfined
      localhostProfile: k8s-deny-write     # Must match the profile name defined in line 1 of the file!
  containers:
  - name: web
    image: nginx:1.25
```

---

## 🔍 6. Verification: Why `/proc/1/attr/current` vs. `aa-status`

* **Why `aa-status` fails inside Pods:** `aa-status` is an administrative utility residing on the host OS. Minimal container images do not have it installed, nor do they possess host capabilities to query global AppArmor tables.
* **Why `/proc/1/attr/current` is the Universal Truth:**
  Every Linux process exposes its active security module context in `/proc/<PID>/attr/current`. Inside the container, PID 1 is the primary application process.
  ```bash
  kubectl exec secured-pod -- cat /proc/1/attr/current
  ```
  - **If active:** Prints `k8s-deny-write (enforce)`.
  - **If unhardened:** Prints `unconfined`.

---

## ⚠️ 7. Critical CKS Exam Pitfalls

1. **The Multi-Node Scheduling Trap:** AppArmor profiles reside in local kernel memory. If a profile is loaded on `controlplane` but the Pod is scheduled on `node01`, Kubelet crashes with:
   `CreateContainerError: AppArmor profile "k8s-deny-write" is not loaded`. Always verify the target node or load across all cluster worker nodes.
2. **Profile Name vs. Filename:** Always use the profile name defined on **line 1 of the profile file** (`profile k8s-deny-write`), not the file path or filename.
