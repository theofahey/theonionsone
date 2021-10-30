def list_to_string(lst):
    return "(" + ", ".join(lst) + ")"

def add_type(field_name):
    return f"{field_name} TEXT"

def create_table(db, table_name, field_names):
    c = db.cursor()
    fields = map(add_type, field_names)
    field_string = list_to_string(fields)
    c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} {field_string}")
    db.commit

def value_exists(db, table_name, field_name, value):
    c = db.cursor()
    c.execute(f"SELECT 1 FROM {table_name} WHERE {field_name} = '{value}'")
    return bool(c.fetchone())

def quote(value):
    return f"'{value}'"

def add_values(db, table_name, values):
    c = db.cursor()
    quoted_values = map(quote, values)
    value_string = list_to_string(quoted_values)
    c.execute(f"INSERT INTO {table_name} VALUES {value_string}")
    db.commit()

def print_table(db, table_name):
    c = db.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    for row in rows:
        print(row)