#fetcmany() Method


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


sql = 'SELECT * FROM student'
# sql = 'SELECT roll FROM student'
myc = conn.cursor(buffered=True)

try:
    myc.execute(sql)
    row = myc.fetchmany(5)
    for r in row:
        # print(r)
        stuid = r[0]
        name = r[1]
        roll = r[2]
        fees = r[3]
        print(f'Student ID: {stuid} Name: {name} Roll: {roll} Fees: {fees}')
    print()
    # row = myc.fetchall()
    # for r in row:
    #     # print(r)
    #     stuid = r[0]
    #     name = r[1]
    #     roll = r[2]
    #     fees = r[3]
    #     print(f'Student ID: {stuid} Name: {name} Roll: {roll} Fees: {fees}')

    print( "Total Row =", myc.rowcount)
except:
    conn.rollback()
    print("Unable to Fetch Data")
myc.close()
conn.close()