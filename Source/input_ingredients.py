from pathlib import Path
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
from datetime import *

def show_input_ingredients_screen(db_conn, username, user_id):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets/input_ingredients")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("784x623")
    window.configure(bg = "#4EB276")
    window.title("My Ingredients")
    window.resizable(False, False)

    canvas = Canvas(
        window,
        bg = "#4EB276",
        height = 623,
        width = 784,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)

    canvas.create_text(
        232.0,
        42.0,
        anchor="nw",
        text="Smart Recipe Builder",
        fill="#FFFFFF",
        font=("Itim Regular", 44 * -1)
    )

    canvas.create_text(
        315.0,
        111.0,
        anchor="nw",
        text="Input Ingredients",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        58.0,
        155.0,
        anchor="nw",
        text="Name:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    canvas.create_text(
        59.0,
        232.0,
        anchor="nw",
        text="Quantity:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    canvas.create_text(
        193.0,
        232.0,
        anchor="nw",
        text="Units:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    canvas.create_text(
        59.0,
        308.0,
        anchor="nw",
        text="Expiration Date:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        248.0,
        491.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        169.0,
        69.0,
        image=image_image_2
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        180.5,
        199.5,
        image=entry_image_1
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        248.0,
        275.5,
        image=entry_image_2
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        180.5,
        350.5,
        image=entry_image_3
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        114.0,
        275.5,
        image=entry_image_4
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))

    def navigate_to_home_screen():
        from home_screen import show_home_screen
        window.destroy()
        show_home_screen(db_conn, username, user_id)

    back_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=navigate_to_home_screen,
        relief="flat"
    )
    back_button.place(
        x=10.0,
        y=583.0,
        width=98.0,
        height=30.75
    )

    def add_ingredient():

        def no_blank_fields():
            if (ingredient_name_input.get() and quantity_input.get() and expiration_date_input.get()) != "":
                return True
            return False

        def ingredient_name_is_valid():
            ingredient_name = ingredient_name_input.get()
            if len(ingredient_name) <= 50:
                return True
            return False

        def quantity_is_valid():
            quantity = quantity_input.get()
            if (quantity.isnumeric() and int(quantity) >= 0 and int(quantity) < 99999):
                return True
            return False

        def quantity_with_units_length_is_valid():
            if units_input.get() == "none":
                quantity = quantity_input.get()
            else:
                quantity = quantity_input.get() + " " + units_input.get()
            if len(quantity) <= 15:
                return True
            return False

        def is_correct_date_format():
            date = expiration_date_input.get()
            pattern = r"[0-1][0-9]\/[0-3][0-9]\/[0-2][0-2][0-9][0-9]"
            if re.match(pattern, date):
                return True
            return False

        def insert_into_database(ingredient_name, expiration_date, quantity, user_id):
            cursor = db_conn.cursor()
            cursor.execute("INSERT INTO ingredients (food_name, expiration_date, quantity, user_id) VALUES (?, ?, ?, ?)", (ingredient_name, expiration_date, quantity, user_id))
            db_conn.commit()
            
            # Update table view after adding ingredient.
            cursor.execute("SELECT food_name, expiration_date, quantity FROM ingredients WHERE user_id = ?", (user_id,))
            user_inventory = cursor.fetchall()
            for row in ingredients_table.get_children():
                ingredients_table.delete(row)
            user_inventory_sorted_by_date = sorted(user_inventory, key=lambda x: datetime.strptime(x[1], "%m/%d/%Y"))
            iid = 0
            for item in user_inventory_sorted_by_date:
                ingredients_table.insert(parent="", index="end", iid=iid,values=(item[0], item[1], item[2]))
                iid += 1
            db_conn.commit()
            cursor.close()

        if no_blank_fields() and ingredient_name_is_valid() and quantity_is_valid() and quantity_with_units_length_is_valid() and is_correct_date_format():
            ingredient_name = ingredient_name_input.get()
            if units_input.get() == "none":
                quantity = quantity_input.get()
            else:
                quantity = quantity_input.get() + " " + units_input.get()
            expiration_date = expiration_date_input.get()
            insert_into_database(ingredient_name, expiration_date, quantity, user_id)
        elif not no_blank_fields():
            messagebox.showwarning("Empty Input Fields", "Please enter all required information.")
        elif not ingredient_name_is_valid():
            messagebox.showwarning("Invalid Product Name", "The product name length is too long.")
        elif not quantity_is_valid():
            messagebox.showwarning("Invalid Quantity", "Please adjust the quantity.")
        elif not quantity_with_units_length_is_valid():
            messagebox.showwarning("Invalid Units", "The quantity with units added is too long.")
        else:
            messagebox.showwarning("Invalid Date", "Please use date format 01/05/2020.")

    add_button = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=add_ingredient,
        relief="flat"
    )
    add_button.place(
        x=58.0,
        y=423.0,
        width=98.0,
        height=30.75
    )

    def remove_ingredient():
        selected_ingredients = ingredients_table.selection()
        if len(selected_ingredients) == 0:
            messagebox.showinfo("Selection Required", "Select an ingredient from the table to remove it.\nHold the CTRL key to select or unselect multiple ingredients.")
            return

        else:
            cursor = db_conn.cursor()
            for ingredient in selected_ingredients:
                column_values = ingredients_table.item(ingredient)
                ingredient_name = column_values['values'][0]
                expiration_date = column_values['values'][1]
                cursor.execute("DELETE FROM ingredients WHERE food_name = ? and expiration_date = ? and user_id = ?", (ingredient_name, expiration_date, user_id))
                db_conn.commit()
                ingredients_table.delete(ingredient)
            cursor.close()

    remove_button = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=remove_ingredient,
        relief="flat"
    )
    remove_button.place(
        x=58.0,
        y=477.0,
        width=98.0,
        height=30.75
    )

    ingredient_name_input = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    ingredient_name_input.insert(0, "Product Name")
    ingredient_name_input.place(
        x=63.0,
        y=179.0,
        width=235.0,
        height=39.0
    )

    style = ttk.Style(window)
    style.configure("TCombobox", background="#D9D9D9", fieldbackground="#D9D9D9")
    style.map("TCombobox", background=[("selected", "#284846")])
    units_input = ttk.Combobox(window, state="readonly", width=13,
                               values=("none", "bag", "bags", "box", "boxes", "can", "cans", "cup", "cups", "gallon",
                                       "gallons", "loaf", "loaves", "ounce", "ounces", "package", "packages", "pound",
                                       "pounds", "quart", "quarts"), style="TCombobox")
    units_input.set("none")
    units_input.place(anchor="nw", x=200, y=266)

    expiration_date_input = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    expiration_date_input.insert(0, "mm/dd/yyyy")
    expiration_date_input.place(
        x=63.0,
        y=330.0,
        width=235.0,
        height=39.0
    )

    quantity_input = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    quantity_input.insert(0, "0")
    quantity_input.place(
        x=64.0,
        y=255.0,
        width=100.0,
        height=39.0
    )

    # initial table setup
    style.theme_use("clam")
    style.configure("Treeview", background="#D9D9D9", fieldbackground="#D9D9D9", borderdwidth=0, relief="flat")
    style.map('Treeview', background=[('selected', '#284846')])
    ingredients_table = ttk.Treeview(window, columns=("Product", "Expiration Date", "Quantity"), show="headings", style="Treeview")

    ingredients_table.heading("Product", text="Product")
    ingredients_table.column("Product", width="130", anchor="c", stretch=NO)
    ingredients_table.heading("Expiration Date", text="Expiration Date")
    ingredients_table.column("Expiration Date", width="130", anchor="c", stretch=NO)
    ingredients_table.heading("Quantity", text="Quantity")
    ingredients_table.column("Quantity", width="130", anchor="c", stretch=NO)

    cursor = db_conn.cursor()
    cursor.execute("SELECT food_name, expiration_date, quantity FROM ingredients WHERE user_id = ?", (user_id,))
    user_inventory = cursor.fetchall()
    cursor.close()
    user_inventory_sorted_by_date = sorted(user_inventory, key=lambda x: datetime.strptime(x[1], "%m/%d/%Y"))
    iid = 0
    for item in user_inventory_sorted_by_date:
        ingredients_table.insert(parent="", index="end", iid=iid, values=(item[0], item[1], item[2]))
        iid += 1

    ingredients_table.place(x=340, y=179, width=390, height=378)

    def open_expiration_date_help_window():
        from expiration_help_window import show_expiration_help_window
        show_expiration_help_window()

    help_link = tk.Button(window, text="Help Me With Expiration Dates", font=("Inter Bold", 14 * -1, "underline"),
                                        fg="#ffffff", activeforeground="#284846", bg="#4EB276", activebackground="#4EB276", bd=0, command=open_expiration_date_help_window)
    help_link.place(x=59, y=378)

    button_image_hover_1 = PhotoImage(
        file=relative_to_assets("button_hover_1.png"))

    def button_1_hover(e):
        back_button.config(
            image=button_image_hover_1
        )
    def button_1_leave(e):
        back_button.config(
            image=button_image_1
        )

    back_button.bind('<Enter>', button_1_hover)
    back_button.bind('<Leave>', button_1_leave)


    button_image_hover_2 = PhotoImage(
        file=relative_to_assets("button_hover_2.png"))

    def button_2_hover(e):
        add_button.config(
            image=button_image_hover_2
        )
    def button_2_leave(e):
        add_button.config(
            image=button_image_2
        )

    add_button.bind('<Enter>', button_2_hover)
    add_button.bind('<Leave>', button_2_leave)

    button_image_hover_3 = PhotoImage(
        file=relative_to_assets("button_hover_3.png"))

    def button_3_hover(e):
        remove_button.config(
            image=button_image_hover_3
        )
    def button_3_leave(e):
        remove_button.config(
            image=button_image_3
        )

    remove_button.bind('<Enter>', button_3_hover)
    remove_button.bind('<Leave>', button_3_leave)

    window.mainloop()
