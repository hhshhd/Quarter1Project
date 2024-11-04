import os
from dotenv import load_dotenv
from etl import load_data, preprocess_data, save_data
from guardrails import CustomGuardrails

load_dotenv()  # Load environment variables from .env file

def main():
    # ETL process
    raw_data_path = "data/raw/input.csv"
    processed_data_path = "data/processed/output.csv"
    
    # Load raw data
    df = load_data(raw_data_path)
    print("Data loaded successfully.")
    
    # Process data
    df_processed = preprocess_data(df)
    print("Data processed successfully.")
    
    # Save processed data
    save_data(df_processed, processed_data_path)
    print(f"Processed data saved to {processed_data_path}")

    # Guardrails Application
    guardrails = CustomGuardrails()
    user_input = "Translate this sentence to French."
    response = guardrails.apply_guardrails(user_input)
    print("Response with Guardrails:", response)

if __name__ == "__main__":
    main()


