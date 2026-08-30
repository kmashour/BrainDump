---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - kubernetes/networking
  - kubernetes/ingress
---

# Module 0-9-3: Ingress Controllers, TLS Termination & Gateway API

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Reference MOC]] > **Module 0-9-3**

---

## 6. Ingress Control and Resources


### 6.1 Limitations of Service Exposure & Ingress Architecture
In microservice architectures, exposing every internal service using a `NodePort` or `LoadBalancer` is highly inefficient and expensive:
*   **NodePort Drawbacks:** Requires managing custom port numbers (30000-32767) for each service and exposes node IPs directly to users.
*   **LoadBalancer Drawbacks:** Allocating a dedicated LoadBalancer service for each application on cloud platforms incurs substantial hosting costs.

An **Ingress** acts as an L7 reverse proxy and unified gateway. It consolidates routing rules into a single resource, routing traffic to different internal ClusterIP services based on HTTP host headers or URI paths.

#### Ingress Routing Layout
![Ingress Routing Layout](../Attachments/Screenshot%20from%202025-04-21%2023-50-42.png)

---

### 6.2 Ingress Controller vs Ingress Resource
1.  **Ingress Controller:** The running reverse proxy pod (e.g. Nginx Ingress Controller, Traefik, HAProxy) that acts as the data plane. It monitors the API server for changes to Ingress resources, updates its configuration rules dynamically, and routes external traffic to the appropriate internal Pod IPs.
2.  **Ingress Resource:** The control plane configuration file defining matching paths, hosts, SSL secrets, and backend target services.

> [!NOTE]
> Most Ingress controllers bypass Kube-Proxy Service ClusterIPs. Instead, they extract Endpoint pod IPs directly from the API Server and route traffic directly to the pods. This avoids an extra routing hop and preserves client source IPs.

---

### 6.3 Ingress Resource Spec (`networking.k8s.io/v1`)
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

### 6.4 Routing Patterns
*   **Prefix PathType:** Routes any path matching the specified prefix (e.g., `/api` matches `/api`, `/api/v1`, and `/api/v2`).
*   **Exact PathType:** Routes only exact path matches.

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

#### Host-Based Routing (Multiple Hosts/Subdomains, Distinct Paths)
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

### 6.5 SSL/TLS Termination
Ingress controllers can terminate SSL connections using private keys and certificates stored in Kubernetes Secrets of type `kubernetes.io/tls`.

#### 1. Generate Self-Signed Certificates (OpenSSL)
In local development or test environments, you can generate self-signed certificates using OpenSSL:
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout tls.key -out tls.crt \
  -subj "/CN=example.com/O=example.com"
```
*   `-nodes`: Disables password encryption on the private key file.
*   `-keyout`: Output path for the private key.
*   `-out`: Output path for the certificate.

#### 2. Create the TLS Secret
Create the TLS secret imperatively inside your namespace:
```bash
kubectl create secret tls store-tls-secret --key=tls.key --cert=tls.crt
```
*   The `tls` type ensures that the secret contains the keys `tls.key` and `tls.crt`.

#### 3. Associate the Secret with the Ingress Resource
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

### 6.6 Advanced Annotations: Rewrite Target
When an Ingress routes traffic via a sub-path (like `/app`), the backend application frequently expects requests at the root path `/`. We use annotations to rewrite the path before forwarding it to the backend:

#### Basic URL Path Rewrite
```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
```
*   *Request:* `http://my-store.com/pay` → *Forwarded to service as:* `http://pay-service:80/`

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
*   *Request:* `http://store.com/service1/login` → *Forwarded to service as:* `http://service1:80/login`

---

### 6.7 Hands-on Lab: Ingress Controllers & KinD Setup
To run Ingress local testing using KinD (Kubernetes in Docker), you must map host ports `80` and `443` into the KinD node containers during cluster bootstrapping.

#### 1. Cluster Configuration Manifest (`kind-ingress-config.yaml`)
```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
```
Bootstrap the cluster:
```bash
kind create cluster --config kind-ingress-config.yaml
```

#### 2. Deploy Nginx Ingress Controller
Deploy the controller daemon configured for KinD port binding:
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

#### 3. Interactive Lab HTML Logs
*   **Ingress Lab 1 Logs:** [../Attachments/resources_lab01.html](../Attachments/resources_lab01.html) (embed: `![[../Attachments/resources_lab01.html]]`)
*   **Ingress Lab 2 (TLS) Logs:** [../Attachments/ingress+-+lab02+-+resources.html](../Attachments/ingress+-+lab02+-+resources.html) (embed: `![[../Attachments/ingress+-+lab02+-+resources.html]]`)

---

## 7. Advanced Service Networking & Modern APIs

As Kubernetes has scaled, legacy APIs like `Ingress` and `Endpoints` have shown limitations. Modern Kubernetes networking introduces specialized resources to handle L4/L7 routing, multi-tenancy, and routing efficiency.

### 7.1 The Gateway API
The **Gateway API** is an official, open-source set of resources that extends service networking in Kubernetes. Designed as the successor to `Ingress`, it offers a role-oriented, expressive, and extensible model.

```
                  [ GatewayClass ] (Managed by Infra Provider)
                         |
                    [ Gateway ]    (Managed by Cluster Operator)
                   /           \
           [ HTTPRoute ]   [ GPCRoute ] (Managed by App Developers)
           /           \         |
      [ service-a ] [ service-b ] [ service-c ]
```

#### 1. Role-Oriented Design & Hierarchy:
*   **`GatewayClass` (Cluster-Scoped):** Defines a template for a gateway implementation (e.g., an Envoy-backed load balancer, an F5 hardware appliance, or an AWS load balancer). Managed by the **Infrastructure Provider**.
*   **`Gateway` (Namespace-Scoped):** Requests an entry point for traffic. It defines the listeners (port, protocol, TLS config) and references a `GatewayClass`. Managed by the **Cluster Operator**.
*   **`HTTPRoute` / `GRPCRoute` / `TCPRoute` / `TLSRoute`:** Defines protocol-specific routing rules from a `Gateway` listener to backends. Managed by **Application Developers**.

#### 2. Comparison with Ingress:
| Feature | Legacy Ingress API | Modern Gateway API |
| :--- | :--- | :--- |
| **Configuration Model** | Monolithic (everything in one resource) | Distributed (split across classes, gateways, and routes) |
| **Multi-tenancy** | Poor (hard to delegate paths to namespaces safely) | Built-in (routes in other namespaces bind to gateways) |
| **Portability** | Heavy reliance on custom annotations | Native, standardized resource fields |
| **Protocols Supported** | Primarily HTTP/HTTPS | HTTP, HTTPS, gRPC, TCP, UDP, TLS |

#### Example Gateway API Manifest (Gateway & HTTPRoute):
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: prod-gateway
  namespace: infra-ns
spec:
  gatewayClassName: internal-envoy
  listeners:
  - name: http
    protocol: HTTP
    port: 80
    allowedRoutes:
      namespaces:
        from: Selector
        selector:
          matchLabels:
            shared-gateway: "true"
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: app-route
  namespace: app-ns
spec:
  parentRefs:
  - name: prod-gateway
    namespace: infra-ns
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /v1
    backendRefs:
    - name: web-service
      port: 8080
      weight: 90
    - name: canary-service
      port: 8080
      weight: 10
```

#### 3. Installing NGINX Gateway Controller
The Gateway API defines standard custom resources (CRDs), but requires an active controller to implement the logic. For standard deployments (e.g., using NGINX Gateway Fabric), installation involves:
```bash
# 1. Install standard Gateway API CRDs
kubectl kustomize "https://github.com/nginx/nginx-gateway-fabric/config/crd/gateway-api/standard?ref=v1.6.2" | kubectl apply -f -

# 2. Install experimental Gateway API CRDs (if using advanced features like rewrites)
kubectl kustomize "https://github.com/nginx/nginx-gateway-fabric/config/crd/gateway-api/experimental?ref=v1.6.2" | kubectl apply -f -

# 3. Install NGINX Gateway Controller using Helm
helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric --create-namespace -n nginx-gateway
```

#### 4. Advanced HTTPRoute Filters (Redirects, Rewrites, Headers, and Mirroring)
Gateway API specifies traffic modifications directly within the resource specs using filters, bypassing the need for ad-hoc annotations.

##### A. HTTP to HTTPS Schema Redirect (`RequestRedirect`):
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: https-redirect
  namespace: default
spec:
  parentRefs:
  - name: nginx-gateway
  rules:
  - filters:
    - type: RequestRedirect
      requestRedirect:
        scheme: https
```

##### B. Prefix Path Rewrite (`URLRewrite`):
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: rewrite-path
  namespace: default
spec:
  parentRefs:
  - name: nginx-gateway
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /old
    filters:
    - type: URLRewrite
      urlRewrite:
        path:
          replacePrefixMatch: /new
    backendRefs:
    - name: my-app
      port: 80
```

##### C. Custom Header Injection (`RequestHeaderModifier`):
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: header-mod
  namespace: default
spec:
  parentRefs:
  - name: nginx-gateway
  rules:
  - filters:
    - type: RequestHeaderModifier
      requestHeaderModifier:
        add:
        - name: x-env
          value: staging
    backendRefs:
    - name: my-app
      port: 80
```

##### D. Request Mirroring (`RequestMirror`):
Sends a copy of incoming traffic to a test/analysis service concurrently without impacting the response returned to the user:
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: request-mirror
  namespace: default
spec:
  parentRefs:
  - name: nginx-gateway
  rules:
  - filters:
    - type: RequestMirror
      requestMirror:
        backendRef:
          name: mirror-service
          port: 80
    backendRefs:
    - name: my-app
      port: 80
```

#### 5. gRPC Routing
Exposing high-performance gRPC services can be done natively matching on methods or services:
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: grpc-route
  namespace: default
spec:
  parentRefs:
  - name: nginx-gateway
  rules:
  - matches:
    - method:
        service: my.grpc.Service
        method: GetData
    backendRefs:
    - name: grpc-service
      port: 50051
```

#### 6. Layer 4 TCP/UDP Listeners & TLS Termination

##### A. TLS Termination Gateway (Decrypt at ingress):
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: nginx-gateway-tls
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
  - name: https
    protocol: HTTPS
    port: 443
    tls:
      mode: Terminate
      certificateRefs:
      - kind: Secret
        name: tls-secret
    allowedRoutes:
      namespaces:
        from: All
```

##### B. Layer 4 TCP Gateway (e.g., exposing a MySQL Database):
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: tcp-gateway
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
  - name: tcp
    protocol: TCP
    port: 3306
    allowedRoutes:
      namespaces:
        from: All
```

##### C. Layer 4 UDP Gateway (e.g., exposing CoreDNS service):
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: udp-gateway
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
  - name: udp
    protocol: UDP
    port: 53
    allowedRoutes:
      namespaces:
        from: All
```

---

### 7.2 EndpointSlices
**EndpointSlices** provide a highly scalable way to track network endpoints (usually Pod IPs) within a Kubernetes cluster. They replace the monolithic legacy `Endpoints` resources.

#### 1. The Scalability Bottleneck of Legacy Endpoints:
The original `Endpoints` resource listed *every* Pod IP for a Service in a single object. If a Service had 5,000 pods, this object grew to megabytes. When a single pod crashed or was rescheduled:
1.  The entire `Endpoints` object had to be updated in the API server.
2.  The entire object was serialized and transmitted over the network to *every* node running `kube-proxy`.
3.  This caused high CPU usage on the control plane and node bottlenecks.

#### 2. The EndpointSlice Solution:
`EndpointSlices` slice the backend endpoints into smaller chunks (default: **100 endpoints per slice**). 
*   If a Service has 5,000 backend pods, Kubernetes creates 50 `EndpointSlice` objects.
*   When a pod IP changes, only one small slice is updated and transmitted, reducing network volume by $O(N)$ where $N$ is the number of pods.

#### 3. Endpoint Conditions:
Every endpoint tracked in an `EndpointSlice` maintains three conditions:
*   `Ready`: Indicates the Pod is healthy and ready to accept traffic.
*   `Serving`: Maps to the Pod's readiness probe status. Unlike `Ready`, it remains `true` even during Pod termination to support graceful shutdown drains.
*   `Terminating`: Indicates the Pod is actively shutting down (`SIGTERM` has been sent) but is still draining. `kube-proxy` can use this to complete current connections while ignoring the Pod for new requests.

```yaml
# Example EndpointSlice snippet
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: web-service-abcde
  labels:
    kubernetes.io/service-name: web-service
addressType: IPv4
ports:
  - name: http
    port: 80
    protocol: TCP
endpoints:
  - addresses:
      - "10.244.1.45"
    conditions:
      ready: true
      serving: true
      terminating: false
    nodeName: worker-node-1
    topology:
      kubernetes.io/zone: us-east-1a
```

---

### 7.3 Topology Aware Routing & Internal Traffic Policies
To optimize routing, reduce latency, and avoid cross-availability-zone data transfer costs, Kubernetes offers advanced traffic-routing parameters.

#### 1. Topology Aware Routing (Zone Preference):
When you enable Topology Aware Routing, the `EndpointSlice` controller appends topology "hints" to endpoints. These hints instruct `kube-proxy` to route traffic to endpoints in the same availability zone.
*   **Enabling:** Add the following annotation to a Service:
    ```yaml
    metadata:
      annotations:
        service.kubernetes.io/topology-mode: Auto
    ```
*   **Constraints:**
    *   **Even Spread:** Pods must be spread evenly across zones (e.g., using `topologySpreadConstraints`).
    *   **Minimum Threshold:** If a zone has too few endpoints relative to its incoming traffic (usually less than 3 endpoints), the controller disables routing hints, falling back to cross-zone traffic to ensure service availability.

#### 2. Internal Traffic Policy (`Cluster` vs `Local`):
Controls how in-cluster clients (Pods) send traffic to Services:
*   `spec.internalTrafficPolicy: Cluster` (Default): Traffic is routed to any available endpoint in the cluster.
*   `spec.internalTrafficPolicy: Local`: Traffic is restricted to endpoints located **only on the same node** as the calling Pod.
    *   *Benefits:* Zero network latency (node-local routing), avoiding network hops.
    *   *Risk:* If the local node has no Pod matching the Service selector, traffic is dropped (no fallback to other nodes). Useful for routing ingress controller traffic to node-level local pods.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: node-local-service
spec:
  selector:
    app: node-agent
  ports:
  - port: 80
    targetPort: 8080
  internalTrafficPolicy: Local
```

---

### 7.4 Service ClusterIP Allocation & CIDR Management (v1.26+)
To prevent collisions when assigning virtual IPs (ClusterIPs) to Services, modern Kubernetes clusters use advanced allocation engines.

#### 1. Range Reservation Mechanics (v1.26+):
Before v1.26, manually assigning a static `clusterIP` carried the risk of colliding with an automatically assigned (dynamic) ClusterIP. To prevent this, Kubernetes reserves a segment of the `service-cluster-ip-range`:
*   The Service CIDR is divided into two bands based on the formula: `bandOffset = min(max(16, cidrSize / 16), 256)`.
*   The **lower band** (from the start of the range up to the `bandOffset` size) is reserved for static allocations (user-specified IPs).
*   The **upper band** is preferred for dynamic allocations (automatically chosen IPs).
*   Dynamic allocations will only use the lower band if the upper band is completely exhausted, preventing collisions between automated and manual IP assignments.

#### 2. Dynamic Service CIDR Expansion (v1.29+):
If a cluster runs out of Service IPs, updating the `--service-cluster-ip-range` on `kube-apiserver` is highly disruptive. v1.29+ introduces stable dynamic expansion via the `ServiceCIDR` API:
*   A cluster can have multiple `ServiceCIDR` resources.
*   The `MultiCIDRServiceAllocator` allocator pools these ranges, dynamically allocating IPs from the newly added blocks without API server restarts.

```yaml
apiVersion: networking.k8s.io/v1alpha1
kind: ServiceCIDR
metadata:
  name: extra-service-range
spec:
  cidrs:
  - 10.96.128.0/20
```

---

## 8. Diagnostics and Verification Cheat Sheet

Use these command patterns to troubleshoot networking, DNS, Ingress, and Gateway routing issues in the cluster.

```bash
# ==============================================================================
# Host Network and Namespace Inspection
# ==============================================================================
# List network interfaces on the current host node
ip link show

# List bridge interfaces on the host (e.g. cni0)
ip address show type bridge

# Find component listening ports (e.g. kube-scheduler port 10259)
netstat -npl | grep -i scheduler

# Find established connections for ETCD client (2379) or peer (2380) ports
netstat -npa | grep -i etcd

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
# Service, EndpointSlice, and Routing Debugging
# ==============================================================================
# List EndpointSlices for a specific service
kubectl get endpointslice -l kubernetes.io/service-name=<service-name>

# Inspect EndpointSlice conditions (Ready, Serving, Terminating)
kubectl get endpointslice <slice-name> -o yaml

# Inspect iptables NAT chains to identify service endpoints
iptables -t nat -L KUBE-SERVICES -n -v

# Inspect IPVS routing rules if kube-proxy is operating in IPVS mode
ipvsadm -ln

# Query the ClusterIP range configured for API Server services
ps -aux | grep kube-apiserver | grep -oE "\-\-service-cluster-ip-range=[^ ]+"

# Check if ServiceCIDR expansion is active (v1.29+)
kubectl get servicecidrs

# ==============================================================================
# DNS Operations and Resolution Checks
# ==============================================================================
# Resolve a service name using a debug pod
kubectl run dns-tester --image=busybox:1.28 --restart=Never --rm -it -- nslookup kubernetes.default.svc.cluster.local

# View logs from CoreDNS to identify query resolution failures
kubectl logs -n kube-system -l k8s-app=kube-dns --tail=100

# ==============================================================================
# Ingress and Gateway Routing Verification
# ==============================================================================
# Check detailed configurations for a deployed Ingress resource
kubectl describe ingress <ingress-name>

# Check log output from the Nginx Ingress Controller
kubectl logs -n ingress-nginx deployment/ingress-nginx-controller

# Query Gateway API resources in the cluster
kubectl get gatewayclasses,gateways,httproutes -A

# Inspect a Gateway's status for bind or listener errors
kubectl describe gateway <gateway-name> -n <namespace>
```

---

### 📖 Sources & Ingested Transcripts
- CKA Course Transcript Segment: `inflow/IngressController.md`
- Inflow Source note: `inflow/Services-Load Balancing-Networking.md`
- Official Documentation References:
  - [Services and Networking Concepts](https://kubernetes.io/docs/concepts/services-networking/)
  - [Print View](https://kubernetes.io/docs/concepts/services-networking/_print)
  - [Cluster IP Allocation](https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation)
  - [DNS for Pods and Services](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service)
  - [IPv4/IPv6 Dual-Stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack)
  - [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices)
  - [Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway)
  - [Ingress API](https://kubernetes.io/docs/concepts/services-networking/ingress)
  - [Ingress Controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers)
  - [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies)
  - [Services API](https://kubernetes.io/docs/concepts/services-networking/service)
