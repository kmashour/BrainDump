---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[github-actions]]"
sub_type: core-concept
source_type: documentation
source_url: "https://docs.github.com/en/actions/security-guides"
author: "GitHub Security"
course_title: "GitHub Actions Security Hardening"
tags:
  - github-actions/security
  - github-actions/deep-dive
---

# github-actions - Security and Secrets

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[github-actions]] > **Security and Secrets**

---

## 📑 Security Architecture & Hardening Protocol

Security in CI/CD pipelines is critical to prevent code manipulation and credential leaks.

### 1. Minimal GITHUB_TOKEN Privileges
The default GITHUB_TOKEN generated for each job run can have write permissions. Restrict this globally by setting read-only defaults in the workflow:
```yaml
permissions:
  contents: read
  packages: write # Grant write permissions ONLY to jobs that need it
```

### 2. Immutable Dependency Pinning
Marketplace tags (e.g. `uses: actions/checkout@v4`) can be repointed to modified code. Pin actions to their immutable 40-character Git commit SHA to ensure execution safety:
```yaml
- name: Secure Checkout
  uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
```

### 3. Secretless Cloud Authentication (OIDC)
Instead of storing permanent cloud credentials (like AWS Access Keys) as GitHub Secrets, establish trust between GitHub Actions and your cloud provider using OpenID Connect (OIDC). GitHub issues a temporary JSON Web Token (JWT) that the runner presents to exchange for short-lived credentials from AWS STS or Google Cloud IAM.

*Read more in [[Reference Notes/9-3_github_actions_administration_and_security.md#2-deep-intuition-aarf-breakdowns-security-hardening]]*
