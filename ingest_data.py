import csv

def ingest_data(input_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"Ingesting data: {row}")

if __name__ == "__main__":
    input_file = "data.csv"
    ingest_data(input_file)
    print(f"Data ingested from {input_file}")
