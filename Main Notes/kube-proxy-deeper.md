---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[kube-proxy]]"
sub_concepts:
  - "[[Services as Virtual Entities]]"
  - "[[iptables Mode Random DNAT]]"
  - "[[IPVS Mode Hash Tables]]"
use_cases:
  - "[[Debugging Services network routing rules]]"
external_links:
  - "[Mumshad CKA Course](https://kodekloud.com)"
  - "[Kubernetes Official Docs](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)"
tags:
  - kubernetes/deep-dive
---

# kube-proxy deeper

**Breadcrumbs:** [[Index|🏠 Index]] > [[kube-proxy]] > **deeper dive**

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

*Read more in [02_cluster_architecture_and_components.md](../Reference%20Notes/02_cluster_architecture_and_components.md#e-kube-proxy-the-network-router).*
