# AZ-104 Section 09: Administer Azure Virtual Machines

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 8

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
