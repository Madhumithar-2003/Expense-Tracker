import tkinter as tk
from tkinter import messagebox
import json
import os

# JSON File for storing expenses
FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Persistent Database
expenses = load_expenses()

# Add Expense
def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    date = date_entry.get()

    if not category or not amount or not date:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number!")
        return

    expenses.append({"category": category, "amount": amount, "date": date})
    save_expenses()  # Save to file
    messagebox.showinfo("Success", "Expense added successfully!")
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# View Expenses
def view_expenses():
    records_window = tk.Toplevel(root)
    records_window.title("Expense Records")
    records_window.configure(bg="#f9f5d7")  # Light yellow background

    # Header Labels
    tk.Label(records_window, text="ID", width=10, borderwidth=1, relief="solid", bg="pink").grid(row=0, column=0)  # Pink
    tk.Label(records_window, text="Category", width=20, borderwidth=1, relief="solid", bg="pink").grid(row=0, column=1)
    tk.Label(records_window, text="Amount", width=15, borderwidth=1, relief="solid", bg="pink").grid(row=0, column=2)
    tk.Label(records_window, text="Date", width=15, borderwidth=1, relief="solid", bg="pink").grid(row=0, column=3)

    # Expense Records
    for i, record in enumerate(expenses):
        tk.Label(records_window, text=i + 1, width=10, borderwidth=1, relief="solid", bg="#e0f7fa").grid(row=i + 1, column=0)  # Light cyan
        tk.Label(records_window, text=record["category"], width=20, borderwidth=1, relief="solid", bg="#e0f7fa").grid(row=i + 1, column=1)
        tk.Label(records_window, text=record["amount"], width=15, borderwidth=1, relief="solid", bg="#e0f7fa").grid(row=i + 1, column=2)
        tk.Label(records_window, text=record["date"], width=15, borderwidth=1, relief="solid", bg="#e0f7fa").grid(row=i + 1, column=3)

# Main Application
root = tk.Tk()
root.title("Expense Tracker")
root.configure(bg="#bbdefb")  # Light blue background

# Input Fields
category_label = tk.Label(root, text="Category:", bg="#bbdefb", fg="black", font=("Arial", 10, "bold"))
category_label.grid(row=0, column=0, padx=20, pady=20)
category_entry = tk.Entry(root, bg="white", font=("Arial", 10))
category_entry.grid(row=0, column=1, padx=20, pady=20)

amount_label = tk.Label(root, text="Amount:", bg="#bbdefb", fg="black", font=("Arial", 10, "bold"))
amount_label.grid(row=1, column=0, padx=20, pady=20)
amount_entry = tk.Entry(root, bg="white", font=("Arial", 10))
amount_entry.grid(row=1, column=1, padx=20, pady=20)

date_label = tk.Label(root, text="Date (YYYY-MM-DD):", bg="#bbdefb", fg="black", font=("Arial", 10, "bold"))
date_label.grid(row=2, column=0, padx=20, pady=20)
date_entry = tk.Entry(root, bg="white", font=("Arial", 10))
date_entry.grid(row=2, column=1, padx=20, pady=20)

# Buttons
add_button = tk.Button(root, text="Add Expense", command=add_expense, bg="#4caf50", fg="white", font=("Arial", 10, "bold"))
add_button.grid(row=3, column=0, padx=20, pady=20)

view_button = tk.Button(root, text="View Expenses", command=view_expenses, bg="#f57c00", fg="white", font=("Arial", 10, "bold"))
view_button.grid(row=3, column=1, padx=20, pady=20)

root.mainloop()
