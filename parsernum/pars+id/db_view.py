import sqlite3
db = sqlite3.connect("date.db")
sql = db.cursor()
i = 0
for value in sql.execute("SELECT * FROM  users"):
    print(value)

