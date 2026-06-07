# Inflow Q&A: Node Heartbeats, Eviction Taints, and API Concurrency

This document consolidates Q&A regarding Kubelet heartbeat failures, eviction taints, default tolerations, and API concurrency mechanics.

---

## Q1: If a Kubelet stops sending heartbeats for 40 seconds, what state is the node put into?

### Answer:
The node is put into both **`NoSchedule`** and **`NoExecute`** taint states, but existing running workloads experience **`NoExecute` with toleration seconds**.

1. **Heartbeat Loss (40 Seconds)**:
   * The Kubelet updates its `Lease` object in the `kube-node-lease` namespace every 10 seconds.
   * If it fails to do so for **40 seconds** (`node-lease-duration-seconds` default), the Node Lifecycle Controller marks the node condition as `Ready: Unknown`.
2. **Automatic Taints Applied**:
   * The Node Controller appends both of these taints to the node's `spec.taints` array:
     * `node.kubernetes.io/unreachable:NoSchedule`
     - `node.kubernetes.io/unreachable:NoExecute`
3. **Default Eviction Toleration**:
   * All pods automatically receive default tolerations during admission:
     ```yaml
     tolerations:
     - key: "node.kubernetes.io/unreachable"
       operator: "Exists"
       effect: "NoExecute"
       tolerationSeconds: 300
     ```
   * As a result, running pods do not get evicted immediately. They remain on the unreachable node for **300 seconds (5 minutes)** before being rescheduled.

---

## Q2: Why are there two separate taints (`not-ready` vs. `unreachable`) with the same `NoExecute` effect?

### Answer:
They represent two completely different physical failure modes of the node:
1. **`node.kubernetes.io/not-ready` (Unhealthy but Alive)**:
   * The Kubelet **is communicating** with the control plane, but has flagged itself as unhealthy (e.g., due to `PIDPressure`, `DiskPressure`, or runtime crashes).
2. **`node.kubernetes.io/unreachable` (Dead or Network Partitioned)**:
   * The Kubelet **is not communicating** at all. The control plane cannot tell if the node crashed or if it is running but partitioned from the network.

### Rationale for Separation:
Keeping them separate allows administrators to write fine-grained policies. 
* *Example:* For a stateless web server, you can evict immediately for both (`tolerationSeconds: 10`).
* *Example:* For a stateful database (like Postgres), you might evict quickly on `not-ready` (where you know the host is alive but broken), but wait 30 minutes on `unreachable` to prevent a network partition from launching a second database replica writing to the same storage (avoiding split-brain data corruption).

---

## Q3: Why does the Node Lifecycle Controller use `PATCH` instead of `PUT` or `POST`?

### Answer:
To prevent **distributed concurrency conflicts** under Optimistic Concurrency Control (OCC).

* **The PUT Conflict**: A `PUT` request replaces the entire object and requires matching `resourceVersion`. If the Node Controller reads the Node object, appends a taint in memory, and sends a `PUT`, the request will fail with a `409 Conflict` if the Kubelet updated its node status (e.g., CPU/RAM metrics) in the same millisecond.
* **The PATCH Solution**: A `PATCH` request sends only the specific delta (e.g., adding a taint to `spec.taints`). The API Server applies this update atomically in `etcd`, resolving conflicts automatically even if status updates occur concurrently.

---

## Q4: How are tolerations evaluated when `effect` is omitted, and how are `NoSchedule` vs. `NoExecute` resolved?

### Answer:
1. **Omitted Effect**:
   * If a toleration omits the `effect` field, it acts as a wildcard and matches **all effects** (`NoSchedule`, `PreferNoSchedule`, and `NoExecute`) for that key.
2. **Additive Evaluation**:
   * If a node is tainted with both `NoSchedule` and `NoExecute`, the Pod must tolerate **both** to be scheduled on it.
   * If the Pod is already running when the node goes offline, the `NoSchedule` taint does not affect it (since `NoSchedule` only blocks new scheduling). The pod only needs to match the `NoExecute` taint to remain running during the `tolerationSeconds` window.

---

## Q5: Does specifying `tolerationSeconds` for a `NoSchedule` taint effect have any effect?

### Answer:
No. **`tolerationSeconds` has absolutely no effect when used with the `NoSchedule` (or `PreferNoSchedule`) taint effects.**

* **`NoExecute`**: Eviction trigger. It evicts running pods. It requires `tolerationSeconds` to define the countdown timer before eviction occurs.
* **`NoSchedule`**: Scheduling filter. It only blocks *new* pods from being scheduled on the node. It is a binary evaluation completed by the scheduler during placement and does not affect already running pods. Consequently, a time delay (`tolerationSeconds`) is ignored.
