# Prepared statement 
# Retrieve Data Row in Tupple --->> 


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

# sql = 'SELECT * FROM student WHERE stuid = %s'
sql = 'SELECT * FROM student WHERE stuid = ?'

myc = conn.cursor(prepared=True)

# Data Input from User
n = int(input('Enter Student ID to Display: '))
disp_value = (n,)
# disp_value = (54,)

try:
    myc.execute(sql, disp_value)
    row = myc.fetchone()
    print(row)
    print(myc.rowcount, "= Total Row ")
except:
    print("Unable to Retrieve Data")
myc.close()                # Close Cursor
conn.close()               # Close Connection