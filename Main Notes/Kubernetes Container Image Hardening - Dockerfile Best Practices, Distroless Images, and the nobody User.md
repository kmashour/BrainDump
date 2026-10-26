---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Supply Chain Security and Artifact Integrity]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Workload Hardening"
tags:
  - kubernetes/security
  - kubernetes/supply-chain
  - kubernetes/dockerfile
  - kubernetes/distroless
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Container Image Hardening: Dockerfile Best Practices, Distroless Images, and the nobody User

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Main Notes/Kubernetes Supply Chain Security and Artifact Integrity|Kubernetes Supply Chain Security and Artifact Integrity]] > **Kubernetes Container Image Hardening: Dockerfile Best Practices, Distroless Images, and the nobody User**

---

## 💀 1. The Supply Chain Threat Model: Image Bloat & Default Root

In cloud-native architectures, an attacker does not need to bypass network firewalls or kernel isolation if they can compromise an application via its container image. The container image represents the foundation upon which all runtime security controls rest.

When an image is constructed with standard developer patterns:
```dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y gcc make curl python3 git
COPY app /app
CMD ["/app/server"]
```
It introduces three severe security vulnerabilities into the production cluster:

```
+-----------------------------------------------------------------------------------------------+
|                            CONTAINER IMAGE ATTACK SURFACE RISKS                               |
+-----------------------------------------------------------------------------------------------+
| RISK                      | MECHANICS                               | THREAT IMPACT                   |
+---------------------------+-----------------------------------------+---------------------------------+
| Default Root Execution    | Omitting the USER directive defaults   | An application RCE arrives on   |
|                           | container PID 1 to UID 0 (root).        | the host kernel with root privs.|
+---------------------------+-----------------------------------------+---------------------------------+
| Living Off The Land       | Image includes compilers (gcc, make)    | Attackers compile kernel        |
|                           | and download utilities (curl, wget).    | rootkits in-memory inside pod.  |
+---------------------------+-----------------------------------------+---------------------------------+
| Package Manager Poisoning | Image includes package managers         | Attackers can dynamically       |
|                           | (apt, apk, yum) inside production pod.  | install nmap, netcat, or hydra. |
+---------------------------+-----------------------------------------+---------------------------------+
| Interactive Shell Access  | Standard bases include /bin/sh and      | Allows trivial reverse-shell    |
|                           | /bin/bash shells.                       | connections to external C2.     |
+-----------------------------------------------------------------------------------------------+
```

---

## 🛡️ 2. Architectural Remedies: Multi-Stage Builds & Distroless Bases

To eliminate build tools, package managers, and shells from production artifacts, production pipelines implement **Multi-Stage Builds** coupled with **Distroless** or **Scratch** base layers:

```
+-----------------------------------------------------------------------------------+
|                           MULTI-STAGE BUILD ARCHITECTURE                          |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ STAGE 1: Builder Stage ] (Temporary, discarded after compilation)              |
|  FROM golang:1.22-alpine AS builder                                               |
|  - Contains compilers, git, package managers, build dependencies                  |
|  - Compiles source code into static binary: /build/server                         |
|                                                                                   |
|         │ (Only the compiled static binary is copied across)                      |
|         ▼                                                                         |
|                                                                                   |
|  [ STAGE 2: Production Stage ] (Minimal runtime layer)                            |
|  FROM gcr.io/distroless/static-debian12 OR scratch                                 |
|  COPY --from=builder /build/server /server                                        |
|  USER 65534:65534                                                                 |
|  ENTRYPOINT ["/server"]                                                           |
|                                                                                   |
|  * Result: No shell (/bin/sh and /bin/bash do NOT exist)                          |
|  * Result: No package manager (apt/apk do NOT exist)                              |
|  * Result: Attackers cannot spawn interactive reverse shells                      |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

---

## 👤 3. The `nobody` User Dilemma: UID 65534 vs 65535

In Unix and Linux systems, **`nobody`** is a standardized user account historically designed for running unprivileged software (such as NFS daemons) without administrative capabilities.

```
+-------------------------------------------------------------------------------------------------------+
|                                    THE "nobody" USER SPECIFICATION                                    |
+-------------------------------------------------------------------------------------------------------+
| OPERATING SYSTEM / DISTRO  | USERNAME   | UID       | GID       | ARCHITECTURAL CONTEXT               |
+----------------------------+------------+-----------+-----------+-------------------------------------+
| Linux Standard (Ubuntu,    | nobody     | 65534     | 65534     | Standard unprivileged UID.          |
| Debian, Alpine Linux)      |            |           | (nogroup) | Defined in /etc/passwd.             |
+----------------------------+------------+-----------+-----------+-------------------------------------+
| Legacy BSD / OpenBSD       | nobody     | 65535     | 65535     | Historically 2^16 - 1 (overflows on |
|                            |            |           |           | older 16-bit Unix UID types).       |
+----------------------------+------------+-----------+-----------+-------------------------------------+
```

### The Dockerfile Directive: Name vs Numeric UID
In a Dockerfile, you can define:
```dockerfile
USER nobody
```
OR:
```dockerfile
USER 65534
```

> [!IMPORTANT]
> **Why Numeric UID is Superior in Kubernetes:**
> Kubernetes Pod Security Standards (PSS) and policy scanners (Trivy, Kubescape, Kyverno) strongly favor **numeric UIDs** (`USER 65534`).
> When a string name (`USER nobody`) is specified, the Kubernetes API Server and Kubelet cannot determine if the user is non-root without inspecting the container's internal `/etc/passwd` file inside the image layer. Using an explicit numeric UID allows Kubelet to validate `runAsNonRoot: true` instantly without image layer extraction.

---

## 🎯 4. Real Exam Question 03: Problem & Solution Blueprint

### Problem Statement
In directory `/opt/course/docker/`:
1. Modify `Dockerfile` so that the image executes under an unprivileged user (`USER nobody` or `USER 65534`).
2. Update the companion Kubernetes Deployment `deployment.yaml` in namespace `production-workloads` to:
   - Run as non-root user (`runAsUser: 65535` or unprivileged UID).
   - Enforce read-only root filesystem (`readOnlyRootFilesystem: true`).
   - Prevent privilege escalation (`allowPrivilegeEscalation: false`).
   - Strip `privileged: true` (ensure `privileged: false` or omitted).
3. Apply the updated deployment to `production-workloads`.

### Part 1: Hardened `Dockerfile`
```dockerfile
FROM alpine:3.19
# Set non-root unprivileged execution
USER nobody
CMD ["sleep", "3600"]
```

### Part 2: Hardened Kubernetes `deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: couchdb-service
  namespace: production-workloads
spec:
  replicas: 1
  selector:
    matchLabels:
      app: couchdb-service
  template:
    metadata:
      labels:
        app: couchdb-service
    spec:
      containers:
      - name: couchdb
        image: alpine:3.19
        command: ["sleep", "3600"]
        # HARDENED CONTAINER SECURITY CONTEXT:
        securityContext:
          runAsUser: 65535
          readOnlyRootFilesystem: true
          allowPrivilegeEscalation: false
          privileged: false
```

### Part 3: Terminal Application & Verification
```bash
# 1. Apply the manifest
kubectl apply -f /opt/course/docker/deployment.yaml

# 2. Verify Pod running status
kubectl get pods -n production-workloads
```

---

## 🔍 5. Terminal Forensics: Auditing Runtime Identity & Immutability

After deployment, confirm the hardened posture directly inside the live container:

### Check 1: Verify Effective UID
```bash
kubectl exec -n production-workloads <pod-name> -- id
```
*Expected Output:*
```text
uid=65535 gid=0(root) groups=0(root)
```
*(Confirms PID 1 is executing under an unprivileged user ID, not UID 0)*.

### Check 2: Verify Root Filesystem Immutability
```bash
kubectl exec -n production-workloads <pod-name> -- touch /root/malware.sh
```
*Expected Output:*
```text
touch: /root/malware.sh: Read-only file system
```
*(Confirms `readOnlyRootFilesystem: true` successfully blocks attackers from writing files, dropping scripts, or compiling payloads)*.

---

## ⚡ 6. Exam Pitfalls & Best Practices Checklist

1. **Do Not Put Container Fields at Pod Level:**
   `readOnlyRootFilesystem` and `allowPrivilegeEscalation` belong strictly under `spec.containers[*].securityContext`. Placing them under `spec.securityContext` triggers a schema validation error.
2. **Handle Writable Ephemeral Paths:**
   If an application requires temporary scratch space (e.g., `/tmp`), pair `readOnlyRootFilesystem: true` with an `emptyDir` volume mount at `/tmp`.
3. **Double Verification:**
   Always run `kubectl exec ... -- id` and `touch /test` to ensure the pod is genuinely functional and hardened before moving to the next exam task.

---

## 🔗 Related Master Notes & References
- Parent Landing Note: [[Main Notes/Kubernetes Supply Chain Security and Artifact Integrity|Kubernetes Supply Chain Security and Artifact Integrity]]
- Workload Hardening: [[Main Notes/Kubernetes Container Hardening - Immutability, SecurityContext Trinity, and Multi-Container Configurations|Container Hardening Trinity & Immutability]]
- Sandboxed Runtimes: [[Main Notes/Kubernetes Sandboxed Runtimes - gVisor, Kata Containers, and the 3-Layer RuntimeClass Chain|Sandboxed Runtimes: gVisor, Kata Containers & RuntimeClass]]
- Reference Guide: [[Reference Notes/0-7-5_supply_chain_security_and_imagepolicywebhook.md|Module 0-7-5: Supply Chain Security & ImagePolicyWebhook Masterclass]]
