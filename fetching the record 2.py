import sqlite3
connection=sqlite3.connect("Form.db")
crsr=connection.cursor()
crsr.execute("SELECT * From Student")
ans=crsr.fetchall()
for i in ans:
    print(i)
