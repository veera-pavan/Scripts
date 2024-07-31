
# Deployment Config

resourcegroup_name = "azurecicd-new"

location = "East US 2"


vnet_name = "azureagent-vnet-new"

vnet_address_space = ["10.1.0.0/26"]
 

subnets = {
  subnet1 = {
    address_prefix = "10.1.0.0/27"
  }
  subnet2 = {
    address_prefix = "10.1.0.0/28"
  }
}

vm_config = {
  vm1 = {
    subnet_key = "subnet1"
  }
  vm2 = {
    subnet_key = "subnet2"
  }
}
  

