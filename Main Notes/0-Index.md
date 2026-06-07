---
obsidianUIMode: preview
class: index-note
tier: main-note
tags:
  - kubernetes/index
  - obsidian/moc
---

# 🏠 Conceptual Map of Content (MOC)

Welcome to the central landing page for the **Main Notes** of your Second Brain knowledge base. This index groups core landing concepts logically by systems domain using the **Dataview** plugin.

---

## 🏗️ Domain 1: Control Plane & Cluster Core
*Core orchestrators running on the control plane that manage cluster state, scheduling decisions, extensions, and configuration queueing.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "control-plane"
SORT file.name ASC
```

---

## 💪 Domain 2: Worker Node Mechanics & Container Runtimes
*Host-level container runtime sandboxes, cgroup resource limits, node agent daemons, and low-level kernel configurations.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "worker-node"
SORT file.name ASC
```

---

## 🧩 Domain 3: Workloads, Controllers & Configuration
*Declarative controllers, scaling templates, batch executions, metadata stores, and local environment variables.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "workload" AND !contains(domains, "networking") AND !contains(domains, "storage")
SORT file.name ASC
```

---

## 🕸️ Domain 4: Service Routing & Network Segregation
*Cluster ingress controllers, internal gateway proxy routing, DNS resolvers, and network segregation policies.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND (contains(domains, "networking") OR role = "network") AND role != "control-plane" AND role != "infra"
SORT file.name ASC
```

---

## 🔌 Domain 5: Persistent Storage & CSI Architecture
*Storage classes, persistent disks, and dynamic workspace volume claims.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND (contains(domains, "storage") OR role = "storage")
SORT file.name ASC
```

---

## 🖥️ Domain 6: Systems Design & Distributed Infrastructure
*Foundational scaling paradigms, database selection, geographically distributed CDNs, caching topologies, and security shields.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "infra" AND (contains(domains, "database") OR contains(domains, "networking") OR contains(domains, "infra") OR contains(domains, "security"))
SORT file.name ASC
```

---

## 🐙 Domain 7: GitOps & Local Infrastructure
*Self-hosted git servers, automated runner CI/CD environments, and local cluster administration.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND (role = "gitops" OR contains(file.name, "gitea"))
SORT file.name ASC
```

---

## 🛠️ Domain 8: Developer Tooling & Introspection
*Introspection clients, configuration contexts, and system-interaction shell wrappers.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "client-tool"
SORT file.name ASC
```

---

## 🔍 Deeper-Dive Architectural Focus Notes
*A consolidated index of all deep architectural dive notes, use cases, and technical pitfalls across the vault.*

```dataview
TABLE parent_concept AS "Component", sub_type AS "Type", tags AS "Tags"
FROM "Main Notes"
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
