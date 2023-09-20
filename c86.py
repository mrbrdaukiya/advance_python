# Delete Row Data


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

sql = 'DELETE FROM student WHERE stuid=12'
# sql = 'INSERT INTO student(name, roll, fees) VALUES("Jai", 113, 1000), ("Veeru", 114, 1000), ("Basnti", 115, 1000)'
myc = conn.cursor()

try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount, "Row Deleted")
except:
    conn.rollback()
    print("Unable to Delete Data")
myc.close()
conn.close()