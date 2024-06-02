resource "azurerm_resource_group" "demo" {
    name = "autoscalling-demo"
    location = var.location 
}