from . import db
from .models import User, Images, Answers

def addImage(app):
    with app.app_context():
        image = Images(imageNo=1, image='C:/Users/vali/Documents/GitHubRepos/ALevelNEA/website/static/images/Question1.png', iAnswer='A')
        db.session.add(image)
        db.session.commit()
        print('Image added')