---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - "github-actions"
concepts_referenced:
  - "[[github-actions]]"
difficulty: intermediate
status: completed
---

# Chapter 3: CI/CD Pipelines & DevSecOps Integration

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 3: CI/CD & DevSecOps**

---

## 🚀 1. Continuous Integration & Pipeline Architecture

Continuous Integration (CI) is the practice of automating the integration of code changes from multiple contributors into a single software project.

### A. GitHub Actions (GHA) Workflow Anatomy
*   **Workflows:** Automated procedures configured in `.github/workflows/` using YAML. Contains one or more **Jobs** that can run sequentially or concurrently.
*   **Triggers:** Events that trigger workflows (e.g. `push`, `pull_request`, `schedule` cron, or `workflow_dispatch` manual run).
*   **Runners:** The execution hosts where the jobs run:
    *   *GitHub-hosted Runners:* Clean virtual machines spawned on-demand by GitHub. Fast and secure but have no access to private resources (like a private AWS subnet).
    *   *Self-hosted Runners:* Virtual machines deployed and managed inside your private infrastructure. Ideal for accessing internal repositories or private subnets, but require manual scaling and security hardening to prevent host-level exploits.

### B. CI Pipeline Security: OIDC IAM Role Assumption
The legacy method of authenticating GitHub Actions with AWS involved creating an IAM User with administrator keys and saving them as GitHub secrets. This creates major credential leak and lifecycle rotation risks.
*   **The Modern Solution:** Use OpenID Connect (OIDC) to federate authentication.
*   **The Handshake:**
    1.  GHA requests an OIDC token (JWT) from GitHub's OIDC provider.
    2.  GHA calls AWS Security Token Service (STS) presenting the token and requesting to assume a specific IAM Role.
    3.  AWS verifies the GitHub OIDC provider signature and checks the Role's Trust Policy.
    4.  AWS issues temporary security credentials (valid for 1 hour) to the GHA runner.

---

## 🛡️ 2. DevSecOps: Security Gates Integration

The Job Description highlights "integrating security tools and vulnerability scanning." You must show how security checks act as gates in the pipeline.

### A. Static Application Security Testing (SAST): SonarQube
SAST inspects raw source code before compilation to identify security bugs, hardcoded secrets, and code smells.
*   **Integration:** Run SonarQube Scanner in the build job.
*   **Quality Gates:** A set of Boolean conditions (e.g., Code Coverage > 80%, 0 Critical Vulnerabilities, Security Rating = A). If any condition fails, the scanner returns an error, blocking the pipeline from proceeding to the build phase.

### B. Container Image Vulnerability Scanning: Trivy
Trivy scans container filesystems and application package lists for known vulnerabilities (CVEs).
*   **Placement:** Execute Trivy *after* the Docker image build but *before* pushing it to ECR.
*   **Blocking Builds:** Configure the Trivy CLI with `exit-code 1` and filter for `severity HIGH,CRITICAL`. If Trivy finds packages (like a vulnerable OpenSSL version in Alpine) matching these parameters, it forces the step to fail, preventing the deployment of a vulnerable image.

---

## 📈 3. Enterprise Deployment Strategies

In a Senior Associate interview, you must compare deployment patterns and justify which one to use based on target database migrations and risk tolerance.

### A. Blue-Green Deployments
*   **Mechanism:** Maintain two identical production environments (Blue is active, Green is idle). You deploy the new code to the Green environment. Once verified, you switch traffic (usually at the Route 53 DNS or Load Balancer level) from Blue to Green.
*   **Pros:** Near-zero downtime, instantaneous rollback (by switching DNS back to Blue).
*   **Cons:** Double the infrastructure cost. Handling active database schema migrations requires backward-compatible changes (expand and contract pattern).

### B. Canary Deployments
*   **Mechanism:** Roll out the new update to a tiny subset of production servers (e.g. 5% of traffic). You monitor error rates and latency. If metrics remain healthy, you incrementally scale up the rollout to 100%.
*   **Pros:** Minimizes blast radius. If a bug exists, only 5% of users experience it.
*   **Cons:** Complex traffic routing setups (requires weighted target groups or service mesh routing).
