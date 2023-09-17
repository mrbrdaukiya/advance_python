# Accessor method
class Mobile:
    def __init__(self):
        self.model = 'RealMe X' 
    
    def get_model(self):
        return self.model
    
realme = Mobile()
m = realme.get_model()
print(m)




print()
print("***************************************************")
print()


# mutator method
class Mobile:
    def __init__(self):
        self.model = 'RealMe X' 
    
    def set_model(self):
        self.model = 'RealMe 2'
    
realme = Mobile()
# Before setting
print(realme.model)
# After Setting
realme.set_model()
print(realme.model)





print()
print("***************************************************")
print()


# mutator method
class Mobile:
    def set_model(self, m):
        self.model = m
   
realme = Mobile()
realme.set_model('RealMe X')
print(realme.model)


