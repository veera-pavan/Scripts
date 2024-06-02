terraform {
  required_providers {
    azurerm = {
        source = "hashicorp/azurerm"
        version = ">=3.70.0"

    }
  }
}

#configure the microsoft azure provider

provider "azurerm" {
  features {
    
  }
  
}