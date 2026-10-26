# Create a resource group
resource "azurerm_resource_group" "rg" {
  name = "my-sql-server-demo-rg"
  location = "eastus"
}

# Create SQL Server
resource "azurerm_mssql_server" "sql_server" {
  name = "my-sql-server-07865"
  resource_group_name = azurerm_resource_group.rg.name
  location = azurerm_resource_group.rg.location
  version = "12.0"
  administrator_login = "sqladmin" # Change this to your desired admin username
  administrator_login_password = "StrongPassword@123" # Change this to your desired password
}

# Create a sample SQL Database
resource "azurerm_mssql_database" "sampledb" {
  name = "sampledb"
  server_id = azurerm_mssql_server.sql_server.id
}

# Create a Firewall rule
resource "azurerm_mssql_firewall_rule" "firewall_rule" {
  name = "my-sql-sever-firewall"
  server_id = azurerm_mssql_server.sql_server.id
  start_ip_address = "YOUR_PUBLIC_IP"  # Replace with your public IP
  end_ip_address   = "YOUR_PUBLIC_IP"  # Replace with your public IP"
}
