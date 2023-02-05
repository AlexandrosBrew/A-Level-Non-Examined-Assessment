#Store the standard routes for the webiste (e.g, login page)

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .databaseCommands import *
import time
views = Blueprint('views', __name__)
edit = EditDatabase()
get = GetDatabase()


#Main page of website
@views.route('/')
def home():
    return render_template("home.html")

@views.route('/question1', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        answer = request.form.get('answer')
        image = get.getImages(1)
        if answer == image[2]:
            flash('Correct!', category='success')
        else:
            flash('Incorrect', category='error')
    return render_template("question.html")