from pathlib import Path
import tkinter as tk
from tkinter import ttk

def show_expiration_help_window():

    # Create the window
    window = tk.Tk()
    window.geometry("300x250")
    window.configure(bg="#4EB276")
    window.title("Expiration Date Guidelines")
    window.resizable(False, False)

    # Define Table Styling
    style = ttk.Style(window)
    style.theme_use("clam")
    style.configure("Treeview", background="#D9D9D9", fieldbackground="#D9D9D9", borderdwidth=0, relief="flat")
    style.map('Treeview', background=[('selected', '#284846')])

    # Create the Treeview
    table = ttk.Treeview(window, columns=("Column 1", "Column 2"), show="headings", style="Treeview")

    # Define the headings
    table.heading("Column 1", text="Product")
    table.column("Column 1", width="150", anchor="c")
    table.heading("Column 2", text="Shelf Life")
    table.column("Column 2", width="150", anchor="c")

    # Insert some grocery data
    table.insert("", tk.END, values=("Tomatoes", "5-7 Days"))
    table.insert("", tk.END, values=("Leafy Greens", "10-12 Days"))
    table.insert("", tk.END, values=("Celery", "14-21 Days"))
    table.insert("", tk.END, values=("Avocados", "7-14 Days"))
    table.insert("", tk.END, values=("Apples", "30 Days"))
    table.insert("", tk.END, values=("Oranges", "14 Days"))
    table.insert("", tk.END, values=("Strawberries", "3-5 Days"))
    table.insert("", tk.END, values=("Watermelon", "6-8 Days"))
    table.insert("", tk.END, values=("Bananas", "5-7 Days"))
    table.insert("", tk.END, values=("Onions", "60-90 Days"))
    table.insert("", tk.END, values=("Mushrooms", "7-8 Days"))
    table.insert("", tk.END, values=("Potatoes", "21-35 Days"))

    # Pack the table
    table.pack(expand=1)