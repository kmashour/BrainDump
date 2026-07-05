---
obsidianUIMode: preview
class: pattern-note
tier: main-note
domains:
  - "kubernetes"
  - "aws"
  - "networking"
components:
  - "[[cni]]"
  - "[[node]]"
  - "[[aws - Virtual Private Cloud]]"
  - "[[bgp]]"
sources:
  - "Kubernetes Networking Reference Guides"
  - "AWS VPC ENI Specifications"
tags:
  - architecture/pattern
---

# Pattern: Cloud Provider Network Routing and CNI Encapsulation Bypasses

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > Patterns > **Cloud Provider Network Routing and CNI Encapsulation Bypasses**

---

## 🏛️ Architectural Context
In cloud environments like AWS, the network underlay (VPC) enforces strict source/destination IP checking. A virtual machine (EC2 node) is only allowed to send and receive packets with IP addresses that match its Elastic Network Interface (ENI) configuration.
To boot multiple Pods with arbitrary IPs (e.g. `10.244.x.x`) on these nodes, Kubernetes network routing must adapt:
- **Encapsulated Overlay (e.g. Flannel/Weave):** Pod-to-Pod traffic is encapsulated inside host-to-host UDP/VXLAN envelopes. The underlay VPC only sees host VM IPs, bypassing the source/destination check.
- **Direct ENI Allocation (e.g. AWS VPC CNI):** The CNI integrates with AWS APIs to assign secondary private IPs from the VPC subnet directly to secondary ENIs on the EC2 instances. Pods run directly on the VPC underlay, bypassing overlay network encapsulations entirely.
- **BGP Routed Underlay (e.g. Calico with BGP Peering):** Calico Felix agents peer with VPC routers (or top-of-rack switches) using Border Gateway Protocol (BGP) to announce pod subnets. This requires disablement of the `SourceDestCheck` attribute on EC2 instances.

---

## ⚖️ Trade-offs & Alternatives

| Strategy | Pros | Cons |
| :--- | :--- | :--- |
| **Encapsulated Overlay** | Works out-of-the-box on any cloud provider without modifying VPC tables or VM permissions. | High CPU overhead due to encapsulation/decapsulation; reduces MTU due to outer headers. |
| **Direct ENI Allocation** | Blazing-fast performance; native integration with VPC security groups, flow logs, and routing. | Limits the number of Pods per node based on instance type ENI limits; consumes real VPC IP address space. |
| **BGP Routed / Route Tables** | Direct routing speed; no encapsulation overhead; flexible route redistribution. | Requires cloud permissions to modify routing tables or disable EC2 source/dest checks; complex configuration. |

---

## 🛠️ Verification & Practical Implementation
- Check AWS EC2 Source/Destination Check configuration:
  ```bash
  aws ec2 describe-instances --instance-ids <instance-id> --query "Reservations[*].Instances[*].SourceDestCheck"
  ```
- Disable Source/Destination Check for BGP direct routing:
  ```bash
  aws ec2 modify-instance-attribute --instance-id <instance-id> --no-source-dest-check
  ```
- *See CNI configuration details in [[Reference Notes/0-9_networking_dns_and_ingress.md#3.3 CNI Plugin Implementations (WeaveNet vs. Calico)]]*
