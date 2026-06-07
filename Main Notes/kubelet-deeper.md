---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kubelet]]"
sub_concepts:
  - "[[Node Bootstrap and TLS Bootstrapping]]"
  - "[[Node Conditions and Hard Eviction Thresholds]]"
  - "[[Kubelet Heartbeats & The Lease API]]"
  - "[[CRI Socket Communication]]"
  - "[[Static Pods]]"
use_cases:
  - "[[Inspecting kubelet systemd service logs]]"
external_links:
  - "[Mumshad CKA Course](https://kodekloud.com)"
  - "[Kubernetes Official Docs](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)"
tags:
  - kubernetes/deep-dive
---

# kubelet deeper

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[kubelet]] > **deeper dive**

---

This note covers the detailed bootstrapping pathway, node conditions, lease metrics, CRI socket integration, and static pod mechanics of the **kubelet**.

---

## 🔑 1. Node Bootstrap & TLS Bootstrapping
When a new worker node joins the cluster, the `kubelet` must authenticate with the API Server:
1. **Initial Authentication:** The kubelet reads a bootstrap token from a bootstrap-kubeconfig file.
2. **CSR Submission:** It submits a Certificate Signing Request (CSR) to the API server requesting client certificates.
3. **Approval & Issuance:** Once the CSR is approved (often automatically by a controller), the API server issues certificates.
4. **Final Kubeconfig:** The kubelet writes these credentials to `/etc/kubernetes/kubelet.conf` and uses them for all future communications.

*Configuration Directory:* Core configurations are loaded from `/var/lib/kubelet/config.yaml`.

---

## 📈 2. Node Conditions & Hard Eviction Thresholds
The `kubelet` continuously monitors host resources and flags the API server with **Node Conditions** if limits are crossed:
* `MemoryPressure`: Host memory is running low.
* `DiskPressure`: Root filesystem or image-registry disk is almost full.
* `PIDPressure`: Too many active processes are running on the host (system risk).

### Eviction Thresholds
If resources fall below hard thresholds, the kubelet initiates evictions immediately, without a grace period, to prevent kernel panics:
* `memory.available < 100Mi`
* `nodefs.available < 10%`
* `imagefs.available < 15%`

---

## 💓 3. The Lease API & Heartbeats
In older Kubernetes versions, the kubelet updated its full Node status object every 10 seconds. This generated heavy write traffic in `etcd`, especially in large clusters.
* **Modern Solution:** The Kubelet updates a lightweight `Lease` object in the `kube-node-lease` namespace every 10 seconds.
* **Optimization:** The heavy Node status object is only updated when there is a significant change in conditions, or every 5 minutes by default, reducing database write loads by up to 90%.

---

## 🔌 4. CRI Socket Communication
The Kubelet interacts with the local container runtime over a Unix domain socket using gRPC services:
* **Default sockets:**
  * Containerd: `unix:///run/containerd/containerd.sock`
  * CRI-O: `unix:///var/run/crio/crio.sock`
  * cri-dockerd: `unix:///var/run/cri-dockerd.sock`
* Configure this via the `--container-runtime-endpoint` flag.

---

## 📁 5. Static Pods
Static Pods are managed directly by the Kubelet without scheduler involvement:
* **Configuration:** Place a YAML manifest in `/etc/kubernetes/manifests/` (defined by the `staticPodPath` variable in the kubelet config).
* **Execution:** The Kubelet reads the directory, creates the pod on the local node, and reports its status back to the API Server.
* **Mirror Pods:** The API Server creates a read-only "Mirror Pod" so administrators can see the static pod using `kubectl get pods`, but attempting to delete it via `kubectl` will not stop it (it must be deleted by removing the YAML file from the node's disk).

*Read more in [02_cluster_architecture_and_components.md](../Reference%20Notes/02_cluster_architecture_and_components.md#21-component-configuration-paths-quick-reference) and [03_node_mechanics_and_resource_limits.md](../Reference%20Notes/03_node_mechanics_and_resource_limits.md#3-node-heartbeats-the-lease-api).*
