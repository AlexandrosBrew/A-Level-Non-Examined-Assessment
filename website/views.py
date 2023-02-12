#Store the standard routes for the webiste (e.g, login page)

from flask import Blueprint,render_template, request, flash, redirect, url_for
from .models import User, Images, Answers
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Images, Answers

views = Blueprint('views', __name__)
questionNo = 1
showAnswer = False

#Main page of website
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/progress')
def progress():
    user = User.query.filter_by(id=current_user.id).first()
    print(user.id)
    count = user.noCorrect
    return render_template("progress.html", user=current_user, progress=count)

@views.route('/questions', methods=['GET', 'POST'])
def questions():
    global questionNo
    user = User.query.filter_by(id=current_user.id).first()
    count = user.noCorrect
    if request.method == 'POST':
        if 'submit' in request.form:
            answer = request.form.get('answer')
            imageA = Images.query.filter_by(imageNo=questionNo).first()
            userAnswer = Answers.query.filter_by(id=current_user.id).first()
            print(userAnswer)
            # print(Answers.query.all())
            # print(user.noCorrect)
            if answer == imageA.iAnswer and userAnswer.answer == False:
                flash('Correct!', category='success')
                user.noCorrect+=1
                userAnswer.questionNo = questionNo
                userAnswer.answer = True
                db.session.commit()
                # print(user.noCorrect)
            elif userAnswer.answer == True:
                flash('You have already answered this question', category='error')
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

@views.route('/learning', methods=['GET', 'POST'])
def learning():
    global questionNo
    global showAnswer
    if request.method == 'POST':
        if 'show' in request.form:
            if showAnswer:
                showAnswer = False
                return render_template("learning.html", user=current_user, answer="", showAnswer=False, questionNo=str(questionNo))
            elif showAnswer == False:
                try:
                    image = Images.query.filter_by(imageNo=questionNo).first()
                    imageA = image.iAnswer
                    showAnswer = True
                    return render_template("learning.html", user=current_user, answer=imageA, showAnswer=True, questionNo=str(questionNo))
                except:
                    flash('No answer available', category='error')
        elif 'next' in request.form:
            questionNo+=1
            return render_template("learning.html", user=current_user, questionNo=str(questionNo), showAnswer=False, answer="")
        elif 'prev' in request.form:
            if questionNo == 1:
                questionNo = 1
            else:
                questionNo-=1
            return render_template("learning.html", user=current_user, questionNo=str(questionNo), showAnswer=False, answer="")
    return render_template("learning.html", user=current_user, questionNo=str(questionNo), showAnswer=False, answer="")