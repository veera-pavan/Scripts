
# Deployment Config

resourcegroup_name = "azurecicd-new"

location = "East US 2"


vnet_name = "azureagent-vnet-new"

vnet_address_space = ["10.0.0.0/16"]

subnets = {
  Subnet_1 = {
    name             = "default"
    address_prefixes = ["10.0.0.0/24"]
  }
  bastion_subnet = {
    name             = "AzureBastionSubnet"
    address_prefixes = ["10.0.1.0/26"]
  }
}

bastionhost_name = "cicdbastionhost"