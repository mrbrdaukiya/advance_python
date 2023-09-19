# Create Database

import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root', 
        password ='guru',
        host='localhost', 
        port=3306
    )
    if(conn.is_connected()):
        print("connected")
except:
    print('Unable to Conect')


# sql ='CREATE DATABASE pdb'
sql ='SHOW DATABASES'
myc = conn.cursor()
myc.execute(sql)

for d in myc:
    print(d)

myc.close()
conn.close
