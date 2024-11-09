import unittest
import pandas as pd
from fpdf import FPDF
import datetime
import numpy as np
import sys

# Read CSV file from command line argument
csv_file = sys.argv[1] if len(sys.argv) > 1 else 'data.csv'

# Read the data from the CSV file
df = pd.read_csv(csv_file)

# Define the unit test class for data quality
class TestDataQuality(unittest.TestCase):
    def setUp(self):
        """Set up the data and report"""
        self.df = df
        self.report = []

    def add_report_entry(self, test_name, result, message):
        """Adds an entry to the report list"""
        self.report.append({
            "test_name": test_name,
            "result": "Pass" if result else "Fail",
            "message": message
        })

    def test_missing_values(self):
        """Test for missing values in the dataset."""
        missing = self.df.isnull().sum().sum()
        result = missing > 0
        self.add_report_entry("Missing Values", result, f"Missing Values Found: {missing}")

    def test_no_duplicates(self):
        """Test for duplicate Transaction_IDs in the dataset."""
        duplicates = self.df.duplicated(subset='Transaction_ID').sum()
        result = duplicates == 0
        self.add_report_entry("Duplicate Transactions", result, f"Duplicates Found: {duplicates}")

    def test_positive_transaction_amount(self):
        """Test that Transaction_Amount has no negative or zero values."""
        non_positive = self.df[self.df['Transaction_Amount'] <= 0]
        result = len(non_positive) == 0
        self.add_report_entry("Positive Transaction Amount", result, f"Non-positive Amounts Found: {len(non_positive)}")

    def test_valid_transaction_types(self):
        """Test for valid Transaction_Type values."""
        valid_types = {"Credit", "Debit"}
        invalid_types = self.df[~self.df['Transaction_Type'].isin(valid_types)]
        result = len(invalid_types) == 0
        self.add_report_entry("Valid Transaction Types", result, f"Invalid Types Found: {len(invalid_types)}")

    def test_unique_transaction_ids(self):
        """Test for uniqueness of Transaction_ID."""
        unique_ids = self.df['Transaction_ID'].nunique() == len(self.df)
        result = unique_ids
        self.add_report_entry("Unique Transaction IDs", result, "All Transaction IDs are unique" if unique_ids else "Duplicates found")

    def test_no_future_dates(self):
        """Test that Transaction_Date contains no future dates."""
        future_dates = self.df[self.df['Transaction_Date'] > datetime.datetime.now()]
        result = len(future_dates) == 0
        self.add_report_entry("No Future Dates", result, f"Future Dates Found: {len(future_dates)}")

# PDF report generator class
class DQReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Data Quality Report', ln=True, align='C')

    def add_test_result(self, test_name, result, message):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, f"Test: {test_name}", ln=True)
        self.set_font('Arial', '', 10)
        self.cell(0, 10, f"Result: {result}", ln=True)
        self.cell(0, 10, f"Message: {message}", ln=True)
        self.ln(5)

    def add_report_data(self, report_data):
        for entry in report_data:
            self.add_test_result(entry["test_name"], entry["result"], entry["message"])

# Function to run tests and generate report
def generate_dq_report():
    # Initialize an instance of the TestDataQuality class
    dq_tester = TestDataQuality()

    # Run each test manually to populate the report
    dq_tester.setUp()  # Set up the DataFrame and report list
    dq_tester.test_missing_values()
    dq_tester.test_no_duplicates()
    dq_tester.test_positive_transaction_amount()
    dq_tester.test_valid_transaction_types()
    dq_tester.test_unique_transaction_ids()
    dq_tester.test_no_future_dates()

    # Collect the report data
    report_data = dq_tester.report

    # Generate PDF report
    pdf = DQReport()
    pdf.add_page()
    pdf.add_report_data(report_data)

    # Save the PDF
    pdf_file_path = "Data_Quality_Report.pdf"
    pdf.output(pdf_file_path)
    print(f"Data Quality Report generated at {pdf_file_path}")

# Run the report generation function
if __name__ == "__main__":
    generate_dq_report()
