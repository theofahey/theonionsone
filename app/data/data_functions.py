from sqlite3 import connect
from table import Table

data = connect("data.db", isolation_level = None)
users = Table(data, "users", "username")
stories = Table(data, "stories", "title")

def user_exists(username):
    return users.value_exists(username)

def correct_password(username, password):
    real_password = users.get_value(username, "password")
    return password == real_password

def add_user(username, password):
    users.add_values([username, password])

def story_exists(title):
    return stories.value_exists(username)

def add_story(title):
    stories.add_values([title, "", ""])

def get_new_part(title):
    return stories.get_value(title, "new_part")

def get_story(title):
    return stories.get_value(title, "story")

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
    stories.set_value(title, "story", new_story)
    stories.set_value(title, "new_part", new_part)

#just for testing:
def clear_users():
    users.clear()

def clear_stories():
    stories.clear()

def initialize():
    users.create(["username", "password"])
    stories.create(["title", "story", "new_part"])