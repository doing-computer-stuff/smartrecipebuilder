"""Module contains the utility functions of the system.
"""
import hashlib
import sqlite3
import os

def hash_password(password):
    """Hash the password before storing into database.
    
    Args:
        password (string): Password to be hashed.
    
    Returns:
        string: The string hash of the password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def compare_passwords(db_password, entered_password):
    """Compare whether two hashed passwords are the same.
    
    Args:
        db_password (string): Password from the database.
        entered_password (string): Password from the user.
    
    Returns:
        bool: If passwords are the same.
    """
    """Hash the supplied password so it can be compared to the one stored in the database."""
    hashed_password = hashlib.sha256(entered_password.encode()).hexdigest()

    return db_password == hashed_password

def create_database_if_not_exists(db_path):
        """Method that check if the sqlite database exists. If it does, it connects
    to the database and returns the connection. If it does not, it create the
    database and initalizes the tables.
    
    Args:
        db_path (string): PATH of the database.
    
    Returns:
        bool: Database connection.
    """
    
    """Check if the database file already exists."""
    if not os.path.exists(db_path):
        """Connect to the database, creating it if it doesn't exist."""
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            
            """Create users table."""
            cursor.execute('''
                CREATE TABLE users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_creation_date text DEFAULT NULL,
                    username varchar(50) DEFAULT NULL,
                    user_password varchar(64) DEFAULT NULL,
                    saved_recipes text DEFAULT NULL
                )
            ''')

            """Create ingredients table."""
            cursor.execute('''
                CREATE TABLE ingredients (
                    food_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    food_name text COLLATE NOCASE DEFAULT NULL,
                    expiration_date text DEFAULT NULL,
                    quantity varchar(15) DEFAULT NULL,
                    user_id INTEGER DEFAULT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                )
            ''')

            """Create recipes table."""
            cursor.execute('''
                CREATE TABLE recipes (
                    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_name text COLLATE NOCASE DEFAULT NULL ,
                    recipe_type text DEFAULT NULL,
                    recipe_ingredients text COLLATE NOCASE DEFAULT NULL,
                    recipe_cooking_method text DEFAULT NULL,
                    recipe_cook_time text DEFAULT NULL,
                    recipe_is_shareable text DEFAULT NULL
                )
            ''')
            
            """Commit changes."""
            conn.commit()
            return conn
    else:
        conn = sqlite3.connect(db_path)
        return conn

def get_user_ingredients_names(db_conn, user_id):
    """Get user ingredients and convert them into a set.
    
    Args:
        db_conn (conn): Database connection.
        user_id (string): Users ID.
    
    Returns:
        list: Users ingredients as a list.
    """
    cursor = db_conn.cursor()
    cursor.execute("SELECT food_name FROM ingredients WHERE user_id = ?", (user_id,))
    user_ingredients = cursor.fetchall()
    user_ingredient_list = [i[0] for i in user_ingredients]
    cursor.close()
    return user_ingredient_list

def get_recipe_ingredients_names_as_set(db_conn, user_id, recipe):
    """Gets a recipes ingredients as a set.
    
    Args:
        db_conn (conn): Database connection.
        recipe (list): A recipe with its related data.
    
    Returns:
        list: The recipes ingredients as a set.
    """
    recipe_ingredients_set = set(recipe[3].split("\n"))
    return recipe_ingredients_set
