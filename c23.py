# Polymorphism (4 type)
# 1) Duck Typing

class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")

class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")

def myfunction(obj):
    obj.walk()

d = Duck()
myfunction(d)

print()

h = Horse()
myfunction(h)