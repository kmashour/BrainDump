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

---

## 🛠️ 4. Production-Grade Pipeline Implementation (GitHub Actions)

A true production-grade CI/CD pipeline enforces modularity, concurrency limits, credential security, build caching, and progressive testing stages.

```
+------------------+     +-----------------+     +-----------------+
| Lint & Hadolint  |     |   Unit Tests    |     | SAST/TruffleHog |
+--------┬---------+     +--------┬--------+     +--------┬--------+
         │                        │                       │
         +────────────────────────┼───────────────────────+
                                  ▼
                       +-------------------+
                       | Build & Trivy Scan|
                       +---------┬---------+
                                 ▼
                       +-------------------+
                       |   Push to ECR     |
                       +---------┬---------+
                                 ▼
                       +-------------------+
                       | Deploy Staging    |
                       +---------┬---------+
                                 ▼
                       +-------------------+
                       | Manual Gate (Prod)|
                       +---------┬---------+
                                 ▼
                       +-------------------+
                       | Deploy Production |
                       +-------------------+
```

### A. Complete Production YAML Definition

```yaml
# .github/workflows/production_pipeline.yml
name: Enterprise Production Pipeline

on:
  push:
    branches: [ main ]
    tags: [ 'v*.*.*' ]
  pull_request:
    branches: [ main ]

permissions:
  id-token: write # Required for AWS STS OIDC connection
  contents: read  # Required for checkout

jobs:
  # =========================================================================
  # PHASE 1: PRE-BUILD VALIDATION
  # =========================================================================
  lint-and-validate:
    name: Code Linting & Docker Validation
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source Code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install Linting Libraries
        run: |
          pip install flake8

      - name: Run Flake8 Linter
        run: |
          # stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

      - name: Lint Dockerfile (Hadolint)
        uses: hadolint/hadolint-action@v3.1.0
        with:
          dockerfile: Dockerfile
          ignore: DL3018 # Ignore apk pinning warnings in Alpine

  unit-testing:
    name: Parallel Unit Execution
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source Code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install Test Dependencies
        run: |
          pip install -r requirements.txt pytest pytest-cov

      - name: Run PyTest with Coverage
        run: |
          pytest --cov=app --cov-report=xml --cov-fail-under=80

  secret-and-sast-scanning:
    name: Credential & Code Security Scan
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source Code
        uses: actions/checkout@v4

      - name: Run TruffleHog Secret Scanner
        uses: trufflesecurity/trufflehog-actions@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          head: HEAD

      - name: Run SonarQube SAST Analysis
        uses: sonarsource/sonarqube-scan-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}

  # =========================================================================
  # PHASE 2: BUILD AND VULNERABILITY GATE
  # =========================================================================
  build-and-vulnerability-gate:
    name: Secure Container Compilation
    needs: [lint-and-validate, unit-testing, secret-and-sast-scanning]
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source Code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build Docker Image Locally (No Push)
        uses: docker/build-push-action@v5
        with:
          context: .
          load: true # Load image into local Docker daemon registry for scanning
          tags: local-scan-image:latest
          cache-from: type=gha # Cache layers on GitHub Actions
          cache-to: type=gha,mode=max

      - name: Scan Image with Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: local-scan-image:latest
          format: 'table'
          exit-code: '1' # Force pipeline failure on vulnerabilities
          ignore-unfixed: true
          severity: 'HIGH,CRITICAL'

  # =========================================================================
  # PHASE 3: SECURE REGISTRY REGISTRATION
  # =========================================================================
  publish-image:
    name: Push Hardened Image to AWS ECR
    needs: build-and-vulnerability-gate
    if: github.event_name == 'push' && (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/tags/v'))
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source Code
        uses: actions/checkout@v4

      - name: Configure AWS Credentials (OIDC Role assumption)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-actions-ecr-push-role
          aws-region: us-east-1

      - name: Log in to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v2

      - name: Set Image Tag
        run: |
          if [[ "${{ github.ref }}" == refs/tags/* ]]; then
            echo "IMAGE_TAG=${GITHUB_REF#refs/tags/}" >> $GITHUB_ENV
          else
            echo "IMAGE_TAG=sha-${GITHUB_SHA::8}" >> $GITHUB_ENV
          fi

      - name: Build and Push Tagged Image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ${{ steps.login-ecr.outputs.registry }}/etic-observability-app:${{ env.IMAGE_TAG }}
            ${{ steps.login-ecr.outputs.registry }}/etic-observability-app:latest
          cache-from: type=gha

  # =========================================================================
  # PHASE 4: STAGING DEPLOYMENT & SMOKE TESTS
  # =========================================================================
  deploy-to-staging:
    name: Deploy to Staging Environment
    needs: publish-image
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-actions-staging-deploy-role
          aws-region: us-east-1

      - name: Trigger Staging Helm Upgrade
        run: |
          aws eks update-kubeconfig --name staging-cluster --region us-east-1
          helm upgrade --install etic-app ./charts/etic-app \
            --namespace staging \
            --set image.tag=sha-${{ github.sha }}

      - name: Execute End-to-End Smoke Tests
        run: |
          # Loop check endpoint liveness
          curl -s --fail http://staging-app.pwc.internal/health || exit 1

  # =========================================================================
  # PHASE 5: CONTROLLED PRODUCTION PROMOTION
  # =========================================================================
  deploy-to-production:
    name: Deploy to Production Environment
    needs: deploy-to-staging
    runs-on: ubuntu-latest
    environment: 
      name: production
      url: https://app.pwc.com
    steps:
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-actions-production-deploy-role
          aws-region: us-east-1

      - name: Deploy Canary Rollout
        run: |
          aws eks update-kubeconfig --name production-cluster --region us-east-1
          helm upgrade --install etic-app ./charts/etic-app \
            --namespace production \
            --set image.tag=sha-${{ github.sha }} \
            --set canary.enabled=true
```

### B. Production Pipeline Mechanics Walkthrough

In the technical interview, walk the panel through these five structural controls:

1.  **Strict Concurrency Controls and Environments:**
    *   By defining `environment: production` in the last job, GitHub Actions automatically halts execution if the Environment has a **Required Reviewers (Manual Gate)** rule configured. The pipeline pauses until the DevOps Lead or Release Manager explicitly approves the run in the GitHub UI.
2.  **Concurrency Build Caching (`cache-from/to: type=gha`):**
    *   This directive stores compiled Docker layer cache objects inside GitHub's storage pool rather than caching locally. In subsequent pipeline runs, the runner pulls the cached build layers, reducing build times from minutes to seconds.
3.  **Dynamic Tagging (Tag vs Commit SHA):**
    *   If a developer pushes code, the pipeline tags the image with the short commit SHA (e.g. `sha-4a2b1c8f`).
    *   If a Git release tag is pushed (matching `v*.*.*`), the bash script extracts the tag string (e.g. `v1.2.0`) and tags the ECR image with it, maintaining an immutable audit history of software releases.
4.  **Security Fail-Safe Gateways:**
    *   **Unit Tests Gate:** PyTest requires `--cov-fail-under=80`. If code coverage falls to 79.9%, the step fails and blocks execution.
    *   **Vulnerability Scan Gate:** Trivy is configured with `exit-code 1` and scans the local image daemon. If any `HIGH` or `CRITICAL` CVE is detected in dependencies or the OS filesystem, the build terminates before ECR can receive the image.
5.  **Declarative Dependencies (`needs: [...]`):**
    *   By using the `needs` parameter, jobs run concurrently where possible (linting, testing, and secret scanning execute at the same time), but sequential execution is guaranteed for critical build/deploy steps, reducing resource wastage.

