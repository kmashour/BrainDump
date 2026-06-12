---
obsidianUIMode: preview
class: study-guide
tier: main-note
tags:
  - kubernetes/study-guide
  - cka/syllabus-mapping
against: []
---

# 🗺️ CKA Conceptual Study Roadmap

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[0-Index - Kubernetes|☸️ Kubernetes MOC]] > **CKA Study Roadmap**

This roadmap outlines the exact step-by-step sequence you should follow when studying the **Main Notes** for the CKA exam. It aligns the atomic concept notes and deeper-dive files with the progression of the Mumshad CKA course.

---

## 🔀 Step-by-Step Learning Path

### 🏛️ Phase 1: Core Concepts & Pod Foundations
*Understand the control plane architecture, basic resource structures, and essential CLI tools.*

1. **Control Plane Core Components:**
   * [[kube-apiserver]] - The gateway of all API requests.
   * [[kube-controller-manager]] - The control-loop manager.
   * [[kube-scheduler]] - The placement algorithm coordinator.
   * [[etcd]] - The state storage engine.
   * [[node]] - The worker host abstraction.
   * [[pod]] - The smallest deployable unit.
   * [[Reconciliation Loop Mechanics]] - How controllers drive actual state to desired state.

2. **API & CLI Basics:**
   * [[kubectl]] - The primary CLI client.
   * [[Kubeconfig Anatomy]] - Authentication profiles and contexts.
   * [[API Discovery and explanation]] - API groups (`/apis/apps/v1`, etc.) and discovery.
   * [[label]] - Key-value metadata for selectors.
   * [[annotation]] - Non-identifying metadata.
   * [[namespace]] - Logical segregation boundaries.

---

### 🎯 Phase 2: Scheduling & Resource Limits
*Control how Pods are placed onto nodes and how physical resources are allocated.*

1. **Node Placement Policies:**
   * [[kube-scheduler - Node Selector and Affinity]] - Attracting pods using labels.
   * [[kube-scheduler - Taints and Tolerations]] - Repelling pods from specific nodes.
   * [[kube-scheduler - Priority Preemption and Topology Spread]] - Pod priority, preemption, and high-availability spreading.
   * [[Manual Node Assignment]] - Allocating pods by editing specs directly.
   * [[Static nodeName Scheduling Bypass]] - Bypassing the scheduler completely.

2. **Scheduling Internals:**
   * [[kube-scheduler-deeper]] - Synchronous scheduling vs. asynchronous binding cycle.
   * [[Scheduler Profiles]] - Configuring multiple profiles in a single process.
   * [[Multiple Custom Schedulers]] - Running custom scheduler binaries with RBAC.

3. **Resource Allocation & Constraints:**
   * [[Quality of Service (QoS) Classes]] - Guaranteed, Burstable, and BestEffort tiers.
   * [[Node Allocatable Math]] - Calculating capacity pool available for user workloads.
   * [[Configuring kube-reserved and system-reserved limits]] - Reserving resources for OS/Kubelet.
   * [[limitrange]] - Default limits and validation rules per namespace.
   * [[resourcequota]] - Total resource consumption restrictions per namespace.

---

### 📦 Phase 3: Application Lifecycle & Configuration
*Manage rolling upgrades, project-level configurations, and advanced container lifecycles.*

1. **Workload Controllers:**
   * [[deployment]] - Declarative rolling updates and replicas management.
   * [[deployment - Rolling Update and Rollback Strategy]] - `maxSurge` / `maxUnavailable` parameters.
   * [[replicaset]] - Pod replica guarantees.
   * [[replicaset - MatchExpressions and Thrashing]] - Resolving controller overlap.
   * [[daemonset]] - Placing copy of a Pod on every qualifying node.

2. **Configuration & Secrets:**
   * [[configmap]] - Projecting non-sensitive key-value configurations.
   * [[configmap - Injection and Volume Mounts]] - File projections vs. env vars.
   * [[secret]] - Managing base64-encoded sensitive keys.
   * [[secret - Encryption at Rest and Ingestion]] - Enforcing encryption providers in KMS.
   * [[serviceaccount]] - Identity passport for system processes inside pods.

3. **Container Lifecycles:**
   * [[Init Containers]] - Sequential pre-setup tasks before main container boots.
   * [[Native Sidecars (v1.29+)]] - Restart-resistant background utility containers.
   * [[Container Lifecycle Hooks (postStart preStop)]] - Executing setup and teardown commands.
   * [[Health Probes (liveness readiness startup)]] - Checking container health.

---

### 🥾 Phase 4: Cluster Operations & Maintenance
*Handle node evacuations, system updates, and etcd backups.*

1. **Node Maintenance:**
   * [[Node Conditions & Lifecycle]] - Node Heartbeats and status flags.
   * [[Node Eviction Grace Periods]] - Scheduling grace timers when a node fails.
   * [[Node Conditions and Hard Eviction Thresholds]] - Out-of-resource eviction behavior.
   * [[Node Leases (Heartbeat Mechanism)]] - Reduced API load using the Lease API.

2. **Control Plane Operations:**
   * [[etcd Backup and Restore]] - Taking snapshots and restoring etcd data directories.
   * [[etcd TLS certificate configurations]] - Mapping TLS cert keys to etcd commands.
   * [[etcd network ports]] - Port configurations (`2379`, `2380`).
   * [[Raft Consensus]] - Leader elections and commit logging.
   * [[Raft Quorum Rules]] - Calculating quorum math: $(N/2) + 1$.

---

### 🛡️ Phase 5: Security & Networking
*Enforce access control policies, service routing, and network isolation.*

1. **API Security & RBAC:**
   * [[api-security]] - Authentication, Authorization, and Admission phases.
   * [[api-security - Defenses]] - Hardening API server endpoints.
   * [[rbac]] - Creating Role, ClusterRole, RoleBinding, and ClusterRoleBinding resources.
   * [[Node Bootstrap and TLS Bootstrapping]] - Secure kubelet client cert rotation.
   * [[Admission Controllers]] - Intercepting requests after authorization.
   * [[Admission Webhooks - Mutating and Validating]] - Extending admission logic dynamically.
   * [[pod-security-admission]] - Built-in admission standards.

2. **Service Routing & CoreDNS:**
   * [[service]] - Exposing pods internally or externally.
   * [[service - EndpointSlices and Topology routing]] - Scalable endpoints backends.
   * [[service - Source IP and Pod Termination Lifecycle]] - Client IP preserving.

3. **Ingress & Policy Enforcement:**
   * [[ingress]] - Layer 7 HTTP/HTTPS reverse-proxy routing.
   * [[gateway-api]] - Role-oriented modern traffic routing.
   * [[networkpolicy]] - Enforcing firewall rules between pods.

---

### 🕵️ Phase 6: Troubleshooting & Diagnostics
*Diagnose runtime engines, system logs, and debug failing containers.*

1. **Host-Level Container Runtimes:**
   * [[container-runtime]] - Enforcing container isolation.
   * [[container-runtime-deeper]] - CRI (gRPC) communication lifecycle.
   * [[containerd-shim mechanics]] - Decoupling container execution from runc.
   * [[CRI Socket Communication]] - Locating daemon unix sockets.
   * [[Cgroup Drivers systemd vs cgroupfs]] - Host isolations drivers.
   * [[cgroups v1 vs v2]] - Single vs. unified hierarchy trees.
   * [[Pause Container Namespace Holder]] - Holding Linux namespaces.

2. **Debugging Tools:**
   * [[Debugging containerd with ctr and nerdctl]] - Inspecting containerd directly.
   * [[CRI troubleshooting with crictl]] - CLI tool for debugging Kubernetes runtimes.
   * [[Inspecting kubelet systemd service logs]] - Troubleshooting systemd units.

3. **Telemetry & Rescue operations:**
   * [[Debugging with Ephemeral Containers]] - Injecting debugging tools at runtime.
   * [[Force Deletion bypass]] - Bypassing blockages and force deleting resources.
   * [[JSONPath and custom-columns filters]] - Fetching telemetry.
