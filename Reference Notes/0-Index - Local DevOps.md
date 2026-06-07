---
obsidianUIMode: preview
class: index-note
tier: reference-note
tags:
  - devops/reference-index
  - obsidian/moc
---

# 🐙 Local DevOps & GitOps Reference MOC

**Breadcrumbs:** [[0-Index|🏠 Index]] > **Local DevOps & GitOps Reference MOC**

---

## 🛠️ Reference Modules & Tooling

This index houses reference modules and diagnostic playbooks covering local development infrastructures, self-hosted source controls, host storage zoning, and diagnostic troubleshooting flows.

- 🐙 **[Gitea GitOps Workflows on RHEL 8](06_gitea_installation_and_workflows.md)** (Module 06)
  *   **Host Environment:** RHEL 8 security hardening, FHS standards, system users, and process namespace isolation.
  *   **Storage Setup:** LVM logical volume zoning, partition expansion, and Apache reverse proxy integrations.
  *   **Git Automation:** CI/CD runners (act_runners), air-gapped host execution, and branch governance git hooks.
  
- 🕵️ **[Cluster Troubleshooting & Diagnostics](12_troubleshooting_and_diagnostics.md)** (Module 12)
  *   **Application Debugging:** top-down container inspects, image pull fail diagnoses, and port testing.
  *   **Control Plane Diagnostics:** API server Manifest recoveries, systemd Kubelet logs, and static pod telemetry.
  *   **Service Redirection:** CoreDNS routing, Kube-Proxy logs, iptables/IPVS validation, and namespace network polices tests.
