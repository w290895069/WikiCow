import sqlite3

DB_FILE = "database.db"

def createTable():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("CREATE TABLE users (user TEXT, pass TEXT, question TEXT, answer TEXT)")
    db.commit()
    db.close()

def register(usr, pass, q, a):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    params = (usr, pass, q, a)
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", params)
    db.commit()
    db.close()

def authenticate(usr, pass):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    line = c.execute("SELECT * FROM users WHERE user = " + usr)
    if len(line) == 0 or line[1] != pass:
        db.close()
        return False
    db.close()
    return True
