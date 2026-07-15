---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - "linux"
  - "storage"
concepts_referenced:
  - "[[container-runtime]]"
  - "[[docker]]"
difficulty: intermediate
status: completed
---

# Chapter 1: Secure Containerization with Docker

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 1: Secure Containerization**

---

## 🏛️ 1. OS-Level Virtualization: Namespaces and Cgroups

To explain container isolation in a technical interview, you must articulate the kernel primitives that separate container processes.

### A. Kernel Namespaces (Virtual Views)
Namespaces restrict what a process can *see*. When you execute a container, the runtime executes a clone system call with namespace flags:
*   **PID (Process ID Namespace):** Isolates the process tree. Inside the container, your application process starts as PID 1, allowing it to receive standard OS signals (like `SIGTERM` on shutdown). On the host, the process is visible under its actual host PID, allowing host resource monitoring.
*   **NET (Network Namespace):** Isolates network adapters, routing tables, and port bindings. The runtime creates a virtual ethernet pair (`veth` interface), moving one end into the container's namespace (as `eth0`) and binding the other to the host bridge network adapter (`docker0`).
*   **MNT (Mount Namespace):** Isolates the filesystem mount table. The container has a unique root directory, separated from the host using the `pivot_root` syscall.
*   **IPC (Inter-Process Communication Namespace):** Prevents containers from reading or writing to the host's shared memory segments or message queues.
*   **UTS (Unix Timesharing System Namespace):** Allows the container to define its own hostname, separating it from the host's domain.
*   **USER (User Namespace):** Maps root inside the container (UID 0) to a high-numbered, non-privileged UID on the host (e.g., UID 10001). This limits the blast radius of container escapes.

### B. Control Groups (Cgroups v1 vs v2)
Cgroups restrict what a process can *consume* (CPU, memory, storage I/O, network bandwidth).
*   **CPU Limits:** Enforced via the CFS (Completely Fair Scheduler) quota. Setting a limit of `0.5 CPU` translates to allocating 50ms of CPU execution time out of every 100ms CFS period.
*   **Memory Limits:** Enforced via kernel memory controllers. If a container exceeds its memory limit, the host kernel triggers the Out-Of-Memory (OOM) killer, terminating the container process (`OOMKilled` status).
*   **cgroups v2:** Introduces a unified resource controller hierarchy, resolving resource accounting conflicts present in the multi-branch structure of cgroups v1.

---

## 📂 2. Layered Filesystem (Overlay2 Storage Driver)

Understanding the filesystem layout is critical for explaining build efficiency and container I/O performance.

```
+-------------------------------------------------------------+
|               Container Layer (Read-Write)                 |  <- Modified files, temp logs
+-------------------------------------------------------------+
|                Overlayfs Indirection Layer                  |  <- Merged view presented to process
+-------------------------------------------------------------+
|               Image Layer 3: Application (Read-Only)       |  <- app/main.py
+-------------------------------------------------------------+
|               Image Layer 2: Dependencies (Read-Only)      |  <- python packages
+-------------------------------------------------------------+
|               Image Layer 1: Base Alpine OS (Read-Only)    |  <- python:alpine base
+-------------------------------------------------------------+
```

### A. The Copy-on-Write (CoW) Mechanism
*   **LowerDir:** Immutable read-only layers representing the base image.
*   **UpperDir:** The mutable read-write layer created when the container starts.
*   **MergedDir:** The unified virtual directory presented to the container process.
*   **Write Operations:** If a container modifies an existing file from a lower layer, the `overlay2` driver intercepts the call, copies the file from the read-only LowerDir to the read-write UpperDir, and applies the changes there. This copy-on-write introduces disk write latency.

### B. Volume Mount Primitives
To bypass overlay2 I/O latency, applications write state to volumes.
*   **Bind Mounts:** Maps a specific directory on the host directly into the container namespace (e.g., `/var/log/nginx`). Operates at host disk speeds.
*   **Named Volumes:** Managed by Docker `/var/lib/docker/volumes/`. High performance, abstracted, and portable.
*   **Host Socket Binding (`/var/run/docker.sock`):** Allows containers to control the host Docker daemon. Essential for monitoring (like Prometheus node-exporters) but represents a major container breakout security risk.

---

## 🔒 3. Production-Grade Dockerfile Best Practices

During the interview, present the secure multi-stage Dockerfile from the project and justify each directive:

1.  **Multi-Stage Build Rationale:** 
    *   *Stage 1 (Builder):* Uses a full build image with compilers (`gcc`, `make`, header libraries) to compile dependencies.
    *   *Stage 2 (Runtime):* Uses a minimal, hardened base (`alpine` or `distroless`). Copies *only* the compiled artifacts from the Builder stage. This reduces image size from ~800MB to <100MB and eliminates the compile tools vulnerability footprint.
2.  **Hardened Base Images:** Prefer `alpine` (busybox-based) or `distroless` (contains only the runtime and its dependencies, lacks shells like `/bin/sh` or `/bin/bash` to stop attackers).
3.  **Non-Root User Configuration:**
    *   Containers run as root (UID 0) by default. If an attacker finds a remote code execution vulnerability, they can execute commands as root inside the container, increasing host escape risks.
    *   Define a system user/group with no shell:
        `RUN addgroup -S appgroup && adduser -S appuser -G appgroup`
        `USER appuser`
4.  **Leveraging Build Cache:**
    *   Docker caches layers. Copying `requirements.txt` and running `pip install` *before* copying the application source code ensures that dependencies are cached. Changing application code will not trigger a reinstall, speeding up CI builds.
