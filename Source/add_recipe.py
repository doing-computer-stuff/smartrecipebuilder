from pathlib import Path
from tkinter import *
from tkinter import ttk, messagebox

#def show_add_recipe_screen(db_conn, username, user_id):

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/add_recipe")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("703x986+500+15")
window.configure(bg = "#4EB276")
window.title("Add a Recipe")
window.resizable(False, False)

canvas = Canvas(
    window,
    bg = "#4EB276",
    height = 986,
    width = 703,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)


image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    350.0,
    481.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    123.0,
    61.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    311.5,
    324.0,
    image=entry_image_1
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    311.5,
    625.5,
    image=entry_image_2
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    424.5,
    876.5,
    image=entry_image_3
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    113.5,
    876.5,
    image=entry_image_4
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    582.5,
    876.5,
    image=entry_image_5
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    268.5,
    876.5,
    image=entry_image_6
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    353.0,
    166.5,
    image=entry_image_7
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))

canvas.create_text(
    186.0,
    34.0,
    anchor="nw",
    text="Smart Recipe Builder",
    fill="#FFFFFF",
    font=("Itim Regular", 44 * -1)
)

canvas.create_text(
    287.0,
    93.0,
    anchor="nw",
    text="Add a Recipe",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    329.0,
    122.0,
    anchor="nw",
    text="Name:",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    69.0,
    837.0,
    anchor="nw",
    text="Recipe Type:",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    230.0,
    837.0,
    anchor="nw",
    text="Cook Time:",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    366.0,
    837.0,
    anchor="nw",
    text="Make Shareable?",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    523.0,
    837.0,
    anchor="nw",
    text="Add to Favorites?",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

recipe_name_field = Entry(
    bd=0,
    bg="#EEEEDE",
    fg="#000716",
    highlightthickness=0
)
recipe_name_field.place(
    x=272.0,
    y=153.0,
    width=162.0,
    height=25.0
)

recipe_ingredients_field = Text(
    wrap='word',
    bd=0,
    bg="#FFF1DA",
    fg="#000716",
    highlightthickness=0
)
recipe_ingredients_field.place(
    x=183.0,
    y=239.0,
    width=257.0,
    height=168.0
)


recipe_cooking_method_field = Text(
    wrap='word',
    bd=0,
    bg="#FFF1DA",
    fg="#000716",
    highlightthickness=0
)
recipe_cooking_method_field.place(
    x=183.0,
    y=504.0,
    width=257.0,
    height=241.0
)

# dropdowns for input boxes
style = ttk.Style(window)
style.theme_use("clam")
style.configure("TCombobox", background="#D9D9D9", fieldbackground="#D9D9D9")
style.map("TCombobox", background=[("selected", "#284846")])

recipe_type_input = ttk.Combobox(window, state="readonly", width=12,
                                 values=("Breakfast", "Lunch", "Dinner", "Snack"), style="TCombobox")
recipe_type_input.place(anchor="nw", x=69, y=868)

recipe_cook_time_input = ttk.Combobox(window, state="readonly", width=12, values=("Under 30 Minutes",
                                     "30 Minutes to 1 Hour", "1 to 2 Hours", "2+ Hours"), style="TCombobox")
recipe_cook_time_input.place(anchor="nw", x=223, y=868)

make_shareable_input = ttk.Combobox(window, state="readonly", width=12, values=("Yes", "No"), style="TCombobox")
make_shareable_input.place(anchor="nw", x=380, y=868)

add_to_favorites_input = ttk.Combobox(window, state="readonly", width=12, values=("Yes", "No"), style="TCombobox")
add_to_favorites_input.place(anchor="nw", x=538, y=868)

# add the user provided recipe to the database
def add_recipe():
    recipe_name = recipe_name_field.get()
    recipe_ingredients = recipe_ingredients_field.get("1.0", "end-1c")
    recipe_cooking_method = recipe_cooking_method_field.get("1.0", "end-1c")
    recipe_type = recipe_type_input.get()
    cook_time = recipe_cook_time_input.get()
    is_shareable = make_shareable_input.get()
    add_to_favorites = add_to_favorites_input.get()
    print(recipe_name)
    print(recipe_ingredients)
    print(recipe_cooking_method)
    print(recipe_type)
    print(cook_time)
    print(is_shareable)
    print(add_to_favorites)

add_recipe_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=add_recipe,
    relief="flat"
)
add_recipe_button.place(
    x=252.0,
    y=911.43,
    width=198.0,
    height=33.3
)

def undo_add_recipe():
    print("undo button clicked")

undo_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=undo_add_recipe,
    relief="flat"
)
undo_button.place(
    x=610.0,
    y=956.08,
    width=81.0,
    height=21.35
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
    y=948.0,
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
    add_recipe_button.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    add_recipe_button.config(
        image=button_image_2
    )

add_recipe_button.bind('<Enter>', button_2_hover)
add_recipe_button.bind('<Leave>', button_2_leave)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

def button_3_hover(e):
    undo_button.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    undo_button.config(
        image=button_image_3
    )

undo_button.bind('<Enter>', button_3_hover)
undo_button.bind('<Leave>', button_3_leave)

window.mainloop()