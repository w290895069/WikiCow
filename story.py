import sqlite3
from datetime import datetime

DB_FILE = "database.db"

# creates the story table
def createTable():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("CREATE TABLE stories (story TEXT, contributer TEXT, timestamp TEXT, contribution TEXT)")
    db.commit()
    db.close()


# creates an entry in the story table
def updateStory(title, user, text):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    params = (title, user, getTime(), text)
    c.execute("INSERT INTO stories VALUES (?, ?, ?, ?)", params)
    db.commit()
    db.close()

# given the title, return a complete story by concatenating all entries if true and a preview if not
def getStory(title,fullStory):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM stories WHERE story = '" + title + "';")
    text = ''
    for row in data:
        if (fullStory):
            text += row[3] + ' '
        else:
            text = row[3] + ' '
    db.close()
    return text


# given the title, returns a list of all writers
def getWriters(title):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM stories WHERE story = '" + title + "';")
    writers = []
    for row in data:
        if row[1] not in writers:
            writers.append(row[1])
    db.close()
    return writers

# helper fxn: returns a string of current time in 'yyyy-mm-dd hh:mm:ss' format
def getTime():
    timeNow = str(datetime.now())
    timeNow = timeNow[: timeNow.find('.')]
    return timeNow

# prints a dictionary of format title: [contributer, timestamp, contribution] in the latest update
def getLastUpdate():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM stories;")
    titles = []
    for row in data:
        if row[0] not in titles:
            titles.append(row[0])
    data = c.execute("SELECT * FROM stories;")
    dict = {}
    for row in data:
        for title in titles:
            # print(row)
            if title == row[0]:
                dict[title] = row[1: ]
    db.close()
    return dict

# returns True if usr contributed to story, False otherwise
def contributed(usr, title):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM stories;")
    for row in data:
        if row[0] == title and row[1] == usr:
            db.close()
            return True
    db.close()
    return False

# print(getTime())
# createTable()
