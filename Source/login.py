from pathlib import Path
from tkinter import *
from tkinter import messagebox
import tkinter as tk
#from PIL import Image
import mysql.connector
import hashlib
from utilities import *

def show_login_screen(db_conn):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets/login_screen")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # create window and canvas, and center on screen
    window = Tk()
    # screen_width = window.winfo_width()
    # screen_height = window.winfo_height()
    # app_width = 700
    # app_height = 436
    # x = (screen_width / 2) - (app_width / 2)
    # y = (screen_height / 2) - (app_height / 2)
    # window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
    window.geometry("700x436")
    window.configure(bg="#4EB276")
    window.title("Login")
    window.resizable(False, False)

    canvas = Canvas(
        window,
        bg = "#4EB276",
        height = 436,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)

    # place images
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        126.0,
        72.0,
        image=image_image_2
    )
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        538.5,
        189.5,
        image=entry_image_1
    )
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        538.5,
        259.5,
        image=entry_image_2
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))

    # place text
    canvas.create_text(
        189.0,
        45.0,
        anchor="nw",
        text="Smart Recipe Builder",
        fill="#FFFFFF",
        font=("Itim Regular", 44 * -1)
    )
    canvas.create_text(
        59.0,
        140.0,
        anchor="nw",
        text="Welcome to Smart Recipe Builder!\n\n  Let’s take the guesswork out of\n           your meal planning! ",
        fill="#FFFFFF",
        font=("Itim Regular", 22 * -1)
    )
    canvas.create_text(
        416.0,
        146.0,
        anchor="nw",
        text="Username:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )
    canvas.create_text(
        416.0,
        216.0,
        anchor="nw",
        text="Password:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    # place entry fields
    username_input = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    username_input.place(
        x=421.0,
        y=169.0,
        width=235.0,
        height=39.0
    )

    password_input = Entry(
        show="*",
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    password_input.place(
        x=421.0,
        y=239.0,
        width=235.0,
        height=39.0
    )

    # Method to check whether the given username and password are in the database.
    # Returns true if there is at least one row with the given username AND password.
    def verify_login_credentials(username, password):

        # Create a cursor to execute SQL commands.
        cursor = db_conn.cursor(dictionary = True)

        # Execute query to see whether user exists.
        cursor.execute(
        "SELECT user_password FROM users WHERE username = %s",
        (username,))

        # Under assumption usernames are unique!
        db_password = cursor.fetchall()[0]["user_password"]
        
        # Commit changes to the database and close connection to cursor.
        cursor.close()

        return compare_passwords(db_password, password)

    # Method to check whether the given username and password are in the database.
    def get_user_info(username):
        # Create a cursor to execute SQL commands.
        cursor = db_conn.cursor(dictionary=True)

        # Execute query to see whether user exists.
        cursor.execute(f"SELECT username, user_id FROM users WHERE username = '{username}'")

        # Grab the id of the user
        # This could cause issues or incorrect behavior if 
        # usernames are not unique
        result = cursor.fetchone()

        # Commit changes to the database and close connection to cursor.
        cursor.close()

        return result


    # links and functions for create account and reset password
    def navigate_to_create_account():
        from create_account import show_create_account
        window.destroy()
        show_create_account(db_conn)

    create_account_link = tk.Button(window, text="Create New Account", font=("Inter Bold", 14 * -1, "underline"),
                                    fg="#ffffff", activeforeground="#284846", bg="#4EB276", activebackground="#4EB276", bd=0, command=navigate_to_create_account)
    create_account_link.place(x=468, y=360)

    def navigate_to_reset_passsword():
        from reset_password import show_reset_password
        window.destroy()
        show_reset_password(db_conn)

    reset_password_link = tk.Button(window, text="Forgot Password", font=("Inter Bold", 14 * -1, "underline"), \
                                    fg="#ffffff", activeforeground="#284846", bg="#4EB276", activebackground="#4EB276", bd=0, command=navigate_to_reset_passsword)
    reset_password_link.place(x=480, y=383)


    # login button and function
    def login():
        from home_screen import show_home_screen
        # Just placeholder code, the user_info passed to home_screen will be in associative array form already, returns that way from db query.
        username = username_input.get()
        password = password_input.get()

        # Check if username and password are in user database.
        # If all is good, connect to the database, get the users unique id, and send them to the homescreen.
        if verify_login_credentials(username, password):

            # Use the user database to get the users unique ID
            # and store it here.
            user_info = get_user_info(username)

            window.destroy()

            # Pass the database connection and user ID here.
            show_home_screen(db_conn, user_info['username'], user_info['user_id'])
        else:
            messagebox.showwarning("Invalid Credentials", "Incorrect username or password.")
            print("log in with 'user' and 'password'")

    login_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=login,
        relief="flat"
    )
    login_button.place(
        x=454.0,
        y=303.0,
        width=169.0,
        height=41.0
    )

    # button hover effects
    button_image_hover_1 = PhotoImage(
        file=relative_to_assets("button_hover_1.png"))

    def button_1_hover(e):
        login_button.config(
            image=button_image_hover_1
        )
    def button_1_leave(e):
        login_button.config(
            image=button_image_1
        )

    login_button.bind('<Enter>', button_1_hover)
    login_button.bind('<Leave>', button_1_leave)

    ### disable this before trying to enable gif
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        219.0,
        336.0,
        image=image_image_1
    )
    ###

    ##################################
    # gif animation for login page, not working correctly
    # gifImage = ".\\assets\\login_screen\\logingif.gif"
    # openImage = Image.open(gifImage)
    # frames = openImage.n_frames
    # imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
    # count = 0
    # showAnimation = None
    #
    # def animation(count):
    #     global showAnimation
    #     newImage = imageObject[count]
    #
    #     gif_Label.configure(image=newImage)
    #     count += 1
    #     if count == frames:
    #         count = 0
    #
    #     showAnimation = window.after(80, lambda: animation(count))
    #
    # gif_Label = Label(window, image="")
    # gif_Label.place(x=122, y=260, width=194, height=145)
    #
    # animation(count)
    ##################################

    window.mainloop()
