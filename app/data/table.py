def list_to_string(lst):
    return "(" + ", ".join(lst) + ")"

def add_type(field_name):
    return f"{field_name} TEXT"

def quote(value):
    return f"'{value}'"

class Table:
    def __init__(self, db, table_name, search_field):
        self.db = db
        self.table_name = table_name
        self.search_field = search_field
        self.c = db.cursor()
    
    def add_values(values):
        quoted_values = map(quote, values)
        value_string = list_to_string(quoted_values)
        self.c.execute(f"INSERT INTO {self.table_name} VALUES {value_string}")
        self.db.commit()
    
    def set_value(self, search, field, value):
        self.c.execute(f"UPDATE {self.table_name} SET {field} = '{value}' WHERE {self.search_field} = '{search}'")
        self.db.commit()
    
    def get_value_list(self, search, field):
        self.c.execute(f"SELECT {field} FROM {self.table_name} WHERE {self.search_field} = '{search}'")
        return self.c.fetchone()
    
    def value_exists(self, search):
        value_list = get_value_list(search, "1")
        return bool(value_list)
    
    def get_value(self, search, field):
        value_list = get_value(search, field)
        return value_list[0]
    
    def clear(self):
        self.c.execute(f"DELETE FROM {self.table_name}")
        self.db.commit()
