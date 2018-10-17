#Creates data base called database.db

import sqlite3

#name of file will be database.db
DB_FILE = "database.db"

#create database.db
db = sqlite3.connect(DB_FILE)
c = db.cursor()

#create table for usernames and passwords
command = "CREATE TABLE users (username TEXT, password TEXT)"
c.execute(command)

#create table for all of the stories and their entries
command = "CREATE TABLE stories (story TEXT, contributer TEXT, timestamp TEXT, contribution TEXT)"
c.execute(command)

#make changes to db and then closer
db.commit()
db.close()
