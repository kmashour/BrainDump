---
domains:
  - "aws"
  - "network"
---

# Module 3-9: AWS VPC Networking

**Breadcrumbs:** [[3-Index - AWS|📐 AWS Index]] > **Module 3-9: AWS VPC Networking**

This module covers custom Virtual Private Cloud (VPC) network planning, public/private subnets isolation, NAT gateways, peering topologies, hybrid cloud connectivity, and endpoint configurations.

---

## 🗺️ Cognitive Map: VPC Network Routing Topology

```
+-------------------------------------------------------------------------+
|                              AWS Region                                 |
|  +-------------------------------------------------------------------+  |
|  |                            VPC (10.0.0.0/16)                      |  |
|  |  +---------------------------+     +---------------------------+  |  |
|  |  |   Public Subnet (AZ A)    |     |   Private Subnet (AZ A)   |  |  |
|  |  |   CIDR: 10.0.1.0/24       |     |   CIDR: 10.0.2.0/24       |  |  |
|  |  |                           |     |                           |  |  |
|  |  |  [Bastion Host]           |     |  [Database Instance]      |  |  |
|  |  |  (Elastic IP)             |     |  (Private IP: 10.0.2.10)  |  |  |
|  |  |                           |     |             |             |  |  |
|  |  |  [NAT Gateway] <----------+-----+-------------+             |  |  |
|  |  |  (Elastic IP)             |     |                           |  |  |
|  |  +-------------+-------------+     +---------------------------+  |  |
|  |                |                                                  |  |
|  |                v                                                  |  |
|  |       [Internet Gateway] (IGW)                                    |  |
|  +----------------|--------------------------------------------------+  |
+-------------------|-----------------------------------------------------+
                    v
             Public Internet
```

---

## 🌐 Core VPC Networking Primitives

* **VPC CIDR block:** Defines the private IP range for the network (e.g., `10.0.0.0/16` provides 65,536 IPs).
* **Subnets:** Segments the VPC CIDR across Availability Zones:
  * *Public Subnet:* Subnet route table contains a default route (`0.0.0.0/0`) pointing to the **Internet Gateway (IGW)**. Instances inside must have public IPs.
  * *Private Subnet:* Subnet route table lacks a route to the IGW. Internal instances communicate with the internet via a **NAT Gateway** located in a public subnet.
* **AWS Reserved IPs:** AWS reserves **5 IP addresses** in every subnet CIDR block (the first 4 and the last 1):
  * `.0`: Network address.
  * `.1`: AWS VPC internal router.
  * `.2`: AWS DNS server.
  * `.3`: Future AWS usage.
  * `.255`: Network broadcast address.

---

## 🛡️ VPC Security: Security Groups vs. Network ACLs

| Feature | Security Group (SG) | Network ACL (NACL) |
| :--- | :--- | :--- |
| **Boundary Scoped** | Instance level (attached to ENIs). | Subnet level (evaluates all traffic entering/leaving). |
| **Statefulness** | **Stateful** (replies allowed automatically). | **Stateless** (replies must be explicitly allowed). |
| **Rule Types** | Only Allow rules. | Allow and Deny rules. |
| **Execution Order** | All rules evaluated simultaneously. | Evaluated sequentially (by rule numbers). |

---

## 🧠 Deep-Intuition (AARF) Breakdown: Security Group and NACL Ephemeral Ports

1. **The Answer (Core Config):** Configure the outbound rules of your stateless NACL to allow traffic to the ephemeral port range `1024-65535` for communication returning from public endpoints.
2. **The Assumptions (Context):** The calling application or client operates within a private/public subnet. Different client operating systems use different ephemeral ranges (e.g., Linux uses `32768-60999`, Windows uses `49152-65535`).
3. **The Rationale (Why):** Because NACLs are stateless, allowing inbound port 80/443 traffic only permits the request to enter the subnet. When the web server replies, the outbound packet targeting the client's randomly generated ephemeral port is blocked unless the NACL explicitly allows outbound ephemeral port ranges.
4. **The Failure Loop (What if not):** Bypassing outbound ephemeral rules in the NACL while keeping port 80/443 inbound open causes TCP connections to hang and fail with timeouts, as the client handshake cannot be completed.
5. **Alternative Case (When to use 'if not'):** If network isolation is handled entirely at the application layer and stateful Security Groups are utilized, leave NACLs at their default settings (Allow All) to simplify routing.

---

## ⚡ Gateway Endpoints vs. Interface Endpoints

VPC Endpoints allow private connections to AWS services without traversing the public internet:
* **Gateway Endpoints:** Layer 3 target routes added to subnet route tables. Free. Supports **S3** and **DynamoDB** only.
* **Interface Endpoints (PrivateLink):** Allocates a private IP address (Elastic Network Interface - ENI) inside the target subnet. Billed per hour + GB processed. Supports all other AWS services (KMS, EC2, CloudWatch).

---

## 🧠 Deep-Intuition (AARF) Breakdown: NAT Gateway vs. NAT Instance

1. **The Answer (Core Pattern):** Deploy AWS-managed **NAT Gateways** in each public AZ subnet instead of self-managed **NAT Instances** on EC2.
2. **The Assumptions (Context):** Requires allocating an Elastic IP (EIP) per NAT Gateway, and routing rules in private subnets must direct `0.0.0.0/0` traffic to the NAT Gateway ID (`nat-xxxx`).
3. **The Rationale (Why):** NAT Instances run on standard EC2 VMs. If the VM crashes, all outbound internet traffic from private subnets stops. NAT Gateways are serverless, scale up to 45 Gbps, and are managed by AWS to guarantee high availability within the AZ.
4. **The Failure Loop (What if not):** Operating a single NAT Instance without auto-recovery results in private application servers failing to download updates, connect to API endpoints, or process payment gateways if the EC2 host suffers hardware degradation.
5. **Alternative Case (When to use 'if not'):** For sandbox/development environments with low outbound volume, run a micro EC2 NAT Instance with source/destination checks disabled to avoid NAT Gateway hourly provisioning charges.

---

## 🏢 VPC Interconnectivity & Hybrid Cloud

* **VPC Peering:** Connects two VPCs using private IPs. Non-transitive (VPC A peering with VPC B, and B with C, does not allow A to talk to C). Requires a mesh topology for multiple VPCs.
* **AWS Transit Gateway (TGW):** Central hub-and-spoke router connecting thousands of VPCs and on-premises networks.
* **AWS VPN:** Creates encrypted IPSec tunnels over the public internet between a Customer Gateway (on-premises) and a Virtual Private Gateway (VGW) inside the VPC.
* **AWS Direct Connect (DX):** Establishes a dedicated physical fiber-optic connection from an on-premises datacenter to an AWS DX location, bypassing the public internet for lowest latency and maximum throughput.

![[../Attachments/Pasted image 20250516113120.png]]
![[../Attachments/Pasted image 20250516114836.png]]
![[../Attachments/Pasted image 20250516115220.png]]
