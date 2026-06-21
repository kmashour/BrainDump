---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Vertical Pod Autoscaler]]"
sub_type: core-concept
source_type: udemy
source_url: "https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/"
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
tags:
  - kubernetes/vpa
  - kubernetes/pod-resizing
  - status/completed
---

# Vertical Pod Autoscaler - In-Place Resizing

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Vertical Pod Autoscaler]] > **In-Place Resizing**

---

## 📑 In-Place Pod Vertical Scaling

By default, modifying container resource requests or limits in an active Pod spec (typically done by changing the Deployment configuration) is disruptive. The control plane destroys the existing Pod and recreates it with the new specifications. To avoid this disruption, Kubernetes introduces **In-Place Pod Vertical Scaling**, allowing dynamic resource scaling of running container boundaries without restarting the Pod.

### ⚙️ Feature Configuration
*   **Feature Gate:** Controlled by the `InPlacePodVerticalScaling` gate. It was introduced as Alpha in v1.27 and promoted to Beta in v1.33+ (enabled by default in newer versions).
*   **Resize Policy (`spec.containers[*].resizePolicy`):** Defines how the container runtime reacts to changes in CPU and memory individually:
    *   `RestartNotRequired` (Default for CPU): The container runtime dynamically adjusts resource allocations (e.g. updating CPU cgroups) on the fly without stopping the container.
    *   `Restart` (Default for Memory): The container runtime restarts the container process to safely apply the new resource parameters.

---

## 🏛️ How It Works Under the Hood

1.  **API Mutation:** The administrator or autoscaling controller patches the Pod's container resources (requests/limits).
2.  **Kubelet Reconciliation:** Kubelet monitors the change, compares it to node capacity, and updates the local container runtime (e.g., `containerd`) settings.
3.  **Container Allocation Status:** The Pod status updates its `.status.containerStatuses[*].resourcesAllocated` field to match the new desired resources.
4.  **Actual Status Update:** Once the container runtime successfully applies the CPU cgroups or memory limits, `.status.containerStatuses[*].resources` is updated to reflect the runtime configuration.

---

## 🔴 Critical Resizing Limitations

*   **Resource Scope:** Scaling is strictly limited to CPU and memory; other resource types cannot be changed dynamically.
*   **QoS Class Immutability:** Changing requests or limits must not alter the Pod's Quality of Service (QoS) class (e.g. you cannot dynamically change a Pod from `Guaranteed` to `Burstable`).
*   **Container Exclusion:** Init containers and ephemeral containers are completely excluded and cannot be resized using this method.
*   **Initial Setup Constraints:** Resources must be declared at Pod creation time; you cannot dynamically add requests/limits to containers that did not define them initially.
*   **Memory Floor Constraints:** You cannot reduce a container's memory limit below its active physical usage. Doing so places the Pod in a `Proposed` state, and the resize status remains `InProgress` until memory usage drops or the limit is raised.
*   **OS Support:** Dynamic scaling is restricted to Linux container environments; Windows pods are not supported.

*Read more in the reference guide: [[Reference Notes/0-6_kubernetes_workloads_and_controllers.md#4-in-place-pod-vertical-scaling-manual-in-place-resizing|0-6_kubernetes_workloads_and_controllers.md > In-Place Pod Vertical Scaling]].*
