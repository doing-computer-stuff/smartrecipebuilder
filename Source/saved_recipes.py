from pathlib import Path
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

#def show_saved_recipes_screen(db_conn, username, user_id):

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/saved_recipes")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("859x873+500+80")
window.configure(bg = "#4EB276")
window.title("My Recipes")
window.resizable(False, False)

canvas = Canvas(
    window,
    bg = "#4EB276",
    height = 873,
    width = 859,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    168.0,
    67.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    598.0,
    492.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    560.5,
    331.0,
    image=entry_image_1
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    560.5,
    630.0,
    image=entry_image_2
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    600.0,
    166.0,
    image=entry_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))

canvas.create_text(
    231.0,
    28.0,
    anchor="nw",
    text="Smart Recipe Builder",
    fill="#FFFFFF",
    font=("Itim Regular", 44 * -1)
)

canvas.create_text(
    321.0,
    92.0,
    anchor="nw",
    text="My Saved Recipes",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    130.0,
    221.0,
    anchor="nw",
    text="Favorites",
    fill="#FFFFFF",
    font=("Itim Regular", 24 * -1)
)

recipe_name_field = Entry(
    bd=0,
    bg="#EEEEDE",
    fg="#000716",
    highlightthickness=0
)
recipe_name_field.place(
    x=524.0,
    y=152.0,
    width=152.0,
    height=26.0
)

recipe_ingredients_field = Text(
    wrap='word',
    bd=0,
    bg="#FFF1DA",
    fg="#000716",
    highlightthickness=0
)
recipe_ingredients_field.place(
    x=425.0,
    y=244.0,
    width=271.0,
    height=172.0
)

recipe_cooking_method_field = Text(
    wrap='word',
    bd=0,
    bg="#FFF1DA",
    fg="#000716",
    highlightthickness=0
)
recipe_cooking_method_field.place(
    x=425.0,
    y=494.0,
    width=271.0,
    height=270.0
)

# create and style saved recipe list
style = ttk.Style(window)
style.theme_use("clam")
style.configure("Treeview", background="#D9D9D9", fieldbackground="#D9D9D9", borderdwidth=0, relief="flat")
style.map('Treeview', background=[('selected', '#284846')])
recipe_list = ttk.Treeview(window, columns=("Recipe"), show="headings", style="Treeview", selectmode="browse")

recipe_list.heading("Recipe", text="Recipe")
recipe_list.column("Recipe", width="300", anchor="c")
recipe_list.place(x=26, y=261, width=304, height=400)
recipe_list.insert("", tk.END, values=(("Street Tacos"),))
recipe_list.insert("", tk.END, values=(("Lasagna"),))
recipe_list.insert("", tk.END, values=(("Sweet and Spicy Chilli"),))

def view_selected_recipe():
    selected_recipe = recipe_list.focus()
    if len(selected_recipe) == 0:
        messagebox.showinfo("Selection Required", "Select a Recipe from the list to view it.")
        return
    else:
        recipe_name_field.delete(0, 'end')
        recipe_name_field.insert(0, recipe_list.item(selected_recipe)['values'][0])
        recipe_ingredients_field.delete(1.0, 'end')
        recipe_ingredients_field.insert(1.0, "Ingredients for " + recipe_list.item(selected_recipe)['values'][0])
        recipe_cooking_method_field.delete(1.0, 'end')
        recipe_cooking_method_field.insert(1.0 , "Cooking method for " + recipe_list.item(selected_recipe)['values'][0])

view_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=view_selected_recipe,
    relief="flat"
)
view_button.place(
    x=46.0,
    y=677.0,
    width=98.0,
    height=30.75
)

def remove_selected_recipe():
    selected_recipe = recipe_list.selection()
    if len(selected_recipe) == 0:
        messagebox.showinfo("Selection Required", "Select a Recipe from the list to remove it.")
        return
    else:
        recipe_list.delete(selected_recipe)
        recipe_name_field.delete(0, 'end')
        recipe_ingredients_field.delete(1.0, 'end')
        recipe_cooking_method_field.delete(1.0, 'end')

remove_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=remove_selected_recipe,
    relief="flat"
)
remove_button.place(
    x=210.0,
    y=677.0,
    width=98.0,
    height=30.75
)

def navigate_to_home_screen():
    print("back button clicked")
    # from home_screen import show_home_screen
    # window.destroy()
    # show_home_screen(db_conn, username, user_id)

back_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=navigate_to_home_screen,
    relief="flat"
)
back_button.place(
    x=12.0,
    y=830.0,
    width=98.0,
    height=30.75
)

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
    remove_button.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    remove_button.config(
        image=button_image_2
    )

remove_button.bind('<Enter>', button_2_hover)
remove_button.bind('<Leave>', button_2_leave)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))


def button_3_hover(e):
    view_button.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    view_button.config(
        image=button_image_3
    )

view_button.bind('<Enter>', button_3_hover)
view_button.bind('<Leave>', button_3_leave)

window.mainloop()