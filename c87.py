# Update Query


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

sql = 'UPDATE student SET fees=200 WHERE stuid = 18'
# sql = 'INSERT INTO student(name, roll, fees) VALUES("Jai", 113, 1000), ("Veeru", 114, 1000), ("Basnti", 115, 1000)'
myc = conn.cursor()

try:
    myc.execute(sql)
    conn.commit()
    print(myc.lastrowid, "= Row Updated")
except:
    conn.rollback()
    print("Unable to Update Data")
myc.close()
conn.close()