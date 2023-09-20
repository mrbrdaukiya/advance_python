# Parameterixed Query in Tupple
# Update Data in Table --->> 


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

sql = 'UPDATE student SET name=%s, roll=%s, fees=%s WHERE stuid = %s'
myc = conn.cursor()

# Data Input from User
id = int(input('Enter Student ID to Update: '))
nm = input('Enter Name: ')
ro = int(input('Enter Roll:'))
fe = float(input('Enter Fees:'))
uptate_value = (nm, ro , fe, id)
# uptate_value = ('raju', 102 , 5000, 37)

try:
    myc.execute(sql, uptate_value)
    conn.commit()
    print(myc.rowcount, "= Row Updated")
except:
    conn.rollback()
    print("Unable to Update Data")
myc.close()
conn.close()