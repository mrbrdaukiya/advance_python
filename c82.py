# Create Table

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

# sql = 'CREATE TABLE student2(stuid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), roll INT, fees FLOAT)'
# myc = conn.cursor()
# myc.execute(sql)


# conn.close()
# conn.close()


print("------------------------------------------------------------------------------------")



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

sql = 'SHOW TABLES'
myc = conn.cursor()
myc.execute(sql)

for t in myc:
    print(t)


conn.close()
conn.close()