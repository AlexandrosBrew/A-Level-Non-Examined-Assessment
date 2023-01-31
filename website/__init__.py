#__init__.py file means that the folder website becomes a python package
#Therefore when import name __init__.py acts like a constructor to this package

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Flask Secret Key' #Encrypt cookies and session data when flask website is running
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix ='/')
    
    return app