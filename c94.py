# Parameterixed Query in Tupple
# Insert Multiple Row
# executemany() Method


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
seq_of_params = [("Rani", 105, 45000), ("Seema", 106, 20000), ("Rima", 107, 5000)]


try:
    myc.executemany(sql, seq_of_params)
    conn.commit()
    
    print( "Row Inserted =", myc.rowcount)
    print(f'Student ID:{myc.lastrowid} Inserted')


except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()
conn.close()