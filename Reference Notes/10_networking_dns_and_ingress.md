# Kubernetes Networking, DNS, and Ingress Reference Module

This module provides an exhaustive, production-grade reference for Linux networking prerequisites, the Container Network Interface (CNI) specification, Kubernetes cluster/pod networking, service networking (iptables vs. IPVS), CoreDNS architecture, and Ingress controllers/resources using modern API specifications.

---

## 1. Linux Networking Prerequisites (OS & Kernel Level)

Before analyzing Kubernetes-specific network mechanics, the underlying Linux kernel networking subsystem must be understood. Kubernetes constructs its network overlays, routing, and services directly on top of standard Linux kernel tools.

### 1.1 Switching, Routing, and Gateways

Linux uses network interfaces, routing tables, and ARP tables to move packets across L2 (data link) and L3 (network) boundaries.

```mermaid
graph TD
    subgraph Host OS
        v-net-0["Bridge: v-net-0<br>(192.168.15.5)"]
        eth0["Physical NIC: eth0<br>(192.168.1.10)"]
        iptables["iptables NAT<br>(POSTROUTING MASQUERADE)"]
        
        subgraph Namespace Red
            veth-red["veth-red<br>(192.168.15.1)"]
            default_red["Default Route<br>via 192.168.15.5"]
        end
        
        subgraph Namespace Blue
            veth-blue["veth-blue<br>(192.168.15.2)"]
            default_blue["Default Route<br>via 192.168.15.5"]
        end
        
        veth-red-br["veth-red-br<br>(master v-net-0)"]
        veth-blue-br["veth-blue-br<br>(master v-net-0)"]
        
        veth-red --- veth-red-br
        veth-blue --- veth-blue-br
        veth-red-br === v-net-0
        veth-blue-br === v-net-0
        v-net-0 --> iptables
        iptables --> eth0
    end
```

#### Diagnostic and Configuration Commands
*   **List Network Interfaces:**
    ```bash
    # Show status and MAC addresses (link/ether)
    ip link
    
    # Show IP addresses assigned to interfaces
    ip addr
    # or
    ip a
    ```
*   **Inspect Host Routing Tables:**
    ```bash
    # Show active routing tables with numerical IPs
    ip route show
    # or
    route -n
    ```
*   **Add L3 Routing Entries:**
    ```bash
    # Route all traffic for 192.168.1.0/24 through gateway 192.168.2.1
    ip route add 192.168.1.0/24 via 192.168.2.1
    ```
*   **Configure the Default Gateway:**
    ```bash
    # Forward all external traffic to the default gateway
    ip route add default via 192.168.2.1
    ```

#### Kernel Packet Forwarding
For a Linux host to act as a router (forwarding packets between different namespaces or interfaces), IPv4 packet forwarding must be explicitly enabled.

*   **Temporary Enablement:**
    ```bash
    # Read status (0 = disabled, 1 = enabled)
    cat /proc/sys/net/ipv4/ip_forward
    
    # Enable temporarily
    echo 1 > /proc/sys/net/ipv4/ip_forward
    # or
    sysctl -w net.ipv4.ip_forward=1
    ```
*   **Permanent Configuration:**
    Edit `/etc/sysctl.conf` or create a drop-in file at `/etc/sysctl.d/99-kubernetes-cri.conf`:
    ```ini
    net.ipv4.ip_forward = 1
    ```
*   **Reload Sysctl Settings:**
    ```bash
    sysctl --system
    ```

---

### 1.2 DNS Resolution on Linux Host
The host resolves human-readable names to IP addresses using configurations in three critical files:

1.  **`/etc/hosts`:** Static local mappings (takes priority by default).
    ```text
    127.0.0.1       localhost
    192.168.1.10    controlplane
    192.168.1.11    node01
    ```
2.  **`/etc/resolv.conf`:** Specifies upstream nameservers.
    ```text
    nameserver 8.8.8.8
    nameserver 1.1.1.1
    options edns0
    ```
3.  **`/etc/nsswitch.conf`:** Dictates the name service lookup order.
    ```text
    hosts:          files dns
    ```
    *(Note: `files` refers to `/etc/hosts`, `dns` refers to resolvers in `/etc/resolv.conf`)*

#### Diagnostic DNS Tools
```bash
# Query A-records for a target host
nslookup google.com

# Verbose lookup printing DNS server replies and query times
dig google.com

# Simple resolution check
host google.com
```

---

### 1.3 Network Namespaces (`netns`)

A network namespace is a logical copy of the network stack, containing its own routing table, firewall (iptables) rules, and network interfaces. This isolation provides the foundation for container/pod networking.

*   **Create Network Namespaces:**
    ```bash
    ip netns add red
    ip netns add blue
    ```
*   **List Network Namespaces:**
    ```bash
    ip netns
    ```
    *(Namespaces are tracked filesystem-wise under `/var/run/netns/`)*
*   **Execute Commands inside a Network Namespace:**
    ```bash
    # View interfaces inside namespace 'red'
    ip netns exec red ip link
    # or using short-hand notation
    ip -n red link
    
    # View routing tables inside namespace 'blue'
    ip netns exec blue ip route
    ```

---

### 1.4 Virtual Ethernet Pairs (`veth`)

A virtual ethernet (`veth`) device is a local tunnel that acts as a bidirectional wire connecting two interfaces. Packets entering one end automatically exit the other. This is used to connect network namespaces to the host.

*   **Create a Virtual Cable (veth pair):**
    ```bash
    ip link add veth-red type veth peer name veth-red-br
    ip link add veth-blue type veth peer name veth-blue-br
    ```
*   **Move One End of the Cable to a Namespace:**
    ```bash
    ip link set veth-red netns red
    ip link set veth-blue netns blue
    ```
*   **Assign IP Addresses to Namespace Interfaces:**
    ```bash
    ip -n red addr add 192.168.15.1/24 dev veth-red
    ip -n blue addr add 192.168.15.2/24 dev veth-blue
    ```
*   **Bring Interfaces UP:**
    ```bash
    # Bring loopback up inside the namespace
    ip -n red link set lo up
    
    # Bring veth up inside namespaces
    ip -n red link set veth-red up
    ip -n blue link set veth-blue up
    ```
*   **Delete a Virtual Cable:**
    ```bash
    # Deleting one end of a veth pair automatically destroys the peer interface
    ip link del veth-red-br
    ```

---

### 1.5 Linux Bridge Networks

To connect multiple namespaces together, a virtual switch (Linux Bridge) is created on the host OS. The peer ends of the veth pairs are attached to this bridge.

*   **Create a Linux Bridge Interface:**
    ```bash
    ip link add v-net-0 type bridge
    ```
*   **Bring the Bridge Interface UP:**
    ```bash
    ip link set dev v-net-0 up
    ```
*   **Assign an IP to the Bridge (acting as the default gateway for namespaces):**
    ```bash
    ip addr add 192.168.15.5/24 dev v-net-0
    ```
*   **Bind Host-Side Veth Peers to the Bridge:**
    ```bash
    ip link set veth-red-br master v-net-0
    ip link set veth-blue-br master v-net-0
    ```
*   **Bring Host-Side Interfaces UP:**
    ```bash
    ip link set dev veth-red-br up
    ip link set dev veth-blue-br up
    ```
*   **Configure Default Gateways Inside Namespaces:**
    ```bash
    # Direct namespace traffic through the host bridge gateway
    ip netns exec red ip route add default via 192.168.15.5
    ip netns exec blue ip route add default via 192.168.15.5
    ```

#### External Connectivity: NAT (MASQUERADE) and Port Forwarding (DNAT)
By default, traffic from namespaces can reach the bridge, but cannot egress to the host's physical network or external networks.

*   **Enable Egress NAT (IP Masquerade):**
    Allow namespaces to reach external networks by rewriting the source IP to the host's IP upon exit:
    ```bash
    iptables -t nat -A POSTROUTING -s 192.168.15.0/24 -j MASQUERADE
    ```
*   **Enable Ingress Port Forwarding (Destination NAT):**
    Forward incoming traffic on host port `8080` to namespace `blue` IP `192.168.15.2` on port `80`:
    ```bash
    iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 192.168.15.2:80
    ```
*   **List Active NAT Rules:**
    ```bash
    iptables -t nat -nvL
    ```

---

### 1.6 Docker Bridge Networking Mapping

Docker implements the same underlying Linux network namespaces and bridges described above:
*   Docker creates a default bridge named `docker0` (typically on subnet `172.17.0.0/16` or `172.18.0.0/24`).
*   Running a container starts an isolated network namespace.
*   Docker allocates a veth pair, moving one end (`eth0`) into the container namespace and binding the other end (`vethXXXX`) to `docker0`.

#### Command Mapping & Inspection
```bash
# Start a container on the default bridge network
docker run -d --name web-nginx -p 8080:80 nginx

# Identify container IP address
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web-nginx

# Inspect iptables NAT rules created by Docker for port forwarding
iptables -t nat -S DOCKER
```
> [!NOTE]
> Docker adds rules directly to a custom `DOCKER` iptables chain. In contrast, Kubernetes bypasses Docker's host port mappings, instead delegating port/routing control to the CNI plugin and Kube-Proxy.

---

## 2. CNI (Container Network Interface) Specifications

The Container Network Interface (CNI) is a CNCF specification that standardizes how container runtimes (such as `containerd` or `CRI-O`) call external plugins to configure networking for container sandboxes.

### 2.1 CNI Concept & Lifecycle Workflow

```
+------------------+                   +-------------------+                   +------------------+
|                  | 1. Create Sandbox |                   | 2. Create NetNS   |                  |
|     Kubelet      |------------------>|    CRI Runtime    |------------------>| Network Namespace|
|                  |                   |  (containerd/CRI) |                   |    (per Pod)     |
+------------------+                   +-------------------+                   +------------------+
         |                                       |
         | 4. Pod Scheduled                      | 3. Invoke CNI (ADD)
         |                                       v
         |                             +-------------------+
         +---------------------------->|    CNI Plugins    |---> Sets up Veth pair
                                       |   (/opt/cni/bin)  |---> Allocates IP (IPAM)
                                       +-------------------+
```

1.  **Pod Creation:** Kubelet instructs the container runtime to create a Pod sandbox.
2.  **Namespace Setup:** The runtime initializes a new network namespace for the Pod.
3.  **CNI Execution:** The runtime invokes CNI plugin binaries (found in `/opt/cni/bin`) with commands:
    *   `ADD`: Configure the network (create veth pair, move to namespace, allocate IP).
    *   `DEL`: Tear down the network resources when the Pod is deleted.
    *   `CHECK`: Verify that the network setup conforms to expectations.
4.  **Information Transfer:** Configuration parameters (including namespace paths, container IDs, and CNI actions) are passed to the plugins via environment variables (`CNI_COMMAND`, `CNI_CONTAINERID`, `CNI_NETNS`, `CNI_IFNAME`) and stdin (JSON configuration).

---

### 2.2 Host and Kubelet CNI Configurations

Kubelet reads configuration files at startup to integrate with CNI plugins.

*   **CNI Binaries Directory:** `--cni-bin-dir` (defaults to `/opt/cni/bin/`).
*   **CNI Configuration Directory:** `--cni-conf-dir` (defaults to `/etc/cni/net.d/`).
*   **Inspect Active Kubelet Environment Flags:**
    ```bash
    # Locate CNI configuration parameters passed to Kubelet
    cat /var/lib/kubelet/kubeadm-flags.env
    
    # Check current systemd service configuration for Kubelet
    systemctl cat kubelet
    ```

---

### 2.3 CNI Directory and Configuration Structures

The `/etc/cni/net.d/` directory contains JSON configuration files. If multiple files are present, Kubelet evaluates them in alphabetical order and uses the first valid file it finds.

*   **List Installed CNI Binaries:**
    ```bash
    ls -l /opt/cni/bin/
    ```
    *Common loopback, bridge, and routing utilities:* `bridge`, `loopback`, `ptp`, `portmap`, `macvlan`, `host-local`, `dhcp`.

*   **Example CNI Configuration List (`/etc/cni/net.d/10-flannel.conflist`):**
    ```json
    {
      "cniVersion": "0.3.1",
      "name": "cbr0",
      "plugins": [
        {
          "type": "flannel",
          "delegate": {
            "hairpinMode": true,
            "isDefaultGateway": true
          }
        },
        {
          "type": "portmap",
          "capabilities": {
            "portMappings": true
          }
        }
      ]
    }
    ```

---

## 3. Cluster and Pod Networking

Kubernetes defines a strict "IP-per-Pod" networking model. This mandates that every Pod gets its own IP address, and Pods must be able to communicate with all other Pods across nodes without NAT.

### 3.1 Node Port Assignments

Kubernetes nodes must maintain specific open ports to facilitate control-plane and worker communications.

| Component | Default Port | Protocol | Purpose |
| :--- | :--- | :--- | :--- |
| **Kube-APIServer** | `6443` | TCP | Control-plane API access |
| **ETCD Client** | `2379` | TCP | Datastore API client access |
| **ETCD Peer** | `2380` | TCP | Datastore clustering peer communication |
| **Kubelet** | `10250` | TCP | Control-plane to node communication |
| **Kube-Scheduler** | `10259` | TCP | Scheduler secure port |
| **Kube-Controller-Manager** | `10257` | TCP | Controller manager secure port |
| **Kube-Proxy** | `10256` | TCP | Health check / metrics port |
| **NodePort Services** | `30000-32767` | TCP/UDP | External service access range |

#### Verification Command
```bash
# List all active listening TCP ports with corresponding process PIDs
netstat -nltp
# or
ss -tulpn
```

---

### 3.2 IP Address Management (IPAM)

IPAM plugins manage the assignment of subnets and IPs to nodes and pods.
*   **`host-local`:** Allocates IP addresses out of a locally defined subnet range on each host. It stores state locally under `/var/lib/cni/networks/`.
*   **`dhcp`:** Delegates IP allocation to an external DHCP server on the network.

---

### 3.3 CNI Plugin Implementations (WeaveNet vs. Calico)

| Feature | WeaveNet | Calico |
| :--- | :--- | :--- |
| **Network Type** | Encapsulated Overlay (VXLAN/UDP) | L3 Routed (No encapsulation by default) |
| **Encapsulation Options** | VXLAN, FastDP (UDP) | IP-in-IP, VXLAN |
| **Routing Protocol** | Proprietary gossip protocol | BGP (Border Gateway Protocol) |
| **Datastore** | Ring-buffer distributed DB | Kubernetes CRDs or direct ETCD |
| **Network Policy** | Supported (built-in) | Advanced Policies (highly scalable) |

#### WeaveNet Overlay Architecture
WeaveNet deploys as a DaemonSet with one agent pod per node. It creates a host bridge named `weave` and builds a virtual overlay network.

*   **Overlay Routing:** Packets between pods on different nodes are captured by the `weave` interface, encapsulated in VXLAN (or UDP/FastDP), and sent to the peer agent on the target node.
*   **Verification Commands:**
    ```bash
    # Check weave pods in kube-system
    kubectl get pods -n kube-system -l name=weave-net
    
    # View weave log output
    kubectl logs -n kube-system daemonset/weave-net -c weave
    
    # View routes inside a container to verify default gateway (usually pointing to weave bridge IP)
    kubectl exec -it <pod-name> -- ip route
    ```

---

## 4. Service Networking

Kubernetes Services are abstract definitions of logical pod groupings. Since pods are ephemeral, services provide a stable virtual IP (ClusterIP) that routes traffic to backend pods.

### 4.1 Service Virtual IPs and ClusterIP Allocation

A Service's ClusterIP is not assigned to any physical interface. Instead, it is a virtual IP registered in the API server.
*   **IP Range Allocation:** The ClusterIP block is configured at API Server startup using the `--service-cluster-ip-range` flag.
*   **Determine Service Cluster IP Range:**
    ```bash
    ps -aux | grep kube-apiserver | grep service-cluster-ip-range
    ```

---

### 4.2 Service Types & Traffic Flow

*   **`ClusterIP`:** Exposes the service on a cluster-internal IP (default).
*   **`NodePort`:** Exposes the service on each node's IP at a static port (in the `30000-32767` range).
*   **`LoadBalancer`:** Provisions an external cloud load balancer pointing to the node's NodePorts.

```yaml
# Example: ClusterIP and NodePort Service Templates
apiVersion: v1
kind: Service
metadata:
  name: web-service-clusterip
  namespace: default
spec:
  type: ClusterIP
  selector:
    app: web-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: web-service-nodeport
  namespace: default
spec:
  type: NodePort
  selector:
    app: web-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
      nodePort: 30080
```

---

### 4.3 Kube-Proxy Modes: iptables vs. IPVS

Kube-Proxy runs as a DaemonSet on every node. It watches the API Server for new Services and Endpoints, translating them into packet forwarding rules on the host.

```mermaid
graph TD
    subgraph iptables Mode (Sequential O(N))
        Client1[Client] --> KubeServices[KUBE-SERVICES Chain]
        KubeServices --> ServiceRule1[Service 1 Rule]
        KubeServices --> ServiceRule2[Service 2 Rule]
        ServiceRule2 --> RandomSEP[Random Endpoint Match]
        RandomSEP --> PodA[Pod A IP]
        RandomSEP --> PodB[Pod B IP]
    end
    subgraph IPVS Mode (Hash Table O(1))
        Client2[Client] --> IPVS_VS[IPVS Virtual Server]
        IPVS_VS -- Hash Table Lookup --> RealServer[Real Server List]
        RealServer -- LB Algorithm --> PodC[Pod C IP]
        RealServer -- LB Algorithm --> PodD[Pod D IP]
    end
```

#### 1. iptables Mode (Default)
In this mode, Kube-Proxy writes rules in the host's iptables NAT table.
*   **Mechanisms:**
    *   Traffic targeting a Service IP matches the `KUBE-SERVICES` chain.
    *   This chain forwards traffic to a service-specific chain (`KUBE-SVC-XXX`).
    *   The service chain uses the iptables `statistic` module to apply probability-based load balancing across endpoint chains (`KUBE-SEP-YYY`). These endpoint chains apply DNAT to redirect traffic to the destination pod IP.
*   **Limitations:**
    *   **Sequential Rule Evaluation:** Rules are evaluated sequentially ($O(N)$ lookup complexity). Large clusters with thousands of services suffer high latency and CPU overhead during packet processing and rule updates.

#### 2. IPVS Mode
In this mode, Kube-Proxy uses IPVS (IP Virtual Server), an L4 transport-layer load balancing mechanism built into the Linux kernel.
*   **Mechanisms:**
    *   Kube-Proxy creates IPVS virtual servers mapped to Service ClusterIPs.
    *   It binds pod endpoints as real servers behind the virtual servers.
    *   Lookup tables are implemented as hash tables ($O(1)$ lookup complexity), maintaining constant performance regardless of service scale.
*   **Algorithms:** IPVS supports various load balancing algorithms:
    *   `rr`: Round Robin
    *   `lc`: Least Connection
    *   `dh`: Destination Hashing
    *   `sh`: Source Hashing

#### Diagnostic Commands for Service Proxying
```bash
# Determine Kube-Proxy proxy mode from logs
kubectl logs -n kube-system -l k8s-app=kube-proxy | grep -E "Using (iptables|ipvs) Proxier"

# Inspect iptables NAT rules for a target service
iptables -t nat -S | grep <service-name>

# View active IPVS virtual servers and real backends (requires ipvsadm)
ipvsadm -ln
```

---

## 5. DNS in Kubernetes

DNS services in the cluster allow pods to resolve services and other pods using human-readable names.

### 5.1 CoreDNS Architecture

CoreDNS is deployed as a Deployment in the `kube-system` namespace. It exposes a service named `kube-dns` with a static ClusterIP (conventionally `10.96.0.10`).

```mermaid
graph TD
    Pod[Pod Resolver] -->|1. DNS Lookup| CoreDNS_SVC[kube-dns Service IP: 10.96.0.10]
    CoreDNS_SVC -->|2. TCP/UDP Port 53| CoreDNS_Pod[CoreDNS Pods]
    CoreDNS_Pod -->|3. Corefile Match| Match{Query Zone}
    Match -->|Cluster Domain: *.cluster.local| KubernetesPlugin[kubernetes Plugin]
    Match -->|External Domain: google.com| ForwardPlugin[forward Plugin]
    KubernetesPlugin -->|Lookup API Cache| ClusterDNS[Cluster IPs / Pod IPs]
    ForwardPlugin -->|Forward Query| Upstream[Upstream Nameserver /etc/resolv.conf]
```

#### Kubelet ClusterDNS Integration
Kubelet injects the `kube-dns` service IP as the DNS nameserver for every container it starts.
*   **Verify Kubelet Configuration:**
    ```bash
    cat /var/lib/kubelet/config.yaml | grep -A2 clusterDNS
    ```
    *Expected output:*
    ```yaml
    clusterDNS:
    - 10.96.0.10
    clusterDomain: cluster.local
    ```

---

### 5.2 CoreDNS ConfigMap & Corefile Details

The Corefile dictates how DNS requests are processed. It is stored in a ConfigMap named `coredns` in the `kube-system` namespace.

*   **View CoreDNS ConfigMap:**
    ```bash
    kubectl describe configmap coredns -n kube-system
    ```

```nginx
# Example Corefile Configuration
.:53 {
    errors          # Log errors to standard output
    health {
        lameduck 5s # Wait 5s before shutdown to drain connections
    }
    ready           # Exposes readiness endpoint on port 8181
    kubernetes cluster.local in-addr.arpa ip6.arpa {
        pods insecure
        fallthrough in-addr.arpa ip6.arpa
        ttl 30
    }
    prometheus :9153  # Exposes metrics on port 9153
    forward . /etc/resolv.conf # Forward non-cluster requests to upstream servers
    cache 30        # Enable a 30-second TTL cache for records
    loop            # Detect forwarding loops
    reload          # Enable dynamic reloading when the ConfigMap changes
}
```

#### Corefile Directives Explained:
*   **`kubernetes`:** Configures CoreDNS to resolve names in the `cluster.local` domain.
    *   `pods insecure`: Resolves pod IPs based on query formatting without verifying their existence in the API server. Alternative options: `verified` (queries the API server to confirm the pod exists before resolving) or `disabled` (prevents pod IP lookup entirely).
    *   `fallthrough`: Forwards requests to subsequent plugins if the local Kubernetes zone lookup yields no results.
*   **`forward`:** Resolves external queries (e.g. `google.com`) by forwarding them to the host resolver configuration at `/etc/resolv.conf`.

---

### 5.3 FQDN and Record Formats

The cluster DNS assigns a Fully Qualified Domain Name (FQDN) to Services, Pods, and StatefulSet members.

#### Service A-Record Format
```text
<service-name>.<namespace>.svc.<cluster-domain>
```
*Example:* `web-service.default.svc.cluster.local` resolves to the Service's ClusterIP.

#### Pod A-Record Format
```text
<ip-with-dashes>.<namespace>.pod.<cluster-domain>
```
*Example:* A pod with IP `10.244.1.4` in namespace `apps` resolves to `10-244-1-4.apps.pod.cluster.local`.

#### StatefulSet Hostname Format
For headless services (with `clusterIP: None`), DNS points directly to the backing pod IPs.
```text
<pod-name>.<service-name>.<namespace>.svc.<cluster-domain>
```
*Example:* `db-statefulset-0.mysql.database.svc.cluster.local` resolves directly to the pod's IP.

---

### 5.4 Pod Name Resolution & `/etc/resolv.conf`

Inside every Pod container, Kubelet configures `/etc/resolv.conf` to direct DNS lookups to CoreDNS and define default search paths.

*   **Inspect Resolver Configuration inside a Pod:**
    ```bash
    kubectl exec -it <pod-name> -- cat /etc/resolv.conf
    ```
    *Expected output:*
    ```text
    nameserver 10.96.0.10
    search default.svc.cluster.local svc.cluster.local cluster.local
    options ndots:5
    ```

#### Search Path and `ndots` Resolution Logic:
*   **`ndots:5`:** Any query containing fewer than 5 dots is treated as a relative query. The resolver appends the search paths sequentially until it finds a match.
*   **Example 1 (Same Namespace):** A pod in namespace `apps` resolving `web-service` will check `web-service.apps.svc.cluster.local`. This yields a match in the first search path.
*   **Example 2 (Cross Namespace):** A pod in namespace `apps` resolving a database service in namespace `db` must use the namespace-qualified name: `db-service.db`. The resolver queries:
    1.  `db-service.db.apps.svc.cluster.local` (Fails)
    2.  `db-service.db.svc.cluster.local` (Matches)

> [!WARNING]
> High `ndots` values (e.g. `ndots:5`) can cause significant DNS latency. Absolute queries (like `google.com`) contain fewer than 5 dots, forcing the resolver to search all internal search domains (e.g., `google.com.default.svc.cluster.local`) before querying external servers.

---

### 5.5 Custom DNS Configurations

You can modify CoreDNS to resolve custom domains or redirect queries to specific nameservers by updating the Corefile ConfigMap.

#### Forwarding a Custom Domain to a Specific Nameserver
Apply this configuration block to forward all queries for `.corp.internal` to DNS server `10.0.0.50`:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health
        kubernetes cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           fallthrough in-addr.arpa ip6.arpa
        }
        prometheus :9153
        forward . /etc/resolv.conf
        cache 30
        loop
        reload
    }
    corp.internal:53 {
        forward . 10.0.0.50
    }
```

---

## 6. Ingress Control and Resources

An Ingress controller is an L7 reverse proxy that routes external HTTP/HTTPS traffic into cluster services. An Ingress resource defines the routing rules that configure the controller.

```
                  +--------------------------------+
                  |  Ingress Controller (Proxy)    |
                  |  e.g., ingress-nginx-controller|
                  +--------------------------------+
                             /            \
              Matches Host:  /              \ Matches Host:
             wear.store.com /                \ watch.store.com
                           /                  \
                          v                    v
                  +---------------+    +---------------+
                  |  wear-service |    |  watch-service|
                  |  (ClusterIP)  |    |  (ClusterIP)  |
                  +---------------+    +---------------+
```

### 6.1 Ingress Controller vs Ingress Resource

1.  **Ingress Controller:** The running application pod (e.g. Nginx Ingress Controller, Traefik, HAProxy) that acts as the data plane. It watches the API server for changes to Ingress resources and dynamically updates its configuration.
2.  **Ingress Resource:** The control plane configuration file defining matching paths, hosts, SSL secrets, and backend target services.

> [!NOTE]
> Most Ingress controllers bypass Kube-Proxy Service ClusterIPs. Instead, they extract Endpoint pod IPs directly from the API Server and route traffic directly to the pods. This avoids an extra routing hop and preserves client source IPs.

---

### 6.2 Ingress Resource Spec (`networking.k8s.io/v1`)

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  namespace: default
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx # Explicitly bind to the Nginx Ingress Controller
  rules:
  - host: my-app.local
    http:
      paths:
      - path: /api
        pathType: Prefix # Matches anything starting with /api
        backend:
          service:
            name: api-service
            port:
              number: 8080
```

---

### 6.3 Routing Patterns

#### Path-Based Routing (Single Host, Multiple Paths)
```yaml
spec:
  rules:
  - http:
      paths:
      - path: /wear
        pathType: Prefix
        backend:
          service:
            name: wear-service
            port:
              number: 80
      - path: /watch
        pathType: Prefix
        backend:
          service:
            name: watch-service
            port:
              number: 80
```

#### Host-Based Routing (Multiple Hosts, Distinct Paths)
```yaml
spec:
  rules:
  - host: wear.my-online-store.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: wear-service
            port:
              number: 80
  - host: watch.my-online-store.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: watch-service
            port:
              number: 80
```

---

### 6.4 SSL/TLS Termination

Ingress controllers can terminate SSL connections using private keys and certificates stored in Kubernetes Secrets.

*   **Generate a TLS Secret:**
    ```bash
    kubectl create secret tls store-tls-secret \
      --cert=path/to/tls.crt \
      --key=path/to/tls.key \
      --namespace=default
    ```
*   **Associate the Secret with the Ingress Resource:**
    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: secure-ingress
      namespace: default
    spec:
      ingressClassName: nginx
      tls:
      - hosts:
        - my-online-store.com
        secretName: store-tls-secret
      rules:
      - host: my-online-store.com
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: secure-service
                port:
                  number: 443
    ```

---

### 6.5 Advanced Annotations: Rewrite Target

When an Ingress matches paths like `/pay` and forwards them to a backend service, the backend service must expect requests on the `/pay` path. If the backend service is configured to handle traffic on the root path `/` instead, the Ingress controller must rewrite the URL path before forwarding the request.

#### Basic URL Path Rewrite
```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
```
*   *Request:* `http://my-store.com/pay` $\rightarrow$ *Forwarded to service as:* `http://pay-service:80/`

#### Dynamic Regex Rewrite
For complex path schemes, capture groups can be used to dynamically rewrite forwarded paths.
```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
spec:
  rules:
  - host: store.com
    http:
      paths:
      - path: /service1(/|$)(.*)
        pathType: Prefix
        backend:
          service:
            name: service1
            port:
              number: 80
```
*   *Request:* `http://store.com/service1/login` $\rightarrow$ *Forwarded to service as:* `http://service1:80/login`

---

## 7. Diagnostics and Verification Cheat Sheet

Use these command patterns to troubleshoot networking, DNS, and Ingress routing issues in the cluster.

```bash
# ==============================================================================
# Host Network and Namespace Inspection
# ==============================================================================
# List network interfaces on the current host node
ip link show

# Execute network status check inside a containerd container's namespace
# 1. Identify container runtime task PID
docker inspect <container-id> --format '{{.State.Pid}}'
# 2. Query interface mappings using nsenter
nsenter -t <pid> -n ip addr show

# ==============================================================================
# CNI and IPAM Diagnostics
# ==============================================================================
# View the configured CNI configuration list file
cat /etc/cni/net.d/*.conflist

# Check WeaveNet status and peer mappings
kubectl exec -n kube-system daemonset/weave-net -c weave -- weave status

# ==============================================================================
# Service and Routing Debugging
# ==============================================================================
# List iptables NAT chains to identify service endpoints
iptables -t nat -L KUBE-SERVICES -n -v

# Inspect IPVS routing rules if kube-proxy is operating in IPVS mode
ipvsadm -ln

# Query the ClusterIP range configured for API Server services
ps -aux | grep kube-apiserver | grep -oE "\-\-service-cluster-ip-range=[^ ]+"

# ==============================================================================
# DNS Operations and Resolution Checks
# ==============================================================================
# Resolve a service name using a debug pod
kubectl run dns-tester --image=busybox:1.28 --restart=Never --rm -it -- nslookup kubernetes.default.svc.cluster.local

# View logs from CoreDNS to identify query resolution failures
kubectl logs -n kube-system -l k8s-app=kube-dns --tail=100

# ==============================================================================
# Ingress Routing Verification
# ==============================================================================
# Check detailed configurations for a deployed Ingress resource
kubectl describe ingress <ingress-name>

# Check log output from the Nginx Ingress Controller
kubectl logs -n ingress-nginx deployment/ingress-nginx-controller
```
