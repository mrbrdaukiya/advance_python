# Constructor

class Mobile:
    def __init__(self):
        self.model = 'RealMe X'

    def show_Model(self):
        print('Model :', self.model)
    
realme = Mobile()
realme.show_Model()

print()
print("***************************************************")
print()


# Constructor

class Mobile:
    # Constructor
    def __init__(self, m, v= 80):
        self.model = m
        self.volumn = v

    def show_model(self, p):
        price = p                # Local Varaible
        print("Model :", self.model , "and Price :", price)
        print("Volumn :", self.volumn)

# Passing Argyment To Constructor

realme = Mobile("RealMe X")

# Accessing Method from outside class
realme.show_model(1000)

print()

redmi = Mobile("Redmi 7s", 50)
redmi.show_model(5000)