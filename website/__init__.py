#__init__.py file means that the folder website becomes a python package
#Therefore when import name __init__.py acts like a constructor to this package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

DB_NAME = "SignTeach.db"
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Flask Secret Key' #Encrypt cookies and session data when flask website is running
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #Connect to database
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .imageAdd import addImage

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix ='/')
    
    from .models import User, Answers, Images

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    with app.app_context():
        db.create_all()
        db.session.commit()

    # addImage(app)
    return app