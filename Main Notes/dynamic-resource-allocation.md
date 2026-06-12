---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: worker-node
domains:
  - "kubernetes"
related_concepts:
  - "[[pod]]"
  - "[[node]]"
against:
  - "[[persistentvolume]]"
reference_guides:
  - "[[Reference Notes/0-7_security_and_network_policies.md]]"
tags:
  - kubernetes/resource
  - status/completed
---

# Dynamic Resource Allocation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > infra > **Dynamic Resource Allocation**

---

## 🎯 Purpose (Why it is used)
**Dynamic Resource Allocation (DRA)** (Beta in v1.36) is a resource scheduling framework that handles device allocation (e.g. GPUs, FPGAs, ASICs) with standard APIs. It decouples hardware class definitions from core Kubernetes schedulers, enabling third-party drivers to request and provision specialized hardware dynamically.

---

## ⚙️ Functionality (What it is doing)
*   **Declarative Claims:** Employs `ResourceClaim` objects to request specialized devices on behalf of Pods.
*   **Custom Classing:** Employs `DeviceClass` to categorize hardware pools.
*   **Driver Coordination:** Communicates with host-level DRA drivers to provision and initialize device interfaces before container execution.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Control Plane Schedulers:** Coordinates with `kube-scheduler` during placement to match `ResourceClaims` with nodes that have available classes.
*   **Host Drivers:** Runs as daemonset plugins on worker nodes, implementing least-privilege status updates via specialized subresources.

---

## 🧩 Problem Solver (What problem it solves)
Legacy device scheduling (like GPU device plugins) operates statically—devices are exposed as integer limits (e.g., `nvidia.com/gpu: 1`), lacking advanced configurations like sharing, parameter passing, or network link bindings. DRA solves this by offering a standardized, claim-based API similar to Persistent Volumes for devices.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Dynamic Hardware Sharing:** Enables multi-container device sharing or fraction-based GPU slicing.
*   **Parameters Support:** Passes driver-specific variables (e.g., driver version, driver profile) directly within the YAML spec.

---

## 🔴 Failure Impact (What will happen without it)
*   **Static Allocations:** Hardware resource management is constrained to rigid integer assignments, causing GPU underutilization.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Dynamic Resource Allocation**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND contains(parent_concept, this.file.link)
SORT file.name ASC
```
