from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from utilities import *

# Define and initalize data needed for function.
active = False
search_preferences_button_num_clicks = 0
potential_recipes = []
filtered_recipes = []
recipe_type = None
cook_time = None
has_all_ingredients = None

def show_find_recipe_screen(db_conn, username, user_id):

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
    generate_recipe_button_clicks = 0
    filtered_recipes_for_user = []
    def generate_a_recipe():
        # If the user only wants recipes where they have all the ingredients.
        # Get user ingredients and convert them into a set
        nonlocal generate_recipe_button_clicks
        nonlocal filtered_recipes_for_user

        # If they have already looked at all the previously searched recipes,
        # preform another search in case anything changed.
        if len(filtered_recipes_for_user) <= generate_recipe_button_clicks:
            filtered_recipes_for_user = []
            generate_recipe_button_clicks = 0
            query = "SELECT recipe_name, recipe_type, recipe_ingredients FROM recipes"
            cursor = db_conn.cursor()
            cursor.execute(query)
            all_recipes = cursor.fetchall()
            cursor.close()
            user_ingredients_set = get_user_ingredients_names_as_set(db_conn, user_id)
            # Loop through potential recipes.
            for recipe in all_recipes:
                # Get recipe ingredients as a set.
                recipe_ingredients_set = set(recipe[2].split("\t"))
                # Check if the current recipes ingredients is a subset of the users ingredients.
                if recipe_ingredients_set.issubset(user_ingredients_set):
                    # Add them to the filtered list for future use.
                    filtered_recipes_for_user.append(recipe)

        if len(filtered_recipes_for_user) <= 0:
            messagebox.showwarning("No Search Results", "No recipes found that match those filters.")
            return

        generate_recipe_button_clicks += 1
        current_recipe = filtered_recipes_for_user[generate_recipe_button_clicks - 1]
        recipe_name_field.delete(0,'end')
        recipe_ingredients_field.delete(1.0, 'end')
        recipe_cooking_method_field.delete(1.0, 'end')
        recipe_name_field.insert(0, current_recipe[0])
        recipe_ingredients_field.insert(END, current_recipe[1])
        recipe_cooking_method_field.insert(END, current_recipe[2])

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

    def has_all_ingredients_button_click(filtered_recipes):
        if len(filtered_recipes) <= 0:
            messagebox.showwarning("No Search Results", "No recipes found that match those filters.")
            return
        else:
            global search_preferences_button_num_clicks
            recipe_name_field.delete(0, 'end')
            recipe_name_field.insert(0, filtered_recipes[search_preferences_button_num_clicks][1])
            recipe_ingredients_field.delete(1.0, 'end')
            recipe_ingredients_field.insert(END, filtered_recipes[search_preferences_button_num_clicks][3])
            recipe_cooking_method_field.delete(1.0, 'end')
            recipe_cooking_method_field.insert(END, filtered_recipes[search_preferences_button_num_clicks][4])
            search_preferences_button_num_clicks += 1

    def normal_search_button_click(potential_recipes):
        if len(potential_recipes) <= 0:
            messagebox.showwarning("No Search Results", "No recipes found that match those filters.")
            return
        else:
            global search_preferences_button_num_clicks
            recipe_name_field.delete(0, 'end')
            recipe_name_field.insert(0, potential_recipes[search_preferences_button_num_clicks][1])
            recipe_ingredients_field.delete(1.0, 'end')
            recipe_ingredients_field.insert(END, potential_recipes[search_preferences_button_num_clicks][3])
            recipe_cooking_method_field.delete(1.0, 'end')
            recipe_cooking_method_field.insert(END, potential_recipes[search_preferences_button_num_clicks][4])
            search_preferences_button_num_clicks += 1

    # Searches for recipes based on the user defined filters.
    def search_for_recipe_with_preferences():
        # Initialize variables needed.
        global active
        global search_preferences_button_num_clicks
        global potential_recipes
        global filtered_recipes
        global recipe_type
        global cook_time
        global has_all_ingredients

        # Check if it is the first iteration or for any changes in the filters.
        if (active == False 
            or recipe_type_input.get() != recipe_type 
            or recipe_cook_time_input.get() != cook_time 
            or has_all_ingredients_input.get() != has_all_ingredients):

            # Reset variables for a first and/or new run.
            search_preferences_button_num_clicks = 0
            recipe_type = recipe_type_input.get()
            cook_time = recipe_cook_time_input.get()
            has_all_ingredients = has_all_ingredients_input.get()
            filtered_recipes = []
            active = True
            
            # Add the 1=1 to make adding additonal clauses easier.
            query = "SELECT * FROM recipes WHERE 1=1"
            params = []
            # Add filters dynamically.
            if recipe_type != "No Preference":
                query += " AND recipe_type = ?"
                params.append(recipe_type)
            if cook_time != "No Preference":
                query += " AND recipe_cook_time = ?"
                params.append(cook_time)

            # Execute the query.
            cursor = db_conn.cursor()
            cursor.execute(query, params)
            potential_recipes = cursor.fetchall()

            # If the user only wants recipes where they have all the ingredients.
            if has_all_ingredients == "Yes":
                # Get user ingredients and convert them into a set.
                user_ingredients_set = get_user_ingredients_names_as_set(db_conn, user_id)
                # Loop through potential recipes.
                for recipe in potential_recipes:
                    # Get recipe ingredients as a set.
                    recipe_ingredients_set = get_recipe_ingredients_names_as_set(db_conn, user_id, recipe)
                    # Check if the current recipes ingredients is a subset of the users ingredients.
                    if recipe_ingredients_set.issubset(user_ingredients_set):
                        # Add them to the filtered list for future use.
                        filtered_recipes.append(recipe)
                has_all_ingredients_button_click(filtered_recipes)

            else:
                normal_search_button_click(potential_recipes)

        # If it is not a first or new run, display the next recipe and iterate the needed values.
        # If loop has reached its end, reset it.
        else:
            if has_all_ingredients == "Yes":
                if search_preferences_button_num_clicks < len(filtered_recipes):
                    has_all_ingredients_button_click(filtered_recipes)
                else:
                    search_preferences_button_num_clicks = 0
                    active = False
                    search_for_recipe_with_preferences()

            else:
                if search_preferences_button_num_clicks < len(potential_recipes):
                    normal_search_button_click(potential_recipes)
                else:
                    search_preferences_button_num_clicks = 0
                    active = False
                    search_for_recipe_with_preferences()


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

    searched_words = []
    search_name_num_of_button_clicks = 0
    found_recipes_by_name = []

    def search_for_recipe_name():
        nonlocal searched_words
        nonlocal search_name_num_of_button_clicks
        nonlocal found_recipes_by_name

        def input_is_empty():
            if search_words_input.get() == "":
                return True
            return False

        rerun_search = False
        if not input_is_empty():
            search_words = []
            for word in search_words_input.get().split():
                if not word in searched_words:
                    rerun_search = True
                search_words.append(word.lower())

            if rerun_search:
                # Reset data since we're running another search
                searched_words = search_words
                search_name_num_of_button_clicks = 0
                # Clear existing data?


                cursor = db_conn.cursor()
                query = "SELECT recipe_name, recipe_ingredients, recipe_cooking_method FROM recipes WHERE "
                query += " AND ".join(["recipe_name LIKE ?" for _ in search_words])
                params = [f"%{foodName}%" for foodName in search_words]
                cursor.execute(query, params)
                found_recipes_by_name = cursor.fetchall()
                print(found_recipes_by_name)
                cursor.close()

            search_name_num_of_button_clicks += 1
            recipes_len = len(found_recipes_by_name)
            current_recipe = found_recipes_by_name[((search_name_num_of_button_clicks % recipes_len) - 1)]
            recipe_name_field.delete(0, 'end')
            recipe_ingredients_field.delete(1.0, 'end')
            recipe_cooking_method_field.delete(1.0, 'end')
            recipe_name_field.insert(0, current_recipe[0])
            recipe_ingredients_field.insert(END, current_recipe[1])
            recipe_cooking_method_field.insert(END, current_recipe[2])

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
