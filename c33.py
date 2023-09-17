# Time Module

from time import time, ctime, localtime
epoch = time()

print(epoch)

et = ctime(epoch)
print(et)

print(ctime())

print("------------------------------------------")

stobj = localtime()
print(stobj)

print("Year :", stobj.tm_year)
print("Month :", stobj.tm_mon)
print("Date :", stobj.tm_mday)
print("Hour :", stobj.tm_hour)
print("Minute :", stobj.tm_min)
print("Second :", stobj.tm_sec)

print("----------------------------------------------")

print(stobj.tm_mday, "/" ,stobj.tm_mon, "/" , stobj.tm_year )
print(stobj.tm_hour, ":" ,stobj.tm_min, ":" , stobj.tm_sec )