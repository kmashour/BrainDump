---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[gitea]]"
sub_type: use-case
source_type: documentation
source_url: "https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks"
author: "Git Core Team"
course_title: "Git Server Administration"
tags:
  - git/gitea
  - git/hooks
---

# gitea - Branch Governance and Git Hooks

**Breadcrumbs:** [[Index|🏠 Index]] > [[gitea]] > **Branch Governance and Git Hooks**

---

## 📑 Branch Governance and Git Hooks

Server-side Git hooks allow administrators to intercept and analyze code pushes before they are committed to the filesystem, enforcing structural standards across teams.

### 1. Enabling Git Hooks
By default, Gitea restricts Git hooks via its administrative settings to prevent unauthorized remote command execution. You must enable them in Gitea's primary configuration:

```ini
# /etc/gitea/app.ini
[security]
DISABLE_GIT_HOOKS = false
```

---

## 🛑 The `pre-receive` Validation Logic

The `pre-receive` hook script executes on the server after authentication but before the repository ref pointer is updated.

### Execution Scope
1. Receives three arguments via standard input: `oldrev` (previous commit hash), `newrev` (target commit hash), and `refname` (ref path, e.g. `refs/heads/master`).
2. Isolates branches from tags.
3. Excludes squashed pull-request merges to the `master` branch.
4. Audits the branch name against a regex rule:
   - Valid Prefixes: `newtool/`, `bugfix/`, `update/`
5. Returns exit code `1` (Reject) if validation fails, printing custom diagnostic notifications directly to the developer's console.

```bash
# Example push rejection output
🚫 FATAL VODAFONE TAT ERROR: Invalid Branch Name! 🚫
You tried to push a branch named: 'feature_x'
RULE: Your branch must start with one of the following:
  - newtool/
  - bugfix/
  - update/
```

*Read more in [06_gitea_installation_and_workflows.md](../Reference%20Notes/06_gitea_installation_and_workflows.md#10-enterprise-branch-governance--git-hooks)*
