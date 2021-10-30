from db_functions import *
from sqlite3 import connect
def printDB(db, table_name):
    c = db.cursor()
    c.execute("SELECT * FROM " + table_name)
    rows = c.fetchall()
    for row in rows:
        print(row)
discobandit = connect("discobandit.db");
create_table(discobandit, "users", ["username", "password"])
add_values(discobandit, "users", ["bob", "goodpassword"])
printDB(discobandit, "users")