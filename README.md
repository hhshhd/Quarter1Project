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
In the run.py under src file, there is a requirement of hand typing the OpenAI-APi-key of your own to run successfuly, since the OpenAI diesn't allow to share my own API key to an online service such as GitHub, you should go [ri ](https://platform.openai.com/api-keys) to generate your own key and replace with my code below in src/run.py.
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
### 4. Run the Steamlit Application
```
streamlit run src/run.py
```
### 5. Interacting with the App:

Once the Streamlit app is running, open the provided URL (usually http://localhost:8501) in your browser.
Test the functionality, including text translation and any guardrail checks you implemented, by inputting various prompts and observing responses.

### 6. Testing Guardrails:

Test the guardrails by inputting phrases that should trigger the profanity or safety checks you set up. You should see outputs reflecting the checks (e.g., messages for blocked or moderated content).
