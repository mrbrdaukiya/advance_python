# Inheritance

# 1) single Inheritance

class Father:
    money = 1000

    def show(self):
        print("Parent class Instance Method")
        
    @classmethod
    def showmoney(cls):
        print("Parent class Class Method :", cls.money)

    @staticmethod
    def start():
        a = 10
        print("Parent class static Method :", a)

class Son(Father):
    def disp(self):
        print("Child class Instance Method")

s = Son()
s.disp()
s.show()
s.showmoney()
s.start()


print()

f = Father()
f.show()
f.showmoney()
f.start()