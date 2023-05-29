import sqlite3
connection=sqlite3.connect("ABC.db")
cursor=connection.cursor
sql_command="""CREATE TABLE item(icode INTEGER PRIMARY KEY,item name VARCHAR(25),rate INTEGER"""
cursor.execute(sql_command)
sql_command="""INSERT INTO item(icode,item name,rate)VALUES(1008,'monitor',15000);"""
cursor.execute(sql_command)
connection.commit()
connection.close()
print("table created")






























