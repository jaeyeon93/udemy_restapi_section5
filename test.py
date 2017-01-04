# -*- coding:utf-8 -*-
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
# users name table has 3 columns id, username, password
cursor.execute(create_table)

user = (1, 'jose','asdf')
# user data type is tuple
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'rolf','asdf'),
    (3, 'anne', 'xyz')
]
cursor.executemany(insert_query, users)


select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print (row)

# this code shows insert data tuple on terminal

connection.commit()
connection.close()

