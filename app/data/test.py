from data_functions import *

def check_username(username):
    if user_exists(username):
        verb = "is"
    else:
        verb = "is not"
    print(f"{username} {verb} a user")

clear_users()
add_user("bob", "goodpassword")
add_user("joe", "okaypassword")
check_username("bob")
check_username("joe")
check_username("carlos")
print(get_password("bob"))
print(get_password("joe"))
change_password("bob", "bienpassword")
print(get_password("bob"))
print(get_password("joe"))
print_users()