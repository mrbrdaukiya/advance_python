from threading import Thread

class Mythread(Thread):
    pass

t = Mythread()
print(t.name)



print()
print("*********************************************")
print()


from threading import Thread

class Mythread(Thread):
    def run(self):
        print('Run Method')

t = Mythread()
t.start()



print()
print("*********************************************")
print()


from threading import Thread

class Mythread(Thread):
    def run(self):
        for i in range(5):
            print('Child Thread')

t = Mythread()
t.start()

for i in range(5):
    print('Main Thread')




print()
print("*********************************************")
print()


from threading import Thread

class Mythread(Thread):
    def run(self):
        for i in range(5):
            print('Child Thread')

t = Mythread()
t.start()
t.join()

for i in range(5):
    print('Main Thread')