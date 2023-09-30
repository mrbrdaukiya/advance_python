# Prepared statement 
# Delete Row in Tupple --->> 


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

# sql = 'UPDATE student SET  fees=%s WHERE stuid = %s'
# sql = 'UPDATE student SET  fees=? WHERE stuid = ?'
sql = 'UPDATE student SET name=?, roll=?, fees=? WHERE stuid = ?'


myc = conn.cursor(prepared=True)

# Data Input from User
id = int(input('Enter Student ID to Update: '))
nm = input('Enter Name: ')
ro = int(input('Enter Roll:'))
fe = float(input('Enter Fees:'))
uptate_value = (nm, ro, fe, id)
# uptate_value = (800, 54)

try:
    myc.execute(sql, uptate_value)
    conn.commit()
    print("Row Updated")
except:
    conn.rollback()
    print("Unable to Update Data")
myc.close()
conn.close()