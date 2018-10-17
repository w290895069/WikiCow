import sqlite3, time

def createStory(title, user, text):
    db = sqlite3.connect('database.db')
    c = db.cursor
    params = (title, user, time, text)
    c.execute('INSERT INTO stories VALUES (?, ?, ?, ?)', params)
