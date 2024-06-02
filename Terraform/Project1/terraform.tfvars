#variable of type object
subnet_prefix = [
    { 
        cidr_block = "10.0.1.0/24", name = "prod_subnet" 
        },
    { 
        cidr_block = "10.0.2.0/24", name = "dev_subnet" 
        }
]

#variable of type = string

subnet_prefix = "10.0.1.0/24"

#variable of type = list

subnet_prefix = ["10.0.1.0/24", "10.0.2.0/24"]

