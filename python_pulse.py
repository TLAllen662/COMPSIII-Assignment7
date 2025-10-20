# Write your code here
import sqlite3
connection = sqlite3.connect('python_pulse.db')
cursor = connection.cursor()
# Create a table to store pulse data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL, 
        password TEXT NOT NULL, 
        email TEXT NOT NULL
    )
    ''')
cursor.execute("INSERT INTO User (user_id, username, password, email) VALUES (1, 'Alice', 'password123', 'alice@gmail.com');") 
cursor.execute("INSERT INTO User (user_id, username, password, email) VALUES (2, 'Bob', 'securepwd456', 'bob@gmail.com');") 
cursor.execute ('''
    CREATE TABLE IF NOT EXISTS profiles (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    height REAL NOT NULL,
    weight REAL NOT NULL,
    age INTEGER,
    notes TEXT
    )
    ''')
cursor.execute("INSERT INTO Profile (profile_id, user_id, height, weight, age, notes) VALUES (1, 1, 5.5, 130, 28, 'Loves running and yoga.');")
cursor.execute("INSERT INTO Profile (profile_id, user_id, height, weight, age, notes) VALUES (2, 2, 6.0, 180, 32, 'Enjoys cycling and swimming.');")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS goals (
    goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    target_value REAL NOT NULL,
    user_id INTEGER
    )
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS workouts (
    workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    duration INTEGER NOT NULL
    )
    ''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_workouts (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
    
)
''')

















# DON'T DELETE THIS LINE - Commit the changes and close the connection. This should be the LAST line of your program.
connection.commit()
connection.close()