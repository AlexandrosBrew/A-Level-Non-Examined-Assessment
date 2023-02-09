#Store the standard routes for the webiste (e.g, login page)

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .databaseCommands import *
from .models import Answers, Images, User

views = Blueprint('views', __name__)
edit = EditDatabase()
get = GetDatabase()
questionNo = 1


#Main page of website
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/question1', methods=['GET', 'POST'])
def questions():
    global questionNo
    if request.method == 'POST':
        if 'submit' in request.form:
            answer = request.form.get('answer')
            image = Images.query.filter_by(answer=answer).first()
            if answer == image:
                flash('Correct!', category='success')
            else:
                flash('Incorrect', category='error')
        elif 'next' in request.form:
            questionNo+=1
            print(questionNo)
            return render_template("question.html", user=current_user, questionNo=str(questionNo))
        elif 'prev' in request.form:
            if questionNo == 1:
                questionNo = 1
            else:
                questionNo-=1
            print(questionNo)
            return render_template("question.html", user=current_user, questionNo=str(questionNo))
    return render_template("question.html", user=current_user, questionNo=str(questionNo))

