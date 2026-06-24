---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Amazon Route 53]]"
sub_type: architecture
source_type: documentation
source_url: "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html"
author: "AWS Documentation"
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/route53
  - aws/deep-dive
---

# Route 53 Resolver

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[Amazon Route 53]] > **Route 53 Resolver**

---

## 🏛️ Default VPC Resolver (Core DNS)
The **Route 53 Resolver** (historically called the `.2` resolver, e.g., `10.0.0.2` in a `10.0.0.0/16` VPC) is a core DNS service provisioned by default inside every AWS VPC. It automatically answers:
*   Local DNS queries for EC2 instances (e.g., `ip-10-0-0-15.ec2.internal`).
*   DNS records registered in VPC-associated **Private Hosted Zones**.
*   Public internet DNS queries.

---

## 🌉 Hybrid DNS Resolver Architecture

In hybrid cloud environments, corporate networks are connected to AWS VPCs via IPsec VPNs or AWS Direct Connect. To enable seamless name resolution across both networks, you must bridge the DNS services. By default, the Route 53 Resolver cannot reach on-premises BIND/AD DNS servers, and on-premises clients cannot reach the VPC's internal `.2` resolver directly.

AWS resolves this using **Route 53 Resolver Endpoints**:

### 📥 Inbound Resolver Endpoints
*   **Purpose:** Allows on-premises DNS servers and clients to resolve hostnames in AWS Private Hosted Zones.
*   **Mechanism:** Provisions Elastic Network Interfaces (ENIs) with private IP addresses in specific subnets of your VPC. 
*   **Resolution Path:** The on-premises DNS server is configured with conditional forwarders for the AWS domain (e.g., `*.aws.internal`) pointing to the Inbound Endpoint IP addresses. The Inbound Endpoint forwards the queries to the core Route 53 Resolver inside the VPC.

### 📤 Outbound Resolver Endpoints
*   **Purpose:** Enables resources in the VPC (like EC2 instances) to resolve hostnames managed by on-premises DNS servers (e.g., `*.corp.local`).
*   **Mechanism:** Establishes endpoints inside the VPC that forward queries based on defined **Forwarding Rules**.
*   **Resolution Path:** An outbound forwarding rule is configured in Route 53 (e.g., "for domains ending in `.corp.local`, forward to target on-premises DNS IPs `192.168.1.10`"). When an EC2 instance queries the VPC `.2` resolver, the resolver evaluates the forwarding rule and routes the query through the Outbound Endpoint across the hybrid tunnel to the on-premises DNS server.

---

## 🎨 Hybrid DNS Resolver Topology Diagram

The following diagram illustrates the relationship and traffic flows between on-premises and AWS networks using Inbound and Outbound endpoints:

```mermaid
graph TD
    subgraph VPC ["AWS Virtual Private Cloud (VPC)"]
        direction TB
        EC2 ["Private EC2 Instance"]
        PHZ ["Private Hosted Zone<br>(e.g., *.aws.internal)"]
        R53R ["Route 53 Resolver<br>(VPC IP .2 Core DNS)"]
        InEP ["Inbound Endpoint<br>(VPC ENIs in Private Subnets)"]
        OutEP ["Outbound Endpoint<br>(Forwarding Rules)"]
    end

    subgraph Connection ["Hybrid Connectivity (VPN / Direct Connect)"]
        Tunnel1 ["IPsec VPN / Direct Connect Tunnel"]
    end

    subgraph OnPrem ["On-Premises Data Center"]
        OnPremDNS ["On-Premises DNS Server<br>(e.g., BIND / Active Directory)"]
        OnPremApp ["On-Premises Client / Server"]
    end

    %% Flow 1: On-Prem to AWS (Inbound)
    OnPremApp -->|Query: web.aws.internal| OnPremDNS
    OnPremDNS -->|Conditional Forwarder| Tunnel1
    Tunnel1 --> InEP
    InEP --> R53R
    R53R -->|Resolve| PHZ

    %% Flow 2: AWS to On-Prem (Outbound)
    EC2 -->|Query: app.corp.local| R53R
    R53R -->|Matches Outbound Rule| OutEP
    OutEP --> Tunnel1
    Tunnel1 --> OnPremDNS
    OnPremDNS -->|Resolve| OnPremDNS

    classDef aws fill:#FF9900,stroke:#333,stroke-width:2px,color:white;
    classDef onprem fill:#3F51B5,stroke:#333,stroke-width:2px,color:white;
    classDef connection fill:#757575,stroke:#333,stroke-width:2px,color:white;
    class EC2,PHZ,R53R,InEP,OutEP aws;
    class OnPremDNS,OnPremApp onprem;
    class Tunnel1 connection;
```

*Read more in [[Reference Notes/3-12_aws_route53_dns.md#6. Route 53 Resolver & Hybrid DNS Architecture]]*
