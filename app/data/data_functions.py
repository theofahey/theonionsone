from db_functions import *
from sqlite3 import connect

def user_exists(username):
    data = connect("data.db")
    return value_exists(data, "users", "username", username)

def add_user(username, password):
    data = connect("data.db")
    add_values(data, "users", [username, password])

def print_users():
    data = connect("data.db")
    print_table(data, "users")

def clear_users():
    data = connect("data.db")
    clear_table(data, "users")