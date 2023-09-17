from threading import Thread, current_thread

def disp():
    print("Child Thread Object", current_thread())


t = Thread(target=disp)
t.start()

print("Main Thread", current_thread())


print()
print("*********************************************")
print()

from threading import Thread, current_thread

def disp():
    print("Child Thread Name :", current_thread().getName())


t = Thread(target=disp)
t.start()


print("Main Thread Name :", current_thread().getName())



print()
print("*********************************************")
print()

from threading import Thread, current_thread

def disp():
    print("Default Child Thread Name :", current_thread().getName())
    current_thread().setName('Doc Thread')
    print("New Child Thread Name :", current_thread().getName())


t = Thread(target=disp)
t.start()


print("Default Main Thread Name :", current_thread().getName())
current_thread().setName('Guru Thread')
print("New Main Thread Name :", current_thread().getName())




print()
print("*********************************************")
print()

from threading import Thread, current_thread

def disp():
    print("Child", current_thread().name)


t = Thread(target=disp)
t.start()


print("Main", current_thread().name)


print()
print("*********************************************")
print()

from threading import Thread, current_thread

def disp():
    print("Default Child Thread Name :", current_thread().name)
    current_thread().name ='Flying Thread'
    print("New Child Name :", current_thread().name)


t = Thread(target=disp)
t.start()


print("Default Main Thread Name :", current_thread().name)
current_thread().name ='Guru Thread'
print("New Main Name :", current_thread().name)



print()
print("*********************************************")
print()

from threading import Thread, current_thread

def disp():
    pass


t = Thread(target=disp)
print(t.getName())




print()
print("*********************************************")
print()

from threading import Thread

def disp():
    pass


t = Thread(target=disp)
print("Default", t.getName())
t.setName('Doc Thread')
print("New", t.getName())




print()
print("*********************************************")
print()

from threading import Thread

def disp():
    pass


t = Thread(target=disp)
print("Default", t.name)
t.name = 'Flying Thread'
print("New", t.name)






print()
print("*********************************************")
print()

from threading import Thread

def disp():
    pass


t = Thread(target=disp,name='Guru Thread')
print(t.name)