# Parameterixed Query in Dictionary
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

sql = 'UPDATE student SET name=%(name)s, roll=%(roll)s, fees=%(fees)s WHERE stuid = %(id)s'
myc = conn.cursor()

# # Data Input from User
id = int(input('Enter Student ID to Update: '))
nm = input('Enter Name: ')
ro = int(input('Enter Roll:'))
fe = float(input('Enter Fees:'))
uptate_value = {'name': nm, 'roll': ro, 'fees':fe, 'id':id}

# uptate_value = {'name': 'Ramesh', 'roll': 122, 'fees':200, 'id':37}

try:
    myc.execute(sql, uptate_value)
    conn.commit()
    print(myc.rowcount, "= Row Updated")
except:
    conn.rollback()
    print("Unable to Update Data")
myc.close()
conn.close()