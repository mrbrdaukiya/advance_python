# constructor Overriding
class Father:
    def __init__(self):
        self.money = 1000
        print("Father Class constructor")

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self, r):
        # self.money = 5000
        self.money = r
        self.car = "BMW"
        print("Son class constructor")
    def disp(self):
        print("Son Class Instance Method :")
f = Father()
s = Son(2000)
print(s.money)
s.disp()