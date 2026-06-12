---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[persistentvolume]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/"
author: "Kubernetes Authors"
course_title: "Kubernetes Storage Concepts"
against: []
tags:
  - kubernetes/storage
  - kubernetes/deep-dive
---

# persistentvolume - Ephemeral and Projected

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[persistentvolume]] > **Ephemeral and Projected**

---

## 📑 Ephemeral and Projected Volumes

Kubernetes manages temporary, pod-bound filesystems using Projected Volumes and inline Ephemeral Volumes (CSI and Generic).

### 1. Projected Volumes
Projected volumes mount multiple existing configurations into a single unified folder. All projected sources are read-only:
*   **Sources:** ConfigMaps, Secrets, Downward API, and ServiceAccount tokens.
*   **Use Case:** Projecting specific keys (e.g. database password from a Secret and application configs from a ConfigMap) to a single folder `/var/run/config` without separate volume mounts.
*   **OIDC Token Projection:** Projecting short-lived, audience-bound `serviceAccountToken` credentials directly to the container.

### 2. CSI Inline Ephemeral Volumes
Allows you to define CSI volumes directly in the Pod specification.
*   **Lifecycle:** The volume is created when the Pod is scheduled and deleted when it terminates.
*   **Use Case:** Local, simple drivers that inject local node configuration or transient secrets directly without PersistentVolume/Claim resources.

### 3. Generic Ephemeral Volumes
Generic ephemeral volumes bring the full feature set of dynamic PVC provisioning (snapshots, limits, resizing) to temporary volumes.
*   **Mechanism:** When a Pod starts, a matching PVC is created automatically by the cluster.
*   **Teardown:** When the Pod terminates, the PVC and the dynamically provisioned PV are automatically deleted.
*   **Manifest Config:** Defined inline in the Pod spec under `spec.volumes[*].ephemeral`.

### 4. Local Ephemeral Storage resource limits
Local ephemeral storage (logs, container layers, and local `emptyDir` mounts) is shared across the host node root disk.
*   **Eviction Thresholds:** If a Pod exceeds its specified `resources.limits.ephemeral-storage`, the Kubelet evicts the Pod to prevent node disk exhaustion.
*   **ResourceQuotas:** Namespace-level storage controls can limit the total ephemeral storage requests/limits.

*Read more in [0-8_storage_mechanics_and_csi.md](../Reference%20Notes/0-8_storage_mechanics_and_csi.md#61-projected-volumes)*
