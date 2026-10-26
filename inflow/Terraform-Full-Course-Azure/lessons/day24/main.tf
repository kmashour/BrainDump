variable "DAY" {
    type = string
    default = "day24"
  
}

variable "location" {
  type = string
  default = "eastus"
}

resource "azurerm_resource_group" "rg1" {
  name = "${var.DAY}-rg"
  location = var.location
}

resource "azurerm_virtual_network" "vnet" {
  name = "${var.DAY}-vnet"
  location = azurerm_resource_group.rg1.location
  resource_group_name = azurerm_resource_group.rg1.name
    address_space = ["10.0.0.0/16"]


}

resource "azurerm_subnet" "sn" {
    name = "default"
    resource_group_name = azurerm_resource_group.rg1.name
    virtual_network_name = azurerm_virtual_network.vnet.name
    address_prefixes = ["10.0.1.0/24"]
}

resource "azurerm_service_plan" "name" {
  name = "${var.DAY}-plan"
  location = azurerm_resource_group.rg1.location
  resource_group_name = azurerm_resource_group.rg1.name 
  os_type = "Linux"
  sku_name = "B1"
 

}

resource "azurerm_linux_web_app" "name" {
  name = "${var.DAY}-webapp-18462"
  location = azurerm_resource_group.rg1.location
  resource_group_name = azurerm_resource_group.rg1.name
  service_plan_id = azurerm_service_plan.name.id
  
  site_config {
   application_stack{
    node_version = "18-lts"
  }
  }
  
  
}