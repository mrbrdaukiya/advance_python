# Namespace


class Mobile:
    
    fp = 'Yes'

    @classmethod                                  # Class Method
    def is_fp(cls):
        print("Finger Print :", cls.fp)
    

realme = Mobile()
redmi = Mobile()
guru = Mobile()

print("Class FP :", Mobile.fp)
print("RealMe :", realme.fp)
print("Redmi :", redmi.fp)
print("Guru :", guru.fp)

print()

Mobile.fp = "No"                   # Modifing class Varibale

print("Class FP :", Mobile.fp)
print("RealMe :", realme.fp)
print("Redmi :", redmi.fp)
print("Guru :", guru.fp)

print()

realme.fp = "Not Working"
print("Class FP :", Mobile.fp)
print("RealMe :", realme.fp)
print("Redmi :", redmi.fp)
print("Guru :", guru.fp)
