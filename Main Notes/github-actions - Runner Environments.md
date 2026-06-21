---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[github-actions]]"
sub_type: architecture
source_type: documentation
source_url: "https://docs.github.com/en/actions/hosting-your-own-runners"
author: "GitHub Ops"
course_title: "GitHub Actions Runner Infrastructure"
tags:
  - github-actions/runners
  - github-actions/deep-dive
---

# github-actions - Runner Environments

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[github-actions]] > **Runner Environments**

---

## 📑 Hosted vs. Self-Hosted Runner Topologies

Workflows execute on virtual or physical instances called Runners.

### 1. GitHub-Hosted Runners
*   **Provisioning:** GitHub manages the infrastructure. Each job executes inside a clean, fresh virtual machine instance.
*   **Security:** High filesystem isolation. Disk storage is wiped immediately after the job finishes.
*   **Use Cases:** General testing, image builds, public projects.

### 2. Self-Hosted Runners
*   **Provisioning:** You install the runner agent (`actions/runner`) on your own hardware, virtual machines, or local containers.
*   **Network Access:** Can securely access resources locked behind internal VPNs or firewalls (e.g. staging databases, local APIs).
*   **Security Warnings:** For public repositories, self-hosted runners present a significant remote code execution (RCE) risk. A PR from an unverified contributor can execute malicious code directly on your internal network. Use approval gates or ephemeral containers.

*Read more in [[Reference Notes/9-3_github_actions_administration_and_security.md#1-self-hosted-runner-administration-on-linux-hosts]]*
