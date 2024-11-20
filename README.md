# Q1 Project: Implementing NeMo Guardrails for LLM Security

## Project Overview
This project explores the use of NVIDIA’s NeMo Guardrails to secure language model (LLM) applications against vulnerabilities such as jailbreaking, injection attacks, and harmful content generation. I apply NeMo Guardrails within a Streamlit application, testing its effectiveness in real-time interactions.

## Repository Structure

```plaintext
Q1_Project
├── README.md                # Project overview, installation, and usage instructions
├── requirements.txt         # Python dependencies
├── config.yml               # Configuration file for guardrails setup
├── src/                     # Source code for data processing, guardrails, etc.
│   ├── etl.py               # Extract, transform, and load functions
│   ├── guardrails.py        # Functions for implementing NeMo guardrails
│   └── run.py               # Script for executing the pipeline
├── data/                    
│   ├── raw/                 # Folder for raw data (excluded from Git)
│   └── processed/           # Folder for processed data
├── test/                    # Unit test files
│   ├── testdata/            # Small synthetic test data for unit tests
│   ├── test_etl.py          # Unit tests for ETL functions
│   └── test_guardrails.py   # Unit tests for guardrails functions
└── notebook.ipynb               # Jupyter notebooks for analysis and EDA, and for checkpoint submission
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/hhshhd/Quarter1Project.git
cd Quarter1Project
```
In the run.py under src file, there is a requirement of hand typing the OpenAI-APi-key of your own to run successfuly, since the OpenAI doesn't allow me to share my own API key to an online service such as GitHub, you should go [this link](https://platform.openai.com/api-keys), create and login in your own OpenAI account to generate your own key and replace with my code below in src/guardrails.py. Replace your key to OpenAI-API-key so that keep the variable as a string type.

```
openai_api_key = "OpenAI-API-key"
```
!!!since it needs some credits for using the OpenAI, so if any TA is viewing my code and find out "Error 429 - You exceeded your current quota, please check your plan and billing details" when asking question on streamlit, please contact my email(hhai@ucsd.edu) so that i can provide u my own api key to use to test the result. Otherwise u might need to add some credits to you own openai account. Sorry about the incovenience but since we need to use openAI and their privacy doesn't allow use to share the key online.
### 2. Create and Activate a Virtual Environment
```
python3 -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```

# Troubleshooting: Building `annoy` Package on macOS

If you encounter errors while installing the `annoy` package on macOS, such as architecture mismatches (`mach-o file, but is an incompatible architecture`), follow these steps to resolve the issue. First, ensure your Python installation matches your Mac's architecture (`arm64` for Apple Silicon or `x86_64` for Intel) by running `python3 -c "import platform; print(platform.machine())"`. If needed, reinstall Python for `arm64` using `brew install python`. Next, update or reinstall Xcode Command Line Tools with `xcode-select --install` or by removing the old tools with `sudo rm -rf /Library/Developer/CommandLineTools` before reinstalling. Install the required development tools using `brew install llvm` to ensure `clang` and `clang++` are properly configured. If the issue persists, force a recompilation of `annoy` using `ARCHFLAGS="-arch arm64" pip install annoy --no-binary :all:`. On Apple Silicon Macs, you can also try running your terminal under Rosetta 2 by right-clicking "Terminal" in `Applications > Utilities`, selecting "Get Info," and checking "Open using Rosetta" before restarting the terminal. Alternatively, check for prebuilt binary wheels and install them with `pip install annoy --only-binary=:all:`. After installation, verify it by running `python3 -c "import annoy; print(annoy.__version__)"`. If the issue persists, feel free to open an issue or request additional support.

### 4. Run the Steamlit Application
```
streamlit run src/run.py
```
### 5. Interacting with the App:

Once the Streamlit app is running, open the provided URL (usually http://localhost:8501) in your browser.
Test the functionality, including text translation and any guardrail checks you implemented, by inputting various prompts and observing responses.

### 6. Testing Guardrails:

Test the guardrails by inputting phrases that should trigger the profanity or safety checks you set up. You should see outputs reflecting the checks (e.g., messages for blocked or moderated content).
