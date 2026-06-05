---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[gitea]]"
sub_type: use-case
source_type: documentation
source_url: "https://gitea.com/gitea/act_runner"
author: "Gitea Actions Authors"
course_title: "Offline CI-CD Infrastructure"
tags:
  - git/gitea
  - cicd/act-runner
---

# gitea - Air-Gapped CI-CD Host Execution

**Breadcrumbs:** [[Index|🏠 Index]] > [[gitea]] > **Air-Gapped CI-CD Host Execution**

---

## 📑 Air-Gapped CI-CD Host Execution

By default, Gitea Actions utilizes Docker/Podman containers to isolate build environments. In an air-gapped environment with no internet access or local private registry, this setup fails because of missing external images.

### The Host Executor Setup
To resolve this "air-gap paradox", the Gitea Actions Runner (`act_runner`) is configured to run pipelines directly inside a native RHEL host shell.

```text
Gitea Actions Server ───(Polling)───> act_runner service ───(Spawns)───> Native Bash Shell (Host)
```

During registration, we configure the runner with a specific execution label:
* **Registration Label:** `rhel-native:host`
* **Interpretation:** Maps the label `rhel-native` to the `:host` executor, bypassing container calls.

---

## ⚠️ Security Trade-offs & Isolation
Running pipelines directly on the host host machine creates significant security implications compared to sandboxed container environments.

| Vector | Container Executor (Docker/Podman) | Host Executor (`:host`) |
| :--- | :--- | :--- |
| **Isolation** | Strong kernel namespaces | None. Runs as host process |
| **Privileges** | Limited root capabilities | Inherits runner's Linux system permissions |
| **Clean Slate** | Discards container state after build | Persists changes, risks side-effects |

### Mitigations
1. **Unprivileged Runner User:** Run the `act_runner` service under an unprivileged user (e.g., `act_runner`).
2. **Sudoers Restriction:** Do not grant the runner user passwordless `sudo` rights on the host VM.
3. **Systemd Limits:** Configure memory/CPU constraints (`MemoryLimit`, `CPUQuota`) in the Systemd service unit.

*Read more in [06_gitea_installation_and_workflows.md](../Reference%20Notes/06_gitea_installation_and_workflows.md#9-cicd-runner-architecture-host-execution)*
