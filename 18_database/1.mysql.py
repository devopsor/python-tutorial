#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='password', database='test')

cursor = conn.cursor()
# Create the user table:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# Insert a row, note that the MySQL placeholder is %s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
#Commit transaction:
conn.commit()
cursor.close()

# Run the query:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# Close Cursor and Connection:
cursor.close()
conn.close()