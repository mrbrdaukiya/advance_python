# constructor in inheritance

class Father:
    def __init__(self, m):
        # self.money = 1000
        self.money = m
        print("Father Class constructor")

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def disp(self):
        print("Son Class Instance Method :", self.money + 1000)

s = Son(1000)
print(s.money)
s.disp()
s.show()