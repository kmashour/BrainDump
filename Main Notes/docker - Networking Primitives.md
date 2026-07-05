---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[docker]]"
sub_type: core-concept
source_type: udemy
source_url: "https://www.udemy.com"
author: "Udemy Instructor"
course_title: "Docker and Containerization"
against: []
tags:
  - docker/networking
  - docker/deep-dive
---

# docker - Networking Primitives

**Breadcrumbs:** [[0-Index|🏠 Index]] > [[docker]] > **Networking Primitives**

---

## 📑 Docker Network Drivers & Port Forwarding

Docker maps networks on the host machine to isolate container communication.

### Network Drivers:
*   **Bridge Network:** Private virtual network isolated behind host NAT routing rules (iptables). Port forwarding is required to expose ports to external systems.
*   **Host Network:** Bypasses network namespace isolation. The container shares the host VM's IP address directly.
*   **None Network:** Disables networking completely for secure offline processing.

---

### Bridge Networking Mechanics Under the Hood

When Docker starts, it creates a virtual software switch called `docker0` bridge (default IP: `172.17.0.1/16`) using the host's bridge interface subsystem.

#### 1. Namespace Integration & virtual veth cables
- Each container executes in its own isolated network namespace.
- Docker connects this namespace to `docker0` by creating a virtual veth ethernet pair. One end binds to `docker0` (e.g. `vethxxxx`) and the other end is moved into the container namespace as `eth0`.
- Odd/even index numbers in `ip link` outputs denote the virtual cable pairs.

#### 2. The Namespace Directory Lookup Hack
Because Docker hides container namespaces from `/var/run/netns/` (making `ip netns list` return empty), you must link the process file manually to inspect using host CLI tools:
```bash
PID=$(docker inspect -f '{{.State.Pid}}' <container-name>)
mkdir -p /var/run/netns/
ln -sf /proc/$PID/ns/net /var/run/netns/<container-name>
ip netns exec <container-name> ip addr
```

#### 3. Port Mapping via iptables NAT Table
Because containers are inside private networks, external traffic cannot route to them directly. When mapping ports (e.g., `-p 8080:80`), Docker appends Destination NAT (DNAT) rules inside the `DOCKER` chain in the host's `iptables` `nat` table:
```bash
iptables -t nat -S DOCKER
```

*Read more in [2-4_docker_networking_and_compose.md](../Reference%20Notes/2-4_docker_networking_and_compose.md#1.1-bridge-networking-mechanics-under-the-hood)*
