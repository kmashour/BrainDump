---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[pod-deeper]]"
sub_type: core-concept
source_type: documentation
source_url: "https://kubernetes.io/docs/concepts/workloads/pods/"
author: "Kubernetes Authors"
course_title: "CKA Exam Prep"
tags:
  - kubernetes/pod
  - troubleshooting/recreation
---

# pod - Spec Immutability and Re-creation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[pod]] > [[pod-deeper]] > **Spec Immutability and Re-creation**

---

## 📑 Pod Spec Immutability

Because Pods represent active running processes mapped to Linux cgroups and namespaces, most of their properties cannot be changed without terminating the container.

### The Exceptions (Mutable Fields)
You can only modify the following fields on a running Pod spec:
1. `spec.containers[*].image`: Swaps out the container image (triggers a container restart).
2. `spec.activeDeadlineSeconds`: Sets a timeout limit.
3. `spec.tolerations`: Allows adding new tolerations (removal/modification of existing ones is blocked).

Attempting to edit other fields (like ports, env variables, or volume mounts) will return a `Forbidden` API error.

---

## 🛠️ The '/tmp/kubectl-edit-xxxx.yaml' Recovery Workflow

When editing a running Pod's immutable fields, the update is rejected, and `kubectl` saves a copy of your edits to a temporary local file: `/tmp/kubectl-edit-xxxx.yaml`.

### The Force-Replace Workflow
To apply the changes, force a replacement using the temporary file. This deletes the old pod and recreates it with the new configuration:

```bash
# Forcefully replace the pod using the temp file
kubectl replace --force -f /tmp/kubectl-edit-xxxx.yaml
```

### 💉 Advanced: Surgical Mutations
* **Strategic Merge Patch:** Use `kubectl patch` to surgically modify only specific mutable fields (like container image tag strings) without sending the entire resource body.
* **API Binding Sub-resource:** If `kube-scheduler` is offline and a Pod is `Pending` (empty `spec.nodeName`), you can surgically bind it by POSTing a `Binding` object directly to `/binding` using `kubectl replace --raw /api/v1/namespaces/default/pods/[pod-name]/binding -f binding.json`. This is only allowed once when `nodeName` is empty.

*Read more in [0-12_kubernetes_api_management_and_pod_immutability.md](../Reference%20Notes/0-12_kubernetes_api_management_and_pod_immutability.md#3-pod-immutability-rules)*
