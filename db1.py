import sqlite3
conn=sqlite3.connect("moksh.db")
print("Database Created")
#sql='''create table emp(id int, name text, salary int)'''
sql='''insert into emp(id,name,salary) values(2,"Nidhi",50000)'''
conn.execute(sql)
conn.commit()
conn.close()
print("Table Created")