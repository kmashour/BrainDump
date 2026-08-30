---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - kubernetes/architecture
  - kubernetes/ha
---

# Module 0-2-2: HA Control Plane Topologies, Konnectivity & Object Metadata

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Reference MOC]] > **Module 0-2-2**

---

## 2.2 Control Plane Egress Proxy (Konnectivity)

In standard cluster topologies, the Control Plane and Worker Nodes reside in different networks or subnetworks. Direct TCP routing from the control plane node to the worker node (specifically pod/service IPs) may be firewalled or unroutable. Historically, Kubernetes used SSH Tunnels (deprecated and removed in v1.22) to resolve this network split. The modern solution is **Konnectivity (apiserver-network-proxy)**.

### A. Architectural Topology & Tunnel Flow

Konnectivity uses a Server-Agent architecture to route egress traffic from the API server to the cluster.

```mermaid
flowchart LR
    subgraph Control_Plane ["Control Plane (Private Subnet)"]
        APIServer["Kube-APIServer"] -->|1. Dial localhost Unix Socket| ProxyServer["Konnectivity Server"]
    end

    subgraph Cluster_Network ["Cluster Network (Worker Nodes)"]
        ProxyServer <-->|2. Bidirectional mTLS gRPC Tunnel (Port 8132)| AgentPod["Konnectivity Agent Pod"]
        AgentPod -->|3. TCP Connection| Target["Target Resource (Pod / Webhook / Kubelet)"]
    end

    style ProxyServer fill:#f9f,stroke:#333,stroke-width:1px
    style AgentPod fill:#bfb,stroke:#333,stroke-width:1px
```

1. **Konnectivity Server:** Runs in the control plane. It listens for agent registrations on port **`8132`** (mTLS/grpc) and exposes a UNIX domain socket or local port (`8055`) for the API server.
2. **Konnectivity Agent:** Runs in the cluster as a Deployment or DaemonSet. Upon startup, it dials the Konnectivity Server (outbound request to port `8132` on the control plane load balancer). It establishes a long-lived, bidirectional mTLS gRPC connection.
3. **The Dial Flow:**
   * When a user runs an interactive command (e.g. `kubectl logs`, `kubectl port-forward`, or an admission webhook triggers in the cluster), the `kube-apiserver` looks up its **Egress Selector Configuration**.
   * Instead of dialing the target pod/node IP directly, the API Server dials the local Unix domain socket connected to the Konnectivity Server.
   * The Konnectivity Server multiplexes this TCP request over the active gRPC tunnel to the registered Agent Pod on the target node.
   * The Agent Pod opens a standard TCP socket segment to the final target IP (e.g., Kubelet port `10250` or the Webhook service port) and forwards the full-duplex payload.

### B. Egress Selector Configuration
The `kube-apiserver` decides where to route egress traffic using `/etc/kubernetes/egress-selector-configuration.yaml`.
```yaml
apiVersion: apiserver.k8s.io/v1beta1
kind: EgressSelectorConfiguration
connectionServices:
  - name: cluster
    controlPlane:
      # Route cluster-destined traffic through the local Konnectivity UNIX socket
      egressSelection:
        name: cluster
      connection:
        proxyProtocol: GRPC
        transport:
          uds:
            udsName: /etc/kubernetes/konnectivity-server/konnectivity-server.socket
```
Configure the API Server flag: `--egress-selector-config-file=/etc/kubernetes/egress-selector-configuration.yaml`.

### C. Scalability & Operational Challenges

1. **DaemonSet vs. Deployment:**
   * Running the agent as a **DaemonSet** guarantees node-local routing, but uses significant Pod IP space and host resources.
   * Running as a **Deployment** saves Pod IP space and limits CPU/Memory footprint. However, it introduces an extra network hop (the Agent pod must route traffic across nodes to reach the target container IP).
2. **The Admission Webhook Deadlock:**
   * **The Trap:** An administrator configures a validating admission webhook (e.g., OPA Gatekeeper) matching all API resources (`*.*`) to run in the cluster. Later, the cluster restarts or the Konnectivity Agent pods are evicted.
   * **The Deadlock:** The Kubelet tries to recreate the Konnectivity Agent pods. The API Server receives the pod creation request and must call the admission webhook to validate it. To call the webhook, the API Server tries to route traffic through the Konnectivity tunnel. But the tunnel is down because the Konnectivity Agent is not running. The pod creation fails, and the cluster is deadlocked.
   * **Resolution:** Ensure the namespace or the webhook configuration excludes system pod paths or runs webhooks in the control plane network if possible, or bypasses validating pods in the `kube-system` namespace.
3. **Outbound Firewall Restrictions:**
   * If egress traffic on worker nodes is locked down by default, worker firewall rules **must** explicitly permit outbound traffic to the Control Plane Load Balancer/APIServer on Port **`8132`**.
4. **Agent Scale Bottleneck:**
   * The Konnectivity Server validates incoming Agent connections using the `TokenReview` API. Under massive node scaling (e.g., 100+ agents restarting simultaneously), the server can trigger client throttling on the token endpoint, queuing connections. Limit the active Agent replicas or increase API Server client throttling thresholds.
5. **Version Skew:**
   * Maintain version skew constraints. The `apiserver-network-proxy` client library compiled into `kube-apiserver` must match the API Server version, while the standalone Konnectivity Server and Agent binaries can vary by up to two minor versions.

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

### D. Stacked HA Control Plane Bootstrapping with kubeadm
In a **Stacked Control Plane** topology, etcd members are co-located on the control plane nodes (i.e. every control plane node runs a local `etcd` instance and `kube-apiserver` instance). 

#### 1. Pre-requisite: External Load Balancer
A highly available setup requires a stable endpoint (usually a TCP Load Balancer) in front of all control plane nodes:
1. Configure the load balancer to forward TCP traffic on port `6443` to the backend control plane nodes' IP addresses on port `6443`.
2. Configure a TCP health check on port `6443` to route traffic only to healthy `kube-apiserver` instances.

#### 2. Bootstrapping the First Control Plane Node
Initialize the first control plane node by specifying the load balancer IP and port using the `--control-plane-endpoint` flag, and upload the generated certificates to the cluster using `--upload-certs`:
```bash
sudo kubeadm init \
  --control-plane-endpoint "LOAD_BALANCER_IP:6443" \
  --upload-certs \
  --pod-network-cidr=10.244.0.0/16
```
* **`--control-plane-endpoint`**: Configures the cluster so that all nodes (including workers and subsequent control plane nodes) point to the load balancer as the API Server endpoint rather than a single master node IP.
* **`--upload-certs`**: Automatically encrypts and uploads the control plane certificates and keys (e.g. CA, etcd CA, service account keys) to a temporary Secret in the cluster (`kubeadm-certs` in the `kube-system` namespace). This Secret is decrypted by subsequent control plane nodes when they join, allowing them to participate in the HA setup.

#### 3. Joining Additional Control Plane Nodes
The initialization output will provide a dedicated join command for other control plane nodes containing a certificate key:
```bash
sudo kubeadm join LOAD_BALANCER_IP:6443 \
  --token <token> \
  --discovery-token-ca-cert-hash sha256:<hash> \
  --control-plane \
  --certificate-key <key>
```
* **`--control-plane`**: Tells `kubeadm` to join this node as an additional control plane member.
* **`--certificate-key`**: The decryption key needed to download and local-extract the uploaded certificates.

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

## 6. Core Kubernetes Object Model and Metadata

Kubernetes represents its cluster state declaratively using persistent entities called **Objects**. Objects contain specifications describing the desired state and status describing the actual runtime state.

### A. Object Identity & Name Restrictions
Every Kubernetes object has a name that is unique for that resource type within its namespace (or cluster-scoped if global).
* **Names & UIDs:** Objects are identified by a string `name` and a globally unique `UID` generated by the cluster.
* **DNS Subdomain Names (RFC 1123):** Most resource names must conform to RFC 1123 subdomain rules:
  * Maximum 253 characters.
  * Contain only ==lowercase== alphanumeric characters, `-` or `.`.
  * Start and end with an alphanumeric character.
* **RFC 1123 Label Names:** Some object names (like Pods) must be valid RFC 1123 labels:
  * Maximum 63 characters.
  * Contain lowercase alphanumeric characters or `-`.
  * Start and end with an alphanumeric character.
* **RFC 1035 Label Names:** Used by certain resources (like Services):
  * Maximum 63 characters.
  * Lowercase alphanumeric or `-`.
  * Must start with an alphabetic character, and end with an alphanumeric.
  * **Service Exception:** When the `RelaxedServiceNameValidation` feature gate is enabled (default in modern versions), Service names are allowed to start with a digit.

### B. Labels & Selectors
Labels are key/value pairs attached to objects (like Pods) that serve as identifying metadata for organizing and grouping resources.
* **Syntax:** Keys consist of an optional DNS prefix (max 253 chars) followed by a name (max 63 chars), separated by `/`.
  * The prefixes `kubernetes.io/` and `k8s.io/` are strictly reserved for core components.
  * Label values must be 63 characters or less, start/end with an alphanumeric, and can contain `-`, `_`, `.`.
* **Selectors:** Used to query groups of labeled resources.
  * **Equality-based:** = or == (equals), `!=` (not equal). E.g., `environment=production`.
  * **Set-based:** `in`, `notin`, `exists` (specified by key), and `!exists` (by key negation). E.g., `tier in (frontend, backend)`.
* **ReplicaSet Selector Overlaps:** ReplicaSet selectors must not overlap with other controllers in the same namespace, or controllers will conflict/thrash trying to reclaim pods.

### C. Annotations
Annotations are key/value metadata maps used to attach arbitrary non-identifying data.
* **Characteristics:** Unlike labels, annotations cannot be used to select or query objects. They can contain large, unstructured, or structured data (like JSON configurations, tool audit logs, or deployment history).
* **Syntax:** Keys follow the same prefix/name syntax as labels.

### D. Namespaces (Logical Partitioning)
Namespaces partition cluster resources logically but do not offer network or physical machine boundaries by default.
* **Initial Namespaces:**
  * `default`: For resources with no namespace specified.
  * `kube-system`: For control plane and system-level resources.
  * `kube-public`: Globally readable, used for cluster bootstrapping (e.g. `cluster-info`).
  * `kube-node-lease`: Holds the `Lease` heartbeat objects for nodes.
* **Naming Restrictions:** Custom namespace names must not start with the prefix `kube-` as it is reserved for system namespaces.
* **Production Recommendation:** Avoid deploying workloads in the `default` namespace; create dedicated namespaces with resource limits.

### E. Finalizers
Finalizers are string keys in `metadata.finalizers` that inform Kubernetes to block the garbage collection of an object until specific cleanup criteria are met.
* **Mechanism:** When an object with finalizers is deleted, the API server sets `metadata.deletionTimestamp` but does not remove it. A controller processes the cleanup, removes its finalizer key, and when the list is empty, the object is purged from `etcd`.
* **Common Finalizers:**
  * `kubernetes.io/pvc-protection`: Prevents PV/PVC deletion while a Pod is actively using the volume.
  * `kubernetes.io/pv-protection`: Prevents PV deletion while bound to a PVC.

### F. Owner References & Garbage Collection
Kubernetes uses owner references to track relationships between parent resources (e.g. Deployments, ReplicaSets) and their dependents (e.g. Pods).
* **Owner References:** Set in `metadata.ownerReferences`. Includes resource name, UID, API version, and kind.
* **Cascading Deletion Modes:**
  * **Foreground:** Parent is deleted, but remains in "Terminating" state. The `foregroundDeletion` finalizer blocks deletion until all dependents with `ownerReferences.blockOwnerDeletion=true` are deleted.
  * **Orphan:** Deletes the parent resource, leaving dependents running in the cluster. Their owner references are removed, making them orphans.
* **Cross-Namespace Restrictions:** ==Cross-namespace owner references are strictly disallowed. ==A namespaced dependent must have its owner in the same namespace. If a mismatch is detected, Kubernetes ignores the reference and reports an `OwnerRefInvalidNamespace` event.

---

## 🔗 Related Modules
- [Module 01: Kubernetes API Mechanics & kubectl CLI](0-1_kube_api_and_kubectl.md) - Explains how clients interact with the `kube-apiserver` fronted by the Control Plane.
- [Module 03: Node Mechanics & Resource Limits](0-3_node_mechanics_and_resource_limits.md) - Deep dive into Kubelet registration, heartbeats, and worker node resource boundaries.
- [Module 04: Workload Lifecycle & Self-Healing](0-4_workload_lifecycle_and_healing.md) - Explains the reconciliation loops managed by the controllers (e.g. ReplicaSets, Pod self-healing).
- [Module 05: Containers, Runtimes, and Lifecycle Management](0-5_containers_runtimes_and_lifecycle.md) - Covers container image pull mechanics, the Container Runtime Interface (CRI), lifecycle hooks, init containers, sidecars, and ephemeral containers.
