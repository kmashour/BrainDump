---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - kubernetes/reference-index
  - obsidian/moc
---

# 📚 Kubernetes Study & Reference Notes Index

Welcome to the structured Study Roadmap and Hands-on PoCs Index for CKA preparation and systems design. This index organizes the 16 reference modules into logical learning tracks to help you build intuition and exam readiness.

---

## 🗺️ CKA Study Roadmap & Tracks

### 🏗️ Track 1: Cluster Core & Bootstrapping
*This track covers the fundamentals of the Kubernetes API, control plane architecture, and how to bootstrap and maintain clusters.*
* 🛠️ **[Module 01: API Mechanics & kubectl CLI](01_kube_api_and_kubectl.md)**
  *Request lifecycle, API groups, versions, introspection, and advanced kubectl JSONPath filtering.*
* 🧠 **[Module 02: Cluster Architecture & Components](02_cluster_architecture_and_components.md)**
  *Control plane/worker components, HA topologies, cloud controller manager, and version skew policy.*
* 🥾 **[Module 11: Cluster Bootstrapping, Maintenance & etcd](11_maintenance_upgrades_and_etcd.md)**
  *Cluster initialization (kubeadm), node draining/cordoning, version upgrades, and etcd backups.*

### 📦 Track 2: Workloads, Runtimes & Scheduling
*Learn how workloads are isolated, configured, scheduled, and healed.*
* ⚙️ **[Module 03: Node Mechanics & Resource Limits](03_node_mechanics_and_resource_limits.md)**
  *Kubelet mechanics, cgroups, resource requests/limits, LimitRanges, ResourceQuotas, and managers.*
* 🏥 **[Module 04: Workload Lifecycle & Self-Healing](04_workload_lifecycle_and_healing.md)**
  *Local restart healing, replacements, replication loops, readiness/liveness/startup probes, and garbage collection.*
* 🧪 **[Module 05: Containers, Runtimes & Lifecycles](05_containers_runtimes_and_lifecycle.md)**
  *OCI images, sandbox pause containers, alternate runtimes (gVisor/Kata), and ephemeral debug containers.*
* 🎛️ **[Module 07: Workloads & Controllers](07_kubernetes_workloads_and_controllers.md)**
  *ReplicaSets, Deployments, StatefulSets, DaemonSets, Jobs, CronJobs, HPAs, VPAs, Helm, and Kustomize.*
* 🎯 **[Module 14: Scheduling, Logging & Lifecycle](14_scheduling_logging_and_lifecycle.md)**
  *Affinity/Anti-Affinity, Taints/Tolerations, Pod Disruption Budgets, and custom scheduler loops.*

### 💾 Track 3: Storage & Networking
*Master how data is persisted and how containers communicate across nodes and namespaces.*
* 🔌 **[Module 09: Storage Mechanics & CSI](09_storage_mechanics_and_csi.md)**
  *Out-of-tree CSI architecture, PV/PVC lifecycles, StorageClasses, dynamic provisioning, and volume mounts.*
* 🕸️ **[Module 10: Networking, DNS & Ingress](10_networking_dns_and_ingress.md)**
  *Linux networking (veth, bridges), CNI overlays (vxlan/BGP), service proxying (iptables/IPVS), DNS resolution, and Ingress.*

### 🛡️ Track 4: Cluster Security, Administration & Extensibility
*Secure, optimize, monitor, and extend the Kubernetes cluster.*
* 🔑 **[Module 08: Cluster Security & Network Policies](08_security_and_network_policies.md)**
  *X.509 certs, RBAC (Roles/Bindings), Pod securityContexts, network segregation, and PSS/PSA.*
* 📊 **[Module 15: Administration, Observability & Flow Control](15_cluster_administration_and_observability.md)**
  *Graceful shutdowns, swap configuration, admission webhooks, Metrics Server, and API Priority & Fairness.*
* 🔌 **[Module 16: API Extensions & Operators](16_kubernetes_api_extension_and_operators.md)**
  *CustomResourceDefinitions (CRDs), custom controllers, Operator pattern, device plugins, and API aggregation.*

### 🚨 Track 5: Diagnostics & Operations
*Troubleshoot cluster failures, maintain local development tools, and execute GitOps pipelines.*
* 🕵️ **[Module 12: Cluster Troubleshooting & Diagnostics](12_troubleshooting_and_diagnostics.md)**
  *Top-down troubleshooting logs, Kubelet failures, API Server outages, CNI debugging, and DNS lookups.*
* 🐙 **[Module 06: Gitea GitOps Workflows on RHEL 8](06_gitea_installation_and_workflows.md)**
  *RHEL 8 hardening, LVM disk zoning, Apache proxy, act_runners CI/CD, and Git hooks.*

---

## 🔎 Quick Navigation Matrix

| Module | Core Domain Focus | Key Hands-on PoC / Playbook |
| :--- | :--- | :--- |
| **01** | API & kubectl | JSONPath & Custom Columns Data Extraction |
| **02** | Cluster Internals | HA Stacked Kubeadm Architecture |
| **03** | Node & Resource | Cgroup configuration & Resource limits |
| **04** | Self-Healing | Probe-based recovery & Cascading GC |
| **05** | Runtimes | gVisor RuntimeClass & Ephemeral debugging |
| **06** | GitOps / RHEL | Local Gitea deployment & CI/CD Runner |
| **07** | Workloads | StatefulSet ordinals & Helm rollbacks |
| **08** | Security | RBAC service-account audits & NetworkPolicies |
| **09** | Storage | Dynamic local-path dynamic PV mounting |
| **10** | Networking | CNI overlay packet tracing & Ingress routing |
| **11** | Administration | Cluster Kubeadm upgrade & ETCD database restore |
| **12** | Troubleshooting | Static Pod API recovery & CNI debug flows |
| **13** | API Management | 3-Way Merge annotation & Pod replacement |
| **14** | Scheduling | Taints/Tolerations & Custom Scheduler Leases |
| **15** | Flow Control | API Priority & Fairness queueing configuration |
| **16** | Extensions | CustomResourceDefinitions & Operator Informers |
