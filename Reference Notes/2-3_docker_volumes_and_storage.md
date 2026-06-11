---
domains:
  - "docker"
  - "infra"
---

# Module 2-3: Docker Volumes & Storage Mechanics

This module details persistent storage configurations in Docker. It covers the difference between host-mapped Bind Mounts, Docker-managed Named Volumes, and host-isolated Anonymous Volumes, along with implementation syntax and security concerns.

---

## 🗺️ Cognitive Map: Storage Types in Docker

```mermaid
graph TD
    subgraph HostFS["Host Filesystem"]
        HostDir["/home/user/data (Specific host directory)"]
        DockerStorage["/var/lib/docker/volumes/ (Docker Managed Area)"]
    end

    subgraph ContainerMounts["Container Storage Mounts"]
        HostDir -->|Mount type: bind| Bind["Bind Mount (/app/data)"]
        DockerStorage -->|Mount type: volume| Named["Named Volume (/db/data)"]
        DockerStorage -->|Mount type: volume (auto-id)| Anon["Anonymous Volume (/temp/cache)"]
    end
```

---

## 1. Storage Mount Primitives

Containers have an ephemeral writable layer. To persist data outside this lifecycle, Docker provides three mount primitives:

### A. Bind Mounts
Map a user-specified directory on the host machine directly to a directory inside the container.
*   **Syntax:** `-v /home/user/app:/app` or `--mount type=bind,source=/home/user/app,target=/app`
*   **Best For:** Development environments (code hot-reloading).

### B. Named Volumes
Docker-managed storage located inside the host's protected filesystem (e.g., `/var/lib/docker/volumes/my_vol/_data`).
*   **Syntax:** `-v my_vol:/var/lib/docker/volumes` or `--mount type=volume,source=my_vol,target=/var/lib/docker/volumes`
*   **Best For:** Production database storage.

### C. Anonymous Volumes
Similar to named volumes, but Docker automatically assigns a unique hash name.
*   **Syntax:** `-v /app/cache`
*   **Best For:** Decoupling write-heavy transient cache files from the container writable layer.

---

## 2. Deep-Intuition (AARF) Breakdown of Storage Selection

Choosing the incorrect storage type compromises cluster scalability and host security.

### A. Named Volumes for Database Persistence
#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Deploy databases (e.g., PostgreSQL) utilizing Docker-managed **Named Volumes**:
    `docker run -d --name pg-db -v pg_data:/var/lib/postgresql/data postgres`
2. **The Assumptions (Context):** The host OS storage subsystem must support the required IOPS, and host directories do not need direct user-level modifications.
3. **The Rationale (Why):** Named volumes are isolated from host-level user interference, have optimized drivers for storage performance, and persist independently of container destruction.
4. **The Failure Loop (What if not):** Storing database files directly inside the container's writable layer results in complete data loss when the container is deleted (`docker rm`). If database files are mapped via a Bind Mount on a shared network drive (NFS), concurrent file locks cause database indexing corruption and data crashes.
5. **Alternative Case (When to use 'if not'):** For lightweight dev testing where persistence is not required, anonymous volumes or temporary storage (`--tmpfs`) can be used to speed up disk I/O.

### B. Bind Mount Security Risks
#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Restrict Bind Mounts to read-only mode in production, or replace them with Named Volumes:
    `docker run -d -v /var/conf:/etc/conf:ro nginx`
2. **The Assumptions (Context):** The host directory path must exist before container startup (otherwise Docker might create it as an empty directory owned by root).
3. **The Rationale (Why):** Bind mounts expose the host's directory structure to the container. If the container process runs as root, it can modify files on the host with root privileges.
4. **The Failure Loop (What if not):** Mapping the host's root system or socket (`-v /:/host` or `-v /var/run/docker.sock:/var/run/docker.sock`) inside a container allows a compromised container process to execute host binaries, elevate privileges to host root, and compromise the entire VM node.
5. **Alternative Case (When to use 'if not'):** Administrative tools (like Portainer or monitoring agents) require bind-mounting the host's socket `/var/run/docker.sock` to manage containers, but these must be locked down using secure profiles.

---

## 3. Practical Verification: Volume Inspection

*   **Create Volume:** `docker volume create my_vol`
*   **Inspect metadata:** `docker volume inspect my_vol`
    ```json
    [
        {
            "CreatedAt": "2026-06-11T19:26:00Z",
            "Driver": "local",
            "Mountpoint": "/var/lib/docker/volumes/my_vol/_data",
            "Name": "my_vol",
            "Scope": "local"
        }
    ]
    ```
*   **Cleanup unused volumes:** `docker volume prune`
