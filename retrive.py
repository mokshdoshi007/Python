import sqlite3
conn=sqlite3.connect("moksh.db")
print("Database opened")
cursor=conn.execute("select * from emp")
for row in cursor:
    print("Id - {}, Name - {}, Salary - {}".format(row[0],row[1],row[2]))
conn.close()