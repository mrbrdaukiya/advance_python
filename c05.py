# class Variable 
class Mobile:
    
    fp = 'Yes'
    
                                    # Instance Variable 
    def __init__(self):
        self.model = 'RealMe X'              # Instance Variable 
    
    def show_model(self):
        print("Mobile :", self.model)                   # Accessing Instance Variable 

    @classmethod                                  # Class Method
    def is_fp(cls):
        print("Finger Print :", cls.fp)                         # Accessing class Variable

realme = Mobile()
realme.show_model()
Mobile.is_fp()

print()

Mobile.fp = "No"

Mobile.is_fp()





print()
print("***************************************************")
print()

class Mobile:
    
    fp = 'Yes'

    @classmethod                                  # Class Method
    def is_fp(cls):
        print("Finger Print :", cls.fp)
    

realme = Mobile()
redmi = Mobile()
guru = Mobile()

print("RealMe :", Mobile.fp)
print("Redmi :", Mobile.fp)
print("Guru :", Mobile.fp)

print()

Mobile.fp = "No"                   # Modifing class Varibale

print("RealMe :", Mobile.fp)
print("Redmi :", Mobile.fp)
print("Guru :", Mobile.fp)