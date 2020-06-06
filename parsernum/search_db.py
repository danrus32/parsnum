import sqlite3
import re
db = sqlite3.connect("date.db")
sql = db.cursor()
inputdate =str(input("Enter a word or number for, search:\n"))
for value in sql.execute("SELECT * FROM  users"):
    if re.search(inputdate, str(value)):
   
        print(value)
