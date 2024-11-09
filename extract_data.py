import csv

def extract_data(output_file):
    data = [
        {"id": 1, "name": "John Doe", "Transaction_Date": "2024-10-01", "amount": 100},
        {"id": 2, "name": "Jane Doe", "Transaction_Date": "2024-10-05", "amount": 150},
        {"id": 3, "name": "Jim Beam", "Transaction_Date": "2024-09-25", "amount": 200}
    ]

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'Transaction_Date', 'amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    output_file = "extracted_data.csv"
    extract_data(output_file)
    print(f"Data extracted to {output_file}")
