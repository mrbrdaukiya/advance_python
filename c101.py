# Parameterixed Query in Tupple
# Retrieve single Row with WHERE Clause --->> 


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

sql = 'SELECT * FROM student WHERE stuid = %s'
myc = conn.cursor()

# Data Input from User
n = int(input('Enter Student ID to Display: '))
# disp_value = (11,)
disp_value = (n,)

try:
    myc.execute(sql, disp_value)
    row = myc.fetchone()
    print(row)
    print(myc.rowcount, "= Total Row ")
except:
    print("Unable to Retrieve Data")
myc.close()                # Close Cursor
conn.close()               # Close Connection