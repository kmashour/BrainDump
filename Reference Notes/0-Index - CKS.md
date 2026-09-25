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
> **KubeAstronaut Certification Track: CKS Dual-Layer Study Roadmap**
> This index organizes the CKS preparation pathway directly following the official **6-Module Course Curriculum Architecture**, synthesizing the **Master Kubernetes Reference Notes (Layer 1: Deep Theory & Internals)** with the **Hands-on Exam Practice Scenarios (Layer 2: Real Terminal Drills)**.
> 🚀 **Hands-On Exam Playbook (20 Practical Scenarios):** [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md|🛡️ CKS Exam Practice Playbook (Hardening & Speed Hacks)]]
> 🎯 **Real Exam 2026 Interactive Lab (16 Hands-On Scenarios & AI Grader):** [[Projects/CKS/Real Exam 2026 - 16 Question Simulation Lab Guide.md|🛡️ Real Exam 2026: 16-Question Interactive Simulation Lab Guide]]

---

## 🏛️ The 6-Module Master Curriculum Roadmap

### 🧭 Module 01: Overview & Attack Surface
*CKS Exam Architecture & Strategy, The 4Cs of Cloud Native Security (Cloud, Cluster, Container, Code), The Voting App Penetration Walkthrough, Defense-in-Depth Remediation Matrix, and AARF Threat Modeling Diagnostics.*
- 📖 **Master Foundation Notes (Layer 1):**
  - [[Reference Notes/0-7-0_attack_surface_and_threat_modeling.md|Module 0-7-0: Attack Surface, 4Cs & Threat Modeling Masterclass]]
- ⚡ **Hands-On Practice Scenarios (Layer 2):**
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#⚡-section-0-cks-speed-setup-aliases--time-management|Playbook Section 0: CKS Speed Setup, Terminal Aliases & Time Management]]

---

### 🛡️ Module 02: Cluster Setup & Hardening
*Control plane security, CIS Kubernetes Benchmarks (kube-bench), Kube-APIServer flag hardening, Authentication mechanisms, RBAC least privilege, ServiceAccounts & Bound Tokens, Certificates API, Kubelet security, Ingress TLS, NetworkPolicies, and secure cluster upgrades.*
- 📖 **Master Foundation Notes (Layer 1):**
  - [[Reference Notes/0-7-1_rbac_service_accounts_and_certificates.md|Module 0-7-1: RBAC, ServiceAccounts, PKI & Bound Token Projection]]
  - [[Reference Notes/0-7-8_cluster_hardening_cis_benchmarks_and_upgrades.md|Module 0-7-8: CIS Benchmarks, Kubelet Hardening, IMDSv2 & Upgrades]]
  - [[Reference Notes/0-7-3_network_policies_and_traffic_segregation.md|Module 0-7-3: NetworkPolicies & Traffic Segregation]]
  - [[Reference Notes/0-1_kube_api_and_kubectl.md|Module 0-1: API Mechanics & kubectl CLI]]
  - [[Reference Notes/0-7-a_tls_and_mtls_handshake_troubleshooting_lecture.md|Module 0-7-a: TLS & mTLS Handshake Troubleshooting]]
- ⚡ **Hands-On Practice Scenarios (Layer 2):**
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🛡️-scenario-1-cis-benchmark-auditing-with-kube-bench|Scenario 1: CIS Benchmark Auditing with kube-bench]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🔒-scenario-2-kubelet-security--noderestriction|Scenario 2: Kubelet Security & NodeRestriction]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🌐-scenario-3-cloud-metadata-endpoint--multi-tenant-networkpolicies|Scenario 3: Cloud Metadata Endpoint & Multi-Tenant NetworkPolicies]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#📋-scenario-14-certificate-expiration-audits--renewal|Scenario 14: Certificate Expiration Audits & Renewal]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#⚙️-scenario-18-security-conscious-cluster-upgrade-with-kubeadm|Scenario 18: Security-Conscious Cluster Upgrade with kubeadm]]

---

### ⚙️ Module 03: System Hardening
*Host OS footprint minimization, Linux user privileges & sudoers, SSH hardening, systemd service masking, socket auditing (`ss`), Docker socket security, Linux Capabilities (`drop: [ALL]`), Seccomp BPF filters, AppArmor Mandatory Access Control (MAC), and kernel parameter tuning (`sysctl`).*
- 📖 **Master Foundation Notes (Layer 1):**
  - [[Reference Notes/0-7-7_host_operating_system_and_node_hardening.md|Module 0-7-7: Host Operating System & Node Hardening]]
  - [[Reference Notes/0-7-9_workload_kernel_isolation_seccomp_apparmor_and_capabilities.md|Module 0-7-9: Workload Kernel Isolation, Seccomp, AppArmor & Capabilities]]
  - [[Reference Notes/0-3_node_mechanics_and_resource_limits.md|Module 0-3: Node Mechanics & Resource Limits]]
- ⚡ **Hands-On Practice Scenarios (Layer 2):**
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#⚙️-scenario-4-host-os-hardening-kernel-modules--port-auditing|Scenario 4: Host OS Hardening (Kernel Modules & Port Auditing)]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🛡️-scenario-5-apparmor-profile-creation--pod-enforcement|Scenario 5: AppArmor Profile Creation & Pod Enforcement]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🔒-scenario-6-seccomp-profile-deployment-enforcement--node-defaulting|Scenario 6: Seccomp Profile Deployment, Enforcement & Node Defaulting]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🔒-scenario-15-docker-daemon-hardening--unix-socket-isolation|Scenario 15: Docker Daemon Hardening & Unix Socket Isolation]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🔒-scenario-19-linux-capabilities-stripping--least-privilege-verification|Scenario 19: Linux Capabilities Stripping & Least Privilege Verification]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🛡️-scenario-20-host-firewall-hardening-with-ufw--subnet-restriction|Scenario 20: Host Firewall Hardening with UFW & Subnet Restriction]]

---

### 📦 Module 04: Microservice Vulnerabilities & Workload Isolation
*Pod Security Standards (Privileged, Baseline, Restricted), Pod Security Admission (PSA tri-mode enforcement), Legacy PodSecurityPolicy (PSP) & KEP-2579 evolutionary bridge, Secret Management & Encryption at Rest (`EncryptionConfiguration` & KMS), Sandboxed Runtimes (gVisor `runsc` / Kata Containers), and mTLS Pod-to-Pod encryption.*
- 📖 **Master Foundation Notes (Layer 1):**
  - [[Reference Notes/0-7-2_pod_security_standards_and_admission.md|Module 0-7-2: Pod Security Standards, PSP & PSA (Masterclass Depth)]]
  - [[Reference Notes/0-7-4_secret_encryption_at_rest.md|Module 0-7-4: Secret Encryption at Rest & KMS Envelope Architecture]]
  - [[Reference Notes/0-5_containers_runtimes_and_lifecycle.md|Module 0-5: Containers, Runtimes & Sandboxing Architecture]]
  - [[Reference Notes/0-16_admission_controllers.md|Module 0-16: Admission Controllers, Dynamic Webhooks & OPA Gatekeeper]]
  - [[Reference Notes/0-7-b_kubecon_sig_auth_psp_deprecation_and_pss_evolution.md|Module 0-7-b: KubeCon Talk: SIG Auth Update & PSP Deprecation]]
  - [[Reference Notes/12-2_secrets_store_csi_driver_integration.md|Module 12-2: Secrets Store CSI Driver Integration]]
- ⚡ **Hands-On Practice Scenarios (Layer 2):**
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#📦-scenario-7-sandboxed-workloads-with-gvisor-runsc|Scenario 7: Sandboxed Workloads with gVisor (runsc)]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🛡️-scenario-10-pod-security-admission-psa-standards-hardening--legacy-psp|Scenario 10: Pod Security Admission (PSA) Standards Hardening & Legacy PSP]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🗝️-scenario-11-secret-encryption-at-rest--etcd-verification|Scenario 11: Secret Encryption at Rest & etcd Verification]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🧬-scenario-17-opa-gatekeeper-policy-enforcement|Scenario 17: OPA Gatekeeper Policy Enforcement]]

---

### 🧬 Module 05: Supply Chain Security
*Container image vulnerability scanning with Trivy, ImagePolicyWebhook admission controller, static manifest analysis with KubeLinter, Software Bill of Materials (SBOM via SPDX/CycloneDX), cryptographic image signing with Cosign, and Dockerfile multi-stage build best practices.*
- 📖 **Master Foundation Notes (Layer 1):**
  - [[Reference Notes/0-7-5_supply_chain_security_and_imagepolicywebhook.md|Module 0-7-5: Supply Chain Security, SBOM, Cosign & ImagePolicyWebhook]]
  - [[Reference Notes/0-5_containers_runtimes_and_lifecycle.md|Module 0-5: Containers, Runtimes & Lifecycle Management]]
  - [[Reference Notes/0-16_admission_controllers.md|Module 0-16: Admission Controllers & Webhooks]]
- ⚡ **Hands-On Practice Scenarios (Layer 2):**
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🔍-scenario-8-vulnerability-scanning-with-trivy|Scenario 8: Vulnerability Scanning with Trivy]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🧬-scenario-9-imagepolicywebhook-admission-configuration|Scenario 9: ImagePolicyWebhook Admission Configuration]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🛡️-scenario-16-manifest-security-linting-with-kubelinter--immutability|Scenario 16: Manifest Security Linting with KubeLinter & Immutability]]

---

### 📊 Module 06: Monitoring, Logging & Runtime Security
*Kubernetes API Server Auditing (Audit Policies, stages, and backend log routing), Syscall-level runtime behavioral monitoring with Falco, custom Falco detection rules, AquaSec Tracee, and container immutability enforcement.*
- 📖 **Master Foundation Notes (Layer 1):**
  - [[Reference Notes/0-7-6_runtime_security_falco_and_audit_logging.md|Module 0-7-6: Runtime Security, Falco eBPF & API Server Auditing]]
  - [[Reference Notes/0-14_cluster_administration_and_observability.md|Module 0-14: Cluster Administration & Observability]]
  - [[Reference Notes/0-13-3_cluster_logging_events_and_monitoring.md|Module 0-13-3: Cluster Logging & Observability]]
  - [[Reference Notes/0-11_troubleshooting_and_diagnostics.md|Module 0-11: Cluster Troubleshooting & Diagnostics]]
- ⚡ **Hands-On Practice Scenarios (Layer 2):**
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#📜-scenario-12-kubernetes-api-server-auditing|Scenario 12: Kubernetes API Server Auditing]]
  - [[Projects/CKS/Practice Playbook - CKS Exam Hardening and Speed Hacks.md#🔍-scenario-13-runtime-threat-detection-with-custom-falco-rules|Scenario 13: Runtime Threat Detection with Custom Falco Rules]]
