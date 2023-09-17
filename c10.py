# Static Method
class Mobile:
    @staticmethod
    def show_model():
        print("RealMe X")

realme = Mobile()
Mobile.show_model()




print()
print("***************************************************")
print()


class Mobile:
    
    fp = 'Yes'

    @staticmethod                                  
    def show_model():
        print("Finger Print :", Mobile.fp)

realme = Mobile()
Mobile.show_model()





print()
print("***************************************************")
print()


class Mobile:

    @staticmethod                                  
    def show_model(m, p):
        model = m
        price = p
        print("Model :", model, "Price :", price)

realme = Mobile()
Mobile.show_model("RealMe X", 1000)
