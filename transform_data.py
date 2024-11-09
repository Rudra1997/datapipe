import csv

def transform_data(input_file):
    transformed_data = []
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Example transformation: add a new field
            row['processed_amount'] = float(row['amount']) * 1.1
            transformed_data.append(row)
    
    with open(input_file, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'Transaction_Date', 'amount', 'processed_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in transformed_data:
            writer.writerow(row)

if __name__ == "__main__":
    input_file = "data.csv"
    transform_data(input_file)
    print(f"Data transformed in {input_file}")
