# Class Method:

class Mobile:
    
    @classmethod
    def show_model(cls):
        print("RealMe X")

realme = Mobile()
Mobile.show_model()




print()
print("***************************************************")
print()


class Mobile:
    
    fp = 'Yes'

    @classmethod                                  # Class Method
    def show_model(cls, r):
        cls.ram = r
        print("Finger Print :", cls.fp)
        print("RAM :", cls.ram,"GB")

realme = Mobile()
Mobile.show_model(8)
