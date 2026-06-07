---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: network
domains:
  - "kubernetes"
  - "networking"
related_concepts:
  - "[[ingress]]"
  - "[[service]]"
against:
  - "[[ingress]]"
reference_guides:
  - "[[Reference Notes/10_networking_dns_and_ingress.md]]"
tags:
  - kubernetes/component
  - status/completed
---

# Gateway API

**Breadcrumbs:** [[0-Index|🏠 Index]] > Networking > **Gateway API**

---

## 🎯 Purpose (Why it is used)
The Gateway API is a role-oriented, highly extensible, and expressive family of API kinds designed to manage service networking in Kubernetes. It serves as the modern successor to the traditional Ingress API, offering first-class, protocol-aware routing structures that decouple infrastructure management from application routing rules.

---

## ⚙️ Functionality (What it is doing)
*   **Decoupled Controls:** Splits the routing configurations into distinct resources (`GatewayClass`, `Gateway`, and Route objects) managed by different user personas (Infra Providers, Cluster Operators, and App Developers).
*   **L4 & L7 Routing:** Standardizes advanced traffic control policies (canary splits, header modifications, redirects) directly within the resource spec, removing the need for proprietary annotations.
*   **Protocol Diversity:** Natively supports routing for HTTP, gRPC, TLS, TCP, and UDP.
*   **Cross-Namespace Routing:** Allows Route resources in developer namespaces to bind securely to shared Gateways in operator namespaces.

---

## 🏛️ Architectural Context (How it fits in the architecture)
*   **Placement:** Operates at the boundary of the cluster as an entry point for external traffic, communicating with the API Server.
*   **Controller Model:** Exists as Custom Resource Definitions (CRDs) implemented by compatible third-party data-plane controllers (e.g., Envoy Gateway, Istio, Cilium, Nginx).
*   **Downstream Target:** Routes traffic directly to Kubernetes Services based on path, host, or header matching rules.

---

## 🧩 Problem Solver (What problem it solves)
*   **The Ingress Annotation Trap:** Eliminates the proliferation of non-standard, vendor-specific annotations in Ingress manifests which broke portability across cloud environments.
*   **Collaborative Management:** Solves the challenge of shared cluster load balancers where multiple app teams had to write to a single monolithic Ingress file, risking configuration overrides and security leaks.

---

## 🟢 Operational Impact (What will happen with it operating)
*   **Canary & Traffic Splits:** Operators can dynamically configure weights for traffic splitting (e.g., 90% prod, 10% canary) directly in `HTTPRoute` rules.
*   **Portable Configs:** Migrating applications across different Kubernetes distributions or cloud providers requires no changes to developer-written Route configurations.

---

## 🔴 Failure Impact (What will happen without it)
*   Without Gateway API, clusters must fall back to legacy `Ingress` controllers (which lack native gRPC/L4 routing support and rely heavily on vendor annotations) or deploy complex, proprietary Service Meshes to achieve advanced routing.
*   Misconfiguration of Route resources can lead to routing loops, unauthorized cross-namespace access, or backend traffic blackholes.

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **Gateway API**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
FROM "Main Notes"
WHERE class = "deeper-dive" AND parent_concept = [[gateway-api]]
SORT file.name ASC
```
