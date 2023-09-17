# Passing Mamber of one class to Another class

class Student:
    # Constructor
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    # Instance Method
    def disp(self):
        print("Student Name :", self.name)
        print("Student Roll :", self.roll)


class User:
    # static method
    @staticmethod
    def show(s):
        print("User Name :", s.name)
        print("User Roll :", s.roll)
        s.disp()

stu = Student('Rahul', 101)

User.show(stu)
