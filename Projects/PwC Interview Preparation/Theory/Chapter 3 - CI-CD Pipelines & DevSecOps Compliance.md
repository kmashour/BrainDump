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

# Chapter 3: Secure CI/CD Pipelines & DevSecOps Compliance

**Breadcrumbs:** [[Projects/PwC Interview Preparation/Plan - DevOps Interview Roadmap|DevOps Interview Roadmap]] > Theory > **Chapter 3: CI/CD & DevSecOps**

---

## 🚀 1. Pipeline Modularity and Trigger Controls

In an enterprise CI/CD setup, you must implement selective triggers to conserve build resources and maintain deployment isolation.

### A. Dynamic Workflow Triggers
Configure trigger events to prevent redundant execution:
*   **Path Filtering:** Trigger workflows only when changes occur in specific directories:
    ```yaml
    on:
      push:
        branches: [ main ]
        paths:
          - 'app/**'
          - 'Dockerfile'
    ```
*   **Pull Request Gating:** Run tests on PR creation, but restrict deployment actions exclusively to merges on the target branch (using `if: github.event_name == 'push'`).

### B. Runner Architectures
*   **GitHub-Hosted Runners:** Spawned in clean VMs by GitHub. Good for standard linting and testing, but have no access to your private virtual networks (like private subnets in AWS).
*   **Self-Hosted Runners:** Virtual machines running the GitHub runner agent deployed inside your private VPC. Enables the runner to execute deployments directly (e.g. running Helm commands against a private EKS endpoint) without opening the cluster API to the public internet. Require hardening (using ephemeral runners, clearing workspaces after execution) to prevent persistent security threats.

---

## 🛡️ 2. DevSecOps: Automated Security Gates

The PwC Job Description heavily emphasizes "continuous security testing and vulnerability scanning."

### A. Secret Scanning Gate (Pre-Commit & CI)
Accidental check-ins of API keys, AWS credentials, or DB strings represent a major compliance failure.
*   **The Control:** Run **TruffleHog** or **GitGuardian** in the pipeline. These scanners inspect the git history diff for high-entropy strings and signatures matching known cloud providers.
*   **Action:** If a secret is detected, the job aborts, preventing the commit from being merged.

### B. Static Application Security Testing (SAST): SonarQube
*   **Function:** Inspects raw source code for security vulnerabilities (e.g., SQL injection pathways, unsafe package deserialization, XSS hotspots) and computes code metrics (duplication, complexity, code coverage).
*   **Quality Gate Enforcement:** Configure a SonarQube Quality Gate. If the code coverage is below 80% or if security hotspots are introduced, the quality gate fails. The GHA pipeline fails, blocking promotion to staging.

### C. Container Image Scanning: Trivy
*   **Function:** Scans the built Docker image filesystem for OS package and application dependency vulnerabilities (CVEs).
*   **Pipeline Gate Integration:** Run Trivy in the CI pipeline after building the local image. Configure it to fail the build on critical vulnerabilities:
    ```yaml
    - name: Run Trivy scan
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: myapp:latest
        exit-code: '1' # Fails the pipeline run
        severity: 'HIGH,CRITICAL'
        ignore-unfixed: true # Ignore CVEs that have no fix patch available yet
    ```

---

## 🌎 3. OIDC AWS Federated Authentication (Secretless CI)

Avoid saving static AWS Access Keys in GitHub Secrets. Use OIDC federation instead.
1.  **Configure Identity Provider:** Establish an OIDC provider trust between GitHub and AWS IAM.
2.  **IAM Role Trust Policy:** The IAM Role in AWS specifies that only your GitHub repository and branch can assume it:
    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Federated": "arn:aws:iam::123456789012:oidc-provider/token.actions.githubusercontent.com"
          },
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Condition": {
            "StringEquals": {
              "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
            },
            "StringLike": {
              "token.actions.githubusercontent.com:sub": "repo:kmashour/BrainDump:*"
            }
          }
        }
      ]
    }
    ```
3.  **STS Token Exchange:** The GHA runner uses the temporary web identity token issued by GitHub to call the AWS Security Token Service (`sts:AssumeRoleWithWebIdentity`) and receives short-lived credentials.

---

## 📈 4. Enterprise Progressive Deployment Strategy

Compare deployment topologies to demonstrate release management maturity:

### A. Blue-Green Deployment Routing
*   **Mechanism:** Deploy version $N+1$ to the idle environment (Green). Once smoke tests pass, switch traffic at the load balancer target group level or Route 53 weighted record level to Green. Blue is kept intact for instant rollbacks.
*   **Database Schema Challenges:** If the database schema changes, the database must support *both* Blue and Green code versions simultaneously. Use the **Expand/Contract Pattern**:
    1.  *Expand:* Apply database migrations to support new columns (making sure old code still runs).
    2.  *Deploy:* Deploy Green.
    3.  *Contract:* Once stable, delete the legacy database columns and old schema components.

### B. Canary Deployment Rollout
*   **Mechanism:** Route a small percentage of traffic (e.g. 5%) to the new version $N+1$. Monitor application error rates, response latencies, and system crashes. If healthy, scale the routing dynamically (25% -> 50% -> 100%).
*   **Helm Canary Setup:** Managed Kubernetes deployments (EKS/GKE) utilize ingress controllers (like Nginx Ingress or AWS Load Balancer Controller) configured with annotation annotations (e.g. `nginx.ingress.kubernetes.io/canary-weight: "10"`) to segment traffic.

*See complete pipeline scripts in [[Reference Notes/9-1_github_actions_architecture_and_workflows]] and [[Reference Notes/9-4_github_actions_lecture_elfakharny]].*
