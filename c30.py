from abc import ABC , abstractmethod

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
c.show()


print("***************************************************")

from abc import ABC , abstractmethod

class DefenceForce(ABC):
    def __init__(self):
        self.id = 101

    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun = AK47", self.id)

class Army(DefenceForce):
    def area(self):
        print("area = Land")


class AirForce(DefenceForce):
    def area(self):
        print("area = Sky")


class Navy(DefenceForce):
    def area(self):
        print("area = Sea")

a = Army()
af = AirForce()
n = Navy()

a.gun()
a.area()

print()

af.gun()
af.area()

print()

n.gun()
n.area()