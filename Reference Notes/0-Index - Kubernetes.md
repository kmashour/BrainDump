---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - kubernetes/reference-index
  - obsidian/moc
---

# ☸️ Kubernetes Reference MOC

**Breadcrumbs:** [[--Index--|🏠 Index]] > **Kubernetes Reference MOC**

> [!TIP]
> **CKA Exam Study Roadmap:** If you are studying using Mumshad's course and want to skip the videos, see the [[0-CKA Study Alignment Guide|CKA Study Alignment & Reference Map]] to follow the syllabus directly using these deep modules.

---

## 🏗️ Domain 1: Cluster Architecture & Administration
*Control plane/worker components, HA topologies, cluster bootstrap (kubeadm), maintenance (cordon/drain), and upgrades.*
- 🧠 **[Cluster Architecture & Components](0-2_cluster_architecture_and_components.md)** (Module 02)
- 🥾 **[Cluster Bootstrapping, Maintenance & etcd](0-10_maintenance_upgrades_and_etcd.md)** (Module 10)
  - 🎥 **[Lecture: Vagrant VM Provisioning for Kubeadm](0-10-a_vagrant_vm_provisioning_lecture.md)**
  - 🎥 **[Lecture: Bootstrapping a Cluster with Kubeadm](0-10-b_kubeadm_cluster_bootstrapping_lecture.md)**
- 📊 **[Administration, Observability & Flow Control](0-14_cluster_administration_and_observability.md)** (Module 14)

---

## 🔌 Domain 2: Core API Engine & Extensibility
*Kubernetes API mechanics, request lifecycles, declarative updates, 3-way merge engine, CRDs, custom controllers, and Operators.*
- 🛠️ **[API Mechanics & kubectl CLI](0-1_kube_api_and_kubectl.md)** (Module 01)
- 🔀 **[API Management & Pod Spec Immutability](0-12_kubernetes_api_management_and_pod_immutability.md)** (Module 12)
- 🔌 **[API Extensions & Operators](0-15_kubernetes_api_extension_and_operators.md)** (Module 15)
- ⛵ **[Helm Package Management & Lifecycle Operations](12-3_helm_package_management.md)** (Module 12-3)

---

## ⚙️ Domain 3: Node Mechanics & Container Runtimes
*Worker host daemon (kubelet), cgroups, resource limits/quotas, OCI runtimes, pause containers, and sandboxing.*
- ⚙️ **[Node Mechanics & Resource Limits](0-3_node_mechanics_and_resource_limits.md)** (Module 03)
- 🧪 **[Containers, Runtimes & Lifecycles](0-5_containers_runtimes_and_lifecycle.md)** (Module 05)

---

## 📦 Domain 4: Workloads, Controllers & Scheduling
*Workload controllers (Deployments, StatefulSets, HPAs), self-healing probes, scheduler pipelines, and pod placements.*
- 🏥 **[Workload Lifecycle & Self-Healing](0-4_workload_lifecycle_and_healing.md)** (Module 04)
- 🎛️ **[Workloads & Controllers](0-6_kubernetes_workloads_and_controllers.md)** (Module 06)
- 🎯 **[Scheduling, Logging & Lifecycle](0-13_scheduling_logging_and_lifecycle.md)** (Module 13)
- 🌐 **[Advanced Scheduling in Kubernetes](advanced_scheduling_in_kubernetes.md)** (Reference Article)
- 🔀 **[How does the Kubernetes scheduler work?](how_does_the_kubernetes_scheduler_work.md)** (Reference Article)
- ⚙️ **[Scheduler Code Hierarchy Overview](scheduling_code_hierarchy_overview.md)** (Reference Article)
- 💬 **[How does Kubernetes scheduler work? (StackOverflow)](how_does_kubernetes_scheduler_work_stackoverflow.md)** (Reference Article)

---

## 💾 Domain 5: Data Storage & Networking
*Out-of-tree CSI, storage classes, PV/PVC lifecycles, Linux networking bridges, CNI overlays (vxlan/BGP), and Service iptables/IPVS routing.*
- 🔌 **[Storage Mechanics & CSI](0-8_storage_mechanics_and_csi.md)** (Module 08)
- 🕸️ **[Networking, DNS & Ingress](0-9_networking_dns_and_ingress.md)** (Module 09)

---

## 🛡️ Domain 6: Cluster Security & Policy Governance
*X.509 certs, RBAC rules, pod securityContexts, network policies, and Pod Security Admission (PSA/PSS).*
- 🔑 **[Cluster Security & Network Policies](0-7_security_and_network_policies.md)** (Module 07)
  - 🎥 **[Lecture: TLS, mTLS & Hostname Resolution Troubleshooting in Kubelet](0-7-a_tls_and_mtls_handshake_troubleshooting_lecture.md)**
- 🧬 **[Admission Controllers & Webhooks](0-16_admission_controllers.md)** (Module 16)
- 🧬 **[Admission Controllers Reference](admission_controllers_reference.md)** (Reference Article)
- 🔀 **[A Guide to Kubernetes Admission Controllers](a_guide_to_kubernetes_admission_controllers.md)** (Reference Article)
- 🛡️ **[Pod Security Admission Reference](pod_security_admission_reference.md)** (Reference Article)

---

## 🕵️ Domain 7: Troubleshooting & Diagnostics
*Application debugging, node logging, control-plane recovery, service networking diagnostics, and advanced JSONPath telemetry.*
- 🕵️ **[Cluster Troubleshooting & Diagnostics](0-11_troubleshooting_and_diagnostics.md)** (Module 11)

---

## 🔎 Quick Navigation Matrix

| Core Focus                    | Study Module                                                            | Key Hands-on PoC / Playbook                   |
| :---------------------------- | :---------------------------------------------------------------------- | :-------------------------------------------- |
| API Mechanics & kubectl       | **[Module 01](0-1_kube_api_and_kubectl.md)**                            | JSONPath & Custom Columns Data Extraction     |
| Cluster Components            | **[Module 02](0-2_cluster_architecture_and_components.md)**             | HA Stacked Kubeadm Architecture               |
| Node & Resource Limits        | **[Module 03](0-3_node_mechanics_and_resource_limits.md)**              | Cgroup configuration & Resource limits        |
| Self-Healing & Probes         | **[Module 04](0-4_workload_lifecycle_and_healing.md)**                  | Probe-based recovery & Cascading GC           |
| Runtimes & Sandboxing         | **[Module 05](0-5_containers_runtimes_and_lifecycle.md)**               | gVisor RuntimeClass & Ephemeral debugging     |
| Controllers & Templates       | **[Module 06](0-6_kubernetes_workloads_and_controllers.md)**            | StatefulSet ordinals & Helm rollbacks         |
| Security & NetPolicies        | **[Module 07](0-7_security_and_network_policies.md)**                   | RBAC service-account audits & NetworkPolicies |
| Storage & CSI                 | **[Module 08](0-8_storage_mechanics_and_csi.md)**                       | Dynamic local-path PV mounting                |
| Networking, DNS & Ingress     | **[Module 09](0-9_networking_dns_and_ingress.md)**                      | CNI overlay packet tracing & Ingress routing  |
| Bootstrapping & Upgrades      | **[Module 10](0-10_maintenance_upgrades_and_etcd.md)**                  | Cluster Upgrade & ETCD Restore Playbook       |
| Troubleshooting & Diagnostics | **[Module 11](0-11_troubleshooting_and_diagnostics.md)**                | Diagnostic node logs & static pod recoveries  |
| API Declarative Updates       | **[Module 12](0-12_kubernetes_api_management_and_pod_immutability.md)** | 3-Way Merge annotation & Pod replacement      |
| Scheduling & Placements       | **[Module 13](0-13_scheduling_logging_and_lifecycle.md)**               | Taints/Tolerations & Custom Scheduler Leases  |
| Observability & Flow Control  | **[Module 14](0-14_cluster_administration_and_observability.md)**       | API Priority & Fairness Queueing Config       |
| Extensions & CRDs             | **[Module 15](0-15_kubernetes_api_extension_and_operators.md)**         | CustomResourceDefinitions & Operator Informers |
| Security & Webhooks           | **[Module 16](0-16_admission_controllers.md)**                          | ImagePolicyWebhook scanner integrations       |

