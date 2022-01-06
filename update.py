import sqlite3
conn=sqlite3.connect("moksh.db")
conn.execute("update emp set salary=60000 where id=1")
conn.commit()
conn.close()