---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: control-plane
related_concepts:
  - "[[kube-apiserver]]"
  - "[[kube-controller-manager]]"
  - "[[node]]"
deeper_dives:
  - "[[cloud-controller-manager-deeper]]"
reference_guides:
  - "[[Reference Notes/02_cluster_architecture_and_components.md]]"
tags:
  - kubernetes/component
  - status/completed
---

# cloud-controller-manager

**Breadcrumbs:** [[Index|🏠 Index]] > Control Plane > **cloud-controller-manager**

---

## 🎯 Purpose (Why it is used)
The `cloud-controller-manager` (CCM) embeds cloud-provider-specific control logic. It decouples the core Kubernetes system from the underlying cloud provider's APIs, allowing cloud vendors to develop and release integrations independently from the core Kubernetes release cycle.

---

## ⚙️ Functionality (What it is doing)
1. **Cloud Node Tracking:** Queries the cloud provider to check if a worker node VM has been deleted/terminated in the cloud console. If so, it removes the Node object from the cluster.
2. **Cloud Load Balancing:** Watches for Kubernetes Services of type `LoadBalancer` and interacts with cloud APIs to provision, update, or tear down physical cloud load balancers.
3. **Cloud Route Management:** Configures routing tables and network interfaces in the cloud provider's VPC/network infrastructure to enable Pod-to-Pod communication across different nodes.

---

## 🏛️ Architectural Context (How it fits in the architecture)
The `cloud-controller-manager` is an optional, pluggable Control Plane component:
* **In-Tree vs. Out-of-Tree:** Previously, cloud code was compiled "in-tree" inside the `kube-controller-manager`. In modern clusters, the CCM runs "out-of-tree" as a separate deployment or daemonset.
* **External Integration:** It acts as a bridge, reading from the `kube-apiserver` and sending API requests outward to the cloud provider (e.g., AWS, GCP, Azure, OpenStack) API endpoints.

---

## 🧩 Problem Solver (What problem it solves)
* **Code Bloat & Security:** Prevents compilation of proprietary cloud provider SDKs inside core Kubernetes binaries, reducing binary size and security attack surfaces.
* **Release Decoupling:** Allows cloud providers to fix bugs and add features to load balancer controllers without waiting for a new core Kubernetes minor release.
* **Manual Cloud Provisioning:** Automates the management of cloud resources (like subnets, routing tables, and public IPs) in response to standard Kubernetes manifest applications.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Automated External Load Balancers:** Creating a Service of type `LoadBalancer` automatically provisions an external cloud load balancer and updates the Service's `.status.loadBalancer.ingress` with a public IP or DNS name.
* **Clean Node Lifecycles:** When a cloud instance is deleted (e.g., auto-scaled down), the Kubernetes node list is updated immediately.
* **Dynamic Cloud Routes:** Cloud network routing tables are updated to direct Pod subnet traffic to the correct VM nodes.

---

## 🔴 Failure Impact (What will happen without it)
* **Broken Load Balancers:** Creating or updating Services of type `LoadBalancer` will hang indefinitely with `<pending>` external IPs. Stale load balancers will not be deleted, incurring unnecessary cloud costs.
* **Orphaned Node Records:** If a cloud VM node is deleted, the cluster will permanently show that node as `NotReady` rather than clean it up, preventing scheduled workloads from being rescheduled promptly.
* **Routing Failures:** If node IP addresses change, the underlying VPC routes will become stale, cutting off Pod-to-Pod communications.
