from flask import Flask, flash, redirect, render_template, session, request, abort, jsonify
import os

app = Flask(__name__)

categories = [
    {
        "id": 1,
        "name": "Application Accounts",
        "Example": "Email,Subsriptions etc"
    }
    , {
        "id": 2,
        "name": "Bank Accounts",
        "Example": "Credit Cards, Savings, Loan Accounts etc"
    }, {
        "id": 3,
        "name": "Miscellaneous",
        "Example": "Tracking Number, Application confirmation # etc"
    }

]


@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return categories()


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong Password !')
    return home()


@app.route("/categories", methods=['GET'])
def catogories():
    return jsonify(categories)


@app.route('/category/<int:key>')
def category(key):
    for category in categories:
        if category['id'] == key:
            return jsonify(category)

    return abort(404)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


app.secret_key = os.urandom(12)
app.run()
