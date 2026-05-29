# Module 02: Cluster Architecture & Control Plane Components

This module covers the macro and micro architecture of a Kubernetes cluster, diving deep into the roles of control plane and worker components, High Availability (HA) topologies, Cloud integration (CCM), and Version Skew proxying.

---

## 1. Macro View: Control Plane vs. Worker Nodes

A Kubernetes cluster is a distributed system consisting of two primary roles:

### A. The Control Plane (The Brains)
* **Purpose:** Manages the overall cluster state, schedules workloads, makes global decisions (e.g., detecting node failures), and exposes the API.
* **Workload Hosting:** By default, the control plane does not host user applications. In production, control plane nodes are dedicated and isolated.

### B. Worker Nodes (The Muscle)
* **Purpose:** Runs your containerized applications (Pods).
* **Operation:** Receives instructions from the control plane, pulls images, launches containers, and continuously feeds health telemetry back to the API server. For details on node registration, resources, and leases, see [Module 03: Node Mechanics & Resource Limits](03_node_mechanics_and_resource_limits.md). For Pod lifecycle and probing details, see [Module 04: Workload Lifecycle & Self-Healing](04_workload_lifecycle_and_healing.md).

---

## 2. Control Plane Components (Deep Dive)

### A. `kube-apiserver` (The Front Gate)
* Exposes the REST API. Serves as the central point of contact for all components. For a deep dive into API endpoints, OpenAPI schemas, and the event Watch mechanism, see [Module 01: Kubernetes API Mechanics & kubectl CLI](01_kube_api_and_kubectl.md).

### B. `etcd` (The Source of Truth)
* **Mechanism:** A highly available, distributed key-value store.
* **Consensus:** Uses the Raft consensus algorithm.
* **Storage:** Holds the configuration, state, and secrets of the entire cluster.
* **Security:** Only the `kube-apiserver` is authorized to talk directly to `etcd`.
> [!WARNING]
> **CKA Core Topic:** If `etcd` is lost without a backup, the cluster state is unrecoverable. Backing up and restoring `etcd` is a guaranteed exam topic.

### C. `kube-scheduler` (The Matchmaker)
* **Role:** Monitors the API server for newly created Pods that have no assigned Node (`spec.nodeName` is empty).
* **Algorithm:**
  1. **Filtering (Predicates):** Filters out nodes that do not meet resource requirements, taints, ports, or affinity rules.
  2. **Scoring (Priorities):** Scores the remaining nodes (e.g., aiming for resource balance or density).
  3. **Binding:** Writes the chosen node name back to the Pod's `spec.nodeName` field in the API server.

### D. `kube-controller-manager` (The Enforcer)
* **Mechanism:** Runs multiple asynchronous control loops packaged into a single binary.
* **Reconciliation Loop:** Continually compares the Desired State (from `etcd`) with the Actual State (from the nodes).
* **Key Controllers:**
  * **Node Controller:** Detects when nodes go offline (see node heartbeat eviction timers in [Module 03: Node Mechanics & Resource Limits](03_node_mechanics_and_resource_limits.md#3-node-heartbeats-the-lease-api)).
  * **ReplicaSet Controller:** Keeps the correct number of Pod replicas running (see replication control in [Module 04: Workload Lifecycle & Self-Healing](04_workload_lifecycle_and_healing.md#1-the-four-pillars-of-self-healing)).
  * **Endpoints Controller:** Links Service objects to the actual Pod IP addresses.

---

## 3. High Availability (HA) Architecture

Running a single control plane node creates a Single Point of Failure (SPOF). HA clusters replicate the control plane (usually across 3 or 5 nodes) to achieve redundancy.

```plaintext
                    [ Load Balancer ]
                     /      |      \
         [ API-Server ] [ API-Server ] [ API-Server ]   (Active-Active)
               \            |            /
             [ etcd ] <--> [ etcd ] <--> [ etcd ]       (Active-Active Consensus)
               |            |            |
         [ Scheduler ]  [ Scheduler ]  [ Scheduler ]    (Active-Passive Leases)
         (Active/Leader)   (Backup)      (Backup)
```

### A. `kube-apiserver` (Active-Active)
* **Stateless:** Stores no local state.
* **HA Mechanism:** All instances run simultaneously. An external Load Balancer routes traffic to them.

### B. `etcd` (Active-Active / Distributed Consensus)
* **Stateful:** Stores the data.
* **HA Mechanism:** All instances run. They replicate data continuously and elect a leader among themselves using Raft. Requires a quorum (majority) to write: `Quorum = N/2 + 1`.

### C. `kube-scheduler` & `kube-controller-manager` (Active-Passive)
* **Stateful Logic:** Running multiple active schedulers/controllers simultaneously would cause conflicts (e.g., scheduling the same pod to different nodes).
* **HA Mechanism:** Uses **Leader Election** based on `Lease` objects. Only one instance holds the lease and acts as the "Active Leader". The others stand by as "Passive Backups", watching the lease and waiting to take over if the leader fails to renew it.

---

## 4. Cloud Controller Manager (CCM)

Kubernetes splits cloud-specific code out of the core binaries ("out-of-tree" architecture) using the CCM.

* **Purpose:** Decouples Kubernetes from cloud provider API versions (AWS, Azure, GCP).
* **Key Controllers inside CCM:**
  1. **Node Controller:** Identifies cloud VM metadata and deletes the Node object if the instance is terminated in the cloud console.
  2. **Route Controller:** Configures routing tables in the cloud VPC.
  3. **Service Controller:** Commands the cloud provider to provision physical Load Balancers (e.g., AWS NLB) for services marked `type: LoadBalancer`.
* **Initialization Taint:** Nodes register with the taint `node.cloudprovider.kubernetes.io/uninitialized:NoSchedule` until the CCM initializes their cloud parameters.

---

## 5. Mixed Version Proxy (Version Skew Support)

During rolling cluster upgrades, a cluster runs in a **Version Skew** state (e.g., one API server is upgraded to `v1.31` while another is still running `v1.30`).

* **The Problem:** If a client requests a resource type unique to `v1.31`, and the load balancer routes the request to the `v1.30` API server, it will fail with a `404 Not Found`.
* **The Solution:** The Mixed Version Proxy. When enabled, an older API server that receives an unknown resource request will query its peers via the `apiservernetwork.discovery.k8s.io` group. It then transparently reverse-proxies the request internally to a newer API server that supports it.

---

## 🛠️ Practical Proof of Concept (PoC)

### Target Scenario
We will create a multi-node cluster (`1 control-plane, 2 worker nodes`), inspect the static pods running the Control Plane components, and locate the HA Leader Election leases.

### Step-by-Step Guided Steps

1. **Create the `kind-config.yaml` for a Multi-Node Cluster:**
   Write a configuration for 1 control-plane and 2 worker nodes:
   ```yaml
   cat <<EOF > kind-config.yaml
   kind: Cluster
   apiVersion: kind.x-k8s.io/v1alpha4
   nodes:
   - role: control-plane
   - role: worker
   - role: worker
   EOF
   ```

2. **Provision the Cluster:**
   Create the cluster using the config:
   ```bash
   kind create cluster --config kind-config.yaml --name cka-poc
   ```

3. **Verify the Multi-Node Nodes Status:**
   Check the node roles and versions:
   ```bash
   kubectl get nodes -o wide
   ```

4. **Inspect Control Plane Static Pods:**
   Control plane components in kubeadm-based clusters (like `kind`) run as Static Pods. Their manifests live on the control plane node. Check them:
   ```bash
   kubectl get pods -n kube-system -o wide
   ```
   Notice that `kube-apiserver-cka-poc-control-plane`, `kube-controller-manager-...`, `kube-scheduler-...`, and `etcd-...` are all running directly on the control plane node.

5. **Access Manifests inside the Control Plane Container:**
   `kind` nodes run as Docker containers. Exec into the control-plane container to inspect the static pod manifests:
   ```bash
   docker exec -it cka-poc-control-plane ls -la /etc/kubernetes/manifests
   ```
   You will see the YAML templates for `etcd.yaml`, `kube-apiserver.yaml`, `kube-controller-manager.yaml`, and `kube-scheduler.yaml`. The local `kubelet` on this master node reads these files and ensures they are running.

6. **Locate HA Leader Election Leases:**
   List the leases in the `kube-system` namespace to identify the active leaders for the scheduler and controller-manager:
   ```bash
   kubectl get leases -n kube-system
   ```
   Describe one of them to see the current leaseholder:
   ```bash
   kubectl describe lease kube-scheduler -n kube-system
   ```
   Look for the `Holder Identity` (which will be the name of the control plane node).

7. **Clean up Resources:**
   Delete the local cluster:
   ```bash
   kind delete cluster --name cka-poc
   rm kind-config.yaml
   ```

---

## 🔗 Related Modules
- [Module 01: Kubernetes API Mechanics & kubectl CLI](01_kube_api_and_kubectl.md) - Explains how clients interact with the `kube-apiserver` fronted by the Control Plane.
- [Module 03: Node Mechanics & Resource Limits](03_node_mechanics_and_resource_limits.md) - Deep dive into Kubelet registration, heartbeats, and worker node resource boundaries.
- [Module 04: Workload Lifecycle & Self-Healing](04_workload_lifecycle_and_healing.md) - Explains the reconciliation loops managed by the controllers (e.g. ReplicaSets, Pod self-healing).
- [Module 05: Containers, Runtimes, and Lifecycle Management](05_containers_runtimes_and_lifecycle.md) - Covers container image pull mechanics, the Container Runtime Interface (CRI), lifecycle hooks, init containers, sidecars, and ephemeral containers.
