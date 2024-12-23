"""Main module for the system.
"""
from login import show_login_screen
from utilities import *

if __name__ == "__main__":
    """Path is in the same location as the program."""
    db_path = "smartrecipebuilder.db"
    """Connect to database if it exists. If it does not, create it."""
    db_conn = create_database_if_not_exists(db_path)
    show_login_screen(db_conn)
    db_conn.close()
