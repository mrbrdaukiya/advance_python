

import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root', 
        password ='guru',
        host='localhost', 
        port=3306
    )
    if(conn.is_connected()):
        print("connected")
except:
    print('Unable to Conect')


print("Before Close :",conn.is_connected())
conn.close()
print("After Close :",conn.is_connected())














# import mysql.connector

# config = {
#     'user':'root',
#     'password':'guru',
#     'host':'localhost',
#     'port':3306
# }

# conn = mysql.connector.connect(**config)
# if(conn.is_connected()):
#     print('Connected')
