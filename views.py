from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
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
        password = request.form['pass']
        print(username, password)
        return redirect(url_for('login'))
    else:
        return render_template('signup/signup.html')


if __name__ == '__main__':
    app.run(debug=True)
