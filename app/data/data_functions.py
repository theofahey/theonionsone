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

def story_exists(title):
    return value_exists(data, "users", "username", username)

def add_story(title):
    add_values(data, "stories", [title, "", ""])

def get_new_part(title):
    return get_value(data, "stories", "title", title, "new_part")

def get_story(title):
    return get_value(data, "stories", "title", title, "story")

def attach(story, new_part):
    if story == "":
        return new_part
    return story + "\n\n" + new_part

def get_full_story(title):
    story = get_story(title)
    new_part = get_new_part(title)
    return attach(story, new_part)

def add_new_part(title, new_part):
    new_story = get_full_story(title)
    change_value(data, "stories", "title", title, "story", new_story)
    change_value(data, "stories", "title", title, "new_part", new_part)

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