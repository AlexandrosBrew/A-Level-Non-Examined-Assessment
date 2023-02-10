from . import db
from flask_login import UserMixin

class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionNo = db.Column(db.Integer)
    answer = db.Column(db.Boolean, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    noCorrect = db.Column(db.Integer)

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imageNo = db.Column(db.Integer)
    image = db.Column(db.String(1000))
    iAnswer = db.Column(db.String(1000))
