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
  default = "vmpipeline.terraform.tfstate"
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
  default     = ["10.1.0.0/26"]
}

variable "subnets" {
  description = "Configuration for the subnets"
  type = map(object({
    address_prefix = string
  }))
} 

variable "vm_config" {
  description = "Configuration for the VMs"
  type = map(object({
    subnet_key = string
  }))
}

