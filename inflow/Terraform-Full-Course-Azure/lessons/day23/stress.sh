# Install stress tool
sudo apt-get update
sudo apt-get install stress

# Generate high CPU load
# This will use 4 workers, each spinning on a sqrt() calculation for 300 seconds
stress --cpu 6 --timeout 300