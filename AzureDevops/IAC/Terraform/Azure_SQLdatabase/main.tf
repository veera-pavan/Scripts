terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">=3.70.0"
    }
  }
}

# Configure the Microsoft Azure Provider and Azure login
provider "azurerm" {
  features {
  }
  subscription_id   = "<azure_subscription_id>"
  tenant_id         = "<azure_subscription_tenant_id>"
  client_id         = "<service_principal_appid>"
  client_secret     = "<service_principal_password>"
}

# Create a resource group
resource "azurerm_resource_group" "demo" {
  name     = "demo"
  location = var.location
}