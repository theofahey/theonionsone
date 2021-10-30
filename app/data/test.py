from db_functions import *
from sqlite3 import connect

def printDB(db, table_name):
    c = db.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    for row in rows:
        print(row)

def check_for_value(db, table_name, field_name, value):
    verb = None
    if value_exists(db, table_name, field_name, value):
        verb = "exists"
    else:
        verb = "doesn't exist"
    print(f"{field_name} value {value} {verb} in {table_name}")


discobandit = connect("discobandit.db")
create_table(discobandit, "users", ["username", "password"])
add_values(discobandit, "users", ["bob", "goodpassword"])
add_values(discobandit, "users", ["joe", "okaypassword"])
printDB(discobandit, "users")
check_for_value(discobandit, "users", "username", "bob")
check_for_value(discobandit, "users", "username", "joe")
check_for_value(discobandit, "users", "username", "carlos")