import os
print(os.path.isfile('student.txt'))

print()
print("-----------------------------------------")
print()


import os
if os.path.isfile('student.txt'):
    f = open('student.txt')
    print('File Opened')
    f.close()
else:
    print('File Not Found')