from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating

debug = True
@app.route("/", methods=['GET', 'POST'])
def disp_homepage():
    return ""