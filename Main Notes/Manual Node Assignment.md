---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-scheduler-deeper]]"
sub_type: use-case
source_type: udemy
author: "Mumshad Mannambeth"
course_title: "Certified Kubernetes Administrator (CKA)"
against: []
tags:
  - kubernetes/kube-scheduler
  - kubernetes/troubleshooting
---

# kube-scheduler - Manual Node Assignment

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kube-scheduler]] > [[kube-scheduler-deeper]] > **Manual Node Assignment**

---

## 📑 1. Purpose of Manual Binding
If the `kube-scheduler` is down or completely broken, newly created Pods will remain in a `Pending` state. To troubleshoot or schedule critical pods, an administrator can manually assign a Pod to a specific node.

---

## ⚙️ 2. Step-by-Step Manual Binding via API
Since `spec.nodeName` cannot be modified on an *already created* running or pending Pod directly via `kubectl edit`, you must submit a **Binding** API resource to the API server.

### Step 1: Define the Binding JSON Object
Create a file named `binding.json`:
```json
{
  "apiVersion": "v1",
  "kind": "Binding",
  "metadata": {
    "name": "my-pending-pod"
  },
  "target": {
    "apiVersion": "v1",
    "kind": "Node",
    "name": "worker-node-1"
  }
}
```

### Step 2: Post the Binding to the API Server
Submit the binding directly to the Pod's binding sub-resource endpoint using `kubectl replace --raw`:
```bash
kubectl replace --raw "/api/v1/namespaces/default/pods/my-pending-pod/binding" -f binding.json
```
Alternatively, if `kubectl` is unavailable, use `curl`:
```bash
curl -X POST -H "Content-Type: application/json"   --data @binding.json   http://localhost:8001/api/v1/namespaces/default/pods/my-pending-pod/binding
```

---

## ⚠️ 3. Key CKA Considerations
* **Pre-existing Pods:** You can only assign a pod manually if its `spec.nodeName` is blank. If it is already bound, you must delete and recreate the pod.
* **Permissions:** Executing a binding requires RBAC permissions for the `pods/binding` sub-resource.

*Read more in [[Reference Notes/0-13_scheduling_logging_and_lifecycle.md#2-manual-node-binding-bypass-mechanisms]]*\n