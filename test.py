import tkinter as tk
import pandastable as pt
from functools import partial
import sqlite3
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

df = pd.DataFrame({'A': [1, 2, 3]})#, 'B': [4, 5, 6]})

class PandasApp():
  def __init__(self, master) -> None:
    self.frame = tk.Frame(master)
    self.frame.pack(padx=10, pady=10)

    self.table = pt.Table(self.frame, dataframe=df, showtoolbar=True, showstatusbar=True)
    self.table.show()

  def insert_line(self, entry):
    if entry.isnumeric():
      self.table.model.df = self.table.model.df._append(entry, ignore_index=True)
      self.table.redraw()

  def refresh_table(self):
    self.table.redraw()

def __init__(self):
  root = tk.Tk()
  root.title("Financial Calculator and Tracker")
  root.geometry("600x400")
  
  main_label = tk.Label(root, text="Financial Calculator and Tracker")
  main_label.pack(fill="both")

  baseFrame = tk.Frame(root)
  baseFrame.pack()

  left_frame = tk.Frame(baseFrame)
  left_frame.grid(row=1, column=0)
  right_frame = tk.Frame(baseFrame)  
  right_frame.grid(row=1, column=1)
    
  insert_label = tk.Label(left_frame, text="Spent:")
  insert_label.grid(row=0, column=0)
  insert_entry = tk.Entry(left_frame)
  insert_entry.grid(row=0, column=1)
    
  insert_btn = tk.Button(left_frame, text="Insert", command=
                         partial(PandasApp.insert_line, self.insert_entry.get()))
  refresh_btn = tk.Button(left_frame, text="Refresh", command=PandasApp.refresh_table)
  insert_btn.grid(row=1, column=0)
  refresh_btn.grid(row=1, column=1)


root.mainloop()
