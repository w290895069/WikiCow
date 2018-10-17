#Creates data base called database.db

import sqlite3

DB_FILE = "database.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()


command = "CREATE TABLE users (username TEXT, password TEXT)"
c.execute(command)

command = "CREATE TABLE stories (story TEXT, contributer TEXT, timestamp TEXT, contribution TEXT)"
c.execute(command)

db.commit()
db.close()
