---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Falco]]"
sub_type: core-concept
source_type: course_notes
source_url: "https://notes.kodekloud.com/docs/Certified-Kubernetes-Security-Specialist-CKS/Monitoring-Logging-and-Runtime-Security/Falco-Configuration-Files/page"
author: "KodeKloud"
course_title: "Certified Kubernetes Security Specialist (CKS)"
tags:
  - kubernetes/security
  - kubernetes/falco
  - kubernetes/deep-dive
---

# Falco - Rule Syntax and Alerting

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Falco]] > **Rule Syntax and Alerting**

---

## 📑 Falco Rule Syntax and Custom Rule Construction

Falco evaluates system call streams against declarative rules defined across `/etc/falco/falco_rules.yaml` (default upstream rules) and `/etc/falco/falco_rules.local.yaml` (custom user overrides).

### Core Fields of a Falco Rule
Every rule requires five fundamental elements:
1. `rule`: A descriptive, unique name for the rule.
2. `desc`: A short summary of what threat the rule detects.
3. `condition`: A boolean expression combining syscall event filters, process parameters, file descriptors, and container context.
4. `output`: The formatted message string dispatched when the rule matches, including interpolated variables (e.g. `%user.name`, `%proc.name`, `%container.id`).
5. `priority`: Syslog severity level (`EMERGENCY`, `ALERT`, `CRITICAL`, `ERROR`, `WARNING`, `NOTICE`, `INFO`, `DEBUG`).

### Modularizing with Lists and Macros
To maintain readable and reusable rules, conditions leverage **Lists** and **Macros**:

```yaml
# 1. Define a list of unauthorized binaries
- list: offensive_tools
  items: [nmap, masscan, sqlmap, netcat, nc]

# 2. Define a macro for container processes
- macro: container_proc
  condition: (container and container.id != host)

# 3. Formulate the comprehensive detection rule
- rule: Offensive Tool Executed in Container
  desc: Detect invocation of scanning or penetration testing tools inside a pod
  condition: >
    spawned_process and 
    container_proc and 
    proc.name in (offensive_tools)
  output: >
    Offensive security tool invoked (user=%user.name tool=%proc.name 
    cmdline=%proc.cmdline container=%container.name pod=%k8s.pod.name ns=%k8s.ns.name)
  priority: ALERT
  tags: [security, reconnaissance, mitre_execution]
```

*Read more in [[Reference Notes/0-7-6_runtime_security_falco_and_audit_logging.md#3-falco-runtime-threat-detection]].*
