from pathlib import Path
from tkinter import *
import tkinter as tk

def show_input_ingredients_screen(db_conn, user_info):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets/input_ingredients")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("784x623")
    window.configure(bg = "#4EB276")
    window.title("Ingredients")
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

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        540.0,
        378.5,
        image=entry_image_5
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))

    back_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("back button clicked"),
        relief="flat"
    )
    back_button.place(
        x=10.0,
        y=583.0,
        width=98.0,
        height=30.749998092651367
    )

    add_button = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("add button clicked"),
        relief="flat"
    )
    add_button.place(
        x=58.0,
        y=423.0,
        width=98.0,
        height=30.749998092651367
    )

    remove_button = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("remove button clicked"),
        relief="flat"
    )
    remove_button.place(
        x=58.0,
        y=477.0,
        width=98.0,
        height=30.749998092651367
    )

    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=63.0,
        y=179.0,
        width=235.0,
        height=39.0
    )


    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=198.0,
        y=255.0,
        width=100.0,
        height=39.0
    )


    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=63.0,
        y=330.0,
        width=235.0,
        height=39.0
    )

    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=64.0,
        y=255.0,
        width=100.0,
        height=39.0
    )

    entry_5 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=340.0,
        y=179.0,
        width=400.0,
        height=397.0
    )

    def navigate_to_login_screen():
        from login import show_login_screen
        window.destroy()
        show_login_screen(db_conn)

    def navigate_to_expiration_help_window():
        from expiration_help_window import show_expiration_help_window
        show_expiration_help_window()


    help_link = tk.Button(window, text="Help Me With Expiration Dates", font=("Inter Bold", 14 * -1, "underline"),
                                        fg="#ffffff", activeforeground="#284846", bg="#4EB276", activebackground="#4EB276", bd=0, command=navigate_to_expiration_help_window)
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
