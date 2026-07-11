---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - cncf/ingress
  - kubernetes/networking
  - status/completed
---

# Module 12-4: Ingress Controllers and Traffic Routing (Mumshad Lecture)

**Breadcrumbs:** [[12-Index - CNCF References|🏠 CNCF References Index]] > **Ingress Controllers and Traffic Routing**

---

> [!NOTE]
> **Source Citation**
> This reference module compiles the lecture transcript **inflow/IngressController.md** from the CKA exam course. It covers the evolutionary rationale behind Kubernetes Ingress, compares NodePort/LoadBalancer limitations to L7 Ingress solutions, explains the NGINX Ingress Controller architecture (ConfigMap, ServiceAccount, Deployment, Service), and details host/path routing configurations.

---

## 🎯 The Evolutionary Problem: NodePort & LoadBalancer Constraints

Exposing multiple applications to external clients without Ingress leads to architectural complexity and high cloud costs.

### 1. NodePort Limitations
* **High Ports:** NodePorts can only allocate high-numbered port ranges (`30000-32767`). External users cannot access the app on standard HTTP/HTTPS ports (80/443) directly.
* **External Proxies Needed:** To map standard ports (e.g., `http://my-store.com`), administrators must deploy external reverse proxy servers (like NGINX/HAProxy) in front of the cluster to forward port 80 requests to port 30080 on the nodes.
* **DNS Overhead:** Requires mapping DNS entries to node IP addresses directly, which breaks if nodes are replaced or rescheduled.

### 2. Cloud LoadBalancer (L4) Limitations
* **One LoadBalancer per Service:** Creating a Service of type `LoadBalancer` triggers the cloud provider to provision an external L4 network Load Balancer.
* **Prohibitive Costs:** Having a dedicated Load Balancer for every single microservice (e.g., `web-service`, `video-service`, `auth-service`) dramatically increases cloud bills.
* **Configuration Overhead:** Reconfiguring DNS entries and firewalls for each service is manual and slow.

---

## 🏛️ The Solution: Layer 7 Ingress

Kubernetes **Ingress** acts as a unified Layer 7 application load balancer built directly into the cluster. It centralizes traffic routing, SSL/TLS termination, and path rewrites, exposing all services via a single external Load Balancer or NodePort entry point.

```
                  +-----------------------------------+
                  |           External DNS            |
                  |     (my-store.com / watch.com)    |
                  +-----------------+-----------------+
                                    |
                                    v
                  +-----------------+-----------------+
                  |       Cloud L4 LoadBalancer       |
                  |     (Unified Entry IP / Port)     |
                  +-----------------+-----------------+
                                    |
                                    v
            +-----------------------+-----------------------+
            |      Ingress Controller (NGINX Proxy Pods)     |
            |       - SSL/TLS Termination & Routing -       |
            +-----------+-----------------------+-----------+
                        |                       |
            (Path: /wear) |                       | (Path: /watch)
                        v                       v
            +-----------+-----------+   +-------+-----------+
            | wear-service (Cluster)|   | watch-service     |
            +-----------+-----------+   +-------+-----------+
                        |                       |
                        v                       v
               [wear-pods (IP)]        [watch-pods (IP)]
```

---

## 🏗️ Ingress Controller vs. Ingress Resource

Ingress is split into two distinct components:

1. **Ingress Controller (The Data Plane):**
   * The actual reverse proxy workload (typically NGINX, Traefik, HAProxy, or Envoy) that handles the traffic routing.
   * **Crucial:** Kubernetes clusters **do not** include an Ingress Controller by default. It must be deployed manually before any rules take effect.
   * It runs a control loop that watches the Kubernetes API for Ingress resource changes, translates them into proxy configuration (e.g., `nginx.conf`), and reloads the engine dynamically.
2. **Ingress Resource (The Control Plane Rules):**
   * A declarative Kubernetes manifest (`kind: Ingress`) detailing the paths, hostnames, and TLS configurations mapping to backing services.

---

## 🧱 NGINX Ingress Controller Components

Deploying a production-grade NGINX Ingress Controller requires four foundational objects:

### 1. Ingress Controller Deployment
Runs the custom NGINX image (`ingress-nginx/controller`) which runs the proxy process.
* **Arguments:** Must specify `--configmap=$(POD_NAMESPACE)/nginx-configuration` to bind to the ConfigMap.
* **Env Variables:** Expects `POD_NAME` and `POD_NAMESPACE` to query API metadata.

### 2. ConfigMap Configuration
An empty or parameterized ConfigMap (`nginx-configuration`). This decouples application-specific NGINX settings (such as logs, keepalive timeout, proxy buffers) from the controller pod definition.

### 3. Exposing Service
A Service of type `NodePort` or `LoadBalancer` that exposes ports 80 and 443 of the Ingress Controller Pods to the external network. This is a one-time setup.

### 4. ServiceAccount & RBAC Roles
Because the controller must read resources across the cluster to update routing tables, it must run with a designated `ServiceAccount` bound to a `ClusterRole` granting `watch`, `list`, and `get` access on:
* `Services`, `Endpoints`, `Pods`, `ConfigMaps`, `Ingress`, and `Secrets`.

---

## 🛠️ Ingress Resource Configurations & Examples

Ingress rules are configured in three primary routing topologies:

### 1. Single Backend (No Host/Path Rules)
Directs all incoming traffic to one service.
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: single-backend-ingress
spec:
  defaultBackend:
    service:
      name: wear-service
      port:
        number: 80
```

### 2. Path-Based Routing (Single Domain, Multiple URL Paths)
Routes traffic to different services depending on the HTTP request URL path.
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: path-based-ingress
spec:
  rules:
  - host: my-store.com
    http:
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

### 3. Host-Based Routing (Multiple Domains / Hostnames)
Routes traffic to services based on the HTTP `Host` header, allowing virtual hosting on a single IP address.
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: host-based-ingress
spec:
  rules:
  - host: wear.my-store.com
    http:
      paths:
      - pathType: Prefix
        path: /
        backend:
          service:
            name: wear-service
            port:
              number: 80
  - host: watch.my-store.com
    http:
      paths:
      - pathType: Prefix
        path: /
        backend:
          service:
            name: watch-service
            port:
              number: 80
```

---

## 🔒 TLS/SSL Termination Setup

To secure external traffic using HTTPS, Ingress controllers terminate TLS using private keys and certificates stored in Kubernetes TLS Secrets:

1. **Create the Secret:**
   ```bash
   kubectl create secret tls my-store-tls-secret \
     --cert=path/to/cert.pem \
     --key=path/to/key.key
   ```
2. **Reference the Secret in the Ingress Manifest:**
   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: secure-ingress
   spec:
     tls:
     - hosts:
       - my-store.com
       secretName: my-store-tls-secret
     rules:
     - host: my-store.com
       http:
         paths:
         - path: /
           pathType: Prefix
           backend:
             service:
               name: wear-service
               port:
                 number: 80
   ```

---

## 🔍 Diagnostics & CLI Verification

```bash
# Get basic ingress information (exposes address/IP)
kubectl get ingress

# Get detailed description (shows routing rules and default backends)
kubectl describe ingress <ingress-name>

# View logs of the NGINX Ingress Controller to debug routing and reloads
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx
```
