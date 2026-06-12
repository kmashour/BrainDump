---
obsidianUIMode: preview
class: study-guide
tier: reference-note
tags:
  - kubernetes/study-guide
  - cka/syllabus-mapping
---

# 🗺️ CKA Study Alignment & Reference Map

**Breadcrumbs:** [[--Index--|🏠 Index]] > [[0-Index - Kubernetes|☸️ Kubernetes Reference MOC]] > **CKA Study Alignment & Reference Map**

This guide helps you bridge the gap between **Mumshad’s CKA Course Syllabus** (which follows a chronological, classroom-friendly sequence) and the **Kubernetes Reference Notes** in your vault (which are structured by **Systems Engineering Domain**). 

By using this map, you can skip the videos, work through the labs, and immediately access the first-principles technical depth required for production-grade Kubernetes troubleshooting.

---

## 🧠 Why is the Reference Index Structured This Way?

Mumshad's course is designed for **pedagogical progression**—introducing high-level abstractions first and teaching concepts step-by-step. The reference index, however, is structured around **architectural layers and production domains** for three primary reasons:

1. **Architectural Cohesion (Anti-Fragmentation):** In Mumshad's course, a single topic like a "Pod" is scattered across several weeks (Core Concepts for basic specs, Scheduling for affinity and resource limits, Application Lifecycle for command args and sidecars, Security for securityContexts). The reference notes centralize these so that when you look at [[0-6_kubernetes_workloads_and_controllers|0-6_kubernetes_workloads_and_controllers.md]], you get the complete picture of how all workloads function.
2. **First-Principles Understanding:** Higher abstractions make sense only when you understand the physical limits beneath them. The reference notes place **Node Mechanics & Container Runtimes (Domain 3)** before scheduling and advanced workloads because a Pod's behavior is defined by cgroups, namespaces, and CRI-level constraints on the worker nodes.
3. **Troubleshooting Orientation:** When a production cluster breaks, it does not fail by "Lecture Module." It fails by system subsystem:
   - *Is it a CNI routing issue?* Go to **Domain 5 (Networking)**.
   - *Is it an RBAC or certificate expiration issue?* Go to **Domain 6 (Security)**.
   - *Is it a kubelet-to-runc communication failure?* Go to **Domain 3 (Runtimes)**.
   Structuring the vault this way builds a mental index optimized for immediate diagnostics.

---

## 🔀 Syllabus-to-Vault Mapping Matrix

| Mumshad CKA Section         | Core Focus                                           | Corresponding Reference Module             | Key Sections to Study                                                                         |                                                                                                      |                                                                                                                            |
| :-------------------------- | :--------------------------------------------------- | :----------------------------------------- | :-------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **1. Core Concepts**        | Cluster Control Plane & Pods                         | [[0-2_cluster_architecture_and_components  | 0-2_cluster_architecture_and_components.md]]<br>[[0-6_kubernetes_workloads_and_controllers    | 0-6_kubernetes_workloads_and_controllers.md]]                                                        | Control Plane components, API Server flow<br>Pod anatomy, CLI speed hacks, and namespaces                                  |
| **2. Scheduling**           | Placement, Affinity, resource limits, DaemonSets     | [[0-3_node_mechanics_and_resource_limits   | 0-3_node_mechanics_and_resource_limits.md]]<br>[[0-13_scheduling_logging_and_lifecycle        | 0-13_scheduling_logging_and_lifecycle.md]]                                                           | CPU/Mem requests & limits, cgroup v1/v2 mapping<br>Taints/Tolerations, Affinity rules, Custom Schedulers                   |
| **3. Logging & Monitoring** | Metrics Server & logging sidecars                    | [[0-13_scheduling_logging_and_lifecycle    | 0-13_scheduling_logging_and_lifecycle.md]]<br>[[0-14_cluster_administration_and_observability | 0-14_cluster_administration_and_observability.md]]                                                   | Logging architectures, tailing stdout/stderr<br>Metrics Server API, CPU/Memory profiling                                   |
| **4. App Lifecycle**        | Rolling updates, ConfigMaps, Secrets, initContainers | [[0-6_kubernetes_workloads_and_controllers | 0-6_kubernetes_workloads_and_controllers.md]]<br>[[0-7_security_and_network_policies          | 0-7_security_and_network_policies.md]]                                                               | Deployment rolling update parameters (`maxSurge`/`maxUnavailable`) & rollbacks<br>ConfigMap/Secret injection (envs, files) |
| **5. Cluster Maintenance**  | Node drain/cordon, upgrades, etcd backup             | [[0-10_maintenance_upgrades_and_etcd       | 0-10_maintenance_upgrades_and_etcd.md]]                                                       | Cordon vs Drain command math, kubeadm upgrades<br>ETCD CTL snapshot backup & restore flow            |                                                                                                                            |
| **6. Security**             | TLS certificates, RBAC, NetworkPolicies              | [[0-7_security_and_network_policies        | 0-7_security_and_network_policies.md]]                                                        | TLS handshake, CA creation, Kubeconfig configs<br>RBAC binding, ServiceAccounts, NetworkPolicy rules |                                                                                                                            |
| **7. Storage**              | PV, PVC, StorageClasses, CSI drivers                 | [[0-8_storage_mechanics_and_csi            | 0-8_storage_mechanics_and_csi.md]]                                                            | CSI architecture, PV bindings, Mount volumes                                                         |                                                                                                                            |
| **8. Networking**           | Services, CoreDNS, CNI plugins, Ingress              | [[0-9_networking_dns_and_ingress           | 0-9_networking_dns_and_ingress.md]]                                                           | Service iptables/IPVS routing, CoreDNS resolution<br>CNI packet headers, Ingress controller setups   |                                                                                                                            |
| **9. Troubleshooting**      | Node, Application, Control Plane recovery            | [[0-11_troubleshooting_and_diagnostics     | 0-11_troubleshooting_and_diagnostics.md]]                                                     | Diagnostic flows, systemd unit health, network tracing                                               |                                                                                                                            |

---

## 🗺️ Step-by-Step Study Pathway

When you approach a new section in Mumshad's course labs, use the following guide to pull the deep reference materials from your vault.

### Phase 1: Foundations & API Control (Mumshad Sections 1 & 2)
Focus on how requests travel from your terminal to the API server and get converted into container execution.
*   **Step 1.1:** Start with the **API Layer**. Read [[0-1_kube_api_and_kubectl|0-1_kube_api_and_kubectl.md]] to understand API request lifecycle, resource versioning, and JSONPath parsing commands.
*   **Step 1.2:** Learn the **Physical Node Host**. Read [[0-5_containers_runtimes_and_lifecycle|0-5_containers_runtimes_and_lifecycle.md]] to study namespaces, cgroups, runc, containerd, and why the `pause` container exists.
*   **Step 1.3:** Study **Control Plane components**. Read [[0-2_cluster_architecture_and_components|0-2_cluster_architecture_and_components.md]] to dissect the API server loop, scheduler pipelines, and kubelet state syncs.
*   **Step 1.4:** Master **Workloads (Pods/Deployments)**. Study [[0-6_kubernetes_workloads_and_controllers|0-6_kubernetes_workloads_and_controllers.md]] (Sections 1-4) for workload YAML structure, rolling updates, and rollback strategies.

### Phase 2: Placement & Configuration (Mumshad Sections 3, 4 & 5)
Control how Pods are scheduled, limits are enforced, and configurations are injected.
*   **Step 2.1:** Study **Resource Restrictions**. Read [[0-3_node_mechanics_and_resource_limits|0-3_node_mechanics_and_resource_limits.md]] to master CPU/Memory limit arithmetic, OOMKiller behaviors, and QoS tiers (Guaranteed, Burstable, BestEffort).
*   **Step 2.2:** Master **Scheduling Logic**. Read [[0-13_scheduling_logging_and_lifecycle|0-13_scheduling_logging_and_lifecycle.md]] to study Taints, Tolerations, Node Affinity, PriorityClasses, and custom scheduler leases.
*   **Step 2.3:** Inject **State & Credentials**. Study [[0-7_security_and_network_policies|0-7_security_and_network_policies.md]] for ConfigMaps and Secrets, and how files/env-vars are projected into container runtimes.

### Phase 3: Cluster Operations & Maintenance (Mumshad Section 6)
Operate and maintain nodes and control planes directly.
*   **Step 3.1:** Read [[0-10_maintenance_upgrades_and_etcd|0-10_maintenance_upgrades_and_etcd.md]]. Study:
    - **Cordon vs Drain:** How the scheduling queue blocks new placements while terminating active workloads.
    - **Kubeadm Upgrades:** The exact sequence of upgrading kubeadm, kubelet, and control plane pods.
    - **etcd Backup & Restore:** How to query etcdctl with TLS certificates and restore snapshots safely.

### Phase 4: Cluster Networking & Data Storage (Mumshad Sections 7 & 8)
Master the persistent state of your cluster and internal network routes.
*   **Step 4.1:** Study **Persistent Storage**. Read [[0-8_storage_mechanics_and_csi|0-8_storage_mechanics_and_csi.md]] to learn how PersistentVolumes bind to claims, the role of StorageClasses, and CSI controller plugin pipelines.
*   **Step 4.2:** Study **CNI & Services**. Read [[0-9_networking_dns_and_ingress|0-9_networking_dns_and_ingress.md]]. Focus on:
    - **CoreDNS:** How namespace DNS searches map to Service names.
    - **Kube-Proxy (iptables vs IPVS):** How packet rewriting redirects traffic to backend Pods.
    - **Ingress Controllers:** How routing tables and TLS certificates are matched.

### Phase 5: Deep Security & Troubleshooting (Mumshad Sections 9 & 10)
Secure the cluster and handle multi-layer failures.
*   **Step 5.1:** Study **TLS, RBAC, and Policies**. Read [[0-7_security_and_network_policies|0-7_security_and_network_policies.md]] to understand X.509 cert chains, Role/ClusterRole bindings, securityContext user mappings, and NetworkPolicy ingress/egress CIDR blocks.
*   **Step 5.2:** Master **Diagnostics**. Read [[0-11_troubleshooting_and_diagnostics|0-11_troubleshooting_and_diagnostics.md]] to learn the systemd journalctl checks for kubelet, packet routing traces, and etcd cluster state recovery procedures.
