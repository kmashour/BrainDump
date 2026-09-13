---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - kubernetes/cks
  - kubernetes/certification
  - obsidian/moc
---

# 🛡️ CKS Certification Reference MOC (Certified Kubernetes Security Specialist)

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Reference MOC]] > **CKS Reference MOC**

> [!IMPORTANT]
> **KubeAstronaut Certification Track: CKS**
> This index maps transcript knowledge, security hardening PoCs, and core Kubernetes security concepts required for the CKS exam.
> 
> 🚀 **Hands-On Exam Playbook (19 Scenarios):** [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md|🛡️ CKS Exam Practice Playbook (Hardening & Speed Hacks)]]

---

## 🎯 1. Cluster Setup & Hardening (15%)
*RBAC, ServiceAccounts, API Priority & Fairness, API Server hardening, Kubelet security, X.509 certs, CIS benchmarks, Cluster upgrades.*
- 🔑 **[Module 0-7-1: RBAC, ServiceAccounts & Certificate Authentication](0-7-1_rbac_service_accounts_and_certificates.md)** *(includes API Priority and Fairness & Bound ServiceAccount Tokens)*
- 🛡️ **[Module 0-7-8: Cluster Hardening, CIS Benchmarks, Platform Security & Upgrades](0-7-8_cluster_hardening_cis_benchmarks_and_upgrades.md)** *(The 4Cs, kube-bench auditing, binary checksum verification, safe upgrades, and IMDSv2 metadata protection)*
- 🔒 **[Module 0-1: API Mechanics & kubectl CLI](0-1_kube_api_and_kubectl.md)**

## 🛡️ 2. System Hardening (15%)
*Host OS security, Docker daemon & socket security, IAM, minimised footprint, kernel parameters, AppArmor & Seccomp.*
- 🛡️ **[Module 0-7-7: Host System Hardening, CIS Benchmarks, AppArmor & Seccomp](0-7-7_system_hardening_seccomp_apparmor_and_syscalls.md)** *(Host OS SUID/sudoers/SSH hardening, service masking, Docker daemon/socket security, AppArmor MAC profiles, Linux Capabilities decomposition, Syscalls & strace profiling, and Seccomp)*
- 🛡️ **[Module 0-7-2: Pod Security Standards & SecurityContexts](0-7-2_pod_security_standards_and_admission.md)** *(includes OPA Gatekeeper Rego policies & Multi-Tenancy Node Isolation)*
- ⚙️ **[Module 0-3: Node Mechanics & Resource Limits](0-3_node_mechanics_and_resource_limits.md)**
- 📦 **Core Landing Concepts:**
  - [[Main Notes/AppArmor.md|AppArmor]]: Path-based Mandatory Access Control (MAC) and container profile enforcement.
  - [[Main Notes/Linux Capabilities.md|Linux Capabilities]]: POSIX capability sets, capability stripping (`drop: [ALL]`), and least privilege.
  - [[Main Notes/Seccomp.md|Seccomp]]: Kernel syscall whitelisting, BPF filter hooks, and node-wide defaulting (`seccompDefault`).


## 🔐 3. Security & Secret Encryption (20%)
*Secret management, KMS integration, EncryptionConfiguration, mTLS.*
- 🗝️ **[Module 0-7-4: Secret Management & Encryption at Rest](0-7-4_secret_encryption_at_rest.md)** *(includes Zero-Downtime Key Rotation Protocol & Low-Level etcdctl Verification)*
- 🔌 **[Secrets Store CSI Driver Integration](12-2_secrets_store_csi_driver_integration.md)**
- 🎥 **[Lecture: TLS & mTLS Handshake Troubleshooting](0-7-a_tls_and_mtls_handshake_troubleshooting_lecture.md)**

## 🕸️ 4. Microservice & Network Security (20%)
*NetworkPolicies, ingress TLS, CNI network isolation, Cilium eBPF, Pod-to-Pod mTLS.*
- 🧱 **[Module 0-7-3: NetworkPolicies & Traffic Segregation](0-7-3_network_policies_and_traffic_segregation.md)** *(includes Cloud Metadata SSRF Blocking, Multi-Tenant Pod Isolation, Cilium eBPF & Transparent mTLS)*
- 🌐 **[Module 0-9-3: Ingress Controllers & TLS Termination](0-9-3_ingress_controllers_and_gateway_api.md)**

## 🧬 5. Supply Chain Security & Admission Control (20%)
*Container image vulnerability scanning, Mutating/Validating Webhooks, ImagePolicyWebhook, PSA, KubeLinter, SBOM.*
- 📦 **[Module 0-7-5: Supply Chain Security, Image Vulnerabilities & ImagePolicyWebhook](0-7-5_supply_chain_security_and_imagepolicywebhook.md)** *(includes Trivy scanning, KubeLinter static linting, and SPDX/CycloneDX SBOM workflows)*
- 🧬 **[Module 0-16: Admission Controllers & Webhooks](0-16_admission_controllers.md)**
- 📦 **[Module 0-5: Containers, Runtimes & Lifecycles](0-5_containers_runtimes_and_lifecycle.md)**

## 📊 6. Monitoring, Logging & Runtime Security (10%)
*Runtime threat detection (Falco, Tracee), behavioral monitoring, API auditing, container immutability.*
- 🔍 **[Module 0-7-6: Runtime Security, Syscall Threat Detection (Falco) & Kubernetes API Auditing](0-7-6_runtime_security_falco_and_audit_logging.md)** *(includes Container Immutability enforcement, Falco threat rules, AquaSec Tracee, and API server audit policies)*
- 📊 **[Module 0-14: Cluster Administration & Observability](0-14_cluster_administration_and_observability.md)**
- 📜 **[Module 0-13-3: Cluster Logging & Observability](0-13-3_cluster_logging_events_and_monitoring.md)**
- 🕵️ **[Module 0-11: Cluster Troubleshooting & Diagnostics](0-11_troubleshooting_and_diagnostics.md)**
