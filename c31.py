# Interface
from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print("Concrete Method")

class Child(Father):
    def disp(self):
        print("Child Class")
        print("Defining Abstract Method")

c = Child()
c.disp()

print("*********************************************")


from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass

    @abstractmethod
    def disp2(self):
        pass

class Child(Father):
    def disp1(self):
        print("Child Class")
        print("Disp1 Abstract Method")
        print()

class GrandChild(Child):
    def disp2(self):
        print("GrandChild Class")
        print("Disp2 Abstract Method")
        print()

gc = GrandChild()
gc.disp1()
gc.disp2()