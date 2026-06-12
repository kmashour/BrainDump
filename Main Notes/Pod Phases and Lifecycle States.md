---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/"
author: "Kubernetes Documentation"
tags:
  - kubernetes/pod
  - kubernetes/deep-dive
---

# pod - Pod Phases and Lifecycle States

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[pod]] > [[pod-deeper]] > **Pod Phases and Lifecycle**

---

## 📑 1. Pod Lifecycle Phases
A Pod's lifecycle is tracked via `status.phase`. This high-level summary represents where the Pod is in its execution:

| Phase | Description |
| :--- | :--- |
| **`Pending`** | The Pod has been accepted by the API server, but one or more containers have not been created yet (e.g. scheduling or downloading images). |
| **`Running`** | The Pod has been bound to a node, and all containers have been created. At least one container is currently running or starting. |
| **`Succeeded`** | All containers in the Pod have terminated successfully (exit code 0) and will not be restarted (e.g. completed Jobs). |
| **`Failed`** | All containers in the Pod have terminated, and at least one container has terminated in failure (non-zero exit code). |
| **`Unknown`** | The state of the Pod cannot be obtained, typically due to communication failure between the control plane and the node Kubelet. |

---

## ⚙️ 2. Pod Conditions
Under `status.conditions`, the API server reports detailed boolean statuses:
* **`PodScheduled`:** `True` if the Pod has been assigned to a node.
* **`Initialized`:** `True` if all init containers have completed successfully.
* **`ContainersReady`:** `True` if all containers in the Pod are ready.
* **`Ready`:** `True` if the Pod is ready to serve requests and should be added to the service endpoint load balancer list.

---

## 🔬 3. Container Restart Policies
Set via `spec.restartPolicy`:
* **`Always` (Default):** Restarts container upon any exit (normal or error). Recommended for Deployments and DaemonSets.
* **`OnFailure`:** Restarts container only if it exits with a non-zero code. Recommended for Jobs.
* **`Never`:** Never restarts terminated containers.

*Read more in [[Reference Notes/0-4_workload_lifecycle_and_healing.md#1-pod-lifecycle-states-and-conditions]]*\n