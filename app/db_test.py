from data.data_functions import *

def username_test(username):
    if user_exists(username):
        no = ""
    else:
        no = " NOT"
    print(f"{username} is{no} a user")

def story_test(title):
    if story_exists(title):
        no = ""
    else:
        no = " NOT"
    print(f"{title} is{no} a story")

def password_test(username, password):
    if correct_password(username, password):
        no = ""
    else:
        no = " NOT"
    print(f"{password} is{no} the correct password for {username}")

def show_edited_stories(username):
    edited_stories = list(get_edited_stories(username))
    print(f"{username} has edited: {edited_stories}")

reset_data()

add_user("bob", "goodpassword")
add_user("joe", "okaypassword")
username_test("bob")
username_test("joe")
username_test("carlos")
add_user("carlos", "coolpassword")
password_test("bob", "goodpassword")
password_test("joe", "okaypassword")
password_test("bob", "idk")

add_story("harry potter")
add_new_part("harry potter", "there once was a boy named harry", "bob")
add_new_part("harry potter", "he did stuff at school", "carlos")
add_story("lord of the rings")
add_new_part("lord of the rings", "frodo baggins liked submarines", "joe")
add_new_part("lord of the rings", "he sailed through the oceans", "carlos")
add_new_part("lord of the rings", "he sailed through all the streams", "bob")
print("\nmost recent add to harry potter:")
print(get_new_part("harry potter"))
print("\nentire text of harry potter:")
print(get_full_story("harry potter"))
print()
story_test("harry potter")
story_test("lord of the rings")
story_test("cheese")
print(list(get_usernames()))
print(list(get_titles()))
show_edited_stories("bob")
show_edited_stories("joe")
show_edited_stories("carlos")
