---
domains:
  - "kubernetes"
  - "devops"
---

# Module 12-3: Helm Package Management & Lifecycle Operations

This module details the architectural principles, CLI operations, and lifecycle management of applications using Helm. It covers templating concepts, repository commands, installation overrides, version rollback mechanics, and the evolutionary transition from Helm 2 to Helm 3.

---

## 🗺️ Cognitive Map: Helm Release Lifecycle & Reconciliation

```mermaid
graph TD
    subgraph ClientWorkstation["Local Admin Workstation"]
        HelmCLI["Helm CLI (v3)"]
        Kubeconfig["Local Kubeconfig Context (RBAC Credentials)"]
    end

    subgraph KubernetesCluster["Kubernetes Cluster Boundary"]
        APIServer["Kubernetes API Server"]
        
        subgraph TargetNamespace["Target Namespace (e.g., default)"]
            Deploy["Deployment"]
            Svc["Service"]
            Sec["Secret (Target App Credentials)"]
        end
        
        subgraph ReleaseMetadata["Release Metadata Storage"]
            HelmSecret["Secret: sh.helm.release.v1.my-site.v1 <br> (Tracks state snapshot revision 1)"]
        end
    end

    subgraph ChartRegistry["Remote Registry (Artifact Hub / Bitnami)"]
        ChartTarball["Chart Package (wordpress.tgz)"]
    end

    %% Client Actions
    HelmCLI -->|1. Reads Credentials| Kubeconfig
    HelmCLI -->|2. Pulls/Searches Charts| ChartRegistry
    HelmCLI -->|3. Submits Manifests via API| APIServer
    
    %% API Actions
    APIServer -->|4. Installs Objects| TargetNamespace
    APIServer -->|5. Persists Release State| ReleaseMetadata

    %% Comparison logic
    HelmCLI -.->|6. Performs 3-Way Strategic Merge <br> (Compares Proposed Chart, Last Revision Secret, and Live State)| APIServer
```

---

## 1. Core Concepts & Design Paradigm

Kubernetes treats cluster resources (Deployments, Services, ConfigMaps, Secrets) as separate, isolated objects. It has no native understanding that a group of resources belongs to a single application stack. Helm bridges this gap by acting as a **package manager** for Kubernetes:

*   **Chart:** A versioned package containing all resource definitions (templates) necessary to run an application.
*   **Release:** A specific installation of a chart in a Kubernetes cluster. You can run multiple concurrent releases of the same chart (e.g., `prod-web` and `dev-web`) within the same or different namespaces.
*   **Revision:** An incremental version history marker (e.g., `v1`, `v2`, `v3`) created automatically whenever a release is installed, upgraded, or rolled back.
*   **Metadata Storage:** Helm tracks release revisions directly inside the cluster, saving history as gzip-compressed, base64-encoded Kubernetes **Secrets** within the release's namespace (named `sh.helm.release.v1.<release-name>.<revision>`).

---

## 2. Helm 2 vs. Helm 3 Architecture

The release of Helm 3 introduced fundamental design changes to security and state reconciliation:

### A. Removal of Tiller (Client-Only Model)
*   **Helm 2 (Legacy):** Relied on a server-side component inside the cluster called **Tiller**. The local Helm CLI communicated with Tiller, and Tiller acted as the "God-mode" middleman, executing all API calls against the cluster. Because Tiller ran with cluster-admin privileges, it bypassed user-level RBAC restrictions, presenting significant security risks.
*   **Helm 3 (Modern):** Removed Tiller entirely. It is a client-only CLI. It communicates directly with the Kubernetes API Server using the administrator's local `kubeconfig` credentials, fully adhering to standard Kubernetes **Role-Based Access Control (RBAC)** policies.

### B. Three-Way Strategic Merge Patch
*   **Helm 2 (Legacy):** When performing upgrades or rollbacks, Helm 2 only compared the proposed new chart against the old chart (last recorded Helm revision). If an administrator manually edited a live resource in the cluster (e.g., changing replicas or container image via `kubectl edit`), Helm 2 was unaware and failed to correct the drift during subsequent Helm actions.
*   **Helm 3 (Modern):** Implements a **three-way strategic merge patch**. It compares:
    1.  The proposed new state (the new chart).
    2.  The last recorded state (the previous Helm revision).
    3.  The **live state** of the running cluster resources.
    This ensures that manual drift inside the cluster is overridden/reverted to the correct chart values during rollbacks, or preserved cleanly during upgrades.

---

## 3. Helm Chart Structure & Metadata

A Helm chart is structured as a directory containing specific files:

```
my-chart/
├── Chart.yaml          # Metadata about the chart
├── values.yaml         # Default configuration values for templates
├── README.md           # Documentation for users
├── LICENSE             # Optional license file
├── templates/          # Directory containing manifest templates
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── _helpers.tpl    # Helper templates / partials
│   └── NOTES.txt       # Printed instructions shown post-installation
└── charts/             # Optional directory for sub-charts (dependencies)
```

### A. The Chart.yaml File Properties
The `Chart.yaml` contains critical package metadata:
*   `apiVersion`: Specifies the schema version. Use **`v2`** for Helm 3 charts (enables native dependencies, type fields). Legacy Helm 2 charts use `v1`.
*   `name`: The name of the chart (e.g. `wordpress`).
*   `version`: The version of the **chart package** itself (using SemVer, e.g., `1.2.3`). Tracks changes to templates and configurations.
*   `appVersion`: The version of the **underlying application software** being packaged (e.g., WordPress `5.8.1`). This is purely informational.
*   `type`: The chart type. Can be `application` (default deployable service) or `library` (reusable helpers that do not deploy manifests themselves).
*   `dependencies`: Lists dependent sub-charts (e.g., database layers like MariaDB) to prevent duplication:
    ```yaml
    dependencies:
      - name: mariadb
        version: "9.x.x"
        repository: "https://charts.bitnami.com/bitnami"
    ```

---

## 4. Helm CLI Command Reference

### A. Repository Management
```bash
# Add a remote repository
helm repo add bitnami https://charts.bitnami.com/bitnami

# List configured repositories
helm repo list

# Update local index cache with remote repositories (similar to 'apt-get update')
helm repo update

# Remove a configured repository
helm repo remove bitnami
```

### B. Searching for Charts
```bash
# Search public Artifact Hub registries (requires internet)
helm search hub wordpress

# Search configured local repositories
helm search repo wordpress
```

### C. Installing and Overriding Parameters
You can install a package using remote references or pointing to local directories. Overriding default values declared in `values.yaml` is achieved via three options:

#### Option 1: Command Line Overrides (`--set`)
Ideal for quick, single-parameter overrides:
```bash
helm install my-site bitnami/wordpress \
  --set wordpressBlogName="Dev Blog" \
  --set wordpressEmail="admin@example.com"
```

#### Option 2: Custom Values YAML File (`-f` or `--values`)
Best for maintaining environment-specific configurations (e.g., `dev-values.yaml` vs. `prod-values.yaml`) in git:
```yaml
# custom-values.yaml
wordpressBlogName: "Production Blog"
replicaCount: 3
```
```bash
helm install my-site bitnami/wordpress -f custom-values.yaml
```

#### Option 3: Local Pull and Directory Modification
Best for complete chart editing. Downloads the chart, untars it, allowing direct template edits:
```bash
# Pull and untar to local directory
helm pull bitnami/wordpress --untar

# Install pointing to the local directory
helm install my-site ./wordpress
```

### D. Release Lifecycle Management
```bash
# List all active releases in the current namespace
helm list

# List releases in all namespaces
helm list -A

# Check installation history and revision statuses
helm history my-site

# Upgrade an active release (triggers revision increment)
helm upgrade my-site bitnami/wordpress --set replicaCount=5

# Rollback a release to a specific historical revision
helm rollback my-site 1

# Uninstall a release and delete all associated cluster objects
helm uninstall my-site
```

---

## 5. Lifecycle Caveats & Troubleshooting

### A. Database Rollback Limitations
When executing `helm rollback`, Helm reverts the **declarative Kubernetes manifests** (e.g. updating container images, ConfigMaps, replicas, and env variables) to their previous state.
> [!WARNING]
> **Data Loss Risk:** Helm does **NOT** roll back persistent database transactions, volume directory contents, or external database schemas. For database schemas and user data, you must configure independent database backup/restore procedures or utilize **Chart Hooks** to coordinate database migrations and backups prior to Helm upgrades.

### B. Upgrading Release Credentials
During Helm upgrades, certain stateful charts (e.g., Bitnami WordPress/MySQL) require administrative passwords to be passed in to complete structural changes. Check the post-install `NOTES.txt` instructions or CLI warnings if an upgrade fails due to password mismatches.
