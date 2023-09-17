from threading import *


class Mythread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print('Child Thread Constructor')

    def run(self):
        pass

t = Mythread()
t.start()
print('Main Thread')



print()
print("*********************************************")
print()



from threading import *


class Mythread(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        print('Child Thread Constructor :', a)

    def run(self):
        pass

t = Mythread(10)
t.start()
print('Main Thread')