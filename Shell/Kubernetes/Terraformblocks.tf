#let write different blocks available in Terraform

##resource block

resource "eks_cluster" "test_ekscluster" {
    region = "eastus2"
    provider = "azure"
  
}

resource "aws_instance" "testvm" {
    ami = "ami-387463498w340q6"
    instance_type = "t2.micro"
}

#provider block

provider "aws" {
    region = "us-west-2"
}

#variable block

variable "instance_count" {
    type = number
    default = 2
  
}

#output block

output "instance_ip" {
    value = aws_instance.testvm.private_ip
  
}

#data block

data "aws_ami" "latest_amazon_linux" {
    most_recent = true
    owners = ["amazon"]
    filter {
      name = "name"
      values = [amzn2-ami-hvm-*-x86_64-gp2]
    }
  
}

#module block

module "vpc" {
    source = "./modules/vpc"
    vpc_cidr_block = "10.0.0.0/23"
  
}

locals {
  instance_type = "t2.micro"
  tags = {
    name = "example-instance"
  }
}

