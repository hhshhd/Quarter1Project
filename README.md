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
streamlit run app.py
```
### 5. Interacting with the App:

Once the Streamlit app is running, open the provided URL (usually http://localhost:8501) in your browser.
Test the functionality, including text translation and any guardrail checks you implemented, by inputting various prompts and observing responses.

### 6. Testing Guardrails:

Test the guardrails by inputting phrases that should trigger the profanity or safety checks you set up. You should see outputs reflecting the checks (e.g., messages for blocked or moderated content).
