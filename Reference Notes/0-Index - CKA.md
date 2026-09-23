---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - kubernetes/cka
  - kubernetes/certification
  - obsidian/moc
---

# ☸️ CKA Certification Reference MOC (Certified Kubernetes Administrator)

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Reference MOC]] > **CKA Reference MOC**

> [!TIP]
> **KubeAstronaut Certification Track: CKA**
> Comprehensive reference map covering cluster architecture, installation, storage, networking, workloads, container runtimes, and troubleshooting.

---

## 🏛️ 1. Cluster Architecture, Installation & Setup (25%)
- 🧠 **[Module 0-2-1: Control Plane Core Architecture](0-2-1_control_plane_and_core_daemons.md)**
- 🏢 **[Module 0-2-2: HA Control Plane Topologies](0-2-2_ha_topologies_and_konnectivity.md)**
- 🥾 **[Module 0-10: Bootstrapping, Upgrades & etcd](0-10_maintenance_upgrades_and_etcd.md)**
- 🧪 **[Module 0-5: Containers, Runtimes & CRI Architecture](0-5_containers_runtimes_and_lifecycle.md)** *(CRI execution path, containerd vs CRI-O, crictl, pause containers, and sandbox namespace isolation)*
- ⚙️ **[Module 0-3: Node Mechanics & Resource Limits](0-3_node_mechanics_and_resource_limits.md)**
- 🛡️ **[Module 0-7-1: RBAC, ServiceAccounts & Kubeconfig](0-7-1_rbac_service_accounts_and_certificates.md)** *(Role/RoleBinding, ClusterRole/ClusterRoleBinding, ServiceAccounts, User certificates, CSR API, Kubeconfig)*

## 📦 2. Workloads & Scheduling (15%)
- 📦 **[Module 0-5: Multi-Container Pod Patterns & Lifecycle](0-5_containers_runtimes_and_lifecycle.md)** *(InitContainers, native sidecar containers v1.28+, lifecycle hooks, and ephemeral debug containers)*
- 🎯 **[Module 0-13-1: Scheduling Predicates & Scoring](0-13-1_pod_scheduling_predicates_and_scoring.md)**
- 📌 **[Module 0-13-2: Advanced Scheduling & Evictions](0-13-2_advanced_scheduling_and_eviction_control.md)**
- 🔄 **[Module 0-6-2: Deployments & Rollouts](0-6-2_deployments_replicasets_and_rollbacks.md)**
- ⚙️ **[Module 0-6-3: StatefulSets, DaemonSets, Jobs & CronJobs](0-6-3_statefulsets_daemonsets_jobs_cronjobs.md)**
- 📦 **[Module 0-6-1: Pod Lifecycle & Probes](0-6-1_pod_lifecycle_probes_and_containers.md)**
- 📜 **[Module 0-6-4: Declarative Management, Helm & Kustomize](0-6-4_declarative_management_helm_kustomize.md)**
- 🔐 **[Module 0-7-4: ConfigMaps & Secrets Management](0-7-4_secret_encryption_at_rest.md)** *(Injection via env/volumes, base64 encoding, immutable configs)*

## 🌐 3. Services & Networking (20%)
- 🕸️ **[Module 0-9-1: CNI & Service Proxying](0-9-1_pod_and_service_networking_iptables_ipvs.md)**
- 🔍 **[Module 0-9-2: CoreDNS Architecture & Resolution](0-9-2_coredns_resolution_and_custom_configs.md)**
- 🚪 **[Module 0-9-3: Ingress Controllers & Gateway API](0-9-3_ingress_controllers_and_gateway_api.md)**
- 🛡️ **[Module 0-7-3: NetworkPolicies & Traffic Segregation](0-7-3_network_policies_and_traffic_segregation.md)** *(Default deny-all, podSelector/namespaceSelector AND/OR logic, Ingress/Egress rules, OSI L3/L4)*

## 💾 4. Storage (10%)
- 📦 **[Module 0-8-1: Storage Primitives & CSI](0-8-1_storage_primitives_emptydir_hostpath.md)**
- 💾 **[Module 0-8-2: PersistentVolumes & StorageClasses](0-8-2_pv_pvc_storageclasses_and_csi.md)**
- 🗄️ **[Module 0-8-a: Local Storage Models & Scheduling Traps](0-8-a_local_storage_models_and_scheduling_traps.md)** *(VolumeBindingMode WaitForFirstConsumer, local PV pinning)*

## 🕵️ 5. Troubleshooting & Diagnostics (30%)
- 🕵️ **[Module 0-11: Cluster Troubleshooting](0-11_troubleshooting_and_diagnostics.md)**
- 📜 **[Module 0-13-3: Cluster Logging & Observability](0-13-3_cluster_logging_events_and_monitoring.md)**
- 📋 **[Module 0-12: API Management & Pod Immutability](0-12_kubernetes_api_management_and_pod_immutability.md)**

---

## 🛠️ Hands-on Exam Preparation & Playbooks
- ⚡ **[CKA Practice Playbook: Lightning Labs & Mock Exams](../Projects/CKA/Practice%20Playbook%20-%20Lightning%20Labs%20and%20Mock%20Exams.md)**
- 🗺️ **[CKA Study Alignment & Syllabus Mapping Guide](0-CKA%20Study%20Alignment%20Guide.md)**
