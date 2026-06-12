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

---

---

## 📖 Detailed Study: Docker Deep Dive (Nigel Poulton)

# 9: Deploying Apps with Docker Compose

## Deploying apps with Compose - The TLDR

“microservices”. A simple example might be an app with the following seven services:

- Web front-end
- Ordering
- Catalog
- Back-end database
- Logging
- Authentication
- Authorization

**Docker Compose** lets you describe an entire app in a single declarative configuration file, and deploy it with a single command

## Deploying apps with Compose - The Deep Dive

### Compose background

- Fig was a powerful Python tool, created by a company called Orchard, let you define entire multi-container apps in a single YAML file.
- Docker, Inc. acquired Orchard and re-branded Fig as Docker Compose.
- In April 2020 announced open standard for defining multi-container cloud-native apps.

**[Compse Specficiation](https://github.com/compose-spec/compose-spec)**



### Installing Compose

Windows and Mac: Part of Docker Desktop

#### Installing Compose on Linux

1. Download the binary using the curl command.
2. Make it executable using chmod

**[docker-compose repo in GitHub](https://github.com/docker/compose/releases)**

`$ sudo curl -L \
https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64 \
-o /usr/local/bin/docker-compose`

`$ sudo chmod +x /usr/local/bin/docker-compose`

`$ docker-compose --version`



### Compose files

- Compose uses YAML files to define multi-service applications. 
- YAML is a subset of JSON, so you can also use JSON. 
- The default name for a Compose YAML file is `docker-compose.yml`.

Four top-level keys:
- `version`
- `services`
- `networks`
- `volumes`



### Deploying an app with Compose

`$ git clone https://github.com/nigelpoulton/counter-app.git`

Inspect the files

Build the App:  
`$ docker-compose up &`

The multi-container app defined in a Compose file is called a _Compose app_.

`docker-compose up` expects the name of the Compose file to `docker-compose.yml`.

Or use the `-f` flag to specify a different compose file name:  
`$ docker-compose -f prod-equus-bass.yml up`

We can see that three images were either built or pulled as part of the deployment.

Run the container in a browser



### Managing an app with Compose

start, stop, delete, and get the status of applications being managed by Docker Compose

To stop and remove all containers in an App  
`$ docker-compose down`

`counter-net` network removed  
`counter-vol` volume NOT rmeoved (persistent)

To start the App in the background `-d`  
`$ docker-compose up -d`

To list the processes running inside of each service (container)  
`$ docker-compose top`

To stop the app without deleting its resources  
`$ docker-compose stop`

To delete a stopped Compose app  
`$ docker-compose rm`

To Restart the app  
`$ docker-compose restart`



## Deploying apps with Compose - The commands

- `docker-compose up`  // deploy a Compose app.
- `docker-compose stop`  // stop all of the containers in a Compose app without deleting them from the system.
- `docker-compose rm`  // delete a stopped Compose app.
- `docker-compose restart`  // restart a Compose app that has been stopped with docker-compose stop.
- `docker-compose ps`  // list each container in the Compose app.
- `docker-compose down`  // stop and delete a running Compose app. It deletes containers and networks, but not volumes and images.



----

# 11: Docker Networking

## Docker Networking - The TLDR

- container-to-container
- continer to other network
- container to VLAN

- Docker networking is based on open-source Container Network Model (CNM).
- `libnetwork` is Docker's implementation of CNM.
    - single-host bridge networks
    - multi-host overlays
    - plugins for existing VLANs
    - native service discovery
    - basic container load balancing

## Docker Networking - The Deep Dive

### The theory

Docker networking components:
- The Container Network Model (CNM)
- libnetwork
- Drivers

![[../Attachments/docker_deep_dive_32.png]]

### The Container Network Model (CNM)

**[CNM Design Specifications on GitHub](https://github.com/docker/libnetwork/blob/master/docs/design.md)**

CNM Building Blocks:
- **Sandboxes**: an isolated network stack. It includes; Ethernet interfaces, ports, routing tables, and DNS config.
- **Endpoints**: virtual network interfaces responsible for making sandboxes connect to networks.
- **Networks**: software implementation of an switch (802.1d bridge)

![[../Attachments/docker_deep_dive_33.png]]

![[../Attachments/docker_deep_dive_34.png]]

![[../Attachments/docker_deep_dive_35.png]]

## `libnetwork`

### Drivers

`libnetwork` implements the control plane and management plane functions and drivers implement the data plane.

![[../Attachments/docker_deep_dive_36.png]]

- Linux drivers: `bridge`, `overlay`, and `macvlan`.  
- Windows drivers: `nat`, `overlay`, `transparent`, and `l2bridge`.
- 3rd parties can also write _remote drivers_ or plugins.
- The driver is responsible for creating, managing and deletings network resources.

### Single-host bridge networks

- **Single-host**: only exists on a single Docker host and can only connect containers that are on the same host.
- **Bridge**: implementation of an 802.1d bridge (layer 2 switch).

- Linux: created by `bridge` driver.
- Windows: created by `nat` driver.

![[../Attachments/docker_deep_dive_37.png]]

All new containers will be connected to this default network unless `--network` flag is used.

To list all current networks:  
`$ docker network ls`

To inspect network driver:  
`$ docker network inspect`

The default “bridge” network, on all Linux-based Docker hosts, maps to an underlying _Linux bridge_ in the kernel called **“docker0”**  
`$ ip link show`

![[../Attachments/docker_deep_dive_39.png]]

To create a new single-host bridge network called "localnet":  
`$ docker network create -d bridge localnet`

Check it by:  
`$ ip link show`

![[../Attachments/docker_deep_dive_40.png]]

Create a container and attach it to the new localnet bridge network:  
`$ docker container run -d --name c1 --network localnet alpine sleep 1d`

![[../Attachments/docker_deep_dive_41.png]]

**Beware:** _The default `bridge` network on Linux does not support name resolution via the Docker DNS service. All other user-defined bridge networks do. The following demo will work because the container is on the user-defined `localnet` network._

Create a new container called "c2":  
`$ docker container run -it --name c2 --network localnet alpine sh`

`# ping c1`

Local DNS resolver forwards requests to an internal Docker DNS server that maintains name mapping for containers started with `--name` or `--net-alias` flags.

### Port Mapping

Containers connected to bridge networks cannot communicate outside it except in the case of _Port Mapping_

![[../Attachments/docker_deep_dive_42.png]]

`$ docker container run -d --name web --network localnet --publish 5000:80 nginx`

To verify port mapping:  
`docker port <container-name>`  
`$ docker port web`

### Connecting to existing networks

A common example is a partially containerized app

The built-in `MACVLAN` driver (`transparent` on Windows) was created with this in mind.

![[../Attachments/docker_deep_dive_43.png]]

on the negative side, it requires the host NIC to be in **promiscuous mode**

![[../Attachments/docker_deep_dive_44.png]]

``$ docker network create -d macvlan \
  --subnet=10.0.0.0/24 \
  --ip-range=10.0.0.0/25 \
  --gateway=10.0.0.1 \
  -o parent=eth0.100 \
  macvlan100``

![[../Attachments/docker_deep_dive_45.png]]

Create a container with the macvlan100 network:  
`$ docker container ran -d --name mactainer1 --network macvlan100 alpine sleep 1d`

![[../Attachments/docker_deep_dive_46.png]]

![[../Attachments/docker_deep_dive_47.png]]

### Service discovery

_Service discovery_ allows all containers and Swarm services to locate each other by name.

![[../Attachments/docker_deep_dive_48.png]]

_service discovery_ is network-scoped. This means that name resolution only works for containers and Services on the same network

`--dns` flag specifies external DNS server.  
`--dns-search` specifies custom search domain suffix  

`$ docker container run -it --name c1 \
  --dns=8.8.8.8 \
  --dns-search=nigelpoulton.com \
  alpine sh`

### Ingress load balancing

Swarm support:  
- Ingress mode (default)
- Host mode

![[../Attachments/docker_deep_dive_49.png]]



## Docker Networking - The Commands

- `docker network ls`  // Lists all networks on the local Docker host.
- `docker network create`  // Creates new Docker networks.
- `docker network inspect`  // Provides detailed configuration information about a Docker network.
- `docker network prune`  // Deletes all unused networks on a Docker host.
- `docker network rm`  // Deletes specific networks on a Docker host.



----

# 12: Docker overlay networking































----

---

## 🛠️ Practical Proof of Concept (PoC): Container DNS & Docker Compose Orchestration

### Target Scenario
We will verify that containers attached to a user-defined bridge network resolve each other automatically via name-based DNS, while default bridge containers fail. Then we will write and launch a multi-tier web application using Docker Compose.

### Step-by-Step Guided Steps

1. **Verify Default Bridge DNS Limitation**:
   - Start two alpine containers on the default bridge network:
     ```bash
     docker run -d --name default-c1 alpine sleep 1000
     docker run -d --name default-c2 alpine sleep 1000
     ```
   - Attempt to resolve `default-c1` from `default-c2`:
     ```bash
     docker exec -it default-c2 ping -c 2 default-c1
     ```
     Observe that this command fails with `ping: bad address 'default-c1'`. Automatic DNS resolution is disabled on the default bridge.
   - Clean up:
     ```bash
     docker rm -f default-c1 default-c2
     ```

2. **Verify User-Defined Bridge Service Discovery**:
   - Create a user-defined bridge network:
     ```bash
     docker network create custom-net
     ```
   - Start two containers attached to the new network:
     ```bash
     docker run -d --name custom-c1 --network custom-net alpine sleep 1000
     docker run -d --name custom-c2 --network custom-net alpine sleep 1000
     ```
   - Perform automatic DNS lookup:
     ```bash
     docker exec -it custom-c2 ping -c 2 custom-c1
     ```
     Observe that the ping succeeds. The Docker daemon resolves the hostname `custom-c1` to its allocated container IP within the subnet.
   - Clean up:
     ```bash
     docker rm -f custom-c1 custom-c2
     docker network rm custom-net
     ```

3. **Orchestrate a Multi-Tier Stack using Docker Compose**:
   - Setup a temporary orchestration workspace:
     ```bash
     mkdir -p compose-poc && cd compose-poc
     ```
   - Create a compose file defining Nginx (reverse proxy) and an alpine server representing the backend:
     ```yaml
     cat <<EOF > docker-compose.yml
     version: "3.8"
     services:
       web-proxy:
         image: nginx:alpine
         ports:
           - "8080:80"
         depends_on:
           - api-backend
         networks:
           - internal-net

       api-backend:
         image: alpine
         command: sh -c "echo 'Backend API operational' > /tmp/index.html && httpd -f -p 80 -h /tmp"
         networks:
           - internal-net

     networks:
       internal-net:
         driver: bridge
     EOF
     ```
   - Spin up the stack in detached mode:
     ```bash
     docker compose up -d
     ```
   - Inspect the created resources and verify service statuses:
     ```bash
     docker compose ps
     ```
   - Test connectivity from Nginx to backend using DNS:
     ```bash
     docker compose exec web-proxy curl http://api-backend
     ```
     Output should print: `Backend API operational`.
   - Tear down the stack and delete its allocated network adapters:
     ```bash
     docker compose down
     ```

4. **Clean Up Workspace**:
   ```bash
   cd .. && rm -rf compose-poc
   ```
