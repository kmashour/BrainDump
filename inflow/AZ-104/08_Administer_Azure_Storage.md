# AZ-104 Section 08: Administer Azure Storage

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 14

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
