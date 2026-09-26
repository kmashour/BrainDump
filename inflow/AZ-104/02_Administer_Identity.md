# AZ-104 Section 02: Administer Identity

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 11

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
