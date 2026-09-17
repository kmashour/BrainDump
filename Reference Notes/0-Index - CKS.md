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
> **KubeAstronaut Certification Track: CKS Master Study Walkthrough**
> This index organizes the CKS knowledge base directly according to the **6-Module Course Curriculum Architecture**, serving as a sequential reference walkthrough from absolute fundamentals to senior diagnostic engineering.
> 
> 🚀 **Hands-On Exam Playbook (19 Scenarios):** [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md|🛡️ CKS Exam Practice Playbook (Hardening & Speed Hacks)]]

---

## 🏛️ The 6-Module Master Course Walkthrough

### 🧭 [Module 0-7-1: Overview & Attack Surface](0-7-1_overview_and_attack_surface.md)
*CKS Exam Architecture & Strategy, The 4Cs of Cloud Native Security (Cloud, Cluster, Container, Code), The Voting App Attack Simulation, Defense-in-Depth Remediation Matrix, and AARF Threat Modeling Diagnostics.*
- 🎯 **Core Walkthrough:** [[Reference Notes/0-7-1_overview_and_attack_surface.md|Module 0-7-1: Overview & Attack Surface]]

---

### 🛡️ [Module 0-7-2: Cluster Setup & Hardening](0-7-2_cluster_setup_and_hardening.md)
*Control plane security, CIS Kubernetes Benchmarks (kube-bench), Kube-APIServer flag hardening, Authentication mechanisms, RBAC least privilege, ServiceAccounts & Bound Tokens, Certificates API, Kubelet security, Ingress TLS, NetworkPolicies, and secure cluster upgrades.*
- 🔑 **Core Walkthrough:** [[Reference Notes/0-7-2_cluster_setup_and_hardening.md|Module 0-7-2: Cluster Setup & Hardening]]
- 🔒 **Specialized Deep Dives & Practical References:**
  - [[Reference Notes/0-7-1_rbac_service_accounts_and_certificates.md|Module: RBAC, ServiceAccounts & Certificate Authentication]]
  - [[Reference Notes/0-7-8_cluster_hardening_cis_benchmarks_and_upgrades.md|Module: Cluster Hardening, CIS Benchmarks & Upgrades]]
  - [[Reference Notes/0-7-3_network_policies_and_traffic_segregation.md|Module: NetworkPolicies & Traffic Segregation]]
  - [[Reference Notes/0-1_kube_api_and_kubectl.md|Module 0-1: API Mechanics & kubectl CLI]]
  - [[Reference Notes/0-7-a_tls_and_mtls_handshake_troubleshooting_lecture.md|Lecture: TLS & mTLS Handshake Troubleshooting]]

---

### ⚙️ [Module 0-7-3: System Hardening](0-7-3_system_hardening.md)
*Host OS footprint minimization, Linux user privileges & sudoers, SSH hardening, systemd service masking, socket auditing (`ss`), Docker socket security, Linux Capabilities (`drop: [ALL]`), Seccomp BPF filters, AppArmor Mandatory Access Control (MAC), and kernel parameter tuning (`sysctl`).*
- 🛡️ **Core Walkthrough:** [[Reference Notes/0-7-3_system_hardening.md|Module 0-7-3: System Hardening]]
- ⚙️ **Specialized Deep Dives & Practical References:**
  - [[Reference Notes/0-7-7_host_operating_system_and_node_hardening.md|Module: Host Operating System & Node Hardening]]
  - [[Reference Notes/0-7-9_workload_kernel_isolation_seccomp_apparmor_and_capabilities.md|Module: Workload Kernel Isolation, Seccomp, AppArmor & Capabilities]]
  - [[Reference Notes/0-3_node_mechanics_and_resource_limits.md|Module 0-3: Node Mechanics & Resource Limits]]

---

### 📦 [Module 0-7-4: Microservice Vulnerabilities & Isolation](0-7-4_microservice_vulnerabilities_and_isolation.md)
*Pod Security Standards (Privileged, Baseline, Restricted), Pod Security Admission (PSA tri-mode enforcement), Legacy PodSecurityPolicy (PSP) & KEP-2579 evolutionary bridge, Secret Management & Encryption at Rest (`EncryptionConfiguration` & KMS), Sandboxed Runtimes (gVisor `runsc` / Kata Containers), and mTLS Pod-to-Pod encryption.*
- 📦 **Core Walkthrough:** [[Reference Notes/0-7-4_microservice_vulnerabilities_and_isolation.md|Module 0-7-4: Microservice Vulnerabilities & Isolation]]
- 🎥 **Specialized Deep Dives & Practical References:**
  - [[Reference Notes/0-7-2_pod_security_standards_and_admission.md|Module: Pod Security Standards, PSP & PSA (Masterclass Depth)]]
  - [[Reference Notes/0-7-4_secret_encryption_at_rest.md|Module: Secret Encryption at Rest]]
  - [[Reference Notes/0-7-b_kubecon_sig_auth_psp_deprecation_and_pss_evolution.md|KubeCon Talk: SIG Auth Update & PSP Deprecation]]
  - [[Reference Notes/12-2_secrets_store_csi_driver_integration.md|Secrets Store CSI Driver Integration]]

---

### 🧬 [Module 0-7-5: Supply Chain Security](0-7-5_supply_chain_security.md)
*Container image vulnerability scanning with Trivy, ImagePolicyWebhook admission controller, static manifest analysis with KubeLinter, Software Bill of Materials (SBOM via SPDX/CycloneDX), cryptographic image signing with Cosign, and Dockerfile multi-stage build best practices.*
- 🧬 **Core Walkthrough:** [[Reference Notes/0-7-5_supply_chain_security.md|Module 0-7-5: Supply Chain Security]]
- 📦 **Specialized Deep Dives & Practical References:**
  - [[Reference Notes/0-7-5_supply_chain_security_and_imagepolicywebhook.md|Module: Supply Chain Security & ImagePolicyWebhook]]
  - [[Reference Notes/0-5_containers_runtimes_and_lifecycle.md|Module 0-5: Containers, Runtimes & Lifecycles]]
  - [[Reference Notes/0-16_admission_controllers.md|Module 0-16: Admission Controllers & Webhooks]]

---

### 📊 [Module 0-7-6: Monitoring, Logging & Runtime Security](0-7-6_monitoring_logging_runtime_security.md)
*Kubernetes API Server Auditing (Audit Policies, stages, and backend log routing), Syscall-level runtime behavioral monitoring with Falco, custom Falco detection rules, AquaSec Tracee, and container immutability enforcement.*
- 📊 **Core Walkthrough:** [[Reference Notes/0-7-6_monitoring_logging_runtime_security.md|Module 0-7-6: Monitoring, Logging & Runtime Security]]
- 🔍 **Specialized Deep Dives & Practical References:**
  - [[Reference Notes/0-7-6_runtime_security_falco_and_audit_logging.md|Module: Runtime Security, Falco & Audit Logging]]
  - [[Reference Notes/0-14_cluster_administration_and_observability.md|Module 0-14: Cluster Administration & Observability]]
  - [[Reference Notes/0-13-3_cluster_logging_events_and_monitoring.md|Module 0-13-3: Cluster Logging & Observability]]
  - [[Reference Notes/0-11_troubleshooting_and_diagnostics.md|Module 0-11: Cluster Troubleshooting & Diagnostics]]
