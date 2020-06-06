import sqlite3
db = sqlite3.connect("date.db")
sql = db.cursor()

for value in sql.execute("SELECT * FROM  users"):
    print(value)
