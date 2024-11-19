from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

#def show_find_recipe_screen(db_conn, username, user_id):

db_path = "smartrecipebuilder.db"
db_conn = sqlite3.connect(db_path)

user_id = 4  # or whatever your account is

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/find_recipe")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("859x920+500+50")
window.configure(bg = "#4EB276")
window.title("Find a Recipe")
window.resizable(False, False)

canvas = Canvas(
    window,
    bg = "#4EB276",
    height = 920,
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
    583.0,
    492.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    545.5,
    330.5,
    image=entry_image_1
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    545.5,
    630.5,
    image=entry_image_2
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    584.5,
    166.0,
    image=entry_image_3
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    178.5,
    409.5,
    image=entry_image_4
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    178.5,
    482.5,
    image=entry_image_5
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    178.5,
    560.5,
    image=entry_image_6
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    178.5,
    762.5,
    image=entry_image_7
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

canvas.create_text(
    231.0,
    28.0,
    anchor="nw",
    text="Smart Recipe Builder",
    fill="#FFFFFF",
    font=("Itim Regular", 44 * -1)
)

canvas.create_text(
    323.0,
    92.0,
    anchor="nw",
    text="Find New Recipes",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    38.0,
    166.0,
    anchor="nw",
    text="Show me a recipe that uses all\n        my ingredients now!",
    fill="#FFFFFF",
    font=("Itim Regular", 21 * -1)
)

canvas.create_text(
    62.0,
    661.0,
    anchor="nw",
    text="",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    162.0,
    649.0,
    anchor="nw",
    text="Or",
    fill="#FFFFFF",
    font=("Itim Regular", 21 * -1)
)

canvas.create_text(
    60.0,
    701.0,
    anchor="nw",
    text="",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    60.0,
    189.0,
    anchor="nw",
    text="",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    62.0,
    303.0,
    anchor="nw",
    text="",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    162.0,
    276.0,
    anchor="nw",
    text="Or",
    fill="#FFFFFF",
    font=("Itim Regular", 21 * -1)
)

canvas.create_text(
    60.0,
    332.0,
    anchor="nw",
    text="",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    38.0,
    309.0,
    anchor="nw",
    text="Let’s select some preferences \n                   first!",
    fill="#FFFFFF",
    font=("Itim Regular", 21 * -1)
)

canvas.create_text(
    56.0,
    365.0,
    anchor="nw",
    text="Recipe Type:",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    57.0,
    439.0,
    anchor="nw",
    text="Cook Time:",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    57.0,
    516.0,
    anchor="nw",
    text="Have all Ingredients?:",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    56.0,
    718.0,
    anchor="nw",
    text="Recipe Name Includes:",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    103.0,
    680.0,
    anchor="nw",
    text="Search by name!",
    fill="#FFFFFF",
    font=("Itim Regular", 21 * -1)
)

canvas.create_text(
    460.0,
    865.0,
    anchor="nw",
    text="Add to Favorites?",
    fill="#FFFFFF",
    font=("Itim Regular", 21 * -1)
)

recipe_name_field = Entry(
    bd=0,
    bg="#EEEEDE",
    fg="#000716",
    highlightthickness=0
)

recipe_name_field.place(
    x=502.0,
    y=152.0,
    width=165.0,
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
    x=410.0,
    y=244.0,
    width=271.0,
    height=171.0
)

recipe_cooking_method_field = Text(
    wrap='word',
    bd=0,
    bg="#FFF1DA",
    fg="#000716",
    highlightthickness=0
)

recipe_cooking_method_field.place(
    x=410.0,
    y=494.0,
    width=271.0,
    height=271.0
)

# use to cycle through found recipes
show_recipe_button_num_clicks = 0

# fetch all recipes from the database that match the users ingredients and cycle through with button click
def generate_a_recipe():

    global show_recipe_button_num_clicks
    recipe_name_field.delete(0,'end')
    recipe_ingredients_field.delete(1.0, 'end')
    recipe_cooking_method_field.delete(1.0, 'end')
    print("Show a Recipe button clicked, fetch all recipes that include the user's ingredients then show one for each click")
    recipes = ["Recipe 1", "Recipe 2", "Recipe 3"]
    if show_recipe_button_num_clicks < len(recipes):
        recipe_name_field.insert(0, recipes[show_recipe_button_num_clicks])
        recipe_ingredients_field.insert(END, "Ingredents for " + recipes[show_recipe_button_num_clicks])
        recipe_cooking_method_field.insert(END, "Cooking method for " + recipes[show_recipe_button_num_clicks])
        show_recipe_button_num_clicks += 1
    else:
        show_recipe_button_num_clicks = 0
        generate_a_recipe()

show_a_recipe_now_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=generate_a_recipe,
    relief="flat"
)

show_a_recipe_now_button.place(
    x=80.0,
    y=230.4375,
    width=198.0,
    height=33.3125
)

# dropdowns for search preferences inputs
style = ttk.Style(window)
style.theme_use("clam")
style.configure("TCombobox", background="#D9D9D9", fieldbackground="#D9D9D9")
style.map("TCombobox", background=[("selected", "#284846")])

recipe_type_input = ttk.Combobox(window, state="readonly", width=35,
                                 values=("No Preference", "Breakfast", "Lunch", "Dinner", "Snack"), style="TCombobox")
recipe_type_input.set("No Preference")
recipe_type_input.place(anchor="nw", x=63, y=400)

recipe_cook_time_input = ttk.Combobox(window, state="readonly", width=35,
                                 values=("No Preference", "Under 30 Minutes", "30 Minutes to 1 Hour", "1 to 2 Hours", "2+ Hours"), style="TCombobox")
recipe_cook_time_input.set("No Preference")
recipe_cook_time_input.place(anchor="nw", x=63, y=473)

has_all_ingredients_input = ttk.Combobox(window, state="readonly", width=35, values=("Yes", "No"), style="TCombobox")
has_all_ingredients_input.set("Yes")
has_all_ingredients_input.place(anchor="nw", x=63, y=550)

def search_for_recipe_with_preferences():
    recipe_type = recipe_type_input.get()
    cook_time = recipe_cook_time_input.get()
    has_all_ingredients = has_all_ingredients_input.get()
    print(recipe_type)
    print(cook_time)
    print(has_all_ingredients)

find_with_preferences_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=search_for_recipe_with_preferences,
    relief="flat"
)

find_with_preferences_button.place(
    x=80.0,
    y=602.4375,
    width=198.0,
    height=33.3125
)

search_words_input = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)

search_words_input.place(
    x=61.0,
    y=742.0,
    width=235.0,
    height=39.0
)

# search for a recipe by name based on user entered keywords, creates an array of lowercase words,
# match them to lowercase words in the recipe names pulled from the database
def search_for_recipe_name():

    def input_is_empty():
        if search_words_input.get() == "":
            return True
        return False


    if not input_is_empty():
        search_words = []
        for word in search_words_input.get().split():
            search_words.append(word.lower())
        cursor = db_conn.cursor()
        query = "SELECT recipe_name, recipe_ingredients, recipe_cooking_method FROM recipes WHERE "
        query += " AND ".join(["recipe_name LIKE ?" for _ in search_words])
        params = [f"%{foodName}%" for foodName in search_words]
        cursor.execute(query, params)
        user_recipes = cursor.fetchall()
        cursor.close()
        print(user_recipes)

        # Clear existing data?
        recipe_name_field.delete(0, 'end')
        recipe_ingredients_field.delete(1.0, 'end')
        recipe_cooking_method_field.delete(1.0, 'end')

        for recipe in user_recipes:
            recipe_name_field.insert(0, recipe[0])
            recipe_ingredients_field.insert(END, recipe[1])
            recipe_cooking_method_field.insert(END, recipe[2])

    else:
        messagebox.showwarning("Empty Search Field", "Please enter search term(s).")
        print(search_words_input.get().lower())



search_by_name_button = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=search_for_recipe_name,
    relief="flat"
)

search_by_name_button.place(
    x=79.0,
    y=805.4375,
    width=198.0,
    height=33.3125
)

# when button is clicked to favorite recipe, add the currently shown recipe_id to the user's saved recipes array in database
def add_current_recipe_to_users_saved_recipes():
    print("This recipe is favorited")

add_to_favorites_button = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=add_current_recipe_to_users_saved_recipes,
    relief="flat"
)
add_to_favorites_button.place(
    x=632.0,
    y=862.0,
    width=76.0,
    height=31.0
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
    x=11.0,
    y=878.0,
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
    show_a_recipe_now_button.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    show_a_recipe_now_button.config(
        image=button_image_2
    )

show_a_recipe_now_button.bind('<Enter>', button_2_hover)
show_a_recipe_now_button.bind('<Leave>', button_2_leave)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

def button_3_hover(e):
    find_with_preferences_button.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    find_with_preferences_button.config(
        image=button_image_3
    )

find_with_preferences_button.bind('<Enter>', button_3_hover)
find_with_preferences_button.bind('<Leave>', button_3_leave)

button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

def button_4_hover(e):
    search_by_name_button.config(
        image=button_image_hover_4
    )
def button_4_leave(e):
    search_by_name_button.config(
        image=button_image_4
    )

search_by_name_button.bind('<Enter>', button_4_hover)
search_by_name_button.bind('<Leave>', button_4_leave)

button_image_hover_5 = PhotoImage(
    file=relative_to_assets("button_hover_5.png"))

def button_5_hover(e):
    add_to_favorites_button.config(
        image=button_image_hover_5
    )
def button_5_leave(e):
    add_to_favorites_button.config(
        image=button_image_5
    )

add_to_favorites_button.bind('<Enter>', button_5_hover)
add_to_favorites_button.bind('<Leave>', button_5_leave)

window.mainloop()