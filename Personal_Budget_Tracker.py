import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class BudgetTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget Tracker")

        self.income_label = tk.Label(root, text="Income:")
        self.income_label.grid(row=0, column=0, padx=10, pady=10)
        self.income_entry = tk.Entry(root)
        self.income_entry.grid(row=0, column=1, padx=10, pady=10)

        self.expense_label = tk.Label(root, text="Expense:")
        self.expense_label.grid(row=1, column=0, padx=10, pady=10)
        self.expense_entry = tk.Entry(root)
        self.expense_entry.grid(row=1, column=1, padx=10, pady=10)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.grid(row=2, column=0, padx=10, pady=10)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Transaction", command=self.add_transaction)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.calculate_button = tk.Button(root, text="Calculate Budget", command=self.calculate_budget)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.analysis_button = tk.Button(root, text="Expense Analysis", command=self.expense_analysis)
        self.analysis_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Load existing transactions from the file
        self.transactions = self.load_transactions()

    def add_transaction(self):
        income = float(self.income_entry.get())
        expense = float(self.expense_entry.get())
        category = self.category_entry.get()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        transaction = {"Timestamp": timestamp, "Income": income, "Expense": expense, "Category": category}
        self.transactions.append(transaction)

        # Save the updated transactions to the file
        self.save_transactions()

        messagebox.showinfo("Transaction Added", "Transaction added successfully.")

    def calculate_budget(self):
        total_income = sum(transaction["Income"] for transaction in self.transactions)
        total_expense = sum(transaction["Expense"] for transaction in self.transactions)

        remaining_budget = total_income - total_expense

        messagebox.showinfo("Budget Calculation", f"Remaining Budget: {remaining_budget:.2f}")

    def expense_analysis(self):
        categories = set(transaction["Category"] for transaction in self.transactions)
        category_expenses = {category: 0 for category in categories}

        for transaction in self.transactions:
            category_expenses[transaction["Category"]] += transaction["Expense"]

        analysis_text = "Expense Analysis:\n"
        for category, expense in category_expenses.items():
            analysis_text += f"{category}: {expense:.2f}\n"

        messagebox.showinfo("Expense Analysis", analysis_text)

    def save_transactions(self):
        with open(r"C:\Users\Admin\Downloads\Task_2\Budget_tracker.txt", "w") as file:
            json.dump(self.transactions, file)

    def load_transactions(self):
        try:
            with open(r"C:\Users\Admin\Downloads\Task_2\Budget_tracker.txt", "r") as file:
                transactions = json.load(file)
        except FileNotFoundError:
            transactions = []
        return transactions


if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTracker(root)
    root.mainloop()
