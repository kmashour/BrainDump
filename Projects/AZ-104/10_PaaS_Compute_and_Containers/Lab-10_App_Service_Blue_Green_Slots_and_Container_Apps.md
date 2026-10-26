---
obsidianUIMode: preview
class: project-note
tier: project
domains:
  - azure
concepts_referenced:
  - "[[13-104-10_administer_paas_compute_options]]"
  - "[[13-3_azure_compute_services_and_workload_paradigms]]"
  - "[[13-104-02_administer_identity]]"
  - "[[13-104-03_manage_governance_and_compliance]]"
  - "[[13-104-05_configure_and_manage_virtual_networking]]"
  - "[[13-104-08_administer_azure_storage]]"
difficulty: advanced
status: completed
---

# Lab 10: App Service Blue/Green Deployment Slots, Sticky Settings & Azure Container Apps

**Breadcrumbs:** [[--Index--|🏠 Index]] > [[13-Index - AZ-104|📘 AZ-104 Track]] > Projects > **Lab 10: PaaS Compute & Containers**

---

## 🎯 Lab Overview & Enterprise Scenario

Modern enterprise DevOps mandates continuous, zero-downtime application deployments, environment-isolated configurations, and elastic serverless container runtimes. In this hands-on project, you will engineer enterprise PaaS compute using **Azure App Service** and **Azure Container Apps (ACA)**.

### Target Deliverables:
1. **Dedicated App Service Plan Provisioning:** Deploy a production App Service Plan (`PremiumV3` / `P1v3`) capable of hosting deployment slots, custom domains, and automated scaling.
2. **Zero-Downtime Blue/Green Deployment Slots:** Provision a production web app alongside an isolated `staging` slot to eliminate cold-start latency and customer-facing downtime during updates.
3. **Sticky Configuration Architecture:** Configure slot-specific application settings (**Deployment slot setting = true**), ensuring database strings and environment flags stay anchored to their target environment during swaps.
4. **Canary Traffic Splitting & Swap Validation:** Route a canary percentage (10%) of live production traffic to the staging slot to observe telemetry before triggering a full atomic swap.
5. **Azure Container Apps (ACA) Serverless Microservice:** Deploy a containerized microservice into an ACA environment, configuring ingress controls and zero-to-many event-driven auto-scaling powered by KEDA (Kubernetes Event-driven Autoscaling).
6. **Cross-Module Enterprise Integrations:** Integrate Regional VNet Integration (Mod 05), access Azure Storage (Mod 08) via System-Assigned Managed Identity (Mod 02), and guard against accidental deletion via Resource Locks (Mod 03).

---

## 🏛️ Target Architecture & Visual Workflow

```mermaid
flowchart TD
    subgraph ExternalClients ["External Users & Testers"]
        ProdUsers["Live Production Users (90% Traffic)"]
        CanaryUsers["Canary Testers (10% Traffic)"]
    end

    subgraph AppServicePlan ["App Service Plan: asp-enterprise-prod (P1v3)"]
        subgraph ProductionWebApp ["Azure Web App: app-enterprise-prod-XXXX"]
            subgraph ProductionSlot ["Production Slot (Live / Blue)"]
                LiveCode["App Code: v1.0.0 (Live)"]
                LiveConfig["Sticky Setting: APP_ENV=Production<br/>Sticky Setting: DB_HOST=sql-prod.corp"]
            end

            subgraph StagingSlot ["Staging Slot (Preview / Green)"]
                StageCode["App Code: v2.0.0 (Candidate)"]
                StageConfig["Sticky Setting: APP_ENV=Staging<br/>Sticky Setting: DB_HOST=sql-stage.corp"]
            end
        end
    end

    subgraph ContainerAppsEnv ["Azure Container Apps Environment: managedEnv-prod"]
        subgraph Microservice ["Container App: ca-order-processor"]
            KEDA["KEDA Autoscaler<br/>- Min Replicas: 0 (Scale to zero)<br/>- Max Replicas: 5<br/>- Rule: 50 concurrent HTTP requests"]
            Pods["Container Replicas (Active Workload)"]
        end
    end

    subgraph Integrations ["Cross-Module Integrations"]
        VNet["VNet Regional Integration (Mod 05)<br/>Outbound traffic routed via private VNet"]
        Identity["System-Assigned Managed Identity (Mod 02)<br/>Storage Blob Data Contributor"]
        Storage["Storage Account stlabXXXX (Mod 08)"]
        Lock["Resource Lock: CanNotDelete (Mod 03)"]
    end

    ProdUsers -->|Traffic Distribution: 90%| ProductionSlot
    CanaryUsers -->|Traffic Distribution: 10%| StagingSlot

    ProductionSlot <-->|Atomic Blue/Green Swap (Zero 502/504s)| StagingSlot

    ProductionWebApp -->|Outbound VNet Integration| VNet
    ProductionWebApp -->|Managed Identity Auth| Storage
    Lock -.->|Protects from Teardown| ProductionWebApp

    Microservice --- KEDA
```

---

## ⚡ Phase 1: Fast Environment Bootstrap (Optional Azure CLI Script)

If you prefer to pre-stage the Resource Group, App Service Plan, and base Web App via automation before configuring deployment slots, sticky settings, canary routing, and Container Apps in the GUI, run this snippet in Azure Cloud Shell:

```bash
#!/usr/bin/env bash
set -euo pipefail

export RG="rg-paas-lab"
export LOCATION="eastus"
export RANDOM_HEX=$(openssl rand -hex 3)
export APP_NAME="app-prod-${RANDOM_HEX}"
export PLAN_NAME="asp-enterprise-prod"

echo "==> Creating Resource Group: ${RG}..."
az group create --name "${RG}" --location "${LOCATION}" --tags Environment=Production Department=Engineering

echo "==> Deploying PremiumV3 App Service Plan (Required for Slots)..."
az appservice plan create \
  --resource-group "${RG}" \
  --name "${PLAN_NAME}" \
  --location "${LOCATION}" \
  --sku "P1v3" \
  --is-linux

echo "==> Deploying Base Web App: ${APP_NAME}..."
az webapp create \
  --resource-group "${RG}" \
  --plan "${PLAN_NAME}" \
  --name "${APP_NAME}" \
  --runtime "DOTNETCORE:8.0"

echo "==> Bootstrap Complete! Web App Name: ${APP_NAME}"
echo "==> Open Azure Portal to begin GUI configuration."
```

---

## 🖥️ Phase 2: Core Hands-On Implementation (Azure Portal GUI - Step-by-Step)

### Task 2.1: Provision Production App Service Plan and Web App via Portal GUI

*If you executed Phase 1, navigate directly to your Web App in the portal and proceed to Task 2.2. Otherwise, follow the steps below to deploy from scratch in the GUI.*

1. In the top search bar, type `App Services` and select it.
2. Click **+ Create** in the command bar ➔ Select **Web App**.
3. On the **Basics** tab, configure:
   * **Subscription:** Select your target active subscription.
   * **Resource Group:** Click **Create new** ➔ Enter `rg-paas-lab` ➔ Click **OK**.
   * **Name:** Enter `app-prod-` followed by your initials and 4 numbers (e.g., `app-prod-kd8921`). *Must be globally unique*.
   * **Publish:** Select **Code**.
   * **Runtime stack:** Select **.NET 8 (LTS)** (or **Node 20 LTS**).
   * **Operating System:** Select **Linux**.
   * **Region:** Select `(US) East US`.
   * **Pricing plan:**
     * Click **Create new** ➔ Enter name `asp-enterprise-prod` ➔ Click **OK**.
     * **Pricing plan (SKU):** Click **Change size**. In the Spec Picker blade, select **Production** tab ➔ Choose **P1v3 (2 vCPU, 8 GB RAM)** ➔ Click **Select**.
     * *Crucial Architectural Note:* Free (F1), Shared (D1), and Basic (B1) tiers **DO NOT** support Deployment Slots. A minimum of Standard (S1) or Premium (P1v3) is mandatory for deployment slot architectures.
4. Click **Next: Database >** ➔ None.
5. Click **Next: Deployment >** ➔ Continuous deployment: Disabled.
6. Click **Next: Networking >** ➔ Enable public access: On.
7. Click **Next: Monitoring >** ➔ Application Insights: Optional.
8. Click **Review + create** ➔ Review validation pass ➔ Click **Create**.
9. Once deployment completes, click **Go to resource**.

> [!NOTE]
> **Visual Checkpoint:** On the Web App **Overview** blade, look at the **App Service plan / pricing tier** field. Verify it displays `asp-enterprise-prod (P1v3)`. Click the **Default domain** URL (e.g., `https://app-prod-XXXX.azurewebsites.net`) and verify Microsoft's default hosting landing page loads successfully.

---

### Task 2.2: Configure Application Settings & Enforce Sticky Slot Flags

In an enterprise deployment, configuration values like database endpoints or external API URLs must be tightly coupled to their target environment. If a setting is **not sticky**, it will swap across slots during a swap, causing production to accidentally connect to test systems!

1. In the left navigation menu under **Settings**, click **Environment variables** (or **Configuration** on older portal layouts).
2. Under the **App settings** tab, click **+ Add**:
   * **Name:** `APP_ENVIRONMENT`.
   * **Value:** `Production`.
   * **Deployment slot setting:** **CHECK THIS BOX** *(This is the critical "Sticky" flag)*.
   * Click **Apply**.
3. Click **+ Add** a second time:
   * **Name:** `DATABASE_HOST`.
   * **Value:** `sql-prod.internal.corp`.
   * **Deployment slot setting:** **CHECK THIS BOX**.
   * Click **Apply**.
4. Click **+ Add** a third time for a non-sticky feature flag:
   * **Name:** `FEATURE_NEW_CHECKOUT`.
   * **Value:** `false`.
   * **Deployment slot setting:** **LEAVE UNCHECKED** *(This flag is non-sticky; it travels with application code during swaps)*.
   * Click **Apply**.
5. Click **Apply** (or **Save**) at the bottom of the Environment variables blade. Confirm the restart prompt.

> [!NOTE]
> **Visual Checkpoint:** In the App settings table, verify that both `APP_ENVIRONMENT` and `DATABASE_HOST` have a checkmark under the **Deployment slot setting** column, while `FEATURE_NEW_CHECKOUT` displays an unchecked status.

---

### Task 2.3: Provision Staging Deployment Slot & Configure Staging Variables

1. In the left navigation menu under the **Deployment** section, click **Deployment slots**.
2. Notice the existing `production` slot (100% traffic, Status: Running).
3. In the top command bar, click **+ Add Slot**.
4. In the **Add slot** slide-over panel:
   * **Name:** Enter `staging`.
   * **Clone settings from:** Select your production app `app-prod-XXXX`.
   * Click **Add**. Wait ~30 seconds for the slot provisioning to complete.
5. In the Deployment slots table, click directly on the newly created **staging** slot.
   * Notice the breadcrumb at the top indicates you are now managing:
     `app-prod-XXXX > app-prod-XXXX-staging`.
   * Notice its URL is: `https://app-prod-XXXX-staging.azurewebsites.net`.
6. In the left navigation menu under **Settings**, click **Environment variables**.
7. Observe that the cloned sticky settings are present. Update them to point to staging infrastructure:
   * Click on `APP_ENVIRONMENT`: Change **Value** to `Staging`. Ensure **Deployment slot setting** remains checked. Click **Apply**.
   * Click on `DATABASE_HOST`: Change **Value** to `sql-staging.internal.corp`. Ensure **Deployment slot setting** remains checked. Click **Apply**.
   * Click on `FEATURE_NEW_CHECKOUT`: Change **Value** to `true` (Candidate feature under test). Leave **Deployment slot setting** unchecked. Click **Apply**.
8. Click **Apply** / **Save** at the bottom of the blade and confirm.

---

### Task 2.4: Test Live Canary Traffic Splitting in Portal GUI

Canary testing lets you route a small percentage of live customer traffic to the staging slot to validate stability before executing a full deployment cutover.

1. Navigate back to the parent Web App `app-prod-XXXX` (using the top breadcrumb or search bar).
2. In the left navigation menu under **Deployment**, click **Deployment slots**.
3. In the slots table, look at the **Traffic %** column:
   * By default, `production` is `100%` and `staging` is `0%`.
4. Click into the **Traffic %** box for `staging` and enter: **`10`**.
5. Notice that `production` automatically calculates down to: **`90`**.
6. Click **Save** in the top command bar.
7. Azure's front-end routing proxy now injects an HTTP cookie (`x-ms-routing-name=staging`) for 10% of incoming requests, directing those clients to the staging slot while keeping 90% on production.

> [!NOTE]
> **Visual Checkpoint:** The Deployment slots overview shows `production` at **90%** and `staging` at **10%**.

---

### Task 2.5: Execute Zero-Downtime Blue/Green Swap with Configuration Diff Review

1. On the parent Web App **Deployment slots** blade, click **Swap** in the top command bar.
2. In the **Swap** modal dialog, review the settings:
   * **Swap type:** Select `Swap`.
   * **Source:** Select `staging`.
   * **Target:** Select `production`.
3. Under the **Changes** preview table, inspect the configuration comparison:
   * **Target setting changes:** Notice that `FEATURE_NEW_CHECKOUT` changes from `false` ➔ `true` (because it was non-sticky and travels with the code release).
   * **Sticky settings preservation:** Notice that `APP_ENVIRONMENT` (`Production`) and `DATABASE_HOST` (`sql-prod.internal.corp`) **DO NOT CHANGE**! They remain firmly anchored to the production slot.
4. Click **Swap**.
   * Azure warms up the candidate worker processes in the staging slot. Once the warmup ping succeeds, Azure's internal routing tables atomically flip the VIP pointers.
   * The transition completes with **zero HTTP 502/504 errors** and zero cold-start delay for end users.
5. Once complete, click **Close**.
6. In the slots table, reset the **Traffic %** of `staging` back to `0%` and `production` to `100%`. Click **Save**.

---

### Task 2.6: Deploy Azure Container Apps (ACA) Serverless Microservice

Azure Container Apps provides serverless container execution built on Kubernetes and KEDA without the overhead of managing AKS clusters.

1. In the top search bar, type `Container Apps` and select it under **Services**.
2. Click **+ Create** ➔ Select **Container App**.
3. On the **Basics** tab, configure:
   * **Subscription:** Your subscription.
   * **Resource group:** Select `rg-paas-lab`.
   * **Container App name:** Enter `ca-order-processor`.
   * **Region:** Select `(US) East US`.
   * **Container Apps Environment:** Click **Create new**:
     * **Environment name:** Enter `managedEnv-prod`.
     * **Workload profiles:** Select `Consumption` (Serverless, pay-per-second).
     * Click **Create**.
4. Click **Next: Container >**:
   * Check **Use quickstart image** (Uses Microsoft's sample web container `mcr.microsoft.com/k8se/quickstart:latest`).
5. Click **Next: Ingress >**:
   * **Ingress:** Check **Enabled**.
   * **Ingress traffic:** Select **Accepting traffic from anywhere**.
   * **Target port:** Enter `80`.
6. Click **Next: Scale >**:
   * **Minimum replicas:** Enter `0` *(Critical serverless finops feature: Scales completely to zero instances when idle)*.
   * **Maximum replicas:** Enter `5`.
   * Under **Scale rules**, click **+ Add**:
     * **Rule name:** `http-traffic-rule`.
     * **Type:** Select `HTTP scaling`.
     * **Concurrent requests:** Enter `50`.
     * Click **Add**.
7. Click **Review + create** ➔ Review validation pass ➔ Click **Create**.
8. Once deployment completes, click **Go to resource**.
9. On the Container App overview, copy the **Application Url** and paste it into a new browser tab.
   * Microsoft's container greeting page renders immediately. When traffic stops, KEDA will scale the instance count down to zero replicas!

> [!NOTE]
> **Visual Checkpoint:** In the Container App left menu under **Application**, click **Replicas**. When no traffic is hitting the endpoint, the replica count drops to **0**, verifying scale-to-zero serverless operation.

---

## 🔗 Phase 3: Cross-Module Integration Task

### Integrating Module 05 (VNet Integration), Module 02 (Managed Identity) & Module 08 (Storage Data Plane)

In enterprise architectures, PaaS Web Apps must not reach backend storage across the public internet with hardcoded access keys. We bind the Web App to our Virtual Network and authenticate using Entra ID Managed Identities.

```
+-----------------------------------------------------------------------------------------+
|                               Cross-Module Architecture                                 |
|                                                                                         |
|   +--------------------------+     +------------------------+    +------------------+   |
|   | Module 05: VNet Integr.  |     | Module 02: Entra ID    |    | Module 08: Azure |   |
|   | Regional VNet Integration|     | System-Assigned        |    | Storage Account  |   |
|   | Routes egress to private |====>| Managed Identity on    |===>| Data Plane Role: |   |
|   | vnet-compute-prod        |     | app-prod-XXXX          |    | Storage Blob Data|   |
|   |                          |     |                        |    | Contributor      |   |
|   +--------------------------+     +------------------------+    +------------------+   |
|               ^                                                           ^             |
|               |                                                           |             |
|   +-----------+-----------------------------------------------------------+---------+   |
|   |                     Production Azure Web App (app-prod-XXXX)                    |   |
|   |       - Governed by Module 03 Resource Lock: lock-protect-production-webapp     |   |
|   |       - Egress traffic securely routed through enterprise private subnets       |   |
|   |       - Passwordless authentication to Azure Storage using Entra tokens         |   |
|   +---------------------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------------------+
```

### Step 1: Enable System-Assigned Managed Identity on Web App (Mod 02 Integration)
1. Navigate to your parent Web App `app-prod-XXXX` in the Azure Portal.
2. In the left navigation menu under **Settings**, click **Identity**.
3. Under the **System assigned** tab:
   * Change **Status** from *Off* to **On**.
   * Click **Save** ➔ Click **Yes** to confirm.
   * Azure generates and binds an Enterprise Object ID in Microsoft Entra ID.

### Step 2: Grant Managed Identity Access to Storage Account (Mod 08 Integration)
1. On the same **Identity** screen, click **Azure role assignments**.
2. Click **+ Add role assignment**:
   * **Scope:** Select `Storage`.
   * **Subscription:** Your subscription.
   * **Resource:** Select your storage account from Lab 08 (`stlabXXXX`).
   * **Role:** Select `Storage Blob Data Contributor`.
   * Click **Save**.
   * The web application can now read and write blobs directly via the Azure SDK without holding any connection string or access key in its configuration!

### Step 3: Apply `CanNotDelete` Resource Lock (Mod 03 Integration)
1. In the left navigation menu under **Settings**, click **Locks**.
2. Click **+ Add**:
   * **Lock name:** `lock-protect-production-webapp`.
   * **Lock type:** Select `Delete`.
   * **Notes:** `Live customer-facing PaaS compute - deletion prohibited.`
3. Click **OK**.
4. Test the lock: Navigate to the **Overview** blade and click **Delete**. Notice the portal blocks the operation immediately.

---

## 🔬 Phase 4: Verification & Validation Testing (Azure CLI / Cloud Shell)

Open Azure Cloud Shell (Bash) and execute these automated verification queries to validate your deployment against AZ-104 production standards:

```bash
#!/usr/bin/env bash
set -euo pipefail

export RG="rg-paas-lab"
export APP_NAME=$(az webapp list --resource-group "${RG}" --query "[0].name" -o tsv)

echo "=========================================================="
echo "==> Auditing PaaS Infrastructure: ${APP_NAME}"
echo "=========================================================="

# Test 1: Verify Sticky Settings on Production Slot
echo -e "\n[Test 1] Auditing Sticky Configuration Flags on Production Slot..."
az webapp config appsettings list \
  --resource-group "${RG}" \
  --name "${APP_NAME}" \
  --query "[?name=='APP_ENVIRONMENT' || name=='DATABASE_HOST' || name=='FEATURE_NEW_CHECKOUT'].{Setting:name, Value:value, IsSticky:slotSetting}" \
  --output table

# Test 2: Verify Sticky Settings on Staging Slot
echo -e "\n[Test 2] Auditing Sticky Configuration Flags on Staging Slot..."
az webapp config appsettings list \
  --resource-group "${RG}" \
  --name "${APP_NAME}" \
  --slot "staging" \
  --query "[?name=='APP_ENVIRONMENT' || name=='DATABASE_HOST' || name=='FEATURE_NEW_CHECKOUT'].{Setting:name, Value:value, IsSticky:slotSetting}" \
  --output table

# Test 3: Verify Deployment Slot Routing Configuration
echo -e "\n[Test 3] Auditing Live Traffic Routing Percentage..."
az webapp traffic-routing show \
  --resource-group "${RG}" \
  --name "${APP_NAME}" \
  --output table

# Test 4: Verify System-Assigned Managed Identity Binding
echo -e "\n[Test 4] Inspecting Managed Identity Principal ID..."
az webapp identity show \
  --resource-group "${RG}" \
  --name "${APP_NAME}" \
  --query "{Type:type, PrincipalId:principalId}" \
  --output table

# Test 5: Verify Container App KEDA Scaling Configuration
echo -e "\n[Test 5] Auditing Container App Ingress and Scale-to-Zero Configuration..."
az containerapp show \
  --resource-group "${RG}" \
  --name "ca-order-processor" \
  --query "{Name:name, FQDN:properties.configuration.ingress.fqdn, MinReplicas:properties.template.scale.minReplicas, MaxReplicas:properties.template.scale.maxReplicas}" \
  --output table

echo -e "\n=========================================================="
echo "==> ALL AUDIT CHECKS PASSED: PaaS topology meets AZ-104 Enterprise Standards!"
echo "=========================================================="
```

---

## ⚠️ Phase 5: "See It in Action" Real-World Failure & Recovery Loop (AARF)

### Scenario A: The Accidental Staging Database Swap Disaster
* **The Architecture:** An engineering team deploys a new release candidate to the `staging` slot.
* **The Assumption:** Developers assume clicking **Swap** only moves application code and that database connection strings will automatically stay in their respective environments.
* **The Failure Loop:**
  * The engineer forgets to check **Deployment slot setting** for `DATABASE_HOST` on both slots.
  * The engineer clicks **Swap**.
  * The code swaps into production, but because the database connection string was treated as portable payload, production begins executing SQL write queries against the **Staging Database**! Live customer transactions write to sandbox tables, and test scripts wipe live tables.
* **The Root Cause:**
  In Azure App Service, unless an application setting has its `slotSetting` property explicitly set to `true`, Azure treats the configuration as mobile payload that travels with the code swap.
* **The Remediation in GUI:**
  1. In the Azure Portal, open the Web App ➔ **Settings** ➔ **Environment variables**.
  2. Click on every environment-specific variable (e.g., `DATABASE_HOST`, `REDIS_CONNECTION`).
  3. Ensure the checkbox **Deployment slot setting** is checked.
  4. Perform the same verification on the `staging` slot.
  5. Repeat the swap: The configuration comparison matrix will now explicitly show that sticky settings do not change.

---

### Scenario B: The Basic SKU Slot Limitation Trap
* **The Failure Scenario:** A cost-conscious team creates an App Service on the **Basic (B1)** pricing tier.
* **The Error in Portal:**
  When navigating to **Deployment slots**, the option to **+ Add Slot** is disabled with an informational message:
  `Deployment slots are not supported on your current pricing tier. Upgrade your App Service plan to Standard or Premium to use deployment slots.`
* **The Remediation in GUI:**
  1. In the left navigation menu under **Settings**, click **Scale up (App Service plan)**.
  2. Select the **Production** tab.
  3. Select **Standard S1** or **Premium V3 P1v3**.
  4. Click **Apply**.
  5. The **Deployment slots** blade immediately unlocks and allows creating slots.

---

## 🧹 Phase 6: Cost Optimization & Lab Teardown

App Service Premium plans incur hourly billing. Follow these steps to tear down the lab resources:

1. **Remove Resource Locks First (Mandatory):**
   * Navigate to `app-prod-XXXX` ➔ **Settings** ➔ **Locks**.
   * Delete `lock-protect-production-webapp`.
2. **Delete the Resource Group:**
   * Open Cloud Shell or execute in local terminal:
     ```bash
     az group delete --name "rg-paas-lab" --yes --no-wait
     ```
3. **Verify Deletion in Portal:**
   * In the Portal search bar, type `Resource groups` ➔ Verify `rg-paas-lab` is marked for deletion.

---

## 🔬 Exam-Specific Gotchas & Speed Shortcuts (AZ-104 Reference)

* **App Service Plan Tiers & Features Matrix:**
  * **Free (F1) / Shared (D1):** 60 min/day compute, shared infrastructure, no custom domains, no SSL, no slots.
  * **Basic (B1–B3):** Dedicated compute, custom domains, manual scale up to 3 instances, **NO deployment slots**, no autoscaling.
  * **Standard (S1–S3):** Dedicated compute, autoscale up to 10 instances, **5 deployment slots**, automated backups.
  * **Premium (P1v3–P3v3):** High performance, autoscale up to 30 instances, **20 deployment slots**, VNet integration.
  * **Isolated (I1v2–I3v2):** Dedicated ASE (App Service Environment) running inside customer private VNet, up to 100 instances.
* **Sticky vs Non-Sticky Settings during Slot Swap:**
  * **Sticky (Stay with slot):** Connection strings, app settings marked as "Deployment slot setting", custom domain names, SSL certificates, IP restrictions.
  * **Non-Sticky (Swap with code):** General settings (framework version, 32/64 bit, web sockets), App settings without the slot setting checkbox, continuous deployment settings.
* **Canary Routing Mechanism:**
  * Configured via **Traffic %** in Deployment slots blade.
  * Azure uses the cookie `x-ms-routing-name` to pin clients to a specific slot for the session duration.
* **Azure Container Apps vs Azure Container Instances (ACI) vs AKS:**
  * **ACI:** Single container instance, no native HTTP load balancing, no scaling rules, best for quick batch jobs.
  * **ACA:** Serverless microservices, built on AKS/Envoy/KEDA, supports scale-to-zero, HTTP ingress, revisions, traffic splitting.
  * **AKS:** Full enterprise Kubernetes control plane, full API access, custom CNI, cluster lifecycle management.
