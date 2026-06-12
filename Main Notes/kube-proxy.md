---
obsidianUIMode: preview
class: landing-note
tier: main-note
domains:
  - "kubernetes"
role: worker-node
related_concepts:
  - "[[kube-apiserver]]"
  - "[[pod]]"
reference_guides:
  - "[[Reference Notes/0-2_cluster_architecture_and_components.md]]"
  - "[[Reference Notes/0-9_networking_dns_and_ingress.md]]"
  - "[[Reference Notes/0-11_troubleshooting_and_diagnostics.md]]"
tags:
  - kubernetes/component
  - status/completed
against: []

---

# kube-proxy

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Worker Node Mechanics > **kube-proxy**

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
---

---

This note covers the virtual service concept, proxy modes (iptables vs IPVS), connection tracking, and verification procedures for **kube-proxy**.

---

## ☁️ 1. Services as Virtual Entities
A Kubernetes Service is not a physical device, network interface, or running process.
* **Pure Logic:** It is a logical object registered in the API Server containing a virtual ClusterIP.
* **Kernel Rules:** Kube-proxy takes this virtual definition and programs Linux kernel packet filters to intercept traffic destined for the ClusterIP, rewriting the destination to a physical Pod IP.

---

## 🔀 2. Kube-Proxy Modes
Kube-proxy operates in one of three modes, which dictate how it updates the host network configuration:

### A. iptables Mode (Default)
* **Mechanics:** programs netfilter rules inside the Linux kernel.
* **Algorithm:** Random distribution. It uses the `statistic` module in iptables to distribute connections (e.g., $33\%$ probability to Pod 1, $50\%$ to Pod 2, $100\%$ to Pod 3).
* **Limitations:** iptables rules are evaluated sequentially ($O(N)$ lookup complexity). In clusters with thousands of Services, the kernel spends significant CPU traversing the iptables rules for every packet, slowing network throughput.

### B. IPVS (IP Virtual Server) Mode
* **Mechanics:** Uses the IPVS netfilter hook, which is designed specifically for load balancing.
* **Performance:** Uses hash tables instead of sequential lists ($O(1)$ lookup complexity), making it highly performant for large-scale clusters.
* **Algorithms:** Supports advanced load balancing algorithms beyond random selection, such as:
  * `rr` (Round Robin)
  * `lc` (Least Connections)
  * `dh` (Destination Hashing)

### C. Userspace Mode (Obsolete)
* **Mechanics:** Intercepts traffic at the port level, copying packets back and forth between kernel space and user space.
* **Limitations:** High latency and CPU overhead due to continuous context switching.

---

## 🔎 3. Verification & Troubleshooting (CKA Commands)
Since kube-proxy runs as a DaemonSet, you can inspect it with these commands:
* **Get DaemonSet status:**
  ```bash
  kubectl get daemonset -n kube-system kube-proxy
  ```
* **Check logs of a kube-proxy instance:**
  ```bash
  kubectl logs -n kube-system -l k8s-app=kube-proxy --tail=100
  ```
* **Verify programmed iptables rules (on worker node):**
  ```bash
  iptables -t nat -L KUBE-SERVICES -n -v
  ```

*Read more in [0-2_cluster_architecture_and_components.md](../Reference%20Notes/0-2_cluster_architecture_and_components.md#e-kube-proxy-the-network-router).*

---

## 🔍 Deeper Dive Notes
This table automatically displays all deeper notes, use cases, and pitfalls associated with the **kube-proxy**.

```dataview
TABLE sub_type AS "Type", tags AS "Tags", sources AS "Sources"
WHERE class = "deeper-dive" AND contains(parent_concept, this.file.link)
SORT file.name ASC
```
