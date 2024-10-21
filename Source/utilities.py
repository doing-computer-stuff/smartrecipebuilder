from pathlib import Path
from tkinter import *
from tkinter import messagebox
import mysql.connector
import hashlib

def hash_password(password):
    # Hash the password before storing into database.
    return hashlib.sha256(password.encode()).hexdigest()

# Compare whether two hashed passwords are the same.
def compare_passwords(db_password, entered_password):

    # Hash the supplied password so it can be compared to the
    # one stored in the database.
    hashed_password = hashlib.sha256(entered_password.encode()).hexdigest()

    return db_password == hashed_password
