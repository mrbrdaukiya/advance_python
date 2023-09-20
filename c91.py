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


# sql = 'SELECT * FROM student WHERE stuid=15'
sql = 'SELECT * FROM student WHERE fees=1000'
myc = conn.cursor(buffered=True)

try:
    myc.execute(sql)
    row = myc.fetchone()
    # print(row)
    while row is not None:
        print(row)
        row = myc.fetchone()


    print( "Total Row =", myc.rowcount)
except:
    conn.rollback()
    print("Unable to Fetch Data")
myc.close()
conn.close()