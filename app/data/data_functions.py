from db_functions import *
from sqlite3 import connect

def user_exists(username):
    with connect("data.db") as data:
        return value_exists(data, "users", "username", username)

def add_user(username, password):
    with connect("data.db") as data:
        add_values(data, "users", [username, password])

def print_users():
    with connect("data.db") as data:
        print_table(data, "users")

def clear_users():
    with connect("data.db") as data:
        clear_table(data, "users")

def get_password(username):
    with connect("data.db") as data:
        return get_value(data, "users", "username", username, "password")

def change_password(username, new_password):
    with connect("data.db") as data:
        change_value(data, "users", "username", username, "password", new_password)