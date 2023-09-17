# Daemon Thread 

from threading import *
from time import *

def disp():
    print('Daemon Thread')

t1 = Thread(target=disp)
print('Before :', t1.daemon)
# t1.setDaemon(True)
t1.daemon = True
print('After :', t1.daemon)
t1.start()


print()
print("************************************************")
print()


mt = current_thread()
print(mt.getName())
print(mt.daemon)



print()
print("************************************************")
print()

def disp():
    print('Disp Function')

mt = current_thread()
print(mt.getName())
print('MT', mt.isDaemon())
t1 = Thread(target=disp)
t1.start()
print('T1', t1.isDaemon())





print()
print("************************************************")
print()

def disp():
    print('Disp Function')
    t2 = Thread(target=show)
    print('T2 :', t2.isDaemon())
    t2.start()

def show():
    print('Show Function')

mt = current_thread()
print(mt.getName())
print('MT', mt.isDaemon())
t1 = Thread(target=disp)
print('T1 Before', t1.isDaemon())
t1.setDaemon(True)
print('T1 After', t1.isDaemon())
t1.start()
t1.join()

print()
print('Main Thread')






print()
print("************************************************")
print()


def teacher():
    for i in range(1, 11):
        print('Teaching Session :', i)
        sleep(1)

t1 = Thread(target=teacher)
# t1.daemon = True
t1.setDaemon(True)
t1.start()
sleep(6)
t1.join()
print('Exam Finish', current_thread().name)