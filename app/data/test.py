from db_functions import *
import sqlite3
def printDB(db, table_name):
    c = db.cursor()
    c.execute("SELECT * FROM " + table_name)
    rows = c.fetchall()
    for row in rows:
        print(row)
discobandit = sqlite3.connect("discobandit.db");
create_table(discobandit, "users", ["username", "password"])
printDB(discobandit, "users")