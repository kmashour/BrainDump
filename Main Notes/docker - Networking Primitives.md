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

*Read more in [2-4_docker_networking_and_compose.md](../Reference%20Notes/2-4_docker_networking_and_compose.md#1-network-drivers-in-docker)*
