from pathlib import Path
from tkinter import *
from tkinter import messagebox
import mysql.connector

# Connect to the ingredients database.
def connect_to_database():
    db_conn = mysql.connector.connect(
        # Put database credentials here!
        # Set credentials when we create the database.
        host = "localhost",
        user = "root",
        password = 'Development1234',
        db = "smartrecipebuilder"
    )
    return db_conn