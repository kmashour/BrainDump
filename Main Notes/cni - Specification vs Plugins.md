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

# cni - Specification vs Plugins

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[cni]] > **Specification vs Plugins**

---

## 📑 CNI Specification vs CNI Plugins

A common confusion in container networking is using "CNI" and "CNI Plugin" interchangeably. Under the hood, they represent two distinct parts of the container network architecture.

### Technical Distinction
- **The CNI Specification:** A standard API contract maintained by the CNCF. It outlines how a container runtime (like `containerd`) should invoke network drivers to set up network namespaces. It specifies command interfaces (`ADD`, `DEL`, `CHECK`) and environment/stdin parameters.
- **The CNI Plugin:** The actual physical software binary (e.g., Calico, Flannel, Cilium) that executes the specification's instructions. It configures the veth pairs, allocates IPs, and installs routing rules on the host OS.

### CNI Solution Layers
1. **Low-Level "Building Blocks":** Reference plugins (e.g. `bridge`, `macvlan`, `ptp`) maintained by the CNI maintainers that only understand host-local networking on a single node.
2. **"Full Package" CNI Solutions:** Comprehensive network orchestrators (e.g. Calico, Cilium) that span multiple hosts, configure overlay tunnels (like VXLAN) or L3 routers (BGP), and enforce security NetworkPolicies. Under the hood, these full solutions often delegate host-local actions to the low-level building blocks.

*Read more in [[Reference Notes/0-9_networking_dns_and_ingress.md#2.0 CNI Specification vs. CNI Plugins]]*
