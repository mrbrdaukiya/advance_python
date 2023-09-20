# Parameterixed Query in Tupple
# Insert single Row


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


sql = 'INSERT INTO student(name, roll, fees) VALUES (%s, %s, %s)'

myc = conn.cursor()
params = ("Sumit", 116, 3000.50)


try:
    myc.execute(sql, params)
    conn.commit()
    
    print( "Row Inserted =", myc.rowcount)
    print(f'Student ID:{myc.lastrowid} Inserted')


except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()
conn.close()