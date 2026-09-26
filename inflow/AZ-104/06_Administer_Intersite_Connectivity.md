# AZ-104 Section 06: Administer Intersite Connectivity

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 9

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
