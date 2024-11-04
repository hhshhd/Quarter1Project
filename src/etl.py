import pandas as pd
import numpy as np

def load_data(file_path):
    """Load data from a specified CSV file path."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Process the DataFrame by handling missing values, renaming columns, etc."""
    df.fillna(0, inplace=True)
    df['processed_column'] = df['raw_column'] * 2  # Example transformation
    return df

def save_data(df, file_path):
    """Save the processed DataFrame to a specified CSV file path."""
    df.to_csv(file_path, index=False)
