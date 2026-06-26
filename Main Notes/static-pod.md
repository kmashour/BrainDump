---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubelet-deeper]]"
sub_type: use-case
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/"
author: "Kubernetes Documentation"
aliases: ["Static Pods", "Static Pod"]
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
Check the Kubelet configuration file (typically `/var/lib/kubelet/config.yaml`) for the `staticPodPath` entry:
```yaml
staticPodPath: /etc/kubernetes/manifests
```
Alternatively, search for the configuration flag in the running process:
```bash
ps aux | grep kubelet | grep -E "(--pod-manifest-path|--config)"
```

### Step 2: Create or Modify a Static Pod
Place a pod manifest YAML file in the designated manifest folder:
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
The Kubelet periodically scans this directory and will spin up the Pod automatically. Removing the file deletes the pod.

### Step 3: Check Static Pods when the Control Plane is Offline
If the API Server is down, `kubectl` commands will fail. To verify that static pods are running on the node, inspect the local container runtime directly:
```bash
# Query the container runtime via CRI command line tool
crictl ps | grep static-web
# Or on older systems using docker:
docker ps | grep static-web
```

---

## 🔬 3. Mirror Pods & Naming Convention
To make static pods visible to cluster administrators, the Kubelet creates a read-only **Mirror Pod** in the API Server.
* **Naming Format:** Mirror Pods automatically use the naming convention `<pod-name>-<node-name>` (e.g. `static-web-controlplane` or `etcd-controlplane`).
* **Management:** You cannot modify or delete mirror pods via the API server (`kubectl delete pod` will temporarily delete the representation, but the Kubelet will recreate it immediately). They must be managed by editing or deleting the manifest files directly on the host node.

*Read more in [[Reference Notes/0-13_scheduling_logging_and_lifecycle.md#i-static-pods]]*\n