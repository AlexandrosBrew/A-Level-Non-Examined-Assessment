from flask import Flask, render_template, request, redirect, url_for, flash

from databaseCommands import *
from validation import *
from createDatabase import *

edit = EditDatabase()
get = GetDatabase()

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    usrList = GetDatabase.getAllUsers()
    if request.method == 'GET':
        for i in range(len(GetDatabase.getAllUsers())):
            if request.form['username'] == usrList[i][1] and request.form['password'] == usrList[i][2]:
                return redirect(url_for('home'))