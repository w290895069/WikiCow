import sqlite3, time
from datetime import datetime

# creates an entry in the story table
def createStory(title, user, text):
    db = sqlite3.connect('database.db')
    c = db.cursor()
    params = (title, user, getTime(), text)
    c.execute('INSERT INTO stories VALUES (?, ?, ?, ?)', params)
    db.commit()
    db.close()

# given the title, return a complete story by concatenating all entries
def getStory(title):
    db = sqlite3.connect('database.db')
    c = db.cursor()
    data = c.execute("SELECT * FROM stories WHERE story = '" + title + "';")
    text = ''
    for row in data:
        text += row[3]
    db.close()
    return text

# given the title, returns a list of all writers
def getWriters(title):
    db = sqlite3.connect('database.db')
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

#print(getTime())
print(getStory('title'))
createStory('title', 'qwer', 'they killed themselves.')
print(getStory('title'))
print(getStory('title1'))
print(getWriters('title'))
