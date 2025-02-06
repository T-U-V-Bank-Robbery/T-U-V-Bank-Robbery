#!/bin/bash

# Deployment Script for AI Heist Agent Project

echo "Starting deployment of AI Heist Agent..."

# Navigate to project root directory
cd "$(dirname "$0")"/..

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Compile smart contracts
echo "Compiling smart contracts..."
cd src/contracts
solc --optimize --bin token_contract.sol -o ../../build/

# Return to root directory
cd ../..

# Configure blockchain settings
echo "Configuring blockchain network..."
export BLOCKCHAIN_NETWORK="https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID"

# Run the main application
echo "Running the AI Heist Agent..."
python src/main.py

echo "Deployment complete."
