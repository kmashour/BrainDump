---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: worker-node
domains:
  - "kubernetes"
related_concepts:
  - "[[dynamic-resource-allocation]]"
against:
  - "[[dynamic-resource-allocation]]"
reference_guides:
  - "[[Reference Notes/0-15_kubernetes_api_extension_and_operators.md]]"
tags:
  - kubernetes/extending
  - status/completed
---

# Device Plugin

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > infra > **Device Plugin**

---

## 🎯 Purpose (Why it is used)
The **Device Plugin** framework allows third-party vendors to advertise custom host hardware resources (such as GPUs, NICs, InfiniBand adapters) to the Kubelet without modifying core Kubernetes code.

---

## ⚙️ Functionality (What it is doing)
*   **Hardware Advertising:** Registers available local device counts (e.g., `nvidia.com/gpu: 4`) with the node's Kubelet.
*   **Health Tracking:** Continuously monitors hardware status, reporting failed devices to Kubelet.
*   **Device Initialization:** Runs an `Allocate` gRPC function during pod startup to pass driver configurations, environment variables, and mount paths to the container runtime.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Node-Agent Connection:** Communicates with the local `kubelet` process via UNIX domain sockets under `/var/lib/kubelet/device-plugins/`.
*   **Scheduler Bind:** Scheduler evaluates node resource capacity (based on advertised counts) to determine target pod placement.

---

## 🧩 Problem Solver (What problem it solves)
Without Device Plugins, Kubernetes would have no native way to understand or configure specialized host hardware accelerators. Supporting new chips or network cards would require patching the core Kubelet code. Device Plugins solve this by offering a standardized gRPC interface for vendors.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Accelerator Support:** Enables high-performance compute workloads (like AI training, GPU rendering, and SR-IOV network acceleration) to run in standard containers.

---

## 🔴 Failure Impact (What will happen without it)
*   **No Hardware Access:** Pods requiring GPU or accelerated networking fail to run or cannot discover the devices.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Device Plugin**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), "device-plugin")
SORT file.name ASC
```
---
*Read more in [0-15_kubernetes_api_extension_and_operators.md](../Reference%20Notes/0-15_kubernetes_api_extension_and_operators.md#4-device-plugins)*
