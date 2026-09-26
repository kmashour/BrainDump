# AZ-104 Section 07: Administer Network Traffic

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 9

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
