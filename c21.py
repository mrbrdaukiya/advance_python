# Multiple Inheritance


class Father:
    def __init__(self):
        super().__init__()
        print("Father Class constructor :")


    def showF(self):
        print("Father Class  Method :")




class Mother:
    def __init__(self):
        super().__init__()
        print("Mother Class constructor :")


    def showM(self):
        print("Mother Class  Method :")




class Son(Mother, Father):           #MRO Method (left 2 right)
    def __init__(self):
        super().__init__()
        print("Son Class constructor :")


    def showS(self):
        print("Son Class  Method :")

s = Son()

print()

# s.showF()
# s.showM()
# s.showS()