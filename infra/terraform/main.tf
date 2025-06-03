provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  name   = "dating-coach-vpc"
  cidr   = "10.0.0.0/16"
}

module "ecs" {
  source  = "terraform-aws-modules/ecs/aws"
  name    = "dating-coach-cluster"
  vpc_id  = module.vpc.vpc_id
}