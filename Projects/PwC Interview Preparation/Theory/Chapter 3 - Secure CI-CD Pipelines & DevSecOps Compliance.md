---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - "github-actions"
concepts_referenced:
  - "[[github-actions]]"
difficulty: advanced
status: completed
---

# Chapter 3: Secure CI/CD Pipelines & DevSecOps Compliance

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 3: CI/CD & DevSecOps**

---

## 🚀 1. GitHub Actions runner security models

To design secure CI/CD pipelines, compare runner environments and security constraints:

### A. GitHub-Hosted Runners
*   **Architecture:** GitHub provisions a clean, isolated virtual machine (running on Azure VM infrastructure) for each job. The VM is destroyed immediately upon job completion.
*   **Security:** Highly secure from cross-job contamination. However, they lack access to your private cloud networks (like private subnets inside an AWS VPC). Opening VPC firewalls to allow incoming traffic from public GitHub IP pools represents a major security vulnerability.

### B. Self-Hosted Runners (In-VPC Execution)
*   **Architecture:** You deploy virtual machines (EC2, ECS tasks, or Kubernetes Pods) running the GitHub Runner agent inside your private VPC.
*   **Pros:** Can securely connect to internal resources (EKS API endpoints, databases) without public exposure.
*   **Cons & Hardening Requirements:**
    *   *Persistent State:* Unlike GitHub-hosted runners, self-hosted runners can persist workspace directories, exposing subsequent jobs to raw build artifacts. Enforce cleanups using post-job scripts or run containerized, ephemeral runners that scale down to zero.
    *   *Privilege Escalation:* A compromised job can execute code that accesses the runner's underlying host or assumes the host's IAM Instance Profile role, exposing the entire VPC. Harden runners by removing unnecessary tooling and using restricted IAM roles.

---

## 🔑 2. Identity Federation: Secretless CI/CD via AWS OIDC

Using static AWS Access Keys (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) saved as long-lived secrets in GitHub is a major security risk. If a developer's account is compromised, the keys can be leaked.

```
+---------------+              +-----------------+             +---------------+
| GHA Runner VM |              | GitHub OIDC IdP |             |    AWS STS    |
+-------┬-------+              +--------┬--------+             +-------┬-------+
        │                               │                              │
        │ 1. Request JWT                │                              │
        ├──────────────────────────────>│                              │
        │                               │                              │
        │ 2. Return Signed JWT          │                              │
        │<──────────────────────────────┤                              │
        │                                                              │
        │ 3. Call AssumeRoleWithWebIdentity (presents JWT)             │
        ├─────────────────────────────────────────────────────────────>│
        │                                                              │
        │ 4. Verify Signature & Trust Policy, Return Temporary STS Token│
        │<─────────────────────────────────────────────────────────────┤
```

### The OIDC Handshake Algorithm
1.  **Request OIDC Token:** The GitHub Actions runner requests a JSON Web Token (JWT) from GitHub's OIDC Provider.
2.  **Issue JWT:** GitHub issues a signed JWT containing metadata about the active build job:
    *   `iss` (Issuer): `https://token.actions.githubusercontent.com`
    *   `aud` (Audience): `sts.amazonaws.com`
    *   `sub` (Subject): `repo:kmashour/BrainDump:ref:refs/heads/main`
3.  **Assume Role:** The runner calls the AWS Security Token Service (STS) API using the `AssumeRoleWithWebIdentity` method, presenting the JWT.
4.  **Verify Trust:** AWS checks the IAM Role's **Trust Relationship Policy** to verify the signature of GitHub's OIDC provider and check the subject string:
    ```json
    "Condition": {
      "StringEquals": {
        "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
      },
      "StringLike": {
        "token.actions.githubusercontent.com:sub": "repo:kmashour/BrainDump:*"
      }
    }
    ```
5.  **Issue STS Token:** If the checks pass, AWS issues temporary credentials (valid for 1 hour) to the runner, bypassing the need for static access keys.

---

## 🛡️ 3. Continuous Security Testing & Vulnerability Gating

### A. Repository Secret Scanning (TruffleHog)
TruffleHog scans the git commit history diff using regex matching and high-entropy detection algorithms (detecting random-looking strings that indicate keys). It validates identified keys against the provider's API (e.g. testing an AWS key against STS) to verify if it is active.

### B. Static Application Security Testing (SAST): SonarQube Quality Gates
SonarQube parses the application source code tree before compilation to build an Abstract Syntax Tree (AST). It scans this AST against known security vulnerability rules (CWEs) and code quality standards:
*   **Enforcing Gates:** The CI pipeline runs the scanner and queries the SonarQube API for the status of the Quality Gate. If the gate fails (e.g., security hotspots > 0, unit test coverage < 80%), the job fails, blocking promotion.

### C. Container Vulnerability Gating (Trivy)
Trivy scans container filesystems and application dependency package managers (e.g. `pip`, `npm`) against vulnerability databases (CVEs).
*   **Pipeline Configuration:**
    ```yaml
    - name: Run Trivy Scanner
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: myapp:${{ github.sha }}
        exit-code: '1' # Fails the pipeline if vulnerabilities are found
        severity: 'HIGH,CRITICAL'
        ignore-unfixed: true # Ignore CVEs that have no vendor patch available
    ```

---

## 📈 4. Advanced Deployment Patterns: Database Schema Migrations

### A. Blue-Green Deployment Database Migration (Expand/Contract Pattern)
If a Blue-Green deployment requires a database schema modification (e.g. renaming or splitting a database table column), you cannot apply the migration directly without risking downtime. If you migrate the database, the active old version (Blue) will fail. If you don't, the new version (Green) will fail.
*   **The Solution:** Use the **Expand and Contract (Parallel Run) Pattern**:
    1.  *Expand (Backward Compatible):* Apply a database migration that adds the new column alongside the old one. Update the application code (in Green) to write to *both* columns but read only from the old column.
    2.  *Deploy & Verify:* Deploy the Green environment.
    3.  *Transition:* Change the Green code to read from the new column. Once verified, switch user traffic from Blue to Green.
    4.  *Contract:* Apply a final database migration deleting the old column and tables.

### B. Canary Routing (Nginx Ingress Annotations)
Route a fraction of production traffic to the new version using an Nginx Ingress Controller. The ingress resource redirects traffic dynamically based on weight:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress-canary
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "10" # Routes exactly 10% of traffic to the canary service
spec:
  rules:
    - host: app.pwc.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: app-service-canary
                port:
                  number: 80
```

*See details on GHA execution in [[Reference Notes/9-1_github_actions_architecture_and_workflows]] and [[Reference Notes/9-4_github_actions_lecture_elfakharny]].*
