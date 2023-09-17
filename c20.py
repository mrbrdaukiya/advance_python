# Hierarchical Inheritance


class Father:
    def __init__(self):
        print("Father Class constructor :")


    def showF(self):
        print("Father Class  Method :")




class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Class constructor :")


    def showS(self):
        print("Son Class  Method :")




class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter Class constructor :")


    def showD(self):
        print("Daughter Class  Method :")
s = Son()

print()

d = Daughter()