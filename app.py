from flask import Flask ,flash,redirect,render_template,session,request,abort
import os


app = Flask(__name__)

@app.route("/")
def home():
       if not session.get('logged_in'):
           return render_template('login.html')
       else:
           return "Hello Boss !"

@app.route('/login',methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong Password !')
    return home()

@app.route("/logout")
def logout():
     session['logged_in'] = False
     return home()

app.secret_key = os.urandom(12)
app.run()