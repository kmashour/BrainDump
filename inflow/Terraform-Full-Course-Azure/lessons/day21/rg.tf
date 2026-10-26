resource "azurerm_resource_group" "rg" {
    name = "test-rg"
    location = "canadacentral"
  
  tags = {
    department = "IT"
    project = "Accelerator"
  }
}

resource "azurerm_resource_group" "rg1" {
    name = "test-rg1"
    location = "canadacentral"
  
  tags = {
    department = "IT"
    project = "Accelerator"
  }
}