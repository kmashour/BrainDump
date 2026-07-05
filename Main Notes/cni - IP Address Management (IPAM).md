---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[cni]]"
sub_type: core-concept
source_type: documentation
tags:
  - kubernetes/cni
  - kubernetes/deep-dive
---

# cni - IP Address Management (IPAM)

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[cni]] > **IP Address Management (IPAM)**

---

## 📑 IP Address Management (IPAM)

Kubernetes allocates unique IP addresses to Pods at high speed without a central runtime IPAM coordinator. Instead, it delegates address spaces in a decentralized hierarchy.

### The Two-Tier Allocation Model
1. **Control Plane Delegation (`PodCIDR`):** When a Node registers with the cluster, the `kube-controller-manager` slices a unique block (typically a `/24` subnet containing 256 IPs) from the master Cluster CIDR (e.g. `10.244.0.0/16`) and writes it to the Node Spec's `PodCIDR` field.
2. **Local CNI Execution (`host-local`):** The local CNI plugin reads the `PodCIDR` assigned to its host and manages allocation locally. It stores the state of allocated IPs in a text-based database inside `/var/lib/cni/networks/`.

Because the prefixes are guaranteed to be different (e.g. `10.244.1.x` on Node 1 vs `10.244.2.x` on Node 2), collisions are mathematically impossible.

### Sizing and Constraints
- **Subnet Sizing:** Sliced block size is configured via the `--node-cidr-mask-size` flag of the `kube-controller-manager`.
- **The maxPods Golden Rule:** The size of the `PodCIDR` subnet must provide at least double the capacity of the Kubelet's `--max-pods` limit to allow for IP recycling delays.

*Read more in [[Reference Notes/0-9_networking_dns_and_ingress.md#3.2 IP Address Management (IPAM)]]*
