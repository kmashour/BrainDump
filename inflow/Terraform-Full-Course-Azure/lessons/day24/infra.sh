# Check if Azure CLI is installed
if ! command -v az &> /dev/null
then
    echo "Azure CLI could not be found. Please install it to proceed."
    exit
fi

# Check if logged in to Azure
if ! az account show &> /dev/null
then
    echo "You are not logged in to Azure. Please login to proceed."
    az login
fi

# Set variables
DAY="day24"
RG_NAME="${DAY}-rg"
LOCATION="eastus"
VNET_NAME="${DAY}-vnet"
WEBAPP_NAME="${DAY}-webapp-${RANDOM}"

# Create resource group
az group create --name $RG_NAME --location $LOCATION || { echo "Failed to create resource group"; exit 1; }

# Create virtual network
az network vnet create \
  --resource-group $RG_NAME \
  --name $VNET_NAME \
  --address-prefix 10.0.0.0/16 \
  --subnet-name default \
  --subnet-prefix 10.0.1.0/24 || { echo "Failed to create virtual network"; exit 1; }

# Create App Service Plan
az appservice plan create \
  --name "${DAY}-plan" \
  --resource-group $RG_NAME \
  --sku B1 \
  --is-linux || { echo "Failed to create App Service Plan"; exit 1; }

# Create Web App
az webapp create \
  --resource-group $RG_NAME \
  --plan "${DAY}-plan" \
  --name $WEBAPP_NAME \
  --runtime "NODE:18-lts" || { echo "Failed to create Web App"; exit 1; }
