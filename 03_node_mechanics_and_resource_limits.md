# Module 03: Node Mechanics & Resource Limits

This module covers node lifecycles, health monitoring, resource allocation math, Quality of Service (QoS) classes, Linux kernel resource limits (`cgroups`), and node-to-control-plane communication.

---

## 1. Node Registration

Nodes in Kubernetes are treated as actual API objects in `etcd`. They register with the control plane in two ways (see [Module 02: Cluster Architecture & Control Plane Components](02_cluster_architecture_and_components.md#2-control-plane-components-deep-dive) for more details on `etcd` and `kube-apiserver`):
* **Self-Registration (Default):** The `kubelet` service starts on the machine, contacts the `kube-apiserver`, and registers itself by providing its hardware capacity, IP addresses, and versions.
* **Manual Administration:** An administrator creates a Node manifest (YAML) and applies it to the cluster manually, disabling self-registration on the `kubelet` configuration.

---

## 2. Reading Node Status (`kubectl describe node`)

Checking node status is a core CKA troubleshooting skill. The output contains:

### A. Addresses
* **HostName:** The OS hostname of the node.
* **InternalIP:** The primary IP routable within the cluster network.
* **ExternalIP:** The public-facing IP (if applicable).

### B. Conditions
The `kubelet` continuously evaluates these health checks:
* **`Ready`:** `True` if the node is healthy and ready to accept Pods. `False` if unhealthy. `Unknown` if heartbeats have stopped.
* **`DiskPressure`:** `True` if free disk space is critically low.
* **`MemoryPressure`:** `True` if system RAM is critically low.
* **`PIDPressure`:** `True` if the node has run out of Process IDs (PIDs).
* **`NetworkUnavailable`:** `True` if the CNI plugin/network routing is misconfigured.

### C. Capacity vs. Allocatable (Resource Math)
* **Capacity:** The absolute physical hardware of the host (CPU cores, RAM, Disk).
* **Allocatable:** The actual resource pool available for user Pods.
$$\text{Allocatable} = \text{Capacity} - \text{OS Reserved} - \text{Kubelet Reserved} - \text{Eviction Thresholds}$$

---

## 3. Node Heartbeats & The Lease API

To keep the control plane informed of node health without overloading the database, Kubernetes uses the **Lease API** (`coordination.k8s.io`). (For the role of the Node Controller inside the `kube-controller-manager` which monitors these lease objects, see [Module 02: Cluster Architecture & Control Plane Components](02_cluster_architecture_and_components.md#2-control-plane-components-deep-dive)).

### A. Heartbeat Mechanism
* **Lease Objects:** Every node gets a lightweight `Lease` object in the `kube-node-lease` namespace. The `kubelet` pings (renews) this lease every **10 seconds**.
* **NodeStatus Updates:** The `kubelet` only sends a full, heavy `NodeStatus` object (containing large lists of images, hardware capacities, and conditions) when a status change occurs, or every **5 minutes** by default.

### B. Failure Detection & Eviction (Timer A vs. Timer B)
1. **Timer A (Node Lease Expiry):**
   * **Interval:** 40 seconds.
   * **Action:** If the `kubelet` fails to renew its Lease for 40s, the Control Plane's Node Controller flips the node's condition to `Ready: Unknown` or `Ready: False`.
2. **Timer B (Pod Eviction Timeout):**
   * **Interval:** 5 minutes (default, controlled by `--pod-eviction-timeout`).
   * **Action:** If the node remains unresponsive after 5 minutes, the Node Controller deletes the Pod objects assigned to that node, triggering the scheduler to recreate them on healthy nodes.

---

## 4. Resource Enforcement: Linux `cgroups` & Drivers

Kubernetes does not isolate container resources. It commands the container runtime (e.g., `containerd`) to use Linux kernel features:
* **Namespaces:** Provide boundary walls (isolating process lists, networks, mount points).
* **Control Groups (`cgroups`):** Provide resource ceilings (throttling CPU, capping Memory).

### A. Cgroup Drivers (A Critical CKA Trap)
To interface with the kernel's cgroups, the container runtime and `kubelet` must use a driver.
* **`cgroupfs`:** The driver writes directly to `/sys/fs/cgroup`.
* **`systemd`:** The driver uses systemd's cgroup management API.
> [!IMPORTANT]
> **The Golden Rule:** The `kubelet` and the container runtime MUST use the exact same Cgroup driver (modern default is `systemd`). If there is a mismatch, the `kubelet` will crash or behave erratically under load, and the node will drop to `NotReady`.

### B. Cgroups v1 vs. Cgroups v2
* **Cgroups v1:** Legacy. Uses a multi-hierarchy system (separate trees for memory, CPU, disk I/O). Makes resource correlation difficult.
* **Cgroups v2:** Unified hierarchy (single tree managing all resource types together). Offers finer-grained resource monitoring and better memory-pressure tracking (PSI), fully supported since Kubernetes `v1.25`.

---

## 5. Kubelet Evictions & Quality of Service (QoS)

If a node runs out of physical resources (crossing hard eviction thresholds like memory < 100MiB), the `kubelet` sets `MemoryPressure: True` (stopping new schedules) and starts killing existing Pods to save the operating system from crashing. It prioritizes which Pod to kill based on its **QoS Class**. For how these eviction actions trigger container lifecycle restarts and workload replacement, see [Module 04: Workload Lifecycle & Self-Healing](04_workload_lifecycle_and_healing.md).

```plaintext
Eviction Priority:
[ HIGH RISK ]   BestEffort  --> No resource requests or limits specified.
     |          Burstable   --> Requests are set, but limits are higher/unset.
[ LOW RISK  ]   Guaranteed  --> Requests and limits are set to identical values.
```

### A. `BestEffort` (First to Die)
* **Definition:** No `requests` or `limits` are configured on any container.
* **Eviction Policy:** Reclaims resources here first.

### B. `Burstable` (Second to Die)
* **Definition:** `requests` are set, but `limits` are higher or not specified.
* **Eviction Policy:** Evicted next if no `BestEffort` pods remain.

### C. `Guaranteed` (Last Resort)
* **Definition:** Every container has matching `requests` and `limits` for both CPU and Memory.
* **Eviction Policy:** Only terminated as a last resort to protect the system.

---

## 6. Control Plane to Node Communication

Cluster network traffic follows distinct secure pathways:

### A. Node to Control Plane (Hub-and-Spoke)
* **Initiator:** The worker node components (`kubelet`, `kube-proxy`) open outbound connections to the `kube-apiserver` port (`6443`).
* **Security:** Secured using mutual TLS (mTLS) with client certificates.

### B. Control Plane to Node (Reaching Out)
* **Initiator:** The `kube-apiserver` acts as the client, connecting outbound to the `kubelet` API server (port `10250`) on the worker node.
* **Triggers:** Interactive administrative tasks:
  * `kubectl logs`: Streams logs from the container.
  * `kubectl exec`: Runs commands inside the container.
  * `kubectl port-forward`: Binds a local port to a container port.
* **Konnectivity Tunnel:** In highly secure firewalled networks, direct control-plane-to-node routing is blocked. The cluster uses **Konnectivity** (an SSH reverse-tunnel manager) where nodes maintain long-lived outbound connections, and the api-server routes interactive traffic backward through these tunnels.

---

## 🛠️ Practical Proof of Concept (PoC)

### Target Scenario
We will spin up a local cluster, explore Lease heartbeat objects, deploy 3 Pods corresponding to the 3 different QoS classes, inspect their fields, and query the node resource specifications.

### Step-by-Step Guided Steps

1. **Verify or Re-create Cluster:**
   If you do not have a cluster, provision a quick single-node cluster:
   ```bash
   kind create cluster --name cka-node-poc
   ```

2. **Inspect Node Lease Objects:**
   Query the lightweight lease objects that represent the 10-second heartbeats:
   ```bash
   kubectl get leases -n kube-node-lease
   ```
   Describe the lease of your master/worker node:
   ```bash
   kubectl describe lease cka-node-poc-control-plane -n kube-node-lease
   ```
   Note the `RenewTime` and `Duration` fields. Try running this multiple times and watch the `RenewTime` update every 10 seconds.

3. **Check Capacity vs. Allocatable Resource Math:**
   Inspect the resource allocations on the node:
   ```bash
   kubectl describe node cka-node-poc-control-plane | grep -A 8 -E "Capacity|Allocatable"
   ```

4. **Create Manifests for the 3 QoS Classes:**
   Generate a single file with three pods:
   * `qos-guaranteed`: Requests and limits match.
   * `qos-burstable`: Request is lower than limit.
   * `qos-besteffort`: No limits/requests.

   ```yaml
   cat <<EOF > qos-pods.yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: qos-guaranteed
   spec:
     containers:
     - name: web
       image: nginx
       resources:
         limits:
           memory: "128Mi"
           cpu: "500m"
         requests:
           memory: "128Mi"
           cpu: "500m"
   ---
   apiVersion: v1
   kind: Pod
   metadata:
     name: qos-burstable
   spec:
     containers:
     - name: web
       image: nginx
       resources:
         limits:
           memory: "256Mi"
         requests:
           memory: "128Mi"
   ---
   apiVersion: v1
   kind: Pod
   metadata:
     name: qos-besteffort
   spec:
     containers:
     - name: web
       image: nginx
   EOF
   ```

5. **Apply and Verify QoS Classes:**
   Deploy the pods:
   ```bash
   kubectl apply -f qos-pods.yaml
   ```
   Query the auto-calculated QoS classes:
   ```bash
   kubectl get pods qos-guaranteed qos-burstable qos-besteffort -o custom-columns=NAME:.metadata.name,QOS:.status.qosClass
   ```
   Verify the output matches:
   ```plaintext
   NAME             QOS
   qos-guaranteed   Guaranteed
   qos-burstable    Burstable
   qos-besteffort   BestEffort
   ```

6. **Clean up Resources:**
   Delete the pods and cluster:
   ```bash
   kubectl delete -f qos-pods.yaml
   rm qos-pods.yaml
   kind delete cluster --name cka-node-poc
   ```

---

## 🔗 Related Modules
- [Module 02: Cluster Architecture & Control Plane Components](02_cluster_architecture_and_components.md) - Outlines the role of the control plane (scheduler, controller-manager, API server) in coordinating with Kubelets.
- [Module 04: Workload Lifecycle & Self-Healing](04_workload_lifecycle_and_healing.md) - Details how eviction triggers restarts and replication controller healing.
- [Module 05: Containers, Runtimes, and Lifecycle Management](05_containers_runtimes_and_lifecycle.md) - Covers container image pull mechanics, the Container Runtime Interface (CRI), lifecycle hooks, init containers, sidecars, and ephemeral containers.
