---
obsidianUIMode: preview
class: index-note
tier: main-note
tags:
  - kubernetes/index
  - obsidian/moc
---

# ☸️ Kubernetes Concepts MOC

**Breadcrumbs:** [[0-Index|🏠 Index]] > **Kubernetes MOC**

---

## 🏛️ Domain 1: Control Plane & Cluster Core
*Control plane API orchestrators, etcd states, API aggregation layers, CRD declarations, and scheduling queue controllers.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "control-plane"
SORT file.name ASC
```

---

## 💪 Domain 2: Worker Node Mechanics & Container Runtimes
*Host-level container runtime sandboxes, cgroup resource limits, node agent daemons, device plugins, and system integrations.*

```dataview
TABLE related_concepts AS "Related Concepts", reference_guides AS "Reference Guides"
FROM "Main Notes"
WHERE class = "landing-note" AND role = "worker-node"
SORT file.name ASC
```

---

## 🧩 Domain 3: Application Workloads & Configuration
*Declarative controllers, scaling templates, batch executions, metadata stores, and local environments variables.*

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
