---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: worker-node
related_concepts:
  - "[[kube-apiserver]]"
  - "[[container-runtime]]"
  - "[[node]]"
  - "[[pod]]"
reference_guides:
  - "[[Reference Notes/0-3_node_mechanics_and_resource_limits.md]]"
  - "[[Reference Notes/0-10_maintenance_upgrades_and_etcd.md]]"
  - "[[Reference Notes/0-11_troubleshooting_and_diagnostics.md]]"
  - "[[Reference Notes/0-14_cluster_administration_and_observability.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []

---

# kubelet

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Worker Node Mechanics > **kubelet**

---

## 🎯 Purpose (Why it is used)
The `kubelet` is the primary worker node agent. It runs directly on every node in the cluster, acting as the node's "captain." Its primary job is to ensure that the containers described in Kubernetes PodSpecs are successfully running, healthy, and isolated on the host operating system.

---

## ⚙️ Functionality (What it is doing)
1. **Node Registration:** Registers the host node with the Kubernetes cluster upon startup.
2. **Pod Manifest Execution:** Watches the `kube-apiserver` for Pods assigned to its node. It parses their PodSpecs and instructs the Container Runtime (via CRI gRPC) to launch or terminate the containers.
3. **Health Monitoring & Probing:** Executes Liveness, Readiness, and Startup probes defined in the Pod specifications, taking corrective action (restarting failed containers) if a probe fails.
4. **Heartbeat Telemetry:** Periodically updates a `Lease` object in the `kube-node-lease` namespace to notify the control plane that the node is active and healthy.
5. **Node Garbage Collection:** Cleans up terminated containers and deletes unused cached container images when host disk utilization exceeds configured thresholds (e.g., 85%).
6. **Static Pod Execution:** Monitors a local directory (e.g., `/etc/kubernetes/manifests`) for raw YAML files and runs them as Static Pods bypasses the API server scheduler.

---

## 🏛️ Architectural Context (How it fits in the architecture)
The `kubelet` sits on the boundary between the Kubernetes cluster control plane and the node's operating system:
* **Systemd Service:** Unlike other Kubernetes components, the `kubelet` does not run inside a container. It runs as a native systemd daemon directly on the host OS.
* **CRI Coordinator:** It translates Kubernetes-specific Pod configurations into low-level container instructions sent over gRPC to the local Container Runtime (e.g., containerd).

---

## 🧩 Problem Solver (What problem it solves)
* **Local Process Orchestration:** Converts abstract, declarative YAML Pod definitions from the database into actual, isolated OS namespaces and processes.
* **Telemetry Loop Closure:** Without the kubelet, the control plane has no hands on the worker node to spin up containers, pull images, or check local process health.
* **Host Overload Protection:** Constantly monitors host-level resources (disk space, memory, PID limits) and evicts pods before the node suffers a hard crash due to kernel Out-Of-Memory (OOM) situations.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Active Workload Execution:** Pods scheduled to the node are successfully downloaded, created, and executed.
* **Self-Healing Pods:** If a containerized application crashes, it is automatically restarted on the spot.
* **Dynamic Node Health:** The node status remains `Ready` in `kubectl get nodes`, allowing scheduling to continue.

---

## 🔴 Failure Impact (What will happen without it)
* **Node Transitions to `NotReady`:** The node's Lease heartbeat fails to renew. After 40 seconds, the Node Controller marks the node `NotReady`.
* **Pod Eviction & Rescheduling:** After the `pod-eviction-timeout` (default 5 minutes), the Control Plane evicts all pods from the node and schedules replacement replicas on remaining healthy nodes.
* **Orphaned Local Processes:** Currently running containers on the node will continue executing on the host OS but are orphaned. If a container crashes, it will not be restarted.
* **Frozen State:** Any updates (such as image changes, scaling requests, or config modifications) cannot be applied to workloads on that node.
---

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

*Read more in [0-2_cluster_architecture_and_components.md](../Reference%20Notes/0-2_cluster_architecture_and_components.md#21-component-configuration-paths-quick-reference) and [0-3_node_mechanics_and_resource_limits.md](../Reference%20Notes/0-3_node_mechanics_and_resource_limits.md#3-node-heartbeats-the-lease-api).*

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **kubelet**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND icontains(string(parent_concept), this.file.name)
SORT file.name ASC
```
