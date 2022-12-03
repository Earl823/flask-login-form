import sqlite3

conn = sqlite3.connect('user.sqlite')
cursor = conn.cursor()

sql = """ CREATE TABLE USER (
	id integer PRIMARY KEY,
	email CHAR(20) NOT NULL,
	password CHAR(20) NOT NULL
)"""

cursor.execute(sql)