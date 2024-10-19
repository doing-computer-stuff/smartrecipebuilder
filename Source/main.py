import mysql.connector
from login import show_login_screen
import mysql.connector

if __name__ == "__main__":
    db_conn = mysql.connector.connect(host="localhost", user="root", passwd="Development1234", database="smartrecipebuilder")
    show_login_screen(db_conn)
    #db_conn.close()
