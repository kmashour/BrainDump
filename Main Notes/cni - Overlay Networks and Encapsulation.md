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

# cni - Overlay Networks and Encapsulation

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[cni]] > **Overlay Networks and Encapsulation**

---

## 📑 Overlay Networks and Encapsulation

An overlay network is a Software-Defined Network (SDN) built on top of a physical network (the Underlay). It abstracts the physical hardware, allowing Pods to communicate on a flat virtual network.

### Why Encapsulation is Needed
Because physical network routers and switches do not know about the virtual `10.x.x.x` Pod subnets, they will drop raw Pod-to-Pod packets. 
Overlay networks (like **WeaveNet** or Flannel VXLAN) solve this by using **Encapsulation**:
- They capture Pod traffic at the host bridge.
- They wrap the raw Pod packet inside a larger, outer packet addressed between the physical hosts' IPs (e.g. Node 1 IP to Node 2 IP).
- Physical routers only see host-to-host traffic, routing it successfully.
- The CNI agent on the target host decapsulates (unwraps) the packet and delivers the naked original packet to the target Pod.

### Calico L3 BGP Mode (The Alternative)
To avoid encapsulation overhead (CPU cycles and latency), Calico defaults to direct routing via **BGP (Border Gateway Protocol)**:
- Turns worker nodes into routers.
- Broadcasts the Pod CIDR block location to underlay physical routers/switches.
- Transfers raw, naked packets directly through the physical switches without outer envelopes.

*Read more in [[Reference Notes/0-9_networking_dns_and_ingress.md#3.3 CNI Plugin Implementations (WeaveNet vs. Calico)]]*
