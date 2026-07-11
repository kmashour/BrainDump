---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - cncf/reference-index
  - obsidian/moc
---

# 🌐 CNCF References MOC

**Breadcrumbs:** [[--Index--|🏠 Index]] > **CNCF References MOC**

---

## 🏛️ Reference Modules & Frameworks

This index contains reference summaries and technical digests of CNCF presentations, whitepapers, and guides mapping cloud-native cluster services, disaster recovery patterns, and platform architectures.

- 🛡️ **[Module 12-1: CNCF Kubernetes Disaster Recovery](12-1_cncf_kubernetes_disaster_recovery.md)**
  * Cluster state boundaries analysis, master/node failures, etcd backup mechanics, persistent volume snapshots, backup hooks (fsfreeze), and Heptio Ark (Velero) architecture.
- 🔑 **[Module 12-2: Secrets Store CSI Driver Integration (KodeKloud Talk)](12-2_secrets_store_csi_driver_integration.md)**
  * Dynamic secret mounting, RAM-backed tmpfs storage, IRSA credential mapping, SecretProviderClass parameters, and auto-rotation reconciliation loops.
- ⛵ **[Module 12-3: Helm Package Management & Lifecycle Operations](12-3_helm_package_management.md)**
  * Chart structure, default values.yaml overrides, installation, upgrade, rollback lifecycle operations, metadata storage, and Helm 2 vs Helm 3 architectural comparisons.
- 🕸️ **[Module 12-4: Ingress Controllers and Traffic Routing (Mumshad Lecture)](12-4_ingress_controllers_architecture.md)**
  * Comparative L7 routing analysis, NodePort limits vs load balancing cost consolidation, NGINX Ingress Controller components deployment, and host-based/path-based YAML resource rules.

---

## 🔗 Related Cross-Domain References
*   **Kubernetes Cluster Maintenance:** [[0-10_maintenance_upgrades_and_etcd|Module 0-10: CKA etcd Maintenance & Upgrades]]
*   **Linux Storage & System Operations:** [[8-9_redhat_enterprise_linux_administration|Module 8-9: Red Hat Enterprise Linux (RHEL) Administration]]
