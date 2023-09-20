# Parameterixed Query in Dictionary
# Data Insert in Table --->> Multitape Row

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


    sql = 'INSERT INTO student(name, roll, fees) VALUES (%(name)s, %(roll)s, %(fees)s)'

    myc = conn.cursor()
    n = nm
    r = ro
    f = fe
    params = {'name':n,'roll': r, 'fees':f}


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
    if(ans=='y'):
        break 