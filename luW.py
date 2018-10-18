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
    return text
        
def getTime():
    timeNow = str(datetime.now())
    timeNow = timeNow[: timeNow.find('.')]
    return timeNow

#print(getTime())
print(getStory('title'))
