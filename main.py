import tkinter as tk
import pandas as pd
import sqlite3

def create_database():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE,
            description TEXT,
            amount REAL,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_transaction():
    date = date_entry.get()
    description = description_entry.get()
    amount = float(amount_entry.get())
    category = category_entry.get()

    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (date, description, amount, category)
        VALUES (?, ?, ?, ?)
    ''', (date, description, amount, category))
    conn.commit()
    conn.close()

    # Update the display
    load_transactions()

def load_transactions():
    conn = sqlite3.connect('finances.db')
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()

    transactions_listbox.delete(0, tk.END)
    for index, row in df.iterrows():
        transactions_listbox.insert(tk.END, f"{row['date']} | {row['description']} | {row['amount']} | {row['category']}")

def remove_transaction():
    selected_index = transactions_listbox.curselection()

    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM transactions (id)
        where id=(?)
    ''', (selected_index))
    conn.commit()
    conn.close()

    load_transactions()

# Create the main window
root = tk.Tk()
root.title("Financial Tracker")

# Create input fields
date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_entry = tk.Entry(root)
description_label = tk.Label(root, text="Description:")
description_entry = tk.Entry(root)
amount_label = tk.Label(root, text="Amount:")
amount_entry = tk.Entry(root)
category_label = tk.Label(root, text="Category:")
category_entry = tk.Entry(root)

add_button = tk.Button(root, text="Add Transaction", command=add_transaction)
remove_button = tk.Button(root, text="Remove Transaction", command=remove_transaction)

# Create the listbox to display transactions
transactions_listbox = tk.Listbox(root)

# Place widgets on the window
date_label.grid(row=0, column=0)
date_entry.grid(row=0, column=1)
description_label.grid(row=1, column=0)
description_entry.grid(row=1, column=1)
amount_label.grid(row=2, column=0)
amount_entry.grid(row=2, column=1)
category_label.grid(row=3, column=0)
category_entry.grid(row=3, column=1)
add_button.grid(row=4, column=0)
remove_button.grid(row=4, column=1)
transactions_listbox.grid(row=5, column=0, columnspan=2)

# Create the database and load transactions
create_database()
load_transactions()

root.mainloop()