from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from config import app

db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


def create_new_user(username, password, email):
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit(new_user)
    print('new user "'+username+'" has been created.')


def load_user(**kwargs):  # need to complete here.
    print('kwargs: ', kwargs)
    for key in kwargs:
        if key == 'username':
            username = kwargs['username']
            password = kwargs['password']
            # return User.query.filter_by(username=username).first()
            return True
        elif key == 'email':
            email = kwargs['email']
            password = kwargs['password']
            return True
        else:
            pass
    return False


