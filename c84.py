# Rowcount Property


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

# sql = 'INSERT INTO student(name, roll, fees) VALUES("Sonam", 108, 35000)'
sql = 'INSERT INTO student(name, roll, fees) VALUES("neeru", 109, 1000), ("Diljit", 110, 1000), ("Gyppy", 111, 1000)'
myc = conn.cursor()

try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount, "Row Inserted")
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()
conn.close()