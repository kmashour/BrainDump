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
  - kubernetes/capabilities
  - linux/capabilities
  - linux/ebpf
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Workload Security - Linux Capabilities Stripping, CAP_NET_RAW, and eBPF Profiling

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Workload Security and Container Hardening]] > **Linux Capabilities Stripping, CAP_NET_RAW, and eBPF Profiling**

---

## 🎯 1. First Principles: The Demise of Binary Root & The SUID Dilemma

In traditional UNIX, process permissions were binary and all-or-nothing:
* **Unprivileged (`UID != 0`):** Cannot bind to ports `< 1024`, cannot configure routing, cannot modify clocks.
* **Superuser (`UID == 0` / Root):** Full, omnipotent kernel power across all subsystems.

### The Historic SUID Vulnerability:
When an unprivileged user needed to perform a single privileged task (e.g. `ping` sending raw ICMP packets):
* Administrators set the Set-User-ID (SUID) bit: `chmod u+s /bin/ping`.
* When executed, `ping` ran with full root authority.
* If `ping` contained a memory corruption or buffer overflow vulnerability, attackers escalated to full, unrestricted root over the host operating system.

---

## ⚙️ 2. The POSIX Capabilities Architecture

The Linux kernel resolved the SUID dilemma by subdividing the omnipotence of `root` into approximately **40 discrete, granular permissions called Capabilities** (`CAP_*`):

```
                       [ TRADITIONAL ROOT (UID 0) ]
                                    │
           ┌────────────────────────┼────────────────────────┐
           ▼                        ▼                        ▼
  [ CAP_NET_BIND_SERVICE ]     [ CAP_NET_RAW ]         [ CAP_SYS_ADMIN ]
  Can bind to privileged       Can craft raw ICMP/     "The New Root": Mount disks,
  ports (< 1024) like 80/443   packets (used by ping)  load eBPF, inspect kernel memory
           │                        │                        │
           ▼                        ▼                        ▼
  [ CAP_SYS_TIME ]             [ CAP_CHOWN ]           [ CAP_KILL ]
  Can modify system clock      Can change file owners  Can signal other users' processes
```

Under POSIX capabilities, processes operate under least privilege: a web server running as non-root user `1000` is granted **only** `CAP_NET_BIND_SERVICE` to open port `80`, while retaining zero access to `CAP_SYS_ADMIN` or `CAP_KILL`.

---

## ⚠️ 3. The Container Threat: The Dangerous Default Set

Containers in Docker and Kubernetes do **not** launch with zero privileges. By default, container runtimes grant **approximately 14 Linux capabilities** to every container:

```text
CAP_CHOWN, CAP_DAC_OVERRIDE, CAP_FOWNER, CAP_FSETID, CAP_KILL, 
CAP_SETGID, CAP_SETUID, CAP_SETPCAP, CAP_NET_BIND_SERVICE, 
CAP_NET_RAW, CAP_SYS_CHROOT, CAP_MKNOD, CAP_AUDIT_WRITE, CAP_SETFCAP
```

### The Critical Vulnerability: `CAP_NET_RAW`
Historically, `CAP_NET_RAW` was included in the default container set solely so developers could run `ping` inside containers.

**The Attack Vector:**
In flat Kubernetes pod networks:
* A compromised pod possessing `CAP_NET_RAW` can craft arbitrary raw Ethernet frames.
* The attacker executes **ARP Spoofing** and **DNS Spoofing** against adjacent pods sharing the node's virtual ethernet (`veth`) bridge.
* Attackers intercept unencrypted traffic, steal bearer tokens, and execute Man-In-The-Middle (MITM) attacks across the cluster data plane.

---

## 🛡️ 4. The Golden Rule: `drop: ["ALL"]`

The foundational rule of workload security in Kubernetes:
> **Never selectively drop individual capabilities. Always drop ALL capabilities first, and then selectively add ONLY what is strictly required.**

```yaml
spec:
  containers:
  - name: secure-web
    image: nginx:1.25
    securityContext:
      capabilities:
        drop:
        - ALL                  # 1. Strip all 40+ Linux capabilities
        add:
        - NET_BIND_SERVICE     # 2. Add back ONLY the port 80/443 permission
```

### Kubernetes YAML Rules for Capabilities:
1. **Omit the `CAP_` prefix:** Declare `NET_BIND_SERVICE`, **not** `CAP_NET_BIND_SERVICE`.
2. **Uppercase `ALL`:** Always specify `ALL` in uppercase.
3. **Container-level only:** Declared strictly under `spec.containers[].securityContext.capabilities`.

---

## 🔬 5. Workload Profiling: Discovering Exact Capability Requirements

In production, capabilities are discovered through active runtime profiling:

### How the Linux Kernel Checks Capabilities Under the Hood
Whenever an application executes a privileged syscall (e.g. `bind()` on port 80), the kernel executes `capable(CAP_...)`:
* If the capability bit is set in the process's `CapEff` mask: Syscall succeeds.
* If the capability bit is missing: Kernel returns `EPERM: Operation not permitted`.

---

### Profiling Tools & Workflows

#### Method 1: Kubernetes eBPF Tracing with Inspektor Gadget
```bash
kubectl gadget trace capabilities -n production -p web-pod
```
**Real-Time Output:**
```text
NODE       NAMESPACE  POD     CONTAINER  PID    COMM   CAP               SYSCALL
worker01   production web-pod nginx      14820  nginx  CAP_NET_BIND_SERV bind
```
Hooks into kernel probes via eBPF and logs every capability requested during live traffic processing.

#### Method 2: Host Tracing via `bcc-tools capable`
```bash
sudo capable -p <CONTAINER_PID>
```
Traces capability checks directly on the Linux host kernel for a specific container process.

#### Method 3: Automated CI/CD Drop-All Testing
Enforce `drop: ["ALL"]` in staging. Run integration and load tests. Inspect container error logs and `dmesg` for `Operation not permitted` to identify the minimal required additions.

---

## 📋 6. Auditing Capabilities in the Terminal

Every Linux process exposes its capability masks in `/proc/<PID>/status`:

```bash
# 1. Extract raw capability hex masks:
grep -i Cap /proc/<PID>/status
# Output:
# CapPrm: 0000000000000400
# CapEff: 0000000000000400

# 2. Decode the hex bitmask into human-readable capability names:
capsh --decode=0000000000000400
# Output:
# 0x0000000000000400=cap_net_bind_service
```

---

## 🏛️ 7. Alignment with Pod Security Admission (PSA)

Under the official Kubernetes **Pod Security Standards (PSS)**:
* The **`restricted`** standard mandates that every container **must** specify:
  ```yaml
  securityContext:
    capabilities:
      drop:
      - ALL
  ```
* Under `restricted`, the **only** permitted addition is `NET_BIND_SERVICE`. Adding any other capability causes immediate admission denial.
