#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# Connect to SQLite database
# The database file is test.db
# If the file does not exist, it will be automatically created in the current directory:
conn = sqlite3.connect('test.db')
# Create a Cursor:
cursor = conn.cursor()
# Execute an SQL statement to create the user table:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# Continue to execute an SQL statement to insert a record:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# Get the number of inserted rows by rowcount:
print('rowcount =', cursor.rowcount)
# Close Cursor:
cursor.close()
#Commit transaction:
conn.commit()
# Close Connection:
conn.close()

# search records：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#execute the query statement:
cursor.execute('select * from user where id=?', '1')
#  Get the query result set
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()