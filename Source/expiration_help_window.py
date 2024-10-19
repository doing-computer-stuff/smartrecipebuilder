from pathlib import Path
import tkinter as tk
from tkinter import ttk

def show_expiration_help_window():

    # Create the window
    window = tk.Tk()
    window.geometry("400x400")
    window.configure(bg="white")
    window.title("Expiration Date Guidelines")
    window.resizable(False, False)

    # Create the Treeview
    table = ttk.Treeview(window, columns=("Column 1", "Column 2"), show="headings")

    # Define the headings
    table.heading("Column 1", text="Product")
    table.heading("Column 2", text="Shelf Life")

    # Insert some grocery data
    table.insert("", tk.END, values=("Bread", "1 Week"))
    table.insert("", tk.END, values=("Flour", "12 Months"))
    table.insert("", tk.END, values=("Canned Goods", "2-5 Years"))
    table.insert("", tk.END, values=("Butter", "1-3 Months"))
    table.insert("", tk.END, values=("Cheese", "3-4 Weeks"))
    table.insert("", tk.END, values=("Canned Goods", "2-5 Years"))
    table.insert("", tk.END, values=("Eggs", "3-5 Weeks"))
    table.insert("", tk.END, values=("Apple", "1-2 Months"))
    table.insert("", tk.END, values=("Carrots", "1-2 Months"))
    table.insert("", tk.END, values=("Onions", "1-3 Months"))
    table.insert("", tk.END, values=("Bananas", "1 Week"))

    # Pack the table
    table.pack()

    # Run the main loop
    window.mainloop()
