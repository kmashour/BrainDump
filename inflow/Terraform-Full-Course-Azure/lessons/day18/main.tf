resource "azurerm_resource_group" "rg" {
  name     = "day18-rg"
  location = "canada central"
}

resource "azurerm_storage_account" "sa" {
  name                     = "techtutorialswith123"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_service_plan" "example" {
  name                = "example-app-service-plan"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_function_app" "example" {
  name                = "piyush-function-qr"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  storage_account_name       = azurerm_storage_account.sa.name
  storage_account_access_key = azurerm_storage_account.sa.primary_access_key
  service_plan_id            = azurerm_service_plan.example.id

  site_config {
   application_stack {
    node_version = 18
   }    
  }
}