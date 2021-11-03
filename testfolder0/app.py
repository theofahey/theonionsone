from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request
from flask import session

app = Flask(__name__)
debug = True

#   Things to work on:
#   Implimentationationation
#   Adding error messages and try and fails

#Pretty useless, just redirects to a different method
@app.route("/", methods=['GET', 'POST'])
def welcome():
    return display_login()

#Login page
@app.route("/welcome", methods=['GET', 'POST'])
def display_login():
    return render_template('login_Page.html')

#Register page
@app.route("/register", methods=['GET', 'POST'])
def disp_registerpage():
    return render_template('register.html')

#Checks the register to make sure everything is good
#Password and confirm password should be the same
@app.route("/check_register", methods=['GET', 'POST'])
def check_register():
    user = request.args.get('username')
    passwd = request.args.get('password')
    conpass = request.args.get('confirm_password')

    #grabs stuff
    if passwd == conpass and bool(user) and bool(passwd) and bool():
        return render_template('login_Page.html', extra_Message = "Successfully Registered")
    else :
        #Need to create different error messages for different things
        return render_template('register.html', extra_Message = "Something went wrong")

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    return render_template('login_Page.html', extra_Message = "Successfully Logged Out")

@app.route("/auth_ed", methods=['GET', 'POST'])
def authenticate():
    return display_home_Page()

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
