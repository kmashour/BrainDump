# 🚀 Advanced Kubernetes Playbook: Walkthrough Playbook

This document contains the complete walkthrough, problems, hints, and step-by-step solutions for all **50 tasks** in the Advanced Kubernetes interactive practice engine (25 Study Q&As and 25 Environment Scenarios). Use this guide to study advanced operator paradigms, admission webhooks, and CKS security standards alongside practicing them via `./gold.sh`.

## 📌 Navigation Table of Contents
- [Advanced API & Extensions / Webhooks](#advanced-api-and-extensions---webhooks)
- [CKS Security & Container Isolation](#cks-security-and-container-isolation)
- [Advanced Services & Routing (Gateway API)](#advanced-services-and-routing-gateway-api)
- [Advanced Workloads & Scheduling](#advanced-workloads-and-scheduling)
- [Advanced Cluster Administration](#advanced-cluster-administration)

---

## Advanced API & Extensions / Webhooks
This section covers all tasks representing Advanced API & Extensions / Webhooks.

### 📝 Conceptual Study Q&As (0 Tasks)
These tasks test your core knowledge of advanced patterns, structures, and systems details.

### 🔬 Hands-on Environment Scenarios (0 Tasks)
These tasks require access to the shared KinD cluster (`./gold.sh`). They inject advanced challenges that you must diagnose and resolve.


---

## CKS Security & Container Isolation
This section covers all tasks representing CKS Security & Container Isolation.

### 📝 Conceptual Study Q&As (0 Tasks)
These tasks test your core knowledge of advanced patterns, structures, and systems details.

### 🔬 Hands-on Environment Scenarios (0 Tasks)
These tasks require access to the shared KinD cluster (`./gold.sh`). They inject advanced challenges that you must diagnose and resolve.


---

## Advanced Services & Routing (Gateway API)
This section covers all tasks representing Advanced Services & Routing (Gateway API).

### 📝 Conceptual Study Q&As (0 Tasks)
These tasks test your core knowledge of advanced patterns, structures, and systems details.

### 🔬 Hands-on Environment Scenarios (0 Tasks)
These tasks require access to the shared KinD cluster (`./gold.sh`). They inject advanced challenges that you must diagnose and resolve.


---

## Advanced Workloads & Scheduling
This section covers all tasks representing Advanced Workloads & Scheduling.

### 📝 Conceptual Study Q&As (3 Tasks)
These tasks test your core knowledge of advanced patterns, structures, and systems details.

#### 🔍 AS-14: Explain PodTopologySpreadConstraints and its key fields....
**Question:**
Explain PodTopologySpreadConstraints and its key fields.

**Answer:**
```
It distributes pods evenly across failure domains (nodes, zones, regions) to ensure high availability. Key fields:
- `maxSkew`: The maximum permissible difference in pod counts between any two topology domains.
- `topologyKey`: The node label key representing the topology domain (e.g., `topology.kubernetes.io/zone`).
- `whenUnsatisfiable`: `DoNotSchedule` (hard rule) or `ScheduleAnyway` (soft rule).
- `labelSelector`: Matches pods to count for spreading.
```

#### 🔍 AS-15: Describe PriorityClasses, Pod Preemption, and how the scheduler resolves resourc...
**Question:**
Describe PriorityClasses, Pod Preemption, and how the scheduler resolves resource conflicts.

**Answer:**
```
A PriorityClass assigns a weight to pods. If a high-priority pod is scheduled but no nodes have enough resource capacity, the scheduler triggers Preemption. It scans nodes to identify low-priority pods that can be evicted. The scheduler evicts the victims, creating space, and schedules the high-priority pod on that node.
```

#### 🔍 AS-23: What is the purpose of kube-scheduler framework extension points?...
**Question:**
What is the purpose of kube-scheduler framework extension points?

**Answer:**
```
The scheduling framework divides scheduling into sequential phases with plugin extension points: QueueSort (orders queue), PreFilter/Filter (prunes nodes), PostFilter (preempts), PreScore/Score (ranks nodes), Reserve (reserves resources), Permit (delays bind), and PreBind/Bind (applies node association in API). Developers write plugins hooking into these stages to customize scheduling behavior.
```

### 🔬 Hands-on Environment Scenarios (2 Tasks)
These tasks require access to the shared KinD cluster (`./gold.sh`). They inject advanced challenges that you must diagnose and resolve.

#### 🛠️ AE-14: Configure PodTopologySpreadConstraints
**Problem Statement:**
Create deployment 'topology-spread-deploy' in default namespace with topologySpreadConstraints configured to spread replicas across nodes (topologyKey: kubernetes.io/hostname) with maxSkew 1.

**💡 Hint:**
> Add spec.template.spec.topologySpreadConstraints block to deployment YAML.

**Setup Injection Command:**
```bash
kubectl delete deployment topology-spread-deploy --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get deploy topology-spread-deploy -o jsonpath='{.spec.template.spec.topologySpreadConstraints[0].topologyKey}' | grep -w 'kubernetes.io/hostname'
```
**🟢 Step-by-Step Solution:**
1. Apply manifest with topologySpreadConstraints config.

---
#### 🛠️ AE-15: Configure PriorityClasses & Preemption
**Problem Statement:**
Create a PriorityClass named 'high-priority' with value 1000000 and preemptionPolicy set to PreemptLowerPriority.

**💡 Hint:**
> Apply PriorityClass manifest specifying value and preemptionPolicy.

**Setup Injection Command:**
```bash
kubectl delete priorityclass high-priority --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get priorityclass high-priority -o jsonpath='{.value}' | grep -w '1000000'
```
**🟢 Step-by-Step Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false
description: "High priority class for testing preemption."
EOF

---

---

## Advanced Cluster Administration
This section covers all tasks representing Advanced Cluster Administration.

### 📝 Conceptual Study Q&As (5 Tasks)
These tasks test your core knowledge of advanced patterns, structures, and systems details.

#### 🔍 AS-16: How does Coordinated Leader Election work in Kubernetes using the Lease API?...
**Question:**
How does Coordinated Leader Election work in Kubernetes using the Lease API?

**Answer:**
```
Components (like custom operators or controllers) create a `Lease` object (in the `coordination.k8s.io` group) to act as a lock. The active leader acquires the Lease and must periodically renew it (e.g., every 10 seconds). Backup instances watch the Lease. If the leader fails to renew before the lease expires, backup nodes attempt to write their ID to the Lease to claim leadership.
```

#### 🔍 AS-17: What is Dynamic Resource Allocation (DRA), and how does it improve hardware devi...
**Question:**
What is Dynamic Resource Allocation (DRA), and how does it improve hardware device scheduling?

**Answer:**
```
DRA replaces the legacy resource limit model for specialized hardware (like GPUs). It models hardware devices using ResourceClass and ResourceClaim templates. It allows pods to claim devices dynamically, configure driver-specific parameters, and share resources between containers in a pod, providing more fine-grained control than standard resource requests.
```

#### 🔍 AS-21: How does systemd journald log management interact with Kubelet's container stdou...
**Question:**
How does systemd journald log management interact with Kubelet's container stdout?

**Answer:**
```
The container runtime intercepts stdout/stderr streams from the container process and writes them to local log files (typically JSON or CRI format in `/var/log/pods/`). If configured to use the journald logging driver, the runtime redirects these streams to the host systemd-journald service, allowing journalctl to index, query, and rate-limit logs at the node level.
```

#### 🔍 AS-22: What are Device Plugins, and how do they expose vendor-specific hardware to the ...
**Question:**
What are Device Plugins, and how do they expose vendor-specific hardware to the kubelet?

**Answer:**
```
Device Plugins are standalone daemons (typically running as DaemonSets) that register with Kubelet over gRPC. They advertise vendor-specific local resources (e.g. nvidia.com/gpu) to Kubelet. When a pod requesting that resource schedules, Kubelet calls the Device Plugin's Allocate() RPC endpoint to configure host paths, environment variables, or mount devices into the container interface.
```

#### 🔍 AS-24: Describe ETCD cluster Raft consensus quorum rules and the consequences of networ...
**Question:**
Describe ETCD cluster Raft consensus quorum rules and the consequences of network partitions.

**Answer:**
```
ETCD uses the Raft consensus protocol. To make writes, a cluster needs a quorum of active members, defined as `(N/2) + 1` where N is the total members. If a network partition occurs, the side containing a quorum continues to operate. The partitioned minority side fails to achieve consensus and blocks all incoming writes, preventing split-brain database states.
```

### 🔬 Hands-on Environment Scenarios (3 Tasks)
These tasks require access to the shared KinD cluster (`./gold.sh`). They inject advanced challenges that you must diagnose and resolve.

#### 🛠️ AE-16: Configure Coordinated Lease lock
**Problem Statement:**
Create a Lease named 'operator-lock' in namespace 'default' representing coordination lock for an operator leader election.

**💡 Hint:**
> Apply Lease resource manifest under apiGroup coordination.k8s.io.

**Setup Injection Command:**
```bash
kubectl delete lease operator-lock --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get lease operator-lock
```
**🟢 Step-by-Step Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: coordination.k8s.io/v1
kind: Lease
metadata:
  name: operator-lock
spec:
  holderIdentity: operator-instance-1
  leaseDurationSeconds: 15
  acquireTime: "2026-06-10T12:00:00.000000Z"
  renewTime: "2026-06-10T12:00:10.000000Z"
EOF

---
#### 🛠️ AE-18: Create Dynamic ResourceClass Claim template
**Problem Statement:**
Create a ResourceClass named 'gpu-class' under apiGroup resource.k8s.io/v1alpha2.

**💡 Hint:**
> Apply a ResourceClass manifest (Note: api version resource.k8s.io/v1alpha2 or resource.k8s.io/v1alpha3).

**Setup Injection Command:**
```bash
kubectl delete resourceclass gpu-class --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get resourceclass gpu-class
```
**🟢 Step-by-Step Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: resource.k8s.io/v1alpha2
kind: ResourceClass
metadata:
  name: gpu-class
driverName: mock-gpu-driver
EOF

---
#### 🛠️ AE-21: Expose Control Plane Metrics scrape target
**Problem Statement:**
Create a service named 'kube-scheduler-metrics' in namespace 'kube-system' exposing scheduler port 10259.

**💡 Hint:**
> Define a service in kube-system namespace mapping port 10259.

**Setup Injection Command:**
```bash
kubectl delete service kube-scheduler-metrics -n kube-system --ignore-not-found=true
```
**Verification check script:**
```bash
kubectl get service kube-scheduler-metrics -n kube-system -o jsonpath='{.spec.ports[0].port}' | grep -w '10259'
```
**🟢 Step-by-Step Solution:**
1. Apply manifest:
kubectl apply -f - <<EOF
apiVersion: v1
kind: Service
metadata:
  name: kube-scheduler-metrics
  namespace: kube-system
spec:
  selector:
    component: kube-scheduler
  ports:
  - port: 10259
    targetPort: 10259
EOF

---

---
