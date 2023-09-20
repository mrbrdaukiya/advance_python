# Insert Data(single and multiple)

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

# sql = 'INSERT INTO student(name, roll, fees) VALUES("Ashok", 102, 2000)'
# sql = 'INSERT INTO student(name, roll, fees) VALUES("Jai", 103, 4000), ("Veeru", 104, 25000)'
sql = 'INSERT INTO student(name, roll, fees) VALUES("Rani", 105, 45000), ("Seema", 106, 20000), ("Rima", 107, 5000)'
myc = conn.cursor()

try:
    myc.execute(sql)
    conn.commit()
    print("Row Inserted")
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()
conn.close()