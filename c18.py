# constructor with super() Method

class Father:
    def __init__(self, m):
        # self.money = 1000
        self.money = m
        print("Father Class constructor :")

    def show(self):
        print("Father Class Instance Method :")


class Son(Father):
    def __init__(self, m, j):
        # super().__init__()         # calling Son class constructor
        super().__init__(m)
        self.job = j
        print("Son class constructor :")

    def disp(self):
        print("Son Class Instance Method :", self.money, "Job :", self.job)

s = Son(1000, "Python")
s.disp()