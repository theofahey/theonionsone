from data_functions import *

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

clear_all()

add_user("bob", "goodpassword")
add_user("joe", "okaypassword")
username_test("bob")
username_test("joe")
username_test("carlos")
password_test("bob", "goodpassword")
password_test("joe", "okaypassword")
password_test("bob", "idk")

add_story("harry potter")
add_new_part("harry potter", "there once was a boy named harry")
add_new_part("harry potter", "he did stuff at school")
add_new_part("harry potter", "he saved the world or something yay")
print(get_new_part("harry potter"))
print(get_full_story("harry potter"))
story_test("harry potter")
story_test("skyward")