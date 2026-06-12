---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[node]]"
sub_type: use-case
source_type: documentation
source_url: "https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/"
author: "Kubernetes Documentation"
tags:
  - kubernetes/node
  - kubernetes/administration
---

# node - Configuring kube-reserved and system-reserved limits

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[node]] > **Configuring Reserved Limits**

---

## 📑 1. Purpose of Reserved Limits
By default, the Kubelet assumes all capacity (except hard eviction thresholds) can be consumed by Pods. If OS processes (like systemd, sshd) spike, they will starve the Kubelet or runtime, causing the node to go `NotReady` or crash. Reserved limits guarantee resources for system processes.

---

## ⚙️ 2. Configuration Steps in Kubelet
Open `/var/lib/kubelet/config.yaml` on the worker node and add the reservation blocks:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
# 1. Enforce limits on system and kube daemons
enforceNodeAllocatable:
- pods
- system-reserved
- kube-reserved
# 2. Set Kube-Reserved memory and CPU
kubeReserved:
  cpu: "250m"
  memory: "500Mi"
# 3. Set System-Reserved memory and CPU
systemReserved:
  cpu: "250m"
  memory: "250Mi"
```

After modifying the file, restart the Kubelet:
```bash
sudo systemctl restart kubelet
```

---

## 🔬 3. Verifying Allocatable Resources
Once Kubelet restarts, verify the changes on the node object using:
```bash
kubectl get node <node-name> -o yaml | grep -A 8 allocatable
```
Look for decreased `allocatable` values compared to the total hardware `capacity`.

*Read more in [[Reference Notes/0-3_node_mechanics_and_resource_limits.md#3-resource-allocation-math-and-limits]]*\n