# Module main

import cal

print("Cal Module's Variable", cal.a)
cal.name()

add = cal.add
a = add(10, 60)
print(a)

b = cal.sub(50,20)
print(b)


print("******************************************************************")


import cal as c

print("Cal Module's Variable", c.a)
c.name()

add = c.add
a = add(10, 60)
print(a)

b = c.sub(50,20)
print(b)


print("******************************************************************")

from cal import a, name, add as s, sub

print(a)
name()
# a = add(10,20)
a = s(10,20)
print(a)
b = sub(20,10)
print(b)

print("******** Last ***************************************")

from cal import *

print(a)
name()
a = add(10,20)
print(a)
b = sub(20,10)
print(b)


# next in c28copy.py