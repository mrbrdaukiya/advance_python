#fetchone() Method


import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root', 
        password ='guru',
        host='localhost',
        database='pdb', 
        port=3306
    )
    if(conn.is_connected()):
        print("connected")
except:
    print('Unable to Conect')



# sql = 'SELECT * FROM student'
sql = 'SELECT roll FROM student'
myc = conn.cursor()

try:
    myc.execute(sql)
    row = myc.fetchone()
    while row is not None:
        print(row)
        # stuid = row[0]
        # name = row[1]
        # roll = row[2]
        # fees = row[3]
        # print(f'Student ID: {stuid} Name: {name} Roll: {roll} Fees: {fees}')

        row = myc.fetchone()

    print(myc.rowcount, "= Total Row")
except:
    conn.rollback()
    print("Unable to Fetch Data")
myc.close()
conn.close()