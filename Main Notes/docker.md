---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: infra
domains:
  - "docker"
  - "linux"
related_concepts:
  - "[[podman]]"
  - "[[containerd]]"
against:
  - "[[virtual-machine]]"
reference_guides:
  - "[[Reference Notes/2-Index - Docker.md]]"
tags:
  - docker/component
  - status/completed
---

# docker

**Breadcrumbs:** [[0-Index|🏠 Index]] > Infrastructure > **docker**

---

## 🎯 Purpose (Why it is used)
Docker is used to develop, ship, and run applications inside isolated user-space processes called containers. It solves the "works on my machine" problem by bundling the application process, binaries, system tools, and configurations into a single, standardized, deployable package.

---

## ⚙️ Functionality (What it is doing)
*   **Virtualizes OS Process Space:** Configures isolated file mounts, process IDs, network interfaces, and host shares using Linux Kernel namespace isolation.
*   **Manages Resource Allocation:** Enforces CPU and Memory allocation limits per container using Linux Kernel cgroups.
*   **Image Management:** Assembles read-only multi-layered images from Dockerfiles and publishes them to central registries.
*   **Storage & Network Configuration:** Manages data persistence through host volumes and routes traffic via bridged virtual interfaces.

---

## 🏛️ Architectural Context (How it fits in the architecture)
Docker acts as the execution layer on top of the host operating system kernel. In single-host environments, it provides complete service packaging. In clustered environments, it historically served as the container runtime, though modern production Kubernetes clusters bypass Docker daemon overhead in favor of direct **containerd** or **CRI-O** CRI interfaces.

---

## 🧩 Problem Solver (What problem it solves)
Without Docker, deploying software across diverse environments (development, staging, production) leads to dependency drift, library version mismatches, and file access conflicts. Docker guarantees environment consistency—the container behaves identically regardless of the host OS kernel version or host software updates.

---

## 🟢 Operational Impact (What will happen with it operating)
Applications run isolated, boot up in milliseconds, and consume minimal host resources (no guest OS overhead). Developers can run hundreds of containers concurrently on a single physical VM, maximizing resource utilization.

---

## 🔴 Failure Impact (What will happen without it)
If the Docker daemon (`dockerd`) crashes, all managed containers immediately stop executing, leading to application downtime. Physical host resource exhaustion can trigger Linux Kernel Out-Of-Memory (OOM) kills of critical daemon processes, taking down containerized infrastructure.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with **docker**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", source_type AS "Source"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[docker]]
SORT file.name ASC
```
