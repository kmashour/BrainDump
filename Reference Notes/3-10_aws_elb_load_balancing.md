---
domains:
  - "aws"
  - "network"
---

# Module 3-10: AWS ELB Elastic Load Balancing

**Breadcrumbs:** [[3-Index - AWS|📐 AWS Index]] > **Module 3-10: AWS ELB Elastic Load Balancing**

This module details Elastic Load Balancing (ELB) topologies, routing layers, SSL certificate management, and cross-zone configurations.

---

## ⚖️ Load Balancer Types

AWS offers three primary load balancer layers:

### A. Application Load Balancer (ALB) - Layer 7
* **Protocol:** HTTP, HTTPS, gRPC.
* **Features:** Path-based routing (e.g., `/api`), host-based routing (e.g., `app.domain.com`), and query string routing rules.
* **Security:** Must configure security groups.

### B. Network Load Balancer (NLB) - Layer 4
* **Protocol:** TCP, UDP, TLS.
* **Performance:** Sub-millisecond latency; scales to millions of requests per second.
* **IP Mapping:** Allocates a **static IP address** per Availability Zone, or binds an Elastic IP. Ideal for client whitelisting.

### C. Gateway Load Balancer (GWLB) - Layer 3
* **Protocol:** IP packets.
* **Features:** Routes traffic to third-party virtual security appliances (e.g., firewalls, deep-packet inspection) before forwarding to targets.

---

## 🎯 Target Groups, Health Checks, and Listeners

* **Listeners:** Evaluates incoming connection requests on a configured port/protocol and forwards them to target groups based on rules.
* **Target Groups:** Logical groupings of resources (EC2, ECS, Lambda, or IP addresses).
* **Health Checks:** Periodic ping requests sent by the load balancer to verify target availability:
  * *Healthy/Unhealthy Threshold:* Number of consecutive successes/failures required to change state.
  * *Unhealthy Target Routing:* If all targets in a group are unhealthy, the load balancer routes traffic to all targets anyway to prevent complete failure.

---

## 🧠 Deep-Intuition (AARF) Breakdown: SSL Offloading vs. TCP Passthrough

1. **The Answer (Core Pattern):** Implement **SSL Offloading** on an Application Load Balancer by binding an ACM (AWS Certificate Manager) SSL/TLS certificate to the HTTPS listener, allowing the ALB to decrypt traffic before sending it to EC2 targets over HTTP.
2. **The Assumptions (Context):** Internal VPC security compliance must permit plaintext HTTP traffic between the ALB and private EC2 instances, and the security groups must allow port 80/8080 ingress from the ALB.
3. **The Rationale (Why):** Decryption is CPU-intensive. Offloading SSL to the ALB frees up compute resources on backend EC2 instances. It also centralizes certificate management, allowing automated rotations via ACM without modifying web server configurations.
4. **The Failure Loop (What if not):** Passing encrypted SSL traffic directly to EC2 instances (TCP Passthrough via NLB) requires installing certificates on every instance. If a certificate expires, all client connections to that instance fail with security alerts, requiring manual redeployments.
5. **Alternative Case (When to use 'if not'):** For strict regulatory environments (e.g., PCI-DSS, HIPAA) requiring end-to-end encryption, deploy TCP Passthrough to enforce decryption only inside the secure boundaries of the target host.

---

## ⚙️ Advanced ELB Configurations

* **Cross-Zone Load Balancing:** Spreads traffic evenly across all registered healthy targets in all AZs, rather than dividing traffic 50/50 between the load balancer nodes in each AZ.
  * *Pricing:* Enabled by default and free on ALBs; disabled by default and incurs data transfer charges on NLBs.
* **Connection Draining (Deregistration Delay):** Keeps existing connections open for a specified period (e.g., 300 seconds) when an instance is deregistered or marked unhealthy, allowing active in-flight requests to complete before termination.
* **SNI (Server Name Indication):** Allows binding multiple SSL certificates with different domain names to a single load balancer listener, enabling the LB to serve the correct certificate based on the client's TLS handshake hostname.

![[../Attachments/Pasted image 20250501174421.png]]
![[../Attachments/Pasted image 20250501174556.png]]
![[../Attachments/Pasted image 20250501174857.png]]
![[../Attachments/Pasted image 20250501175443.png]]
![[../Attachments/Pasted image 20250501180443.png]]
![[../Attachments/Pasted image 20250501180459.png]]
![[../Attachments/Pasted image 20250501180910.png]]
![[../Attachments/Pasted image 20250501181431.png]]
![[../Attachments/Pasted image 20250502101828.png]]
![[../Attachments/Pasted image 20250502102957.png]]
![[../Attachments/Pasted image 20250502103308.png]]
![[../Attachments/Pasted image 20250502103329.png]]
