# Write your code here
import sqlite3
connection = sqlite3.connect('python_pulse.db')
cursor = connection.cursor()
# Create a table to store pulse data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        age INTEGER NOT NULL, 
        pulse_rate INTEGER NOT NULL
    )
    ''')
cursor.execute ('''
    CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user id INTEGER,
    height REAL NOT NULL,
    weight REAL NOT NULL,
    ))
    

















# DON'T DELETE THIS LINE - Commit the changes and close the connection. This should be the LAST line of your program.
connection.commit()
connection.close()