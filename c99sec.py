# Parameterixed Query in Dictionary
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

sql = 'DELETE FROM student WHERE stuid=%(id)s'

myc = conn.cursor()

n = int(input('Enter ID to Delete: '))
del_value = {'id':n}

# del_value = {'id':44}


try:
    myc.execute(sql,del_value)
    conn.commit()
    print(myc.rowcount, "Row Deleted")
except:
    conn.rollback()
    print("Unable to Delete Data")
myc.close()
conn.close()