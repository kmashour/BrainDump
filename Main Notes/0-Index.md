---
obsidianUIMode: preview
class: index-note
tier: main-note
against: []
tags:
  - kubernetes/index
  - obsidian/moc
---

# 🏠 Second Brain Conceptual Index

Welcome to the central conceptual landing page. To ensure atomic segregation and prevent subdomain mixing, the conceptual Map of Content (MOC) is divided into topic-specific index notes.

Select a domain to view its active landing concepts, deeper dive notes, and architectural structures:

---

### ☸️ [Kubernetes Concepts MOC](0-Index%20-%20Kubernetes.md)
*Control plane orchestrators, worker node mechanics, container runtimes, scheduling workloads, configuration components, storage mounts, and network policies.*
- **Go to MOC:** [[0-Index - Kubernetes|Kubernetes MOC]]

---

### 📐 [Systems Design MOC](0-Index%20-%20Systems%20Design.md)
*Distributed scaling frameworks, database selector models, caching write topologies, geographical CDN edge nodes, and API communication protocols/security.*
- **Go to MOC:** [[0-Index - Systems Design|Systems Design MOC]]

---

### 🐳 [Docker MOC](../Reference%20Notes/2-Index%20-%20Docker.md)
*Process isolation, container lifecycle states, Dockerfiles layer caching, volumes persistency, and multi-container orchestration.*
- **Go to MOC:** [[Reference Notes/2-Index - Docker|Docker MOC]]

---

### ☁️ [AWS MOC](../Reference%20Notes/3-Index%20-%20AWS.md)
*Identity and Access Management policies, customer keys KMS, block/shared storage, and elastic VPC networking.*
- **Go to MOC:** [[Reference Notes/3-Index - AWS|AWS MOC]]

---

### 🌐 [BGP Routing MOC](../Reference%20Notes/4-Index%20-%20BGP%20Routing.md)
*Exterior network routing paths, eBGP/iBGP peer setups, and Route Reflector scalability.*
- **Go to MOC:** [[Reference Notes/4-Index - BGP Routing|BGP Routing MOC]]

---

### 📨 [Jenkins CI/CD MOC](../Reference%20Notes/5-Index%20-%20Jenkins.md)
*Orchestrated automation pipelines, declarative build rules, triggers, and multi-node execution agents.*
- **Go to MOC:** [[Reference Notes/5-Index - Jenkins|Jenkins MOC]]

---

### 🎨 [Web Fundamentals MOC](../Reference%20Notes/6-Index%20-%20Web%20Fundamentals.md)
*Semantic document layout markup and CSS box model styling definitions.*
- **Go to MOC:** [[Reference Notes/6-Index - Web Fundamentals|Web Fundamentals MOC]]

---

### 🐍 [Python Programming MOC](../Reference%20Notes/7-Index%20-%20Python.md)
*General scripting and automation syntax, virtual environments isolation, and Flask WSGI microservers.*
- **Go to MOC:** [[Reference Notes/7-Index - Python|Python Programming MOC]]

---

### 🐧 [Linux and OS MOC](../Reference%20Notes/8-Index%20-%20Linux%20and%20OS.md)
*Kernel configurations, filesystem partitions, Keepalived failovers, systemd services, and system diagnostics.*
- **Go to MOC:** [[Reference Notes/8-Index - Linux and OS|Linux and OS MOC]]

---

### 🐙 [GitHub Actions MOC](../Reference%20Notes/9-Index%20-%20GitHub%20Actions.md)
*Workflow definitions, job parallel strategies, runner configurations, dynamic token secrets, and OpenID Connect cloud trust.*
- **Go to MOC:** [[Reference Notes/9-Index - GitHub Actions|GitHub Actions MOC]]

### 📦 Miscellaneous Projects & Tooling (MISC)
*Self-hosted version control, automated runner deployment contexts, developer introspection clients, and system command-line utilities.*
- **Version Control & GitOps:** [[gitea|Gitea Git Server Setup]]
- **Developer Tooling & Commands:** [[kubectl|Kubectl CLI Utility]]

---

## 🔍 Deeper-Dive Architectural Focus Notes
*A consolidated index of all deep architectural dive notes, use cases, and technical pitfalls across the vault.*

```dataview
TABLE parent_concept AS "Component", sub_type AS "Type", tags AS "Tags"
WHERE class = "deeper-dive"
SORT parent_concept ASC, file.name ASC
```

---

## 🏛️ Architectural Patterns (Digital Garden)
*Connective pattern notes mapping intersections between multiple domains (e.g. Linux kernel hooks, AWS, Kubernetes namespaces) in production.*

```dataview
TABLE domains AS "Domains", components AS "Components", sources AS "Sources"
FROM "Digital Garden"
WHERE class = "pattern-note"
SORT file.name ASC
```
