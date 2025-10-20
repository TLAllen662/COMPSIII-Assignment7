# Write your code here
import sqlite3
connection = sqlite3.connect('python_pulse.db')
cursor = connection.cursor()
# Create a table to store user information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL, 
        password TEXT NOT NULL, 
        email TEXT NOT NULL
    )
    ''')
# Insert sample user data
cursor.execute("INSERT INTO User (user_id, username, password, email) VALUES (1, 'Alice', 'password123', 'alice@gmail.com');") 
cursor.execute("INSERT INTO User (user_id, username, password, email) VALUES (2, 'Bob', 'securepwd456', 'bob@gmail.com');") 
#Create a table to store user profile information
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
# Insert sample profile data
cursor.execute("INSERT INTO Profile (profile_id, user_id, height, weight, age, notes) VALUES (1, 1, 5.5, 130, 28, 'Loves running and yoga.');")
cursor.execute("INSERT INTO Profile (profile_id, user_id, height, weight, age, notes) VALUES (2, 2, 6.0, 180, 32, 'Enjoys cycling and swimming.');")
# Link users with their profiles
cursor.execute('''
SELECT user_id, username, email
FROM users;
JOIN profile ON User.id = profile.user_id;
''')
connection.commit()
print(cursor.fetchall()) 
# create tables for goals
cursor.execute('''
    CREATE TABLE IF NOT EXISTS goals (
    goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    target_value REAL NOT NULL,
    user_id INTEGER
    )
    ''')
# Insert sample goal data
cursor.execute("INSERT into goals (goal_id, name, target_value, user_id) VALUES (1, 'Lose Weight', 10.0, 1);")
cursor.execute("INSERT into goals (goal_id, name, target_value, user_id) VALUES (2, 'Run 5K', 5.0, 2);")
#Link users with their goals
cursor.execute('''
SELECT user_id, username, email
FROM users;
JOIN goals ON users.user_id = goals.user_id;
''')
print(cursor.fetchall())
connection.commit()
# create tables for workouts
cursor.execute('''
    CREATE TABLE IF NOT EXISTS workouts (
    workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    duration INTEGER NOT NULL
    )
    ''')
# insert sample workout data
cursor.execute("INSERT into workouts (workout_id, name, description, duration) VALUES (1, 'Morning Run', 'A quick 30 minute run to start the day.', 30);")
cursor.execute("INSERT into workouts (workout_id, name, description, duration) VALUES (2, 'Evening Yoga', 'A relaxing 45 minute yoga session.', 45);")
#Link workouts with user workouts
cursor.execute('''
SELECT workout_id, name, description, duration
FROM workouts;
JOIN user_workouts ON workouts.workout_id = user_workouts.workout_id;
''')
print(cursor.fetchall())
connection.commit()
#create table for user workouts
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_workouts (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
)
''')
#insert sample user workout data
cursor.execute("INSERT into user_workouts (user_id, workout_id) VALUES (1,1);")
cursor.execute("INSERT into user_workouts (user_id, workout_id) VALUES (2,2);")
#Link user workouts with users
cursor.execute('''
SELECT user_id, workout_id
FROM user_workouts;
JOIN users ON users.user_id = user_workouts.user_id;
''')
print(cursor.fetchall())
connection.commit()

















# DON'T DELETE THIS LINE - Commit the changes and close the connection. This should be the LAST line of your program.
connection.commit()
connection.close()