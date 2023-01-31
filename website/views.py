#Store the standard routes for the webiste (e.g, login page)

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#Main page of website
@views.route('/')
def home():
    return render_template("home.html")