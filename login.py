from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'test@flask.app' or request.form['password'] != 'password123':
            error = 'Your credentials are invalid. Please try again!'
        else:
            return redirect(url_for('success'))
    return render_template('login.html', error=error)