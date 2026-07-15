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
difficulty: advanced
status: completed
---

# Chapter 4: Enterprise Containerization & Kubernetes Orchestration

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 4: Containerization & Kubernetes**

---

## 🏛️ 1. Container Runtimes & Linux OS Resource Drivers

In a technical interview, you must separate Docker (the developer tool) from the production Kubernetes runtime environment.

### A. The Container Runtime Interface (CRI) Architecture
When scheduling a Pod, the `kubelet` does not interact with Docker directly. It uses gRPC to query the node's CRI:
*   **The CRI Layer (containerd / CRI-O):** Acts as a daemon managing image pull requests, container sandboxes, and lifecycle states.
*   **The OCI Layer (`runc`):** The CRI daemon invokes an Open Container Initiative (OCI) compliant runtime (like `runc`) to execute the container.
*   **The Execution:** `runc` interfaces with the Linux kernel to configure namespaces and cgroups, starts the container application process, and exits. A lightweight **`containerd-shim-v2`** process remains running to collect container exit codes and preserve standard input/output descriptors without keeping the main CRI daemon locked.

### B. The Cgroup Driver Conflict (`systemd` vs. `cgroupfs`)
Linux systems running systemd utilize a unified resource management hierarchy.
*   **`cgroupfs` Driver:** Kubelet directly writes resource allocations to the `/sys/fs/cgroup` directory.
*   **`systemd` Driver:** Kubelet requests cgroup resource updates via the systemd IPC interface.
*   **The Conflict:** If `kubelet` is configured to use `cgroupfs` on a host running systemd, the node has two distinct resource management entities writing to cgroups. During high resource contention, the systemd process manager may terminate `kubelet` processes or evict running Pods due to incorrect resource tracking. **Always align the kubelet cgroup driver to `systemd` in production configurations.**

---

## ⚙️ 2. Kubernetes API Mechanics: The 3-Way Strategic Merge Patch

When you execute `kubectl apply -f manifest.yaml`, the `kube-apiserver` does not simply overwrite the existing object in etcd. It calculates updates using a **3-Way Strategic Merge Patch**:
1.  **Original (Last-Applied Configuration):** Read from the `kubectl.kubernetes.io/last-applied-configuration` annotation stored on the active cluster resource.
2.  **Proposed:** The contents of the local manifest file you are applying.
3.  **Active (Live State):** The current configuration of the resource in etcd (which may contain dynamic values added by control loops, such as `NodePort` numbers, Pod IPs, or replica counts adjusted by an HPA).
*   **The Merge:** The API server compares all three configurations. It preserves dynamic cluster changes (present in Active but absent in Proposed) while applying your configuration changes (present in Proposed but absent in Original). This prevents configuration updates from overwriting live operational state.

---

## 🕸️ 3. Cluster Network Security: Default-Deny NetworkPolicies

By default, all pods in a Kubernetes cluster can communicate freely with each other. To secure microservices, you must implement a Zero-Trust network layout:

*   **The CNI Engine Requirements:** Enforcing network rules requires a CNI plugin that supports policy engines (e.g. **Calico**, **Cilium** using eBPF, or AWS VPC CNI with security groups). Standard plugins like Flannel ignore NetworkPolicy manifests.
*   **Default-Deny Ingress Pattern:** Secure namespaces by blocking all incoming traffic by default, then explicitly whitelist permitted paths:
    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: default-deny-all
      namespace: production
    spec:
      podSelector: {} # Matches all pods in the namespace
      policyTypes:
        - Ingress # Applies block on incoming connections
    ```
*   **Whitelisting Service Paths:** Explicitly permit your Flask backend to receive traffic *only* from the Nginx Ingress controller:
    ```yaml
    spec:
      podSelector:
        matchLabels:
          app: flask-backend
      ingress:
        - from:
            - podSelector:
                matchLabels:
                  app: ingress-nginx
          ports:
            - protocol: TCP
              port: 5000
    ```

---

## 💾 4. Local Storage Scheduling Deadlocks (WaitForFirstConsumer)

For stateful systems running local physical disks (such as high-performance databases), volume binding must be coordinated with node scheduling:

### A. Volume Binding Modes
*   **`Immediate` (Default):** As soon as a user submits a PVC, the control plane binds it to an available local PV (or provisions a new one).
*   **`WaitForFirstConsumer`:** Delays PV binding until a Pod using the PVC is scheduled.

### B. The Node Affinity Deadlock Trap
1.  A local PV is tied to a physical disk on `Node A`.
2.  If the StorageClass is set to `Immediate`, the PVC binds to this PV immediately.
3.  When the Pod is created, the scheduler evaluates node constraints (e.g., `Node A` lacks required memory capacity, or has a Taint, but `Node B` is free).
4.  The scheduler attempts to schedule the Pod on `Node B`.
5.  The Pod fails to start because its bound volume is physically locked to `Node A`. The Pod hangs indefinitely in `Pending` with `volume node affinity conflict`.
*   **Remediation:** Enforce `volumeBindingMode: WaitForFirstConsumer` inside your StorageClass definitions. This forces the scheduler to select a node *first*, and then binds the PVC to a PV on that selected node.

*See details on runtimes in [[Reference Notes/2-1_container_runtime_interfaces_and_cgroups]], storage in [[Reference Notes/0-8-a_local_storage_models_and_scheduling_traps]], and security in [[Reference Notes/0-7_security_and_network_policies]].*
