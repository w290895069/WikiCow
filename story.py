import sqlite3, time
from datetime import datetime

def createStory(title, user, text):
    db = sqlite3.connect('database.db')
    c = db.cursor()
    params = (title, user, getTime(), text)
    c.execute('INSERT INTO stories VALUES (?, ?, ?, ?)', params)
    db.commit()
    db.close()
    
def getStory(title):
    db = sqlite3.connect('database.db')
    c = db.cursor()
    data = c.execute("SELECT * FROM stories WHERE story = '" + title + "';")
    text = ''
    for row in data:
        text += row[3]
    db.close()
    return text

def getWriters(title):
    db = sqlite3.connect('database.db')
    c = db.cursor()
    data = c.execute("SELECT * FROM stories WHERE story = '" + title + "';")
    writers = []
    for row in data:
        if row[1] not in writers:
            writers.append(row[1])
    return writers

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
