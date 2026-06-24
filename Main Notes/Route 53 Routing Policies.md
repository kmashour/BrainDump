---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Amazon Route 53]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html"
author: "AWS Documentation"
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/route53
  - aws/deep-dive
---

# Route 53 Routing Policies

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[Amazon Route 53]] > **Route 53 Routing Policies**

---

## 📑 Routing Policies Overview
Route 53 routing policies determine how Route 53 responds to client DNS queries. Crucially, client data traffic does *not* flow through Route 53; the service only translates names to endpoints, allowing clients to establish direct connections.

### 1. Simple Routing
*   **Behavior:** Routes traffic to a single resource or returns multiple static values (e.g., several IP addresses) in a single record. If multiple values are returned, the client randomly picks one.
*   **Health Checks:** Cannot be associated with health checks. If an endpoint becomes unhealthy, it continues to be returned to clients.

### 2. Weighted Routing
*   **Behavior:** Distributes traffic based on relative numeric weights.
    *   $\text{Traffic \%} = \text{Weight of Record} / \text{Sum of All Weights}$
*   **Details:** Multiple records must share the identical name and record type.
*   **Use Cases:** Load balancing, canary releases, and testing software versions. Setting weight to `0` stops routing to that resource. If all records have a weight of `0`, they return with equal weight.

### 3. Latency-Based Routing
*   **Behavior:** Routes queries to the AWS region that provides the lowest network latency for the client.
*   **Details:** Latency maps are dynamically updated by AWS. Combined with health checks to route away from degraded regions.

### 4. Failover Routing (Active-Passive)
*   **Behavior:** Implements active-passive disaster recovery.
*   **Details:** The **Primary** record is associated with a mandatory health check. Route 53 routes to the primary as long as it is healthy. If the primary health check fails, Route 53 fails over and resolves queries to the **Secondary** backup record.

### 5. Geolocation Routing
*   **Behavior:** Routes traffic based on the user's physical geographic location (continent, country, or state).
*   **Details:** The most specific geographic rule matches first. You must create a **Default** geolocation record to handle query requests that do not match any explicit location rules, preventing DNS resolution failure.
*   **Use Cases:** Web localization, content distribution restrictions, and data residency compliance.

### 6. Geoproximity Routing (With Bias)
*   **Behavior:** Routes traffic to resources based on the geographic distance between users and resources.
*   **Details:** Allows shifting regional boundaries by applying a **Bias** value:
    *   *Positive Bias:* Expands the resource's region, attracting more users.
    *   *Negative Bias:* Shrinks the region, deflecting traffic.
*   Supports non-AWS endpoints by specifying latitude and longitude.
*   *Prerequisite:* Requires using Route 53 **Traffic Flow**.

### 7. IP-Based Routing
*   **Behavior:** Routes traffic based on the client's subnet (CIDR block).
*   **Details:** You define IP ranges (CIDRs) and map specific subnets to dedicated resource endpoints.
*   **Use Cases:** Routing specific ISPs to dedicated hosts, or optimizing traffic for known client networks.

### 8. Multi-Value Answer Routing
*   **Behavior:** Returns up to 8 healthy records for client-side load balancing.
*   **Details:** Integrates directly with health checks. Unlike simple routing with multiple values, Multi-value answer dynamically filters out and excludes unhealthy IP targets.

---

## 🛠️ Route 53 Health Checking & Monitoring

Route 53 health checking enables automated failover by evaluating resource availability.

*   **Endpoint Probes:** ~15 global health checkers probe public endpoints. Probes pass only if they receive a `2xx` or `3xx` status code. You must allow Route 53 checker IP ranges in security groups. Can parse the first 5,120 bytes of a response body to search for specific strings.
*   **Calculated Health Checks:** Group up to 256 child health checks into a single parent check using `AND`, `OR`, or `NOT` operators.
*   **Private Monitoring via CloudWatch Alarms:** Since Route 53 public health checkers cannot reach private VPC or on-premises networks, you must configure a CloudWatch Alarm based on private metrics (e.g., metric streams) and configure the Route 53 health check to mirror the alarm state.

---

## ⏱️ Time To Live (TTL) Caching Strategies
TTL controls how long DNS resolvers cache a record.
*   **High TTL (e.g., 24 hours):** Minimizes Route 53 queries and reduces cost, but slows down DNS record propagation.
*   **Low TTL (e.g., 60 seconds):** Promotes fast propagation and fast failover, but generates high query traffic and higher Route 53 costs.
*   *Note:* TTL is mandatory for all records except Alias records.

*Read more in [[Reference Notes/3-12_aws_route53_dns.md#4. Route 53 Health Checking & Monitoring]] and [[Reference Notes/3-12_aws_route53_dns.md#5. Route 53 Routing Policies]]*
