---
domains:
  - "aws"
  - "network"
---

# Module 3-12: AWS Route 53 DNS

**Breadcrumbs:** [[3-Index - AWS|📐 AWS Index]] > **Module 3-12: AWS Route 53 DNS**

This module covers DNS zone configurations, Alias record optimizations, health checking, and routing policies.

---

## 🗺️ Route 53 Hosted Zones

* **Public Hosted Zone:** Determines how traffic is routed on the internet for your domain.
* **Private Hosted Zone:** Resolves domain queries inside one or more VPCs privately (e.g., resolving `db.local` to a private IP).
* **DNS Records:**
  * **A Record:** Maps domain name to IPv4 (e.g., `10.0.0.5`).
  * **AAAA Record:** Maps domain name to IPv6.
  * **CNAME Record:** Maps domain name to another domain name. Cannot be created for the zone apex (e.g., `domain.com`).
  * **Alias Record:** AWS-specific record mapping a domain name to AWS resources (ALB, CloudFront, S3). Can be used at the zone apex. Billed as free query evaluations.

---

## 🚦 Routing Policies

Route 53 evaluates queries based on seven routing algorithms:

### A. Simple Routing
* **Behavior:** Maps a domain to a single or multiple static IP addresses. Returns all IP values randomly to the client. No health checks.

### B. Weighted Routing
* **Behavior:** Distributes traffic across resources based on assigned weights (percentages). Useful for blue-green deployments.

### C. Latency Routing
* **Behavior:** Directs users to the AWS region that provides the lowest latency to their IP address.

### D. Failover Routing (Active-Passive)
* **Behavior:** Routes traffic to a Primary target. If a Route 53 health check fails, it automatically redirects traffic to a Secondary Disaster Recovery target.

### E. Geolocation Routing
* **Behavior:** Routes traffic based on the geographic location of the client (continent, country, or state).

### F. Geoproximity Routing
* **Behavior:** Routes traffic based on the physical proximity of the user to AWS resources, allowing you to warp proximity boundaries using a "bias" value.

### G. Multivalue Answer Routing
* **Behavior:** Returns up to 8 healthy records in response to a query. If a record is unhealthy, it is excluded, providing a basic client-side load balancing.

---

## 🧠 Deep-Intuition (AARF) Breakdown: Active-Passive Failover Routing Configuration

1. **The Answer (Core Pattern):** Configure a Route 53 Failover Routing Policy with a Primary record pointing to the main ALB and a Secondary record pointing to a static backup website hosted on S3, coupled with an HTTP health check monitoring the main site.
2. **The Assumptions (Context):** The primary domain must use an Alias record, and the S3 bucket must be configured for public website hosting with the exact name of the domain.
3. **The Rationale (Why):** Automates disaster recovery. If the primary application tier crashes, the Route 53 health check fails. Route 53 immediately switches the DNS response to the S3 bucket, serving a static "maintenance page" to users without manual intervention.
4. **The Failure Loop (What if not):** Without failover routing, if the web tier goes down, clients receive browser "Connection Timeout" or 502 Bad Gateway errors, leading to a poor user experience.
5. **Alternative Case (When to use 'if not'):** For global deployments with active processing facilities in multiple regions, deploy Latency or Weighted routing to utilize all regions simultaneously.

![[../Attachments/Pasted image 20250511004319.png]]
![[../Attachments/Pasted image 20250511003916.png]]
![[../Attachments/Pasted image 20250513221529.png]]
![[../Attachments/Pasted image 20250513221555.png]]
![[../Attachments/Pasted image 20250513221701.png]]
