# Alexander Liu
# SoftDev1 pd7
# P #00: Da Art of Storytellin'
# 2018-10-17

from flask import Flask, render_template, request, session, url_for, redirect
import user
import story
import os

app = Flask(__name__)

@app.route('/')
def disp_login():
    loginMess = "Please enter a valid username and password."
    return render_template("login.html", message = loginMess)

@app.route('/signup')
def signup():
    loginMess = "Please enter a valid username and password to signup :)"
    return render_template("signup.html", message = loginMess)

@app.route('/signupauth', methods = ['POST'] )
def sign_Auth():
        print("PRINTING SESSIONS \n")
        print(session)

        session['username'] = request.form['username']
        session['password0'] = request.form['password0']
        session['password1'] = request.form['password1']
        session['question'] = request.form['question']
        session['answer'] = request.form['answer']

        print(session)
        print(session['username'])

        # Invalid username: ===================================
        if len(session['username']) < 3:
            msg = "It looks like you've entered an invalid username. Please try again."
            # print('bad username')
            return render_template("signup.html", message = msg)

        # Invalid password: ===================================
        elif len(session['password0']) < 5:
            msg = "It looks like your password does not have enough characters. Please try again."
            # print('bad password')
            return render_template("signup.html", message = msg)

        # Both username and password are valid ================
        elif len(session['username']) >= 3 and len(session['password0']) >= 5:
            # enter username and password into the database
            # command = 'INSERT INTO users VALUES(' + session['username'] + ' , ' + session['password'] + ')'
            # c.execute(command)
            # db.commit()
            # db.close()
            if session['password0'] != session['password1']:
                msg = "Signup failed. Passwords don't match"
                return render_template("signup.html", message = msg)

            elif user.register(session['username'], session['password0'], session['question'], session['answer']):
                msg = "You have successfully signed up"
                return render_template("login.html", message = msg)

            else:
                msg = "Signup failed. Username already exists"
                return render_template("signup.html", message = msg)

        # All other invalid cases =============================
        else:
            msg = "Oops! Looks like something went wrong. Please try again."
            return render_template("signup.html", message = msg )

        print (url_for('disp_login'))
        print (url_for('authenticate'))
        return redirect(url_for("disp_login"))

# what is the difference between render_template, redirect, and url_for?
@app.route('/auth', methods = ['POST'] )
def authenticate():

    session['username'] = request.form['username']
    session['password'] = request.form['password']
    print(session)

    # Both username and password are valid ================
    if user.authenticate(session['username'], session['password']):
        return redirect("/menu")

    # All other invalid cases =============================
    else:
        msg = "It looks like you've entered an invalid password or username. Please try again."
        return render_template("login.html", message = msg)

    print (url_for('disp_login'))
    print (url_for('authenticate'))
    return redirect(url_for("disp_login"))


app.secret_key = os.urandom(32)

@app.route('/add', methods = ['POST'])
def add():
    session['title'] = request.form['title']
    msg = "Please add new content to " + session['title']
    return render_template('constructor.html', message = msg)

@app.route('/create')
def create():
    msg = "Please create a new story"
    return render_template('new_story.html', message = msg)

@app.route('/complete', methods = ['POST'])
def complete():
    if 'title' not in session:
        session['title'] = request.form['title']
    session['content'] = request.form['content']
    story.updateStory(session['title'], session['username'], session['content'])
    msg = "Story Updated"
    return render_template('complete.html', message = msg)

@app.route('/menu')
def menu():
    def contributed(usr, title):
        return story.contributed(usr, title)
    return render_template("landing.html", d = story.getLastUpdate(), u = session['username'], c = contributed)

@app.route('/logout')
def logout():
    return ( render_template ( "login.html", message = "You have been successfully logged out."))

    print(app)
    print(request) ##prints returned URL with auth tags
    print(request.args) ##gives immutabledict based on names of input fields (ie username & sub1)
    print(request.args['username'])
    print(request.headers)


if __name__ == "__main__":
    app.debug = True
    app.run()
