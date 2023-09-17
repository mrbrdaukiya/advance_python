class Myclass(object):
    def show(self):
        print("I am a Method")

# x = Myclass()
# x.show()

class Mobile:
    def __init__(self, m):
        # self.model = "RealMe X"
        self.model = m



    def show_model(self, p):
        # price = 1000
        self.price = p
        print("Mobile :", self.model,"::", "Price :", self.price)

# realme = Mobile()
realme = Mobile("RealMe X")

realme.show_model(1000)
# print(realme.model)

print(id(realme))


# realme.model = "RealMe Pro 2"

# print(realme.model)
# realme.show_model()




print()

redmi = Mobile("Redmi 7s")
redmi.show_model(7000)
print(id(redmi))



print()

guru = Mobile("Python")
guru.show_model(10)
print(id(guru))