---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubelet-deeper]]"
sub_type: use-case
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/"
author: "Kubernetes Documentation"
against: []
tags:
  - kubernetes/kubelet
  - kubernetes/static-pods
---

# kubelet - Static Pods

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[kubelet]] > [[kubelet-deeper]] > **Static Pods**

---

## 📑 1. What is a Static Pod?
Static Pods are managed directly by the `kubelet` daemon on a specific node without API server supervision. The Kubelet reads local manifest files from a designated directory and ensures they are running.

* **Control Plane Daemons:** Core control plane components (API Server, Controller Manager, Scheduler, ETCD) are run as static pods.

---

## ⚙️ 2. Step-by-Step Static Pod Troubleshooting (CKA Task)

### Step 1: Find the Static Pod Path
Check the Kubelet configuration file (`/var/lib/kubelet/config.yaml`) for the `staticPodPath` entry:
```yaml
staticPodPath: /etc/kubernetes/manifests
```
Alternatively, search for the flag in running processes:
```bash
ps aux | grep kubelet | grep -i -- --pod-manifest-path
```

### Step 2: Create a Static Pod
Place a pod manifest YAML file in that folder:
```bash
cat <<EOF > /etc/kubernetes/manifests/static-web.yaml
apiVersion: v1
kind: Pod
metadata:
  name: static-web
spec:
  containers:
  - name: web
    image: nginx:alpine
EOF
```
The Kubelet will detect the file and spin up the Pod automatically.

---

## 🔬 3. Mirror Pods
To make static pods visible to administrators, Kubelet creates a read-only **Mirror Pod** in the API Server. You can list them via `kubectl get pods`, but you cannot modify or delete them from the API server. If deleted, Kubelet recreates them immediately.

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#1-node-bootstrapping-and-kubelet-self-registration]]*\n