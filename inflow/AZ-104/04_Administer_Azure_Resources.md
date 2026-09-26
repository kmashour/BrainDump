# AZ-104 Section 04: Administer Azure Resources

> Course: [Updated] AZ-104: Microsoft Azure Administrator (KodeKloud)

> Total Lessons: 6

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
