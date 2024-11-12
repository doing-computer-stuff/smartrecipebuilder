import mysql.connector
from login import show_login_screen
from utilities import *
import sqlite3
import os

if __name__ == "__main__":
    # Path is in the same location as the program.
    db_path = "smartrecipebuilder.db"
    # Connect to database if it exists. If it does not, create it.
    db_conn = create_database_if_not_exists(db_path)
    # print("Current working directory:", os.getcwd())
    show_login_screen(db_conn)
    db_conn.close()
