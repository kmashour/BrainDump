---
domains:
  - "docker"
  - "infra"
---

# Module 2-3: Docker Volumes & Storage Mechanics

This module details persistent storage configurations in Docker. It covers the difference between host-mapped Bind Mounts, Docker-managed Named Volumes, and host-isolated Anonymous Volumes, along with filesystem merging/obscuring behaviors, volume lifecycle commands, and security vulnerabilities.

---

## 🗺️ Cognitive Map: Storage Types in Docker

```mermaid
graph TD
    subgraph HostFS["Host Filesystem"]
        HostDir["/home/user/data (Specific Host Directory)"]
        DockerStorage["/var/lib/docker/volumes/ (Docker Managed Area - Root Only)"]
    end

    subgraph ContainerMounts["Container Storage Mounts"]
        HostDir -->|Mount type: bind| Bind["Bind Mount (/app/data) <br> Obscures pre-existing container directory files"]
        DockerStorage -->|Mount type: volume| Named["Named Volume (/db/data) <br> Merges & copies pre-existing container files"]
        DockerStorage -->|Mount type: volume (auto-hash)| Anon["Anonymous Volume (/temp/cache) <br> Tied to container unless cleared via rm -v"]
    end
```

---

## 1. Docker Storage Drivers & Layered Filesystems

Docker uses **Storage Drivers** to maintain its layered image architecture and manage the filesystems of running containers.

### A. Layered Architecture & Read-Only Images
When building an image, Docker processes instructions in the Dockerfile sequentially, creating a separate, read-only layer for each step. 
* **Layer Sharing:** If multiple images share identical base instructions (e.g., identical base operating system and dependencies), Docker shares those read-only layers in cache to save disk space and accelerate builds.
* **Ephemeral Writable Layer:** When a container is started from an image, the runtime driver mounts a transient, read-write layer on top of the image's read-only layers. This container layer stores all modifications, logs, and temporary files created during the container's lifecycle.
* **Copy-on-Write (CoW) Mechanism:** Image layers are immutable. If a containerized process needs to modify a pre-existing file located in one of the read-only image layers, Docker automatically copies that file up into the container's read-write layer *before* saving the modifications. The container then operates on the copied version, leaving the original image layer untouched.

### B. Common Storage Drivers
The choice of storage driver dictates how these filesystem layers are managed. The selection depends on the underlying host operating system:
* **`overlay2`**: The modern, default storage driver for most Linux distributions (Ubuntu, Debian, RHEL). Highly efficient, fast, and does not require complex disk management.
* **`aufs`**: Legacy storage driver, historically popular on Debian/Ubuntu systems but largely succeeded by `overlay2`.
* **`devicemapper`**: Uses thin-provisioning block storage, historically used on CentOS/Fedora hosts where union filesystems were not natively supported.
* **`btrfs` / `zfs`**: Utilizes host filesystems with native copy-on-write features, suitable for systems where Docker partitions reside on Btrfs or ZFS disks.

### C. Volume Driver Plugins
While storage drivers manage transient filesystem layers, **Volume Driver Plugins** manage persistent volumes outside the layered union filesystem:
* **`local` (Default)**: Provisions storage folders locally on the host, defaulting to `/var/lib/docker/volumes/<volume-name>/_data`.
* **Third-Party Plugins**: Allow containers to connect directly to external network arrays, cloud storage systems, or SAN/NAS pools. Notable plugins include:
  * **REX-Ray**: Manages mounts for Amazon EBS, Amazon S3, Google Persistent Disk, OpenStack Cinder, or EMC arrays.
  * **Others**: Portworx, GlusterFS, NetApp, Convoy, Flocker, DigitalOcean Block Storage, and VMware vSphere Storage.

---

## 2. Storage Mount Primitives

Container images utilize a Union Filesystem (UFS) where layers are read-only. When a container runs, a transient, writable layer (ephemeral layer) is added on top. Any modification to container data resides in this writable layer and is destroyed when the container is deleted. To persist data or share it across environments, Docker provides three mount primitives:

### A. Bind Mounts
Map a user-defined directory or file on the host machine to a directory or file inside the container.
*   **Syntax:** `-v /home/user/app:/app` or `--mount type=bind,source=/home/user/app,target=/app`
*   **Best For:** Development environments (source code hot-reloading) and mounting host config files (e.g., `/etc/nginx/nginx.conf`).

### B. Named Volumes
Docker-managed storage located inside the host's protected filesystem.
*   **Default Path:** `/var/lib/docker/volumes/<volume_name>/_data` (Accessible only by root).
*   **Syntax:** `-v my_vol:/app` or `--mount type=volume,source=my_vol,target=/app`
*   **Best For:** Database engines and production file storage.

### C. Anonymous Volumes
Docker-managed storage where the volume is assigned a randomly generated hash name by the daemon.
*   **Syntax:** `-v /app/cache` or `--mount type=volume,target=/app/cache`
*   **Best For:** Decoupling write-heavy, transient files (caches, logs, temporary builds) from the container's writable layer to optimize filesystem performance.

---

## 2. Deep-Intuition (AARF) Breakdowns

### A. Named Volumes vs. Bind Mounts (Merging vs. Obscuring Files)
#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Utilize **Named Volumes** for application storage when initializing containers that contain pre-existing directory files (like default assets or configuration skeletons), reserving **Bind Mounts** for copying or replacing entire target directories.
2. **The Assumptions (Context):** The destination path inside the container must exist and contain files, and the named volume must be empty at the time of mounting.
3. **The Rationale (Why):** If you mount an empty **Named Volume** to a container directory containing files, Docker copies those files into the volume's host storage (`/var/lib/docker/volumes/.../_data`) on startup, establishing a two-way synchronization door. Conversely, if you mount a **Bind Mount** over a directory, the files on the host mask (obscure) the container's files, making them invisible, like mounting a USB drive over a populated directory.
4. **The Failure Loop (What if not):** Bind-mounting an empty host folder (e.g., `/var/www`) over an application container's pre-populated code directory (e.g., `/usr/share/nginx/html`) obscures all application code. Nginx starts up but serves empty directories or generates HTTP 403 Forbidden errors. There is no simple command to unmount a running container's bind mount to expose the hidden files again; the container must be destroyed and recreated.
5. **Alternative Case (When to use 'if not'):** If the host directory already contains the desired files (e.g., local HTML source files) and you want to override the default assets inside the container, a Bind Mount is the correct pattern.

### B. Anonymous Volumes Lifecycles & Dangling Resource Leakage
#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Remove containers along with their associated anonymous volumes using the `-v` flag during deletion (`docker rm -v <container_id>`), and configure automated cleanup tasks using `docker volume prune`.
2. **The Assumptions (Context):** The anonymous volume must not be shared or referenced by other containers using their hash identifier.
3. **The Rationale (Why):** When a container utilizing an anonymous volume is stopped, the volume remains on the host disk under `/var/lib/docker/volumes/<hash>/_data` to protect the data. Deleting the container using standard `docker rm` leaves the anonymous volume behind as a "dangling volume" with no associated container pointer.
4. **The Failure Loop (What if not):** In systems running automated tests or CI pipelines where containers are continuously created, stopped, and removed without the `-v` flag, anonymous volumes leak disk space. Over time, hundreds of orphaned hash directories accumulate in the host filesystem, exhausting storage and leading to host disk failures.
5. **Alternative Case (When to use 'if not'):** If you want to rescue data from an anonymous volume before deleting the container, you must inspect the container (`docker inspect`) to retrieve the volume's hash name, copy the files out of `/var/lib/docker/volumes/<hash>/_data`, and then perform a standard cleanup.

### C. Host Socket & Root Filesystem Bind Mount Vulnerabilities
#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Avoid bind-mounting the host's root filesystem (`/`) or the Docker socket (`/var/run/docker.sock`) inside production containers. If a bind mount is required, mount it as read-only (`:ro`).
2. **The Assumptions (Context):** Container security boundaries depend on namespaces. The container must run as a non-privileged user to limit host access.
3. **The Rationale (Why):** Mounting `/var/run/docker.sock` exposes the Docker API. A container process communicating with the socket can send API calls directly to the host's Docker daemon. Since the daemon runs as root on the host, the container can issue commands to run new containers, mount the host root filesystem, and execute commands as host root.
4. **The Failure Loop (What if not):** If a container running a monitoring tool with a writable Docker socket mount is compromised by an external attacker, the attacker can leverage the socket to escape container isolation. By executing `docker run -v /:/host ...`, the attacker gains write access to the host's filesystem, modifies system files (e.g., `/etc/shadow`), elevates host privileges, and compromises the physical host.
5. **Alternative Case (When to use 'if not'):** Administrative tools (e.g., Portainer, Traefik, or Prometheus node exporters) require socket access to monitor container lifecycles. In these cases, use specific SELinux or AppArmor profiles, run the daemon in rootless mode, or apply read-only restrictions to the socket bindings.

---

---

## 📖 Detailed Study: Docker Deep Dive (Nigel Poulton)

# 13: Volumes and persistent data

## Volumes and persistent data - The TLDR

two main categories of data — persistent and non-persistent.

### Volumes and persistent data - The Deep Dive

#### Containers and non-persistent data

- Containers are designed to be immutable
- many applications require a read-write filesystem in order to simply run – they won’t even run on a read-only filesystem.
- Every Docker container is created by adding a thin read-write layer on top of the read-only image it’s based on
- The writeable layer is called many names: _local storage_, _ephemeral storage_, and _graphdriver storage_.
- It’s typically located on the Docker host in these locations:
    - Linux Docker hosts: `/var/lib/docker/<storage-driver>/...`
    - Windows Docker hosts: `C:\ProgramData\Docker\windowsfilter\...`
- it gets created when the container is created and it gets deleted when the container is deleted
- Managed on Docker host using a storage driver (Ubuntu: `overlay2` or `aufs`. `overlay2` is recommended)

![[../Attachments/docker_deep_dive_50.png]]

#### Containers and persistent data

- _Volumes_ are the recommended way to persist data in containers.
    - Volumes are independent objects that are not tied to the lifecycle of a container
    - Volumes can be mapped to specialized external storage systems
    - Volumes enable multiple containers on different Docker hosts to access and share the same data

1. Create a volume
2. Create a container 
3. Mount the volume into it 
4. The volume is mounted into a directory in the container’s filesystem
5. Anyhing written to that directory is stored in the volume
6. If you delete the container, the volume and its data will still exist.

![[../Attachments/docker_deep_dive_51.png]]

### Creating and managing Docker volumes

To create a volume using `local` driver:  
`$ docker volume create myvol`

Third-party volume drivers are available as plugins (Cloud, SAN, NAS, etc.)

![[../Attachments/docker_deep_dive_52.png]]

To Inspect a volume:  
`$ docker volume inspect myvol`

Two ways to delete a Docker volume:  
- Remove all volumes not used by any container: `$ docker volume prune`
- Choose which volume to remove: `$ docker volume rm <volume-name>`

#### Volumes in Dockerfiles

- it’s also possible to deploy volumes via Dockerfiles using the VOLUME instruction
- The format is `VOLUME <container-mount-point>`
- you cannot specify a directory on the host when defining a volume in a Dockerfile

#### Demonstrating volumes with containers and services

- `$ docker container run -dit --name voltainer --mount source=bizvol,target=/vol alpine`
- `$ docker volume ls`
- `$ docker volume rm bizvol`    /// error

Write something to volume:  
- `$ docker container exec -it voltainer sh`
    - `# echo "I Think Therefore I Am" > /vol/file1`
    - `# cat /vol/file1`
    - `# exit`
- `$ docker container rm voltainer -f`
- `$ docker volume ls`
- `$ ls -l /var/lib/docker/volumes/bizvol/_data/`

Create another container and attach it to the previous volume:  
- `$ docker run --name hellcat --mount source=bizvol,target=/vol alpine sleep 1d`

### Sharing storage across cluster nodes

![[../Attachments/docker_deep_dive_53.png]]

Docker Hub is the best place to find volume plugins



## Volumes and persistent data - The Commands

- `docker volume create`  /// create new volumes.
- `docker volume ls`  /// list all volumes on the local Docker host.
- `docker volume inspect`  /// shows detailed volume information.
- `docker volume prune`  /// delete all volumes that are not in use by a container or service replica. Use with caution!
- `docker volume rm`   /// deletes specific volumes that are not in use.
- `docker plugin install`  /// install new volume plugins from Docker Hub.
- `docker plugin ls`  /// lists all plugins installed on a Docker host.





----

---

## 3. Practical Verification & Volume CLI Syntax

```bash
# 1. Create a Docker-managed named volume
docker volume create my_data

# 2. Inspect the volume details to locate the mount point
docker volume inspect my_data
```
**Output JSON:**
```json
[
    {
        "CreatedAt": "2026-06-11T19:26:00Z",
        "Driver": "local",
        "Mountpoint": "/var/lib/docker/volumes/my_data/_data",
        "Name": "my_data",
        "Scope": "local"
    }
]
```

### A. Lifecycle Operations Reference:
*   `docker volume ls`: Lists all local volumes (both named and anonymous hash volumes).
*   `docker run -d -v my_data:/usr/share/nginx/html:ro nginx`: Runs Nginx mounting the named volume as read-only.
*   `docker run -d -P nginx`: Automatically opens ports and creates anonymous volumes for any `VOLUME` paths declared in the image's Dockerfile.
*   `docker volume rm my_data`: Deletes the named volume. This fails if any container (running or stopped) is still attached to the volume.
*   `docker volume prune`: Cleans up all dangling volumes (volumes not connected to any existing containers).
