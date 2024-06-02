provider "azurerm" {
    features {
      
    }
  
}

module "storage_account" {
    source = "path/to/azure-storage-account-module"
    resource_group_name = "your-resource-group-name"
    storage_account_name = "your-storage-account-name"
    location = "East US"
    account_tier = "Standard"
    account_replication = "LRS"
}