# Prepared statement 
# Insert Single and Multiple Row in Tupple



import mysql.connector
# def student_data(nm, ro, fe):
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


# sql = 'INSERT INTO student(name, roll, fees) VALUES (%s, %s, %s)'
sql = 'INSERT INTO student(name, roll, fees) VALUES (?, ?, ?)'


myc = conn.cursor(prepared=True)
# Input from user
# nm = input('Enter Name:')
# ro = int(input('Enter Roll:'))
# fe = float(input('Enter Fees:'))
# params = (nm, ro, fe)

# params = ("Rohan", 111, 5000.75)

# params = [
#     ("Niti", 333, 1000),
#     ("Mohan", 444, 1000),
#     ("Shreya", 555, 1000),]


try:
    myc.execute(sql, params)
    conn.commit()
        
    print( "Row Inserted =", myc.rowcount)
    print(f'Student ID:{myc.lastrowid} Inserted')


except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()
conn.close()




print("--------------------------------------------------------")



import mysql.connector
def student_data(nm, ro, fe):
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


    # sql = 'INSERT INTO student(name, roll, fees) VALUES (%s, %s, %s)'
    sql = 'INSERT INTO student(name, roll, fees) VALUES (?, ?, ?)'


    myc = conn.cursor(prepared=True)
    n = nm
    r = ro 
    f = fe 
    params = (n, r, f)

    try:
        myc.execute(sql, params)
        conn.commit()
            
        print( "Row Inserted =", myc.rowcount)
        print(f'Student ID:{myc.lastrowid} Inserted')


    except:
        conn.rollback()
        print("Unable to Insert Data")
    myc.close()
    conn.close()



while True:
    # Input from user
    nm = input('Enter Name:')
    ro = int(input('Enter Roll:'))
    fe = float(input('Enter Fees:'))
    student_data(nm, ro, fe)
    ans = input('Do You Want to exit?(y/n)')
    if(ans == 'y'):
        break 