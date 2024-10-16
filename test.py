import tkinter as tk
from tkinter import ttk
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS transactions (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, description VARCHAR(255), amount DECIMAL(10,2))")

class FinancialTracker:
    def __init__(self, master):
        self.master = master
        master.title("Financial Tracker")

        # Create input fields
        self.date_label = tk.Label(master, text="Date (YYYY-MM-DD):")
        self.date_entry = tk.Entry(master)

        self.desc_label = tk.Label(master, text="Description:")
        self.desc_entry = tk.Entry(master)

        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_entry = tk.Entry(master)

        # Create buttons
        self.add_button = tk.Button(master, text="Add Transaction", command=self.add_transaction)
        self.view_button = tk.Button(master, text="View Transactions", command=self.view_transactions)

        # Place elements on the grid
        # ...

    def add_transaction(self):
        # Get values from input fields
        # Insert into the database
        # ...

    def view_transactions(self):
        # Fetch data from the database
        # Display in a table using Pandas
        # ...

root = tk.Tk()
tracker = FinancialTracker(root)
root.mainloop()

def view_transactions(self):
    mycursor.execute("SELECT * FROM transactions")
    data = mycursor.fetchall()

    df = pd.DataFrame(data, columns=['id', 'date', 'description', 'amount'])
    # Display df in a table (e.g., using a Treeview)