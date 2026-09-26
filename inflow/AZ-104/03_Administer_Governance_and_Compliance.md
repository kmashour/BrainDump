# AZ-104 Section 03: Administer Governance and Compliance

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 11

---


## Lesson 1: Module Introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Module-Introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Module-Introduction/page.md)

**Summary:** This module covers strategies for managing Azure environments, including subscriptions, policies, and role-based access control.

# Module Introduction

> This module covers strategies for managing Azure environments, including subscriptions, policies, and role-based access control.

Welcome to the administer governance and compliance module of the [AZ-104: Microsoft Azure Administrator](https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator) course. In this lesson, you’ll explore essential strategies for effectively managing your Azure environment. This module is designed around three key learning objectives:

* **Configuring Subscriptions and Azure Resource Manager Resources**
* **Configuring Azure Policies**
* **Configuring Role-Based Access Control (RBAC)**

Below, each section is detailed to provide clear guidance on best practices and key focus areas.

## Configuring Subscriptions and Azure Resource Manager Resources

In this section, you will learn to organize and manage your Azure subscriptions and resources efficiently. Topics include:

* **Managing Subscriptions:** Techniques to keep your Azure subscriptions organized.
* **Resource Groups and Limits:** Strategies to structure your resources while maintaining preset limits.
* **Understanding the Hierarchy:** A clear breakdown of the Azure resource structure for effective management.
* **Azure Resource Tags:** Methods to simplify the organization and retrieval of Azure resources using tags.
* **Azure Resource Locks:** Approaches to safeguard your resources from accidental deletion or modification.

<Frame>
  ![The image lists learning objectives for configuring subscriptions and Azure Resource Manager resources, including managing subscriptions, resource groups, understanding hierarchy, Azure resource tags, and locks.](https://kodekloud.com/kk-media/image/upload/v1752884559/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Module-Introduction/azure-resource-manager-learning-objectives.jpg)
</Frame>

* **Managing Cost:** Explore proven techniques to monitor and control your Azure spending effectively.

<Frame>
  ![The image lists learning objectives related to configuring subscriptions and Azure Resource Manager resources, including managing subscriptions, resource groups, understanding hierarchy, resource tags, resource locks, and managing costs.](https://kodekloud.com/kk-media/image/upload/v1752884560/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Module-Introduction/azure-resource-manager-learning-objectives-2.jpg)
</Frame>

## Configuring Azure Policies

This section focuses on utilizing Azure Policy to enforce organizational standards and assess compliance at scale. You will discover:

* **Azure Policy Implementation:** How to apply policies that ensure continual compliance across your environment.
* **Initiatives:** Ways to group related policies to achieve specific compliance goals.

<Callout icon="lightbulb" color="#1CB2FE">
  Understanding Azure Policies is key to maintaining security and governance standards in your environment.
</Callout>

## Configuring Azure Role-Based Access Control (RBAC)

In this section, we dive into Azure RBAC, which is essential for assigning the proper levels of access to users. Topics include:

* **Defining Azure RBAC:** Learn how to manage and implement permissions effectively.
* **Comparing with Microsoft Entra ID Roles:** Although Microsoft Entra ID roles are covered in a separate module, you will also explore the differences between Azure RBAC and Entra ID roles, and understand when to apply each for optimal security.

<Frame>
  ![The image outlines learning objectives related to configuring Azure policies and role-based access control, including Azure Policy, Initiatives, and comparisons between Azure RBAC and Microsoft Entra ID Roles.](https://kodekloud.com/kk-media/image/upload/v1752884560/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Module-Introduction/azure-policies-rbac-learning-objectives.jpg)
</Frame>

With these objectives in mind, we now transition to our first topic: managing subscriptions.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/a683396b-3325-4f68-bb04-2c956bf5659a" />
</CardGroup>

---


## Lesson 2: Managing subscriptions

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Managing-subscriptions/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Managing-subscriptions/page.md)

**Summary:** This article explains Azure Subscriptions, their types, management, and how they help organize and monitor cloud resources effectively.

# Managing subscriptions

> This article explains Azure Subscriptions, their types, management, and how they help organize and monitor cloud resources effectively.

Imagine a library with thousands of books where your library card helps you track what you have read and what you owe. In Microsoft Azure, subscriptions work like that library card in the cloud. They help you manage, organize, and monitor your resources effectively.

Azure Subscriptions are logical containers that not only define billing boundaries for resource usage but also establish environmental limits. This allows you to monitor consumption, maintain control over expenditure, and enforce tailored policies across your cloud resources.

<Callout icon="lightbulb" color="#1CB2FE">
  Every subscription is assigned a unique identifier, known as a subscription ID, which ensures that every transaction or service used is traceable to your account for better management and security.
</Callout>

Azure grants you the flexibility to have multiple subscriptions under a single account. Whether you are managing different projects or departments, each can have its own billing and policy enforcement. To sign up for an Azure subscription, you need a Microsoft Entra ID or a trusted personal Microsoft account.

The versatility of Azure Subscriptions is evident with the various types available. They can be customized to meet your specific needs—be it development, testing, production, or even training. Beyond billing, subscriptions serve as a scope for access management and policy enforcement, ensuring roles and policies can be assigned universally across all resources.

<Frame>
  ![The image is an infographic about Azure Subscriptions, highlighting features such as billing boundaries, resource mapping, environmental boundaries, unique IDs, multiple subscriptions, identity sign-up, subscription types, and access management.](https://kodekloud.com/kk-media/image/upload/v1752884552/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Managing-subscriptions/azure-subscriptions-infographic-features.jpg)
</Frame>

Below, we explore the different subscription offer types available in Azure.

***

## Subscription Offer Types

Azure provides a variety of subscription options to cater to the needs of diverse users, from large enterprises to individual developers.

### Enterprise Agreements

Enterprise Agreements are tailored for large organizations needing comprehensive solutions with volume pricing. These agreements simplify the management of cloud services across entire enterprises by offering flexible pricing that scales with your business. Organizations often commit to a predetermined consumption level—such as $1 million, $5 million, or \$10 million—paying the cost upfront.

### Pay-As-You-Go

The Pay-As-You-Go model offers maximum flexibility with no long-term commitment. You pay only for the resources you consume, allowing you to scale your usage up or down as needed while maintaining full control over your cloud spending.

### Cloud Solution Provider (CSP)

The Cloud Solution Provider (CSP) program allows businesses to partner with experts who create custom solutions. Instead of paying Microsoft directly, you purchase a subscription from a partner—often at a cost lower than the Pay-As-You-Go option—as the partner adds their own markup for the service.

### Free Trial

For new users eager to explore Azure, the Free Trial subscription provides a risk-free opportunity. This option lets you experiment with Azure’s capabilities without any initial financial commitment, making it perfect for learning and prototyping.

### Azure for Students

Azure for Students is designed to empower students by offering free access to Azure resources and credits. This subscription enables students to develop real-world skills and experiment with cloud technologies, usually verified by a student ID or an academic email address.

### Visual Studio Subscription

The Visual Studio subscription is ideal for developers, combining cloud resources with the powerful development tools of Visual Studio. Purchasing a Visual Studio Professional or Enterprise subscription includes an MSDN or Visual Studio subscription that offers a recurring monthly credit (for example, $100 or $150 depending on the license type).

<Frame>
  ![The image lists different subscription offer types: Enterprise Agreements, Pay-as-You-Go, Cloud Solution Provider, Free Trial, Azure for Students, and Visual Studio, each with an icon.](https://kodekloud.com/kk-media/image/upload/v1752884553/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Managing-subscriptions/subscription-offer-types-list.jpg)
</Frame>

Additional subscriptions, like the DevTest offer found under Microsoft Azure Offer Details, further expand your options, varying by licenses, agreements, and specific Microsoft plans.

***

## Navigating Subscriptions in the Azure Portal

When you log into the [Azure Portal](https://portal.azure.com), you can easily view all your subscriptions. A search for “subscriptions” will display entries with details such as the offer ID, helping you identify and manage each one.

For example, consider a Visual Studio subscription that provides monthly credits for development and testing. In the portal, notifications might display an available balance of 6,000 rupees alongside the subscription details. Offer IDs, such as "62P" for platform subscriptions or "243P" for sponsorship-based subscriptions, help further distinguish them.

<Frame>
  ![The image shows a Microsoft Azure portal dashboard displaying subscription details for "MSDN Firbish RTN," including subscription ID, billing period, and cost management options. It also features charts for spending forecasts, resource costs, and Azure Defender coverage.](https://kodekloud.com/kk-media/image/upload/v1752884555/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Managing-subscriptions/azure-portal-dashboard-msdn-firbish.jpg)
</Frame>

Some subscriptions are based on sponsorships. Searching for “Azure Pass” in the portal will quickly identify these special offers.

<Frame>
  ![The image shows a Microsoft Azure portal displaying subscription details for "Kodekloud Azure Admin - PoC 1," including subscription ID, offer details, and billing information. It also indicates that Azure Defender is not enabled for this subscription.](https://kodekloud.com/kk-media/image/upload/v1752884556/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Managing-subscriptions/azure-portal-subscription-details.jpg)
</Frame>

Each subscription entry includes hyperlinks that provide more information on offer details and subscription management.

<Frame>
  ![The image shows a webpage listing various Microsoft Azure offers, each with an associated offer number and some with a checkmark indicating a spending limit. A cursor is pointing at the "Azure Pass Sponsorship" offer.](https://kodekloud.com/kk-media/image/upload/v1752884557/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Managing-subscriptions/azure-offers-listing-checkmark.jpg)
</Frame>

If you wish to add a new subscription, navigate to the offer selection within the Azure Portal. The system will verify your eligibility and display the offers available to you. For instance, if you have exhausted your free trial, only alternative options like Pay-As-You-Go or Azure for Students may be available. Note that choosing Azure for Students will require university credential verification. Other offers include Pass Sponsorship, Visual Studio, Enterprise, Developer Support, and Azure in Open—a voucher-like option for recharging your Azure credits.

<Frame>
  ![The image shows a Microsoft Azure portal page where users can select offers for their subscriptions, with options like "Microsoft Partner Network" and "Azure in Open." There are buttons to check eligibility and select offers.](https://kodekloud.com/kk-media/image/upload/v1752884558/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Managing-subscriptions/azure-portal-offer-selection.jpg)
</Frame>

***

With a clear understanding of Azure Subscriptions and their various offer types, the next step is to focus on managing Resource Groups and Resource Limits, which further streamline resource organization and ensure operational efficiency.

For more insights on Azure resource management, consider exploring additional resources such as [Azure Documentation](https://docs.microsoft.com/azure).

Happy cloud managing!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/50db585f-47cb-472b-bd18-a16c06b20b39" />
</CardGroup>

---


## Lesson 3: Resource Groups and Limits

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Resource-Groups-and-Limits/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Resource-Groups-and-Limits/page.md)

**Summary:** This article explains Azure resource groups, their organization strategies, and service limits to enhance resource management and prevent overuse.

# Resource Groups and Limits

> This article explains Azure resource groups, their organization strategies, and service limits to enhance resource management and prevent overuse.

Resource groups in Azure work similarly to folders on your computer. They help you organize resources such as virtual machines, databases, storage accounts, and more. Grouping related resources into a single container simplifies administration, monitoring, and access control by applying permissions and policies at the group level.

There are two primary strategies for organizing your Azure resources:

1. Group all resources related to an application (e.g., web servers, databases, storage) into one resource group.\
   This approach is ideal for scenarios like an e-commerce website where keeping all components together simplifies management and interdependency tracking.

2. Group resources by type.\
   For instance, you might create one group for all virtual machines and another for storage accounts—similar to organizing shirts and pants in separate drawers. This method works well for large organizations with complex resource management needs.

A common concern is whether placing resources in different resource groups affects networking or communication. The answer is no—resource grouping is purely logical. Networking is managed independently, so resources communicate regardless of their group placement.

## Key Points about Resource Groups

* A resource group serves as a container to simplify billing, monitoring, and overall administration.
* Resource groups can include services deployed across multiple geographic locations, offering greater scalability and flexibility. For example, a resource group created in East US might contain a resource physically running in West Europe, while the metadata remains stored in East US.
* Once established, the name of a resource group cannot be changed, nor can resource groups be nested within one another.

<Frame>
  ![The image explains the concept of creating resource groups, highlighting that they can contain various services and cannot be renamed or nested. It illustrates grouping resources like web, database, virtual machines, and storage either together or separately.](https://kodekloud.com/kk-media/image/upload/v1752884562/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Resource-Groups-and-Limits/resource-groups-services-illustration.jpg)
</Frame>

* Although resource group names are permanent, you can still move resources between groups using Azure Resource Mover—much like moving files between folders on your computer.

## Creating a Resource Group in the Azure Portal

To create a resource group using the Azure Portal, follow these steps:

1. Open the Azure Portal and either click on the Resource Groups button or search for "Resource Groups".

<Frame>
  ![The image shows the Microsoft Azure portal interface, displaying various Azure services and a list of resources with details such as type and last viewed time.](https://kodekloud.com/kk-media/image/upload/v1752884563/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Resource-Groups-and-Limits/azure-portal-interface-services-list.jpg)
</Frame>

2. On the Resource Groups page, view existing groups or create a new one.

<Frame>
  ![The image shows a Microsoft Azure portal page displaying a list of resource groups. There are options to create, manage, and filter resource groups, with three listed: "about-nithin," "dns-domains," and "NetworkWatcherRG."](https://kodekloud.com/kk-media/image/upload/v1752884564/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Resource-Groups-and-Limits/azure-portal-resource-groups-list.jpg)
</Frame>

3. To create a new resource group:
   * Select the desired subscription.
   * Enter a unique name for the group.
   * Choose a region that meets your compliance and organizational requirements (e.g., East US).
   * Optionally, add tags for easier resource management.
   * Proceed by clicking "Review and Create".

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a resource group, with fields for subscription, resource group name, and region.](https://kodekloud.com/kk-media/image/upload/v1752884564/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Resource-Groups-and-Limits/azure-portal-resource-group-creation.jpg)
</Frame>

After the resource group is created, you can reference it when deploying resources. For example, when creating a Storage Account, you have the option to select an existing resource group (e.g., RG Admin 01) or to create a new one seamlessly.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a storage account, with fields for project and instance details such as subscription, resource group, and performance options.](https://kodekloud.com/kk-media/image/upload/v1752884565/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Resource-Groups-and-Limits/azure-portal-storage-account-creation.jpg)
</Frame>

Resource groups can also be created using the Azure CLI, Azure PowerShell, or REST APIs. Detailed guidance on these methods will be provided in upcoming sessions. For now, note that creating a resource group through the portal is a straightforward and essential step in managing your Azure environment.

## Service Limits and Quotas

Azure's service limits and quotas are designed to maintain the cloud ecosystem's health and performance. They help prevent unexpected usage spikes that might degrade performance and allow you to manage costs effectively while preventing platform overuse.

For example, if a script attempts to deploy 10,000 virtual machines, a predefined limit ensures that one user does not consume all the available resources. This safeguard ensures fair resource distribution among customers. Should your business require usage beyond the default limits, you have the option to request an increase.

Azure enforces default limits (quotas) at the subscription level to prevent accidental over-provisioning and unexpected charges. For instance, there might be a cap on the number of virtual CPUs deployable in a region to help manage budgets and resource allocation.

You can think of these usage statistics much like a fuel gauge in a car, providing visibility into remaining capacity.

<Frame>
  ![The image shows a dashboard for determining service limits and quotas, displaying usage statistics for various resources in different regions. It includes information on current usage, subscription details, and whether the limits are adjustable.](https://kodekloud.com/kk-media/image/upload/v1752884566/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Resource-Groups-and-Limits/service-limits-usage-dashboard.jpg)
</Frame>

Limits may be adjustable or fixed:

* Some quotas can be increased directly through the portal by submitting a request.
* Others require a support ticket with Microsoft.
* Some limits are "hard limits" that cannot be changed, whereas "soft limits" can be increased with Microsoft’s assistance. In cases where a hard limit is reached, provisioning an additional subscription may be necessary to meet your requirements.

## Managing Quotas in the Azure Portal

To view and manage your quotas:

1. Navigate to your subscription within the Azure Portal, where these limits are enforced.
2. Select "Usage + Quotas" to view your current consumption. You can filter the data by provider (e.g., Storage or Compute) or sort by region.
3. For example, when reviewing compute resources (virtual machines) in a specific region, you will see the total regional vCPU count along with current usage status. If the quota is adjustable, you may submit a request for an increase.

<Frame>
  ![The image shows a Microsoft Azure portal screen displaying a quota management interface for a subscription, with a sidebar for submitting a new quota request for virtual CPUs in the Central India region.](https://kodekloud.com/kk-media/image/upload/v1752884566/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Resource-Groups-and-Limits/azure-portal-quota-management-cpu.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Free trial or sponsored subscriptions generally have stricter quota limits compared to paid subscriptions, which usually have better chances for quota adjustments.
</Callout>

## Conclusion

Understanding how resource groups and service limitations work is crucial for effective Azure cloud resource management. With resource groups, you optimize the organization, control, and billing of your resources. Meanwhile, Azure’s service limits and quotas ensure fair usage and prevent resource exhaustion, contributing to a balanced and sustainable cloud environment.

Now that you are familiar with managing subscriptions, resource groups, and limits, you are better equipped to understand the overall hierarchy and integration of these elements within your Azure environment.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/ff530a0b-2359-42b7-aa66-7470961f1167" />
</CardGroup>

---


## Lesson 4: Understanding the hierarchy

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Understanding-the-hierarchy/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Understanding-the-hierarchy/page.md)

**Summary:** This article explains Azures hierarchical framework for organizing, managing, and securing subscriptions and resources, highlighting its importance for policy implementation and cost control.

# Understanding the hierarchy

> This article explains Azures hierarchical framework for organizing, managing, and securing subscriptions and resources, highlighting its importance for policy implementation and cost control.

Effective management and organization of resources in Azure is essential for maintaining a well-structured cloud environment. Azure’s hierarchical framework organizes, manages, and secures multiple subscriptions and their associated resources. In this article, we explain how the hierarchy functions and why its structure is critical for implementing policies, managing access, and controlling costs.

## Overview of Azure's Hierarchy

At the very top of the hierarchy are management groups. These groups serve as a scope above individual subscriptions, allowing you to group multiple subscriptions together. By default, Azure creates a root management group for your organization. Beneath the root, you can establish up to six levels of nested management groups—forming a tiered structure that resembles a tree with many branches (excluding the root itself).

As shown in the diagram below, the hierarchy starts with the root management group at the top. It then branches into segments such as IT and Finance. For instance, within the IT branch, further subdivisions like production and development can be created. This logical structure is indispensable for the effective grouping and management of resources.

<Frame>
  ![The image is a hierarchical diagram explaining management groups, subscriptions, and resource groups, with a flow from the root management group to IT and Finance, and further to specific subscriptions. It includes text boxes describing the purpose and structure of these elements.](https://kodekloud.com/kk-media/image/upload/v1752884568/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Understanding-the-hierarchy/management-groups-subscriptions-diagram.jpg)
</Frame>

Within each management group, subscriptions are organized, and each subscription can contain one or more resource groups. These resource groups allow logical grouping of resources such as virtual machines, databases, and more. The cascading application of policies and permissions, known as inheritance, ensures consistent governance across your Azure environment. For example, granting access at the IT level automatically applies the same permissions to all underlying subscriptions and their resources, which is a fundamental aspect of Role Based Access Control (RBAC).

## Managing the Hierarchy in the Azure Portal

Working with management groups in the Azure portal is straightforward. Follow these steps to manage your Azure hierarchy effectively:

1. **Viewing Management Groups and Subscriptions**\
   Open the Azure portal and navigate to the management groups section. Here, you will see the root group alongside various subscriptions and any additional management groups. Expanding a group may reveal, for example, three subscriptions under the IT category.

2. **Creating a New Management Group**\
   If you need to create a new management group—say, one named AZ-104—enter the desired display name, and the group is created. Initially, AZ-104 will not have any subscriptions assigned. You can later move existing subscriptions into this group.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying management groups and subscriptions. It lists various groups and subscriptions with their types and IDs.](https://kodekloud.com/kk-media/image/upload/v1752884568/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Understanding-the-hierarchy/azure-portal-management-groups-subscriptions.jpg)
</Frame>

3. **Adding a Subscription to a Management Group**\
   To add a subscription to the AZ-104 management group, navigate into the group and select the option to add a subscription.

<Frame>
  ![The image shows a Microsoft Azure portal interface where a user is adding a subscription to a management group named "AZ-104." The "Add subscription" window is open, displaying options for selecting a subscription.](https://kodekloud.com/kk-media/image/upload/v1752884569/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Understanding-the-hierarchy/azure-portal-add-subscription-az104.jpg)
</Frame>

4. **Verifying the Hierarchy**\
   After adding subscriptions, refresh the hierarchy view. This ensures that the subscriptions now appear correctly under the AZ-104 group.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a management group named "AZ-104," including its subscriptions and related information. The interface includes options for creating, adding subscriptions, and managing access control.](https://kodekloud.com/kk-media/image/upload/v1752884570/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Understanding-the-hierarchy/azure-portal-management-group-az104.jpg)
</Frame>

5. **Reorganizing Subscriptions**\
   In cases where a subscription isn’t in its appropriate management group—such as appearing under the root instead of the IT group—you can easily move it. Click on the subscription options (typically represented by three dots), select "Move," choose the target group (e.g., IT), and then click "Save." This action helps maintain an organized and logical hierarchy.

<Callout icon="lightbulb" color="#1CB2FE">
  Remember, applying RBAC policies at a higher level will automatically propagate permissions to all child resources, saving time and ensuring consistency.
</Callout>

## Conclusion

The Azure resource hierarchy—comprising management groups, subscriptions, resource groups, and the resources themselves—is vital for efficient policy implementation, access control, and cost management. A solid understanding of this structure not only simplifies governance but also supports scalable management strategies within your Azure environment.

Stay tuned for our next discussion, where we will explore Azure Resource Tags in detail.

<Frame>
  ![The image shows a Microsoft Azure portal page displaying management groups and subscriptions, with details such as names, types, IDs, and total subscriptions.](https://kodekloud.com/kk-media/image/upload/v1752884571/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Understanding-the-hierarchy/azure-portal-management-groups-subscriptions-2.jpg)
</Frame>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/18b3faf0-1c52-443b-9ca9-07b37e8e4491" />
</CardGroup>

---


## Lesson 5: Azure Resource Tags

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/page.md)

**Summary:** Guide explaining Azure resource tags, how to manage them in the portal, enforce inheritance with Azure Policy, and follow best practices for organization and cost allocation.

# Azure Resource Tags

> Guide explaining Azure resource tags, how to manage them in the portal, enforce inheritance with Azure Policy, and follow best practices for organization and cost allocation.

Tags in Azure are key-value pairs you attach to resources to provide searchable metadata for organization, governance, automation, and cost allocation. In environments with many subscriptions, resource groups, and resources, tags help you identify ownership, environment, project, and billing information quickly and consistently.

This guide explains how Azure resource tags work, how to manage them in the Azure portal, and best practices for tagging at scale.

## Why use Azure tags?

Use tags to add metadata, group cross-resource workloads, and track costs. Common scenarios include ownership, environment identification, project grouping, and cost center allocation.

| Use case         |                                                 Purpose | Example tag               |
| ---------------- | ------------------------------------------------------: | ------------------------- |
| Ownership        |                 Identify the responsible person or team | `Owner: Sam`              |
| Environment      |         Separate production, staging, and dev resources | `Environment: Production` |
| Project grouping | Group resources across resource groups or subscriptions | `Project: Apollo`         |
| Cost allocation  |            Attribute spend to finance codes or projects | `CostCenter: 1100`        |

Key points about scope and inheritance:

* Tags can be applied to subscriptions, resource groups, and individual resources.
* Billing and cost reporting are determined at the resource level—tags must be on the resource for accurate cost allocation.
* Tags do not automatically flow from a resource group or subscription to underlying resources unless you enforce that behavior (for example, through Azure Policy or supported preview features).

<Callout icon="lightbulb" color="#1CB2FE">
  Tip: If you prefer tagging at the resource group level for human convenience, use policy enforcement to copy or inherit those tags onto resources so billing and automation tools see them at the resource level.
</Callout>

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/azure-tags-usecases-inheritance-policy.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=ab170c5a8aebeb5e9ee5b7e19c863e02" alt="A slide titled &#x22;Azure Resource Tags&#x22; showing four use cases—Adding metadata, Logical grouping, Name-value pair, and Cost management—each illustrated with an Azure icon and a colored tag. A footer notes that tags don't follow inheritance by default and Azure Policy can be used to inherit tags from a resource group or subscription." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/azure-tags-usecases-inheritance-policy.jpg" />
</Frame>

## Preview features vs. production

Azure occasionally offers preview capabilities for tag inheritance. In production, rely on GA (generally available) features like Azure Policy to ensure consistent, auditable, and enforceable tag behavior.

<Callout icon="warning" color="#FF6B6B">
  Warning: Avoid relying on preview features in production. Prefer policy enforcement to ensure tag inheritance and governance for stable, auditable behavior.
</Callout>

## Managing tags in the Azure portal

Follow these steps to add or edit tags on individual resources from the portal:

1. Open the Azure portal and go to All resources.
2. Select a resource (for example, a virtual machine or storage account) and open the Tags pane.
3. Add name-value pairs. Example:
   * Name: `Owner` — Value: `Sam`
   * Name: `Environment` — Value: `Dev`
   * Name: `CostCenter` — Value: `1100`
4. Save to apply the tags.

The portal suggests existing tag names and values from your subscription while you type, encouraging consistent naming and reuse.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/azure-portal-storage-aboutrithin-edit-tags.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=7f30440e24e2dd63dc662fc228c8ba47" alt="A screenshot of the Microsoft Azure portal showing the &#x22;All resources&#x22; list and the &#x22;about-rithin&#x22; storage account details, with an &#x22;Edit tags&#x22; panel open where an Environment tag value (e.g., &#x22;Dev&#x22;) is being entered. The left pane lists multiple resources and the center pane shows resource properties and services." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/azure-portal-storage-aboutrithin-edit-tags.jpg" />
</Frame>

## Filter, discover, and edit tagged resources

* Filtering: Use the filters in All resources to find resources by tag (for example, filter where `Environment` = `Dev` to show development resources).
* Tag blade: The Tags blade lists all name-value combinations used across the subscription. Clicking an entry shows resources that use that tag.
* Editing tags on a resource: Open the resource, click Edit tags, change the value or delete a tag using the trash icon, then save. Refresh the resource list or Tags view to see updates.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/azure-about-rithin-vm-edit-tags.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=4291e1fcb5054924f3f9481a67012553" alt="A screenshot of the Microsoft Azure portal showing the overview for a virtual machine named &#x22;about-rithin-vm&#x22; with the Edit tags pane open. The tags shown include &#x22;Cost Center: 1100&#x22; and &#x22;Environment: Dev.&#x22;" width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/azure-about-rithin-vm-edit-tags.jpg" />
</Frame>

## Tag listing and propagation

* The Tags blade provides a subscription-wide view of tag keys and values and enables quick navigation to tagged resources.
* You can add new keys or values directly from the Tags blade; newly added entries will appear across the portal after a refresh.
* To ensure tags exist on resources (important for billing and automation), use Azure Policy to enforce tag presence, copy tags from resource groups, or deny resource creation unless required tags are present.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/azure-portal-tags-environment-prod-cursor.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=1bd2fbd2082054cc903c33d7f9b854c1" alt="A screenshot of the Microsoft Azure portal showing the &#x22;Tags&#x22; blade with tag entries like &#x22;Cost Center : 1100&#x22;, &#x22;Environment : Dev&#x22;, and &#x22;Environment : Prod&#x22;. A cursor is hovering over or clicking the &#x22;Environment : Prod&#x22; tag." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/azure-portal-tags-environment-prod-cursor.jpg" />
</Frame>

## Applying tags to resource groups

* Resource group tags help organization and discovery, especially for teams that think in terms of application boundaries.
* Resource group tags do not automatically propagate to underlying resources unless you deploy or enforce propagation (for example, with Azure Policy).
* For production governance, enforce tag standards and inheritance via Azure Policy to ensure consistent application across resources and accurate cost reporting.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/azure-portal-resource-group-about-rithin.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=5f884ac20d075878c7dc93b85a62c013" alt="A screenshot of the Microsoft Azure portal showing the &#x22;Resource groups&#x22; view with the &#x22;about-rithin&#x22; resource group selected and a list of resources (VMs, public IP, NSG, disks, etc.) in the right-hand pane. The left navigation menu, filters, and subscription/essentials info are also visible." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Tags/azure-portal-resource-group-about-rithin.jpg" />
</Frame>

## Best practices for tagging

* Define a tagging taxonomy and publish it (keys, allowed values, conventions).
* Standardize on casing and separators (e.g., kebab-case or PascalCase) to avoid duplicates like `CostCenter` vs `cost-center`.
* Use a small, consistent set of keys (Owner, Environment, Project, CostCenter, Compliance) to reduce management overhead.
* Enforce mandatory tags at resource creation using Azure Policy and remediate noncompliant resources automatically where appropriate.
* Review and clean up unused tag keys periodically to keep the catalog manageable.

## Summary

* Tags are name-value pairs used to label resources for management, billing, and organization.
* For billing and automation, tags must exist on the resource level—resource group or subscription tags won’t automatically apply to resources without enforcement.
* Use Azure Policy to enforce tagging standards, automate inheritance, and maintain consistent governance at scale.

## Links and references

* [Azure Policy documentation](https://learn.microsoft.com/azure/governance/policy/)
* [Tag resources in Azure](https://learn.microsoft.com/azure/azure-resource-manager/management/tag-resources)
* [Azure cost management and billing](https://learn.microsoft.com/azure/cost-management-billing/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/00d038ab-75ff-452a-b885-1a1324b4f015" />

  <Card title="Practice Lab" icon="flask-conical" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/4b712333-ccaf-4e8b-9ff1-90288e4853e0" />
</CardGroup>

---


## Lesson 6: Azure Resource Locks

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Locks/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Resource-Locks/page.md)

**Summary:** Azure Resource Locks protect your Azure resources from accidental modifications or deletions, ensuring critical resources remain secure during maintenance or script executions.

# Azure Resource Locks

> Azure Resource Locks protect your Azure resources from accidental modifications or deletions, ensuring critical resources remain secure during maintenance or script executions.

Imagine working late while deploying updates to your Azure environment. A single moment of distraction could lead to running a script without a proper double-check, causing your crucial DNS domain to be deleted. Azure Resource Locks act as a safeguard, preventing accidental modifications or deletions and ensuring that a small mistake doesn’t result in irreversible damage.

In this article, we explore how resource locks protect your Azure environment from unintentional changes.

## What Are Resource Locks?

Resource locks are a critical feature designed to protect your Azure resources from unintended modifications. Think of them as a safety cover on a switch—ensuring that nothing is toggled accidentally. When enabled, these locks keep your resources unchanged during routine maintenance or while scripts are running.

Azure allows you to apply locks at various scopes:

* **Subscription**
* **Resource Group**
* **Individual Resource**

Once a lock is applied at a particular scope, it is automatically inherited by all underlying resources. For instance, applying a lock at the resource group level means every resource within that group is protected.

## Types of Resource Locks

Azure provides two primary types of resource locks:

1. **Read-Only Locks**\
   A read-only lock lets you view a resource without modifying or deleting it, much like placing valuable items in a display case—you can admire them but not alter them.

2. **Delete Locks**\
   A delete lock allows modifications but prevents the complete removal of a resource. This is akin to writing with a pencil that does not have an eraser—you can adjust details, but the resource itself remains undeletable.

The following infographic illustrates the benefits of Azure Resource Locks, highlighting the prevention of accidental changes, inheritance across resources, and the flexibility to operate in both read-only and delete modes.

<Frame>
  ![The image is an infographic about resource locks, explaining their benefits such as avoiding accidental changes, inheritance, read-only locks, and delete locks.](https://kodekloud.com/kk-media/image/upload/v1752884530/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Resource-Locks/resource-locks-infographic-benefits.jpg)
</Frame>

## Implementing Resource Locks in the Azure Portal

Follow these steps to implement resource locks using the Azure portal:

1. **Navigate to the Resource Groups Section**\
   Open the Azure portal and locate the Resource Group that contains the resource you wish to protect. For example, select a Resource Group that holds an automation account.

2. **Select the Resource**\
   Within your chosen Resource Group, open the automation account. In the left-hand menu, click on the "Locks" option.

3. **Add a Delete Lock**
   * Click on **Add lock**.
   * Provide a name (e.g., "DND" for "Do Not Delete").
   * Set the lock type to **Delete**.
   * Optionally, add a note for other users.
   * Click **Save**.

After saving, the delete lock becomes active. If you navigate back to the Overview blade for the resource and attempt to delete it, an error message will confirm that deletion is blocked due to the active lock.

<Frame>
  ![The image shows a Microsoft Azure portal page displaying a lock configuration for a resource group named "cleanup-env." It lists a lock named "DND" with a lock type of "Delete" and a note stating "Do not delete this resource."](https://kodekloud.com/kk-media/image/upload/v1752884531/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Resource-Locks/azure-portal-lock-configuration.jpg)
</Frame>

Even though the delete lock stops resource removal, you can still modify aspects of the resource. For instance, you can update runbooks within the automation account without any issues.

4. **Switching to a Read-Only Lock**
   * Return to the "Locks" section in the automation account.
   * Remove the existing delete lock.
   * Add a new lock, setting the type to **Read-only**.
   * Name it "RO" and include any notes or descriptions.
   * Click **Save**.

<Frame>
  ![The image shows a Microsoft Azure portal interface where a user is adding a lock to a resource group named "cleanup-env." The lock type is set to "Read-only," and the lock name is being entered as "RO."](https://kodekloud.com/kk-media/image/upload/v1752884532/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Resource-Locks/azure-portal-lock-readonly-cleanup-env.jpg)
</Frame>

With the read-only lock in place, attempts to create a new resource—such as a Python runbook (version 3.8) named "demo2"—will result in an error message indicating that the scope is locked. This clearly demonstrates the difference in behavior between a read-only lock and a delete lock.

<Frame>
  ![The image shows a Microsoft Azure portal screen for creating a runbook with fields for name, runbook type, and runtime version. An error message indicates a "ScopeLocked" issue preventing the creation of the runbook.](https://kodekloud.com/kk-media/image/upload/v1752884533/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Resource-Locks/azure-portal-runbook-creation-error.jpg)
</Frame>

## Applying Locks at the Resource Group Level

From the Resource Groups view, you can inspect any locks applied at that level. The locking mechanism works similarly at the subscription level, where every resource within the subscription inherits the lock.

To further enhance protection, you can add an additional lock at the resource group level. For instance, add a delete lock named "RG lock" (or any custom name) to the Resource Group.

<Frame>
  ![The image shows a Microsoft Azure portal interface where a user is adding a lock to a resource group named "about-rithin." The lock type is set to "Delete," and the user is about to confirm by clicking "OK."](https://kodekloud.com/kk-media/image/upload/v1752884535/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Resource-Locks/azure-portal-add-lock-resource-group.jpg)
</Frame>

After saving this lock, all resources within the Resource Group—such as virtual machines (VMs), storage accounts, and network interfaces—are protected. Attempting to delete a VM along with its associated resources (disk, network interface, etc.) will fail due to the active lock.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a resource group named "about-rithin," with a list of resources such as virtual machines, IP addresses, and network security groups, along with their types and locations.](https://kodekloud.com/kk-media/image/upload/v1752884536/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Resource-Locks/azure-portal-resource-group-about-rithin.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Remember, to make any change to a resource that is locked, you must first remove the active lock, perform the necessary updates, and then reapply the lock to maintain continuous protection.
</Callout>

## Conclusion

Azure Resource Locks are a powerful tool that safeguards your cloud environment against accidental modifications or deletions. By strategically applying read-only or delete locks, you add an essential layer of protection to your resources. This ensures that routine maintenance or inadvertent script executions do not lead to critical mistakes.

Next, we will delve into strategies for managing costs in your Azure subscription, providing further insights for maintaining a secure and efficient cloud environment.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/84a0bcaf-7696-445f-b093-5150e192b0c5" />
</CardGroup>

---


## Lesson 7: Manage costs

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Manage-costs/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Manage-costs/page.md)

**Summary:** This article discusses Azure Cost Management tools and strategies for monitoring, allocating, and optimizing cloud spending effectively.

# Manage costs

> This article discusses Azure Cost Management tools and strategies for monitoring, allocating, and optimizing cloud spending effectively.

Managing cost in the cloud is as crucial as managing your resources. Azure Cost Management serves as a financial navigator on your cloud journey by providing visibility and tools to monitor, allocate, and optimize your spending.

Imagine planning a road trip. You map out your route, budget your expenses, and continuously monitor your fuel. In a similar way, Azure Cost Management helps you track service usage, set budgets, and analyze costs to ensure you stay on the most economical path. In this guide, we will explore the key features of Azure Cost Management and strategies to optimize your spending.

## Cost Analysis: Your Financial Dashboard

Cost analysis offers a clear dashboard to visualize your spending by service, location, or Resource Group. You can quickly identify major expenses—like a high cost on Azure App Service—and investigate ways to optimize further.

For instance, when viewing cost analysis in the Azure portal:

* **Customization:** You can change the currency (e.g., from your local currency to US dollars) or adjust the time period (last seven days, this month, last invoice, or even a custom date range).
* **Scope Navigation:** Click on the scope to change your view. You can filter at the root management group level, a specific subscription, or even down to a particular Resource Group. Note that not all subscriptions (e.g., sponsorship subscriptions) support cost management.
* **Filtering:** Use filters such as meter category (for example, "Virtual Machines") to focus on specific costs, and group data by dimensions like Resource Group name.

<Callout icon="lightbulb" color="#1CB2FE">
  When switching the granularity to monthly, you can view trends over time instead of an accumulated cost, which helps in detailed month-to-month analysis.
</Callout>

### Example Walkthrough

1. **Currency Conversion:** Change to US dollars for consistency.
2. **Time Frame:** Adjust the invoice period (e.g., November 20 to December 19) or select predefined periods like "last seven days" or "quarter."
3. **Filtering Virtual Machines:** Filter by the meter category "Virtual Machines," resulting in a focused view of spending (e.g., \$3.71 for VMs).
4. **Grouping:** Group by Resource Group to see consumption distribution.
5. **Graph Customization:** Choose between area graphs or column charts. For instance, selecting a stacked column chart shows consistent spending over several months and highlights changes when additional VMs are deployed.

Once you set up the desired filters and view, Azure Cost Management allows you to save these settings as a custom dashboard (e.g., "VM cost dashboard"). You can later share, update, or export these dashboards in PNG, Excel, or CSV formats for reporting purposes.

## Budgeting: Financial Guardrails

Budgets in Azure Cost Management help you set spending limits and forecast future costs. They serve as financial guardrails, alerting you when spending nears or exceeds budget thresholds. Azure Advisor further provides personalized recommendations to save money by suggesting cost-effective resource options and identifying underutilized services.

### Creating and Configuring a Budget

1. **Setting the Scope:** Adjust the scope based on your needs. For example, create a budget specifically for virtual machines within a subscription.
2. **Adding Filters:** Apply a filter by meter category to focus the budget on a particular resource type.
3. **Budget Details:** Assign a unique name (e.g., "VM-budget")—note that spaces are not allowed—and set a monthly reset period.
4. **Defining Budget Amount:** Input your budget amount (e.g., \$300) and observe the red line indicator that represents your set threshold.
5. **Alerts and Notifications:** Configure alert conditions to notify you when spending reaches a certain percentage (e.g., 80%). Use action groups to specify how alerts are delivered (e.g., text messages, emails, or phone calls).

<Callout icon="lightbulb" color="#1CB2FE">
  Azure Cost Management supports multiple alert thresholds, so you can notify different recipients as costs increase. Ensure you configure the alert recipients correctly to keep all key stakeholders informed.
</Callout>

Once created, your budget is visible within the cost analysis dashboard. You can view forecasted costs, historical spending, and make data-driven decisions to remain within your allocation.

## Exporting Cost Data

Azure Cost Management also provides the ability to export and download cost data, making it easy to perform further analysis or distribute reports to stakeholders.

### Export Options Include:

* **Recurring Exports:** Daily, weekly, or monthly exports that automatically dump data into an Azure storage account.
* **One-Time Export:** On-demand export of current cost data for immediate analysis.
* **Supported Formats:** Choose from PNG, Excel, or CSV formats to best suit your reporting needs.

Simply navigate to the "View all exports" section in the Azure portal to set up your preferred export schedule.

## Cost-Saving Strategies in Azure

Every penny saved in the cloud is a penny that can be reinvested in innovation and growth. Azure provides a suite of cost-saving measures designed to maximize efficiency while minimizing spending.

### Key Cost-Saving Options:

1. **Azure Reserved Instances (RI):**
   * Reserve capacity for one or three years for services like virtual machines running continuously, resulting in significant discounts compared to pay-as-you-go pricing.
2. **Azure Hybrid Benefit (AHB):**
   * Utilize your existing Windows Server and SQL Server licenses with Software Assurance on Azure to reduce licensing costs drastically.
3. **Credit-Based Subscriptions:**
   * For developers and IT professionals, subscriptions like Visual Studio Enterprise or those provided by the Microsoft Partner Network offer monthly Azure credits for testing and development purposes.
4. **Test Subscriptions:**
   * Enjoy lower rates on non-production environments for development and testing, though note that these subscriptions do not come with a Service Level Agreement (SLA).
5. **Regional Differences:**
   * Deploy resources in regions with lower costs to further optimize your budget. However, balance this against compliance and performance needs since some applications require data residency.

### Balancing Cost with Other Requirements

It is crucial to understand that aggressive cost optimization might come at the expense of performance, security, or compliance. For example, even if East US offers cheaper rates, a government entity may require data to be stored in a specific region for compliance reasons. Always ensure that cost savings do not compromise your organization's other critical pillars.

<Callout icon="triangle-alert" color="#FF6B6B">
  While using cost-saving measures, double-check that any optimization does not infringe on compliance or performance requirements. Adjust strategies carefully, ensuring optimal balance among cost efficiency, performance, and security.
</Callout>

## Pricing Calculator Example

To better understand potential savings, use the [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/). Here’s an example:

1. **Select Virtual Machines:** Choose a region (e.g., East US) and the operating system (e.g., Windows – Standard).
2. **Configuration:** Pick a VM size, such as D2v3 (2 vCPUs, 8 GB RAM).
3. **Savings Options:**
   * **Pay-As-You-Go:** Baseline cost, e.g., \$70.08.
   * **Monthly Reserved Instance:** Cost reduces to approximately \$41.75.
   * **Three-Year Reserved Instance:** Further reduction to around \$26.89.
   * **Azure Hybrid Benefit:** Apply your own license to eliminate licensing costs.

This example demonstrates how cost optimization strategies—like reserved instances and hybrid benefits—can lead to significant savings in your overall expenses.

## Conclusion

Azure Cost Management equips you with the financial clarity and control needed to efficiently manage cloud spending. By leveraging cost analysis, budgeting with alerts, data export, and various cost-saving strategies, you can ensure that every dollar invested in the cloud contributes to innovation and growth.

Next, learn how to configure Azure Policy to further streamline your cloud operations while maintaining control over your resources.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/eb5b895f-afd8-411f-9275-0c61b343fc46" />
</CardGroup>

---


## Lesson 8: Azure Policy

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Policy/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-Policy/page.md)

**Summary:** This article explains how to configure Azure Policies for governance and compliance across Azure resources.

# Azure Policy

> This article explains how to configure Azure Policies for governance and compliance across Azure resources.

Configuring Azure Policies.

Azure Policy is a governance tool

that helps you to set and enforce rules

across your Azure resources.

Policies can be used to define organizational standards

and identify non-compliant resources.

Just to give you an example,

if your organization requires all your resources

to be deployed in a certain region,

for example, in East US or within the United States,

then you can enforce a policy

and users will not be able to deploy it

in any other region,

for example, Southeast Asia or Western Europe.

This is where we primarily use policies for.

Now, when it comes to policy,

like RBAC, there are certain keywords

that you need to remember,

starting with definitions.

A policy definition, like RBAC definition,

outlines what the rule is

and what to do when a resource doesn't comply.

Example, a built-in policy could state

that all storage accounts must enforce HTTPS.

The JSON document would specify the conditions

for compliance and the actions to take

if the condition is not met.

So when we go to the portal,

I'll show you how the policy definition looks like.

So in a nutshell,

policy definition is a JSON document

used to define the policy and its effect.

Like RBAC, Azure has built-in policies

or you can write your own policies if required.

Second, scope.

Like RBAC, you must specify the scope

to enforce the policy.

Scope can be a management group,

subscription or a resource group.

Here we don't have the option

to enforce a policy to a resource.

The least we could do is a Resource Group.

So the scope is where your policy will be applied.

You can define it broadly,

like at the organizational level,

at the management group,

or narrowly, like to a very specific Resource Group.

So if you set the scope to a particular subscription,

the policy will only affect the resources

within that subscription.

So at this point,

we know what and where.

Next is the assignment.

In RBAC, we had VU as well.

Here it doesn't apply to VU.

This is an organizational standard.

So it's not specific to certain users or groups.

It is an organizational level policy that we are applying.

So definition, scope, and we have the assignment.

As the name implies,

assignment is the process of assigning a policy definition

to a scope.

Once you have created the policy,

you must assign it to a scope to be enforced.

Example, if you have a policy

that restricts the creation of public IP addresses,

once assigned to a Resource Group,

any attempt to create a public IP within that group

would be blocked or denied.

So once the assignment is done,

next is the compliance.

So after assigning the policy,

you can evaluate the compliance

to understand compliant and non-compliant resources.

So you might be wondering

if we are assigning the policy to block something,

how come we have noncompliant resources?

Policy cannot alter your existing resources.

For example, I don't want any resources

outside the United States,

but my users have already started deploying resources

in West Europe, Southeast Asia,

and other regions.

So when I apply this policy,

from that point onwards,

users will not be able to deploy the resources

outside the United States.

But whichever resources deployed before the assignment

will be marked as non-compliant resources

because they don't follow the organizational standards.

So this is why we have compliant

and non-compliant resources.

So if you have a policy enforcing

that all VMs must be tagged with an owner tag,

your compliance report will list all VMs

that either comply or fail to meet this requirement.

So if the VM is missing the tag,

that basically means that it's a non-compliant resource.

Administrators can use this compliance score

to understand how much they're aligned

to the organizational standards.

They can also create remediation policies

in certain Azure ADs, or it's called a remediation task.

They can run it and wherever the tag is missing,

they will be able to add the tags.

But keep in mind,

if you want to redeploy a resource

from one region to another to make it compliant,

that cannot be done using policy,

you have to do it manually.

But there are certain policies

where you will be able to create remediation tasks.

For example, something is missing

and you want to deploy it.

That can be achieved from the policy itself.

All right, I hope that's clear.

Now let's take a look at some of the use cases

so that you have a better understanding of policy.

So here I have a list of policies

that most organizations use.

Starting with required tags.

In Azure, we use tags for adding metadata to our resources.

This metadata can be used to organize our resources

and the tags that are applied at the resource level

can be used for billing purposes as well.

Now most of the time what users do is

they'll skip this tagging section

and they'll straight away deploy the resource.

And we want to avoid that.

So with the help of this required tags policy,

we will be able to enforce tags

that need to be added to the resources.

Another example is inherited tags.

By default, the tags that are applied on Resource Groups

or at the subscription level

will not get inherited to the underlying resources.

So unlike RBAC where you get inheritance everywhere,

policy, the tags don't get inherited.

So we need something to inherit those tags

from the subscription or Resource Group

to the underlying resources.

So with the help of this policy,

whenever you add a tag to the Resource Group,

the policy will automatically populate that tag

to the underlying resources.

Next is allowed location.

So many organizations have this data residency requirement

where they need to keep the data

within their region or the country,

like GDPR compliance.

So with the help of this policy,

they will be able to define the regions

where the users can deploy the resources.

And if a user tries to deploy outside the selected regions,

that will be blocked.

Allowed virtual machine SKUs.

This is mainly useful in development

and testing environments,

and also in certain environments

where budget is a constraint.

In Azure, we have a variety of virtual machines.

We have low-power machines

all the way to high-power machines.

So if you go with these high power machines,

obviously the cost is going to be high.

So let's say we don't want the users

to deploy certain expensive SKUs.

So what we can do is,

we can block those SKUs.

Consider these as VM sizes.

So we can block these sizes,

so the user will not be able to create

those virtual machines of that size.

Allowed resource group location.

The main difference between allowed locations

and allowed resource group location is,

allowed locations target resources.

Resource group can contain resources from multiple regions.

Resource group is where the metadata

of your resources gets stored.

If you want to enforce the location constraint

on your Resource Group,

you can apply this policy.

Allowed resource type.

In certain environments,

just like the allowed virtual machine SKUs,

administrators don't want users to deploy everything.

For example, if a user deploys ExpressRoute,

it's a very expensive service.

So in order to avoid these kinds of issues,

what we can do is,

let's say in this subscription,

we want to only deploy virtual machines,

app services and databases,

and virtual networks.

We don't want to deploy anything else.

So you can restrict that using this policy.

I hope that's clear.

Now we will go to Azure portal

and see how we can work with the policies.

So in Azure portal,

what I have to do is,

I have to search for Azure Policy,

and you'll see policy.

Here, you can go to definitions,

where you'll be able to see all the built-in policies

and also custom policies,

if you have created one.

Here you will see one more term,

which is called initiative.

So initiative is like chaining multiple policies.

Let's say you have 20 policies

that your organization requires,

and you don't want to assign this one by one.

This will be a management overhead,

and you will not be able to see the overall compliance.

In this case, what you can do is,

you can create an initiative,

where you can group multiple policies together

and assign it as a single unit to the scope.

So for this initiative,

you can see that there are seven policies inside that.

So once you open the initiative,

you'll see which are the seven policies

that are part of that initiative.

In short, policies are collected together

inside a module,

which we call an initiative,

so that we can assign it as a single unit

and calculate the compliance.

For certain regulatory standards,

such as PCI DSS, FedRAMP,

you will be able to find the initiative from here itself.

So PCI, you can see there is an initiative

with 277 policies.

So if I open this,

you'll be able to see the 277 policies,

and it will be easy for you to assign these,

rather than assigning these 277 policies one by one.

So this makes your work easier

if you have a set of policies

that you want to apply in a single shot,

you can go for initiative.

For now, let's just work on a single policy,

and I'll also show you how to set up an initiative.

Let's take the common example,

which is allowed locations.

So you can see the policy definition here.

It says,

of, as in all resources,

the field location is not in the parameters.

So parameter is something that we supply to the policy.

So let's say if I supply East US and West US,

if the location of all resources

is not in the selected resources,

or the field not equals global,

so if it's a global resource,

it will not have a region like Azure DNS,

Azure Front, or they don't have a region.

So either it should be in the allowed locations,

or it should be a global resource,

then only it will deploy.

Otherwise, what happens is,

it will take the effect of the policy.

We can see the effect of the policy right here,

which is denied.

Deny means that it will stop me from deploying it.

So what I'll do is I'll click on assign,

have to select the scope

where exactly I want to apply this policy.

I'll send it to POC2 subscription.

Optionally, I can choose a Resource Group

if I want a further granular scope.

Like I said earlier,

you will not be able to choose a resource

because the compliance maximum you can do is Resource Groups.

So I'll select that subscription.

Inside that subscription, if I want to exclude something,

I'll be able to add it here,

like a Resource Group,

I don't want to check compliance

or I don't want to enforce the policy for that.

I'll be able to add that exclusion here.

But in my case,

I want it to be everywhere inside the subscription.

I can give it a custom name.

For example, let me call it as a core cloud

allowed locations.

I can give a description,

list of allowed locations for deployment.

Whenever you apply a policy,

if you want to enforce it,

make sure that this is enabled.

Otherwise, it will be in an audit mode.

Whatever happens, it will be logged,

but it will not stop the user from doing anything.

So make sure it is enabled.

Assign by, you can give the name admin.

Click on Next.

Advance is not required for this particular policy.

There are certain policies

where you'll have resource selectors and overrides,

but in your case, it is not required.

Remember, we had a parameter in the policy definition,

which is called list of allowed locations.

This is what that parameter refers to.

So here, what I'll do is I will select East US

and also West US.

So for me, these are the allowed locations,

which are approved for deployment by my organization.

I'll click on review and create

because we don't require remediation.

Non-compliance message, you can always add it.

This will be the message that will be given to the users

if they try to deploy outside the list of allowed locations.

For example, I can give a message like,

you need to deploy in East US

or West US.

Review and create.

So once the policy is assigned,

it will take five to fifteen minutes to take effect.

We can go back to the policy definitions

and to assignments.

So both the scopes are selected here.

I'll just do a refresh

and you'll be able to see the assignment here.

The compliance has not started yet.

You will see it as not started or not registered.

Since we don't have any resources outside East US,

I think we only have one Virtual Network

in the subscription.

The evaluation was very quick.

And it says zero out of zero.

If I open this policy,

so I don't have any non-compliant resources

and compliant resources.

I think it is not completely evaluated as of now

because we still have a Virtual Network,

which is in our subscription.

So it is gonna take some time to complete the evaluation.

Meanwhile, we can always test this

by just going to a Resource Group

or try to create another Virtual Network.

Any resource.

I'll click on create.

This time I will give it as a demo vnet2

and I'll select somewhere else

like Central US, for example.

So during the validation,

the policy should ideally kick in.

If you see validation passed,

that means the policy is not in effect.

For us, it hasn't shown the message.

So we can try to create it

and see if we are able to initialize the deployment.

It says deploying,

that means the policy is still not in place.

Okay, it's not working as of now.

We can go back to the Virtual Networks,

try to add another.

Again, failed because somewhere it is stopping,

but the message is not clear anyways.

So I can give it another shot.

I'll put it to Central US.

So it's in the process of applying

that that's where you see the underlying API field.

It could be other reasons as well,

but for the time being,

we can assume that it's because the policy

is taking effect.

We can try to create again.

Ideally, we shouldn't reach this page,

but somehow the policy will take its own time

to apply like five to fifteen minutes

to take effect.

Okay, the deployment failed.

Now it says forbidden.

If I click on the error details,

it says resource demo VNet 2 was disallowed by policy.

If I take a look at the row error,

you can see that it is disallowed by policy reasons.

And you can see the non-compliance message,

which I passed to the policy assignment.

You need to deploy in East US or West US.

And if I scroll down,

I'll be able to see the name of the policy right here,

core cloud allowed locations.

And that's how policy works.

So it's still working,

but ideally we should get this message a little earlier.

Anyways, we can try with another resource,

say a Storage Account or something.

So let me try to look for Storage Accounts,

create a Storage Account.

I need to come up with a unique name.

So I'll just add some numbers to make it unique.

So here I'll select Central US.

There you go.

So immediately it said that policy enforcement value

does not meet requirements on resource.

The value Central US in this field was denied.

I can click on the policy details

and it will show me the policy.

You can see that the parameter name here,

list of allowed locations,

and the values are East US and West US.

This is how policy works.

In the next lesson,

we will see how we can work with Azure initiatives.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/d4ea929f-4a17-4446-a218-1fdab0b8627f" />
</CardGroup>

---


## Lesson 9: Configuring Initiatives

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Configuring-Initiatives/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Configuring-Initiatives/page.md)

**Summary:** This article explains how to configure initiatives in Azure Policy by combining multiple policy definitions into one cohesive initiative.

# Configuring Initiatives

> This article explains how to configure initiatives in Azure Policy by combining multiple policy definitions into one cohesive initiative.

This article explains how to configure initiatives in Azure Policy by combining multiple policy definitions into one cohesive initiative. We will walk you through the process of creating, assigning, and validating the effects of an initiative on your resource deployments.

The available individual policy definitions include:

* Required Tags
* Inherited Tags
* Allowed Virtual Machine SKUs
* Allowed Resource Group Locations
* Allowed Resource Types

All these policies can be combined under a single initiative.

<Frame>
  ![The image illustrates Azure Policy use cases, highlighting features like allowed resource types, resource group locations, virtual machine SKUs, required and inherited tags, and allowed locations. It includes a central graphic with colorful segments representing each use case.](https://kodekloud.com/kk-media/image/upload/v1752884537/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-policy-use-cases-illustration.jpg)
</Frame>

Below is an in-depth guide on how to create an initiative directly from the Azure portal.

## Creating an Initiative Definition

1. Open the Azure portal and navigate to **Policy Definitions**.
2. Choose to create a new initiative definition.
3. For the location, select IT (or your preferred location). Set the name as "KodeKloud Standard Policies" to align with your organizational requirements.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a new initiative definition. It includes fields for initiative location, name, description, and category selection.](https://kodekloud.com/kk-media/image/upload/v1752884538/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-portal-initiative-definition.jpg)
</Frame>

4. Under **Category**, you can create a new category (e.g., "KodeKloud") or use an existing one to group your policies.
5. Add the necessary policy definitions to the initiative:
   * **Require a tag and its value on Resource Groups**
   * **Allowed Virtual Machine SKUs**
   * **Allowed Resource Types**

<Frame>
  ![The image shows a Microsoft Azure portal interface for adding policy definitions to an initiative. It includes options for selecting policies like "Allowed virtual machine size SKUs" under the "Policies" tab.](https://kodekloud.com/kk-media/image/upload/v1752884540/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-portal-policy-definitions-initiative.jpg)
</Frame>

6. Optionally, include the **Inherit tags from Resource Groups** policy. For better organization, you can create groups (e.g., "tags group" for tag-related policies and "resource types" for policies related to allowed resource types).

7. Configure the initiative parameters next. Although the initiative itself may not require parameters, individual policies do. For example:

   * The tag policy requires a tag named "environment" with a fixed value of "POC".
   * The allowed VM sizes policy requires a set of approved sizes.
   * The allowed resource types policy requires allowed resources (e.g., Virtual Machines under Microsoft.Compute and Storage accounts under Microsoft.Storage).
   * The inherited tag policy ensures that resources inherit the environment tag from the resource group.

   For the parameter configuration:

   * Set the **environment** parameter value to "POC".
   * Limit the allowed virtual machine sizes to approved values such as **B1S** and **B1MS**.

<Frame>
  ![The image shows a Microsoft Azure portal screen for defining an initiative, specifically focusing on setting policy parameters such as tags and allowed virtual machine size SKUs. A dropdown menu is open for selecting virtual machine sizes.](https://kodekloud.com/kk-media/image/upload/v1752884541/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-portal-initiative-policy-settings.jpg)
</Frame>

8. For allowed resource types, specify:
   * Virtual Machines (under Microsoft.Compute)
   * Storage accounts (from Microsoft.Storage)

9. For the inherited tag policy, ensure that the resource inherits the "environment" tag from the resource group.

<Frame>
  ![The image shows a Microsoft Azure portal screen for defining policy parameters in an initiative. It lists various parameters with their types and values, such as tag names and allowed resource types.](https://kodekloud.com/kk-media/image/upload/v1752884543/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-portal-policy-parameters-initiative.jpg)
</Frame>

10. Click **Review and Create** to save the initiative definition. This step only creates the definition; it does not assign it.

<Frame>
  ![The image shows a Microsoft Azure portal screen displaying the "KodeKloud Standard Policies" initiative definition, which includes a list of policies with details such as reference ID, type, evaluation type, and default effect.](https://kodekloud.com/kk-media/image/upload/v1752884544/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-portal-kodekloud-policies-definition.jpg)
</Frame>

## Assigning the Initiative

1. Navigate to the initiative definitions and select the "KodeKloud Standard Policies" initiative.
2. Click **Assign Initiative**. The defined scope (in this case, IT) will be applied. If the target subscription (e.g., POC2) is not within IT, it will not be visible. To assign the initiative at a broader scope, consider creating it at the tenant root level.

<Frame>
  ![The image shows a Microsoft Azure portal page for assigning "KodeKloud Standard Policies," with fields for scope, exclusions, and basic settings.](https://kodekloud.com/kk-media/image/upload/v1752884545/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-portal-kodekloud-policies-2.jpg)
</Frame>

3. If needed, move subscriptions between management groups (for example, moving the POC2 subscription to IT) to ensure the correct scope.
4. Return to the policy definitions page to verify that the location is correctly set (e.g., 001 for IT). Then, assign the initiative to the desired subscription (e.g., POC2). You may also select a specific Resource Group; however, for demonstration purposes, leaving the Resource Group selection empty showcases how the policy (like the tag requirement) works at a broader level.

<Frame>
  ![The image shows a Microsoft Azure portal interface for assigning a policy initiative named "KodeKloud Standard Policies." It includes options for setting the scope, exclusions, and policy enforcement.](https://kodekloud.com/kk-media/image/upload/v1752884546/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-portal-kodekloud-policies-3.jpg)
</Frame>

5. Review the assignment and click **Create**. The assignment process will take a few moments, and a confirmation will appear once role assignments have succeeded. Note that the policy for inheriting tags requires a role (such as Tags Contributor) for the policy identity, which is why a role assignment is necessary.

<Frame>
  ![The image shows a Microsoft Azure portal screen where a user is creating an initiative assignment for "KodeKloud Standard Policies." The screen displays details like scope, policy definition, and enforcement status, with options to create, cancel, or navigate through the process.](https://kodekloud.com/kk-media/image/upload/v1752884547/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-portal-kodekloud-initiative.jpg)
</Frame>

## Testing and Validating Policies

After assigning the initiative, the following policies are enforced:

* Allowed Resource Types
* Require a Tag and Its Value on Resource Groups
* Inherit Tags from Resource Groups
* Allowed Virtual Machine Sizes

### Testing the Tag Policy

1. Navigate to **Resource Groups**.
2. Attempt to create a new resource group without a tag. For example, create a Resource Group named "azpolicy-check-rg" in the approved region (e.g., East US), leaving the tags section empty.
3. The creation process will fail with an error similar to:

<Callout icon="triangle-alert" color="#FF6B6B">
  ```json theme={null}
     {
       "error": {
         "code": "RequestDisallowedByPolicy",
         "target": "azpolicy-check-rg",
         "message": "Resource 'azpolicy-check-rg' was disallowed by policy. Policy identifiers: '[{\"policyAssignment\":{\"name\":\"Kodekloud Standard Policies\", ...",
         "additionalInfo": [
           {
             "type": "PolicyViolation",
             "info": {
               "evaluationDetails": {
                 "evaluatedExpressions": [
                   {
                     "result": "True",
                     "expressionkind": "Field",
                     "expressionType": "path",
                     "expressionValue": "Microsoft.Resources/subscriptions/resourceGroups",
                     "targetValue": "Microsoft.Resources/subscriptions/resourceGroups",
                     "message": "Equals"
                   }
                 ]
               }
             }
           }
         ]
       }
     }
  ```
</Callout>

The error indicates that the policy requires a tag named "environment" with the value "POC."

4. To fix the error, enter the tag "environment" with the value "POC." Using a different value, such as "prod," will result in a similar denial message:

<Callout icon="triangle-alert" color="#FF6B6B">
  ```json theme={null}
     {
       "policySetDefinitions": [
         "b54394e9e80747e89838764e"
       ],
       "additionalInfo": {
         "type": "PolicyViolation",
         "info": {
           "evaluationDetails": {
             "evaluatedExpressions": [
               {
                 "result": "True",
                 "expressionKind": "Field",
                 "expression": "type",
                 "path": "type",
                 "expressionValue": "Microsoft.Resources/subscriptions/resourceGroups",
                 "targetValue": "Microsoft.Resources/subscriptions/resourceGroups",
                 "operator": "Equals"
               },
               {
                 "result": "True",
                 "expressionKind": "Field",
                 "expression": "tags[Environment]",
                 "path": "tags[Environment]",
                 "targetValue": "PoC",
                 "operator": "NotEquals"
               }
             ]
           }
         }
       }
     }
  ```
</Callout>

5. After setting the correct tag value ("POC"), the resource group creation will succeed.

### Testing the Allowed Resource Types Policy

1. Try creating a Virtual Network. With the allowed resource types policy only permitting virtual machines and storage accounts, the Virtual Network creation should be blocked.
2. The resulting validation error will indicate that the resource type for virtual networks is not approved.

### Testing the Allowed Virtual Machine Sizes Policy

1. Create a new Virtual Machine in the Resource Group "Azure Policy Check RG" in the approved region (East US).
2. When selecting a VM size, the dropdown will restrict options to the approved sizes. Only **B1S** and **B1MS** will appear. Selecting any other size will not be allowed.

<Frame>
  ![The image shows a Microsoft Azure portal page for selecting a virtual machine (VM) size, displaying various VM options with details like type, vCPUs, RAM, and cost per month.](https://kodekloud.com/kk-media/image/upload/v1752884549/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-portal-vm-size-selection.jpg)
</Frame>

### Testing the Storage Account Deployment and Inherited Tag Policy

1. Create a Storage Account in the Resource Group "Azure Policy Check." Use a valid name, select East US, and choose a cost-effective option like LRS.
2. After deployment, verify that the storage account has automatically inherited the "environment: POC" tag from the Resource Group.

<Frame>
  ![The image shows the Microsoft Azure Policy Definitions page, listing various policy definitions with details such as name, definition location, policies, type, definition type, and category.](https://kodekloud.com/kk-media/image/upload/v1752884550/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-policy-definitions-page.jpg)
</Frame>

Once the policies are deployed, you can check the compliance state in your Azure Policy dashboard:

<Frame>
  ![The image shows a Microsoft Azure portal page displaying compliance states for "KodeKloud Standard Policies," listing policy names, effect types, compliance states, and resource counts.](https://kodekloud.com/kk-media/image/upload/v1752884551/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-Initiatives/azure-portal-kodekloud-compliance.jpg)
</Frame>

## Summary

In this article, we demonstrated how to group multiple Azure policies into a single initiative to enforce compliance across your resources. The initiative covers policies for:

* Enforcing a required tag and its value on resource groups.
* Restricting allowed resource types.
* Limiting allowed virtual machine sizes.
* Automatically inheriting tags from resource groups.

By assigning this initiative at the appropriate scope, you can ensure that all resources under that scope adhere to your organization's standards.

For further clarity on how Azure Policy differs from Role-Based Access Control (RBAC), refer to the detailed discussions in the official [Azure Policy Documentation](https://learn.microsoft.com/en-us/azure/governance/policy/).

Happy configuring!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/90e071df-9caa-4138-a4da-a51fee1e9132" />
</CardGroup>

---


## Lesson 10: Role Based Access Control

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Role-Based-Access-Control/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Role-Based-Access-Control/page.md)

**Summary:** This article explains Azure Role-Based Access Control (RBAC) for managing permissions and access to Azure resources effectively.

# Role Based Access Control

> This article explains Azure Role-Based Access Control (RBAC) for managing permissions and access to Azure resources effectively.

If you're looking to manage permissions

and access within your Azure environment,

RBAC will be your friend.

So what exactly is Azure RBAC?

It is a system that helps you to manage

who has access to your Azure resources,

what they can do with those resources,

and what areas they have access to.

It provides a fine-grained access management

to better enforce your organization's security policies.

Let's talk about some key terms that you hear often.

So whenever we think about Azure RBAC,

the first thing that comes to your mind will be who.

So who refers to a security principal,

as in who will get the access.

So any identity which is requesting for access.

It could be a user, group, service principal,

or a managed identity.

Second is what.

What refers to what permissions you want to give

to the security principal.

So the what is defined using something called

role definition, which defines a set of operations

that a particular role can perform.

This is written in JSON format.

Lastly, where.

Where exactly do you want to give the role

for the user or the security principal.

That's what we call Azure scope.

This is a limit of access which defines a boundary,

for example, to a Resource Group,

to a virtual machine, to a database.

All this is considered as a scope.

So if we combine this together,

we will get something called a role assignment.

When we attach a role definition to a service principal

at a particular scope, then it becomes a role assignment.

Maximum you can have up to 2000 role assignments

in each subscription.

Always follow the principle of least privilege

whenever you're assigning the permissions.

Also, you can make use of privileged identity management

when you're working with Azure RBAC.

So we don't want to give permanent direct access

to our resources.

Instead, the access will be provided

through Privileged Identity Management.

In Azure Active Directory,

we studied about different security principles, right?

How a user works, how groups work,

service principal, et cetera.

And we already know what the scope is.

So that's why we learned about hierarchy.

You have management groups, subscriptions,

resource groups, resources.

Something that is missing is a role definition.

So let's just double click on that

and understand more about this.

So in Azure, you have built-in roles.

These are the roles that are supplied

with Azure out of the box,

like Owner, Reader, Contributor, et cetera.

And you also have very specific roles

limited to certain services

like Virtual Machine Contributor,

Storage Blob Contributor, et cetera.

Also, you can come up with custom roles.

It's not necessary that you have to go

with the built-in roles.

Let's say your organization requires

a very fine-tuned role for your users,

then you can create custom roles.

Basically, this is how a role definition will look like.

And this is the role definition for the Contributor role.

You can see that the name is Contributor.

There will be a unique Object ID that is assigned.

Is custom is set to false because it's not a custom role.

It's a built-in role from Azure.

And it has a description where it says

grants full access to manage all resources,

but does not allow assigning roles in Azure RBAC.

In actions, you can see that there is an asterisk

that means everything is allowed.

Not actions, you have certain things

like Microsoft.Authorization slash delete,

Microsoft.Authorization write,

elevate access, et cetera.

So basically, this is the contributor role definition

where the contributor will be able to do everything,

but the user will not be able to assign roles

in Azure RBAC.

That's why you see that authorization provider.

Also, there are some limitations on the blueprint.

And also, share image galleries.

That's why you have Microsoft.Compute

slash gallery slash share slash action there.

Data actions, no data actions usually come

into picture if you're dealing with the storage role

on what permissions the user should have on the data plane.

And finally, assignable scopes,

which all scopes you can assign.

The slash denotes root.

That means anything under the root can use this role.

So this is how the role definition looks like.

Now, let's just see what are the built-in roles

available in Azure.

Then we will go to Azure portal

and see how we can assign the roles.

So built-in roles are roles offered by Azure,

which we can assign to users,

groups, service principals, and managed identities.

Here are the fundamental roles that you need to be aware of.

First one is owner.

This has full access to all resources

and can delegate access to other users.

For example, if I am the owner of a resource,

say a virtual machine,

I will be able to make other people owners,

contributors, readers, or any other role that I want.

Basically, I will be able to delegate access to other users.

Next is Contributor.

We have already seen the definition of contributor

in the previous slide.

Contributor can create and manage all types of resources,

but cannot grant access to others.

If I'm a contributor,

I will not be able to make another person a contributor

or an owner.

If you need to get access to something,

you should get in touch with the owner.

Next is the Reader.

As the name implies,

Reader has read access to all resources,

no permission to make changes to the resources.

Also, the reader will not be able to see

sensitive information like connection strings,

account keys, API keys, etc.

That will be only visible to owner and contributor.

Last but not least, we have User Access Administrator.

This user has access to Azure resources.

To a certain level only.

That means the user can provide access to other users.

It's more like a delegation role.

If I'm a User Access Administrator,

I'll be able to give access to other permissions,

but I will not be able to manage the resources.

If I'm able to manage the resources,

that essentially becomes an owner.

So User Access Administrator is more like an owner

without the permission to manage the resources.

We already covered scope in understanding hierarchy,

but I want to bring this topic again

so that you understand this clearly

and you don't forget this.

So at the top, we have the management group,

then the subscription, resource group,

and finally resources.

So if you assign a role at the management group,

that will be inherited to the subscription,

resource group, and resources.

Similarly, if you assign a role at the subscription level,

that will be inherited to the Resource Group and resources.

Likewise, if you apply at the Resource Group level,

that will be inherited to the resources.

This is how the scope works.

So don't forget the scope

because this has a lot of importance in policies

as well as in RBAC.

I hope that's clear.

Now we will go to Azure portal

and see how we can assign these permissions

and how we can set up a custom role if required.

So we are in Azure portal.

Now what I will do is I'll simply go to this Resource Group.

Unfortunately, the subscription is disabled,

so we'll not be able to make any changes.

So what I'll do is I'll create a new resource group here.

I'll call it as AC Demo RBAC,

and I'll place it in East Europe.

I'm not gonna add any resources,

so I'll just simply use the name of the Resource Group.

Create this resource group.

So the resource group is created.

If I just refresh this,

or I can go to the resource group here.

On every scope where you can assign RBAC,

you will see this access control IAM blade.

All you have to do is just click on that

and you will be able to check access and view your access.

You will be able to check access for other users as well,

but you can go to role assignments.

This is where you'll be able to see all the roles.

For example, my account is an Owner,

but I don't have the Owner role

at this Resource Group level,

but I have a role at the Subscription level

and it is inherited.

So remember the hierarchy.

If you give the permission at the very top,

like at the management group,

that will get inherited to all the underlying resources,

including subscriptions, Resource Groups,

and your Azure resources.

So RBAC goes with inheritance.

Similarly, if I apply RBAC at the Resource Group level,

all the resources inside that Resource Group

will get that permission.

So if I want to add a role,

I'll click on Add Role Assignment.

I have to choose a role here.

You can see there are a lot of built-in roles available

specific to every resource.

For example, you can see there is an ACR delete,

ACR image signer.

This is for Azure Container Registry.

There are some roles for Attestation Contributor,

Attestation Reader.

This is for attestation purposes.

You have an automation job, automation contributor.

This is for automation account.

So for every resource,

there will be certain roles available

because we don't want to give owner

or contributor to everyone.

We follow the principle of least privilege.

So if someone just needs to create and manage jobs

in Azure Runbooks in the automation account,

this is the role I'll be giving

instead of giving a privileged role.

So this view gives you job function role,

which basically targets certain jobs,

but you have privileged roles as well,

like Owner, Contributor, et cetera.

So if I want to give a Reader role,

for example, I'll click on Reader,

click on Next.

This is where I'll select members,

the users that I want to give the role to.

So in the first place,

this is the role definition,

what exactly we need to give.

And in the next page,

this is where we set rules.

And we already decided where,

because where is a scope

and we know it is going to be the Resource Group.

So I'll just select users

that I want to give read access to

and I'll select Next,

Review and Assign.

And you can see that

these users have been added as a reader here.

And the scope is this resource.

Whenever you see this resource,

you have to look at here

to understand what this resource is.

Now let's say inside this Resource Group,

what I'll do is I'll create a Virtual Network.

For example,

so I'll choose that subscription

and the Resource Group.

I'll say demo VNet,

review and create.

I will not look in the address space

and all which is not required at this point.

So I'll just skip that

and I'll create this virtual network.

So I'll click on create

and the virtual network will be created right now.

The deployment is in progress.

Okay, the resource has been created.

If I click on go to resource

that will take me to the Virtual Network.

In the virtual network also,

you will see this access control IAM

because this resource or this level supports Azure RBAC.

So I'll click on that,

I'll take a look at the role assignments.

Obviously, my name will be there

because it is inherited from the subscription.

You can see other users,

which we added as readers

and you can see the scope.

This is coming from the Resource Group.

So this is not assigned directly to the resource.

It is assigned to the Resource Group

and got inherited.

Similarly, I can go to Management Groups as well.

For example, IT here,

I can go to access control IAM.

I'll be able to add a role assignment here.

So it says I'm the owner for this one.

and I have given this permission

at this resource level, I have the permission.

I can add more users, owners, readers,

whatever role I want here

and all subscriptions under IT

will get that permission inherited.

This is how RBAC works.

Let's say you want to come up with a custom role.

You're not happy with the built-in roles.

So you can click on add

and you'll see add custom role.

Earlier, a couple of years back,

we used to write JSON for this

and create this from PowerShell or CLI.

Now the portal supports creation of custom roles.

Now I can give a name.

I'll add CR just for me to understand

that it's a custom role.

I'll say this is VM App Operator,

something like that.

I can give a description.

If I need, it will be very helpful

for someone who wants to assign this role.

I can clone an existing role, a built-in role.

I can start from scratch or I can start from JSON.

I'll use start from scratch

because we get the option

to choose the permissions from here.

I can click on add permissions.

You'll see all services here.

For example, if I want to see

Virtual Machine related permissions,

you can see it right here.

Or in case you're not able to find it,

you can search for Microsoft Docs Compute.

Yeah, this is a virtual machine.

So you'll be able to see all the permissions

that are available with virtual machines.

For example, let me randomly pick some permissions.

For example, right here,

read latest patch assessment operation details,

get virtual machine log definitions,

get virtual machine run command,

delete virtual machine run command.

You can add these permissions.

So the custom role will only have these permissions

and the user will be able to only accomplish

these actions.

I'll click on next.

I'll click on create.

And this custom role will be created.

As you can see, it may take a few minutes

to display this role everywhere,

but we can give it a shot.

This time I'll go for add role assignment.

In job function, what you can do is

you can filter type to a custom role

and you can see your CRVM operator

custom role available here.

I can click on that, click on next,

select members.

I can add people here or groups here.

For example, we have an HR group.

That group also can be added here.

I'll click on select,

review and assign,

review and assign.

And you can see that CRM app operator

has been added here.

And all these users have permission

at the management group level.

That means they have access to everything

under the management group.

Now that you know what Azure RBAC is,

we also have Microsoft Entra ID roles.

And for beginners, this is quite confusing.

So let's understand the differences

between Azure RBAC and Microsoft Entra ID roles.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/9e0ebfef-0121-402d-bc21-c0c2605ade1e" />
</CardGroup>

---


## Lesson 11: Azure RBAC vs Microsoft Entra ID Roles

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-RBAC-vs-Microsoft-Entra-ID-Roles/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Governance-and-Compliance/Azure-RBAC-vs-Microsoft-Entra-ID-Roles/page.md)

**Summary:** This article compares Azure RBAC and Microsoft Entra ID roles for effective access management in Azure environments.

# Azure RBAC vs Microsoft Entra ID Roles

> This article compares Azure RBAC and Microsoft Entra ID roles for effective access management in Azure environments.

In this article, we compare two essential permission management tools in the Azure ecosystem: Azure RBAC and Microsoft Entra ID roles. Understanding the differences between these tools is crucial for efficiently managing access within your Azure environment.

## Overview

Access control is a key component of any secure Azure deployment. Both Azure RBAC and Microsoft Entra ID roles play unique roles in this process:

* **Azure RBAC** is designed to manage access to Azure resources such as virtual machines, databases, resource groups, subscriptions, and management groups.
* **Microsoft Entra ID roles** (formerly known as Azure AD roles) focus on governing access within Microsoft Entra ID. These roles provide control over features like privileged identity management, users, groups, and service principals.

Using this guide, you will learn about the functionalities, scopes, and best practices associated with each tool to help you determine when and how to implement them.

## Scope and Functionality

### Azure RBAC

Azure RBAC (Role-Based Access Control) allows you to define permissions precisely across various scopes in your Azure environment. You can assign roles at multiple levels, including:

* Entire subscriptions
* Management groups
* Individual resources, such as virtual machines or storage accounts

This flexibility ensures granular control over resource access.

### Microsoft Entra ID Roles

Microsoft Entra ID roles operate exclusively at the tenant level. When you assign a role in Microsoft Entra ID, the permissions apply across the entire tenant. Some common roles include:

* Global Administrator
* Billing Administrator
* Global Reader

These roles are intended to provide broad access and management capabilities for the Microsoft Entra ID environment.

## Role Assignment and Management Tools

### Azure RBAC Role Assignments

Azure RBAC roles can be assigned using various tools and interfaces:

* Azure Portal
* PowerShell scripting
* Azure CLI
* ARM templates for automated deployments
* REST APIs

These multiple interfaces make it easy to integrate RBAC into your existing workflows.

### Microsoft Entra ID Role Management

You can manage Microsoft Entra ID roles through several platforms:

* Azure Portal (via Microsoft Entra ID)
* M365 Admin Portal
* Microsoft Graph API and the optional Graph PowerShell module

#### Practical Demonstration in the Azure Portal

To assign Microsoft Entra ID roles in the Azure Portal, follow these steps:

1. Navigate to **Microsoft Entra ID**.
2. Select **Roles and Administrators** to view available roles for services like Exchange, Teams, and SharePoint.
3. To assign a role:
   * Choose **Users** and select a specific user (for example, Abigail).
   * Click on **Assigned Roles** and then **Add Assignment**.
   * Select the appropriate role from the list. Note that roles may include eligible or expired options, which are managed through Privileged Identity Management.

<Callout icon="lightbulb" color="#1CB2FE">
  The steps provided in this demonstration are representative and may vary with updates to the Azure Portal interface.
</Callout>

This demonstration illustrates that while both Azure RBAC and Microsoft Entra ID roles help manage permissions, they are designed for different aspects of access control—resource-level versus tenant-level management.

## Hierarchical Structure and Integration

Every Azure subscription is linked to a Microsoft Entra ID tenant, creating a hierarchy that harmonizes these two permission systems:

1. **Microsoft Entra ID Tenant (Root):**\
   All Entra roles reside here (e.g., Global Administrator, Application Administrator, Developer, Billing Administrator). A Global Administrator can enable elevated access across both Microsoft Entra ID features and the associated subscriptions without separate Azure RBAC assignments.

2. **Root Management Group:**\
   Governed by Azure RBAC with roles such as Owner, Contributor, or Reader. This level can also include nested management groups.

3. **Subscriptions, Resource Groups, and Resources:**\
   These follow Azure RBAC rules. For instance, even if a user is assigned as a Billing Administrator at the tenant level, they may not have direct access to subscription-specific billing information without the corresponding RBAC role at that scope.

This integrated approach ensures that high-level administrative tasks are managed via Microsoft Entra ID roles while detailed resource access is handled by Azure RBAC.

<Frame>
  ![The image compares Azure RBAC roles with Microsoft Entra ID roles, illustrating their hierarchy and access levels within a management structure. It shows the relationship between global admin roles and Azure RBAC roles across different management groups and resources.](https://kodekloud.com/kk-media/image/upload/v1752884528/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-RBAC-vs-Microsoft-Entra-ID-Roles/azure-rbac-enra-id-roles-comparison.jpg)
</Frame>

## Conclusion

In summary, this article has highlighted the key differences between Azure RBAC and Microsoft Entra ID roles. By distinguishing between tenant-level administration and resource-level control, you can implement a robust permission strategy that secures your entire Azure ecosystem.

We hope this guide has enhanced your understanding of access control in Azure. Happy managing, and see you in the next module!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/df99187b-f512-443a-a64b-93af9d73c5bc/lesson/3eef02ac-df4d-4e8e-9c1d-5a45fbb611dc" />
</CardGroup>

---
