variable "bkstrgrg" {
  type        = string
  description = "The name of the backend storage account resource group"
  default     = "azurecicd-new"
}

variable "bkstrg" {
  type        = string
  description = "The name of the backend storage account"
  default     = "cicdstorageaccount"
}

variable "bkcontainer" {
  type = string
  description = "The container name for the backend config"
  default = "tfstate"
}

variable "bkstrgkey" {
  type = string
  description = "The access key for the storage account"
  default = "cicdpipeline.terraform.tfstate"
}

variable "resourcegroup_name" {
  type        = string
  description = "The name of the resource group"
  default     = "azurecicd-new"
}

variable "location" {
  type        = string
  description = "The region for the deployment"
  default     = "East US 2"
}


variable "vnet_name" {
  type        = string
  description = "The name of the vnet"
  default     = "azureagent-vnet-new"
}

variable "vnet_address_space" {
  type        = list(any)
  description = "the address space of the VNet"
  default     = ["10.0.0.0/16"]
}

variable "subnets" {
  type = map(any)
  default = {
    subnet_1 = {
      name             = "default"
      address_prefixes = ["10.0.0.0/24"]
    }
    # The name must be AzureBastionSubnet
    bastion_subnet = {
      name             = "AzureBastionSubnet"
      address_prefixes = ["10.0.1.0/26"]
    }
  }
}

variable "bastionhost_name" {
  type        = string
  description = "The name of the basion host"
  default     = "cicdbastionhost"
}