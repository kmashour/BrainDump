---
obsidianUIMode: preview
class: index-note
tier: main-note
tags:
  - kubernetes/main-index
  - obsidian/moc
---

# ☸️ Kubernetes Main Notes Hub

This directory houses the foundational **Landing Notes** and **Deeper Dive Notes** for Kubernetes concepts, capturing first-principles intuition, architectural roles, and deep-dive comparisons.

---

## 🏛️ Kubernetes Landing Notes

* [[Main Notes/CKS Real Exam 2026 - Master Curriculum and Question Navigation Hub|🛡️ CKS Real Exam 2026: Master Curriculum & 16-Question Navigation Hub]]
* [[Main Notes/CKAD Real Exam 2026 - Master Curriculum and Question Navigation Hub|🚀 CKAD Real Exam 2026: Master Curriculum & 20-Question Navigation Hub]]
* [[Main Notes/Kubernetes Attack Surface and the 4Cs of Cloud Native Security|🛡️ Kubernetes Attack Surface and the 4Cs of Cloud Native Security]]
* [[Main Notes/Kubernetes Cluster Component Hardening and Communication Security|🔒 Kubernetes Cluster Component Hardening and Communication Security]]
* [[Main Notes/Kubernetes Network Security and Traffic Segregation|🌐 Kubernetes Network Security and Traffic Segregation]]
* [[Main Notes/Kubernetes ServiceAccounts and Workload Identity|👤 Kubernetes ServiceAccounts and Workload Identity]]
* [[Main Notes/Kubernetes Pod Security and Policy Engines|📦 Kubernetes Pod Security and Policy Engines]]
* [[Main Notes/Kubernetes Workload Security and Container Hardening|🛡️ Kubernetes Workload Security and Container Hardening]]
* [[Main Notes/Kubernetes Supply Chain Security and Artifact Integrity|📦 Kubernetes Supply Chain Security and Artifact Integrity]]
* [[Main Notes/Kubernetes Runtime Security and Threat Forensics|🦅 Kubernetes Runtime Security and Threat Forensics]]
* [[Main Notes/Linux Operating System Architecture and Kernel Mechanics|🐧 Linux Operating System Architecture and Kernel Mechanics]]

---

## ☁️ Azure Cloud Architecture & Governance Landing Notes

* [[Main Notes/Azure Resource Governance and Access Control|☁️ Azure Resource Governance and Access Control]]

```dataview
TABLE role AS "Role", domains AS "Domains", reference_guides AS "Reference Notes"
FROM "Main Notes"
WHERE class = "landing-note"
SORT file.name ASC
```
