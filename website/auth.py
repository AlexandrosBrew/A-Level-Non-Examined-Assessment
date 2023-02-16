#Stores standard routes for auth (e.g login in, log out, register)

from flask import Blueprint,render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Images, Answers
from .views import *
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again', category='error')
        else:
            flash('Email does not exist', category='error')
            
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    flash('Logged out successfully', category='success')
    user = User.query.filter_by(id=current_user.id).first()
    count = user.noCorrect
    User.query.filter_by(id=current_user.id).update(dict(noCorrect=count))
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists', category='error')
        elif  password1 == password2:
            new_user = User(email=email, username=firstName, password=generate_password_hash(password1, method='sha256'), noCorrect=0)
            new_Answer = Answers(userID=new_user.id, questionNo=1, answer=False)
            db.session.add(new_user)
            db.session.add(new_Answer)
            db.session.commit()
            print(new_Answer.answer)
            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Something went wrong please try again', category='error')
    return render_template('sign_up.html', user=current_user)
