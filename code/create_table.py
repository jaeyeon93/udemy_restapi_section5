import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# sqlite3 gives auto increment
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
# real is decimal, decimal contain float, integer
cursor.execute(create_table)

connection.commit()

connection.close()