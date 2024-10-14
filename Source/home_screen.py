from pathlib import Path
from tkinter import *
from utilities import *
import mysql.connector

def show_home_screen(ing_db_conn, user_info):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets/home_screen")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("784x759")
    window.configure(bg = "#4EB276")
    window.title("Home")
    window.resizable(False, False)

    canvas = Canvas(
        window,
        bg = "#4EB276",
        height = 759,
        width = 784,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        394.0,
        403.0,
        image=image_image_1
    )
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        164.0,
        76.0,
        image=image_image_2
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))

    entry_bg_1 = canvas.create_image(
        248.0,
        401.0,
        image=entry_image_1
    )

    canvas.create_text(
        227.0,
        49.0,
        anchor="nw",
        text="Smart Recipe Builder",
        fill="#FFFFFF",
        font=("Itim Regular", 44 * -1)
    )
    canvas.create_text(
        320.0,
        108.0,
        anchor="nw",
        text=user_info['username'] + "’s Ingredients",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    # Put the table here?
    # How to create a table?
    # How to place one here?
    # How to populate it with data?

    # Use the db_conn to access and interact with the data.
    inventory_table = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    inventory_table.place(
        x=98.0,
        y=201.0,
        width=300.0,
        height=398.0
    )
    inventory_table.insert(0.0, "change to a table")

    def navigate_to_login_screen():
        from login import show_login_screen
        window.destroy()
        show_login_screen()

    logout_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=navigate_to_login_screen,
        relief="flat"
    )
    logout_button.place(
        x=16.0,
        y=726.1666870117188,
        width=88.0,
        height=22.208332061767578
    )

    def navigate_to_find_new_recipes_screen():
        print("Find New Recipe button clicked")

    find_new_recipe_button = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=navigate_to_find_new_recipes_screen,
        relief="flat"
    )
    find_new_recipe_button.place(
        x=44.0,
        y=672.4375,
        width=150.0,
        height=33.3125
    )

    def navigate_to_saved_recipes_screen():
        print("My Saved Recipes button clicked")

    saved_recipes_button = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=navigate_to_saved_recipes_screen,
        relief="flat"
    )
    saved_recipes_button.place(
        x=221.0,
        y=672.4375,
        width=146.9178009033203,
        height=33.3125
    )

    def navigate_to_add_recipe_screen():
        print("Add a Recipe button clicked")

    add_recipe_button = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=navigate_to_add_recipe_screen,
        relief="flat"
    )
    add_recipe_button.place(
        x=401.0,
        y=672.4375,
        width=150.0,
        height=33.3125
    )

    # Use the ing_db_conn and user_id to interact with specifed users data.
    def navigate_to_input_ingredients_screen():
        print("Input Ingredients button clicked")

    input_ingredients_button = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=navigate_to_input_ingredients_screen,
        relief="flat"
    )
    input_ingredients_button.place(
        x=578.0,
        y=671.4375,
        width=150.0,
        height=33.3125
    )

    button_image_hover_1 = PhotoImage(
        file=relative_to_assets("button_hover_1.png"))

    def button_1_hover(e):
        logout_button.config(
            image=button_image_hover_1
        )
    def button_1_leave(e):
        logout_button.config(
            image=button_image_1
        )

    logout_button.bind('<Enter>', button_1_hover)
    logout_button.bind('<Leave>', button_1_leave)

    button_image_hover_2 = PhotoImage(
        file=relative_to_assets("button_hover_2.png"))

    def button_2_hover(e):
        find_new_recipe_button.config(
            image=button_image_hover_2
        )
    def button_2_leave(e):
        find_new_recipe_button.config(
            image=button_image_2
        )

    find_new_recipe_button.bind('<Enter>', button_2_hover)
    find_new_recipe_button.bind('<Leave>', button_2_leave)

    button_image_hover_3 = PhotoImage(
        file=relative_to_assets("button_hover_3.png"))

    def button_3_hover(e):
        input_ingredients_button.config(
            image=button_image_hover_3
        )
    def button_3_leave(e):
        input_ingredients_button.config(
            image=button_image_3
        )

    input_ingredients_button.bind('<Enter>', button_3_hover)
    input_ingredients_button.bind('<Leave>', button_3_leave)

    button_image_hover_4 = PhotoImage(
        file=relative_to_assets("button_hover_4.png"))

    def button_4_hover(e):
        add_recipe_button.config(
            image=button_image_hover_4
        )
    def button_4_leave(e):
        add_recipe_button.config(
            image=button_image_4
        )

    add_recipe_button.bind('<Enter>', button_4_hover)
    add_recipe_button.bind('<Leave>', button_4_leave)

    button_image_hover_5 = PhotoImage(
        file=relative_to_assets("button_hover_5.png"))

    def button_5_hover(e):
        saved_recipes_button.config(
            image=button_image_hover_5
        )
    def button_5_leave(e):
        saved_recipes_button.config(
            image=button_image_5
        )

    saved_recipes_button.bind('<Enter>', button_5_hover)
    saved_recipes_button.bind('<Leave>', button_5_leave)

    window.mainloop()