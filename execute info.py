import sqlite3
connection=sqlite3.connect("student.db")
crsr=connection.cursor()
#fetching record
crsr.execute("SELECT * FROM school")
ans=crsr.fetchall()
for i in ans:
    print(i)
        
