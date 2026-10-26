terraform {
  required_version = ">=1.0"
  required_providers {
    azurerm ={
      source = "hashicorp/azurerm"
      version = "4.8.0"
    }
  }
}

provider "azurerm"{
  features {
  }
}