import sqlite3

try:
    db=sqlite3.connect("newdb.db")#create/connect database
    print("Database connected!")
except Exception as e:
    print(e)

#Table create
tbl_create="create table studinformation(id integer primary key autoincrement,name text,city text)"

try:
    db.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

#Insert data
"""insert_data="insert into studinformation(name,city)values('hemil','rajkot'),('ryan','mumbai'),('ayaan','ahmedabad'),('prince','surendranagar'),('raj','surat')"

try:
    db.execute(insert_data)
    db.commit()
    print("Data inserted!")
except Exception as e:
    print(e)"""

#Update data
update_data="update studinformation set name='arnav' where name='prince'"
try:
    db.execute(update_data)
    db.commit()
    print("Data updated!")
except Exception as e:
    print(e)

