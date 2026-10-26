---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Runtime Security and Threat Forensics]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Workload Hardening"
tags:
  - kubernetes/security
  - kubernetes/falco
  - kubernetes/ebpf
  - linux/memory-management
  - linux/dev-mem
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Runtime Threat Detection: Falco eBPF Mechanics, /dev/mem Memory Scraping, and Rogue Pod Remediation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Main Notes/Kubernetes Runtime Security and Threat Forensics|Kubernetes Runtime Security and Threat Forensics]] > **Kubernetes Runtime Threat Detection: Falco eBPF Mechanics, /dev/mem Memory Scraping, and Rogue Pod Remediation**

---

## 🧱 1. Memory Architecture Foundations: Virtual Memory vs. Physical RAM

To understand memory scraping threats and runtime detection, we must examine how the CPU and the Linux kernel isolate processes under normal conditions.

### The Virtual Memory Illusion
Every Linux process (whether `nginx` inside a container or `kube-apiserver` on the host node) is executed inside an independent **Virtual Address Space** (typically `0x000000000000` to `0x7FFFFFFFFFFF` on 64-bit architectures).
- A process never directly addresses physical RAM chips.
- The CPU contains a dedicated physical hardware component: the **Memory Management Unit (MMU)**.
- The Linux kernel maintains per-process **Page Tables** that translate process-virtual addresses into physical memory blocks (pages).

```
+-----------------------------------------------------------------------------------+
|                         NORMAL VIRTUAL MEMORY ISOLATION                           |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ Pod A: Nginx (PID 100) ]                 [ Pod B: etcd (PID 200) ]             |
|  Virtual Space: 0x0000 -> 0xFFFF            Virtual Space: 0x0000 -> 0xFFFF       |
|             │                                           │                         |
|             ▼ (Page Table A)                            ▼ (Page Table B)          |
|  +--------------------+                     +--------------------+                |
|  | MMU Hardware Wall  |                     | MMU Hardware Wall  |                |
|  +--------------------+                     +--------------------+                |
|             │                                           │                         |
|             ▼                                           ▼                         |
|  [ Physical RAM Block A ]                   [ Physical RAM Block B ]              |
|  (Contains web assets)                      (Contains TLS Keys & Root Secrets!)   |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### The Hardware Boundary Enforcement
If Process A attempts to read or write to a memory address outside its registered page tables or belonging to Process B:
1. The MMU hardware intercepts the invalid memory dereference.
2. The CPU generates a hardware trap and interrupts the Linux kernel.
3. The kernel immediately terminates Process A with a **Segmentation Fault (`SIGSEGV`)**.

**Process isolation is strictly enforced by CPU hardware through this page-table barrier.**

---

## 💀 2. The Exploit: Deconstructing `/dev/mem` Memory Scraping

In Unix and Linux systems, physical hardware components are exposed as device nodes within the filesystem tree.

### What is `/dev/mem`?
`/dev/mem` is a character device file (Major number `1`, Minor number `1`) that represents **the complete, physical memory (RAM) of the host computer**.
- Reading `/dev/mem` at offset `0` reads physical byte 0 of the host's RAM stick.
- Reading `/dev/mem` at offset `4,000,000,000` reads the physical byte at the 4 GB marker.

### The Boundary Bypass
When a process opens `/dev/mem`, **it completely bypasses the MMU, the page tables, and the virtual memory sandbox**:

```
+-----------------------------------------------------------------------------------+
|                             THE /dev/mem BYPASS ATTACK                            |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ Compromised Pod A ]                                                            |
|         │                                                                         |
|         │ Executes: head -c 100M /dev/mem                                         |
|         ▼                                                                         |
|  ===============================================================================  |
|     BYPASSES MMU HARDWARE WALLS & PAGE TABLES (Zero Virtual Memory Sandbox)       |
|  ===============================================================================  |
|         │                                                                         |
|         ▼                                                                         |
|  [ THE PHYSICAL RAM CHIP (ALL PROCESSES STORED HERE IN CLEAR TEXT) ]              |
|         │                                                                         |
|         ├──► Reads etcd unencrypted memory cache (Cluster Admin Tokens)           |
|         ├──► Reads kube-apiserver private TLS keys (/etc/kubernetes/pki)          |
|         ├──► Reads plaintext passwords handled by Pod B, C, D                     |
|         └──► Reads Linux Kernel core structures (task_struct, creds)              |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### What "Scraping Raw RAM Buffers" Means in Practice
Even if databases or Kubernetes secrets are encrypted at rest on disk (`aescbc` in etcd), **the exact moment the CPU processes that data, it MUST reside in physical RAM in plain text**:
- If an attacker gains access to `/dev/mem`, they run utilities like `strings /dev/mem | grep -i "BEGIN RSA PRIVATE KEY"` or grep for `Bearer eyJhbGci...`.
- They can harvest TLS private keys, cluster tokens, database connection strings, and passwords belonging to other tenants and host system daemons without making a single Kubernetes API call.

Because containerized applications never have a legitimate operational need to inspect physical host RAM, any container access to `/dev/mem` is an **unambiguous Indicator of Compromise (IoC)**.

---

## 🔬 3. Falco Architecture: Kernel Syscall Interception via eBPF

To catch attacks that occur inside running containers in real time, **Falco** hooks directly into the **Linux kernel** using extended Berkeley Packet Filters (**eBPF**) or a dedicated kernel module:

```
+-----------------------------------------------------------------------------------+
|                            FALCO eBPF RUNTIME ARCHITECTURE                        |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ Compromised Pod ] (Process: cat /dev/mem)                                      |
|             │                                                                     |
|             │ Syscall: sys_openat(fd, "/dev/mem", O_RDONLY)                       |
|             ▼                                                                     |
|  ===============================================================================  |
|                         LINUX KERNEL TRACEPOINTS (eBPF)                           |
|  ===============================================================================  |
|             │                                                                     |
|             │ Event captured in kernel space (< 50 microseconds)                  |
|             ▼                                                                     |
|  +-----------------------------------------------------------------------------+  |
|  | FALCO DAEMON (Userspace Security Engine)                                    |  |
|  | - Consumes syscall event stream from ring buffer                            |  |
|  | - Enriches with Kubernetes metadata (Pod, Namespace, Container ID)          |  |
|  | - Evaluates rules in /etc/falco/falco_rules.local.yaml                      |  |
|  +--------------------------------------┬--------------------------------------+  |
|                                         │ MATCH: Condition met!                   |
|                                         ▼                                         |
|  [ ALERT GENERATED ] ──► Emitted to journald / syslog                             |
|  "Suspicious /dev/mem access (pod=rogue-inspector ns=threat-zone user=root...)"   |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

---

## 📝 4. Falco Rule Anatomy: `/etc/falco/falco_rules.local.yaml`

Default rules are stored in `/etc/falco/falco_rules.yaml`. Custom organizational rules must **always** be appended to **`/etc/falco/falco_rules.local.yaml`** so they are preserved across package updates.

```yaml
- rule: Detect /dev/mem Access
  desc: Alert when any process opens /dev/mem
  condition: container and open_read and fd.name = "/dev/mem"
  output: "Suspicious /dev/mem access (pod=%k8s.pod.name ns=%k8s.ns.name user=%user.name cmd=%proc.cmdline file=%fd.name)"
  priority: WARNING
  tags: [filesystem, mitre_discovery]
```

### Deconstructing the Schema Fields:
```
+---------------------------------------------------------------------------------------------------+
|                                     FALCO RULE FIELD REFERENCE                                    |
+---------------------------------------------------------------------------------------------------+
| FIELD      | VALUE                                    | MEANING                                   |
+------------+------------------------------------------+-------------------------------------------+
| rule       | Detect /dev/mem Access                   | Unique human-readable rule identifier.    |
+------------+------------------------------------------+-------------------------------------------+
| condition  | container and open_read and              | Boolean expression filtering the event.   |
|            | fd.name = "/dev/mem"                     | Requires event in container, open_read,   |
|            |                                          | targeting file path /dev/mem.             |
+------------+------------------------------------------+-------------------------------------------+
| output     | "Suspicious ... (%k8s.pod.name ...)"     | Formatted alert string with context macros|
|            |                                          | (%k8s.pod.name, %proc.cmdline, %fd.name). |
+------------+------------------------------------------+-------------------------------------------+
| priority   | WARNING                                  | Severity level (EMERGENCY, ALERT,         |
|            |                                          | CRITICAL, ERROR, WARNING, NOTICE, INFO).  |
+------------+------------------------------------------+-------------------------------------------+
| tags       | [filesystem, mitre_discovery]            | Taxonomical categories for SIEM triage.   |
+---------------------------------------------------------------------------------------------------+
```

### ⚠️ Falco Condition Syntax Rules: Why `fd.name = "/dev/mem"` Strictly Requires Quotes
1. **The Lexer & Path Parsing Trap:**
   Falco's condition parser distinguishes between **identifiers/macros** (e.g., `container`, `open_read`) and **literal values**.
   Because file paths contain forward slashes (`/`), if you omit double quotes (e.g. `fd.name = /dev/mem`):
   - The parser attempts to evaluate `/` as a syntax operator or token.
   - Falco crashes with `LOAD_ERR_VALIDATE: Syntax error near '/dev/mem'`.
   - **Rule:** Any string literal, path, or command parameter MUST be enclosed in double quotes: `"/dev/mem"`, `"/etc/shadow"`, `"nc"`.
2. **Spacing Around Operators:**
   - Both `fd.name = "/dev/mem"` and `fd.name="/dev/mem"` are valid for Falco's parser.
   - However, always adhere to single spaces around operators (`fd.name = "/dev/mem"`) to ensure strict compatibility with automated exam grading scripts.

---

## 🎯 5. Real Exam Question 04: End-to-End Walkthrough

### Scenario
A compromised workload in namespace `threat-zone` is attempting memory inspection.
1. Append rule `Detect /dev/mem Access` to `/etc/falco/falco_rules.local.yaml`.
2. Reload/restart Falco.
3. Identify the malicious Pod in namespace `threat-zone` triggering the alert.
4. Scale the offending Deployment down to **0 replicas**.

---

### Step-by-Step Exam Execution

#### Step 1: Append Rule to Local Rules File
Open `/etc/falco/falco_rules.local.yaml`:
```bash
sudo vi /etc/falco/falco_rules.local.yaml
```
Append the exact rule block:
```yaml
- rule: Detect /dev/mem Access
  desc: Alert when any process opens /dev/mem
  condition: container and open_read and fd.name = "/dev/mem"
  output: "Suspicious /dev/mem access (pod=%k8s.pod.name ns=%k8s.ns.name user=%user.name cmd=%proc.cmdline file=%fd.name)"
  priority: WARNING
  tags: [filesystem, mitre_discovery]
```

#### Step 2: Validate Rule Syntax & Restart Falco
Validate configuration before restarting:
```bash
falco --validate /etc/falco/falco_rules.local.yaml
```
Restart the systemd service:
```bash
sudo systemctl restart falco
# Verify active status:
sudo systemctl status falco
```

#### Step 3: Forensic Log Analysis
Inspect the systemd journal for the emitted alert string:
```bash
journalctl -u falco -n 100 --no-pager | grep "Suspicious /dev/mem access"
```

**Forensic Output:**
```text
Oct 07 14:22:01 worker-01 falco[14521]: 14:22:01.120349123: Warning Suspicious /dev/mem access 
(pod=rogue-inspector-7c6d8f58c7-2k9x4 ns=threat-zone user=root cmd=head -c 100 /dev/mem file=/dev/mem)
```

**Identified Offender:**
- Pod: `rogue-inspector-7c6d8f58c7-2k9x4`
- Namespace: `threat-zone`

#### Step 4: Identify Parent Deployment
```bash
kubectl get deployment -n threat-zone
# Output: rogue-inspector
```

#### Step 5: Remediate Workload (Scale to 0)
```bash
kubectl scale deployment rogue-inspector -n threat-zone --replicas=0
```

Verify pod termination:
```bash
kubectl get pods -n threat-zone
# Output: No resources found in threat-zone namespace.
```

---

## ⚡ 6. Speed & Troubleshooting Tips for the Exam

1. **Hot-Reloading without Dropping Syscalls:**
   Instead of restarting systemd, send `SIGHUP` to the process:
   ```bash
   sudo kill -1 $(pidof falco)
   ```
2. **Log Grep Precision:**
   If logs are verbose, follow the live stream filtered by priority:
   ```bash
   journalctl -u falco -f | grep -i "Warning"
   ```

---

## 🔗 Related Master Notes & References
- Parent Landing Note: [[Main Notes/Kubernetes Runtime Security and Threat Forensics|Kubernetes Runtime Security and Threat Forensics]]
- Linux Kernel Introspection: [[Main Notes/Linux Proc Filesystem - Kernel Introspection, Process Memory, and Security Auditing|Linux Proc Filesystem & Process Memory]]
- Workload Hardening: [[Main Notes/Kubernetes Workload Security and Container Hardening|Workload Security & Container Hardening]]
- Reference Guide: [[Reference Notes/0-7-6_runtime_security_falco_and_audit_logging.md|Module 0-7-6: Runtime Security, Syscall Threat Detection & API Auditing Masterclass]]
