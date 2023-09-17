# 2) Strong Typing


class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")

class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")

class Cat:
    def talk(self):
        print("Meow Meow Meow Meow")


def myfunction(obj):
    if hasattr(obj, 'walk'):
        obj.walk()
    if hasattr(obj, 'talk'):
        obj.talk()

d = Duck()
myfunction(d)

print()

h = Horse()
myfunction(h)

print()

c = Cat()
myfunction(c)

print("************************************")