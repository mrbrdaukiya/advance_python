# Parameterixed Query in Dictionary
# Retrieve Multiple Row with WHERE Clause --->> 


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

sql = 'SELECT * FROM student WHERE fees= %(fees)s'
myc = conn.cursor()

# Data Input from User
n = int(input('Enter Student Fees to Display: '))
disp_value = {'fees': n}
# disp_value = {'fees': 1000}

try:
    myc.execute(sql, disp_value)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    print(myc.rowcount, "= Total Row ")
except:
    print("Unable to Retrieve Data")
myc.close()                # Close Cursor
conn.close()               # Close Connection