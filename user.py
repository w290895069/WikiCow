import sqlite3

DB_FILE = "database.db"

# creates table called users
def createTable():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("CREATE TABLE users (user TEXT, password TEXT, question TEXT, answer TEXT)")
    db.commit()
    db.close()

# if username already exists, returns false. otherwise inserts a row in users, returns true.
def register(usr, psw, q, a):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM users;")
    for row in data:
        if usr == row[0]:
            return False
    params = (usr, psw, q, a)
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", params)
    db.commit()
    db.close()
    return True

# returns true if username and password match, false otherwise
def authenticate(usr, psw):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM users")
    for row in data:
        if row[0] == usr and row[1] == psw:
            db.close()
            return True
    db.close()
    return False

# trivial
def resetPassword(usr, psw):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    params = (psw, usr)
    c.execute("UPDATE users SET password = ? WHERE user = ?", params)
    db.commit()
    db.close()

def getQuestion(usr):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM users")
    for row in data:
        if row[0] == usr:
            db.close()
            return row[2]
    db.close()
    return -1

def checkAnswer(usr, ans):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM users")
    for row in data:
        if row[0] == usr:
            db.close()
            return row[3] == ans

# createTable()
