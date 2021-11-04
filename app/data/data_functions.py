from sqlite3 import connect
from data.table import Table

data = connect("data.db", isolation_level = None, check_same_thread=False)
users = Table(data, "users", "username")
stories = Table(data, "stories", "title")

def get_usernames():
    return users.get_main_values()

def user_exists(username):
    return users.value_exists(username)

def correct_password(username, password):
    real_password = users.get_value(username, "password")
    return password == real_password

def add_user(username, password):
    users.add_values([username, password])

def get_titles():
    return stories.get_main_values()

def story_exists(title):
    return stories.value_exists(title)

def add_story(title):
    stories.add_values([title, "", ""])

def get_old_part(title):
    return stories.get_value(title, "old_part")

def get_new_part(title):
    return stories.get_value(title, "new_part")

def attach(old_part, new_part):
    if old_part == "":
        return new_part
    return old_part + "\n\n" + new_part

def get_full_story(title):
    old_part = get_old_part(title)
    new_part = get_new_part(title)
    return attach(old_part, new_part)

def add_new_part(title, new_part):
    full_story = get_full_story(title)
    stories.set_value(title, "old_part", full_story)
    stories.set_value(title, "new_part", new_part)

def clear_all():
    users.clear()
    stories.clear()

def initialize():
    users.create(["username", "password"])
    stories.create(["title", "old_part", "new_part"])
