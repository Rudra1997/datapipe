import pandas as pd
import numpy as np

def extract_data(file_path):
    data = {
        'Transaction_ID': range(1, 21),
        'Sender_Name': ['Mario James Ltd.', 'John Doe','Jane Smith','Emily Brown', np.nan, 'Robert Lee', 'Michael Davis', 'William Taylor', 'Bob Williams', 'Alice Thompson'] * 2,
        'Counterparty_Name': ['Emergent Bio Solutions', 'VASSILIADES & CO UK LIMITED', 'David Miller', 'Kevin Peter', 'Rachel Geller'] * 4,
        'Transaction_Type': ['Credit', 'Debit'] * 10,
        'Transaction_Amount': [100, 500, 0, 200, -300, 1000, 200, 150, 500, 250] * 2,
        'Transaction_Mode': ['Online', 'Offline'] * 10,
        'Transaction_Date': pd.date_range(start="2023-01-01", periods=20, freq='7D')
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Data extracted to {file_path}")

if __name__ == "__main__":
    file_path = "extracted_data.csv"
    extract_data(file_path)
