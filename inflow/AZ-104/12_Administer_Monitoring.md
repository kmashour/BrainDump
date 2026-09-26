# AZ-104 Section 12: Administer Monitoring

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 6

---


## Lesson 1: Module Introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Module-Introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Module-Introduction/page.md)

**Summary:** This article covers objectives to enhance observability and operational excellence of Azure services through monitoring, alerting, and log analytics.

# Module Introduction

> This article covers objectives to enhance observability and operational excellence of Azure services through monitoring, alerting, and log analytics.

In this article, we cover three essential objectives designed to enhance the observability and operational excellence of Azure services. By following these steps, you'll be able to monitor, analyze, and react to telemetry data from both Azure and on-premises environments.

## Configuring Azure Monitor

Azure Monitor collects, analyzes, and acts on telemetry data from your applications, infrastructure, and networks. This service is vital for gaining insights into performance and overall system health. With Azure Monitor, you can proactively identify potential issues and ensure your services run smoothly.

## Setting Up Azure Alerts

The next step involves configuring Azure Alerts. Here, you will learn how to create alerts based on the metrics and log data collected by Azure Monitor. These alerts notify you of critical conditions and can trigger automated actions when specific thresholds are met, ensuring a proactive approach to maintenance and problem resolution.

## Establishing Log Analytics

The third objective focuses on Azure Log Analytics. By setting up and managing Log Analytics workspaces, you can query and analyze the log data gathered by Azure Monitor. This powerful tool allows you to create complex queries, visualize data, and extract actionable insights for effective decision-making and troubleshooting.

<Frame>
  ![The image lists learning objectives related to configuring Azure Monitor, Azure Alerts, and Log Analytics, with a gradient blue background on the left.](https://kodekloud.com/kk-media/image/upload/v1752884687/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Module-Introduction/azure-monitor-alerts-log-analytics.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  For comprehensive guidance on Azure Monitor and Alerts, refer to the [Azure Documentation](https://docs.microsoft.com/en-us/azure/monitoring/) and ensure you follow best practices for accurate data collection and effective alert configurations.
</Callout>

Let’s begin by exploring Azure Monitor in greater detail.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/e208e27a-6519-4eb4-aaf1-342bb14def21/lesson/367ced34-2c5e-475c-8ac5-ef2d4ea424cf" />
</CardGroup>

---


## Lesson 2: Azure Monitor

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Azure-Monitor/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Azure-Monitor/page.md)

**Summary:** Azure Monitor is a solution for full-stack monitoring, analytics, and automation across applications and infrastructure in Microsoft Azure.

# Azure Monitor

> Azure Monitor is a solution for full-stack monitoring, analytics, and automation across applications and infrastructure in Microsoft Azure.

Azure Monitor is a comprehensive solution within Microsoft Azure designed to deliver full-stack monitoring, advanced analytics, and intelligent automation across applications and infrastructure. By collecting, analyzing, and acting on telemetry data from Azure, on-premises, and non-Azure cloud environments, Azure Monitor enables you to understand your applications' performance and proactively identify and resolve issues.

## Azure Monitor Architecture

Azure Monitor’s architecture is designed to efficiently collect and process vast amounts of telemetry data through a series of structured stages. The process begins at the data sources and continues through data collection, processing in the data platform, and finally, data consumption where insights, visualization, analysis, and response come into play.

### Data Sources

Monitoring starts at the data source level, where Azure Monitor collects data from multiple origins:

* **Applications and Workloads:** Telemetry from applications running in Azure, other clouds, or on-premises.
* **Infrastructure Components:** Metrics and logs from virtual machines, networks, and other infrastructure components.
* **Azure Platform:** Built-in telemetry from Azure services.
* **Custom Sources:** User-configured sources that capture specialized data.

All these data streams are funneled into Azure Monitor, where agents, data collection rules, and diagnostic settings help in collecting, routing, and transforming the incoming data.

### Data Platform

At the core of Azure Monitor lies the Data Platform, serving as the centralized repository for all telemetry data. The platform categorizes data into several types:

* **Metrics:** Numerical values representing system states at specific time intervals.
* **Logs:** Timestamped records that detail operations and state changes.
* **Traces:** In-depth insights into application code execution.
* **Change Data:** Records that trace modifications in Azure resource configurations.

### Data Consumption

Once processed, the telemetry data is made available for various consumption methods to generate actionable insights and responses:

* **Insights:** Detailed performance and health metrics for applications, containers, virtual machines, and network resources.
* **Visualization:** Interactive representations using workbooks, dashboards, Power BI, and Grafana.
* **Analysis:** Advanced examination with tools like Metrics Explorer and Log Analytics.
* **Response:** Automated alerts, autoscaling actions, and AI-driven operational responses through features like AIOps.

Organizations also benefit from integration with System Center Operations Manager (SCOM), allowing unified monitoring of SCOM-managed instances, including databases. Further integrations with Event Hubs, Azure Storage, managed partners, APIs, Logic Apps, Functions, Azure DevOps, and GitHub help in creating a robust monitoring environment.

<Frame>
  ![The image is a diagram of Azure Monitor, illustrating its data sources, data collection, routing, transformation, data platform, and consumption processes. It shows how data from various sources is processed and utilized for insights, visualization, analysis, and response.](https://kodekloud.com/kk-media/image/upload/v1752884678/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Monitor/azure-monitor-data-flow-diagram.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  In this article, the focus will be on two crucial components of Azure Monitor for exam preparation: metrics and logs.
</Callout>

## Metrics

Metrics within Azure Monitor are numerical data points collected at regular intervals that provide a near real-time snapshot of resource performance and health. Examples of common metrics include CPU usage and network traffic, which help in monitoring the operational efficiency of virtual machines and other resources without the need for complex configuration.

Metrics are typically rendered as time series, offering frequent updates that present an accurate view of system performance.

<Frame>
  ![The image shows two graphs displaying CPU usage and network activity over time, with a noticeable spike in both metrics. The CPU usage averages 2.7275%, and the network shows 13.86 MiB in and 15.75 MiB out.](https://kodekloud.com/kk-media/image/upload/v1752884679/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Monitor/cpu-usage-network-activity-graphs.jpg)
</Frame>

## Logs

Logs in Azure Monitor are a vital resource for diagnosing issues, understanding system behavior, and performing comprehensive analyses. Unlike metrics, logs capture a range of data types and provide descriptive context.

Each log entry consists of fields such as the timestamp, resource identifiers, and event details, allowing for efficient search and filtering. A powerful tool for exploring logs is the Kusto Query Language (KQL). For instance, the following KQL snippet filters log data for specific events:

```plaintext theme={null}
VMProcess
| where Computer contains "SQL" and ExecutableName == "svchost"
| extend TimeInEST = TimeGenerated - 5h
| project TimeInEST, Computer, ExecutableName, Group, FileVersion
```

KQL supports complex queries including joins, aggregations, and advanced analytics, making it indispensable for retrieving and scrutinizing large volumes of telemetry data. While default logging is provided for many services, detailed logs may require additional configuration such as enabling diagnostic settings, deploying specialized agents on virtual machines, or setting up custom data collection protocols.

## Data Sources Relevant for the Exam

Azure Monitor ingests data from several critical sources, each contributing unique insights:

| Data Source      | Description                                                                                                                | Key Components/Mechanisms                                   |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Application      | Telemetry from applications via instrumentation packages such as Application Insights and availability tests               | Application performance, response times, exceptions         |
| Operating System | Performance metrics and operational events collected from virtual machines using agents                                    | Azure Monitor Agent, Diagnostics Extensions                 |
| Subscription     | Activity logs that document subscription-level events including resource creation, updates, and deletions                  | Activity Log monitoring of resource changes                 |
| Azure Tenant     | Logs from services such as Microsoft Entra ID (formerly Active Directory) that monitor user activities and security events | User authentication events, security alerts, policy changes |
| Custom Sources   | Monitors additional customer-defined data such as specialized workloads or custom applications                             | Custom configuration using diagnostic settings and agents   |

All collected data is categorized as either metrics or logs, which can be queried and visualized with the robust set of tools provided by Azure.

<Frame>
  ![The image is a diagram showing different data sources for Azure, including Application, OS, Azure Resources, Azure Subscription, Azure Tenant, and Custom, with metrics and logs as outputs.](https://kodekloud.com/kk-media/image/upload/v1752884681/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Monitor/azure-data-sources-diagram.jpg)
</Frame>

## Azure Activity Logs

Azure Activity Logs provide a comprehensive record of subscription-level events, including resource creation, updates, and deletions, as well as insights into service health. These logs are crucial for maintaining an overview of changes and activities within your Azure environment and ensuring that you can effectively troubleshoot and verify operations.

<Callout icon="lightbulb" color="#1CB2FE">
  This article has provided an overview of Azure Monitor’s architecture, highlighting the key components of metrics and logs essential for both operational insights and exam preparation.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/e208e27a-6519-4eb4-aaf1-342bb14def21/lesson/cf6f4b29-a84a-4d53-930f-28ff47f6a8c9" />
</CardGroup>

---


## Lesson 3: Azure Activity Logs

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Azure-Activity-Logs/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Azure-Activity-Logs/page.md)

**Summary:** Azure Activity Logs capture subscription-level events in Azure Resource Manager, providing insights into resource operations and enabling auditing and compliance tracking.

# Azure Activity Logs

> Azure Activity Logs capture subscription-level events in Azure Resource Manager, providing insights into resource operations and enabling auditing and compliance tracking.

Azure Activity Logs provide subscription-level logging for all events occurring at the Azure Resource Manager level. Every operation that modifies resources—such as creating or updating a virtual machine, deleting a database, or changing configurations—is recorded as a POST or PUT request. Note that simple GET operations, like merely viewing resources, are not logged.

These logs offer detailed insights into resource operations by recording essential data such as the initiator, timestamp, status, and other relevant information that is crucial for auditing.

<Callout icon="lightbulb" color="#1CB2FE">
  Azure Activity Logs are enabled by default with no additional setup required. They retain data for up to 90 days within the portal. For organizations needing longer retention periods (e.g., 180 days for compliance), logs can be exported to a storage account or sent to a Log Analytics workspace.
</Callout>

## Querying Activity Logs

You can query Activity Logs directly from the Azure portal. The portal offers several filtering options including:

* Subscription
* Timespan
* Severity
* Resource group
* Resource
* Initiating user
* Keyword search

This intuitive filtering allows you to view recent events without needing deep query language expertise. However, when querying older data stored in a Log Analytics workspace, familiarity with the query language is beneficial.

## Position of Activity Logs in the Azure Resource Stack

Activity Logs sit above the Azure infrastructure but below the host virtual machine and guest operating system layers. This means that internal events within a guest OS (for example, Windows events) are not captured in the Activity Logs. Instead, these logs record operations that directly interact with Azure’s infrastructure.

## Viewing Metrics and Activity Logs in the Azure Portal

In the Azure portal, you can access both operational metrics and activity logs for your resources. For instance, when you navigate to a virtual machine and select the "Monitoring" section, you can view platform metrics. Clicking on "See all metrics" opens the Metrics Explorer, where you can compare metrics like CPU usage and available memory.

<Frame>
  ![The image shows a Microsoft Azure metrics dashboard for a virtual machine named "win-sql-access," displaying a line chart of average CPU percentage and available memory bytes over time. The chart indicates a drop in available memory at one point, with current values of 3.4556% CPU usage and 5.4 GiB available memory.](https://kodekloud.com/kk-media/image/upload/v1752884654/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Activity-Logs/azure-metrics-dashboard-win-sql-access.jpg)
</Frame>

Access the "Activity Log" blade from any resource to inspect scoped events. When viewed at the subscription level, it provides a comprehensive log of all activities, including details about who initiated each action.

<Frame>
  ![The image shows an activity log from the Microsoft Azure portal, listing various activities such as "Update datascanners" and "Registers EventGrid Resource Provider," all marked as succeeded.](https://kodekloud.com/kk-media/image/upload/v1752884655/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Activity-Logs/azure-activity-log-succeeded.jpg)
</Frame>

Adjust the timeframe (e.g., last 6 hours, 24 hours) and apply filters such as resource group, resource, or specific operations (like create or update VM events). The "Event Severity" filter further refines logs based on their importance, and you can filter by event categories as needed.

## Event Categories

Azure Activity Logs categorize events into several types:

| Category        | Description                                                          |
| --------------- | -------------------------------------------------------------------- |
| Administrative  | Actions performed by users, service principals, or accounts.         |
| Security        | Alerts from Microsoft Defender for Cloud.                            |
| Service Health  | Information on Azure service health.                                 |
| Recommendation  | Suggestions from Microsoft Azure Advisor.                            |
| Policy          | Policy-related actions (e.g., deny, audit, or deploy if not exists). |
| Auto Scale      | Activities related to auto scaling.                                  |
| Resource Health | Events pertaining to the health of specific resources.               |

For example, filtering the logs by administrative events or searching by your email address under "Event initiated by" displays all actions you have taken within a specified timeframe.

<Frame>
  ![The image shows the activity log page of a Microsoft Azure subscription, displaying various operations and filters for event categories.](https://kodekloud.com/kk-media/image/upload/v1752884657/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Activity-Logs/azure-subscription-activity-log.jpg)
</Frame>

If further analysis is required, Activity Logs can be exported as CSV files. To extend retention beyond 90 days, use the "Export Activity Logs" option and configure diagnostic settings to send logs to a Log Analytics workspace or a storage account, based on your compliance requirements.

<Frame>
  ![The image shows a Microsoft Azure portal page for configuring diagnostic settings, where various log categories can be selected and sent to a Log Analytics workspace. Options for archiving to a storage account, streaming to an event hub, and sending to a partner solution are also available.](https://kodekloud.com/kk-media/image/upload/v1752884658/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Activity-Logs/azure-portal-diagnostic-settings.jpg)
</Frame>

## Working with Azure Monitor Alerts

Azure Monitor Alerts complement Activity Logs by enabling proactive surveillance of resource events. The diagram below summarizes the integration of Activity Logs with alerting, auditing, retention, and querying across various resource types (both compute and non-compute):

<Frame>
  ![The image is a diagram of the Azure Activity Log, showing components like subscription-level logging, auditing, retention, and querying data, along with application and resource logs. It categorizes logs into compute and non-compute resources.](https://kodekloud.com/kk-media/image/upload/v1752884659/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Activity-Logs/azure-activity-log-diagram.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  This integrated approach enhances your ability to track and manage resource operations effectively across your entire subscription.
</Callout>

## Summary

This article details how Azure Activity Logs capture interactions with the Azure Resource Manager, outlines methods to view and query these logs using the Azure portal, and explains how to extend log retention to meet organizational compliance needs.

For more detailed information, you may refer to [Microsoft Azure Documentation](https://docs.microsoft.com/en-us/azure/monitoring/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/e208e27a-6519-4eb4-aaf1-342bb14def21/lesson/61013798-23bc-4c30-bae7-a543d603d485" />
</CardGroup>

---


## Lesson 4: Enable Log Analytics Workspace

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Enable-Log-Analytics-Workspace/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Enable-Log-Analytics-Workspace/page.md)

**Summary:** This guide explains how to set up an Azure Log Analytics workspace and highlights its key features and pricing considerations.

# Enable Log Analytics Workspace

> This guide explains how to set up an Azure Log Analytics workspace and highlights its key features and pricing considerations.

Azure Log Analytics is a powerful service that collects, analyzes, and stores data from a variety of sources, whether your resources are hosted in Azure, on-premises, or across different cloud environments. In this guide, you'll learn about the key features of Azure Log Analytics and how to set up a workspace using the Azure Portal.

## Key Features of Azure Log Analytics

Azure Log Analytics comes with several important benefits:

1. Data Collection\
   It centralizes data generated from cloud resources and on-premises systems into a single workspace.

2. Reporting and Visualization\
   Leverage the Kusto Query Language (KQL) to build detailed reports and interactive dashboards for monitoring and analyzing your data.

3. Data Ingestion\
   To ingest data, you first create a Log Analytics workspace. While you can operate multiple workspaces across various regions, many architectures consolidate logs into a centralized workspace. Depending on your project requirements, you might also deploy a dedicated workspace.

4. Data Isolation\
   For compliance and data residency needs, you can create separate workspaces in different regions. For example, production and disaster recovery (DR) environments often require distinct Log Analytics workspaces.

## Pricing Considerations

Log Analytics pricing depends on two main factors:

* Data Ingestion\
  Charges are applied per gigabyte ingested. For instance, the following Kusto query filters performance metrics:

  ```kusto theme={null}
  Perf
  | where Computer contains "SQL" and ObjectName == "LogicalDisk"
  | where CounterName == "% Free Space" and InstanceName == "C:"
  | extend TimeInEST = TimeGenerated - 5h
  | project TimeInEST, CounterName, CounterValue
  ```

* Data Retention\
  Data retention is set to 30 days by default (with activity logs kept for 90 days). If you need to store logs for an extended period—say 180 days—adjust the workspace's retention settings, keeping in mind that this may lead to additional costs.

<Callout icon="lightbulb" color="#1CB2FE">
  If you expect high daily data ingestion volumes (above 100 gigabytes), consider switching from the pay-as-you-go model to the commitment tier to reduce your per-gigabyte costs.
</Callout>

## Creating a Log Analytics Workspace

A Log Analytics workspace is your central hub for collecting, analyzing, and visualizing data from a wide range of resources including Azure, Google Cloud Platform (GCP), AWS, and on-premises systems (using agents or tools like Azure Arc).

Data from Application Insights and Azure Sentinel is also routed to your Log Analytics workspace. Keep in mind that if you are using Sentinel, you will be billed for both Sentinel services and the underlying Log Analytics data storage.

### Step-by-Step Creation Using the Azure Portal

1. Open the Azure Portal and search for "Log Analytics workspaces."
2. Click **Create a new Log Analytics workspace.**
3. Set up a new resource group (for example, "RGMonitoring") and select your desired region (e.g., East US).

<Frame>
  ![The image shows a user interface for creating a Log Analytics workspace in Azure, highlighting features like workspace management, data isolation, and storage of insights and sentinel data. It includes sections for project and instance details.](https://kodekloud.com/kk-media/image/upload/v1752884682/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Enable-Log-Analytics-Workspace/azure-log-analytics-workspace-ui.jpg)
</Frame>

4. Configure the pricing tier. By default, the workspace uses a pay-as-you-go model. For high-volume ingestion environments (over 100 gigabytes per day), opt for the commitment tier to reduce costs.

Once you've created the workspace, you can begin onboarding resources.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a Log Analytics workspace, with fields for project and instance details. Options for subscription, resource group, name, and region are visible, along with navigation buttons for review and creation.](https://kodekloud.com/kk-media/image/upload/v1752884683/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Enable-Log-Analytics-Workspace/azure-log-analytics-workspace-portal.jpg)
</Frame>

After the deployment is complete, you will see a confirmation screen in the Azure Portal.

<Frame>
  ![The image shows a Microsoft Azure portal page indicating that a deployment of "Microsoft.LogAnalyticsOMS" is complete. It includes details like the deployment name, subscription, resource group, and start time, with options to view deployment details and next steps.](https://kodekloud.com/kk-media/image/upload/v1752884685/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Enable-Log-Analytics-Workspace/azure-portal-deployment-complete.jpg)
</Frame>

## Onboarding Resources to Your Workspace

After setting up your Log Analytics workspace, the next step is to onboard your resources. This involves configuring diagnostic settings to send logs to the workspace and connecting various data sources for an integrated monitoring solution.

<Frame>
  ![The image shows a Microsoft Azure portal page for a Log Analytics workspace named "law-monitoring," displaying details such as resource group, status, location, and subscription information. It also provides options for getting started with Log Analytics, including connecting data sources and configuring monitoring solutions.](https://kodekloud.com/kk-media/image/upload/v1752884686/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Enable-Log-Analytics-Workspace/azure-log-analytics-workspace.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Later in this guide, we will cover how to seamlessly connect additional resources to your Log Analytics workspace to enhance your monitoring capabilities.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/e208e27a-6519-4eb4-aaf1-342bb14def21/lesson/3b48fdd4-c4c3-4440-ac54-bed4ecb05806" />
</CardGroup>

---


## Lesson 5: Querying Log Analytics Workspace

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Querying-Log-Analytics-Workspace/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Querying-Log-Analytics-Workspace/page.md)

**Summary:** This article explains how to query a Log Analytics Workspace in Azure and onboard machines using Azure Monitoring Agent.

# Querying Log Analytics Workspace

> This article explains how to query a Log Analytics Workspace in Azure and onboard machines using Azure Monitoring Agent.

In this lesson, we explore how to query a Log Analytics Workspace in Azure. Learn how to ingest data from various environments—including on-premises systems, AWS, and GCP—using agents. Although legacy certification exams might still reference the older Log Analytics Agent (also known as the Microsoft Monitoring Agent or MMA), note that MMA is being deprecated. The recommended approach is to use the Azure Monitoring Agent (AMA) with Azure Arc for managing on-premises machines.

***

## Onboarding Machines and Agents

Traditionally, onboarding non-Azure machines involved installing the Log Analytics Agent and providing the appropriate workspace key. With the deprecation of MMA, the onboarding process now leverages Azure Arc to manage non-Azure machines. Once onboarded to Azure Arc, you can easily deploy the necessary extensions using Azure Resource Manager (ARM), much like managing an Azure Virtual Machine.

The diagram below illustrates the process flow for managing connected log sources in Log Analytics:

<Frame>
  ![The image is a flowchart illustrating the process of managing connected source log analytics, showing the interaction between Operations Manager, Linux and Windows agents, and the Log Analytics Workspace via Azure Portal.](https://kodekloud.com/kk-media/image/upload/v1752884688/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/log-analytics-flowchart-operations-manager.jpg)
</Frame>

After onboarding, use the Azure Portal to run queries that analyze and visualize the collected data. Data is organized into tables based on its type. For instance:

* Windows Event Logs populate the "Event" table.
* Syslog data is stored in the "Syslog" table.
* Heartbeat data, which monitors agent connectivity, appears in the "Heartbeat" table.
* Performance metrics are stored in the "perf" table.
* Custom logs can also be defined.

Below is an example Kusto query that unions data from the Event table and applies multiple filters to extract and render performance counter data:

```kusto theme={null}
| union Event
| where SeverityLevel == "Error"
| where ComputerIP startswith "52"
| where Computer startswith "DC"
| where OSType == "Windows" and OSName contains "2016"
| where CounterName == "Available MBytes" and Computer == "JBOX00"
| project TimeGenerated, CounterValue
| sort by TimeGenerated asc
| render timechart
```

***

## Configuring Monitoring for Virtual Machines

For demonstration purposes, we deploy a Windows machine, a Linux machine, and an App Service. These resources can be provisioned using a PowerShell script from the GitHub repository (named `monitoring-prep-infra-powershell`), which creates a resource group called `rgsecops` containing two virtual machines and a web app.

### Using the Legacy Agent (MMA)

Initially, the legacy MMA (Microsoft Monitoring Agent) is used for onboarding, even though it is scheduled for deprecation in August 2024. In the Log Analytics workspace within the Azure Portal, navigate to "Resources" and then "Virtual Machine" to view the onboarded machines:

<Frame>
  ![The image shows a Microsoft Azure portal interface for a Log Analytics workspace named "law-monitoring," displaying various settings and options related to log management and monitoring.](https://kodekloud.com/kk-media/image/upload/v1752884690/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-portal-log-analytics-workspace.jpg)
</Frame>

By clicking on "Connect," you can verify that the machines are attempting to join the workspace. Note that some operating systems are not supported by MMA; for example, Ubuntu 22.04 may exhibit compatibility issues. To diagnose such issues, check the extensions on the affected machine:

1. Navigate to Virtual Machines.
2. Select the Linux machine.
3. Click on "Extensions" to review the installation status.

For instance, if you encounter an error for the OMS Agent for Linux, it indicates that MMA does not support Ubuntu 22.04:

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a virtual machine named "linux-ra-vm." It highlights the "OmsAgentForLinux" extension, which is in a transitioning status with an error message related to an unsupported operating system.](https://kodekloud.com/kk-media/image/upload/v1752884690/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-portal-linux-ra-vm-error.jpg)
</Frame>

For Windows machines, the MMA status will indicate that it is provisioned and connected to your Log Analytics workspace. Return to the workspace to review the connected machines:

<Frame>
  ![The image shows a Microsoft Azure portal interface for a Log Analytics workspace named "law-monitoring," displaying the status of connected Windows computers and options for data collection rules.](https://kodekloud.com/kk-media/image/upload/v1752884691/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-log-analytics-workspace.jpg)
</Frame>

After connecting, run a simple heartbeat query to verify data reporting from your Windows machine. For example:

```kusto theme={null}
Heartbeat
| distinct Computer, Category
```

This query displays the distinct computer names and agent categories (e.g., direct agent for MMA and Azure Monitor Agent for AMA). Additionally, querying the Syslog table confirms data ingestion from the Linux machine.

<Frame>
  ![The image shows a Microsoft Azure Log Analytics workspace interface displaying a query result for "Heartbeat" logs, including details like time generated, computer ID, IP address, and operating system information.](https://kodekloud.com/kk-media/image/upload/v1752884693/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-log-analytics-heartbeat-logs.jpg)
</Frame>

***

## Transitioning to the Azure Monitor Agent (AMA) with Data Collection Rules

To adopt the modern agent (AMA), configure Data Collection Rules (DCRs) to define what data to collect and to specify the target Log Analytics workspace. AMA and MMA can coexist; however, be aware that sending data from both agents to the same workspace may result in duplicate billing.

Follow these steps to create a Data Collection Rule:

1. In the Azure Portal, go to the Monitor section and select "Data Collection Rules."
2. Create a new rule (e.g., named "AMADCR") in your monitoring resource group.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a data collection rule, with fields for rule name, subscription, resource group, region, and platform type.](https://kodekloud.com/kk-media/image/upload/v1752884694/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-portal-data-collection-rule.jpg)
</Frame>

3. Select "All" for the platform type to cover both Windows and Linux.
4. Under "Collect & Deliver," add the required data sources:

   * **Windows Event Logs:** Configure the desired logging levels (e.g., only critical events from Application or Security).
   * **Performance Counters:** Choose metrics such as CPU, memory, disk, network, system, and process counters.
   * **Linux Syslog:** Specify the desired logging levels (e.g., Debug, Info, Notice, Warning).

   Ensure that for each data source, the destination is set to your Log Analytics workspace.

<Frame>
  ![The image shows a Microsoft Azure interface for creating a data collection rule, specifically in the "Collect and deliver" section. It includes options to add a data source, with performance counters like CPU, Memory, Disk, Network, System, and Process selected for data collection.](https://kodekloud.com/kk-media/image/upload/v1752884695/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-data-collection-rule-interface.jpg)
</Frame>

<Frame>
  ![The image shows a Microsoft Azure interface for creating a data collection rule, specifically in the "Collect and deliver" section, where a data source type "Linux Syslog" is being configured with various log facilities and minimum log levels.](https://kodekloud.com/kk-media/image/upload/v1752884696/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-data-collection-linux-syslog.jpg)
</Frame>

5. Review and create the Data Collection Rule. During this process, a system-assigned managed identity is enabled, and the extension installation for the Azure Monitor Agent is automatically initiated.

<Frame>
  ![The image shows a Microsoft Azure portal screen for creating a data collection rule, with details about selected resources and configurations. Notifications indicate successful enabling of system-assigned managed identities and a deployment submission.](https://kodekloud.com/kk-media/image/upload/v1752884697/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-portal-data-collection-rule-2.jpg)
</Frame>

After configuring the DCR, verify the agent installation on your virtual machines by checking the extensions. On your Windows machine, you should now see the "Azure Monitoring Windows Agent," and on your Linux machine, the corresponding Azure agent appears (while MMA is not supported).

Return to your Log Analytics workspace and refresh the view of connected machines. After a short period, you should observe at least one Windows and one Linux computer reporting heartbeats via AMA:

<Frame>
  ![The image shows a Microsoft Azure portal interface for a Log Analytics workspace named "law-monitoring," displaying options for managing agents and connected computers. It indicates that there are no Linux computers connected via Azure Monitor or Log Analytics agents.](https://kodekloud.com/kk-media/image/upload/v1752884698/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-portal-log-analytics-workspace-2.jpg)
</Frame>

Run the heartbeat query again:

```kusto theme={null}
Heartbeat
| distinct Computer, Category
```

This confirms that the Windows VM is now sending two heartbeats (one from the legacy agent and another from AMA), while Linux machines report via AMA. Query the Syslog table to verify that entries are arriving from your Linux machine.

***

## Monitoring App Services

For Platform-as-a-Service (PaaS) resources such as App Services, an agent is not required because Microsoft manages the underlying infrastructure. Instead, configure Diagnostic Settings to capture logs and metrics. Follow these steps:

1. In the Azure Portal, navigate to your Web App and go to the "Diagnostic Settings" section.
2. Create a new diagnostic setting (e.g., "App DAG") and select the log and metric categories you want to capture.
3. Choose your Log Analytics workspace as the destination.

<Frame>
  ![The image shows a Microsoft Azure portal page for configuring diagnostic settings, where various log categories and destination details are selected for an application.](https://kodekloud.com/kk-media/image/upload/v1752884699/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-portal-diagnostic-settings.jpg)
</Frame>

Once configured, HTTP requests and other logs for your web app will be captured and stored in the "App Service HTTP Logs" table. These logs include details such as status codes and responses, which you can later query within your Log Analytics workspace.

<Frame>
  ![The image shows a Microsoft Azure portal interface focused on the "law-monitoring" Log Analytics workspace, displaying a list of log management options and a description of the "Event" log.](https://kodekloud.com/kk-media/image/upload/v1752884700/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Querying-Log-Analytics-Workspace/azure-portal-law-monitoring-log-analytics.jpg)
</Frame>

***

## Conclusion

In this lesson, we demonstrated how to onboard machines to a Log Analytics workspace using both the legacy MMA and the modern AMA approaches. While current exams may reference MMA, it is advisable to adopt AMA for new deployments due to its enhanced capabilities and support for modern operating systems. We also covered how to capture logs from App Services using Diagnostic Settings.

<Callout icon="lightbulb" color="#1CB2FE">
  Stay tuned for our upcoming guide on Azure Monitor Alerts to further enhance your monitoring strategy.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/e208e27a-6519-4eb4-aaf1-342bb14def21/lesson/ed41d04b-8a16-458d-949e-2af0824a8de8" />
</CardGroup>

---


## Lesson 6: Azure Alerts

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Azure-Alerts/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Monitoring/Azure-Alerts/page.md)

**Summary:** Learn to enable and configure Azure Monitor Alerts for critical event notifications in your Azure subscription.

# Azure Alerts

> Learn to enable and configure Azure Monitor Alerts for critical event notifications in your Azure subscription.

In this lesson, you will learn how to enable and configure Azure Monitor Alerts to stay informed of critical events in your Azure subscription. Azure Monitor Alerts provide a unified experience for creating notifications on various data sources such as activity logs, service health events, Log Analytics queries, and metrics.

<Frame>
  ![The image shows an Azure Monitor Alert dashboard with a list of critical alerts related to "Missing Assessment Data," all marked as fired and new. The dashboard displays a total of 24 critical alerts within the past 24 hours.](https://kodekloud.com/kk-media/image/upload/v1752884660/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-monitor-alerts-dashboard.jpg)
</Frame>

Azure Monitor Alerts work consistently across all resource types by classifying alerts by severity (from 0 to 4), categorizing them based on user responses (new, acknowledged, or closed), and integrating seamlessly with action groups. Action groups allow you to customize your notification and automation preferences—whether it’s email, SMS, voice calls, or triggering automated workflows using services like Automation Accounts, Function Apps, Logic Apps, or webhooks.

<Callout icon="lightbulb" color="#1CB2FE">
  Using Azure Monitor Alerts ensures that you receive timely notifications, making it easier to manage and remediate issues before they impact your production workloads.
</Callout>

Below are the four key stages for creating an alert rule:

## 1. Scope

The **Scope** defines the resources that the alert will monitor. Similar to Azure RBAC or Azure Policy, you can include one or more resources in your alert. This flexibility is particularly useful when creating alerts for activity logs or log query results.

<Frame>
  ![The image shows a screenshot of the "Create an alert rule" interface in Azure Monitor, focusing on setting the scope for an alert. Below are icons representing different steps in the alert creation process.](https://kodekloud.com/kk-media/image/upload/v1752884661/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-monitor-alert-rule-screenshot.jpg)
</Frame>

## 2. Condition

In the **Condition** step, you define the signal and the criteria that will trigger the alert. For example, you can set up a condition where an alert is fired if the percentage CPU utilization exceeds 80%.

<Frame>
  ![The image shows a setup screen for creating an Azure Monitor alert rule, focusing on configuring conditions like signal name and alert logic. Below, there are labeled icons for "Scope," "Condition," and other steps in the alert creation process.](https://kodekloud.com/kk-media/image/upload/v1752884662/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-monitor-alert-rule-setup.jpg)
</Frame>

## 3. Action

The **Action** stage involves selecting the action group that determines what happens when an alert fires. Action groups let you configure various notification options (such as email, SMS, push notifications, or voice calls) and automation options (including Automation Runbook, Azure Function, ITSM connectors, etc.). You can even set up multiple action groups for a single alert rule.

<Frame>
  ![The image is a guide on enabling Azure Monitor Alerts, showing options for setting up notifications and actions, including email, SMS, and various Azure services like Automation Runbook and Logic App.](https://kodekloud.com/kk-media/image/upload/v1752884664/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-monitor-alerts-guide.jpg)
</Frame>

## 4. Rule Details

In the **Rule Details** step, you provide essential information such as the alert rule’s name, description, and severity. This metadata is used in notifications to help you prioritize and manage alerts effectively.

Once configured, Azure Alerts integrates tightly with action groups, offering flexibility in notifying Azure Resource Manager roles (such as owner, contributor, or reader) or directing alerts to specific email addresses. You can also automate responses by invoking an Automation Runbook, calling a webhook, or integrating with ITSM systems.

***

## Creating an Alert Rule in the Azure Portal

Follow these steps to create an alert for a Log Analytics workspace:

1. **Open the Log Analytics Workspace:**\
   Navigate to your Log Analytics workspace and select the **Logs** section.

2. **Run a Query:**\
   Execute a query, like the one below, to check App Service HTTP logs for the last 25 minutes:

   ```kusto theme={null}
   AppServiceHTTPLogs
   | where TimeGenerated > ago(25m)
   | count
   ```

   In this scenario, the scope (the Log Analytics workspace) is predefined. If your query returns a result (e.g., 51 requests), you can set a threshold (such as 100 requests in 25 minutes) to trigger the alert.

<Frame>
  ![The image shows a Microsoft Azure interface for creating an alert rule, where users can set parameters like dimensions, alert logic, and evaluation frequency.](https://kodekloud.com/kk-media/image/upload/v1752884665/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-alert-rule-creation-interface.jpg)
</Frame>

For activity log alerts, you can apply filters for events such as the creation of a web app. Simply click the available action to create a new alert rule, and Azure will preconfigure the alert settings based on your selection.

***

## Creating Alerts for Virtual Machines

Setting up alerts for virtual machines is essential for monitoring production servers. The following instructions use CPU usage as an example metric:

1. **Navigate to Virtual Machines:**\
   In the Azure Portal, go to **Virtual Machines** and select a Linux machine.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a list of virtual machines, including details like name, type, subscription, location, status, operating system, and public IP address.](https://kodekloud.com/kk-media/image/upload/v1752884666/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-portal-virtual-machines-list.jpg)
</Frame>

2. **Create the Alert Rule:**\
   Click on the **Alerts** blade or select **Create a custom alert rule**. The system automatically selects the current resource; you can add resources, such as Windows machines if needed.

3. **Define the Condition:**\
   Under **Condition**, choose the appropriate metric, for instance, **Percentage CPU**. You can opt for static thresholds or dynamic ones—the latter adjusts to usage patterns to minimize false positives. For demonstration purposes, set a static threshold where the average CPU utilization over five minutes exceeds 80%.

<Frame>
  ![The image shows a Microsoft Azure interface for creating an alert rule, with settings for threshold, aggregation type, and time range. A preview graph displays CPU usage over time, with a threshold set at 80%.](https://kodekloud.com/kk-media/image/upload/v1752884667/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-alert-rule-cpu-usage.jpg)
</Frame>

4. **Configure the Action:**\
   Under **Action**, either select an existing action group or create a new one (e.g., "VM notification"). This group should define how you want to be notified (email, SMS, push, voice) and any associated automation actions.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating an action group, with a dropdown menu for selecting an action type such as Automation Runbook, Azure Function, and others.](https://kodekloud.com/kk-media/image/upload/v1752884668/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-portal-action-group-dropdown.jpg)
</Frame>

5. **Set Rule Details:**\
   In the **Rule Details** section, provide a relevant name (for example, "CPU Alert Metrics - Linux"), choose the severity level (e.g., Critical), and configure any advanced settings like immediate rule enabling.

<Frame>
  ![The image shows a Microsoft Azure interface for creating an alert rule, specifically on the "Actions" tab, where an action group named "vm-notification" containing one email action is listed. There is also a section for adding custom properties to the alert rule.](https://kodekloud.com/kk-media/image/upload/v1752884669/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-portal-alert-rule-cpu.jpg)
</Frame>

6. **Review and Create:**\
   Click **Review and Create** to finalize your alert rule.

<Callout icon="triangle-alert" color="#FF6B6B">
  Before testing alerts in a production environment, ensure you understand the potential impact on system performance when applying stress tests.
</Callout>

During testing, you can simulate high CPU load on your Linux VM using a stress program.

***

## Testing the Alert Using a Stress Program

To verify that your alert fires correctly, follow these steps:

1. **Connect to the Linux VM via SSH:**

   ```plaintext theme={null}
   ED25519 key fingerprint is SHA256:5wQadLwZ9EGH97C4SMttl7t6T6GFEnsl20qwhVXz6wQ.
   Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
   Warning: Permanently added '20.242.246.105' (ED25519) to the list of known hosts.
   Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 6.2.0-1014-azure x86_64)
   ...
   kodekloud@linux-ra-vm:~$
   ```

2. **Update and Install the Stress Program:**\
   Ensure your system is up-to-date and install the stress tool if it isn’t already installed.

3. **Run the Stress Test:**\
   Open another terminal session and SSH into the same VM to run the stress command. For example, to stress 4 CPU cores for 1000 seconds, use:

   ```bash theme={null}
   stress -c 4 -t 1000
   ```

   This command forces CPU usage to reach 100%. Monitor the CPU utilization dashboard in the Azure Portal to observe the increase.

<Frame>
  ![The image shows a Microsoft Azure portal screen for creating an alert rule, detailing the scope, condition, and actions for monitoring virtual machines. The alert is set to trigger when the CPU percentage exceeds a certain threshold.](https://kodekloud.com/kk-media/image/upload/v1752884670/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-portal-alert-rule-cpu-2.jpg)
</Frame>

4. **Alert Trigger:**\
   As the CPU utilization surpasses the set threshold (e.g., the average over the last five minutes exceeds 80%), Azure Monitor will trigger the alert and send an email notification.

<Frame>
  ![The image shows a Microsoft Azure monitoring dashboard displaying a line chart of CPU usage for a virtual machine, with a significant spike reaching 99.84% at a specific time.](https://kodekloud.com/kk-media/image/upload/v1752884671/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-monitoring-cpu-usage-chart.jpg)
</Frame>

***

## Verifying and Managing Alerts

After an alert is triggered, you can take the following actions:

* **Check Email Notifications:**\
  The email will include information such as the rule ID, resource ID, and metric details.

<Frame>
  ![The image shows an email notification from Microsoft Azure indicating that an Azure Monitor alert was triggered due to a CPU alert for a virtual machine. It includes details such as the rule ID, resource ID, and metric information.](https://kodekloud.com/kk-media/image/upload/v1752884673/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-monitor-cpu-alert-notification.jpg)
</Frame>

* **Review Alerts in Azure Portal:**\
  Examine the alert in the Azure Portal under the **Alerts** blade or check the activity logs for the specific resource.

<Frame>
  ![The image shows the Microsoft Azure portal displaying the activity log for a virtual machine named "linux-ra-vm." It lists various operations, their status, and timestamps.](https://kodekloud.com/kk-media/image/upload/v1752884674/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-portal-activity-log-linux-ra-vm.jpg)
</Frame>

* **Manage Alert Status:**\
  Change the alert status from "Fired" to "Acknowledged" or "Closed" to track incident resolution.

<Frame>
  ![The image shows the Microsoft Azure Monitor Alerts dashboard, displaying a critical alert for a resource named "linux-ra-vm" with the alert condition marked as "Fired."](https://kodekloud.com/kk-media/image/upload/v1752884675/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-monitor-alerts-linux-ra-vm.jpg)
</Frame>

You can always review all your alert rules and their current statuses within the portal to ensure your monitoring setup remains effective.

***

With this lesson, you have learned how to configure and test Azure Monitor Alerts using the Azure Portal along with a practical stress test on a Linux VM. This approach ensures you are promptly notified and can take swift action when your critical resources experience high CPU usage.

<Frame>
  ![The image shows a setup screen for creating an alert rule in Azure Monitor, with sections for project and alert rule details. Below, there are colorful icons labeled "Scope," "Condition," "Action," and "Rule details."](https://kodekloud.com/kk-media/image/upload/v1752884676/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Alerts/azure-monitor-alert-rule-setup-2.jpg)
</Frame>

For more detailed information, consider reviewing the [Azure Monitor documentation](https://docs.microsoft.com/en-us/azure/azure-monitor/).

Good luck, and happy monitoring!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/e208e27a-6519-4eb4-aaf1-342bb14def21/lesson/6878f0ca-097d-4e98-8e43-0a573c66c422" />
</CardGroup>

---
