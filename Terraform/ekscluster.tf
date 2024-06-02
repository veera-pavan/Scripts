 provider "aws" {
  region = "ap-southeast-2"  # Specify your AWS region
}

resource "aws_eks_cluster" "my_cluster" {
  name     = "my-eks-cluster"
  role_arn = aws_iam_role.eks_cluster.arn
  vpc_config {
    subnet_ids = ["subnet-1","subnet-2","subnet-3"]  # IDs of existing subnets
  }
}

resource "aws_iam_role" "eks_cluster" {
  name = "eks-cluster-role2"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
  Service = "eks.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy_attachment" "eks_cluster_policy_attachment" {
  name       = "eks-cluster-policy-attachment"
roles = [aws_iam_role.eks_cluster.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}
resource "aws_iam_role" "eks_node_role" {
  name = "eks-node-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
Service = "ec2.amazonaws.com"  # Allow EC2 instances to assume this role
        }
      }
    ]
  })
  # Attach policies or permissions as needed for your worker nodes
}
resource "aws_iam_policy_attachment" "eks_worker_node_policy" {
  name       = "eks-worker-node-policy-attachment"
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
roles = [aws_iam_role.eks_node_role.name]
}
resource "aws_iam_policy_attachment" "ecr_readonly_policy" {
  name       = "ecr-readonly-policy-attachment"
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
roles = [aws_iam_role.eks_node_role.name]
}

resource "aws_eks_node_group" "my_node_group" {
cluster_name = aws_eks_cluster.my_cluster.name
  node_group_name = "my-node-group"
  node_role_arn = aws_iam_role.eks_node_role.arn
  launch_template {
    id      = "lt-0d99e1f51cdc94a22"  # Specify your launch template ID
    version = "1"                  # Specify the template version or use "$Latest"
  }
  scaling_config {
    desired_size = 1  # Number of nodes to create
    min_size     = 1  # Minimum number of nodes
    max_size     = 2  # Maximum number of nodes
  }
 subnet_ids = ["subnet-1", "subnet-2", "subnet-3"]  # Specify your existing subnet IDs
}
