import sqlite3, time
from datetime import datetime

def createStory(title, user, text):
    db = sqlite3.connect('database.db')
    c = db.cursor
    params = (title, user, getTime(), text)
    c.execute('INSERT INTO stories VALUES (?, ?, ?, ?)', params)

def getTime():
    timeNow = str(datetime.now())
    timeNow = timeNow[: timeNow.find('.')]
    return timeNow

print(getTime())
