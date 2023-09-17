# Creating a thread

from threading import Thread
def disp(a,b):
    print("Thread Running", a, b)

t = Thread(target=disp, args=(10,20))
t.start()

# for i in range(5):
#     t = Thread(target=disp, args=(10,20))

#     t.start()

print("***************************************************")


from threading import Thread
def disp():
    for i in range(5):
        print("Child Thread")

t = Thread(target=disp)
t.start()

for i in range(5):
    print("Main Thread")


print("***************************************************")


from threading import Thread
def disp():
    for i in range(5):
        print("Publish Video C")

t = Thread(target=disp)
t.start()

for i in range(5):
    print("Publish Video M")


for i in range(10):
    print("Publish Video")