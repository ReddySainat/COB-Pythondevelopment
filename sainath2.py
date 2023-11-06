import os
import csv
from collections import defaultdict
from datetime import datetime
from prettytable import PrettyTable

# Define the data file
DATA_FILE = "expenses.csv"

# Check if the data file exists, and if not, create it
if not os.path.isfile(DATA_FILE):
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Description", "Category", "Amount"])

# Function to record an expense
def record_expense():
    date = input("Date (YYYY-MM-DD): ")
    description = input("Description: ")
    category = input("Category: ")
    amount = float(input("Amount: $"))

    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount])
    print("Expense recorded successfully!")

# Function to generate monthly expense report
def generate_monthly_report():
    month = input("Enter the month and year (YYYY-MM): ")
    total_expenses = 0
    expenses_by_category = defaultdict(float)

    with open(DATA_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):
                amount = float(row["Amount"])
                total_expenses += amount
                expenses_by_category[row["Category"]] += amount

    report_table = PrettyTable()
    report_table.field_names = ["Category", "Amount"]
    for category, amount in expenses_by_category.items():
        report_table.add_row([category, f"${amount:.2f}"])

    print("\nMonthly Expense Report for", month)
    print("Total Expenses: $", total_expenses)
    print("\nExpense breakdown by category:")
    print(report_table)

# Main menu loop
while True:
    print("\nExpense Manager Menu:")
    print("1. Record an Expense")
    print("2. Generate Monthly Report")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        record_expense()
    elif choice == "2":
        generate_monthly_report()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Goodbye!")
