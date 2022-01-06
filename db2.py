import mysql.connector
mydb=mysql.connector.connect(host="localhost",port="3306",database="python",user="root",password="")
mycursor=mydb.cursor() 
#mycursor.execute("insert into student values(1,'moksh',987654321,'Ahmedabad')") 
#mycursor.execute("update student set contact=123456789 where id=1") 
mycursor.execute("insert into student values(2,'nidhi',987654321,'Ahmedabad')") 
mycursor.execute("delete from student where id=1") 
mydb.commit() 
mydb.close() 