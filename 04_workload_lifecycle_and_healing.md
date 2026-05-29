# Module 04: Workload Lifecycle & Self-Healing

This module covers the core self-healing algorithms in Kubernetes, automated application health checks (Probes), API object relationships, and the garbage collection mechanisms running on both the control plane and individual nodes.

---

## 1. The Four Pillars of Self-Healing

Kubernetes is built to react to failures at different structural levels. Failures are handled through one of four mechanisms:

### A. Restart (Local Container Healing)
* **Component:** `kubelet`.
* **Action:** If a container process exits or crashes, the local `kubelet` restarts the container inside the existing Pod. (See [Module 03: Node Mechanics & Resource Limits](03_node_mechanics_and_resource_limits.md#4-resource-enforcement-linux-cgroups-drivers) for how Kubelet manages local container runtimes and cgroups).
* **Mechanism:** Checks the Pod's `restartPolicy` (`Always`, `OnFailure`, `Never`). Uses an exponential backoff delay (from 10s up to 5 minutes) to avoid thrashing, entering the `CrashLoopBackOff` state.
* **Result:** Pod name, IP address, and node assignment stay identical. Only the `RESTARTS` count increments.

### B. Replace (Workload Recovery)
* **Component:** Controllers (`kube-controller-manager`). (For Control Plane details, see [Module 02: Cluster Architecture & Control Plane Components](02_cluster_architecture_and_components.md#2-control-plane-components-deep-dive)).
* **Action:** Pods are completely immutable. If a Pod becomes corrupted or fails its startup sequence, the system terminates the bad Pod and builds a clean replacement from the original manifest.

### C. Replicate (Scale Enforcement)
* **Component:** `kube-controller-manager` (specifically the ReplicaSet/Deployment controller loops).
* **Action:** Constantly checks if the number of running Pods matches the desired replica count. If a user deletes a Pod, the controller detects the mismatch and immediately creates a new Pod.

### D. Reschedule (Infrastructure Failure Recovery)
* **Component:** `kube-controller-manager` (Node Controller) & `kube-scheduler`. (For scheduler algorithms, see [Module 02: Cluster Architecture & Control Plane Components](02_cluster_architecture_and_components.md#2-control-plane-components-deep-dive)).
* **Action:** If a physical server dies, the Node Controller waits out the 5-minute eviction grace period, flags the node as dead, deletes the Pods on it, and the `kube-scheduler` places replacement Pods onto healthy nodes. (For node Lease objects and eviction timers, see [Module 03: Node Mechanics & Resource Limits](03_node_mechanics_and_resource_limits.md#3-node-heartbeats-the-lease-api)).

---

## 2. Automated Health Checks: Probes

Probes are health checks executed periodically by the local `kubelet` on a container.

```yaml
spec:
  containers:
  - name: app
    image: nginx
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 3
      periodSeconds: 5
```

### A. Liveness Probe
* **Purpose:** Detects if the application is deadlocked or frozen.
* **Action on Failure:** The `kubelet` terminates the container and triggers a container restart (according to `restartPolicy`).

### B. Readiness Probe
* **Purpose:** Detects if the container is ready to accept network traffic (e.g., has finished loading database schemas).
* **Action on Failure:** The Pod is kept running, but its IP address is removed from all matching Service Endpoints, isolating the Pod from client traffic until the probe succeeds.

### C. Startup Probe
* **Purpose:** Protects slow-starting legacy applications.
* **Action on Failure:** Disables liveness and readiness checks until the startup probe succeeds (up to a configured threshold). If the startup probe fails to succeed within the threshold, the container is killed and restarted.

---

## 3. Garbage Collection (GC)

Garbage collection runs at two levels: the Control Plane (database cleanup) and the Worker Nodes (disk cleanup).

### A. API Object Cleanup (Control Plane)
Kubernetes tracks parent-child relationships using `metadata.ownerReferences` (e.g., a ReplicaSet owns Pods). When a parent is deleted, the garbage collector handles the children using **Cascading Deletion**:
1. **Background (Default):** The parent is deleted instantly. The GC then cleans up the children in the background.
2. **Foreground:** The parent enters a "deletion in progress" state. The GC deletes all children first. Once the children are gone, the parent is deleted.
   ```bash
   kubectl delete deployment <name> --cascade=foreground
   ```
3. **Orphan:** The parent is deleted, but the children are spared. They become "orphans" and keep running with their owner references removed.
   ```bash
   kubectl delete deployment <name> --cascade=orphan
   ```

### B. Node Cleanup (Kubelet GC)
The `kubelet` garbage collector runs locally to keep the worker node's disk from filling up:
1. **Container GC:** Automatically purges dead containers and their logs once they are no longer needed for troubleshooting.
2. **Image GC:** Monitors node disk usage. Triggers cleanups based on thresholds:
   * **`HighThresholdPercent` (Default: 85%):** If disk usage hits this mark, image GC starts deleting the oldest, unused container images.
   * **`LowThresholdPercent` (Default: 80%):** Image GC continues deleting until disk usage drops below this mark.
> [!WARNING]
> If the disk usage increases faster than image GC can delete, the node condition flips to `DiskPressure: True` (see Node Conditions in [Module 03: Node Mechanics & Resource Limits](03_node_mechanics_and_resource_limits.md#b-conditions)), and scheduling halts.

---

## 🛠️ Practical Proof of Concept (PoC)

### Target Scenario
We will deploy a Pod with a failing livenessProbe to witness local healing, a Pod with a failing readinessProbe to observe traffic routing isolation, and perform cascading deletions to verify background vs. orphan garbage collection.

### Step-by-Step Guided Steps

1. **Verify or Provision Cluster:**
   ```bash
   kind create cluster --name cka-healing-poc
   ```

2. **Test Liveness Probe (Local Restart Healing):**
   Create a Pod that fails its liveness probe. The app container creates a `/tmp/healthy` file and deletes it after 30 seconds. The liveness probe checks this file.
   ```yaml
   cat <<EOF > liveness-poc.yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: liveness-pod
   spec:
     containers:
     - name: app
       image: busybox
       args:
       - /bin/sh
       - -c
       - touch /tmp/healthy; sleep 30; rm -rf /tmp/healthy; sleep 600
       livenessProbe:
         exec:
           command:
           - cat
           - /tmp/healthy
         initialDelaySeconds: 5
         periodSeconds: 5
   EOF
   ```
   Apply the Pod:
   ```bash
   kubectl apply -f liveness-poc.yaml
   ```
   Monitor the Pod's lifecycle in real-time. Notice the restarts increase after 30-40 seconds:
   ```bash
   kubectl get pod liveness-pod -w
   ```
   Inspect the events to see the liveness probe failure:
   ```bash
   kubectl describe pod liveness-pod | grep -E "Liveness|Restart"
   ```

3. **Test Readiness Probe (Traffic Routing Isolation):**
   Create a Pod with a readiness probe checking for a `/tmp/ready` file, which does not exist:
   ```yaml
   cat <<EOF > readiness-poc.yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: readiness-pod
     labels:
       app: web
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: web-service
   spec:
     selector:
       app: web
     ports:
     - port: 80
       targetPort: 80
   EOF
   ```
   Apply the configuration:
   ```bash
   kubectl apply -f readiness-poc.yaml
   ```
   Now update the Pod definition to include a readiness probe looking for `/tmp/ready`:
   ```yaml
   cat <<EOF > readiness-pod-probe.yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: readiness-pod
     labels:
       app: web
   spec:
     containers:
     - name: app
       image: nginx
       readinessProbe:
         exec:
           command:
           - cat
           - /tmp/ready
         initialDelaySeconds: 3
         periodSeconds: 3
   EOF
   ```
   Apply the probe update (requires recreating or replacing the pod):
   ```bash
   kubectl replace --force -f readiness-pod-probe.yaml
   ```
   Check the Pod readiness status:
   ```bash
   kubectl get pod readiness-pod
   ```
   It will show `0/1 READY` because the `/tmp/ready` file is missing.
   Now, check if the Service has registered the Pod's IP as an Endpoint:
   ```bash
   kubectl get endpoints web-service
   ```
   Notice that `ENDPOINTS` is blank (or `<none>`). The readiness probe isolated the traffic.
   Create the file inside the container:
   ```bash
   kubectl exec readiness-pod -- touch /tmp/ready
   ```
   Wait 3 seconds and check the status again:
   ```bash
   kubectl get pod readiness-pod
   kubectl get endpoints web-service
   ```
   It now shows `1/1 READY` and the Endpoint contains the Pod's IP!

4. **Test Cascading Garbage Collection (Orphan Mode):**
   Create a small Deployment:
   ```bash
   kubectl create deployment gc-poc --image=nginx --replicas=2
   ```
   Verify the ReplicaSet and Pods are running:
   ```bash
   kubectl get rs,po -l app=gc-poc
   ```
   Now, delete the Deployment but orphan the children:
   ```bash
   kubectl delete deployment gc-poc --cascade=orphan
   ```
   Query the ReplicaSet and Pods again:
   ```bash
   kubectl get rs,po -l app=gc-poc
   ```
   Notice the Deployment is gone, but the ReplicaSet and Pods are still running in the cluster.
   Clean up the orphans:
   ```bash
   kubectl delete rs -l app=gc-poc
   ```

5. **Clean up Resources:**
   ```bash
   kubectl delete -f liveness-poc.yaml
   kubectl delete -f readiness-poc.yaml
   rm liveness-poc.yaml readiness-poc.yaml readiness-pod-probe.yaml
   kind delete cluster --name cka-healing-poc
   ```

---

## 🔗 Related Modules
- [Module 02: Cluster Architecture & Control Plane Components](02_cluster_architecture_and_components.md) - Deep dive into controller reconciliation loops and high availability topologies.
- [Module 03: Node Mechanics & Resource Limits](03_node_mechanics_and_resource_limits.md) - Describes node conditions (`DiskPressure`, etc.), heartbeats via the Lease API, and Kubelet resource eviction policies.
- [Module 05: Containers, Runtimes, and Lifecycle Management](05_containers_runtimes_and_lifecycle.md) - Covers container image pull mechanics, the Container Runtime Interface (CRI), lifecycle hooks, init containers, sidecars, and ephemeral containers.
