""" Project: Expense Tracker App """

import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Logging and storing expenses
def log_expense(date, category, amount, description):
    with open('expenses.csv', 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

# example
# log_expense(datetime.now().strftime("%Y-%m-%d"), "Food", 200, "Transport at cafe")
# print("Expense logged!")

# categorizing and summarizing data
def load_expenses():
    return pd.read_csv("expenses.csv", names = ['Date', 'Category', 'Amount', 'Description'])

def summarize_expenses(df):
    summary = df.groupby('Category')['Amount'].sum()
    print("\nExpense summayr: ")
    print(summary)

# df = load_expenses()
# summarize_expenses(df)

def plot_expense_by_category(df):
    summary = df.groupby('Category')['Amount'].sum()
    summary.plot(kind = 'pie', autopct = "%1.1f%%", figsize = (6,6), title = "Expenses by Category")
    plt.ylabel("")
    plt.show()

# plot_expense_by_category(df)

def plot_monthly_trends(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_summary = df.groupby("Month")["Amount"].sum()
    monthly_summary.plot(kind = "bar", figsize = (10, 6), title = "Monthly Expense Trends")
    plt.xlabel("Month")
    plt.ylabel("Total Expenses")
    plt.xticks(rotation = 45)
    plt.show()

# plot_monthly_trends(df)

def main():
    print("Welcome to the expense tracker!")
    while True:
        print("\nOptions:")
        print("1. Log an Expense")
        print("2. View expense summary")
        print('3. Plot expense by category')
        print("4. Plot montly trends")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")
            log_expense(date, category, amount, description)
            print("Expense logged successfully")
        elif choice == "2":
            df = load_expenses()
            summarize_expenses(df)
        elif choice == "3":
            df = load_expenses()
            plot_expense_by_category(df)
        elif choice == "4":
            df = load_expenses()
            plot_monthly_trends(df)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter number between 1-5 only.")

if __name__ == "__main__":
    main()