# Directory

import os
print(os.getcwd())

# os.mkdir('newdir')
# os.mkdir('mydir/mychilddir')
# os.makedirs('parentdir/childdir/grandchilddir')
# os.chdir('mydir')
# print(os.getcwd())
# os.rename('mydir', 'yourdir')
# os.rmdir('yourdir/mychilddir')
# os.removedirs("parentdir/childdir/grandchilddir")



w = os.walk('.', topdown=False)
w = os.walk('newdir', topdown=False)
for i in w:
    print(i)