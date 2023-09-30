# Prepared statement 
# Delete Row in Tupple




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
sql = 'DELETE FROM student WHERE stuid=?'

myc = conn.cursor(prepared=True)

n = int(input('Enter ID to Delete: '))
del_value = (n,)

# del_value = (56,)s


try:
    myc.execute(sql,del_value)
    conn.commit()
    print("Row Deleted")
except:
    conn.rollback()
    print("Unable to Delete Data")
myc.close()                # Close Cursor
conn.close()               # Close Connection