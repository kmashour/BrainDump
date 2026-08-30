---
obsidianUIMode: preview
class: reference-note
tier: reference-note
tags:
  - kubernetes/workloads
  - kubernetes/helm
---

# Module 0-6-4: Declarative Operations, Dry-Run Verification & Helm

**Breadcrumbs:** [[0-Index - Kubernetes|🏠 Kubernetes Reference MOC]] > **Module 0-6-4**

---

## 13. Production Verification, Auditing, and Dry-Run CLI Run Sheet

Mastering CLI commands for workloads is essential for passing the CKA exam and managing live cluster events.

### 13.1 Dry-Run Generation and Verification
Never write YAML manifests from scratch. Use imperative commands with `--dry-run=client -o yaml` to generate baseline files.

```bash
# Generate a baseline Pod manifest
kubectl run nginx-pod --image=nginx:alpine --dry-run=client -o yaml > pod.yaml

# Generate a Deployment manifest with 3 replicas
kubectl create deployment web-deploy --image=nginx:alpine --replicas=3 --dry-run=client -o yaml > deployment.yaml

# Generate a ClusterIP Service manifest exposing port 80 to 8080
kubectl create service clusterip web-svc --tcp=8080:80 --dry-run=client -o yaml > service.yaml

# Generate a CronJob manifest
kubectl create cronjob nightly-backup --schedule="0 1 * * *" --image=busybox --dry-run=client -o yaml -- sh -c "echo backup" > cronjob.yaml

# Validate a generated YAML manifest against the API without writing it
kubectl apply -f pod.yaml --dry-run=server
```

### 13.2 Real-Time Pod Debugging and Namespace Inspection
```bash
# Interrogate a Pod's phase, conditions, and events
kubectl describe pod <pod-name>

# Get Pods with wide formatting (shows Node name and Pod IP)
kubectl get pods -o wide

# Watch Pod status changes in real-time
kubectl get pods -w

# Output specific JSONPath elements (e.g., QoS class of all Pods)
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.qosClass}{"\n"}{end}'

# Fetch container exit codes from terminated Pods
kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[*].state.terminated.exitCode}'
```

### 13.3 Multi-Container and Init Container Diagnostics
```bash
# View logs of the main container inside a multi-container Pod
kubectl logs <pod-name> -c <app-container-name>

# View logs of a failed Init Container or Native Sidecar
kubectl logs <pod-name> -c <init-container-name>

# Stream logs of all containers in a Pod simultaneously
kubectl logs <pod-name> --all-containers=true -f

# Run command inside a specific container of a Pod
kubectl exec -it <pod-name> -c <container-name> -- /bin/sh
```

### 13.4 Ephemeral Container Debugging Run Sheet
```bash
# Inject a debugging container sharing the Network namespace
kubectl debug -it <running-pod-name> --image=busybox:1.28 --image-pull-policy=IfNotPresent

# Inject a container sharing both the Network and PID namespace of a target container
kubectl debug -it <running-pod-name> --image=nicolaka/netshoot --target=<target-app-container>

# Clone a crashing Pod, override the entrypoint to keep it alive, and drop into a shell
kubectl debug <crashing-pod-name> -it --copy-to=debug-pod-copy --container=<crashing-container-name> -- sh
```

### 13.5 Deployment Rollout and Scaling Operations
```bash
# Scale a deployment immediately to 10 replicas
kubectl scale deployment/web-deploy --replicas=10

# Update the image of a deployment container on the fly
kubectl set image deployment/web-deploy nginx-web=nginx:1.25.4-alpine

# Monitor the progress of a rolling update
kubectl rollout status deployment/web-deploy

# View the history of deployment revisions
kubectl rollout history deployment/web-deploy

# View details of a specific deployment revision
kubectl rollout history deployment/web-deploy --revision=2

# Rollback a deployment to the immediate previous revision
kubectl rollout undo deployment/web-deploy

# Rollback to a specific historical revision
kubectl rollout undo deployment/web-deploy --to-revision=2

# Pause a rollout to perform testing/canary steps
kubectl rollout pause deployment/web-deploy

# Resume a paused rollout
kubectl rollout resume deployment/web-deploy
```

### 13.6 Force Deletions and Cleanup
If a node goes offline, the API Server may block deletion of Pods because it cannot confirm termination with the Kubelet. Use force deletion to bypass this.

```bash
# Force delete a Pod immediately (bypasses graceful shutdown and deletes from API)
kubectl delete pod <pod-name> --grace-period=0 --force

# Force delete all Pods in a terminating state in the namespace
kubectl get pods | grep Terminating | awk '{print $1}' | xargs -I {} kubectl delete pod {} --grace-period=0 --force
```

### 13.7 Automated Workload Pattern Verification Script

To validate workload patterns automatically on a running Kubernetes cluster, use the verification script `Reference Notes/scripts/verify_workloads_poc.sh`.

#### 13.7.1 Scope of Automated Checks
The script deploys temporary resources to verify:
1. **Shared Unix Domain Sockets (`emptyDir`):** Boots a Python-based server and sidecar client, verifying data exchange over a shared socket mount.
2. **Localhost Network Port Sharing:** Verifies that a `curlimages/curl` container inside a Pod can query an `nginx:alpine` container over `localhost:80`.
3. **Native gRPC Health Probes:** Launches an `agnhost` container on port `5000` with native gRPC readiness check, asserting the Kubelet updates status to `Ready`.
4. **StatefulSet Headless DNS Audit:** Launches a `netshoot` debugging Pod to resolve SRV and A records for a two-replica StatefulSet, asserting that ordinals map precisely to Pod IPs.

#### 13.7.2 How to Execute the Script
```bash
# 1. Start your local environment (kind or minikube)
kind create cluster --name k8s-poc

# 2. Make the script executable
chmod +x "Reference Notes/scripts/verify_workloads_poc.sh"

# 3. Run the verification audit
./"Reference Notes/scripts/verify_workloads_poc.sh" --namespace default

# 4. Optional: Keep resources for debugging/inspection
./"Reference Notes/scripts/verify_workloads_poc.sh" --namespace default --keep
```

---

## 14. Application Packaging & Declarative Customization (Helm & Kustomize)

For complex multi-component applications, managing individual raw Kubernetes manifests is inefficient. Administrators use **Helm** and **Kustomize** to streamline deployment configurations.

### 14.1 Helm: The Kubernetes Package Manager
Helm packages multiple interdependent resources into a single versioned unit called a **Chart**. It template-interpolates parameters using a `values.yaml` file.

#### 14.1.1 Helm 2 vs. Helm 3 Architectural Evolution
*   **Tiller Removal (Security and Simplicity):**
    - **Helm 2 (Deprecated):** Utilized a server-side pod called **Tiller** running inside the cluster. The Helm CLI client sent requests to Tiller, which then executed them against the API Server. Because Tiller was typically granted `cluster-admin` privileges, it bypassed fine-grained RBAC controls, creating severe security vulnerabilities.
    - **Helm 3 (Modern):** Tiller was completely removed. The Helm client communicates directly with the Kubernetes API Server, using the authentication and permissions defined in the user's local `kubeconfig`. This natively respects Kubernetes RBAC constraints.
*   **Three-Way Strategic Merge Patch:**
    - **Helm 2:** Used a simple two-way merge, comparing only the manifest of the old Helm chart version and the new version. If a user made out-of-band manual changes using `kubectl` (such as changing an image version or adding annotations), Helm 2 did not inspect the live cluster state, resulting in manual adjustments being overwritten during upgrades or ignored during rollbacks.
    - **Helm 3:** Employs a three-way strategic merge patch by comparing:
      1. The chart template recorded in Helm storage.
      2. The target chart template to install/rollback.
      3. The live state of resources running in the cluster.
    - **Result:** Manual live additions (like sidecar injections) are preserved during upgrades, and out-of-band configuration drift is successfully identified and corrected during rollbacks.

#### Core Helm Commands (CKA Run Sheet):
*   **Add Repository:** Add charts repositories:
    ```bash
    helm repo add bitnami https://charts.bitnami.com/bitnami
    ```
*   **Update Repository Indices:** Fetch the latest chart indices:
    ```bash
    helm repo update
    ```
*   **Search for Charts:** Search the repo for specific applications:
    ```bash
    helm search repo nginx
    ```
*   **Install a Chart (Release):** Deploy a chart to the cluster with custom overrides:
    ```bash
    helm install my-release bitnami/nginx --set service.type=NodePort --namespace web-apps
    ```
*   **List Releases:** View all installed helm releases:
    ```bash
    helm list --all-namespaces
    ```
*   **Upgrade a Release:** Apply config changes or update chart version:
    ```bash
    helm upgrade my-release bitnami/nginx --set replicaCount=3
    ```
*   **Rollback a Release:** Revert to a previous release revision:
    ```bash
    helm rollback my-release 1
    ```
*   **Uninstall a Release:** Delete all resource objects managed by the release:
    ```bash
    helm uninstall my-release
    ```

---

### 14.2 Kustomize: Template-Free Customization
Kustomize is a template-free tool built directly into `kubectl` (via `kubectl apply -k <dir>`). It uses a `kustomization.yaml` file to apply overlays and patches on top of a common set of base manifests (allowing dev/staging/prod variance).

#### 14.2.1 Kustomize vs. Helm (Conceptual Comparison)
*   **Helm (Template-Based):**
    - Uses Go templating syntax (`{{ .Values.parameter }}`).
    - Manifests are not valid YAML on their own and must be compiled.
    - Highly functional (supports loops, conditionals, hooks, package repositories, and rollback state history).
    - Can become hard to read when heavily parameterized.
*   **Kustomize (Overlay-Based):**
    - Template-free customization.
    - All base manifests and overlay patches are 100% valid Kubernetes YAML.
    - Built-in directly to `kubectl`, requiring no additional binaries for basic apply workflows.
    - Simple and readable, but lacks loops, conditionals, and package management repository structures.

#### 14.2.2 Common Transformers
Kustomize provides standard transformers to apply settings globally across all resources imported by a `kustomization.yaml`:
*   **`namespace`:** Places all imported resources into a specific namespace.
    ```yaml
    namespace: dev-namespace
    ```
*   **`namePrefix` / `nameSuffix`:** Prepends or appends a string to the names of all resources.
    ```yaml
    namePrefix: dev-
    nameSuffix: -v1
    ```
*   **`commonLabels`:** Adds a common set of labels to all resources.
    ```yaml
    commonLabels:
      environment: development
      team: backend
    ```
*   **`commonAnnotations`:** Injects annotations across all resources.
    ```yaml
    commonAnnotations:
      monitoring: prometheus
    ```

#### 14.2.3 Surgical Modifications: Patches
When global transformations are too broad, patches allow targeting specific resources. Kustomize supports two main patch styles:
1.  **Strategic Merge Patch:** Overrides fields by supplying a partial standard Kubernetes manifest. Kustomize merges the fields automatically based on matching API Version, Kind, and Name.
    *   *Example (Scale replicas to 5):*
        ```yaml
        # replica-patch.yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: api-deployment
        spec:
          replicas: 5
        ```
2.  **JSON 6902 Patch:** Performs precise operations (`add`, `remove`, `replace`) targeting specific path coordinates inside a resource.
    *   *Example (Change a label component):*
        ```yaml
        patches:
          - target:
              kind: Deployment
              name: api-deployment
            patch: |
              - op: replace
                path: /spec/template/metadata/labels/component
                value: web
        ```

#### Crucial Alignment: Deprecated `bases` vs. `resources`
*   **Deprecated Syntax:** Historically, Kustomize configurations referenced bases using:
    ```yaml
    # DEPRECATED AND CAN CAUSE WARNINGS/FAILURES
    bases:
      - ../../base
    ```
*   **Recommended Syntax:** Modern versions of Kustomize (and `kubectl` integration) require the `resources` block:
    ```yaml
    # MODERN STANDARD
    resources:
      - ../../base
    ```

#### Fixing Deprecated Fields Automatically
If you encounter legacy manifests using `bases`, you can resolve them automatically by running the `edit fix` command:
```bash
# Fix deprecated fields inside kustomization.yaml in the current directory
kustomize edit fix
```
*(If the standalone `kustomize` binary is not installed, manually replace the `bases:` key with `resources:` in `kustomization.yaml` using a text editor like `nano` or `vi`).*

#### Ingress-to-Overlay Application Walkthrough
1. **Base Configuration (`my-app/base/`)**:
   Create a standard `kustomization.yaml` referencing the core deployment:
   ```yaml
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - deployment.yaml
   ```
2. **Production Overlay (`my-app/overlays/production/`)**:
   Create a patch `patch.yaml` to scale replicas to 3:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: my-app
   spec:
     replicas: 3
   ```
   Reference the base using the modern `resources` block and apply the patch in the overlay `kustomization.yaml`:
   ```yaml
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - ../../base
   patches:
     - path: patch.yaml
   ```
3. **Deployment Command:**
   Deploy the merged configuration to the API server:
   ```bash
   kubectl apply -k my-app/overlays/production/
   ```
