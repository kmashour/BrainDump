---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - "kubernetes"
  - "storage"
  - "networking"
concepts_referenced:
  - "[[kubernetes]]"
  - "[[storageclass]]"
  - "[[persistentvolume]]"
  - "[[persistentvolumeclaim]]"
difficulty: intermediate
status: completed
---

# Chapter 4: Enterprise Containerization & Kubernetes Orchestration

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 4: Containerization & Kubernetes**

---

## 🏛️ 1. Container Primitives: Docker Namespace & Cgroups isolation

When presenting your Docker experience, explain the low-level Linux kernel boundaries:

1.  **Namespaces (Isolation):** Virtualizes system resources. Enforces isolation using:
    *   `PID`: Separate process trees.
    *   `NET`: Custom routing tables, interfaces, and `veth` bridge endpoints.
    *   `MNT`: Custom root filesystems mounted via `pivot_root`.
    *   `USER`: Maps container root (UID 0) to non-privileged host UIDs.
2.  **Cgroups (Resource Limits):** Sets limits on CPU execution windows (CFS quota) and physical memory. Mismatched host cgroup drivers (using `cgroupfs` instead of `systemd` on systemd hosts) cause container eviction and node instability.
3.  **Overlay2 copy-on-write (CoW):** Filesystem storage driver. Modifying files in the read-only lower layers copies them to the mutable upper container layer, creating write latency. Bypass this latency for active I/O using volume mounts.
4.  **Multi-stage builds & Hardened Bases:** Use stages to drop compilation tools from final release images. Run as a non-root system user (`USER appuser`) and set `readOnlyRootFilesystem: true` in the pod spec to stop write access to the host.

---

## ☸️ 2. Kubernetes Cluster Components & API Mechanics

Explain how the Kubernetes control plane coordinates state:

*   **`kube-apiserver`:** The stateless gateway of the cluster. Every query, state change, and client command passes through the API server, which validates requests and writes them to etcd.
*   **`etcd`:** The distributed, transactional key-value store acting as the cluster's single source of truth. Enforces consistency via the Raft consensus algorithm.
*   **`kube-scheduler`:** Watches for newly created Pods with no assigned node. Filters nodes based on scheduling predicates (resource availability, selectors, taints) and scores them to pick the best host.
*   **`kube-controller-manager`:** A collection of control loops (Node Controller, ReplicaSet Controller) that continuously query the API server to reconcile the actual cluster state with the declared state.
*   **`kubelet`:** The worker node agent. It watches the API server for Pod assignments, communicates with local runtimes (containerd/Docker) via the **CRI (Container Runtime Interface)** to build containers, and exposes node health.

---

## 🕸️ 3. EKS Networking, CoreDNS, and Service Discoveries

### A. CoreDNS Internal Naming Hierarchy
Kubernetes services receive stable internal DNS FQDNs resolved by CoreDNS:
*   **ClusterIP Service:** Resolves to a virtual IP load-balanced across pods:
    `service-name.namespace-name.svc.cluster.local`
*   **Headless Service (`clusterIP: None`):** Exposes no virtual IP. Querying the DNS record returns the raw IPs of all matching backend pods, allowing direct peer-to-peer clustering (e.g. database replicas):
    `db-pod-0.db-service.default.svc.cluster.local`

### B. Networking Plugins (CNI Overlay)
The **Container Network Interface (CNI)** allocates IPs to pods.
*   **Overlay Networks (Flannel, Calico VXLAN):** Encapsulate pod network packets inside standard host IP packets, creating a virtual layer-3 network.
*   **AWS VPC CNI:** Bypasses encapsulation. Allocates native private IPs from the host's VPC subnet directly to Pods using elastic network interfaces (ENIs), achieving near-zero networking latency.

---

## 💾 4. Kubernetes Storage & The Scheduling Deadlock Trap

This is a critical area based on your recent local storage updates:

### A. StorageClass Binding Modes
*   **`Immediate`:** Binds the PVC to a PV (or provisions a new disk) instantly.
*   **`WaitForFirstConsumer`:** Delays binding until the Pod using the PVC is scheduled.
*   **The Trap:** If a local volume uses `Immediate` binding, it binds to a PV on `Node A` immediately. If the Pod is later scheduled but is forced to `Node B` (due to cpu limits or selectors), the Pod hangs in `Pending` with `volume node affinity conflict`. **For local storage, always use `WaitForFirstConsumer`.**

### B. Node Affinity on PVs
Static local PVs require an explicit `nodeAffinity` block locking them to a specific node, and the StorageClass must use `kubernetes.io/no-provisioner` to tell Kubernetes that a human is responsible for mounting the physical drive.

---

## 🛡️ 5. Pod Security Admission (PSA) & Hardening

*   **PSA Standards:** Built-in admission controllers enforcing security profiles:
    *   *Privileged:* No restrictions.
    *   *Baseline:* Prevents known privilege escalations (default host namespace block).
    *   *Restricted:* Enforces strict security best practices (forces non-root user, blocks privilege escalation, blocks raw hostPath volumes).
*   **Pod SecurityContext Hardening:**
    ```yaml
    securityContext:
      runAsNonRoot: true
      runAsUser: 10001
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
    ```

*See details in [[Reference Notes/0-8-a_local_storage_models_and_scheduling_traps]], [[Reference Notes/0-3_node_mechanics_and_resource_limits]], and [[Reference Notes/0-7_security_and_network_policies]].*
