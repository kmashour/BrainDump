---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: master-curriculum-hub
domains:
  - kubernetes
  - security
  - cks
  - linux-kernel
related_concepts:
  - "[[CKA Certification Real Exam 2026 - Master Curriculum and Question Navigation Hub]]"
  - "[[CKAD Real Exam 2026 - Master Curriculum and Question Navigation Hub]]"
against: []
reference_guides:
  - "[[Reference Notes/0-7-1_kubernetes_security_foundations_and_attack_surface.md]]"
  - "[[Reference Notes/0-7-2_cluster_setup_and_hardening.md]]"
tags:
  - kubernetes/cks
  - kubernetes/exam-prep
  - kubernetes/curriculum-map
  - status/completed
---

# 🛡️ CKS Master Curriculum & Knowledge Directory: What's Inside Every Note

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Master Index]] > **CKS Master Curriculum & Knowledge Directory**

---

## 🎯 Purpose of This Knowledge Directory

Navigating technical notes by title alone can be confusing during intense exam preparation. This directory solves that by mapping **every single Main Note in your Second Brain** directly into the **6 Official CKS Exam Curriculum Modules** (plus the foundational **Linux Operating System Architecture**).

For each note, you will find:
1. **Direct Link:** Instant navigation to the atomic note.
2. **What's Inside:** A detailed breakdown of the exact technical concepts, kernel subsystems, and architectural flows explained in the note.
3. **Key Files, Flags & Syntax:** The critical configurations, YAML blocks, and CLI flags documented.
4. **Failure Modes & Traps Unmasked:** The subtle traps, silent errors, and debugging workflows captured.
5. **Exam Scenario Alignment:** The specific CKS simulation question (Q01 to Q16) or exam objective it prepares you to solve.

---

```
===================================================================================================
                                CKS CURRICULUM ARCHITECTURE AT A GLANCE
===================================================================================================

  [ Linux Kernel Foundation ] ──► System Calls, FDs, Procfs, Namespaces, Socket Activation
             │
             ├──► [ Module 01: Cluster Setup & Threat Modeling ] ──► 4Cs, NetPol, Ingress, Node Upgrades
             │
             ├──► [ Module 02: Cluster Component Hardening ]    ──► Kubelet Auth, etcd mTLS, API Auditing
             │
             ├──► [ Module 03: System Hardening & Isolation ]   ──► Docker Sockets, Immutability, Caps, AppArmor, Seccomp
             │
             ├──► [ Module 04: Microservice & Identity ]        ──► PSA Restricted, Token Projection, Istio mTLS, etcd Crypt
             │
             ├──► [ Module 05: Supply Chain & Admission ]       ──► Dockerfile nobody, SBOM bom, ImagePolicyWebhook
             │
             └──► [ Module 06: Runtime Threat & Forensics ]     ──► Falco eBPF, /dev/mem Scraping, Audit Forensics
===================================================================================================
```

---

## 🐧 FOUNDATION: Linux Operating System Architecture & Kernel Internals

These notes cover the foundational Linux operating system primitives upon which all containerization, Kubernetes isolation, and runtime security depend.

---

### 1. [[Main Notes/Linux Operating System Architecture and Kernel Mechanics|Linux Operating System Architecture and Kernel Mechanics]] *(Landing Note)*
* **Role:** Architectural hub for core Linux OS concepts.
* **What's Inside:**
  - The hardware-to-userland execution hierarchy: Hardware -> Ring 0 (Kernel Space) -> Ring 3 (User Space).
  - How system calls (`syscalls`) act as the controlled gateway between unprivileged userland programs and kernel privileged execution.
  - The structural decomposition of Linux subsystems: Process Scheduler, Virtual File System (VFS), Network Stack, Memory Management, and Inter-Process Communication (IPC).
  - First-principles definition of containers: containers are not virtual machines; they are standard Linux processes isolated via Kernel Namespaces and restricted via Control Groups (cgroups).

---

### 2. [[Main Notes/Linux Process Lifecycle - Fork, Clone Syscalls, and PID Namespaces|Linux Process Lifecycle: Fork, Clone Syscalls & PID Namespaces]] *(Deeper Dive)*
* **Role:** Deconstructs how Linux creates, duplicates, and isolates running processes.
* **What's Inside:**
  - The evolution of process creation: `fork()` (duplicate memory via copy-on-write) vs. `execve()` (replace binary in process image) vs. `clone()` (fine-grained sharing flags).
  - The 8 Linux Kernel Namespaces (`CLONE_NEWPID`, `CLONE_NEWNET`, `CLONE_NEWNS`, `CLONE_NEWIPC`, `CLONE_NEWUTS`, `CLONE_NEWUSER`, `CLONE_NEWCGROUP`, `CLONE_NEWTIME`).
  - How PID 1 inside a container namespace maps to an arbitrary high-numbered PID on the host node kernel.
  - The "Zombie Process" problem: why PID 1 inside a container must reap orphaned child processes (`waitpid()`), and how `tini` or `shareProcessNamespace: true` solves orphan accumulation.
* **Key Pitfalls Addressed:** The silent starvation of container memory when container PID 1 fails to reap defunct zombie children.

---

### 3. [[Main Notes/Linux File Descriptors - Socket Activation, FD Passing, and Container Breakouts|Linux File Descriptors: Socket Activation, FD Passing & Container Breakouts]] *(Deeper Dive)*
* **Role:** Explains Linux I/O mechanics, file descriptors, and socket handoffs.
* **What's Inside:**
  - The UNIX axiom: *"Everything is a file"*. Deconstructs the Process File Descriptor Table, System-Wide Open File Table, and Inode Table.
  - The standard descriptors: `0` (stdin), `1` (stdout), `2` (stderr).
  - Systemd Socket Activation: how systemd listens on a network socket (FD 3) and passes it directly to a newly launched daemon on the first incoming packet without dropping connections.
  - The Leaked File Descriptor Threat: how an unclosed FD passed across `fork`/`execve` (missing `O_CLOEXEC` flag) allows a child process inside a chroot/container to escape back to the host filesystem.
* **Exam Relevance:** Directly underpins **Question 13 (Securing Docker Daemon)** and container isolation auditing.

---

### 4. [[Main Notes/Linux Proc Filesystem - Kernel Introspection, Process Memory, and Security Auditing|Linux Proc Filesystem: Kernel Introspection, Process Memory & Security Auditing]] *(Deeper Dive)*
* **Role:** Deep dive into `/proc` as the real-time kernel memory window.
* **What's Inside:**
  - The `/proc` virtual filesystem architecture: `/proc` contains no physical files on disk; every read operation synthesizes data directly from kernel memory structs on the fly.
  - Process inspection structures: `/proc/<PID>/cmdline`, `/proc/<PID>/environ`, `/proc/<PID>/fd/`, and `/proc/<PID>/status`.
  - Security auditing via procfs: Inspecting capability bitmasks (`CapInh`, `CapPrm`, `CapEff`, `CapBnd`) and AppArmor confinement states via `/proc/<PID>/attr/current`.
  - Process memory dumping: `/proc/<PID>/mem` and why memory scraping attacks like `/dev/mem` or `/proc/<PID>/mem` theft are critical runtime risks.
* **Exam Relevance:** Directly underpins **Question 04 (Falco /dev/mem)** and auditing active AppArmor profiles without host utilities.

---

## 🏛️ MODULE 01: Cluster Setup, Threat Modeling & Network Hardening (10-15%)

This module covers the overall cloud-native attack surface, perimeter defense, network segmentation, and cluster upgrade maintenance.

---

### 1. [[Main Notes/Kubernetes Attack Surface and the 4Cs of Cloud Native Security|Kubernetes Attack Surface and the 4Cs of Cloud Native Security]] *(Landing Note)*
* **Role:** High-level strategic model for layered cloud-native defense.
* **What's Inside:**
  - The Cloud Native Computing Foundation (CNCF) 4Cs Security Hierarchy: **Cloud**, **Cluster**, **Container**, and **Code**.
  - Why outer layers dictate inner layer security: a compromised Cloud layer (e.g. leaked AWS IAM keys) renders all cluster and container security controls useless.
  - Architectural role of each layer and where CKS security controls fit across the stack.

---

### 2. [[Main Notes/Kubernetes Attack Surface - 4Cs Layer Exploits and the Voting App Kill Chain|Kubernetes Attack Surface: 4Cs Layer Exploits & The Voting App Kill Chain]] *(Deeper Dive)*
* **Role:** Practical attack simulation modeling a real-world multi-stage breach.
* **What's Inside:**
  - The End-to-End Kill Chain breakdown on an exemplary multi-tier application:
    1. *Code:* Remote code execution (RCE) via web framework exploit.
    2. *Container:* Container breakout via writable root filesystem, mounted `/var/run/docker.sock`, or excessive Linux capabilities (`CAP_SYS_ADMIN`).
    3. *Cluster:* ServiceAccount token theft from `/var/run/secrets/kubernetes.io/serviceaccount/token` and privilege escalation via permissive RBAC.
    4. *Cloud:* Instance metadata service (IMDSv1 at `169.254.169.254`) query extracting node IAM credentials.
  - Defenses mapped to every phase: Read-only roots, non-root users, token projection, NetworkPolicies, and IMDSv2 hop limits.

---

### 3. [[Main Notes/Kubernetes Network Security and Traffic Segregation|Kubernetes Network Security and Traffic Segregation]] *(Landing Note)*
* **Role:** Architectural hub for network segmentation and traffic control.
* **What's Inside:**
  - The fundamental Kubernetes flat-network design: by default, all pods can communicate with all other pods across all namespaces without NAT.
  - The role of the Container Network Interface (CNI) plugin (Calico, Cilium, Flannel) in enforcing NetworkPolicies.
  - High-level isolation strategies: Default-Deny, Multi-tenant namespace isolation, egress lockdown, and Ingress TLS termination.

---

### 4. [[Main Notes/Kubernetes Network Policies - Default Deny Ingress, Multi-Tenant Whitelisting, and Selector Logic|Kubernetes Network Policies: Default Deny Ingress, Whitelisting & Selector Logic]] *(Deeper Dive)*
* **Role:** Step-by-step policy creation, selector Boolean logic, and whitelist architecture.
* **What's Inside:**
  - The Default-Deny Ingress baseline: `policyTypes: ["Ingress"]` with an empty `ingress: []` block.
  - The "Additive Whitelist" rule: Once a NetworkPolicy selects a pod, that pod enters isolated mode; only explicitly defined rules allow traffic through.
  - The `from:` block Boolean Logic:
    - Multiple items in a single list item (AND logic): `namespaceSelector` AND `podSelector`.
    - Multiple separate list items (OR logic): `namespaceSelector` OR `podSelector`.
  - Port definitions and protocol specification (`TCP` on port `80`/`6379`).
* **Key Pitfalls Addressed:** Accidental wildcard exposure by omitting `podSelector` inside a `namespaceSelector`, or assuming NetworkPolicies work without a CNI provider that supports policy enforcement.
* **Exam Scenario Alignment:** **Question 07 (`q07-network-policy`)** — Isolating namespaces and whitelisting specific backend microservices.

---

### 5. [[Main Notes/Kubernetes Ingress Security - TLS Termination, Force-HTTPS, and Controller Annotations|Kubernetes Ingress Security: TLS Termination, Force-HTTPS & Controller Annotations]] *(Deeper Dive)*
* **Role:** Edge routing security, TLS certificate termination, and HTTP-to-HTTPS redirect enforcement.
* **What's Inside:**
  - The Ingress architecture: Ingress Resource (routing spec) vs. Ingress Controller (reverse proxy implementation like Nginx, Traefik, or Cilium).
  - TLS termination mechanics: decrypting HTTPS traffic at the cluster perimeter and passing cleartext HTTP inside the internal cluster network.
  - Creating TLS Secrets: `kubectl create secret tls <name> --cert=... --key=...`.
  - Configuring the `tls:` stanza in Ingress manifests (`hosts` and `secretName`).
  - Enforcing HTTPS redirects via controller annotations: `nginx.ingress.kubernetes.io/ssl-redirect: "true"` and `force-ssl-redirect: "true"`.
* **Key Pitfalls Addressed:** Hostname mismatch between the TLS certificate Common Name (CN)/SAN and the Ingress `rules.host` field; missing `tls:` block resulting in plain HTTP fallback.
* **Exam Scenario Alignment:** **Question 02 (`q02-tls-secret`)** and **Question 08 (`q08-ingress-tls`)**.

---

### 6. [[Main Notes/Kubernetes Node Maintenance - Kubeadm Upgrades, APT Hold Mechanics, and Package Lifecycle|Kubernetes Node Maintenance: Kubeadm Upgrades, APT Hold Mechanics & Package Lifecycle]] *(Deeper Dive)*
* **Role:** Safe worker node maintenance, version parity, and operating system package management.
* **What's Inside:**
  - The 3-Step Node Evacuation workflow: `kubectl cordon <node>` -> `kubectl drain <node> --ignore-daemonsets --delete-emptydir-data --force` -> maintenance -> `kubectl uncordon <node>`.
  - Why the drain flags are strictly mandatory in production and the exam: DaemonSets cannot be evicted, and pods with local `emptyDir` storage require explicit deletion authorization.
  - APT Package Management on Ubuntu/Debian: Unholding pinned packages (`apt-mark unhold kubeadm kubelet kubectl`), upgrading to exact patch versions, and re-holding (`apt-mark hold`).
  - Upgrading sequence: Control plane first (`kubeadm upgrade apply`), then Worker nodes (`kubeadm upgrade node`), followed by `systemctl restart kubelet`.
  - **Target Version Discovery Formula:** When prompts omit the target version, deduce it by matching the control plane version (`kubectl get nodes`).
  - **Why Upgrade `kubectl` on Workers:** While not strictly needed by Kubelet to run pods, it is required for on-node emergency debugging (`--kubeconfig /etc/kubernetes/kubelet.conf`), satisfies the $\pm 1$ version skew policy, and fulfills autograder `dpkg -l` assertions.
* **Key Pitfalls Addressed:** Attempting `kubeadm upgrade apply` on worker nodes; missing drain flags; package suffix mismatch in `apt`; omitting `kubectl uncordon`.
* **Exam Scenario Alignment:** **Question 10 (`q10-node-upgrade`)** — Live worker node upgrade drill.

---

## 🔒 MODULE 02: Cluster Component Hardening & Control Plane Security (20%)

This module focuses on locking down core control plane binaries (Kubelet, etcd, API Server), mutual TLS authentication, and comprehensive audit logging.

---

### 1. [[Main Notes/Kubernetes Cluster Component Hardening and Communication Security|Kubernetes Cluster Component Hardening and Communication Security]] *(Landing Note)*
* **Role:** Architectural hub for securing the control plane and cluster component communication channels.
* **What's Inside:**
  - The Control Plane communication mesh: API Server at the center, communicating with Kubelet, etcd, Controller Manager, and Scheduler.
  - The requirement for Mutual TLS (mTLS): why every internal hop must require valid x509 client certificates signed by the cluster Certificate Authority (CA).
  - Hardening principles: Disabling anonymous authentication, enforcing RBAC authorization, and securing static pod manifests in `/etc/kubernetes/manifests/`.

---

### 2. [[Main Notes/Kubernetes Component Security - Kubelet Port 10250, etcd Client Auth, and mTLS Handshake Mechanics|Kubernetes Component Security: Kubelet Port 10250, etcd Client Auth & mTLS Handshake]] *(Deeper Dive)*
* **Role:** Securing Kubelet worker daemons and etcd key-value datastores.
* **What's Inside:**
  - **The Kubelet Port 10250 Vulnerability:** Why default Kubelet allows unauthenticated `system:anonymous` access to `/run`, `/exec`, and pod logs if `--anonymous-auth=true` is left open.
  - Fixing Kubelet in `/var/lib/kubelet/config.yaml`:
    - `authentication.anonymous.enabled: false`
    - `authentication.x509.clientCAFile: /etc/kubernetes/pki/ca.crt`
    - `authorization.mode: Webhook` (forces Kubelet to ask API Server via SubjectAccessReview if the caller is authorized).
  - **The etcd Client Authentication Architecture:** Locking down port `2379`.
  - Enforcing etcd flags in `/etc/kubernetes/manifests/etcd.yaml`: `--client-cert-auth=true`, `--trusted-ca-file=...`, `--cert-file=...`, `--key-file=...`.
  - Verifying etcd with `etcdctl` using the 3 required PKI flags: `--cacert`, `--cert`, `--key`.
* **Key Pitfalls Addressed:** Modifying `/etc/kubernetes/manifests/kubelet.yaml` (which does not exist—Kubelet is a systemd unit configured in `/var/lib/kubelet/config.yaml`); forgetting to `systemctl restart kubelet`.
* **Exam Scenario Alignment:** **Question 01 (`q01-kubelet-etcd`)** — Remediating insecure Kubelet and etcd.

---

### 3. [[Main Notes/Kubernetes API Server Security - Request Lifecycle, NodeRestriction, and Protected Namespaces|Kubernetes API Server Security: Request Lifecycle, NodeRestriction & Protected Namespaces]] *(Deeper Dive)*
* **Role:** Securing the kube-apiserver binary, admission controllers, and node authority boundaries.
* **What's Inside:**
  - The 3-Phase API Server Request Pipeline: **Authentication** -> **Authorization** (Node, RBAC) -> **Admission Control** (Mutating & Validating).
  - Disabling anonymous API access: `--anonymous-auth=false`.
  - Authorizer chain ordering: `--authorization-mode=Node,RBAC` (Node authorizer intercepts kubelet requests first; RBAC handles user and service workloads).
  - **The `NodeRestriction` Admission Controller:** How it prevents a compromised worker node's Kubelet from modifying pods on other nodes, claiming labels outside `node-restriction.kubernetes.io/`, or deleting secrets outside its own pods.
* **Key Pitfalls Addressed:** Removing the `Node` authorizer breaks Kubelet heartbeat and lease renewals; syntax typos in `--enable-admission-plugins` crashing the API server static pod.
* **Exam Scenario Alignment:** **Question 16 (`q16-apiserver-auth`)** — API Server hardening and NodeRestriction admission.

---

### 4. [[Main Notes/Kubernetes API Server Auditing - Policy Stages, Log Retention, and Volume Mount Isolation|Kubernetes API Server Auditing: Policy Stages, Log Retention & Volume Mount Isolation]] *(Deeper Dive)*
* **Role:** Comprehensive guide to audit policies, stages, log rotation, and volume mounts.
* **What's Inside:**
  - The 4 Audit Stages: `RequestReceived`, `ResponseStarted`, `ResponseComplete`, `Panic`.
  - The 4 Audit Levels: `None` (silent), `Metadata` (who, when, what URI), `Request` (metadata + request body), `RequestResponse` (full payload + response body).
  - **The Audit vs. etcd Encryption Paradox:** Audit logging intercepts requests at the REST layer *before* admission and encryption providers execute. Logging `secrets` or `configmaps` at `RequestResponse` writes plain unencrypted Base64 secret strings to `/var/log/kubernetes/audit/audit.log`, completely bypassing etcd encryption at rest! Secrets must ALWAYS be logged at `Metadata`.
  - Audit Log Retention Flags: `--audit-log-path=/var/log/kubernetes/audit/audit.log`, `--audit-log-maxage=10`, `--audit-log-maxbackup=2`, `--audit-log-maxsize=100`.
  - Static Pod Mount Isolation: Why hostPath `type: DirectoryOrCreate` is required over `FileOrCreate` (log rotation creates new files and backup archives, breaking single-file mounts).
* **Key Pitfalls Addressed:** API server boot-loops caused by missing hostPath volume mounts for `/etc/kubernetes/audit` or `/var/log/kubernetes/audit`; using `FileOrCreate` on directory paths causing `ENOTDIR` crashes.
* **Exam Scenario Alignment:** **Question 06 (`q06-audit-logging`)** — Implementing audit policies and retention flags.

---

## ⚙️ MODULE 03: System Hardening, Host OS & Workload Isolation (15%)

This module hardens container runtimes, eliminates root privileges, strips Linux capabilities, and confines workloads using host Mandatory Access Control (AppArmor) and Syscall filtering (Seccomp).

---

### 1. [[Main Notes/Kubernetes Workload Security and Container Hardening|Kubernetes Workload Security and Container Hardening]] *(Landing Note)*
* **Role:** Architectural hub for container isolation, least privilege, and Linux kernel sandboxing.
* **What's Inside:**
  - The threat model of shared-kernel multi-tenancy: every container on a node shares the same underlying Linux kernel.
  - Defense-in-depth layers: Non-root execution (`runAsUser`), Read-only filesystems (`readOnlyRootFilesystem`), Capability stripping (`drop: [ALL]`), AppArmor MAC profiles, and Seccomp syscall filtering.
  - Architectural differentiation between Pod-level and Container-level `securityContext`.

---

### 2. [[Main Notes/Kubernetes Node Security - Host OS Hardening, Docker Daemon, and Socket Isolation|Kubernetes Node Security: Host OS Hardening, Docker Daemon & Socket Isolation]] *(Deeper Dive)*
* **Role:** Securing the host operating system, Docker daemon, and UNIX sockets.
* **What's Inside:**
  - The `/var/run/docker.sock` threat: anyone with write access to the Docker socket has unhindered root authority over the host operating system (can launch containers mounting `/`).
  - Restricting Docker socket permissions: Ensuring ownership `root:docker` and mode `0660`.
  - Securing Docker daemon in `/etc/docker/daemon.json`: Disabling remote unauthenticated TCP listening on `0.0.0.0:2375`, configuring TLS mutual authentication for remote management, and enabling `userns-remap`.
  - Systemd socket activation audit: `systemctl status docker.socket`.
* **Key Pitfalls Addressed:** Exposing unencrypted TCP socket `0.0.0.0:2375` without TLS certificates; mounting `/var/run/docker.sock` inside untrusted tenant pods.
* **Exam Scenario Alignment:** **Question 13 (`q13-secure-docker`)** — Securing Docker daemon and socket files.

---

### 3. [[Main Notes/Kubernetes Container Hardening - Immutability, SecurityContext Trinity, and Multi-Container Configurations|Kubernetes Container Hardening: Immutability, SecurityContext Trinity & Multi-Container Configs]] *(Deeper Dive)*
* **Role:** The practical implementation of container immutability and multi-container hardening.
* **What's Inside:**
  - **The SecurityContext Trinity:**
    1. `readOnlyRootFilesystem: true` — Eliminates file-based malware downloads and backdoor installations.
    2. `allowPrivilegeEscalation: false` — Sets the Linux kernel `no_new_privs` bit, blocking SUID binaries (`chmod u+s`) from escalating privileges.
    3. `runAsUser: 30000` / `runAsNonRoot: true` — Guarantees the process executes as a non-zero UID.
  - Handling applications requiring temporary write space: mounting memory-backed `emptyDir` scratchpads at `/tmp` or `/var/log` with `readOnly: false`.
  - **Multi-Container Pod Traps:** How to harden pods containing multiple containers (`2/2`). Schema rules: `readOnlyRootFilesystem` and `allowPrivilegeEscalation` MUST be declared under individual `containers[i].securityContext`, not pod-level!
* **Key Pitfalls Addressed:** Declaring container-only fields at `spec.securityContext` resulting in silent YAML validation rejection; crashing read-only containers because application logs or temp files cannot be written.
* **Exam Scenario Alignment:** **Question 05 (`q05-container-immutability`)** — Multi-container pod hardening drill.

---

### 4. [[Main Notes/Kubernetes Volume Permissions - fsGroup Mechanics, Supplemental Groups, and RootMismatch Optimization|Kubernetes Volume Permissions: fsGroup Mechanics, Supplemental Groups & RootMismatch Optimization]] *(Deeper Dive)*
* **Role:** Resolving volume permission deadlocks for non-root containers.
* **What's Inside:**
  - The Non-Root Volume Deadlock: When a container runs as `runAsUser: 10001`, how does it read/write to a mounted PersistentVolume owned by `root:root (0:0)`?
  - `fsGroup` Mechanics: Kubernetes dynamically assigns a supplemental GID (e.g. `fsGroup: 2000`) and adds it to the container process.
  - The `setgid` bit (`g+s`): Volumes mounted with `fsGroup` have their root ownership changed to the GID, and new files automatically inherit the group ID.
  - The Recursive `chown` Performance Problem: Large volumes with millions of files hanging during pod startup.
  - The Solution: **`fsGroupChangePolicy: "OnRootMismatch"`** (only executes `chown` if the top-level directory ownership does not match the desired GID).
* **Key Pitfalls Addressed:** Pods stuck in `CrashLoopBackOff` or `ContainerCreating` due to recursive permissions scanning on large storage volumes.

---

### 5. [[Main Notes/Kubernetes Workload Security - Linux Capabilities Stripping, CAP_NET_RAW, and eBPF Profiling|Kubernetes Workload Security: Linux Capabilities Stripping, CAP_NET_RAW & eBPF Profiling]] *(Deeper Dive)*
* **Role:** POSIX capabilities architecture, container default sets, and eBPF profiling.
* **What's Inside:**
  - Why POSIX capabilities exist: Deconstructing traditional binary root (UID 0) into ~40 discrete privileges (`CAP_*`) to eliminate SUID vulnerabilities.
  - The Dangerous Default Set: Container runtimes grant ~14 default capabilities to every pod, including **`CAP_NET_RAW`** (allows raw packet crafting, ARP spoofing, and DNS hijacking in flat pod networks).
  - The Golden Least-Privilege Rule:
    ```yaml
    securityContext:
      capabilities:
        drop: ["ALL"]
        add: ["NET_BIND_SERVICE"]
    ```
  - Schema Rules: Omit the `CAP_` prefix; uppercase `ALL`; declare only under `containers[].securityContext`.
  - **Capability Profiling:** How the kernel checks `capable(CAP_...)` and returns `EPERM`; profiling live workloads using **Inspektor Gadget** (`kubectl gadget trace capabilities`) and host `bcc-tools capable`.
* **Exam Relevance:** Foundation for **Question 12 (Pod Security Admission Restricted)**.

---

### 6. [[Main Notes/Kubernetes Workload Security - AppArmor Mandatory Access Control, Profile Lifecycle, and Modern v1.30 Syntax|Kubernetes Workload Security: AppArmor Mandatory Access Control, Profile Lifecycle & Modern v1.30 Syntax]] *(Deeper Dive)*
* **Role:** Host-level Mandatory Access Control (MAC) profiles and pod confinement.
* **What's Inside:**
  - DAC vs. MAC: Discretionary Access Control (file owner discretion, bypassed by root) vs. Mandatory Access Control (kernel policy overrides root).
  - Profile Anatomy: Enforce mode vs. Complain mode; path permissions (`r`=read, `w`=write, `x`=execute, `ix`=inherit execute).
  - The 3-Step Node-to-Pod Lifecycle:
    1. Write profile on node: `/etc/apparmor.d/k8s-deny-write`
    2. Load into host kernel: `sudo apparmor_parser -q /etc/apparmor.d/k8s-deny-write`
    3. Enforce in Pod YAML: Native **Kubernetes 1.30+ GA** syntax:
       ```yaml
       securityContext:
         appArmorProfile:
           type: Localhost
           localhostProfile: k8s-deny-write
       ```
  - Terminal Verification: Checking `/proc/1/attr/current` inside the container without needing `aa-status`.
* **Key Pitfalls Addressed:** The Multi-Node Scheduling Trap (loading a profile on controlplane but pod schedules on node01, causing `CreateContainerError`); using deprecated annotation syntax (`container.apparmor.security.beta.kubernetes.io/`).

---

### 7. [[Main Notes/Kubernetes Workload Security - Seccomp BPF Syscall Filtering and RuntimeDefault Profiles|Kubernetes Workload Security: Seccomp BPF Syscall Filtering & RuntimeDefault Profiles]] *(Deeper Dive)*
* **Role:** Secure Computing Mode (Seccomp) Berkeley Packet Filter (BPF) system call isolation.
* **What's Inside:**
  - What Seccomp does: Restricts the ~450 Linux kernel system calls available to a process; blocks dangerous syscalls (`ptrace`, `sys_chroot`, `reboot`, `bpf`).
  - The **`RuntimeDefault`** profile: The container runtime's built-in seccomp filter blocking ~50 dangerous syscalls while keeping standard apps operational.
  - Modern native syntax in Kubernetes:
    ```yaml
    securityContext:
      seccompProfile:
        type: RuntimeDefault  # Options: RuntimeDefault, Localhost, Unconfined
    ```
  - Custom profiles: Stored in `/var/lib/kubelet/seccomp/<profile>.json` on worker nodes; referenced via `type: Localhost` and `localhostProfile: my-profile.json`.
* **Key Pitfalls Addressed:** Custom seccomp profiles referencing paths outside `/var/lib/kubelet/seccomp/` (Kubelet rejects absolute paths or parent traversal `../`); running workloads as `Unconfined`.

---

## 👥 MODULE 04: Microservice Protection, Identity & Workload Security (20%)

This module focuses on workload identity, Pod Security Admission (PSA), automated service mesh encryption (Istio), and protecting sensitive secrets at rest.

---

### 1. [[Main Notes/Kubernetes Pod Security and Policy Engines|Kubernetes Pod Security and Policy Engines]] *(Landing Note)*
* **Role:** Architectural hub for workload admission policies and policy engines.
* **What's Inside:**
  - The evolution of pod policy engines: Deprecation of PodSecurityPolicy (PSP) in Kubernetes 1.25 -> Built-in Pod Security Admission (PSA) -> External webhook engines (OPA Gatekeeper, Kyverno).
  - When to use built-in PSA vs. complex external policy engines.

---

### 2. [[Main Notes/Kubernetes Pod Security and Policy Engines - Evolution from PSP to PSA, Gatekeeper, and Kyverno|Kubernetes Pod Security: Evolution from PSP to PSA, Gatekeeper & Kyverno]] *(Deeper Dive)*
* **Role:** Comparative technical deep dive into policy architecture and admission mechanics.
* **What's Inside:**
  - Why PSP was removed: Unintuitive mutation ordering, binding complexities via RBAC RoleBindings, and cluster instability.
  - How PSA replaced PSP: Native, non-mutating admission controller built directly into kube-apiserver without external controller dependencies.
  - OPA Gatekeeper vs. Kyverno: Rego language compilation vs. native Kubernetes YAML validation/mutation policies.

---

### 3. [[Main Notes/Kubernetes Pod Security Admission - Tri-Mode Enforcement, Tiers, and Namespace Labels|Kubernetes Pod Security Admission: Tri-Mode Enforcement, Tiers & Namespace Labels]] *(Deeper Dive)*
* **Role:** Labeling namespaces, the 3 security tiers, and the 3 enforcement modes.
* **What's Inside:**
  - The 3 Security Standards Tiers:
    1. **Privileged:** Unrestricted. Allows root, hostPath, hostNetwork, capabilities.
    2. **Baseline:** Minimally restrictive. Blocks known privilege escalations; default for unprivileged workloads.
    3. **Restricted:** Hardened. Mandates non-root, drop all capabilities, read-only root filesystems, seccomp `RuntimeDefault`.
  - The 3 Enforcement Modes: `enforce` (blocks admission), `audit` (records violation in audit log), `warn` (returns human warning in CLI).
  - Namespace Label Syntax:
    `pod-security.kubernetes.io/enforce: restricted`
    `pod-security.kubernetes.io/enforce-version: latest`

---

### 4. [[Main Notes/Kubernetes Pod Security Admission - Restricted Standards, Pod Creation Control Flow, and ReplicaSet Debugging|Kubernetes Pod Security Admission: Restricted Standards, Control Flow & ReplicaSet Debugging]] *(Deeper Dive)*
* **Role:** Step-by-step resolution of PSA Restricted violations and the silent ReplicaSet admission trap.
* **What's Inside:**
  - **The 5-Field Mandate for PSA Restricted:**
    1. `runAsNonRoot: true`
    2. `allowPrivilegeEscalation: false`
    3. `capabilities.drop: ["ALL"]`
    4. `seccompProfile.type: RuntimeDefault`
    5. No host namespaces (`hostNetwork`, `hostPID`, `hostIPC: false`).
  - **The "Silent ReplicaSet" Admission Trap:**
    - You deploy a Deployment to a restricted namespace.
    - `kubectl get pods` is **empty**! (No error is printed on screen).
    - **Why?** Deployments create ReplicaSets. The ReplicaSet controller attempts to create pods. The PSA admission plugin rejects the pod creation request from the ReplicaSet!
    - **How to debug:** `kubectl describe rs <replicaset-name>` reveals the exact PSA policy violation events (`FailedCreate`).
* **Key Pitfalls Addressed:** Missing the `allowPrivilegeEscalation: false` field; relying solely on `kubectl get pods` when debugging failed deployments.
* **Exam Scenario Alignment:** **Question 12 (`q12-restricted-pss`)** — Enforcing PSA Restricted on production namespaces and debugging blocked pods.

---

### 5. [[Main Notes/Kubernetes ServiceAccounts and Workload Identity|Kubernetes ServiceAccounts and Workload Identity]] *(Landing Note)*
* **Role:** Architectural hub for workload identity and API credentials.
* **What's Inside:**
  - What ServiceAccounts are: Workload identities representing pods interacting with the API server.
  - The Legacy vs. Modern token paradigm: Legacy static secret-based tokens (eternal, non-expiring, cluster-wide) vs. Modern Bound ServiceAccount Tokens (ephemeral, time-limited, audience-scoped).

---

### 6. [[Main Notes/Kubernetes ServiceAccount Token Projection - Bound Tokens, Volume Projections, and Audience Scoping|Kubernetes ServiceAccount Token Projection: Bound Tokens, Projections & Audience Scoping]] *(Deeper Dive)*
* **Role:** Securing pod identity tokens, volume projection, and token theft defense.
* **What's Inside:**
  - The Bound ServiceAccount Token Volume feature:
    - Time-bound: Tokens automatically expire (e.g. `expirationSeconds: 3600`).
    - Workload-bound: Token is cryptographically tied to the lifetime of the specific pod; if the pod is deleted, the token is instantly invalid.
    - Audience-bound: Token is only valid for specified audiences (`audiences: ["vault", "api"]`), preventing token reuse attacks on other services.
  - Projected Volume Syntax in Pod YAML:
    ```yaml
    volumes:
    - name: token-vol
      projected:
        sources:
        - serviceAccountToken:
            audience: api
            expirationSeconds: 3600
            path: token
    ```
  - Disabling automatic token mounting: `automountServiceAccountToken: false` on pods that do not need to speak to the API server.
* **Key Pitfalls Addressed:** Workloads mounting unneeded API credentials exposing the cluster to token theft via SSRF/RCE vulnerabilities.
* **Exam Scenario Alignment:** **Question 09 (`q09-serviceaccount-token`)** — ServiceAccount token volume projection drill.

---

### 7. [[Main Notes/Kubernetes Service Mesh Security - Istio mTLS, PeerAuthentication CRDs, and Sidecar Injection|Kubernetes Service Mesh Security: Istio mTLS, PeerAuthentication CRDs & Sidecar Injection]] *(Deeper Dive)*
* **Role:** Zero-trust service mesh networking, automatic mTLS encryption, and traffic microsegmentation.
* **What's Inside:**
  - How Istio enforces zero-trust: Envoy sidecar proxies deployed alongside application containers intercept all inbound and outbound TCP traffic via iptables.
  - Sidecar Injection: Enabling automatic injection via namespace labeling (`istio-injection: enabled`).
  - **`PeerAuthentication` CRD:**
    - Setting `mtls.mode: STRICT` (rejects plain text; all microservice-to-microservice traffic must be encrypted with mTLS).
    - Setting `mtls.mode: PERMISSIVE` (allows both plain text and mTLS, used during migrations).
  - Rolling restart workflow: `kubectl rollout restart deployment <name>` to inject Envoy sidecars into running pods.
  - Verification: Inspecting pod container count (`2/2` indicating application + `istio-proxy`).
* **Key Pitfalls Addressed:** Setting `STRICT` mode before Envoy sidecars are injected, causing immediate connection dropouts across the namespace.
* **Exam Scenario Alignment:** **Question 14 (`q14-istio-mtls`)** — Enforcing STRICT mTLS across microservices.

---

### 8. [[Main Notes/Kubernetes Secret Encryption at Rest - EncryptionConfiguration, Provider Chains, and etcd Verification|Kubernetes Secret Encryption at Rest: EncryptionConfiguration, Provider Chains & etcd Verification]] *(Deeper Dive)*
* **Role:** Encrypting Kubernetes secrets in the etcd datastore.
* **What's Inside:**
  - The Default etcd Vulnerability: By default, Kubernetes secrets are stored in etcd as plain Base64-encoded strings; anyone with etcd disk access or snapshot access can read all cluster passwords and keys.
  - The `EncryptionConfiguration` Architecture:
    - Provider hierarchy: Evaluated strictly **top-to-bottom** (first provider in the list encrypts new writes; all providers in the list are attempted during reads).
    - Providers: `aescbc`, `secretbox`, `aesgcm`, `kms`, and `identity` (cleartext).
  - Configuring kube-apiserver: Adding `--encryption-provider-config=/etc/kubernetes/enc/enc.yaml` and mounting the file path.
  - **The Re-encryption Step:** Modifying the config does NOT automatically encrypt existing secrets! You must run:
    ```bash
    kubectl get secrets -A -o json | kubectl replace -f -
    ```
  - Verification via `etcdctl`: Dumping raw keys from etcd (`etcdctl get /registry/secrets/...`) and verifying the `k8s:enc:aescbc:v1:` cryptographic header.
* **Key Pitfalls Addressed:** Putting the `identity: {}` provider before `aescbc` (which leaves writes unencrypted); forgetting to re-encrypt existing secrets; breaking API server startup due to wrong provider key Base64 formatting.

---

### 9. [[Main Notes/Kubernetes Sandboxed Runtimes - gVisor, Kata Containers, and the 3-Layer RuntimeClass Chain|Kubernetes Sandboxed Runtimes: gVisor, Kata Containers & The 3-Layer RuntimeClass Chain]] *(Deeper Dive)*
* **Role:** Hardware and user-space kernel virtualization for untrusted workloads.
* **What's Inside:**
  - Why standard runtimes (runc) are vulnerable: Shared host kernel vulnerabilities (kernel exploits like Dirty COW allow immediate node takeover).
  - The two sandboxing paradigms:
    1. **gVisor (`runsc`):** Application-level user-space kernel written in Go (Sentry intercepts syscalls; Gofer handles file I/O).
    2. **Kata Containers:** Lightweight hardware-isolated MicroVMs running individual container pods under QEMU/Cloud-Hypervisor.
  - **The 3-Layer RuntimeClass Integration Chain:**
    1. Node Runtime: Configure containerd runtime handler in `/etc/containerd/config.toml` (`[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runsc]`).
    2. Kubernetes Resource: Create `RuntimeClass` object:
       ```yaml
       apiVersion: node.k8s.io/v1
       kind: RuntimeClass
       metadata:
         name: gvisor
       handler: runsc
       ```
    3. Workload Manifest: Add `runtimeClassName: gvisor` to `spec` of the Pod.
  - Forensics inside the sandbox: Running `dmesg` (gVisor returns fake kernel messages) and `uname -a` (shows gVisor virtualized Linux).
* **Key Pitfalls Addressed:** Typos between the `RuntimeClass.handler` string and the containerd config runtime handler name, resulting in `FailedCreatePodSandBox`.

---

## 📦 MODULE 05: Supply Chain Security, Artifact Integrity & Admission Control (20%)

This module ensures that only minimal, scanned, and cryptographically verified container images enter the cluster, and that dynamic admission webhooks enforce policy at deploy time.

---

### 1. [[Main Notes/Kubernetes Supply Chain Security and Artifact Integrity|Kubernetes Supply Chain Security and Artifact Integrity]] *(Landing Note)*
* **Role:** Architectural hub for container image hardening, SBOM generation, and admission gating.
* **What's Inside:**
  - The Software Supply Chain lifecycle: Developer Workstation -> Git Repository -> CI Build Pipeline -> Container Registry -> Admission Gatekeeper -> Cluster Runtime.
  - Attack vectors: Compromised base images, dependency vulnerabilities, supply chain poisoning, and unvalidated third-party registries.

---

### 2. [[Main Notes/Kubernetes Container Image Hardening - Dockerfile Best Practices, Distroless Images, and the nobody User|Kubernetes Container Image Hardening: Dockerfile Best Practices, Distroless Images & the nobody User]] *(Deeper Dive)*
* **Role:** Secure container image compilation, multi-stage builds, and user ID assignments.
* **What's Inside:**
  - Multi-stage builds: Compiling code in heavy build stages and copying only the final binary into a minimal scratch/distroless production image (removes compilers, package managers, and shells).
  - Distroless benefits: Eliminates `/bin/sh`, `curl`, `wget`, depriving attackers of basic reconnaissance tools.
  - **The `nobody` User (`UID 65534`):**
    - Why numeric UIDs matter: Declaring `USER 65534` instead of `USER nobody` prevents ambiguity across different Linux distros.
  - **Runtime Override Precedence:** Kubernetes `securityContext.runAsUser` **overrides** Dockerfile `USER` instructions at runtime.
* **Key Pitfalls Addressed:** Installing debug tools in production images; running processes as default `root` (UID 0); hardcoding sensitive credentials in Dockerfile `ENV` directives.
* **Exam Scenario Alignment:** **Question 03 (`q03-dockerfile-security`)** — Dockerfile hardening and the `nobody` user.

---

### 3. [[Main Notes/Kubernetes Software Bill of Materials - bom Tool, Vulnerability Hunting, and Cosign Attachments|Kubernetes Software Bill of Materials: bom Tool, Vulnerability Hunting & Cosign]] *(Deeper Dive)*
* **Role:** Generating SPDX SBOMs, hunting package vulnerabilities, and signing container artifacts.
* **What's Inside:**
  - What an SBOM is: A complete cryptographic inventory of all libraries, dependencies, and OS packages included inside an image.
  - **The Kubernetes `bom` CLI tool:**
    - Generating an SPDX format SBOM for an image:
      ```bash
      bom generate --image <image-tag> -o <output.spdx>
      ```
    - Analyzing files and directories.
  - Vulnerability hunting in the exam: Querying in-container package managers (`apk list`, `dpkg -l`, `rpm -qa`) to identify vulnerable libraries (e.g. vulnerable `libcrypto` or `openssl`), eliminating the vulnerable container from the Deployment, and generating the SPDX SBOM specifically for the **compromised/bad image** for forensic analysis and compliance archiving.
  - Production verification: Scanning SBOMs via Trivy (`trivy sbom <file>`) and signing/attaching SBOMs to OCI registries using Sigstore `cosign`.
* **Exam Scenario Alignment:** **Question 11 (`q11-sbom-bom-tool`)** — Hunting compromised packages, evicting rogue containers, and generating SPDX SBOMs for the bad image using `bom`.

---

### 4. [[Main Notes/Kubernetes Admission Control - Request Lifecycle, Mutating and Validating Architecture|Kubernetes Admission Control: Request Lifecycle, Mutating & Validating Architecture]] *(Deeper Dive)*
* **Role:** The mechanics of the API Server admission phase.
* **What's Inside:**
  - The two-phase Admission Controller pipeline:
    1. **Mutating Admission Webhooks:** Can modify the incoming object (e.g. inject sidecars, set default securityContexts). Evaluated in series.
    2. **Validating Admission Webhooks:** Can only approve or reject the request (e.g. block images with `latest` tag, enforce required labels). Evaluated in parallel.
  - Why Mutating runs before Validating: Validating webhooks must inspect the *final* object after all mutations have completed.

---

### 5. [[Main Notes/Kubernetes Admission Control - Webhook Deadlocks, CNI Collapse, and Namespace Blacklisting|Kubernetes Admission Control: Webhook Deadlocks, CNI Collapse & Namespace Blacklisting]] *(Deeper Dive)*
* **Role:** Failure modes, operational disasters, and webhook deadlocks.
* **What's Inside:**
  - **The Webhook Deadlock Disaster:** What happens when an admission webhook controller pod crashes?
    - If `failurePolicy: Fail` is set, the API server rejects ALL pod creation requests—including the pods needed to bring the webhook controller itself back online!
  - **The CNI Collapse:** A webhook configured without namespace exclusions blocks core networking pods in `kube-system`, causing the entire cluster network to collapse.
  - The Solution: Namespace whitelisting via `namespaceSelector` (always exempt `kube-system`), and using `failurePolicy: Ignore` during bootstrapping.

---

### 6. [[Main Notes/Kubernetes Admission Control - ImagePolicyWebhook, Kubeconfig Bundles, and Scanner Backends|Kubernetes Admission Control: ImagePolicyWebhook, Kubeconfig Bundles & Scanner Backends]] *(Deeper Dive)*
* **Role:** External image scanner integration and admission bundle configuration.
* **What's Inside:**
  - What `ImagePolicyWebhook` is: A specialized built-in admission controller plugin that intercepts every container image deployment and queries an external scanner oracle before the pod is allowed to run.
  - The Kubeconfig bundle: How the API Server authenticates to the external webhook endpoint via client certificates.

---

### 7. [[Main Notes/Kubernetes Dynamic Admission Control - ImagePolicyWebhook, Decision Caching, and Fail-Closed Enforcement|Kubernetes Dynamic Admission Control: ImagePolicyWebhook, Decision Caching & Fail-Closed Enforcement]] *(Deeper Dive)*
* **Role:** Step-by-step configuration, caching TTLs, and fail-closed security posture.
* **What's Inside:**
  - The Admission Configuration file (`/etc/kubernetes/admission/admission-config.yaml`):
    - `imagePolicy.kubeConfigFile: /etc/kubernetes/admission/kubeconfig.yaml`
    - Decision Caching: `allowTTL: 50` (caches positive scanner decisions for 50s to avoid API latency), `denyTTL: 50` (caches rejected images).
    - Retry backoff: `retryBackoff: 500`.
    - **Fail-Closed Security Posture:** `defaultAllow: false` (if the external scanner backend is unreachable or times out, the deployment MUST be rejected!).
  - Kube-apiserver flags required:
    - `--enable-admission-plugins=...,ImagePolicyWebhook`
    - `--admission-control-config-file=/etc/kubernetes/admission/admission-config.yaml`
    - Necessary hostPath volume mounts for the admission configuration directory.
* **Key Pitfalls Addressed:** Setting `defaultAllow: true` (which fails-open and lets unscanned malware run if the scanner is down); missing volume mounts causing kube-apiserver boot crashes.
* **Exam Scenario Alignment:** **Question 15 (`q15-image-policy-webhook`)** — Enabling ImagePolicyWebhook with fail-closed security.

---

## 🦅 MODULE 06: Monitoring, Logging, Runtime Security & Threat Forensics (15-20%)

This module focuses on detecting live threats, identifying memory tampering attacks, and executing rapid incident response in running clusters.

---

### 1. [[Main Notes/Kubernetes Runtime Security and Threat Forensics|Kubernetes Runtime Security and Threat Forensics]] *(Landing Note)*
* **Role:** Architectural hub for runtime intrusion detection, system call monitoring, and security telemetry.
* **What's Inside:**
  - Why static scanning is not enough: Zero-day exploits, stolen credentials, and compromised dependencies only manifest malicious activity at runtime.
  - The runtime monitoring hierarchy: Host logs (`journalctl`), Kubernetes audit logs, and kernel eBPF tracepoint instrumentation (Falco).

---

### 2. [[Main Notes/Kubernetes Runtime Threat Detection - Falco eBPF Mechanics, dev mem Memory Scraping, and Rogue Pod Remediation|Kubernetes Runtime Threat Detection: Falco eBPF Mechanics, dev mem Scraping & Rogue Pod Remediation]] *(Deeper Dive)*
* **Role:** Falco architecture, rule syntax, `/dev/mem` threat forensics, and incident remediation.
* **What's Inside:**
  - **Falco Architecture:** How Falco hooks into the Linux kernel via eBPF probes or kernel modules to evaluate every system call in real time against declarative rule sets.
  - **The `/dev/mem` Threat Vector:** `/dev/mem` is a character device file providing direct physical memory access; attackers accessing `/dev/mem` can scrape raw RAM to extract unencrypted TLS private keys, Kubernetes tokens, and kernel data structures.
  - Writing Custom Falco Rules in `/etc/falco/falco_rules.local.yaml`:
    ```yaml
    - rule: Detect /dev/mem Access
      desc: Detect unauthorized access to physical memory device
      condition: container and open_read and fd.name = "/dev/mem"
      output: Unauthorized /dev/mem read (user=%user.name container=%container.name pod=%k8s.pod.name)
      priority: CRITICAL
      tags: [filesystem, security]
    ```
  - **The Macro Dependency Trap:** Validating local rules via `falco -V /etc/falco/falco_rules.yaml -V /etc/falco/falco_rules.local.yaml` (macros like `container` and `open_read` are defined in the main rules file).
  - Threat Hunting & Incident Remediation: Grepping system logs (`journalctl -u falco | grep -i "dev/mem"`), identifying the rogue pod, tracing its parent Deployment, and instantly neutralizing the threat by scaling the deployment to 0:
    ```bash
    kubectl scale deployment <rogue-deployment> --replicas=0 -n <namespace>
    ```
* **Exam Scenario Alignment:** **Question 04 (`q04-falco-dev-mem`)** — Live Falco threat detection and rogue pod remediation.

---

### 3. [[Main Notes/Kubernetes API Server Auditing - Policy Stages, Log Retention, and Volume Mount Isolation|Kubernetes API Server Auditing: Policy Stages, Log Retention & Volume Mount Isolation]] *(Cross-Reference)*
* **Role:** (Documented in detail under Module 02).
* **Runtime Forensics Value:** Serves as the immutable chronological record of all administrative cluster interactions, tracking *who* deleted a deployment, *what* IP called the API server, and *when* unauthorized privilege escalations occurred.
* **Exam Scenario Alignment:** **Question 06 (`q06-audit-logging`)**.




