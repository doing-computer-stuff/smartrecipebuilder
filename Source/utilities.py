from pathlib import Path
from tkinter import *
from tkinter import messagebox
import mysql.connector
import hashlib
import sqlite3
import os

def hash_password(password):
    # Hash the password before storing into database.
    return hashlib.sha256(password.encode()).hexdigest()

# Compare whether two hashed passwords are the same.
def compare_passwords(db_password, entered_password):

    # Hash the supplied password so it can be compared to the
    # one stored in the database.
    hashed_password = hashlib.sha256(entered_password.encode()).hexdigest()

    return db_password == hashed_password

# Method that check if the sqlite database exists. If it does, it connects
# to the database and returns the connection. If it does not, it create the
# database and initalizes the tables.
def create_database_if_not_exists(db_path):
    # Check if the database file already exists.
    if not os.path.exists(db_path):
        # Connect to the database, creating it if it doesn't exist.
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            
            # Create users table.
            cursor.execute('''
                CREATE TABLE users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_creation_date text DEFAULT NULL,
                    username varchar(50) DEFAULT NULL,
                    user_password varchar(64) DEFAULT NULL
                )
            ''')

            # Create ingredients table.
            cursor.execute('''
                CREATE TABLE ingredients (
                    food_name varchar(50) DEFAULT NULL,
                    expiration_date text DEFAULT NULL,
                    quantity varchar(15) DEFAULT NULL,
                    user_id INTEGER DEFAULT NULL,
                    food_id INTEGER PRIMARY KEY NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                )
            ''')
            
            # Commit changes
            conn.commit()
            return conn
    else:
        conn = sqlite3.connect(db_path)
        return conn
