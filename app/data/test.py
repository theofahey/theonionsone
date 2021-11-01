from data_functions import *

def username_test(username):
    if user_exists(username):
        no = ""
    else:
        no = " not"
    print(f"{username} is{no} a user")

def password_test(username, password):
    if check_password(username, password):
        no = ""
    else:
        no = " not"
    print(f"{password} is{no} the correct password for {username}")

clear_users()
clear_stories()

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