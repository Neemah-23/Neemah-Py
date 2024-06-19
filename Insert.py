import sqlite3

conn = sqlite3.connect('test.db')
print("Successfully connected")

conn.execute("INSERT INTO TEACHERS VALUES(1,'James','Kariuki',45,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(2,'Sofia','Sarita',34,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(3,'John','Kamau',44,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(4,'Shantel','Makena',18,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(5,'Carlos','Mio',21,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(6,'Faith','Sheba',23,56000.00)")

conn.commit()
print("Successfully inserted records")

conn.close()