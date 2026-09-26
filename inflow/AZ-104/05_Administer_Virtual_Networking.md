# AZ-104 Section 05: Administer Virtual Networking

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 7

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
