class Student:
    def __init__(self, name, roll, addrs):
        self.name = name
        self.roll = roll
        self.addrs = addrs

    def disp(self):
        print(f'Name:{self.name} Roll:{self.roll} Address:{self.addrs}')
