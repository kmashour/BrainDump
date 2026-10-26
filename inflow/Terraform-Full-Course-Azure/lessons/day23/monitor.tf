resource "azurerm_monitor_action_group" "main" {
  name                = "example-actiongroup"
  resource_group_name = azurerm_resource_group.app_rg.name
  short_name          = "exampleact"

  email_receiver {
    name = "sendtoadmin"
    email_address = var.email
  }
}

resource "azurerm_monitor_metric_alert" "example" {
  name                = "example-metricalert"
  resource_group_name = azurerm_resource_group.app_rg.name
  scopes              = [azurerm_linux_virtual_machine.demo_vm.id]
  description         = "Action will be triggered when CPU is greater than 60."

  criteria {
    metric_namespace = "Microsoft.Compute/virtualMachines"
    metric_name      = "Percentage CPU"
    aggregation      = "Average"
    operator         = "GreaterThan"
    threshold        = 60
    # when Average CPU > 60 for 5 min(default)

  }

  action {
    action_group_id = azurerm_monitor_action_group.main.id
  }
}

resource "azurerm_monitor_metric_alert" "disk" {
  name                = "example-metricalert1"
  resource_group_name = azurerm_resource_group.app_rg.name
  scopes              = [azurerm_linux_virtual_machine.demo_vm.id]
  description         = "Action will be triggered when Free disk space is less than 20."

  criteria {
    metric_namespace = "Microsoft.Compute/virtualMachines"
    metric_name      = "Available Memory Bytes"
    aggregation      = "Average"
    operator         = "LessThan"
    threshold        = 20
    # when Available Memory Bytes < 20 for 5 min(default)

  }

  action {
    action_group_id = azurerm_monitor_action_group.main.id
  }
}