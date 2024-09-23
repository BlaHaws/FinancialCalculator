import tkinter as tk
import pandastable as pt
import sqlite3
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt


def insert_line():
  if insert_entry.get().isnumeric():
    df.loc[len(df.index)] = [insert_entry.get()]
  insert_entry.delete(0, 'end')
  display_table.redraw()
  print(df)


def refresh_table():
  display_table.redraw()


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
right_frame.grid(row=1, column=1, rowspan=2)

insert_label = tk.Label(left_frame, text="Spent:")
insert_label.grid(row=0, column=0)
insert_entry = tk.Entry(left_frame)
insert_entry.grid(row=0, column=1)

insert_btn = tk.Button(left_frame, text="Insert", command=insert_line)
refresh_btn = tk.Button(left_frame, text="Refresh", command=refresh_table)
insert_btn.grid(row=1, column=0)
refresh_btn.grid(row=1, column=1)

df = pd.DataFrame({'A': [1, 2, 3]})
display_table = pt.Table(right_frame,
                         dataframe=df,
                         showtoolbar=True,
                         showstatusbar=True)
display_table.show()

root.mainloop()
