---
obsidianUIMode: preview
class: deeper-dive
tier: main-note
parent_concept: "[[Kubernetes Network Security and Traffic Segregation]]"
sub_type: mechanics
source_type: gemini-chat
author: "Antigravity Assistant"
course_title: "CKS Real Exam Blueprint & Ingress Hardening"
tags:
  - kubernetes/security
  - kubernetes/networking
  - kubernetes/ingress
  - kubernetes/tls
  - kubernetes/cks
  - kubernetes/deep-dive
---

# Kubernetes Ingress Security - TLS Termination, Force-HTTPS, and Controller Annotations

**Breadcrumbs:** [[Main Notes/0-Index|🏠 Index]] > [[Kubernetes Network Security and Traffic Segregation]] > **Ingress Security - TLS Termination, Force-HTTPS, and Controller Annotations**

---

## 🎯 1. Architectural Foundations: Ingress Layer 7 TLS Termination

While NetworkPolicies operate at Layer 3 and Layer 4 to block or allow packet flows between IP subnets, the **Ingress Controller** (such as Nginx Ingress or Cilium Ingress) functions as a Layer 7 reverse proxy and SSL edge terminator.

```
[ Outside User / Client ]
            │
            ├──── Plaintext HTTP (Port 80) ────► [ Ingress Controller ]
            │                                           │
            │ <── 301/308 Redirect to HTTPS ────────────┤ (Forces HTTPS!)
            │
            └──── Encrypted HTTPS (Port 443) ──► [ Ingress Controller ]
                                                        │
                                          [Decrypts via TLS Secret]
                                                        │
                                                        ▼ (ClusterIP)
                                              [ Backend Web Pod ]
```

### The Ingress Edge Threat Vector
* Cleartext HTTP routes expose user credentials, authorization tokens, and confidential application data to eavesdropping across transit networks.
* The Ingress Controller terminates the external TLS session using certificates stored in a Kubernetes `kubernetes.io/tls` Secret, then routes traffic to cluster workloads.
* Plaintext traffic must be explicitly redirected (via HTTP 301 or 308) to HTTPS.

---

## ⚙️ 2. The Configuration Anatomy: Standard Spec vs. Vendor Annotations

The core Kubernetes `networking.k8s.io/v1` `Ingress` API standardizes routing rules (`spec.rules`) and TLS certificates (`spec.tls`). However, behavioral directives—such as forcing an automatic SSL redirect—are controlled via **vendor-specific annotations** under `metadata.annotations`.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  namespace: web-tier
  annotations:
    # Controller-specific SSL redirection directive:
    ingress.cilium.io/force-https: "enabled"
    # nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  ingressClassName: cilium       # Ingress controller class (e.g., cilium or nginx)
  tls:
  - hosts:
    - kodekloud.com             # FQDN matching the TLS certificate CN/SAN
    secretName: web-secret      # Namespaced Secret containing tls.crt and tls.key
  rules:
  - host: kodekloud.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-svc
            port:
              number: 80
```

---

## 💡 3. Exam Strategy: How to Handle Annotations Without Memorizing Them

> [!TIP]
> **Exam Navigation Protocol: The "Only Two" Ingress Annotations**
> You do **not** need to memorize an exhaustive dictionary of ingress annotations. In the CKS exam, there are only two annotations tested for Ingress TLS redirection:
> 
> | Controller | Annotation Key | Required Value | Where to Find It During the Exam |
> | :--- | :--- | :--- | :--- |
> | **Cilium Ingress** | `ingress.cilium.io/force-https` | `"enabled"` | **Provided directly in the exam prompt.** (Third-party docs like `cilium.io` are blocked in the exam browser; questions requiring Cilium explicitly include the annotation string). |
> | **Nginx Ingress** | `nginx.ingress.kubernetes.io/ssl-redirect` | `"true"` | **Allowed Whitelisted Docs:** `https://kubernetes.github.io/ingress-nginx/` (under Annotations page) or official `https://kubernetes.io/docs/` TLS sections. |
> 
> > [!WARNING]
> > **The String Quote Mandate:**
> > In Kubernetes manifests, annotations are `map[string]string`. They **MUST always be enclosed in double quotes** (`"true"`, `"enabled"`). If you write a bare boolean `ssl-redirect: true`, `kubectl` will reject the YAML with a schema validation error!
> 
> **The 3 Ways to Discover Annotations in the Exam:**
> 1. **The Question Prompt Itself:** Because annotations are controller-specific, Linux Foundation prompts frequently provide the exact annotation name or an embedded hyperlink leading directly to the Ingress NGINX annotations page.
> 2. **Allowed Ingress NGINX Docs:** Navigate to `https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/` and search `ssl-redirect`.
> 3. **The In-Cluster Scout Trick:** Query existing ingress resources across all namespaces:
> ```bash
> kubectl get ingress -A -o yaml | grep -E "annotations|ingress.cilium|nginx.ingress" -B 1 -A 5
> ```
> Or search locally in the course directories:
> ```bash
> grep -rn "force-https" /opt/course/ 2>/dev/null
> grep -rn "ssl-redirect" /opt/course/ 2>/dev/null
> ```

---

## ⚡ 4. Speed CLI Generator Formula

To avoid manual indentation errors in YAML during timed exam conditions, generate the complete Ingress skeleton with a single command:

```bash
kubectl create ingress web-ingress \
  -n web-tier \
  --class=cilium \
  --rule="kodekloud.com/*=web-svc:80,tls=web-secret" \
  --dry-run=client -o yaml > ing.yaml
```

This automatically populates:
1. `spec.ingressClassName: cilium`
2. `spec.tls[0].hosts: [kodekloud.com]` with `secretName: web-secret`
3. `spec.rules[0].host: kodekloud.com` with `path: /` and `pathType: Prefix`
4. Backend service targeting `web-svc:80`

Simply open `ing.yaml` in `vim`, insert the required annotation under `metadata.annotations`, and apply:
```bash
kubectl apply -f ing.yaml
```

---

## 🔍 5. Verification & Testing

```bash
# 1. Test Plaintext HTTP (Must return HTTP 301 or 308 Redirect)
curl -I http://kodekloud.com --resolve kodekloud.com:80:127.0.0.1

# 2. Test HTTPS (Must return HTTP 200 OK)
curl -k -I https://kodekloud.com --resolve kodekloud.com:443:127.0.0.1
```
