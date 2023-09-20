# Parameterixed Query in Tupple
# Insert Multiple Row
# executemany() Method


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


    sql = 'INSERT INTO student(name, roll, fees) VALUES (%s, %s, %s)'

    myc = conn.cursor()
    # Input from user
    # nm = input('Enter Name:')
    # ro = int(input('Enter Roll:'))
    # fe = float(input('Enter Fees:'))
    # params = (nm, ro, fe)

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