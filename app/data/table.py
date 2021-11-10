def list_to_string(lst):
    return "(" + ", ".join(lst) + ")"

def add_type(field_name):
    return f"{field_name} TEXT"

def get_question_mark(thing):
    return "?"

def first(lst):
    return lst[0]

class Table:
    def __init__(self, db, table_name, search_field):
        self.db = db
        self.table_name = table_name
        self.search_field = search_field
        self.c = db.cursor()
    
    def add_values(self, values):
        '''
        adds desired values
        '''
        question_marks = map(get_question_mark, values)
        value_string = list_to_string(question_marks)
        self.c.execute(f"INSERT INTO {self.table_name} VALUES {value_string}", values)
        self.db.commit()
    
    def set_value(self, search, field, value):
        '''
        sets targetted value using search and field
        '''
        self.c.execute(f"UPDATE {self.table_name} SET {field} = ? WHERE {self.search_field} = ?", [value, search])
        self.db.commit()
    
    def get_main_values(self):
        '''
        fetches main values
        '''
        self.c.execute(f"SELECT {self.search_field} FROM {self.table_name}")
        value_lists = self.c.fetchall()
        return map(first, value_lists)
    
    def get_value_list(self, search, field):
        '''
        gets list of values
        '''
        self.c.execute(f"SELECT {field} FROM {self.table_name} WHERE {self.search_field} = ?", [search])
        return self.c.fetchone()
    
    def get_value(self, search, field):
        '''
        gets first entry of desired values
        '''
        value_list = self.get_value_list(search, field)
        return value_list[0]
    
    def value_exists(self, search):
        '''
        returns boolean based on value search field existence
        '''
        value_list = self.get_value_list(search, "1")
        return bool(value_list)
    
    def clear(self):
        '''
        removes data
        '''
        self.c.execute(f"DELETE FROM {self.table_name}")
        self.c.execute("VACUUM")
        self.db.commit()
    
    def create(self, field_names):
        '''
        creates TABLE for data
        '''
        fields = map(add_type, field_names)
        field_string = list_to_string(fields)
        self.c.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} {field_string}")
        self.db.commit()