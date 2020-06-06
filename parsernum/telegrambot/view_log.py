import sqlite3
db = sqlite3.connect("log.db")
sql = db.cursor()

for value in sql.execute("SELECT * FROM  USERS"):
    print(value)
