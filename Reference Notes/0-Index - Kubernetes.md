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

---

## 🏗️ Domain 1: Cluster Architecture & Administration
*Control plane/worker components, HA topologies, cluster bootstrap (kubeadm), maintenance (cordon/drain), and upgrades.*
- 🧠 **[Cluster Architecture & Components](0-2_cluster_architecture_and_components.md)** (Module 02)
- 🥾 **[Cluster Bootstrapping, Maintenance & etcd](0-10_maintenance_upgrades_and_etcd.md)** (Module 10)
- 📊 **[Administration, Observability & Flow Control](0-14_cluster_administration_and_observability.md)** (Module 14)

---

## 🔌 Domain 2: Core API Engine & Extensibility
*Kubernetes API mechanics, request lifecycles, declarative updates, 3-way merge engine, CRDs, custom controllers, and Operators.*
- 🛠️ **[API Mechanics & kubectl CLI](0-1_kube_api_and_kubectl.md)** (Module 01)
- 🔀 **[API Management & Pod Spec Immutability](0-12_kubernetes_api_management_and_pod_immutability.md)** (Module 12)
- 🔌 **[API Extensions & Operators](0-15_kubernetes_api_extension_and_operators.md)** (Module 15)

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

---

## 💾 Domain 5: Data Storage & Networking
*Out-of-tree CSI, storage classes, PV/PVC lifecycles, Linux networking bridges, CNI overlays (vxlan/BGP), and Service iptables/IPVS routing.*
- 🔌 **[Storage Mechanics & CSI](0-8_storage_mechanics_and_csi.md)** (Module 08)
- 🕸️ **[Networking, DNS & Ingress](0-9_networking_dns_and_ingress.md)** (Module 09)

---

## 🛡️ Domain 6: Cluster Security & Policy Governance
*X.509 certs, RBAC rules, pod securityContexts, network policies, and Pod Security Admission (PSA/PSS).*
- 🔑 **[Cluster Security & Network Policies](0-7_security_and_network_policies.md)** (Module 07)

---

## 🕵️ Domain 7: Troubleshooting & Diagnostics
*Application debugging, node logging, control-plane recovery, service networking diagnostics, and advanced JSONPath telemetry.*
- 🕵️ **[Cluster Troubleshooting & Diagnostics](0-11_troubleshooting_and_diagnostics.md)** (Module 11)

---

## 🔎 Quick Navigation Matrix

| Core Focus | Study Module | Key Hands-on PoC / Playbook |
| :--- | :--- | :--- |
| API Mechanics & kubectl | **[Module 01](0-1_kube_api_and_kubectl.md)** | JSONPath & Custom Columns Data Extraction |
| Cluster Components | **[Module 02](0-2_cluster_architecture_and_components.md)** | HA Stacked Kubeadm Architecture |
| Node & Resource Limits | **[Module 03](0-3_node_mechanics_and_resource_limits.md)** | Cgroup configuration & Resource limits |
| Self-Healing & Probes | **[Module 04](0-4_workload_lifecycle_and_healing.md)** | Probe-based recovery & Cascading GC |
| Runtimes & Sandboxing | **[Module 05](0-5_containers_runtimes_and_lifecycle.md)** | gVisor RuntimeClass & Ephemeral debugging |
| Controllers & Templates | **[Module 06](0-6_kubernetes_workloads_and_controllers.md)** | StatefulSet ordinals & Helm rollbacks |
| Security & NetPolicies | **[Module 07](0-7_security_and_network_policies.md)** | RBAC service-account audits & NetworkPolicies |
| Storage & CSI | **[Module 08](0-8_storage_mechanics_and_csi.md)** | Dynamic local-path PV mounting |
| Networking, DNS & Ingress | **[Module 09](0-9_networking_dns_and_ingress.md)** | CNI overlay packet tracing & Ingress routing |
| Bootstrapping & Upgrades | **[Module 10](0-10_maintenance_upgrades_and_etcd.md)** | Cluster Upgrade & ETCD Restore Playbook |
| Troubleshooting & Diagnostics | **[Module 11](0-11_troubleshooting_and_diagnostics.md)** | Diagnostic node logs & static pod recoveries |
| API Declarative Updates | **[Module 12](0-12_kubernetes_api_management_and_pod_immutability.md)** | 3-Way Merge annotation & Pod replacement |
| Scheduling & Placements | **[Module 13](0-13_scheduling_logging_and_lifecycle.md)** | Taints/Tolerations & Custom Scheduler Leases |
| Observability & Flow Control | **[Module 14](0-14_cluster_administration_and_observability.md)** | API Priority & Fairness Queueing Config |
| Extensions & CRDs | **[Module 15](0-15_kubernetes_api_extension_and_operators.md)** | CustomResourceDefinitions & Operator Informers |
---

## 🧪 Domain 8: NTI & Udemy Practice Labs
*Hands-on Kubernetes labs, ConfigMaps/Secrets volumes, Ingress ingress configurations, taints/tolerations scheduling, and custom RBAC setup.*
- 🧠 **[Kubernetes Idea & Architecture](Notes_AWS_Docker_Kubernets/kubernetes-Idea-behind-it.md)**
- 📦 **[Why Kubernetes uses Pods](Notes_AWS_Docker_Kubernets/kubernetes-Why-uses-Pods.md)**
- 🥾 **[Working and Running a Pod](Notes_AWS_Docker_Kubernets/kubernetes-working-running-a-pod.md)**
- ✏️ **[Creating Pods Configuration](Notes_AWS_Docker_Kubernets/kubernetes-creating-Pods.md)**
- 🏷️ **[Using Labels and Selectors](Notes_AWS_Docker_Kubernets/kubernetes-using-labels.md)**
- 📝 **[Using Annotations Metadata](Notes_AWS_Docker_Kubernets/kubernetes-using-annotations.md)**
- 🏥 **[Liveness, Readiness & Startup Probes](Notes_AWS_Docker_Kubernets/kubernetes-liveness-readiness-startup-probes.md)**
- ⚙️ **[Probes Configurations Reference](Notes_AWS_Docker_Kubernets/kubernetes-Probes-Configurations.md)**
- 💎 **[Pods Requests and Limits Math](Notes_AWS_Docker_Kubernets/kubernetes-pods-requests-and-limits.md)**
- 🔄 **[What is a ReplicaSet](Notes_AWS_Docker_Kubernets/kubernetes-what-is-a-Replica-set.md)**
- 🧪 **[ReplicaSet Lab Walkthrough](Notes_AWS_Docker_Kubernets/Kubernetes-Replica-set-lab.md)**
- 🏗️ **[What is a Deployment](Notes_AWS_Docker_Kubernets/kubernetes-what-is-a-Deployment.md)**
- 🧪 **[Deployment Lab Walkthrough](Notes_AWS_Docker_Kubernets/kubernetes-Deployment-lab.md)**
- 🧪 **[Advanced Deployment Lab 2](Notes_AWS_Docker_Kubernets/kubernetes-Deployment-lab-2.md)**
- 🔒 **[Introduction to Secrets](Notes_AWS_Docker_Kubernets/kubernetes-introduction-to-secrets.md)**
- ⚙️ **[ConfigMaps Configurations](Notes_AWS_Docker_Kubernets/kubernetes-Config-Maps.md)**
- 🧪 **[ConfigMaps & Secrets Lab](Notes_AWS_Docker_Kubernets/kubernetes-Config-maps-secrets-lab.md)**
- 🎛️ **[DaemonSets Configurations](Notes_AWS_Docker_Kubernets/kubernetes-Daemonsets.md)**
- 🧪 **[DaemonSet Lab Walkthrough](Notes_AWS_Docker_Kubernets/kubernetes-Daemonsets-lab.md)**
- 💾 **[Volumes and Storage mounts](Notes_AWS_Docker_Kubernets/kubernetes-Volumes.md)**
- 🏗️ **[StatefulSets Configurations](Notes_AWS_Docker_Kubernets/kubernetes-StatefulSets.md)**
- 🧪 **[StatefulSets Lab Walkthrough](Notes_AWS_Docker_Kubernets/kubernetes-Statefulsets-lab.md)**
- 🔌 **[What is a Service Object](Notes_AWS_Docker_Kubernets/Kubernetes-service-what-it-is.md)**
- 🔌 **[Service Types Comparison](Notes_AWS_Docker_Kubernets/kubernetes-service-types.md)**
- 🧪 **[Lab 01: ClusterIP and NodePort Services](Notes_AWS_Docker_Kubernets/Kubernetes-Lab-01_ClusterIP_NodePort.md)**
- 🔌 **[External Services Integrations](Notes_AWS_Docker_Kubernets/Kubernetes-External-Services.md)**
- 🧪 **[Lab 02: External Services Insights](Notes_AWS_Docker_Kubernets/Kubernetes-Lab-02-insights_External_Services.md)**
- 🕸️ **[What is an Ingress Object](Notes_AWS_Docker_Kubernets/kubernetes-what-is-Ingress.md)**
- 🕸️ **[The Ingress Object Details](Notes_AWS_Docker_Kubernets/kubernetes-The-Ingress-Object.md)**
- 🧪 **[Ingress Lab 1 Walkthrough](Notes_AWS_Docker_Kubernets/kubernetes-Ingress-Lab-1.md)**
- 🧪 **[Ingress Lab 2 Walkthrough](Notes_AWS_Docker_Kubernets/kubernetes-Ingress-Lab-2.md)**
- ⏰ **[Jobs and CronJobs Scopes](Notes_AWS_Docker_Kubernets/kubernetes-Jobs-cronjobs.md)**
- 🧪 **[Jobs Lab Walkthrough](Notes_AWS_Docker_Kubernets/Kubernetes-Jobs-Lab.md)**
- 🔑 **[KUBECONFIG File Anatomy](Notes_AWS_Docker_Kubernets/kubernetes-KUBECONFIG-FILE.md)**
- 🔑 **[RBAC: What is a Role](Notes_AWS_Docker_Kubernets/kubernetes-what-is-a-Role-%28RBAC%29.md)**
- 🔑 **[RBAC: Cluster Roles](Notes_AWS_Docker_Kubernets/kubernetes-cluster-Role.md)**
- 🧪 **[Roles & ClusterRoles Lab](Notes_AWS_Docker_Kubernets/kubernetes-Roles-ClusterRole-lab.md)**
- 🛡️ **[Security and NetworkPolicies](Notes_AWS_Docker_Kubernets/kubernetes-Security-NetworkPolicies.md)**
- 🥾 **[Kubernetes NTI Day 1 Lab](Notes_AWS_Docker_Kubernets/kubernetes-NTI-Day-1.md)**
- 🥾 **[Kubernetes NTI Day 2 Lab](Notes_AWS_Docker_Kubernets/kubernetes-NTI-Day-2.md)**
- 🧪 **[Kubernetes Final Project Playbook](Notes_AWS_Docker_Kubernets/kubernetes-Final-Project.md)**
- 🛠️ **[Kubernetes Tooling & KinD Setup](Notes_AWS_Docker_Kubernets/Kubernetes-Tooling.md)**
- 🧪 **[Kind Multi-Node Installation](Notes_AWS_Docker_Kubernets/kubernetes-KinD.md)**
