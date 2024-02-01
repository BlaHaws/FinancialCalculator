import tkinter as tk
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Financial Calculator and Tracker")
root.geometry("600x400")

baseFrame = tk.Frame(root)
baseFrame.pack()

message1 = tk.Label(baseFrame, text="Welcome to the Financial Calculator and Tracker", 
                    font=('Arial', 12), justify='center', padx=5)
message1.config(wraplength=300)
message1.grid(row=0, column=0, sticky='nws',)

message3 = tk.Message(baseFrame, text="Money Spent:", 
                    font=('Arial', 8), width=300, justify='left')
message3.grid(row=1, column=0, sticky='nws')

textBox = tk.Text(baseFrame, height=1, width=10, font=('Arial', 8))
textBox.grid(row=2, column=0, sticky='nws', padx=5)

message2 = tk.Label(baseFrame, text="Please enter your financial information below", 
                    font=('Arial', 12), justify='center')
message2.config(wraplength=300)
message2.grid(row=0, column=1, sticky='nes')

baseFrame.pack(pady=5)

root.mainloop()
