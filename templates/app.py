# Alexander Liu
# SoftDev1 pd7
# P #00: Da Art of Storytellin'
# 2018-10-17

from flask import Flask, render_template, request, session, url_for, redirect
import os
app = Flask(__name__)

username = 'alex'
password = 'starwars4'

@app.route('/')
def disp_login():
    loginMess = "Please enter a valid username and password."
    return render_template("login.html", message = loginMess)

# what is the difference between render_template, redirect, and url_for?
@app.route('/auth', methods = ['POST'] )
def authenticate():

    session['username'] = request.form['username']
    session['password'] = request.form['password']
    # print(session)

    # Invalid username: ===================================
    if session['username'] != username:
        errorMess = "*cue sad trombone music* <br> It looks like you've entered an invalid username. Please try again."
        # print('bad username')
        return (render_template("login.html", message = errorMess))

    # Invalid password: ===================================
    elif session['password'] != password:
        errorMess = "*cue sad trombone music* \n It looks like your password does not match your username. Please try again."
        print('bad password')
        return (render_template("login.html", message = errorMess))

    # Both username and password are valid ================
    elif (session['username'] == username and session['password'] == password):
        return render_template("landing.html")

    # All other invalid cases =============================
    else:
        errorMess = "Oops! Looks like something went wrong. Please try again."
        return ((render_template("login.html", message = errorMess))


    print (url_for('disp_login'))
    print (url_for('authenticate'))
    return redirect(url_for("disp_login"))
app.secret_key = os.urandom(32)

@app.route('/logout')
def logout():
    return ( render_template ( "login.html", message = "You have been successfully logged out."))

    print(app)
    print(request) ##prints returned URL with auth tags
    print(request.args) ## gives immutabledict based on names of input fields (ie username & sub1)
    print(request.args['username'])
    print(request.headers)
    return "Waaaa hooo HAAAH"

if __name__ == "__main__":
    app.debug = True
    app.run()
