# Operator OverLoading

print(10+20)

print(int.__add__(20,20))
print(str.__add__('Guru ','Choudhary'))


print("***************************************************")

class A:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return self.x + other.x

class B:
    def __init__(self, x):
        self.x = x


a = A(100)
b = B(500)
print(a+b)