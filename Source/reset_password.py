from pathlib import Path
from tkinter import *
from tkinter import messagebox
import mysql.connector
from utilities import *

def show_reset_password(db_conn):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets/reset_password_screen")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("700x487")
    window.configure(bg = "#4EB276")
    window.title("Reset Password")
    window.resizable(False, False)

    canvas = Canvas(
        window,
        bg = "#4EB276",
        height = 487,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        117.0,
        77.0,
        image=image_image_1
    )
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        349.5,
        361.5,
        image=entry_image_1
    )
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        349.5,
        284.5,
        image=entry_image_2
    )
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        349.5,
        210.5,
        image=entry_image_3
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))

    canvas.create_text(
        180.0,
        50.0,
        anchor="nw",
        text="Smart Recipe Builder",
        fill="#FFFFFF",
        font=("Itim Regular", 44 * -1)
    )
    canvas.create_text(
        270.0,
        119.0,
        anchor="nw",
        text="Password Reset",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )
    canvas.create_text(
        227.0,
        166.0,
        anchor="nw",
        text="Username:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )
    canvas.create_text(
        228.0,
        240.0,
        anchor="nw",
        text="New Password:",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )
    canvas.create_text(
        228.0,
        317.0,
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
        x=232.0,
        y=341.0,
        width=235.0,
        height=39.0
    )

    new_password_input = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    new_password_input.place(
        x=232.0,
        y=264.0,
        width=235.0,
        height=39.0
    )

    confirm_new_password_input = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    confirm_new_password_input.place(
        x=232.0,
        y=190.0,
        width=235.0,
        height=39.0
    )

    # Method to reset the password of the user.
    def password_reset():
        # If the provided passwords match, connect to the user database
        # and update the password of the user.
        if new_password_input.get() == confirm_new_password.get():

            # Create a cursor to execute SQL commands.
            cursor = db_conn.cursor()

            # Execute query to update users password.
            cursor.execute("UPDATE users SET user_password = %s WHERE username = %s",
            (new_password, username))
            
            # Commit changes to the database and close connection to cursor.
            db_conn.commit()
            cursor.close()

            messagebox.showinfo("Success", "Password successfully changed.")
            navigate_to_login_screen()
        else:
            messagebox.showinfo("Error", "Passwords do not match.")
            navigate_to_login_screen()

    reset_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=password_reset,
        relief="flat"
    )
    reset_button.place(
        x=264.0,
        y=406.0,
        width=169.0,
        height=41.0
    )

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
        y=449.0,
        width=76.0,
        height=27.333332061767578
    )

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
        reset_button.config(
            image=button_image_hover_1
        )

    def button_1_leave(e):
        reset_button.config(
            image=button_image_1
        )

    reset_button.bind('<Enter>', button_1_hover)
    reset_button.bind('<Leave>', button_1_leave)

    window.mainloop()
