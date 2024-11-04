import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Perform data cleaning operations."""
    # Implement cleaning steps, e.g., handling missing values
    df = df.dropna()
    return df
