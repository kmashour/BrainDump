# AZ-104 Section 10: Administer PaaS Compute Options

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 10

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
