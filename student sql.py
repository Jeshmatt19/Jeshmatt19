import sqlite3
connection=sqlite3.connect("student.db")
crsr=connection.cursor()
sql_command="""CREATE TABLE school(stid INTEGER PRIMARY KEY,fname VARCHAR(300),Lname VARCHAR(300),gender CHAR(1),date1 DATE);"""
crsr.execute(sql_command)
print("Table Created Successfully")
connection.close()
