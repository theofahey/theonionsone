from flask import session
from flask import request, render_template, Flask, redirect
from data.data_functions import *
from os import urandom
app = Flask(__name__)
debug = True
#why do we need secret keys? For this project it is not really necessary but...
#https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key
#I believe in a real life environment we should store the key somewhere safe in case of server crash
app.secret_key = urandom(24)
#   Things to work on:
#   Implimentationationation
#   Adding error messages and try and fails

#Pretty useless, just redirects to a different method


@app.route("/", methods=['GET', 'POST'])
def welcome():
    '''
    Welcome Page
    '''
    if 'username' in session.keys() and session['username']:
        return render_template("home_Page.html", user = session['username'])
    else:
        return render_template('login_Page.html')


@app.route("/register", methods=['GET', 'POST'])
def disp_registerpage():
    '''
    register page
    '''
    return render_template('register.html')



#Checks the register to make sure everything is good
#Password and confirm password should be the same
@app.route("/check_register", methods=['GET', 'POST'])
def check_register():
    '''

    '''
    username = request.form.get('username')
    password = request.form.get('password')
    con_password = request.form.get('confirm_password')

    #grabs stuff
    password_requirements = password == con_password and bool(password)

    username_conflict = False or (not bool(username))

    if password_requirements and (not username_conflict):
        return render_template('login_Page.html', extra_Message="Successfully Registered")

    else:
        #Need to create different error messages for different things
        extra_Message = "An error has been made trying to register you."
        if not password_requirements:
            extra_Message = "Password requirements not met. Check to see that password is at least one character and that password confirmation matches"
        
        elif username_conflict:
            extra_Message = "Username may already be in use, or does not contain at least one character"
        return render_template('register.html', extra_Message=extra_Message)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    return render_template('login_Page.html', extra_Message="Successfully Logged Out")


@app.route("/auth_ed", methods=['POST'])
def authenticate():
    '''
    authorization page; redirects and logs in if credentials work, loads login template if not
    '''

    #retrieve from FORM instead of ARGS because we are retrieving from POST method
    username = request.form.get('username')
    password = request.form.get('password')
    
    #authflow variable
    loginAuthorized = False

    if loginAuthorized:
        session['username'] = username
        return redirect("/", code = 302)
    else:
        return render_template('login_Page.html', extra_Message="Login failed, please try again")


@app.route("/home", methods=['GET', 'POST'])
def display_home_Page():
    return render_template('home_Page.html')


@app.route("/your_Stories", methods=['GET', 'POST'])
def your_Story():
    return render_template('your_Stories.html')


@app.route("/new_Stories", methods=['GET', 'POST'])
def new_Story():
    return render_template('new_Stories.html')


def main():
    """
    false if this file imported as module
    debugging enabled
    """
    app.debug = True
    app.run()


if __name__ == "__main__":
    main()
