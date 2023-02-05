#__init__.py file means that the folder website becomes a python package
#Therefore when import name __init__.py acts like a constructor to this package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME = "SignTeach.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Flask Secret Key' #Encrypt cookies and session data when flask website is running
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #Connect to database
    db = SQLAlchemy(app) #Create database object
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix ='/')
    
    return app