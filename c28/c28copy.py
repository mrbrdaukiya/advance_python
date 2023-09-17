# Module main

import first
import second

print(first.a)
first.name()

print("--------------------------------------------")

print(second.a)
second.name()

print("* 1st *************************************************************")

import first as f
import second as s

print(f.a)
f.name()

print("--------------------------------------------")

print(s.a)
s.name()


print("* 2nd *************************************************************")

# from first import a , name 
from first import *

print(a)

name()

# print(tup)

print("--------------------------------------------")
# from second import a , name 
from second import *

print(a)
name()

# next in c28copy.py