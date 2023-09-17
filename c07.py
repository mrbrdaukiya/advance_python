# Type Of Method

# 1) Instance Method
#   - accessor method
#   - mutator method

# 2) Class Method

# 3) Static Method




# 1) Instance Method

class Mobile:
    def __init__(self):
        self.model = 'RealMe X'           # Instance variable



    # 1) Instance Method
    def show_model(self, p):
        self.price = p
        print("Model :", self.model , "and Price :", self.price)

realme = Mobile()
redmi = Mobile()
realme.show_model(1000)
redmi.show_model(2000)