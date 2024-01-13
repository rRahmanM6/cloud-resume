terraform {
  required_providers {
    aws = {
      version =">=4.9.0"
      source = "hashicorp/aws"
    }
  }
}
provider "aws" {
  access_key="AKIAR3ZFC6TB6LLKTZ7K"
  secret_key = "LyB3d4+2"
  region = "us-east-2"
}