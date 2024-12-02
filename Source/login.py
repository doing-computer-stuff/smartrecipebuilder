"""Module supplies login functionality.
"""
from pathlib import Path
from tkinter import *
from tkinter import messagebox
import tkinter as tk
#from PIL import Image
from utilities import *

def show_login_screen(db_conn):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets/login_screen")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    """Create window and canvas and center on screen."""
    window = Tk()
    window.geometry("700x436+500+80")
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

    """Place images."""
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

    """Place text."""
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

    """Place entry fields."""
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


    """Links and functions for create account and reset password."""
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

    def login():
        """Logs the user in and does authentication.
        """
        from home_screen import show_home_screen

        def valid_username(username):
            """Verifies that the username exists in the db.
            
            Args:
                username (string): Users username.
            """
            cursor = db_conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            cursor.close()
            if result[0] == 0:
                return False
            return True

        def verify_login_credentials(username, password):
            """Method to check whether the given username and password are in the database.
            Returns true if there is at least one row with the given username AND password.
            
            Args:
                username (string): Users username.
                password (string): Users password.
            
            Returns:
                bool: If passwords match.
            """
            cursor = db_conn.cursor()
            """Execute query to see whether user exists."""
            cursor.execute(
            "SELECT user_password FROM users WHERE username = ?",
            (username,))
            db_password = cursor.fetchall()[0][0]
            cursor.close()
            return compare_passwords(db_password, password)

        def get_user_info(username):
            """Method to check whether the given username and password are in the database.
            
            Args:
                username (string): Users username.
            
            Returns:
                string: Users username and user ID.
            """
            cursor = db_conn.cursor()
            """Execute query to see whether user exists."""
            cursor.execute("SELECT username, user_id FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            cursor.close()
            return result

        username = username_input.get()
        password = password_input.get()

        if valid_username(username):
            if verify_login_credentials(username, password):
                user_info = get_user_info(username)
                window.destroy()
                """Pass the database connection and user ID here."""
                show_home_screen(db_conn, user_info[0], user_info[1])
            else:
                messagebox.showwarning("Invalid Credentials", "Incorrect Password.")
                return

        else:
            messagebox.showwarning("Invalid Credentials", "Username does not exist.")
            return

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

    # Button hover effects
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

    ### Disable this before trying to enable gif.
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
