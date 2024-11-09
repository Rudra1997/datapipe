import pandas as pd
import numpy as np

def transform_data(file_path):
    df = pd.read_csv(file_path)
    # Example transformation: add a new field
    df['processed_amount'] = df['Transaction_Amount'] * 1.1
    # Example transformation: fill NaN values in 'Sender_Name' with 'Unknown Sender'
    df['Sender_Name'] = df['Sender_Name'].fillna('Unknown Sender')
    df.to_csv(file_path, index=False)
    print(f"Data transformed and saved to {file_path}")

if __name__ == "__main__":
    file_path = "extracted_data.csv"
    transform_data(file_path)
