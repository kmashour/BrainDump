---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[docker]]"
sub_type: architecture
source_type: book
source_url: "https://nigelpoulton.com/books"
author: "Nigel Poulton"
course_title: "Docker Deep Dive"
against: []
tags:
  - docker/engine
  - docker/namespaces
  - docker/deep-dive
---

# docker - Container Engine Architecture and Namespaces

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[docker]] > **Container Engine Architecture and Namespaces**

---

## 📑 Container Engine Architecture

Modern Docker uses a modular execution stack derived from OCI (Open Container Initiative) standards, replacing the historical monolithic daemon architecture:

*   **`dockerd` (Docker Daemon):** Handles high-level client REST API requests, image management, build cycles, volumes, and networks.
*   **`containerd`:** Manages the container lifecycle (pushes, pulls, lifecycle events, and runtime states). It is a lightweight supervisor daemon that invokes lower-level runtime engines.
*   **`runc`:** The OCI-compliant reference runtime. It interacts directly with the Linux kernel to configure namespaces and cgroups, starts the container process, and exits.
*   **`containerd-shim`:** Acts as the daemon controller for a running container. It handles standard I/O (stdout/stderr) streams and keeps process streams open if `dockerd` restarts, preventing container outages.

---

## 📑 Kernel Isolation Primitives

Containers achieve hardware-like isolation at the OS level using two key Linux kernel primitives:

1.  **Namespaces (Virtualize Resources):** virtualizes system boundaries so a process sees only its slice:
    *   `mnt` (Mount): Isolates file systems.
    *   `pid` (Process ID): Isolates process trees (container process becomes PID 1).
    *   `net` (Network): Isolates routing tables, devices, and ports.
    *   `ipc` (Inter-Process Communication): Isolates shared memory.
    *   `uts` (Hostnames): Isolates hostnames.
    *   `user` (User IDs): Maps privileged container root to non-privileged host users.
2.  **Control Groups - cgroups (Restrict Resources):** Enforces physical limits (CPU time, memory hard-caps, disk/network I/O throttling) to prevent "noisy neighbor" resource exhaustion.

*Read more in [2-1_docker_fundamentals_and_containers.md](../Reference%20Notes/2-1_docker_fundamentals_and_containers.md#1-container-vs-virtual-machine-isolation)*
