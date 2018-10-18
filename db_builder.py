# Creates data base called database.db

import sqlite3

# name of file will be database.db
DB_FILE = "database.db"

# create database.db
db = sqlite3.connect(DB_FILE)
c = db.cursor()

# create table for usernames and passwords
command = "CREATE TABLE users (username TEXT, password TEXT)"
c.execute(command)

# some hard coded values for now
params = [('clara', 'pass'), ('jiajie', 'pass1'), ('william', 'pass2'), ('alex', 'pass0')]
for i in params:
    c.execute('INSERT INTO users VALUES(?, ?)', i)


# create table for all of the stories and their entries
command = "CREATE TABLE stories (story TEXT, contributer TEXT, timestamp TEXT, contribution TEXT)"
c.execute(command)

# some hard coded values for now
# title, name of contributor, timestamp, their contribution
params = [('title', 'clara', '001', 'once upon a time'),
          ('title', 'jiajie', '010', 'there was a family'),
          ('title', 'william', '011', 'that lived in America.'),
          ('title1', 'alex', '001', 'The sky was blue,')]

for i in params:
    c.execute('INSERT INTO stories VALUES(?, ?, ?, ?)', i)

# make changes to db and then closer
db.commit()
db.close()
