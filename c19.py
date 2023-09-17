# 2) Multi-level Inheritance

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

class GrandSon(Son):
    def __init__(self):
        super().__init__()
        print("GrandSon Class constructor :")


    def showG(self):
        print("GrandSon Class  Method :")

g = GrandSon()
# g.showF()
# g.showS()
# g.showG()