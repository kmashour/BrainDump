---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - kubernetes/reference-index
  - obsidian/moc
---

# ☸️ Kubernetes Reference MOC

**Breadcrumbs:** [[0-Index|🏠 Index]] > **Kubernetes Reference MOC**

---

## 🏗️ Domain 1: Cluster Architecture & Administration
*Control plane/worker components, HA topologies, cluster bootstrap (kubeadm), maintenance (cordon/drain), and upgrades.*
- 🧠 **[Cluster Architecture & Components](02_cluster_architecture_and_components.md)** (Module 02)
- 🥾 **[Cluster Bootstrapping, Maintenance & etcd](11_maintenance_upgrades_and_etcd.md)** (Module 11)
- 📊 **[Administration, Observability & Flow Control](15_cluster_administration_and_observability.md)** (Module 15)

---

## 🔌 Domain 2: Core API Engine & Extensibility
*Kubernetes API mechanics, request lifecycles, declarative updates, 3-way merge engine, CRDs, custom controllers, and Operators.*
- 🛠️ **[API Mechanics & kubectl CLI](01_kube_api_and_kubectl.md)** (Module 01)
- 🔀 **[API Management & Pod Spec Immutability](13_kubernetes_api_management_and_pod_immutability.md)** (Module 13)
- 🔌 **[API Extensions & Operators](16_kubernetes_api_extension_and_operators.md)** (Module 16)

---

## ⚙️ Domain 3: Node Mechanics & Container Runtimes
*Worker host daemon (kubelet), cgroups, resource limits/quotas, OCI runtimes, pause containers, and sandboxing.*
- ⚙️ **[Node Mechanics & Resource Limits](03_node_mechanics_and_resource_limits.md)** (Module 03)
- 🧪 **[Containers, Runtimes & Lifecycles](05_containers_runtimes_and_lifecycle.md)** (Module 05)

---

## 📦 Domain 4: Workloads, Controllers & Scheduling
*Workload controllers (Deployments, StatefulSets, HPAs), self-healing probes, scheduler pipelines, and pod placements.*
- 🏥 **[Workload Lifecycle & Self-Healing](04_workload_lifecycle_and_healing.md)** (Module 04)
- 🎛️ **[Workloads & Controllers](07_kubernetes_workloads_and_controllers.md)** (Module 07)
- 🎯 **[Scheduling, Logging & Lifecycle](14_scheduling_logging_and_lifecycle.md)** (Module 14)

---

## 💾 Domain 5: Data Storage & Networking
*Out-of-tree CSI, storage classes, PV/PVC lifecycles, Linux networking bridges, CNI overlays (vxlan/BGP), and Service iptables/IPVS routing.*
- 🔌 **[Storage Mechanics & CSI](09_storage_mechanics_and_csi.md)** (Module 09)
- 🕸️ **[Networking, DNS & Ingress](10_networking_dns_and_ingress.md)** (Module 10)

---

## 🛡️ Domain 6: Cluster Security & Policy Governance
*X.509 certs, RBAC rules, pod securityContexts, network policies, and Pod Security Admission (PSA/PSS).*
- 🔑 **[Cluster Security & Network Policies](08_security_and_network_policies.md)** (Module 08)

---

## 🔎 Quick Navigation Matrix

| Core Focus | Study Module | Key Hands-on PoC / Playbook |
| :--- | :--- | :--- |
| API Mechanics & kubectl | **[Module 01](01_kube_api_and_kubectl.md)** | JSONPath & Custom Columns Data Extraction |
| Cluster Components | **[Module 02](02_cluster_architecture_and_components.md)** | HA Stacked Kubeadm Architecture |
| Node & Resource Limits | **[Module 03](03_node_mechanics_and_resource_limits.md)** | Cgroup configuration & Resource limits |
| Self-Healing & Probes | **[Module 04](04_workload_lifecycle_and_healing.md)** | Probe-based recovery & Cascading GC |
| Runtimes & Sandboxing | **[Module 05](05_containers_runtimes_and_lifecycle.md)** | gVisor RuntimeClass & Ephemeral debugging |
| Controllers & Templates | **[Module 07](07_kubernetes_workloads_and_controllers.md)** | StatefulSet ordinals & Helm rollbacks |
| Security & NetPolicies | **[Module 08](08_security_and_network_policies.md)** | RBAC service-account audits & NetworkPolicies |
| Storage & CSI | **[Module 09](09_storage_mechanics_and_csi.md)** | Dynamic local-path PV mounting |
| Networking, DNS & Ingress | **[Module 10](10_networking_dns_and_ingress.md)** | CNI overlay packet tracing & Ingress routing |
| Bootstrapping & Upgrades | **[Module 11](11_maintenance_upgrades_and_etcd.md)** | Cluster Upgrade & ETCD Restore Playbook |
| API Declarative Updates | **[Module 13](13_kubernetes_api_management_and_pod_immutability.md)** | 3-Way Merge annotation & Pod replacement |
| Scheduling & Placements | **[Module 14](14_scheduling_logging_and_lifecycle.md)** | Taints/Tolerations & Custom Scheduler Leases |
| Observability & Flow Control | **[Module 15](15_cluster_administration_and_observability.md)** | API Priority & Fairness Queueing Config |
| Extensions & CRDs | **[Module 16](16_kubernetes_api_extension_and_operators.md)** | CustomResourceDefinitions & Operator Informers |
