---
class: exam-checklist
tier: project-note
project: 'CKA Exam'
status: 'Ready for Review'
---

# CKA Exam Checklist - Troubleshooting and Networking

This guide covers diagnostic workflows for application failures, control plane static pods, worker node systems, and cluster networking components.

---

## 1. Troubleshooting Application Failures

Application failures include pods not starting, crashing, or failing service routing.

### 1.1 Pod Status Diagnostics
*   **`ImagePullBackOff` / `ErrImagePull`**: Typos in image names or tags. Check `spec.containers[*].image` and verify that required `imagePullSecrets` are present.
*   **`CrashLoopBackOff`**: Application starts but exits repeatedly. Check pod logs (especially `--previous`).
*   **`RunContainerError`**: Failed mounts (ConfigMap/Secret/PVC missing or misconfigured).
*   **`CreateContainerConfigError`**: Referencing a missing ConfigMap/Secret key in `env` or `envFrom`.
*   **`OOMKilled` (Exit Code 137)**: Container exceeded its memory limit. Increase `spec.containers[*].resources.limits.memory`.

### 1.2 Diagnostic Commands
```bash
# 1. Inspect events and conditions
kubectl describe pod <pod-name>

# 2. View last 100 lines of container logs
kubectl logs <pod-name> --tail=100

# 3. View logs of the crashed container instance
kubectl logs <pod-name> --previous

# 4. Exec into container to test local files
kubectl exec -it <pod-name> -c <container-name> -- /bin/sh
```

### 1.3 Standalone Pod Re-creation & Force-Replace Workflows
Unlike Deployments, DaemonSets, or StatefulSets, standalone Pods are fundamentally immutable. Modifying fields other than `spec.containers[*].image`, `spec.activeDeadlineSeconds`, or `spec.tolerations` (additions only) directly on a running Pod will trigger a `403 Forbidden` API error.

#### Workflow A: The 'kubectl edit' & Temp File Recovery Playbook (Exam Speed Hack)
When you run `kubectl edit pod <pod-name>` to modify an environment variable, volume mount, or port, the API server will reject the change on save:
1. **Trigger Rejection**: Save and exit the editor (`:wq` in Vim). You will see:
   ```plaintext
   error: pods "<pod-name>" is invalid
   A copy of your changes has been stored to "/tmp/kubectl-edit-xxxx.yaml"
   error: Edit cancelled, no changes made.
   ```
2. **Execute Force-Replace**: Instantly recreate the Pod by running the exact command:
   ```bash
   kubectl replace --force -f /tmp/kubectl-edit-xxxx.yaml
   ```
   *Note: In the CKA exam, do not waste time creating a new YAML manifest manually if this happens. Instantly force-replace it using the temporary file path provided in the error output.*

#### Workflow B: The Manual Export Recovery Workflow
If you need to make changes using a localized config file first:
1. **Export definition**:
   ```bash
   kubectl get pod <pod-name> -o yaml > pod-recovery.yaml
   ```
2. **Edit configuration**: Modify `pod-recovery.yaml` (e.g., fix env variables, resources, or ports).
3. **Execute replacement**:
   ```bash
   kubectl replace --force -f pod-recovery.yaml
   ```

#### Under the Hood: What `--force` Does
* **Immediate Deletion**: The `kubectl replace --force` command sends a deletion request with `grace-period=0`, bypassing the default 30-second graceful termination delay.
* **Process Signal Escalation**: Instead of sending a `SIGTERM` signal (giving the process time to shut down gracefully) followed by a 30-second countdown, the container runtime immediately issues a `SIGKILL` (Signal 9) to PID 1 in the container's namespace.
* **Instant Re-creation**: The cgroups, namespaces, and mounts are instantly destroyed, and the resource is immediately re-created with the new spec from the file. This ensures minimum downtime during the exam.


---

## 2. Troubleshooting Control Plane Failures

The control plane consists of `kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, and `etcd`. In `kubeadm` clusters, these run as Static Pods.

### 2.1 Static Pod Manifest Auditing
If the API Server is down (`connection refused` on port `6443`), SSH to the control plane node:
*   **Manifest Path**: `/etc/kubernetes/manifests/`
    *   API Server: `kube-apiserver.yaml`
    *   Controller Manager: `kube-controller-manager.yaml`
    *   Scheduler: `kube-scheduler.yaml`
    *   ETCD: `etcd.yaml`

### 2.2 Control Plane Diagnostics Flow
1.  **Check Kubelet Status**: Static pods will not run if kubelet is stopped.
    ```bash
    systemctl status kubelet
    journalctl -u kubelet -n 100 -f
    ```
2.  **Inspect Container Runtime**: Query running containers directly when API Server is down.
    ```bash
    crictl ps -a
    crictl logs <container-id>
    ```
3.  **Check for Common Errors**:
    *   Typos in certificate file paths inside manifests (e.g. `/etc/kubernetes/pki/`).
    *   Syntax errors (incorrect yaml indentation).
    *   Typos in binaries or arguments.

> [!TIP]
> **Static Pod Reload Trick:** If a static pod is stuck, force the Kubelet to reload it by moving its manifest file out of `/etc/kubernetes/manifests/`, waiting 10 seconds, and moving it back.

---

## 3. Troubleshooting Worker Node Failures

Worker node failures cause nodes to switch to a `NotReady` or `Unknown` state.

### 3.1 Node Readiness Verification
```bash
# Check general node status
kubectl get nodes -o wide

# Inspect node conditions (MemoryPressure, DiskPressure, PIDPressure, Ready)
kubectl describe node <node-name>
```

### 3.2 Kubelet Service Debugging (Execute on Worker Node)
1.  **Verify Service Status**:
    ```bash
    systemctl status kubelet
    ```
2.  **Check Logs for Failures**:
    ```bash
    journalctl -u kubelet -n 100 --no-pager -f
    ```
3.  **Common Issue 1: CA Certificate path typos**
    *   *Symptom*: Kubelet fails to start, reporting: `unable to load client CA file... no such file or directory`.
    *   *Fix*: Find config path (usually `--config` in `systemctl cat kubelet`, pointing to `/var/lib/kubelet/config.yaml`). Edit `/var/lib/kubelet/config.yaml` to correct `clientCAFile`.
4.  **Common Issue 2: Incorrect API Server Port in Kubeconfig**
    *   *Symptom*: Kubelet runs but cannot contact the API server. Logs report connection refused on a port like `6553`.
    *   *Fix*: Open Kubelet's kubeconfig file `/etc/kubernetes/kubelet.conf`. Locate `server` and fix the port (e.g. from `6553` to `6443`):
    ```yaml
    clusters:
    - cluster:
        server: https://controlplane:6443 # Fix port here
    ```
    Then run:
    ```bash
    systemctl restart kubelet
    ```

### 3.3 Container Runtime Interface (CRI) Diagnostics
Verify that the runtime is running:
```bash
systemctl status containerd
```

Configure `crictl` to target the containerd socket (edit `/etc/crictl.yaml`):
```yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
```

Use `crictl` for local container checks:
```bash
crictl pods
crictl ps -a
crictl logs <container-id>
```

---

## 4. Troubleshooting Cluster Networking

Cluster networking failures include CNI failures, service routing issues, and CoreDNS name resolution issues.

### 4.1 CNI Failures
If CNI is misconfigured or not running, pods stay stuck in `ContainerCreating` or `Pending`.
*   Verify that configuration files exist in `/etc/cni/net.d/` (e.g., `10-flannel.conflist`, `10-calico.conflist`).
*   Verify CNI binaries in `/opt/cni/bin/`.
*   Deploy a CNI if missing:
    ```bash
    kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
    ```

### 4.2 Service Routing & Kube-Proxy Failures
If pod-to-pod IP traffic works, but Service IPs fail to route:
1.  **Check Kube-Proxy Pods**:
    ```bash
    kubectl get pods -n kube-system -l k8s-app=kube-proxy
    ```
2.  **Inspect Kube-Proxy Logs**:
    ```bash
    kubectl logs -n kube-system -l k8s-app=kube-proxy
    ```
    *Common Error*: Kube-proxy fails to start because of a typo in the config file argument path (e.g. `--config=/var/lib/kube-proxy/configuration.conf` instead of `/var/lib/kube-proxy/config.conf`). Edit the DaemonSet to fix:
    ```bash
    kubectl edit ds -n kube-system kube-proxy
    ```
3.  **Audit host rules (iptables or IPVS)**:
    ```bash
    # Search for Service ClusterIP rules in iptables
    iptables-save | grep <service-cluster-ip>
    
    # Or list virtual servers if in IPVS mode
    ipvsadm -ln
    ```

### 4.3 CoreDNS Resolution Failures
If internal service names fail to resolve:
1.  **Check CoreDNS Pods & Service**:
    ```bash
    kubectl get pods -n kube-system -l k8s-app=kube-dns
    kubectl get svc -n kube-system kube-dns
    ```
2.  **Test DNS Resolution using a temporary busybox pod**:
    ```bash
    kubectl run dns-test-util --image=registry.k8s.io/e2e-test-images/jessie-dnsutils:1.7 --restart=Never -- sleep 3600
    
    # Run nslookup
    kubectl exec dns-test-util -- nslookup kubernetes.default
    ```
3.  **Check CoreDNS ConfigMap**:
    ```bash
    kubectl get cm -n kube-system coredns -o yaml
    ```
    Ensure the `Corefile` has a valid `forward` directive pointing to `/etc/resolv.conf`.

---

### 4.4 Ingress L7 Path Rewriting
If a backend application serves traffic at the root path `/` but the Ingress path is `/api`, configure the Ingress controller to rewrite the path before forwarding the request.

#### Option A: Basic URL path rewrite
Add the `rewrite-target` annotation:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: my-app.local
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8080
```
*   *Behavior*: Request `http://my-app.local/api` is rewritten and forwarded to the backend service as `/`.

#### Option B: Dynamic Regex Path Rewrite
To forward subpaths dynamically, capture groups in regex:
```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
spec:
  rules:
  - host: my-app.local
    http:
      paths:
      - path: /app(/|$)(.*)
        pathType: Prefix
        backend:
          service:
            name: app-service
            port:
              number: 80
```
*   *Behavior*: Request `http://my-app.local/app/profile` matches the second capture group (`(.*)`) and is forwarded to the backend service as `/profile`.
