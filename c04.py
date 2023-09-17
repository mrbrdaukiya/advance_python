# Instance Variable 

class Mobile:
    def __init__(self):
        self.model = 'RealMe X'              # Instance Variable 
    
    def show_model(self):
        print(self.model)                   # Accessing Instance Variable 

realme = Mobile()
redmi = Mobile()
guru = Mobile()

print(realme.model)
print(redmi.model)
print(guru.model)

print()



redmi.model = "Redmi 7s"



print(realme.model)
print(redmi.model)
print(guru.model)

print()