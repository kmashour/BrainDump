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
- 🔌 **[Module 12-4: Prometheus and Grafana Observability Stack](12-4_prometheus_and_grafana_observability_stack.md)**
  * Scraper pull-model, TSDB engine internals, write-ahead log (WAL), Prometheus metric types (Counter, Gauge, Histogram, Summary), PromQL query vector algebra, and Alertmanager routing hierarchies.
- 🎬 **[Module 12-5: Distributed Cloud-Native Authorization Architecture at Netflix Scale](12-5_netflix_cloud_native_authorization_architecture.md)**
  * Decoupling AuthN from AuthZ, universal $(I, O, R)$ authorization matrix, self-service policy portal, Aggregator & Distributor delta synchronization, sub-millisecond in-memory sidecar evaluation, intent unit testing guardrails, and payroll service Rego implementation.
- 🛡️ **[Module 12-6: Open Policy Agent (OPA) Internals & Policy-as-Code Engine](12-6_open_policy_agent_architecture_and_deep_dive.md)**
  * General-purpose policy decoupling (JSON-in/JSON-out), host-local cache principle, OPA Management APIs (Bundle, Status, Decision Log), Rego language mechanics (undefined propagation, set comprehensions), Kubernetes AdmissionReview webhooks, WebAssembly (Wasm) compilation, partial evaluation query pushdown, and static complexity analysis.

---

## 🔗 Related Cross-Domain References
*   **Kubernetes Cluster Maintenance:** [[0-10_maintenance_upgrades_and_etcd|Module 0-10: CKA etcd Maintenance & Upgrades]]
*   **Kubernetes Admission Controllers:** [[0-16_admission_controllers|Module 0-16: Kubernetes Admission Controllers]]
*   **Linux Storage & System Operations:** [[8-9_redhat_enterprise_linux_administration|Module 8-9: Red Hat Enterprise Linux (RHEL) Administration]]
*   **Distributed Authorization Pattern:** [[Digital Garden/Pattern - Distributed Policy as Code and Sidecar Authorization|Pattern: Distributed Policy as Code and Sidecar Authorization]]
*   **Dynamic Security Admission Pattern:** [[Digital Garden/Pattern - Dynamic Security Admission and Webhook TLS Verification|Pattern: Dynamic Security Admission and Webhook TLS Verification]]

