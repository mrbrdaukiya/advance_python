# Nested Class
class Army:
    def __init__(self):
        self.name = 'Rahul'
        self.gn = self.Gun()                # creating Inner Class Object

    def show(self):
        print('Name :', self.name)
    
    class Gun:
        def __init__(self):
            self.name = 'AK 47'
            self.capacity = '75 Rounds'
            self.length = '34.3 Inch'

        def disp(self):
            print('Gun Name :', self.name)
            print('Capacity :', self.capacity)
            print('length :', self.length)

a = Army()
print(a.name)
a.show()

# print(a.gn.name)
# a.gn.disp()

print()
g = a.gn
g.disp()

g = Army().Gun()
print()

print(g.name)
print(g.capacity)
print(g.length)