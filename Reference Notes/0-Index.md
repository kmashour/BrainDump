---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - kubernetes/reference-index
  - obsidian/moc
---

# 📚 Second Brain - Reference Notes Index (MOC)

Welcome to the logical Map of Content (MOC) for all study reference modules, hands-on verification suites, and CKA playbooks. This index organizes our detailed study notes logically by domain focus, making it easier to discover structural patterns and engineering principles.

---

## 🏗️ Domain 1: Cluster Architecture & Administration
*This domain covers the architecture of the Kubernetes control plane, worker node daemons, high-availability stacked topologies, and cluster bootstrap/maintenance workflows.*
- 🧠 **[Cluster Architecture & Components](02_cluster_architecture_and_components.md)** (Module 02)
  *Control plane/worker components, HA topologies, cloud controller manager, and version skew policy.*
- 🥾 **[Cluster Bootstrapping, Maintenance & etcd](11_maintenance_upgrades_and_etcd.md)** (Module 11)
  *Cluster initialization (kubeadm), node draining/cordoning, version upgrades, and etcd snapshot backups/restores.*
- 📊 **[Administration, Observability & Flow Control](15_cluster_administration_and_observability.md)** (Module 15)
  *Graceful node shutdowns, swap configuration, admission webhooks, Metrics Server, and API Priority & Fairness.*

---

## 🔌 Domain 2: Core API Engine & Extensibility
*Deep mechanics of the Kubernetes API engine, request lifecycles, declarative update controllers, schema versioning, and custom operator extension loops.*
- 🛠️ **[API Mechanics & kubectl CLI](01_kube_api_and_kubectl.md)** (Module 01)
  *Request lifecycle, API groups, versions, introspection, and advanced kubectl JSONPath/custom-column filtering.*
- 🔀 **[API Management & Pod Spec Immutability](13_kubernetes_api_management_and_pod_immutability.md)** (Module 13)
  *Imperative vs. declarative object updates, 3-way merge engine internals, and pod specification immutability boundaries.*
- 🔌 **[API Extensions & Operators](16_kubernetes_api_extension_and_operators.md)** (Module 16)
  *CustomResourceDefinitions (CRDs), custom controllers, Operator pattern, device plugins, and API aggregation.*

---

## ⚙️ Domain 3: Node Mechanics & Container Runtimes
*Understanding how container runtimes isolate processes on worker nodes, cgroup resource management, pause container namespaces, AppArmor/Seccomp policies, and hardware acceleration.*
- ⚙️ **[Node Mechanics & Resource Limits](03_node_mechanics_and_resource_limits.md)** (Module 03)
  *Kubelet mechanics, host-level cgroups, resource requests/limits, LimitRanges, ResourceQuotas, and node resource managers.*
- 🧪 **[Containers, Runtimes & Lifecycles](05_containers_runtimes_and_lifecycle.md)** (Module 05)
  *OCI images, sandbox pause containers, alternate runtimes (gVisor/Kata), and ephemeral debug containers.*

---

## 📦 Domain 4: Workloads, Controllers & Scheduling
*Declarative workload controllers, lifecycle hooks, replica management, self-healing probes, and advanced scheduling placement algorithms.*
- 🏥 **[Workload Lifecycle & Self-Healing](04_workload_lifecycle_and_healing.md)** (Module 04)
  *Local restart healing, replacements, replication loops, readiness/liveness/startup probes, and garbage collection.*
- 🎛️ **[Workloads & Controllers](07_kubernetes_workloads_and_controllers.md)** (Module 07)
  *ReplicaSets, Deployments, StatefulSets, DaemonSets, Jobs, CronJobs, HPAs, VPAs, Helm, and Kustomize.*
- 🎯 **[Scheduling, Logging & Lifecycle](14_scheduling_logging_and_lifecycle.md)** (Module 14)
  *Affinity/Anti-Affinity, Taints/Tolerations, Pod Disruption Budgets, and custom scheduler loops.*

---

## 💾 Domain 5: Data Storage & Networking
*Mastering persistent storage drivers (CSI) and container-to-container, pod-to-pod, and cluster-ingress network flows.*
- 🔌 **[Storage Mechanics & CSI](09_storage_mechanics_and_csi.md)** (Module 09)
  *Out-of-tree CSI architecture, PV/PVC lifecycles, StorageClasses, dynamic provisioning, and volume mounts.*
- 🕸️ **[Networking, DNS & Ingress](10_networking_dns_and_ingress.md)** (Module 10)
  *Linux networking (veth, bridges), CNI overlays (vxlan/BGP), service proxying (iptables/IPVS), DNS resolution, and Ingress.*

---

## 🛡️ Domain 6: Cluster Security & Policy Governance
*Hardening worker workloads, securing API access, auditing permissions, and network-level traffic segregation.*
- 🔑 **[Cluster Security & Network Policies](08_security_and_network_policies.md)** (Module 08)
  *X.509 certs, RBAC (Roles/Bindings), Pod securityContexts, network segregation, and PSS/PSA.*

---

## 📐 Domain 7: Systems Architecture & Distributed Scaling
*High-level system design principles, horizontal scaling, data layer selection, caching strategies, and traffic routing outside the cluster.*
- 🖥️ **[System Design Fundamentals](17_system_design_fundamentals.md)** (Module 17)
  *Horizontal/Vertical Scaling, Load Balancing algorithms, Sharding, Consistent Hashing, Caching/CDNs, API protocols (REST/GraphQL/gRPC), authentication, and security protections.*

---

## 🚨 Domain 8: Operations & Local DevOps
*Practical troubleshooting guides, local GitOps infrastructure, and automated delivery pipelines.*
- 🕵️ **[Cluster Troubleshooting & Diagnostics](12_troubleshooting_and_diagnostics.md)** (Module 12)
  *Top-down troubleshooting logs, Kubelet failures, API Server outages, CNI debugging, and DNS lookups.*
- 🐙 **[Gitea GitOps Workflows on RHEL 8](06_gitea_installation_and_workflows.md)** (Module 06)
  *RHEL 8 hardening, LVM disk zoning, Apache proxy, act_runners CI/CD, and Git hooks.*

---

## 🔎 Quick Navigation Matrix

| Domain | Core Focus | Study Module | Key Hands-on PoC / Playbook |
| :--- | :--- | :--- | :--- |
| **Cluster Admin** | Architecture & Components | **[Module 02](02_cluster_architecture_and_components.md)** | HA Stacked Kubeadm Architecture |
| **Cluster Admin** | Bootstrapping & Upgrades | **[Module 11](11_maintenance_upgrades_and_etcd.md)** | Cluster Upgrade & ETCD Restore Playbook |
| **Cluster Admin** | Observability & Flow Control | **[Module 15](15_cluster_administration_and_observability.md)** | API Priority & Fairness Queueing Config |
| **Core API Engine**| API Mechanics & kubectl | **[Module 01](01_kube_api_and_kubectl.md)** | JSONPath & Custom Columns Data Extraction |
| **Core API Engine**| API Declarative Updates | **[Module 13](13_kubernetes_api_management_and_pod_immutability.md)** | 3-Way Merge annotation & Pod replacement |
| **Core API Engine**| Extensions & CRDs | **[Module 16](16_kubernetes_api_extension_and_operators.md)** | CustomResourceDefinitions & Operator Informers |
| **Node & Runtime** | Node & Resource Limits | **[Module 03](03_node_mechanics_and_resource_limits.md)** | Cgroup configuration & Resource limits |
| **Node & Runtime** | Runtimes & Sandboxing | **[Module 05](05_containers_runtimes_and_lifecycle.md)** | gVisor RuntimeClass & Ephemeral debugging |
| **Workloads** | Self-Healing & Probes | **[Module 04](04_workload_lifecycle_and_healing.md)** | Probe-based recovery & Cascading GC |
| **Workloads** | Controllers & Templates | **[Module 07](07_kubernetes_workloads_and_controllers.md)** | StatefulSet ordinals & Helm rollbacks |
| **Workloads** | Scheduling & Placements | **[Module 14](14_scheduling_logging_and_lifecycle.md)** | Taints/Tolerations & Custom Scheduler Leases |
| **Data & Network** | Storage & CSI | **[Module 09](09_storage_mechanics_and_csi.md)** | Dynamic local-path PV mounting |
| **Data & Network** | Networking, DNS & Ingress | **[Module 10](10_networking_dns_and_ingress.md)** | CNI overlay packet tracing & Ingress routing |
| **Security** | Security & Network Policies | **[Module 08](08_security_and_network_policies.md)** | RBAC service-account audits & NetworkPolicies |
| **System Design**  | Architecture & Scaling | **[Module 17](17_system_design_fundamentals.md)** | Nginx LB, FastAPI JWT auth, Postgres migration |
| **DevOps** | Troubleshooting | **[Module 12](12_troubleshooting_and_diagnostics.md)** | Static Pod API recovery & CNI debug flows |
| **DevOps** | Local GitOps on RHEL | **[Module 06](06_gitea_installation_and_workflows.md)** | Local Gitea deployment & CI/CD act_runner |
