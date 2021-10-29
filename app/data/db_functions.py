import sqlite3

def value_exists(db, table_name, field_name, value):
    c = db.cursor()
    c.execute("SELECT 1 FROM " + table_name + " WHERE " + field_name + " = '" + value + "'")
    return bool(c.fetchone())

def list_to_string(lst):
    return "(" + ", ".join(lst) + ")"

def add_values(db, table_name, values):
    value_string = list_to_string(values)
    c.execute("INSERT INTO " + table_name + " VALUES " + value_string)