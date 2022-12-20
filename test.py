import sqlite3

connection = sqlite3.connect("temperatur.db")
cursor = connection.cursor()

print(cursor.execute("SELECT * FROM daten").fetchall()), 
