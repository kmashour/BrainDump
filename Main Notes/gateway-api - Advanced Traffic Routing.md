---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[gateway-api]]"
sub_type: core-concept
source_type: documentation
source_url: "https://gateway-api.sigs.k8s.io/"
tags:
  - kubernetes/gateway-api
  - kubernetes/networking
  - kubernetes/deep-dive
---

# gateway-api - Advanced Traffic Routing

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[gateway-api]] > **Advanced Traffic Routing**

---

## 📑 Gateway API Blueprints & Configurations

This note outlines standard, implementation-agnostic configurations for the Kubernetes **Gateway API**, demonstrating redirects, rewrites, header modifications, L4 listeners, and gRPC routing.

---

### 1. Installation & Base Setup
Before configuring routing resources, ensure the Gateway API CRDs and controller are deployed.

#### A. Deploy standard CRDs:
```bash
# Standard CRDs (HTTPRoute, Gateway, GatewayClass)
kubectl kustomize "https://github.com/nginx/nginx-gateway-fabric/config/crd/gateway-api/standard?ref=v1.6.2" | kubectl apply -f -

# Experimental CRDs (Required for URLRewrite / redirects)
kubectl kustomize "https://github.com/nginx/nginx-gateway-fabric/config/crd/gateway-api/experimental?ref=v1.6.2" | kubectl apply -f -
```

#### B. Deploy Controller (e.g. NGINX Gateway Fabric):
```bash
helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric --create-namespace -n nginx-gateway
```

#### C. Instantiate GatewayClass:
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: nginx
spec:
  controllerName: nginx.org/gateway-controller
```

---

### 2. HTTP/HTTPS listeners & TLS Termination
A Gateway resource acts as the ingress load balancer listener.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: secured-gateway
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
  - name: http
    protocol: HTTP
    port: 80
    allowedRoutes:
      namespaces:
        from: All
  - name: https
    protocol: HTTPS
    port: 443
    tls:
      mode: Terminate
      certificateRefs:
      - kind: Secret
        name: prod-tls-secret
    allowedRoutes:
      namespaces:
        from: All
```

---

### 3. HTTPRoute Routing & Traffic Modification Filters

#### A. HTTP to HTTPS Schema Redirect (`RequestRedirect`):
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http-redirect-route
  namespace: default
spec:
  parentRefs:
  - name: secured-gateway
  rules:
  - filters:
    - type: RequestRedirect
      requestRedirect:
        scheme: https
        statusCode: 301
```

#### B. Prefix Path Rewrite (`URLRewrite`):
Replaces matching prefix paths (e.g. `/old-path`) with the desired prefix (`/new-path`) before forwarding to the backend service.
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: rewrite-route
  namespace: default
spec:
  parentRefs:
  - name: secured-gateway
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /old-path
    filters:
    - type: URLRewrite
      urlRewrite:
        path:
          replacePrefixMatch: /new-path
    backendRefs:
    - name: web-app-service
      port: 8080
```

#### C. Custom Header Injection (`RequestHeaderModifier`):
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: header-mod-route
  namespace: default
spec:
  parentRefs:
  - name: secured-gateway
  rules:
  - filters:
    - type: RequestHeaderModifier
      requestHeaderModifier:
        add:
        - name: x-env
          value: production
    backendRefs:
    - name: backend-service
      port: 80
```

#### D. Request Mirroring (`RequestMirror`):
Forwards a duplicate stream of traffic to a secondary service (e.g. for testing) without impacting primary responses.
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: mirror-route
  namespace: default
spec:
  parentRefs:
  - name: secured-gateway
  rules:
  - filters:
    - type: RequestMirror
      requestMirror:
        backendRef:
          name: staging-mirror-service
          port: 8080
    backendRefs:
    - name: production-service
      port: 8080
```

---

### 4. Layer 4 TCP/UDP Listener Gateways

#### A. MySQL Database L4 TCP Listener:
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: mysql-gateway
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
  - name: mysql-tcp
    protocol: TCP
    port: 3306
    allowedRoutes:
      namespaces:
        from: All
```

#### B. DNS Service L4 UDP Listener:
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: dns-gateway
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
  - name: dns-udp
    protocol: UDP
    port: 53
    allowedRoutes:
      namespaces:
        from: All
```

---

### 5. gRPC Routing HTTPRoute
gRPC calls can be routed natively matching on specific service names and methods.
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: grpc-api-route
  namespace: default
spec:
  parentRefs:
  - name: secured-gateway
  rules:
  - matches:
    - method:
        service: internal.api.v1.BillingService
        method: ProcessInvoice
    backendRefs:
    - name: billing-grpc-service
      port: 50051
```

*Read more in [[Reference Notes/0-9_networking_dns_and_ingress.md#7.1 The Gateway API]]*
