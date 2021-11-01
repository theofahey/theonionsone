from db_functions import *
from sqlite3 import connect

data = connect("data.db")
        
def user_exists(username):
    return value_exists(data, "users", "username", username)

def check_password(username, password):
    correct_password = get_value(data, "users", "username", username, "password")
    return password == correct_password

def add_user(username, password):
    add_values(data, "users", [username, password])


#just for testing:
def print_users():
    print_table(data, "users")

def clear_users():
    clear_table(data, "users")

def clear_stories():
    clear_table(data, "stories")

def get_password(username):
    return get_value(data, "users", "username", username, "password")

def change_password(username, new_password):
    change_value(data, "users", "username", username, "password", new_password)