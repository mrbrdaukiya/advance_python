# lastrowid Property


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

# sql = 'INSERT INTO student(name, roll, fees) VALUES("JatBaba", 112, 50000)'
sql = 'INSERT INTO student(name, roll, fees) VALUES("Jai", 113, 1000), ("Veeru", 114, 1000), ("Basnti", 115, 1000)'
myc = conn.cursor()

try:
    myc.execute(sql)
    conn.commit()
    print(myc.lastrowid, "= Last Row Insert ID")
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()
conn.close()