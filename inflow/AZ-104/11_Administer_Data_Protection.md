# AZ-104 Section 11: Administer Data Protection

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 9

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
