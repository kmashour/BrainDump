# [Updated] AZ-104: Microsoft Azure Administrator - Full Course Transcript

> Source: KodeKloud Notes (https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Course-Introduction/page)

> Ingestion Date: 2026-09-26

---


# Section 01: Introduction

---


## Lesson 1: Course Introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Course-Introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Course-Introduction/page.md)

**Summary:** This course covers core concepts and functionalities essential for mastering Microsoft Azure Administration, including managing identities, resources, and security in the cloud.

# Course Introduction

> This course covers core concepts and functionalities essential for mastering Microsoft Azure Administration, including managing identities, resources, and security in the cloud.

Welcome to this comprehensive course on Microsoft Azure Administration. I'm Ravindra Skaria, and I'm excited to guide you through the core concepts and functionalities essential for mastering Azure Administration.

Before we dive in, let's review what this course entails and the prerequisites you'll need.

## Course Overview and Prerequisites

To succeed in this exam and course, you should have expertise in implementing, managing, and monitoring an organization's Microsoft Azure environment. A foundational knowledge equivalent to the [AZ900: Microsoft Azure Fundamentals](https://learn.kodekloud.com/user/courses/az900-microsoft-azure-fundamentals) course is recommended.

As an Azure Administrator, your role is critical in ensuring that your organization operates securely and efficiently in the cloud. By the end of this training, you will be proficient in:

* Managing Azure identities and governance
* Deploying and managing Azure compute resources
* Implementing and managing Azure storage solutions
* Configuring and managing Azure virtual networking
* Securing identities, data, and applications
* Monitoring and maintaining Azure resources

<Callout icon="lightbulb" color="#1CB2FE">
  By completing this course, you will gain the necessary skills to implement and manage advanced Azure solutions tailored to your organization’s needs.
</Callout>

## Learning Materials

This course is designed with a blend of theoretical knowledge and hands-on demonstrations. The practical examples help bridge the gap between theory and real-world application.

In addition to detailed explanations, you will encounter quizzes and strategic reinforcement questions throughout the course. These checkpoints ensure you grasp the material thoroughly and enable you to monitor your progress effectively.

Your active participation is vital. Feel free to ask questions, engage with your peers, and join our community forum to share insights and further expand your Azure expertise.

Without further ado, let's embark on this exciting Azure Administration journey. Let's get started!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/edb6b82d-2942-45b9-89e9-33fbe75528c2/lesson/4bf18f91-9693-4d2e-a953-53b017c39b89" />
</CardGroup>

---


## Lesson 2: Certification Details

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Certification-Details/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Certification-Details/page.md)

**Summary:** Overview of AZ-104 exam objectives and key study topics for managing Azure identities, governance, storage, compute, networking, monitoring, backups, and troubleshooting

# Certification Details

> Overview of AZ-104 exam objectives and key study topics for managing Azure identities, governance, storage, compute, networking, monitoring, backups, and troubleshooting

This lesson summarizes the AZ-104: Microsoft Azure Administrator exam objectives and shows the core topics to study. The AZ-104 tests skills required to manage Azure identities, governance, storage, compute, networking, and monitoring.

There are five main domains in the exam:

* Manage identities and governance
* Implement and manage storage
* Deploy and manage Azure compute resources
* Implement and maintain virtual networking
* Monitor and maintain Azure resources

Below is a quick overview followed by a deeper look at each domain and recommended topics to study.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Certification-Details/az-104-certification-topics.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=23fb0debe00848bb650074ebc8722be0" alt="A presentation slide titled &#x22;AZ-104 Certification: Topics.&#x22; It shows five colored boxes listing exam domains: manage identities and governance; implement and manage storage; deploy and manage Azure compute resources; implement and maintain virtual networking; and monitor and maintain Azure resources." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Certification-Details/az-104-certification-topics.jpg" />
</Frame>

Summary table of domains and focus areas

| Domain                                    | Exam weight | Core topics to study                                                                                                                    |
| ----------------------------------------- | ----------: | --------------------------------------------------------------------------------------------------------------------------------------- |
| Manage identities and governance          |      20–25% | Microsoft Entra ID (Azure AD), RBAC, policies, subscriptions, management groups, ARM templates, CLI/PowerShell resource management      |
| Implement and manage storage              |      15–20% | Storage account types, replication, access control, blob/files/queues/tables, lifecycle management                                      |
| Deploy and manage compute resources       |      20–25% | Azure VMs (provisioning, sizing, extensions), PaaS compute (App Service, Container Instances, Container Apps), basic container concepts |
| Implement and maintain virtual networking |      15–20% | vNets, subnets, NSGs, peering, VPN Gateway, load balancers, UDRs, routing                                                               |
| Monitor and maintain resources            |      10–15% | Azure Backup, Site Recovery, Azure Monitor, Log Analytics, diagnostic settings, alerts and metrics                                      |

Manage Azure Identities and Governance (20–25%)

This domain tests identity management, governance, and resource administration. Key study items:

* Microsoft Entra ID (formerly Azure AD): users, groups, service principals, managed identities.
* Authentication and conditional access basics.
* Role-Based Access Control (RBAC): built-in & custom roles, assignments and effective permissions.
* Governance constructs: management groups, subscriptions, resource groups, Azure Policy (definition/assignment).
* Resource deployment and automation: ARM templates, Bicep (if applicable), Azure CLI, and Azure PowerShell for provisioning and role assignments.
* Troubleshooting identity and access issues.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Certification-Details/az-104-manage-identities-governance.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=0ba4c3d5b7b9983e1e7b8d4e026c6184" alt="A slide titled &#x22;AZ-104 Certification: Topics&#x22; highlighting &#x22;Manage Azure identities and governance (20–25%)&#x22; with subitems (Administer Identity, Administer Governance and Compliance, Administer Azure Resources). To the right are colored boxes listing other domains: Implement and manage storage; Deploy and manage Azure compute resources; Implement and maintain virtual networking; Monitor and maintain Azure resources." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Certification-Details/az-104-manage-identities-governance.jpg" />
</Frame>

Implement and Manage Storage (15–20%)

Focus on managing Azure Storage services:

* Storage account types and tiers (Standard/Premium, hot/cool/archive).
* Data replication options (LRS, GRS, RA-GRS, ZRS) and choosing based on availability and recovery needs.
* Access control: shared keys, SAS tokens, Azure AD integration.
* Data management: lifecycle policies, soft delete, immutable blobs, file shares.

Deploy and Manage Azure Compute Resources (20–25%)

Understand compute options and administration:

* Virtual Machines: deployment, sizes, extensions (e.g., custom script, VM Agent), managed disks, availability sets/zones, backups and updates.
* PaaS compute: App Service plans and app deployment, Azure Container Instances, Container Apps and how they differ from AKS.
* Containers and orchestration: basic container concepts and when to choose PaaS vs container services.

Note: Azure Kubernetes Service (AKS) is a deeper, specialized topic. It is useful to understand at a high level but is not a primary focus of the AZ-104 objectives. For a dedicated AKS course, see the linked resource below.

Implement and Maintain Virtual Networking (15–20%)

This domain covers network design, connectivity, and traffic management:

* Virtual networks, subnets, and network security groups (NSGs).
* Private connectivity: Virtual Network Peering and VPN Gateway for inter-site connectivity.
* Traffic management: Azure Load Balancer, Application Gateway (high level), route tables, and user-defined routes (UDRs).
* Network troubleshooting basics and service endpoints/private endpoints.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Certification-Details/az-104-implement-manage-virtual-networking.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=8b50e59ec6f39c28d47dee49e5175c4e" alt="A slide titled &#x22;AZ-104 Certification: Topics&#x22; highlighting the central topic &#x22;Implement and manage virtual networking (15–20%)&#x22; with subitems for administering virtual networking, intersite connectivity, and network traffic. Four colored boxes on the right list other domains: manage Azure identities and governance, implement and manage storage, deploy/manage Azure compute resources, and monitor/maintain Azure resources." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Certification-Details/az-104-implement-manage-virtual-networking.jpg" />
</Frame>

Monitor and Maintain Azure Resources (10–15%)

This domain focuses on monitoring, backup, and recovery:

* Azure Backup: backup policies, recovery points, and restore operations.
* Azure Site Recovery (ASR) basics for disaster recovery scenarios.
* Azure Monitor: collecting metrics, logs, and configuring diagnostic settings.
* Log Analytics and Kusto Query Language (KQL) basics for querying logs.
* Setting up alerts (metric and log alerts) and automated actions.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Certification-Details/az-104-monitor-maintain-azure-resources.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=922d2c72ba97116489302fe2a8d8bde9" alt="A presentation slide titled &#x22;AZ-104 Certification: Topics&#x22; highlighting &#x22;Monitor and maintain Azure resources (10–15%)&#x22; with subitems &#x22;Administer Data Protection&#x22; and &#x22;Administer Monitoring.&#x22; To the right are four colored boxes listing other domains: Manage Azure identities and governance; Implement and manage storage; Deploy and manage Azure compute resources; and Implement and maintain virtual networking." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Introduction/Certification-Details/az-104-monitor-maintain-azure-resources.jpg" />
</Frame>

Service name changes and official resources

* Microsoft Entra ID is the new name for Azure AD. This is a rebranding; functionality remains consistent, though some product pages and learning content may reference the new name.
* Always verify current exam objectives and platform terminology on official Microsoft pages.

<Callout icon="lightbulb" color="#1CB2FE">
  For up-to-date exam objectives and guided learning paths, rely on official sources such as Microsoft Learn and the Azure documentation. Combine hands-on practice (deploying VMs, setting up RBAC, configuring networks, and using Azure Monitor) with study modules to reinforce practical skills.
</Callout>

Links and references

* [Microsoft Learn](https://learn.microsoft.com/learn/) — official learning paths and modules for AZ-104.
* [Azure documentation](https://learn.microsoft.com/azure/) — product docs, how-tos, and architecture guidance.
* [Azure Kubernetes Service (AKS) course example](https://learn.kodekloud.com/user/courses/azure-kubernetes-service) — additional AKS-focused content if you want to dive deeper into container orchestration.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/edb6b82d-2942-45b9-89e9-33fbe75528c2/lesson/71f11178-1751-4192-9bd1-e82c83f18146" />
</CardGroup>

---


# Section 02: Administer Identity

---


## Lesson 1: Module Introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Module-Introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Module-Introduction/page.md)

**Summary:** This article outlines the learning objectives and provides an overview of identity management in Azure, focusing on Microsoft Entra ID and user account configuration.

# Module Introduction

> This article outlines the learning objectives and provides an overview of identity management in Azure, focusing on Microsoft Entra ID and user account configuration.

Administering identity is crucial for managing Azure resources because it involves handling user identities, permissions, groups, devices, and access within a cloud environment. This ensures that the right individuals have appropriate access to technology resources. In this article, we outline the learning objectives of this module and provide an overview of identity management in Azure.

## Module Learning Objectives

This module has two primary objectives:

### 1. Configure Microsoft Entra ID

In this section, you will learn to set up and manage Microsoft Entra ID—formerly known as Azure Active Directory (Azure AD)—which serves as the core component of Azure Identity Services. The following subsections cover essential topics:

* **Introduction to Microsoft Entra ID:**\
  Understand the fundamentals of Microsoft Entra ID and its importance within Azure Identity Services.

* **Key Concepts:**\
  Explore vital concepts such as identity types, authentication methods, and access management practices that define Microsoft Entra ID.

* **Microsoft Entra ID Editions:**\
  Get an overview of the various editions and service levels available, allowing you to select the edition that best meets your organization’s requirements.

* **Configuration of Device Identities:**\
  Learn techniques for configuring device identities, ensuring secure management of devices alongside user identities within Azure.

<Frame>
  ![The image lists learning objectives related to configuring Microsoft Entra ID, including an introduction, concepts, editions, and configuring device identities.](https://kodekloud.com/kk-media/image/upload/v1752884594/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Module-Introduction/microsoft-entra-id-learning-objectives.jpg)
</Frame>

### 2. Configure User and Group Accounts

This objective focuses on managing user and group accounts effectively. You will cover these key areas:

* **User Accounts:**\
  Discover how to create and manage individual user accounts in Azure, an essential aspect of controlling access rights.

* **Bulk Operations:**\
  Learn strategies for large-scale administration of user accounts, including bulk creation, modification, and deletion.

* **Group Accounts:**\
  Understand how to manage group accounts to streamline permissions and simplify the administration process for users with shared access needs.

* **Self-Service Password Reset (SSPR):**\
  Enable SSPR to allow users to reset their passwords independently, thereby enhancing overall security and operational efficiency.

* **Multitenant Environments:**\
  Analyze the challenges and best practices associated with managing identities in multitenant environments—key for organizations overseeing multiple Azure services or catering to various customers.

<Frame>
  ![The image lists learning objectives related to configuring user and group accounts, including user accounts, bulk operations, group accounts, self-service password reset, and multi-tenant environments. It features a gradient background with the title "Learning Objectives" on the left.](https://kodekloud.com/kk-media/image/upload/v1752884595/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Module-Introduction/learning-objectives-user-group-accounts.jpg)
</Frame>

## Overview of Managing Identity in Azure

This section provides a high-level view of identity management in Azure, emphasizing how Microsoft Entra ID integrates various identity types and services.

Microsoft Entra ID acts as a central hub that extends your identity capabilities to the cloud by enabling features such as single sign-on, multi-factor authentication, and conditional access policies. Although on-premises identity synchronization is not covered in this article, note that it is comprehensively addressed in the [Microsoft Azure Security Technologies (AZ-500)](https://learn.kodekloud.com/user/courses/microsoft-azure-security-technologies-az-500) course.

<Callout icon="lightbulb" color="#1CB2FE">
  Identity synchronization using tools like Entra ID Connect bridges on-premises directories with Azure's cloud-based identity service.
</Callout>

The following diagram summarizes the overall architecture:

* **On-Premises Identities:**\
  Traditional user accounts within an organization's Active Directory, synchronized with Microsoft Entra ID via tools such as Entra ID Connect, ensure smooth integration between on-premises systems and Azure.

* **B2B Scenario:**\
  Demonstrates how business-to-business (B2B) collaboration is enabled, allowing guest users from partner companies to securely access resources while maintaining robust security.

* **External Identity Providers:**\
  Shows the support for integrating external identity providers without the need to add those users to your primary directory.

* **Users and Groups in Microsoft Entra ID:**\
  Outlines how individual user accounts—with their associated roles and permissions—and groups help streamline permission management at scale.

<Frame>
  ![The image is a flowchart titled "Administer Identity – Overview," illustrating the relationship between on-premises identities, Microsoft Entra ID, external identity providers, users, and groups, including details on licenses, administrative units, and group types.](https://kodekloud.com/kk-media/image/upload/v1752884596/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Module-Introduction/administer-identity-overview-flowchart.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  * On-premises identities are synchronized with Microsoft Entra ID using tools like Entra ID Connect.
  * The diagram highlights a secure B2B collaboration scenario and the integration with external identity providers.
  * It also emphasizes clearly defined roles and permissions for users and groups in the cloud.
</Callout>

As you progress through this article, you will gain detailed insights into Microsoft Entra ID and learn how to integrate B2B connections while effectively managing user, group, and device identities in Azure.

Let’s begin with the introduction to Microsoft Entra ID.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/cda68ce1-d25f-4c63-9081-6ff77f6069eb" />
</CardGroup>

---


## Lesson 2: Introduction to Microsoft Entra ID

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Introduction-to-Microsoft-Entra-ID/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Introduction-to-Microsoft-Entra-ID/page.md)

**Summary:** Microsoft Entra ID is a security service that provides seamless access to Microsoft Cloud services and enhances identity management, security, and productivity.

# Introduction to Microsoft Entra ID

> Microsoft Entra ID is a security service that provides seamless access to Microsoft Cloud services and enhances identity management, security, and productivity.

Microsoft Entra ID (formerly known as Azure Active Directory) is a security cornerstone that provides seamless access to a wide array of Microsoft Cloud services—including Azure, Office 365, and many other SaaS applications. Imagine accessing your company resources, emails, calendars, documents, and more—all with a single sign-on. This seamless integration is possible because Microsoft Entra ID acts as an invisible gatekeeper, verifying your identity and granting you secure access to essential tools and services.

## Overview

As a cloud-based service, Microsoft Entra ID offers universal accessibility and scalability. It not only manages user identities but also streamlines security and productivity with features such as:

* **Multi-Factor Authentication:** Enhances security through an additional layer of verification.
* **Conditional Access:** Implements adaptive security policies based on user location, device status, and risk factors.
* **Group and Device Management:** Efficiently administers user groups and connected devices.
* **Hybrid Identity Support:** Bridges on-premises environments with the cloud for seamless identity management.

Moreover, Microsoft Entra ID supports secure access to Azure services as well as numerous SaaS solutions including Microsoft 365, Dropbox, Concur, and Salesforce.

<Callout icon="lightbulb" color="#1CB2FE">
  Microsoft Entra ID empowers users with self-service capabilities. They can securely reset or change their passwords without requiring direct IT intervention, significantly reducing helpdesk overhead and ensuring a smoother user experience.
</Callout>

## Seamless Integration and Security

Consider the last time you logged into the Azure Portal or accessed your Microsoft 365 dashboard—the smooth and secure login process you experienced is powered by Microsoft Entra ID. It keeps your credentials safe while ensuring that your access remains protected.

Entra ID serves as the central connectivity hub within an IT environment by:

* Integrating with on-premises applications, including legacy systems.
* Enabling secure collaboration with business partners.
* Authenticating devices regardless of location.
* Connecting with multiple SaaS applications to enforce unified security policies.
* Synchronizing with on-premises Active Directory environments for consistent identity management.

<Callout icon="lightbulb" color="#1CB2FE">
  The strength of Microsoft Entra ID lies not only in its robust security but also in its ability to enhance productivity, foster collaboration, and provide a seamless user experience.
</Callout>

Now that you understand the fundamentals of Microsoft Entra ID and its core functions, let's explore the key concepts and how they empower modern identity management within the enterprise.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/130c57fd-47e9-40d0-9354-5d349a66f2ed" />
</CardGroup>

---


## Lesson 3: Microsoft Entra ID concepts

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Microsoft-Entra-ID-concepts/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Microsoft-Entra-ID-concepts/page.md)

**Summary:** This lesson explores the core components of Microsoft Entra ID, detailing how identities and accounts are structured and managed within Microsoft cloud services.

# Microsoft Entra ID concepts

> This lesson explores the core components of Microsoft Entra ID, detailing how identities and accounts are structured and managed within Microsoft cloud services.

This lesson explores the core components of Microsoft Entra ID, detailing how identities and accounts are structured and managed within Microsoft cloud services. It breaks down the relationship between identity, account, Microsoft Entra ID account, and tenant (also known as directory) while providing clear definitions and examples for each concept.

## What is an Identity?

An identity is any object that can be authenticated within a system. In Microsoft Entra ID, identities come in various forms, including:

* **User:** Represents an individual with access to services.
* **Group:** A collection of users often managed together.
* **Managed Identity:** The identity associated with a service in Azure (such as a virtual machine or app service) that enables secure access to other services.
* **Service Principal:** Similar to on-premises service accounts, these are used for automated tasks or to execute processes on behalf of a user.

<Callout icon="lightbulb" color="#1CB2FE">
  An identity alone is not sufficient for detailed resource management—it must be supplemented with additional data attributes to form an account.
</Callout>

## Defining an Account

An account is formed when data attributes—such as location, department, manager, and phone number—are associated with an identity. In essence, once an identity carries additional metadata, it becomes a fully featured account that is used for managing user access and resource permissions.

## Microsoft Entra ID Account Explained

A Microsoft Entra ID account is an account created through Microsoft Entra ID or another Microsoft cloud service. These accounts fall into two main categories:

* **Work or School Account:** Typically provided and managed by organizations for employees or students.
* **Personal Account:** Used by individuals for accessing services like Xbox, Outlook, or Hotmail.

Both types of accounts ensure secure and efficient access to Microsoft services while using a unified identity management system.

## Understanding Tenant (Directory)

A tenant, also referred to as a directory, is a dedicated instance of Microsoft Entra ID that is automatically generated during the sign-up process for any Microsoft cloud service subscription. When you create an Azure account, you also create a tenant, and all associated subscriptions are mapped to this tenant.

<Frame>
  ![The image is a diagram titled "Microsoft Entra ID Concepts," illustrating four concepts: Identity, Account, Microsoft Entra ID Account, and Microsoft Entra ID or Tenant or Directory, each represented with icons.](https://kodekloud.com/kk-media/image/upload/v1752884593/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Microsoft-Entra-ID-concepts/microsoft-entra-id-concepts-diagram.jpg)
</Frame>

## Key Takeaways

* **Identity:** The foundational element used for authentication (including users, groups, managed identities, and service principals).
* **Account:** An identity enriched with detailed data attributes.
* **Microsoft Entra ID Account:** An account provisioned via Microsoft Entra ID that supports both work/school and personal use cases.
* **Tenant/Directory:** A dedicated instance of Microsoft Entra ID that organizes your subscriptions and resources.

<Callout icon="lightbulb" color="#1CB2FE">
  Understanding the differences between Microsoft Entra ID (formerly Azure AD) and Active Directory Domain Services will greatly enhance your ability to manage user identities, managed identities, and service principals in the Azure environment.
</Callout>

By mastering these concepts, you will be better equipped to navigate and manage the flexible, secure landscape of Microsoft cloud services. For further reading, consider exploring the [Microsoft Entra ID Documentation](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis) and related resources on Microsoft cloud management.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/b2b559d8-c5f7-4fe4-ab99-274565b847d6" />
</CardGroup>

---


## Lesson 4: Microsoft Entra ID vs Active Directory Domain Services

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Microsoft-Entra-ID-vs-Active-Directory-Domain-Services/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Microsoft-Entra-ID-vs-Active-Directory-Domain-Services/page.md)

**Summary:** This article explores the differences between Microsoft Entra ID and Active Directory Domain Services in identity management and infrastructure requirements.

# Microsoft Entra ID vs Active Directory Domain Services

> This article explores the differences between Microsoft Entra ID and Active Directory Domain Services in identity management and infrastructure requirements.

Microsoft Entra ID introduces a modern solution for identity management that stands in stark contrast to the traditional Active Directory Domain Services (AD DS). This article explores the fundamental differences between these two technologies and explains how each fulfills unique infrastructure requirements.

## Accessibility and Protocols

Microsoft Entra ID is built for today’s cloud-first environment by utilizing web-based protocols such as HTTP and HTTPS. This approach ensures that resources are securely accessible from any location. In addition, Entra ID incorporates state-of-the-art authentication protocols—including SAML, WS-Federation, OpenID Connect, and OAuth—making it the preferred choice for secure, internet-based applications.

Conversely, Active Directory Domain Services relies heavily on LDAP, a protocol that was developed with on-premises, network-restricted environments in mind. While AD DS supports Kerberos for secure authentication, it lacks the flexibility required for seamless integration with modern web applications.

<Callout icon="lightbulb" color="#1CB2FE">
  Active Directory works best in controlled, on-premises environments, whereas Microsoft Entra ID is optimized for scalable, cloud-based operations.
</Callout>

## Federation and Integration

A key strength of Microsoft Entra ID is its robust federation capability. It enables smooth integration with a wide range of third-party providers, including popular social media platforms like Facebook and Google. This extensive federated ecosystem simplifies the integration of external services into your identity management framework.

In contrast, Active Directory’s federation capabilities are generally confined to interactions with other domains. Organizations often require complex workarounds to establish third-party integrations in AD DS environments, complicating deployment and management.

## Infrastructure and Management

One of the most significant benefits of Microsoft Entra ID is that it is offered as a fully managed service. By eliminating the need for on-premises servers, organizations can reduce IT overhead, lower maintenance costs, and shift their focus to strategic initiatives.

On the other hand, Active Directory requires dedicated infrastructure—whether on physical servers or virtual machines. This necessity can introduce additional complexity, create more potential points of failure, and require a higher level of maintenance and oversight.

## User Experience and Single Sign-On

Microsoft Entra ID delivers a seamless single sign-on (SSO) experience, allowing users to access multiple applications with a single set of credentials. This streamlined approach is particularly beneficial for customers leveraging Microsoft's suite of cloud services.

In comparison, achieving a similar level of integrated sign-on with Active Directory is more challenging, especially when extending services beyond the corporate network.

<Callout icon="triangle-alert" color="#FF6B6B">
  Organizations transitioning from Active Directory to a cloud-based identity solution should plan carefully and evaluate synchronization tools like Entra ID Connect to bridge on-premises and cloud environments.
</Callout>

## Summary

In summary, Microsoft Entra ID is designed for the modern workplace. It offers enhanced usability, greater flexibility, and robust security to meet the evolving needs of contemporary applications and users. While many organizations continue to depend on Active Directory, transitioning to Microsoft Entra ID—or using hybrid solutions like Entra ID Connect—can simplify identity management and accelerate cloud integration.

Next, let's explore the different editions of Microsoft Entra ID.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/299d0542-91cd-4578-883e-11f7ac996348" />
</CardGroup>

---


## Lesson 5: Microsoft Entra ID Editions

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Microsoft-Entra-ID-Editions/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Microsoft-Entra-ID-Editions/page.md)

**Summary:** This article explores the key editions of Microsoft Entra ID, tailored for enhancing identity and access management capabilities in organizations.

# Microsoft Entra ID Editions

> This article explores the key editions of Microsoft Entra ID, tailored for enhancing identity and access management capabilities in organizations.

In this article, we explore the key editions of Microsoft Entra ID, each tailored to enhance your organization's identity and access management capabilities. The editions range from a comprehensive premium offering to a feature-rich free version, ensuring that organizations of any size can find the solution that best meets their needs.

## Premium P2 Edition

The Premium P2 license stands at the top of the Entra ID suite as the most comprehensive solution. It not only incorporates all features from the lower tiers but also introduces advanced identity protection, governance, and privileged identity management capabilities. These advanced tools help safeguard against cyber threats, ensure compliance, and provide robust control over privileged access.

## Premium P1 Edition

The Premium P1 edition offers a solid foundation for identity management with advanced group management, conditional access, and multi-factor authentication. These features dynamically adjust access based on risk profiles, bolstering your organization’s security while ensuring that compliance with company policies is maintained.

## Governance Edition

The Governance Edition, an evolution of the former Azure AD, focuses on streamlining identity lifecycle management through robust governance practices. It ensures that access rights are granted based on established policies and undergo regular reviews. Among its key features is Privileged Identity Management (PIM), which controls and monitors administrative access, and automated provisioning for user and group accounts to optimize operational processes.

## Free Edition

The Free Edition equips organizations with essential identity management tools while remaining accessible in cost. It provides self-service account management—allowing users to update account details and passwords—and basic single sign-on capabilities. This edition is designed to deliver core identity services suitable for organizations starting their journey with identity and access management.

<Frame>
  ![The image is a chart showing different editions of Microsoft Entra ID, detailing features available in Premium P2, Premium P1, Governance, and Free versions. Each edition includes various features like self-service account management, single sign-on, and conditional access.](https://kodekloud.com/kk-media/image/upload/v1752884588/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Microsoft-Entra-ID-Editions/microsoft-entra-id-editions-chart.jpg)
</Frame>

No matter the size of your organization or the complexity of your requirements, there is a Microsoft Entra ID edition crafted to meet your unique needs. Each edition builds on the previous one, providing progressively enhanced secure and compliant identity infrastructures.

## Reviewing Documentation for Detailed Comparisons

For a thorough understanding of the differences between these editions, it is recommended to consult the official Entra ID plans and pricing documentation. Detailed comparisons will highlight which authentication methods, single sign-on components, and identity governance features are included in each plan. For example, you may find that certain authentication options are unavailable in the Free edition, while some advanced features are exclusive to the P2 or Governance editions.

<Frame>
  ![The image shows a pricing comparison table for Microsoft Entra services, detailing features included in different subscription plans such as Free, 6.00/user/month, 9.00/user/month, and Governance at \$7.00/user/month. Each plan offers various levels of features like authentication, administration, and identity protection.](https://kodekloud.com/kk-media/image/upload/v1752884590/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Microsoft-Entra-ID-Editions/microsoft-entra-pricing-comparison-table.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  For the latest and most detailed information, always refer to the official Microsoft Entra ID documentation. This ensures you have insight into current feature sets, pricing changes, and available plans.
</Callout>

Previously, the Premium P2 license was seen as the ultimate offering for Azure Active Directory. However, with the advent of Microsoft Entra ID, certain advanced features are now exclusive to the Governance Edition. Customers using the P2 plan can purchase governance add-ons to access these additional identity governance capabilities.

## New Products and Upcoming Features

Microsoft Entra ID continues to evolve, now offering innovative products such as Entra Verified ID, Permissions Management License, and Entra Workload ID. These new additions provide enhanced identity solutions and expand the capabilities available within the Entra ecosystem.

<Frame>
  ![The image shows pricing information for Microsoft Entra services, including Permissions Management at 10.40 per resource/month and Workload ID at 3.00 per identity/month, with options to try for free and contact sales.](https://kodekloud.com/kk-media/image/upload/v1752884592/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Microsoft-Entra-ID-Editions/microsoft-entra-pricing-info.jpg)
</Frame>

Stay informed about the latest releases and updates by regularly reviewing official documentation and announcements, ensuring that your organization continues to benefit from cutting-edge identity management innovations.

With a comprehensive understanding of the Microsoft Entra ID editions, we now transition to exploring device identities within Microsoft Entra ID.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/9d8c0f37-4009-4245-9c01-07866a31dfea" />
</CardGroup>

---


## Lesson 6: Configure device identities

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Configure-device-identities/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Configure-device-identities/page.md)

**Summary:** This guide explains how to configure device identities in Microsoft Entra ID for improved security and productivity in modern IT management.

# Configure device identities

> This guide explains how to configure device identities in Microsoft Entra ID for improved security and productivity in modern IT management.

In this guide, we explain how to configure device identities in Microsoft Entra ID—a critical aspect of modern IT management. Although configuring device identities is optional for the [AZ-104: Microsoft Azure Administrator](https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator) exam, previous versions included it for users interested in advanced device management topics.

In today’s modern workspace, managing device identities improves security and productivity. Microsoft Entra ID supports several types of device identities, each tailored to different organizational needs. Let’s explore the three main types:

## Registered Devices

Registered Devices are primarily personal devices, such as smartphones or tablets, that users add to Microsoft Entra ID. These devices enable convenient access to organizational resources like emails and documents and support a bring-your-own-device (BYOD) strategy. Managed via Microsoft Intune, Registered Devices support various operating systems, including Windows 10, iOS, Android, and macOS.

## Joined Devices

Joined Devices are company-owned devices that are exclusively intended for work. They are directly joined to Microsoft Entra ID and require a company account for sign-in. By leveraging cloud-driven security features such as Conditional Access, these devices are ideal for cloud-centric organizations. Joined Devices are mainly compatible with Windows 10 and later operating systems.

<Frame>
  ![The image illustrates three types of device identities: Registered Devices, Joined Devices, and Hybrid Joined Devices, with diagrams and a list of features for cloud-centric organizations.](https://kodekloud.com/kk-media/image/upload/v1752884576/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configure-device-identities/device-identities-diagram-cloud-features.jpg)
</Frame>

## Hybrid Joined Devices

Hybrid Joined Devices serve organizations that blend cloud services with on-premises infrastructure. These devices are joined to both the local Active Directory and Microsoft Entra ID. This dual configuration supports environments that rely on legacy desktop applications and Group Policy management, and it is compatible with Windows 7 and later versions. Hybrid Joined Devices enable the deployment of preconfigured system images along with seamless integration.

<Frame>
  ![The image illustrates three types of device identities: Registered Devices, Joined Devices, and Hybrid Joined Devices, with diagrams and a list of features for hybrid joined devices.](https://kodekloud.com/kk-media/image/upload/v1752884577/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configure-device-identities/device-identities-registered-joined-hybrid.jpg)
</Frame>

Each device identity configuration offers unique benefits:

* **Registered Devices:** Flexibility with personal devices.
* **Joined Devices:** Enhanced security for company-owned machines.
* **Hybrid Joined Devices:** Seamless integration for mixed on-premises and cloud environments.

Selecting the optimal configuration is a strategic decision that can significantly boost both organizational productivity and security.

## Viewing Devices in the Azure Portal

To view the configured devices, sign in to the Azure Portal and navigate to Microsoft Entra ID. Then select Devices to see the list of devices in your environment.

In a demo environment, you may only notice a few unmanaged devices. These devices appear as unmanaged because they are not controlled by a device management solution like Intune, though they remain Entra-joined machines.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a list of devices, including details such as device name, OS version, join type, and registration date.](https://kodekloud.com/kk-media/image/upload/v1752884578/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configure-device-identities/azure-portal-device-list-interface.jpg)
</Frame>

When devices are created as work or school account machines, they display as Microsoft Entra ID Joined devices. For example, if you join your personal phone, it appears as a Registered Device since it is added as a personal device.

By clicking on a device in the Azure Portal, you can view detailed information such as the user principal name of the owner.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying the properties of a device named "DESKTOP-R1A05D7," including details like device ID, OS, version, and user principal name.](https://kodekloud.com/kk-media/image/upload/v1752884579/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configure-device-identities/azure-portal-device-properties-desktop.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  The Mobile Device Management (MDM) field may show "none," indicating that the device is unmanaged. To test device joining, you can use a Windows 10 or Windows 11 machine.
</Callout>

<Frame>
  ![The image shows a Microsoft Azure portal dashboard for device management, displaying alerts and statistics about stale, noncompliant, and unmanaged devices. It also includes navigation options and feature highlights related to device settings and troubleshooting.](https://kodekloud.com/kk-media/image/upload/v1752884580/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configure-device-identities/azure-portal-device-management-dashboard.jpg)
</Frame>

## Joining a Device to Microsoft Entra ID

Follow these steps to join a device to Microsoft Entra ID:

1. Open Windows Settings.
2. Navigate to Accounts and select Access work or school.
3. Connect your work or school account to Microsoft Entra ID. (Note: You might also see Azure AD referenced interchangeably.)
4. Enter your work or school email address when prompted, which redirects you to the sign-in page.

<Frame>
  ![The image shows a Windows settings screen for setting up a work or school account, with a field to enter an email address. The left sidebar displays various settings options like System, Bluetooth & devices, and Accounts.](https://kodekloud.com/kk-media/image/upload/v1752884581/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configure-device-identities/windows-settings-work-school-account.jpg)
</Frame>

After signing in, if the device is not connected already, it will be joined to Microsoft Entra ID automatically.

## Conclusion

In this article, we explored the different types of device identity configurations supported in Microsoft Entra ID and demonstrated how to view and manage these devices using the Azure Portal. Configuring device identities strengthens secure access management—whether you are leveraging personal devices, dedicated work machines, or hybrid setups.

We will continue our exploration by covering effective strategies for managing user and group accounts within Microsoft Entra ID.

Thank you for reading.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/723a0bf2-fa70-4323-9bdf-d1e2599585dd" />
</CardGroup>

---


## Lesson 7: User Accounts

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/User-Accounts/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/User-Accounts/page.md)

**Summary:** This article explains user accounts in Microsoft Entra ID, detailing their types, management, and features for secure access to organizational resources.

# User Accounts

> This article explains user accounts in Microsoft Entra ID, detailing their types, management, and features for secure access to organizational resources.

Welcome to the foundational element of Microsoft Entra ID. In this guide, we will explain how user accounts serve as the gateway to securing and streamlining access to your organizational resources. These accounts are much more than just a username and password—they are digital passports that provide entry to applications, systems, and services while also enabling richer profile configurations.

In Microsoft Entra ID, each user requires a unique account. These accounts not only support secure authentication and authorization but also offer optional properties such as address, department, and role. This enrichment helps streamline communication and improve operational workflows across your organization.

Administrators can manage identities centrally via the Microsoft Entra ID portal under "Users > All Users." With bulk operations available for creating, inviting, and deleting multiple accounts, the portal significantly enhances the efficiency of onboarding or offboarding processes.

## Types of User Accounts in Microsoft Entra ID

### Cloud Identities

Cloud Identities are standalone accounts that exist solely in the cloud without any dependency on an on-premises directory. They are ideal for organizations fully embracing cloud technology, offering flexibility and secure access from anywhere. Note that these cloud identities can belong either to a home Entra ID tenant or to an external one.

### Guest Accounts

Guest Accounts are tailored for external users, such as partners or contractors, who need access to specific resources without being fully integrated into the internal directory. These accounts can include Microsoft, Live, or Gmail accounts and facilitate secure collaboration while maintaining organizational boundaries.

<Callout icon="lightbulb" color="#1CB2FE">
  If a user belongs to another company with its own Entra ID, they are treated as a cloud identity; however, if that user does not have an Entra ID, the account is considered a guest account.
</Callout>

### Directory Synchronized Users

Directory Synchronized Users have identities synchronized from an on-premises Active Directory to the cloud through the Microsoft Entra ID Connect tool (formerly known as Azure AD Connect). Synchronization ensures a unified identity framework across on-premises and cloud environments, simplifying the management of access rights and security policies.

<Frame>
  ![The image is an informational graphic about user accounts in Microsoft Entra ID, detailing features like authentication, optional properties, and bulk operations. It includes a screenshot of a user management interface and highlights categories such as Cloud Identities, Guest Accounts, and Directory Synchronized Users.](https://kodekloud.com/kk-media/image/upload/v1752884607/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-User-Accounts/microsoft-entra-id-user-accounts-graphic.jpg)
</Frame>

Each type of account plays a vital role in constructing a robust identity and access management strategy, ensuring that users receive the appropriate level of access exactly when they need it.

## Managing User Accounts in the Azure Portal

The Azure Portal is your central hub for creating and managing both cloud identities and guest accounts. Follow these steps to manage your users effectively:

1. **Navigate to the Users Section:**\
   Go to the Azure Portal, access Microsoft Entra ID, and click on "Users."

2. **Search and Identify Account Types:**\
   Use the search function to filter users by name or account type. For example, when you search for a given name, an account from another directory might appear. If that account exists solely within Microsoft Entra ID, it is classified as a cloud identity—even if it originates from an external source. Conversely, a Microsoft account created through an invitation is marked as a guest, even if related to Entra ID.

3. **B2B Collaboration:**\
   When inviting an external user who does not have an Entra ID (e.g., Outlook or Gmail users), they will be designated as a guest user.

4. **On-Premises Synchronized Users:**\
   Users synchronized from an on-premises Active Directory via Entra ID Connect appear as directory synchronized users. These accounts cannot be directly created from the portal; they are managed through your synchronization tasks.

### Creating a New User

To add a new user:

1. Click on "New User" to display two options:
   * **Create a new user** (for internal accounts)
   * **Invite an external user** (for guest accounts)

2. For internal accounts, fill in the details such as user principal name, display name, and password. Additional attributes and role assignments can be configured as required.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a new user, with fields for user principal name, mail nickname, display name, and password settings.](https://kodekloud.com/kk-media/image/upload/v1752884608/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-User-Accounts/azure-portal-create-user-interface.jpg)
</Frame>

After providing the required information, click "Create" to add the user to your Entra ID directory. Upon creation, the user’s account type and domain (for example, "kodekloudlab.onmicrosoft.com") will be visible in search results.

### Inviting Guest Users

To include external collaborators:

* Enter the guest user's email address (e.g., [ChrisW@xyc.com](mailto:ChrisW@xyc.com)) and send an invitation.
* Although the account appears as a guest, if the invited user belongs to another Microsoft Entra ID tenant, their underlying identity will still be classified as a cloud identity.

### Working with Directory Synchronized Users

To focus on synchronized users from an on-premises Active Directory:

* Apply the relevant filter to display only sync-enabled users.
* These accounts are identified by an "on-premises sync enabled" property, typically set to "Yes," indicating their source.

### Modifying and Deleting User Accounts

For ongoing account management:

* **Editing:**\
  Select a user (e.g., Abigail's account) and click "Edit Properties." You can update details including name, user principal name, job information, and contact information. Global administrators or tenant owners also have the option to reset passwords.

* **Deleting:**\
  When you delete an account, it moves to the "Deleted Users" list. This provides a grace period of 30 days during which the account can be restored before permanent deletion occurs.

<Frame>
  ![The image shows a Microsoft Azure user profile page for "Abigail Richards," displaying various user properties and settings such as identity, contact information, and job information.](https://kodekloud.com/kk-media/image/upload/v1752884609/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-User-Accounts/azure-user-profile-abigail-richards.jpg)
</Frame>

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a list of deleted users, with options to restore or permanently delete them. A specific user, "Abigail Richards," is selected for potential restoration.](https://kodekloud.com/kk-media/image/upload/v1752884610/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-User-Accounts/azure-portal-deleted-users-list.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  To restore a deleted user, click "Restore Users." If the account is to be removed permanently, choose the deletion option.
</Callout>

## Bulk Operations and Additional Features

While the steps above cover individual account management, Microsoft Entra ID supports bulk operations for scenarios involving large numbers of users. These bulk actions include:

| Operation Type        | Use Case                                                    | Example Command/Action                                  |
| --------------------- | ----------------------------------------------------------- | ------------------------------------------------------- |
| Mass Invitations      | Inviting multiple external users simultaneously             | Use the bulk invitation tool in the portal              |
| Bulk Account Creation | Rapidly onboarding many internal users                      | Import user details through a CSV file                  |
| Bulk Deletion         | Efficiently offboarding users during organizational changes | Select and delete multiple user accounts at once        |
| Bulk Password Resets  | Resetting passwords for groups of users to enhance security | Execute a batch password reset operation via PowerShell |

These operations are particularly beneficial for organizations undergoing rapid growth or restructuring, ensuring that identity management scales with your organizational needs.

This concludes our comprehensive overview of user accounts in Microsoft Entra ID. In the next lesson, we will explore advanced bulk operations for efficient user management at scale. For more detailed insights and further configuration tips, consider exploring the official [Microsoft Entra ID documentation](https://learn.microsoft.com/en-us/azure/active-directory/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/51d8c0a7-6d65-4903-b37e-b0050789fef8" />
</CardGroup>

---


## Lesson 8: Bulk Operations

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Bulk-Operations/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Bulk-Operations/page.md)

**Summary:** This guide covers key bulk operations in Microsoft Entra ID to streamline user management and reduce manual effort.

# Bulk Operations

> This guide covers key bulk operations in Microsoft Entra ID to streamline user management and reduce manual effort.

Efficiency in user management is essential for maintaining a secure and agile IT environment. This guide covers the key bulk operations available in Microsoft Entra ID that streamline administrative tasks by managing multiple user accounts simultaneously. Instead of processing user additions, deletions, or invitations one at a time, bulk operations let you handle them in large groups, cutting down on manual effort and reducing the risk of errors.

Below are the available bulk operations:

* **Bulk Create:** Upload a CSV file to rapidly add multiple new users to your directory. This is ideal for onboarding large groups of employees, ensuring a smooth setup from day one.
* **Bulk Invite:** Easily invite external users such as contractors, vendors, or partners. This feature sends an invitation, enabling users to sign in using either their existing Microsoft account or Microsoft Entra ID credentials.
* **Bulk Delete:** Remove multiple user accounts at once to keep your directory updated. This helps maintain an active directory with only current and relevant user accounts.
* **Download Users:** Export user data for reporting, auditing, or archival needs to promote transparency and effective record keeping.

Bulk operations not only increase efficiency but also minimize errors compared to repetitive manual entries. They are indispensable tools for administrators looking to optimize workflows in Microsoft Entra ID.

***

## Accessing Bulk Operations in Microsoft Entra ID

After logging into Microsoft Entra ID, go to the **Users** section. At the top of the page, you will find options for bulk operations including Bulk Create, Bulk Invite, and Bulk Delete. With recent updates, the Download Users option is also available here.

***

## Using Bulk Create

Start by selecting the Bulk Create option from the dropdown menu and download the CSV template provided.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a list of users with details such as display names, user principal names, and user types. A dropdown menu for bulk operations is open, highlighting options like "Bulk create."](https://kodekloud.com/kk-media/image/upload/v1752884572/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Bulk-Operations/azure-portal-user-list-dropdown.jpg)
</Frame>

Open the downloaded CSV file in Microsoft Excel. The template includes one required field and several optional fields for additional user details. The screenshot below displays an example entry with columns for name, username, password, and job title.

<Frame>
  ![The image shows an Excel spreadsheet with columns for user information such as name, username, password, and job title. There is an example entry in the first row.](https://kodekloud.com/kk-media/image/upload/v1752884573/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Bulk-Operations/excel-user-information-spreadsheet.jpg)
</Frame>

For instance, fill in the required field with your domain name and enter a generated password (or any secure, random string) for the new user accounts. In this example, entries for "Captain America" and "Loki" were included using the same password for both users. After populating the CSV with the necessary details for all users, save the file to your computer.

Next, return to the Azure Portal and upload your CSV file by selecting the appropriate option. Once the file is uploaded successfully, click on **Submit**. Monitor the progress in the Bulk Operation Results section, which shows detailed status information for each account creation.

<Frame>
  ![The image shows a Microsoft Azure portal page displaying the results of a bulk user creation operation, with three users successfully created.](https://kodekloud.com/kk-media/image/upload/v1752884574/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Bulk-Operations/azure-portal-bulk-user-creation.jpg)
</Frame>

Finally, navigate to the **All Users** blade to verify that your new accounts have been added. While this guide uses an example with three users, this process can easily scale to hundreds of users.

***

## Using Bulk Invite

Bulk Invite follows a similar process to Bulk Create but simplifies user inclusion by eliminating the need for a password. Instead, invited users can sign in with their existing Microsoft account or Microsoft Entra ID credentials. The CSV template for Bulk Invite requires only the email address for each user and an optional redirection URL.

After uploading your invitation CSV file, the system sends an invitation email to each address. Users with an existing Microsoft account can use their current password; new users can register during the invitation process. Administrators also have the option to customize the invitation message or manually copy the invitation link if required—for example, when users do not have an Exchange license.

<Callout icon="lightbulb" color="#1CB2FE">
  Take advantage of the Bulk Invite feature to reduce onboarding times for external partners and ensure secure access to your tenant.
</Callout>

***

## Using Bulk Delete

Bulk Delete lets you efficiently remove multiple user accounts. To use this feature, download the CSV template provided for deletion, which requires only the User Principal Name (UPN) for each account you intend to delete.

For example, if you need to delete the users created earlier, copy their UPNs from the Bulk Create CSV file into the Bulk Delete template, save the file, and then upload it to the portal. After confirming the deletion prompt, click **Submit**.

Review the results of the bulk deletion in the Bulk Operation Results section. The screenshot below confirms that the deletion operation was completed successfully with three successful requests.

<Frame>
  ![The image shows the "Bulk operation results" page in Microsoft Azure, displaying the status of user creation and deletion operations, both completed successfully without errors.](https://kodekloud.com/kk-media/image/upload/v1752884575/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Bulk-Operations/bulk-operation-results-azure.jpg)
</Frame>

Then, inspect the **Users** section or the **Deleted Users** blade to verify that the specified accounts have been removed.

***

## Invitation Email Preview

The invitation email sent out during a Bulk Invite includes your organization’s name, tenant information, and an option for the user to accept the invitation. Once a user clicks **Accept Invitation**, they gain access to your tenant.

***

With these streamlined steps, you are now equipped to manage bulk operations in Microsoft Entra ID effectively. Up next, we will explore best practices for Group Account management. Explore more detailed guides at [Microsoft Entra ID documentation](https://docs.microsoft.com/entra-id).

Happy managing!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/9638b0c2-d4bd-4acd-9516-209a9c4a30fe" />
</CardGroup>

---


## Lesson 9: Group Accounts

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Group-Accounts/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Group-Accounts/page.md)

**Summary:** This guide covers managing Microsoft Entra ID group accounts, including group types, assignment methods, and configuration steps via the Azure Portal.

# Group Accounts

> This guide covers managing Microsoft Entra ID group accounts, including group types, assignment methods, and configuration steps via the Azure Portal.

Microsoft Entra ID group accounts are essential for managing and securing resource access within your organization. This guide provides an overview of different group types and assignment methods, along with step-by-step instructions for configuring groups via the Azure Portal.

***

## Group Types

### Security Groups

Security groups let you manage member permissions for accessing resources. For example, you might create a security group named "Azure Administrators" to grant specific administrative privileges on Azure services to its members.

### Microsoft 365 Groups

Microsoft 365 Groups are built for collaboration. They integrate seamlessly with Microsoft 365 services such as Outlook, Teams, and SharePoint by offering a shared workspace. For instance, a "Finance" group can provide its members with a shared mailbox, document library, and OneNote notebook, enhancing team productivity.

***

## Assignment Types

### Assigned Groups

Assigned groups require that members be added manually. For example, if an employee needs access to HR-related Azure resources, an Azure Administrator would manually add them to the HR group. This traditional method offers straightforward and direct control over group membership.

### Dynamic User Groups

Dynamic user groups use attribute-based rules to automatically update membership. For example, you can define a rule that adds users to the HR group if their job title contains "HR". This approach minimizes manual intervention while ensuring membership remains current.

### Dynamic Device Groups

Dynamic device groups apply only to security groups and function in a similar way as dynamic user groups, but they rely on device attributes. For example, you could set a rule to automatically include all devices running a specific operating system, enabling targeted software updates.

<Callout icon="lightbulb" color="#1CB2FE">
  Using dynamic groups can improve security and administrative efficiency by automating membership based on up-to-date user or device attributes.
</Callout>

***

## Working with Groups in Microsoft Entra ID via the Azure Portal

To manage groups, log in to the Azure Portal, navigate to Microsoft Entra ID, and then select Groups. This section of the portal is where you create, update, and review your groups.

### Creating a Security Group

1. Click the "New Group" button.
2. Select the appropriate group type—choose "Security Group" for this example—and name it "Hiring Managers".
3. Optionally, add a description.
4. If you plan to assign Azure AD or Microsoft Entra ID roles to the group, change this setting to "Yes" (the default is "No").

<Callout icon="lightbulb" color="#1CB2FE">
  Detailed role assignments are available in courses such as [Microsoft Azure Security Technologies (AZ-500)](https://learn.kodekloud.com/user/courses/microsoft-azure-security-technologies-az-500).
</Callout>

5. Set the membership type to "Assigned" to manage users manually.
6. By default, the group creator becomes the owner. You can add more owners during or after the creation process.
7. Under the Members section, add users—or even another group (e.g., DevRel) to form nested groups.
8. Click "Create" to finalize the group.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a list of groups with details such as name, object ID, group type, membership type, and email.](https://kodekloud.com/kk-media/image/upload/v1752884582/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Group-Accounts/azure-portal-groups-list.jpg)
</Frame>

### Creating a Microsoft 365 Group

To create a Microsoft 365 group:

1. Click on "New Group" and select "Microsoft 365."
2. Fill in the group settings. Besides the common settings, you must specify a group email address, which will be used to create a shared mailbox (ensure you have an Exchange license).

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a new Microsoft 365 group. It includes fields for group type, name, email address, description, and membership type, with options for assigning Microsoft Entra roles.](https://kodekloud.com/kk-media/image/upload/v1752884583/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Group-Accounts/azure-portal-microsoft-365-group.jpg)
</Frame>

The process is quite similar to creating a security group, with the additional step of providing an email address.

<Frame>
  ![The image shows a Microsoft Azure portal interface where a new group named "Hiring Managers" is being created. The "Add members" section is open, displaying a list of groups and selected members on the right.](https://kodekloud.com/kk-media/image/upload/v1752884584/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Group-Accounts/azure-portal-hiring-managers-group.jpg)
</Frame>

***

## Bulk Operations and Dynamic Group Membership

Using bulk operations can streamline the management of group memberships, particularly when dealing with a large number of users.

### Bulk User Creation

Bulk user creation is an efficient way to prepare for dynamic memberships. For example, you might use a CSV file containing details such as department and usage location for multiple users.

1. Navigate to Bulk Operations under the Users section.
2. Select "Bulk Create" and upload your CSV template.
3. Click "Submit" to process the creation of users.
4. Wait for the operation to complete. The CSV file settings will later help define dynamic group membership.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a list of users with details such as display name, user principal name, and user type. On the right, there is a section for bulk creating users with options to download, edit, and upload a CSV file.](https://kodekloud.com/kk-media/image/upload/v1752884585/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Group-Accounts/azure-portal-user-list-interface.jpg)
</Frame>

Once the process is complete (e.g., "20 out of 20 completed without any errors"), you can proceed to configure dynamic groups.

<Frame>
  ![The image shows a Microsoft Azure portal page displaying the results of bulk user operations, including user creation and deletion, with details on file names, upload times, completion times, and statuses.](https://kodekloud.com/kk-media/image/upload/v1752884587/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Group-Accounts/azure-portal-bulk-user-operations.jpg)
</Frame>

### Creating a Dynamic User Group

Dynamic user groups update automatically based on your defined criteria:

1. In Microsoft Entra ID, select Groups and click on "New Group."

2. Name the group (for example, "Avengers") and choose "Dynamic User" as the membership type.

3. Enter a dynamic query to define membership criteria. For example, to include users from the "Avengers" department, use:

   ```none theme={null}
   (user.department -eq "Avengers")
   ```

   To further refine the criteria (e.g., including only users in the US), modify the query as follows:

   ```none theme={null}
   (user.department -eq "Avengers") and (user.usageLocation -eq "US")
   ```

4. Save the rule. The system will automatically add users who meet the criteria and adjust membership if user attributes change.

5. Use the "Validate Rules" option to troubleshoot dynamic membership issues. For example, if a user like Gamora is missing from the "Avengers" group, the tool can help highlight that, despite matching one condition (e.g., usage location), the department attribute does not match.

### Creating a Dynamic Device Group

Dynamic device groups, available exclusively for security groups, rely on device properties (such as operating system or vendor):

1. Create a new group in Microsoft Entra ID, selecting "Dynamic Device" as the membership type.
2. Construct a dynamic query to include devices based on properties (for example, devices where the operating system is Windows).
3. Follow similar steps as for dynamic user groups, but base your query on device attributes.

<Callout icon="triangle-alert" color="#FF6B6B">
  Ensure that device attribute data is accurate and up-to-date, as this directly affects dynamic group membership and subsequent policy applications.
</Callout>

***

## Additional Group Settings

Microsoft Entra ID provides several advanced settings for group management, including:

* Deleted Groups (acting as a recycle bin)
* Group Expiration Policies
* Naming Policies to restrict certain words

***

This guide has provided a comprehensive overview of creating and managing different group types in Microsoft Entra ID, with a focus on both manual and dynamic membership methods. Next, we will explore one of the self-service features: Self-Service Password Reset (SSPR).

Thank you.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/44ef192e-51aa-4070-b223-3379ac21553b" />
</CardGroup>

---


## Lesson 10: Self service password reset SSPR

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Self-service-password-reset-SSPR/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Self-service-password-reset-SSPR/page.md)

**Summary:** Self-Service Password Reset (SSPR) enables users to securely reset passwords independently, reducing reliance on IT support and streamlining the password management process.

# Self service password reset SSPR

> Self-Service Password Reset (SSPR) enables users to securely reset passwords independently, reducing reliance on IT support and streamlining the password management process.

Self-Service Password Reset (SSPR) offers a secure, streamlined approach to managing your passwords without having to rely on IT support. Instead of waiting on hold every time you forget your password, SSPR empowers you to reset it independently with just a few clicks—saving time and reducing frustration.

Many of us have experienced the hassle of contacting IT support and enduring long wait times just to reset a password. With SSPR, you can bypass these delays by choosing from multiple authentication methods such as email, phone, or mobile app verification. The process is similar to resetting your internet banking password: click "Forgot Password," complete a verification step (using a one-time code or answering security questions), and reset your password securely.

<Callout icon="lightbulb" color="#1CB2FE">
  In Azure, SSPR is available as a premium feature requiring a P2 license. However, administrators have SSPR enabled by default for their accounts. This feature can be applied organization-wide or targeted to specific groups for added flexibility.
</Callout>

Getting started with SSPR involves the following steps:

1. **Enable SSPR** – Choose to enable the feature for all users or selected groups.
2. **Configure Authentication Methods** – Set up the required authentication methods for password reset.
3. **User Registration Prompt** – Ensure users are prompted to register their reset methods at their next sign-in.

<Frame>
  ![The image is an infographic about Self-Service Password Reset (SSPR) in Microsoft Azure, explaining its features, requirements, and setup steps. It includes a screenshot of the Azure interface for configuring authentication methods.](https://kodekloud.com/kk-media/image/upload/v1752884598/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Self-service-password-reset-SSPR/self-service-password-reset-azure-infographic.jpg)
</Frame>

***

## Configuring SSPR in Azure

To configure SSPR in the Azure portal, follow these steps:

1. **Access the SSPR Feature**\
   Sign in to the Azure portal and navigate to Microsoft Entra ID. You can access SSPR via the password reset blade or through the user's blade. Note that while SSPR is typically disabled for users by default, it is enabled automatically for administrators.

2. **Select Targeted Groups**\
   In our configuration example, we select the "Selected" option and target a specific group (such as the Avengers group created previously). After choosing the group, click **Save** to establish a password reset policy for that group.

3. **Configure Authentication Methods**\
   Decide on the number of authentication methods required to reset a password. In our example, we require only one method, the mobile app code. This setting requires users to verify the reset process using an authenticator app. Remember to click **Save** after making any changes.

4. **Enforce Registration Settings**\
   Under the registration settings, you can enforce SSPR registration. By default, users are prompted to register for SSPR at their next sign-in if they haven't already done so. You also have the option to configure how frequently users need to reconfirm their authentication information (in days) to keep their details up to date.

<Frame>
  ![The image shows a Microsoft Azure portal page for password reset registration settings, where users can configure options like requiring registration upon sign-in and setting the number of days before users must reconfirm their authentication information.](https://kodekloud.com/kk-media/image/upload/v1752884600/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Self-service-password-reset-SSPR/azure-password-reset-registration-settings.jpg)
</Frame>

After configuring these settings, your SSPR setup is complete.

***

## Testing the SSPR Setup

To ensure your SSPR configuration works as expected:

1. **Sign Out and Sign In**\
   Log out of a user account (for example, an account named Iron Man) and sign in again. You should see a prompt stating, "Your organization needs more information to keep your account secure." This indicates that some required password reset information is missing and triggers the registration process.

2. **Proceed with Registration**\
   Click **Next** when prompted.

<Frame>
  ![The image shows a Microsoft Azure login screen requesting more information to secure an account, with a "Next" button highlighted.](https://kodekloud.com/kk-media/image/upload/v1752884601/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Self-service-password-reset-SSPR/azure-login-screen-secure-account.jpg)
</Frame>

3. **Set Up the Microsoft Authenticator App**\
   The process will guide you to download and set up the Microsoft Authenticator app. Follow the instructions by scanning the provided QR code and verifying the setup with a six-digit code.

   Click **Next** to continue with the Authenticator setup.

<Frame>
  ![The image shows a Microsoft Authenticator setup page prompting the user to download the app to keep their account secure. There is a "Next" button and an option to skip the setup.](https://kodekloud.com/kk-media/image/upload/v1752884602/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Self-service-password-reset-SSPR/microsoft-authenticator-setup-page.jpg)
</Frame>

4. **Scan the QR Code**\
   Use your phone to scan the QR code presented on the screen.

<Frame>
  ![The image shows a Microsoft Authenticator setup page with a QR code for scanning, and options to go back or skip the setup.](https://kodekloud.com/kk-media/image/upload/v1752884603/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Self-service-password-reset-SSPR/microsoft-authenticator-setup-qr-code.jpg)
</Frame>

5. **Enter the Verification Code**\
   After scanning, enter the six-digit code (e.g., 278382) displayed on your screen and click **Next**. This confirms that SSPR is configured correctly.

6. **Finalize Setup**\
   A confirmation screen will appear once the security information has been successfully registered.

<Frame>
  ![The image shows a confirmation screen indicating successful setup of security information using an authenticator app. A message at the top confirms the registration of the app.](https://kodekloud.com/kk-media/image/upload/v1752884604/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Self-service-password-reset-SSPR/security-setup-confirmation-authenticator.jpg)
</Frame>

***

## Updating Your Security Information

If you ever need to update or change your security details, navigate to [https://aka.ms/SSPRsetup](https://aka.ms/SSPRsetup). This page allows you to add, update, or delete your sign-in methods, depending on the permissions set by your administrator.

<Frame>
  ![The image shows a "Security info" page from a Microsoft account settings interface, displaying sign-in methods such as password and authenticator app. The interface includes options to change or delete these methods.](https://kodekloud.com/kk-media/image/upload/v1752884605/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Self-service-password-reset-SSPR/microsoft-account-security-info-page.jpg)
</Frame>

***

## Resetting a Forgotten Password

If a user, such as Iron Man, forgets their password, they can reset it using either of the following methods:

1. **Via the SSPR Page**
   * Navigate to [https://aka.ms/SSPRsetup](https://aka.ms/SSPRsetup).
   * Enter your username, complete the CAPTCHA, and input the verification code from your authenticator app.

2. **Using the "Can't access your account" Link**
   * Click on the "Can't access your account" hyperlink on the login page.
   * Choose "Work or School Account" when prompted.
   * Complete the CAPTCHA and enter the verification code.
   * Once verified, you will be prompted to set a new password.

<Frame>
  ![The image shows a Microsoft account recovery page where users are prompted to enter their email or username and solve a CAPTCHA to verify their identity.](https://kodekloud.com/kk-media/image/upload/v1752884606/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Self-service-password-reset-SSPR/microsoft-account-recovery-captcha.jpg)
</Frame>

This process provides a secure and efficient method for password recovery.

***

## Multi-Tenant Environments

The procedures described above apply primarily to single-tenant environments (e.g., a single instance of Microsoft Entra ID). In multi-tenant environments, the same principles apply, though additional considerations for managing and delegating SSPR across different tenants are necessary.

***

In conclusion, SSPR is a critical tool for ensuring that password recovery is both efficient and secure, minimizing the need for IT intervention. By following the configured steps in the Azure portal, users can easily manage and reset their passwords, ensuring continuous access to essential services.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/7d734330-1593-45a8-bbf8-8a14f6f4ef93" />
</CardGroup>

---


## Lesson 11: Multi tenant environments

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Multi-tenant-environments/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Identity/Multi-tenant-environments/page.md)

**Summary:** This article explores multi-tenant environments, focusing on principles that define tenant operations within Microsoft Entra ID for the AZ-104 exam.

# Multi tenant environments

> This article explores multi-tenant environments, focusing on principles that define tenant operations within Microsoft Entra ID for the AZ-104 exam.

This article delves into the concept of multi-tenant environments, an essential topic for those preparing for the [AZ-104: Microsoft Azure Administrator](https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator) exam. The discussion highlights four key principles that define tenant operations within Microsoft Entra ID.

## Relationship Independence

Each Microsoft Entra ID organization, often referred to as a tenant, functions autonomously. Unlike on-premises Active Directory—with its intricate structures like forests, root domains, trees, and trusts—cloud environments feature a flat hierarchy. There is no parent-child or hierarchical relationship between tenants. Multiple tenants can coexist, each managing its own subscriptions, users, groups, and resources.

## Resource Independence

Actions performed in one tenant—whether it's the creation or deletion of resources—do not influence other tenants. This strict isolation guarantees that each tenant's data and assets remain secure and separate from those in other tenants.

<Callout icon="lightbulb" color="#1CB2FE">
  Resource independence ensures that any changes, issues, or maintenance activities in one tenant have no unintended consequences on another, maintaining a robust security posture.
</Callout>

## Administration Independence

Administrative rights are tenant-specific. For example, holding a global administrator role in one tenant does not automatically extend similar privileges in another tenant. If global rights are required in Tenant B, they must be explicitly granted for that tenant. This separation reinforces a secure and well-controlled management environment across all tenants.

## Synchronization Independence

Each Microsoft Entra ID tenant can configure its own on-premises synchronization approach based on its unique needs. Modifications in the synchronization settings of one tenant do not impact any other tenant. This independent synchronization setup offers flexibility and streamlined management.

These principles collectively ensure that even though tenants share the underlying Azure data center infrastructure, each tenant enjoys enhanced security, precise control, and tailored customization.

## Managing Tenants in the Azure Portal

The Azure portal facilitates effortless tenant management, allowing you to switch between different tenants you have access to. For example, your personal account might be set as your home tenant. Previously displayed in a single location, tenant information has now been moved to the settings icon.

Clicking on the settings icon reveals a list of tenants accessible to you. This feature makes it simple to switch profiles and manage tenant-specific resources. Notably, the visual theme of the portal—including its color scheme—changes dynamically to reflect the identity of the currently selected tenant.

<Frame>
  ![The image shows the Microsoft Azure portal settings page, specifically the "Directories + subscriptions" section, where different directories and their details are listed.](https://kodekloud.com/kk-media/image/upload/v1752884598/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Multi-tenant-environments/azure-portal-directories-subscriptions.jpg)
</Frame>

Switching between tenants enables you to manage your home tenant as well as additional tenants you might be invited to join through a B2B process. Even though this is not a primary focus of the exam, understanding the concept of multiple tenant memberships is critical.

<Callout icon="lightbulb" color="#1CB2FE">
  Familiarity with the multi-tenant environment is essential not only for exam success but also for real-world administration and security management.
</Callout>

With this overview, you now understand the foundational aspects of administering identity within Microsoft Entra ID as part of the [AZ-104: Microsoft Azure Administrator](https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator) training. Next, we will explore governance and compliance.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/07e3a37e-65a9-430c-9919-011cc605b25d/lesson/64e01d4f-a2d0-4933-99cd-096d87011320" />
</CardGroup>

---


# Section 03: Administer Governance and Compliance

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


# Section 04: Administer Azure Resources

---


## Lesson 1: Module introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/Module-introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/Module-introduction/page.md)

**Summary:** This module focuses on administering and managing Azure resources through practical deployment and management methods, including ARM templates and Bicep.

# Module introduction

> This module focuses on administering and managing Azure resources through practical deployment and management methods, including ARM templates and Bicep.

In this module, we delve into administering and managing Azure resources, focusing on practical deployment and management methods. Building on your foundational understanding of Azure—such as management groups, subscriptions, resource groups, and their hierarchies—we now shift our attention to the active phase of resource administration.

Below are the primary learning objectives for this module:

1. Configure Azure with administrator tools.
2. Deploy and manage resources using ARM templates.
3. Understand ARM template structure.
4. Explore Bicep, the domain-specific language that streamlines your infrastructure-as-code practices.

## Comparing Administrator Tools

In this section, we compare various administrator tools available for Azure management. This comparison empowers you to choose the ideal tool for each task when managing your Azure resources.

<Callout icon="lightbulb" color="#1CB2FE">
  Selecting the right administrator tool can significantly improve the efficiency and ease of managing your Azure environment.
</Callout>

## Configuring Resources with ARM Templates

Azure Resource Manager (ARM) is the deployment and management layer of Azure. It enables the consistent and predictable deployment, management, and monitoring of Azure resources.

### Key Concepts:

* **Azure Resource Manager:**\
  ARM facilitates resource deployment, management, and monitoring across your Azure environment.

* **ARM Templates:**\
  These templates allow you to define your infrastructure and configurations declaratively and repeatably, ensuring consistency across deployments.

<Callout icon="lightbulb" color="#1CB2FE">
  Utilizing ARM templates can reduce manual configuration errors and streamline your deployment processes.
</Callout>

## ARM Template Structure

Understanding the structure of ARM templates is crucial. These templates serve as blueprints for your Azure resources, detailing all necessary configuration parameters for deployment. Although mastering ARM templates is optional for certifications, a solid grasp of their structure enhances your resource administration capabilities and career skills.

## Introducing Bicep

Bicep is a domain-specific language designed to simplify the creation and management of ARM templates. It offers a cleaner, more readable syntax that enhances your infrastructure-as-code practices.

<Callout icon="lightbulb" color="#1CB2FE">
  Bicep simplifies resource configuration, making it easier to maintain and update your infrastructure code.
</Callout>

Let's begin by exploring the available administrator tools and understand how they fit into the broader scheme of effective Azure resource management.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/7f421132-242f-4d10-85e5-6673b7307d12/lesson/46dfa767-0f31-4eab-a54f-3ea6edb939ab" />
</CardGroup>

---


## Lesson 2: Compare Administrator Tools

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/Compare-Administrator-Tools/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/Compare-Administrator-Tools/page.md)

**Summary:** This article compares various Azure administrator tools, highlighting their unique features and how they enhance resource management efficiency.

# Compare Administrator Tools

> This article compares various Azure administrator tools, highlighting their unique features and how they enhance resource management efficiency.

This article offers a detailed comparison of the various administrator tools available in Azure, including Azure Portal, Azure Cloud Shell, Azure PowerShell, and Azure CLI. Each tool provides unique features that can enhance your daily workflow and help you manage Azure resources more efficiently.

***

## Azure Portal

Azure Portal is a user-friendly, graphical interface designed for managing and organizing your Azure resources. With its intuitive design, you can perform tasks quickly, such as restarting a virtual machine. For example, you can execute the following command to restart a VM:

```bash theme={null}
az vm restart -g MyResourceGroup -n MyVm
```

Azure Portal is not only a gateway to your services but also a comprehensive hub filled with learning resources and detailed documentation. The built-in "learn more" hyperlinks and the availability of a mobile application make it perfect for managing operations such as scaling databases or creating virtual machines on the go.

***

## Azure Cloud Shell

For those who prefer working in a command-line interface via a web browser, Azure Cloud Shell is an excellent choice. This tool offers both Bash and PowerShell environments, allowing you to choose the interface that best aligns with your experience.

Restarting a virtual machine using Cloud Shell is as simple as running:

```bash theme={null}
az vm restart -g MyResourceGroup -n MyVm
```

With an automatic sign-in using your Azure credentials, Cloud Shell maintains your session for 20 minutes of inactivity. This feature is ideal for short-lived tasks. However, be aware that long-running operations might be interrupted by session timeouts.

When you access Cloud Shell through the Azure Portal by clicking the terminal icon, you will be prompted to create a Storage Account if one does not already exist. For instance, if there is no existing storage account, you might see a pop-up like the following:

<Frame>
  ![The image shows the Microsoft Azure portal with a list of resources and a pop-up window for creating storage, including options for subscription, resource group, and storage account settings.](https://kodekloud.com/kk-media/image/upload/v1752884369/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Compare-Administrator-Tools/azure-portal-storage-creation.jpg)
</Frame>

Once you create the storage account (e.g., in East US with a unique name and an associated file share), Cloud Shell launches and displays your cloud drive. An example session may resemble:

```bash theme={null}
Requesting a Cloud Shell. Succeeded.
Connecting terminal...

Welcome to Azure Cloud Shell

Type "az" to use Azure CLI
Type "help" to learn about Cloud Shell

Storage fileshare subscription 2cda1881-8c1e-4c15-be23-a00a708afaf3 is not registered to Microsoft.CloudShell Namespace. Please follow these instructions "https://aka.ms/RegisterCloudShell" to register. Unregistered subscriptions will have restricted access to CloudShell service.

rithin [ ~ ]$ ls
clouddrive
rithin [ ~ ]$
```

<Callout icon="lightbulb" color="#1CB2FE">
  Azure Cloud Shell allows you to easily switch between Bash and PowerShell, create files, and clear the screen, providing a flexible environment for your command-line activities.
</Callout>

***

## Azure PowerShell and Azure CLI

Azure PowerShell and Azure CLI are robust, terminal-based utilities that facilitate command-line operations and script automation. These tools are platform-independent, running seamlessly on Windows, Linux, and macOS, making them ideal for automated deployments.

For example, to restart a virtual machine, you can use the same command previously demonstrated:

```bash theme={null}
az vm restart -g MyResourceGroup -n MyVm
```

### Azure PowerShell

You can install Azure PowerShell on your computer, and the process is straightforward regardless of your operating system. After installation, verify your environment with the following commands:

```powershell theme={null}
$PSVersionTable.PSVersion
```

```powershell theme={null}
Get-Module -Name AzureRM -ListAvailable
```

To sign in, use a browser-based login:

```powershell theme={null}
Login-AzAccount
```

If you prefer device authentication without launching a browser automatically, run:

```powershell theme={null}
Login-AzAccount -UseDeviceAuthentication
```

This command displays a code (e.g., DJ9CKZBF2) along with instructions to navigate to [https://aka.ms/devicelogin](https://aka.ms/devicelogin). After entering the code in your browser and completing the login process, your terminal will update with your subscription details. An example output is shown below:

<Frame>
  ![The image shows a Microsoft Azure login prompt asking if the user is trying to sign in to Microsoft Azure PowerShell, with options to cancel or continue.](https://kodekloud.com/kk-media/image/upload/v1752884369/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Compare-Administrator-Tools/azure-login-prompt-powershell.jpg)
</Frame>

Once authenticated, list your subscriptions with:

```powershell theme={null}
PS C:\Users\RithinSkaria\Downloads> Get-AzSubscription

Name                         Id                                   TenantId
----                         --                                   ---------
KodekLoud - AZ500 - POC    5383dd92-41d0-4b1a-b613-68383d631b15 1e0fa212-37dc-45f5-b668687cac64b Disabled
KodekLoud AZ500 PoC2       434ff1f0-4152-4d36-b959-952d2559b952 1e0fa212-37dc-45f5-b668687cac64b Disabled
KodekLoud AZ-500 PoC3      5217f8ba-e4de-45b5-9e1b-83c5e1ec12ca 1e0fa212-37dc-45f5-b668687cac64b Enabled
KodekLoud Azure Admin - POC 1 2cda1881-81c6-41e5-be23-a0078afa1530 1e0fa212-37dc-45f5-b668687cac64b Enabled
```

To view your storage accounts, run:

```powershell theme={null}
PS C:\Users\RithinSkaria\Downloads> Get-AzStorageAccount

StorageAccountName ResourceGroupName PrimaryLocation SkuName     Kind              AccessTier CreationTime            ProvisioningState
-------------------- ------------------ ---------------- ---------- ----              ----------- --------------------- ------------------
aboutrithin         about-rithin      southindia       Standard_LRS StorageV2      Cool       3/8/2019 11:17:03 AM   Succeeded
```

### Azure CLI

Azure CLI is another popular tool, which after installation allows you to log in using:

```bash theme={null}
az login
```

After logging in, simply running the command "az" will display a list of base commands available, such as account management, container registries (acr), Active Directory management (ad), and Advisor. Here’s an introductory message from Azure CLI:

```bash theme={null}
az
Welcome to Azure CLI!
------------------------
Use `az -h` to see available commands or go to https://aka.ms/cli.

Telemetry
-----------
The Azure CLI collects usage data in order to improve your experience.
The data is anonymous and does not include command line argument values.
The data is collected by Microsoft.

You can change your telemetry settings with `az configure`.

Azure
------------------------
Welcome to the cool new Azure CLI!
Use `az --version` to display the current version.
Here are the base commands:

    account  : Manage Azure subscription information.
    acr      : Manage private registries with Azure Container Registries.
    ad       : Manage Azure Active Directory Graph entities needed for Role Based Access Control.
    advisor  : Manage Azure Advisor.
```

Both Azure PowerShell and Azure CLI offer similar functionalities, allowing you to list subscriptions, execute automation scripts, and integrate with other services. Their robust command-line interfaces provide a powerful way to manage your Azure resources programmatically.

<Callout icon="lightbulb" color="#1CB2FE">
  For users with a .NET background, Azure PowerShell provides rich object-oriented outputs, while Azure CLI may be preferable for those looking for simplicity and quick command responses, such as for container image deployment and management.
</Callout>

***

## Conclusion

In summary, selecting the right administration tool in Azure depends on your specific needs:

* **Azure Portal:** Best for quick, ad hoc tasks with its intuitive and interactive graphical interface.
* **Azure Cloud Shell:** Ideal for administrators who prefer a cloud-based command-line experience without local setup.
* **Azure PowerShell and Azure CLI:** Perfect for automation and scripting, enabling cross-platform command-line management.

By understanding the features and capabilities of each tool, you can choose the solution—or combination of solutions—that best supports your workflow and helps manage your Azure environment efficiently.

Up next, we will explore Azure Resource Manager and uncover its powerful capabilities for resource deployment and management.

For additional information on managing Azure resources, check out the following resources:

* [Azure Administration Documentation](https://docs.microsoft.com/en-us/azure/)
* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/7f421132-242f-4d10-85e5-6673b7307d12/lesson/21aa5219-d10f-4f47-807c-0d2759952aa8" />
</CardGroup>

---


## Lesson 3: Azure Resource Manager

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/Azure-Resource-Manager/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/Azure-Resource-Manager/page.md)

**Summary:** Azure Resource Manager is a centralized management layer in Azure responsible for deploying, updating, and deleting resources like virtual machines and databases.

# Azure Resource Manager

> Azure Resource Manager is a centralized management layer in Azure responsible for deploying, updating, and deleting resources like virtual machines and databases.

Azure Resource Manager (ARM) is the backbone of resource management in Azure. Acting as a centralized management layer, ARM is responsible for deploying, updating, and deleting resources, such as virtual machines, databases, and web apps.

When you issue commands—whether through the Azure portal, Azure PowerShell, CLI, REST clients, or SDKs—ARM is the first component to process these requests. It interprets the high-level instructions you provide and translates them into precise actions, ensuring your services are deployed consistently, organized logically, and configured as specified.

## Key Responsibilities of ARM

* Processing commands to create, update, or delete resources.
* Translating user instructions into concrete backend actions.
* Provisioning resources based on your configuration parameters.

When you deploy a resource, your instructions are forwarded to ARM, which then provisions the necessary services behind the scenes. Conversely, when a resource is slated for deletion, the request is routed through the API to ARM, which manages the removal process.

<Callout icon="lightbulb" color="#1CB2FE">
  ARM provides a reliable and consistent way to manage your cloud infrastructure, reducing the complexity involved in handling disparate services.
</Callout>

## Core Features

ARM offers essential features that enhance the management and security of your resources:

* **Access Control**: Utilize Azure Role-Based Access Control (RBAC) to manage permissions effectively.
* **Resource Tagging**: Easily categorize and filter resources with tags.
* **Resource Groups**: Organize resources logically using Resource Groups for better management.
* **Deployment Templates**: Automate resource provisioning with ARM templates.

| Feature                          | Description                                                   |
| -------------------------------- | ------------------------------------------------------------- |
| Role-Based Access Control (RBAC) | Manages fine-grained access to resources                      |
| Resource Tagging                 | Helps in categorizing resources for improved clarity          |
| Resource Groups                  | Logical containers that group related resources               |
| Deployment Templates             | Automates resource deployment using predefined configurations |

This refined approach marks a significant advancement compared to the older Azure Service Manager (ASM) model. Unlike ASM, ARM supports Resource Groups, RBAC locks, and tagging, making it the essential framework for managing Azure resources efficiently.

## Moving Forward with ARM Templates

Next, we will explore ARM templates—Azure Resource Manager templates—and demonstrate how they automate the deployment process. To learn more about these templates and automate your resource deployment process, refer to the [Azure Resource Manager documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/7f421132-242f-4d10-85e5-6673b7307d12/lesson/d6fc98fd-cd32-480f-ab6a-78785d7ba196" />
</CardGroup>

---


## Lesson 4: Azure Resource Manager Templates

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/Azure-Resource-Manager-Templates/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/Azure-Resource-Manager-Templates/page.md)

**Summary:** Azure Resource Manager templates provide a declarative method for deploying and managing Azure resources using JSON, ensuring consistency and reducing human error.

# Azure Resource Manager Templates

> Azure Resource Manager templates provide a declarative method for deploying and managing Azure resources using JSON, ensuring consistency and reducing human error.

Azure Resource Manager (ARM) templates offer a declarative method for deploying and managing Azure resources. Written in JSON, these templates follow a defined structure that we'll explore in detail below.

## Overview

ARM templates let you specify the desired resources without dictating the deployment procedure—similar to writing HTML to create content while letting the browser handle rendering. By defining your infrastructure declaratively, Azure Resource Manager automatically creates and configures your resources, ensuring consistency and reducing human error.

## Basic Structure

Below is an example of a basic ARM template structure:

```json theme={null}
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {},
  "functions": [],
  "variables": {},
  "resources": [],
  "outputs": {}
}
```

In this template, you specify parameters, functions, variables, resources, and outputs. Parameters are particularly useful for creating dynamic, reusable templates rather than hard-coding values.

## Benefits of ARM Templates

* **Declarative Automation**: List the resources to be created, and let Azure handle the deployment.
* **Consistency and Reusability**: Ensure each environment is set up consistently with standardized templates.
* **Reduced Human Error**: Automated deployments decrease the likelihood of manual mistakes.
* **Modular Design**: Link smaller templates to a parent template to manage and deploy complex environments more efficiently.

<Callout icon="lightbulb" color="#1CB2FE">
  Consider using parameters and variables to enhance template reusability and simplify management.
</Callout>

## Deployment Approaches

ARM templates can be structured in several ways to meet different deployment requirements:

### 1. Single Template for Multiple Resources

Deploy a multi-tier application—for instance, an app service, a virtual machine, and a database—by defining all components within a single ARM template. This approach allows internal referencing, such as linking a SQL database to an app service.

### 2. Linked Templates (Nested Deployment)

Using linked or nested templates is another effective strategy. In this approach, you might combine:

* A main template that orchestrates the overall deployment.
* A nested template for deploying VMs.
* A nested template for deploying App Services.
* A nested template for deploying SQL databases.

This modular design simplifies managing complex deployments and ensures that dependencies are created in the correct order.

<Frame>
  ![The image illustrates an ARM Template Design, showing a flow from a main template to nested templates for a Virtual Machine, App Service, and SQL Database.](https://kodekloud.com/kk-media/image/upload/v1752884368/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Resource-Manager-Templates/arm-template-design-virtual-machine-app-service-sql-database.jpg)
</Frame>

### 3. Individual Templates per Resource Group

For scenarios where resources are grouped into different Resource Groups by type or project, you can maintain a separate ARM template for each resource group. This approach is best for logically separated deployments, while the linked template approach is more efficient when managing a large number of interconnected resources.

<Callout icon="lightbulb" color="#1CB2FE">
  For larger deployments, the linked (nested) template approach is generally more efficient, whereas a single comprehensive template works well for one or two resources.
</Callout>

## Authoring ARM Templates

For a streamlined ARM template authoring experience, use the Azure Resource Manager Tools extension in [Visual Studio Code](https://code.visualstudio.com/). This extension offers features such as syntax highlighting, validation, and deployment assistance to make writing ARM templates easier and more efficient.

## Next Steps

In the following section, we'll dive deeper into each part of an ARM template—parameters, resources, variables, functions, and outputs. This detailed explanation will provide you with a solid foundation for authoring ARM templates and managing your deployments effectively. Although not required for certification exams, understanding this structure is invaluable for automating and maintaining your Azure environments.

Let's now explore the detailed structure of ARM templates.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/7f421132-242f-4d10-85e5-6673b7307d12/lesson/366b6cd1-dd53-4350-bc7b-41320a321c77" />
</CardGroup>

---


## Lesson 5: ARM template structure

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/ARM-template-structure/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/ARM-template-structure/page.md)

**Summary:** This article explains the structure and components of ARM templates for defining and deploying Azure resources using Infrastructure as Code.

# ARM template structure

> This article explains the structure and components of ARM templates for defining and deploying Azure resources using Infrastructure as Code.

ARM templates are a powerful way to define and deploy Azure resources using Infrastructure as Code. They follow a specific structure which includes essential elements such as the schema, content version, parameters, variables, functions, resources, and outputs. Elements marked with an asterisk (\*) are mandatory and must be included in your template.

Below is a detailed explanation of each section:

***

## Schema

The schema element specifies the location of the JSON schema that defines the version of the template language. Think of it as the grammar guide for your template—it ensures that your template adheres to the correct format. The schema you choose depends on the deployment scope (tenant, management groups, or subscriptions). Every ARM template requires a schema.

<Callout icon="lightbulb" color="#1CB2FE">
  The ARM template schema acts as the blueprint for the template structure, ensuring standardized deployments.
</Callout>

***

## Content Version

The content version is used to version the template itself, with the default value being "1.0.0.0". As you update your template, especially when using source control systems like GitHub, you can adjust this versioning to reflect minor or major changes. For example, a minor change could update the version to "1.0.0.1" while a major update might change it significantly.

<Frame>
  ![ARM Template Versioning](https://kodekloud.com/kk-media/image/upload/v1752884362/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-ARM-template-structure/frame_120.jpg)
</Frame>

***

## Parameters

Parameters add flexibility to your template by allowing you to supply deployment-time values. They promote reusability and enable users to pass different values without modifying the entire template. Consider a parameter for location that accepts only predefined values like "East US" or "West US", with a default set to "East US". Metadata such as a description can also be provided to help clarify the purpose of the parameter.

<Frame>
  ![Parameters Explanation](https://kodekloud.com/kk-media/image/upload/v1752884363/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-ARM-template-structure/frame_140.jpg)
</Frame>

<Frame>
  ![Allowed Values](https://kodekloud.com/kk-media/image/upload/v1752884364/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-ARM-template-structure/frame_160.jpg)
</Frame>

<Frame>
  ![Default Value](https://kodekloud.com/kk-media/image/upload/v1752884365/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-ARM-template-structure/frame_170.jpg)
</Frame>

<Frame>
  ![Parameter Metadata](https://kodekloud.com/kk-media/image/upload/v1752884366/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-ARM-template-structure/frame_180.jpg)
</Frame>

***

## Variables

Variables store hardcoded values within the template, simplifying maintenance by centralizing value changes. Instead of modifying the value throughout the template, you simply update it at one place. Keep in mind that unlike parameters, variable values are static and cannot be altered at deployment time.

***

## Functions

Functions in ARM templates allow you to encapsulate and reuse code blocks, reducing redundancy. For instance, you can create a function that generates a unique virtual machine (VM) name by combining an input keyword with random values. This approach is especially useful when deploying multiple instances of similar resources.

***

## Resources

The resources section is the heart of your ARM template, describing the infrastructure to be deployed. For example, when deploying an App Service Plan, you must define the resource name, type (e.g., "Microsoft.Web/serverFarms"), API version, location (which can be dynamic through a parameter), and other properties such as SKU details and tags.

<Callout icon="lightbulb" color="#1CB2FE">
  This section outlines all the components that Azure will create, making it a critical part of your ARM template.
</Callout>

***

## Outputs

Outputs allow you to return values from the deployment process. As an example, if you deploy a public IP address, you can output its value back to the user. This is particularly useful for chaining deployments or for verifying deployment outcomes.

***

## Example: Deploying an ARM Template in Visual Studio Code

Below is a step-by-step workflow for writing and deploying an ARM template using Visual Studio Code.

1. **Create a New Template File**
   * Open Visual Studio Code and create a new file named `template.json`.
   * Set the file type to "Azure Resource Manager Template." (Ensure you have the Azure Resource Manager extension installed; you can search for it in the Extensions view.)

2. **Generate the Template Structure**
   * With the file type set, Visual Studio Code will start the template server.
   * For resource deployments within a Resource Group, type `ARM!` to trigger IntelliSense. The extension will generate the base template structure.
   * If you are deploying a Resource Group itself (a subscription-level deployment), the schema automatically adjusts accordingly.

3. **Define Parameters and Variables**

   * Begin by creating a parameter for location. For example:

   ```json theme={null}
   "parameters": {
     "location": {
       "type": "string",
       "allowedValues": ["East US", "West US"],
       "defaultValue": "East US",
       "metadata": {
         "description": "The location for the resources."
       }
     },
     "part": {
       "type": "string",
       "minLength": 4,
       "maxLength": 7,
       "metadata": {
         "description": "A short identifier part for the resource name."
       }
     }
   }
   ```

   * Next, define a variable that uses these parameters to generate a unique name:

   ```json theme={null}
   "variables": {
     "name": "[concat(parameters('part'), 'resource')]"
   }
   ```

4. **Define a Resource (e.g., Storage Account)**

   * Use IntelliSense to insert a storage account resource snippet and customize it as needed. For instance, to create a unique storage account name by concatenating a keyword with a variable:

   ```json theme={null}
   "resources": [
     {
       "name": "[concat('st', variables('name'), '001')]",
       "type": "Microsoft.Storage/storageAccounts",
       "apiVersion": "2019-06-01",
       "location": "[parameters('location')]",
       "sku": {
         "name": "Standard_LRS"
       },
       "kind": "StorageV2",
       "tags": {
         "displayName": "StorageAccount"
       },
       "properties": {}
     }
   ]
   ```

5. **Deploy the Template Using PowerShell**

   * Open the PowerShell terminal in Visual Studio Code and log in to your Azure account using device authentication:

   ```powershell theme={null}
   Connect-AzAccount -UseDeviceAuthentication
   ```

   * Set the desired subscription context:

   ```powershell theme={null}
   Set-AzContext -Subscription "Your-Subscription-ID"
   ```

   * Create a new Resource Group if necessary:

   ```powershell theme={null}
   New-AzResourceGroup -Name "ARMdemo" -Location "Central US"
   ```

   * Deploy your ARM template:

   ```powershell theme={null}
   New-AzResourceGroupDeployment -Name "DemoDeployment" -ResourceGroupName "ARMdemo" -TemplateFile "template.json"
   ```

   * If your template uses a separate parameters file, reference that file during the deployment process.

6. **Verify the Deployment**
   * After deployment, open the Azure portal to verify the resource creation. For example, navigate to "Storage accounts" to confirm the storage account's existence, which should reflect the concatenated name as defined in your template.
   * Check the Resource Group's "Deployments" section for detailed deployment logs and the raw template used.

***

## Next Steps: Bicep for Infrastructure as Code

For a more streamlined approach to writing Infrastructure as Code, consider exploring Bicep—a domain-specific language endorsed for its simplicity compared to traditional ARM templates. [Learn more about Bicep here](https://docs.microsoft.com/azure/azure-resource-manager/bicep/).

Happy deploying!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/7f421132-242f-4d10-85e5-6673b7307d12/lesson/28b13698-c6a4-4638-a297-e60fb2ab91d5" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/7f421132-242f-4d10-85e5-6673b7307d12/lesson/88f0dbeb-d7e4-4ffc-a67b-e70eff7e2df5" />
</CardGroup>

---


## Lesson 6: Azure Bicep

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/Azure-Bicep/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Resources/Azure-Bicep/page.md)

**Summary:** Azure Bicep simplifies Azure resource deployment and management with a cleaner syntax, modular files, and enhanced capabilities compared to traditional ARM JSON templates.

# Azure Bicep

> Azure Bicep simplifies Azure resource deployment and management with a cleaner syntax, modular files, and enhanced capabilities compared to traditional ARM JSON templates.

Azure Bicep is a domain-specific language designed to simplify the deployment and management of Azure resources. This guide explains how Azure Bicep streamlines your Azure deployments compared to traditional ARM JSON templates, offering a cleaner syntax and enhanced capabilities.

Azure Bicep files reduce the complexity and clutter inherent in ARM templates by providing a simpler, more intuitive syntax. This allows you to spend less time deciphering code and more time creating and managing robust Azure resources.

## Benefits of Azure Bicep

Azure Bicep enables you to build smaller, modular files while automatically detecting dependencies between resources—minimizing deployment errors that arise when resource relationships are not clearly defined. Additionally, the Visual Studio Code extension offers auto-completion and code snippets, ensuring a smoother authoring experience.

<Frame>
  ![The image lists benefits of using Azure Bicep files, including simpler syntax, smaller module files, auto-detecting dependencies, and a VS Code extension for seamless authoring.](https://kodekloud.com/kk-media/image/upload/v1752884367/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Bicep/azure-bicep-benefits-list.jpg)
</Frame>

Whether you are new to Azure or an experienced cloud professional, leveraging Azure Bicep can transform the way you manage and deploy your cloud infrastructure.

## Example: Storage Account Deployment

### ARM Template Example

Before using Bicep, you might have deployed a storage account using an ARM template. Below is an example JSON snippet that creates a storage account:

```json theme={null}
{
    "name": "[concat('st889', variables('name'))]",
    "type": "Microsoft.Storage/storageAccounts",
    "apiVersion": "2023-01-01",
    "tags": {
        "displayName": "storageaccount1"
    },
    "location": "[parameters('location')]",
    "kind": "StorageV2",
    "sku": {
        "name": "Standard_LRS",
        "tier": "Standard"
    },
    "outputs": {}
}
```

You might deploy this ARM template using PowerShell as shown below:

```powershell theme={null}
PS C:\Users\RithinSkaria\Downloads\arm> New-AzResourceGroupDeployment -Name 'demo-deployment' -ResourceGroupName arm-demo -TemplateFile .\template.json
cmdlet New-AzResourceGroupDeployment at command pipeline position 1
Supply values for the following parameters:
(Type !? for Help.)
New-AzResourceGroupDeployment: Cannot validate argument on parameter 'part'. The character length (2) of the argument is too short. Specify an argument with a length that is greater than or equal to 3 and then try the command again.
PS C:\Users\RithinSkaria\Downloads\arm> New-AzResourceGroupDeployment -Name 'demo-deployment' -ResourceGroupName arm-demo -TemplateFile .\template.json
cmdlet New-AzResourceGroupDeployment at command pipeline position 1
Supply values for the following parameters:
(Type !? for Help.)
part: w45
```

### Converting to Bicep

Converting the above ARM template to Bicep results in a much easier-to-read and maintain code. Compare the following Bicep snippet:

```bicep theme={null}
resource storageAccount 'Microsoft.Storage/storageAccounts@2021-01-01' = {
  name: storageAccountName
  location: location
  tags: {
    displayName: storageAccountName
  }
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
}
```

Use Visual Studio Code with the Bicep extension to create and edit these files. Simply install the extension from the Visual Studio Code marketplace, open a new file, select "Bicep" as the language, and begin authoring your template.

## Defining Parameters, Variables, and Resources

When deploying resources, defining parameters with allowed values and constraints is crucial—in addition to using variables to dynamically build resource names. Consider the following ARM template JSON example:

```json theme={null}
{
  "parameters": {
    "location": {
      "type": "string",
      "allowedValues": [
        "eastus",
        "westus"
      ],
      "defaultValue": "eastus",
      "metadata": {
        "description": "description"
      }
    },
    "part": {
      "type": "string",
      "minLength": 4,
      "maxLength": 7,
      "metadata": {
        "description": "description"
      }
    }
  },
  "variables": {
    "name": "[concat(parameters('part'), 'res')]"
  },
  "resources": [
    {
      "name": "[concat('st889', variables('name'))]",
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2023-01-01",
      "tags": {
        "displayName": "storageaccount1"
      },
      "location": "[parameters('location')]"
    }
  ]
}
```

Below is the equivalent, more concise Bicep version of the same configuration:

```bicep theme={null}
@allowed([
  'eastus'
  'westus'
])
param location string = 'eastus'

@minLength(4)
@maxLength(7)
param part string

var name = '${part}res'

resource storageaccount 'Microsoft.Storage/storageAccounts@2021-02-01' = {
  name: 'st889${name}'
  location: location
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
}
```

In this Bicep snippet, parameters enforce allowed values and string length constraints, while the variable "name" concatenates the `part` parameter with a suffix. The resource declaration then uses these values to create a storage account with a dynamic name.

## Deploying Your Bicep Template

After saving your Bicep file (for example, as storage.bicep), you can deploy it using your preferred method. Remember to install the Bicep CLI manually if you are deploying through PowerShell.

<Callout icon="lightbulb" color="#1CB2FE">
  To deploy using PowerShell, even though ARM deployments require a template file, the process is similar:

  ```powershell theme={null}
  PS C:\Users\RithinSkaria\Downloads\arm> New-AzResourceGroupDeployment -Name 'demo-deployment' -ResourceGroupName arm-demo -TemplateFile .\template.json
  ```
</Callout>

For Azure CLI, deploying a Bicep template is even more straightforward as Azure CLI natively supports the Bicep language. Begin by verifying your active account and subscription:

```plaintext theme={null}
PS C:\Users\RithinSkaria\Downloads\arm> az account list -o table
A few accounts are skipped as they don't have 'Enabled' state. Use '--all' to display them.
Name                      CloudName    SubscriptionId                           TenantId
-----------------------  ------------  --------------------------------------  ------------------------------------
MSDN Firbirh RTN         AzureCloud    548f726b-b5b1-468e-ad45-6e21c4ecf7e7  1e0fa212-37dc-45f5-bb0f-b60687cac64b
Kodekuld Azure Admin - PoC 1 AzureCloud    2cd2d881-8c1e-4c25-be23-a00a708afa7f  1e0fa212-37dc-45f5-bb0f-b60687cac64b
```

Set the appropriate subscription context, then deploy your Bicep template by passing parameters as needed:

```bash theme={null}
az deployment group create --name BYSEP-demo --resource-group arm-demo --template-file storage.bicep --parameters part=BYSEP
```

Upon successful deployment, refresh the storage accounts list in the Azure portal to verify that your storage account has been created.

## Conclusion

This lesson demonstrates how Azure Bicep simplifies resource deployment with its concise syntax, modular design, and integrated tooling in Visual Studio Code. By converting complex ARM JSON templates into more manageable Bicep code, you can streamline and enhance your cloud resource management. Happy deploying!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/7f421132-242f-4d10-85e5-6673b7307d12/lesson/9dbf305e-278b-4812-b7b3-32e7bdb9c1a3" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/7f421132-242f-4d10-85e5-6673b7307d12/lesson/ee6f8050-c244-4b4e-b815-754326e66cfc" />
</CardGroup>

---


# Section 05: Administer Virtual Networking

---


## Lesson 1: Module Introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Module-Introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Module-Introduction/page.md)

**Summary:** This guide explores Azure's networking capabilities, focusing on virtual networks for secure and efficient communication among Azure services.

# Module Introduction

> This guide explores Azure's networking capabilities, focusing on virtual networks for secure and efficient communication among Azure services.

Welcome to the Azure Administrator Virtual Networking module. In this guide, we explore Azure's robust networking capabilities, with a particular focus on how virtual networks enable secure and efficient communication among Azure services.

## Module Objectives

This module is designed to help you master three essential areas:

1. **Configuring Virtual Networks**\
   Discover how to create and manage Azure Virtual Networks. You will learn how to set up IP ranges, subnets, and other critical parameters that establish a controlled and scalable communication environment for your applications and resources.

2. **Configuring Network Security Groups (NSGs)**\
   Gain insights into securing your virtual networks with NSGs. This section covers how to define security rules that allow or deny network traffic, thereby strengthening the overall security posture of your infrastructure.

3. **Configuring Azure DNS**\
   Understand the steps to manage Azure DNS effectively. Learn how to handle domain names and maintain proper name resolution within your Azure environment to ensure your applications remain accessible and performant.

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure you have the required permissions and a valid Azure subscription before beginning the configuration steps in this module.
</Callout>

With these objectives in mind, let's begin by exploring the creation and configuration of Virtual Networks.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/809fc274-7871-4b13-8f85-052b43442c81/lesson/30269f0b-9b5e-4e54-acaf-4e387c49ba44" />
</CardGroup>

---


## Lesson 2: Creating and configuring virtual networks

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Creating-and-configuring-virtual-networks/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Creating-and-configuring-virtual-networks/page.md)

**Summary:** This article explains the creation and configuration of virtual networks in Azure, focusing on their structure, connectivity, and management for secure cloud infrastructure.

# Creating and configuring virtual networks

> This article explains the creation and configuration of virtual networks in Azure, focusing on their structure, connectivity, and management for secure cloud infrastructure.

Virtual networks (VNets) are a cornerstone of cloud infrastructure, providing an isolated network environment that enables the provisioning and management of scalable, secure network resources. In Azure, a VNet is the fundamental building block that allows virtual machines, applications, and other services to communicate safely with each other, with the internet, and with on-premises networks. Essentially, a VNet creates a private section of the cloud dedicated exclusively to your use.

As illustrated in the diagram below, two distinct virtual networks are depicted, each assigned its own address space and divided further into subnets. This design lets you customize your network by defining IP ranges, subnets, route tables, network gateways, and more, effectively replicating the structure of an on-premises network. This capability is especially advantageous for hybrid cloud scenarios.

<Frame>
  ![The image illustrates a diagram of virtual networks, showing two virtual networks with subnets containing Linux and Windows virtual machines, connected to an on-premises setup. It includes a legend explaining symbols for cloud network representation, dedicated instances, hybrid scenarios, and Azure services connectivity.](https://kodekloud.com/kk-media/image/upload/v1752884807/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-and-configuring-virtual-networks/virtual-networks-diagram-linux-windows.jpg)
</Frame>

In many real-world configurations, cloud-based virtual networks connect seamlessly with on-premises networks. While the diagram simplifies this connectivity, additional components such as route tables, VPN Gateways, and often ExpressRoute (covered in advanced materials) typically play a role in establishing secure connections between your cloud resources and on-premises infrastructure.

The flexibility of VNets stands as one of their greatest strengths. By segmenting a VNet into multiple subnets, you can effectively organize and secure your resources. Features like Network Security Groups (NSGs) and traffic routing through a firewall further enable you to tailor your network infrastructure to the specific needs of your applications and workloads.

In the following sections, we will explore how to create virtual networks, configure address spaces and DNS settings, implement route tables, set up hybrid connectivity, and enable communication between virtual networks.

## Virtual Network Overview

A virtual network in Azure is a logical construct that mirrors an on-premises network, yet it exists entirely in the cloud. Each Azure VNet is private and dedicated, with IP addresses drawn from RFC 1918 private ranges (for example, 10.0.0.0/8).

Consider it similar to a home router setup, where your devices (PCs, tablets, smartphones) are assigned IP addresses by a router. Even if adjacent networks use the same default IP range, they remain isolated and independent. In the context of VNets, this separation is maintained even when identical IP ranges are in use across different networks, unless you deliberately establish connectivity through VPN Gateways or similar methods.

VNets enable connectivity for Azure Virtual Machines and services, providing access to both the internet and on-premises networks. The diagram below visually represents these concepts:

<Frame>
  ![The image illustrates virtual network concepts, showing a virtual network with three subnets: GatewaySubnet, frontendSubnet, and databaseSubnet, each with specific IP ranges.](https://kodekloud.com/kk-media/image/upload/v1752884809/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-and-configuring-virtual-networks/virtual-network-subnets-diagram.jpg)
</Frame>

## Key Concepts in Virtual Networks

### 1. Azure Subscription and Regions

Before creating a VNet, you must have an Azure Subscription. Azure services are generally deployed regionally, with each region hosting multiple data centers organized into availability zones to ensure redundancy and high availability. Deploying VNets within a specific region not only maintains data sovereignty but also helps you meet regional regulatory standards.

### 2. Address Space and Subnets

Every VNet in Azure comes with an address space defined by public or more commonly by private IP addresses (typically adhering to RFC 1918). It is crucial to ensure that the VNet's address space does not overlap with those of other VNets or your on-premises network, as overlapping can lead to routing conflicts.

Subnets are logical subdivisions of a VNet, allowing you to partition network resources into manageable segments. You can allocate a portion of the VNet’s IP address range to each subnet and designate them for specific functions—for example:

| Subnet Type      | Typical Usage                                |
| ---------------- | -------------------------------------------- |
| Front-end Subnet | Hosting web servers                          |
| Database Subnet  | Running SQL databases                        |
| Gateway Subnet   | Managing VPN connectivity and other gateways |

### 3. VNet Connectivity

VNets not only facilitate internal secure communication between Azure services but also enable connectivity to on-premises networks and even other cloud providers. This is most often achieved using VPN Gateways or ExpressRoute. While a deep dive into ExpressRoute is available in advanced materials, it is helpful to grasp its basic role in linking cloud resources with on-premises infrastructure.

<Callout icon="lightbulb" color="#1CB2FE">
  When planning your network configuration, ensure that the address space and subnet divisions are carefully designed to avoid overlaps and potential routing conflicts.
</Callout>

In summary, virtual networks are instrumental in:

* Facilitating secure communication between Azure Virtual Machines and services.
* Enabling Azure VMs to access the internet securely.
* Supporting connectivity between cloud-based resources and on-premises networks.

This lesson lays the foundation for a more detailed exploration of these topics. Up next, we will delve into private versus public IP addresses within VNets and analyze how these concepts influence network connectivity and design.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/809fc274-7871-4b13-8f85-052b43442c81/lesson/c3f13966-7b47-405e-b262-94fb412eeda5" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/809fc274-7871-4b13-8f85-052b43442c81/lesson/dbb424ff-711c-4692-9dd2-567bd835ac01" />
</CardGroup>

---


## Lesson 3: Private and Public IP addresses

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Private-and-Public-IP-addresses/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Private-and-Public-IP-addresses/page.md)

**Summary:** This article explores private and public IP addresses in Azure, their allocation methods, and configurations within virtual networks.

# Private and Public IP addresses

> This article explores private and public IP addresses in Azure, their allocation methods, and configurations within virtual networks.

In this article, we explore the concepts of private and public IP addresses, their allocation methods, and how they are utilized within Azure environments. Detailed diagrams illustrate virtual network structures, subnet configurations, and the relationships between private and public IP addresses.

***

## Private IP Addresses

Azure virtual networks are allocated a large private address space defined by a CIDR block (e.g., 192.168.0.0/16). This range forms the backbone for assigning private IP addresses to Azure resources. Within this address space, you can create multiple subnets—such as gateway, front-end, and database subnets—where each resource receives its own private IP, enabling internal communication without exposure to the public internet.

For instance, virtual machines in a front-end subnet might be assigned addresses from the 192.168.1.0/24 range. These private IPs facilitate communication within the network and support interactions with other virtual networks or on-premises systems via VPNs.

There are two methods for assigning private IP addresses:

* **Static Allocation:** Assign a fixed IP address to critical services (e.g., domain controllers, web servers, DNS servers, internal Azure Load Balancer, or Application Gateway). Static allocation guarantees that the IP address remains unchanged after a server reboot.
* **Dynamic Allocation:** Automatically assign an available IP address from the address pool (often using DHCP principles). In this case, when a server restarts and its previous IP is unavailable, a new IP is assigned.

Below is a diagram that illustrates a virtual network with multiple subnets and highlights the allocation methods for IP addresses:

<Frame>
  ![The image illustrates a virtual network with three subnets: GatewaySubnet, frontendSubnet, and databaseSubnet, each with specific IP address ranges. It also mentions allocation methods: static and dynamic.](https://kodekloud.com/kk-media/image/upload/v1752884825/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-and-Public-IP-addresses/virtual-network-subnets-ip-allocation.jpg)
</Frame>

***

## Public IP Addresses

While private IP addresses enable internal communication, they are not routable over the internet. For example, a web service running on a virtual machine with a private IP address (e.g., 192.168.1.4) cannot be directly accessed from the internet. Azure addresses this limitation by using public IP addresses, which allow external access to services.

Public IP addresses can also be allocated either statically or dynamically:

* **Static Public IP Allocation:** Provides an unchanging IP address accessible from the internet.
* **Dynamic Public IP Allocation:** May assign a new IP address upon a system reboot if the previous one is no longer available.

Public IP addresses in Azure come with two SKUs: Basic and Standard. The following table summarizes their key differences:

| Feature                | Basic SKU                              | Standard SKU                                |
| ---------------------- | -------------------------------------- | ------------------------------------------- |
| Allocation Method      | Supports static and dynamic allocation | Supports static allocation only             |
| Security               | Open by default                        | Closed by default; secured using NSGs       |
| Redundancy             | Deployed in a single data center/zone  | Offers zone redundancy                      |
| Resource Attachability | Limited (excludes certain services)    | More flexible; supports additional services |

The diagram below compares the two SKUs and their features:

<Frame>
  ![The image is a comparison chart of public IP address allocation types and SKUs, detailing features like IP allocation, security, resources, and redundancy for Basic and Standard SKUs.](https://kodekloud.com/kk-media/image/upload/v1752884827/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-and-Public-IP-addresses/ip-address-allocation-comparison-chart.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  In enterprise architectures, public IPs are often not assigned directly to individual resources. Instead, traffic is routed through a firewall to provide an extra layer of security, protecting resources against threats like DDoS attacks. For testing or lab environments, however, public IPs may be attached directly to VMs for SSH or RDP access.
</Callout>

***

## Configuring a Virtual Network in Azure

Follow these steps to create and configure a Virtual Network in the Azure portal:

1. **Create a Virtual Network:**\
   Navigate to "Virtual Networks" in the Azure portal and create a new Virtual Network. Choose the appropriate subscription, create a new resource group (for example, "M4"), and select a deployment region.

2. **Configure the Address Space:**\
   By default, Azure might assign an address space like 10.0.0.0/16 for new subscriptions. For on-premises compatibility or to align with previous configurations, remove the default and set the address space to 192.168.0.0/16.

3. **Add a Subnet:**\
   Create a subnet by specifying a name and an IP range. For example, name the subnet "workloads-fe" to designate the front-end subnet. Azure segments the IP range automatically, and you may adjust the subnet mask (e.g., using /24) as needed.

Below is an illustration of the Azure portal interface for creating a Virtual Network, including IP address configuration and subnet settings:

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a virtual network, with options to configure IP addresses and add a subnet. The left side displays the IP address space configuration, while the right side shows the "Add a subnet" settings.](https://kodekloud.com/kk-media/image/upload/v1752884828/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-and-Public-IP-addresses/azure-portal-virtual-network-setup.jpg)
</Frame>

Once you complete these steps, click "Review and Create" to deploy the Virtual Network.

4. **Managing Existing Resources:**\
   For existing virtual machines, inspect the network settings to view both private and public IP configurations:

   * **Private IP Address:** Facilitates internal communication within the Virtual Network.
   * **Public IP Address:** Exposes the VM to the internet.

   To modify these settings, navigate to the VM's networking section in the Azure portal. You can change the private IP allocation method (static or dynamic) or update the public IP assignment.

The following screenshot displays the networking settings for a virtual machine:

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying the networking settings for a virtual machine, including inbound port rules and network interface details.](https://kodekloud.com/kk-media/image/upload/v1752884829/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-and-Public-IP-addresses/azure-portal-network-settings-vm.jpg)
</Frame>

By selecting "IP Configurations," you can view and modify subnet settings, and change the allocation method to static if required. You can also create or associate a new public IP address from this interface.

<Frame>
  ![The image shows a Microsoft Azure portal interface for configuring IP settings of a virtual machine. It includes options for IP forwarding, virtual network selection, and IP configuration details such as IP version, type, and allocation.](https://kodekloud.com/kk-media/image/upload/v1752884830/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-and-Public-IP-addresses/azure-portal-ip-settings-virtual-machine.jpg)
</Frame>

To change the public IP address setup, select the current configuration to modify it— for example, switching to static allocation. Note that from September 30, 2025, Azure Basic public IPs will be retired, leaving only the Standard option available:

<Frame>
  ![The image shows the Microsoft Azure portal interface for configuring IP settings of a virtual machine, with options to add a public IP address and select its configuration.](https://kodekloud.com/kk-media/image/upload/v1752884831/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-and-Public-IP-addresses/azure-portal-ip-settings-virtual-machine-2.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  Remember, a single network interface can be configured with only one public IP address. To assign multiple public IP addresses to a virtual machine, attach an additional network interface.
</Callout>

***

## Conclusion

This article has detailed the essential differences between private and public IP addresses in Azure, including their allocation methods and the distinctions between Basic and Standard public IP SKUs. We also guided you through setting up a Virtual Network, configuring address spaces, and managing subnets and IP addresses.

With this comprehensive understanding, you are now better prepared to manage network configurations in Azure. For more detailed information, consider exploring the official [Azure Networking Documentation](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview).

Happy networking!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/809fc274-7871-4b13-8f85-052b43442c81/lesson/0e1b0d45-5f1a-4fbe-adea-b565037f2047" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/809fc274-7871-4b13-8f85-052b43442c81/lesson/97678ff6-4c6c-45ea-b6b3-e840c7213937" />
</CardGroup>

---


## Lesson 4: Network Security Groups

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Network-Security-Groups/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Network-Security-Groups/page.md)

**Summary:** This article explores Network Security Groups in Azure, detailing their functions, configurations, and integration with Azure Firewall for enhanced network security.

# Network Security Groups

> This article explores Network Security Groups in Azure, detailing their functions, configurations, and integration with Azure Firewall for enhanced network security.

In this article, we explore Network Security Groups (NSGs) in Azure, detailing their core functions, configurations, and how to integrate them with Azure Firewall to achieve layered network security.

Azure provides two primary services for network security:

* **Azure Firewall:** Best for centralized rule and logging management, supporting layer-seven filtering (e.g., by application or Fully Qualified Domain Name).
* **Network Security Groups (NSGs):** Operate at layer four of the OSI model and govern inbound and outbound access to network resources such as network interfaces, subnets, and VMs. NSGs enforce rules based on IP protocol, port number, and address prefix.

<Callout icon="lightbulb" color="#1CB2FE">
  For complex, large-scale environments requiring centralized management, use Azure Firewall. For simpler, resource-level access control, NSGs are ideal. Both services can complement each other to deliver multiple layers of filtering.
</Callout>

***

## Core Functionalities of Network Security Groups

### Filtering Traffic

NSGs monitor the source and destination IP addresses and ports for all inbound and outbound traffic. They then allow or deny traffic according to a set of predefined rules operating at layer four of the OSI model.

### Rule Set

* NSGs contain a prioritized list of rules where each rule specifies whether to allow or deny traffic.
* The priority is defined by a numerical value (lower numbers indicate higher priority).
* For example, a rule with priority 100 is processed before one with priority 400, while default rules typically have values in the 65,000 range.

### Association

An NSG can be associated with both subnets and individual network interfaces. This association strategy allows uniform rule enforcement across a network, while providing the option to override subnet-level rules at the network interface level.

### Evaluation

* Rules applied at both the subnet and NIC levels are evaluated independently.
* Inbound or outbound traffic must be permitted at both levels to successfully reach a resource.

<Frame>
  ![The image is a diagram about Network Security Groups (NSG), showing four components: Filter Traffic, Rule Set, Evaluation, and Association, surrounding a shield icon.](https://kodekloud.com/kk-media/image/upload/v1752884810/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Security-Groups/network-security-groups-diagram.jpg)
</Frame>

The diagram above illustrates that an inbound or outbound packet must be approved by both subnet and NIC NSGs before reaching its destination, thus establishing a secure perimeter around Azure resources.

***

## NSG Rule Attributes

When configuring NSG rules, you specify several attributes to control network traffic:

* **Service:** Define either custom or predefined services (e.g., HTTP, HTTPS, RDP, SSH) for the corresponding open ports.
* **Port Range:** Specify a single port or a range of ports.
* **Priority:** A numerical value (commonly between 100 and 4,096 for custom rules; default rules use values around 65,000) that indicates rule precedence.
* **Action:** Determine whether traffic will be allowed or denied.

<Frame>
  ![The image is a graphic titled "Explore Network Security Groups (NSG)" featuring four colorful icons labeled Service, Priority, Port Range, and Action.](https://kodekloud.com/kk-media/image/upload/v1752884812/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Security-Groups/explore-network-security-groups-icons.jpg)
</Frame>

These attributes empower administrators to craft robust NSG rule sets that effectively manage network traffic and enforce security policies.

***

## NSG Rule Evaluation Example

Consider a virtual network hosting a web server VM within a subnet. An NSG associated at the subnet level governs inbound traffic before it reaches the VM. For instance, to allow HTTP traffic (port 80) to the web server:

1. Create a rule on the subnet NSG permitting traffic on port 80.
2. Optionally, apply an additional NSG rule at the NIC level for further filtering.
3. Traffic is allowed only if both NSGs permit the connection.
4. If either NSG denies the traffic, it is blocked.

For outbound connections initiated from a VM:

* The NIC-level NSG evaluates the traffic first.
* Then, the subnet-level NSG evaluates it.
* The outgoing traffic is allowed only if both NSG levels approve it.

<Frame>
  ![The image illustrates the deployment of Network Security Groups (NSG) within a subnet, showing the flow of HTTP traffic through two NSGs.](https://kodekloud.com/kk-media/image/upload/v1752884813/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Security-Groups/nsg-deployment-http-traffic-diagram.jpg)
</Frame>

This example demonstrates how paired NSG evaluations enforce a secure environment for both inbound and outbound communications.

***

## Configuring and Testing NSGs in Azure

### Deploying the Test Environment

To test NSGs, deploy a set of virtual machines, a virtual network, and NSGs using the provided script. Locate the `nsg-prep-infra.ps1` script in the "050- Administer Virtual Networking" folder of your training materials.

Before running the script, ensure that you are in the correct subscription context. For example:

```powershell theme={null}
PS > cd <path-to-your-training-materials>
PS > cd .\050- Administer Virtual Networking\
PS > ls

    Directory: <your-training-materials-path>\050- Administer Virtual Networking

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         12/7/2023  6:03 PM          2560 nsg-prep-infra.ps1
```

After confirming your context with `Get-AzContext`, run the script:

```powershell theme={null}
PS > .\nsg-prep-infra.ps1
```

The script will create a resource group and deploy four VMs (workload-a-vm-1, workload-a-vm-2, workload-b-vm-1, and workload-b-vm-2) to test NSGs. Verify the deployment through the Azure Portal by checking the VMs and their associated NSGs.

### Verifying NSG Settings via the Azure Portal

1. Open the Azure Portal and navigate to **Virtual Machines** to see the list of four VMs.
2. Select a VM (e.g., workload-a-vm-1) and inspect its **Networking** settings.
3. Notice that an NSG is applied to the network interface, with default rules like:
   * Allow VNet inbound (priority around 65,000).
   * Allow Azure Load Balancer for health probes.
   * Deny all inbound traffic.

These default settings ensure that only permitted traffic (e.g., SSH on port 22) reaches the VM.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a virtual machine named "workload-a-vm-1," including its status, location, operating system, and network information.](https://kodekloud.com/kk-media/image/upload/v1752884814/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Security-Groups/azure-portal-workload-a-vm-1.jpg)
</Frame>

### Establishing Connectivity via SSH

Use the public IP address of a VM (such as workload-a-vm-1) to test connectivity via SSH. Since SSH (port 22) is allowed by default, the connection should succeed. Below is an example SSH session:

```plaintext theme={null}
PS > ssh kodekloud@172.173.168.151
The authenticity of host '172.173.168.151 (172.173.168.151)' can't be established.
ED25519 key fingerprint is SHA256:FgaCDyU+yuqGbyz1RkWrhJTxIlyIZkJqg3P7QzelHyo.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '172.173.168.151' (ED25519) to the list of known hosts.
kodekloud@172.173.168.151's password:
```

After logging in, update the system and install Apache. Change the landing page to display a custom message:

```bash theme={null}
root@workload-a-vm-1:/home/kodekloud# echo "From VM-A-1" > /var/www/html/index.html
```

Verify the update using `curl`:

```bash theme={null}
root@workload-a-vm-1:/home/kodekloud# curl localhost
```

If browsing via the public IP produces no response, it indicates that port 80 is not open. To enable HTTP access, add an inbound NSG rule with the following configuration:

* **Source:** Any
* **Source Port Range:** \*
* **Destination:** Any
* **Service:** HTTP
* **Priority:** 100 (for example)
* **Action:** Allow

After creating the rule, accessing the site via the public IP should reflect the updated index page.

### Advanced NSG Scenario – Denying Specific Traffic

To further refine security, NSG rules can be modified to block specific traffic. For example, to block inbound traffic from a particular IP range (e.g., 192.168.2.0/24, typically corresponding to VMs in subnet B), create a rule with:

* **Action:** Deny
* **Priority:** A value higher than default rules (e.g., 100)

Even though a default rule (priority 65,000) may allow VNet communication, a higher priority deny rule will override this behavior.

<Frame>
  ![The image shows a Microsoft Azure portal interface, specifically the networking settings for a virtual machine named "workload-a-vm-1." It includes configuration details for inbound port rules, with a focus on allowing HTTP traffic from a specified IP range.](https://kodekloud.com/kk-media/image/upload/v1752884816/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Security-Groups/azure-portal-networking-workload-a-vm-1.jpg)
</Frame>

To test the modified rule:

1. SSH into another VM (e.g., workload-b-vm-1) to simulate inter-VM communication.
2. Use `curl` to connect to the IP address of workload-a-vm-1.
3. If the deny rule is active, the connection will be blocked despite system routes allowing communication.

For example:

```bash theme={null}
kodekloud@workload-b-vm-1:~$ curl 192.168.1.4
```

After updating the NSG rule, the connection should fail if the deny policy is correctly enforced.

<Frame>
  ![The image shows the Microsoft Azure portal interface, specifically the networking settings for a virtual machine named "workload-a-vm-1," displaying inbound port rules and network security group details.](https://kodekloud.com/kk-media/image/upload/v1752884817/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Security-Groups/azure-portal-network-settings-workload-a-vm-1.jpg)
</Frame>

For outbound traffic, note that if an inbound rule allows traffic, the corresponding outbound connection is automatically permitted. Outbound traffic that does not match an allow rule will be blocked.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying the networking settings for a virtual machine named "workload-a-vm-1," including outbound port rules and network security group details.](https://kodekloud.com/kk-media/image/upload/v1752884818/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Security-Groups/azure-portal-network-settings-workload-a-vm-1-2.jpg)
</Frame>

***

## Creating a New NSG to Block SSH Traffic

Next, create a new NSG to block SSH traffic at the subnet level, effectively overriding the NIC-level rule that allows SSH by default:

1. In the Azure Portal, create a new NSG (e.g., "block SSH NSG") within the appropriate resource group.
2. Add an inbound rule with the following details to **Deny** SSH (port 22) from any source.
3. Associate the NSG with the target subnet (e.g., subnet B).

Once associated, attempts to SSH into any VM within that subnet will be blocked at the subnet level, bypassing the NIC-level allow rule.

<Frame>
  ![The image shows the Microsoft Azure portal page indicating that a deployment named "Microsoft.NetworkSecurityGroup-20230929123037" is complete. It includes details like the subscription, resource group, and options for further actions.](https://kodekloud.com/kk-media/image/upload/v1752884819/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Security-Groups/azure-portal-deployment-complete.jpg)
</Frame>

<Frame>
  ![The image shows the Microsoft Azure portal displaying inbound security rules for a network security group. It lists rules with details such as priority, name, port, protocol, source, destination, and action (allow or deny).](https://kodekloud.com/kk-media/image/upload/v1752884820/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Security-Groups/azure-portal-inbound-security-rules.jpg)
</Frame>

Test the new configuration by attempting to SSH into a VM from the affected subnet. You should receive a connection error (for example, “connection reset by port 22”), confirming that the NSG rule is blocking SSH traffic.

***

## Augmented Network Security Rules

Augmented NSG rules allow you to specify a range of ports or multiple IP addresses in a single rule. This reduces the complexity and number of individual rules needed.

* Instead of creating separate rules for different ports, list them as comma-separated values or specify a range (e.g., 80-85).
* Similarly, define multiple source IP ranges in one rule (e.g., "192.168.1.0/24,192.168.3.0/24").

This approach enhances manageability and simplifies your NSG configurations.

***

With this comprehensive understanding of NSGs, their evaluation process, and configuration strategies, you are now equipped to manage network traffic and enforce security policies effectively in your Azure environments. Next, we will explore Application Security Groups and how they further extend these capabilities.

For more detailed guidance on Azure networking and security, refer to the following links:

* [Azure Networking Documentation](https://docs.microsoft.com/azure/networking/)
* [Azure Firewall Overview](https://docs.microsoft.com/azure/firewall/overview)
* [Microsoft Azure Security Documentation](https://docs.microsoft.com/azure/security/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/809fc274-7871-4b13-8f85-052b43442c81/lesson/d9e36647-99bc-4e75-9b04-0806991313f3" />
</CardGroup>

---


## Lesson 5: Application Security Groups

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Application-Security-Groups/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Application-Security-Groups/page.md)

**Summary:** Azure Application Security Groups simplify network security management by grouping virtual machines based on application roles instead of IP addresses, enhancing scalability and ease of configuration.

# Application Security Groups

> Azure Application Security Groups simplify network security management by grouping virtual machines based on application roles instead of IP addresses, enhancing scalability and ease of configuration.

Azure Application Security Groups (ASGs) provide a flexible and efficient way to manage network security by grouping virtual machines (VMs) based on their application roles rather than relying on explicit IP addresses. This logical grouping simplifies the configuration of Network Security Groups (NSGs) and streamlines network policy management in dynamic and scalable environments.

## Overview

ASGs enable you to organize your VMs with similar security requirements into logical groups. For example:

* VM1 and VM2, handling front-end duties, belong to an ASG named "web."
* VM3, managing business logic, is grouped under "logic."
* VM4, serving as the database, belongs to an ASG called "DB."

This grouping technique allows you to reference an ASG directly in your NSG rules instead of individual IP addresses, reducing management complexity and easing future modifications.

<Callout icon="lightbulb" color="#1CB2FE">
  Grouping VMs by application roles not only simplifies the creation of security rules but also enhances the overall manageability of your network security posture.
</Callout>

## Practical Scenario

In a typical environment, all communication within the Virtual Network is allowed by default. Suppose you want to restrict internet access such that only the front-end VMs (VM1 and VM2) are accessible externally, while both the logic (VM3) and database (VM4) VMs remain protected from direct internet exposure. Additionally, you may need to ensure that the front-end VMs do not interact directly with the database — only the logic tier should have that privilege.

Using ASGs, you can implement several NSG rules that reference these groups rather than managing each rule by individual IP addresses. This method simplifies rule creation and modification, especially as your network scales.

Below is a network diagram illustrating this setup:

<Frame>
  ![The image is a network diagram illustrating the setup of application security groups within a virtual network, showing connections between virtual machines, subnets, and the internet using specific TCP ports.](https://kodekloud.com/kk-media/image/upload/v1752884794/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Application-Security-Groups/application-security-groups-network-diagram.jpg)
</Frame>

## Configuring ASGs in the Azure Portal

The following steps outline how to configure ASGs using the Azure portal:

1. **Access the Virtual Machine Settings:**

   Begin by opening the networking settings for VM1. In this demonstration:

   * Some predefined rules are temporarily removed to facilitate the setup.
   * SSH is allowed from external sources on VM1.

<Frame>
  ![The image shows a Microsoft Azure portal interface for managing virtual machines, specifically focusing on the networking settings of "workload-a-vm-1." A pop-up is asking to confirm the deletion of a security rule named "Allow\_web."](https://kodekloud.com/kk-media/image/upload/v1752884796/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Application-Security-Groups/azure-portal-vm-network-settings.jpg)
</Frame>

2. **Review Effective Security Rules:**

   ASGs work in harmony with NSGs applied at both the subnet and network interface controller (NIC) levels. When reviewing effective security rules:

   * You may notice that a rule allowing SSH from one source could be overwritten by another that denies SSH at the subnet level.
   * Ensure that conflicting NSG rules are disassociated from the subnet to maintain desired connectivity.

3. **Creating Application Security Groups:**

   With your VMs already running web server workloads (from previous NSG configurations), create logical groups by following these steps:

   * Navigate to the **Application Security Groups** section in the Azure portal.
   * Create a new ASG — for instance, name it "VMs" for your web servers.
   * Similarly, create another ASG for non-web VMs if required.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating an application security group, with fields for project and instance details such as subscription, resource group, name, and region.](https://kodekloud.com/kk-media/image/upload/v1752884797/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Application-Security-Groups/azure-portal-application-security-group.jpg)
</Frame>

4. **Assigning ASGs to Virtual Machines:**

   After creating the ASGs, assign them to the appropriate VMs by navigating to each VM’s networking settings. For example:

   * In the "Networking" section of a non-web VM, locate the "Application Security Groups" area and assign the corresponding ASG.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of an application security group named "b-vms," including its resource group, location, and subscription information. A notification about modifying the network interface is visible in the top right corner.](https://kodekloud.com/kk-media/image/upload/v1752884798/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Application-Security-Groups/azure-portal-application-security-group-2.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Although the Application Security Groups blade displays the groups, actual assignments and modifications occur from within each virtual machine's configuration pane.
</Callout>

5. **Creating Inbound NSG Rules Using ASGs:**

   To control traffic, create inbound NSG rules that reference your ASGs. For example, on VM1:

   * Navigate to the networking settings and add an inbound security rule.
   * Set the source to an Application Security Group (e.g., the ASG for front-end VMs).
   * Specify the destination as a particular IP (e.g., 192.168.1.4) or any VM.
   * Choose a service tag like HTTP or specify a custom port (e.g., port 80).
   * Set the action to "Allow."

<Frame>
  ![The image shows a Microsoft Azure portal interface where a user is configuring networking settings for a virtual machine, specifically adding an inbound security rule.](https://kodekloud.com/kk-media/image/upload/v1752884799/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Application-Security-Groups/azure-portal-networking-settings.jpg)
</Frame>

After adding the rule, refresh the view to verify that traffic from the designated ASG can access the web server.

## Testing the Configuration

Once you have configured ASGs and NSG rules, testing the network setup is crucial to ensure proper security enforcement:

1. Establish an SSH connection into VM1.

2. Execute a connectivity test by using curl against the web server’s IP (e.g., 192.168.1.4):

   ```bash theme={null}
   kodekloud@workload-b-vm-1:~$ curl 192.168.1.4
   ```

3. If VM1 is removed from the ASG that permits web server access, connectivity may still persist due to default virtual network allowances. To enforce a block, create a high-priority NSG rule (using a lower numerical priority value, such as 100) to deny the unwanted traffic. This ensures that once removed from the ASG, the VM will no longer access the web server.

<Callout icon="triangle-alert" color="#FF6B6B">
  Ensure that you test the connectivity after applying rule changes. Improper configurations might expose VMs to unintended access.
</Callout>

## Benefits of Using ASGs with NSGs

Integrating ASGs with NSGs in Azure offers numerous advantages:

* **Streamlined Management:**\
  By referring to logical VM groups instead of individual IPs, rule management becomes more intuitive and less time-consuming.

* **Enhanced Scalability:**\
  ASGs allow you to manage a large number of VMs under common rules, supporting the growth and evolution of your network infrastructure.

* **Simplified Security Administration:**\
  The combined use of ASGs and NSGs reduces the complexity of managing network security, allowing for easier modifications and updates.

* **Seamless Architecture Integration:**\
  Whether your VMs span different subnets, virtual networks, or even subscriptions (connected via peering), ASGs and NSGs can be uniformly applied to maintain a cohesive security framework.

## Conclusion

By leveraging Application Security Groups together with Network Security Groups, you can achieve simplified, scalable, and consistent network security management across your Azure environment. Grouping related virtual machines by roles and referencing these groups in your NSG rules minimizes the overhead associated with manual IP-based configurations.

This comprehensive approach not only boosts security but also enhances operational efficiency, making it an ideal solution for modern, dynamic cloud environments. Thanks for reading!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/809fc274-7871-4b13-8f85-052b43442c81/lesson/09a84e9d-070f-4ac9-88e7-424d3d7fa7bd" />
</CardGroup>

---


## Lesson 6: Azure DNS

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Azure-DNS/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Azure-DNS/page.md)

**Summary:** Azure DNS is a secure and reliable DNS hosting solution that enables accurate name resolution for domains and effective management of DNS infrastructure.

# Azure DNS

> Azure DNS is a secure and reliable DNS hosting solution that enables accurate name resolution for domains and effective management of DNS infrastructure.

Azure DNS is a highly secure and reliable DNS hosting solution by Microsoft Azure. It enables you to host your DNS zones, ensuring accurate name resolution for your domains. Once you create a DNS zone, you can add multiple DNS record sets within that zone to manage your DNS infrastructure effectively.

## DNS Zone Naming Convention

The zone name must be unique within a Resource Group; however, you can have the same zone name in different resource groups. In such cases, each instance of the DNS zone will have its own set of name servers.

## Delegation

Most organizations purchase domains from registrars like Cloudflare, GoDaddy, etc. For example, if you purchase a domain from GoDaddy, it comes with GoDaddy’s default name servers. To use Azure DNS for your domain, delegate DNS queries to the Azure DNS name servers by following these steps:

1. Log in to your domain registrar’s portal (e.g., GoDaddy).
2. Update the name server settings to the provided Azure DNS name servers.
3. Save your configuration.

After completing these changes, client queries are forwarded to the globally distributed Azure DNS name servers, which then respond based on the DNS records present in your Azure DNS zone.

## Record Sets in Azure DNS

Azure DNS supports various types of record sets. Records with the same name and type are grouped into a record set, and every record within the set must be unique. Note that a record set can contain a maximum of 20 records.

## How Azure DNS Works

For instance, in one subscription I manage, there is a DNS zone called KodeKloud.org that is assigned dedicated name servers provided by Microsoft Azure. Within this zone, various DNS records are created, such as an A record for Azure and a CNAME record for Microsoft.

In a typical scenario, you might have an on-premises DNS server with a zone delegated to the Azure DNS name servers. When a client sends a DNS query (using tools like dig or nslookup), the on-premises server forwards the request to the Azure DNS name servers, which then return the necessary DNS response.

### Example Using Dig

```bash theme={null}
oh-my-zsh git:(master) ✗ dig azure.kodekloud.org A
; <<>> DiG 9.16.1-Ubuntu <<>> @ns1-09.azure-dns.com azure.kodekloud.org A
; (2 servers found)
global options: +cmd
;edsandrew: server0: opened: QUERY, status: NOERROR, id: 45278
;; global options: +cmd
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;azure.kodekloud.org.    IN  A

;; ANSWER SECTION:
azure.kodekloud.org. 3600 IN  A 13.11.15.11

;; Query time: 64 msec
;; SERVER: 40.80.69.194#53(40.80.69.194)
;; WHEN: Tue Oct 03 12:49:49 IST 2022
;; MSG SIZE  rcvd: 64
```

<Callout icon="lightbulb" color="#1CB2FE">
  If your domain registrar manages your DNS, update the domain’s name server settings to point to the Azure DNS servers. Otherwise, you might need to manually specify the Azure name servers when performing DNS lookups, or consider purchasing domains directly from Azure for seamless integration.
</Callout>

## Creating a DNS Zone in the Azure Portal

Follow these steps to create a DNS zone in the Azure Portal:

1. Log in to the Azure Portal.
2. Search for "DNS zones" and select the option to create a new zone.
3. Specify your desired resource group (e.g., "demo M4") and provide a zone name (e.g., corecloud.org).

Since DNS zones are global resources, they do not have a specific region. However, the zone metadata will inherit the region from the resource group, even though the DNS records are globally replicated.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a DNS zone, with fields for project and instance details.](https://kodekloud.com/kk-media/image/upload/v1752884800/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-DNS/azure-portal-dns-zone-creation.jpg)
</Frame>

Review your details and then create the DNS zone.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a DNS zone, with details about the subscription, resource group, and location. A notification indicates the initialization of a template deployment.](https://kodekloud.com/kk-media/image/upload/v1752884802/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-DNS/azure-portal-dns-zone-creation-2.jpg)
</Frame>

Once the deployment is complete, you can add DNS records and verify query resolution.

<Frame>
  ![The image shows a Microsoft Azure portal page indicating that a DNS zone deployment is complete, with options to view deployment details and next steps.](https://kodekloud.com/kk-media/image/upload/v1752884803/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-DNS/azure-portal-dns-zone-deployment.jpg)
</Frame>

## Managing DNS Records

After creating your DNS zone, navigate to its resources. You will notice that default records such as SOA and NS are automatically created. You have the option to manually add additional record sets. For example, to add an A record for [www.corecloud.org](http://www.corecloud.org) with IP address 1.1.1.1:

1. Click on "Add record set".
2. Enter the record name (e.g., [www.corecloud.org](http://www.corecloud.org)).
3. Set the record type to A and specify the IP address.
4. Confirm by clicking "OK".

<Frame>
  ![The image shows a Microsoft Azure DNS zone management interface for the domain "kodekloud.org," where a new A record is being added with the IP address "1.1.1.1."](https://kodekloud.com/kk-media/image/upload/v1752884804/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-DNS/azure-dns-zone-kodekloud-a-record.jpg)
</Frame>

Azure DNS supports various other record types as well, such as CAA, CNAME, and more. For instance, if you create a CNAME record so that google.cloud.org points to [www.google.com](http://www.google.com), any DNS queries for google.cloud.org will resolve to [www.google.com](http://www.google.com).

<Frame>
  ![The image shows a Microsoft Azure DNS zone management interface for the domain "kodekloud.org," displaying DNS records such as NS, SOA, CNAME, and A records.](https://kodekloud.com/kk-media/image/upload/v1752884806/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-DNS/azure-dns-zone-management-kodekloud.jpg)
</Frame>

Additionally, you may configure subzones (or child zones) within your DNS zone. For example, configuring azure.corecloud.org as a subzone provides a separate domain space if needed.

## Testing DNS Resolution

To validate your DNS configuration, you can use tools like nslookup. Follow these steps:

1. Open your terminal and run the nslookup command. By default, nslookup might target your localhost DNS server.
2. Use the command prompt to switch to one of the Azure DNS name servers using the "server" directive.

For example, in a Windows PowerShell prompt:

```powershell theme={null}
PS C:\Users\RithinSkaria\Documents\kodekloud-az120\050- Administer Virtual Networking> nslookup
Default Server:  Unknown
Address:  fe80::1

> server ns1-35.azure-dns.com.
```

3. Query a DNS record, such as [www.corecloud.org](http://www.corecloud.org):

```powershell theme={null}
> nslookup www.corecloud.org
Server:  ns1-35.azure-dns.com
Address:  2603:1061:0:10::23
         150.171.10.35

Name:    www.corecloud.org
Address:  1.1.1.1
```

Similarly, you can test a CNAME lookup by setting the query type to CNAME and querying for google.cloud.org, which should resolve to [www.google.com](http://www.google.com), confirming that your DNS zone is correctly configured.

## Private DNS Zones

While this guide focuses on public-facing DNS zones, there are situations where a Private DNS zone is required for internal name resolution. Private DNS zones enable you to resolve the names of internal resources, like virtual machines, to their private IP addresses without exposing those records to the internet.

<Callout icon="lightbulb" color="#1CB2FE">
  For detailed guidance on configuring and using Private DNS zones, refer to the related documentation and best practices for network security.
</Callout>

Thank you for reading this guide on Azure DNS. For more detailed information and updates, consider checking the [Azure DNS documentation](https://docs.microsoft.com/en-us/azure/dns/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/809fc274-7871-4b13-8f85-052b43442c81/lesson/ad4ccf01-7b4f-4286-a403-fcef56ed5505" />
</CardGroup>

---


## Lesson 7: Private DNS Zones

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Private-DNS-Zones/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Virtual-Networking/Private-DNS-Zones/page.md)

**Summary:** This article explores Private DNS Zones in Azure for resolving names to private IP addresses and managing internal resources across virtual networks.

# Private DNS Zones

> This article explores Private DNS Zones in Azure for resolving names to private IP addresses and managing internal resources across virtual networks.

In this guide, we explore Private DNS Zones—a key component for resolving names to private IP addresses and managing internal resources. Unlike public DNS zones used for websites or SharePoint sites, Private DNS Zones provide enhanced name resolution within your private network.

## Overview of Private DNS Zones

Imagine a scenario where your subscription contains two virtual networks (VNet A and VNet B), each with its own address space. Virtual machines (VMs) within a single VNet can automatically resolve names due to Azure’s internal domain configuration. For instance, VM01 in VNet A can easily resolve VM02 within the same network.

However, when you need to resolve names across different VNets—such as resolving VM04 in VNet B from VM01 in VNet A—a standard VNet DNS configuration is insufficient. This is where Private DNS Zones become vital. By creating a Private DNS Zone (for example, kodekloudinternal.com) and linking it to relevant virtual networks, you enable automatic registration and resolution of DNS records across multiple VNets.

An auto-registration feature can be optionally enabled so that any new VM added to the linked networks automatically registers its DNS record.

<Frame>
  ![The image illustrates a diagram of private DNS zones, showing virtual machines (VMs) with their names and IP addresses linked to two virtual networks (vnet-a and vnet-b). It includes a table listing the VMs and their corresponding IPs.](https://kodekloud.com/kk-media/image/upload/v1752884821/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-DNS-Zones/private-dns-zones-vms-diagram.jpg)
</Frame>

Once connected via virtual network links, VMs are able to resolve each other’s names across different networks. For example, VM1 can resolve VM5 and VM6, while VM4 can resolve VM3. Note that this configuration only ensures DNS resolution; actual communication between VMs requires additional settings, like Virtual Network Peering.

## Configuring Private DNS Zones in the Azure Portal

To get started, follow these steps in the Azure Portal:

1. Search for "Private DNS Zones."
2. Create a new DNS zone within the appropriate resource group (e.g., kodecloudinternal.com, sometimes abbreviated as "int" for internal use).

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a Private DNS zone, with fields for project and instance details being filled out.](https://kodekloud.com/kk-media/image/upload/v1752884822/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-DNS-Zones/azure-portal-private-dns-zone.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Private DNS Zones are global resources. You do not need to specify a resource location since the zone’s metadata is stored in the resource group's location.
</Callout>

After creating your DNS zone, you can begin managing virtual machines. For demonstration, we use pre-deployed VMs to verify name resolution using the nslookup command-line tool.

### Example Terminal Session

Upon logging into VM1, you will notice that the DNS configuration file (/etc/resolv.conf) automatically includes an Azure-provided search domain. Next, perform an nslookup to resolve another VM in the same network:

```bash theme={null}
kodekloud@workload-a-vm-1:~$ nslookup workload-a-vm-2
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   workload-a-vm-2.hnv5wu0qur4nejnur5qdmnwrjryh.bx.internal.cloudapp.net
Address: 192.168.1.5
```

This successful resolution occurs because both VMs reside in the same VNet, utilizing Azure's internal DNS. However, attempting to resolve a VM from a different VNet that isn’t registered in the internal domain results in a failure:

```bash theme={null}
kodekloud@workload-a-vm-1:~$ nslookup dns-demo-vm
Server:         127.0.0.53
Address:        127.0.0.53#53

** server can't find dns-demo-vm: SERVFAIL
```

At this point, Private DNS Zones are essential for enabling cross-VNet name resolution.

## Deploying a Virtual Machine via Azure CLI

For testing, let’s deploy a virtual machine using the Azure CLI. First, verify you’re using the correct Azure subscription:

```bash theme={null}
rithin [ ~ ]$ az account show
{
  "environmentName": "AzureCloud",
  "homeTenantId": "1e0fa212-37dc-45fb-bbef-b60867cac64b",
  "id": "5487d26b-b5b1-468e-ad45-6e12acff7e7",
  "isDefault": true,
  "managedByTenants": [],
  "name": "MSDN Firbish RTN",
  "state": "Enabled",
  "tenantId": "1e0fa212-37dc-45fb-bbef-b60867cac64b",
  "user": {
    "cloudShellId": true,
    "name": "rithinskaria@kodekLOUDlab.onmicrosoft.com",
    "type": "user"
  }
}
rithin [ ~ ]$ az account set --subscription "Your_Subscription_ID"
```

Next, create a resource group and deploy the new VM:

```bash theme={null}
az group create -n dns-demo -l "East US"

az vm create -g dns-demo -n dns-demo-vm --image Ubuntu2204 --admin-username kodekloud --admin-password 'WMP5$word12'
```

After deployment, the VM is assigned both private and public IP addresses. You can confirm its status in the "Virtual Machines" section of the Azure Portal.

## Testing DNS Resolution: With and Without Private DNS Zones

Return to your terminal on workload VM1 and run a series of nslookup tests:

```bash theme={null}
kodekloud@workload-a-vm-1:~$ nslookup workload-a-vm-2
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   workload-a-vm-2.hnv5wu0qur4nejnur5qdmnwjryh.bx.internal.cloudapp.net
Address: 192.168.1.5

kodekloud@workload-a-vm-1:~$ nslookup workload-b-vm-2
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   workload-b-vm-2.hnv5wu0qur4nejnur5qdmnwjryh.bx.internal.cloudapp.net
Address: 192.168.2.5

kodekloud@workload-a-vm-1:~$ nslookup dns-demo-vm
Server:         127.0.0.53
Address:        127.0.0.53#53

** server can't find dns-demo-vm: SERVFAIL
```

The nslookup for dns-demo-vm fails because it is not yet registered in the internal domain. This gap is resolved by configuring Private DNS Zones for cross-VNet name resolution.

## Creating Virtual Network Links for Private DNS Zones

To enable automatic DNS record registration across virtual networks, configure virtual network links within your Private DNS Zone:

1. Open your Private DNS Zone in the Azure Portal.
2. Click on "Add" to create a new virtual network link.
   * Provide a descriptive link name (e.g., dnsdemovm\_vnet).
   * Select the appropriate virtual network.
   * Enable auto-registration to allow both new and existing VMs to automatically add their DNS records.
3. Repeat the process for a second virtual network (e.g., vnlvnetworkloads), linking it to your NSG workload VNet.

<Frame>
  ![The image shows a Microsoft Azure portal interface for adding a virtual network link to a private DNS zone. It includes fields for link name, subscription, and virtual network selection.](https://kodekloud.com/kk-media/image/upload/v1752884823/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-DNS-Zones/azure-portal-virtual-network-link.jpg)
</Frame>

After creating the virtual network links, ensure that each displays a "Completed" status. With these links active, DNS records from all linked networks populate automatically in the Private DNS Zone.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying the "Virtual network links" section for a private DNS zone named "kodekloud-int.com," with details about link status, virtual networks, and auto-registration.](https://kodekloud.com/kk-media/image/upload/v1752884823/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-DNS-Zones/azure-portal-virtual-network-links.jpg)
</Frame>

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a private DNS zone for "kodekloud-int.com," including resource group, subscription information, and DNS record sets.](https://kodekloud.com/kk-media/image/upload/v1752884824/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-DNS-Zones/azure-portal-private-dns-zone-2.jpg)
</Frame>

## Verifying Enhanced DNS Resolution

Once the virtual network links are in place and DNS records are updated, test name resolution again from workload VM1:

```bash theme={null}
kodekloud@workload-a-vm-1:~$ nslookup workload-a-vm-2
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   workload-a-vm-2.hnv5wu0qur4nejnur5qdmnwjryh.bx.internal.cloudapp.net
Address: 192.168.1.5

kodekloud@workload-a-vm-1:~$ nslookup workload-b-vm-2
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   workload-b-vm-2.hnv5wu0qur4nejnur5qdmnwjryh.bx.internal.cloudapp.net
Address: 192.168.2.5

kodekloud@workload-a-vm-1:~$ nslookup dns-demo-vm.kodekloud-int.com
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   dns-demo-vm.kodekloud-int.com
Address: 10.0.0.4
```

Now, the dns-demo-vm is successfully resolved within the Private DNS Zone, proving that VMs across linked VNets can discover each other’s DNS records. Remember, while DNS resolution is now improved, the actual inter-VM connectivity requires solutions like Virtual Network Peering.

## Conclusion

Private DNS Zones are essential for managing internal name resolution and establishing secure links between virtual networks without exposing internal IP addresses publicly. In this article, we covered:

* The core concept and benefits of Private DNS Zones.
* How to create a Private DNS Zone using the Azure Portal.
* Deploying a virtual machine via the Azure CLI.
* Configuring virtual network links for automatic DNS registration.
* Verifying improved DNS resolution across different VNets.

For further exploration, upcoming articles will delve into Virtual Network Peering, VPN connectivity, and routing with private endpoints—enhancing your overall understanding of hybrid connectivity in Azure.

Happy learning!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/809fc274-7871-4b13-8f85-052b43442c81/lesson/ebe40b5c-4a2f-49ae-bf69-f95688ad75d8" />
</CardGroup>

---


# Section 06: Administer Intersite Connectivity

---


## Lesson 1: Module Introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Module-Introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Module-Introduction/page.md)

**Summary:** This module teaches how to manage and interlink networking components in Azure for an efficient and secure network environment.

# Module Introduction

> This module teaches how to manage and interlink networking components in Azure for an efficient and secure network environment.

Welcome to the Azure Administrator inter-site connectivity module. In this lesson, you'll discover how to manage and interlink various networking components within Microsoft Azure to create an efficient and secure network environment.

## Lesson Objectives

This module focuses on two main objectives:

1. **Configure Virtual Network Peering (VNet Peering):**\
   Connect two VNets in Azure to enable efficient communication between resources over Microsoft's robust backbone network.

2. **Configure Network Routing and Endpoints:**\
   Explore essential components such as Private Endpoints, Service Endpoints, and Route Tables that help manage and secure your network traffic.

<Frame>
  ![The image lists two learning objectives: configuring VNet peering and configuring network routing and endpoints.](https://kodekloud.com/kk-media/image/upload/v1752884620/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Module-Introduction/vnet-peering-network-routing-objectives.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  This module also covers hybrid networking scenarios, including VPN Gateway, site-to-site, and point-to-site connections. While these topics are not exam requirements, understanding them will further enhance your networking skills.
</Callout>

## Course Benefits

By the end of this lesson, you'll have a comprehensive understanding of Azure networking concepts and best practices. This module is designed to help you build and manage a robust, scalable network infrastructure in Azure—whether you're preparing for certification or seeking to improve your practical skills.

Let's embark on your journey to mastering inter-site connectivity in Azure.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/f7470a91-91f6-4c6c-8a03-565abfeb7aee/lesson/412b7ad0-28ff-4bc9-82ae-469bad6e6694" />
</CardGroup>

---


## Lesson 2: Intersite connectivity

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Intersite-connectivity/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Intersite-connectivity/page.md)

**Summary:** Overview of Azure intersite connectivity options and guidance for choosing between VNet peering, VPN gateways, ExpressRoute, and P2S based on latency, bandwidth, encryption, cost, and topology

# Intersite connectivity

> Overview of Azure intersite connectivity options and guidance for choosing between VNet peering, VPN gateways, ExpressRoute, and P2S based on latency, bandwidth, encryption, cost, and topology

This article explains inter-site connectivity options in Azure and how to choose between them. Two broad categories are covered:

* Azure-to-Azure connectivity (VNet-to-VNet)
* Azure-to-on-premises connectivity

Each option varies by latency, bandwidth, encryption, cost, topology, and management overhead. Below are concise descriptions, comparison tables, and diagrams to help you pick the best approach for your scenario.

## Azure-to-Azure connectivity

Two common ways to connect separate VNets (for example, VNet-A and VNet-B) are VNet Peering and VPN Gateway (VNet-to-VNet).

* By default VNets are isolated. To enable communication you must explicitly connect them.
* Consider region, throughput needs, whether traffic must traverse the public internet, and whether you require encryption in transit for your selection.

Comparison of the two approaches:

| Option                     | How it works                                                                                 | Best for                                                                          | Pros                                                                                         | Cons                                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| VNet Peering               | Direct connection over the Azure backbone between two VNets (same region or global)          | Low-latency, high-throughput intra-Azure connectivity                             | Low latency, high bandwidth, simple, no gateway cost                                         | Requires non-overlapping address spaces; traffic is not encrypted over the internet (stays on Azure backbone) |
| VPN Gateway (VNet-to-VNet) | GatewaySubnet with Azure VPN Gateway establishes IPsec/IKE encrypted tunnel between gateways | Encrypted connectivity across regions or when you need site-to-site-style tunnels | Encrypts traffic end-to-end across public internet; supports cross-region gateway-to-gateway | Higher latency and cost vs peering; requires GatewaySubnet and gateway SKUs                                   |

When to choose which:

* Choose VNet Peering when both VNets are in Azure and you want the lowest latency and highest throughput without extra gateway costs.
* Choose VPN Gateway (VNet-to-VNet) when you need encryption across the public internet, or you must use a gateway topology (for example, transitive scenarios with on-premises integration).

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Intersite-connectivity/intersite-azure-vnet-gateway-peering.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=0a06be15d5bc9674cac57ceb3cac05d9" alt="A network diagram titled &#x22;Intersite Connectivity – Azure-to-Azure Connectivity&#x22; showing two VNets (VNet-A and VNet-B), each containing a GatewaySubnet and a VM Subnet. The VNets are linked via peering and a VNet-to-VNet gateway connection." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Intersite-connectivity/intersite-azure-vnet-gateway-peering.jpg" />
</Frame>

## Azure-to-on-premises connectivity

Connecting Azure VNets to your on-premises network typically uses one of the following methods: Site-to-Site VPN, ExpressRoute, or Point-to-Site (P2S) VPN. Each approach addresses different needs for performance, security, and cost.

| Option                       | How it works                                                                                            | Best for                                                          | Pros                                                                         | Cons                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Site-to-Site VPN (IPsec/IKE) | Azure VPN Gateway in GatewaySubnet establishes IPsec/IKE tunnel to on-prem VPN device over the internet | Secure datacenter-to-Azure connectivity without a private circuit | Encrypted over internet; straightforward to deploy; cost-effective           | Traverses public internet (higher latency and variable throughput) |
| ExpressRoute                 | Dedicated private circuit through a connectivity provider                                               | High-throughput, low-latency enterprise links to Azure            | Private connection (no public internet), SLA-backed, predictable performance | Higher cost; requires provider coordination and provisioning       |
| Point-to-Site (P2S) VPN      | Individual client devices connect to Azure via VPN Gateway (SSTP/OpenVPN/IKEv2)                         | Remote workers, developers, ad-hoc access                         | Simple remote access for users; supports multiple protocols depending on SKU | Not intended for large-scale site connectivity                     |

Guidance:

* Use Site-to-Site VPN when you need encrypted connectivity quickly or cost-effectively.
* Use ExpressRoute when you require predictable performance, large bandwidth, and a private, SLA-backed link.
* Use P2S for remote-user access to resources in Azure without exposing your on-premises network.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Intersite-connectivity/azure-onprem-intersite-vnet-s2s-expressroute.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=1a8bae25ba7028783ff21a84905ded62" alt="A network diagram titled &#x22;Intersite Connectivity – Azure-to-On-Premises Connectivity.&#x22; It shows an Azure VNet with Subnet, GatewaySubnet and ERSubnet connected to an on-premises network via Site-to-Site and ExpressRoute links, plus a Point-to-Site connection for remote users." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Intersite-connectivity/azure-onprem-intersite-vnet-s2s-expressroute.jpg" />
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Key operational notes:

  * GatewaySubnet: When deploying any Azure VPN Gateway (VNet-to-VNet, Site-to-Site, or Point-to-Site), create a subnet named exactly `GatewaySubnet`. Size it according to the gateway SKU you choose. See Azure VPN Gateway guidance: [https://learn.microsoft.com/azure/vpn-gateway/vpn-gateway-about-gateway-subnet](https://learn.microsoft.com/azure/vpn-gateway/vpn-gateway-about-gateway-subnet).
  * VNet Peering: Uses Azure’s private backbone, requires non-overlapping address spaces, and provides low-latency/high-throughput connectivity without explicit gateways.
  * ExpressRoute: Provides a private circuit via connectivity providers—better throughput and latency than internet VPNs but requires provider setup and higher cost.
</Callout>

<Callout icon="warning" color="#FF6B6B">
  Important caveats:

  * VNet Peering does not encrypt traffic across public internet because peering traffic stays on Azure’s backbone; if you require encryption end-to-end, use VPN Gateway (IPsec/IKE) or implement application-level encryption.
  * Address space overlap prevents peering and can complicate routing for all connection types—plan IP addressing to avoid conflicts.
</Callout>

## Quick decision checklist

* Need lowest latency and highest bandwidth within Azure? -> VNet Peering
* Need encrypted site-to-site connectivity across the internet? -> VPN Gateway (Site-to-Site or VNet-to-VNet)
* Need a private, high-throughput connection with SLA? -> ExpressRoute
* Need secure remote access for individual users? -> Point-to-Site VPN

## References and further reading

* Azure VPN Gateway documentation: [https://learn.microsoft.com/azure/vpn-gateway/](https://learn.microsoft.com/azure/vpn-gateway/)
* VNet Peering documentation: [https://learn.microsoft.com/azure/virtual-network/virtual-network-peering-overview](https://learn.microsoft.com/azure/virtual-network/virtual-network-peering-overview)
* ExpressRoute documentation: [https://learn.microsoft.com/azure/expressroute/](https://learn.microsoft.com/azure/expressroute/)
* IPsec/IKE overview: [https://learn.microsoft.com/azure/vpn-gateway/vpn-gateway-about-ipsec](https://learn.microsoft.com/azure/vpn-gateway/vpn-gateway-about-ipsec)

This article introduced the main inter-site connectivity options in Azure. For deeper configuration steps, gateway SKU selection, IPsec/IKE version support, P2S transport protocols, and cost tradeoffs, refer to the linked Microsoft documentation above.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/f7470a91-91f6-4c6c-8a03-565abfeb7aee/lesson/05cb5db3-2482-4b3f-8567-df19b115ce9f" />
</CardGroup>

---


## Lesson 3: Virtual Network Peering

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Virtual-Network-Peering/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Virtual-Network-Peering/page.md)

**Summary:** This article explores Virtual Network Peering in Azure, detailing its benefits, configuration, and a demonstration setup for seamless connectivity between virtual networks.

# Virtual Network Peering

> This article explores Virtual Network Peering in Azure, detailing its benefits, configuration, and a demonstration setup for seamless connectivity between virtual networks.

Virtual Network Peering in Microsoft Azure enables seamless connectivity between separate virtual networks (VNets) as if they were part of a single, unified network. In this guide, you'll explore the concept, benefits, and configuration of Virtual Network Peering, along with a detailed demonstration setup.

## Overview of Virtual Network Peering

Virtual Network Peering simplifies the process of connecting resources across different VNets without the need for additional gateways, hubs, or public internet exposure. There are two primary types of peering:

* **Global VNet Peering:** Connects VNets across different Azure regions.
* **Regional VNet Peering:** Connects VNets within the same Azure region.

Both configurations offer secure, high-speed communication and reduce complexity when managing network architectures.

## Key Benefits and Capabilities

* **High-Speed Data Transfer:** Optimized for robust performance with low latency, ensuring seamless application communication.
* **Utilization of Microsoft Backbone Network:** When peered, data flows over Microsoft’s secure private backbone network instead of the public internet.
* **Seamless Connectivity:** Supports connectivity across VNets in different regions, subscriptions, and even Azure Active Directory tenants, facilitating scalable and resilient network architectures.

<Frame>
  ![The image is an infographic about Virtual Network Peering, highlighting types of peering, high-speed data transfer, use of Microsoft's backbone network, and connectivity across Azure virtual networks.](https://kodekloud.com/kk-media/image/upload/v1752884652/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Virtual-Network-Peering/virtual-network-peering-infographic.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure you have the necessary permissions and network configurations in place before starting the peering setup.
</Callout>

## Demonstration Setup

In this section, we will create an environment using a PowerShell script to test Virtual Network Peering. The provided repository includes a folder named "060-Administer Intersite Connectivity" containing the script `peering-pref-infra.ps1`.

### Setting Up the Environment

Begin by navigating to the correct directory in your terminal:

```powershell theme={null}
PS C:\Users\RithinSkaria\Documents> cd .\kodekloud-az104\
PS C:\Users\RithinSkaria\Documents\kodekloud-az104> cd '.\060-Administer Intersite Connectivity\'
PS C:\Users\RithinSkaria\Documents\kodekloud-az104\060-Administer Intersite Connectivity> ls

    Directory: C:\Users\RithinSkaria\Documents\kodekloud-az104\060-Administer Intersite Connectivity

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        12/8/2023   12:03 PM          1959 peering-pref-infra.ps1
PS C:\Users\RithinSkaria\Documents\kodekloud-az104\060-Administer Intersite Connectivity>
```

Run the script to deploy two Linux virtual machines in separate virtual networks—one in East US and another in West US. After the deployment is complete, verify your Azure context using the command:

```powershell theme={null}
PS C:\Users\RithinSkaria\Documents\kodekloud-az104\060-Administer Intersite Connectivity> Get-AzContext

Name                                                                                                                        
----                                                                                                                        
Kodekloud Azure Admin - PoC 1 (2cd1a8... rithinska... Kodekloud... AzureCloud  1e0fa212...
PS C:\Users\RithinSkaria\Documents\kodekloud-az104\060-Administer Intersite Connectivity>
```

### Testing Connectivity Between Virtual Machines

After deployment, note the IP assignments:

* The East US VM is part of the East US VNet and is assigned the IP address 192.168.0.4.
* The West US VM is in a separate IP range, for instance, 192.168.1.4.

To test connectivity, establish an SSH connection to the East US VM:

```bash theme={null}
PS C:\Users\RithinSkaria\Documents\kodekloud-az104\060-Administer Intersite Connectivity>> ssh kodekloud@172.191.37.104
```

Upon confirming the host's authenticity, the terminal will display the Ubuntu system information for the East US VM:

```bash theme={null}
kodekloud@vm-eus:~$
```

Next, try to ping the West US VM from the East US VM:

```bash theme={null}
kodekloud@vm-eus:~$ ping 192.168.1.4
PING 192.168.1.4 (192.168.1.4) 56(84) bytes of data.
```

At this point, the ping will fail because the two VNets have not yet been peered.

## Configuring Virtual Network Peering

To establish a peering connection:

1. Open the Azure portal and navigate to the **Virtual Network** section of either the East US or West US VNet.
2. Select the **Peerings** option.
3. Follow these steps:
   * Click **Add peering**.
   * Enter a link name (e.g., "USWS link").
   * Configure the following settings:
     * Allow VNets to access the peered network: Yes.
     * Allow the VNET (West US) to receive forwarded traffic from the peered network: Yes.
     * Optionally enable Gateway Transit (this is not required for the demonstration).
   * For the remote virtual network, select the corresponding VNet (e.g., "WUS US link") and enable forwarded traffic.
   * Click **Add** to create the peering connection.

<Callout icon="lightbulb" color="#1CB2FE">
  Both VNets must be configured simultaneously for peering to work correctly. The settings ensure secure data flow between the networks.
</Callout>

<Frame>
  ![The image shows the Microsoft Azure portal interface, specifically the "Peerings" section for a virtual network named "vnet-wus," with a peering status of "Initiated" to "vnet-eus." Notifications indicate successful addition of virtual network peering.](https://kodekloud.com/kk-media/image/upload/v1752884653/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Virtual-Network-Peering/azure-portal-peerings-vnet-wus.jpg)
</Frame>

### Verifying the Peering Connection

After configuring peering, return to the SSH session on the East US VM. The previously unsuccessful ping to the West US VM should now succeed. Additionally, you can initiate an SSH connection between the two VMs using their internal IP addresses (e.g., connecting from 192.168.0.4 to 192.168.1.4).

By default, the Network Security Group (NSG) rule "Allow VNET inbound" permits traffic between peered VNets. There is no need to manually open additional ports unless custom traffic rules are required.

## Conclusion

This guide demonstrated the end-to-end process of setting up Virtual Network Peering in Azure, from deploying virtual machines in separate regions to configuring and verifying secure connectivity through peering.

Stay tuned for the next section, which will cover setting up a VPN Gateway for advanced connectivity scenarios.

Happy learning!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/f7470a91-91f6-4c6c-8a03-565abfeb7aee/lesson/ecfc5c37-65e2-497a-a222-57dafad279dc" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/f7470a91-91f6-4c6c-8a03-565abfeb7aee/lesson/628f77b7-26bd-4d3f-a13d-41811b13bc5a" />
</CardGroup>

---


## Lesson 4: VPN Gateway

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/VPN-Gateway/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/VPN-Gateway/page.md)

**Summary:** VPN Gateways facilitate connectivity within and between Azure virtual networks, supporting VNet-to-VNet, Site-to-Site, and Point-to-Site connections to on-premises infrastructures.

# VPN Gateway

> VPN Gateways facilitate connectivity within and between Azure virtual networks, supporting VNet-to-VNet, Site-to-Site, and Point-to-Site connections to on-premises infrastructures.

VPN Gateways enable various types of connectivity within and between Azure virtual networks (VNets). They can establish VNet-to-VNet connections as well as Site-to-Site and Point-to-Site connections to on-premises infrastructures.

<Frame>
  ![The image illustrates a VPN Gateway setup, showing connections between virtual networks (VNet-A and VNet-B) and point-to-site and site-to-site connections to locations labeled LON and NYC.](https://kodekloud.com/kk-media/image/upload/v1752884648/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-VPN-Gateway/vpn-gateway-setup-vnet-connections.jpg)
</Frame>

In the architecture depicted above, VNet A is configured with a VPN Gateway (also known as a virtual network gateway) and connected to VNet B via a VNet-to-VNet connection. It is important to note that both VNets must have their own gateway to establish this connection—a key difference from VNet peering, which does not require a gateway on both sides. For example, VNet A can serve the London office using its Site-to-Site connection, while VNet B serves the New York office; the New York office can access VNet A through the established connectivity.

<Callout icon="lightbulb" color="#1CB2FE">
  Understanding VPN Gateway concepts is crucial, as they serve as the foundation for Gateway Transit—a concept that is particularly relevant for exam scenarios.
</Callout>

There are multiple SKUs available for VPN Gateways, including Generation 1 (Gen 1) and Generation 2 (Gen 2), with some SKUs even supporting zone redundancy. The SKU selection depends on the number of required connections and throughput needs. Within the same generation, a VPN Gateway can be resized (for instance, from a Gen 1 GW1 to a Gen 1 GW2). However, resizing between generations (from Gen 1 to Gen 2) is not supported and requires the gateway to be completely redeployed. Additionally, a Basic SKU is available; however, it is considered legacy and is not recommended for production environments.

To set up a VNet-to-VNet connection using VPN gateways, ensure that each VNet has a dedicated gateway subnet. The process involves three major steps:

1. Create a gateway subnet in each VNet.
2. Deploy a VPN Gateway in each virtual network.
3. Establish the VNet-to-VNet connection between the two gateways.

<Frame>
  ![The image is a diagram illustrating the steps for creating a VNet-to-VNet connection, including creating a gateway subnet, creating the VPN gateway, and establishing the VPN connection.](https://kodekloud.com/kk-media/image/upload/v1752884649/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-VPN-Gateway/vnet-to-vnet-connection-diagram.jpg)
</Frame>

Many organizations continue to use VPN Gateways, largely due to their built-in encryption capabilities. The following section provides a detailed comparison between VNet peering and VNet-to-VNet connections.

## Comparison Between VNet Peering and VNet-to-VNet Connections

| Feature                   | VNet Peering                                                                                                                                    | VNet-to-VNet Connection                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Number of Connections** | Supports up to 500 peerings per VNet. For example, VNet A can peer with VNets B, C, D, etc.                                                     | Supports a single VPN Gateway per VNet, but a gateway can handle multiple connections as determined by the SKU (up to 300 in some cases).                   |
| **Pricing**               | Only data ingress and egress charges apply; you pay solely for data transfers.                                                                  | In addition to data egress charges, there is an hourly cost for the gateway, regardless of active usage.                                                    |
| **Encryption**            | Lacks built-in encryption; however, software-level encryption can be implemented.                                                               | Offers built-in encryption using IPsec or Internet Key Exchange (IKE), making it ideal for scenarios where encryption is mandatory.                         |
| **Bandwidth**             | Utilizes Microsoft’s backbone network without bandwidth restrictions; suitable for high data transfers with low latency.                        | Bandwidth is determined by the chosen SKU, with higher-end SKUs offering up to 10 Gbps.                                                                     |
| **Routing**               | Traffic is routed through Microsoft’s backbone network, ensuring fast and private connectivity.                                                 | Uses the public internet via an encrypted VPN tunnel, which may affect performance depending on the SKU and network conditions.                             |
| **Public IP Requirement** | Does not require public IP addresses as traffic remains within the Microsoft backbone.                                                          | Requires a public IP for the deployment of the virtual network gateway.                                                                                     |
| **Transitivity**          | Non-transitive; for example, if VNet A peers with VNet B and VNet B peers with VNet C, connectivity between VNet A and VNet C is not automatic. | Can be configured as transitive with Border Gateway Protocol (BGP) enabled, allowing routes from other networks to be published and used for communication. |
| **Initial Setup Time**    | Can be configured rapidly.                                                                                                                      | Takes between 30 to 40 minutes per VPN gateway. With two gateways, expect an overall deployment time of around 45 to 50 minutes.                            |
| **Use Cases**             | Ideal for data replication, failover, and large-scale backups due to its high-speed, low-latency connectivity.                                  | Preferred in environments where encryption is critical, despite reliance on the public internet and SKU-dependent performance.                              |

<Frame>
  ![The image is a comparison table between VNet Peering and VNet-to-VNet Connection, detailing properties such as number of connections, pricing, encryption, bandwidth, route, public IP, transitivity, initial setup time, and use cases.](https://kodekloud.com/kk-media/image/upload/v1752884651/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-VPN-Gateway/vnet-peering-vnet-connection-comparison.jpg)
</Frame>

This detailed comparison outlines the key differences between VNet peering and VNet-to-VNet connections. In the following sections, we will explore Site-to-Site and Point-to-Site connections to further expand on VPN connectivity solutions.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/f7470a91-91f6-4c6c-8a03-565abfeb7aee/lesson/7d9abfa9-71b9-49d3-a7a7-947e5b8a9ba7" />
</CardGroup>

---


## Lesson 5: Site to Site and Point to Site

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Site-to-Site-and-Point-to-Site/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Site-to-Site-and-Point-to-Site/page.md)

**Summary:** This guide explains how to set up Site-to-Site and Point-to-Site VPN connections in Azure, detailing resources, configurations, and procedures for secure connectivity.

# Site to Site and Point to Site

> This guide explains how to set up Site-to-Site and Point-to-Site VPN connections in Azure, detailing resources, configurations, and procedures for secure connectivity.

This guide details how to establish both Site-to-Site and Point-to-Site VPN connections in Azure. It covers the required resources, configurations, and step-by-step procedures for securely linking your on-premises network or individual devices to an Azure Virtual Network.

***

## Site-to-Site Connection

A Site-to-Site connection creates a secure VPN tunnel between your on-premises VPN device and an Azure VPN Gateway in your Virtual Network Gateway subnet. This setup enables seamless data transfer between your local environment and Azure as if they were part of the same network.

### Key Components

1. **Gateway Subnet**\
   Begin by creating a dedicated gateway subnet within your Virtual Network (VNet) in Azure. This subnet is exclusively reserved for the Azure Virtual Network Gateway.

2. **Virtual Network Gateway (VPN Gateway)**\
   Deployed within the gateway subnet, the VPN Gateway encrypts and decrypts data, maintains the VPN tunnel, and manages the connectivity between Azure and on-premises resources.

3. **Local Network Gateway**\
   This resource acts as a reference for your on-premises VPN device by storing its public IP address and address range. For example, if your on-premises device has an IP address of 13.12.11.11, configure the Local Network Gateway to reference this IP accordingly.

4. **On-Premises VPN Device**\
   The VPN appliance (either physical or virtual) on your local network must be configured to align with the Azure VPN Gateway settings. Once the Site-to-Site connection is established, the Azure VPN Gateway and your on-premises VPN device communicate to form a secure tunnel.

The diagram below illustrates the overall architecture of a Site-to-Site VPN connection, including the gateway subnet, VPN gateway, local network gateway, and the on-premises VPN device:

<Frame>
  ![The image is a diagram illustrating a site-to-site connection, showing components like a gateway subnet, VPN gateway, local network gateway, on-premises VPN device, and the site-to-site connection.](https://kodekloud.com/kk-media/image/upload/v1752884639/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Site-to-Site-and-Point-to-Site/site-to-site-connection-diagram.jpg)
</Frame>

### Setting Up a Site-to-Site Connection

1. **Configure the Virtual Network Gateway:**\
   In the Azure portal, navigate to your Virtual Network Gateway. Although the creation process for the Virtual Network Gateway is outside the scope of this guide, reviewing its configuration can help you understand the overall setup.

2. **Add a Connection:**\
   Under the "Connections" section of the Virtual Network Gateway, click on "Add connection." You can choose between a VNet-to-VNet connection (for connecting to another VNet) or a Site-to-Site connection. For this guide, select Site-to-Site and assign a suitable name (e.g., "Demo Site-to-Site East US").

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a connection, with fields for project and instance details such as subscription, resource group, connection type, name, and region. The "Review + create" and "Next: Settings" buttons are visible at the bottom.](https://kodekloud.com/kk-media/image/upload/v1752884641/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Site-to-Site-and-Point-to-Site/azure-portal-connection-setup.jpg)
</Frame>

3. **Configure Connection Settings:**\
   In the next step, select the appropriate Virtual Network Gateway and reference the Local Network Gateway. Provide details such as the public IP address (or FQDN) of your on-premises VPN device and its served address range.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a connection, with settings for a virtual network gateway and a search for "local network gateways" in progress.](https://kodekloud.com/kk-media/image/upload/v1752884642/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Site-to-Site-and-Point-to-Site/azure-portal-virtual-network-gateway.jpg)
</Frame>

4. **Finalize the Connection:**\
   Specify additional parameters such as BGP (if needed), private IP addressing, policy settings, and connection modes. Make sure these settings are mirrored on your on-premises VPN device. After reviewing and confirming all settings, the Site-to-Site VPN connection will be established.

***

## Point-to-Site Connection

A Point-to-Site connection is designed for individual devices to securely connect to an Azure VNet, creating a virtual experience that mimics being physically present within an Azure data center. This connection is ideal for remote workers, developers, and IT professionals requiring on-demand access to Azure resources.

### Overview of the Setup Process

1. **Gateway Subnet and VPN Gateway:**\
   Like the Site-to-Site setup, a Point-to-Site connection requires an existing gateway subnet and Virtual Network Gateway.

2. **Point-to-Site VPN Configuration:**\
   Within the Azure portal, configure the VPN client settings by specifying an address pool for VPN clients, choosing a tunnel type (such as IKEv2, OpenVPN, or SSTP), and selecting an authentication method. Supported authentication methods include Azure Certificate Authentication, RADIUS Authentication, and Azure Active Directory integration. If you opt for Azure Active Directory, provide the tenant ID, audience, and issuer details as outlined in the official documentation.

3. **Download and Install the VPN Client:**\
   After finalizing the Point-to-Site configuration, download the VPN client package from the Azure portal. Windows users can opt for the "Azure VPN" app available in the Windows Store. Once installed, import the configuration details and connect to the Azure VNet securely.

The flowchart below outlines the key steps involved in establishing a Point-to-Site VPN connection:

<Frame>
  ![The image is a flowchart illustrating the steps for a Point-to-Site Connection, including Gateway Subnet, VPN Gateway, P2S Configuration, Download, and Connect.](https://kodekloud.com/kk-media/image/upload/v1752884643/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Site-to-Site-and-Point-to-Site/point-to-site-connection-flowchart.jpg)
</Frame>

### Demonstration in the Azure Portal

1. **Access Point-to-Site Configuration:**\
   In the Virtual Network Gateway settings of the Azure portal, navigate to the "Point-to-Site configuration" tab (instead of "Connections"). Click on "Configure now" to begin setting up the connection.

2. **Set Up VPN Client Settings:**\
   Enter the necessary details, such as the address pool for connected clients, preferred tunnel type, and selected authentication method. After saving these settings, download the VPN client configuration.

3. **Connect to Azure:**\
   Install and launch the VPN client on your device. Use the provided settings to establish a secure connection to your Azure Virtual Network. Once connected, you can access Azure virtual machines and other resources as if they were part of your local network.

<Callout icon="lightbulb" color="#1CB2FE">
  For enhanced security, ensure that the configurations on your on-premises VPN device precisely match the settings in the Azure portal.
</Callout>

***

## Gateway Transit

Both Site-to-Site and Point-to-Site VPN connections leverage Gateway Transit. This feature allows on-premises networks and remote clients to extend the secure connection established by the Azure VPN Gateway. Implementing Gateway Transit ensures that all connected devices benefit from robust, secure connectivity.

Happy networking!

For further reading on Azure VPN solutions, consider reviewing the [Azure VPN Gateway documentation](https://learn.microsoft.com/en-us/azure/vpn-gateway/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/f7470a91-91f6-4c6c-8a03-565abfeb7aee/lesson/e60f2c26-54e6-4fb1-b01d-0004a230d439" />
</CardGroup>

---


## Lesson 6: Gateway Transit

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Gateway-Transit/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Gateway-Transit/page.md)

**Summary:** Gateway Transit simplifies network connectivity in Azure by using a single virtual network gateway for multiple VNets, reducing complexity and operational costs.

# Gateway Transit

> Gateway Transit simplifies network connectivity in Azure by using a single virtual network gateway for multiple VNets, reducing complexity and operational costs.

## Overview

Gateway Transit is an Azure feature that simplifies network connectivity by using a single, shared, peered virtual network gateway rather than provisioning individual gateways for each virtual network (VNet). This design not only streamlines connectivity but also reduces management overhead and operational expenses.

Imagine you have three virtual networks—VNet A, VNet B, and VNet C—along with your on-premises network for developers. Traditionally, every VNet would require its own VPN gateway for a site-to-site connection to the on-premises network. This conventional approach leads to several challenges:

* **Redundancy and Complexity:** Managing separate VPN gateways for each VNet increases complexity and the risk of misconfigurations.
* **Cost:** Multiple VPN gateways incur additional charges, raising operational expenses.
* **Resource Utilization:** Valuable resources are tied up managing multiple gateways instead of being efficiently deployed elsewhere.

<Callout icon="lightbulb" color="#1CB2FE">
  Gateway Transit centralizes connectivity by using a hub-and-spoke design. Instead of establishing direct site-to-site connections from every VNet, each connects via peering to a central hub where a single virtual network gateway handles the connection to the on-premises network.
</Callout>

### Hub-and-Spoke Architecture

In a Gateway Transit configuration, the hub VNet contains a single VPN gateway connected via a site-to-site link to the on-premises network. The benefits of this approach include:

* **Centralized Management:** Simplifies network topology with a single control point.
* **Reduced Complexity:** Eliminates the need for multiple individual gateways.
* **Cost Efficiency:** Reduces operational costs by requiring only one VPN gateway.
* **Resource Optimization:** Allows spoke VNets to allocate resources to other tasks.
* **Streamlined Connectivity:** Provides a low-latency path for inter-network traffic.

The diagram below illustrates the hub-and-spoke network architecture for Gateway Transit:

<Frame>
  ![The image illustrates a network architecture for "Gateway Transit," showing multiple virtual networks (VNet-A, VNet-B, VNet-C) connected through a hub VNet with peering, and an on-premises network connected via site-to-site (S2S) VPN.](https://kodekloud.com/kk-media/image/upload/v1752884611/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Gateway-Transit/gateway-transit-network-architecture.jpg)
</Frame>

This architecture is a best practice in Azure landing zones and supports scalability, high performance, and effective cost management.

### Demo Walkthrough: Point-to-Site VPN Connection

In this lesson, we demonstrate a point-to-site VPN connection, which allows direct access to Azure virtual machines over a private IP connection. The demo involves several configuration steps:

1. **Configure Point-to-Site VPN:**\
   Within Azure, a point-to-site VPN connection is set up using Azure Active Directory authentication.

2. **Establish VNet Peering:**\
   A peering is created between the virtual network in East US (host to a VM) and the hub VNet that contains the VPN gateway. Gateway transit is enabled in the peering settings to properly route traffic to on-premises networks or other destinations.

The Azure portal displays the point-to-site VPN configuration as follows:

<Frame>
  ![The image shows a Microsoft Azure portal page for configuring a point-to-site VPN connection. It includes settings for address pool, tunnel type, and Azure Active Directory authentication.](https://kodekloud.com/kk-media/image/upload/v1752884613/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Gateway-Transit/azure-portal-point-to-site-vpn.jpg)
</Frame>

The following screenshot confirms the peering connection with the VPN gateway:

<Frame>
  ![The image shows the Microsoft Azure portal displaying the "Peerings" section of a virtual network, listing two connected peerings with their statuses and gateway transit settings.](https://kodekloud.com/kk-media/image/upload/v1752884615/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Gateway-Transit/azure-portal-peerings-virtual-network.jpg)
</Frame>

The next image illustrates the gateway transit configuration details in the peering setup:

<Frame>
  ![The image shows a Microsoft Azure portal page for configuring a virtual network peering named "eus-hub," with options for network access and traffic forwarding settings.](https://kodekloud.com/kk-media/image/upload/v1752884616/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Gateway-Transit/azure-portal-virtual-network-peering.jpg)
</Frame>

After configuring the connection, you can establish a point-to-site session using the Azure VPN Client. The following image shows the VPN connection interface and status logs:

<Frame>
  ![The image shows a Microsoft Azure portal with a VPN connection interface. It displays connection properties and status logs for a VPN named "intersite-vnet."](https://kodekloud.com/kk-media/image/upload/v1752884618/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Gateway-Transit/azure-portal-vpn-connection-interface.jpg)
</Frame>

### Verifying Connectivity

Below is an example demonstration using a Linux terminal. The steps show how to verify connectivity by pinging an Azure virtual machine and establishing an SSH connection over a private IP.

```bash theme={null}
kodekLOUD@vm-eus:~$ ping 192.168.1.4
64 bytes from 192.168.1.4: icmp_seq=120 ttl=64 time=72.8 ms
64 bytes from 192.168.1.4: icmp_seq=121 ttl=64 time=72.4 ms
64 bytes from 192.168.1.4: icmp_seq=122 ttl=64 time=72.3 ms
--- 192.168.1.4 ping statistics ---
12 packets transmitted, 12 received, 0.163% packet loss, time 123604ms
rtt min/avg/max/mdev = 72.338/72.841/75.112/0.729 ms

kodekLOUD@vm-eus:~$ ip address
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host
    inet6 ::1/128 scope host
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default
    link/ether 00:0d:34:55:89:36 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.4/24 brd 192.168.0.255 scope global eth0
    inet6 fe80::20d:3aff:fe55:8936/64 scope link

kodekLOUD@vm-eus:~$ ssh kodekLOUD@192.168.1.4
The authenticity of host '192.168.1.4 (192.168.1.4)' can't be established.
ED25519 key fingerprint is SHA256:gwSm0n3l4fYqCQVYGHYMN0wFbduhdUwJ4K/9Co9Gs.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.1.4' (ED25519) to the list of known hosts.
kodekLOUD@192.168.1.4's password:
```

A similar process can be executed in a Windows environment using PowerShell. Use the following command to establish an SSH connection over the private IP:

```bash theme={null}
PS C:\> ssh kodekloud@192.168.0.4
The authenticity of host '192.168.0.4 (192.168.0.4)' can't be established.
ED25519 key fingerprint is SHA256:tQXst535TmKurM5PHX5ZTozvQskMiiJ4VLnFdjy/70.
This host key is known by the following other names/addresses:
    C:\Users\RithinSkaria\.ssh\known_hosts:54: 172.191.37.104
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
kodekloud@192.168.0.4's password:
```

After connecting, verify network connectivity by running a ping command:

```bash theme={null}
PS C:\> ping 192.168.0.4

Pinging 192.168.0.4 with 32 bytes of data:
Reply from 192.168.0.4: bytes=32 time=199ms TTL=64
Reply from 192.168.0.4: bytes=32 time=198ms TTL=64
Reply from 192.168.0.4: bytes=32 time=197ms TTL=64

Ping statistics for 192.168.0.4:
    Packets: Sent = 3, Received = 3, Lost = 0 (0% loss)
Approximate round trip times in milli-seconds:
    Minimum = 197ms, Maximum = 199ms, Average = 198ms
```

<Callout icon="lightbulb" color="#1CB2FE">
  By setting up a point-to-site connection to the virtual network gateway, you enable routing through a peered virtual network using Gateway Transit. As a result, VNets A, B, and C can securely access on-premises resources through a single, centralized gateway.
</Callout>

With the Gateway Transit configuration successfully completed, the next topic in this lesson will cover user-defined routes. This further enhances network routing by allowing more granular control over traffic flows across your Azure environment.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/f7470a91-91f6-4c6c-8a03-565abfeb7aee/lesson/d33994fa-dd8c-45a7-932a-dcb86124a01b" />
</CardGroup>

---


## Lesson 7: User Defined Routes

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/User-Defined-Routes/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/User-Defined-Routes/page.md)

**Summary:** This article explains User-Defined Routes in Azure for managing inter-site connectivity and advanced traffic control.

# User Defined Routes

> This article explains User-Defined Routes in Azure for managing inter-site connectivity and advanced traffic control.

This article explains how User-Defined Routes (UDRs) work in Azure, compares them with default system routes, and shows how they can be applied to manage inter-site connectivity for advanced traffic control.

Azure automatically includes a set of system routes that allow most networking scenarios. These routes enable virtual machines (VMs) and other resources within the same virtual network to communicate and access the internet for outbound traffic. However, when you need enhanced control over traffic—such as directing traffic through a network virtual appliance (NVA) for security or inspection—you must implement custom routing policies using UDRs.

## Virtual Network Traffic and System Routes

By default, system routes allow seamless communication between VMs in the same subnet or across subnets within a virtual network. For example:

* VMs within the same subnet can ping one another.
* VMs can access external resources (like NTP servers or Windows updates) using outbound connectivity.

Keep in mind that these system routes govern outbound connections initiated by VMs. Inbound connectivity from the internet is restricted by Network Security Groups (NSGs) and is typically disabled by default.

## When to Use User-Defined Routes

Imagine a scenario where traffic from a frontend subnet must communicate with a database subnet. Normally, system routes would enable direct connectivity between these subnets. However, if your organization’s security policy requires that all traffic from the frontend to the database passes through an NVA (acting as a firewall), then default routing is insufficient.

To enforce this level of security:

1. Create a route table to redirect traffic from the frontend subnet to the NVA’s IP address.
2. Associate the route table with the frontend subnet.
3. Ensure there is a peering connection between the virtual network containing the frontend and database subnets and the network where the NVA is deployed.

The diagram below illustrates this setup:

<Frame>
  ![The image illustrates a network diagram showing user-defined routes with a DMZ subnet, frontend subnet, and database subnet within virtual networks. It includes a route table and network virtual appliance (NVA) for managing traffic flow.](https://kodekloud.com/kk-media/image/upload/v1752884645/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-User-Defined-Routes/network-diagram-user-routes-dmz.jpg)
</Frame>

After associating the route table with the frontend subnet, all outbound traffic destined for the database subnet is routed through the NVA. The NVA inspects and then forwards the traffic to the database subnet—an extra layer of security that system routes alone cannot provide.

## Creating a Route Table in the Azure Portal

To configure a UDR in the Azure portal, follow these steps:

1. Sign in to the Azure portal and search for "Route table".
2. Create a new route table. For example, you could use a resource group named "inter-site" and name your route table "RT-inter-site".
3. Enable the "Propagate gateway routes" option to automatically include routes learned from connected gateways.
4. Once deployed, you can add one or more user-defined routes to the table.

After deployment, the portal displays a confirmation message similar to the following:

<Frame>
  ![The image shows a Microsoft Azure portal page indicating that a deployment named "Microsoft.RouteTable-20231208142724" is complete. It includes options to view deployment details and next steps, with a "Go to resource" button.](https://kodekloud.com/kk-media/image/upload/v1752884646/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-User-Defined-Routes/azure-portal-deployment-complete.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  After deployment, review the deployment details to ensure your route table is configured correctly before association.
</Callout>

### Associating the Route Table with a Subnet

1. In the Azure portal, select your newly created route table and click on "Associate".
2. Choose the appropriate virtual network and subnet (for example, the default subnet).
3. Associating the route table with the subnet ensures that all traffic from that subnet follows the defined routing rules.

### Adding User-Defined Routes

Suppose you want all traffic from the associated subnet to route through a firewall. To add a specific route:

1. Click on "Routes" within the route table and then click "Add".
2. Create a route (e.g., name it "all traffic firewall") with these settings:
   * Destination Type: IP address
   * Destination IP address range: 0.0.0.0/0 (to capture all traffic)
   * Next Hop Type: Virtual Appliance
   * Next Hop IP Address: Enter the IP address of your firewall (e.g., 15.1.x.x)

This route forces all outbound traffic from the subnet to pass through your firewall for inspection.

If further segmentation is needed, you can add additional routes. For example, to add a route for internal traffic:

1. Click "Add" again within the route table.
2. Create a route named "internal" with these settings:
   * Destination Type: IP address
   * Destination IP address range: 192.168.1.0/24
   * Next Hop Type: Virtual network

<Frame>
  ![The image shows a Microsoft Azure portal interface where a user is adding a route to a route table named "rt-intersite." The route being added has a destination IP address range of 192.168.1.0/24 with a next hop type set to "Virtual network."](https://kodekloud.com/kk-media/image/upload/v1752884647/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-User-Defined-Routes/azure-portal-route-table-addition.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  When multiple routes are configured, Azure selects the route with the most specific address range. For example, a route for 192.168.1.0/24 takes precedence over one for 0.0.0.0/0. Adding an even more specific CIDR (like /27) will override both.
</Callout>

## Route Priority

Azure’s routing engine selects the route with the most specific destination range. In the example above:

* The route with destination 192.168.1.0/24 (more specific) is prioritized over the generic 0.0.0.0/0 route.
* If a route with an even narrower range (such as /27) is added, it will take precedence over both the /24 and /0 routes.

You can configure multiple routing rules to selectively direct traffic. For instance:

* General outbound traffic may be forwarded to a firewall.
* Specific traffic blocks, such as those for on-premises addresses, may be directed to a VPN Gateway.

## Conclusion

This guide demonstrated how to leverage User-Defined Routes in Azure to enforce custom traffic routing policies. Key steps include creating a route table, adding specific routing rules, and ensuring proper network peering. By implementing UDRs, you can ensure traffic flows securely—such as directing traffic through an NVA before it reaches a sensitive database subnet.

Additionally, consider using Service Endpoints for enhanced security and streamlined connectivity in your Azure environments.

For more detailed information on Azure networking concepts, explore these resources:

* [Azure Route Tables Documentation](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)
* [Azure Networking Overview](https://learn.microsoft.com/en-us/azure/networking/)

Understanding and properly configuring UDRs is essential for maintaining secure and efficient network architectures in Azure.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/f7470a91-91f6-4c6c-8a03-565abfeb7aee/lesson/f9401c2a-65fc-4d9f-a647-9aee85e8ec56" />
</CardGroup>

---


## Lesson 8: Service Endpoints

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Service-Endpoints/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Service-Endpoints/page.md)

**Summary:** This guide explores Azure Service Endpoints, enhancing security by connecting virtual networks to Azure resources while restricting public access.

# Service Endpoints

> This guide explores Azure Service Endpoints, enhancing security by connecting virtual networks to Azure resources while restricting public access.

Azure Service Endpoints enhance security by extending your virtual network's private address space to Azure resources. This guide explores how service endpoints work and provides a step-by-step implementation using the Azure portal.

Imagine you have a virtual network with a subnet containing a virtual machine (VM) with the IP address 192.168.1.4. Additionally, suppose you have a storage account (named “KodeKloud storage account”) with public internet access enabled. In the default configuration, the VM accesses the storage account using its public IP—for example, the Blob service endpoint is accessible via a URL formatted as:

KodeKloudStorageAccountName.blob.core.windows.net

This name resolves to a public IP, meaning the storage account is accessible over the internet.

If you need to restrict public access to the storage account, you can enforce a firewall policy that blocks all public traffic. However, the virtual machine still requires access to the storage account. This is where service endpoints come into play. By configuring a service endpoint on the storage account, you can limit connections solely from your workload subnet. Even though the storage account continues to resolve to a public IP, the connectivity between the VM and storage account occurs using the VM's private IP via Azure's secure backbone network.

To summarize the initial setup:

* A VM exists inside your Azure virtual network.
* A storage account holds critical data.
* Service endpoints for the Storage Accounts service are enabled on the VM’s subnet.

This configuration extends your VNet's private IP address space to the storage account. In the storage account settings, you configure network rules to accept connections only from the designated subnet by selecting the option to allow access from selected networks. Consequently, the VM securely connects to the storage account via a service endpoint, ensuring that the traffic remains on the Microsoft Azure backbone—enhancing both security and performance.

<Frame>
  ![The image illustrates a network diagram showing a virtual machine within a virtual network using a service endpoint to connect to an Azure storage account, with internet access blocked.](https://kodekloud.com/kk-media/image/upload/v1752884631/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Service-Endpoints/network-diagram-virtual-machine-azure.jpg)
</Frame>

Below are some key benefits of using Azure service endpoints:

1. Enhanced Security for Azure Services\
   Service endpoints strictly regulate access to critical Azure resources, such as Azure Storage or Azure SQL Database.

2. Leveraging the Microsoft Backbone Network\
   Traffic is routed over Microsoft’s secure backbone network, bypassing the public internet and resulting in a more reliable and faster connection.

3. Simple Setup and Management\
   Configuring service endpoints via the Azure portal is straightforward, reducing operational overhead.

4. Wide Range of Supported Services\
   Service endpoints support many Azure services, including Azure Storage, Azure SQL Database, Synapse Analytics, PostgreSQL, Cognitive Services, Container Registry, App Services, and more.

<Frame>
  ![The image is an infographic titled "Service Endpoints" highlighting benefits such as better security for Azure services, leveraging Microsoft's backbone network, ease of setup and management, and supported services.](https://kodekloud.com/kk-media/image/upload/v1752884633/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Service-Endpoints/service-endpoints-infographic-azure.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Even though the storage account retains a public endpoint, the service endpoint ensures that the traffic between your VM and the storage account stays private within the Azure backbone network.
</Callout>

In conclusion, Azure Service Endpoints provide a robust mechanism for securing access to Azure services. By restricting public internet access and allowing traffic only from specific virtual networks, you ensure secure and efficient connectivity.

***

## Implementing the Architecture in the Azure Portal

In this section, we will implement the architecture using the Azure portal. The demonstration involves deploying a virtual machine and a storage account. A deployment script, "service-endpoints-prep-infra," is available to provision these resources.

The following PowerShell snippet shows the creation of the infrastructure:

```powershell theme={null}
PS C:\Users\RithinSkaria\Documents\kodekloud-az104\060-Administer Intersite Connectivity>> ls

Directory: C:\Users\RithinSkaria\Documents\kodekloud-az104\060-Administer Intersite Connectivity

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         12/8/2023   12:37 PM          1436 peering-pref-infra.ps1
-a----         12/8/2023   2:43 PM           1246 service-endpoints-prep-infra.ps1

PS C:\Users\RithinSkaria\Documents\kodekloud-az104\060-Administer Intersite Connectivity>> .\service-endpoints-prep-infra.ps1

Creating VM
workload-a-vm - FQDN : vm-01-abfb51.eastus.cloudapp.azure.com
Creating storage

StorageAccountName                   ResourceGroupName    PrimaryLocation      SkuName         Kind        AccessTier    CreationTime
--------------------                   -----------------    ---------------      -------         ----        ----------    -------------
st118683879520232108 rg-se-workload-20230929        eastus        Standard_LRS   StorageV2  Hot          12/8/2023 ...
```

After running the script, navigate to the storage account in the Azure portal. Create a new container (for example, name it “demo”) in the containers section to store your files.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a storage account's container section, with one existing container named "logs" and a new container creation panel on the right.](https://kodekloud.com/kk-media/image/upload/v1752884635/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Service-Endpoints/azure-portal-storage-containers.jpg)
</Frame>

Once the container is created, upload your desired files. After selecting and browsing for files, confirm that the blobs are uploaded successfully.

<Frame>
  ![The image shows a Microsoft Azure portal interface for uploading blobs to a container named "demo," with several image files listed under current uploads.](https://kodekloud.com/kk-media/image/upload/v1752884636/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Service-Endpoints/azure-portal-upload-blobs-demo.jpg)
</Frame>

At this time, you can copy the URL of any uploaded file and paste it into a browser to verify that it is accessible over the public internet.

***

## Accessing Storage from the VM

Next, access the virtual machine (for instance, VM01 within the RGSE resource group) via SSH. After logging in, the terminal prompt will appear as follows:

```bash theme={null}
kodekloud@vm-01:~$
```

From here, you can use wget to download a file from the storage account. For example:

```bash theme={null}
kodekloud@vm-01:~$ wget https://st90629754120320929.blob.core.windows.net/demo/City3.png -O City3.jpg
--2023-09-29 12:07:39--  https://st90629754120320929.blob.core.windows.net/demo/City3.png
Resolving st90629754120320929.blob.core.windows.net (st90629754120320929.blob.core.windows.net)... 52.239.169.4
Connecting to st90629754120320929.blob.core.windows.net (st90629754120320929.blob.core.windows.net)|52.239.169.4|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4030282 (3.8M) [image/png]
Saving to: ‘City3.jpg’

City3.jpg           100%[==============================================================>]   3.84M   78.1 MB/s    in 0.05s

2023-09-29 12:07:39 (78.1 MB/s) - ‘City3.jpg’ saved [4030282/4030282]
```

Later, to enhance security by restricting public access, modify the networking settings in the storage account. In the Networking section of the storage account, change the access option from “All networks” to “Selected virtual networks and IP addresses.” Then, add your existing virtual network (e.g., VNet01 and its default subnet where your VM is located). Once saved, a service endpoint is created. This configuration means that while accessing the file via a browser will now result in an authorization failure, the VM can still download the file over the service endpoint.

<Frame>
  ![The image shows a Microsoft Azure portal interface focused on the networking settings of a storage account, with options for configuring firewalls, virtual networks, and network routing preferences.](https://kodekloud.com/kk-media/image/upload/v1752884637/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Service-Endpoints/azure-portal-networking-settings.jpg)
</Frame>

After saving the network configuration, verify that the settings have been applied by checking the notifications.

<Frame>
  ![The image shows a Microsoft Azure portal interface focused on the networking settings of a storage account, with options for configuring firewalls and virtual networks. A notification indicates that firewall and virtual network settings have been successfully saved.](https://kodekloud.com/kk-media/image/upload/v1752884638/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Service-Endpoints/azure-portal-networking-settings-2.jpg)
</Frame>

Open an incognito window and try accessing the blob URL from your browser; you should see an authorization failure message similar to:

```xml theme={null}
<Error>
  <Code>AuthorizationFailure</Code>
  <Message>This request is not authorized to perform this operation. RequestId:a79ecbc2-881e-001d-5ce0-f29dada000000 Time:2023-09-29T12:13:35.9352713Z</Message>
</Error>
```

Return to the VM and try downloading the file again using wget:

```bash theme={null}
kodekloud@vm-01:~$ wget https://st906297541203029.blob.core.windows.net/demo/City3.png -O City3.jpg
--2023-09-29 12:07:39--  https://st906297541203029.blob.core.windows.net/demo/City3.png
Resolving st906297541203029.blob.core.windows.net (st906297541203029.blob.core.windows.net)... 52.239.169.4
Connecting to st906297541203029.blob.core.windows.net (st906297541203029.blob.core.windows.net)|52.239.169.4|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 403282 (3.8M) [image/png]
Saving to: ‘City3.jpg’

City3.jpg            100%[===================>]   3.84M  78.1 MB/s    in 0.05s

2023-09-29 12:07:39 (78.1 MB/s) - ‘City3.jpg’ saved [403282/403282]
```

This confirms that even though public access is restricted, the VM can securely download the file through the service endpoint. You can further experiment with different file URLs to verify connectivity or to intentionally trigger authorization failures on invalid requests.

For further validation, try downloading another file (e.g., City2.jpg):

```bash theme={null}
kodekloud@vm-01:~$ wget https://st9062975412030299.blob.core.windows.net/demo/City2.jpg -O City2.jpg
--2023-09-29 12:19:07--  https://st9062975412030299.blob.core.windows.net/demo/City2.jpg
Resolving st9062975412030299.blob.core.windows.net (st9062975412030299.blob.core.windows.net)... 52.239.169.4
Connecting to st9062975412030299.blob.core.windows.net (st9062975412030299.blob.core.windows.net)|52.239.169.4|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 105108 (103K) [image/jpeg]
Saving to: ‘City2.jpg’

City2.jpg           100%[================================>] 102.64K  --.-KB/s    in 0.01s

2023-09-29 12:19:07 (9.51 MB/s) - ‘City2.jpg’ saved [105108/105108]
```

Even though the storage account uses a public endpoint, the traffic between your VM and the storage account flows securely over the Azure backbone network via the service endpoint.

***

## Private Link Comparison

Private Link provides secure connectivity similar to service endpoints but with different mechanisms for managing connectivity and access control. The example below demonstrates file download using Private Link:

```plaintext theme={null}
kodekloud@vm-01:~$ wget https://st9062975412030929.blob.core.windows.net/demo/City2.jpg -O City2.jpg
--2023-09-29 12:19:07--  https://st9062975412030929.blob.core.windows.net/demo/City2.jpg
Resolving st9062975412030929.blob.core.windows.net (st9062975412030929.blob.core.windows.net)... 52.239.169.4
Connecting to st9062975412030929.blob.core.windows.net (st9062975412030929.blob.core.windows.net)|52.239.169.4|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 105108 (103K) [image/jpeg]
Saving to: ‘City2.jpg’

City2.jpg           100%[===================================>] 102.64K  --.-KB/s    in 0.01s

2023-09-29 12:19:07 (9.51 MB/s) - ‘City2.jpg’ saved [105108/105108]
```

While both Private Link and Service Endpoints provide secure connectivity from your virtual network to Azure service resources, they differ in configuration and management. Understanding these differences helps determine the best option based on your security and connectivity requirements.

<Callout icon="triangle-alert" color="#FF6B6B">
  Avoid exposing sensitive data to the public internet. Always validate your network configurations to ensure that only trusted sources have access to your critical resources.
</Callout>

***

This article demonstrated how to secure storage account access using Azure Service Endpoints by restricting public internet access and allowing traffic only from specified virtual networks. With this setup, your VM utilizes its private IP to access the storage account's public endpoint, ensuring that all communication remains on the secure Microsoft Azure backbone network.

For further reading, consider exploring [Azure Networking Documentation](https://docs.microsoft.com/azure/networking/) for additional best practices and advanced configurations.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/f7470a91-91f6-4c6c-8a03-565abfeb7aee/lesson/5ced50ce-6893-4def-b4cb-bb978e039102" />
</CardGroup>

---


## Lesson 9: Private Endpoint

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Private-Endpoint/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Intersite-Connectivity/Private-Endpoint/page.md)

**Summary:** This article explores Azure Private Endpoints for secure connectivity to storage accounts using private IP addresses from your Virtual Network.

# Private Endpoint

> This article explores Azure Private Endpoints for secure connectivity to storage accounts using private IP addresses from your Virtual Network.

In this article, we explore the concept of a private endpoint for an Azure Storage account. Unlike service endpoints—which allow access to Azure services over the Azure backbone network while still using public endpoints—Azure Private Link uses private endpoints to provide direct, secure connectivity using an IP address from your Virtual Network (VNet).

When using service endpoints, the source IP (for instance, that of your Virtual Machine or VM) remains unchanged, but the connection still terminates at a public endpoint. Although the traffic remains within the Azure backbone, this setup may not meet strict security requirements for a fully private network. Service endpoints are limited to Azure VNets; they do not extend to on-premises networks. When you add your on-premises IP to the storage firewall, traffic traverses the public internet, which often does not satisfy high-security standards.

Azure Private Link resolves these limitations. By creating a private endpoint for your storage account, the service appears within your VNet. In effect, the storage service receives a network interface from your VNet's address space, resulting in a connection established through a private IP address. You can deploy the private endpoint in the same VNet as your VM or in another VNet connected through peering, making the storage account accessible as a local resource rather than a public one.

## Benefits of Azure Private Endpoint

* **Private Connection to Azure Services:** Each supported PaaS solution receives a private IP address from your VNet.
* **Seamless Integration for On-Premises and Inter-VNet Connectivity:** On-premises networks can resolve service names to private IP addresses using VPN or ExpressRoute connections, thereby avoiding public internet routing.
* **Enhanced Data Exfiltration Protection:** Keeping traffic within a private network mitigates the chance of unauthorized data exposure.
* **Direct Access within Azure VNets:** Services become directly available via private IP addresses without the need for additional network configurations.

<Callout icon="lightbulb" color="#1CB2FE">
  Disabling public network access will render any previously configured service endpoints non-functional. Attempting to access the storage account via a VM without the proper configuration will result in an "Authorization Failure" error.
</Callout>

In the next sections, we will configure a private endpoint for your storage account using the Azure portal, integrate DNS settings, test connectivity, and verify that your configuration is working as expected.

## Configuring a Private Endpoint in the Azure Portal

To configure a private endpoint for your storage account, follow these steps:

1. In the Azure portal, navigate to the **Private Endpoint** section.
2. Create a new private endpoint by entering a name (for example, "PE Storage"). This action automatically creates a network interface linking the private endpoint to your storage account.
3. Under resource selection, choose **Storage** and opt for the Blob endpoint if you store files in Blob storage.
4. Select the appropriate Virtual Network and subnet. To simplify, you can choose the same subnet where your VM resides; however, the private endpoint can reside in a different subnet or even in a VNet that is connected via peering.

The image below illustrates the private endpoint creation page in the Azure portal:

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a private endpoint, with fields for project and instance details such as subscription, resource group, name, and region.](https://kodekloud.com/kk-media/image/upload/v1752884621/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-Endpoint/azure-portal-private-endpoint-creation.jpg)
</Frame>

Next, configure the Virtual Network settings:

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a private endpoint, specifically on the "Virtual Network" configuration step. It includes options for selecting a virtual network, subnet, and configuring private IP settings.](https://kodekloud.com/kk-media/image/upload/v1752884623/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-Endpoint/azure-portal-private-endpoint-configuration.jpg)
</Frame>

After configuring the private endpoint, Azure automatically creates a private DNS zone to enable name resolution for the storage account. The DNS zone is formatted as "privatelink.blob.core.windows.net" and holds an A record mapping the storage account’s name to its private IP address. For Azure VMs using the Azure-provided DNS, the integration is automatic. However, for on-premises hosts, you must configure a conditional forwarder from your on-premises DNS to an Azure DNS resolver or a private resolver.

Review the DNS integration settings on the portal:

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a private endpoint, specifically focusing on DNS integration settings. It includes options for configuring a private DNS zone and selecting a resource group.](https://kodekloud.com/kk-media/image/upload/v1752884624/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-Endpoint/azure-portal-private-endpoint-dns-settings.jpg)
</Frame>

Once all settings are applied, wait for the private endpoint deployment to complete. The image below indicates the deployment progress:

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a private endpoint, with details about the subscription, resource group, and virtual network. A notification indicates that a template deployment is being initialized.](https://kodekloud.com/kk-media/image/upload/v1752884625/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-Endpoint/azure-portal-private-endpoint-creation-2.jpg)
</Frame>

After creation, the Azure portal displays the following details:

* The private endpoint (sometimes abbreviated as "pe") along with an associated private link resource.
* DNS configurations mapping the storage account name to its private IP address.

The dashboard summarizes these details:

<Frame>
  ![The image shows a Microsoft Azure portal page displaying details of a private endpoint named "pe-st," including its resource group, location, subscription ID, and connection status. The provisioning state is marked as "Succeeded," and the connection status is "Approved."](https://kodekloud.com/kk-media/image/upload/v1752884627/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-Endpoint/azure-portal-private-endpoint-details.jpg)
</Frame>

Additionally, you can review the private DNS zone configuration:

<Frame>
  ![The image shows a Microsoft Azure portal page displaying details of a private DNS zone configuration for "privatelink.blob.core.windows.net," including resource group and subscription information.](https://kodekloud.com/kk-media/image/upload/v1752884628/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-Endpoint/azure-private-dns-zone-configuration.jpg)
</Frame>

Verify that your Virtual Network (e.g., vnet01) is properly linked:

<Frame>
  ![The image shows a Microsoft Azure portal page displaying virtual network links for a private DNS zone. It lists a completed link with the virtual network "vnet-01" and auto-registration disabled.](https://kodekloud.com/kk-media/image/upload/v1752884630/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Private-Endpoint/azure-portal-private-dns-vnet-links.jpg)
</Frame>

## Testing Private Endpoint Connectivity

After deploying the private endpoint, you must verify that the storage account resolves to a private IP address. On your VM, use the following command to inspect DNS resolution:

```bash theme={null}
kodekloud@vm-01:~$ dig st90629754120320929.blob.core.windows.net
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 52399
;; flags: qr raa; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; QUESTION SECTION:
;st90629754120320929.blob.core.windows.net. IN A

;; ANSWER SECTION:
st90629754120320929.blob.core.windows.net. 60 IN CNAME st90629754120320929.privatelink.blob.core.windows.net.
st90629754120320929.privatelink.blob.core.windows.net. 10 IN A 192.168.1.5

Query time: 8 msec
SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
When: Fri Sep 29 12:40:23 UTC 2023
MSG SIZE  rcvd: 132
```

Next, test file access using curl. An attempt to access the storage account without proper authorization will yield an error:

```bash theme={null}
kodekloud@vm-01:~$ curl https://st90629754120320929.blob.core.windows.net/demo/City3.png
<?xml version="1.0" encoding="utf-8"?>
<Error>
  <Code>AuthorizationFailure</Code>
  <Message>This request is not authorized to perform this operation.</Message>
</Error>
```

Once you have the correct authorization or you are simply testing connectivity via a file download, redirect the output to a file:

```bash theme={null}
kodekloud@vm-01:~$ curl https://st90629754120320929.blob.core.windows.net/demo/City3.png > City4.png
```

Finally, list the directory contents to confirm the file has been downloaded:

```bash theme={null}
kodekloud@vm-01:~$ ls
City1.jpg  City2.jpg  City3-copy.jpg  City3.jpg  City4.png
```

This confirms that the storage account now resolves via the private endpoint using the private DNS zone, with the resolution pointing to 192.168.1.5.

## Summary

Azure Private Endpoints offer a secure method for accessing storage accounts and other Azure services over a private connection using an IP from your Virtual Network. The seamless integration with Azure Private DNS Zones allows service names to resolve accurately to private IP addresses, simplifying connectivity for both Azure VMs and on-premises systems (when DNS forwarders are configured). This configuration improves your security posture by eliminating exposure to the public internet and reducing the risk of data exfiltration.

<Callout icon="lightbulb" color="#1CB2FE">
  In the next module, we will explore techniques for managing and administering network traffic within your Azure environment.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/f7470a91-91f6-4c6c-8a03-565abfeb7aee/lesson/052b4988-4be8-4f66-8979-d5c22fb02036" />
</CardGroup>

---


# Section 07: Administer Network Traffic

---


## Lesson 1: Module Introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Module-Introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Module-Introduction/page.md)

**Summary:** This article covers managing network traffic in Microsoft Azure, focusing on load balancing, application gateways, and network monitoring for high availability and security.

# Module Introduction

> This article covers managing network traffic in Microsoft Azure, focusing on load balancing, application gateways, and network monitoring for high availability and security.

In this article, we delve into the intricacies of managing network traffic within Microsoft Azure. Our comprehensive guide is designed to provide you with the knowledge and best practices to ensure high availability, efficient routing, and robust security in your cloud environment.

## Learning Objectives

This guide is structured around three key Azure components:

1. **Azure Load Balancer**\
   The Azure Load Balancer is a fundamental service that increases application availability by distributing incoming network traffic across multiple servers. In this section, you will learn how to:

   * Configure load balancing rules to optimize traffic distribution.
   * Implement session persistence for a consistent and reliable user experience.

2. **Azure Application Gateways**\
   Azure Application Gateways offer advanced routing capabilities with application-level load balancing. This section focuses on:

   * Identifying and understanding the key components of the gateway.
   * Implementing routing rules to efficiently manage web traffic.
   * Enhancing application security and performance through smart configuration.

3. **Network Watcher**\
   Network Watcher is an essential tool for monitoring and troubleshooting network operations. Here, we cover:

   * Continuous monitoring of network communications.
   * Diagnosing network issues quickly and effectively.
   * Ensuring compliance with network security standards.

<Callout icon="lightbulb" color="#1CB2FE">
  Before you begin, verify that your Azure subscription is properly configured and that you have the necessary permissions to manage these network services.
</Callout>

Let’s start our journey by diving into the configuration of the Azure Load Balancer.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/50248c52-4b17-4c2d-87f8-52a42eff2d2f/lesson/ca43c9ae-6de4-4da7-a65d-f8184bac17f8" />
</CardGroup>

---


## Lesson 2: Azure Load Balancer

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Azure-Load-Balancer/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Azure-Load-Balancer/page.md)

**Summary:** Azure Load Balancer efficiently distributes network traffic among backend servers, ensuring consistent application performance and high availability through defined rules and health probes.

# Azure Load Balancer

> Azure Load Balancer efficiently distributes network traffic among backend servers, ensuring consistent application performance and high availability through defined rules and health probes.

Azure Load Balancer is a high-performance service that efficiently distributes incoming network traffic among backend servers using defined rules and health probes. By doing so, it prevents any single server from becoming overloaded, ensuring consistent application performance and high availability.

## Overview and Key Features

Operating at Layer 4 (Transport Layer) of the OSI model, Azure Load Balancer manages both TCP and UDP traffic. It is optimized for Azure Virtual Machines and Virtual Machine Scale Sets, providing reliable and scalable traffic distribution.

Azure Load Balancer is available in two SKUs:

* **Basic SKU**: A cost-effective option designed for smaller or less complex workloads, suitable for development and testing.
* **Standard SKU**: A robust solution that offers advanced features including higher scale, enhanced diagnostics, a 99.99% SLA, improved network security, and multi-zone support.

Both SKUs can handle all TCP and UDP traffic, making the Azure Load Balancer a flexible choice for a broad range of applications. Integration with Network Security Groups (NSGs) adds an extra layer of protection by enforcing strict security policies on the traffic that reaches your backend servers.

By leveraging Azure Load Balancer, you can build a highly available, secure, and scalable application architecture.

## Load Balancer SKUs

The key differences between the Basic and Standard SKUs are summarized in the table below:

| Characteristic       | Basic SKU                                            | Standard SKU                                                                |
| -------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------- |
| Backend Pool Size    | Up to 300 instances                                  | Up to 1,000 instances                                                       |
| Health Probes        | Supports TCP and HTTP probes                         | Supports TCP, HTTP, and HTTPS probes (*HTTP/HTTPS evaluate response codes*) |
| Redundancy Options   | No built-in redundancy options                       | Multiple redundant availability options available                           |
| Frontend Connections | Supports multiple frontends for inbound traffic only | Supports both inbound and outbound connections                              |
| Security Posture     | Open by default (optional NSG configuration)         | Closed by default; requires explicit NSG rules to allow traffic             |
| SLA                  | No SLA provided                                      | 99.99% SLA                                                                  |

<Frame>
  ![The image compares features of Basic and Standard Load Balancers, highlighting differences in backend pool size, health probes, redundancy, multiple frontends, security, and SLA.](https://kodekloud.com/kk-media/image/upload/v1752884704/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Load-Balancer/load-balancer-comparison-features.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  When selecting a SKU, consider your workload’s requirements for performance, security, and availability. The Standard SKU is better suited for production environments with stringent SLA needs.
</Callout>

## Public and Internal Load Balancers

Azure Load Balancer is offered in two main configurations: public and internal. Each configuration caters to different network scenarios and workload requirements.

### Public Load Balancer

The Public Load Balancer is designed for applications that require direct Internet connectivity. It is ideal for scenarios where client requests from the Internet need to be evenly distributed among multiple servers. For instance, a virtual network with several web servers in a web subnet can use a public load balancer to handle incoming HTTP requests on port 80, thereby ensuring minimal impact in the event of a server failure.

<Frame>
  ![The image illustrates a public load balancer setup, showing how it distributes traffic on port 80 to multiple servers within a virtual network. It highlights that this configuration is ideal for public-facing workloads.](https://kodekloud.com/kk-media/image/upload/v1752884705/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Load-Balancer/public-load-balancer-setup.jpg)
</Frame>

In a public load balancer configuration, a public IP address is associated with the load balancer to ensure it receives traffic directly from the Internet.

### Internal Load Balancer

For services that do not need exposure to the Internet, the Internal Load Balancer is the optimal choice. It efficiently routes traffic within your Azure Virtual Network, making it perfect for internal workloads such as database communications or inter-service communication within multi-tier applications.

Consider a scenario where web servers need to communicate with a backend database cluster located in a separate data subnet. An internal load balancer can distribute database requests among multiple database servers, enhancing both performance and security.

<Frame>
  ![The image is a diagram illustrating an internal load balancer setup within a virtual network, showing the flow of traffic through public and internal load balancers to web and data subnets.](https://kodekloud.com/kk-media/image/upload/v1752884706/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Load-Balancer/internal-load-balancer-diagram.jpg)
</Frame>

Using an internal load balancer improves your application's security posture by segregating public-facing services from internal systems; it operates without a public IP address.

## Configuring Azure Load Balancer Rules

After understanding the types and features of Azure Load Balancer, configuring load balancing rules is the next step. These rules determine how incoming traffic is distributed among backend servers and encompass parameters such as frontend IP configuration, backend pool assignments, load balancing rules, and health probes.

Implementing these rules correctly ensures that your Azure Load Balancer maximizes performance, reliability, and scalability. In this lesson, we delve deeper into rule configuration, empowering you to optimize your Azure infrastructure for seamless application delivery.

<Callout icon="lightbulb" color="#1CB2FE">
  For detailed instructions on configuring your load balancing rules, refer to the official [Azure Load Balancer documentation](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-standard-overview).
</Callout>

This concludes our in-depth overview of Azure Load Balancer and its configuration options. By understanding the distinctions between SKUs and the appropriate use cases for public and internal load balancers, you can design robust systems that adhere to best practices for both performance and security.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/50248c52-4b17-4c2d-87f8-52a42eff2d2f/lesson/3a6bab28-6158-4817-864f-083488f1f33b" />
</CardGroup>

---


## Lesson 3: Load Balancer Rules

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Load-Balancer-Rules/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Load-Balancer-Rules/page.md)

**Summary:** This article explores various Azure Load Balancer rule types for efficient traffic management across resources.

# Load Balancer Rules

> This article explores various Azure Load Balancer rule types for efficient traffic management across resources.

Azure Load Balancer rules are crucial for efficiently managing how traffic is distributed across your resources. In this article, we explore the various rule types that guide the behavior of an Azure Load Balancer.

## Load Balancing Rules

Load balancing rules are the backbone of effective traffic management. They dictate how incoming requests are evenly distributed among instances in a back-end pool. For example, in a Virtual Network hosting multiple servers within a web subnet, load balancing rules ensure that user traffic is allocated across these servers, preventing any single server from becoming overwhelmed. This balanced distribution enhances performance and maintains service reliability.

## Inbound NAT Rules

Inbound Network Address Translation (NAT) rules enable precise traffic redirection. These rules forward incoming traffic to a specific port on a designated Virtual Machine in your back-end pool. For example, if port 30008 on the load balancer is mapped to port 3389 on a particular VM, incoming traffic on port 30008 will be directed to port 3389 of that VM. Administrators can configure similar mappings for other VMs as needed, ensuring targeted access control.

## Outbound Rules

Outbound rules manage traffic leaving your virtual network. They ensure that responses reach users and that your VMs can securely access external resources, whether on the internet or other networks. By defining clear pathways for outbound communication, these rules play a key role in maintaining network security and operational predictability.

## Session Persistence

Session persistence ensures that client requests within the same session are consistently directed to the same back-end instance. This is especially important when the application requires the preservation of state or context across sequential requests, thereby enhancing the overall user experience.

<Callout icon="lightbulb" color="#1CB2FE">
  Collectively, these rules provide a comprehensive framework for managing both inbound and outbound traffic in Azure environments. Implementing these configurations helps achieve optimized performance, high availability, and improved security for your applications.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/50248c52-4b17-4c2d-87f8-52a42eff2d2f/lesson/e4b6ed95-c6c8-42ca-a804-ae1589e8ff3c" />
</CardGroup>

---


## Lesson 4: Session Persistence

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Session-Persistence/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Session-Persistence/page.md)

**Summary:** This article explains session persistence options in Azure Load Balancer and guides on deploying and configuring it for traffic distribution across web servers.

# Session Persistence

> This article explains session persistence options in Azure Load Balancer and guides on deploying and configuring it for traffic distribution across web servers.

Session persistence in the Azure Load Balancer determines how client requests are consistently routed to specific server sessions. In this lesson, we explore the three session persistence options available for an Azure Load Balancer: none, client IP, and client IP and protocol. The default selection is "none." At the end of the lesson, you will see a demonstration that combines these concepts with practical deployment.

## Session Persistence Options

### None (Default)

When session persistence is set to "none," Azure Load Balancer uses a five-tuple hash to distribute incoming requests. This hash includes:

* Source IP address
* Destination IP address
* Source port
* Destination port
* Protocol

Using this five-tuple, each request is independently load balanced to a server. This method is ideal for stateless applications where session affinity is not required.

### Client IP

Selecting the "client IP" option, also known as the two-tuple hash, causes the load balancer to use a combination of the source and destination IP addresses. This ensures that all requests from a specific client IP are directed to the same server. This approach is particularly beneficial for applications that maintain user state, such as e-commerce shopping carts or scenarios requiring persistent server-side sessions.

<Frame>
  ![The image shows options for session persistence, including "None (default)" and "Client IP," with a dropdown menu listing "None," "Client IP," and "Client IP and protocol."](https://kodekloud.com/kk-media/image/upload/v1752884728/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Session-Persistence/session-persistence-options-dropdown.jpg)
</Frame>

### Client IP and Protocol

The "client IP and protocol" option, known as the three-tuple hash, adds the protocol to the source and destination IP addresses. This method is particularly useful when a single virtual machine hosts multiple services (for example, secure and non-secure traffic on different protocols, even when sharing the same IP address).

<Callout icon="lightbulb" color="#1CB2FE">
  Choosing the appropriate session persistence option is key to balancing session affinity with efficient resource utilization and delivering an optimal user experience.
</Callout>

***

## Deploying and Configuring the Azure Load Balancer

In this section, you will learn how to deploy an Azure Load Balancer to distribute traffic across web servers. This process includes deploying virtual machines (VMs), installing a web server role, updating web pages, and configuring the load balancer.

### Preparing the Infrastructure

Within the repository, there is a script (for example, "070\_load\_balancer\_prep\_infra.ps1") that deploys virtual machines and sets up the environment. Navigate to the repository folder using the following commands:

```powershell theme={null}
PS C:\Users\RithinSkaria\Documents> cd .\kodekloud-az104\
PS C:\Users\RithinSkaria\Documents\kodekloud-az104>
```

Next, execute the infrastructure preparation script (e.g., `prep_infra.ps1`) to deploy resources such as VMs and a jumpbox. When the script runs, it outputs important details like the jumpbox DNS name and the private IP addresses of the web servers. Note that these servers are not yet exposed to the internet—they will be made accessible via the load balancer.

The output should resemble the following:

```plaintext theme={null}
Setting OS Profile
Creating VM webserver-03

RequestId         : 
IsSuccessStatusCode : True
StatusCode       : OK
ReasonPhrase     : 

Creating jumpbox VM

RequestId         : 
IsSuccessStatusCode : True
StatusCode       : OK
ReasonPhrase     : 

Jumpbox VM DNS name : jumpbox-vm-168e36.eastus.cloudapp.azure.com
Private IP (webserver-01) : 10.0.2.4
Private IP (webserver-02) : 10.0.2.5
Private IP (webserver-03) : 10.0.2.6

PS C:\Users\RithinSkaria\Documents\kodekloud-az104>
```

You can then connect via SSH to the jumpbox using the provided credentials:

```plaintext theme={null}
PS C:\Users\RithinSkaria> ssh kodekloud@jumpbox-vm-168e36.eastus.cloudapp.azure.com
The authenticity of host 'jumpbox-vm-168e36.eastus.cloudapp.azure.com (20.163.147.93)' can't be established.
ED25519 key fingerprint is SHA256:AMcvFrj/j3uGPLXJJzqlmeFAE3jj37OdYFuc.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'jumpbox-vm-168e36.eastus.cloudapp.azure.com' (ED25519) to the list of known hosts.
kodekloud@jumpbox-vm-168e36.eastus.cloudapp.azure.com's password:
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 6.2.0-1018-azure x86_64)
...
```

Once connected, verify that the web servers are configured correctly by using the curl command from the jumpbox. For example:

```bash theme={null}
kodekloud@jumpbox-vm:~$ curl 10.0.2.4
<html>
<body style="background-color:red;">
<h1 style="color:white;">Hello world</h1>
</body>
</html>

kodekloud@jumpbox-vm:~$ curl 10.0.2.5
<html>
<body style="background-color:green;">
<h1 style="color:white;">Hello world</h1>
</body>
</html>

kodekloud@jumpbox-vm:~$ curl 10.0.2.6
<html>
<body style="background-color:blue;">
<h1 style="color:white;">Hello world</h1>
</body>
</html>
```

Each web server responds with a distinct background color, verifying that the load balancing functions correctly.

***

## Configuring the Azure Load Balancer

Follow these steps to create and configure your Azure Load Balancer:

1. **Create the Load Balancer:**
   * In the Azure portal, navigate to "Create a resource" and choose "Load Balancer."
   * Select the Standard SKU for production use and opt for a public (regional) load balancer.
   * Provide a name (e.g., `sclbweb01`) and ensure it belongs to the same resource group as your VMs.

2. **Configure the Frontend IP:**
   * Create a public IP address resource (for example, `sclbpip` or named "fe" for frontend).
   * Associate this public IP with the frontend configuration of the load balancer.

<Frame>
  ![The image shows the Microsoft Azure portal interface for creating a load balancer, with options to configure project and instance details such as subscription, resource group, name, region, SKU, type, and tier.](https://kodekloud.com/kk-media/image/upload/v1752884729/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Session-Persistence/azure-load-balancer-creation-page.jpg)
</Frame>

<Frame>
  ![The image shows the Microsoft Azure portal interface for creating a load balancer, specifically the "Frontend IP configuration" section. It includes options to add a frontend IP configuration with fields for name, IP version, IP type, and public IP address.](https://kodekloud.com/kk-media/image/upload/v1752884731/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Session-Persistence/azure-portal-load-balancer-frontend-ip.jpg)
</Frame>

3. **Set Up the Backend Pool:**
   * Create a backend pool and choose the virtual network where your web servers are located.
   * Add all three web servers to the backend pool.

<Frame>
  ![The image shows a Microsoft Azure portal interface for adding a backend pool to a load balancer, listing virtual machines with their IP configurations and addresses.](https://kodekloud.com/kk-media/image/upload/v1752884732/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Session-Persistence/azure-portal-load-balancer-backend-pool.jpg)
</Frame>

4. **Add Load Balancing Rules:**\
   Create a load balancing rule to connect the frontend with the backend pool:
   * Provide a rule name (e.g., `sclb_lb_http`).
   * Select the previously created frontend IP address.
   * Choose the appropriate backend pool.
   * Set both the frontend and backend TCP port to 80.
   * Create a new health probe (e.g., `sclb_http_probe`) that checks port 80 every 5 seconds. If a server fails to respond, it is marked as unhealthy and excluded from the load-balanced pool.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a load balancer, with options to add load balancing and inbound NAT rules. A sidebar is open for adding a load balancing rule, displaying various configuration settings.](https://kodekloud.com/kk-media/image/upload/v1752884733/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Session-Persistence/azure-portal-load-balancer-setup.jpg)
</Frame>

5. **Configure Session Persistence:**\
   Within the load balancing rule settings, select the session persistence method. By default, the five-tuple hash (none) is used. You may choose the two-tuple (client IP) or three-tuple (client IP and protocol) option based on your application's needs. For demonstration purposes, we'll keep the default "none" setting.

6. **Finalize and Create:**\
   Review your settings carefully, ensuring that no extra inbound NAT or outbound rules are enabled since the jumpbox handles management. When ready, click "Review and Create" followed by "Create." Wait for the deployment to complete.

After the load balancer is deployed, navigate back to its resource page to view its details.

<Frame>
  ![The image shows the Microsoft Azure portal displaying details of a load balancer named "azlb-web-01," including its resource group, location, and configuration settings. The interface provides options for managing IP configurations, backend pools, health probes, and load balancing rules.](https://kodekloud.com/kk-media/image/upload/v1752884734/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Session-Persistence/azure-portal-load-balancer-details.jpg)
</Frame>

<Frame>
  ![The image shows a Microsoft Azure portal page listing virtual machines, including their names, types, locations, statuses, operating systems, sizes, public IP addresses, and disk counts.](https://kodekloud.com/kk-media/image/upload/v1752884735/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Session-Persistence/azure-portal-virtual-machines-list.jpg)
</Frame>

Once the public IP of the load balancer is associated with the web servers, entering the IP address in your browser will direct you to one of the servers based on the configured session persistence mechanism. Depending on the underlying session details, you may see different responses (red, green, or blue).

***

## Next Steps

In this lesson, you learned how Azure Load Balancer manages session persistence using multiple options and how to deploy and configure it to balance traffic across multiple web servers. Up next, we will explore another load balancing solution: Azure Application Gateway.

Happy learning!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/50248c52-4b17-4c2d-87f8-52a42eff2d2f/lesson/42d31a2b-2cbb-4808-8d9e-d2dd3050d5c5" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/50248c52-4b17-4c2d-87f8-52a42eff2d2f/lesson/2fc7374a-2d09-4449-91cd-9ab8d83aea60" />
</CardGroup>

---


## Lesson 5: Azure Application Gateway

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Azure-Application-Gateway/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Azure-Application-Gateway/page.md)

**Summary:** Azure Application Gateway is a Layer 7 load balancing solution for managing HTTP, HTTPS, and WebSocket traffic with advanced routing and security features.

# Azure Application Gateway

> Azure Application Gateway is a Layer 7 load balancing solution for managing HTTP, HTTPS, and WebSocket traffic with advanced routing and security features.

Azure Application Gateway is a robust Layer 7 load balancing solution in Microsoft Azure. It is designed to efficiently handle HTTP, HTTPS, HTTP/2, and WebSocket traffic while providing advanced routing capabilities and enhanced security through features such as a Web Application Firewall.

## Key Features

* **Advanced Routing:** Utilizes path-based routing to direct requests based on URL, making it possible to host multiple websites behind one gateway.
* **Enhanced Security:** Optionally integrates with a Web Application Firewall to protect backend resources.
* **URL Redirection & SSL Termination:** Supports URL redirection, SSL termination, and HTTP header rewriting.
* **Custom Error Pages:** Allows customization of error messages for improved user experience.
* **Broad Backend Support:** Unlike the Azure Load Balancer—which is limited to virtual machines and virtual machine scale sets—the Application Gateway supports a variety of resources, including:

  | Resource Type              | Supported Backend Resources           |
  | -------------------------- | ------------------------------------- |
  | Virtual Machines           | Traditional virtual machines in Azure |
  | Virtual Machine Scale Sets | Scalable VM deployments               |
  | Azure App Services         | Includes support for deployment slots |
  | Other Cloud/On-Premises    | Servers hosted outside of Azure       |

## How It Works

The following workflow illustrates how Azure Application Gateway manages incoming traffic:

1. **Request Initiation:**\
   A user initiates a request for a webpage, image, or any other resource via their browser.

2. **Traffic Management:**\
   The request is first received by the Azure Application Gateway, which manages all incoming web traffic.

3. **Listener Interception:**\
   An HTTP or HTTPS listener on the gateway intercepts the request, configured to respond based on specific criteria such as URL path and host header.

4. **Routing Rule Application:**\
   The listener applies predefined routing rules. Based on evaluating the URL path or other attributes, the rules determine the appropriate backend pool to which the request should be forwarded.

5. **HTTP Settings Enforcement:**\
   Before sending the request to the backend, the gateway applies HTTP settings, which set parameters for communication. These include timeout settings, cookie-based affinity for session persistence, and rewrite rules to modify headers if needed.

6. **Request Forwarding:**\
   With routing and HTTP settings in place, the gateway forwards the request to a selected backend pool comprising resources like virtual machines, App Services, or other servers.

7. **Load Balancing:**\
   Within the backend pool, load balancing algorithms (e.g., round-robin, least connections) are employed to distribute incoming requests evenly across multiple servers, ensuring optimal performance and reliability.

<Callout icon="lightbulb" color="#1CB2FE">
  Azure Application Gateway seamlessly integrates listeners, routing rules, HTTP settings, and backend pools to ensure efficient and secure management of user requests.
</Callout>

## Architecture Diagram

Below is a visual representation of the Azure Application Gateway architecture. The diagram illustrates the various components such as the Layer 7 load balancer, routing features, backend pools, and how traffic flows from a user's browser to different types of backend resources including virtual machines, virtual machine scale sets, and external servers.

<Frame>
  ![The image is a diagram of an application gateway, illustrating components like a Layer 7 load balancer, routing features, backend pools, and the flow from a browser to virtual machines, VMSS, and servers.](https://kodekloud.com/kk-media/image/upload/v1752884702/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Application-Gateway/application-gateway-diagram-load-balancer.jpg)
</Frame>

For more detailed information on Azure networking and load balancing, you may refer to the official [Azure Documentation](https://docs.microsoft.com/azure/application-gateway/overview).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/50248c52-4b17-4c2d-87f8-52a42eff2d2f/lesson/bc4997cc-0fef-4d38-945c-7994c9b7f18d" />
</CardGroup>

---


## Lesson 6: Application Gateway components

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Application-Gateway-components/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Application-Gateway-components/page.md)

**Summary:** This article explains the components of Azure Application Gateway for managing web traffic through routing, load balancing, and security features.

# Application Gateway components

> This article explains the components of Azure Application Gateway for managing web traffic through routing, load balancing, and security features.

The Azure Application Gateway is a robust solution for managing web traffic through advanced routing, load balancing, and security features. In this guide, we break down the major components that work together to efficiently handle incoming requests and ensure smooth communication between clients and back-end servers.

## Front-End IP

The front-end IP acts as the entry point for all incoming traffic. It is configurable as either a public IP for internet-facing applications or as a private IP for internal applications. When configured privately, it is often referred to as a VIP or Internal Load Balancer (ILB).

## Listener

The listener is responsible for monitoring incoming traffic requests. It binds to a specific IP address and port, and when operating in HTTPS mode, it is paired with an SSL certificate for secure communication. By handling SSL offloading at the listener level, the Application Gateway reduces the processing load on back-end servers.

<Callout icon="lightbulb" color="#1CB2FE">
  The upward connection depicted in conceptual diagrams from the front-end IP to the listener illustrates how the listener continuously monitors the entry point for new traffic.
</Callout>

## Certificate

For HTTPS traffic, the Application Gateway uses SSL certificates to encrypt and decrypt data. These certificates, associated with the listener, maintain secure communications between clients and the gateway, ensuring data integrity and privacy.

## Rule

The rule component acts as the intermediary between the front end and the back-end pool. It defines how incoming requests are directed to the appropriate services based on criteria such as URL paths, host headers, or other custom conditions. Within each rule, associated HTTP settings determine the precise method of communication with the back-end servers.

## HTTP Settings

HTTP settings define the parameters for server communication. These settings include:

* Configuring health probes to continuously monitor back-end server availability.
* Setting timeout parameters to limit the waiting period for server responses.
* Enabling session stickiness where required, ensuring continuous user sessions.

Additionally, you can set up custom probes to periodically check the health of your back-end servers, ensuring the system consistently routes traffic to healthy instances.

<Frame>
  ![The image is a flowchart illustrating the components of an Application Gateway, including elements like Frontend IP, Listener, Port, Certificate, Rule, HTTP Setting, Custom Probe, and Backend Pool, with annotations explaining their functions.](https://kodekloud.com/kk-media/image/upload/v1752884701/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Application-Gateway-components/application-gateway-flowchart-components.jpg)
</Frame>

## Back-End Pool

The back-end pool consists of the actual service instances such as virtual machines, virtual machine scale sets, or other web service endpoints that handle HTTP or HTTPS requests. The Application Gateway routes traffic to these instances based on the established rules and settings, ensuring efficient distribution of requests.

## Routing Rules

Routing rules play a critical role in defining how traffic flows from the front end to the back-end pool. These rules ensure that incoming requests are correctly distributed based on predefined logic, such as URL path-based routing or host header matching. With these rules in place, you can ensure that your web traffic is managed effectively and securely.

<Callout icon="lightbulb" color="#1CB2FE">
  This overview of Azure Application Gateway components highlights how each part collaborates to deliver secure, efficient, and reliable web traffic management.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/50248c52-4b17-4c2d-87f8-52a42eff2d2f/lesson/e6d6e937-05b9-42d5-a068-db32dc9689ad" />
</CardGroup>

---


## Lesson 7: Routing Rules

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Routing-Rules/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Routing-Rules/page.md)

**Summary:** This guide explains advanced routing methods in Azure Application Gateway, including path-based and multi-site routing, with practical deployment instructions using the Azure Portal.

# Routing Rules

> This guide explains advanced routing methods in Azure Application Gateway, including path-based and multi-site routing, with practical deployment instructions using the Azure Portal.

Azure Application Gateway offers advanced routing capabilities including both path-based and multi-site routing. This guide explains these routing methods and presents a practical deployment using the Azure Portal.

## Path-Based Routing

Path-based routing directs incoming traffic to different backend pools based on the URL path. For example, when a user accesses a URL containing "/images," the Application Gateway forwards the request to an image server pool optimized for image delivery. Similarly, if the URL includes "/video," the gateway directs the request to a video server pool designed to efficiently handle video content. This approach is ideal for applications that serve specific content types from dedicated infrastructure components.

## Multiple-Site Routing

Multi-site routing allows a single Application Gateway to service multiple web applications by directing requests based on the domain name. For instance, traffic arriving at KodeKloud.com may be routed to a learning pool, while requests to KodeKloudLabs.com are sent to a lab pool. This consolidated approach simplifies infrastructure management and reduces costs by centralizing traffic management onto a single gateway. Both routing methodologies leverage Layer 7 load balancing to ensure that users receive responses from the correct backend resources.

<Frame>
  ![The image illustrates application gateway routing rules, showing path-based routing and multiple-site routing with different server pools for images, videos, learning, and labs.](https://kodekloud.com/kk-media/image/upload/v1752884718/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Routing-Rules/application-gateway-routing-rules.jpg)
</Frame>

## Demonstration: Configuring Azure Application Gateway

In this demonstration, we deploy an Application Gateway that uses path-based routing. The deployment script named AppGatewayPrepInfra1 sets up the required infrastructure—including two red VMs, two blue VMs, and two green VMs. Initially, all requests are routed to the red servers. If the URL path offers a clue (e.g., containing "blue" or "green"), the traffic is directed to the blue or green servers as appropriate.

```powershell theme={null}
RequestId              : True
IsSuccessStatusCode    : OK
StatusCode             : True
ReasonPhrase           : OK
Creating jumpbox VM	
RequestId              : True
IsSuccessStatusCode    : OK
StatusCode             : True
ReasonPhrase           : OK

Jumpbox VM DNS name   : jumpbox-vm-168e36.eastus.cloudapp.azure.com
Private IP (webserver-01) : 10.0.2.4
Private IP (webserver-02) : 10.0.2.5
Private IP (webserver-03) : 10.0.2.6
PS C:\Users\RithinSkarla\Documents\kodekloud-az104>
PS C:\Users\RithinSkarla\Documents\kodekloud-az104> & .\070-Administer Network Traffic\appgw-prep
```

> **Warning: Deployment Error**
>
> If a deployment error occurs, you might see output similar to the following:
>
> ```powershell theme={null}
> ErrorTarget:
> StartTime: 12/9/2023 1:30:31 PM
> EndTime: 12/9/2023 1:34:21 PM
> OperationID: 1f1ca72-477d-4e69-91c2-024f13617746
> Status: Failed
> At C:\Users\RithinSkaria\Documents\kodekloud-az104\070-Administer Network Traffic\appgw_prep-infra.ps1:178 char:1
> + Set-AzVMExtension @Params
>     + CategoryInfo          : CloseError: (:) [Set-AzVMExtension], ComputeCloudException
>     + FullyQualifiedErrorId : Microsoft.Azure.Commands.Compute.SetAzureVMExtensionCommand
> Deployment Completed!
> Jumpbox VM DNS name: jumpbox-vm-e6c623.eastus.cloudapp.azure.com
> Private IP (green-01): 10.0.1.4
> Private IP (green-02): 10.0.1.5
> Private IP (blue-01): 10.0.1.4
> Private IP (blue-02): 10.0.1.5
> Private IP (red-01): 10.0.2.4
> Private IP (red-02): 10.0.2.5
> Use username: kodekLoud and password: VMP055w0rd to login to any VMs
> PS C:\Users\RithinSkaria\Documents\kodekloud-az104>
> ```

Once the deployment completes, verify that the virtual machines (including blue, green, red, and the jumpbox VMs) are visible in the Azure Portal.

## Deploying the Application Gateway via the Azure Portal

### Step 1: Virtual Machines Overview

Access the Azure Portal and verify your list of virtual machines to ensure all instances are deployed correctly.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a list of virtual machines, including details like name, type, status, and operating system.](https://kodekloud.com/kk-media/image/upload/v1752884719/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Routing-Rules/azure-portal-virtual-machines-list.jpg)
</Frame>

### Step 2: Creating the Application Gateway

Click on "Create" and complete the configuration fields including subscription, resource group, Application Gateway name (e.g., APPGW Colors or H2S), and region.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating an application gateway, with fields for project and instance details such as subscription, resource group, and region.](https://kodekloud.com/kk-media/image/upload/v1752884721/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Routing-Rules/azure-portal-application-gateway.jpg)
</Frame>

Select the Standard V2 SKU to leverage auto-scaling capabilities (which are disabled in this demo). Set the instance count and do not select availability zones.

### Step 3: Configuring the Virtual Network

The Application Gateway requires a dedicated subnet. Select your Virtual Network and click on "Manage subnet configuration" to add a new subnet specifically for the Application Gateway. With a large address space (e.g., /16), you can configure a subnet with a /24 CIDR.

<Frame>
  ![The image shows the Microsoft Azure portal interface for managing subnets within a virtual network. It includes a list of existing subnets and a form to add a new subnet with various configuration options.](https://kodekloud.com/kk-media/image/upload/v1752884722/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Routing-Rules/azure-portal-managing-subnets.jpg)
</Frame>

Ensure that the Application Gateway subnet is created and selected without errors before proceeding.

### Step 4: Frontend Setup

For the frontend configuration, create a new public IP address (named "PIP") for the public-facing gateway.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating an application gateway, specifically on the "Frontends" tab, with a pop-up window for adding a public IP address.](https://kodekloud.com/kk-media/image/upload/v1752884723/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Routing-Rules/azure-portal-application-gateway-frontends.jpg)
</Frame>

### Step 5: Backend and Routing Rule Configuration

1. Create backend pools for your server groups. Initially, define pools for red, blue, and green servers.
2. Configure the routing rules:
   * Create a primary routing rule (e.g., "App GW Colors HTTP Route") with a priority of 1.
   * Set up a listener (e.g., "App Gateway Colors HTTP Listener") with the following details:
     * Frontend IP: Public
     * Protocol: HTTP
     * Port: 80
     * Listener type: Basic (no multi-site configuration)

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating an application gateway, specifically focusing on adding a routing rule with configuration options for listener settings and custom error pages.](https://kodekloud.com/kk-media/image/upload/v1752884724/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Routing-Rules/azure-portal-application-gateway-routing-rule.jpg)
</Frame>

Configure the default backend target to use the red pool on port 80 with HTTP. Then, add path-based routing rules:

* For instance, create a rule such that when the URL path contains "blue/\*", traffic is forwarded to the blue pool.
* Similarly, configure a rule for "green" paths that directs traffic to the green pool.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating an application gateway, specifically in the "Configuration" step, with a pop-up for adding a path to a routing rule.](https://kodekloud.com/kk-media/image/upload/v1752884725/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Routing-Rules/azure-portal-application-gateway-configuration.jpg)
</Frame>

Review your configurations, add tags if needed, and start the deployment of the Application Gateway. The deployment process typically takes 10 to 15 minutes.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating an application gateway, displaying configuration details such as subscription, resource group, and network settings. A notification indicates the initialization of a template deployment.](https://kodekloud.com/kk-media/image/upload/v1752884725/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Routing-Rules/azure-portal-application-gateway-config.jpg)
</Frame>

### Step 6: Mapping Virtual Machines to Backend Pools

After successful deployment, navigate to the Resource Group to locate your Application Gateway. Since backend pools are empty initially, manually add virtual machines to the respective pools:

* For the red pool, assign the "Red One" and "Red Two" VMs.
* Similarly, add the appropriate blue and green VMs to their designated pools.

<Frame>
  ![The image shows a Microsoft Azure portal interface for editing a backend pool. It includes options to select a target type and target, with a dropdown list of virtual machines and their associated IP addresses.](https://kodekloud.com/kk-media/image/upload/v1752884726/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Routing-Rules/azure-portal-backend-pool-edit.jpg)
</Frame>

## Testing the Application Gateway

After mapping the virtual machines, test the routing configuration:

* Access the public IP of the Application Gateway to verify that traffic is, by default, routed to the red servers (using a round-robin distribution).
* Append the specific path (e.g., "/blue") to the URL and confirm that the request is directed to the blue servers.
* Similarly, test a path corresponding to the green rules to ensure traffic is properly forwarded to the green pool.

## Troubleshooting and Final Steps

If you encounter issues with the server setup or if the custom script extension becomes unresponsive, download and run the Gembox script from the jumpbox. This script will apply the necessary configuration changes to all machines.

<Frame>
  ![The image illustrates application gateway routing rules, showing path-based routing and multiple-site routing with different server pools for images, videos, learning, and labs.](https://kodekloud.com/kk-media/image/upload/v1752884727/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Routing-Rules/application-gateway-routing-rules-2.jpg)
</Frame>

## Conclusion

In this guide, we demonstrated how to deploy and configure the Azure Application Gateway using both path-based and multi-site routing. We mapped backend pools to virtual machines and verified the entire setup through the Azure Portal. For additional load balancing strategies and performance optimizations, consider exploring alternative solutions to further enhance your network infrastructure.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/50248c52-4b17-4c2d-87f8-52a42eff2d2f/lesson/4707fd5c-4fc2-47b1-93fd-a86745c57d12" />
</CardGroup>

---


## Lesson 8: Other load balancing solutions

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Other-load-balancing-solutions/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Other-load-balancing-solutions/page.md)

**Summary:** This article explores additional Azure load balancing options beyond the standard services, offering insights for designing scalable and highly available architectures on Azure.

# Other load balancing solutions

> This article explores additional Azure load balancing options beyond the standard services, offering insights for designing scalable and highly available architectures on Azure.

In this article, we explore additional Azure load balancing options beyond the Azure Load Balancer and Azure Application Gateway. Although these solutions are not part of the exam syllabus, they offer valuable insights for designing robust, scalable, and highly available architectures on Azure.

Azure provides a range of load balancing services to meet diverse needs:

## Azure Front Door

Azure Front Door is a modern content delivery network (CDN) solution engineered for secure, rapid, and globally distributed content delivery. Leveraging the Microsoft Global Edge Network—which includes hundreds of global and local points of presence—Azure Front Door enables you to deploy solutions across multiple regions. It supports features such as path-based and multi-site routing and can easily integrate with a web application firewall to enhance your application's security.

## Azure Traffic Manager

Azure Traffic Manager is a DNS-based load balancer designed to optimize client request distribution across your application endpoints. By using DNS to direct traffic based on customizable routing rules, Traffic Manager selects the optimal endpoint and returns its DNS response. It supports a variety of routing methods including priority, weighted, geographic, performance-based routing, and even nested profiles. This solution works seamlessly with both public-facing Azure services and known Azure environments.

## Comparison of Azure Load Balancing Solutions

Below is a visual comparison of different load balancing solutions, detailing features such as usage, protocols, internal support, cross-region capabilities, environments, and security.

<Frame>
  ![The image is a comparison table of different load balancing solutions, detailing features such as usage, protocols, internal support, cross-region capabilities, environment, and security for Application Gateway, Front Door, Load Balancer, and Traffic Manager.](https://kodekloud.com/kk-media/image/upload/v1752884717/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Other-load-balancing-solutions/load-balancing-solutions-comparison.jpg)
</Frame>

### Key Features Overview

* **Usage:**
  * *Application Gateway* is optimized for backend application server farms and enhances security via its web application firewall.
  * *Front Door* delivers a scalable and secure global entry point for microservice-based web applications.
  * *Load Balancer* balances both inbound and outbound traffic, efficiently routing requests to application or server endpoints.
  * *Traffic Manager* distributes traffic across different Azure regions, ensuring high availability and responsive performance.

* **Protocols Supported:**
  * **Application Gateway** and **Front Door:** Support HTTP, HTTPS, and HTTP/2.
  * **Load Balancer:** Supports TCP and UDP.
  * **Traffic Manager:** Is protocol-agnostic as it operates at the DNS level.

* **Deployment Types:**
  * *Internal Solutions:* Application Gateway and Azure Load Balancer can be deployed for internal use.
  * *External-Facing Solutions:* Front Door and Traffic Manager are designed for public endpoints.
  * *Cross-Region Capabilities:* Front Door provides built-in cross-region support, whereas Application Gateway is limited to specific regions.

* **Global Reach and Environments:**
  * **Global Solutions:** Both Front Door and Traffic Manager are inherently global, with Azure Load Balancer also expanding its global availability in preview.
  * **Regional Constraints:** Application Gateway must be tied to a specific region, although Traffic Manager’s metadata is managed at the resource group level.
  * **Resource Compatibility:** Application Gateway, Front Door, and Traffic Manager support Azure, non-Azure, and on-premises resources, while Load Balancer is limited to Azure-based resources.

* **Security Options:**
  * *Application Gateway* and *Front Door* support the integration of web application firewalls and network security groups (NSGs).
  * The *Azure Load Balancer* relies solely on NSGs for its security configuration.
  * *Traffic Manager* does not provide intrinsic security features, as it only resolves DNS responses without directly managing traffic flows.

<Callout icon="lightbulb" color="#1CB2FE">
  For more detailed comparisons and further technical insights, refer to the official Microsoft documentation and Azure load balancing resources.
</Callout>

Having reviewed these load balancing solutions, we now move on to an overview of Network Watcher, which provides comprehensive network monitoring and diagnostic tools in Azure.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/50248c52-4b17-4c2d-87f8-52a42eff2d2f/lesson/c1488bff-fcdc-44e3-8ef9-6ff13280a7fc" />
</CardGroup>

---


## Lesson 9: Network Watcher

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Network-Watcher/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Network-Traffic/Network-Watcher/page.md)

**Summary:** Azure Network Watcher offers diagnostic and monitoring tools for insights into Azure network performance, health, and security.

# Network Watcher

> Azure Network Watcher offers diagnostic and monitoring tools for insights into Azure network performance, health, and security.

Azure Network Watcher is a robust suite of diagnostic and monitoring tools designed to help you gain deep insights into your Azure network infrastructure's performance, health, and security.

<Frame>
  ![The image shows a list of network diagnostic tools, monitoring options, and logs under the title "Network Watcher." It includes tools like IP flow verify, NSG diagnostic, and monitoring options like Topology and Network Performance Monitor.](https://kodekloud.com/kk-media/image/upload/v1752884707/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Watcher/network-watcher-diagnostic-tools.jpg)
</Frame>

Below, you will find a detailed overview of several key network diagnostic tools that are essential for both troubleshooting and exam preparation:

1. **IP Flow Verify**

   IP Flow Verify determines if a packet is allowed or denied based on the current Network Security Group (NSG) rules. It is especially useful when you suspect that a particular port is being blocked. For example, you can simulate traffic to confirm whether the NSG is inadvertently preventing connectivity.

2. **Next Hop**

   The Next Hop tool helps you trace the path a packet takes within your Azure Virtual Network. This is beneficial when troubleshooting routing issues. If you have configured a route table to forward traffic to a firewall but cannot see the traffic at the firewall, Next Hop can reveal whether the traffic is correctly directed.

3. **VPN Diagnostics**

   VPN Diagnostics enables you to assess the health of your VPN Gateways and connections, ensuring that secure connectivity to your on-premises infrastructure is maintained. Diagnostic data is stored in a designated storage account, which can be reviewed later to troubleshoot connectivity problems.

4. **NSG Flow Logs**

   NSG Flow Logs capture detailed information about ingress and egress IP traffic as it flows through your NSGs. These logs are crucial for auditing and analyzing network security policies. Once the logs are collected, they are stored in a storage account for further analysis.

5. **Connection Troubleshoot**

   Connection Troubleshoot provides insights into the connectivity between two endpoints. It displays information like travel time, intermediate hops, and any issues that may be blocking the connection, thus simplifying the troubleshooting process.

6. **Topology**

   The Topology feature offers a visual map of the components within your Virtual Network. It displays the arrangement of resources such as virtual machines, subnets, and network interfaces, helping you understand the overall architectural layout of your solution.

<Callout icon="lightbulb" color="#1CB2FE">
  Each tool within Network Watcher plays a vital role in ensuring clear visibility into your network's operation and security. This guide will walk you through how each feature functions within the Azure Portal.
</Callout>

***

## Exploring Network Watcher in the Azure Portal

To get started, log into the [Azure Portal](https://portal.azure.com/) and search for "Network Watcher." Once you access the service, you'll see a list of available tools to diagnose and monitor your network.

### IP Flow Verify

To diagnose traffic connectivity issues for a virtual machine:

1. Navigate to IP Flow Verify.
2. Select a virtual machine (e.g., the Gembox VM) and choose its network interface.
3. Set the protocol to TCP and the direction to inbound.
4. Specify the local IP address and port (for example, local port 3389) and then provide the remote IP address along with its corresponding port (e.g., 3389).

<Frame>
  ![The image shows the "Network Watcher | IP flow verify" page in the Microsoft Azure portal, where users can specify network diagnostic settings for a virtual machine.](https://kodekloud.com/kk-media/image/upload/v1752884709/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Watcher/network-watcher-ip-flow-verify.jpg)
</Frame>

This tool checks if traffic from the specified remote IP and port can reach the target machine. For instance, if using a Linux VM configured with a "deny all inbound" rule, port 3389 may be blocked. In such cases, testing port 22 (a common SSH port) might show successful connectivity.

### NSG Diagnostics

NSG Diagnostics collects logs from your NSGs and sends them to a storage account for further analysis. These logs help you review traffic patterns and evaluate the impact of your security rules.

### Next Hop

The Next Hop tool determines the subsequent route for network packets. For instance, if two virtual machines within the same Virtual Network are involved, the expected next hop is typically "vnet local." The test will indicate if the system’s default route or a user-defined route (UDR) is in effect. If an external internet destination is involved or a virtual appliance with a UDR is used, the tool will display "internet" or "virtual appliance" along with the corresponding IP address and details.

<Frame>
  ![The image shows the "Network Watcher | Next hop" page in Microsoft Azure, where a user is configuring network diagnostic tools by specifying a target virtual machine and destination IP address.](https://kodekloud.com/kk-media/image/upload/v1752884710/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Watcher/network-watcher-next-hop-azure.jpg)
</Frame>

### Effective Security Rules

This feature aggregates and displays all effective NSG rules when multiple NSGs are applied (such as at both the subnet and network interface levels). It consolidates these rules, allowing you to easily understand the overall security posture impacting your resources.

### VPN Troubleshoot

VPN Troubleshoot allows you to diagnose issues with your VPN Gateway and its connections. By selecting an appropriate storage account, you can capture diagnostic metrics like bandwidth and throughput, which help identify potential issues such as packet drops.

<Frame>
  ![The image shows the Microsoft Azure portal, specifically the Network Watcher VPN troubleshoot page, where users can diagnose the health of virtual network gateways or connections. It includes options to select a subscription, resource group, and location, with a section for selecting a storage account.](https://kodekloud.com/kk-media/image/upload/v1752884711/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Watcher/azure-portal-network-watcher-vpn-troubleshoot.jpg)
</Frame>

### Packet Capture

Packet Capture eliminates the need to install separate tools like Wireshark or TCPdump on your virtual machine. Instead, you can initiate a packet capture session directly from the Azure Portal by:

* Selecting the target virtual machine.
* Specifying the storage account for saving the capture file.
* Applying filters, such as capturing traffic on a specific port (e.g., port 53).

After capturing the network traffic, you can download the .pcap file and analyze it using Wireshark.

<Frame>
  ![The image shows the Microsoft Azure portal with the "Network Watcher | Packet capture" interface open, displaying options for configuring a packet capture session.](https://kodekloud.com/kk-media/image/upload/v1752884713/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Watcher/azure-portal-network-watcher-packet-capture.jpg)
</Frame>

### Connection Troubleshoot

Connection Troubleshoot helps verify connectivity between two endpoints. For example, to test connectivity between the Gembox VM and another virtual machine (e.g., a blue VM):

1. Choose IPv4.
2. Select the desired protocol (such as TCP) and specify the destination port (e.g., 22).
3. Run the diagnostic test to collect data on next hop details, round trip times, effective NSG rules, and port accessibility.

<Frame>
  ![The image shows the Microsoft Azure Network Watcher interface, specifically the "Connection Troubleshoot" section, where a user is configuring settings for diagnosing network connectivity issues between virtual machines.](https://kodekloud.com/kk-media/image/upload/v1752884714/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Watcher/azure-network-watcher-connection-troubleshoot.jpg)
</Frame>

The detailed results will include insights into connectivity status, NSG rules (both inbound and outbound), next hop information, and overall network performance.

### Topology

The Topology tool provides a visual layout of your Virtual Network. By selecting a particular virtual network, you can view its topology, which includes resources such as virtual machines, network interfaces, and subnets. For example, you might see a diagram displaying components such as a gateway NSG, blue subnet, and red subnet. Expanding a subnet (like the blue subnet) allows you to view the underlying resources, including each virtual machine and its associated network interface.

<Frame>
  ![The image shows the Microsoft Azure Network Watcher interface displaying a network topology with two nodes, "blue-01" and "jumpbox-vm," both showing successful status. A pop-up message indicates unsaved edits will be discarded.](https://kodekloud.com/kk-media/image/upload/v1752884715/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Watcher/azure-network-watcher-topology.jpg)
</Frame>

Expanding further:

<Frame>
  ![The image shows the Microsoft Azure Network Watcher interface displaying a network topology diagram. It includes various nodes and connections representing virtual networks and resources.](https://kodekloud.com/kk-media/image/upload/v1752884716/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Network-Watcher/azure-network-watcher-topology-diagram.jpg)
</Frame>

This visual representation provides a clear understanding of how virtual machines, multiple NICs, and their IP configurations are interconnected.

***

That concludes our in-depth overview of Azure Network Watcher. With these powerful tools at your disposal, managing and troubleshooting your Azure network has never been easier.

<Callout icon="lightbulb" color="#1CB2FE">
  In the next section, we will dive into best practices for administering Azure Storage. Stay tuned to expand your Azure knowledge!
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/50248c52-4b17-4c2d-87f8-52a42eff2d2f/lesson/1e4f0186-2a9f-4d86-af45-e86419735858" />
</CardGroup>

---


# Section 08: Administer Azure Storage

---


## Lesson 1: Module Introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Module-Introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Module-Introduction/page.md)

**Summary:** This article explores managing storage solutions within Azure, covering storage accounts, services, security best practices, and ensuring data accessibility.

# Module Introduction

> This article explores managing storage solutions within Azure, covering storage accounts, services, security best practices, and ensuring data accessibility.

In this article, we will explore the key aspects of managing storage solutions within the [Azure Cloud Platform](https://azure.microsoft.com/en-us/services/storage/). Azure Storage provides a suite of services that are highly available, secure, durable, scalable, and redundant, ensuring reliable storage for all your data.

## Learning Objectives

In this module, you will learn how to:

* Create and manage storage accounts as containers for your storage data.
* Utilize various storage services, including blobs, files, queues, tables, and disks.
* Configure Blob Storage for efficiently handling vast amounts of unstructured data (e.g., text or binary data).
* Set up Azure Files to provide fully managed file shares that are accessible via SMB or NFS protocols, whether in the cloud or on-premises.
* Implement storage security best practices by configuring access keys, shared access signatures, service encryption, and network rules to protect your storage infrastructure.

<Frame>
  ![The image lists learning objectives related to configuring storage in Azure, including storage accounts, blob storage, Azure files, and storage security. It features a gradient background with numbered steps.](https://kodekloud.com/kk-media/image/upload/v1752884390/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Module-Introduction/azure-storage-learning-objectives.jpg)
</Frame>

By the end of this module, you will have the expertise to deploy and manage Azure Storage solutions, ensuring your data remains secure and easily accessible.

<Callout icon="lightbulb" color="#1CB2FE">
  Familiarize yourself with the basic concepts of Azure Storage as you progress through this module; it will build a solid foundation for the advanced topics ahead.
</Callout>

Let's begin with the first topic: configuring storage accounts.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/44d08df2-a735-4a20-a44d-b751afdfb332" />
</CardGroup>

---


## Lesson 2: Storage accounts

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Storage-accounts/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Storage-accounts/page.md)

**Summary:** This article explores Azure Storage accounts, their benefits, services, and types to optimize cloud storage strategies.

# Storage accounts

> This article explores Azure Storage accounts, their benefits, services, and types to optimize cloud storage strategies.

Azure Storage accounts are the fundamental building blocks for data storage in Azure, offering secure, scalable cloud storage for a wide range of data objects. In this article, we explore the benefits, services, and account types available in Azure Storage, helping you optimize your cloud storage strategy.

## Key Benefits

Azure Storage accounts provide several key advantages that make them an essential component of any cloud architecture:

* **High Availability and Durability:**\
  Multiple redundancy options allow your data to be replicated across different data centers—or even across regions—to ensure maximum availability and durability.

* **Security:**\
  Data stored in Azure is automatically encrypted using storage service encryption. Additionally, various authorization methods are available, including storage keys, shared access signatures, and Azure Active Directory (now known as Microsoft Entra ID).

* **Scalability and Management:**\
  Managed as a platform service, Azure Storage automatically adjusts to your performance and storage needs, making it an ideal solution for both small and large-scale applications.

* **Access:**\
  Secure access via HTTP or HTTPS is provided through Microsoft’s SDKs, Azure PowerShell, Azure CLI, and REST APIs, ensuring seamless integration with your applications.

Azure Storage supports two performance tiers:

* **Standard:**\
  Uses magnetic drives to offer cost-effective storage for workloads that do not require high throughput and low latency.
* **Premium:**\
  Utilizes solid-state drives for high-performance workloads, making it ideal for databases and high-processing applications.

Azure Storage accounts are versatile and support various data types and scenarios:

* **Virtual Machine Storage:**\
  Provides reliable disk storage for running a wide range of applications on Azure.
* **Unstructured Data:**\
  Blob storage is optimized for storing massive amounts of text, binary data, documents, media files, and installers.
* **Structured Data:**\
  Azure Table Storage is suitable for applications that manage structured data sets like user information and metadata.

Overall, Azure Storage accounts offer a robust, flexible platform for both everyday applications and data-intensive workloads.

## Azure Storage Services

Azure Storage comprises multiple services, each optimized for specific use cases. A single storage account can host several services, making it easy to consolidate your storage needs. Below are the primary services along with their use cases:

### Containers (Azure Blob Storage)

Containers in Azure Blob Storage are used for storing unstructured data such as documents, images, videos, and audio files. For example, a media hosting service can use Blob Storage to store and manage user-uploaded videos and photos. Each file is stored as a blob within a container, which functions similarly to a directory in your storage account.

### Azure Files

Azure Files provides a fully managed file share accessible via the SMB protocol. This service functions like a traditional file server, enabling shared access to files and directories across different locations. A common use case is document sharing and collaboration across geographically dispersed teams.

### Azure Tables

Azure Tables offer a scalable NoSQL data storage solution for structured data. Think of each entity as a row in a database. Applications that collect and manage user information, such as names, addresses, and contact details, can efficiently use Azure Tables for structured data storage.

### Azure Queues

Azure Queue Storage is designed to handle storage of large volumes of messages, accessible globally over authenticated HTTP or HTTPS. For instance, a video processing service might use queues to manage encoding tasks, where processing jobs are queued and processed by background services.

<Frame>
  ![The image is a diagram illustrating Azure Storage Services, showing the relationship between containers, files, tables, and queues with their respective data types like blobs, directories, entities, and messages. It highlights Azure Containers, Azure Files, Azure Tables, and Azure Queues.](https://kodekloud.com/kk-media/image/upload/v1752884406/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-accounts/azure-storage-services-diagram.jpg)
</Frame>

Each of these services is engineered for high availability, durability, and scalability, ensuring that your application maintains excellent performance as it grows.

## Storage Account Types

Azure offers a variety of storage account types to meet different operational and performance needs. Each account type provides distinct services, performance tiers, and replication options:

### Blob Storage

Designed specifically for storing unstructured data as blobs, this account type is ideal for hosting images, documents, audio, video, and more. It operates under the standard performance tier and supports replication options like Locally Redundant Storage (LRS), Geo-Redundant Storage (GRS), and Read-Access Geo-Redundant Storage (RA-GRS).

### General Purpose V1 (GPV1)

The first-generation storage account gives you access to all Azure Storage services, including blobs, files, queues, tables, and disks. GPV1 accounts are available in both standard and premium tiers and support replication options such as LRS, GRS, and REGRS.

### General Purpose V2 (GPV2)

Recommended for most scenarios, the second-generation GPV2 storage account offers enhanced performance and a wider range of replication choices, including Zone-Redundant Storage (ZRS), Geo-Zone-Redundant Storage (GZRS), and Read-Access Geo-Zone-Redundant Storage (RA-GZRS) along with all services offered by GPV1.

### Block Blob Storage

Optimized for block blobs and append blobs, this account type is ideal for textual and binary data storage. Operating under the premium performance tier, it delivers higher throughput and lower latency, supporting replication options like LRS and GRS.

### File Storage

Specifically designed for cloud-based file shares, File Storage is perfect for legacy applications that rely on traditional file systems. Available in the premium tier, this account type ensures high throughput and low latency with replication options such as LRS and GRS.

<Frame>
  ![The image is a table listing different storage account types, their services, performance tiers, and replication options. It includes types like Blob storage, General Purpose V1 and V2, Block blob storage, and File storage.](https://kodekloud.com/kk-media/image/upload/v1752884407/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-accounts/storage-account-types-table.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  If you find the various replication options such as LRS, GRS, and REGRS confusing, detailed explanations of each method are provided in the subsequent discussion.
</Callout>

## Storage Redundancy

In the next section, we will dive deeper into the storage redundancy options provided by Azure. Understanding these replication methods will help you make informed decisions about data durability and availability, ensuring that your applications remain resilient in case of hardware failures or other disruptions.

For more information on Azure Storage services and best practices, consider visiting the following resources:

* [Azure Storage Documentation](https://docs.microsoft.com/en-us/azure/storage/)
* [Microsoft Entra ID Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)

Stay tuned for our upcoming discussion on storage redundancy to further optimize your Azure environment.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/1d82ecd0-b25b-4c2b-b8a7-e197aed0a16c" />
</CardGroup>

---


## Lesson 3: Storage redundancy

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Storage-redundancy/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Storage-redundancy/page.md)

**Summary:** This guide explores various storage replication strategies in Azure, balancing data durability, availability, and cost for different application needs.

# Storage redundancy

> This guide explores various storage replication strategies in Azure, balancing data durability, availability, and cost for different application needs.

This guide explores the various storage replication strategies in Azure, including Locally Redundant Storage (LRS), Zone Redundant Storage (ZRS), Geo-Redundant Storage (GRS), Read Access Geo-Redundant Storage (RA-GRS), and Geo-Redundant Storage with Zones (GCRS and RA-GCRS). Each replication method balances data durability, availability, and cost differently. Choosing the right strategy depends on your application’s needs.

## Locally Redundant Storage (LRS)

LRS creates three copies of your data within a single data center, distributing them across different fault domains. Fault domains are isolated hardware units endowed with independent cooling, power, and networking systems. In case of a hardware failure, the replicated copies ensure data availability. However, LRS only covers a single data center, and if that center goes down, access to your data will be interrupted. Despite this, LRS remains the most cost-effective option, offering 99.99% durability.

<Frame>
  ![The image illustrates "Storage Replication – Locally Redundant Storage" with a diagram showing data replication across multiple servers within a single data center, highlighting one server with a red cross to indicate failure.](https://kodekloud.com/kk-media/image/upload/v1752884408/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-redundancy/storage-replication-locally-redundant-diagram.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  For scenarios where cost efficiency is critical and data center-wide disasters are unlikely, LRS is a solid choice.
</Callout>

## Zone Redundant Storage (ZRS)

ZRS enhances resilience by replicating data across three different availability zones within a single region. Each zone is typically situated in separate clusters of data centers located at least 300 miles apart, ensuring independent power, cooling, and networking. This redundancy means if one zone fails, the other zones maintain data availability. ZRS provides 99.12% durability but does not safeguard against a full regional outage.

<Frame>
  ![The image illustrates zone-redundant storage (ZRS) with three zones (A, B, and C) within a region, highlighting replication, durability, and chances of failure. Zone B is marked with an "X" to indicate a failure, while Zones A and C show storage availability.](https://kodekloud.com/kk-media/image/upload/v1752884408/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-redundancy/zone-redundant-storage-illustration.jpg)
</Frame>

## Geo-Redundant Storage (GRS)

GRS offers enhanced redundancy by combining data replication in two regions. Initially, your data is replicated in a primary region using LRS (three copies within one data center). The system then asynchronously replicates the data to a secondary region, also utilizing LRS. In the event that the primary region experiences an outage, a failover can be initiated—either manually or by Microsoft—to the secondary region. Note that the secondary region provides read access only until a complete failover occurs. GRS guarantees 99.69% durability.

<Frame>
  ![The image illustrates a geo-redundant storage system with replication and durability features, showing a primary and secondary data center setup with failover capabilities. It highlights the concept of geo-replication for enhanced data reliability.](https://kodekloud.com/kk-media/image/upload/v1752884409/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-redundancy/geo-redundant-storage-replication-diagram.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  When planning for GRS, remember that new data writes during a regional outage require additional application logic (using mechanisms like queues or a secondary storage account) to ensure proper synchronization when the primary region is restored.
</Callout>

## Read Access Geo-Redundant Storage (RA-GRS)

RA-GRS functions similarly to GRS by maintaining three data copies in both the primary and secondary regions. However, it extends functionality by enabling continuous read access from the secondary region. This setup allows your applications to query data from the secondary region without the need for a manual failover, providing a balance between accessibility and redundancy. RA-GRS achieves 99.16% durability.

<Frame>
  ![The image illustrates a storage replication process with read access geo-redundant storage, showing primary and secondary data centers, geo-replication, and failover mechanisms. It highlights replication, durability, and considerations for storage accounts.](https://kodekloud.com/kk-media/image/upload/v1752884410/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-redundancy/storage-replication-geo-redundancy-diagram.jpg)
</Frame>

## Geo-Redundant Storage with Zones (GCRS and RA-GCRS)

By integrating the benefits of availability zones into geo-redundancy, Azure’s GCRS takes data protection further:

* In GCRS, data is first spread across three availability zones within the primary region. It is then asynchronously replicated (using LRS) to a secondary region, effectively combining zone-level and region-level redundancy for higher durability ("ZRS plus LRS").
* RA-GCRS operates in a similar fashion, but it allows for continuous read access to the secondary region without waiting for a failover.

<Frame>
  ![The image illustrates a storage replication system with geo-zone-redundant storage, showing a primary region with multiple zones and a secondary region for geo-replication. It highlights the flow of read requests from clients to the storage account.](https://kodekloud.com/kk-media/image/upload/v1752884412/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-redundancy/storage-replication-geo-redundancy-diagram-2.jpg)
</Frame>

## Creating a Storage Account in Azure

Follow these steps to create and configure a storage account through the Azure portal:

1. **Sign in to the Azure portal:** Navigate to "Storage accounts."
2. **Initiate Creation:** Click "Create" and select the desired subscription and resource group. If needed, create a new resource group.
3. **Name Your Account:** Provide a unique name—this name will be part of your account’s public endpoint.
4. **Configure Settings:** Choose the region for deployment along with the performance tier (HDD or SSD) and the redundancy option (LRS, GRS, ZRS, etc.). For demonstration purposes, LRS is selected due to its cost efficiency.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a storage account, with options for project details, instance details, and redundancy settings. A dropdown menu is open, displaying different redundancy options like locally-redundant storage and geo-redundant storage.](https://kodekloud.com/kk-media/image/upload/v1752884413/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-redundancy/azure-portal-storage-account-creation.jpg)
</Frame>

5. **Review and Create:** Double-check your configuration settings and click "Review + Create."
6. **Manage Your Storage Account:** Once the account is created, you can explore services like blobs, file shares, queues, and tables.

<Frame>
  ![The image shows a Microsoft Azure portal screen where a user is in the process of creating a storage account, with details such as subscription, resource group, and location displayed. The "Review" tab is active, and a notification indicates that deployment is being initialized.](https://kodekloud.com/kk-media/image/upload/v1752884415/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-redundancy/azure-portal-storage-account-creation-2.jpg)
</Frame>

7. **View Account Properties:** After deployment, the storage account overview will indicate that it is a general-purpose v2 account using LRS. Should your requirements change, you can later modify the redundancy option (for example, switching from LRS to ZRS) via the account's redundancy settings.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a storage account, including its properties, security settings, and networking configurations.](https://kodekloud.com/kk-media/image/upload/v1752884416/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-redundancy/azure-portal-storage-account-details.jpg)
</Frame>

## Summary

This article outlines the different storage replication strategies available in Azure:

| Storage Type   | Redundancy Location                              | Durability | Key Benefit                                            |
| -------------- | ------------------------------------------------ | ---------- | ------------------------------------------------------ |
| LRS            | Single data center across multiple fault domains | 99.99%     | Most cost-effective with intra-data center replication |
| ZRS            | Multiple zones within one region                 | 99.12%     | Protects against zone-level failures                   |
| GRS            | Primary and secondary regions                    | 99.69%     | Enables failover to a secondary region                 |
| RA-GRS         | Primary and secondary regions                    | 99.16%     | Continuous read access in the secondary region         |
| GCRS / RA-GCRS | Availability zones in primary + secondary region | Very high  | Combines zone and regional redundancy                  |

Choose the strategy that best aligns with your application’s availability and cost requirements. For more detailed insights, visit the [Azure Storage Documentation](https://docs.microsoft.com/azure/storage/common/storage-redundancy).

By following this guide, you can confidently select and configure the optimal storage redundancy option for your Azure solutions.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/9f6ffdb2-5648-4afe-a1d1-c8b1d806e9c8" />
</CardGroup>

---


## Lesson 4: Accessing storage endpoints

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Accessing-storage-endpoints/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Accessing-storage-endpoints/page.md)

**Summary:** Learn to construct and understand the endpoints required to access various services within an Azure storage account.

# Accessing storage endpoints

> Learn to construct and understand the endpoints required to access various services within an Azure storage account.

In this lesson, you'll learn how to construct and understand the endpoints required to access various services within an Azure storage account. Each storage service follows a consistent endpoint URL format, making it easy to integrate and manage your storage resources.

Every endpoint is built using the following structure:

```plaintext theme={null}
<protocol>://<storage account name>.<service>.core.windows.net
```

Here's what each element represents:

* **Protocol:** Either `HTTP` or `HTTPS`.
* **Storage Account Name:** The unique name you have chosen for your account.
* **Service:** Represents the Azure service you are accessing (e.g., blob, queue, file, or table).
* **Domain:** All endpoints end with `core.windows.net`, which is the default domain for Azure storage.

For example, if your storage account is named `KodeKloud`, the corresponding endpoints would be:

* **Blob Service:** kodekloud.blob.core.windows.net
* **Queue Service:** kodekloud.queue.core.windows.net
* **File Service:** kodekloud.file.core.windows.net
* **Table Service:** kodekloud.table.core.windows.net

<Callout icon="lightbulb" color="#1CB2FE">
  If your preferred storage account name is already taken, consider modifying it by appending additional characters or using a custom domain. This approach can also reinforce your branding; for example, you might configure `blobs.codecloud.com` to point to `codecloud.blob.core.windows.net`.
</Callout>

<Frame>
  ![The image provides information on accessing storage endpoints for a storage account, showing the format for endpoint URLs and examples for different services like container, queue, file, and table. It also mentions using a custom domain with CNAME mapping.](https://kodekloud.com/kk-media/image/upload/v1752884371/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Accessing-storage-endpoints/storage-endpoints-url-format-examples.jpg)
</Frame>

In addition to direct URL access, several tools help manage your Azure storage resources effectively:

## Azure Storage Management Tools

| Tool                   | Description                                                                                                                                              | Example Command/Usage                                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Azure Storage Explorer | Desktop application that connects to your storage account, allowing you to drag and drop files, delete files, and manage data directly.                  | Launch the app and connect using your storage account credentials                                                      |
| Import Export Service  | Service for transferring large quantities of on-premises data (terabytes or more) into Azure. It enables secure data transfer via pre-configured drives. | Prepare drives, copy, encrypt, and ship them to an Azure Data Center for upload                                        |
| AZCopy                 | Command-line tool designed for fast and efficient data transfers within your storage account, and supports other cloud providers like GCP and AWS.       | `azcopy copy [source] [destination] [flags]` This command can be automated to handle disaster recovery data transfers. |

<Frame>
  ![The image shows a configuration guide for storage tools, featuring Azure Storage Explorer and an Import and Export Service interface.](https://kodekloud.com/kk-media/image/upload/v1752884372/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Accessing-storage-endpoints/azure-storage-tools-configuration-guide.jpg)
</Frame>

For example, the following command uses AZCopy to transfer data:

```bash theme={null}
azcopy copy [source] [destination] [flags]
```

This tool is especially useful for automating data workflows and migrating data between different cloud providers.

When managing your storage account via the Azure Portal, you can easily capture the endpoints for blob, file, queue, table services, and even static website hosting. Additionally, services like Data Lake Store—designed for analytics—offer their own respective endpoints.

Up next, we will explore how to configure Azure Blob Storage, building on the concepts discussed in this lesson.

<Callout icon="lightbulb" color="#1CB2FE">
  For further reading on Azure storage, visit the [Azure Storage Documentation](https://docs.microsoft.com/en-us/azure/storage/) and explore [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) for related containerized solutions.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/1ccae4d6-20ed-4ebc-9042-ea47f2d66dbc" />
</CardGroup>

---


## Lesson 5: Azure Containers

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Azure-Containers/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Azure-Containers/page.md)

**Summary:** This article provides an overview of Azure Blob Storage architecture, including storage accounts, containers, blobs, access levels, and file management using the Azure Portal.

# Azure Containers

> This article provides an overview of Azure Blob Storage architecture, including storage accounts, containers, blobs, access levels, and file management using the Azure Portal.

## Configuring Azure Blob Storage

Azure Blob Storage is a robust service for storing a vast amount of unstructured data, including text and binary data. Accessible globally via HTTP or HTTPS, it is ideal for serving images, documents, streaming media, writing log files, and handling backup, restore, disaster recovery, or archival scenarios.

The Blob Storage architecture is structured into three main components: storage accounts, containers, and blobs.

### Storage Account

At the highest level is the Storage Account, which serves as the unique namespace in Azure for your data. This account holds all access keys, properties, and configurations, functioning as the "web files" repository where your data is stored.

### Containers

Inside a storage account, containers work like directories in a file system. They group related blobs and dictate access policies. For example, within the "web files" storage account, you might create separate containers for documents and videos. A documents container could hold PDF files, while a videos container might store MP4 files.

### Blobs

Blobs are the individual files stored in Azure Blob Storage and can be of any type and size. Azure Blob Storage supports three types of blobs:

1. **Block Blobs**\
   These are optimal for storing text and binary data, with a maximum size of up to 4.75 TB. They allow efficient management of large data sets by handling each block individually.\
   Examples include various documents and media files.

2. **Append Blobs**\
   Specifically designed for append operations, these blobs are perfect for logging scenarios. When your application continuously writes logs, append blobs ensure efficient addition of new entries.

3. **Page Blobs**\
   With a capacity of up to 8 TB, page blobs are engineered for frequent read-write operations and are ideal for storing virtual machine disks.

A practical example is a website hosting its assets on Azure Blob Storage. The website might use a "web files" storage account with dedicated containers for different asset types (e.g., PDFs in one and videos in another). Users can directly retrieve these blobs based on the access policies set within the containers.

### Creating and Managing Containers

Containers can be created through the Azure Portal, Azure PowerShell, CLI, or REST APIs. They function similarly to directories on your local machine. A critical setting for containers is the public access level, which determines how blobs are available to the public. The access levels include:

* **Private**\
  No anonymous access is allowed. Access is restricted to the account owner or specifically authorized users.

<Frame>
  ![The image illustrates the process of creating containers in a storage account, showing a hierarchy from storage account to containers and blobs, with a focus on privacy settings.](https://kodekloud.com/kk-media/image/upload/v1752884373/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Containers/storage-account-containers-privacy.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Enabling private access ensures that sensitive data remains protected unless accessed with proper authentication and authorization.
</Callout>

* **Blob**\
  This setting permits anonymous read access to individual blobs, though container metadata remains concealed. Users can access blobs via direct URLs but cannot list all blobs in the container.

* **Container**\
  With container-level access, all content within the container is publicly readable. This setting allows users to list and download blobs, making it suitable for hosting public content like images or documents.

These access levels can be adjusted at any time based on your data security requirements.

### Creating a Container and Uploading Blobs via the Azure Portal

Follow these steps to create and manage containers in the Azure Portal:

1. Navigate to your storage account and select the "Containers" section.
2. Click "Add" to create a new container. For example, name the container "images".

<Callout icon="lightbulb" color="#1CB2FE">
  If certain options appear greyed out, it may be due to your storage account's default settings. You might need to enable the "allow blob anonymous access" option in the storage account's configuration.
</Callout>

<Frame>
  ![The image shows the configuration settings of a Microsoft Azure storage account, with options for performance, secure transfer, and access settings. A notification indicates that the storage account was successfully updated.](https://kodekloud.com/kk-media/image/upload/v1752884375/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Containers/azure-storage-account-configuration.jpg)
</Frame>

3. After enabling the appropriate settings, select the desired public access level—in this case, container-level access for the "images" container.
4. Open the "images" container and click "Upload" to add your files. Browse for your files, select them, and confirm the upload. The portal automatically checks for naming conflicts before completing the process.

Once the upload is complete, you can click on an individual blob to view its properties and obtain its URL.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying the properties of a blob named "City1.jpg" within a storage container. It includes details like URL, size, type, and encryption status.](https://kodekloud.com/kk-media/image/upload/v1752884376/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Containers/azure-portal-blob-properties-city1.jpg)
</Frame>

For example, when you copy the URL of a blob like "City1.jpg" and paste it into your browser, the image will load if the public access level is enabled. Changing the access level to private and refreshing the page will result in a "resource not found" error, requiring storage access keys or Azure AD authentication for access.

### Understanding Storage Tiers

In addition to access levels, storage tiers play a significant role in optimizing cost and performance. Typically, content is initially set to the "hot" tier. Storage tiers allow you to balance performance and cost by moving data between different tiers based on usage patterns. Detailed discussions on storage tiers will be covered in upcoming lessons.

This article provided a comprehensive overview of Azure Blob Storage architecture, highlighting the roles of storage accounts, containers, and blobs. It also showcased how to manage access levels and upload files using the Azure Portal. In subsequent lessons, you will explore storage tiers in-depth and learn how to secure access further using storage keys and Azure AD authentication.

For more information on Azure Blob Storage and related topics, visit [Azure Documentation](https://docs.microsoft.com/azure/storage/blobs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/eaba2072-5c58-4b73-ae95-f5b0a5f19194" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/50777290-02c7-441f-92af-7d2134a01d13" />
</CardGroup>

---


## Lesson 6: Storage Tiers

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Storage-Tiers/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Storage-Tiers/page.md)

**Summary:** This article explains Azure Storage access tiers—Hot, Cool, and Archive—highlighting their specific use cases, cost structures, and configuration options.

# Storage Tiers

> This article explains Azure Storage access tiers—Hot, Cool, and Archive—highlighting their specific use cases, cost structures, and configuration options.

Azure Storage provides three main access tiers—Hot, Cool, and Archive—to accommodate various storage needs and cost efficiency requirements. Each tier is optimized for specific access patterns and cost profiles, ensuring that you can match your chosen tier with your data's usage frequency and retrieval speed requirements.

## Hot Tier

The Hot Tier is best suited for data that is frequently accessed and demands high availability. Although the storage cost is higher, it significantly reduces access costs, making it an ideal choice for transactional files, logs, or any data that is regularly read or modified.

## Cool Tier

The Cool Tier targets data that is accessed less frequently but still requires a reasonable retrieval speed. It offers lower storage costs compared to the Hot Tier, albeit at slightly higher access costs. This tier is particularly well-suited for data stored for at least 30 days, including monthly financial reports or backups that are only occasionally retrieved.

## Archive Tier

The Archive Tier is designed for data that is rarely accessed and for which longer retrieval times (several hours) are acceptable. With the lowest storage costs and the highest access fees, this tier is perfect for storing raw data such as old legal documents or historical records that do not require frequent modifications or rapid access.

### Pricing Overview

Below is an overview summarizing the cost differences among the storage tiers:

<Frame>
  ![The image illustrates storage access tiers (Hot, Cool, Archive) with associated storage and access costs, alongside a dropdown menu for changing the access tier.](https://kodekloud.com/kk-media/image/upload/v1752884403/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-Tiers/storage-access-tiers-costs-diagram.jpg)
</Frame>

* **Hot Storage:** Highest storage cost with lower access expense.
* **Cool Storage:** Lower storage cost compared to Hot, with increased access expense.
* **Archive Storage:** Lowest storage cost paired with the highest access fee.

When choosing an access tier, it is essential to weigh the frequency of data access against the required retrieval performance. For instance:

* Data that is regularly accessed, like transactional logs or real-time data streams, performs best on the Hot Tier.
* Infrequently accessed data—such as periodic backups or monthly financial reports—fits well with the Cool Tier.
* Long-term archival data, required for compliance or historical reference and accessed very rarely, is ideally stored in the Archive Tier.

## Configuring Storage Tiers in the Azure Portal

When you create an Azure storage account, you can select the default access tier—Hot or Cool—at the account level. The Archive (and Cold) options are configurable only at the object level.

Upon logging into the Azure Portal, the storage account overview displays the default access tier (for example, Hot). Selecting this option allows you to navigate to a configuration blade where you can change the default tier to Cool if necessary.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a storage account, including properties, security settings, and networking configurations.](https://kodekloud.com/kk-media/image/upload/v1752884404/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-Tiers/azure-portal-storage-account-details.jpg)
</Frame>

Within individual containers, such as one labeled "Site 1," you have the ability to adjust the access tier to Archive, Cold, or maintain Hot or Cool. By clicking on the "Change Tier" button, a selection menu presents the available options: Hot, Cool, Archive, and the newly introduced Cold Tier.

### Cold Tier

The Cold option provides an additional level of cost reduction for data that is not expected to be accessed for 90 days or longer. It offers even lower capacity costs compared to the Cool Tier.

<Callout icon="lightbulb" color="#1CB2FE">
  While some Azure Portal interfaces display a "Cold" option for object-level tiering, the primary officially supported access tiers in Azure Storage remain Hot, Cool, and Archive. Users should verify the latest Azure documentation to ensure compatibility with their storage account configuration.
</Callout>

## Upcoming: Lifecycle Management

In the next section, we will explore Lifecycle Management, an important feature that automates the organization and transition of data based on its access patterns and age. This helps optimize storage costs and improves data management efficiency.

For additional information on Azure Storage and configuration best practices, consider visiting the [Azure Storage Documentation](https://docs.microsoft.com/en-us/azure/storage/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/4055366c-d46e-44e9-9af8-2e292b23bd1c" />
</CardGroup>

---


## Lesson 7: Lifecycle Management

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Lifecycle-Management/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Lifecycle-Management/page.md)

**Summary:** Lifecycle management in Azure Storage optimizes costs by automatically transitioning data between access tiers based on usage patterns, reducing storage expenses without manual intervention.

# Lifecycle Management

> Lifecycle management in Azure Storage optimizes costs by automatically transitioning data between access tiers based on usage patterns, reducing storage expenses without manual intervention.

Lifecycle management in Azure Storage optimizes costs by automatically transitioning data between different access tiers—such as hot, cool, cold, and archive—based on usage patterns. When data remains unmodified for a defined period, policies automatically move blobs between tiers, reducing storage expenses without manual intervention.

This capability is available for Blob Storage and General Purpose v2 storage accounts only. If you're still using a General Purpose v1 storage account, you'll need to upgrade to General Purpose v2 to take advantage of lifecycle management.

Lifecycle management is based on policy-driven transitions. You can configure policies to:

* Automatically move blobs to cooler tiers based on their last modified date.
* Delete blobs and snapshots that haven’t been modified after a specified number of days.
* Filter policies to target specific file types (e.g., PDF or MP4 files).

Additionally, these policies support multiple blob types. Rules can be applied to Block Blobs, Append Blobs, and even target specific subtypes such as blob versions and snapshots.

Below is an example of a JSON lifecycle policy definition. In this example:

* Blobs not modified for 60 days are moved to the cool tier.
* Blobs not modified for 180 days are moved to the archive tier.
* Blobs not modified for 365 days are deleted.

```json theme={null}
{
  "rules": [
    {
      "enabled": true,
      "name": "rule",
      "type": "Lifecycle",
      "definition": {
        "actions": {
          "baseBlob": {
            "tierToCool": {
              "daysAfterModificationGreaterThan": 60
            },
            "tierToArchive": {
              "daysAfterModificationGreaterThan": 180
            },
            "delete": {
              "daysAfterModificationGreaterThan": 365
            }
          }
        }
      },
      "filters": {
        "blobTypes": [
          "blockBlob"
        ]
      }
    }
  ]
}
```

The policy above illustrates how a blob transitions to the cool tier after 60 days, to the archive tier after 180 days, and is ultimately deleted after 365 days.

<Callout icon="lightbulb" color="#1CB2FE">
  You do not need to write this JSON manually. The Azure portal offers a graphical interface to create these rules without any coding. Simply navigate to your storage account, select the Lifecycle Management option, and use the list view to add and configure your rule.
</Callout>

Returning to your storage account, select the Lifecycle Management option. Click "Add Rule" and enter a name (for example, "Policy 1"). Then you can set up filters to limit the policy to specific blob types—such as append blobs or block blobs—and even include snapshots and versions.

<Frame>
  ![The image shows a Microsoft Azure portal interface for adding a rule in lifecycle management. It includes options for rule name, rule scope, and blob type selections.](https://kodekloud.com/kk-media/image/upload/v1752884380/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Lifecycle-Management/azure-portal-lifecycle-management-rule.jpg)
</Frame>

After naming the rule, click "Next" to define the policy conditions. For example:

* If a blob was last modified more than 60 days ago, move it to the cool tier.
* If it was last modified 90 days ago, move it to cold storage.
* If modified over 180 days ago, move it to the archive tier, while skipping blobs that have been rehydrated in the last seven days.
* Finally, delete the blob after 365 days.

Each condition can be added using the "Add" button. Once you have finalized these settings, the policy will be created, and you can review its JSON representation directly within the portal.

<Frame>
  ![The image shows a Microsoft Azure interface for adding a rule in lifecycle management, where users can set conditions to move blobs to cooler storage or delete them based on their last modified or created date.](https://kodekloud.com/kk-media/image/upload/v1752884381/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Lifecycle-Management/azure-lifecycle-management-rule-interface.jpg)
</Frame>

Below is another example JSON policy that demonstrates executing multiple actions within a single rule. In this scenario, besides the cool and archive transitions, there is also a transition to the cold tier:

```json theme={null}
{
  "rules": [
    {
      "enabled": true,
      "name": "policy-1",
      "type": "lifecycle",
      "definition": {
        "actions": {
          "baseBlob": {
            "tierToCold": {
              "daysAfterModificationGreaterThan": 90
            },
            "tierToCool": {
              "daysAfterModificationGreaterThan": 60
            },
            "tierToArchive": {
              "daysAfterLastTierChangeGreaterThan": 7,
              "daysAfterModificationGreaterThan": 180
            },
            "delete": {
              "daysAfterModificationGreaterThan": 365
            }
          }
        },
        "filters": {
          "blobTypes": [
            "blockBlob"
          ]
        }
      }
    }
  ]
}
```

After you create the policy, you have the flexibility to enable or disable it as needed from the portal.

<Frame>
  ![The image shows the Microsoft Azure portal, specifically the "Lifecycle management" section of a storage account, with a policy named "policy-1" that is enabled for block blob type.](https://kodekloud.com/kk-media/image/upload/v1752884382/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Lifecycle-Management/azure-portal-lifecycle-management-policy1.jpg)
</Frame>

## Azure File Share Lifecycle Management

Now, let's focus on how lifecycle management applies to Azure File Share. (Content regarding Azure File Share lifecycle management continues here.)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/7dddf5a5-609c-47a0-aea2-276dc2af440b" />
</CardGroup>

---


## Lesson 8: Creating Azure File Share

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Creating-Azure-File-Share/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Creating-Azure-File-Share/page.md)

**Summary:** This article explains how to create and connect to an Azure File Share for cloud file storage.

# Creating Azure File Share

> This article explains how to create and connect to an Azure File Share for cloud file storage.

Azure File Share offers an enterprise-grade cloud file storage solution that can be accessed concurrently by multiple virtual machines, whether they are on Azure or not. This service supports Windows, Linux, and macOS operating systems and provides essential features such as backup, snapshots for data recovery, and compatibility with both SMB and NFS protocols. You can easily mount the file share on your system using script commands—just like an on-premises file share. Remember to ensure that port 445 is open for SMB traffic.

## Use Cases

Azure File Share is ideal for:

* Migrating from on-premises file shares to the cloud.
* Storing diagnostic data.
* Sharing tools and utilities across multiple teams.

## Creating a File Share in the Azure Portal

In this section, we detail how to create and connect to an Azure File Share using the Azure Portal.

1. Sign in to the Azure Portal and navigate to "File Shares."
2. Click on "Add a File Share" and enter a name (e.g., "Files01").
3. Select a performance tier that meets your requirements. Options include Transaction Optimized, Hot, and Cool—Transaction Optimized is optimal for applications requiring a reliable backend file store.
4. Set the maximum capacity (up to five terabytes) and click "Review and Create." The portal will then generate a script that you can use to mount the file share by specifying the drive letter, storage account key, and your operating system.

<Frame>
  ![The image shows a Microsoft Azure interface for creating a new file share, with options for naming, tier selection, and performance settings like maximum I/O and capacity.](https://kodekloud.com/kk-media/image/upload/v1752884377/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-Azure-File-Share/azure-file-share-creation-interface.jpg)
</Frame>

## Connecting to the Azure File Share

After the file share has been created, click on "Connect" in the Azure Portal to view the mounting script tailored for your operating system. The portal will display different scripts for Windows, Linux, and macOS. Make sure your local network allows traffic through port 445 for SMB connections, as some Internet Service Providers might block this port.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a file share named "files-01," including its properties, performance metrics, and backup status.](https://kodekloud.com/kk-media/image/upload/v1752884379/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-Azure-File-Share/azure-portal-file-share-details.jpg)
</Frame>

When you click "Show Script," the portal displays the relevant script for your operating system. Copy and execute the script on your system to mount the Azure File Share.

### Example: Connecting on Windows

Run the following PowerShell script in your terminal:

```powershell theme={null}
$ErrorActionPreference = "Stop"
$cmd = New-PSDrive -Name Z -PSProvider FileSystem -Root "\\demoaz0735533.file.core.windows.net\files-01" -Persist
if ($cmd) {
    Write-Host "Drive Z successfully mapped."
} else {
    Write-Error -Message "Unable to reach the Azure storage account via port 445. Check to make sure your organization or ISP is not blocking port 445, or use Azure P2S VPN, or ExpressRoute to tunnel SMB traffic over a different port."
}
```

After running this script, a new drive (for example, drive Z) should appear on your system. To verify the connection, try creating a new text document on the mounted drive.

For further configuration, you can save credential information and remount the file share using this script:

```powershell theme={null}
# Save Credential Information
cmd.exe /c "cmdkey /add:demooza0735533.file.core.windows.net /user:Azure\demooza0735533 /pass:YourPasswordHere"

# Mount the File Share
New-PSDrive -Name Z -PSProvider FileSystem -Root "\\demooza0735533.file.core.windows.net\files-01" -Persist
```

Once executed, you should observe the "demo" file or folder you created reflected in the Azure Portal.

## Securing Your Storage Account

Currently, the file share is accessible over the public internet. If you require enhanced security, Azure provides several options to restrict access. Consider using Azure P2S VPN or ExpressRoute to tunnel SMB traffic through an alternative port.

<Callout icon="lightbulb" color="#1CB2FE">
  For improved security and compliance, always review and configure your storage account's network settings according to your organization's best practices.
</Callout>

This guide has demonstrated how to create an Azure File Share, mount it on your computer, and troubleshoot connectivity issues. Enjoy exploring the robust capabilities of Azure File Share and streamline your file storage solutions in the cloud!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/b5a6ca91-86a6-46bd-8e03-f0b6ec3ccac4" />
</CardGroup>

---


## Lesson 9: Securing storage endpoints

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Securing-storage-endpoints/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Securing-storage-endpoints/page.md)

**Summary:** This article explains how to secure storage account endpoints using networking rules to control and restrict access for secure communication.

# Securing storage endpoints

> This article explains how to secure storage account endpoints using networking rules to control and restrict access for secure communication.

This article explains how to secure your storage account endpoints using robust networking rules. By following these guidelines, you can control and restrict access to your storage resources, ensuring secure and efficient communication.

When you access the Networking blade in your storage account, you will observe that public network access is enabled by default. However, you have several options to enhance security:

* Restrict public access by selecting specific virtual networks or IP addresses.
* Disable public network access completely.
* Integrate your existing virtual networks or create new ones for communication through service endpoints.
* Add designated IP ranges from your organization to the firewall for precise access control.

<Frame>
  ![The image is a screenshot of a networking settings interface for securing storage endpoints, highlighting options to control public access, restrict access to specific virtual networks, and allow IP ranges from the internet or on-premises.](https://kodekloud.com/kk-media/image/upload/v1752884391/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Securing-storage-endpoints/networking-settings-storage-endpoints.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  For organizations that prefer to eliminate all public communication, consider disabling public network access and configuring a private endpoint. This approach ensures a fully private connection to your storage accounts.
</Callout>

## Key Security Capabilities for Storage Accounts

Storage accounts are equipped with built-in security features that provide comprehensive protection:

* **Encryption:**\
  All data stored in your storage account is encrypted by default using Storage Service Encryption (SSE). No additional configuration is required, ensuring data remains secure at rest.

* **Authentication:**\
  Leveraging Azure Active Directory (Azure AD) and Role-Based Access Control (RBAC), you can authenticate requests and authorize access to your storage accounts with fine-grained control.

* **Data in Transit:**\
  Data is protected during transfer through HTTPS, client-side encryption, and protocols such as SMB 3.0. Additionally, Azure Disk Encryption secures the operating system and data disks in both Linux and Windows virtual machines.

* **Shared Access Signatures (SAS):**\
  SAS tokens provide granular control by defining which operations can be performed on your storage account, enhancing overall security and access management.

<Frame>
  ![The image illustrates "Storage Security Capabilities" with icons and labels for encryption, authentication, data in transit, disk encryption, and shared access signature.](https://kodekloud.com/kk-media/image/upload/v1752884392/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Securing-storage-endpoints/storage-security-capabilities-icons.jpg)
</Frame>

## In-Depth Topics Covered

This article will delve into the following areas to help you understand and implement these security features effectively:

* Storage Service Encryption (SSE)
* Azure Disk Encryption
* Configuring networking rules for secure access
* Integrating virtual networks and private endpoints

By the end of this guide, you will be well-equipped to secure the endpoints of your storage accounts, ensuring your data remains protected and accessible only to authorized networks and users.

For further details on securing your Azure resources, consider exploring the following helpful resources:

* [Azure Storage Documentation](https://docs.microsoft.com/en-us/azure/storage/)
* [Networking in Azure](https://docs.microsoft.com/en-us/azure/virtual-network/)
* [Azure Security Best Practices](https://docs.microsoft.com/en-us/azure/security/fundamentals/)

Implement these best practices to strengthen the security posture of your Azure storage accounts and safeguard your critical data.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/4468a3ee-4be1-427e-9774-0654b86bd6f5" />
</CardGroup>

---


## Lesson 10: Storage Service Encryption SSE and Azure Disk Encryption ADE

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Storage-Service-Encryption-SSE-and-Azure-Disk-Encryption-ADE/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Storage-Service-Encryption-SSE-and-Azure-Disk-Encryption-ADE/page.md)

**Summary:** This article explains Azures encryption solutions, Storage Service Encryption and Azure Disk Encryption, for securing data at rest while ensuring compliance and performance.

# Storage Service Encryption SSE and Azure Disk Encryption ADE

> This article explains Azures encryption solutions, Storage Service Encryption and Azure Disk Encryption, for securing data at rest while ensuring compliance and performance.

This article explains two essential encryption solutions available in Azure that help secure your data at rest while ensuring compliance and performance: Storage Service Encryption (SSE) and Azure Disk Encryption (ADE).

Both encryption methods provide robust security measures, using industry-standard 256-bit AES encryption, with automatic encryption and decryption processes managed by Azure services. They also support customer control over encryption keys to meet specific regulatory and security requirements.

## Storage Service Encryption (SSE)

Storage Service Encryption (SSE), also known as Server Side Encryption, automatically encrypts data as it is stored in Azure. This built-in service applies to Azure Disk, Blob, File, Queue, and Table services, ensuring that data is encrypted at rest and transparently decrypted when accessed.

### Key Benefits of SSE

* **Protection:** All data stored in Azure is encrypted by default, ensuring that data at rest remains secure.
* **Compliance:** Organizations can meet strict security and regulatory requirements without developing custom encryption solutions.
* **Robust Security:** SSE employs 256-bit AES encryption along with automatic key and data management by the Storage Service.

<Frame>
  ![The image is about Storage Service Encryption (SSE) and includes icons for protection, compliance, and strong cipher, alongside a description of encryption options and settings for Azure Storage.](https://kodekloud.com/kk-media/image/upload/v1752884398/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-Service-Encryption-SSE-and-Azure-Disk-Encryption-ADE/storage-service-encryption-azure.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  By default, SSE is enabled on all storage accounts, and this setting cannot be disabled, ensuring consistent data protection.
</Callout>

### Bring Your Own Keys (BYOK)

If you require full control over your encryption keys and their rotation, Azure supports the Bring Your Own Keys (BYOK) model. Simply create an Azure Key Vault to securely store your keys, and then configure your Storage Service to use these Customer Managed Keys for both encryption and decryption.

## Azure Disk Encryption (ADE)

Azure Disk Encryption (ADE) secures the disks of your virtual machines (VMs) by encrypting both operating system (OS) and data disks. Without ADE, a snapshot VHD could be attached to another VM, potentially exposing sensitive information. ADE mitigates this risk by ensuring the disk is encrypted.

### Key Features of ADE

* **Comprehensive Coverage:** ADE encrypts both OS and data disks for Windows and Linux VMs.
* **Encryption Mechanisms:** Utilizes BitLocker for Windows and dm-crypt for Linux.
* **Key Management:** Encryption keys are securely stored in Azure Key Vault.
* **Access Control:** Only the VM owner can access the encrypted data. If a VHD is downloaded and attached elsewhere without the corresponding keys, the data remains inaccessible.
* **Backup Security:** When using Azure Backup, encryption keys are backed up in the Recovery Services Vault, ensuring that all backups are also encrypted.
* **Encryption Standard:** Implements robust 256-bit encryption.

<Frame>
  ![The image is about Azure Disk Encryption (ADE) and includes icons for encrypting disks, restricting access, encrypted backup, and considerations, alongside a screenshot of disk settings options.](https://kodekloud.com/kk-media/image/upload/v1752884400/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-Service-Encryption-SSE-and-Azure-Disk-Encryption-ADE/azure-disk-encryption-icons-settings.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  Encrypting both OS and data disks may cause a slight performance impact due to the encryption and decryption overhead. In CPU-intensive scenarios, consider encrypting only the data disk to optimize performance. Also, note that if "Encryption at Host" is enabled, ADE cannot be used because host-level encryption relies solely on platform-managed keys.
</Callout>

Additionally, Azure offers an "Encryption at Host" option. For further information on this feature, refer to [Microsoft Azure Security Technologies (AZ-500)](https://learn.kodekloud.com/user/courses/microsoft-azure-security-technologies-az-500).

## Configuring Encryption in the Azure Portal

Azure provides a straightforward interface for configuring both SSE and ADE. Follow the steps below to set up encryption:

### Configuring SSE for Storage Accounts

1. Navigate to your Storage Account in the Azure Portal.
2. Select the "Encryption" option to view the current encryption model.
3. By default, Microsoft Managed Keys are used. If you prefer to use Customer Managed Keys for Blobs and Files, select your Azure Key Vault and assign the keys accordingly.

### Enabling ADE on Virtual Machines

1. Open your Virtual Machine settings in the Azure Portal.
2. Navigate to Disk > Additional Settings.
3. Enable Azure Disk Encryption (ADE) and choose whether to encrypt the OS disk, data disk, or both.
4. Note that updating the Azure Active Directory (AAD) configuration for your VM requires a reboot.
5. If you wish to enable "Encryption at Host," ensure the VM is properly shut down during configuration.

<Frame>
  ![The image shows a Microsoft Azure portal page focused on encryption settings for a storage account. It includes options for encryption selection, key selection, and identity type configuration.](https://kodekloud.com/kk-media/image/upload/v1752884401/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-Service-Encryption-SSE-and-Azure-Disk-Encryption-ADE/azure-portal-encryption-settings.jpg)
</Frame>

<Frame>
  ![The image shows the "Disk settings" page in the Microsoft Azure portal, where options for ultra disk compatibility and encryption settings are displayed. The page includes toggles for enabling ultra disk and host encryption, as well as a dropdown for selecting disks to encrypt.](https://kodekloud.com/kk-media/image/upload/v1752884402/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-Service-Encryption-SSE-and-Azure-Disk-Encryption-ADE/azure-disk-settings-ultra-encryption.jpg)
</Frame>

## Next Topic: Storage Security and Authorization

This concludes our detailed overview of Storage Service Encryption (SSE) and Azure Disk Encryption (ADE). In the next section, we will explore Storage Security and Authorization. For more Azure security best practices, check out the [Azure Security Documentation](https://learn.microsoft.com/en-us/azure/security/).

Enhance your data protection strategy by implementing these encryption services to meet your organization's compliance and security goals.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/cedc440c-b261-4ca3-8688-a966bab7acde" />
</CardGroup>

---


## Lesson 11: Configuring storage access

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Configuring-storage-access/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Configuring-storage-access/page.md)

**Summary:** This guide explains methods for granting secure and efficient access to Azure Storage accounts, including account keys, SAS, Microsoft Entra ID, and anonymous access.

# Configuring storage access

> This guide explains methods for granting secure and efficient access to Azure Storage accounts, including account keys, SAS, Microsoft Entra ID, and anonymous access.

Ensuring secure and efficient access to Azure Storage is essential for protecting your data while maintaining smooth operations. This guide walks you through several methods available for granting access to your Azure Storage account, each suited to different security and operational needs.

## Methods for Granting Access

### Storage Account Keys

Storage account keys are the primary login credentials for Azure Storage services. Acting as root-level passwords, these keys grant complete access to all services and data in the storage account. To enhance security and facilitate maintenance, Azure provides two keys per storage account, allowing for seamless key rotation without disrupting service availability.

### Shared Access Signature (SAS)

A Shared Access Signature (SAS) offers a secure and controlled way to delegate access to specific resources within your storage account. With SAS, you can:

* **Set precise permissions:** Limit what operations can be performed.
* **Define expiration times:** Ensure that access is granted only for a limited period.
* **Restrict access by IP:** Specify allowed IP addresses to further safeguard your resources.

This granularity helps ensure that third-party applications or external users have only the access they need, reducing the risk of unintended data exposure.

### Microsoft Entra ID (Azure AD)

Leveraging Microsoft Entra ID (formerly known as Azure AD) for storage access adds a robust layer of identity-based security. Key benefits include:

* **Seamless Role-Based Access Control (RBAC):** Assign and manage user permissions efficiently.
* **Multi-factor authentication support:** Enhance security by requiring additional verification steps.
* **Simplified user management:** Integrate with your existing Azure identity services for centralized control.

This method is especially well-suited for enterprise environments that demand high standards of security and compliance.

### Anonymous Access

Anonymous access permits unauthenticated users to retrieve data from your storage account. While this can be useful for sharing publicly accessible data, it comes with significant security risks.

<Callout icon="triangle-alert" color="#FF6B6B">
  Enabling anonymous access may expose your data to the entire internet. Use this option only if your data is intended for public distribution, and always evaluate the potential impacts on your security posture.
</Callout>

## Summary

In forthcoming lessons, we will delve into each of these access methods in greater detail. You can expect step-by-step guides on how to:

* Configure and manage storage account keys.
* Set up and secure Shared Access Signatures.
* Integrate Microsoft Entra ID for identity-driven access control.
* Implement and manage anonymous access appropriately.

By mastering these configurations, you will enhance the security, efficiency, and compliance of your Azure Storage deployments while aligning with industry best practices.

For additional resources, consider exploring:

* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/e4e717f3-ead0-4de0-a5d9-9412aa7b2e23" />
</CardGroup>

---


## Lesson 12: Storage Account Access Keys

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Storage-Account-Access-Keys/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Storage-Account-Access-Keys/page.md)

**Summary:** This article explains the importance of Azure storage account access keys for security and access management, including best practices for handling and rotating them.

# Storage Account Access Keys

> This article explains the importance of Azure storage account access keys for security and access management, including best practices for handling and rotating them.

Storage account keys are fundamental to Azure security and access management. They authenticate applications and services that access storage resources such as blobs, queues, tables, and files.

<Callout icon="triangle-alert" color="#FF6B6B">
  These keys operate as a master password for your storage account. Unauthorized access to these keys can result in complete control over your data, including reading, writing, and deletion across all associated services. Handle them with the utmost care.
</Callout>

Azure issues two keys per storage account to ensure redundancy and facilitate seamless key rotation. This approach helps maintain continuous service operation while you update the keys. Always share these keys only with trusted and authorized parties.

<Frame>
  ![The image shows information about storage account keys, including two keys with their connection strings and a reminder to be cautious with the account key.](https://kodekloud.com/kk-media/image/upload/v1752884397/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Storage-Account-Access-Keys/storage-account-keys-connection-strings.jpg)
</Frame>

Regular key rotation is a best practice that minimizes security risks. Azure allows you to regenerate these keys without incurring any downtime, thereby preserving uninterrupted access to your services.

<Callout icon="lightbulb" color="#1CB2FE">
  For enhanced security, consider using [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/) to manage and rotate your keys. Additionally, employ Shared Access Signatures (SAS) to provide fine-grained, time-restricted access to specific resources, reducing the risk associated with exposing full storage account keys.
</Callout>

Protecting your storage account keys is vital for securing your Azure data. Next, we will explore Shared Access Signatures, a more secure approach to managing resource access in your Azure environment.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/ad3c5936-9ef7-487a-a70f-12b19c30e463" />
</CardGroup>

---


## Lesson 13: Shared Access Signatures

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Shared-Access-Signatures/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Shared-Access-Signatures/page.md)

**Summary:** Explains Azure Storage Shared Access Signatures for granting time-limited, fine-grained access to blobs, files, queues, and tables, including types, token structure, generation, and security best practices.

# Shared Access Signatures

> Explains Azure Storage Shared Access Signatures for granting time-limited, fine-grained access to blobs, files, queues, and tables, including types, token structure, generation, and security best practices.

Shared Access Signature (SAS) is a secure, time-limited mechanism in Azure Storage that lets you grant granular access to storage resources—blobs, files, queues, and tables—without sharing your account keys. SAS tokens encode permissions, resource scope, time windows, IP restrictions, and protocol constraints in a URL query string so clients can access storage resources directly while you retain control.

Key benefits:

* Fine-grained access control (read, write, delete, list, etc.).
* Time-limited access to reduce risk.
* Option to delegate via Azure AD (user-delegated SAS) to avoid using account keys.

Types of SAS

| SAS Type           | Scope                                                                      | Best use case                                                                                                           |
| ------------------ | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Service SAS        | Access to a specific resource in a service (e.g., a blob or container)     | Grant access to a particular blob or container for clients or apps.                                                     |
| Account SAS        | Access across services within a storage account (blob, file, queue, table) | Allow cross-service operations (e.g., read from blob and write to queue) across the same storage account.               |
| User-delegated SAS | Delegated via Microsoft Entra ID (Azure AD) using a user delegation key    | Use Azure AD identities to issue SAS without relying on account keys; better for enterprise scenarios and key rotation. |

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Shared-Access-Signatures/shared-access-signature-sas-configuration-slide.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=f6da0b000c6f2a1c3c3bc26b3b8610e7" alt="A presentation slide titled &#x22;Shared Access Signature&#x22; showing two colorful boxes labeled &#x22;Fine-tuned access&#x22; and &#x22;Three types of SAS keys&#x22; on the left, and a detailed SAS configuration panel with checkboxes for services, permissions, start/end times, IPs and protocols on the right. The slide also includes a small copyright note &#x22;KodeKloud&#x22; and a decorative &#x22;S&#x22; logo." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Shared-Access-Signatures/shared-access-signature-sas-configuration-slide.jpg" />
</Frame>

SAS structure and signing

<Callout icon="lightbulb" color="#1CB2FE">
  A SAS URL has two parts: the resource endpoint (the storage resource to access) and the SAS token (query string describing permissions, allowed times, IPs, protocols, and the cryptographic signature). The signature is generated by signing the token with an account key (service/account SAS) or a user delegation key obtained after authenticating with Azure AD (user-delegated SAS).
</Callout>

Understanding a SAS URL

* Resource endpoint — the base URL of the target resource, for example:

```text theme={null}
https://kodekloud.blob.core.windows.net
```

* SAS token — query parameters specifying permissions, scope, duration, and signature. Common parameters include:

| Parameter | Meaning                                                                                  | Example / Notes                            |
| --------- | ---------------------------------------------------------------------------------------- | ------------------------------------------ |
| sv        | Storage service version                                                                  | `2022-11-02`                               |
| ss        | Services the SAS applies to (b = blob, f = file, t = table, q = queue)                   | `ss=b`                                     |
| srt       | Resource types (s = service, c = container, o = object)                                  | `srt=sco`                                  |
| sp        | Permissions (r = read, w = write, d = delete, l = list, a = add, c = create, u = update) | `sp=r`                                     |
| st        | Start time (UTC)                                                                         | `st=2023-12-10T15:14:50Z`                  |
| se        | Expiry time (UTC)                                                                        | `se=2023-12-10T23:14:50Z`                  |
| sip       | Allowed client IP or range                                                               | `sip=203.0.113.5-203.0.113.10`             |
| spr       | Allowed protocols (https or https,http)                                                  | `spr=https` (use HTTPS-only when possible) |
| sig       | HMAC signature computed using the signing key                                            | `sig=...`                                  |

Example SAS token (appended to a resource URL):

```text theme={null}
?sv=2022-11-02&ss=b&srt=sco&sp=r&st=2023-12-10T15:14:50Z&se=2023-12-10T23:14:50Z&spr=https&sig=P3kV00LVZA66w%2FjwiKVrUDe8X%2BBZQjCAyfpUPf1axZe0%3D
```

Full SAS URL (resource endpoint + SAS token):

```text theme={null}
https://<your-storage-account>.blob.core.windows.net/images/City1.jpg?sv=2022-11-02&ss=b&srt=sco&sp=r&st=2023-12-10T15:14:50Z&se=2023-12-10T23:14:50Z&spr=https&sig=...
```

If the SAS token is modified or expired, access will be denied.

Walkthrough — Generate a SAS in the Azure portal

1. Change container access level
   * To avoid public exposure, set the container to Private and use SAS for controlled access. In the Azure portal you can also allow anonymous public access (Blob or Container) if that is explicitly required.

<Frame>
  <img src="https://mintcdn.com/kodekloud-c4ac6d9a/qTPiNmqXKGQjbUh5/images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Shared-Access-Signatures/azure-storage-container-images-access-changed.jpg?fit=max&auto=format&n=qTPiNmqXKGQjbUh5&q=85&s=e4c41735f2c3177f2fa527e70d50a12e" alt="A screenshot of the Microsoft Azure portal showing a storage container named &#x22;images&#x22; with a list of image blobs (City1.jpg, City2.jpg, Colour1.jpg, etc.), sizes, access tiers and other metadata. A notification toast at the top-right says the access level for the container was successfully changed." width="1920" height="1080" data-path="images/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Shared-Access-Signatures/azure-storage-container-images-access-changed.jpg" />
</Frame>

2. Generate a SAS token from the storage account
   * In the Azure portal: Storage account -> Security + networking -> Shared access signature.
   * Select services (e.g., Blob), resource types (service/container/object), and permissions (Read, Write, etc.).
   * Configure start and expiry times, optional allowed IP ranges, and allowed protocols (HTTPS recommended).
   * Choose the signing key (Key1 or Key2) to sign the SAS token. The portal will display the generated SAS token and the full URL(s) for access.
   * For improved security and key-rotation resilience, prefer user-delegated SAS with Azure AD when possible.

3. Use the SAS URL
   * Append the SAS token to the blob or container URL and access it from a browser or client. The SAS enforces exactly the permissions and constraints you specified.

Operational considerations

* Key rotation impact: If you regenerate an account access key (Key1 or Key2), any SAS tokens that were signed with that key become invalid.

<Callout icon="warning" color="#FF6B6B">
  Regenerating an account key will invalidate SAS tokens signed with that key. User-delegated SAS tokens (issued via Azure AD) are not affected by account key regeneration. Plan key rotation carefully to avoid service interruptions.
</Callout>

* Security best practices:
  * Use the least privilege: grant only the necessary permissions and the shortest practical time window.
  * Restrict allowed IP ranges when possible.
  * Use HTTPS-only (spr=https) to protect tokens in transit.
  * Prefer user-delegated SAS (Azure AD) for enterprise scenarios and better lifecycle management.
  * Monitor and log SAS usage using Azure Storage analytics and diagnostic logs.

Summary

* Azure SAS provides flexible, time-bound access to storage without exposing account keys.
* Choose the SAS type that fits your scenario: Service SAS for resource-level access, Account SAS for cross-service scenarios, or User-delegated SAS for Azure AD-based delegation.
* Configure permissions, duration, IP ranges, and protocols carefully to minimize risk.
* Remember: regenerating account keys invalidates SAS tokens signed by those keys; user-delegated SAS follows Azure AD lifecycle rules.

Further reading

* [Azure Storage SAS overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
* [Azure Storage account keys and rotation](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)
* [Azure Active Directory overview](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/876265bd-d9af-4b59-95f3-2452b27662a8" />
</CardGroup>

---


## Lesson 14: Microsoft Entra ID Authentication

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Microsoft-Entra-ID-Authentication/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Storage/Microsoft-Entra-ID-Authentication/page.md)

**Summary:** Microsoft Entra ID Authentication provides secure access to Azure Storage resources, enhancing security with multi-factor authentication and conditional access policies.

# Microsoft Entra ID Authentication

> Microsoft Entra ID Authentication provides secure access to Azure Storage resources, enhancing security with multi-factor authentication and conditional access policies.

Microsoft Entra ID Authentication (formerly Azure AD Authentication) offers a secure and modern method to access Azure Storage resources—such as blobs, queues, and tables—while avoiding the risks associated with SAS tokens. Unlike SAS tokens, which may inadvertently expose your storage account through logs or application history, Entra ID brings built-in multi-factor authentication and conditional access policies. These advanced features allow you to restrict access based on corporate network conditions or geographic regions. Even if you hold owner or contributor permissions at the subscription level, you still require storage-specific RBAC (Role-Based Access Control) assignments to access storage resources.

<Callout icon="lightbulb" color="#1CB2FE">
  For enhanced security, always prefer Entra ID Authentication over SAS tokens to protect your storage account. Integrated features such as multi-factor authentication and conditional access provide an additional layer of security.
</Callout>

In the following sections, we detail the authentication and authorization workflow using Microsoft Entra ID and demonstrate the process in the Azure Portal via a service principal setup.

***

## Authentication and Authorization Workflow

Consider a scenario where you have the "Storage Blob Data Contributor" role and need to access a storage account. The process involves three key steps:

1. **Authentication:**\
   The process begins with submitting a login request to Microsoft Entra ID using your credentials (username and password). After successful authentication—potentially including multi-factor verification—Microsoft Entra ID returns an HTTP 200 status with a bearer token.

2. **Authorization:**\
   This bearer token is then used to authenticate your subsequent request to the Azure Storage API. Access is verified against your assigned RBAC role (e.g., Storage Blob Data Contributor), ensuring that only authorized operations are allowed.

3. **Data Access:**\
   On successful authorization, the storage service processes your request and returns the requested data.

<Frame>
  ![The image illustrates Microsoft Entra ID Authentication, highlighting a secure authentication process that requires dedicated RBAC roles. It includes a flow diagram showing interactions between a user, authentication service, and storage blob container using bearer tokens.](https://kodekloud.com/kk-media/image/upload/v1752884383/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Microsoft-Entra-ID-Authentication/microsoft-entra-id-authentication-diagram.jpg)
</Frame>

***

## Setting Up a Service Principal for Storage Access in Azure Portal

This section explains how to set up a service principal (an app registration in Microsoft Entra ID) to access an Azure Storage account without using a personal user account.

1. **Create the Service Principal:**

   * Log in to the Azure Portal and navigate to **Azure AD (Microsoft Entra ID)**.
   * Open **App registrations** and create a new registration (for instance, "storage-spn") for a single tenant.
   * After the app is created, copy the **Client ID** from the overview page.
   * Move to the **Certificates & secrets** section, generate a new client secret, and save its value for later use.
   * Also, note the **Tenant ID** found on the Azure AD overview page.

<Frame>
  ![The image shows a Microsoft Azure portal page for managing "Certificates & secrets" under an app registration named "storage-spn." It displays details of a client secret, including its description, expiration date, and value.](https://kodekloud.com/kk-media/image/upload/v1752884384/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Microsoft-Entra-ID-Authentication/azure-portal-certificates-secrets-storage-spn.jpg)
</Frame>

* Additionally, copy the endpoint for V1 if required.

2. **Assign RBAC Roles on the Storage Account:**

   * Navigate to the desired Storage Account.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of an app registration named "storage-spn," including its application ID, object ID, and various OAuth and API endpoints.](https://kodekloud.com/kk-media/image/upload/v1752884385/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Microsoft-Entra-ID-Authentication/azure-portal-storage-spn-details.jpg)
</Frame>

* Under the **Access Control (IAM)** section, add a role assignment.
* For example, assign the built-in **Storage Blob Data Reader** role to grant read-only access to blob data.
* Click **Next**, select **Members**, and search for the registered service principal named "storage-spn" to complete the role assignment.

<Frame>
  ![The image shows a Microsoft Azure portal interface for adding a role assignment, specifically for managing access to Azure Storage Blob Data with various built-in roles listed.](https://kodekloud.com/kk-media/image/upload/v1752884386/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Microsoft-Entra-ID-Authentication/azure-portal-role-assignment-storage.jpg)
</Frame>

<Frame>
  ![The image shows a Microsoft Azure portal interface for adding a role assignment, specifically for the "Storage Blob Data Reader" role. A sidebar is open for selecting members, displaying a list of potential users to assign the role to.](https://kodekloud.com/kk-media/image/upload/v1752884387/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Microsoft-Entra-ID-Authentication/azure-portal-role-assignment-storage-blob-reader.jpg)
</Frame>

***

## Generating an Access Token Using Postman

After configuring the service principal with the appropriate RBAC role, you can generate an access token to communicate with the Storage API via Postman.

1. **Token Request Setup:**

   * In Postman, initiate a POST request to the Azure AD token endpoint.

   * Set the following form data parameters:
     * **client\_id:** Paste the Client ID obtained from your app registration.
     * **client\_secret:** Paste the generated client secret.
     * **grant\_type:** Use `client_credentials` to indicate the type of authentication.
     * **resource:** Set this parameter to `https://storage.azure.com`.

   * Send the request; a successful call returns a JSON response similar to the following:

   ```json theme={null}
   {
     "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImYzYTA4MjJjZWVkZTc5Y2ExOWM3ZTA5MjcyYTY2MGE2MTA1YzBiYTciLCJ4NXAiOiJhbGciOiJSUzI1NiIsImtpZCI6ImYzYTA4MjJjZWVkZTc5Y2ExOWM3ZTA5MjcyYTY2MGE2MTA1YzBiYTci... (truncated for brevity)"
   }
   ```

2. **Accessing Storage Resources:**

   * Use the generated access token in subsequent requests to the storage API.

   * Paste the storage endpoint URL in Postman.

   * If you send the request without setting an authentication header, you will receive a "ResourceNotFound" response.

   * To resolve this, add the following headers:
     * **X-MS-Version:** Set to `2017-11-09` to specify the storage service version.
     * **Authorization:** Use the format `Bearer <your_access_token>` to include your token.

   * After adding these headers, resend the request. If the token is valid and RBAC permissions are correct, the storage service will return the file data.

Below is an example of an XML error response encountered when authentication is not properly applied:

```xml theme={null}
<?xml version="1.0" encoding="utf-8"?>
<Error>
    <Code>ResourceNotFound</Code>
    <Message>The specified resource does not exist.</Message>
    <RequestId>e9c936c6-9780-4b66-716c-fa1920098900</RequestId>
    <Time>2023-10-09T14:09:23.6599575Z</Time>
</Error>
```

Once the authentication headers are correctly set, Azure AD validates the token and the storage resource is successfully retrieved. Keep in mind that when the token expires, you must repeat the process to obtain a new token.

<Frame>
  ![The image shows a Postman interface with a POST request to an Azure AD token endpoint, displaying form data parameters and a JSON response containing an access token.](https://kodekloud.com/kk-media/image/upload/v1752884389/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Microsoft-Entra-ID-Authentication/postman-azure-ad-token-request.jpg)
</Frame>

***

## Conclusion

By integrating Microsoft Entra ID Authentication with Azure RBAC, you achieve robust security for accessing Azure Storage. This method ensures that access is granted only through verified identity and precise role-based permissions, whether accessed via a user account or service principal. These practices form a strong foundation for secure and scalable Azure administration.

For further details on Azure administration and identity management, explore additional resources on [Azure Documentation](https://docs.microsoft.com/azure) and [Microsoft Entra](https://docs.microsoft.com/azure/active-directory/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/48d08f66-feb9-4bae-83b0-2e6aa34e24ae/lesson/d8b58f6f-2018-4125-94c3-9ceaa343755a" />
</CardGroup>

---


# Section 09: Administer Azure Virtual Machines

---


## Lesson 1: Module Introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Module-Introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Module-Introduction/page.md)

**Summary:** This module covers best practices for deploying Azure Virtual Machines, including configuration, scalability, and resource management.

# Module Introduction

> This module covers best practices for deploying Azure Virtual Machines, including configuration, scalability, and resource management.

Welcome back! In this module, we begin our journey into administering Azure Virtual Machines. Our focus is on configuring these resources efficiently and ensuring their high availability in the Azure environment.

<Callout icon="lightbulb" color="#1CB2FE">
  This module covers best practices for deploying Azure Virtual Machines, including configuration, scalability, and resource management.
</Callout>

Let's kick off this lesson by planning our virtual machine deployments to optimize performance, security, and scalability.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/34d9af06-fc33-4556-a3f2-2e7a5c5db484/lesson/4b55cdd6-2d2f-4605-956e-8b1525b401bc" />
</CardGroup>

---


## Lesson 2: Planning VMs

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Planning-VMs/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Planning-VMs/page.md)

**Summary:** This article discusses planning considerations for deploying virtual machines in Azure, focusing on responsibilities, networking, naming conventions, VM size, performance, and pricing models.

# Planning VMs

> This article discusses planning considerations for deploying virtual machines in Azure, focusing on responsibilities, networking, naming conventions, VM size, performance, and pricing models.

When planning virtual machines (VMs) in Azure, it's critical to understand the shared responsibility model in cloud computing. This model delineates the roles and obligations between the cloud service provider and the customer based on the service model—whether Infrastructure as a Service (IaaS), Platform as a Service (PaaS), or Software as a Service (SaaS).

In an IaaS scenario such as Azure VMs, the cloud provider (e.g., Microsoft) ensures the physical security of the data center, physical network, host, and virtualization layer. Meanwhile, the customer is responsible for managing the operating system, network configuration, access controls, and the data and applications running on the VM. As you shift toward PaaS or SaaS, additional responsibilities, such as handling runtime, middleware, or even parts of the operating system, transfer to the cloud provider. However, the customer always retains full responsibility for their data—ensuring proper data classification, accountability, and protection.

<Callout icon="lightbulb" color="#1CB2FE">
  Understanding these distinctions is essential for effective security, compliance, and management practices within your cloud environment.
</Callout>

***

## Virtual Machine Planning Considerations

When preparing to deploy VMs in Azure, several key factors need to be considered to optimize performance, efficiency, and cost. Below are the critical aspects you must address:

### 1. Networking

Design your network address space meticulously to support both current operations and future growth:

* Define appropriate IP address ranges for your virtual network and subnets.
* Account for the total number of VMs, as this influences your network layout.
* Ensure the allocated address space does not conflict with other networks, such as your on-premises infrastructure.

### 2. Naming Conventions

A clearly defined naming convention simplifies management and enhances compliance:

* Include identifiers like the environment (e.g., dev, test, prod).
* Add role designations (e.g., web, dv, middleware) to distinguish between services.
* For multi-region deployments, incorporate region-specific identifiers to clearly differentiate resources.

### 3. VM Size and Regional Availability

Before selecting a VM size, keep these points in mind:

* Verify that the desired VM size is available in your chosen region, as each region supports a distinct set of configurations.
* Consider how regional availability impacts both performance and cost.

### 4. Proximity and Performance

Optimal performance is often achieved by choosing a region close to your user base:

* Leverage Azure's global footprint by selecting regions that minimize latency and maximize user experience.

### 5. Pricing Models

Familiarize yourself with Azure's pricing strategies to optimize your budget:

* Evaluate the pay-as-you-go model for flexible, short-term needs.
* Consider reserved instances for longer-term deployments to benefit from cost savings.
* Factor in potential advantages from existing on-premises Windows Server or SQL Server licenses when migrating to Azure.
* Explore advanced cost-management strategies to further optimize expenses.

<Callout icon="lightbulb" color="#1CB2FE">
  Balancing performance, availability, and cost is crucial when deploying virtual machines in Azure. Integrating these planning considerations will contribute to a robust and scalable cloud strategy.
</Callout>

On that note, let's take a closer look at the VM sizes available in Azure.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/34d9af06-fc33-4556-a3f2-2e7a5c5db484/lesson/441f90ea-2cf7-43f0-8928-364f8d78b8c1" />
</CardGroup>

---


## Lesson 3: Managing VM sizes

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Managing-VM-sizes/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Managing-VM-sizes/page.md)

**Summary:** This guide provides an overview of Azure VM families and their typical use cases for optimal performance and cost efficiency.

# Managing VM sizes

> This guide provides an overview of Azure VM families and their typical use cases for optimal performance and cost efficiency.

Selecting the appropriate Azure Virtual Machine (VM) size is essential for achieving optimal performance and cost efficiency. Azure categorizes VMs into several families, each specifically designed to address various workload requirements. This guide provides a detailed overview of the Azure VM families and highlights their typical use cases.

## General Purpose

General purpose VMs feature a balanced CPU-to-memory ratio, making them ideal for diverse workloads such as development environments, small databases, and general-purpose applications. They offer an excellent blend of performance and cost efficiency without the need for over-provisioning resources.

## Compute Optimized

For highly compute-intensive tasks, compute optimized VMs deliver a higher CPU-to-memory ratio. These are best suited for application servers, batch processing, and workloads where rapid computation is crucial.

## Memory Optimized

Memory optimized VMs cater to scenarios where enhanced memory capacity is required. They provide substantial memory allocation, making them perfect for large databases, in-memory data processing, and other memory-intensive applications.

## Storage Optimized

Storage optimized VMs are engineered to handle significant amounts of data with high disk throughput and I/O performance. They are an excellent choice for big data applications and SQL databases, where disk performance is a key performance driver.

## GPU VMs

GPU VMs are designed to power graphics-intensive operations and artificial intelligence workloads. Their robust GPU capabilities make them ideal for rendering tasks, deep learning, and other processes that benefit from accelerated graphics processing.

## High Performance Compute (HPC)

High performance compute VMs offer robust CPU performance along with optional high-throughput network interfaces. They are best utilized for extremely demanding compute tasks that require top-tier processing power and network efficiency.

## Confidential Compute

Confidential compute VMs are built with enhanced security in mind. They ensure that sensitive data remains protected during processing, making them especially suitable for workloads involving confidential or regulated information.

<Callout icon="lightbulb" color="#1CB2FE">
  Azure continually expands its VM portfolio with new sizes and configurations to leverage the latest technological advancements. Stay current by regularly reviewing the [Azure Documentation](https://docs.microsoft.com/azure/).
</Callout>

Selecting the right VM size goes beyond merely matching hardware specifications:

<Frame>
  ![The image is a table detailing virtual machine sizing, including types, sizes, and targeted workloads for storage optimization, GPU, HPC, and confidential computing.](https://kodekloud.com/kk-media/image/upload/v1752884458/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Managing-VM-sizes/virtual-machine-sizing-table.jpg)
</Frame>

It also involves ensuring that the chosen VM aligns with your application's unique demands and scaling requirements.

## Virtual Machine Storage

Managing virtual machine storage in Azure is equally crucial. The following sections will address key considerations and strategies to optimize storage performance and maintain data reliability in your VM deployments.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/34d9af06-fc33-4556-a3f2-2e7a5c5db484/lesson/233f2920-86f1-41e7-bd3d-ca718be28f11" />
</CardGroup>

---


## Lesson 4: Virtual Machine Storage

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Virtual-Machine-Storage/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Virtual-Machine-Storage/page.md)

**Summary:** This article explains the storage options for virtual machines in Azure, including OS disks, temporary disks, data disks, and the differences between managed and unmanaged disks.

# Virtual Machine Storage

> This article explains the storage options for virtual machines in Azure, including OS disks, temporary disks, data disks, and the differences between managed and unmanaged disks.

Understanding how storage works for virtual machines in Azure is crucial for deploying robust and efficient cloud resources. Each Azure virtual machine (VM) is equipped with different types of storage disks designed to serve specific purposes.

## OS Disk

The OS disk acts as the primary storage device where the operating system resides. This disk is a Virtual Hard Disk (VHD) stored in Azure Blob Storage, ensuring both persistence and durability of your OS.

## Temporary Disk

The temporary disk is located on the host machine and provides storage for ephemeral data, such as swap or page files.

<Callout icon="lightbulb" color="#1CB2FE">
  Data stored on the temporary disk may be lost during maintenance events or when the VM is redeployed, so use it only for data that does not require persistence.
</Callout>

## Data Disks

Data disks offer persistent storage for your applications and their data. The number of data disks you can attach depends on the VM size and family. For example, one VM family might support up to two data disks, while another may allow three. Choose a VM size that meets your application's storage needs.

## Performance Tiers

Selecting the right disk performance tier is essential to align with your application's workload requirements. Consider the following options:

* **Standard HDDs**: Suitable for basic workloads with moderate performance needs.
* **Standard SSDs**: Ideal for applications requiring better performance than HDDs.
* **Premium SSDs**: Recommended for I/O-intensive tasks that need high throughput and low latency.

When selecting a tier, evaluate factors such as Input/Output Operations Per Second (IOPS) and cost to determine the best fit for your environment.

## Managed vs. Unmanaged Disks

Azure offers two primary methods for managing your VM disks: managed and unmanaged.

### Managed Disks

Managed disks provide a simplified storage solution by abstracting the complexities of storage account management. Azure takes care of disk provisioning and storage account scalability, which helps avoid concerns about IOPS limits. Managed disks offer several built-in features, including:

* Snapshots and backups
* Site recovery support
* Integration with Azure availability sets to eliminate single points of failure

They are available in both standard and premium options, supporting both SSDs and HDDs.

### Unmanaged Disks

With unmanaged disks, you are responsible for creating and managing the storage accounts that hold your disks. This approach gives you more control but also requires you to manually handle scalability and monitor IOPS limits. Unmanaged disks store page blobs in storage accounts that you manage. Due to the increased management overhead, Microsoft generally recommends using managed disks for most deployments.

## Deploying a Virtual Machine

With a clear understanding of virtual machine storage components—OS disks, temporary disks, and data disks—as well as knowing the differences between managed and unmanaged disks and the importance of choosing the right performance tier, you're ready to deploy your Azure virtual machines.

In the upcoming sections, we will guide you through the process of creating a VM using the Azure portal. We will delve into the key factors to consider during deployment to ensure your configuration meets both performance and cost requirements.

Enjoy learning and deploying your Azure virtual machines, and leverage these insights to build a scalable and resilient infrastructure!

For additional resources, check out the following links:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Azure Virtual Machines Documentation](https://docs.microsoft.com/azure/virtual-machines/)
* [Terraform Registry](https://registry.terraform.io/)

Happy deploying!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/34d9af06-fc33-4556-a3f2-2e7a5c5db484/lesson/f41c1fe0-a757-4826-841b-c44b6ae25b13" />
</CardGroup>

---


## Lesson 5: Creating VMs

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Creating-VMs/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Creating-VMs/page.md)

**Summary:** This guide provides a step-by-step process for deploying virtual machines in Azure using the Portal and command-line tools.

# Creating VMs

> This guide provides a step-by-step process for deploying virtual machines in Azure using the Portal and command-line tools.

Deploying a virtual machine (VM) in Azure involves several steps that are carefully organized into distinct sections for clarity and ease of management. This guide covers the basics of configuring a VM using both the Azure Portal and command-line tools, ensuring you have all the necessary details for effective deployment.

## VM Basics

Before you begin, you need to specify the following details:

* **Subscription Details & Resource Group:** Define which subscription and resource group will host your VM.
* **Region:** Choose the regional data center where your VM will be deployed.
* **VM Name & Image:** Provide a unique name and select a VM image (operating system) to run.
* **Size & Disk Configuration:**
  * The **size** should match your application's performance and scalability requirements.
  * Configure the disk settings to choose between SSDs or HDDs, set the desired disk size, and add additional data disks if necessary.

<Frame>
  ![The image shows a guide for creating a virtual machine using a portal, highlighting the "Basics" section with details like subscription, resource group, and instance details. It includes options for disks, networking, and management settings.](https://kodekloud.com/kk-media/image/upload/v1752884434/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-VMs/virtual-machine-creation-guide-basics.jpg)
</Frame>

## Networking Configuration

Within the networking section, you can:

* Select your virtual network and the specific subnet for the VM.
* Configure associated network security groups (NSG), load balancers, and public IP settings.

This configuration ensures that your VM is both reachable and secure.

## Management Options

The management section offers additional configurations:

* **Monitoring:** Set up monitoring to keep track of your VM’s performance.
* **Diagnostics:** Send diagnostics information to a storage account for analysis.
* **Microsoft Entra ID (Azure AD):** Integrate for streamlined login and identity management.
* **Backup & Auto Shutdown:** Configure backups and scheduled shutdowns to optimize cost control, especially useful during testing.

<Callout icon="lightbulb" color="#1CB2FE">
  For optimal cost management, always review the auto shutdown and backup options when configuring your VM.
</Callout>

## Creating VMs Using Command-Line Tools

You can create a VM using either Azure PowerShell or the Azure CLI. Both methods allow you to configure your resource details from scratch.

### Using Azure PowerShell

Run the following command to create a VM with the necessary resource parameters:

```powershell theme={null}
PS > New-AzVm `
-ResourceGroupName "web-rg" `
-Name "vm-01" `
-Location "East US" `
-VirtualNetworkName "vm-01-vnet" `
-SubnetName "default" `
-SecurityGroupName "vm-01-nsg" `
-PublicIpAddressName "vm-01-pip"
```

### Using Azure CLI

Alternatively, use the Azure CLI with this command:

```bash theme={null}
$ az vm create \
  --name vm-01 \
  --resource-group web-rg \
  --image UbuntuLTS \
  --location EastUS2 \
  --admin-username adminuser \
  --admin-password Pa$$w0rd1234
```

## Deploying a VM via the Azure Portal

Follow these steps to deploy a VM using the Azure Portal:

1. **Navigate and Initiate Creation:**\
   Open the "Virtual Machines" blade, click "Create," and select "Azure Virtual Machine."

2. **Set Up Basics:**
   * In the **Basics** tab, select your subscription and resource group (or create a new one, e.g., "azvm01rg").
   * Enter a VM name (e.g., "azvm01") and choose the region.
     * For availability, select "No infrastructure redundancy required" if applicable.
   * Choose the security type as "Standard VMs" to avoid unnecessary configurations like trusted machines if not needed.

3. **Select the OS Image and Size:**
   * Under the **Image** section, pick your preferred operating system (e.g., Ubuntu 22.04 for a Linux environment).
   * Click "See all sizes" in the **Size** section. Use filters (e.g., general purpose) to choose an appropriate size, such as the B1S for a cost-effective instance.

<Frame>
  ![The image shows a Microsoft Azure portal page for selecting a virtual machine (VM) size, listing various VM options with details like vCPUs, RAM, and cost per hour.](https://kodekloud.com/kk-media/image/upload/v1752884435/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-VMs/azure-portal-vm-size-selection.jpg)
</Frame>

4. **Configure Authentication and Inbound Ports:**
   * Set the administrative credentials, choosing a robust password and username.
   * Under the **Inbound ports** section, select the necessary ports (HTTP, HTTPS, or SSH) based on your requirements.

5. **Disk Configuration:**
   * In the **Disk** tab, choose the disk type (e.g., Standard SSD) and specify the disk size (e.g., 30 GB).
   * Optionally, add more data disks as needed.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a virtual machine, with options for configuring the OS disk and data disks. A notification about a saved password in Microsoft Edge is also visible.](https://kodekloud.com/kk-media/image/upload/v1752884437/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-VMs/azure-portal-virtual-machine-setup.jpg)
</Frame>

6. **Networking Configuration:**
   * Under the **Networking** tab, either select an existing virtual network or create a new one.
   * Configure the public IP and associate a network security group (NSG) appropriately.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a virtual machine, specifically focusing on the networking configuration options. It includes settings for virtual network, subnet, public IP, and network security group.](https://kodekloud.com/kk-media/image/upload/v1752884438/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-VMs/azure-portal-virtual-machine-networking.jpg)
</Frame>

7. **Management Settings:**\
   Configure options including Defender for Cloud, managed identities, Azure AD login, auto shutdown, backup, and monitoring (alerts, diagnostics, and health monitoring).

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a virtual machine, specifically on the "Monitoring" tab, where options for configuring alerts, diagnostics, and health monitoring are available.](https://kodekloud.com/kk-media/image/upload/v1752884440/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-VMs/azure-portal-virtual-machine-monitoring.jpg)
</Frame>

8. **Advanced Configuration:**\
   Use the **Advanced** tab to set up extensions for post-deployment configuration and automation.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a virtual machine, specifically on the "Advanced" tab, where users can configure extensions, VM applications, and custom data.](https://kodekloud.com/kk-media/image/upload/v1752884440/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-VMs/azure-portal-virtual-machine-advanced.jpg)
</Frame>

9. **Finalize and Create:**
   * Optionally, add tags to your VM for better organization.
   * Click "Review + create," then "Create" once validation passes.

After deployment, you can access your VM using a terminal or remote access tool.

<Frame>
  ![The image shows a Microsoft Azure portal page indicating that a deployment of an Ubuntu server virtual machine is complete. It includes deployment details, next steps, and options for cost management and security.](https://kodekloud.com/kk-media/image/upload/v1752884442/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Creating-VMs/azure-portal-ubuntu-vm-deployment.jpg)
</Frame>

## Connecting to Your Deployed VM

Once the VM is running, connect using your preferred remote access method:

* **Linux VMs:** Typically accessed via SSH.
* **Windows VMs:** Access using Remote Desktop Protocol (RDP).

You can use Cloud Shell or a locally installed version of PowerShell/Azure CLI for further management tasks.

<Callout icon="lightbulb" color="#1CB2FE">
  Remember to update your firewall rules or NSG configurations to allow the required inbound connections.
</Callout>

This guide has provided a step-by-step walkthrough for deploying a VM in Azure using both the Portal and command-line tools. With your VM now in place, you can focus on installing applications and configuring additional services as needed.

For further reading and more advanced configurations, visit the [Azure Documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/34d9af06-fc33-4556-a3f2-2e7a5c5db484/lesson/3de0eaa9-8fc7-41b2-a176-6b07346b9e89" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/34d9af06-fc33-4556-a3f2-2e7a5c5db484/lesson/ccf84311-6da6-41c3-a74f-895fc9cbd732" />
</CardGroup>

---


## Lesson 6: Connecting to VMs

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Connecting-to-VMs/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Connecting-to-VMs/page.md)

**Summary:** Learn to connect to virtual machines using public IPs, jumpboxes, and Azure Bastion, covering methods, benefits, and security considerations.

# Connecting to VMs

> Learn to connect to virtual machines using public IPs, jumpboxes, and Azure Bastion, covering methods, benefits, and security considerations.

In this lesson, you'll learn how to connect to the virtual machines (VMs) created in the previous lesson using different methods. We will cover accessing VMs via public IP addresses, jumpboxes, and Azure Bastion. Each method has its own benefits and security considerations.

## Connecting Using Public IP Address and Jumpbox

One common method to access a virtual machine is by using its public IP address. With a public IP, you can:

* Use an SSH client (for Linux)
* Use an RDP client (for Windows)

Another secure option is to connect via a jumpbox. A jumpbox is a machine with a public IP address placed within a dedicated subnet, while your workloads run in a different, private subnet within the same virtual network. By connecting to the jumpbox, you can then access other machines securely on the private network.

<Frame>
  ![The image illustrates a network setup for connecting to virtual machines using a jumpbox within a virtual network, showing connections via private and public IPs. It includes elements like a virtual machine, public IP, and user access.](https://kodekloud.com/kk-media/image/upload/v1752884427/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Connecting-to-VMs/network-setup-jumpbox-virtual-machines.jpg)
</Frame>

## Connecting with Azure Bastion

Azure Bastion is a managed service that simplifies VM connectivity by allowing secure, direct browser-based access to your VMs. This method eliminates the need to deploy and manage jumpbox VMs, download special clients, or expose any ports directly to the internet.

<Callout icon="lightbulb" color="#1CB2FE">
  Azure Bastion enhances security by ensuring that no public ports are exposed, which helps protect your infrastructure from potential attackers.
</Callout>

<Frame>
  ![The image is a diagram illustrating how to connect to virtual machines using Azure Bastion, showing the flow from a bastion host through a virtual network to users.](https://kodekloud.com/kk-media/image/upload/v1752884428/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Connecting-to-VMs/azure-bastion-virtual-machines-diagram.jpg)
</Frame>

## Overview of Connection Methods

Below is an overview of available connection methods based on the operating system, protocol, and authentication:

* **Windows:**
  * **RDP:** Uses TCP port 3389. Authenticate with a password.
  * **WinRM:** Utilizes PowerShell for remote management over TCP port 5986 (requires certificate configuration).

* **Linux:**
  * **SSH:** Utilizes TCP port 22. Supports authentication via passwords or SSH key pairs.

<Frame>
  ![The image is a diagram showing methods for connecting to virtual machines, detailing operating systems, protocols/ports, and authentication methods. It includes Windows and Linux systems with protocols like RDP, WinRM, and SSH, and authentication via passwords, certificates, or keys.](https://kodekloud.com/kk-media/image/upload/v1752884429/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Connecting-to-VMs/vm-connection-methods-diagram.jpg)
</Frame>

## Connecting via SSH

To connect to a Linux VM using its public IP address, open your terminal and run:

```python theme={null}
ssh kodekloud@20.124.250.11
```

When you run the command, you will be prompted to verify the host authenticity and enter the password:

```console theme={null}
The authenticity of host '20.124.250.11 (20.124.250.11)' can't be established.
ED25519 key fingerprint is SHA256:WF3fDk9RW5FBHx6A619YVajH2O27TNQGyGPdCZZU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '20.124.250.11' (ED25519) to the list of known hosts.
kodekloud@20.124.250.11's password:
```

Once authenticated, you are connected to the VM using its public IP address. Alternatively, you can reconnect using the jumpbox that was set up earlier.

Below is a sample output of system information from one of our VMs to confirm connectivity via the jumpbox:

```plaintext theme={null}
System information as of Sun Dec 10 18:11:58 UTC 2023
System load:  0.0                Processes:              100
Usage of /:   1.1% of 28.9GB     Users logged in:        0
Memory usage: 31%                IPv4 address for eth0: 10.0.0.4
Swap usage:   0%

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.
kodeKLOUD@az-vm-01:~$
```

## Deploying VMs for Azure Bastion

Now, let’s explore how to use Azure Bastion. The following PowerShell script creates two VMs—one Linux and one Windows—both with private IP addresses. These VMs are ideal for secure access via Bastion.

```powershell theme={null}
#Create Windows VM
New-AzVm `
    -ResourceGroupName $rg `
    -Name 'win-ra-vm' `
    -Location $region `
    -Image 'MicrosoftWindowsServer:WindowsServer:2022-datacenter-azure-edition:latest' `
    -VirtualNetworkName 'vnet-remoteaccess' `
    -SubnetName 'windows' `
    -SecurityGroupName 'windows-nsg' `
    -Credential $credential

#Create Linux VM
New-AzVm `
    -ResourceGroupName $rg `
    -Name 'linux-ra-vm' `
    -Location $region `
    -Image 'Ubuntu2204' `
    -VirtualNetworkName 'vnet-remoteaccess' `
    -SubnetName 'linux' `
    -SecurityGroupName 'linux-nsg' `
    -Credential $credential `
    -Size $VMSize
```

After the script completes, verify that the VMs appear in the virtual machines list. Since these VMs do not have public IP addresses, they are perfectly suited for private access using Azure Bastion.

<Frame>
  ![The image shows a Microsoft Azure portal displaying a list of virtual machines, including details like name, type, subscription, location, status, operating system, size, and public IP address.](https://kodekloud.com/kk-media/image/upload/v1752884431/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Connecting-to-VMs/azure-portal-virtual-machines-list.jpg)
</Frame>

## Configuring Azure Bastion

Follow these steps to set up a Bastion host:

1. Navigate to the Bastion resource in the Azure portal.
2. Create a new Bastion host with the settings below:
   * **Resource Group:** Remote Access
   * **Name:** RABastion01
   * **Region:** East US
   * **Tier:** Basic (to minimize costs)
3. Choose the virtual network (vnet-remoteaccess) and ensure Bastion has a dedicated subnet named "AzureBastionSubnet" by clicking on "Manage subnet configuration."
4. Create a new public IP address.
5. Click "Review and Create" to deploy Bastion.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a Bastion host, with fields for project and instance details such as subscription, resource group, name, region, and tier.](https://kodekloud.com/kk-media/image/upload/v1752884432/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Connecting-to-VMs/azure-portal-bastion-host-creation.jpg)
</Frame>

Once the Bastion host is deployed, you can connect to your VMs privately through your browser.

### Connecting to the Linux VM via Azure Bastion

1. Open the Azure portal and navigate to the Linux VM.
2. Click on "Connect" and select "Connect via Bastion."
3. Enter your username and password, then click "Connect."

A new browser tab will open with an SSH session to the Linux VM. You can run commands as usual. For example, update the package list:

```bash theme={null}
kodekloud@linux-ra-vm:~$ sudo -s
root@linux-ra-vm:/home/kodekloud# apt update
Get:1 http://azure.archive.ubuntu.com/ubuntu jammy InRelease [119 kB]
Get:2 http://azure.archive.ubuntu.com/ubuntu jammy-backports InRelease [109 kB]
Get:3 http://azure.archive.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
...
```

### Connecting to the Windows VM via Azure Bastion

1. In the Azure portal, navigate to the Windows VM.
2. Click on "Connect" and choose "Connect via Bastion."
3. Enter the required credentials and click "Connect."

This will open an RDP session in your browser with the Windows login screen. Once you sign in, you can securely manage the Windows VM.

<Callout icon="lightbulb" color="#1CB2FE">
  Using Azure Bastion provides secure, private access to your VMs without exposing them to the public internet.
</Callout>

## Next Steps

In the next lesson, we will explore how to configure high availability for your virtual machines. By following these best practices, you'll enhance the security and efficiency of your remote access setup.

For more information, refer to the following resources:

* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Docker Hub](https://hub.docker.com/)
* [Terraform Registry](https://registry.terraform.io/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/34d9af06-fc33-4556-a3f2-2e7a5c5db484/lesson/e818446d-8a52-4ec6-8922-2b7981ff8000" />
</CardGroup>

---


## Lesson 7: Configuring high availability

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Configuring-high-availability/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Configuring-high-availability/page.md)

**Summary:** This article discusses configuring high availability for virtual machines in Azure to ensure continuous service during failures and maintenance.

# Configuring high availability

> This article discusses configuring high availability for virtual machines in Azure to ensure continuous service during failures and maintenance.

Ensuring high availability when deploying virtual machines is critical. A single VM can become a single point of failure; if the VM or its underlying hardware encounters an issue, the hosted services may become inaccessible. High availability configurations are designed to keep systems accessible during unplanned hardware failures, software bugs, network outages, and even scheduled maintenance.

## Managing Unexpected Downtime

Unexpected downtime can result from network failures, power outages, or software bugs. Azure's architecture is designed to automatically handle these situations with redundant power sources, networking, and failover strategies. However, implementing your own high availability measures is essential to minimize the risk and impact of outages.

## Addressing Planned Maintenance

Azure routinely performs maintenance to enhance performance and security. During these events, virtual machines might need to be rebooted. Azure’s live migration technology helps move VMs to updated hosts with minimal downtime. Despite this, it is crucial to plan for redundancy and ensure proper distribution across update and fault domains to maintain service continuity.

Using availability sets and availability zones, you can configure your virtual machines to remain operational even if one component fails or is undergoing maintenance.

## Understanding Availability Sets

In Azure, high availability is often achieved by deploying your virtual machines within availability sets. An availability set is a logical grouping that enables Azure to understand the architecture of your application, providing redundancy through two main concepts:

* **Fault Domains:** These represent racks of servers within an Azure datacenter. By distributing VMs across multiple fault domains, you ensure that a hardware failure in one rack does not affect all your VMs.
* **Update Domains:** These group VMs that are updated or restarted together during planned maintenance. Azure staggers these updates so that at least one instance remains available during maintenance events.

<Callout icon="lightbulb" color="#1CB2FE">
  For example, if you deploy three VMs across separate fault domains, a power failure in one domain will only impact the affected machine, while the others remain operational.
</Callout>

Below is a diagram that illustrates how an availability set distributes VMs across fault and update domains:

<Frame>
  ![The image illustrates an "Availability Set" in a datacenter, showing three fault domains (FD0, FD1, FD2) each containing an update domain (UD0, UD1, UD2) with icons representing different types of failures.](https://kodekloud.com/kk-media/image/upload/v1752884417/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-high-availability/availability-set-fault-domains-diagram.jpg)
</Frame>

For instance, if your VMs are distributed across UD0, UD1, and UD2, a planned update in UD1 will not affect VMs in UD0 or UD2. Once UD1 completes its update, its VMs come back online, ensuring continuous service availability.

<Frame>
  ![The image illustrates an "Availability Set" in a datacenter, showing three fault domains (FD0, FD1, FD2) with update domains (UD0, UD1, UD2, UD3, UD4) and icons indicating the status of virtual machines.](https://kodekloud.com/kk-media/image/upload/v1752884418/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-high-availability/availability-set-fault-domains-diagram-2.jpg)
</Frame>

## Deploying VMs Within an Availability Set

Follow these steps to deploy virtual machines across an availability set using the Azure portal:

1. In the Azure portal, search for "availability sets" and select Create. You can also configure an availability set during the virtual machine creation process.
2. When creating a virtual machine:
   * Fill in the required basic information.
   * Under availability options, select "availability set." If no existing set is available, create a new set (for example, "HAAS01").
   * Remember that Azure supports up to three fault domains and can accommodate up to 20 update domains.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a virtual machine and an availability set. It includes fields for project and instance details, such as subscription, resource group, virtual machine name, region, and availability options.](https://kodekloud.com/kk-media/image/upload/v1752884420/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-high-availability/azure-portal-virtual-machine-creation.jpg)
</Frame>

3. Confirm the availability set settings by clicking OK. The selected availability set will be referenced when proceeding with the virtual machine creation.
4. Review the configuration and create the virtual machine. The first VM might be placed in FD0, UD0; subsequent VMs are automatically assigned to FD1, UD1, then FD2, UD2, and so on.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a virtual machine, with options for availability set, security type, image selection, VM architecture, and other configurations.](https://kodekloud.com/kk-media/image/upload/v1752884421/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-high-availability/azure-portal-virtual-machine-creation-2.jpg)
</Frame>

5. Monitor your deployment progress:

<Frame>
  ![The image shows a Microsoft Azure portal screen displaying the progress of a deployment named "CreateVm-canonical.0001-com-ubuntu-server-jammy-2." It lists various resources with their types, statuses, and operation details.](https://kodekloud.com/kk-media/image/upload/v1752884423/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-high-availability/azure-portal-deployment-progress.jpg)
</Frame>

6. Verify the deployment by navigating to your availability set in the Azure portal. Details will confirm the VMs’ placement, for example:
   * VM01: FD0, UD0
   * VM02: FD1, UD1

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of an availability set named "ha-as-01," including resource group information, location, and virtual machine status.](https://kodekloud.com/kk-media/image/upload/v1752884424/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-high-availability/azure-portal-ha-as-01-details.jpg)
</Frame>

Adding more machines is straightforward. To distribute user requests evenly, place a load balancer in front of these VMs.

## Leveraging Availability Zones for Enhanced Redundancy

While availability sets provide resilience within a single datacenter, they do not protect against complete datacenter outages. For risks such as floods, earthquakes, or large-scale failures, availability zones offer another layer of protection.

Availability zones are groups of datacenters within a region that are physically separated and interconnected with independent power, networking, and cooling. Most Azure regions now offer up to three availability zones. Deploying VMs across these zones ensures that if one zone faces an outage, the VMs in other zones remain operational.

<Frame>
  ![The image illustrates three availability zones within "Region A," with the first zone marked with a red "X," indicating an issue or failure.](https://kodekloud.com/kk-media/image/upload/v1752884426/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-high-availability/availability-zones-region-a-issue.jpg)
</Frame>

### Configuring VMs Across Availability Zones

To set up deployment across availability zones:

1. In the Azure portal, navigate to Virtual Machines and begin the creation process.
2. Under availability options, choose "availability zone" instead of an availability set.
3. Enter the required details (using the same resource group, for instance) and assign a name such as "VM HA."
4. Select multiple availability zones so that Azure deploys three VMs (e.g., VMHA1, VMHA2, and VMHA3) distributed across the zones.
5. Once deployed, you can use a load balancer to efficiently manage incoming traffic.

This strategy enhances resilience, ensuring that even if an entire datacenter or zone is impacted, your services continue to run smoothly.

## Conclusion

In this guide, we explored various methods for configuring high availability for virtual machines in Azure. We covered:

* The significance of high availability to mitigate both unexpected downtime and planned maintenance risks.
* The role of availability sets, including how fault domains and update domains help maintain service continuity.
* Step-by-step instructions for deploying VMs within an availability set via the Azure portal.
* The additional benefits of using availability zones to secure your applications against complete datacenter outages.

Next, we will delve into virtual machine scale sets to further enhance the deployment and management of scalable applications.

<Callout icon="lightbulb" color="#1CB2FE">
  For additional details on configuring and managing high availability, visit the [Azure Documentation](https://docs.microsoft.com/azure) to stay updated with the latest best practices.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/34d9af06-fc33-4556-a3f2-2e7a5c5db484/lesson/76451d6e-adaa-4f3c-81c2-180d5b50bb8d" />
</CardGroup>

---


## Lesson 8: Deploying Virtual Machine Scale Sets

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Deploying-Virtual-Machine-Scale-Sets/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Azure-Virtual-Machines/Deploying-Virtual-Machine-Scale-Sets/page.md)

**Summary:** This guide covers deploying Virtual Machine Scale Sets in Azure and explains scaling strategies, configuration, and testing autoscaling features.

# Deploying Virtual Machine Scale Sets

> This guide covers deploying Virtual Machine Scale Sets in Azure and explains scaling strategies, configuration, and testing autoscaling features.

In this guide, we explore how to deploy Virtual Machine Scale Sets (VMSS) in Azure and understand how scaling works in the cloud. You'll learn the differences between vertical and horizontal scaling and see how VMSS leverages horizontal scaling to manage a group of load-balanced VMs.

## Scaling in Azure

Azure supports two primary scaling strategies:

• Vertical scaling involves adjusting the capacity of an individual resource. For example, you might upgrade a virtual machine (VM) to a more powerful configuration (scale up) or downgrade it (scale down). Note that vertical scaling is subject to the maximum instance sizes available (hypothetically 96 vCPUs and 96 GB of RAM) and may require downtime during resizing.

• Horizontal scaling means adding or removing instances rather than modifying individual resource capacity. Adding instances is known as scale out, while removing instances is called scale in.

<Frame>
  ![The image illustrates the concept of deploying VM scale sets, showing vertical and horizontal scaling, with a diagram of server instances scaling out and in.](https://kodekloud.com/kk-media/image/upload/v1752884443/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/vm-scale-sets-deployment-diagram.jpg)
</Frame>

VM Scale Sets in Azure use horizontal scaling to distribute the load across a group of VMs automatically.

## Overview of Virtual Machine Scale Sets

Azure Virtual Machine Scale Sets (VMSS) enable you to create and manage a group of load-balanced VMs with identical configurations or, with recent updates, mixed OS images. VMSS supports scaling based on schedules, performance metrics, or on-demand requirements. Additionally, by distributing instances across availability zones, VMSS ensures high availability.

Key details about VMSS:

* Up to 1,000 instances can be deployed using marketplace or custom images.
* The limit is 600 instances when deploying with a managed image.

<Frame>
  ![The image is a screenshot of a user interface for deploying VM scale sets in Azure, highlighting features like dynamic instance adjustment and shared configuration. It includes project and scale set details such as subscription, resource group, and region.](https://kodekloud.com/kk-media/image/upload/v1752884443/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-vm-scale-sets-ui-screenshot.jpg)
</Frame>

<Frame>
  ![The image shows a guide for deploying VM scale sets in Azure, highlighting features like distribution across zones, high availability, and access via other VMs. It includes a form for creating a virtual machine scale set with options for subscription, resource group, and region.](https://kodekloud.com/kk-media/image/upload/v1752884444/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-vm-scale-sets-guide.jpg)
</Frame>

## Deploying a Virtual Machine Scale Set via the Azure Portal

Deploying a VMSS resembles deploying a single VM, with additional scaling-specific options. Follow these steps:

1. In the Azure portal, search for "VMSS" or "Virtual Machine Scale Set" and select it.

<Frame>
  ![The image shows the Microsoft Azure portal with a search bar where "vms" is typed, displaying a dropdown list of related services and resources. The background lists various Azure resources with their names and types.](https://kodekloud.com/kk-media/image/upload/v1752884445/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-portal-vms-search-dropdown.jpg)
</Frame>

2. Click on the option to create a new Virtual Machine Scale Set. For instance, you might choose a resource group named "RGHA" and name your scale set "VMSS HA01". When configuring, select the availability zones to ensure that instances are spread across different zones.

3. Choose an orchestration mode based on your needs:

   * Select **Flexible** if you need to run varied VM types or mix configurations.
   * Select **Uniform** if you prefer all instances to be identical.

   In this example, we choose **Uniform** and select a Standard VM image.

4. Set your admin credentials and configure network options. You can also configure settings related to scaling. For load balancing, you may opt for the Azure Load Balancer or Application Gateway. In our demonstration, we choose not to use either option.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a virtual machine scale set. It includes options for availability zones, orchestration mode, security type, and instance details like image and size.](https://kodekloud.com/kk-media/image/upload/v1752884447/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-portal-virtual-machine-scale-set.jpg)
</Frame>

5. Configure the scaling settings:
   * Set the initial number of instances.
   * Define the scaling policy by specifying the minimum and maximum instance counts.
   * Configure thresholds; for example, add one instance (scale out) if CPU utilization exceeds 75% for 10 minutes, or remove one instance (scale in) if it drops to 25% after a cooldown period.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a virtual machine scale set, with options for configuring scaling policies and instance counts. A pop-up in the top right corner prompts to update a saved password in Microsoft Edge.](https://kodekloud.com/kk-media/image/upload/v1752884448/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-portal-virtual-machine-scale-set-3.jpg)
</Frame>

6. On the Management tab, review the default settings for health monitoring and additional options. In the Advanced tab, you can enable the option to scale beyond 100 instances and enforce an even distribution of instances across availability zones.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a virtual machine scale set, specifically on the "Advanced" tab, with options for allocation policy and extensions.](https://kodekloud.com/kk-media/image/upload/v1752884450/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-portal-virtual-machine-scale-set-advanced.jpg)
</Frame>

7. Finally, click **Review and Create** to deploy your scale set.

<Frame>
  ![The image is a screenshot of a guide for deploying VM scale sets in Azure, showing project details and instance limits for marketplace and managed images.](https://kodekloud.com/kk-media/image/upload/v1752884451/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-vm-scale-sets-deployment-guide.jpg)
</Frame>

## Verifying the Deployment and Testing Autoscaling

After deployment, navigate to the VMSS resource page and verify the running instances. Depending on your configuration, you might initially see one or two instances. The activity log can also provide details about scaling operations, such as scaling down from two instances to one.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a virtual machine scale set instance named "vmss-ha-01" with one running instance. The status and other details of the instance are visible, such as computer name, protection policy, and provisioning state.](https://kodekloud.com/kk-media/image/upload/v1752884452/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-portal-vmss-ha-01-instance.jpg)
</Frame>

<Frame>
  ![The image shows the activity log of a virtual machine scale set in Microsoft Azure, displaying various operations with their status, time, and initiator details.](https://kodekloud.com/kk-media/image/upload/v1752884453/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-virtual-machine-scale-set-log.jpg)
</Frame>

### Connecting to an Instance for Stress Testing

Since scale set instances do not receive public IP addresses by default, a jumpbox—a VM within the same virtual network that has a public IP—is required to connect to them.

1. Identify a jumpbox VM from the list of connected devices within your virtual network.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying connected devices within a virtual network, listing a network interface and a scale set instance with their respective IP addresses and subnet information.](https://kodekloud.com/kk-media/image/upload/v1752884454/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-portal-virtual-network-devices.jpg)
</Frame>

2. Connect to the jumpbox VM via SSH using its public IP address. For example, in your terminal:

   ```bash theme={null}
   ssh kodekloud@20.124.250.11
   ```

   After entering the password and being authenticated, use this jumpbox to connect to your scale set instance. Identify the internal IP of the scale set instance (e.g., 10.0.0.6) and connect via SSH or Bastion.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a virtual machine scale set instance, including options for connecting via SSH, RDP, or Bastion, and monitoring CPU usage.](https://kodekloud.com/kk-media/image/upload/v1752884455/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-portal-virtual-machine-scale-set-5.jpg)
</Frame>

### Installing and Running Stress on the Instance

Once connected to your scale set instance, update the package list and install the stress testing tool:

```bash theme={null}
sudo apt update
sudo apt install stress -y
```

Below is an example of the installation process:

```bash theme={null}
Reading package lists... Done
Building dependency tree 
Reading state information... Done
The following NEW packages will be installed:
  stress
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 18.4 kB of archives.
After this operation, 55.3 kB of additional disk space will be used.
Fetched 18.4 kB in 0s (533 kB/s)
Selecting previously unselected package stress.
(Reading database ... 58930 files and directories currently installed.)
Preparing to unpack .../stress_1.0.4-6_amd64.deb ...
Unpacking stress (1.0.4-6) ...
Setting up stress (1.0.4-6) ...
Processing triggers for install-info (6.7.0.dfsg.2-5) ...
Processing triggers for man-db (2.9.1-1) ...
```

Before running tests, refer to the manual page of the stress tool:

```bash theme={null}
man stress
```

A common usage example is:

```bash theme={null}
stress -c 2 -t 600 -v
```

In this command:

* `-c 2` spawns two CPU stress workers.
* `-t 600` sets the test duration to 600 seconds.
* `-v` enables verbose output.

To monitor the impact on CPU usage, open another terminal session (via the jumpbox) and run:

```bash theme={null}
htop
```

You should observe CPU usage rising significantly, nearing 100% due to the stress test.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying CPU usage metrics for a virtual machine scale set instance over the past hour. The graph indicates a fluctuation in CPU usage, with a notable increase towards the end.](https://kodekloud.com/kk-media/image/upload/v1752884456/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-portal-cpu-usage-graph.jpg)
</Frame>

As the CPU usage climbs, the autoscale policy initiates the creation of additional instances. Monitor these scaling activities in the activity log:

<Frame>
  ![The image shows a Microsoft Azure portal interface with an activity log for a virtual machine scale set, indicating that an autoscale operation was initiated to increase the instance count from 1 to 2.](https://kodekloud.com/kk-media/image/upload/v1752884457/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-Virtual-Machine-Scale-Sets/azure-portal-activity-log-autoscale.jpg)
</Frame>

If the load remains high, additional instances will be added until the maximum limit defined during configuration (e.g., 10 instances) is reached.

## Conclusion

In this article, you learned how to deploy and configure Virtual Machine Scale Sets in Azure. By leveraging VMSS with a load balancer, your application can automatically scale based on CPU utilization thresholds, ensuring resources are dynamically allocated to meet demand.

<Callout icon="lightbulb" color="#1CB2FE">
  Autoscaling is a powerful feature of Azure that helps maintain performance and availability under varying load conditions. Always monitor the resource usage and adjust your scaling rules as needed.
</Callout>

This concludes our deep dive into administering virtual machine scale sets. For more insights on Azure solutions, please refer to the [Azure Documentation](https://docs.microsoft.com/azure/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/34d9af06-fc33-4556-a3f2-2e7a5c5db484/lesson/2f383198-f908-4af5-b7a7-f6b00e60ed69" />
</CardGroup>

---


# Section 10: Administer PaaS Compute Options

---


## Lesson 1: Module Introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Module-Introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Module-Introduction/page.md)

**Summary:** This guide covers administering Azure PaaS compute options, focusing on App Service Plans, App Services, and Container Instances for optimized management.

# Module Introduction

> This guide covers administering Azure PaaS compute options, focusing on App Service Plans, App Services, and Container Instances for optimized management.

Welcome to our comprehensive guide on administering Platform-as-a-Service (PaaS) compute options in Azure. In this article, you will learn how to optimize your management of Azure compute solutions by focusing on three essential services:

1. **Configuring Azure App Service Plans**\
   Azure App Service Plans define the performance and scalability of your web apps, functions, and APIs. Mastering these configurations enables you to balance performance with cost efficiency, ensuring your applications run smoothly.

2. **Configuring Azure App Services**\
   Azure App Services provide a fully managed platform ideal for hosting web applications and APIs. This section covers the setup and ongoing management processes required to deploy reliable, scalable web applications in Azure.

3. **Configuring Azure Container Instances**\
   Azure Container Instances (ACI) offer a lightweight solution for running containers without the overhead of managing virtual machines or a full orchestration platform like Kubernetes. ACI is perfect for quickly deploying containerized applications with minimal configuration.

Azure delivers a range of compute options tailored to different needs. For complete control and extensive customization, virtual machines under the Infrastructure as a Service (IaaS) model are ideal. However, when your focus is on developing web applications or mobile backends, Azure App Service is a superior PaaS solution that manages all the underlying infrastructure so you can concentrate on writing code.

For containerized workloads, if you prefer to avoid orchestration complexity, Azure Container Instances provide an excellent solution. In scenarios where you require a moderated orchestration layer that simplifies management without the full intricacies of Kubernetes, Azure Container Apps offer a balanced approach. For advanced container orchestration needs, Azure Kubernetes Service (AKS) is available.

<Callout icon="lightbulb" color="#1CB2FE">
  While AKS simplifies the deployment and management of containerized applications, it is not included in the [AZ-104: Microsoft Azure Administrator](https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator) exam curriculum. This guide will concentrate on Azure App Service, Container Instances, and select aspects of Container Apps.
</Callout>

<Frame>
  ![The image is a flowchart outlining different PaaS compute options based on specific requirements, such as full control, web apps, container solutions, and orchestration, leading to various Azure services.](https://kodekloud.com/kk-media/image/upload/v1752884788/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Module-Introduction/paas-compute-options-flowchart.jpg)
</Frame>

The diverse compute options in Azure are designed to meet varying requirements for control, complexity, and scalability. With this overview in mind, let’s begin by exploring how to configure Azure App Service Plans.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/1c21fd87-4af0-45bc-9e62-6788cd15aa71" />
</CardGroup>

---


## Lesson 2: App Service Plans

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/App-Service-Plans/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/App-Service-Plans/page.md)

**Summary:** This article explores App Service Plans, comparing them to virtual machines and guiding on selecting the best deployment option for applications.

# App Service Plans

> This article explores App Service Plans, comparing them to virtual machines and guiding on selecting the best deployment option for applications.

In this article, we explore how App Service Plans work, compare them with deploying an application on a virtual machine (VM), and guide you on selecting the best option for your needs.

Deploying an application on a VM involves Microsoft providing the underlying storage, network, and compute resources. You start by creating a VM, selecting the desired operating system, and installing the required runtime (for example, Python for a Python application). In this setup, you are responsible for managing the operating system, runtime, and your application data.

In contrast, an App Service Plan abstracts much of the infrastructure management for you. The cloud provider manages the underlying resources (such as VMs and the operating system), while you choose the appropriate runtime—like ASP.NET Core or Python—and deploy your application along with its data. Essentially, an App Service Plan defines a collection of compute resources that power your App Service (or application).

Multiple applications can run on a single App Service Plan, similar to how different VM types—General Purpose, Memory Optimized, or CPU Optimized—serve different workloads. For example, you might host both ASP.NET Core and Python applications on a Linux App Service Plan.

There are scenarios where creating a new App Service Plan is advantageous:

* Deploying applications in separate regions (for instance, an existing plan in North Europe versus a new app in West Europe).
* Switching operating systems (e.g., moving from Linux to Windows).
* Meeting high-performance demands when your application requires more memory or processing power than your current plan supports.

<Callout icon="triangle-alert" color="#FF6B6B">
  Even if no applications are deployed, you are billed for the App Service Plan. Unlike VMs, stopping the service does not stop billing, so choosing the right plan is critical for cost optimization.
</Callout>

<Frame>
  ![The image is a diagram of app service plans, showing components like data access, applications, runtime, and operating systems, with specific mentions of .NET Core, Python, and Linux App Service Plan. It also includes considerations like compute, performance tier, and hosting multiple apps.](https://kodekloud.com/kk-media/image/upload/v1752884736/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-App-Service-Plans/app-service-plans-diagram-dotnet-python-linux.jpg)
</Frame>

## App Service Plan Tiers

Azure provides multiple tiers of App Service Plans to accommodate projects ranging from small experiments to large-scale enterprise applications. Each tier offers varying levels of performance, features, capacity, and pricing:

* **Free Tier:**\
  Ideal for learning and small-scale projects.\
  • 1 GB of disk space\
  • Up to 10 web apps, mobile apps, or APIs\
  • No autoscaling, deployment slots, or scale-out capability\
  • Limited to 60 minutes of runtime per day

* **Shared Tier:**\
  Similar to the Free tier, but runs on shared Azure VM infrastructure, making it suitable for small websites with modest traffic.\
  • Limited runtime of 240 minutes per day

* **Basic Tier:**\
  Provides increased storage (10 GB) and supports up to 3 instances; however, autoscaling is not available.

* **Standard Tier:**\
  Designed for business-grade applications.\
  • 50 GB of disk space\
  • Autoscaling support\
  • 5 deployment slots\
  • Scale-out capability up to 10 instances

* **Premium Tier:**\
  Meant for more demanding applications.\
  • 250 GB of disk space\
  • 20 deployment slots\
  • Autoscaling support\
  • Scale-out capability up to 30 instances

* **Isolated Tier:**\
  The highest level for applications that require secure network access and complete isolation.\
  • 1 TB of disk space\
  • Autoscaling support\
  • 20 deployment slots\
  • Scale-out capability up to 100 instances\
  • Virtual Network support (deployed as an App Service Environment)

<Frame>
  ![The image shows a comparison table of app service plans, detailing features like web apps, disk space, auto scale, deployment slots, and max instances across different tiers (Free, Shared, Basic, Standard, Premium, Isolated). It also describes the compute options: Shared, Dedicated, and Isolated.](https://kodekloud.com/kk-media/image/upload/v1752884738/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-App-Service-Plans/app-service-plans-comparison-table.jpg)
</Frame>

Choosing the right tier depends on your application's requirements, anticipated traffic, and budget.

## Compute Options in App Service Plans

Azure App Service Plans cater to diverse compute needs with three primary compute options:

* **Shared Compute:**\
  Utilized by the Free and Shared tiers, where resources are shared with other customers.

* **Dedicated Compute:**\
  Available in the Basic through Premium tiers, this option allocates dedicated VMs to your applications, ensuring that resources are not shared with others.

* **Isolated Compute:**\
  Exclusive to the Isolated tier, VMs run within a dedicated Virtual Network, providing the highest level of isolation and scaling.

<Frame>
  ![The image shows a comparison of app service plans with different pricing tiers for Dev/Test, Production, and Isolated environments, highlighting features like memory and compute time. It also includes a note about scaling up by adding more CPU, memory, disk, and features.](https://kodekloud.com/kk-media/image/upload/v1752884739/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-App-Service-Plans/app-service-plans-comparison.jpg)
</Frame>

## Scaling in Azure App Service Plans

Azure App Service Plans support two types of scaling to ensure your application can handle variable workloads effectively:

* **Scale Up (Vertical Scaling):**\
  Upgrade your service plan to a higher tier with enhanced CPU, RAM, or disk resources without increasing the number of instances. This is ideal for applications that require more power on a single server.

* **Scale Out (Horizontal Scaling):**\
  Increase the number of running instances to distribute the load across multiple servers. Autoscaling—available from the Standard tier onward—automatically adjusts instances based on metrics like CPU usage or request queues, while manual scaling is an option in the Basic tier.

<Frame>
  ![The image shows a user interface for configuring app service plans, with options for manual scaling and custom autoscaling. It includes a sidebar menu and a description of scaling methods.](https://kodekloud.com/kk-media/image/upload/v1752884740/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-App-Service-Plans/app-service-plans-ui-scaling.jpg)
</Frame>

## Deploying an App Service Plan in the Azure Portal

Follow these steps to deploy an App Service Plan using the Azure Portal:

1. In the Azure Portal, search for "App Service Plans."
2. Click on "Create a new App Service Plan."
3. Select your subscription and create a new resource group (for example, "RG apps 01").
4. Name your plan (e.g., "ASP 01 App Service Plan 01").

<Frame>
  ![The image shows a Microsoft Azure portal page for creating an App Service Plan, with fields for project details, app service plan details, and pricing tier options.](https://kodekloud.com/kk-media/image/upload/v1752884741/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-App-Service-Plans/azure-portal-app-service-plan.jpg)
</Frame>

5. Choose the operating system (select Windows in this example) and click on "Explore Pricing Plans" to view available options. Two views will be presented:
   * A hardware view detailing the underlying infrastructure.
   * A feature view listing capabilities such as custom domains, autoscaling, backups, staging slots, and zone redundancy.

<Frame>
  ![The image shows a Microsoft Azure portal page displaying various App Service pricing plans, including details like custom domain, auto scale, daily backups, and costs per hour and month.](https://kodekloud.com/kk-media/image/upload/v1752884742/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-App-Service-Plans/azure-portal-app-service-pricing.jpg)
</Frame>

6. Select the Free tier (or another tier based on your requirements) and create the App Service Plan.

Once deployed, click "Go to resource" to view an overview of your App Service Plan. At this stage, you will notice that no apps or deployment slots are configured. (Deployment slots will be discussed later.) Auto scaling options are also visible; remember that the Free tier does not support autoscaling—upgrading to the Standard tier or above will unlock autoscaling features.

<Callout icon="lightbulb" color="#1CB2FE">
  For the Isolated plan, note that it is deployed as an App Service Environment and requires native integration with a Virtual Network. During deployment, you must select a Virtual Network.
</Callout>

<Frame>
  ![The image shows an overview of an App Service plan in Microsoft Azure, displaying details like resource group, status, location, and performance metrics such as CPU and memory percentage.](https://kodekloud.com/kk-media/image/upload/v1752884744/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-App-Service-Plans/azure-app-service-plan-overview.jpg)
</Frame>

With your App Service Plan up and running, you can now start deploying your applications. Later on, you may scale out or upgrade the plan to meet increased traffic or take advantage of advanced features.

Next, we will explore how to add applications to your App Service Plan.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/17b5b4de-3570-4b78-bfb3-a3fd79ab6883" />
</CardGroup>

---


## Lesson 3: Deploying App Service

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Deploying-App-Service/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Deploying-App-Service/page.md)

**Summary:** This article explains how to deploy and configure Azure App Service for hosting web applications and APIs with built-in CI/CD capabilities.

# Deploying App Service

> This article explains how to deploy and configure Azure App Service for hosting web applications and APIs with built-in CI/CD capabilities.

Azure App Service is a fully managed Platform-as-a-Service (PaaS) that enables you to host web applications, APIs, mobile backends, and more. Designed to support multiple programming languages and frameworks—including .NET, .NET Core, Node.js, PHP, Java, Python, and containerized applications—App Service lets you focus on your code while Azure handles the underlying infrastructure and management.

<Callout icon="lightbulb" color="#1CB2FE">
  Historically known as "Web Apps," App Service is the underlying platform that runs your web, API, or mobile application on a dedicated App Service plan. It meets enterprise standards such as ISO, SOC, and PCI, and allows integration with Microsoft Entra ID or popular social login providers for authentication.
</Callout>

## Configuring App Service

In our previous lesson, we covered the creation of an App Service plan, a prerequisite for deploying various types of applications on Azure. With App Service, you can not only host web applications but also leverage built-in capabilities like continuous integration and continuous deployment (CI/CD) directly from popular source control systems or Visual Studio.

### CI/CD and Visual Studio Integration

Azure App Service simplifies automation with support for CI/CD pipelines, enabling smooth code deployment using tools like Visual Studio and templates available from the [Azure Marketplace](https://azuremarketplace.microsoft.com/). Additional features include Core Support, Offline Data Sync, and Push Notifications that make App Service an excellent option for hosting mobile apps. Furthermore, you can run Azure Functions on an existing App Service plan without additional infrastructure.

<Frame>
  ![The image is an infographic about an App Service, highlighting supported programming languages and features like security, compliance, and CI/CD integration. It includes icons for .NET, Node.js, PHP, Java, Python, HTML5, and Docker.](https://kodekloud.com/kk-media/image/upload/v1752884776/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-App-Service/app-service-infographic-languages-features.jpg)
</Frame>

## Creating an App Service Using the Azure Portal

Follow these steps to create an App Service via the Azure portal:

1. **Access the Azure Portal**\
   After logging in, search for "App Service" to view the relevant options.

<Frame>
  ![The image shows a Microsoft Azure portal interface with a search bar and a dropdown menu displaying options related to app services, such as App Configuration and Application Insights.](https://kodekloud.com/kk-media/image/upload/v1752884778/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-App-Service/azure-portal-app-services-interface.jpg)
</Frame>

2. **Create a Web App**\
   Click on "Create Web App." Unlike creating an App Service plan, you can set up the App Service on the fly, much like creating a Resource Group. Choose your desired resource group.

3. **Configure Basic Details**\
   Provide a unique name for your App Service that will be registered under azurewebsites.net (e.g., "KodeKloudDemo"). Confirm name availability and select your publish option—whether it's Code, a Docker container, or a Static Web App.

<Frame>
  ![The image shows the "Create Web App" page on the Microsoft Azure portal, where details such as subscription, resource group, app name, and publishing options are being configured.](https://kodekloud.com/kk-media/image/upload/v1752884779/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-App-Service/create-web-app-azure-portal.jpg)
</Frame>

4. **Select a Runtime**\
   If you choose "Code" as your publishing option, select the appropriate runtime such as .NET, Java, Node.js, PHP, or Python. (For Docker deployments, select an image for the container.) If an existing App Service plan is available, it will auto-populate; otherwise, create a new one.

5. **Skip Database Configuration if Unnecessary**\
   Only configure database settings if required by your application.

6. **Configure CI/CD (Optional)**\
   In the "Deployment" section, set up your CI/CD pipeline. Detailed CI/CD configuration will be discussed in a future lesson.

7. **Finalize Networking and Monitoring Settings**\
   Configure the "Networking" and "Monitoring" sections as desired, then click "Create" to deploy your web app.

After creation, you'll receive a unique URL to access your web app through a browser. Clicking "Go to resource" will take you to your app's overview page, where you can also review all apps running under the same App Service plan.

<Frame>
  ![The image shows the Microsoft Azure portal interface for creating a web app, displaying details such as subscription, resource group, app service plan, and monitoring options. The "Review + create" tab is selected, and a "Validation" button is highlighted.](https://kodekloud.com/kk-media/image/upload/v1752884779/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-App-Service/azure-portal-web-app-creation-2.jpg)
</Frame>

## Scaling the App Service Plan

To accommodate growing demand, you might need to scale your App Service plan. For example, you can upgrade from a free or shared tier to a Standard plan.

1. **Select a Pricing Tier**\
   Choose the desired pricing tier (e.g., Standard S1) and click "Select."

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying options for scaling out an App Service plan, with various pricing tiers and specifications listed.](https://kodekloud.com/kk-media/image/upload/v1752884780/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-App-Service/azure-portal-app-service-scaling.jpg)
</Frame>

<Callout icon="triangle-alert" color="#FF6B6B">
  Resizing the plan will restart your App Service, which may lead to temporary downtime.
</Callout>

2. **Adjust Instance Count**\
   Once upgraded to the Standard plan, you can manually set the instance count (up to a maximum of 10 by default).

<Frame>
  ![The image shows a Microsoft Azure portal interface for configuring the scaling options of an App Service plan. It includes settings for manual, automatic, and rules-based scaling methods.](https://kodekloud.com/kk-media/image/upload/v1752884782/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-App-Service/azure-portal-app-service-scaling-2.jpg)
</Frame>

3. **Configure Autoscale Rules**\
   Alternatively, set up rule-based autoscale settings. For example:
   * Increase the instance count by one when CPU usage exceeds 70%.
   * Decrease the instance count by one when CPU usage falls below 25%.

<Frame>
  ![The image shows the Microsoft Azure portal with an autoscale setting configuration for an App Service plan. It includes options for setting the scale mode, rules, and instance limits.](https://kodekloud.com/kk-media/image/upload/v1752884782/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Deploying-App-Service/azure-portal-autoscale-settings.jpg)
</Frame>

These autoscale configurations enable your application to dynamically adjust resources based on real-time demand.

## Next Steps

In upcoming lessons, we will build upon this foundation by enhancing security features, configuring advanced CI/CD pipelines, and setting up deployment slots. This initial App Service deployment serves as a launching point for further application development and scaling.

Happy deploying!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/3f97f761-339d-4c7c-83a4-12e99f522282" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/24a6c129-cc0c-4638-a923-6b7276b2f889" />
</CardGroup>

---


## Lesson 4: Securing App Service

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Securing-App-Service/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Securing-App-Service/page.md)

**Summary:** This guide covers essential security measures for App Service, including authentication, SSL, diagnostic settings, network ACLs, and Key Vault integration to protect applications.

# Securing App Service

> This guide covers essential security measures for App Service, including authentication, SSL, diagnostic settings, network ACLs, and Key Vault integration to protect applications.

Securing your App Service is essential for protecting your applications from unauthorized access and potential threats. In this guide, we cover several security topics including App Service Authentication, SSL certificates, diagnostic settings, network ACLs, and Key Vault integration. These measures combine to create a robust security framework for your web applications.

## App Service Authentication

App Service Authentication adds a layer of protection by intercepting incoming requests and requiring valid credentials before allowing access. This built-in feature supports multiple identity providers such as Microsoft, Apple, Facebook, GitHub, Google, and Twitter. For providers that use OpenID Connect, Azure App Service leverages OAuth 2.0 protocols to ensure secure integration.

By default, anonymous access is permitted. For example, navigating directly to your app’s URL will load the landing page without any authentication prompts. To secure your app, switch the default setting and enforce the authentication mechanism of your choice.

<Callout icon="lightbulb" color="#1CB2FE">
  Ensure that you select a provider that complements your application's user base and security requirements.
</Callout>

## Securing Data with SSL Certificates

Implementing SSL certificates is vital for encrypting the data exchanged between your application and its users. This encryption safeguards sensitive information during transit and builds trust with your end-users.

## Diagnostic Settings

Diagnostic settings are a key part of maintaining and troubleshooting your Azure App Service. By enabling detailed logging and monitoring, you can quickly identify and resolve potential performance issues or security vulnerabilities.

## Network Access Control Lists (ACLs)

Network ACLs further secure your App Service by specifying which IP addresses or networks are permitted to access your application. Configuring these rules minimizes the exposure of your web app to unauthorized traffic.

<Callout icon="lightbulb" color="#1CB2FE">
  Always evaluate your network access rules to ensure that only trusted sources can communicate with your App Service.
</Callout>

## Key Vault Integration

Managing sensitive data such as API keys, connection strings, and other secrets is streamlined with Azure Key Vault. By integrating your App Service with Key Vault, you eliminate the risk of exposing secrets in your code or configuration files, ensuring that sensitive information remains secure.

<Frame>
  ![The image is a presentation slide about securing an app service, highlighting authentication and security features, and showing a dropdown menu for selecting an identity provider.](https://kodekloud.com/kk-media/image/upload/v1752884790/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Securing-App-Service/securing-app-service-authentication-slide.jpg)
</Frame>

## Deploying Code to Your App Service

After securing your service, the next step is deploying your application code. While there are multiple deployment methods available, this guide focuses on using Visual Studio Code. However, Visual Studio, FTP, and other techniques are equally effective.

### Deploying with Visual Studio Code

To deploy with Visual Studio Code, press Control+Shift+P and select "Deploy to Web App." You will be prompted to choose your project folder and target web app. If you haven’t authenticated with your Azure account yet, follow the on-screen instructions. Once connected, the deployment process automatically begins.

Below is an example of an HTML file deployed to the App Service:

```html theme={null}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NiceAdmin</title>
    <!-- Template Azure App Service: Deploy to Web App... -->
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- ====== Header ====== -->
    <header id="header" class="header fixed-top d-flex align-items-center">
        <div class="d-flex align-items-center justify-content-between">
            <a href="index.html" class="logo d-flex align-items-center">
                <img src="assets/img/logo.png" alt="">
                <span class="d-none d-lg-block">NiceAdmin</span>
            </a>
            <i class="bi bi-list toggle-sidebar-btn"></i>
        </div><!-- End Logo -->
        
        <div class="search-bar">
            <form class="search-form d-flex align-items-center" method="POST" action="#">
                <input type="text" name="query" placeholder="Search keyword" title="Enter search keyword">
                <button type="submit"><i class="bi bi-search"></i></button>
            </form>
        </div><!-- End Search Bar -->
    </header><!-- End Header -->
</body>
</html>
```

After selecting your folder and target app, Visual Studio Code deploys your code to Azure. The following snippet demonstrates how vendor CSS and associated resources are included during deployment:

```html theme={null}
<!-- Vendor CSS -->
<link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
<link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
<link href="assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
<link href="assets/vendor/quill/quill.bubble.css" rel="stylesheet">
<link href="assets/vendor/quill/quill.snow.css" rel="stylesheet">
<link href="assets/vendor/remixicon/remixicon.css" rel="stylesheet">
<link href="assets/vendor/simple-datatables/style.css" rel="stylesheet">

<!-- Template Main CSS File -->
<link href="assets/css/style.css" rel="stylesheet">

<!-- Template Name: NiceAdmin -->
<!-- Updated: Nov 17 2023 with Bootstrap v5.3.2 -->
<!-- Template URL: https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/ -->
<!-- License: BootstrapMade.com/license/ -->

<body>
<!-- ======= Header ======= -->
<header id="header" class="header fixed-top d-flex align-items-center">
  <div class="d-flex align-items-center justify-content-between">
    <a href="index.html" class="logo d-flex align-items-center">
      <img src="assets/img/logo.png" alt="">
      <span class="d-none d-lg-block">NiceAdmin</span>
    </a>
    <i class="bi bi-list toggle-sidebar-btn"></i>
  </div><!-- End Logo -->

  <!-- End Search Bar -->
</header>
```

During deployment, a zip package of your application is created and pushed to your App Service. You can review the deployment log to ensure everything processed smoothly:

```html theme={null}
<!-- Deployment Log Output -->
10:07:29 PM kodekloudemoapp: Copying file: 'assets\img\messages-3.JPG'
10:07:29 PM kodekloudemoapp: Copying file: 'assets\img\news-1.jpg'
10:07:30 PM kodekloudemoapp: Copying file: 'assets\img\news-3.jpg'
10:07:30 PM kodekloudemoapp: Copying file: 'assets\img\news-4.jpg'
10:07:30 PM kodekloudemoapp: Omitting next output lines...
10:07:30 PM kodekloudemoapp: Finished successfully.
10:07:30 PM kodekloudemoapp: Running post deployment command(s)...
10:07:30 PM kodekloudemoapp: Triggering recycle (preview mode disabled).
10:07:30 PM kodekloudemoapp: Deployment successful.
```

After a successful deployment, navigate to your website. A refresh will display the deployed Bootstrap template and confirm that your application is live.

## Securing Your Application with Authentication

By default, App Service does not enforce authentication. To enhance security, go to the Authentication section of your web app in the Azure Portal and add an identity provider. In this example, Microsoft Entra ID is used.

After creating an app registration within Microsoft Entra ID, use the default configuration settings and click "Add." With the identity provider active, open an incognito window and navigate to your app’s URL. A sign-in prompt confirms that authentication is now required to access your application.

<Frame>
  ![The image shows a Microsoft Azure portal page for adding an identity provider, with options for app registration and authentication settings.](https://kodekloud.com/kk-media/image/upload/v1752884791/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Securing-App-Service/azure-portal-identity-provider-settings.jpg)
</Frame>

## Additional Deployment Options

If Visual Studio Code is not your preferred deployment tool, consider these alternatives:

* **Deployment Center:** A centralized hub to explore various deployment methods.
* **FTPS Credentials:** Retrieve your FTPS endpoint, username, and password to deploy files using any FTP client.

<Frame>
  ![The image shows the FTPS credentials section of the Deployment Center in Microsoft Azure for a web app named "kodekloudemoapp." It includes fields for FTPS endpoint, username, and password management.](https://kodekloud.com/kk-media/image/upload/v1752884792/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Securing-App-Service/ftps-credentials-deployment-center-kodekloudemoapp.jpg)
</Frame>

* **Kudu Portal:** A web-based interface for file management and uploads.

## Implementing SSL Certificates

Azure provides various options for securing your web app with SSL certificates. You can either purchase a Managed Certificate directly from Azure or bring your own public key certificates, ensuring that all communication to and from your application is encrypted.

## Configuring Network Access Restrictions

Control public access to your App Service via the Networking blade in the Azure Portal. Here, you can configure rules to restrict traffic to specific IP addresses. The process involves creating "Allow" rules for trusted sources and adding a "Deny All" rule to block unauthorized access.

For instance, to allow a specific IPv4 address, set up a rule with:

* Action: Allow
* Priority: 100
* Type: IPv4 (or IPv6/Virtual Network Service Tag)
* Source IP: \[Your desired IP]

Then, create an additional rule to deny all other traffic:

* Rule Name: Deny All
* Action: Deny
* Priority: 101
* Type: IPv4

<Frame>
  ![The image shows the Microsoft Azure portal with the "Access Restrictions" settings for a web app. It includes options for configuring site access rules and adding a new rule with specific settings like action, priority, and source IP address.](https://kodekloud.com/kk-media/image/upload/v1752884793/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Securing-App-Service/azure-portal-access-restrictions-settings.jpg)
</Frame>

With these rules configured, any access attempt from an unauthorized IP address will result in a "Forbidden" error message.

## Custom Domains

By default, your App Service is hosted under the azurewebsites.net domain. For branding or SEO purposes, you may configure a custom domain (e.g., kodecloud.com) in the Azure Portal to better align with your business identity.

***

This guide has reviewed the key strategies for securing your App Service, deploying your application code, and enforcing robust authentication and network restrictions. Implement these best practices to safeguard your web applications and improve overall performance and security.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/5c87991c-d266-4f47-874a-8f455779ddf7" />
</CardGroup>

---


## Lesson 5: Custom Domains

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Custom-Domains/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Custom-Domains/page.md)

**Summary:** Learn to validate and map a custom domain to Azure App Service using A and CNAME methods for enhanced branding.

# Custom Domains

> Learn to validate and map a custom domain to Azure App Service using A and CNAME methods for enhanced branding.

Azure App Service automatically provides a default domain (azurewebsites.net) for every web app. For enhanced branding and a more professional appearance, you can configure your own custom domain. In this guide, you'll learn how to validate and map a custom domain to your App Service using both A and CNAME mapping methods.

<Callout icon="lightbulb" color="#1CB2FE">
  Custom domains are supported on the Basic plan and higher. The free and shared tiers do not support custom domains.
</Callout>

## Validating Domain Ownership

Before mapping your custom domain, you need to prove ownership by adding a TXT record at your DNS provider. Once this TXT record is successfully added, you can choose to create an A record or a CNAME record to point your custom domain to the App Service.

## Step-by-Step Process

In this example, we will map the custom domain "furbish.com" using the CNAME method. Follow these steps in the Azure portal:

1. **Access the Custom Domains Section**\
   Navigate to your App Service and select the **Custom domains** section.

2. **Add a Custom Domain**\
   Click on **Add custom domain**. You can either use a domain you already own or purchase an App Service domain directly from Azure, which collaborates with GoDaddy. For this example, enter "[www.furbish.com](http://www.furbish.com)".

3. **Choose the CNAME Method**\
   Select the CNAME option. Azure will display the required DNS records needed for the configuration. Copy the provided TXT record value as it will be used to validate domain ownership.

4. **Update Your DNS Records**\
   In your DNS management system (such as Azure DNS), add the TXT record with the specified value. Then, add the CNAME record following Azure's instructions.

Below is an image from the Azure portal showing the custom domain settings, which include the domain provider options, TLS/SSL certificate settings, and domain validation details:

<Frame>
  ![The image shows a Microsoft Azure portal interface for adding a custom domain to a web app. It includes settings for domain provider, TLS/SSL certificate, and domain validation details.](https://kodekloud.com/kk-media/image/upload/v1752884771/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Custom-Domains/azure-portal-custom-domain-settings.jpg)
</Frame>

5. **Validate DNS Propagation**\
   After saving your DNS records, allow some time for propagation. Once your DNS changes are effective, click on **Validate** in the Azure portal. Azure will query your DNS zone to confirm the existence of the records.

6. **Complete the Custom Domain Setup**\
   When validation is successful, click on **Add** to associate the custom domain with your App Service. Initially, you might see a binding error due to the absence of an SSL certificate. This error is temporary and will be resolved once an SSL certificate is added to secure your connection.

<Callout icon="triangle-alert" color="#FF6B6B">
  Until an SSL certificate is applied, your web app may display a "Not Secure" message.
</Callout>

After clicking **Continue**, you will be redirected to the App Service dashboard with your updated domain settings.

## Next Steps

In the following section, we will cover the backup process for your App Service. Before moving on, take a look at the dashboard view from a web application interface, which illustrates sales, revenue, and customer statistics:

<Frame>
  ![The image shows a dashboard interface from a web application called "NiceAdmin," displaying sales, revenue, and customer statistics, along with recent activity and budget reports. It includes graphs and tables for data visualization.](https://kodekloud.com/kk-media/image/upload/v1752884772/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Custom-Domains/niceadmin-dashboard-sales-revenue-stats.jpg)
</Frame>

This concludes the custom domain integration process with Azure App Service. Up next, we will explore how to back up your App Service to ensure your data is secure.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/b1011360-3eb0-417a-89e7-b6a1d82cdcfc" />
</CardGroup>

---


## Lesson 6: Backup App Service

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Backup-App-Service/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Backup-App-Service/page.md)

**Summary:** The article describes the Backup App Service in Azure for safeguarding web applications through manual and scheduled backups.

# Backup App Service

> The article describes the Backup App Service in Azure for safeguarding web applications through manual and scheduled backups.

The Backup App Service feature in Azure provides a reliable solution to safeguard your web applications against catastrophic failures. With this functionality, you can perform both manual and scheduled backups, ensuring that your app’s configuration settings, file contents, and connected databases are securely saved.

<Callout icon="lightbulb" color="#1CB2FE">
  Backup App Service supports up to 10 GB of data per backup, which includes both your app and its associated database. Note that this feature is available exclusively on Standard and Premium plans.
</Callout>

You can configure both full and partial backups based on your specific requirements. Once a backup is created, you have the flexibility to restore the app to a previous state or even create a new web app from the backup file, enabling rapid recovery with minimal downtime.

When you access the backup option in the Azure portal, you will first need to select a storage account where your backups will be securely stored. Additionally, you have the option to configure custom backup settings to tailor the retention policy and backup schedule to your needs.

<Frame>
  ![The image shows a Microsoft Azure portal interface for managing backups of a web app named "kodekloudemoapp." It displays backup details, including the schedule, status, and options to configure or restore backups.](https://kodekloud.com/kk-media/image/upload/v1752884752/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Backup-App-Service/azure-portal-kodekloudemoapp-backups.jpg)
</Frame>

Custom backups let you define your own retention policies and schedules for backup collection, whereas the automatic backup configuration provided by Azure runs every hour. This automated approach allows you to quickly restore your app from a previous restore point whenever needed.

Next, we will explore how to set up CI/CD pipelines and deployment slots for your web app, enhancing your development workflow and streamlining the deployment process.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/5c4c62e2-6aea-4d3d-a156-c21e0526ffb6" />
</CardGroup>

---


## Lesson 7: CICD and Deployment slots

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/CICD-and-Deployment-slots/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/CICD-and-Deployment-slots/page.md)

**Summary:** Learn to streamline development workflows using CI/CD and deployment slots for Azure App Service, covering automated deployments, environment management, and rollback strategies.

# CICD and Deployment slots

> Learn to streamline development workflows using CI/CD and deployment slots for Azure App Service, covering automated deployments, environment management, and rollback strategies.

Learn how to streamline your development workflow using Continuous Integration/Continuous Deployment (CI/CD) and deployment slots for Azure App Service. This guide covers best practices for automated deployments, managing multiple environments, and ensuring smooth rollbacks.

***

## CI/CD Overview

CI/CD enhances code quality and accelerates delivery by automating integration and deployment processes. Azure App Service supports two primary deployment methods that help teams minimize downtime and improve reliability:

1. **Automated Deployment**\
   Developers push new code—including features, patches, and bug fixes—to repositories such as GitHub, Bitbucket, Local Git, or Azure Repos. When integrated with CI/CD, these updates are automatically propagated to the App Service with minimal impact on end users.

2. **Manual Deployment**\
   Developers store code in remote cloud storage services (e.g., OneDrive or Dropbox) or external Git repositories, then manually trigger updates to the App Service.

<Callout icon="lightbulb" color="#1CB2FE">
  As of September 30, 2023, integrations for Microsoft OneDrive and Dropbox have been retired for Azure App Service and Azure Functions. Ensure any cascading deployments are disabled since these options no longer appear in the Azure portal.
</Callout>

<Frame>
  ![The image illustrates a CI/CD process with two deployment methods: automated and manual, connected to various repositories and storage services like Azure Repos, Bitbucket, Git, OneDrive, and Dropbox.](https://kodekloud.com/kk-media/image/upload/v1752884753/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/ci-cd-process-automated-manual.jpg)
</Frame>

***

## Configuring CI/CD in Azure App Service

To configure CI/CD for your web app in Azure App Service, follow these steps:

1. **Browse Code in the Azure Portal**\
   Start by exploring your code directly within the Azure portal. Below is an example of an HTML snippet from an application deployed earlier:

   ```html theme={null}
   <link href="assets/css/style.css" rel="stylesheet">
   <!--
   Template Name: NiceAdmin
   Updated: Nov 17 2023 with Bootstrap v5.3.2
   Template URL: https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/
   Author: BootstrapMade.com
   License: https://bootstrapmade.com/license/
   -->
   ```

2. **Review Git Terminal Logs**\
   The following sample log snippets illustrate common Git operations during CI/CD processes:

   ```bash theme={null}
   2023-12-17 10:19:49 | git status -z -uall [77ms]
   2023-12-17 10:18:17 | git diff --cached --files --stage C:\Users\RithinSkaria\App Service Demo Site\index.html [672ms]
   2023-12-17 10:18:17 | git show --textconv :index.html [609ms]
   ```

   These operations can be collectively referred to as the “code cloud dashboard.” Subsequent Git logs after saving changes might appear as follows:

   ```bash theme={null}
   (upstream:remote:refs/heads/main refs/remotes/main [63ms]
   2023-12-12 17:10:09.494 [info] git status -z --all [77ms]
   2023-12-12 17:10:09.614 [info] git ls-files --stage 2> /dev/null [53ms]
   2023-12-12 17:10:09.723 [info] git show --textconv  65587bb26627 [69ms]
   [113ms]
   ```

Since the repository is linked to Azure Repos, you can directly view it in the portal. When you commit changes, they automatically reflect on your App Service. For example, after configuring CI/CD through the Deployment Center, you may observe a log entry like the one below:

<Frame>
  ![The image shows a screenshot of an Azure DevOps repository interface, displaying a list of HTML files and folders with details about their last changes and commit information.](https://kodekloud.com/kk-media/image/upload/v1752884754/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/azure-devops-repo-html-files-screenshot.jpg)
</Frame>

Within Deployment Center, select Azure Repos (or alternatives like GitHub or Bitbucket), then choose the organization, project, repository, and branch as needed. After saving your configuration, inspect the deployment logs:

<Frame>
  ![The image shows the Deployment Center page of a web app in Microsoft Azure, displaying a successful deployment log entry with details such as time, commit ID, and author.](https://kodekloud.com/kk-media/image/upload/v1752884756/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/azure-deployment-center-log-entry.jpg)
</Frame>

Changes made in Visual Studio Code—such as modifications to the index.html file—are automatically tracked, committed, and synchronized with your repository. Refreshing the Azure repository confirms the push, and your web app reflects these updates. Consider the following Git log outputs during development:

```bash theme={null}
2023-12-12 17:20:33.838 [info] git for-each-ref --format=%(refname:short) %(objectname) %(upstream:track) %(upstream:remotename)%
2023-12-12 17:20:33.874 [info] git config --get commit.template [401ms]
2023-12-12 17:20:34.321 [info] git status --porcelain [341ms]
```

If further edits are made (such as renaming the dashboard to "KodeKloud demo dashboard"), these operations are tracked similarly:

```bash theme={null}
2023-12-12 17:20:33.874 [info] git config --get commit.template [401ms]
2023-12-12 17:20:52.228 [info] git status --zaull [341ms]
2023-12-12 17:20:52.444 [info] git ls-files --stage -- C:\Users\RithinSkaria\App Service Demo Site\index.html [100ms]
2023-12-12 17:20:52.519 [info] git cat-file -s 238484d627e559be [83ms]
2023-12-12 17:20:53.400 [info] git show --textconv :index.html [94ms]
```

After committing these changes, the updated repository synchronizes with the App Service. The production environment remains unchanged until you merge into the main branch or manually swap deployment slots.

For instance, a further commit updating the production dashboard might include the following HTML snippet:

```html theme={null}
<h1>Kodekloud Production Dashboard</h1>
<nav>
    <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="index.html">Home</a></li>
        <li class="breadcrumb-item active">Dashboard</li>
    </ol>
</nav>
```

And the corresponding Git operations could look like this:

```bash theme={null}
2023-12-12 17:50:49.Z0  [info] git add -A -- [303ms]
2023-12-12 17:51:02.750 [info] git commit -C user.useRongularityhere commit --quiet --allow-empty-message --file - [53ms]
2023-12-12 17:51:03.142 [info] git config --get commit.template [259ms]
2023-12-12 17:51:03.584 [info] git for-each-ref --format=%(refname:short)%(objectname)%(upstream:track)%(upstream:remotename)... [428ms]
```

After syncing with the Azure portal, these changes are deployed successfully. Note that if you use separate branches (e.g., development vs. production), the production App Service remains on the older version until a merge or slot swap occurs.

<Frame>
  ![The image shows a dashboard interface from a web application, displaying sales, revenue, and customer metrics, along with graphs and recent activity logs.](https://kodekloud.com/kk-media/image/upload/v1752884757/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/web-application-dashboard-sales-metrics.jpg)
</Frame>

***

## Deployment Slots Explained

Deployment slots enable you to create multiple environments (such as staging, QA, UAT, or development) within a single Azure App Service. Testing new code in a staging slot prior to a production swap minimizes downtime and avoids performance issues like cold starts.

Key features of deployment slots include:

* **Environment Separation:**\
  Each slot represents an environment—production, QA, or development—allowing for isolated testing and validation.

* **Auto Swap:**\
  Automatically swap slots when validations are successful to eliminate service disruptions.

* **Rollback Capability:**\
  Quickly revert to a previous version by swapping back to the last known good configuration.

* **Service Plan Limitations:**
  * Free, Shared, and Basic: Deployment slots are not supported.
  * Standard: Supports up to 5 slots.
  * Premium and Isolated: Support up to 20 slots.

When creating a deployment slot, decide whether to clone the app configuration (from production or another slot) or start fresh. Understand which settings swap and which do not. Generally, swappable settings include general settings, WebJob contents, app settings, path mappings, hybrid connections, connection strings, service endpoints, handler mappings, and Azure CDN configurations. Non-swappable settings include publishing endpoints, scale settings, CORS, custom domains, IP restrictions, VNet integration, non-public certificates, always-on configuration, managed identities, TLS/SSL settings, diagnostic settings, and any setting ending with an extension version suffix.

<Frame>
  ![The image illustrates the process of deployment slots in Azure, showing the flow from Azure Repos to Staging and Production, along with considerations for settings that can and cannot be swapped.](https://kodekloud.com/kk-media/image/upload/v1752884758/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/azure-deployment-slots-flow-diagram.jpg)
</Frame>

A common workflow involves committing code to a development branch, validating the changes via CI/CD, and then creating a pull request to merge into the main (production) branch. This triggers a production deployment automatically.

***

## Working with Branches and Slots

You can configure separate deployment slots for different branches to facilitate parallel development. For example, create a "dev" branch in Azure Repos containing the same content as the main branch, and then add a corresponding deployment slot in your App Service.

1. Open the Azure portal and navigate to your App Service.
2. Under Deployment Center, add a new slot (e.g., "dev").\
   When prompted, choose whether to clone the settings from the production app.

<Frame>
  ![The image shows the Microsoft Azure portal with a focus on the "Deployment Slots" section for a web app named "kodekloudemoapp." A panel is open to add a new slot named "dev," with an option to clone settings.](https://kodekloud.com/kk-media/image/upload/v1752884759/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/azure-portal-deployment-slots-kodekloudemoapp.jpg)
</Frame>

3. Configure CI/CD for the new slot to pull code from the "dev" branch. After saving, you will see a pending deployment log entry:

<Frame>
  ![The image shows the Deployment Center settings in Microsoft Azure, where Azure Repos is selected as the source for deploying and building code. It includes options for organization, project, repository, and branch selection.](https://kodekloud.com/kk-media/image/upload/v1752884761/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/azure-deployment-center-repos-settings.jpg)
</Frame>

<Frame>
  ![The image shows the Deployment Center in Microsoft Azure, displaying a pending deployment log entry for a commit from VSTS on December 12, 2023.](https://kodekloud.com/kk-media/image/upload/v1752884762/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/azure-deployment-center-pending-log.jpg)
</Frame>

Once the CI/CD process completes for the "dev" slot, preview the changes by refreshing the slot’s URL. Changes committed to the development branch will only affect the "dev" slot until merged with the main branch or manually swapped.

In Visual Studio Code, switching to the "dev" branch and committing changes might generate Git logs like:

```bash theme={null}
2023-12-12 17:50:27.720 [info] git ls-files --stage -- C:\Users\RithinSkaria\App Service Demo Site\index.html [214ms]
2023-12-12 17:50:28.029 [info] git cat-file -s 800aac8961d7f959b221c21678c17 [240ms]
2023-12-12 17:50:28.032 [info] git show --textconv index.html [218ms]
2023-12-12 17:50:28.483 [info] git for-each-ref --format=%(refname:short)%(objectname)%(upstream:track)%(upstream:remotename) [265ms]
2023-12-12 17:50:28.658 [info] git status -v -z [342ms]
```

Once you push these changes to the "dev" branch, you can later merge them into the main branch through a pull request:

<Frame>
  ![The image shows an Azure DevOps interface displaying a repository named "App Service Demo Site" with a list of files and folders, including HTML files and directories like "assets" and "forms." The interface includes options for setting up a build and creating a pull request.](https://kodekloud.com/kk-media/image/upload/v1752884763/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/azure-devops-app-service-repo.jpg)
</Frame>

If you choose not to create a pull request, you can swap the deployment slots directly. Swapping exchanges the contents of the "dev" and production slots, enabling a quick rollback if needed.

<Frame>
  ![The image shows a Microsoft Azure DevOps interface with a pull request titled "prod-change" proposing to merge a branch. A sidebar is open for completing the pull request with options like "Delete dev after merging" selected.](https://kodekloud.com/kk-media/image/upload/v1752884764/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/azure-devops-pull-request-prod-change.jpg)
</Frame>

After additional commits—such as adding a version marker "build 1.0" in the "dev" slot—and verifying deployment logs, perform the swap:

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying deployment slots for a web app named "kodekloudemoapp." It includes a swap configuration panel with source and target settings for deployment changes.](https://kodekloud.com/kk-media/image/upload/v1752884766/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/azure-portal-deployment-slots-kodekloudemoapp-2.jpg)
</Frame>

Swapping pushes the new code from the "dev" slot into production while moving the old production code into the "dev" slot. This method enables quick rollbacks in case of deployment issues.

After a successful swap, both production and development slots display the updated builds. For example, refreshing the production site will show the updated “build 1.0” dashboard, while the development slot reverts to its previous state.

<Frame>
  ![The image shows a Microsoft Azure Deployment Center interface displaying deployment logs for a web app, including commit IDs, authors, statuses, and messages.](https://kodekloud.com/kk-media/image/upload/v1752884767/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/azure-deployment-center-logs-web-app.jpg)
</Frame>

***

## Summary

This guide demonstrated setting up CI/CD with Azure App Service and using deployment slots to efficiently manage multiple environments. These techniques not only streamline deployments but also ensure seamless testing and safe rollbacks to maintain production stability.

Next, explore Azure Container Instances in our upcoming lesson for containerized deployment solutions.

<Frame>
  ![The image shows a dashboard interface from "NiceAdmin" with various widgets displaying sales, revenue, customer data, recent activity, and budget reports. It includes graphs and tables for visualizing data trends and performance metrics.](https://kodekloud.com/kk-media/image/upload/v1752884769/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-CICD-and-Deployment-slots/niceadmin-dashboard-sales-revenue-widgets.jpg)
</Frame>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/1e055acf-9eab-4086-82b6-f5875b6660e4" />
</CardGroup>

---


## Lesson 8: Azure Container Instances

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Azure-Container-Instances/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Azure-Container-Instances/page.md)

**Summary:** Azure Container Instances provide a serverless approach to deploying containerized applications, simplifying management and enhancing scalability within the Azure ecosystem.

# Azure Container Instances

> Azure Container Instances provide a serverless approach to deploying containerized applications, simplifying management and enhancing scalability within the Azure ecosystem.

Azure Container Instances (ACI) offer a serverless, streamlined approach to deploying containerized applications. In this guide, we compare traditional virtual machines (VMs) with containers and explain how ACI simplifies container deployment and management within the Azure ecosystem, making it an ideal solution for modern cloud applications.

## Comparing Virtual Machines and Containers

In cloud computing, both traditional VMs and modern containers serve as ways to run applications, but they follow distinct models.

### Virtual Machines

Virtual machines are a well-established method of virtualization. A typical VM setup includes:

* **Hypervisor:** A server hosting the hypervisor.
* **Guest Operating System:** Each VM runs its own guest OS.
* **Application Environment:** The allocated OS contains the application along with its necessary binaries and libraries.

This architecture provides robust isolation and security, as each VM operates independently. However, the overhead of maintaining a full operating system often leads to increased resource usage and slower startup times.

### Containers

Containers deliver a more agile and lightweight solution by:

* **Sharing the Host Kernel:** Containers use the host OS kernel while running in isolated user mode environments.
* **Packaging Dependencies:** Each container packages the application and its dependencies (libraries and binaries) without bundling an entire operating system.
* **Efficient Runtime:** Managed by a container runtime, containers are significantly smaller and faster to start compared to VMs.

Think of VMs as separate houses—each with their own infrastructure—whereas containers are like apartments within a building that share common utilities but maintain distinct, secure spaces.

### Detailed Comparison

| Feature               | Virtual Machines                                                        | Containers                                                                                            |
| --------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Isolation & Execution | Hardware-level isolation using a hypervisor and guest OS                | OS-level isolation with the host OS kernel simplifies management                                      |
| Deployment            | Involves provisioning an entire OS, configuring storage, and networking | Image-based deployment that encapsulates all dependencies for rapid scaling                           |
| Storage               | Uses block storage with its own file system                             | Supports ephemeral storage or persistent storage via volumes                                          |
| Fault Tolerance       | Achieved through replication, failover clustering, or availability sets | Utilizes orchestration tools (e.g., [Kubernetes](https://kubernetes.io/docs/)) for automatic recovery |

<Frame>
  ![The image compares virtual machines and containers, illustrating their architecture layers, including applications, libraries, guest OS, hypervisor, container runtime, host OS, and server. It highlights key features like isolation, deployment, storage, and fault tolerance.](https://kodekloud.com/kk-media/image/upload/v1752884744/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Container-Instances/vm-vs-containers-architecture-comparison.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Containers provide faster startup times and efficient resource usage, which makes them ideal for dynamic scaling and microservices architectures compared to traditional VMs.
</Callout>

## Azure Container Instances Overview

Azure Container Instances abstracts the infrastructure complexity, allowing you to run containerized applications without managing VMs. Under the hood, ACI leverages a virtual network and container host, equipped with a container runtime that simplifies container execution.

Key advantages of ACI include:

* **Fast Startup:**\
  Containers on ACI start in seconds, enabling rapid deployments—ideal for web applications, APIs, and event-driven workloads.
* **Strong Isolation:**\
  Each container instance operates in an isolated environment, ensuring processes remain secure and independent.
* **Scalability:**\
  ACI supports dynamic scaling by increasing the number of container instances as workload demands rise.
* **Persistent Storage:**\
  ACI allows you to mount Azure Storage volumes (such as Azure Files or Azure Disk) to facilitate persistent storage even though container instances are typically ephemeral.
* **Flexible Networking:**\
  Configure ACI for public or private networking, with features like port mapping, public IP assignment, and integration with Azure Virtual Networks for secure communications.
* **Multi-OS Support:**\
  Depending on your container image, ACI supports both Windows and Linux containers.

<Frame>
  ![The image illustrates the features and network setup of Azure Container Instances, highlighting benefits like faster startup, scalability, and isolation, alongside a diagram showing a container host within a virtual network.](https://kodekloud.com/kk-media/image/upload/v1752884745/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Container-Instances/azure-container-instances-network-setup.jpg)
</Frame>

## Deploying a Container Instance in Azure

Follow these steps to deploy a container instance using the Azure Portal:

1. **Launch the Azure Portal and Search for Container Instances:**\
   Open the Azure Portal, type “Container Instances” in the search bar, and click **Create**.

2. **Configure Basic Settings:**
   * **Resource Group:** Choose an existing resource group or create a new one (e.g., "ACI Web 0.1").
   * **Availability Zone:** Optionally specify an availability zone (such as East US Availability Zones currently in preview).
   * **SKU:** Choose the appropriate SKU (standard or confidential containers; this example uses standard).

3. **Select Your Container Image:**\
   Use a preconfigured image like Hello World, or pull an image from Azure Container Registry, Docker Hub, or another registry. For this walkthrough, select the NGINX image.

4. **Set Container Sizing and Advanced Options:**\
   Determine the container size and configure additional settings, like enabling GPU support if necessary.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a container instance, with fields for subscription, resource group, container details, and image selection.](https://kodekloud.com/kk-media/image/upload/v1752884747/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Container-Instances/azure-portal-container-instance-creation.jpg)
</Frame>

5. **Configure Networking Options:**
   * Decide on the networking type (public, private, or none).
   * Optionally set a DNS label and specify open port numbers.
   * Adjust the container restart policy based on your requirements.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a container instance, specifically on the "Networking" tab, where options for networking type, DNS name label, and port settings are being configured.](https://kodekloud.com/kk-media/image/upload/v1752884748/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Container-Instances/azure-portal-container-networking.jpg)
</Frame>

6. **Override Commands (Optional):**\
   If necessary, customize startup commands or scripts to run when the container launches.

7. **Review and Create:**\
   Verify your settings and click **Review and Create**. Once validation is complete, click **Create** to deploy your container. Deployments typically complete within 15 to 20 seconds.

8. **Access the Container Instance:**\
   When the deployment finishes, select **Go to resource**. You'll find details of your container instance, including its public IP address for direct access. For example, visiting the NGINX welcome page confirms the container is running smoothly.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a container instance named "aci-web-01," including its status, location, and resource usage metrics like CPU and memory.](https://kodekloud.com/kk-media/image/upload/v1752884749/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Container-Instances/azure-portal-aci-web-01-details.jpg)
</Frame>

9. **Interact with the Container:**\
   Review logs and connect to your container using the integrated terminal. For example, you can navigate directories within a running NGINX container as shown below:

```bash theme={null}
# cd /usr/
/usr # ls
bin  lib  local  sbin  share  src
/usr # cd share
/usr/share # ls
nginx  perl5  terminfo
/usr/share # cd
```

<Callout icon="lightbulb" color="#1CB2FE">
  While modifying files (e.g., index.html) is acceptable for demonstration purposes, container updates in production environments are typically managed through image updates and redeployments rather than direct SSH modifications.
</Callout>

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a container instance named "aci-web-01," with options to connect and choose a startup command.](https://kodekloud.com/kk-media/image/upload/v1752884750/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Container-Instances/azure-portal-aci-web-01.jpg)
</Frame>

## Conclusion

Azure Container Instances streamline the deployment of containerized applications by removing the need to manage underlying virtual machines. With benefits such as rapid startup times, scalability, secure isolation, and integrated networking and storage, ACI is a robust platform for running modern applications in the cloud.

Up next, we will delve into container groups and advanced configurations within Azure Container Instances.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/4dd57403-a848-419f-b23c-299e984c5f13" />
</CardGroup>

---


## Lesson 9: Container Groups

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Container-Groups/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Container-Groups/page.md)

**Summary:** Container groups in Azure enable unified deployment and management of multiple containers as a single entity, enhancing resource utilization and communication in applications.

# Container Groups

> Container groups in Azure enable unified deployment and management of multiple containers as a single entity, enhancing resource utilization and communication in applications.

Container groups in Azure offer a unified approach to deploying and managing multiple containers as a single entity. They are especially beneficial when running sidecar containers alongside a main application or grouping multiple containers that form a logical unit of your application.

For instance, imagine a Platform as a Service (PaaS) architecture where the underlying container host is abstracted away. When you create an Azure Container Instance, Azure automatically assigns it to a container host—without requiring direct user interaction with the host. In a typical scenario, two container instances might be used: one container connects to Azure Storage for persistent storage and exposes the web application to the internet, while a second container opens port 1433 internally to facilitate communication with the web server. Together, these containers function as a cohesive unit, illustrating the fundamental concept behind container groups.

<Callout icon="lightbulb" color="#1CB2FE">
  Container groups cannot be created directly from the Azure portal. Instead, you must use the Azure CLI, Resource Manager templates, or a YAML file to deploy them. When you use these methods, a unique group ID is generated for the container group, and you can add additional containers to this group to make them operate as a single logical unit.
</Callout>

## Deployment Options

Container groups provide flexible deployment options, allowing you to deploy either a single container or multiple containers that must work together. When deploying a container group, you define the total amount of CPU and memory, which are then allocated proportionately among the containers. This ensures efficient resource utilization and smooth operation across the group.

An important aspect of container groups is their shared network namespace. All containers within a container group receive IPs from a virtual network and can communicate seamlessly over private IP addresses. This shared networking capability is especially useful in microservices architectures where different services within the same application need to interact with low latency. It simplifies resource management and streamlines the overall deployment process.

<Frame>
  ![The image illustrates the concept of container groups, showing how containers share resources, lifecycle, local network, and storage volumes on a container host. It includes elements like DNS, deployment options, resource allocation, and shared networking.](https://kodekloud.com/kk-media/image/upload/v1752884770/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Container-Groups/container-groups-resource-sharing-diagram.jpg)
</Frame>

Now that you have a comprehensive understanding of container groups, it's important to note the emergence of a new service: container apps. Building on the principles of container groups, container apps offer additional capabilities and further simplify the deployment of containerized applications.

For more detailed insights on Azure services, consider exploring the [Azure Documentation](https://docs.microsoft.com/en-us/azure/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/044836a8-0a33-4f7a-ae26-bf38511f847e" />
</CardGroup>

---


## Lesson 10: Manage Containers with Azure Container Apps

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Manage-Containers-with-Azure-Container-Apps/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-PaaS-Compute-Options/Manage-Containers-with-Azure-Container-Apps/page.md)

**Summary:** This article explains how to manage and deploy containerized applications using Azure Container Apps in a serverless environment.

# Manage Containers with Azure Container Apps

> This article explains how to manage and deploy containerized applications using Azure Container Apps in a serverless environment.

Azure Container Apps provide a serverless hosting environment that simplifies running containerized applications without the burden of managing underlying infrastructure. They offer a streamlined alternative to Azure Kubernetes Service (AKS) by enabling partial orchestration for microservices instead of full orchestration. This setup is particularly effective when each container operates as a distinct component within a larger application architecture.

For example, one container might be dedicated to data ingestion (the ingestion service), another to processing that data (the delivery service), and a third to packaging processed data for consumption (the packaging service). This modular approach demonstrates how microservices can be effectively managed within an Azure Container Apps environment, where each service is isolated in its own container for optimal performance and scalability.

Integration with the Azure Container Registry is straightforward. A DevOps pipeline can build container images, push them to the registry, and trigger deployments seamlessly. In this context, Azure Container Instances (ACI) serve as the building blocks of container apps. While ACI provides rapid scalability for single containers, Azure Container Apps excel when orchestrating multiple containers as a grouped service.

<Callout icon="lightbulb" color="#1CB2FE">
  Azure Container Apps reduce deployment complexity and streamline scaling operations, enabling developers to focus on application logic rather than managing intricate Kubernetes configurations.
</Callout>

<Frame>
  ![The image illustrates the management of containers using Azure Container Apps, highlighting its integration with Azure Container Registry and its role as an alternative to Azure Kubernetes Service. It also shows a diagram of the Azure Container Apps environment with components like Ingestion, Delivery, and Package Services.](https://kodekloud.com/kk-media/image/upload/v1752884783/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Manage-Containers-with-Azure-Container-Apps/azure-container-apps-management-diagram.jpg)
</Frame>

## Deploying Azure Container Apps via the Azure Portal

Follow these steps to deploy Azure Container Apps using the Azure Portal:

1. Open the Azure Portal and search for "Container Apps." Click on the "Create" option.
2. Choose your subscription and select an existing resource group or create a new one.
3. Provide a name for your container app (e.g., "demo-app").
4. Select the appropriate Container Apps environment where your apps will run. You can create a new environment by clicking on "Create new" and configuring options such as workload profiles (consumption or dedicated plans), redundancy, and networking (either your own network or a Microsoft-provided network).

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a Container Apps Environment, with options for setting the environment name, type, and zone redundancy.](https://kodekloud.com/kk-media/image/upload/v1752884785/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Manage-Containers-with-Azure-Container-Apps/azure-portal-container-apps-environment.jpg)
</Frame>

5. In the container settings, select a quickstart image for convenience. In this example, a simple "Hello World" container is chosen with HTTP traffic enabled on port 80.
6. Click on "Review + Create" to validate your settings. Once validation passes, proceed with creating the Azure Container App.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a container app, with options for selecting a quickstart image, resource allocation, and application ingress settings.](https://kodekloud.com/kk-media/image/upload/v1752884786/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Manage-Containers-with-Azure-Container-Apps/azure-portal-container-app-creation.jpg)
</Frame>

After deployment, click "Go to resource" to view your demo app. A URL will be displayed for accessing the deployed application, allowing you to verify the deployment.

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a container app, displaying project details and container settings such as region, environment, and resource specifications.](https://kodekloud.com/kk-media/image/upload/v1752884787/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Manage-Containers-with-Azure-Container-Apps/azure-portal-container-app-settings.jpg)
</Frame>

Within the demo app resource, additional options include:

* Adding more containers for further orchestration.
* Configuring scaling, specifying replica counts, and enabling continuous deployment.
* Setting up a custom domain, integrating Dapr, or using service connectors for enhanced customization.

This guide has walked you through the deployment process and key configuration options for Azure Container Apps. By leveraging these features, managing and scaling containerized applications becomes more accessible, significantly reducing the complexity associated with traditional Kubernetes deployments.

Next, we will discuss data protection.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/c1871647-c1ec-478a-beab-b21781cec58f/lesson/80e5e07f-f919-4238-a74d-55dd4c316d46" />
</CardGroup>

---


# Section 11: Administer Data Protection

---


## Lesson 1: Module introduction

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Module-introduction/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Module-introduction/page.md)

**Summary:** This article explores objectives for securing and recovering data in Azure, focusing on Azure Backup Solution and Azure Site Recovery for robust data protection.

# Module introduction

> This article explores objectives for securing and recovering data in Azure, focusing on Azure Backup Solution and Azure Site Recovery for robust data protection.

In this article, we explore the essential objectives for ensuring your data is both secure and recoverable in Azure. Our focus begins with the powerful Azure Backup Solution, designed to safeguard your files, folders, and complete virtual machines from data loss caused by accidental deletions or cyberattacks.

<Callout icon="lightbulb" color="#1CB2FE">
  The Azure Backup Solution provides robust mechanisms to preserve your data. You will learn how to set up backups for individual files and folders, ensuring seamless data preservation and quick recovery. Key features such as redundancy and soft-delete are managed through the Azure Recovery Services Vault, which plays a pivotal role in overseeing and executing backup and recovery processes.
</Callout>

Additionally, the guide covers the protection of entire virtual machines (VMs). By following the outlined steps, you can secure your VM environments and ensure rapid restoration in case of any failures.

Our discussion also includes an in-depth look at Azure Site Recovery—a disaster recovery service that replicates your virtual machines to a secondary region. This replication allows you to run your VMs in an alternate location, ensuring business continuity even when unforeseen issues arise.

With this comprehensive overview of Azure data protection strategies, let's embark on a journey that begins with mastering the Azure Backup Solution, setting the stage for resilient and recoverable infrastructures in the cloud.

For further insights on Azure data protection, consider exploring related topics such as [Azure Disaster Recovery](https://azure.microsoft.com/en-us/services/site-recovery/) and [Azure Backup Best Practices](https://docs.microsoft.com/en-us/azure/backup/backup-best-practices).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/a25ecd10-20ce-4ff9-bcc1-386c2e018b09/lesson/5fd7881a-4db2-41e7-b8eb-1884aa21d099" />
</CardGroup>

---


## Lesson 2: Azure Backup

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Azure-Backup/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Azure-Backup/page.md)

**Summary:** Azure Backup is a Microsoft service that simplifies cloud data backup and restoration with automatic storage management and various storage options for compliance and continuity.

# Azure Backup

> Azure Backup is a Microsoft service that simplifies cloud data backup and restoration with automatic storage management and various storage options for compliance and continuity.

Azure Backup is a native Microsoft Azure service that simplifies the process of backing up and restoring your data in the cloud. With automatic storage management that scales with your data, it minimizes the need for manual interventions while optimizing costs.

Azure Backup supports several storage options, including Locally Redundant Storage (LRS), Geo-Redundant Storage (GRS), and Zone-Redundant Storage (ZRS). This flexibility helps you meet diverse compliance and business continuity requirements. Best of all, there are no transfer fees for backup data or restored content.

<Callout icon="lightbulb" color="#1CB2FE">
  Data security is a top priority. Azure Backup encrypts data both in transit and at rest and supports application-consistent backups. This ensures that even running applications remain uninterrupted during the backup process while preserving data integrity. Additionally, configurable retention policies let you store backups for as long as needed to satisfy regulatory and organizational demands.
</Callout>

One of the standout benefits of Azure Backup is its versatility. Whether you need to back up files, folders, or entire computers—whether they're hosted on-premises, in AWS, GCP, or on Azure—the service securely stores your data in the cloud.

<Frame>
  ![The image outlines the benefits of Azure Backup, highlighting features like automatic storage management, multiple storage options, unlimited data transfer, data encryption, application-consistent backup, and long-term retention. It also shows a flowchart for backing up files, folders, and computers.](https://kodekloud.com/kk-media/image/upload/v1752884459/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Backup/azure-backup-benefits-flowchart.jpg)
</Frame>

The backup process is designed to accommodate different environments and resource types. Whether you are protecting files, folders, or computers, each is seamlessly integrated into the Azure Backup Service.

## Data Sources

Azure Backup is capable of handling a wide range of data sources. Here's a breakdown of supported workloads:

### Azure Workloads

* **Virtual Machines:** Protect your Azure VMs.
* **Azure Files Shares:** Back up file shares stored on Azure.
* **SQL VMs:** Ensure the integrity of your SQL Virtual Machines.
* **SAP HANA on Azure VMs:** Secure your SAP HANA environments.

### On-Premises and Other Environments

* **Files and Folders:** Safeguard critical documents and directories.
* **Hyper-V Virtual Machines:** Manage backups for Hyper-V VMs.
* **VMware Virtual Machines:** Integrate VMware environment backups.
* **SQL Server:** Protect your SQL Server databases.
* **SharePoint:** Ensure SharePoint data consistency.
* **Exchange:** Back up your Exchange server data.
* **System State:** Preserve essential system configuration.
* **Bare Metal Recovery:** Support comprehensive system restores.

<Frame>
  ![The image shows two sections for selecting data sources for backup: "Azure Workloads" with options like Virtual Machine and Azure FileShare, and "On-Premises Workloads" with options like Files and Folders and Hyper-V Virtual Machines.](https://kodekloud.com/kk-media/image/upload/v1752884460/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Backup/data-sources-backup-azure-on-premises.jpg)
</Frame>

Multiple data sources can be seamlessly integrated into Azure Backup. In the following sections, you will learn how to back up file shares from on-premises environments and virtual machines in the cloud.

The next section introduces the Azure Backup Center, where you can manage and monitor your backup processes effectively.

<Callout icon="triangle-alert" color="#FF6B6B">
  Before proceeding, ensure that your backup policies align with your organization's compliance and retention requirements. This proactive check can help prevent potential data governance issues later on.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/a25ecd10-20ce-4ff9-bcc1-386c2e018b09/lesson/910718fa-1df8-4439-a964-2e5b237e76d1" />
</CardGroup>

---


## Lesson 3: Azure Backup Center

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Azure-Backup-Center/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Azure-Backup-Center/page.md)

**Summary:** Azure Backup Center provides integrated management for overseeing backup operations across hybrid and cloud environments.

# Azure Backup Center

> Azure Backup Center provides integrated management for overseeing backup operations across hybrid and cloud environments.

Azure Backup Center offers an integrated management experience that enables enterprises to oversee their backup estate across hybrid and cloud environments with ease. Acting as a single pane of glass, it simplifies the monitoring and control of backup operations across distributed Azure and non-Azure assets.

Azure Backup Center emphasizes data source–centric management, allowing administrators to apply tailored tools and policies based on the specific type of data—whether it's virtual machines, databases, or file shares. This granular approach ensures that backup operations are optimized for each unique data source.

Furthermore, Azure Backup Center seamlessly integrates with other Azure services. These native integrations enable advanced functionalities such as automated backup scheduling, policy enforcement, and compliance reporting. As a result, managing large-scale backup operations becomes more streamlined and efficient.

<Callout icon="lightbulb" color="#1CB2FE">
  Azure Backup Center is free to use. Simply navigate to the Azure portal and search for "Backup Center." If no backup operations are configured, you may initially see an empty dashboard. Once you complete demos for file and folder backup as well as VM backup, the dashboard will populate with the relevant data.
</Callout>

On that note, let's begin by exploring file and folder backup.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/a25ecd10-20ce-4ff9-bcc1-386c2e018b09/lesson/eb29cde8-f318-4eb1-9955-7cd28b41060e" />
</CardGroup>

---


## Lesson 4: File and Folder Backup

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/File-and-Folder-Backup/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/File-and-Folder-Backup/page.md)

**Summary:** This guide explains how to back up files and folders using Azure Backup for both on-premises systems and Azure File Shares.

# File and Folder Backup

> This guide explains how to back up files and folders using Azure Backup for both on-premises systems and Azure File Shares.

In this guide, you will learn how to back up files and folders from both on-premises systems and Azure File Shares using Azure Backup. The process involves deploying an Azure Recovery Services Vault to securely store your data. The vault leverages managed Azure storage along with robust backup functionalities.

## Overview

Azure Backup offers native integration with Azure Files for seamless file share protection. For on-premises Windows servers, the Microsoft Azure Recovery Services (MARS) Agent is required to replicate your data to the Recovery Services Vault.

The guide is divided into two main sections:

* Backing up Azure File Shares using the Azure portal
* Backing up on-premises files and folders using the MARS Agent on a Hyper-V machine

***

## Setting Up Azure File Share Backup

### Creating a Storage Account and File Share

1. In the Azure portal, navigate to **Storage Accounts** and create a new account. Select your subscription and create a new resource group.
2. Provide a distinctive name for the storage account (for example, "RSV Demo"), and choose the appropriate options (e.g., Standard, LRS advanced). Click **Review + Create** and proceed after validation.
3. After the storage account is deployed, configure a file share within it.

You can then upload files directly via the Azure portal:

* **Image:**

<Frame>
  ![The image shows a Microsoft Azure interface for creating a new file share with backup options enabled, including settings for a recovery services vault, resource group, and backup policy.](https://kodekloud.com/kk-media/image/upload/v1752884502/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-file-share-backup-settings.jpg)
</Frame>

After creating the file share, click on **Browse** and upload your files.

* **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal interface with a file upload section on the right, displaying a list of uploaded image files.](https://kodekloud.com/kk-media/image/upload/v1752884503/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-file-upload-interface.jpg)
</Frame>

### Configuring the Recovery Services Vault

1. In the Azure portal, go to **Recovery Services Vaults** and create a new vault. Use an existing resource group or create a new one (for example, RG Data Protection), assign a name such as "RSV01", and select your preferred region (e.g., East US).

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal interface with a search for "recovery services," displaying various services, marketplace options, and documentation related to recovery and backup.](https://kodekloud.com/kk-media/image/upload/v1752884504/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-recovery-services-search.jpg)
</Frame>

2. If a private endpoint is not required, skip its configuration by clicking **Review endpoint** and then **Review and Create**.

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal page for creating a Recovery Services vault, with details like subscription, resource group, and region specified. A cursor is hovering over the "Create" button.](https://kodekloud.com/kk-media/image/upload/v1752884506/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-recovery-services-vault-creation.jpg)
</Frame>

After the vault is deployed, register your file share for backup:

1. In the Recovery Services Vault, select **Backup**, specify that your workload runs in Azure, and choose **File Share** as the backup option.
2. Select the target storage account and file share from the list. Optionally, you can enable a lock on the storage account to prevent accidental deletion.
3. Complete the registration process by setting your backup policy details such as frequency and retention period.

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal interface for configuring a backup policy for an Azure File Share. It includes options for setting the backup schedule, frequency, and retention range.](https://kodekloud.com/kk-media/image/upload/v1752884507/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-backup-policy-interface.jpg)
</Frame>

Click **Enable Backup** to start protecting your file share. Once enabled, you can view the backup items in your Recovery Services Vault:

* **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying backup items in a Recovery Services vault, with a list of backup management types and their item counts.](https://kodekloud.com/kk-media/image/upload/v1752884508/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-backup-items-vault.jpg)
</Frame>

If you see a warning such as "Initial Backup Pending", trigger the backup manually by clicking **Back Up Now** within the backup item details.

* **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal page displaying backup items for Azure Storage (Azure Files). It lists details such as the name, storage account, resource group, and backup status, with a warning indicating an initial backup is pending.](https://kodekloud.com/kk-media/image/upload/v1752884509/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-backup-items-storage.jpg)
</Frame>

Once the backup status changes to "Success", you can simulate a restore process by deleting some files from the file share.

* **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal page displaying backup details for an Azure file share named "rsvdemo." It includes information about the backup status, subscription, and storage account, with a warning indicating that the initial backup is pending.](https://kodekloud.com/kk-media/image/upload/v1752884510/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-backup-rsvdemo-details.jpg)
</Frame>

Next, navigate back to the file share, delete some files, and then restore them from the Recovery Services Vault by choosing the **File Recovery** option. Select an appropriate restore point (if multiple exist), and pick the individual files you need. In case of conflicts, options to skip or override are provided.

* **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal interface for restoring files, with options to select a restore point, destination, and conflict resolution. Two files, "City2.jpg" and "City1.jpg," are listed for recovery.](https://kodekloud.com/kk-media/image/upload/v1752884512/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-file-restore-options.jpg)
</Frame>

After the restore process, you will see the recovered files back in your file share.

***

## On-Premises Files and Folders Backup

To back up on-premises files and folders, you need to install the MARS Agent. This section explains how to configure your on-premises environment and register it with the Recovery Services Vault.

### Preparing the Infrastructure

1. In the Azure portal under the backup section for on-premises, select **Files and Folders** and click **Prepare Infrastructure**. This action provides download links for the MARS Agent and the vault credentials.

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal page with instructions for preparing infrastructure using the Recovery Services Agent. It includes steps for installing the agent, downloading vault credentials, scheduling backups, and configuring notifications.](https://kodekloud.com/kk-media/image/upload/v1752884513/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-recovery-services-agent.jpg)
</Frame>

2. Download both the MARS Agent installer and the vault credentials file (an XML text file) and copy them to your on-premises Windows Server or Hyper-V machine.

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal page with instructions for preparing infrastructure, alongside a Windows Server Manager dashboard window. The Server Manager window includes a prompt about managing servers with Windows Admin Center.](https://kodekloud.com/kk-media/image/upload/v1752884514/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-windows-server-manager.jpg)
</Frame>

### Installing and Registering the MARS Agent

1. Execute the MARS Agent installer on your server. During installation, configure the cache location and any necessary proxy settings if using a private network connection.

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal with a virtual machine connection open, displaying the Microsoft Azure Recovery Services Agent Setup Wizard in the Server Manager Dashboard. The setup wizard is at the "Installation Settings" stage, where installation and cache locations are being configured.](https://kodekloud.com/kk-media/image/upload/v1752884515/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-virtual-machine-setup.jpg)
</Frame>

2. When prompted, load the downloaded vault credentials file. This file links your server to the Recovery Services Vault. An example vault credentials file is shown below:

```xml theme={null}
<?xml version="1.0" encoding="utf-8"?>
<RBackupVaultAADCreds xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/Microsoft.Azure.Portal.RecoveryServices.Models.Common">
  <Version>2.0</Version>
  <SubscriptionId>2cda1881-8c1e-4c15-be23-9aegTyfo9o1e41T5XhR</SubscriptionId>
  <ResourceType>Vaults</ResourceType>
  <ResourceName>rsv-01</ResourceName>
  <ManagementCert>MIIBIjANBgkqhkiG9w0B...</ManagementCert>
</RBackupVaultAADCreds>
```

3. The wizard will then request you to input a password for backup encryption (a minimum of 16 characters). It is recommended to store this password securely for recovery purposes.

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal with a Server Manager window open, displaying the "Encryption Setting" section of the Register Server Wizard. It includes options for entering and confirming a passphrase for data backup encryption.](https://kodekloud.com/kk-media/image/upload/v1752884517/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-portal-server-manager-encryption.jpg)
</Frame>

Once registration is complete, the MARS Agent appears in the **All Programs** list as **Azure Backup**.

### Scheduling and Running Backups

1. Open the Azure Backup console on your server and choose the files and folders you wish to protect. For example, you might want to back up data from `C:\Users\Administrator\Documents`.
2. Configure your preferred backup schedule (up to three times per day) and define the retention period.

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure interface with a "Schedule Backup Wizard" window open, where a backup schedule is being specified for files and folders.](https://kodekloud.com/kk-media/image/upload/v1752884518/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-schedule-backup-wizard.jpg)
</Frame>

3. For the initial backup, select whether to transfer data online or offline. For larger datasets, options such as using a Data Box or physical disk are available, whereas online transfers are typically sufficient for smaller volumes.

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure interface with a "Schedule Backup Wizard" window open, where the user is selecting an initial backup type for files and folders, with options for online and offline transfers.](https://kodekloud.com/kk-media/image/upload/v1752884519/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-schedule-backup-wizard-interface.jpg)
</Frame>

After scheduling, the backup process starts automatically. You can also trigger an immediate backup if necessary. In cases where a backup job fails (for instance, due to temporary network issues), you can restart the process from the MARS Agent console.

* **Image:**

<Frame>
  ![The image shows a Microsoft Azure Backup interface with a list of backup jobs, one completed and one failed, along with options for managing backups. The background displays a web page for preparing infrastructure in Azure.](https://kodekloud.com/kk-media/image/upload/v1752884520/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-backup-interface-jobs-management.jpg)
</Frame>

***

## Restoring Files and Folders from an On-Premises Backup

1. Open the Azure Backup console and select **Recover Data**.

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure Backup interface with a "Recover Data Wizard" window open, guiding the user through the process of recovering files from a backup service.](https://kodekloud.com/kk-media/image/upload/v1752884522/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-backup-recover-data-wizard.jpg)
</Frame>

2. Choose the server and specify the recovery location (typically the primary region). Select your desired recovery mode (individual files and folders, volume, or system state), then choose the appropriate volume (e.g., C:) and the date that corresponds to the desired recovery point.
3. Mount the recovery point. It will appear as a temporary drive on your system, allowing you up to six hours (extendable up to seven days if necessary) to copy the data back to its original location.

   * **Image:**

<Frame>
  ![The image shows a Microsoft Azure Backup interface with a recovery process in progress, displaying recovery details and options to browse or unmount the recovery volume.](https://kodekloud.com/kk-media/image/upload/v1752884523/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-backup-recovery-interface.jpg)
</Frame>

After verifying and copying over the recovered files, unmount the temporary recovery volume. Detailed backup history and recovery points can be reviewed within the Recovery Services Vault.

* **Image:**

<Frame>
  ![The image shows a Microsoft Azure portal page displaying backup details for a computer named "win-bkbran4psd9," with a successful last backup status and one recovery point.](https://kodekloud.com/kk-media/image/upload/v1752884524/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-File-and-Folder-Backup/azure-backup-details-win-bkbran4psd9.jpg)
</Frame>

***

## Conclusion

In this article, we demonstrated how to protect your data using Azure Backup for both Azure File Shares and on-premises files and folders. By setting up a Recovery Services Vault and configuring appropriate backup policies, you can ensure your critical data is securely stored and can be restored when needed.

<Callout icon="lightbulb" color="#1CB2FE">
  Azure Backup not only handles files and folders but can also be applied to virtual machines, making it an essential component in a comprehensive data protection strategy.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/a25ecd10-20ce-4ff9-bcc1-386c2e018b09/lesson/87dfcc3b-38b6-4d82-b5ba-7512ca5f5a94" />
</CardGroup>

---


## Lesson 5: Configuring backup Azure VM

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Configuring-backup-Azure-VM/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Configuring-backup-Azure-VM/page.md)

**Summary:** This guide explains configuring and managing backups for Azure virtual machines using the Azure Backup service.

# Configuring backup Azure VM

> This guide explains configuring and managing backups for Azure virtual machines using the Azure Backup service.

This guide explains how to configure and manage backups for Azure virtual machines (VMs) using the Azure Backup service. The service automatically deploys a backup extension on your VM (if not already installed) to orchestrate consistent backup operations. This extension coordinates snapshot creation for your VM’s managed disks. For application-consistent backups, it interacts with the Volume Shadow Copy Service (VSS) on Windows VMs or runs user-defined post scripts on Linux VMs. In doing so, it ensures that in-flight transactions and caches are fully flushed to disk before taking a snapshot.

During backup configuration, you define policies that set the backup frequency, retention periods (daily, weekly, monthly, and yearly), and establish instant restore points. For instance, you might schedule a daily backup at 7 a.m., retain that backup for 30 days, and configure additional weekly or monthly backups as needed to meet your recovery objectives.

At the scheduled backup time, the Azure Backup service sends a request to the backup extension to start the process. The extension creates a snapshot of the VM’s attached managed disk. This snapshot—representing the VM’s current state—is transferred incrementally to the Recovery Services vault over encrypted HTTPS connections. If the VM uses Azure Disk Encryption, the encryption key is also exported to assist with future restore operations.

<Frame>
  ![The image is a diagram illustrating the process of virtual machine backup for Azure VMs, showing components like managed disks, instant recovery snapshots, and Azure Backup Service with backup policy management and recovery services vault.](https://kodekloud.com/kk-media/image/upload/v1752884482/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-vm-backup-diagram.jpg)
</Frame>

***

## Creating a Backup for an Azure VM

To create a backup for your Azure VM, follow these steps:

1. **Access Your Virtual Machine:**
   * Open the Azure portal and navigate to the Virtual Machines section.
   * In this demonstration, we are using a VM named "RSV Demo 1," which is running a web server. Although the web server is accessible via its public IP, the focus here is solely on backup configuration.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a virtual machine named "rsv-demo-1," including its status, location, operating system, and network information.](https://kodekloud.com/kk-media/image/upload/v1752884483/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-virtual-machine-rsv-demo-1.jpg)
</Frame>

2. **Select or Create a Recovery Services Vault:**
   Before enabling backup, create or choose an existing Recovery Services vault. This vault acts as the centralized storage location for your backup data. In this example, we use a previously created vault used for file and folder backups, a method that is especially beneficial when managing backups for multiple VMs.

<Frame>
  ![The image shows a Microsoft Azure portal interface for managing Recovery Services vaults, with options for backup and site recovery. It includes a list of features and updates related to Azure VMs and databases.](https://kodekloud.com/kk-media/image/upload/v1752884484/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-recovery-services-vaults.jpg)
</Frame>

3. **Set Up Your Backup Goal:**
   * With the vault selected, set your backup goal by clicking on "Backup."
   * From the options provided (such as once-a-day backups with different operational tiers and enhanced modes), choose the one that fits your scenario—in this demonstration, the standard mode is used.

<Frame>
  ![The image shows a Microsoft Azure portal page for setting a backup goal, with options to select where the workload is running and what to back up, such as a virtual machine.](https://kodekloud.com/kk-media/image/upload/v1752884485/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-backup-goal-setup.jpg)
</Frame>

***

## Configuring the Backup Policy

### 1. Policy Settings

* Create a new policy (e.g., "VM Backup Policy") or modify the default policy.
* Set the backup frequency (e.g., daily at 4 a.m. with support for your local time zone).
* Define instant restore points (snapshot retention) and specify a retention period (the default might be two days).
* Configure retention for weekly, monthly, and yearly backups, determining both the scheduled backup day and the retention duration.

### 2. Assigning VMs to the Policy

* After configuring your policy, click **OK** to save it.
* Add the desired VMs to the policy. The portal will list all VMs in the selected region, allowing you to choose which ones to back up.

<Frame>
  ![The image shows a Microsoft Azure portal interface for configuring a backup policy for virtual machines. It includes options for backup frequency, instant restore, and retention settings, with a virtual machine selected for backup.](https://kodekloud.com/kk-media/image/upload/v1752884487/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-backup-policy-configuration.jpg)
</Frame>

### 3. Enabling Backup

* Validate your configuration. The system checks if the backup extension can be installed on the selected VMs.
* Once validated, click on "Enable Backup" to install the backup extension, which will handle ongoing backup operations.
* The deployment details displayed in the portal will confirm the addition of the backup extension to your VM.

<Frame>
  ![The image shows a Microsoft Azure portal screen with a deployment in progress for configuring protection, including details about resources and operation status. The right panel displays operation details such as provisioning state, timestamp, and tracking ID.](https://kodekloud.com/kk-media/image/upload/v1752884488/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-deployment-progress.jpg)
</Frame>

***

## Initiating the First Backup

Once backup is enabled, initiate the first backup operation as follows:

1. Open the Recovery Services vault resource.
2. Under the Backup Items section, locate your virtual machine (for example, "VM1").
3. Click on "View Details" and then start the first backup.

This initial backup creates a restore point that you can later use either to restore the entire VM or to recover specific files.

<Frame>
  ![The image shows a Microsoft Azure portal interface for a backup item named "rsv-demo-1," displaying backup status, recovery points, and related details. The backup pre-check is passed, but the last backup status shows a warning for an initial backup pending.](https://kodekloud.com/kk-media/image/upload/v1752884490/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-backup-rsv-demo-1.jpg)
</Frame>

Monitor the backup process using the job details:

<Frame>
  ![The image shows a Microsoft Azure portal page displaying backup job details, including workload names, operations, statuses, types, start times, and durations.](https://kodekloud.com/kk-media/image/upload/v1752884491/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-backup-job-details.jpg)
</Frame>

When the extension creates the snapshot, the data is securely transferred to the Recovery Services vault. Refresh the page to confirm that backup completion is successful—the most recent restore point should indicate a recently completed backup.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying backup details for a virtual machine, including backup status, recovery points, and backup policy information.](https://kodekloud.com/kk-media/image/upload/v1752884492/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-backup-details-vm.jpg)
</Frame>

***

## Restore Options

Azure Backup offers two primary restoration methods:

### 1. File Recovery

Use this option to restore individual files:

* Select the desired restore point.
* Download the file recovery executable.
* Run the executable to mount a recovery disk and extract the required files.

<Frame>
  ![The image shows a Microsoft Azure File Recovery interface, where a user can select a restore point, download an executable script for file recovery, and unmount disks after recovery.](https://kodekloud.com/kk-media/image/upload/v1752884493/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-file-recovery-interface.jpg)
</Frame>

### 2. Virtual Machine Restore

For full VM restoration, you have multiple options:

* Create a new virtual machine from the chosen restore point. This option is ideal for testing recovery without affecting your production environment.
* Restore the disk to recover from corruption or issues. In this case, specify the resource group and location for a staging account; the restored disk appears as a VHD file in your storage account.

Select a restore point and then decide whether to use "Create New" or "Restore Disk" based on your scenario.

<Frame>
  ![The image shows a Microsoft Azure portal interface for restoring a virtual machine, with options to select a restore point based on date and consistency type.](https://kodekloud.com/kk-media/image/upload/v1752884494/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-restore-virtual-machine.jpg)
</Frame>

If you have an existing disk backup and wish to replace the disk, choose the "Replace Existing" option.

<Frame>
  ![The image shows a Microsoft Azure portal interface for restoring a virtual machine, with options to create a new virtual machine or replace an existing one. Various configuration settings such as restore point, data store, and network options are available for selection.](https://kodekloud.com/kk-media/image/upload/v1752884495/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-restore-virtual-machine-2.jpg)
</Frame>

Additional restore details and options are available in the portal once the restore job is initiated.

<Frame>
  ![The image shows a Microsoft Azure portal interface for restoring a virtual machine, with options to select a restore point, data store, restore configuration, and other settings.](https://kodekloud.com/kk-media/image/upload/v1752884497/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-restore-virtual-machine-3.jpg)
</Frame>

Monitor the job status to determine when your new VM or restored disk is ready for use. You can later create a snapshot from the restored disk if needed.

<Frame>
  ![The image shows a Microsoft Azure portal interface for restoring a virtual machine. It includes options for selecting a restore point, data store, restore configuration, and other settings.](https://kodekloud.com/kk-media/image/upload/v1752884498/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-Azure-VM/azure-portal-restore-virtual-machine-4.jpg)
</Frame>

***

## Conclusion

In this guide, you learned how to configure Azure VM backups using the Recovery Services vault and the backup extension deployed on your VM. We covered setting up backup policies, initiating backup operations, and exploring restore options for both file-level and full VM recoveries.

<Callout icon="lightbulb" color="#1CB2FE">
  Up next, explore how to back up and restore on-premises virtual machines to expand your data protection strategy.
</Callout>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/a25ecd10-20ce-4ff9-bcc1-386c2e018b09/lesson/55f44e1c-8f80-4b97-b28e-cdfdc2693dc0" />
</CardGroup>

---


## Lesson 6: Configuring backup non Azure VM

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Configuring-backup-non-Azure-VM/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Configuring-backup-non-Azure-VM/page.md)

**Summary:** This article explains how to back up on-premises virtual machines to Azure using the Recovery Services Vault and associated tools.

# Configuring backup non Azure VM

> This article explains how to back up on-premises virtual machines to Azure using the Recovery Services Vault and associated tools.

In this article, we explain how to back up on-premises virtual machines (VMs) to Azure using the Recovery Services Vault. The Recovery Services Vault can store backups for various specialized workloads, including Exchange, SharePoint, and SQL Server, supporting both Linux and Windows VMs on Hyper-V, VMware, and even physical Windows Server machines.

When leveraging Azure, backups can be configured easily via the portal. For on-premises environments, however, you can utilize tools like Microsoft Azure Backup Server (MABS) and System Center Data Protection Manager (DPM). These tools bridge your on-premises environment with Azure by handling backup scheduling, retention policies, and securely transferring data to Azure over an HTTPS-encrypted connection.

<Frame>
  ![The image illustrates a process for backing up on-premises virtual machines, showing specialized workloads, virtual machines, and physical servers being backed up to a Recovery Services Vault via MABS or DPM.](https://kodekloud.com/kk-media/image/upload/v1752884499/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-non-Azure-VM/vm-backup-process-recovery-services.jpg)
</Frame>

When a backup is initiated, data is securely transmitted over the network to the Recovery Services Vault. In addition to the cloud backup, a local copy is maintained to facilitate rapid restore operations in case of issues. This dual backup strategy ensures low latency access on-premises while also providing a secure secondary copy in the cloud.

If you are using System Center Configuration Manager (SCCM), you have the option to configure backups with the DPM agent. The diagram below outlines the process for setting up the Azure Backup Server, including installation steps and downloading vault credentials:

<Frame>
  ![The image shows a Microsoft Azure portal page for preparing infrastructure, specifically for installing and configuring the Azure Backup Server. It includes steps for installation and downloading vault credentials.](https://kodekloud.com/kk-media/image/upload/v1752884500/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Configuring-backup-non-Azure-VM/azure-backup-server-setup-guide.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Once MABS is enabled, the data flows securely to the Recovery Services Vault, ensuring an efficient and safe backup process.
</Callout>

Due to limited on-premises resources, a live demonstration of this configuration is not provided. However, the outlined process reliably secures your backup data both locally and in the cloud.

This concludes the overview of configuring backup for non-Azure VMs. In the next section, we will compare MABS with MARS to help you determine the best solution for your backup strategy.

## Additional Resources

* [Azure Backup Documentation](https://learn.microsoft.com/azure/backup/)
* [Microsoft Azure Recovery Services Vault](https://learn.microsoft.com/azure/backup/backup-recovery-services-vault-overview)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/a25ecd10-20ce-4ff9-bcc1-386c2e018b09/lesson/842c051b-1a60-4a56-bca2-cb64a6948d7e" />
</CardGroup>

---


## Lesson 7: Compare Backup Options

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Compare-Backup-Options/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Compare-Backup-Options/page.md)

**Summary:** This article compares two on-premises backup strategies, MARS agent and backup server, to help determine the best solution for your backup needs.

# Compare Backup Options

> This article compares two on-premises backup strategies, MARS agent and backup server, to help determine the best solution for your backup needs.

In this lesson, we'll explore and compare two on-premises backup strategies: the MARS agent and the backup server (MABS). This comparison will help you determine which solution best meets your backup needs.

## Benefits

### MARS Agent

The MARS agent is ideal for users seeking a straightforward backup solution for Windows-based systems. Key advantages include:

* Backing up files and folders on both physical and virtual Windows environments without needing a dedicated backup server.
* Direct installation on the machine, allowing you to synchronize backups, delete backups, and restore data directly from the host.

### Backup Server (MABS)

MABS offers a more robust set of features for advanced backup scenarios. Its benefits include:

* Application-aware snapshots that ensure consistent backups of critical applications.
* Flexible backup scheduling combined with granular recovery options.
* Support for Linux on Hyper‑V and VMware environments.
* Operation without requiring a System Center license.

A complete evaluation of these options covers their components, benefits, limitations, the types of items they protect, and their backup storage mechanisms. See the comparison table below for a quick visual reference:

<Frame>
  ![The image is a comparison table of Azure Backup options, detailing components, benefits, limits, what they protect, and backup storage for Azure Backup (MARS) agent and Azure Backup Server (MABS).](https://kodekloud.com/kk-media/image/upload/v1752884480/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Compare-Backup-Options/azure-backup-options-comparison-table.jpg)
</Frame>

## Limitations

<Callout icon="lightbulb" color="#1CB2FE">
  Review the following limitations for each solution to ensure they align with your backup strategy.
</Callout>

### MARS Agent Limitations

* Backups are limited to three per day, matching the three time slots available in the Azure agent user interface.
* The agent is not application-aware and can only restore individual files, folders, or entire volumes.
* Linux environments are not supported.

### Backup Server (MABS) Limitations

* Oracle workloads cannot be backed up using MABS.
* Requires an active Azure subscription for operation.
* Tape backups are not supported.

## Protection Capabilities

The protection scope of each solution varies significantly:

* **MARS Agent:** Primarily designed to secure files and folders.
* **Backup Server (MABS):** Offers broader protection, securing files, folders, volumes, virtual machines, applications, and complete workloads.

## Storage Options

Both solutions utilize Recovery Services vaults, albeit with different storage strategies:

* **MARS Agent:** All backup data is stored exclusively in a Recovery Services vault.
* **Backup Server (MABS):** In addition to using the Recovery Services vault, MABS maintains a local backup copy. This local copy facilitates low-latency and rapid restores.

With these detailed insights, you now have a comprehensive understanding of how each backup option caters to different environments and requirements. Next, we'll delve into additional data protection methods, including the benefits of soft delete, to further enhance your backup strategy.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/a25ecd10-20ce-4ff9-bcc1-386c2e018b09/lesson/2c08d923-b216-4e80-bfa9-bf822eddb3f0" />
</CardGroup>

---


## Lesson 8: Manage Soft Delete

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Manage-Soft-Delete/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Manage-Soft-Delete/page.md)

**Summary:** This article explains Azure Backups Soft Delete feature, its management, and configuration to enhance data protection against accidental loss.

# Manage Soft Delete

> This article explains Azure Backups Soft Delete feature, its management, and configuration to enhance data protection against accidental loss.

Azure Backup’s Soft Delete feature significantly enhances data protection by retaining deleted backup data for a defined grace period after a delete command is issued. This mechanism minimizes the risk of accidental data loss by placing your data in a soft-deleted state rather than removing it immediately. In this guide, we explain how soft delete works, how to manage backup deletion, and how to configure these settings within the Azure portal.

## Understanding Soft Delete

When your data is securely backed up in Azure, it remains protected even if you decide to stop the backup process later. Instead of being permanently removed right away, the data enters a soft-deleted state—similar to a pause—providing you with a window to verify or recover any unintentionally deleted data.

During this 14-day grace period, if you choose to stop the backup while retaining existing data, no new backups are created. However, your current backup data remains intact and available for restoration. If you later determine that the deletion should be final, you can execute a purge operation to permanently remove the data. Conversely, if you need to recover mistakenly deleted data, you can resume the backup, effectively restoring the soft-deleted backup as part of your backup strategy.

<Callout icon="lightbulb" color="#1CB2FE">
  While the default retention period is 14 days, you have the option to extend this period for an additional fee. This policy applies across all backup items protected within the Recovery Services vault, ensuring comprehensive data protection for both virtual machine backups and other workloads.
</Callout>

<Frame>
  ![The image is a flowchart illustrating the process of managing soft delete for backup items, including states like "Soft Deleted" and "Stop Backup with Retain Data," and actions such as undeleting within 14 days or permanently deleting data. It also includes notes on data retention and recovery features.](https://kodekloud.com/kk-media/image/upload/v1752884525/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Manage-Soft-Delete/soft-delete-backup-flowchart.jpg)
</Frame>

## Configuring Soft Delete in the Azure Portal

To configure the Soft Delete feature, follow these steps:

1. **Navigate to your Recovery Services Vault:**\
   Access the vault's properties from the Azure portal, where you'll find settings related to backup and site recovery.

2. **Access Security and Soft Delete Settings:**\
   Within the vault's properties, locate the "Security and soft delete settings" section. Here, you can enable the Soft Delete feature, adjust the retention period, and manage other related security options for both cloud and hybrid workloads.

3. **Adjust Settings as Needed:**\
   Customize the soft delete configuration to align with your organizational data protection and disaster recovery strategies.

<Frame>
  ![The image shows a Microsoft Azure portal interface focused on a Recovery Services vault, displaying options for backup and site recovery, along with a list of new features.](https://kodekloud.com/kk-media/image/upload/v1752884526/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Manage-Soft-Delete/azure-portal-recovery-services-vault.jpg)
</Frame>

<Frame>
  ![The image shows the Microsoft Azure portal with the "Security and soft delete settings" for a Recovery Services vault. It includes options for enabling soft delete for cloud and hybrid workloads, setting retention periods, and configuring other security settings.](https://kodekloud.com/kk-media/image/upload/v1752884527/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Manage-Soft-Delete/azure-portal-security-settings-recovery-vault.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  Integrating a robust backup management strategy with soft delete capabilities into your disaster recovery plan can greatly enhance your organization's resilience against data loss.
</Callout>

## Final Thoughts

By leveraging Azure Backup’s Soft Delete feature, you add an extra layer of protection to your data, ensuring that even after a delete command, your backup information remains recoverable for a limited time. Consider regularly reviewing and testing your recovery strategy to keep your data protection measures up-to-date and effective.

For further information, visit the official [Azure Backup documentation](https://docs.microsoft.com/en-us/azure/backup/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/a25ecd10-20ce-4ff9-bcc1-386c2e018b09/lesson/ad5de685-6644-45e5-b059-e705bfcf8346" />
</CardGroup>

---


## Lesson 9: Azure Site Recovery

**Source URL:** [https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Azure-Site-Recovery/page.md](https://notes.kodekloud.com/docs/Updated-AZ-104-Microsoft-Azure-Administrator/Administer-Data-Protection/Azure-Site-Recovery/page.md)

**Summary:** This article explains how to set up and test disaster recovery for virtual machines using Azure Site Recovery.

# Azure Site Recovery

> This article explains how to set up and test disaster recovery for virtual machines using Azure Site Recovery.

Azure Site Recovery (ASR) ensures uninterrupted business operations by replicating your virtual machine workloads to a secondary location in the event of a disaster. In this guide, you will learn how to set up disaster recovery for a single VM using ASR, along with how to perform a test failover to validate your configuration.

Consider a scenario where your primary source environment is in Region A. In this region, virtual machines operate within an availability set and use a virtual network (VNet). When these machines are enrolled in Azure Site Recovery, an extension is installed on each machine and a cache storage account is created in Region A to temporarily hold replication data. The target environment in Region B is configured with the necessary infrastructure components—including a VNet, subnet, and availability set.

Data is replicated from the source cache storage account to managed disks in Region B. During a primary site failure, new virtual machine instances are provisioned in the secondary region, and the replicated managed disks are attached. This ensures the machine continues to function in Region B with the complete data set from Region A.

<Frame>
  ![The image illustrates Azure Site Recovery, showing a failover process from a source environment (Region A) to a target environment (Region B) with virtual networks, availability sets, and disks.](https://kodekloud.com/kk-media/image/upload/v1752884461/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-site-recovery-failover-diagram.jpg)
</Frame>

<Callout icon="lightbulb" color="#1CB2FE">
  ASR not only facilitates disaster recovery but can also be automated using REST APIs, health metrics, and load balancing solutions such as [Azure Traffic Manager](https://azure.microsoft.com/en-us/services/traffic-manager/).
</Callout>

***

## Configuring Disaster Recovery via the Azure Portal

In this section, we walk through configuring disaster recovery for a virtual machine named "RSV Demo 1" running IIS on a Windows server.

1. **Access the Virtual Machine Details**

   Open the virtual machine details page in the Azure portal.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying details of a virtual machine named "rsv-demo-1," including its status, location, operating system, and IP address.](https://kodekloud.com/kk-media/image/upload/v1752884462/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-virtual-machine-rsv-demo-1.jpg)
</Frame>

2. **Initiate Disaster Recovery Setup**

   Click on the disaster recovery option. You can create a Recovery Services vault during this process. For this demonstration, review the disaster recovery map and settings.

<Frame>
  ![The image shows a Microsoft Azure portal interface for setting up disaster recovery for a virtual machine, with options for selecting a target region and a world map indicating regions.](https://kodekloud.com/kk-media/image/upload/v1752884463/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-disaster-recovery-portal.jpg)
</Frame>

3. **Select the Target Region**

   Choose a target region—for example, West US if the source is located in East US. In the advanced settings, Azure creates the necessary infrastructure (resource groups, virtual networks, and availability sets) in the target region. The target resource group may be annotated with an "ASR" suffix (e.g., "RG Backup RSV ASR").

<Frame>
  ![The image shows a Microsoft Azure portal interface for configuring disaster recovery settings for a virtual machine. It includes options for target settings, capacity reservation, and replication review.](https://kodekloud.com/kk-media/image/upload/v1752884465/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-disaster-recovery-settings.jpg)
</Frame>

4. **Review and Configure Replication Settings**

   Examine the storage options, replication settings, and extension management. Storage settings define the cache storage account. Replication options let you choose the recovery services vault, vault resource group, and replication policy. Extension settings manage the ASR extension on the virtual machine.

<Frame>
  ![The image shows a Microsoft Azure portal interface for configuring disaster recovery settings for a virtual machine. It includes options for churn settings, cache storage, replication settings, and extension settings.](https://kodekloud.com/kk-media/image/upload/v1752884466/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-disaster-recovery-settings-2.jpg)
</Frame>

5. **Start Replication**

   Click "Review and Start Replication" to see details such as the source disk, replica disk (configured as premium SSD), and cache storage account. Confirm by clicking "Start Replication" to trigger the creation of resources in West US. The replication of data to the target region will commence once the resources are provisioned.

After the replication process completes, you can monitor key metrics like the Recovery Point Objective (RPO), replication health, and details of the underlying infrastructure.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying an infrastructure view of a recovery services vault, with components like a virtual machine, cache storage account, Azure Site Recovery, and managed disks.](https://kodekloud.com/kk-media/image/upload/v1752884467/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-recovery-services-vault.jpg)
</Frame>

If you have not yet performed a test failover, continue to the next section.

***

## Performing a Test Failover

Conducting a test failover validates that your disaster recovery setup functions correctly without affecting your production environment.

1. **Initiate the Test Failover**

   In the Azure portal, select the test failover option.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying the status of a recovery services vault named "rsv-demo-1." It indicates the replication health as healthy, with no errors, but notes that a test failover has never been performed successfully.](https://kodekloud.com/kk-media/image/upload/v1752884468/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-recovery-vault-status.jpg)
</Frame>

2. **Configure Test Failover Settings**

   * Choose the source region (e.g., East US) and the destination (e.g., West US).
   * Select the appropriate recovery point; typically, the latest recovery point with application consistency is recommended.
   * Pick the ASR virtual network that was created during the initial setup.

3. **Provisioning a Temporary Virtual Machine**

   The test failover process creates a temporary virtual machine in the target region, attaching the relevant managed disk. To ensure connectivity, a public IP address must be available. Since this is not created automatically, you need to create a new public IP.

<Frame>
  ![The image shows a Microsoft Azure portal screen for creating a public IP address, with deployment details and notifications on the right side.](https://kodekloud.com/kk-media/image/upload/v1752884469/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-public-ip-creation.jpg)
</Frame>

Create a public IP (e.g., "RSVDRVMIP") in your ASR resource group and allow the test failover process to continue.

4. **Verify the Test VM Deployment**

   After the virtual machine starts, monitor its status in the virtual machines list.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying a list of virtual machines, including details like name, type, subscription, location, status, operating system, size, and public IP address.](https://kodekloud.com/kk-media/image/upload/v1752884471/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-virtual-machines-list.jpg)
</Frame>

5. **Set Up Network Connectivity**

   If no Network Security Group (NSG) is attached to the test VM, proceed as follows:

   * Create an NSG in the ASR resource group.
   * Add inbound security rules for required ports (e.g., TCP ports 80 and 3389).

<Frame>
  ![The image shows the Microsoft Azure portal displaying a list of network security groups. There are two entries listed: "about-rithin-vm-nsg" and "rsv-nsg."](https://kodekloud.com/kk-media/image/upload/v1752884472/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-network-security-groups.jpg)
</Frame>

Next, configure the inbound security rules.

<Frame>
  ![The image shows a Microsoft Azure portal interface for creating a network security group, with fields for project and instance details such as subscription, resource group, name, and region.](https://kodekloud.com/kk-media/image/upload/v1752884473/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-network-security-group.jpg)
</Frame>

Then add the inbound security rules.

<Frame>
  ![The image shows a Microsoft Azure portal interface for managing inbound security rules in a network security group, with a form open to add a new inbound security rule.](https://kodekloud.com/kk-media/image/upload/v1752884474/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-inbound-security-rules.jpg)
</Frame>

6. **Associate NSG and Public IP**

   * Associate the NSG with the DR subnet so that any VM in the subnet inherits the security rules.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying network security group settings, including a list of security rules with details like priority, name, port, protocol, source, destination, and action.](https://kodekloud.com/kk-media/image/upload/v1752884476/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-network-security-settings.jpg)
</Frame>

* Finally, associate the newly created public IP address with the test VM's network interface.

<Frame>
  ![The image shows a Microsoft Azure portal interface where a public IP address is being associated with a network interface. The interface displays details like resource group, location, and subscription information.](https://kodekloud.com/kk-media/image/upload/v1752884478/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-public-ip-association.jpg)
</Frame>

7. **Verify the Test Failover**

   Access the public IP address via a browser. If you see the IIS page (identical to production), the test failover is confirmed successful.

<Callout icon="lightbulb" color="#1CB2FE">
  A test failover does not impact your production environment. It enables you to validate that all systems, from network connectivity to replication accuracy, are functioning as expected.
</Callout>

***

## Completing the Disaster Recovery Test

After a successful test failover, it is essential to clean up the test environment:

1. Navigate to the replicated items in the Azure portal.
2. Select "Clean Up Test Failover Pending" to remove the test configurations.
3. Confirm by deleting the test virtual machine when prompted.

<Frame>
  ![The image shows a Microsoft Azure portal interface displaying the "Site-recovery-vault-westus" with details about replicated items, including replication health and status. A notification indicates a task to delete a test failover environment is in progress.](https://kodekloud.com/kk-media/image/upload/v1752884479/notes-assets/images/Updated-AZ-104-Microsoft-Azure-Administrator-Azure-Site-Recovery/azure-portal-site-recovery-vault.jpg)
</Frame>

Following cleanup, if a full production failover is required, the option will be available once the test process is complete. A full failover permanently transfers workloads to the disaster recovery region. When the primary region is restored, you can reverse the process by re-synchronizing and committing the changes to switch back to the primary region.

Other advanced features of ASR include recovery plans, automation, and integration with [Azure Traffic Manager](https://azure.microsoft.com/en-us/services/traffic-manager/). However, mastering the failover process is key for certification and ensuring business continuity.

This concludes our lesson on setting up and testing Azure Site Recovery for robust disaster recovery and business continuity in Microsoft Azure.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/az-104-microsoft-azure-administrator/module/a25ecd10-20ce-4ff9-bcc1-386c2e018b09/lesson/7152e573-cd8d-4dac-9b8d-7675b93f4437" />
</CardGroup>

---


# Section 12: Administer Monitoring

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
