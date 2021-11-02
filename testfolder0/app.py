from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request
from flask import session

app = Flask(__name__)
debug = True
@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template('login_Page.html')

@app.route("/auth_ed", methods=['GET', 'POST'])
def disp_homepage():
    return render_template('home_Page.html')

@app.route("/register", methods=['GET', 'POST'])
def disp_registerpage():
    return render_template('register.html')

def main():
    """
    false if this file imported as module
    debugging enabled
    """
    app.debug = True
    app.run()

if __name__ == "__main__":
    main()
