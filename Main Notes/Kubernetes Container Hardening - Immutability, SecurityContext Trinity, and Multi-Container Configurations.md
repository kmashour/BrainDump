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
  - kubernetes/immutability
  - kubernetes/security-context
  - kubernetes/no-new-privs
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Container Hardening - Immutability, SecurityContext Trinity, and Multi-Container Configurations

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Workload Security and Container Hardening]] > **Container Hardening - Immutability, SecurityContext Trinity, and Multi-Container Configurations**

---

## 🎯 1. The Threat Vector: Writable Containers & Attack Persistence

By default, container runtimes mount container images with a writable **OverlayFS** top layer. When an application vulnerability (such as a Remote Code Execution or file upload flaw) is exploited:
1. The attacker writes reverse shell scripts or cryptominers directly into `/tmp`, `/dev/shm`, or application directories.
2. The attacker modifies system configuration files (e.g. `/etc/passwd` or `/etc/hosts`).
3. The attacker establishes persistent execution environments that survive application crashes.

```
[ Attacker Exploit (RCE) ]
           │
           ▼
[ Writable Container Layer ]
   ├── Writes /tmp/malware.sh ────► Permitted!
   ├── chmod +x /tmp/malware.sh ──► Permitted!
   └── Executes reverse shell to Command & Control server!
```

---

## 🛡️ 2. The In-Container Security Trinity

To achieve true least privilege and workload immutability, three Linux security controls must be configured inside `securityContext`:

```
┌─────────────────────────────────────────────────────────────┐
│              THE IMMUTABILITY SECURITY TRINITY              │
├─────────────────────────────────────────────────────────────┤
│ 1. readOnlyRootFilesystem: true                             │
│    (Linux kernel mounts overlayfs with MS_RDONLY)           │
│                                                             │
│ 2. allowPrivilegeEscalation: false                          │
│    (Linux kernel sets the no_new_privs bit on the process)  │
│                                                             │
│ 3. runAsUser: <UID>  (e.g., 30000)                          │
│    (Forces process to execute with non-root UID on host)    │
└─────────────────────────────────────────────────────────────┘
```

---

### Control 1: `readOnlyRootFilesystem: true`
* **Kernel Enforcement:** The container runtime passes the `MS_RDONLY` flag to the kernel's `mount()` syscall when mounting the container rootfs.
* **The Behavioral Effect:** Any system call attempting write operations (`open(..., O_WRONLY)`, `write()`, `mkdir()`, `unlink()`) fails instantly at the Virtual File System (VFS) layer with:
  ```text
  EROFS: Read-only file system
  ```
* Attackers cannot download tools, drop webshells, or alter binaries.

---

### Control 2: `allowPrivilegeEscalation: false` (The `no_new_privs` Bit)
* **The SUID Threat:** In standard Linux, binaries possessing the Set-User-ID (SUID) permission bit (e.g. `/bin/su`, `/usr/bin/passwd`) temporarily elevate the calling process to the permissions of the file owner (**root**).
* **The Kernel Fix:** Setting `allowPrivilegeEscalation: false` executes the kernel system call:
  ```c
  prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0);
  ```
  Once the **`no_new_privs`** bit is set to `1`, the Linux kernel strictly guarantees that **neither this process nor any of its descendants can ever acquire new privileges through SUID binaries**, neutralizing SUID-based container escapes.

---

### Control 3: `runAsUser: <UID>` (Non-Root Execution)
* Mandates that the container process executes with an unprivileged User ID (e.g., UID `30000`).
* Because Linux **User Namespaces are disabled by default** in standard Kubernetes, running as `root` (UID 0) inside a container means executing as `root` (UID 0) on the host kernel. Enforcing a non-zero UID ensures that any container breakout lands on the host as an unprivileged user.

---

## ⚠️ 3. Schema Architecture: Pod-Level vs. Container-Level `securityContext`

In Kubernetes API manifests, `securityContext` is declared in two locations with distinct field rules:

```
Pod Spec: spec.template.spec
  ├── securityContext: (Pod-Level)
  │     ├── runAsUser, runAsGroup, fsGroup, seccompProfile
  │
  └── containers:
        └── - name: app
              securityContext: (Container-Level)
                ├── readOnlyRootFilesystem  <── CONTAINER-LEVEL ONLY!
                ├── allowPrivilegeEscalation <── CONTAINER-LEVEL ONLY!
                └── capabilities            <── CONTAINER-LEVEL ONLY!
```

| Field | Pod-Level (`pod.spec.securityContext`) | Container-Level (`containers[].securityContext`) |
| :--- | :---: | :---: |
| `runAsUser` / `runAsGroup` |  YES |  YES (Overrides Pod-level) |
| `fsGroup` |  YES (Governs volume permissions) | ❌ NO |
| `seccompProfile` |  YES |  YES |
| **`readOnlyRootFilesystem`** | ❌ **INVALID! Schema Error!** |  **CONTAINER-LEVEL ONLY** |
| **`allowPrivilegeEscalation`**| ❌ **INVALID! Schema Error!** |  **CONTAINER-LEVEL ONLY** |
| **`capabilities`** | ❌ **INVALID! Schema Error!** |  **CONTAINER-LEVEL ONLY** |

> [!WARNING]
> Placing `readOnlyRootFilesystem: true` under `pod.spec.securityContext` causes immediate admission rejection:
> `unknown field "readOnlyRootFilesystem" in io.k8s.api.core.v1.PodSecurityContext`.
> It must be declared under `containers[].securityContext`.

---

## 📦 4. Multi-Container Pod Configuration (CKS Question 05 Blueprint)

In multi-container pods, immutability controls must be declared on **every individual container**:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-workload
  namespace: production-workloads
spec:
  replicas: 1
  selector:
    matchLabels:
      app: secure-app
  template:
    metadata:
      labels:
        app: secure-app
    spec:
      containers:
      # ── CONTAINER 1 ──────────────────────────────
      - name: web-frontend
        image: nginx:1.25
        securityContext:
          runAsUser: 30000
          readOnlyRootFilesystem: true
          allowPrivilegeEscalation: false

      # ── CONTAINER 2 ──────────────────────────────
      - name: cache-proxy
        image: redis:7.2
        securityContext:
          runAsUser: 30000
          readOnlyRootFilesystem: true
          allowPrivilegeEscalation: false
```

---

## 🔬 5. The Writable Scratchpad (`emptyDir` at `/tmp`) & Attack Vectors

### The Engineering Catch:
Setting `readOnlyRootFilesystem: true` causes applications that generate temporary caches, lockfiles, or PID files (e.g. Nginx writing `/var/cache/nginx`) to crash immediately.

### The Remediation:
Attach an ephemeral **`emptyDir`** volume at the specific scratch directory:
```yaml
        securityContext:
          readOnlyRootFilesystem: true
        volumeMounts:
        - name: scratch-vol
          mountPath: /tmp
      volumes:
      - name: scratch-vol
        emptyDir: {}
```

### Can an Attacker Abuse Writable `/tmp`?
If an attacker exploits the application, they can write scripts to `/tmp`. Defense-in-depth mitigates this risk via 4 complementary layers:
1. **Linux `noexec` Mount Option:** The filesystem rejects code execution (`Permission denied - EACCES`) on files inside `/tmp`.
2. **`allowPrivilegeEscalation: false`:** SUID binaries inside `/tmp` cannot elevate privileges.
3. **`runAsUser: 30000`:** Files created in `/tmp` are unprivileged; the attacker cannot alter root-owned data.
4. **Linux Capabilities Stripping (`drop: [ALL]`):** The process cannot mount devices, load modules, or sniff packets.

---

## 🛠️ 6. Terminal Verification Commands

```bash
# 1. Verify non-root UID on Container 1:
kubectl exec -it <pod-name> -c web-frontend -- id
# Expected: uid=30000

# 2. Verify rootfs immutability on Container 1:
kubectl exec -it <pod-name> -c web-frontend -- touch /test.txt
# Expected: touch: /test.txt: Read-only file system

# 3. Verify non-root UID on Container 2:
kubectl exec -it <pod-name> -c cache-proxy -- id
# Expected: uid=30000

# 4. Verify rootfs immutability on Container 2:
kubectl exec -it <pod-name> -c cache-proxy -- touch /test.txt
# Expected: touch: /test.txt: Read-only file system
```
