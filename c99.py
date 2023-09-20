# Parameterixed Query in Tupple
# Delete Data in Table --->> 


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

sql = 'DELETE FROM student WHERE stuid=%s'

myc = conn.cursor()

n = int(input('Enter ID to Delete: '))
del_value = (n,)

# del_value = (46,)


try:
    myc.execute(sql,del_value)
    conn.commit()
    print(myc.rowcount, "Row Deleted")
except:
    conn.rollback()
    print("Unable to Delete Data")
myc.close()
conn.close()