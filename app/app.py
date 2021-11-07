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


#helper method
def unauthorizedFlow():
    '''
    returns static html for when user accesses site they should not
    '''

    #simply redirects to desired site
    return redirect("/static/unauthorized.html", code=302)

#helper method
def userSignedIn(session):
    '''
    returns the status of user login
    '''
    return 'username' in session.keys() and session['username']


@app.route("/", methods=['GET', 'POST'])
def welcome():
    '''
    Welcome Page
    '''

    if userSignedIn(session):
        return render_template("home_Page.html", user = session['username'])

    else:
        return render_template('login_Page.html')


@app.route("/register", methods=['GET', 'POST'])
def disp_registerpage():
    '''
    register page
    '''
    if userSignedIn(session):
        return unauthorizedFlow()

    return render_template('register.html')



#Checks the register to make sure everything is good
#Password and confirm password should be the same
@app.route("/check_register", methods=['GET', 'POST'])
def check_register():
    '''
    function for post-form request; register process given POST form arguments
    '''
    if userSignedIn(session):
        return redirect("/unauthorized.html", code = 302)

    #store form information
    username = request.form.get('username')
    password = request.form.get('password')
    con_password = request.form.get('confirm_password')

    #checks password requirements against password confirmation and password existence; False means it fails requirements
    password_requirements = password == con_password and bool(password)

    #checks db for existing user and user existence; False means it passes requirements
    username_conflict = user_exists(username) or (not bool(username))

    if password_requirements and (not username_conflict):
        add_user(username,password)
        return render_template('login_Page.html', extra_Message="Successfully Registered")

    else:
        #Error messages based on incorrect input types
        extra_Message = "An error has been made trying to register you."
        if not password_requirements:
            extra_Message = "Password requirements not met. Check to see that password is at least one character and that password confirmation matches"

        elif username_conflict:
            extra_Message = "Username may already be in use, or does not contain at least one character"

        return render_template('register.html', extra_Message=extra_Message)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    '''
    logs out the user by setting 'username' key to None
    '''
    session['username'] = None
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
    loginAuthorized = user_exists(username) and correct_password(username,password)

    if loginAuthorized:
        session['username'] = username
        return redirect("/", code = 302)
    else:
        return render_template('login_Page.html', extra_Message="Login failed, please try again")


@app.route("/home", methods=['GET', 'POST'])
def display_home_Page():
    if(userSignedIn(session)):
        return render_template('home_Page.html')
    else:
        return unauthorizedFlow()


@app.route("/your_stories", methods=['GET', 'POST'])
def your_Story():
    if(userSignedIn(session)):
        return render_template('your_Stories.html', stories = ["henlo","yummyumyum","kool"])
    else:
        return unauthorizedFlow()


@app.route("/new_stories", methods=['GET', 'POST'])
def new_Story():
    if(userSignedIn(session)):
        return render_template('new_Stories.html')
    else:
        return unauthorizedFlow()


@app.route("/stories", methods=['GET', 'POST'])
def stories():
    return "here should be a list of ALL the stories"


@app.route("/stories/<string:title>")
def getStory(title):
    return "this should return the story " + title


@app.route("/createstory" , methods = ['GET', 'POST'])
def create_story():
    if(not userSignedIn(session)):
        return unauthorizedFlow()
    
    return render_template('create_New.html', user = session['username'])


@app.route("/requestcreate", methods = ["GET","POST"])
def requestCreate():
    if(not userSignedIn(session)):
        return unauthorizedFlow()
    
    title = request.form.get('title')
    contents = request.form.get('story')
    
    matchedRequirements = not story_exists(title)

    if matchedRequirements:
        if debug:
            print (user_exists(session['username']))
            print("Requirements Met. Creating story")

            add_story(title)
            print("Story created")

            add_new_part(title,contents,session['username'])
            print("Contents added")

            print("Was the story added to db? " + str(story_exists(title)))
            print("Contents of the story: " + get_full_story(title))
        else:

            add_story(title)
            add_new_part(title, contents, session['username'])
    else:
        return render_template("create_New.html", user = session['username'], error = True)




    return redirect("/your_stories")

def main():
    """
    false if this file imported as module
    debugging enabled
    """
    app.debug = True
    app.run()


if __name__ == "__main__":
    main()
