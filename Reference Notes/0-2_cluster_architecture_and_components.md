# Module 0-2: Cluster Architecture & Control Plane Components

This module covers the macro and micro architecture of a Kubernetes cluster, diving deep into the roles of control plane and worker components, High Availability (HA) topologies, Cloud integration (CCM), and Version Skew proxying.

---

## 🗺️ Cognitive Map: How to Think About the Flow of Knowledge

To build a strong intuition for this module, think of the topics as moving from macro cluster layout to micro component interactions, scalability, and the object model:

```mermaid
graph TD
    A["Macro Architecture (Brain vs. Muscle)"] --> B["Micro Components (Deep dive of daemons)"]
    B --> C["HA and Scaling Topologies (Stacked vs. External etcd)"]
    C --> D["Node Integration and Version Skew (How components match versions)"]
    D --> E["Declarative Object Model (API Objects, Namespaces, Finalizers)"]
```

1. **Step 1: Macro Architecture (Section 1):** We start with the bird's-eye view, dividing the cluster into the Control Plane (state management) and Worker Nodes (workload execution).
2. **Step 2: Micro Components (Section 2 & 2.1):** We dive deep into the specific daemons running on these hosts—how the `apiserver`, `etcd`, `scheduler`, `controller-manager`, `kubelet`, and `kube-proxy` cooperate to run a Pod.
3. **Step 3: HA & Scaling Topologies (Section 3):** We look at high availability, comparing stacked `etcd` configurations against external topologies to build fault-tolerant control planes.
4. **Step 4: Node Integration & Version Skew (Section 4 & 5):** We examine the mechanics of worker registration and the version skew policies, ensuring components of different release versions can safely co-exist.
5. **Step 5: Declarative Object Model (Section 6):** Finally, we study the metadata and lifecycle rules (Namespaces, Labels, Annotations, OwnerReferences, and Finalizers) that govern how resources are managed and garbage collected inside the cluster.

By following this flow, you progress from **System Topology (Macro) → Daemon Mechanics (Micro) → High Availability Design (Scaling) → API Object Model (Data Schema)**.

---


## 1. Macro View: Control Plane vs. Worker Nodes

A Kubernetes cluster is a distributed system consisting of two primary roles: the **Control Plane** (the brain) and **Worker Nodes** (the muscle). Below is a structural diagram showing how these components interact:

```mermaid
graph TD
    subgraph ControlPlane ["Control Plane (Master Node)"]
        API[kube-apiserver]
        ETCD[(etcd cluster)]
        SCHED[kube-scheduler]
        KCM[kube-controller-manager]
        
        API <--> ETCD
        SCHED <--> API
        KCM <--> API
    end

    subgraph WorkerNode1 ["Worker Node 1"]
        KLET1[kubelet]
        KPROX1[kube-proxy]
        CR1[Container Runtime Engine]
        
        subgraph Pods1 ["Pods"]
            POD1[Pod 1]
            POD2[Pod 2]
        end
        
        KLET1 <--> API
        KPROX1 <--> API
        KLET1 --> CR1
        CR1 --> POD1
        CR1 --> POD2
    end

    subgraph WorkerNode2 ["Worker Node 2"]
        KLET2[kubelet]
        KPROX2[kube-proxy]
        CR2[Container Runtime Engine]
        
        subgraph Pods2 ["Pods"]
            POD3[Pod 3]
        end
        
        KLET2 <--> API
        KPROX2 <--> API
        KLET2 --> CR2
        CR2 --> POD3
    end
```

### Conceptual Intuition: The Ship Analogy
To build an intuitive understanding of the Kubernetes architecture, think of a shipping port containing cargo and control ships:

| Kubernetes Component | Ship Analogy Role | Description |
| :--- | :--- | :--- |
| **Worker Nodes** | **Cargo Ships** | The physical or virtual machines that do the actual work of carrying and running the containers. |
| **Control Plane (Master Node)** | **Control Ship** | The command ship responsible for managing and monitoring the cargo ships, planning operations, and coordinating loading processes. |
| **`etcd`** | **Ship Logbook / Registry** | A highly available database that stores information in a key-value format about all ships, which containers are on which ship, loading times, and configurations. |
| **`kube-scheduler`** | **Loading Crane** | The scheduler that plans and places containers on specific cargo ships based on size, capacity, available resources, and constraints (like container destinations, taints, tolerations, and affinity rules). |
| **`kube-controller-manager`** | **Port Offices / Departments** | Specialized departments that handle specific control operations: <br>• *Operations Team (Node Controller)*: Handles ship onboarding, traffic control, and deals with damaged/destroyed ships.<br>• *Cargo Team (Replication Controller)*: Ensures the desired number of containers are active and undamaged in a replication group. |
| **`kube-apiserver`** | **Port Authority / Coordinator** | The primary management component that orchestrates all actions. It exposes the API used by external users and internal offices to query state and make changes. |
| **`kubelet`** | **Ship Captain** | An agent running on each worker node (cargo ship) that listens for instructions from the `kube-apiserver`, deploys or destroys containers, and sends periodic status reports back. |
| **`kube-proxy`** | **Port Services / Communications** | The service that installs communication rules so containers on different cargo ships can talk to each other (e.g., routing traffic from a web server on one ship to a database server on another). |
| **Container Runtime Engine** | **Container Compatibility Engine** | The underlying software (e.g., `containerd`, Docker) required on all nodes to support running containers. If control plane components are run as containers, it is also required on control plane nodes. |

### A. Core Architectural Foundations

Before container orchestration, deploying multi-tier applications (e.g., UI, backend, database) in **standalone containers** posed major reliability challenges:
* **Host Failures:** If a container crashed, the host system restarted it. However, if the entire host machine crashed, all containers went offline.
* **Network Resolution:** Manually resolving container network locations across different hosts required custom, fragile routing layers.
* **Orchestration Need:** An Orchestrator acts as a control agent to handle container runtime states, configure virtual networks, scale containers, and automate recovery.
  * **Docker Swarm:** A lightweight, simple Orchestrator suitable for small teams but hard to scale for massive configurations.
  * **Kubernetes:** A mature, open-source Orchestrator developed by Google (derived from their internal project **Borg**).

Kubernetes operates as both an **Orchestrator** (managing container life-cycle, networks, and configurations) and a **Cluster** (pooling compute, memory, and storage from multiple physical or virtual nodes into a single unified resource pool).
* **Node Redundancy:** If a node crashes, other nodes complement the resource deficiency and take over the workloads.
* **Horizontal Scaling (Scale Out/In):** Dynamically adding or removing nodes to adjust cluster compute capacity.
* **Vertical Scaling:** Increasing or decreasing the CPU/Memory resources allocated to a node or a container.

### B. The Control Plane (The Brains / Master Nodes)
* **Purpose:** Manages overall cluster state, schedules workloads, makes global decisions (e.g., detecting node failures), and exposes the API.
* **Linux Domain:** Runs on one or more Linux-based nodes, referred to as **Master Node(s)**.
* **Cluster Decoupling:** Kubernetes completely decouples the master control plane from the worker data plane. This ensures that control plane resources are not overloaded by high-resource user application loads, protecting cluster management performance. In small-scale or development environments, both control plane and worker components may run on a single node.
* **Production Sizing:** In production, master nodes must be deployed in **odd numbers** (e.g., 3, 5) to achieve consensus quorum (majority) and avoid split-brain issues.
* **Core Components:**
  * **`kube-apiserver`**: The front gate; receives and validates API requests, writing state directly to etcd.
  * **`etcd`**: Key-value data store representing the source of truth for all cluster configurations.
  * **`kube-scheduler`**: Matches unassigned Pods to nodes based on resource capacity, constraints, and affinity rules.
  * **`kube-controller-manager`**: Runs controller loops to compare actual cluster state with desired state.

### C. Worker Nodes (The Muscle / Data Plane)
* **Purpose:** Runs your containerized applications (Pods).
* **OS Support:** One or more nodes running Linux or Windows (Linux remains the dominant, primary platform for containers; Windows support exists but is specialized).
* **Core Components:**
  * **`kubelet`**: The node captain service; ensures containers are running inside Pods according to the PodSpecs.
  * **`kube-proxy`**: The network manager; maintains host network routing rules to implement Services.
  * **`Container Runtime`**: The container execution engine (e.g., `containerd` or `cri-o`) that pulls images and runs containers.
* **Operation:** Receives instructions from the control plane, pulls images, launches containers, and continuously feeds health telemetry back to the API server. For details on node registration, resources, and leases, see [Module 03: Node Mechanics & Resource Limits](0-3_node_mechanics_and_resource_limits.md). For Pod lifecycle and probing details, see [Module 04: Workload Lifecycle & Self-Healing](0-4_workload_lifecycle_and_healing.md).

---

## 2. Control Plane & Core Components (Deep Dive)

### A. `kube-apiserver` (The Front Gate)
* **Central Management:** Serves as the primary entry point for all control operations. Without it, the control plane cannot receive commands.
* **HTTP & JSON Protocol:** Receives incoming requests using standard HTTP protocol (REST API Web Server) but **always responds in JSON format**, which is parsed by tools (like `kubectl`) and applications to communicate.
* **Security Checks:** Authenticates the caller, validates their authorization permissions (e.g., checking if the user is allowed to create nodes or pods), applies admission plug-ins (e.g., `NodeRestriction`, `LimitRanger`), and persists state.
* **Configurations & Flags:**
  * `--advertise-address`: IP address to advertise to cluster members.
  * `--etcd-servers`: List of backend `etcd` URLs (e.g. `https://127.0.0.1:2379`). This is how the API server connects to the etcd cluster.
  * `--authorization-mode`: Decides auth chain order (e.g., `Node,RBAC`).
  * `--enable-admission-plugins`: Sequence of admission controllers (e.g., `NamespaceLifecycle`, `LimitRanger`, `ServiceAccount`).
* **Client and Component Certificate Configurations:**
  * To secure connectivity, several certificates are specified as CLI flags:
    * `--client-ca-file`: CA certificate bundle used to authenticate client certificates (e.g., `/etc/kubernetes/pki/ca.crt`).
    * `--tls-cert-file` and `--tls-private-key-file`: The server certificate and key enabling HTTPS on the API server.
    * `--etcd-cafile`, `--etcd-certfile`, `--etcd-keyfile`: Client certificates used by the API server to authenticate itself to the `etcd` cluster securely.
    * `--kubelet-client-certificate` and `--kubelet-client-key`: Credentials used by the API server to connect and authenticate to worker node `kubelet` API endpoints.
* **Verification Paths:**
  * **kubeadm Clusters:** Configured as a Static Pod. Manifest path: `/etc/kubernetes/manifests/kube-apiserver.yaml`.
  * **Manual Setup:** Configured as a systemd service. Service file path: `/etc/systemd/system/kube-apiserver.service`.
  * For runtime process inspection, execute: `ps -aux | grep kube-apiserver`.

### B. `etcd` (The Source of Truth)
* **Storage Model Comparison (SQL vs. Document vs. Key-Value):**
  * **Relational / SQL Databases:** Tabular format using rigid schemas with rows and columns. Adding new columns (e.g. salary, grades) affects the entire table structure, resulting in null/empty cells for rows that do not require those attributes. Best for structured data and complex SQL queries, but rigid.
  * **Document Stores:** Stores independent documents (usually in JSON format) per entry. Changes to one document do not affect others, meaning no strict schema is required. Flexible and best for semi-structured data, but limits complex queries (such as joins).
  * **Key-Value Stores:** Stores values against unique keys (e.g. `name: John`, or hierarchical key strings like `user:john_doe` pointing to a JSON document). No schema constraints, extremely fast lookup performance, and highly flexible since any payload structure can be stored. `etcd` is a distributed, reliable key-value store optimized for simple, high-speed lookups and writes.
* **Independence:** It runs as an independent daemon/service outside the API server (it is a standalone cluster/process).
* **Consensus & Ports:** Uses the **Raft consensus algorithm** to prevent split-brain. Client communication (e.g., API Server queries) listens on port **`2379`** by default. Peer-to-peer cluster node communication (e.g., leader election and replication) listens on port **`2380`**.
* **Raft Consensus Evolution & Quorum:**
  * **Evolution:** etcd version 2.0 (released in February 2015) redesigned the Raft consensus algorithm, enabling it to support more than 1,000 writes per second.
  * **HA Quorum:** In high-availability configurations, an odd number of `etcd` members (e.g., 3, 5) form a cluster to maintain consensus. Quorum is the majority of members needed to agree on writes and elect a leader:
    $$\text{Quorum} = \left\lfloor \frac{N}{2} \right\rfloor + 1$$
* **Configurations & Flags:**
  * `--listen-client-urls` and `--advertise-client-urls`: Specifies the addresses on which etcd listens for client API requests (port `2379`). Kube API server configuration dials this advertised client URL.
  * `--initial-cluster`: Lists cluster peer instances (`controller-0=https://...:2380,controller-1=https://...:2380`) for Raft consensus group formation.
  * `--data-dir`: Node-level directory path where keys are persisted (`/var/lib/etcd`).
* **API v2 vs v3 (CKA Essential CLI Tricks):**
  * Default behavior of `etcdctl` can vary; you must target API v3 by exporting `export ETCDCTL_API=3` (or prepending `ETCDCTL_API=3` to commands).
  * **API Changes:** Version 2.0 (2015) redesigned Raft; version 3.0 (2017) changed commands and added transaction support. API v2 used `set`, `get`, `rm` commands, while API v3 uses `put`, `get`, `del` (or `delete`) commands and supports transactions. CNCF incubation began in Nov 2018 and graduated in Nov 2020. Version 3.5 (2021) introduced `etcdutl`.
* **Kubernetes Registry Key Layout:**
  * All cluster state objects (nodes/minions, pods, replica sets, deployments, secrets, roles) are organized under a physical tree/directory hierarchy starting with `/registry` as the root.
  * *Example Path:* Pod specs are written under `/registry/pods/<namespace>/<pod-name>`.
  * Every change applied via `kubectl` is only considered complete once successfully written to the `etcd` registry database.
* **Querying Registry Keys Command:**
  To list all objects registered by the API Server in etcd, target the static pod using certificate flags (required for TLS client authorization):
  ```bash
  kubectl exec -n kube-system etcd-control-plane -- etcdctl \
    --cacert=/etc/kubernetes/pki/etcd/ca.crt \
    --cert=/etc/kubernetes/pki/etcd/server.crt \
    --key=/etc/kubernetes/pki/etcd/server.key \
    get / --prefix --keys-only
  ```

### C. `kube-scheduler` (The Matchmaker)
* **Role:** Watches the API server for unassigned Pods (`spec.nodeName` is blank) and assigns them to nodes.
* **Resource Utilization & Metrics:** Evaluates nodes using algorithms that assess node health, available vs. utilized resources (percentage of free memory/CPU), and checks if the pod has any node affinity/anti-affinity bindings to verify if the placement can occur.
* **Scheduling Pipeline Phases:**
  1. **Filtering (Predicates):** Evaluates nodes and filters out those unable to accommodate the Pod (e.g., checks CPU/Memory requests, node selectors, taints).
  2. **Ranking (Priorities):** Scores the remaining candidate nodes on a scale of `0` to `10` using priority functions (e.g., resource balance, image locality). The node with the highest score is selected.
  3. **Binding:** Submits a binding object to the API server, which writes the selected node name to `spec.nodeName`. Kubelet then detects and executes this binding.
* **Configurations & Customization:** Schedulers are highly customizable. You can configure multiple custom schedulers in the same cluster and reference them via `spec.schedulerName` in your Pod manifests.
* **Config Files & Binary Run:** In manual installations, the scheduler runs as a service pointing to a scheduler configuration file via `--config=<path-to-config-file>`.
* **Verification & Static Pod Paths:**
  * **kubeadm:** Manifest at `/etc/kubernetes/manifests/kube-scheduler.yaml`.
  * **Manual Setup:** Service file at `/etc/systemd/system/kube-scheduler.service`.
  * Process check: `ps -aux | grep kube-scheduler`.

### D. `kube-controller-manager` (The Enforcer)
The **`kube-controller-manager`** is the core Control Plane component responsible for running the **reconciliation loops** that maintain the cluster's state. It is compiled as a single binary daemon but runs many independent controllers concurrently.

```text
 ┌────────────────────────────────────────────────────────┐
 │            The Reconciliation Loop                     │
 │                                                        │
 │      ┌──────────────┐          Desired State (etcd)    │
 │      │   Observe    │◄─────────┐                       │
 │      └──────┬───────┘          │                       │
 │             │                  │                       │
 │             ▼                  │                       │
 │      ┌──────────────┐          │                       │
 │      │   Analyze    │──────────┼──► [ Diff ? ]         │
 │      └──────┬───────┘          │        │              │
 │             │                  │        ▼              │
 │             ▼                  │    Yes: Act           │
 │      ┌──────────────┐          │    No: Loop           │
 │      │     Act      │──────────┘                       │
 │      └──────────────┘                                  │
 └────────────────────────────────────────────────────────┘
```

#### 1. What is the Reconciliation Loop?
The Reconciliation Loop is a continuous, infinite control loop that monitors the cluster and drives it toward the **desired state** defined in your YAML manifests. It performs three core steps repeatedly:
1.  **Observe (Current State):** Queries the actual state of the cluster (e.g., checking how many containers are running, or if a node is healthy).
2.  **Analyze (Diff):** Compares the *observed actual state* against the *desired state* retrieved from `etcd` (e.g. "Desired replicas: 3, Actual running: 2. Diff: +1 Pod needed").
3.  **Act (Remediate):** Executes the necessary operations to eliminate the difference (e.g. telling the API Server to create a new Pod).

#### 2. The Role of the Controller Manager
The `kube-controller-manager` hosts these reconciliation loops. Inside it, a dedicated controller exists for every Kubernetes resource type:
*   **ReplicaSet Controller:** Reconciles Pod counts. If a Pod is deleted manually, it spins up a replacement.
*   **Node Controller:** Audits node health. Rather than scanning heavy Node objects, it watches lightweight **Lease Objects** (heartbeats) updated by each node's `kubelet` every 10 seconds in the `kube-node-lease` namespace. If a lease is not updated within the node monitor grace period (default 40s), the controller marks the node `Unreachable` and coordinates workload evictions. This Lease model reduces `etcd` write load dramatically.
*   **Namespace Controller:** Cleans up all nested resources when a namespace is deleted.
*   **Deployment Controller:** Orchestrates rolling updates by shifting traffic between old and new ReplicaSets.

#### 3. How Controllers Watch the API Server (Informers vs. Polling)
To prevent crushing the API server with constant query requests (polling), controllers use **Informers** and HTTP **Watch** connections:
*   **HTTP Watch:** A controller establishes a persistent HTTP connection to the `kube-apiserver`.
*   **Push Notifications:** When a resource changes (e.g., a Pod is added or deleted), the API Server pushes an event notification directly to the controller.
*   **Shared Informers:** The controller caches the state locally using a `SharedInformer` to read resource status instantly without hitting the API server database repeatedly.

#### 4. Configuration Directories & Static Pod Manifests
*   **kubeadm:** Manifest at `/etc/kubernetes/manifests/kube-controller-manager.yaml`.
*   **Manual Setup:** Service file at `/etc/systemd/system/kube-controller-manager.service`.
*   You can select which controllers to run using the `--controllers` flag (e.g. `--controllers=*` to enable all, or prefixing with a minus `-` to disable specific ones).

#### 5. Deep-Dive: Watch Connections, Concurrency & Data Consistency

To implement a highly reliable distributed control plane, Kubernetes coordinates updates, monitors node heartbeats, and handles write concurrency using specific protocols:

##### A. The Watch Connection (HTTP Chunked Streaming)
*   **The Polling Problem:** If controllers constantly polled the API Server (e.g., asking *"Has this lease changed?"* every 1s), the API Server and `etcd` would run out of resources and crash.
*   **The Watch Solution:** Instead of polling, a controller initiates an HTTP `GET` request appending the query parameter `?watch=true`.
*   **Chunked Transfer Encoding:** The API Server returns an HTTP `200 OK` response but keeps the TCP connection open indefinitely (`Transfer-Encoding: chunked`).
*   **Push Notifications:** Whenever a resource changes, the API Server instantly pushes a tiny JSON chunk containing the change details down that pre-established pipe (the Pub/Sub pattern). 
*   **Decoupled Action:** The controller reads the stream, updates its local `SharedInformer` memory cache, runs its business logic, and initiates a **new, separate connection** (like a `POST` or `PUT`) to request updates.

##### B. Kubelet to API-Server Network Paths
*   **Worker-to-Master (Outbound HTTPS):** The `kubelet` is an HTTPS client. It does **not** have an ongoing persistent bidirectional connection to the API Server. It makes standard outbound HTTPS requests (e.g., PUT/PATCH updates to its Lease object every 10s) and closes them or returns them to a standard reuse pool.
*   **Master-to-Worker (The Persistent Proxy Tunnel):** When you run `kubectl logs` or `kubectl exec`, the API Server must act as the client and initiate a connection *down* to the Kubelet on port `10250`. 
    *   *The Firewall Issue:* Master nodes are often isolated and blocked by firewalls from initiating inbound traffic to worker subnets.
    *   *The Konnectivity Solution:* An agent (`konnectivity-agent`) on the worker node establishes a **persistent outbound TCP connection** to the `konnectivity-server` on the master. When the API Server needs to talk to the Kubelet, it routes the traffic down this pre-established tunnel.

##### C. Optimistic Concurrency Control (OCC) vs. Pessimistic Locking
When thousands of controllers send write requests, Kubernetes must prevent them from overwriting each other's changes.
*   **Pessimistic Locking (PCC):** Locks a database record when Client A reads it, blocking Client B from even reading it until Client A finishes. This creates massive performance bottlenecks and is **not** used by Kubernetes.
*   **Optimistic Concurrency Control (OCC):** Assumes conflicts are rare. It allows concurrent reads and writes, but verifies that no other client has modified the object since it was read, using `metadata.resourceVersion`.

###### The Race Condition Scenario: SRE vs. HPA Scale Conflict
*   **Setup:** A Deployment `web-server` has `replicas: 10` and `resourceVersion: "500"`.
*   **Action 1:** SRE reads version `"500"` and prepares a scale-down to `5` replicas.
*   **Action 2:** HPA reads version `"500"` and prepares a scale-up to `12` replicas.
*   **The Execution:**
    1.  **HPA's request arrives first:** The API Server checks the DB (which is currently `"500"`). It matches the request version `"500"`. The write succeeds, setting replicas to `12` and bumping the database version to `"501"`.
    2.  **SRE's request arrives a millisecond later:** SRE sends a request to scale to `5` with base version `"500"`. The API Server checks the DB (which is now `"501"`).
    3.  **The Mismatch:** The versions do not match (`"500"` != `"501"`). The API Server rejects the SRE's write and returns an **HTTP 409 Conflict** error.
*   **The Resolution:** The SRE's CLI tool catches the 409 error, fetches the fresh copy of the Deployment (which has version `"501"` and `replicas: 12`), and prompts or retries the scale request with base version `"501"`.

> [!NOTE] **Q&A: If the SRE retries and sets it to 5, isn't the 12 still overwritten?**
> **Yes.** The database value is logically overwritten to 5. However, OCC changes **how** this happens to prevent bugs:
> *   **Without OCC (Silent/Accidental Erasure):** The SRE's command would overwrite the HPA's scale-up *blindly and silently*. The SRE has no idea the HPA had scaled it to 12 (thinking they scaled from 10 to 5). The 12 replicas are lost by accident.
> *   **With OCC (Intentional/Aware Override):** The SRE's command is blocked by the 409 Conflict. The SRE is forced to pull the new version, revealing that the HPA had scaled it to 12. The SRE now makes an **informed decision**:
>     *   *Option A (Retreat):* Cancel the scale-down because they see the app is under high load (the 12 replicas are saved).
>     *   *Option B (Manual Override):* Intentionally override the HPA and scale to 5 anyway (e.g. for emergency maintenance).
> OCC does not stop you from overriding data; it stops you from modifying data **based on stale information**.

##### D. Declarative Merging (PATCH vs. PUT) & The Tug-of-War
To avoid conflicts and prevent actors from fighting over fields:
*   **PATCH (Declarative / `kubectl apply`):** Instead of sending the full object, clients send only the specific fields they wish to modify (e.g. SRE patches a label, HPA patches replica count). The API Server merges these changes seamlessly without triggering version conflicts.
*   **Tug-of-War:** If two components *do* patch the same field (e.g. SRE manually edits `replicas: 5` while HPA sets `replicas: 12`), the SRE's change will initially succeed, but on the next HPA loop cycle (usually 15 seconds), the HPA will see the high CPU and patch it back to 12.
*   **Best Practice:** Never manually edit the `replicas` field of a Deployment managed by an HPA. Instead, modify the HPA configuration (e.g., changing its `minReplicas` or `maxReplicas` settings) to keep human and machine state goals aligned.



> [!NOTE] Object vs. Resource Terminologies
> * A **Kubernetes object** is a persistent *record of intent* in the cluster. It represents a specific instance of something you want to exist. When created, you tell Kubernetes your desired state (spec) and Kubernetes ensures the actual state (status) is reconciled to match it ("make it so and keep it that way"). Objects have a `spec`, `status`, and `metadata`.
> * A **resource** is a category or API class of objects.
> * *Example:* **Pod** is a resource type, while **my-app-pod** is an instance object of that Pod resource type.

### E. Pod Creation Lifecycle Flow
When a user applies a manifest (e.g., `kubectl apply -f pod.yaml`):
1. The `kube-apiserver` receives the HTTP POST request containing the manifest data.
2. The API server performs authentication, authorization, and validation checks.
3. Upon approval, the API server saves the Pod specification as a record of intent in `etcd`.
4. The API server **publishes** a "Pod Created" event.  # Important note
5. The `kube-scheduler` (which is subscribed/watching the API server event stream) detects the new unscheduled Pod (where `spec.nodeName` is empty).
6. The scheduler runs its filter/rank algorithms, chooses a worker node, and writes the selected host back to the API server (`binding` operation).
7. The API server updates `etcd` and **publishes** a binding event. .  # Important note
8. The `kubelet` running on the selected worker node (also watching the API server) detects that a Pod has been assigned to its node.
9. The `kubelet` interfaces with the local Container Runtime (CRI) to pull the image and run the containers, writing the status back to the API server.

### F. Worker Node Status Telemetry & Eviction Timings
Worker nodes through their `kubelet` actively update the control plane with health telemetry:
* **Kubelet Status Heartbeat:** The `kubelet` updates the node status every **5 seconds**.
* **Lease Timeout (40s):** If the API server does not receive a heartbeat for **40 seconds** (the node lease expiry window), the Node Controller flags the node as unreachable and stops routing new traffic/requests to it.
* **Eviction Timeout (5m):** To the user, everything might still appear ready or pending, but once **5 minutes** (default eviction grace period) passes, the node status is fully updated to `NotReady` and the **node controller initiates cascading deletions** to evict the Pods and reschedule them to healthy nodes.

### G. `kube-proxy` (The Network Router)
* **Role:** A network agent running on every node that enables cluster-wide network routing for Services.
* **Service Virtual Entity:** Services are *virtual entities in the cluster's memory*  — they do not correspond to any container, network card, or physical interface.
* **Routing Mechanism (iptables vs IPVS):**
  * Kube-proxy watches the API Server for new Services and Endpoints and implements host-level routing:
    * **`iptables` Mode (Default):** Configures sequential netfilter rules inside the kernel. Lookup complexity is $O(N)$, causing high CPU overhead in large clusters. Uses random selection load balancing.
    * **`IPVS` Mode:** Configures hash tables in the kernel's IP Virtual Server module. Lookup complexity is $O(1)$, which is highly scalable for large clusters. Supports advanced algorithms like Round Robin (`rr`) or Least Connections (`lc`).
* **Important Distinction:** `kube-proxy` is for **Service networking** (handling client-to-service routing), not for API server-to-node ---> control plane communications to worker nodes (is handled directly by the `kubelet` to api-server).
* **Verification & Deployment:**
  * **kubeadm:** Deployed as a `DaemonSet` in the `kube-system` namespace.
  * Retrieve DaemonSet configuration: `kubectl get daemonset -n kube-system kube-proxy`.
  * List instances and check logs: `kubectl get pods -n kube-system -l k8s-app=kube-proxy` and `kubectl logs -n kube-system <pod-name>`.
  * Verify programmed iptables rules on worker nodes: `iptables -t nat -L KUBE-SERVICES -n -v`.

---

## 2.1 Component Configuration Paths Quick Reference

| Component              | Installation Mode    | Config File / Path                                       | Check Status Command                                                 |
| :--------------------- | :------------------- | :------------------------------------------------------- | :------------------------------------------------------------------- |
| **Kube API Server**    | kubeadm (Static Pod) | `/etc/kubernetes/manifests/kube-apiserver.yaml`          | `kubectl get po -n kube-system -l component=kube-apiserver`          |
|                        | Manual (systemd)     | `/etc/systemd/system/kube-apiserver.service`             | `systemctl status kube-apiserver`                                    |
| **etcd**               | kubeadm (Static Pod) | `/etc/kubernetes/manifests/etcd.yaml`                    | `kubectl get po -n kube-system -l component=etcd`                    |
|                        | Manual (systemd)     | `/etc/systemd/system/kube-apiserver.service`             | `systemctl status etcd`                                              |
| **Kube Scheduler**     | kubeadm (Static Pod) | `/etc/kubernetes/manifests/kube-scheduler.yaml`          | `kubectl get po -n kube-system -l component=kube-scheduler`          |
|                        | Manual (systemd)     | `/etc/systemd/system/kube-scheduler.service`             | `systemctl status kube-scheduler`                                    |
| **Controller Manager** | kubeadm (Static Pod) | `/etc/kubernetes/manifests/kube-controller-manager.yaml` | `kubectl get po -n kube-system -l component=kube-controller-manager` |
|                        | Manual (systemd)     | `/etc/systemd/system/kube-controller-manager.service`    | `systemctl status kube-controller-manager`                           |
| **Kube Proxy**         | kubeadm (DaemonSet)  | `kubectl edit ds/kube-proxy -n kube-system`              | `kubectl get ds -n kube-system -l k8s-app=kube-proxy`                |
|                        | Manual (systemd)     | `/etc/systemd/system/kube-proxy.service`                 | `systemctl status kube-proxy`                                        |

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
