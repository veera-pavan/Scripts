provider "azurerm" {
}
 
resource "azurerm_resource_group" "example" {
  name     = "example-resource-group"
  location = "East US"  # Update with your desired Azure region
}
 
resource "azurerm_sql_server" "example" {
  name                         = "example-sql-server"
resource_group_name = azurerm_resource_group.example.name
  location                     = azurerm_resource_group.example.location
  version                      = "12.0"  # Choose the desired SQL Server version
  administrator_login          = "sqladmin"
  administrator_login_password = "StrongPassword123!"  # Replace with a strong password
}
 
resource "azurerm_sql_database" "example" {
  name                = "example-sql-db"
resource_group_name = azurerm_resource_group.example.name
server_name = azurerm_sql_server.example.name
  edition             = "GeneralPurpose"
  collation           = "SQL_Latin1_General_CP1_CI_AS"
  max_size_gb         = 1
  location = East US
}
 
resource "azurerm_sql_firewall_rule" "example" {
  name                = "AllowAllWindowsAzureIps"
resource_group_name = azurerm_resource_group.example.name
server_name = azurerm_sql_server.example.name
  start_ip_address    = "0.0.0.0"
  end_ip_address      = "0.0.0.0"
}
 
resource "azurerm_key_vault" "example" {
  name                        = "example-key-vault"
resource_group_name = azurerm_resource_group.example.name
  location                    = azurerm_resource_group.example.location
  enabled_for_disk_encryption = true
  enabled_for_template_deployment = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name                    = "standard"
}
 
resource "azurerm_key_vault_secret" "sql_connection_string" {
  name         = "SqlConnection"
value = azurerm_sql_database.example.connection_strings["ado.net"]
key_vault_id = azurerm_key_vault.example.id
}
 
resource "azurerm_app_service_plan" "example" {
  name                = "example-app-service-plan"
  location            = azurerm_resource_group.example.location
resource_group_name = azurerm_resource_group.example.name
 
  sku {
    tier = "Standard"
    size = "S1"
  }
}
 
resource "azurerm_app_service" "example" {
  name                = "example-web-app"
  location            = azurerm_resource_group.example.location
resource_group_name = azurerm_resource_group.example.name
app_service_plan_id = azurerm_app_service_plan.example.id
 
  site_config {
    dotnet_framework_version = "v5.0"
    scm_type                = "LocalGit"
  }
 
  app_settings = {
    "WEBSITE_NODE_DEFAULT_VERSION" = "14.17.0"
    "ASPNETCORE_ENVIRONMENT"       = "Production"
"ConnectionStrings__DefaultConnection" = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault_secret.sql_connection_string.id})"
  }
}
 
output "web_app_url" {
  value = azurerm_app_service.example.default_site_hostname
}