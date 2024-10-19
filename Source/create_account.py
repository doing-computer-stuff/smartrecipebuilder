from pathlib import Path
from tkinter import *
from tkinter import messagebox
import mysql.connector
from utilities import *

def show_create_account(db_conn):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets/create_account_screen")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("700x484")
    window.configure(bg = "#4EB276")
    window.title("Create Account")
    window.resizable(False, False)

    canvas = Canvas(
        window,
        bg = "#4EB276",
        height = 484,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        535.5,
        214.5,
        image=entry_image_1
    )
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        535.5,
        288.5,
        image=entry_image_2
    )
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        535.5,
        365.5,
        image=entry_image_3
    )
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        123.0,
        74.0,
        image=image_image_1
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))

    canvas.create_text(
        186.0,
        47.0,
        anchor="nw",
        text="Smart Recipe Builder",
        fill="#FFFFFF",
        font=("Itim Regular", 44 * -1)
    )
    canvas.create_text(
        249.0,
        116.0,
        anchor="nw",
        text="Create New Account",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )
    canvas.create_text(
        25.0,
        151.0,
        anchor="nw",
        text="                  Hey new user!\n\nJoin today to gain access to simple yet\npowerful tools for taking the guesswork\n          out of your meal planning!\n\n"
             "    From saving your own recipes to\ndiscovering new recipe suggestions by\n   other users to ingredient expiration\nreminders, "
             "we have all your meal prep\n                 needs in mind!",
        fill="#FFFFFF",
        font=("Itim Regular", 20 * -1)
    )
    canvas.create_text(
        413.0,
        170.0,
        anchor="nw",
        text="Username:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )
    canvas.create_text(
        414.0,
        244.0,
        anchor="nw",
        text="Password:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )
    canvas.create_text(
        414.0,
        321.0,
        anchor="nw",
        text="Confirm Password:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    username_input = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    username_input.place(
        x=418.0,
        y=194.0,
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
        x=418.0,
        y=268.0,
        width=235.0,
        height=39.0
    )

    confirm_password_input = Entry(
        show="*",
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    confirm_password_input.place(
        x=418.0,
        y=345.0,
        width=235.0,
        height=39.0
    )

    # create account button and function
    def create_account():
        # Getting it through the console?
        if (username_input.get() != "") and (password_input.get() != "") and (password_input.get() == confirm_password_input.get()):

            # Create a cursor to execute SQL commands.
            cursor = db_conn.cursor()

            # Execute query to insert new user data into user database.
            cursor.execute("INSERT INTO users (username, user_password) VALUES (%s, %s)",
                (username_input.get(), password_input.get()))

            # Commit changes to the database and close connection to cursor.
            db_conn.commit()
            cursor.close()

            messagebox.showinfo("Success", "You have successfully created an account!")
            navigate_to_login_screen()
        else:
            print("Create Account button clicked")

    create_account_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=create_account,
        relief="flat"
    )
    create_account_button.place(
        x=437.0,
        y=413.0,
        width=198.0,
        height=41.0
    )

    # back button function
    def navigate_to_login_screen():
        from login import show_login_screen
        window.destroy()
        show_login_screen(db_conn)

    back_button = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=navigate_to_login_screen,
        relief="flat"
    )
    back_button.place(
        x=11.0,
        y=443.6666564941406,
        width=76.0,
        height=27.666675567626953
    )

    # button hover effects
    button_image_hover_2 = PhotoImage(
        file=relative_to_assets("button_hover_1.png"))

    def button_2_hover(e):
        back_button.config(
            image=button_image_hover_2
        )
    def button_2_leave(e):
        back_button.config(
            image=button_image_2
        )

    back_button.bind('<Enter>', button_2_hover)
    back_button.bind('<Leave>', button_2_leave)

    button_image_hover_1 = PhotoImage(
        file=relative_to_assets("button_hover_2.png"))

    def button_1_hover(e):
        create_account_button.config(
            image=button_image_hover_1
        )
    def button_1_leave(e):
        create_account_button.config(
            image=button_image_1
        )

    create_account_button.bind('<Enter>', button_1_hover)
    create_account_button.bind('<Leave>', button_1_leave)

    window.mainloop()
