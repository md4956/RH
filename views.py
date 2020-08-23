from flask import render_template, request, redirect, url_for
from run import app
from db import models as dbModel
from db.models import db


@app.route('/')
def home():
    db.create_all()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']
        print(username, password)
        return '<h1>Weeeeeellllllcooooomeeeee!!!</h1>'
    else:
        return render_template('login/login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['pass']
        dbModel.create_new_user(username, password, email)
        return redirect(url_for('login'))
    else:
        return render_template('signup/signup.html')


if __name__ == '__main__':
    app.run(debug=True)
