---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/route53
---

# Module 3-12: AWS Route 53 DNS

## 1. Route 53 DNS Core Concepts & Hosted Zones

### A. Core DNS Mechanics & Terminology
Amazon Route 53 is a highly available, scalable, fully managed, and authoritative Domain Name System (DNS) service. Port 53 is a reference to the traditional DNS port. As an authoritative DNS, customers have full control to write and update DNS records. Route 53 also acts as a Domain Registrar.
*   **Top Level Domain (TLD):** The suffix at the end of a domain name (e.g., `.com`, `.gov`, `.org`). Managed by registry operators.
*   **Second Level Domain (SLD):** The primary domain name under the TLD (e.g., `amazon` in `amazon.com`).
*   **Fully Qualified Domain Name (FQDN):** The complete domain address including the hostname (e.g., `api.www.example.com.`).
*   **Zone File:** A text file containing all the DNS records mapping hostnames to IPs/destinations.
*   **Name Servers:** Servers that resolve queries by returning the target records.

### B. Public vs. Private Hosted Zones
A hosted zone is a container for records that define how to route traffic for a domain and its subdomains.
*   **Public Hosted Zones:** Route traffic over the public internet to public-facing resources. Anyone on the internet can query public records.
*   **Private Hosted Zones:** Resolve DNS queries internally inside one or more VPCs. The domain name is completely hidden from the public internet (e.g., `api.company.internal`).
    *   *Requirement:* You must enable `enableDnsHostnames` and `enableDnsSupport` in the VPC configuration to resolve private hosted zones.
*   **Pricing:**
    *   $0.50 per hosted zone per month.
    *   Domain registration costs minimum of $12 to $13 per year depending on TLD.

### C. Domain Registration Process & Initial Configuration
When registering a new domain using Amazon Route 53 as the Domain Registrar:
*   **Registration Options & Best Practices:**
    *   **Auto-Renewal:** Can be toggled on/off. Best practice is keeping it active for production domains to prevent expiration and hijacking.
    *   **Contact Information:** Requires entering registrant, administrator, and technical contact details (can be duplicated across roles).
    *   **Privacy Protection:** Enabling privacy protection is highly recommended to shield personal contact details (email, address, phone number) from the public WHOIS registry, preventing spam.
*   **Initial Hosted Zone Creation:**
    *   Once domain registration completes, Route 53 automatically spins up a matching **Public Hosted Zone** containing two default records:
        1.  **Name Server (NS) Record:** Contains four authoritative DNS servers delegated by AWS Route 53 to host name resolution for the zone.
        2.  **Start of Authority (SOA) Record:** Contains administrative metadata about the zone file, including the primary name server, serial number, refresh intervals, and retry timers.

![[Pasted image 20250513221529.png]]
![[Pasted image 20250513221555.png]]
![[Pasted image 20250513221701.png]]

---

## 2. DNS Record Types & CNAME vs. Alias

### A. Supported Record Types
*   **A Record:** Maps a hostname to an IPv4 address (e.g., `example.com` -> `1.2.3.4`).
*   **AAAA Record:** Maps a hostname to an IPv6 address.
*   **CNAME Record:** Maps a hostname to another hostname (e.g., `myapp.example.com` -> `anotherapp.amazonaws.com`).
    *   *Constraint:* CNAME records cannot be created for the Zone Apex (the root domain, e.g., `example.com`). They can only be created for subdomains.
*   **NS Record:** Name Server records containing the DNS servers authorized to resolve the zone.

### B. Route 53 Alias Records
An Alias record is a Route 53-specific extension to DNS that maps a hostname directly to an AWS Resource (e.g., Application Load Balancer, CloudFront distribution, S3 website, API Gateway).
*   **Zone Apex Compatibility:** Unlike CNAMEs, Alias records can be used for the Zone Apex (root domain).
*   **Auto-IP Mapping:** If the underlying AWS resource (like an ALB) changes its IP addresses, Route 53 automatically recognizes the change and resolves to the new IPs.
*   **Cost & Performance:** Queries for Alias records are free of charge. They support native health checks.
*   **TTL Configuration:** You cannot set the TTL manually on an Alias record. Route 53 handles the TTL dynamically.
*   **Unsupported Targets:** You cannot map an Alias record to an EC2 instance's public DNS name.

---

## 3. DNS Caching (Time To Live - TTL)

TTL is the duration in seconds that a DNS resolver caches a record before querying Route 53 again.
*   **TTL is mandatory** for all records except Alias records.
*   **High TTL (e.g., 24 hours / 86400s):**
    *   *Pros:* Minimizes queries to Route 53, reducing overall costs.
    *   *Cons:* Record modifications propagate slowly. Clients will access stale resource destinations until the cache expires.
*   **Low TTL (e.g., 60 seconds):**
    *   *Pros:* Rapid propagation of changes. Fast failover.
    *   *Cons:* High volume of queries to Route 53, which increases costs (billed per query).
*   **Migration Strategy:** To change record values with minimal downtime, first reduce the TTL. Once the new low TTL propagates to all clients, modify the record value, and then restore the high TTL.

---

## 4. Route 53 Health Checking & Monitoring

Route 53 monitors endpoints, calculated health checks, or CloudWatch alarms to enable automated DNS failover.

### A. Endpoint Health Checks
*   ~15 global health checkers perform probes against the target endpoint.
*   Requires allowing inbound access from the Route 53 health checkers' IP range in the security group of the resource.
*   **Status Codes:** Probes pass only if they receive a `2xx` or `3xx` response.
*   **Text Matching:** Health checks can examine the first 5,120 bytes of a response body to confirm specific text content.
*   **Probing Intervals:** Standard interval is 30 seconds. Fast interval is 10 seconds (costs more).
*   **Healthy/Unhealthy Threshold:** Custom threshold of failures/successes (e.g., 3 consecutive failures). Over 18% of global checkers must report healthy for Route 53 to consider the resource healthy overall.

### B. Calculated Health Checks
*   Combine up to 256 child health checks into a single parent health check using logical operations (`AND`, `OR`, `NOT`).
*   Useful for multi-component status aggregation (e.g., reporting a site as healthy if at least 2 of 3 instances are healthy).

### C. CloudWatch Alarm-Based Health Checks
*   Routes 53 health checks cannot directly query resources inside private subnets or on-premises networks because health checkers exist on the public internet.
*   *Solution:* Monitor private resources using CloudWatch Metrics, set a CloudWatch Alarm, and assign the Route 53 health check to trigger based on the alarm state.

---

## 5. Route 53 Routing Policies

Routing policies define how Route 53 responds to DNS queries. Traffic does not pass *through* Route 53; it only returns the endpoint coordinates to the client.

### A. Simple Routing Policy
*   Routes traffic to a single resource or returns multiple values in a single record.
*   If multiple values are returned (e.g., multiple IP addresses), the client randomly selects one.
*   **No Health Check Integration:** Cannot be associated with health checks. If a returned resource is down, clients may still attempt to connect to it.

### B. Weighted Routing Policy
*   Distributes traffic based on relative weights assigned to different records.
*   **Weight Math:** Traffic % = $\text{Weight of Record} / \text{Sum of All Weights}$.
*   Weights do not need to sum to 100.
*   All records in the set must have the same name and record type.
*   **Use Cases:** Load balancing, canary deployments, or regional testing. A weight of `0` stops sending traffic to a resource. If all records have a weight of `0`, they default to equal distribution.

### C. Latency-Based Routing Policy
*   Redirects users to the AWS region that provides the lowest network latency.
*   Latency maps are constantly updated by AWS based on network performance.
*   Can be associated with health checks to redirect traffic away from a degraded region.

### D. Failover Routing Policy (Active-Passive)
*   Used for active-passive disaster recovery configurations.
*   **Primary Record:** Associated with a mandatory health check. Traffic goes here by default.
*   **Secondary Record:** Serves as the backup/DR resource. Route 53 only resolves queries to this record when the Primary record's health check fails.

### E. Geolocation Routing Policy
*   Routes traffic based on the physical location of the user (continent, country, or U.S. state).
*   The most specific geographic match takes precedence.
*   **Default Record:** You must configure a "Default" geolocation record to handle traffic from locations that do not match any specified rules, preventing resolution failures.
*   **Use Cases:** Localization (language/currency), restricting content distribution, or meeting local data residency compliance laws.

### F. Geoproximity Routing Policy (With Bias)
*   Routes traffic to resources based on the geographic location of users and resources.
*   Allows shifting traffic boundaries using a parameter called **Bias**:
    *   *Positive Bias:* Expands the geographic region of a resource, attracting more users/traffic from neighboring areas.
    *   *Negative Bias:* Shrinks the region, deflecting traffic to other resources.
*   Supports non-AWS resources by specifying latitude and longitude coordinates.
*   *Requirement:* Requires Route 53 **Traffic Flow** configuration to use biases.

### G. IP-Based Routing Policy
*   Routes queries based on the client's subnet (CIDR block).
*   Define client IP ranges (CIDRs) as "IP blocks" and associate them with specific endpoints.
*   **Use Cases:** Routing specific ISPs to dedicated servers, reducing transit costs, or optimizing performance for known client networks.

### H. Multi-Value Answer Routing Policy
*   Returns multiple IP addresses (up to 8 healthy records) to the client for client-side load balancing.
*   **Health Check Integration:** Relies on active health checks. Route 53 will only return IPs of healthy resources.
*   *Difference from Simple:* Simple routing returns all listed IPs regardless of health status, whereas Multi-value dynamically filters out unhealthy endpoints.

---

## 6. Route 53 Resolver & Hybrid DNS Architecture

### A. Route 53 Resolver (Core DNS)
By default, the Route 53 Resolver (available at the VPC IP base `+2`, e.g., `10.0.0.2`) handles DNS queries for local EC2 instances, private hosted zones, and public domain resolution.

### B. Hybrid DNS Resolver Architecture
To connect an AWS VPC and an on-premises network over VPN or Direct Connect so both environments can resolve each other's domain names, you must configure **Route 53 Resolver Endpoints**:
1.  **Inbound Resolver Endpoints:** Allows on-premises DNS servers to forward queries to AWS to resolve private hosted zones (e.g., `aws.internal`).
2.  **Outbound Resolver Endpoints:** Enables EC2 instances in the VPC to forward queries to on-premises DNS servers to resolve on-premises domains (e.g., `corp.local`) via forwarding rules.

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

---

## 7. Hands-on Lab & DNS Verification Commands

### A. Lab Infrastructure Design
To validate routing behavior and caching propagation, the following infrastructure setup is deployed:
1.  **Three EC2 Instances** (t2.micro / Amazon Linux 2) in three distinct AWS regions:
    *   Frankfurt (`eu-central-1`)
    *   Northern Virginia (`us-east-1`)
    *   Singapore (`ap-southeast-1`)
    *   *Bootstrap Script:* Installs Apache and queries the instance metadata service to output the local availability zone:
        ```bash
        #!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
        EC2_AVAILABILITY_ZONE=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
        echo "<h1>Hello World from AZ $EC2_AVAILABILITY_ZONE</h1>" > /var/www/html/index.html
        ```
2.  **Application Load Balancer (ALB):** Named `DemoRoute53ALB`, configured in Frankfurt (`eu-central-1`) as an internet-facing balancer forwarding traffic to the local Frankfurt EC2 instance on Port 80.

### B. Diagnostic DNS Commands & Setup
DNS verification can be performed from any terminal. If running inside **AWS CloudShell**, the diagnostic tools must first be installed:
```bash
# Install dig and nslookup on Amazon Linux 2 / CloudShell
sudo yum install -y bind-utils
```

*   **nslookup Command:** Query the A record address mapping:
    ```bash
    nslookup test.stephanetheteacher.com
    ```
*   **dig Command:** Retain complete query logging including TTL decrement tracking:
    ```bash
    dig demo.stephanetheteacher.com
    ```

### C. TTL Cache Propagation & Verification Flow
To observe the caching mechanics of Time To Live (TTL):
1.  Create a new A record `demo.stephanetheteacher.com` pointing to the Frankfurt instance IP (`eu-central-1`) with a TTL of 120 seconds.
2.  Perform a `dig` query:
    ```bash
    dig demo.stephanetheteacher.com
    ```
    *   *Result:* Returns the Frankfurt IP and a TTL caching timer (e.g., `115`).
3.  Edit the record in Route 53 to point to the Singapore instance IP (`ap-southeast-1`).
4.  Re-run the query and refresh browser pages:
    *   *Result:* `dig` continues to output the old Frankfurt IP with a decrementing TTL (e.g., `98`, `66`), and browsers continue displaying the Frankfurt page.
5.  Wait for the TTL timer to expire (hits `0`). The local resolver fetches the updated record from Route 53.
6.  Re-query and verify browser:
    *   *Result:* Resolves to the Singapore IP and resets the TTL cache counter to `120`.

