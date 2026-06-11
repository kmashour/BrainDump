---
domains:
  - "docker"
  - "infra"
---

# Module 2-4: Docker Networking & Multi-Container Compose

This module details how Docker manages container network namespaces, virtual interface adapters, and multi-container stacks. It covers core network drivers, automatic name resolution differences, port mapping iptables mechanics, and multi-container orchestration using Docker Compose.

---

## 🗺️ Cognitive Map: Bridge vs. Host vs. Macvlan Networking

```mermaid
graph TD
    subgraph HostSystem["Host Physical Machine (IP: 192.168.1.100)"]
        direction TB
        HostNIC["Host Network Interface (eth0)"]
        
        subgraph DefaultBridge["Default Bridge Network (docker0 / 172.17.0.1)"]
            ContA["Container A (IP: 172.17.0.2)"] <-->|veth pair| DefaultBridge
            ContB["Container B (IP: 172.17.0.3)"] <-->|veth pair| DefaultBridge
            ContA <-->|Direct IP Communication Only <br> No DNS Name Resolution| ContB
        end

        subgraph UserBridge["User-Defined Bridge Network (10.0.0.0/16)"]
            ContC["Container C (IP: 10.0.0.2)"]
            ContD["Container D (IP: 10.0.0.3)"]
            ContC <-->|Automatic DNS Resolution <br> Ping by Name| ContD
        end

        subgraph HostMode["Host Network Driver"]
            ContE["Container E"] <-->|Direct Stack Bind <br> Uses Host Port 80| HostNIC
        end

        subgraph MacvlanMode["Macvlan Network Driver"]
            ContF["Container F <br> IP: 192.168.1.150 <br> Custom MAC Address"] <-->|Bypasses NAT / Layer 2| HostNIC
        end
    end
    
    DefaultBridge <-->|Port Mapping: -p 8080:80 <br> Host iptables NAT Rules| HostNIC
    UserBridge <-->|Internet Gateway| HostNIC
```

---

## 1. Network Drivers in Docker

Docker uses namespaces to isolate network stacks (routing tables, interfaces, port binds). Containers communicate via virtual drivers:

*   **`bridge` (Default):** Creates a virtual software bridge (`docker0`) on the host. When a container starts, a virtual ethernet interface pair (veth) is created. One end binds to the host's `docker0` bridge; the other end is injected into the container's network namespace as `eth0`.
*   **`host`:** Disables network namespace isolation. The container shares the host's network interfaces, hostname, and port spaces directly.
*   **`none`:** Creates a container with only a loopback interface (`127.0.0.1`), completely blocking network input/output.
*   **`macvlan`:** Assigns a unique MAC address and a physical network IP directly to the container. It connects the container to the host's physical network, bypassing NAT routing.
*   **`overlay`:** Connects multiple Docker daemons across different hosts, enabling multi-host container-to-container communication (Docker Swarm).

---

## 2. Deep-Intuition (AARF) Breakdowns: Networking

### A. Default Bridge vs. User-Defined Bridge (Service Discovery)
#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Create a user-defined bridge network (`docker network create my_bridge`) for microservices that need to communicate, and avoid using the default `bridge` network.
2. **The Assumptions (Context):** Containers must reside on the same host and communicate using application-level protocol hosts (e.g., HTTP connection strings pointing to service names).
3. **The Rationale (Why):** User-defined bridge networks feature an **embedded DNS server** at IP `127.0.1.1` inside the container. This DNS resolver maps container names to active container IPs. The default bridge network does not contain this DNS server; containers on the default bridge can resolve each other only via hardcoded IP addresses or legacy `--link` configs.
4. **The Failure Loop (What if not):** Deploying a database container and web application container on the default bridge requires hardcoding the database IP (e.g., `172.17.0.2`) in the web application's configuration. If the host restarts or containers are recreated, Docker assigns IPs dynamically based on boot order. The database container might get `172.17.0.3`, causing the web application to fail with socket connection timeouts.
5. **Alternative Case (When to use 'if not'):** If container names are unknown or dynamic, you can pass temporary DNS configurations via `--add-host web:172.17.0.2` during container execution, which writes static host-to-IP records directly to `/etc/hosts`.

### B. Host Network Driver vs. Macvlan Driver
#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Utilize the **host** driver for high-throughput network applications on single nodes, reserving the **macvlan** driver for security monitoring tools or legacy applications that require a unique Layer 2 MAC address.
2. **The Assumptions (Context):** The host OS must be Linux (macOS and Windows run Docker in a VM, meaning the host network driver binds to the VM's ports, not the physical machine's ports).
3. **The Rationale (Why):** Host networking bypasses the virtual bridge (`docker0`), routing tables, and iptables NAT translations, reducing packet processing overhead. Macvlan assigns a dedicated hardware sub-interface to the container's MAC address, making it behave like a physical device on the LAN.
4. **The Failure Loop (What if not):** Running multiple web containers on the same host using `--network=host` causes port binding conflicts. The first container binds to port 80; the second container fails to start, throwing "address already in use" errors. Additionally, host networking exposes the container directly to the host network stack, allowing a compromised container to capture host network packets and communicate with private loopback services.
5. **Alternative Case (When to use 'if not'):** For standard microservices, use the user-defined `bridge` network with explicit port forwarding (`-p 8080:80`). This provides security isolation, allowing multiple containers to run on internal port 80 while mapped to unique ports on the host.

### C. Internal Networks & Multi-Interface Routing
#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Segregate internal services (e.g., databases) onto an isolated internal network (`docker network create --internal secure_net`), and connect application gateways to multiple networks.
2. **The Assumptions (Context):** The secure internal containers do not require external internet updates or external API calls.
3. **The Rationale (Why):** The `--internal` flag configures the bridge network without a default gateway to the host's network interfaces. Containers on this network can communicate with each other but cannot route traffic to the external internet. An application gateway container (e.g., a reverse proxy) can connect to both the public bridge network and the internal secure network, acting as a controlled bridge.
4. **The Failure Loop (What if not):** Leaving database containers on a standard bridge network exposes them to outbound routing. If compromised, the database container can download malicious scripts from the internet or establish reverse shells to command-and-control servers.
5. **Alternative Case (When to use 'if not'):** If the database engine requires direct outbound connections (e.g., for cloud licensing or log streaming), standard user-defined bridge networks must be used, hardened with custom iptables rules.

---

## 3. Docker Compose Orchestration

Docker Compose is a declarative tool for defining and running multi-container Docker applications using a YAML configuration file (`docker-compose.yml`).

```yaml
version: '3.8'

services:
  ui:
    build: ./UI
    restart: always
    ports:
      - "3000:3000"
    environment:
      - AUTH_HOST=auth
      - AUTH_PORT=8080
      - WEATHER_HOST=weather
      - WEATHER_PORT=5000
    depends_on:
      - auth
      - weather
    networks:
      - app-net

  auth:
    build: ./auth
    restart: always
    environment:
      - DB_HOST=db
      - DB_USER=root
      - DB_PASSWORD=${DB_PASSWORD} # Injected from local .env file
      - DB_NAME=authdb
    depends_on:
      - db
    networks:
      - app-net

  weather:
    build: ./weather
    restart: always
    environment:
      - APIKEY=${WEATHER_API_KEY}
    networks:
      - app-net

  db:
    image: mysql:8.0.25
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=${DB_PASSWORD}
      - MYSQL_DATABASE=authdb
    volumes:
      - db-data:/var/lib/mysql # Named volume (requires definition at bottom)
      - ./db-configs:/etc/mysql/conf.d # Bind mount (does not require definition)
    networks:
      - app-net

networks:
  app-net:
    driver: bridge

volumes:
  db-data:
```

### A. Core Configuration Syntax:
1.  **`restart` policy:** Specifies the restart behavior (e.g., `always` restarts the container if it exits due to failures or system reboots).
2.  **`depends_on`:** Establishes startup order. In the example, `db` starts before `auth`, and `auth` starts before `ui`. Note: `depends_on` only tracks container startup status, not application readiness.
3.  **`volumes` definition:** Named volumes must be declared under the root-level `volumes:` block. Host path Bind Mounts (e.g., `./db-configs:...`) are resolved directly and do not require root-level declaration.
4.  **`networks` block:** Compose automatically creates a default user-defined bridge network for all services in the file. Service names are registered as DNS hostnames within this network.

### B. Security & Variable Injection
To prevent exposing database passwords and API tokens in version control:
*   Define variables inside a `.env` file located in the same directory as the `docker-compose.yml` file.
*   Reference these variables using the `${VARIABLE_NAME}` syntax inside the Compose YAML.
*   Add the `.env` file to the `.gitignore` configuration.

---

## 4. Docker Compose Lifecycle Command Reference

Docker Compose commands must be run from the directory containing the `docker-compose.yml` file.

*   `docker compose up -d`: Builds missing images, creates networks and volumes, and starts all containers in detached background mode. Re-running this command evaluates changes in configurations and updates only altered services.
*   `docker compose ps`: Shows the status, ID, port mappings, and running processes of all containers in the stack.
*   `docker compose logs -f <service_name>`: Aggregates and follows live stdout/stderr streams from the stack (or a specific service).
*   `docker compose down`: Stops running containers and deletes containers, networks, and internal interface adapters created by `up`.
*   `docker compose down -v`: Stops containers and deletes networks along with any **named volumes** declared in the YAML file. This is crucial for troubleshooting database initialization scripts from scratch.
*   **Version History:** Version 1 & 2 are deprecated. Version 3 introduced declarative `networks` configuration, replacing the legacy `links` parameter, allowing container engines to route traffic dynamically without rigid, hard-linked dependencies.
