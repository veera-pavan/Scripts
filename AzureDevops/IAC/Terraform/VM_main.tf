provider "azurerm" {
}


resource "azurerm_resource_group" "demoRG" {
    name = "Demo_resource_group"
    location = "east_Europe"
  
}

resource "azurerm_virtual_network" "demoVN" {
    location = azurerm_resource_group.demoRG.location
    address_space = "10.0.0.1/24"
    name = "Demo_virtual_network"
    resource_group_name = azurerm_resource_group.demoRG.name
  
}

resource "azurerm_subnet" "demoSN" {
    name = "Demo_Subnet"
    virtual_network_name = azurerm_virtual_network.demoVN
    address_prefixes = "10.0.0.1/32"
    resource_group_name = azurerm_resource_group.demoRG.name
}

resource "azurerm_network_interface" "demoNIC" {
  ip_configuration {
    name = "internal"
    subnet_id = azurerm_subnet.demoSN.id
    private_ip_address_allocation = "Dynamic"
    
  }
  name = "Demo_network_interface"
  location = azurerm_resource_group.demoRG.location
  resource_group_name = azurerm_resource_group.demoRG.name

}

resource "azurerm_network_security_group" "demoNSG" {
    name = "Demo_network_security_group"
    resource_group_name = azurerm_resource_group.demoRG.name
    location = azurerm_resource_group.demoRG.location
    security_rule = connection {
        name                       = "demo_security_rule"
        priority                   = 100
        direction                  = "Inbound"
        access                     = "Allow"
        protocol                   = "Tcp"
        source_port_range          = "*"
        destination_port_range     = "*"
        source_address_prefix      = "*"
        destination_address_prefix = "*"
      
    } 
    tags = {
      environment = "Development"
    }
  
}
 #Create storage account for boot diagnostics
resource "azurerm_storage_account" "my_storage_account" {
  name                     = "diag${random_id.random_id.hex}"
  location                 = azurerm_resource_group.rg.location
  resource_group_name      = azurerm_resource_group.rg.name
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_windows_virtual_machine" "demoVM" {
    name = "Demo_virtual_machine"
    admin_username = "azureuser"
    admin_password = random random_password.password.result
    location = azurerm_resource_group.demoRG.location
    resource_group_name = azurerm_resource_group.demoRG.name
    size = "Standard_DS1_v2"
    network_interface_ids = azurerm_network_interface.demoNIC.private_ip_addresses
    os_disk {
     name = "Demo_os_disk"
     caching = "ReadWrite"
     storage_account_type = "Premium_LRS"
    }
    source_image_reference {
      publisher = "MicrosoftWindowsServer"
      offer =   "WindowsServer"
      sku = "2022-datacenter-azure-edition"
      version = "latest" 
       }
    boot_diagnostics {
      storage_account_uri = azurerm_storage_account.my_storage_account.primary_blob_endpoint
    }
    
  
}

resource "random_password" "password" {
   length = 20
   min_lower = 1
   min_numeric = 1
   min_special = 1
   min_upper = 1
   special = true
}  