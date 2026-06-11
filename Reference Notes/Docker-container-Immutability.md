---
tags:
  - Docker
Type: Reference Note
source: GPT
page: "[[Docker-Containers-Operations]]"
Date: 2025-04-20T14:02:00
deadline: 
status:
---

⚙️ 1. **Containers Are Immutable Once Created**


❌ Why You Can't Change Ports/Volumes Later
📌 Port Mapping
Mapped at container creation through Docker's network stack.

Changing it would mean changing how Docker's internal virtual network is wired, which is not allowed dynamically.

Docker doesn’t support re-wiring existing containers to new host ports.

📌 Volumes
Bound to the container at startup.

Attaching a new volume after the fact would require Docker to inject new mount points into the container's namespace, which isn’t supported.

It would also risk data corruption if the app inside already initialized path


## 🧠 Why Docker Does It This Way (Philosophically)

Docker treats containers as **ephemeral** and **replaceable**. The idea is:

> Don’t fix containers. Recreate them.

This makes things:

- **Repeatable** (same `docker run` always creates the same environment)
    
- **Predictable** (no surprises or mismatched config)
    
- **Declarative** (think infrastructure-as-code)External sources citation Books articles Research papers blogs video-courses courses lectures 