import pandas as pd

def ingest_data(file_path):
    df = pd.read_csv(file_path)
    # Example ingestion: print the dataframe to simulate ingestion
    print(f"Data ingested from {file_path}")
    print(df.head())

if __name__ == "__main__":
    file_path = "extracted_data.csv"
    ingest_data(file_path)
