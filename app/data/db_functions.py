import sqlite3
def value_exists(db, table_name, field_name, value):
    c = db.cursor()
    c.execute("SELECT 1 FROM " + table_name + " WHERE " + field_name + " = '" + value + "'")
    return bool(c.fetchone())