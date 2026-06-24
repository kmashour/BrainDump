---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[aws - EC2 and Elastic Load Balancing]]"
sub_type: security
source_type: udemy
course_title: "AWS Certified Solutions Architect Associate"
tags:
  - aws/compute
  - aws/security
---

# aws - IMDS

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[aws]] > [[aws - EC2 and Elastic Load Balancing]] > **IMDS**

---

## 📑 Instance Metadata Service (IMDS)

The **Instance Metadata Service (IMDS)** is an on-instance endpoint used by applications, agents, and configuration scripts running within an EC2 instance to query its local configuration metadata and temporary security credentials.

### 🌐 The Metadata Endpoint
*   **Link-Local Address:** All metadata queries are directed internally to the non-routable link-local IPv4 address:
    `http://169.254.169.254/latest/meta-data/`
*   **Common Attributes Queryable:**
    *   `local-ipv4` / `public-ipv4`
    *   `instance-id` / `instance-type`
    *   `ami-id`
    *   `security-groups`
    *   `iam/security-credentials/<role-name>` (provides temporary STS access tokens for the attached IAM Instance Profile).
*   **User Data Endpoint:** Queryable via `http://169.254.169.254/latest/user-data` to retrieve the launch script.

---

## 🔒 IMDSv1 vs. IMDSv2 (AARF Security Architecture)

AWS supports two versions of the metadata service, with IMDSv2 providing critical defenses against unauthorized access.

### 1. IMDSv1 (Request/Response)
*   **Protocol:** Uses standard HTTP GET requests (e.g., `curl http://169.254.169.254/latest/meta-data/`).
*   **Security Risk:** Vulnerable to **Server-Side Request Forgery (SSRF)**. If a web application running on the instance has a SSRF or directory traversal bug, an attacker can trick the app into fetching the metadata URL, exposing the instance profile credentials.

### 2. IMDSv2 (Session-Oriented)
*   **Protocol:** Requires a session token generated via an initial HTTP PUT request. Subsequent GET requests must include the token in a header.
*   **Mechanics:**
    ```bash
    # Step 1: Obtain a session token (valid for 21600 seconds)
    TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

    # Step 2: Use token to query metadata
    curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/instance-id
    ```
*   **Mitigation:** The PUT request is blocked by standard HTTP proxies. The session token cannot be retrieved via simple URL redirection or standard SSRF vulnerabilities.
*   **Hop Limit Control:** Set the HTTP PUT response hop limit (e.g., `--http-put-response-hop-limit 1`) to prevent containers (which require network hops through host virtual bridges) from querying the metadata service from within Docker/Kubernetes.

*Read more in [[Reference Notes/3-4_aws_ec2_compute.md#Deep-Intuition (AARF) Breakdowns]]*
