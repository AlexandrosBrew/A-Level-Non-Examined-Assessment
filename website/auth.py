#Stores standard routes for auth (e.g login in, log out, register)

from flask import Blueprint,render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from .validation import *
from .databaseCommands import *

get = GetDatabase()
edit = EditDatabase()
valid = Validation()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        results = get.getAllUsers()
        for i in range(len(results)):
            if results[i][3] == email:
                break
        if results[i][3] == email and results[i][2] == password:
            return redirect(url_for('views.home'))
        else:
            flash('Failed Login Try Again.', category='error')
            
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>logout</p>'


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if valid.validate_add([email, firstName, password1, password2]) and password1 == password2:
            edit.addUserAccount(firstName, password1, email)
            print(get.getAllUsers())
            flash('Account Created!', category='success')
        else:
            flash('Something went wrong please try again', category='error')
    return render_template('sign_up.html')
