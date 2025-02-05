# Installation Guide: AI Heist Agent Project

This guide will help you set up and run the AI Heist Agent Project on your local development environment.

---

## Requirements
- **Operating System:** Linux, macOS, or Windows  
- **Python Version:** 3.8+  
- **Additional Tools:** Solidity Compiler, Virtual Protocol Game SDK  

---

## 1. Clone the Repository  
Open your terminal and run the following command:  
git clone https://github.com/your-organization/AI-Heist-Agent-Project.git  
cd AI-Heist-Agent-Project/english  

---

## 2. Create a Virtual Environment  
python3 -m venv venv  
source venv/bin/activate  # For Linux/macOS  
venv\Scripts\activate     # For Windows  

---

## 3. Install Dependencies  
pip install -r requirements.txt  

---

## 4. Configure the Project  
Edit the configuration file (`src/config.yaml`) to match your local setup. Set the required API keys, network settings, and token configurations.

---

## 5. Compile the Smart Contracts (if applicable)  
Navigate to the `src/contracts` directory and run:  
solc --optimize --bin token_contract.sol -o build/  

---

## 6. Run the Application  
python src/main.py  

---

## 7. Running Tests  
To ensure everything is working as expected:  
pytest tests/  

---

## Troubleshooting  
- **Dependency Errors:** Ensure your virtual environment is activated and the `requirements.txt` file is properly installed.  
- **Network Issues:** Check your blockchain node configuration in `src/network/node_config.yaml`.

---

For more information, refer to the **[whitepaper](whitepaper.md)** or **[README.md](../README.md)**.
