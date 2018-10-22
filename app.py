# Alexander Liu
# SoftDev1 pd7
# P #00: Da Art of Storytellin'
# 2018-10-17

from flask import Flask, render_template, request, session, url_for, redirect
from story import getTime, getLastUpdate, getWriters, updateStory, getStory
import sqlite3
import os
app = Flask(__name__)

username = 'alex'
password = 'starwars4'

# name of file will be database.db
DB_FILE = "database.db"

# create database.db
db = sqlite3.connect(DB_FILE)
c = db.cursor()

# returns true if username and password match, false otherwise
def good(usr, psw):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM users")
    for row in data:
        if row[0] == usr and row[1] == psw:
            db.close()
            return True
    db.close()
    return False

@app.route('/')
def disp_login():
    loginMess = "Please enter a valid username and password."
    return render_template("login.html", message = loginMess)

@app.route('/signup')
def signup():
        loginMess = "Please enter a valid username and password to signup :)"
        return render_template("signup.html", message = loginMess)

@app.route('/signupauth')
def sign_Auth():

        session['username'] = request.form['username']
        session['password'] = request.form['password']
        print(session)
        print(session['username'])

        # Invalid username: ===================================
        if len (session['username']) < 3:
            msg = "*cue sad trombone music* It looks like you've entered an invalid username. Please try again."
            # print('bad username')
            return (render_template("signup.html", message = msg))

        # Invalid password: ===================================
        elif len (session['password']) < 5:
            msg = "*cue sad trombone music* It looks like your password does not match your username. Please try again."
            # print('bad password')
            return (render_template("signup.html", message = msg))

        # Both username and password are valid ================
        elif (len (session['username']) > 3 and len (session['password']) > 5):
            # enter username and password into the database
            command = 'INSERT INTO users VALUES(' + session['username'] + ' , ' + session['password'] + ')'
            c.execute(command)
            db.commit()
            db.close()
            dictInput = getLastUpdate()
            return render_template("landing.html", d = dictInput)

        # All other invalid cases =============================
        else:
            msg = "Oops! Looks like something went wrong. Please try again."
            return ((render_template("signup.html", message = msg )))

        print (url_for('disp_login'))
        print (url_for('authenticate'))
        return redirect(url_for("disp_login"))

# what is the difference between render_template, redirect, and url_for?
@app.route('/auth', methods = ['POST'] )
def authenticate():

    session['username'] = request.form['username']
    session['password'] = request.form['password']
    # print(session)

    # Both username and password are valid ================
    if good(session['username'], session['password']):
        dictInput = story.getStory()
        return render_template("landing.html", d = dictInput)

    # All other invalid cases =============================
    else:
        msg = "It looks like you've entered an invalid password or username. Please try again."
        return (render_template("login.html", message = msg))

    print (url_for('disp_login'))
    print (url_for('authenticate'))
    return redirect(url_for("disp_login"))


app.secret_key = os.urandom(32)


@app.route('/logout')
def logout():
    return ( render_template ( "login.html", message = "You have been successfully logged out."))

    print(app)
    print(request) ##prints returned URL with auth tags
    print(request.args) ##gives immutabledict based on names of input fields (ie username & sub1)
    print(request.args['username'])
    print(request.headers)
    return "Waaaa hooo HAAAH"


if __name__ == "__main__":
    app.debug = True
    app.run()
