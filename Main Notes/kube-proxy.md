---
obsidianUIMode: preview
class: landing-note
tier: main-note
role: worker-node
related_concepts:
  - "[[kube-apiserver]]"
  - "[[pod]]"
deeper_dives:
  - "[[kube-proxy-deeper]]"
reference_guides:
  - "[[Reference Notes/02_cluster_architecture_and_components.md]]"
tags:
  - kubernetes/component
  - status/completed
---

# kube-proxy

**Breadcrumbs:** [[Index|🏠 Index]] > Worker Node Mechanics > **kube-proxy**

---

## 🎯 Purpose (Why it is used)
`kube-proxy` is a network agent that runs on every node in the cluster. Its purpose is to implement the Kubernetes Service concept, enabling network communication and load balancing to Pods from both inside and outside the cluster.

---

## ⚙️ Functionality (What it is doing)
1. **Service and Endpoint Watch:** Watches the `kube-apiserver` for new or updated Service objects and their corresponding EndpointSlices (backend Pod IPs).
2. **OS Routing Table Injection:** Configures host-level network address translation (NAT) rules in the node's Linux kernel network stack.
3. **Traffic Redirection:** Intercepts traffic sent to a Service's virtual IP (ClusterIP) and redirects it to the actual IP address of a running backend Pod.
4. **Load Balancing:** Automatically distributes incoming traffic across multiple backend pods of a Service at the packet level.

---

## 🏛️ Architectural Context (How it fits in the architecture)
`kube-proxy` runs on every worker and control plane node:
* **DaemonSet Deployment:** In modern clusters, it is deployed as a DaemonSet managed by the control plane.
* **Kernel Manipulator:** It does not act as a traditional proxy that intercepts and forwards network traffic in userspace. Instead, it programs the OS kernel (via `iptables` or `IPVS`) to handle traffic routing at the fast kernel level.

---

## 🧩 Problem Solver (What problem it solves)
* **Dynamic Pod IP Management:** Pods are transient; they are constantly created and destroyed, changing their IP addresses. Services provide a single, immutable ClusterIP. `kube-proxy` dynamically maps this stable IP to the current set of healthy Pod IPs, solving the problem of stale destination addresses.
* **Low-Overhead Routing:** By utilizing Linux kernel subsystems, it routes packets without requiring application processes to perform DNS lookups or pass traffic through user-space proxy software.

---

## 🟢 Operational Impact (What will happen with it operating)
* **Service Reachability:** Pods can communicate with other applications using standard Service names (e.g., `http://my-service`) or ClusterIPs.
* **Automatic Load Balancing:** Traffic to a Service is split across all backing pod replicas.
* **Dynamic Endpoint Adaptation:** If a pod crashes or scale-up occurs, network routing rules on all nodes update within seconds to match.

---

## 🔴 Failure Impact (What will happen without it)
* **Broken Services:** Accessing applications via Service ClusterIPs or DNS names will timeout or fail immediately.
* **Direct Pod Connectivity Only:** Pods can only communicate using direct Pod-to-Pod IP routing. If a Pod is replaced, other services cannot discover its new IP.
* **Stale Routing Tables:** Nodes will continue trying to route traffic to deleted pods or fail to recognize new ones.
* **No Load Balancer/NodePort Traffic:** External traffic coming through NodePorts or LoadBalancers will fail to distribute to backend pods.
